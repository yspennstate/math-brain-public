# r29 scope correction addendum

**Run:** `20260923T071947Z-fleet03-B06-qform-r29`  
**Status:** theorem retained; live application scope narrowed before user-facing publication.

The analytic statements in Sections 3–5 of `REPORT.md` are unchanged and proved as written:

1. `QFORM-JOINT-COEFFICIENT-NEGATIVE-HALF-MOMENT-v1`;
2. `QFORM-SHARED-COEFFICIENT-DOUBLESTAR-v1`;
3. the linear-product corollary
   `||p_T||_inf <=2 sqrt(3e) sqrt(1+1/sin(theta))/sqrt(||alpha||||beta||)`.

A scope error was found in the first version of Section 6. In the previous r28 report the scalar `b` in

`B=[[b,r^T],[c,D]]`

is an entry of the **cross block** between two coordinate banks. Thus `b=0` means the selected cross coefficient vanishes. It does **not** imply that the diagonal coefficients of the two selected physical anchor variables inside the same-bank quadratic blocks vanish.

Accordingly, the representation

`Q=2XW(Omega)+2YZ(Omega)+R(Omega)`

used in r29 equation (6.1) is valid only in the **double-null diagonal subbranch**, namely when, in addition to the cross-anchor coefficient being zero, the two selected anchor diagonal coefficients are zero (or have previously been removed by a separately proved source-valid reduction). Same-side off-diagonal anchor couplings are still retained inside `W,Z`, and all leaf-only quadratic terms remain in `R`.

Therefore the correct live consequence is:

> In the r28 zero-cross anchor state, assume additionally that both anchor diagonal coefficients vanish. Let `alpha,beta` be the two complete background coefficient vectors. The r28 star currency still gives
>
> `||alpha||||beta|| >= ||r||||c|| > sqrt(127/800) G^2`.
>
> If `sin(theta(alpha,beta))>=1/4`, then the proved r29 receiver gives a continuous density with
>
> `||p_Q||_inf <20.233/G`.
>
> If the angle gate fails, then
> `beta=lambda alpha+epsilon`, `epsilon perp alpha`,
> `||epsilon||<||beta||/4`.

The fleet04/B18 outer-square splice
`<8.997/sqrt(|a|G)`
is likewise valid only when its base residual is this corrected double-null transverse subbranch and the already-source-valid conditional cap-one square hypothesis holds.

No claim is made here that the general r28 zero-cross branch with one or two nonzero anchor diagonal coefficients is paid by the new theorem. Those diagonal cases remain part of the unpaid curved-fiber problem and must be routed through a valid parabola-line / same-sign / third-direction mechanism without deleting their curvature.

This correction does not affect the new negative-moment lemma or shared-coefficient receiver themselves. It prevents a cross-block zero from being silently confused with a full quadratic diagonal zero.
