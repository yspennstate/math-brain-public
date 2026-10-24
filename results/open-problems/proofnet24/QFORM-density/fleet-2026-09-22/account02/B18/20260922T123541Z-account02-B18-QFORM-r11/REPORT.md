# account02/B18 — literature-to-proof transfer: sharp 2D marginals and rank-three elliptic closure

**Run:** `20260922T123541Z-account02-B18-QFORM-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
**Assignment:** Literature-to-proof transfer / STRUCTURE  
**Status:** target-level structural subclass proved; full conjecture OPEN / NOT PROVED  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication and correction discipline

The target is unchanged: independent real coordinates `X_i` with densities bounded by 1, and a real symmetric matrix `A` with at least three eigenvalues satisfying `|lambda|>=1`; prove a dimension-independent bound on the density of `X^T A X`, or give a genuine counterexample.

The first unpaid implication after this run is now narrower in rank three:

> **QFORM-RANK3-LOCALIZED-INDEFINITE-v1.** Control a rank-exactly-three indefinite form when the selected spectral frame has a row leverage `>1/2` but no quantitatively useful minority-sign physical pivot; then extend beyond rank three without treating the remaining spectral coordinates as an independent remainder.

This report consumes the live corrections `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, and `QFORM-TWOSHEET-XRAY-ONLY-FALSE`. In particular, no orthogonal spectral rotation is followed by a false independence claim, no bare cross minor is treated as sufficient, and no arbitrary bounded projected density is substituted for product provenance in an indefinite quadratic form.

## 2. Primary literature transfer: the sharp product-marginal theorem

The primary source newly transferred here is:

Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, **On sharp bounds for marginal densities of product measures**, *Israel Journal of Mathematics* 216(2) (2016), 877–889, DOI `10.1007/s11856-016-1431-5`, arXiv `1507.07949`.

Their Theorem 1.1 states: if

`f(x)=prod_{i=1}^n f_i(x_i)`, `||f_i||_1=1`,

then for every `k`-dimensional subspace `E` there are `gamma_i in [0,1]`, `sum gamma_i=k`, such that

`||pi_E(f)||_infty <= min((n/(n-k))^((n-k)/2), 2^(k/2)) prod_i ||f_i||_infty^(gamma_i)`.

Therefore, under the present hypothesis `||f_i||_infty<=1`, every two-dimensional orthogonal projection of `X` has joint density bounded by

`2`.                                                                  (2.1)

This is exact source matching: independence and one-dimensional bounded densities are precisely the input hypotheses; there is no moment, support, centering, identical-distribution, log-concavity, or Gaussian assumption. Crucially, (2.1) is a **joint-density** statement only; it does not say the two projected coordinates are independent.

For comparison, Rudelson–Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, IMRN 2015(19), 9594–9617, DOI `10.1093/imrn/rnu243`, Theorem 1.1 gives `(C K)^k` with an unspecified absolute `C`; Livshyts–Paouris–Pivovarov supplies the sharp `2^(k/2)` form needed below.

## 3. Rank-two elliptic spectral transfer

### Theorem 3.1 — `QFORM-RANK2-ELLIPTIC-MARGINAL-v1`

Let `U` be an `n x 2` matrix with orthonormal columns, and let

`Lambda=diag(lambda_1,lambda_2)`, with `lambda_1 lambda_2>0`.

For independent `X_i` with densities bounded by 1, put

`T=(U^T X)^T Lambda (U^T X)`.

Then `T` has an essentially bounded density and

`||p_T||_infty <= 2 pi / sqrt(|lambda_1 lambda_2|)`.                    (3.1)

### Proof

Write `Y=U^T X`. By (2.1), `Y` has a joint density `g` on `R^2` satisfying `g<=2` almost everywhere. After changing the sign of `T` if necessary, take both eigenvalues positive and set

`V=(sqrt(lambda_1)Y_1, sqrt(lambda_2)Y_2)`.

The density of `V` is bounded by `2/sqrt(lambda_1 lambda_2)`. For `R=|V|^2`, the coarea formula in polar coordinates gives, for almost every `s>0`,

`p_R(s) = (1/2) int_0^(2pi) f_V(sqrt(s)(cos theta,sin theta)) dtheta`

and hence

`p_R(s) <= pi * 2/sqrt(lambda_1 lambda_2)`.

Reflection handles the negative-definite case. QED.

**What this closes.** A rank-two same-sign spectral quadratic form may be arbitrarily rotated relative to the physical coordinates; no independence of the rotated coordinates is needed. If such a form lives on one original-coordinate block and the rest of the quadratic form lives on a disjoint block, convolution preserves (3.1), giving a target-level block-separable bound `2pi` whenever `|lambda_1|,|lambda_2|>=1`.

## 4. Physical elliptic two-minor lemma

A complementary elementary certificate, useful with arbitrary outside couplings, is stronger when it applies.

### Lemma 4.1 — `QFORM-PHYSICAL-ELLIPTIC-2MINOR-v1`

