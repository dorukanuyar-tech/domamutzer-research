# Technical Brief — Domamutzer v3.0.1

Domamutzer is a second-stage people-discovery reranker. It does not replace candidate retrieval.

The private engine uses a conventional query-matched pairwise baseline plus a bounded residual trained on hard baseline comparisons. Grouped-query cross-validation chooses the residual blend; if auxiliary signal is unstable, the exported model can use `alpha=0` and preserve the baseline path.

The reciprocal serving mode is separate from the undirected proxy path. With directional platform labels it scores both A->B and B->A and combines the two conservatively.

Public benchmark history is intentionally mixed/negative. The requested partner evaluation is therefore a controlled replay or shadow test on the platform's own fixed candidate pool with predeclared mutual-quality and safety metrics.
