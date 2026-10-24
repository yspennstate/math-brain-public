# Latest designated-partner refresh during account01/B01 run

A newer completed account02/B01 handoff appeared after the main report was written. It was consumed before final publication.

Source: `yspennstate/math-open-problems@be378245962c1c91f8d1406efc6c6bd5f50741c7`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T170428Z-account02-B01-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-ONE-HUB-ONE-CROSS-HALFRIESZ-PEEL-v1` says that after scalar completion

`Q=a(X+h(Y,Z))^2+R`,

if the residual has one original hub slope `ell_J` and one projected crossing matrix `C` with one-volume row weights at most `1/2`, then

`||p_Q||_infinity <= 8 |a|^(-1/2)(||ell_J||_2 ||C||_F)^(-1/4).`  (P.1)

No reciprocal residual quadratic coefficient, pair determinant, or pair smallest singular value appears.

## Equation-level application

In the partner's strict-N3 family,

`a=eps`,
`||ell_J||_2=eps^(-1)`,
`C=eps^(-1) w q^T`, with `||w||=||q||=1`, hence `||C||_F=eps^(-1)`.

Substitution into (P.1) gives

`||p_Q||_infinity
 <= 8 eps^(-1/2)(eps^(-1) eps^(-1))^(-1/4)
 = 8 eps^(-1/2) eps^(1/2)
 = 8.`

Thus the latest partner theorem pays its near-null strict-N3 family uniformly even though the relevant physical pair has `sigma_min ->0`.

## Complementarity with the new account01/B01 theorem

The two results fit together cleanly.

- account02/B01: one outer scalar square + one residual hub + a **diffuse** projected one-volume crossing; the row-marginal gate `<=1/2` is essential.
- account01/B01 this run: two hubs + one scalar square whose linear coefficient is entangled with the same leaf bank; it pays the explicit strict no-pivot family where the projected crossing is concentrated on a **single physical row**, so the current projected-crossing marginal is exactly `alpha=1` and the diffuse theorem cannot be invoked.

Hence a sharper combined remaining endpoint is: a concentrated/heavy projected crossing together with zero/near-zero scalar self-curvature or direct hub--third-coordinate coupling. Diffuse projected crossings are now paid by account02/B01; concentrated single-row crossings with nonzero scalar self-curvature are paid by account01/B01.

Full QFORM remains OPEN. No continuity claim is imported from the partner branch; account01/B01's scoped theorem itself has a continuous `C_0` density because its characteristic function is in `L^1`.
