# account01/B09 — zero-curvature transverse shear and one-overlap minor energy

Run: `B09-20260922T134455Z-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.5`  
Assignment: `Bilinear block mechanism`  
Outcome: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and conditional route

The full target remains OPEN: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal linear small-ball estimate

\[
\Pr\{X^TAX\in I\}\le C|I|
\]

or give a valid counterexample. A continuous density is tracked separately.

The live correction set rules out law-uniform pointwise quadratic-phase decay, naive post-rotation independence, naive fiber-sup integration, a rank-two cross minor by itself, a universal single Schur-pivot extraction, and a universal local principal-block/rank-three-cross-cut dichotomy. The latest regularized-determinant result closes a diffuse entire-range branch but leaves the heavy/nonseparable bridge open.

For B09 the first missing local implication was the branch left out by `QFORM-RANK2-CROSS-TRANSVERSE-CURVATURE-v1`: a genuine `3 x 2` rank-two cross packet whose one-dimensional left-kernel direction has **zero quadratic curvature**, but couples linearly to the two active coordinates through the within-`S` block. This run closes that branch by an integrated Fourier-energy estimate. It also identifies the exact one-overlap `3 x 3` minor energy that measures this shear.

A compact conditional end-to-end route is now:

1. rank-at-least-three disjoint cross smoothing / regularized-determinant branches;
2. rank-two cross plus nonzero kernel curvature: the previous B09 theorem;
3. rank-two `3 x 2` cross plus zero kernel curvature but nonzero transverse shear: the theorem proved below;
4. rank-two cross with neither transverse curvature nor shear, or configurations for which no quantitatively useful packet is extractable: aggregate independent-bank / heavy-coordinate structure remains to be paid before reciprocal local-minor costs.

The new theorem is a supporting target-level implication, not a full extraction theorem.

## 2. Exact dependencies and partner result actually applied

Fresh source control was read from `yspennstate/math-research-brain/main`; the control remained revision `2026-09-22.5` on refresh. Relevant corrections consumed include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, and the newer fiberwise/phase-Wiener corrections.

Named assigned partner result:

- repository `yspennstate/math-open-problems`;
- commit `17dec75dc10459933f8bfde30daa86d1c6d90a6a`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T124417Z-account02-B09-QFORM-r2/REPORT.md`;
- theorem `QFORM-RANK2-CROSS-LP-v1`.

For any original-coordinate rank-two cross cut with nonzero singular-value product `D`, arbitrary same-side quadratic-affine terms are allowed and

\[
\|p_Q\|_3\le 6^{2/3}D^{-1/3}. \tag{2.1}
\]

This exact inequality is applied in Section 7 to the same packet as the new endpoint theorem, yielding a quantitative `L^3`/`L^infinity` interpolation and small-ball ladder.

The previous B09 curvature endpoint is:

- commit `6ac13cdb8eabadf6f99c954107b1fa8ebec70e13`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260922T124649Z-account01-B09-qform-transverse-r11/REPORT.md`;
- theorem `QFORM-RANK2-CROSS-TRANSVERSE-CURVATURE-v1`.

It gives `||p_Q||_infinity <= C_tc D^(-3/7)|kappa|^(-1/7)` when the kernel curvature `kappa` is nonzero. The present result is genuinely different: it assumes `kappa=0` and spends the off-kernel shear instead.

The only external analytic input beyond Plancherel/Hausdorff facts is the standard product-marginal estimate of Livshyts--Paouris--Pivovarov: a `k`-dimensional orthogonal marginal of a product probability density whose factors are bounded by one has density at most `2^(k/2)`. In particular the two-dimensional marginal below is bounded by `2`, and every one-dimensional unit projection is bounded by `sqrt(2)`.

## 3. New endpoint theorem — zero-curvature transverse shear

### Theorem 3.1 — `QFORM-RANK2-CROSS-TRANSVERSE-SHEAR-v1`

