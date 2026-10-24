# PROB20-21 balanced two-point perturbation coverage manifest

Status: **PASS for the named seven-bit balanced two-point dictator perturbation only; PARTIAL for Courtade-Kumar.**

Selected compressed truth table:

`15555555555555555555555555555557`

Relative to the nearest dictator (output 1 iff coordinate 0 is 0), the selected truth table differs exactly at vertices `1` and `126`; these are antipodal. Its exact average sensitivity is `37/32`.

## Continuous interval coverage

Pinned earlier all-function certificates already cover this function on:

- low noise: `alpha in [0,1/5000]`, artifact `2026-09-16_20-12-15_UTC__n7_low_noise_1_5000.out`;
- high noise: `alpha in [67/135,1/2]`, artifact `2026-09-16_18-40-00_UTC__n7_endpoint_certificate.out`.

The new exact checker certifies the whole remaining middle interval `alpha in [1/5000,67/135]` for this selected function. It proves the stronger pointwise conditional-entropy inequalities for tail Hamming classes `k=0,1,2`; the `k=3` class is proved analytically, and classes `k=4,5,6` follow by complement symmetry.

Therefore this selected balanced two-point perturbation is certified on the complete interval

`alpha in [0,1/2]`.

This does **not** certify all 44,315 source-compressed seven-bit functions on the middle interval and therefore does **not** move the frozen fleet metric beyond `n=6`.

## New executed artifacts

Checker:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/artifacts/2026-09-16_22-00-00_UTC__balanced_two_point_full_interval.py`

Creation commit: `17cf90cfa95f0d2af4f4ffe8f87e6b8df79cc2d5`

Local pre-upload SHA256: `2969c0f29e84e5e69fdc20b9c23a843d155eae452d4c40112d3c7cd84766cf04`

Executed output:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/artifacts/2026-09-16_22-00-00_UTC__balanced_two_point_full_interval.out`

Creation commit: `26d272ccd3809fb4522bf726f715380b58ae1704`

Local pre-upload SHA256: `eadaec3eff19aee4cb0e2c4bbd6fee6a4840e52f0bd41d182a5cbd4233eb3461`

Readback at the creation commit contains:

- `transition_polynomial_identity=PASS`;
- `POINTWISE_K0_K1_K2_MIDDLE_INTERVAL_PASS`;
- `k=3_ANALYTIC_PASS`;
- `BALANCED_TWO_POINT_PERTURBATION_FULL_INTERVAL_PASS_WITH_PINNED_ENDPOINT_CERTIFICATES`.

## Exact validation method

The checker independently reconstructs the posterior transition polynomials from the 128-bit truth table and checks them against the derived two-point formula. On each rational alpha cell it encloses each posterior polynomial by exact Bernstein coefficients. Logarithms are enclosed by 220-bit outward-rounded integer fixed-point arithmetic using the positive atanh series with 23 retained terms and an explicit rational tail bound. Entropy concavity makes the endpoint posterior values sufficient for a lower enclosure on each cell; binary entropy monotonicity on `[0,1/2]` supplies the upper enclosure for `h(alpha)`. Adaptive bisection continues until every cell has a strict positive lower bound.

The output reports strict interval-wide lower bounds for `2 Phi_k`:

- `k=0`: minimum certified lower bound `2.84362569061138787e-08`;
- `k=1`: `6.2906604641033464e-08`;
- `k=2`: `5.8345561742821697e-11`.

These are checker display values only; proof-critical comparisons are performed with exact integers/rationals.

Review level: self-review plus executed exact-arithmetic interval certificate. No P26 or distinct OTHER-task audit exists for this special-case claim.
