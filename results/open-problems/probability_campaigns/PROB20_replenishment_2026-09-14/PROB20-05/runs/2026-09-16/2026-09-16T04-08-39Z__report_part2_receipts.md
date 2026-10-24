# PROB20-05 — 2026-09-16T04-08-39Z receipt part

This append-only receipt records the actual GitHub delivery and exact-commit readback status for the `n=11` eleven-bin full-grid checkpoint.

## Main report

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/runs/2026-09-16/2026-09-16T04-08-39Z__report.md`

Creation commit:

`1bb8c8a7edc42e48fe6d458c870888eafa9896ed`

Exact-commit readback blob:

`b372c3de1def6b813bc3421901c653bcc3f0c726`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

## Phase-1 reproducibility source

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T04-08-39Z__s11_n11_phase1_universal.cpp`

Creation commit:

`2f7e5092c1f02530414e1d1acb749a2ac36a7d55`

Exact-commit readback blob:

`5f278f8d62fa0aa2dddbf46cc221993342195f95`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

The actual phase-1 run reproduced:

- `total=39916800`;
- `pass=39489793`;
- `fail=427007`;
- `min_pass_margin=2`;
- `max_fail_margin=-8`.

## Phase-2 reproducibility source

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T04-08-39Z__s11_n11_phase2_cell.py`

Creation commit:

`b4664dae98307ad352848bf0c7c3a3c8e30848a7`

Exact-commit readback blob:

`c75b9d4a2322d85682f4d9a3ff7d101653f5b426`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

The actual phase-2 check was executed in disjoint bounded chunks covering all `109285` canonical residual representatives. Aggregating the successful chunks gives:

- canonical residual representatives: `109285`;
- exact cell-certificate successes: `109283`;
- exact cell-certificate failures: exactly identity and full positive cell reversal;
- minimum successful exact cell margin: `0`;
- exact cell margin of identity: `-720`;
- exact cell margin of full positive reversal: `-720`.

The identity is the diagonal equality target. The full positive cell reversal is separately certified by the exact equal-slab computation `D=40`, `G=7/15`, `H=2/3`, giving `Delta/h^2=-1`.

A first monolithic phase-2 execution exceeded the local execution window; it is not used as evidence. The bounded chunk runs are the actual successful evidence.

These are computational/self-check certificates, not independent external verification and not formal proof-assistant verification.
