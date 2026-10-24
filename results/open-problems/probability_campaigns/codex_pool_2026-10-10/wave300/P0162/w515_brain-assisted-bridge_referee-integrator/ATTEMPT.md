# P0162 bridge attempt

Target: Fourier entropy versus total influence for Boolean functions under the uniform product measure. The exact source statement and current status are being checked separately in SOURCE_STATUS.json.

## First load-bearing check

Han's published theorem bounds Fourier entropy by a universal multiple of total influence plus the sum of coordinate influences times log of their reciprocal. A tempting bridge is to upper-bound that extra sum by a universal multiple of total influence. It fails on the n-bit conjunction: coordinate influence is 2^(1-n), so the extra sum divided by total influence is n-1. See CLAIMS.jsonl row P0162-w515-001.

This is a refuted route, not a solution of FEI. Next: compare brain retrieval and the peer artifacts with the theorem's actual hypotheses; identify a narrower valid bridge or an obstruction.

## Theorem hypothesis comparison

Li and Han, arXiv:2512.03117v1, prove in natural logs that H <= I + sum_i I_i ln(1/I_i) for every **real-valued** unit-L2 function on the uniform cube. Thus this upper bound alone uses no Boolean spectral realizability; it cannot bridge the gap identified in the September P0162 attempt, which shows an arbitrary subset law can have entropy log n and mean cardinality 1. Han's earlier published theorem assumes Boolean output but retains the same extra term. Our conjunction calculation demonstrates that simply absorbing this term into I is impossible even inside the Boolean class.

The math-brain query `P0162 Fourier entropy influence Boolean constraint Han correction bridge` returned the P0162 open-problem and old-attempt cards among eight direct hits but no Han or Li-Han theorem card among those eight (MATH_RECALL_RECEIPT.json, command `python -X utf8 math_recall_gate.py`, 14.1097 s). The bounded repair is bundle_001.json: a precisely scoped Li-Han theorem node and a refuted-bridge concept with a conjunction witness, related to the existing P0162 card. The draft is submitted, with review, ingestion, and retrieval recheck pending. No recall improvement is claimed yet.

## Referee synthesis

Both peers' restriction identities and logarithmic coordinate bounds checked. w514's exact selector construction proves a bad split can cost at least n times its influence, yet the function itself has H<=2I. w513's disjoint balanced majority composition keeps every individual influence arbitrarily small while preserving one bad selected coordinate, even in a family with H<=4I. These findings rule out an arbitrary-coordinate local induction. They do not rule out choosing a good coordinate at each node.

The single hardest open piece is now explicit: for arbitrary Boolean f, obtain a dimension-free bound for the weighted sum of conditional selector entropies B_v over a complete restriction tree, or prove that a suitable coordinate can always be selected recursively. w513's tree telescoping establishes that such an aggregate bound is equivalent to FEI up to a constant; it does not prove the bound. All source statuses remain scoped to the checked primary papers and local records.
