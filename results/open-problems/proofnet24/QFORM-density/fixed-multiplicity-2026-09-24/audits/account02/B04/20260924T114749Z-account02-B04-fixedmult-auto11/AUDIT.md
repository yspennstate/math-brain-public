SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-24T11:47:49Z.
attacking: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924, geometric Brascamp--Lieb heat-flow proof and limiting steps, plus an end-to-end dependency audit and a lower-threshold analytic improvement attempt.

# Independent B04 audit of the fixed-multiplicity manuscript

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned manuscript source: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
Source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
Source git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
Manuscript: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, 790 lines.

## Verdict

**Mathematical verdict: PASS (independent B04 review of the complete manuscript).** I found no FALSE statement and no mathematical GAP in the written 17-eigenvalue argument. The theorem therefore survives this independent audit as a candidate theorem. This review is not a self-awarded independent-validation certificate; the owner requires two genuinely separate complete reviews before that status.

**Repository-package verdict: GAP.** At the fresh master tree used for this review, the manuscript root contained `manuscript.tex`, `README.md`, `AUDIT.md`, and `audits/`, but did not contain the `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, or `checks.json` files named by the README/current objective. This blocks reproduction of the advertised finite checker from the current repository package. It does not create a mathematical gap in the self-contained 790-line manuscript, which was reviewed directly.

No part of the mathematical manuscript remains UNCHECKED in this review. The finite checker is UNCHECKED because its files are absent from the current tree.

## Line-by-line / statement audit

### Lines 1--74: theorem statement, normalization, architecture — PASS

The quantifiers are the intended ones: arbitrary dimension, arbitrary independent real coordinate laws with density cap `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and no support/moment/log-concavity hypothesis. `s_j(A)` is the singular-value ordering, hence absolute eigenvalue ordering for symmetric `A`. The theorem's scale `K^2/s` is dimensionally correct. The normalization in the final proof uses `Y=KX` and `Q=(s/K^2)\widetilde Q`, with the affine coefficients transformed correctly.

The split into scalar pivots, definite/indefinite two-coordinate pivots, and no-pivot volume branches is exhaustive under the manuscript definition of pivot.

### Lines 75--129: Fourier identities and power envelope — PASS

The Fourier convention and Gaussian normalization are consistent. For `g_epsilon(x)=(4*pi*epsilon)^(-1/2) exp(-x^2/(4epsilon))`, the transform is `exp(-epsilon t^2)`. The Plancherel proof uses a legitimate Gaussian regularization and `L^2` approximate identity. If `phi_Z in L^1`, the Gaussian-smoothed laws converge uniformly to the Fourier inversion density, while weak convergence identifies it with the law of `Z`. The power-envelope integral gives exactly `2ap/(p-1)` and hence `ap/[pi(p-1)]` after inversion.

### Lines 130--169: negative half moments — PASS

The gamma representation and Gaussian inversion yield

`E|Z-a|^(-1/2) <= (2*pi)^(-1/2) int |t|^(-1/2)|phi_Z(t)| dt`.

The inner `v` integral has constant `sqrt(2) Gamma(1/4)|t|^(-1/2)`, so the displayed normalization is correct. For the `3/4` Fourier envelope, the weighted integral is exactly `12 sqrt(u)`, giving the stated `12 sqrt(u/(2*pi))` bound. Tonelli is used only on nonnegative quantities.

### Lines 170--218: singular-value perturbation, Schur counts, diagonal dominance — PASS

The approximation characterization of singular values supports both the Lipschitz perturbation inequality and the rank shift `s_{j+q}(D+R)<=s_j(D)` without symmetry. The Schur-complement spectral count is correct: for invertible `A`, the complementary principal block of `A^{-1}` is `S^{-1}`, and positive/negative threshold counts for principal compressions give `N_S(t)>=N_A(t)-k`. The singular case is reached by `A+epsilon I`; the pivot remains invertible for small epsilon and the threshold is safely relaxed to `t-|epsilon|`. Strict row diagonal dominance is correctly applied to nonsymmetric matrices.

