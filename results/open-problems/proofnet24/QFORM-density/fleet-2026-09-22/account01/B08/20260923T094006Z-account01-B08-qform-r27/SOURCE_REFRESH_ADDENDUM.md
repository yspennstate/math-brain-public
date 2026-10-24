# r27 source-refresh addendum

Final-source refresh found a newer completed designated-partner run than the r24 predecessor cited in the base report:

`yspennstate/math-open-problems@ac9b000da88c4923d8a3adb6a0a8bdccbd27ccae`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T093606Z-account02-B08-qform-diffuse-r25/REPORT.md`.

The r24 structural gate and `N3(tau_*)` facts used in `REPORT.md` remain inputs of r25 and are not contradicted. The phrase in the base report calling r24 the newest completed account02/B08 result is therefore superseded by this addendum; r25 is the newest partner source observed before final publication.

## Direct application of r25 to the new r27 theorem

Partner r25 proves that in its exact Hadamard hybrid, after conditioning any `h<=m/100` original coordinates, `m=2^24`, the mixed gate persists. It also proves that the surviving exact-range leverage after such conditioning is at most

`delta_h <= (3/m)/(1-3h/m) <= (3/m)/0.97`,

and in the `k=2` hybrid both high child eigenvalues stay above

`L_c=0.869771560359221`.

For the child spectral projector at threshold `L_c/1000`, its diagonal is bounded by the diagonal of the full conditioned child-range projector, hence by `delta_h`. Apply r27 Theorem `QFORM-WIDE-TWOEIG-HALFRIESZ-v1` conditionally on every remaining coordinate outside that child. With

`g_h=1/2-delta_h-sqrt(2 delta_h)`,

one gets uniformly in all conditioned values

`H_(1/2)(Q | X_H) <= 8 / sqrt((g_h-0.001)L_c) < 12.151.`

Thus r25's conditioned `k=2` state now has an explicit full-form fractional-potential payment, complementing its already proved `k=1` two-cross payment

`H_(1/2)(Q | X_H)<9.083`.

This yields the source-refreshed statement:

### `QFORM-R25-CONDITIONED-K12-HALFRIESZ-v1`

For the target-valid conditioned Hadamard hybrid of account02/B08 r25 with `h<=m/100`, both mixed gate counts have uniform half-Riesz currency:

- `k=1`: `H_(1/2)<9.083` from the two actual cross directions;
- `k=2`: `H_(1/2)<12.151` from the two actual child directions via r27's wide spectral-window theorem.

The partner's stronger exact-range Fresnel theorem already gives `L^infinity<7.612` and `<7.256` respectively for this special finite-range family. Therefore this addendum does **not** claim a stronger density constant there. Its point is that the fractional receiver now exists for both mixed orientations, including after substantial original-coordinate conditioning. The remaining general debt is exactly the partner's arbitrary-complementary-spectrum `L^infinity` stability problem.

No current correction invalidates this use: the proof conditions only original coordinates, never asserts independence after a spectral rotation, and retains the actual conditioned quadratic child rather than deleting a small matrix tail.
