# HARD8-04 verification addendum — 2026-09-16T10:40:43Z

This append-only note records publication/readback receipts and exact execution results for the immediately preceding checkpoint.

## Main mathematical report

Path:

`hard8_2026-09-16/HARD8-04/runs/2026-09-16/2026-09-16T10-35-03Z__report.md`

Creation commit:

`6d586ff20f6c1c05e8c077498ea1da600785b2cf`

Exact-commit readback succeeded. Returned blob SHA:

`75d2165210769c19fad955d76d3ba11d7948d5f1`

Status: **VERIFIED BY READBACK**.

## Exact verifier

Path:

`hard8_2026-09-16/HARD8-04/artifacts/2026-09-16T10-35-03Z__bordered_gs_verifier.py`

Creation commit:

`25d961710196de04aec60137f49795e9929f8360`

Exact-commit readback succeeded. Returned blob SHA:

`44c646521d2158842d18c00bb7a6708b90b13b59`

Status: **VERIFIED BY READBACK**.

The verifier was executed locally before publication using pure integer arithmetic. Its completed output was:

```text
v=2: BGS difference family and bordered Hadamard order 12 PASS
v=4: BGS difference family and bordered Hadamard order 20 PASS
v=6: BGS difference family and bordered Hadamard order 28 PASS
v=8: BGS difference family and bordered Hadamard order 36 PASS
v=10: BGS difference family and bordered Hadamard order 44 PASS
v=12: BGS difference family and bordered Hadamard order 52 PASS
v=14: BGS difference family and bordered Hadamard order 60 PASS
v=16: BGS difference family and bordered Hadamard order 68 PASS
v=18: BGS difference family and bordered Hadamard order 76 PASS
v=20: BGS difference family and bordered Hadamard order 84 PASS
ALL EXACT BGS CHECKS PASSED
v=4: minimum-defect vector states=0; universal one-round repair PASS
v=6: minimum-defect vector states=15; universal one-round repair PASS
v=8: minimum-defect vector states=122; universal one-round repair PASS
v=10: minimum-defect vector states=1046; universal one-round repair PASS
v=12: minimum-defect vector states=13569; universal one-round repair PASS
v=14: minimum-defect vector states=217422; universal one-round repair PASS
ALL EXACT BORDERED REPAIR CHECKS PASSED
```

The full bordered matrix `H` was explicitly constructed at each listed `v` and every entry of `HH^T` was compared to the exact target `4(v+1)I`.

No floating-point acceptance condition, randomization, SAT timeout, or heuristic nonexistence inference was used.

## Scope limitation

The checkpoint does **not** prove existence of the bordered cyclic difference family for all even `v`, and therefore does not resolve the Hadamard conjecture. The finite census supports the stated local repair conjecture only through `v=14`. A bounded `v=22` construction search and larger local census attempts that did not finish are not treated as mathematical evidence of nonexistence.
