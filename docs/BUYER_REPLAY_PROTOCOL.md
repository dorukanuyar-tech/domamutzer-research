# Buyer Replay Protocol

## Goal

Test whether Domamutzer adds value **on top of the buyer's current candidate/ranking stack**, rather than asking the buyer to replace it.

## Minimum pseudonymous schema

Per impression/candidate row:

- viewer ID
- candidate ID
- timestamp
- incumbent score or rank
- logging propensity if known
- allowed pair/context features or buyer-side embeddings
- directional outcomes: open/request/accept/reply/continuation
- safety outcomes: hide/block/report

Raw DMs are not required.

## Split

Prefer time-based or strict user/query group separation. Never tune policy parameters on the final replay period.

## Arms

1. incumbent ranking
2. Domamutzer v4 safe reciprocal rerank over the same candidate set

## Primary metric

Choose one before evaluation, e.g. reciprocal accept or D7 reciprocal connection rate. Secondary ranking metrics and safety guardrails should be predeclared.

## Bias control

If historical exposure was policy-driven, naive observed-outcome averages are biased. Prefer randomized shadow traffic; otherwise report IPS/SNIPS and doubly robust estimates when the required propensity/outcome-model inputs are defensible.

## Launch rule

Do not move to an online A/B test solely because one offline point estimate is positive. Require a predeclared confidence/guardrail rule and review segment-level failures.