### Lines 219--255: geometric Brascamp--Lieb heat-flow proof — PASS

This was the primary B04 lens and was independently re-derived.

For `f_i(t)=g_t*h_i` with the manuscript heat kernel, `partial_t f_i=partial_s^2 f_i`. Writing `v_i=partial_s log f_i` and `F=prod_i f_i(t,u_i.x)^{c_i}`, direct differentiation gives

`partial_t F - Delta F = F[sum c_i v_i^2 - |sum c_i u_i v_i|^2]`.

The frame map with columns `sqrt(c_i)u_i` satisfies `WW^T=I`, hence has operator norm one; applied to `(sqrt(c_i)v_i)` this makes the bracket nonnegative. For bounded compactly supported positive-mass data, heat convolutions are positive for `t>0`, and on compact time intervals away from zero their Gaussian tails and polynomially growing logarithmic derivatives justify differentiation under the integral and integration by parts. Thus `int F(t)` is nondecreasing.

Taking the trace of the frame identity gives `sum c_i=d`. After `x=sqrt(t) z`, the transformed integrand is `prod_i [sqrt(t) f_i(t,sqrt(t)u_i.z)]^{c_i}`. Each factor converges to `(4*pi)^(-1/2) M_i exp(-(u_i.z)^2/4)`. The frame identity turns the product exponent into `-|z|^2/4`; compact support gives a uniform Gaussian majorant (for example `C exp(-|z|^2/8)`) for `t>=1`, so dominated convergence yields the exact large-time limit `prod_i M_i^{c_i}`.

As `t downarrow 0`, for each fixed nonzero `u_i` the inverse image of the one-dimensional non-Lebesgue-point set is null; finitely many such sets remain null. Fatou therefore gives the desired inequality for bounded compactly supported data. The truncations `min(h_i,m) 1_{[-m,m]}` increase pointwise to arbitrary nonnegative integrable `h_i`, so monotone convergence closes the rough-data limit. I found no missing normalization or unproved boundary term.

### Lines 257--309: product projections and scalar Fourier powers — PASS

The orthogonal completion `(U,W)` is used only as a deterministic coordinate change in an integral; no rotated random coordinates are asserted independent. With `b_i=|w_i|^2`, the normalized rows `v_i=w_i/sqrt(b_i)` form the required geometric frame. The choice `h_i(t)=f_i((Uy)_i+sqrt(b_i)t)^{1/b_i}` is valid because `0<=f_i<=1` and `1/b_i>=1`; its integral is at most `b_i^(-1/2)`. The entropy estimate `-b log b<=1-b`, together with `sum_i(1-b_i)=d`, gives `e^{d/2}`.

For scalar Fourier powers, `m=floor(p/2)>=p/4`, `|hat f|<=1`, Plancherel, and Fourier inversion of the `m`-fold difference law are all used with the correct exponents. The projection lemma applied to the `2m` signed independent coordinates gives the stated constant `2*pi*sqrt(2e)/sqrt(p)`.

### Lines 311--421: decoupling, graph Brascamp--Lieb, determinant and volume envelopes — PASS

The first Cauchy--Schwarz is taken in the original product law, the copied `J` bank leaves independent differences with density at most one, and no moment assumptions enter. The fourth-power inequality is a valid Jensen consequence of the second-power bound.

For the determinant theorem, set `a=2t`, `alpha=(2*pi*e)^2`, `H=alpha I+a^2 M^TM`. The quantities

`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`

produce an exact rank-one geometric frame, and `theta=sum d_i=sum(1-c_j)`. After `x=H^{-1/2}z`, the one-dimensional Jacobians are exactly those displayed. Since each difference density is at most one, its `L^{1/c_j}` norm is at most one. Applying the scalar Fourier-power lemma with `p=2/d_i` gives

