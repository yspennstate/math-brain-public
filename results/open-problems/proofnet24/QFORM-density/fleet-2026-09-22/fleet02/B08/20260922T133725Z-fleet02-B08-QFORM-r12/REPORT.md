# fleet02/B08 — fractional-MSS diffuse-range extension and block-remainder complement

**Run:** `20260922T133725Z-fleet02-B08-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Diffuse eigenvector case`  
**Classification:** `ESSENTIAL_STEP_APPLIED / QFORM-DIFFUSE-RANGE-FRACTIONAL-MSS-v1`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full conjecture:** **OPEN / NOT PROVED / NOT DISPROVED**.

## 0. Fresh scope, corrections, and sources

The target remains: for arbitrary independent real coordinates with densities `0<=f_i<=1` and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove one dimension/law/matrix-independent upper bound for the density of `X^T A X`, or give a valid counterexample. No moment, compact-support, identical-law, sign, or post-rotation independence hypothesis is added.


Source-pinned mathematics actually used:

1. **Regularized determinant theorem**, `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, path `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`, source report blob recorded in the brain handoff as `080253f929411bfa9c7aa3254a2bdaf37be72ebb`. For an original-coordinate cross block `B=A[I,J]`, `1<=q<2`, left range leverage at most `q/2`, and at least `r>2q` singular values at least `sigma`, it proves

   `||p_Q||_infinity <= e r / [sqrt(2q) sigma (r-2q)]`,

   with a sharper gamma-factor constant, while retaining arbitrary self-block phases/outside couplings and arbitrary extra small singular values.
2. **Marcus--Spielman--Srivastava two-part frame partition**, Corollary 1.5 as quoted and source-pinned in the regularized-determinant report: if `sum_i u_i u_i^T=I` and `||u_i||^2<=delta`, there is a two-partition whose two Gram sums have operator norm at most `(1/sqrt(2)+sqrt(delta))^2`.
3. **Named partner fleet03/B08 latest completed report**, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T122924Z-fleet03-B08-qform-diffuse-v2/REPORT.md`, current blob `4741a2fa3876dc21a520cc8d990e2a95ca438d15`. Its theorem `QFORM-DIFFUSE-BLOCK-REMAINDER-v1` gives, for selected rank `r=3` and residual physical blocks of mass `mu<1/3`, the bound `12/(1-sqrt(3mu)) |det Lambda|^(-1/3)`.
4. This slot's preceding theorem `QFORM-WHITENED-PHYSICAL-BLOCK-v1`, canonical report `yspennstate/math-open-problems@84657e690f8411d99602ddc772b622686c3874ed`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T124007Z-r11/REPORT.md`.
5. Fresh complementary result `QFORM-AGGREGATE-CROSSMINOR-DETERMINANT-v1`, fleet01/B07, `yspennstate/math-open-problems@22acf813ef825872ffe594818d6adb27e9d4e41f`, report blob `6b0996f550365a62f2a3bb7ac9322fb20f3c160f`. Its exact determinant-decrement identity confirms that high physical leverage is the remaining payment variable, not a missing single-minor estimate.

The regularized-determinant source is a complete supplied supporting proof but was explicitly marked pending its assigned independent reviews when read. The theorem below is therefore source-dependent on that result; it is not promoted to a reviewed full solution.

## 1. First unpaid implication, attacked immediately

The current diffuse end-to-end route is:

1. turn spectral delocalization into an original-coordinate cut with three large cross singular directions;
2. keep the cross-range coordinate leverage below the fractional determinant gate;
3. apply the regularized determinant estimate, which already tolerates all self-block phases and arbitrarily small additional eigenvalues;
4. use localized/block mechanisms on the complement.

Step 2 is the first quantitative debt on the diffuse branch, while the global heavy-coordinate/nonseparable reduction remains the first structural debt for the full conjecture.

The existing full-range theorem fixed `delta<=1/32` and `q=1`. The first new calculation below optimizes the *fractional* exponent `q` jointly with the MSS partition. It nearly doubles the permitted entire-range leverage, to the clean threshold `delta<=1/16`, without adding any restriction on the number, signs, or sizes of the additional nonzero eigenvalues.

## 2. Fractional-MSS theorem for the entire spectral range

### Theorem 2.1 — `QFORM-DIFFUSE-RANGE-FRACTIONAL-MSS-v1`

Let

`A = U Lambda U^T`,

where the columns of `U in R^{n x m}` are orthonormal and span the **entire range** of `A`, so `Lambda` is invertible. Assume at least three eigenvalues of `Lambda` have absolute value at least one. Put

`delta = max_i ||u_i||^2`,

where `u_i^T` are the rows of `U`, and define

`alpha(delta) = 1/2 - delta - sqrt(2 delta)`.

If `alpha(delta)>0` and there is a number `q` such that