Partition the original independent coordinates into disjoint sets `S,T,R`, with

\[
|S|=3,\qquad |T|=2.
\]

Condition on `R`. Write the remaining quadratic-affine polynomial as

\[
q(s,t)=s^T B s+2s^TMt+t^TCt+\ell_S^Ts+\ell_T^Tt+c_0,
\]

where `B` and `C` are symmetric and `M` is `3 x 2`. Assume:

1. `rank(M)=2`;
2. its two nonzero singular values are `s_1,s_2>0`, and `D=s_1s_2`;
3. `e` is a unit vector spanning `ker(M^T)`;
4. the kernel curvature vanishes,
   \[
   \kappa=e^TBe=0;
   \]
5. the transverse shear vector
   \[
   c=(I-ee^T)Be
   \]
   is nonzero.

Then, uniformly over the outside conditioning and hence unconditionally, `Q=X^TAX` has a bounded **continuous** density satisfying

\[
\boxed{
\|p_Q\|_\infty\le C_{\rm sh}\,D^{-3/8}\|c\|^{-1/4},
\qquad C_{\rm sh}<5.948.
} \tag{3.1}
\]

An exact admissible constant is

\[
C_{\rm sh}=\frac4\pi\left(\frac{K}{6}\right)^{3/4},\qquad
K=2\pi\sqrt{\frac{3C_E}{2}},\qquad
C_E=3\,2^{2/3}\left(\frac32+2\pi\right). \tag{3.2}
\]

Consequently every interval `I` obeys

\[
\Pr\{Q\in I\}\le C_{\rm sh}D^{-3/8}\|c\|^{-1/4}|I|. \tag{3.3}
\]

The scaling is exact: `D` has quadratic scale and `c` linear scale, so the right side of (3.1) scales as `A^{-1}`.

## 4. Weighted linear-shear Fourier energy

Take a thin SVD of `M`. Rotate only inside the three-coordinate packet `S` and the two-coordinate packet `T`. No independence is claimed after those rotations. The transformed joint density on `S` is still a probability density `F(z,u)` bounded by one, where `z in R` is the kernel coordinate and `u in R^2` are the active coordinates. The transformed joint density on `T` is likewise bounded by one.

Because `kappa=0`, the `z`-dependence of the phase is exactly linear:

\[
2z\,c\cdot u+\lambda z+G(u),
\]

where the affine coefficient `lambda` may depend on the conditioned outside variables. Define

\[
h_u(z)=F(z,u),\qquad m(u)=\int h_u(z)\,dz,
\]

and

\[
a_t(u)=e^{itG(u)}\widehat h_u\bigl(t(2c\cdot u+\lambda)\bigr).
\]

The two-dimensional marginal theorem gives

\[
0\le m(u)\le2,\qquad \int m(u)\,du=1. \tag{4.1}
\]

For a one-dimensional function `0<=h<=1` of mass `m`, Plancherel and the trivial Fourier bound give

\[
\int_0^\infty \xi^{-1/3}|\widehat h(\xi)|^2d\xi
\le\left(\frac32+2\pi\right)m^{4/3}. \tag{4.2}
\]

Indeed split at `xi=1/m`: below the split use `|hat h|<=m`, and above it use `xi^(-1/3)<=m^(1/3)` together with `int_R |hat h|^2=2pi int h^2<=2pi m`.

Now put `w(u)=2c\cdot u+lambda`. Changing variables `xi=t|w(u)|` in (4.2), then integrating in `u`, gives

\[
\int_0^\infty t^{-1/3}\|a_t\|_2^2dt
\le\left(\frac32+2\pi\right)2^{1/3}
\int |w(u)|^{-2/3}m(u)\,du. \tag{4.3}
\]

The random variable `w(U)` under density `m(u)du` is a one-dimensional linear projection of the original three-coordinate product law, scaled by `2||c||` and translated. Hence its density is bounded by

