# Domamutzer Twitch Final Holdout Protocol

Version: 2.3-twitch-final
Algorithm: domamutzer-adaptive-pairwise-v1
Seed: 20260911
Primary metric: paired NDCG@10 delta vs matched conventional baseline.
Training objective: query-matched pairwise logistic ranking; each training comparison keeps the same viewer and contrasts the held positive candidate with hard candidate negatives.
Adaptive feature policy: rarity/reciprocal/shared-evidence are greedily selected using internal development queries only; both disjoint dev halves must improve and average gain must be >= 0.00075.
Fresh test queries are not used for feature selection or hyperparameter choice.
All six SNAP Twitch language networks are reported; no network may be omitted after execution.
Final gate: GREEN = positive macro delta + pooled 95% CI > 0 + >=4/6 positive networks; AMBER = positive macro delta + >=3/6 positive networks; otherwise RED.