`|| |hat f_i|^2 ||_{1/d_i} <= (2*pi*sqrt(e d_i))^{d_i}`.

The `d_i` powers cancel the row-Jacobian factors. The `c_j` entropy tax is at most `e^{theta/2}`. Since `sqrt(alpha)=2*pi*e`, the remaining constant is exactly one. Factoring `alpha^d` out of `det H` and then taking the fourth root gives

`|phi_Z(t)| <= det(I+t^2 M^TM/(pi^2 e^2))^(-1/8)`.

Cauchy--Binet gives the coefficient identity for `Z_k`; retaining the order-k term produces exponent `k/4`. The k=5 inversion and k=3 Riesz applications use the correct exponents and constants.

### Lines 422--519: scalar/definite/hyperbolic coordinate pivots and quarter-power concentration — PASS

The scalar-square density and interval preimage estimates are correct and are used as conditional measure domination, not as an independence assertion. The definite-pair Jacobian gives `pi M/sqrt(|det B|)`.

For the indefinite pair, the hyperbolic level-set parameterization has absolute `(delta,t)` Jacobian `1/(2 sqrt D)` per branch. The tail monotonicity argument correctly uses one original coordinate density cap and the one-sided decreasing rearrangement bound for `1/|y|`; the middle interval length produces the logarithmic term. The final AM--GM bound on `Lambda` has the right direction.

The quarter-power concentration splits into a large diagonal entry or a random-sign cross block. In the latter case `||M||>=L/4`, and retaining one determinant factor gives the `|t|^{-1/4}` characteristic-function envelope. Gaussian smoothing converts it to small-ball probability with the displayed quarter exponent. Layer cake then yields the logarithmic potential bound. No atom claim is used before it is proved.

### Lines 520--679: disjoint minors, nonsymmetric interpolation, spectral-to-volume conversion, random cuts — PASS

The ordered disjoint-volume definition is used consistently. In the sampling lemma, the bordered determinant identity is correct, and singular seeds are excluded from the sampling law; because singular seeds can possess nonsingular extensions, the manuscript correctly uses an inequality rather than an equality in the multiplicity count.

The interpolation matrix `P=A_{.,T}B^{-1}A_{S,.}` can be nonsymmetric. It has rank at most `r`, agrees exactly with `A` on rows `S` and columns `T`, and the completion `A=D+R+E` has `D=0` on the seed, zero diagonal `E`, global `rank R<=3r`, and restricted `R[L,L]=P[L,L]` of rank at most `r`.

For a bad volume ratio, `||E||<=||E||_F<=1/16`. The singular-value rank shift gives at least `r+1` diagonal entries of `D` of modulus at least `1-epsilon` because `m=4k-3>=4r+1`. They lie in `L` because `D` vanishes on `S union T`. On their `(r+1)`-set, the diagonal of `R` has modulus at least `371/400` while the total off-diagonal row mass is strictly below `23/28`; the slack is positive. This contradicts `rank R[L,L]<=r`. The argument legitimately uses singular values for the nonsymmetric auxiliary matrix.

The random cut identity is exact: each ordered disjoint `(S,T)` survives with probability `4^{-k}`. Thus the no-pivot k=3 and k=5 analytic receivers follow with the stated constants.

### Lines 680--790: pivot half potentials, nine-direction receiver, main theorem and scaling — PASS

For a scalar pivot, Schur reduction plus the quarter-power/log estimate controls the truncated half potential. Definite and indefinite pair cases use their conditional density envelopes with the correct singular kernels. The truncated/full distinction is respected: Proposition nine adds at most one outside `|Q-a|<=1`.

In the main proof, no pivot plus `s_17>=1` uses the order-five density receiver. A scalar pivot removes at most one spectral direction, leaving at least sixteen and therefore enough for the nine-direction half-potential result. A two-coordinate pivot removes at most two; the definite branch is immediate, while the indefinite branch only needs one surviving spectral direction for its logarithmic critical-value average. All affine terms are retained after conditioning. The normalized result scales to `10^4 K^2/s` exactly.

