# B02 r12 addendum — pair plus residual-row closure

Canonical addendum: `yspennstate/math-open-problems@99f0eb89b7b1ad3ef3f225460fb08d4d22c19a75`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T201015Z-account02-B02-qform-r12/ADDENDUM_FRACTIONAL_ROW.md`, blob `92e6e799892ad13dd2250f845cf7cb0deecaf22a`.

Fresh corrections consumed: `QFORM-SQUARE-COLLISION-ALPHA1-ENDPOINT-FALSE-v1` (`b687954d8696656f27ce85d96b376c346157b614`) and `QFORM-CROSS-CYCLE-ARBITRARY-SELF-CURVATURE-FALSE-v1` (`ec721c7cff0759e9daf10b251bd26c05bc2cd3c8`). The new argument stays at quarter-Riesz exponent and requires a genuine invertible indefinite physical pair, so neither correction invalidates it.

From the main row theorem, if `T=aX^2+2XU+R` with `f_X<=1`, `X` independent of the remaining coordinates, and marginal density cap `||p_U||_infinity<=M`, then

`H_(1/4)(T)<=4(4/3)^(3/4)M^(1/4)`.

For a physical row with off-diagonal coefficient norm `sigma`, the product-projection bound gives `M<=sqrt(2)/sigma`, hence

`H_(1/4)(T)<=4(4/3)^(3/4)2^(1/8)sigma^(-1/4)`.

Applying the previous B02 `QFORM-PAIR-FRACTIONAL-TRACE-TRANSDUCER-v1` gives the new branch `QFORM-INDEFINITE-PAIR-RESIDUAL-ROW-v1`: if an outer physical principal pair is invertible indefinite with `D=|det B|`, `kappa=sigma_min(B)`, and one row of its physical Schur residual has off-diagonal norm `sigma>0`, then

`||p_Q||_infinity <= C_*(D kappa sigma)^(-1/4)`,

`C_*=16*2^(3/8)*(4/3)^(3/4)*exp(-1+1/sqrt(2))<19.210`.

Unlike the preceding pair-plus-scalar-pivot theorem, this requires no nonzero residual diagonal and remains valid when the selected residual scalar pivot is exactly zero.

First unpaid implication is structural: force a dimension-free outer principal-pair resource `D*kappa` or replace it by a source-valid aggregate-before-inversion mechanism. The fresh cross-cycle correction rules out treating three cross coefficients alone as that replacement. On the exact-rank-three overlap-one branch, combine the main report's stable `L3_t` credit with retained residual disjoint-pair mass without using the refuted one-square alpha=1 endpoint.
