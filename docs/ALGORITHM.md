# Domamutzer v4 — Public Algorithm Specification

## Objective

Domamutzer is a second-stage reranker. It assumes an upstream platform already provides an eligible candidate set and an incumbent score `s0` for every pair.

The product objective is not “predict whether an undirected social edge exists.” The desired labels are directional outcomes such as A accepting B, B accepting A, reply/continuation, and negative safety outcomes.

## Directional preference

Train or supply a directional model:

`pAB = P(A values B | context)`

and evaluate the reversed pair:

`pBA = P(B values A | reversed context)`.

Do not collapse directional features before prediction.

## Mutual target

Supported public reference fusion rules:

- harmonic: `2ab/(a+b)`,
- product: `ab`,
- geometric: `sqrt(ab)`,
- minimum: `min(a,b)`.

Harmonic fusion is the public default because one very weak direction should substantially reduce a match score.

## Support gate

The public reference gate combines minimum profile confidence, shared-evidence support, and directional coverage balance. It is an intervention-control policy, not a learned probability.

Weak support means stay near the incumbent.

## Trust region

With `L=logit`:

`delta = clip(L(mutual)-L(incumbent), -max_shift, +max_shift)`

`final = sigmoid(L(incumbent) + gate * delta)`.

This gives an exact fallback when `gate=0` and prevents unbounded changes even when the directional model is overconfident.

## List-level constraint

The reference `windowed_rerank` sorts by the incumbent, divides the list into contiguous windows, and only reranks inside a window. It is intentionally simple and inspectable.

## Logged-data evaluation

A buyer should not compare accept/reply rates naively if the incumbent logging policy determined exposure. Prefer randomized traffic where possible; otherwise report policy-aware estimates such as IPS/SNIPS and, when outcome models are available, doubly robust estimates. Always report support and variance diagnostics alongside a point estimate.
