# account01/B15 — mixed localized/diffuse obstruction to the two-branch bridge, with a universal continuous-density bound for the witness family

**Run:** `20260922T130222Z-account01-B15-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** `Absolute continuity and regularity`  
**Classification:** `ESSENTIAL_STEP_APPLIED / STRUCTURAL_BRIDGE_REFUTED`; full universal QFORM conjecture remains `OPEN`.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Current target and sources actually applied

The live target is: for every dimension `n`, every independent real `X_i` with densities `f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal interval bound

`P(X^T A X in [t,t+h]) <= C h`

with one finite `C` independent of `n`, the input laws and `A`.

This run uses the following completed peer result substantively, not just as background:

- `account02/B15`, scientific source `yspennstate/math-open-problems@60e7f51716e67553ce759519f9801ff3674dcce9`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T120155Z-account02-B15-qform-r1/REPORT.md`. It proves that every fixed rank-`>=3` symmetric matrix has an `L^infinity` density certificate through an invertible principal `3x3` or `4x4` block, with constants `C_3=2*pi+3*sqrt(3)` and `C_4=4*pi+8`, but the certificate may deteriorate through the smallest singular value of that block. I apply that theorem below to the exact family `A_m` and compute its loss to be linear in `m`.

I also use the independently checked diffuse/separable-phase theorem summarized at brain commit `783e9f753b93f8ba23d9358c12d0d2b44feb8478`: its rank-three mechanism needs either an unconditioned diffuse frame or a nonsingular residual whitening. The family below lies at the endpoint where one leverage equals one, so the rank-three whitened residual determinant is zero.

For one-dimensional linear projections I use the published marginal-density theorem of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949: if the coordinates are independent with densities bounded by one, every one-dimensional orthogonal projection has density bounded by `sqrt(2)`.

Fresh correction dependencies consumed before this write include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, and `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE`. None is contradicted or bypassed here.

## 2. A universal continuous-density theorem for disjoint spectral supports

### Theorem 2.1 — `QFORM-DISJOINT-SPECTRAL-SUPPORT-v1`

Let

`A = lambda_1 r_1 r_1^T + lambda_2 r_2 r_2^T + lambda_3 r_3 r_3^T`

where `r_1,r_2,r_3` are orthonormal, their physical-coordinate supports are pairwise disjoint, and `|lambda_j|>=1`. Let the physical coordinates `X_i` be independent with one-dimensional densities bounded by one. Then `Q=X^TAX` has a bounded continuous density satisfying

`||p_Q||_infinity <= 2*pi`.

If one of a same-sign spectral pair is a single physical coordinate, the bound improves to `pi*sqrt(2)`.

### Proof

Put `Z_j=<r_j,X>`. Pairwise disjoint physical supports and physical-coordinate independence imply that `Z_1,Z_2,Z_3` are independent. The one-dimensional marginal-density theorem gives

`||p_{Z_j}||_infinity <= sqrt(2)`.

Among three real nonzero `lambda_j`, two have the same sign. Relabel them `lambda_1,lambda_2`. Reflect the output if necessary, so these two coefficients are positive.

For a real variable `Z` with density bounded by `M` and `lambda>0`, the density of `Y=lambda Z^2` is, for `y>0`,

`p_Y(y)=[p_Z(sqrt(y/lambda))+p_Z(-sqrt(y/lambda))]/(2 sqrt(lambda y))`

and hence

`p_Y(y) <= M / sqrt(lambda y)`.

Therefore, since `Y_1=lambda_1 Z_1^2` and `Y_2=lambda_2 Z_2^2` are independent,

`p_{Y_1+Y_2}(s)`
`<= (M_1 M_2 / sqrt(lambda_1 lambda_2)) * integral_0^s [u(s-u)]^(-1/2) du`
`= pi M_1 M_2 / sqrt(lambda_1 lambda_2)`
`<= 2*pi`.

The third spectral term is independent of the first two. Convolution with its probability law cannot increase an `L^infinity` norm, so `||p_Q||_infinity<=2*pi`.

Each square-law density is in `L^1`; convolution of two `L^1(R)` functions is continuous and vanishes at infinity. Convolving that `C_0` density with the third probability density preserves continuity. Thus the displayed bounded density has a continuous representative.

If one variable in the same-sign pair is literally one physical coordinate, its density cap is `1` rather than `sqrt(2)`, giving `pi*sqrt(2)`. QED.

This theorem is a genuine rotated, non-diagonal family: each `r_j` may be spread over arbitrarily many physical coordinates inside its own support block.

## 3. Exact mixed-leverage family that kills the proposed local/cross-block dichotomy

For any integer `m>=2`, set `n=2m+1` and define

`e_0=(1,0,...,0)`,

`u_m = m^(-1/2) sum_{i=1}^m e_i`,

`v_m = m^(-1/2) sum_{i=m+1}^{2m} e_i`,

and

`A_m = e_0 e_0^T + u_m u_m^T - v_m v_m^T`.

The three displayed vectors are orthonormal, so the nonzero spectrum is exactly `{1,1,-1}`. Thus every `A_m` satisfies the full target spectral hypothesis.

### 3.1 Principal `3/4` blocks are never uniformly good

If a principal set `J` omits coordinate `0`, then `(A_m)_{J,J}` is the sum of at most two rank-one blocks and has rank at most two. Hence every principal `3x3` or `4x4` block omitting `0` is singular.

If `0 in J`, then the block is the direct sum of `[1]`, a positive all-ones block scaled by `1/m` on selected indices from the first diffuse group, and a negative all-ones block scaled by `1/m` on selected indices from the second diffuse group.

For `|J|=3`, invertibility occurs exactly when `J` contains `0`, one coordinate from the `u_m` group and one from the `v_m` group. In that case the block is permutation-equivalent to

`diag(1,1/m,-1/m)`,

so its least singular value is exactly `1/m`.

For `|J|=4`, after removing the `[1]` coordinate the remaining `3x3` block has rank at most two, hence every such `4x4` principal block is singular.

Consequently the principal-pivot quantity of account02/B15 satisfies exactly

`kappa_*(A_m)=1/m`.

Applying the partner theorem therefore gives only

`||p_{X^T A_m X}||_infinity <= C_3 m`,

with `C_3=2*pi+3*sqrt(3)`, even though the true family is uniformly controlled below. This is an explicit application of the partner theorem and an exact diagnosis of where its matrix-dependent loss occurs.

### 3.2 Every original-coordinate cross block has rank at most two

For any cut `S | S^c`, the cross block of `e_0e_0^T` is identically zero. The cross block of `u_mu_m^T` has rank at most one, and the cross block of `v_mv_m^T` has rank at most one. Therefore

`rank((A_m)_{S,S^c}) <= 2`

for every physical-coordinate cut, for every `m`.

Hence no branch requiring an original-coordinate cross block of rank at least three can apply to this family, regardless of determinant threshold.

### 3.3 The full density is nevertheless uniformly bounded and continuous

The quadratic form is exactly

`Q_m = X_0^2 + (m^(-1/2) sum_{i=1}^m X_i)^2 - (m^(-1/2) sum_{i=m+1}^{2m} X_i)^2`.

The three summands depend on disjoint physical-coordinate groups and are independent. Theorem 2.1 applies, and because `X_0` itself has density cap one while the positive diffuse projection has density cap at most `sqrt(2)`,

`||p_{Q_m}||_infinity <= pi*sqrt(2)`

for every `m`, with a continuous representative.

Thus the linear-in-`m` principal-pivot certificate is entirely a mechanism loss on this family, not target-level evidence.

## 4. Decisive consequence

The concrete bridge proposed in the previous account02/B15 report was:

- either a principal `3/4` block has least singular value at least a universal `c>0`,
- or an original-coordinate cut has a cross block carrying three singular directions with determinant product at least a universal `c>0`.

The family `A_m` refutes this bridge for every positive universal `c`: its best invertible principal `3/4` block has least singular value `1/m ->0`, while every cross block has rank at most two.

This does **not** refute the owner conjecture. In fact the same family satisfies the stronger continuous-density estimate `||p||_infinity<=pi*sqrt(2)`. What it refutes is the sufficiency of a two-branch proof architecture using only a uniformly good small principal pivot or rank-three cross-block smoothing.

## 5. New first unpaid implication

A third, genuinely mixed localized/diffuse mechanism is necessary. The simplest target is:

> `QFORM-RANK1-PLUS-RANK2-MIXED-v1`: obtain a dimension-free interval bound when one spectral direction is physically localized (or nearly localized) and the remaining two large directions are diffuse, without requiring a rank-three cross block and without paying the vanishing residual-whitening determinant.

The endpoint `A_m` is solved here because the three spectral directions use disjoint physical supports. The unresolved step is to retain this payment when the localized direction and the two diffuse directions overlap weakly or strongly in physical coordinates, while preserving the original product law. This is exactly where the recent corrections warn against replacing physical independence by conditional density caps.

A plausible analytic formulation is to seek a rank-two logarithmic small-ball estimate for the residual diffuse quadratic component and combine it with the square-root smoothing supplied by the localized direction, but any proof must retain the actual shared-coordinate dependence rather than treating the pieces as independent.

## 6. Status

**Full QFORM:** `OPEN -> OPEN`.  
**New proved claim:** `QFORM-DISJOINT-SPECTRAL-SUPPORT-v1`, bounded continuous density with universal constant `2*pi` (and `pi*sqrt(2)` for the explicit witness family).  
**Refuted intermediate bridge:** universal `good principal 3/4 block OR rank>=3 physical cross block` dichotomy.  
**Next recipient:** synthesis/rank-three workers, especially the rank-three coupled branch and proof assembly.

No schedule, notification, email, permission, public-release or cross-account authentication changes are made in this run.
