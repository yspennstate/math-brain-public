# HARD8-01 checkpoint 7 — verification addendum

**Date:** 2026-09-16 UTC  
**Status:** unrestricted Černý conjecture remains **OPEN**.

This append-only note records the actual GitHub creation receipts, exact-SHA readbacks, and deterministic finite checks for checkpoint 7.

## 1. Mathematical report

Path:

`hard8_2026-09-16/HARD8-01/runs/2026-09-16/2026-09-16T12-21-14Z__report.md`

Creation commit:

`040899a3d6106a04f523badedc6b2e08ead98700`

Exact-commit readback at that SHA succeeded. Returned content blob SHA:

`37f527bb25d10aabb177e2bb4bb6cf4b7394707d`

Therefore the mathematical report is **VERIFIED as delivered**.

## 2. Exact verifier artifact

Path:

`hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T12-21-14Z__prefix_credit_census_verifier.py`

Creation commit:

`18ec8fc6bfb1c363f6e2899fd04e114bdec4cf0f`

Exact-commit readback succeeded. Returned blob SHA:

`567194575208297ad5435cc4873c90342b41ea3a`

Therefore the verifier is **VERIFIED as delivered**.

The verifier is standard-library Python. It uses exact finite permutations, integer path lengths, positive-generator breadth-first search, memoized Bellman recursion, and finite dynamic programming. It uses no floating point, randomness, SAT/SMT solver, heuristic acceptance, or timeout-as-proof.

## 3. Exact output artifact

Path:

`hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T12-21-14Z__prefix_credit_census_output.txt`

Creation commit:

`691bcfd098e7cda076f905fc4714a28f61f2b488`

Exact-commit readback succeeded. Returned blob SHA:

`5534cbe8c48599abafe8fc7c9458745e915f9c50`

The executed output was:

```text
ALPHABETS_CHECKED 7260
SYNCHRONIZING 5760
PREFIX_FAILURES 0
PREFIX_OPTIMUM_PENALTIES 0
BELLMAN_TRAVEL_DISTRIBUTION [(3, 1770), (4, 954), (5, 1272), (6, 990), (7, 492), (8, 204), (9, 60), (10, 6), (12, 12)]
GROUP_ORDER_DISTRIBUTION [(4, 24), (5, 84), (8, 36), (10, 180), (12, 48), (20, 720), (24, 108), (60, 1140), (120, 3420)]
VIABLE_TWO_HOLE_DISTRIBUTION [(1, 264), (3, 5496)]
MAX_POSITIVE_CAYLEY_DIAMETER 14
MIN_START_CREDIT_MARGIN 0
EQUALITY_SIGNATURE [((10, 3, 120, 10), 6), ((12, 1, 5, 4), 12)]
C5_FIRST_TRANSITIONS [(2, (0, 2), None), (3, (0, 3), None), (4, (0, 4), 8)]
ALL_CHECKS_PASSED
```

## 4. Scope

The new mathematical results are restricted SI-automaton reductions and exact finite evidence for a prefix-credit architecture. They do **not** prove the unrestricted Černý conjecture and do not constitute independent external review of the hand proofs.

The next attack is a viability-aware Bellman potential on subset-Schreier states that can convert successor branching/expansion into quantitative credit for later inter-singular gaps.
