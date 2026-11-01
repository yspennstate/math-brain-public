# fleet02/B08 — whitened physical-block hybrid for diffuse eigenvectors

**Run:** `B08-20260922T124007Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Diffuse eigenvector case`  
**Classification:** `ESSENTIAL_STEP_APPLIED / QFORM-WHITENED-PHYSICAL-BLOCK-v1`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full conjecture:** **OPEN / NOT PROVED / NOT DISPROVED**.

## 0. Fresh sources, corrections, and exact scope

The live target is the universal bounded-density conjecture for `Q=X^T A X` with independent real inputs having densities `0<=f_i<=1` and at least three eigenvalues of `A` of absolute value at least `1`.


Required route corrections were consumed: law-uniform pointwise one-dimensional Fresnel decay is false; unrestricted spectral-fiber suprema can lose dimension; diagonalizing `A` destroys the original coordinate independence. The live correction inbox at `defae9228f184bc5ea8495a040773b578e39e374` also records `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, and `QFORM-TWOSHEET-XRAY-ONLY-FALSE`. None is contradicted below. In particular, no universal `C=pi` claim is made.

Completed sources actually used:

1. `fleet03/B08`, report `yspennstate/math-open-problems@9dcddd0bf3fbcb8e0b3396e0a4d883924d3f4ada`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T114830Z-fleet03-B08-qform-diffuse-v1/REPORT.md`, blob `022e24d4e6470665c48d7bfb1a3ad5c7963f664a`. Its Corollary 4 is the conditional/whitened diffuse estimate.
2. Interactive supporting theorem `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, `yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb`, path `proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`, blob `d08d2488c072386e2b8ad818e30b1a6dec79e63a`.
3. `fleet02/B15`, localized principal-triple theorem, `yspennstate/math-open-problems@d5392d73398e2811f58b612fb8f191aa79d8ee5e`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`, blob `1da4167bbf6b2785659bd50007cab5f04b9c3084`.
4. This slot's preceding diffuse theorem `QFORM-DIFFUSE-RANK3-BL-v1`, `yspennstate/math-open-problems@0b5925a458d36c1ec1cf8ab344c9676260a97c8a`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T113624Z-qform11/REPORT.md`, blob `212febc02c4c1f3a8e6c073d0a8ed5d2d6b4ea0a`.

No moment, support, continuity, identical-law, centering, sign, or post-rotation independence assumption is added.

## 1. First unpaid implication, attacked immediately

For a general target matrix, selecting three diffuse large eigenvectors gives

`A = U Lambda U^T + C`, with `C U = 0`,

but `X^T C X` is generally an off-diagonal quadratic phase in the original independent coordinates. The reviewed separable-phase theorem only absorbs phases of the form `sum_i V_i(X_i)`. Therefore the first unpaid implication remains:

`QFORM-DIFFUSE-OFFDIAGONAL-REMAINDER-v1` — control the arbitrary nonseparable residual `X^T C X` while retaining the product law.

The contribution below does not pretend to solve that generic residual. Instead it closes a strictly larger product-preserving hybrid class: after conditioning localized physical coordinates, the surviving principal block may have a **non-orthonormal** diffuse rank-r component, arbitrary diagonal terms, and arbitrary couplings to all conditioned coordinates.

## 2. Independent review of `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`

**Review outcome:** `REVIEW_PASS_SCOPED`; no defect found in the stated theorem. This is an independent review of the supporting theorem, not a review or proof of the full conjecture.

The critical points check as follows.

### 2.1 Complex amplitudes preserve the exact input norms

For fixed `t`, put

`h_{i,t}(x)=f_i(x) exp(i t V_i(x))`.

Then `|h_{i,t}|=f_i`, hence for every `1<=p<=infinity`,

`||h_{i,t}||_p=||f_i||_p<=1`,

and `||h_{i,t}||_1=1`. Sharp Hausdorff-Young is valid for complex functions, so the Brascamp-Lieb/Hausdorff-Young step is unchanged by the phases.

### 2.2 The t-dependent projected complex density is legitimate

Complete the orthonormal-column matrix `U` to an orthogonal matrix `(U,W)`. The pushforward of the complex product density `prod_i h_{i,t}(x_i)` by `x -> U^T x` has density

`g_t(y)=int prod_i h_{i,t}((Uy+Wz)_i) dz`.

Tonelli applied to the absolute value gives

`||g_t||_1 <= int prod_i f_i(x_i) dx = 1`.

Its Fourier transform is exactly

`hat g_t(xi)=prod_i hat h_{i,t}(u_i dot xi)`.

No independence of the rotated coordinates is asserted.

### 2.3 Gaussian-regularized inversion is dominated correctly

The source proof inserts `exp(-epsilon |y|^2)` in physical y-space. Because `g_t in L^1` and the Brascamp-Lieb step gives `hat g_t in L^1`, Fourier inversion and Fubini are valid for the regularized integral. The complex Gaussian kernel has modulus bounded uniformly by

