import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
from domamutzer_reference import PolicyConfig,reciprocal_policy_score,windowed_rerank

support={'profile_confidence':.92,'shared_evidence':.80,'coverage_balance':.88}
rows=[]
for cid,base,pab,pba in [('candidate-A',.70,.88,.82),('candidate-B',.68,.91,.31),('candidate-C',.66,.74,.77)]:
    out=reciprocal_policy_score(incumbent_score=base,p_ab=pab,p_ba=pba,forward_support=support,reverse_support=support,cfg=PolicyConfig(max_logit_shift=.7))
    rows.append({'id':cid,'incumbent_score':base,**out})
for r in windowed_rerank(rows,window_size=3):
    print(r['id'],f"base={r['incumbent_score']:.3f}",f"mutual={r['mutual_target']:.3f}",f"final={r['score']:.3f}")