The manuscript correctly refrains from claiming continuity in pivot branches and correctly states that the full three-eigenvalue conjecture remains open.

## Lower-threshold improvement attempt: leverage-half determinant lemma

The audit exposed an exact analytic strengthening of the determinant theorem in a diffuse crossing. It does **not** by itself lower the unconditional 17-eigenvalue theorem, because the manuscript's no-pivot hypothesis does not force the needed physical row-leverage cap.

Let `M` be a physical crossing matrix, write its rows as `m_i^T`, and let

`ell_i = m_i^T (M^TM)^dagger m_i`

be the physical row leverage (zero on the null row). Assume `ell_i<=1/2` for every row. Then for every cross-form

`Z=F(X_I)+2 X_I^T M X_J+G(X_J)`

with the same arbitrary measurable within-bank terms as in the manuscript,

`|phi_Z(t)| <= det(I + t^2 M^TM/(2*pi^2*e^2))^(-1/4)`.

Proof: start from the manuscript's **second-power** decoupling inequality instead of the fourth-power inequality. Put `a=2t`, `alpha=(2*pi*e*sqrt(2))^2`, `H=alpha I+a^2M^TM`, and use the same geometric frame. Its row weights satisfy

`d_i=a^2 m_i^T H^{-1}m_i <= ell_i <=1/2`.

Apply geometric Brascamp--Lieb to the row functions `h_i=|hat f_i|` rather than `|hat f_i|^2`. Now the required scalar Fourier exponent is `p=1/d_i>=2`, and the manuscript's scalar Fourier lemma gives

`||h_i||_{1/d_i} <= (2*pi*sqrt(2e d_i))^{d_i}`.

The `d_i` powers again cancel. The coordinate entropy tax contributes `e^{theta/2}`, so the total scalar factor is `(2*pi*e*sqrt(2)/sqrt(alpha))^theta=1`. Hence the BL integral is at most `det(I+a^2M^TM/alpha)^(-1/2)`. Taking the square root required by second-power decoupling proves the displayed `-1/4` determinant exponent.

If `Z_3(M)>0`, retaining the cubic determinant term gives the integrable envelope

`|phi_Z(t)| <= min(1,(u/|t|)^(3/2))`,

with

`u=sqrt(2)*pi*e*Z_3(M)^(-1/6)`.

Fourier inversion therefore gives the explicit direct density bound

`||p_Z||_infinity <= 3*sqrt(2)*e*Z_3(M)^(-1/6)`.

This shows analytically that **order three is already enough for direct density inversion on leverage-half crossings**. It identifies an exact potential route from 17 directions toward 9 in a diffuse physical regime. The remaining structural obligation is to prove, under a lower spectral multiplicity, either a target-scale order-three crossing with row leverage at most one-half, or a separate high-leverage receiver. The present manuscript's random-cut argument controls `Z_3` but does not control those row leverages, so this lemma is not an unconditional threshold reduction.

## Final status and next obligation

- `thm:main` (17 eigenvalues): **PASS in this independent B04 review**.
- Geometric BL heat flow and rough limiting steps: **PASS**.
- Full manuscript dependency chain: **PASS**.
- Supplementary reproducibility package named by README/current objective: **GAP / files absent in fresh root**.
- Full three-eigenvalue conjecture: **OPEN**.
- Lower multiplicity: **not reduced unconditionally in this run**.
- New proved supporting lemma: the leverage-half crossing improves determinant exponent from `-1/8` to `-1/4`, making `Z_3` directly density-integrable.
- First unpaid implication: derive a product-preserving structural dichotomy below 17 directions that either produces such a leverage-half order-three crossing or pays the complementary high-leverage branch without post-rotation independence or rough-tail deletion.

Execution context: `WITHOUT_VERIFIED_BRAIN`; authenticated repository retrieval was used, but native learned-memory receiver/ingestion was not observed.