`1 <= q < 3/2`,

`2 delta / alpha(delta) <= q`,

then for every admissible independent product law the quadratic form `Q=X^TAX` has a continuous density, vanishing at infinity, and

`||p_Q||_infinity
 <= [e sqrt(pi)/(2 sqrt(2q) alpha(delta))]
    Gamma(3/(4q)-1/2) / Gamma(3/(4q))`

and in particular

`||p_Q||_infinity
 <= 3e / [sqrt(2q) alpha(delta) (3-2q)]`.

All additional nonzero eigenvalues may be arbitrarily small, of either sign and in arbitrary number.

### Proof

Apply the two-part MSS partition to the rows of `U`. There is an original-coordinate partition `I union J=[n]` such that, writing

`M_I=U_I^T U_I`, `M_J=U_J^T U_J`,

both satisfy

`M_I,M_J <= beta I_m`,

where

`beta=(1/sqrt(2)+sqrt(delta))^2
     =1/2+delta+sqrt(2delta)`.

Since `M_I+M_J=I_m`, both also satisfy

`M_I,M_J >= alpha I_m`,

with `alpha=1-beta=alpha(delta)>0`.

For the original-coordinate cross block

`B=A[I,J]=U_I Lambda U_J^T`,

write

`U_I=P M_I^(1/2)`, `U_J=R M_J^(1/2)`

with `P,R` isometries. Thus the nonzero singular values of `B` are those of

`T=M_I^(1/2) Lambda M_J^(1/2)`.

For every singular-value index `k`,

`s_k(T) >= sqrt(lambda_min(M_I)) sqrt(lambda_min(M_J)) s_k(Lambda)
        >= alpha s_k(Lambda)`.

Since `s_3(Lambda)>=1`, `B` has at least three singular values at least `alpha`.

Because `Lambda` is invertible and both restricted frames have full column rank,

`range(B)=range(U_I)`.

Hence the coordinate leverage on the `I` side is

`(P_range(B))_ii
 = u_i^T M_I^(-1)u_i
 <= ||u_i||^2/alpha
 <= delta/alpha
 <= q/2`.

The source regularized-determinant theorem therefore applies with exactly three retained cross singular values, `sigma=alpha`, and the chosen `q`. The condition `q<3/2` is exactly `3>2q`, so the time envelope is integrable. Its Section 6 density estimate gives the two displayed bounds. No spectral coordinate was declared independent. QED.

## 3. Exact leverage threshold of this mechanism

A suitable `q in [1,3/2)` exists exactly when

`2delta/alpha(delta) < 3/2`.

Equivalently,

`7delta + 3 sqrt(2delta) < 3/2`.

The positive endpoint is

`delta_* = 39/98 - 3 sqrt(30)/49
         = 0.0626188423438...`.

Thus the two-part-MSS + three-cross-direction fractional determinant mechanism reaches every fixed leverage threshold strictly below `delta_*`. The blow-up as `delta` approaches `delta_*` is a **method ceiling**, not a counterexample to QFORM.

Two clean uniform corollaries are useful.

### Corollary 3.1 — full-range leverage `<=1/16`

If

`max_i ||u_i||^2 <= 1/16`,

then the full target conclusion holds for this matrix class with the explicit universal bound

`||p_Q||_infinity < 2814`.

Indeed at `delta=1/16`,

`alpha_* = 7/16 - sqrt(2)/4 = 0.0839466094067...`,

and

`delta/alpha_* = (7+4sqrt(2))/17
                =0.744520838205... <149/200`.

Choose `q=149/100`; then `q/2=149/200` and `3-2q=1/50`. The simple bound in Theorem 2.1 gives

`||p_Q||_infinity
 <= 3e/[sqrt(149/50) alpha_* (1/50)]
 =2813.67835196808... <2814`.

This strictly enlarges the existing source theorem's clean `1/32` full-range leverage branch. The price is only the displayed larger constant; all arbitrary small additional eigenvalues remain permitted.

### Corollary 3.2 — a better constant at leverage `<=3/50`

If `delta<=3/50`, choose `q=4/3`. Here

`alpha=11/25-sqrt(3)/5=0.0935898384862...`

and `delta/alpha<2/3=q/2`. Hence

`||p_Q||_infinity < 161`.

The computed simple constant is `160.075153671890...`.

## 4. Named partner application to an actual complementary family

The partner's completed block-remainder theorem covers a family that the new full-range result deliberately does not.

Let `K=12`. Let `H` be a normalized real `4 x 4` Hadamard matrix, let `V` be its first three columns, and let `w` be its fourth column. Then `V^T V=I_3`, `V^T w=0`, and every row of `V` has squared norm `3/4`, while every coordinate of `w` has square `1/4`.

Split `n=48` original coordinates into twelve four-coordinate blocks `G_k`. Define

`R_{G_k}=K^(-1/2) V`.

