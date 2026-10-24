SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T01:58:09Z.
attacking: simultaneous affine-envelope localization—localize the full small-ball supremum over conditioning-generated shifts, then splice it with volume-sampling certificates without any support or perturbative-law tax.

# Early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`; full target OPEN.

## First unpaid implication attacked

The completed account03/B14 r23 theorem localizes a *fixed* measurable output map and convex TV-lower-semicontinuous output functional to compact finite-fragment product indicators with no support/fragment/moment tax. The remaining localization issue needed by conditional reductions is stronger: the affine term created by outside conditioning varies with the outside realization, and a proof may also optimize over target intervals. We need the entire affine/small-ball envelope localized at once, not an attained common maximizer.

## New theorem skeleton: simultaneous parameter small-ball localization

Let `D_n` be all product laws with one-dimensional densities `<=1`, and `F_n` the product laws whose marginals are indicators of compact finite unions of intervals of total length one. Let `{P_theta:R^n->R}_{theta in Theta}` be any family of measurable maps. Define

`SB_Theta(mu)=sup_{theta,t,h>0} mu{P_theta in [t,t+h]}/h`.

Using the finite convex-mixture TV approximation underlying account03/B14 r23, one gets exactly

`sup_{mu in D_n} SB_Theta(mu) = sup_{nu in F_n} SB_Theta(nu)`.

Reason: `SB_Theta` is convex (supremum of positive linear functionals of `mu`) and TV-lower-semicontinuous (each fixed event functional is TV-continuous; a supremum of continuous maps is l.s.c.). If `mu_m=sum_r w_r nu_{m,r}->mu` in TV, then

`SB_Theta(mu) <= liminf_m SB_Theta(mu_m) <= sup_{nu in F_n} SB_Theta(nu)`.

For one fixed output law `eta`, `sup_{t,h>0} eta([t,t+h])/h` is exactly the extended `L^infinity` density norm: finiteness implies `eta<=C dx` on all intervals and hence on all Borel sets; conversely Lebesgue differentiation recovers the essential supremum. Thus the theorem localizes the full simultaneous affine `L^infinity` envelope, not only a fixed affine parameter.

## Translation quotient to prove next

For symmetric `B` and affine coefficient `ell`, write `ell=ell_K+ell_R` with `ell_K in Ker(B)` and `ell_R in Range(B)`. Choose `s` with `2Bs=ell_R`. The change `y=x+s` gives

`x^T B x + ell^T x + c = y^T B y + ell_K^T y + c'`.

Coordinatewise translation is a bijection of both `D_n` and `F_n`. Therefore the worst-case small-ball/density constant for fixed `ell` depends only on `P_Ker(B) ell`; for invertible `B`, all conditioning-generated affine terms are removable at zero cost at the worst-law level.

## Required Claude-source application

Claude's completed Theorem D/D' at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, proves for a physical cross block `M=A[I,J]`, third-volume `Z=e_3(M^T M)` and row volume marginals `alpha_i<=h<3/4`, a uniform density estimate (older D' constant)

`||p_Q||inf <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) Z^(-1/6)`

with arbitrary self blocks and affine terms. The simultaneous localization theorem upgrades this to an exact extremal statement: the supremum of the left side over *all* cap-one product laws and all affine parameters equals the same supremum over compact finite-fragment extreme products, and the displayed bound controls that entire envelope. No support radius or common affine maximizer is needed.

Next: write the full proof, derive the range-compatible ambient-core compiler, and combine with the newer volume-stability certificate without treating small matrix error as a small random quadratic error.