\[
M_w=\frac{\sqrt2}{2\|c\|}=\frac1{\sqrt2\|c\|}. \tag{4.4}
\]

For any probability density `rho<=M`, symmetric decreasing rearrangement gives

\[
\int |x|^{-2/3}\rho(x)dx\le3(2M)^{2/3}. \tag{4.5}
\]

Combining (4.3)--(4.5),

\[
\boxed{
\int_0^\infty t^{-1/3}\|a_t\|_2^2dt
\le C_E\|c\|^{-2/3},
\qquad
C_E=3\,2^{2/3}\left(\frac32+2\pi\right).
} \tag{4.6}
\]

This is an integrated estimate. It does not invoke the refuted law-uniform pointwise van-der-Corput claim.

## 5. Bilinear Plancherel and `L^1_t`

In the active singular coordinates let `Sigma=diag(s_1,s_2)`. Since `T` has exactly two original coordinates, after its orthogonal rotation its joint density remains bounded by one and has mass one; therefore the corresponding complex amplitude `b_t(v)` satisfies

\[
\|b_t\|_2\le1. \tag{5.1}
\]

Two-dimensional Plancherel gives, for every conditioned outside value,

\[
|\phi(t)|
\le \pi D^{-1/2}|t|^{-1}\|a_t\|_2. \tag{5.2}
\]

For `T_0>0`, Cauchy--Schwarz with (4.6) yields on the positive half-line

\[
\int_{T_0}^\infty |\phi(t)|dt
\le
\pi D^{-1/2}C_E^{1/2}\|c\|^{-1/3}
\left(\frac32\right)^{1/2}T_0^{-1/3}. \tag{5.3}
\]

The same estimate holds for negative `t`. Thus with

\[
K=2\pi\sqrt{\frac{3C_E}{2}},
\]

\[
\int_{\mathbb R}|\phi(t)|dt
\le2T_0+K D^{-1/2}\|c\|^{-1/3}T_0^{-1/3}. \tag{5.4}
\]

At the minimizer, the tail term equals `6T_0`, so the total is `8T_0`, with

\[
T_0=\left(\frac K6\right)^{3/4}D^{-3/8}\|c\|^{-1/4}. \tag{5.5}
\]

Fourier inversion proves (3.1)--(3.3). Since the characteristic function is in `L^1`, the density obtained here is continuous and vanishes at infinity.

All estimates are uniform in the initially conditioned coordinates, so Tonelli transfers the same `L^1_t` bound to the unconditional characteristic function.

## 6. Exact one-overlap minor identity

The preceding endpoint has an exterior-algebra interpretation that connects directly to the heavy/local structural bridge.

Keep `S` of size three and `T` of size two disjoint, with `rank M=2`, `M=A[S,T]`, singular product `D=s_1s_2`, and unit `e in ker(M^T)`. For each `k in S`, define the one-overlap minor

\[
m_k=\det A[S,\{k\}\cup T], \tag{6.1}
\]

with a fixed consistent ordering of the three columns. Let

\[
\mathcal M_1(S,T)=\sum_{k\in S}m_k^2. \tag{6.2}
\]

The two columns of `M` have cross product of norm `D` and direction `plus/minus e`. Therefore

\[
m_k=\pm D\,e^TB e_k
\]

with one common orientation sign. Since `B` is symmetric,

\[
\boxed{
\mathcal M_1(S,T)
=D^2\|Be\|^2
=D^2\bigl(\kappa^2+\|c\|^2\bigr).
} \tag{6.3}
\]

Also

\[
\sum_{k\in S}e_km_k=\pm D\kappa. \tag{6.4}
\]

Thus the one-overlap minors are not merely formal determinant data: they are exactly the components of the within-`S` image of the rank-two cross-kernel direction.

On the new zero-curvature branch `kappa=0`, (6.3) gives `||c||=mathcal M_1^(1/2)/D`. Substitution into (3.1) yields the clean overlap-energy certificate

