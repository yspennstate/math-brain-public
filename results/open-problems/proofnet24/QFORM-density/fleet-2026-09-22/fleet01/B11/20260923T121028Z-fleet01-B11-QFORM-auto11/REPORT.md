SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T12:10:28Z.
attacking: an exhaustive exact-rank-three diffuse-residual versus finite-heavy-coordinate reduction, using the spectral-window theorem before reciprocal physical-minor payment.

# fleet01/B11 — diffuse residual or finite heavy carrier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T121028Z-fleet01-B11-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** continuous density is proved in the diffuse-residual branch; the complementary finite-heavy branch remains open.

## 1. Exact scope and dependencies

The target remains the unrestricted cap-one product-law conjecture. This report proves a dimension-free reduction for **exact rank three**. It applies to both indefinite signatures `(2,1)` and `(1,2)` (in fact to every exact-rank-three inertia), but it does not yet pay the complementary finite-heavy branch and it does not handle arbitrary extra nonseparable spectrum.

The only non-elementary project dependency used in the proof is the completed spectral-window theorem:

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

path

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

Its stated scope is: if a symmetric matrix has at least three eigenvalues of modulus at least one, and if the spectral projection `P` onto all eigenspaces with `|lambda|>=1/64` satisfies `max_i P_ii<=1/32`, then the full quadratic form, even with arbitrary coordinate-separable measurable additions, has a continuous `C_0` density with

`||p||_infinity <= C_sw := 288 sqrt(3e)/13 <64`.             (1.1)

The proof there supplies a uniform integrable characteristic-function envelope, so conditioning on disjoint original coordinates and then averaging preserves the continuity conclusion as well as the sup bound.

Current corrections consumed here include: no independence after rotation; no law-uniform pointwise van-der-Corput decay; no dimension-free naive fibre supremum; no universal good physical triple; and no replacement of product provenance by an arbitrary bounded joint density. None of those false interfaces is used below.

## 2. Exact-rank-three frame notation

Let

`A = R M R^T`,                                                  (2.1)

where `R` is `n x 3`, `R^T R=I_3`, and `M` is real symmetric and invertible. Assume

`min_j |lambda_j(M)| >= s >0`.                                 (2.2)

Write the `i`-th row of `R` as `r_i^T` and define its spectral leverage

`c_i=||r_i||_2^2`.                                              (2.3)

Parseval gives the exact identities

`sum_i r_i r_i^T = I_3`,   `sum_i c_i =3`.                    (2.4)

For a set of original coordinates `D`, put

`G_D = R_D^T R_D = sum_(i in D) r_i r_i^T`.                    (2.5)

The matrix `G_D` keeps the product-law provenance explicit: no spectral-coordinate independence is claimed.

## 3. Main structural theorem

### Theorem 3.1 — `QFORM-RANK3-HEAVY-OR-DIFFUSE-RESIDUAL-v1`

Fix `0<alpha<1` and define

`tau=alpha/32`,
`D={i: c_i<=tau}`,
`H={i: c_i>tau}`.                                               (3.1)

For arbitrary independent real inputs with densities bounded by one, exactly one of the following useful alternatives holds.

**Diffuse-residual exit.** If

`G_D >= alpha I_3`,                                             (3.2)

