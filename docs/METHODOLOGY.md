# Methodology

Public tests use leakage-controlled historical link ranking with hard candidate negatives and paired NDCG@10 comparisons. They are proxy evaluations only.

v2 evidence showed that simple always-on reciprocal/rarity additions are distribution-sensitive. The final private engine therefore uses a baseline-first safe-residual policy: extra signal is bounded and may be disabled entirely when grouped-query validation is unstable.

Public undirected link datasets cannot validate the product's central two-sided objective because they do not identify `A -> B` and `B -> A` acceptance probabilities or downstream conversation/retention outcomes.

No further tuning to the disclosed GEMSEC/GitHub/Twitch test results is used as sales evidence. The next decision-grade evaluation is a buyer-controlled replay/shadow/A-B test on a fixed candidate pool with predeclared directional metrics and safety guardrails.