`pi^(r/2) |t|^(-r/2) |det Lambda|^(-1/2)`.

Dominated convergence as `epsilon downarrow 0` uses `|g_t| in L^1`; it does not require positivity of `g_t`. The separate trivial bound `|phi_T(t)|<=1` comes from the actual probability law of `T`.

### 2.4 Principal-block conditioning retains continuity

Conditioning on outside original coordinates leaves the inside variables independent with the same one-dimensional densities. Cross-block terms become coordinatewise linear potentials. The conditional characteristic functions obey the same integrable envelope uniformly in the conditioning value, so averaging preserves an `L^1(dt)` characteristic function bound. Hence the unconditional law has a bounded continuous density. No division by a conditional probability and no hidden normalization occurs.

Thus the separable-phase/principal-block extension is valid in its stated scope.

## 3. New theorem: whitened physical-block certificate

### Theorem 3.1 — `QFORM-WHITENED-PHYSICAL-BLOCK-v1`

Let `X_1,...,X_n` be independent real variables with densities `0<=f_i<=1`. Let `A` be any real symmetric `n x n` matrix. Suppose there is a set of original coordinates `I` such that its principal block has a decomposition

`A_{I,I} = D + R Lambda R^T`,

where

- `D` is diagonal on `I`;
- `R` is an `|I| x r` real matrix of full column rank, `r>=3`;
- `Lambda` is real symmetric and invertible.

Put

`M=R^T R`, `W=R M^(-1/2)`.

Then `W^T W=I_r`. Write `w_i^T` for the rows of `W`, `d_i=||w_i||^2`, and assume

`max_i d_i <= 1/2`.

Define

`B(W)=prod_{d_i>0} (1-d_i)^(-(1-d_i)/2)`.

Then the full quadratic form `Q=X^T A X` has a bounded continuous density and

`||p_Q||_infinity <= [r/(r-2)] B(W)^(2/r) [det(M) |det Lambda|]^(-1/r)`.

In particular, since `B(W)<=exp(r/2)`, one has the simpler bound

`||p_Q||_infinity <= [e r/(r-2)] [det(M) |det Lambda|]^(-1/r)`.

No restriction is imposed on `A_{I,I^c}` or `A_{I^c,I^c}`.

### Proof

Condition on `X_{I^c}=z`. The conditional polynomial in the original independent coordinates `x_I` is

`x_I^T A_{I,I} x_I + 2 x_I^T A_{I,I^c} z + const(z)`.

Because `R=W M^(1/2)`,

`R Lambda R^T = W B W^T`,

where

`B=M^(1/2) Lambda M^(1/2)`.

Therefore the conditional polynomial equals

`(W^T x_I)^T B (W^T x_I) + sum_{i in I} V_{i,z}(x_i) + const(z)`,

with

`V_{i,z}(x)=D_{ii} x^2 + 2 (A_{I,I^c} z)_i x`.

The independently reviewed separable-phase theorem applies because `W` has orthonormal columns and every row leverage is at most `1/2`. Its exact bound is uniform in the arbitrary measurable coordinatewise potentials `V_{i,z}`. Moreover

`|det B| = det(M) |det Lambda|`.

Thus every conditional characteristic function satisfies the same integrable envelope

`min(1, K |t|^(-r/2))`

with `K` depending only on `W`, `M`, and `Lambda`, not on `z`. Averaging the conditional characteristic functions preserves that envelope. Fourier inversion gives the claimed bounded continuous density and the displayed constant. `QED`.

### Why this is a genuine extension

The source separable-phase theorem is stated for an orthonormal-column low-rank component inside the physical block. The source partner theorem supplies the whitening mechanism after conditioning. Theorem 3.1 combines them: the physical principal block may contain an arbitrary full-rank `R`, and all outside/cross couplings are unrestricted. The determinant penalty is exactly the retained spectral-volume factor `det(R^T R)`.

## 4. One-localized-coordinate heavy/light corollary

Let `U in R^{n x 3}` have orthonormal columns, with rows `u_i^T`, and let

`A = D + U Lambda U^T`

with `D` diagonal and `Lambda` real symmetric invertible. Fix a coordinate `h` and put

`c=||u_h||^2 < 1`, `L=[n]\{h}`.

Then

`M=U_L^T U_L = I-u_h u_h^T`,

so by the matrix determinant lemma

`det M = 1-c`.

For every residual row `u_i`, Sherman-Morrison gives its whitened leverage exactly as

`ell_i = u_i^T M^(-1) u_i = ||u_i||^2 + (u_i dot u_h)^2/(1-c)`.

Hence if

`max_{i != h} ell_i <= 1/2`,

Theorem 3.1 gives

