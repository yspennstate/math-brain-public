# account02/B16 — authentic product-fiber trace obstruction and the correct averaged rescue

**Run:** `20260922T133220Z-account02-B16-QFORM-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Projection-product interaction  
**Classification:** `NEW SOURCE-VALID INTERMEDIATE COUNTEREXAMPLE + PARTNER APPLICATION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Full target and source pins

The target remains: for independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal finite essential-supremum bound on the density of `X^T A X`, or produce a valid target-level counterexample. No moment, support, centering, identical-law, sign, or eigenbasis-independence assumption is added.

Fresh control was read from `yspennstate/math-research-brain` main; the last pre-write control snapshot used here is commit `1d572dbe9e647943b289ca845937e74dc7fae407`, revision `2026-09-22.5`. Live corrections consumed include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE`, and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`.

The required completed partner result is account03/B16 run `20260922T125240Z-account03-B16-qform-r11`, canonical report `yspennstate/math-open-problems@d094743ca1c1429601fe7fdc4a4f548103a62bb0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T125240Z-account03-B16-qform-r11/REPORT.md`, blob `4ecafadc8570e17c2b5b647e9a871ca1797f0049`. I use its proved sign-free spectral-row smoothing theorem, not just its summary.

## 2. First unpaid implication attacked

A natural attempt after projecting to the three selected eigen-directions is to orthogonally disintegrate the original product density over the complementary variable `z`, prove a uniform quadratic trace estimate on each projected fiber, and then integrate in `z`.

For an `n x 3` Parseval frame `R` (`R^T R=I_3`), write orthogonally

`x = R y + z`,  `y in R^3`, `z in ker(R^T)`.

If `F(x)=prod_i f_i(x_i)`, define the authentic unnormalized fiber amplitude

`a_z(y)=F(Ry+z)=prod_i f_i(r_i dot y + z_i)`,

its mass `m(z)=int a_z(y)dy`, and for a fixed nondegenerate three-dimensional quadratic `q(y)` the fiber trace density

`T_z(s)=int delta(s-q(y)) a_z(y)dy`.

The tempting interface is a dimension-free inequality

`||T_z||_infinity <= C m(z)`                                                (2.1)

uniformly (or essentially uniformly) in `z`. If true, integrating `z` would immediately preserve the original product law and pay the curved pushforward.

The theorem below shows (2.1) is false even for an explicit **authentic product source**, an exact rank-three Parseval frame, unit-interval input densities, and maximum row leverage `<=1/2`. Thus the failure is stronger than an arbitrary dependent-projection counterexample: the bad dependent fiber is produced by a genuine independent bounded-density product law.

## 3. Exact eight-coordinate construction

Let

`u=(1,-1,0)/sqrt(2)`,

`w=(1,1,2)/sqrt(6)`,

`v=(-1,-1,1)/sqrt(3)`.

These form an orthonormal basis of `R^3`. Let `R` have eight rows

`r_1=r_2=r_3=r_4=v/2`,

`r_5=r_6=u/sqrt(2)`,

`r_7=r_8=w/sqrt(2)`.

Then exactly

`sum_i r_i r_i^T = v v^T + u u^T + w w^T = I_3`,

so `R^T R=I_3`, while every row leverage is at most `1/2`.

Fix `0<delta<=1/100`. Set

`L=1/sqrt(2)`, `d=1-L`.

Take the independent input densities to be indicators of the following length-one intervals:

`I_1=[-1,0]`,

`I_2=[-delta/2, 1-delta/2]`,

`I_3=I_4=[-1/2,1/2]`,

`I_5=I_7=[-1/2-d/2, 1/2-d/2]`,

`I_6=I_8=[-1/2+d/2, 1/2+d/2]`,

and `f_i=1_{I_i}`. Every `f_i` is a probability density bounded by one.

Use orthogonal coordinates

`alpha=u dot y`, `beta=w dot y`, `t=v dot y`.

On the complement fiber `z=0`, the first two `v` rows have support intersection `t/2 in [-delta/2,0]`; rows 3 and 4 are nonbinding there. The two `u` rows intersect in `alpha/sqrt(2) in [-L/2,L/2]`, and the two `w` rows do the same. Therefore the authentic fiber is exactly

`a_0(y)=1_{|alpha|<=1/2} 1_{|beta|<=1/2} 1_{-delta<=t<=0}`.      (3.1)

Its mass is exactly

`m(0)=delta`.                                                     (3.2)

No arbitrary copula has been inserted: (3.1) is obtained by conditioning the stated independent product law in the actual orthogonal decomposition attached to `R`.

## 4. The curved trace on that fiber has a logarithmically diverging normalized peak

Take

