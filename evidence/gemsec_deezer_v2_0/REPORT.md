# Domamutzer Public Evidence Benchmark

**Gate: AMBER**

This is a public-data historical proxy, not production-lift proof.

## Primary comparison

Both systems are learned on the same leakage-safe training pairs. The baseline uses conventional graph features plus taste cosine. Domamutzer adds rarity-aware overlap, directional reciprocal coverage, and shared-evidence strength.

| Dataset | Baseline NDCG@10 | Domamutzer NDCG@10 | Paired delta | 95% bootstrap CI | Baseline Hit@10 | Domamutzer Hit@10 | Baseline AUC | Domamutzer AUC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Romania | 0.0941 | 0.0942 | +0.0001 | [-0.0065, +0.0060] | 0.2033 | 0.2083 | 0.8643 | 0.8644 |
| Croatia | 0.0632 | 0.0646 | +0.0014 | [-0.0041, +0.0071] | 0.1333 | 0.1350 | 0.6689 | 0.6683 |
| Hungary | 0.1017 | 0.1082 | +0.0065 | [+0.0010, +0.0122] | 0.2017 | 0.2117 | 0.7605 | 0.7601 |

## Gate meaning

- GREEN: positive paired NDCG@10 lift on all three countries and the 95% bootstrap CI is above zero in every country.
- AMBER: positive mean lift on all three countries, but at least one confidence interval crosses zero.
- RED: at least one country has non-positive mean lift.

## What this benchmark can support

If GREEN/AMBER, it can support a narrow statement such as: 'Domamutzer-specific reciprocal/rarity features added offline ranking signal on external public social-network datasets under a predeclared proxy protocol.'

It cannot support claims that Domamutzer improves Instagram/TikTok/Snap production outcomes. Buyer-controlled historical replay, shadow ranking, or an online experiment is still required for that.