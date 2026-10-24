# account03/B04 r14 addendum — bounded 3D density alone does not control a rank-three quadratic pushforward

This addendum records a later-control correction discovered in the same invocation. After the main report was committed, fresh owner control advanced to revision `2026-09-22.8`. That message proposed, as an intermediate lemma, that if a three-dimensional vector `Y` has bounded joint density `rho`, then an indefinite rank-three quadratic form such as

`q(Y)=Y_1^2+Y_2^2-Y_3^2`

should have density bounded by a universal constant times `||rho||_infinity`. The following exact construction refutes that intermediate statement. It does **not** refute the QFORM conjecture because the constructed `rho` is not asserted to arise as an orthogonal projection of an independent cap-one product source.

## Proposition — `QFORM-RANK3-COAREA-LINF-ONLY-FALSE-v1`

There is no universal `C` such that, for every probability density `rho` on `R^3`,

`||p_{Y_1^2+Y_2^2-Y_3^2}||_infinity <= C ||rho||_infinity`.

In fact this fails even with `||rho||_infinity=1` and compact support.

### Proof

Fix `R>1` and put

`delta_R = 1/(pi R)`.

Use cylindrical coordinates

`Y_1=r cos(theta)`, `Y_2=r sin(theta)`, `Y_3=z`,

and define

`E_R = { R<=z<=2R, 0<=r^2-z^2<=delta_R }`.

Set `rho_R=1_{E_R}`. Introduce the quadratic coordinate

`u=r^2-z^2`.

Since `du=2r dr`, the Euclidean volume element becomes

`r dr dtheta dz = (1/2) du dtheta dz`.

Therefore

`|E_R|
 = integral_R^{2R} integral_0^{2pi} integral_0^{delta_R} (1/2) du dtheta dz
 = pi R delta_R
 =1`.

Thus `rho_R` is a probability density and `||rho_R||_infinity=1`.

For `Q_R=Y_1^2+Y_2^2-Y_3^2=u`, the same change of variables gives, for every `0<u<delta_R`,

`p_{Q_R}(u)
 = integral_R^{2R} integral_0^{2pi} (1/2) dtheta dz
 = pi R`.

Hence

`||p_{Q_R}||_infinity = pi R -> infinity`,

while `||rho_R||_infinity=1`. QED.

The same shell mechanism also shows why bare `L^infinity` control of a multidimensional density cannot by itself control a quadratic pushforward: a probability density can concentrate on a unit-volume thin tubular neighborhood of one long quadratic level set. The noncompact cone makes the signature `(2,1)` example especially transparent.

## Relation to the fresh account02/B17 correction

The same final control refresh exposed the completed `account02/B17` result `QFORM-CONDITIONAL-3D-PROJECTION-CAP-FALSE-v1`, canonical `yspennstate/math-open-problems@f117a4870969d37706b8d7e62cbcae671cc2d3b0`. It shows independently that the proposed universal **conditional** cap for three active spectral coordinates is false even for an exact QFORM product source.

Thus both scalar interfaces in the revision-8 sketch require replacement:

1. bounded conditional 3D density is not available pointwise;
2. even an arbitrary bounded 3D density does not have a universally bounded indefinite quadratic pushforward from `L^infinity` alone.

A viable rank-three coarea route must retain additional product/projection provenance in the curved trace, for example an integrated slice norm, a product-space Fourier/rearrangement currency, or a joint bank aggregate. This is consistent with the main r14 theorem, which keeps an original-coordinate conditional cap through an actual scalar pivot rather than replacing product provenance by a projected-density supremum.

Full QFORM remains OPEN. This is a correction to an intermediate proof route, not a target counterexample.