`Lambda=diag(1,1,-1)`, `q(y)=y^T Lambda y`.

In the `(u,w,v)` coordinates one checks exactly

`q(alpha,beta,t)
 = alpha^2 - beta^2/3 - (4 sqrt(2)/3) beta t + t^2/3
 = alpha^2 - (beta+2 sqrt(2)t)^2/3 + 3t^2`.                      (4.1)

Put `gamma=beta+2 sqrt(2)t` and then

`r=alpha-gamma/sqrt(3)`, `s=alpha+gamma/sqrt(3)`.

The Jacobian is

`d alpha d beta = (sqrt(3)/2) dr ds`,

and (4.1) becomes

`q = r s + 3t^2`.                                                 (4.2)

For fixed `t<0`, restrict to

`6|t| <= r <= 1/8`.

At level `q=0`, the root is `s=-3t^2/r`, with `|s|<=|t|/2`. For `delta<=1/100`, these roots stay strictly inside `|alpha|,|beta|<1/2`. Integrating the delta function in `s` gives

`T_0(0)
 >= (sqrt(3)/2) int_{-delta}^0 int_{6|t|}^{1/8} dr/r dt
 = (sqrt(3)/2) int_0^delta log(1/(48t)) dt`

and hence

`T_0(0) >= (sqrt(3)/2) delta [ log(1/(48delta)) + 1 ]`.           (4.3)

Combining (3.2) and (4.3),

`T_0(0)/m(0)
 >= (sqrt(3)/2)[ log(1/(48delta)) + 1 ] -> infinity`.            (4.4)

So no universal pointwise fiber trace/mass inequality can hold.

## 5. The failure is not confined to a null exceptional fiber

The complement is explicit. Since the row groups lie in the mutually orthogonal directions `v,u,w`,

`ker R^T = { z : z_1+z_2+z_3+z_4=0, z_5+z_6=0, z_7+z_8=0 }`.

Consider the positive-five-dimensional-measure set `Z_delta` obtained by taking

`|z_1|,|z_2|,|z_3| < delta/64`, `z_4=-(z_1+z_2+z_3)`,

`|z_5|<1/(64sqrt(2))`, `z_6=-z_5`,

`|z_7|<1/(64sqrt(2))`, `z_8=-z_7`.

For every `z in Z_delta`:

* the `t`-interval has width between `15delta/16` and `17delta/16` and contains `[-delta/2,-delta/4]`;
* the `alpha` and `beta` intervals remain centered at zero, each with width between `31/32` and `33/32`;
* rows 3 and 4 remain nonbinding on the inner region used below.

Therefore

`m(z) <= (33/32)^2 (17delta/16) = (18513/16384) delta`.           (5.1)

Repeating the regular-root calculation only on `t in [-delta/2,-delta/4]` gives

`T_z(0) >= (sqrt(3) delta/8) log(1/(24delta))`.                  (5.2)

Hence throughout a positive-measure set of complement fibers,

`T_z(0)/m(z)
 >= (2048 sqrt(3)/18513) log(1/(24delta))`.                     (5.3)

The coefficient is about `0.191608`. Thus even an **essential-uniform** normalized fiber trace estimate diverges logarithmically.

This is the new correction:

`QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`.

It refutes only the intermediate disintegrate-then-take-a-uniform-fiber-bound mechanism. It is **not** a counterexample to the owner conjecture.

## 6. Applying the completed account03/B16 partner theorem: averaging before the trace succeeds

Now form the exact rank-three physical quadratic matrix

`A=R Lambda R^T`.

It has nonzero spectrum `{1,1,-1}`, so it lies exactly at the target spectral threshold.

Apply account03/B16's completed theorem `QFORM-SPECTRAL-ROW-DIFFUSE-RESIDUAL-v1` with physical pivot row `r_5=u/sqrt(2)`. Here

`ell=||r_5||^2=1/2`,

`a=A_55=r_5^T Lambda r_5=1/2`,

`|det Lambda|=1`.

After projecting the remaining rows to `r_5^perp`, the other `u` row vanishes, the four `v/2` rows have residual leverage `1/4`, and the two `w/sqrt(2)` rows have residual leverage `1/2`. Thus the partner theorem's diffuse-residual condition is exactly satisfied. It yields for the **full unconditioned product law**

`||p_{X^T A X}||_infinity
 <= 4 sqrt(3e) (ell |det Lambda| |a|)^(-1/4)
 = 4 sqrt(6e)
 < 16.155`.                                                       (6.1)

So the same family simultaneously has:

* a uniformly bounded full target output by a completed partner theorem; and
* complement fibers of positive measure whose normalized curved trace grows like `log(1/delta)`.

