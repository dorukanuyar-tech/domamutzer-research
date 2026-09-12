# Domamutzer Adaptive Pairwise Fresh Holdout — Twitch Social Networks

**Gate: RED**

Macro paired NDCG@10 delta: -0.000828; pooled 95% bootstrap CI [-0.002871, +0.001170]; positive networks: 2/6.

| Network | Selected Domamutzer features | Baseline NDCG@10 | Domamutzer NDCG@10 | Delta | 95% CI | Hit@10 base | Hit@10 Dom |
|---|---|---:|---:|---:|---:|---:|---:|
| DE | reciprocal_coverage | 0.1405 | 0.1388 | -0.0017 | [-0.0070, +0.0036] | 0.2600 | 0.2600 |
| ENGB | shared_evidence | 0.1061 | 0.1018 | -0.0043 | [-0.0095, +0.0009] | 0.2100 | 0.2033 |
| ES | none | 0.1338 | 0.1338 | +0.0000 | [+0.0000, +0.0000] | 0.2467 | 0.2467 |
| FR | shared_evidence | 0.1443 | 0.1401 | -0.0042 | [-0.0111, +0.0027] | 0.2517 | 0.2433 |
| PTBR | rarity_overlap | 0.1542 | 0.1564 | +0.0022 | [-0.0005, +0.0053] | 0.2867 | 0.2917 |
| RU | rarity_overlap | 0.1575 | 0.1606 | +0.0030 | [-0.0038, +0.0092] | 0.2817 | 0.2817 |

Gate was fixed before seeing Twitch results: GREEN requires positive macro delta, pooled CI above zero, and positive mean delta on at least 4/6 networks; AMBER requires positive macro delta and at least 3/6 positive networks; otherwise RED.

This benchmark is still an offline historical proxy. Buyer-controlled replay/shadow/A-B testing is required for production claims.