Then `R^T R=I_3` and

`M_k=R_{G_k}^T R_{G_k}=K^(-1)I_3=(1/12)I_3`.

Choose any invertible symmetric `3 x 3` matrix `Lambda` whose three eigenvalues have modulus at least one, and choose arbitrary nonzero `tau_k` with `|tau_k|<1`. Put

`C[G_k,G_k]=tau_k w w^T`,

with all cross-block entries of `C` zero, and set

`A=R Lambda R^T+C`.

Because `w` is orthogonal to `V` blockwise, `CR=0`: the three columns of `R` are genuine large spectral directions and the twelve `w_k` are genuine additional small spectral directions. Each `C[G_k,G_k]` is a dense rank-one off-diagonal physical block, not a coordinate-separable remainder.

The named partner theorem applies with

`mu=max_k ||M_k||=1/12`.

Therefore

`||p_Q||_infinity
 <= 12/(1-sqrt(3/12)) |det Lambda|^(-1/3)
 =24 |det Lambda|^(-1/3)
 <=24`.

This is an actual quantitative use of fleet03/B08's completed result.

It is genuinely complementary to Theorem 2.1. Because every `tau_k` is nonzero, the full range also contains each block vector `w_k`. The full-range coordinate leverage is therefore

`3/(4K)+1/4 = 1/16+1/4 =5/16`,

far above `1/16` (and above the method endpoint `delta_*`). Thus the partner's physical-component theorem closes this dense-block family precisely where the full-range diffuse theorem cannot.

## 5. Compact conditional end-to-end argument after this run

A full proof would follow from an exhaustive original-coordinate reduction that sends every target matrix into one of the already paid branches:

1. **full-range diffuse:** `max diag(P_range(A))<=1/16`, paid by Theorem 2.1 / Corollary 3.1, including arbitrary small extra spectrum;
2. **selected-large-space with physically decomposable residual:** paid quantitatively by fleet03/B08's block-remainder theorem (Section 4 gives an explicit overlapping dense-block example);
3. **localized physical curvature / whitened block:** paid by the preceding B08 physical-block theorem and the existing localized-coordinate results;
4. the remaining heavy/dense branch, where no such reduction has yet been proved.

The first essential missing implication is therefore sharpened to

`QFORM-DIFFUSE-HEAVY-RANGE-BRIDGE-v2`:

> When the entire range has leverage above `1/16` but the three large spectral directions are delocalized, either produce a source-valid physical component/conditioning decomposition with a uniform determinant payment, or carry the regularized determinant through high-leverage coordinate removal while paying the removed determinant by a localized product-preserving smoothing inequality.

The fresh fleet01/B07 identity

`D_{I\{i}}(t)=D_I(t)(1-d_i(t))`

shows exactly what such a stopping argument must pay: deleting a high-regularized-leverage physical coordinate loses the same determinant mass that supplies Fourier integrability. Merely selecting one good minor/cut is already refuted by the live correction set.

## 6. Exact computation used

The accompanying `check.py` is a symbolic/numeric verification of the threshold algebra and the partner-family constants. Its recorded output is in `check_output.txt`. The calculation verifies

- `alpha(1/16)=7/16-sqrt(2)/4`;
- the exact leverage gap to `q/2=149/200` is positive;
- the simple `1/16` density constant is `2813.67835196808...`;
- `delta_*=39/98-3sqrt(30)/49`;
- the `3/50,q=4/3` constant is `160.075153671890...`;
- the twelve-block partner family has selected row leverage `1/16`, full-range leverage `5/16`, `mu=1/12`, and partner bound `24`.

These finite algebra checks support constants only; they are not proof of the analytic source theorem.

## 7. Status and integrity

**Outcome:** `ESSENTIAL_STEP_APPLIED`.

New proved/source-dependent implication: the complete full-spectrum diffuse-range argument extends from the clean source threshold `1/32` to the universal clean threshold `1/16` by using the source theorem's fractional exponent, with explicit constant `<2814`; more generally the two-part-MSS/three-direction mechanism reaches every fixed `delta<delta_*`.

Named partner result actually applied: fleet03/B08 `QFORM-DIFFUSE-BLOCK-REMAINDER-v1`, yielding the explicit bound `24` on the twelve-block dense-remainder family above.

**Not proved:** an exhaustive heavy/light reduction, arbitrary dense residual with heavy full-range coordinates, or the full conjecture. No pointwise scalar Fresnel decay, arbitrary fiber supremum, post-rotation independence, transformed conditional density cap, or single-cross-minor shortcut is used.

Changed-file review is limited to this run's new report/check files plus its worker-owned brain handoff/memory/status files. The available connector exposes no repository-side secret scanner; a manual fallback review found no credentials, scheduler identifiers, machine paths, private personal material, benchmark data, or external-release content.
