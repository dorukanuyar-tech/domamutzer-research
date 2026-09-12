# Domamutzer Fresh Holdout Validation — GitHub Social Network

**Gate: RED**

This is a fresh external public-data holdout proxy, not production-lift proof.

## Primary comparison

Both systems are learned on the same leakage-safe training pairs. The baseline uses conventional graph features plus feature cosine. Domamutzer adds rarity-aware overlap, directional reciprocal coverage, and shared-evidence strength. The feature family was frozen before opening this holdout result.

| Dataset | Baseline NDCG@10 | Domamutzer NDCG@10 | Paired delta | 95% bootstrap CI | Baseline Hit@10 | Domamutzer Hit@10 | Baseline AUC | Domamutzer AUC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| GitHub developers | 0.1216 | 0.1181 | -0.0035 | [-0.0144, +0.0068] | 0.2188 | 0.2250 | 0.7878 | 0.7841 |

## Gate meaning

- GREEN: positive paired NDCG@10 lift and the 95% bootstrap CI is above zero on the fresh holdout.
- AMBER: positive mean lift, but the 95% bootstrap confidence interval crosses zero.
- RED: non-positive mean lift on the fresh holdout.

## What this benchmark can support

If GREEN/AMBER, it can support a narrow statement such as: 'The frozen Domamutzer reciprocal/rarity feature family added offline ranking signal on a fresh external attributed social-network holdout under a predeclared proxy protocol.'

It cannot support claims that Domamutzer improves Instagram/TikTok/Snap production outcomes. Buyer-controlled historical replay, shadow ranking, or an online experiment is still required for that.