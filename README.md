# Domamutzer

**Reciprocal people-discovery reranking research.**

Domamutzer studies a narrow problem for social platforms: given an already eligible candidate set, can a second-stage ranker improve **mutual connection quality** while safely falling back to the incumbent-style baseline when extra signals are unstable?

## Current status

Domamutzer is **evaluation-stage research technology**. It is not claimed to be production-proven or broadly superior to existing social-platform recommenders. Negative and mixed external results are retained intentionally.

| Evaluation | Status | Result |
|---|---|---|
| GEMSEC Deezer v2.0 | AMBER | small positive mean NDCG@10 deltas; only Hungary statistically clear |
| GitHub developers v2.1 | RED | fixed added-feature model did not improve the fresh holdout |
| Twitch 6-network v2.3 | RED | macro paired NDCG@10 delta -0.000828; pooled 95% CI [-0.002871,+0.001170]; 2/6 positive networks |
| Private engine v3.0.1 | FINAL evaluation build | baseline-first safe residual + directional reciprocal serving; no broad public-superiority claim |

The negative holdouts are why the private engine architecture changed rather than hiding unfavorable evidence.

## Final architecture

The private v3.0.1 engine is baseline-first:

1. learn a conventional query-matched pairwise baseline,
2. train a bounded residual only on hard/low-margin baseline comparisons,
3. select residual blend strength with grouped-query cross-validation,
4. allow `alpha = 0` as an explicit no-augmentation fallback,
5. keep directional signals separate for real reciprocal outcomes.

For partner data with directional labels, the engine can estimate:

- `p(A -> B)` — A accepts/values B,
- `p(B -> A)` — B accepts/values A,
- mutual score — conservative two-sided fusion.

That directional problem is **not identifiable from undirected friendship-link datasets** such as the public proxies above.

## Why the public results do not end the project

GEMSEC, GitHub and Twitch provide historical links and attributes. They do not provide recommendation impressions followed by invite, reciprocal acceptance, reply, D7 continuation, hide, block or report. They are useful for regression/generalization checks, but they are not the product's decision-grade test.

The next meaningful evaluation is therefore a **buyer-controlled historical replay or shadow test** on a fixed candidate pool with directional outcomes.

## Evidence history

- [`evidence/gemsec_deezer_v2_0/`](evidence/gemsec_deezer_v2_0/)
- [`evidence/github_v2_1/`](evidence/github_v2_1/)
- [`evidence/twitch_v2_3/`](evidence/twitch_v2_3/)

## Requested partner evaluation

Use the platform's existing candidate generator and pseudonymous historical outcomes. Compare the incumbent ranker against Domamutzer under the same candidate pool and predeclare metrics. Useful outcomes include mutual connect/accept, reply or conversation continuation and D7 connection quality, with hide/block/report as safety guardrails.

## Repository boundary

This public repository contains methodology and external evidence only. It does **not** contain the private engine source, production credentials, user data or a production model.

## Contact

For technical evaluation, use the contact information on the GitHub profile associated with this repository.
