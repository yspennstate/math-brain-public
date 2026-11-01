# HARD8-08 — verification addendum for checkpoint 7

This file records exact-SHA readback receipts and the deterministic checks executed for the checkpoint beginning at `2026-09-16T11-50-00Z`.

## 1. Main mathematical report

Path:
`hard8_2026-09-16/HARD8-08/runs/2026-09-16/2026-09-16T11-50-00Z__report.md`

Creation commit:
`0642528582ebffb926591a7a2ffac7ebd43b0e24`

Exact-creation-SHA readback succeeded. Returned content blob:
`4cb1568d83bdb44332a78a4fc89f0d395dfe12bc`

Status: **VERIFIED**.

## 2. Exact verifier source

Path:
`hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T11-50-00Z__sqrt3_skeleton_verifier.py`

Creation commit:
`0152ab771dd49f82782077c8ad00ea99b509b05f`

Exact-creation-SHA readback succeeded. Returned content blob:
`43f1b443faecbf6354ea5bbf7efd7ab0ca5ae52b`

Status: **VERIFIED**.

The archived standard-library verifier was executed before upload. It terminated normally and printed:

```text
VERTICES 33
UNIT_EDGES 81
SQRT3_EDGES 32
TOTAL_EDGES 113
FULL_6_COLORING_VALID True
FULL_5_COLORABLE False
SQRT3_DELETION_WITNESSES_VALID 32
ALL_CHECKS_PASSED
```

The verifier uses no floating point, randomness, external SAT solver, or timeout inference. Squared distances are represented exactly as `A+B*sqrt(5)` after multiplying by 64. Non-five-colourability is checked by deterministic exhaustive DSATUR backtracking. Edge-deletion colourings are explicit finite certificates and are checked directly.

## 3. `sqrt(3)` edge-deletion witness table

Path:
`hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T11-50-00Z__sqrt3_edge_deletion_witnesses.tsv`

Creation commit:
`41cfc7d075bbfe0ef1f63692f59003b8ea9c442b`

Exact-creation-SHA readback succeeded. Returned content blob:
`7fdc68de87356f98b71dbc571c91a34481e7867e`

Status: **VERIFIED**.

There are 32 rows, one for each exact `sqrt(3)` edge reconstructed from the published 33-coordinate table. Each row gives an explicit proper five-colouring after deletion of that edge. In each witness the deleted edge's two endpoints receive the same colour, certifying that the omitted constraint is exactly what the witness violates.

## 4. Exact execution output record

Path:
`hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T11-50-00Z__sqrt3_skeleton_output.txt`

Creation commit:
`e54f57401635db14ed24021dca596ec4447fa469`

Exact-creation-SHA readback succeeded. Returned content blob:
`ad05b27ab6681d4df5743733fc7b1f757002850e`

Status: **VERIFIED**.

## 5. Source-data cross-check

The accepted manuscript of De Neve–Vanden Kerchove–Colle–Tavernier–Pickavet gives the 33 exact coordinate quadruples in Table 1 and states that the minimized `d=sqrt(3)` graph has 113 edges. The exact reconstruction from those coordinates produced `81+32=113`, agreeing with the paper's total.

The published source also reports the graph as six-chromatic. The project verifier independently checks an explicit six-colouring and exhaustively rules out five colours for the reconstructed abstract graph.

## 6. Status

The new result is a **conditional reduction**, not a solution of Hadwiger–Nelson:

> a single five-colour forced-different unit-distance gadget at terminal separation `sqrt(3)` would suffice, via 32 copies placed on the 32 non-unit edges of the exact published 33-vertex `{1,sqrt(3)}` six-chromatic skeleton, to produce a finite planar unit-distance graph requiring at least six colours.

Every one of those 32 `sqrt(3)` constraints is individually critical in the exact skeleton. No such five-colour unit-distance terminal gadget was found in this run, so the unrestricted problem remains open.