If a physical `2 x 2` principal submatrix `B=A_{I,I}` is positive or negative definite, then

`||p_{X^T A X}||_infty <= pi/sqrt(det B)`,                             (4.1)

where `det B>0` in either definite case.

### Proof

Condition on all coordinates outside `I`. The conditional form is

`x^T B x + 2 ell^T x + c`.

After a translation in the two physical coordinates its conditional joint density is still a product of translated coordinate densities and is bounded by 1. For `C=+B` in the positive case and `C=-B` in the negative case,

`int_{R^2} delta(z^T C z-s) dz = pi/sqrt(det C)`

for every `s>0`, by the linear change `y=C^(1/2)z` and polar coordinates. Multiplication by a density bounded by 1 and then averaging the outside conditioning proves (4.1). QED.

No support or moment condition appears, and arbitrary cross-couplings to the conditioned coordinates are allowed.

## 5. Exact rank-three Schur identity

Let `A` now have rank exactly three, with nonzero eigen-decomposition

`A=U Lambda U^T`, `U^T U=I_3`, `Lambda=diag(lambda_1,lambda_2,lambda_3)`.

For a physical coordinate `i`, define its spectral leverage

`tau_i = ||U^T e_i||_2^2`

and physical pivot

`a_i=A_{ii}`.

Assume `a_i!=0`, write after permutation

`A=[[a_i,b^T],[b,C]]`, and let

`S_i=C-bb^T/a_i`.

Then `rank S_i=2`. If `mu_1,mu_2` are its two nonzero eigenvalues, the following exact identity holds:

`a_i mu_1 mu_2 = tau_i lambda_1 lambda_2 lambda_3`.                     (5.1)

### Proof

For every two-element set `J` not containing `i`, Schur complementation gives

`det A_{ {i} union J } = a_i det (S_i)_J`.

Summing over `J`, the right side is `a_i e_2(S_i)=a_i mu_1 mu_2` because `rank S_i=2`.

On the other hand,

`det A_K = det(Lambda) det(U_K)^2` for every three-element `K`.

For an orthonormal-column matrix `U`,

`sum_{K: i in K} det(U_K)^2 = tau_i`.                                  (5.2)

One proof of (5.2) differentiates Cauchy–Binet

`det(U^T D U)=sum_{|K|=3} det(U_K)^2 prod_{j in K} d_j`

with respect to `d_i` at `D=I`; the derivative of the left side is `e_i^T U U^T e_i=tau_i`. Summing the principal-minor identities proves (5.1). QED.

## 6. Elliptic Schur residual plus the physical pivot square

The previous B18 run proved the following conditional square-smoothing lemma: if `T` has density bounded by `K_T`, and conditional on `T=t` the variable `W` has density bounded by 1, then

`||p_{T+beta W^2}||_infty <= 2 sqrt(K_T/|beta|)`.                        (6.1)

Apply this to the physical square completion

`X^T A X = a_i [X_i + b^T X_{-i}/a_i]^2 + X_{-i}^T S_i X_{-i}`.         (6.2)

If `S_i` is positive or negative semidefinite of rank two, Theorem 3.1 gives

`K_T <= 2pi/sqrt(|mu_1 mu_2|)`.

The original pivot `X_i` is independent of `X_{-i}`; hence, conditional on `T=X_{-i}^T S_i X_{-i}`, the shifted variable in square brackets is a mixture of translations of `X_i` and still has density at most 1. Equations (6.1), (5.1) yield the source-exact bound

`||p_{X^T A X}||_infty`
` <= 2 sqrt(2pi) ( |a_i| tau_i |lambda_1 lambda_2 lambda_3| )^(-1/4)`.   (6.3)

This is `QFORM-RANK3-ELLIPTIC-SCHUR-v1`.

The condition `S_i` semidefinite is automatic in either of two situations:

1. all three nonzero eigenvalues of `A` have the same sign; or
2. `A` has signature `(2,1)` or `(1,2)` and `a_i` has the minority sign.

The second statement follows from inertia additivity under a nonzero scalar pivot.

## 7. Target-level closure: all rank-exactly-three one-sign forms

### Theorem 7.1 — `QFORM-RANK3-SEMIDEFINITE-v1`

Suppose `A` has rank exactly three, its three nonzero eigenvalues all have the same sign, and

`|lambda_j|>=1`, `j=1,2,3`.

For arbitrary independent coordinate densities bounded by 1,

`||p_{X^T A X}||_infty <= 3e`.                                         (7.1)

### Proof

Use the completed account03/B08 theorem `QFORM-DIFFUSE-SPECTRAL-FRAME-v1` when

`max_i tau_i <=1/2`.

That theorem applies to rank `r=3` with zero coordinatewise remainder and `|det Lambda|>=1`, giving exactly

`||p||_infty <= e*r/(r-2)=3e`.

Otherwise choose `i` with `tau_i>1/2`. Since all nonzero eigenvalues have one sign and magnitude at least 1,

`|a_i| = |sum_j lambda_j U_{ij}^2| >= tau_i`,