then `Q=X^TAX` has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <= C_sw/(alpha s)
       = [288 sqrt(3e)/(13 alpha s)].`                          (3.3)

**Finite-heavy carrier.** If (3.2) fails, then there is a unit vector `v in R^3` such that

`boxed: sum_(i in H) (r_i dot v)^2 > 1-alpha`,                 (3.4)

while

`boxed: |H| < 96/alpha.`                                       (3.5)

Thus failure of the continuous diffuse exit forces more than `1-alpha` of one spectral direction onto a dimension-free number of original coordinates.

For the convenient choice `alpha=1/2`, either

`boxed: ||p_Q||_infinity <126.529/s`                            (3.6)

with a continuous `C_0` density, or fewer than `192` original coordinates carry more than half of some spectral direction.

### Proof

Assume first (3.2). Since `G_D` is positive definite, define

`U_D = R_D G_D^(-1/2)`.                                        (3.7)

Then `U_D^T U_D=I_3`, and the residual principal matrix factors as

`A_DD = U_D [G_D^(1/2) M G_D^(1/2)] U_D^T`.                   (3.8)

Hence its three nonzero eigenvalues are precisely those of the symmetric matrix

`M_D=G_D^(1/2) M G_D^(1/2)`.                                  (3.9)

For every vector `x`, using (2.2) and `G_D>=alpha I`,

`||M_D x||
 >= sqrt(alpha) ||M G_D^(1/2)x||
 >= sqrt(alpha) s ||G_D^(1/2)x||
 >= alpha s ||x||`.                                            (3.10)

Because `M_D` is symmetric, (3.10) says every nonzero eigenvalue of `A_DD` has modulus at least `alpha s`.

The orthogonal projection onto the range of `A_DD` is

`P_D = U_D U_D^T = R_D G_D^(-1) R_D^T`.                        (3.11)

For every `i in D`,

`(P_D)_ii = r_i^T G_D^(-1) r_i
 <= alpha^(-1)||r_i||^2
 <= tau/alpha
 =1/32`.                                                       (3.12)

Now condition on the original coordinates `X_H`. Independence is genuine because `D` and `H` are disjoint original-coordinate sets. For a fixed value `x_H`,

`Q = X_D^T A_DD X_D + 2(A_DH x_H)^T X_D + const(x_H)`.        (3.13)

Divide (3.13) by `alpha s`. The quadratic matrix has three eigenvalues of modulus at least one, and since it has exact rank three its spectral projection onto `|lambda|>=1/64` is exactly `P_D`. Equation (3.12) therefore verifies the spectral-window leverage gate. The induced linear term in (3.13) is coordinate-separable, so the spectral-window theorem applies at its stated scope and yields, uniformly in `x_H`,

`||p_(Q|X_H=x_H)||_infinity <= C_sw/(alpha s)`.               (3.14)

Averaging the conditional laws proves (3.3). The source theorem is proved by a conditioning-uniform integrable characteristic-function envelope; averaging that same envelope over `X_H` gives an integrable envelope for the unconditional characteristic function. Fourier inversion therefore supplies the continuous `C_0` representative claimed in the diffuse branch.

Suppose instead (3.2) fails. Then some unit vector `v` satisfies

`v^T G_D v < alpha`.                                          (3.15)

Using Parseval (2.4),

`1 = sum_i (r_i dot v)^2
   = sum_(i in D)(r_i dot v)^2 + sum_(i in H)(r_i dot v)^2`,   (3.16)

so (3.15) gives (3.4). Finally every `i in H` has `c_i>tau`, while `sum_i c_i=3`; hence

`|H| tau <3`,

which is exactly (3.5). This proves the theorem. QED.

## 4. Why this is useful for the indefinite signatures

Earlier B11 branches paid a quantitatively good original-coordinate indefinite pair, disjoint three-bank reductions, exact/null-ray bank endpoints, and diffuse ridge/volume configurations. The obstruction was that distributed frames may make every local reciprocal minor expensive.

Theorem 3.1 avoids choosing a physical pair or triple at the outset. It first removes all high-leverage original coordinates and asks whether the **entire residual three-dimensional spectral frame** remains nondegenerate. If it does, the spectral-window theorem pays the form continuously without any reciprocal minor. If it does not, the failure is not diffuse: one spectral direction is quantitatively carried by fewer than `96/alpha` original coordinates. Thus the next indefinite-signature step can be confined to a finite heavy carrier while all light rows remain present, instead of searching over arbitrary `n` for one good pair.

For `alpha=1/2`, the hard branch has fewer than 192 heavy coordinates. This is dimension-free but is not yet itself a density theorem; no bounded-support, moment, or deletion assumption is made for the light coordinates.

## 5. Designated partner application at an actual inequality

The newest completed `fleet02/B11` result is

`yspennstate/math-open-problems@f4772f0391b0088ff7698500b0d3c0b0e4a9c9c8`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260923T114511Z-fleet02-B11-QFORM-r30/REPORT.md`.