\[
\boxed{
\|p_Q\|_\infty
\le C_{\rm sh}\,[D\,\mathcal M_1(S,T)]^{-1/8}
\qquad (\kappa=0,\;\mathcal M_1>0).
} \tag{6.5}
\]

This aggregates all three one-overlap `3 x 3` minors in the packet **before** paying a reciprocal determinant cost. It is scale-correct because `D mathcal M_1` has eighth-order quadratic-form scale.

In particular, a rank-two `3 x 2` packet with zero kernel curvature and at least one nonzero one-overlap minor is automatically a bounded-continuous-density certificate.

## 7. Direct application of the named partner theorem

The same packet satisfies the partner inequality (2.1):

\[
\|p_Q\|_3\le 6^{2/3}D^{-1/3}. \tag{7.1}
\]

Combining the **actual partner bound** (7.1) with (6.5) by interpolation gives, for every `3<=p<=infinity`,

\[
\boxed{
\|p_Q\|_p
\le
6^{2/p}C_{\rm sh}^{1-3/p}
D^{-1/8-5/(8p)}
\mathcal M_1(S,T)^{-(1-3/p)/8}.
} \tag{7.2}
\]

At the small-ball level, the same two proved estimates give the two-scale bound

\[
\boxed{
\Pr\{Q\in I\}
\le
\min\left\{
6^{2/3}D^{-1/3}|I|^{2/3},
\;C_{\rm sh}[D\mathcal M_1(S,T)]^{-1/8}|I|
\right\}.
} \tag{7.3}
\]

Thus the named partner's finite-`p` rank-two regularity and the new one-overlap endpoint are quantitatively compatible on the same source-valid configuration.

## 8. Exact status and first unpaid implication

Outcome: `ESSENTIAL_STEP_APPLIED`; full conjecture remains OPEN / not proved / not disproved.

New proved claims:

1. `QFORM-RANK2-CROSS-TRANSVERSE-SHEAR-v1`: zero kernel curvature but nonzero within-packet transverse shear upgrades a genuine `3 x 2` rank-two bilinear channel to an `L^1` characteristic function and bounded continuous density.
2. `QFORM-ONEOVERLAP-MINOR-IDENTITY-v1`: the three one-overlap minors satisfy the exact identity (6.3).
3. `QFORM-ZEROCURV-ONEOVERLAP-ENDPOINT-v1`: on `kappa=0`, the endpoint can be written directly as the aggregate minor-energy bound (6.5).
4. The named account02/B09 `L^3` theorem is applied to obtain (7.2)--(7.3).

The first unpaid implication is now structural rather than analytic:

> **`QFORM-OVERLAP-ENERGY-AGGREGATION-v1` (OPEN).** Starting only from the global hypothesis `s_3(A)>=1`, aggregate the exterior `3 x 3` minor energy before reciprocal local costs and prove that either a quantitatively useful disjoint rank-three / regularized-determinant branch fires, a rank-two packet has sufficient curvature or zero-curvature one-overlap energy for the two B09 endpoint theorems, or one of the already-proved high-cardinality independent-bank / principal-triple branches fires. The extraction must tolerate arbitrary extra spectrum and the source-valid family refuting a single-pivot or single-local-block dichotomy.

A particularly concrete next step is to decompose

\[
\|\wedge^3 A\|_{HS}^2
=\sum_{|I|=|J|=3}\det A[I,J]^2
\ge1
\]

by overlap size `|I cap J|=0,1,2,3`, and convert the **aggregate** one-overlap class into a sum of packet resources of the form `D mathcal M_1`, rather than selecting one tiny minor. The identity (6.3) is the exact local algebra needed for the overlap-one class.

No finite computation, histogram, Gaussian assumption, eigenbasis independence assumption, or refuted pointwise oscillatory estimate is used.
