"""Public reference implementation of the Domamutzer v4 policy layer.

Private ingestion, security, tenant, feature-derivation and production-serving
code are intentionally excluded from the public research repository.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Sequence


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    x=float(x)
    if not math.isfinite(x):
        raise ValueError('score must be finite')
    return max(lo,min(hi,x))


def logit(p: float, eps: float=1e-6) -> float:
    p=min(1-eps,max(eps,float(p)))
    return math.log(p/(1-p))


def sigmoid(x: float) -> float:
    if x>=0:
        z=math.exp(-x)
        return 1/(1+z)
    z=math.exp(x)
    return z/(1+z)


def reciprocal_fusion(p_ab: float,p_ba: float,method: str='harmonic') -> float:
    a=clamp(p_ab); b=clamp(p_ba)
    if method=='product': return a*b
    if method=='geometric': return math.sqrt(a*b)
    if method=='minimum': return min(a,b)
    if method=='harmonic': return 2*a*b/(a+b) if a+b else 0.0
    raise ValueError('unsupported fusion method')


@dataclass(frozen=True)
class PolicyConfig:
    fusion: str='harmonic'
    max_logit_shift: float=.80
    confidence_weight: float=.50
    evidence_weight: float=.30
    balance_weight: float=.20


def support_gate(forward: Mapping[str,float],reverse: Mapping[str,float],cfg: PolicyConfig=PolicyConfig()) -> float:
    confidence=min(clamp(forward.get('profile_confidence',0)),clamp(reverse.get('profile_confidence',0)))
    evidence=max(clamp(forward.get('shared_evidence',0)),clamp(reverse.get('shared_evidence',0)))
    balance=min(clamp(forward.get('coverage_balance',0)),clamp(reverse.get('coverage_balance',0)))
    den=cfg.confidence_weight+cfg.evidence_weight+cfg.balance_weight
    return clamp((cfg.confidence_weight*confidence+cfg.evidence_weight*evidence+cfg.balance_weight*balance)/den)


def trust_region_blend(incumbent: float,target: float,gate: float,max_logit_shift: float=.80) -> tuple[float,float]:
    delta=max(-max_logit_shift,min(max_logit_shift,logit(target)-logit(incumbent)))
    applied=clamp(gate)*delta
    return clamp(sigmoid(logit(incumbent)+applied)),applied


def reciprocal_policy_score(*,incumbent_score: float,p_ab: float,p_ba: float,
                            forward_support: Mapping[str,float],reverse_support: Mapping[str,float],
                            cfg: PolicyConfig=PolicyConfig()) -> dict:
    mutual=reciprocal_fusion(p_ab,p_ba,cfg.fusion)
    gate=support_gate(forward_support,reverse_support,cfg)
    final,delta=trust_region_blend(incumbent_score,mutual,gate,cfg.max_logit_shift)
    return {
        'score':final,'incumbent_score':clamp(incumbent_score),'p_ab':clamp(p_ab),'p_ba':clamp(p_ba),
        'mutual_target':mutual,'support_gate':gate,'applied_logit_delta':delta,
    }


def windowed_rerank(rows: Sequence[Mapping[str,object]],window_size: int=10) -> list[dict]:
    if window_size<1: raise ValueError('window_size must be >=1')
    rows=[dict(r) for r in rows]
    if any(r.get('incumbent_score') is None for r in rows): raise ValueError('incumbent_score required')
    rows.sort(key=lambda r:(-float(r['incumbent_score']),str(r.get('id',''))))
    out=[]
    for start in range(0,len(rows),window_size):
        w=rows[start:start+window_size]
        w.sort(key=lambda r:(-float(r['score']),str(r.get('id',''))))
        out.extend(w)
    return out