`||p_Q||_infinity <= 3 B(W)^(2/3) [(1-c)|det Lambda|]^(-1/3)
                 <= 3e [(1-c)|det Lambda|]^(-1/3)`.

A simple raw-leverage sufficient condition is

`max_{i != h} ||u_i||^2 <= (1-c)/2`,

because Cauchy-Schwarz gives `(u_i dot u_h)^2<=c ||u_i||^2`, hence

`ell_i <= ||u_i||^2/(1-c) <=1/2`.

This is a real heavy/light extension of the previous global diffuse theorem: the conditioned row may have leverage strictly larger than `1/2`.

## 5. Explicit mixed family not closed by either previous extreme certificate

Fix `c in (1/2,1)` and an integer `m>=2`. Let `U` have `1+3m` rows in `R^3`:

- one row `sqrt(c) e_1`;
- `m` rows `sqrt((1-c)/m) e_1`;
- `m` rows `m^(-1/2) e_2`;
- `m` rows `m^(-1/2) e_3`.

Then `U^T U=I_3`. The global maximum row leverage is `c>1/2`, so the preceding unconditioned diffuse theorem does not apply.

Condition on the single heavy coordinate. The residual covariance is

`M=diag(1-c,1,1)`.

After whitening, every one of the remaining `3m` rows has leverage exactly `1/m<=1/2`. Therefore, for arbitrary independent input densities bounded by `1` and arbitrary diagonal `D`,

`Q=X^T(D+U Lambda U^T)X`

has a bounded continuous density with the exact estimate

`||p_Q||_infinity
 <= 3 (1-1/m)^(-(m-1)) [(1-c)|det Lambda|]^(-1/3)`.

Indeed here

`B(W)=(1-1/m)^(-3(m-1)/2)`.

If all three eigenvalues represented by `Lambda` have magnitude at least `1`, then

`||p_Q||_infinity <= 3e (1-c)^(-1/3)`.

For example `c=3/4` gives a bound independent of `m`.

Now set `D=0` and `Lambda=diag(1,1,-1)`. Any physical `3 x 3` principal block that does not select one row from each of the three coordinate directions is singular. A spanning triple has two diagonal magnitudes equal to `1/m`, hence

`max_{|I|=3} sigma_min(A_{I,I}) <= 1/m`.

Thus the localized principal-triple theorem alone yields a bound growing like `m`, while the new one-heavy/diffuse-tail certificate is dimension-free in `m`. This family is also outside the unconditioned leverage-`<=1/2` theorem. It therefore occupies a genuine intermediate heavy/light region rather than merely restating either extreme branch.

## 6. Exact partner application

The named partner result `fleet03/B08` is applied, not merely cited. Its conditional whitening formula uses

`M=U_L^T U_L`, `W=U_L M^(-1/2)`

and gives a conditional/unconditional bound with determinant factor `det(M)^(-1/3)`. In the explicit family above this becomes

`det(M)^(-1/3)=(1-c)^(-1/3)`,

while the reviewed exact `B(W)` factor evaluates to

`B(W)^(2/3)=(1-1/m)^(-(m-1))`.

This yields the displayed quantitative inequality. No surrogate bistochastic, Gaussian-input, or post-rotation independence assumption is involved.

## 7. Remaining connection to the full target

The full conjecture remains open. The new theorem solves every matrix possessing a physical principal block whose non-diagonal part can be written as a sufficiently diffuse whitened rank-`r>=3` component plus a diagonal remainder, with a determinant-volume lower bound. It also handles arbitrary couplings to conditioned coordinates.

The first essential missing implication is now sharply structural:

`QFORM-DIFFUSE-NONSEPARABLE-PRINCIPAL-REMAINDER-v1` — starting from an arbitrary target matrix with three large eigenvalues, find a physical block for which the residual after extracting three large directions is diagonal/separable (or otherwise controllable) while `det(R^T R)|det Lambda|` stays uniformly positive; failing that, control a genuinely off-diagonal residual inside the surviving diffuse block without destroying the Fourier-Brascamp-Lieb product estimate.

The determinant factor shows exactly what is lost by conditioning. A future hybrid proof must pay small `det(R^T R)` using localized curvature rather than simply conditioning more coordinates until the bound diverges.

## 8. Status and integrity

**New proved supporting result:** `QFORM-WHITENED-PHYSICAL-BLOCK-v1` and its one-localized-coordinate heavy/light corollary.

**Independent review:** `QFORM-DIFFUSE-SEPARABLE-PHASE-v1` passes in its stated scope, including the complex-amplitude, Gaussian-regularization, and uniform conditioning steps.

**Full target:** OPEN.

No numerical computation was needed for the proof. No benchmark material, credentials, machine paths, email, paid call, remote workflow, public release, permission change, or unrelated private data is included. A narrow manual changed-file scope/secret review found only mathematical source pins and nonsecret Git object identifiers; no full repository privacy scanner was invoked in this run.