For

`Q_c = X_1^2 + (c/2)(X_2+X_3)^2 + 2(X_2+X_3)X_4`, `|c|<=1`,  (5.1)

it proves by product-preserving grouping that the original four-dimensional matrix has three eigenvalues of modulus at least one and

`boxed: ||p_(Q_c)||_infinity
 <= 24 sqrt(pi)/(sqrt(17)-1)
 <13.621.`                                                     (5.2)

Apply (5.2) to an arbitrary independent direct-sum tail. If `Z` consists of any further original coordinates independent of `X_1,...,X_4` and `S=S(Z)` is any almost surely finite measurable random variable (in particular any quadratic form on those disjoint coordinates), then

`p_(Q_c+S) = p_(Q_c) * law(S)`                                 (5.3)

in the measure-convolution sense, and Young's endpoint inequality gives the actual extension

`boxed: ||p_(Q_c+S)||_infinity <13.621.`                       (5.4)

No condition at all is imposed on the distribution of `S`; the only essential condition is that it is built from disjoint original coordinates so that it is independent of `Q_c`. This does **not** cover cross-coupled tails, and no such claim is made.

## 6. Rank-two logarithmic control and the third direction

The partner family retains the required rank-two obstruction exactly. At `c=0`, set

`Y=X_2+X_3`

for centered unit-uniform `X_2,X_3`, and let `X_4` be another centered unit uniform. The triangular density of `Y` gives

`p_(2Y X_4)(t)=log(1/|t|)-1+|t|`, `0<|t|<1`.                 (6.1)

Thus the opposite-sign rank-two receiver is genuinely logarithmically unbounded. The third direction `X_1^2` does not make (6.1) bounded by itself; it supplies a half-order smoothing kernel. Equivalently, its small-ball mass is `O(sqrt(rho))`, and the layer-cake integral of the logarithmic critical-value envelope is finite. This is the precise local mechanism by which the third direction removes the saddle singularity in this product-preserving realization.

Theorem 3.1 gives a complementary global mechanism: when the three-dimensional residual spectral frame stays diffuse after deleting high-leverage coordinates, three cross directions are present at one ridge scale and yield an integrable Fourier envelope. If that mechanism fails, the geometry is forced into a finite heavy carrier rather than an uncontrolled high-dimensional diffuse configuration.

## 7. First unpaid implication

The full conjecture remains open. The first B11 debt is now

**`QFORM-INDEFINITE-FINITE-HEAVY-DIRECTION-COMPILER-v1`.** In the finite-heavy branch of Theorem 3.1, use the fact that fewer than `96/alpha` original coordinates carry more than `1-alpha` of some spectral direction to force, without deleting the light rows, one of the already-paid mechanisms: a quantitatively good indefinite physical pair, a product-preserving grouped/null-sum bank, a ridge/volume exit, or a ruled/half-Riesz exit. The argument must remain uniform as the heavy direction approaches a Lorentz-null direction and must retain arbitrary within-light-bank cross couplings.

Arbitrary additional nonseparable spectrum is still a separate bridge to the unrestricted full target. A full candidate also needs all signs/degenerate cases and two independent end-to-end reviews.

## 8. Checks

A deterministic numerical sanity check generated random Parseval frames and random `(2,1)` spectral matrices. Whenever `G_D>=alpha I`, it verified

`min |eig(G_D^(1/2) M G_D^(1/2))| >= alpha s`

and

`max_i diag(R_D G_D^(-1) R_D^T) <=1/32`

for the stated threshold `tau=alpha/32`. The check is only regression evidence; the universal identities and inequalities are proved analytically above.

Numerical constants:

`C_sw = 63.26405187778285...`,
`2 C_sw =126.5281037555657...`,
`24 sqrt(pi)/(sqrt(17)-1)=13.6207024420826...`.
