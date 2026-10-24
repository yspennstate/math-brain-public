# PROB20-05 — delivery receipts for checkpoint 2026-09-16T03-01-29Z

This append-only receipt note supplements `2026-09-16T03-01-29Z__report.md`; it does not change the mathematical claims.

## Main report

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/runs/2026-09-16/2026-09-16T03-01-29Z__report.md`

Creation commit:

`f778002fc36056bdfdc2d7cbe82fd9dbd64d95da`

Exact-commit readback blob:

`d4c0927d0a443f35b8a408b89a9b94cbeb859635`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

## Phase-1 exact enumerator

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T03-01-29Z__eleven_bin_endpoint_phase1.cpp`

Creation commit:

`b289a34b2f8a6a9cecf561ea5fa0a1ae8c6abeec`

Exact-commit readback blob:

`84b00ce7657b1aa65c656090f2c6842e737dddc7`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

Actual successful run output included:

`total=39916800`

`indecomposable=31998903`

`equal_slab_pass=29028075`

`equal_slab_residual=2970828`

`deterministic_domino_pass=2949943`

`phase2_residual=20885`

`EXACT S11 ENDPOINT PHASE1 PASSED`

The generated residual CSV had 20,885 rows and local SHA-256

`992ba3a27ee9d0201381008ac6e72942f2f45f6cd6c5f0656a6b0cf9d87979cb`.

The CSV is intentionally not separately required as an archived dependency because the verified phase-1 source deterministically regenerates it.

## Phase-2 exact certificate checker

Path:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/artifacts/2026-09-16T03-01-29Z__eleven_bin_endpoint_phase2.py`

Creation commit:

`4324ab346d1b0a3ea1ec6684bf7647211f71c9fd`

Exact-commit readback blob:

`ef6d3f8144e7427d819340bffdc1ed475f172a7f`

Status: **VERIFIED BY EXACT-COMMIT READBACK**.

Actual successful run output included:

`residuals=20885`

`tiling_use={3: 1680, 2: 6229, 1: 3347, 4: 5, 0: 9624}`

`distinct_exact_tuples=1044`

`minimum_exact_margin=710-502*sqrt(2); square_gap=92`

`EXACT S11 ENDPOINT PHASE2 PASSED`

SciPy/Hungarian matching is only a certificate finder. Each returned branch-to-domino bijection is reduced to exact integer tuple data and the final sign is checked by integer comparison in `Z[sqrt(2)]`; numerical optimality is not a proof dependency.