This proves a precise noncommutation statement: **the product aggregation must be used before, or jointly with, the curved quadratic pushforward.** Passing first to normalized complement-fiber laws and then demanding a uniform three-dimensional trace bound destroys the compensation supplied by the original independent coordinates.

Equivalently, if

`T_z(s)=int delta(s-q(y)) prod_i f_i(r_i dot y+z_i) dy`,

then the correct full density identity is

`p_Q(s)=int_{ker R^T} T_z(s) dz`,                                (6.2)

and (6.1) controls the integral in (6.2) although `ess sup_z ||T_z/m(z)||_infinity` is arbitrarily large by (5.3). The order `integrate z -> estimate the curved trace` cannot in general be replaced by `estimate each normalized fiber -> integrate z`.

## 7. Consequence for B16's previous phase-Wiener interface

The previous account02/B16 run reduced the general higher-rank problem to an averaged phase-weighted Wiener tail. The present construction does not refute that averaged interface. It does rule out one tempting way to prove it: orthogonally disintegrate the product law over the complement and replace the product source by a uniform pointwise bound for each normalized projected fiber before applying the indefinite quadratic trace.

The surviving source-valid route must keep at least one of the following until after the nonlinear trace:

1. original-coordinate product aggregation (as in account03/B16's diffuse rank-two theorem and spectral-row smoothing), or
2. signed/oscillatory averaging over the complement before taking absolute values, or
3. a finite-heavy-core plus diffuse-remainder theorem that averages the heavy complement coordinates rather than freezing them.

This narrows `QFORM-PHASE-WIENER-AVERAGED-v1`: any proposed proof based on a pointwise complement-fiber `L^infinity` or trace/mass replacement is now excluded by an authentic product-source example.

## 8. Additional partner consequence: separable nonpivot perturbations are already harmless

The same completed account03/B16 theorem `QFORM-DIFFUSE-RANK2-L3-SEPARABLE-v1` allows arbitrary coordinate-separable phases in the residual two-dimensional diffuse projection. Therefore its spectral-row smoothing proof extends verbatim as follows.

Let `R` be any `n x 3` Parseval frame, `Lambda` invertible, choose row `v=r_i` with `a=v^T Lambda v !=0`, and suppose the residual two-frame after projection to `v^perp` has all row leverages `<=1/2`. For arbitrary measurable finite-a.s. functions `V_k`, `k!=i`, define

`Y=(R^T X)^T Lambda(R^T X) + sum_{k!=i} V_k(X_k)`.

Completing the square only in the original independent coordinate `X_i` leaves a residual

`D(Z)=xi^T B xi + sum_{k!=i} V_k(X_k)`

with the same rank-two Schur matrix `B` and

`det B = ||v||^2 det(Lambda)/a`.

The partner theorem gives

`||p_D||_3 <= (3e)^(2/3) |det B|^(-1/3)`.

Conditioning on `D`, the shifted `X_i` is still a mixture of translates of the original cap-one density. The completed dependent `L^3 -> L^infinity` square-smoothing step used inside the partner proof therefore gives

`||p_Y||_infinity
 <= 4 sqrt(3e) ( ||v||^2 |det Lambda| |a| )^(-1/4)`.            (8.1)

Thus arbitrary diagonal quadratic/linear perturbations on the **nonpivot** physical coordinates are already harmless in this localized-plus-diffuse branch. Affine perturbations of the pivot are harmless as well, since they only translate the completed square and add linear coordinate-separable terms to the residual. A quadratic perturbation of the pivot is not claimed: it changes the Schur rank and must be reanalyzed.

For a full matrix, conditioning on variables outside a physical block turns outside cross-couplings into affine terms on the block, so (8.1) is stable under arbitrary outside couplings whenever the chosen principal block has this rank-three-plus-nonpivot-separable structure. This is a genuine supporting target-level subclass, not a universal structural reduction.

## 9. Status and next implication

**PROVED here:** an explicit authentic product-source, Parseval-frame, positive-measure family of complement fibers for which normalized indefinite quadratic traces grow logarithmically; the full product law for the same family is nonetheless bounded by the completed assigned-partner theorem. Also derived the explicit nonpivot-separable extension (8.1) of that partner mechanism.

**NOT PROVED:** the full owner conjecture. No target-level counterexample is claimed.

The next B16 implication is now sharper: build an **averaged** heavy-core/diffuse-remainder inequality in which the complement variables responsible for thin projected fibers are integrated before the indefinite trace is bounded. In particular, any finite-heavy-core reduction must preserve the overlap-width averaging that converts a conditional `log(1/delta)` loss into a finite unconditional contribution; freezing the heavy complement and taking a fiber supremum is invalid.