and `|lambda_1 lambda_2 lambda_3|>=1`. The Schur residual is rank-two semidefinite, so (6.3) gives

`||p||_infty <=2 sqrt(2pi) tau_i^(-1/2) <4 sqrt(pi) <3e`.

Thus (7.1) holds in both leverage regimes. QED.

Numerically, `4 sqrt(pi)=7.0898154036...` and `3e=8.1548454854...`; the theorem is analytic, not numerical.

This is a genuine target-level structural theorem: arbitrary independent densities bounded by 1, no hidden moments/support/centering, and no rotation-independence assumption.

## 8. Indefinite rank-three quantitative branch

For rank-exactly-three indefinite `A`, the diffuse branch `max tau_i<=1/2` is already covered by account03/B08 with the same `3e` bound. In the localized branch, if a physical pivot `a_i` has the minority inertia sign, then `S_i` is semidefinite and (6.3) applies. In particular, if

`|a_i| tau_i |lambda_1 lambda_2 lambda_3| >= delta>0`,

then

`||p||_infty <=2 sqrt(2pi) delta^(-1/4)`.                               (8.1)

What remains is precisely the localized indefinite geometry where high-leverage coordinates have majority-sign pivots, or every minority-sign pivot has arbitrarily small `|a_i| tau_i`; then the rank-two Schur residual is indefinite or the square-smoothing scale degenerates.

## 9. Assigned-partner application and elliptic/hyperbolic dictionary

The completed assigned partner account03/B18 run `20260922T120058Z-account03-B18-qform-r1` transferred Banks' non-Gaussian bilinear theorem and proved the source-valid physical-bipartite bound

`A=[[0,B],[B^T,0]]  =>  ||p_{X^T A X}||_infty <= 2 sqrt(e pi)/sqrt(sigma_1(B)sigma_2(B))`. (9.1)

Its late correction addendum explicitly keeps the required zero-within-side structure; a large cross minor alone is not sufficient.

The present theorem complements (9.1) rather than replacing it:

- **elliptic rank two:** arbitrary spectral orientation is safe because the sharp two-dimensional product marginal bound plus the constant ellipse-shell Jacobian gives (3.1);
- **hyperbolic rank two:** a bounded joint projected density is not enough. Even the physical product form `2XY` with independent uniform variables has a logarithmic density singularity at zero. Source-valid control therefore needs partner/Banks physical bipartite structure plus an additional singular direction, or the third-square mechanism from the preceding B18 report.

This is exactly where one must not infer independence after spectral rotation.

## 10. Source exclusions checked

Several nearby results do **not** transfer to the target and are not used as premises:

- Gaussian quadratic-form concentration results assume Gaussian inputs.
- Carbery–Wright style polynomial anti-concentration requires log-concavity in its standard continuous form and gives a weaker small-ball exponent rather than the required density bound here.
- Hanson–Wright bounds impose subgaussian/tail hypotheses absent from the target.
- General bounded joint density of a rotated projection is insufficient for an indefinite quadratic surface; the live two-sheet/X-ray correction already records this obstruction.

The Livshyts–Paouris–Pivovarov theorem is used only at the exact point where its hypotheses survive: an **unconditional joint marginal density bound** for a linear projection of the original product vector.

## 11. Full-target status and next step

**Full conjecture:** OPEN / NOT PROVED.

**New closure:** every rank-exactly-three same-sign form with `|lambda_j|>=1` has density at most `3e`; diffuse rank-three indefinite forms are also covered, and localized indefinite forms with a quantitatively nondegenerate minority pivot satisfy (8.1).

**Next mathematical implication:** prove a dimension-free smoothing inequality for the remaining localized rank-three indefinite Schur form that retains original product-projection provenance, or derive a structural pivot/partition forcing either the minority-pivot elliptic branch above or the assigned partner's genuine physical-bipartite branch. After that, control the extra-eigenvalue remainder for rank greater than three without treating spectral components as independent.

## 12. Source pins

- Livshyts–Paouris–Pivovarov: Israel J. Math. 216(2) (2016), 877–889; DOI `10.1007/s11856-016-1431-5`; arXiv `1507.07949`; Theorem 1.1, especially the `2^(k/2)` marginal bound.
- Rudelson–Vershynin: IMRN 2015(19), 9594–9617; DOI `10.1093/imrn/rnu243`; Theorems 1.1–1.2.
- account03/B18 completed partner scientific commit `53bf1a45bf46dfa09a963d95935f6413c911d1b5`, with late correction addendum scientific commit `43c76354f3fbba5301eb1993b79cbee523eb9737`.
- account03/B08 `QFORM-DIFFUSE-SPECTRAL-FRAME-v1`, scientific commit `9dcddd0bf3fbcb8e0b3396e0a4d883924d3f4ada`.
- preceding account02/B18 conditional square smoothing and joint bilinear-square report, scientific commit `43d49b06197ea4f07770f8dae426236ad074b684`.

No claim in this report has independent end-to-end review yet.
