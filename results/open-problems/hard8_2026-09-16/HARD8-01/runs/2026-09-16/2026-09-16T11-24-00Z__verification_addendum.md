# HARD8-01 checkpoint 6 — verification addendum

**Date:** 2026-09-16 UTC  
**Status:** unrestricted Černý conjecture remains **OPEN**.

This append-only note records the actual GitHub creation receipts/readbacks and the deterministic exact checks for checkpoint 6.

## 1. Mathematical report receipt

Path:

`hard8_2026-09-16/HARD8-01/runs/2026-09-16/2026-09-16T11-05-00Z__report.md`

Creation commit:

`28c33034f329cece792e61d0822105b23648aa9a`

Exact-commit readback at that SHA succeeded. Returned content blob SHA:

`3ce4f8146fcafa2fa4cffee23e8a504237309d9f`

Therefore the mathematical report is **VERIFIED as delivered**.

## 2. Exact verifier artifact receipt

Path:

`hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T11-05-00Z__hole_bellman_amortization_verifier.py`

Creation commit:

`267650e61b36696ee432b9dce6e20d8230e416ad`

Exact-commit readback at that SHA succeeded. Returned content blob SHA:

`0aa6a312cccf3facbc07259aba3dd4cf19bd38f7`

Therefore the code artifact is **VERIFIED as delivered**.

The verifier is standard-library Python and uses only finite permutations, integer lengths, exact subset BFS, finite group BFS, memoized finite Bellman recursion, and exhaustive finite transition enumeration. It uses no floating point, randomness, SAT/SMT solver, heuristic acceptance, or timeout-as-proof.

## 3. Deterministic execution checks

The exact mathematical logic implemented in the archived verifier was executed in the run environment. The run completed with `ALL_CHECKS_PASSED` and returned:

```text
S5_RESET_THRESHOLD 14
S5_BELLMAN_START 10
S5_FINAL_STAGE_DISTANCES [5, 5, 6]
S5_PROFILE_0_TO_7 [(0, 0, 1, 1), (1, 0, 1, 1), (2, 1, 1, 1), (3, 1, 1, 1), (4, 1, 1, 1), (5, 2, 2, 3), (6, 3, 4, 4), (7, 4, 4, 4)]
S5_MIXED_HITTING_LEVELS [5, 5, 6]
S5_ONE_COORDINATE_LOCAL_TOTAL 19
C5_RESET_THRESHOLD 16
C5_BELLMAN_START 12
C5_POSITIVE_GENERATOR_DIAMETER 4
ALL_CHECKS_PASSED
```

The execution verifies the following finite claims used in the report.

### Five-state `S_5` automaton

With permutation generators

```text
p=(0,1,2,4,3)
q=(1,2,3,0,4)
```

and simple idempotent `e: 0 -> 2`:

- the generated permutation group has order `120`;
- exact subset BFS gives reset threshold `14`;
- the exact hole-Bellman start value is `10`, so `4 + 10 = 14`;
- the complete finite Bellman table on reachable canonical hole states agrees with the report;
- from the three possible size-three canonical hole states, the exact minimum final permutation costs are `5,5,6`;
- explicit shortest generator-index words are checked for all three final transitions;
- the bounded chain/sibling endpoint profile through saturation agrees with the report and gives mixed hitting levels `5,5,6`;
- exhaustive dynamic programming over **all** canonical schedules in which every consecutive defect-arc transition is either chain-compatible or sibling-compatible gives minimum total reset length `19`, with an optimal local path having gap costs `5,5,5` and modes `sibling, chain, sibling`.

Thus the finite obstruction to a universal per-gap `n-1` strategy, and the stronger obstruction to using only chain/sibling one-coordinate moves, are exact finite statements for this automaton.

### Classical five-state Černý automaton

With the 5-cycle permutation generator and simple idempotent `0 -> 1`:

- exact subset BFS gives reset threshold `16=(5-1)^2`;
- the exact hole-Bellman permutation budget is `12`;
- the positive-generator diameter of the cyclic permutation group is `4`.

Consequently any canonical threshold-16 reset word, after shortening each permutation block to its induced group element, has three inter-singular block lengths summing to `12` with every block at most `4`; all three are therefore exactly `4`. Combined with the `S_5` final-gap lower bound `5`, this proves the report's no-universal-rank-only-stage-cap theorem at `n=5`.

## 4. Scope and review requirement

These finite checks support the new restricted SI theorems and negative proof-architecture results. They are **not** a proof of the unrestricted Černý conjecture, and they are not an independent external mathematical review of the hand proofs in the report.

The next mathematical target remains a state-dependent Bellman supersolution / branch-aware amortization inequality that controls total permutation travel while allowing individual gaps above `n-1`.
