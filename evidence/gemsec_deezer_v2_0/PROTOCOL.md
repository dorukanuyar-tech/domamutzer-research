# Domamutzer Benchmark Protocol

Version: 2.0
Seed: 20260910
Primary metric: paired NDCG@10 delta vs learned conventional baseline.
Candidate pool: 100 candidates/query, targeting 70 hard two-hop negatives before random fill.
Leakage control: all model-training positive edges and test positive edges are absent from the graph used for graph features.
Comparison fairness: both baseline and Domamutzer are logistic models trained on the same positive/negative pair set; Domamutzer differs only by the added rarity/reciprocal/evidence features.
Confidence interval: paired bootstrap over per-query NDCG@10 differences, 1000 deterministic resamples.
Known limitation: GEMSEC has no temporal recommendation exposure/outcome labels, so this remains a historical link-prediction proxy.