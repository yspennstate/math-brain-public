# HARD8-01 checkpoint 4 verification addendum

This append-only note records the publication and exact-verifier receipts for the checkpoint-4 research iteration.

## Mathematical report

Path:
`hard8_2026-09-16/HARD8-01/runs/2026-09-16/2026-09-16T09-03-23Z__report.md`

Creation commit:
`8f5d9a0675dce63c27a9cfc916ffea79d160c64e`

Read back at that exact commit: **YES**.

Returned content blob SHA:
`80a3397c6c1ae6ab46f38cdd3e070e6246265f30`

Status: **VERIFIED**.

## Exact verifier source

Path:
`hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T09-03-23Z__si_arborescence_exact_verifier.py`

Creation commit:
`9efc5b126eeaf7138ad91cbedfe028fa69ae9171`

Read back at that exact commit: **YES**.

Returned content blob SHA:
`e5007f7a5fcadc523cda087a542e1fa716b93e39`

Status: **VERIFIED**.

## Actual deterministic execution

The archived verifier was also executed from the matching local source during this iteration. It completed without timeout or external solver and printed:

```text
HARD8-01 checkpoint 4 exact verifier: PASS
small SI threshold comparisons: 8624 automata; synchronizing=4911
regular cyclic generator-sensitive formula checks: 4483
regular noncyclic minimum-rank checks: 5 -> [('V4', 1, 2), ('V4', 2, 2), ('V4', 3, 2), ('S3', 2, 3), ('S3', 3, 2)]
prior cyclic-family bridge checks: 78
```

The comparisons use exact finite-state BFS and exact permutation arithmetic only; no floating point, heuristic solver, SAT timeout, or probabilistic acceptance criterion enters the asserted checks.

## Scope reminder

These receipts verify preservation and reproducibility of this checkpoint's mathematical work products. They do **not** constitute independent mathematical review, and the unrestricted Černý conjecture remains open.