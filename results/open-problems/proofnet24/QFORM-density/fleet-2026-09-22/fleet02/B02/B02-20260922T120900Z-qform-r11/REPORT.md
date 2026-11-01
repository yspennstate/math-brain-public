# fleet02/B02 — asymmetric cross-block integrated Fourier theorem

**Run:** `B02-20260922T120900Z-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Integrated Fourier estimate`, pathway `FOURIER`  
**Classification:** `ESSENTIAL_STEP_APPLIED / INTEGRATED_FOURIER_CROSSBLOCK_SHARPENING / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 0. Exact target and current corrections

The target remains: for independent real random variables `X_1,...,X_n` with probability densities bounded by `1`, and real symmetric `A` having at least three eigenvalues of absolute value at least `1`, prove a universal bound on the essential supremum of the density of `Q=X^T A X`, or give a genuine counterexample. No moment, centering, continuity, log-concavity, diagonal-basis independence, or post-rotation independence assumption is available.

This run consumed all live route corrections before publication:

- `QFORM-POINTWISE-DECAY-FALSE`: no law-uniform one-dimensional pointwise Fresnel decay may be assumed.
- `QFORM-FIBER-SUP-DIMENSION-LOSS`: naive unrestricted spectral-fiber suprema can lose dimension.
- `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`: spectral rotation does not preserve coordinate independence.
- `QFORM-CROSSMINOR-ALONE-FALSE`: a nonsingular `2x2` cross block alone does not force bounded density; the rank-two Fourier tail is only `|t|^{-1}`.
- `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`: the global constant cannot be `pi`; the current analytic lower bound is `C>=3 sqrt(2)`. The same correction supplied `QFORM-CROSSBLOCK-RANK-r-FOURIER-v1`, giving `2r/(r-2) Delta^{-1/r}` for an arbitrary rank-`r>2` original-coordinate cross block, where `Delta` is the product of its nonzero singular values. Canonical correction report: `yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc`, blob `d0546b3190cb35a070fabd86162f4b4874975f62`.

The assigned partner `fleet03/B02` had a current QFORM start record (`math-research-brain@d85ce8bcca55a068b70ab443f8edb4063ed479c8`) but no completed QFORM handoff at the final pre-write partner check. I therefore did not wait or fabricate a partner premise.

Two completed same-programme dependencies were actually used for compatibility, not as closure claims:

1. fleet02/B08, canonical report `math-open-problems@0b5925a458d36c1ec1cf8ab344c9676260a97c8a`, proves a diffuse rank-three Fourier/Brascamp--Lieb branch and identifies leverage-heavy rows as its mechanism boundary.
2. fleet02/B07, canonical report `math-open-problems@7ba557b8854ea86dcdc22a342d6fdd73d6882c6a`, records exterior-power determinant mass and the fact that fixed-size physical minors can be individually tiny in Walsh/Hadamard stress families.

External source input: Galyna Livshyts, Grigoris Paouris and Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949v2 / Israel J. Math. 216 (2016), prove that every `r`-dimensional orthogonal marginal of a product density with one-dimensional factors bounded by `1` has density at most `2^{r/2}`. For the one-dimensional aggregate used later I also use Mark Rudelson and Roman Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, IMRN 2015, Theorem 1.2: a normalized linear combination of independent density-`<=1` variables has density at most `sqrt(2)`.

No numerical or symbolic computation is used below; all constants come from exact Fourier/Plancherel calculations.

## 1. Main new theorem: one physical pivot side saves a factor `sqrt(2)`

### Theorem `QFORM-PHYSICAL-PIVOT-CROSSBLOCK-FOURIER-v1`

Let `I,J` be disjoint original-coordinate sets with

`|I|=r>2`.

Let

`B=A[I,J]`

have rank `r`, with nonzero singular values `s_1,...,s_r`, and put

`Delta = product_{a=1}^r s_a`.

All coordinates outside `I union J` may be present, and all principal blocks and couplings of `A` may be arbitrary. Then for every permitted product input law the characteristic function of `Q=X^TAX` satisfies

`|phi_Q(t)| <= min(1, 2^{r/4} pi^{r/2} Delta^{-1/2} |t|^{-r/2})`.   (1.1)

Consequently `phi_Q in L^1(R)`, `Q` has a bounded continuous density vanishing at infinity, and

`boxed( ||p_Q||_infinity <= sqrt(2) * r/(r-2) * Delta^{-1/r}. )`   (1.2)

For `r=3`,

`boxed( ||p_Q||_infinity <= 3 sqrt(2) Delta^{-1/3}. )`   (1.3)

This retains every target quantifier except for the explicitly stated quantitative cross-block condition. It does not assume independence after any eigenvector rotation.

### Proof

Condition first on every coordinate in `K=(I union J)^c`. The conditional problem has the same product laws on the untouched original-coordinate blocks `I` and `J`; conditioning only adds deterministic linear and constant terms. Since the final estimate is uniform in the conditioned value, it is enough to work with the conditional form.

Take a thin singular-value decomposition

`B=P S R^T`,

where, because `|I|=r`, `P` is an `r x r` orthogonal matrix, `R` has orthonormal columns, and `S=diag(s_1,...,s_r)`. Put

`Y=P^T X_I`, `Z=R^T X_J`.

The two vectors are independent because `I` and `J` are disjoint original-coordinate blocks. Write the conditional quadratic form as

`Q=q_I(X_I)+q_J(X_J)+2 Y^T S Z + c`,

where `q_I,q_J` include all within-block quadratic and linear terms. For fixed real `t`, define complex pushforward measures

`nu_{I,t}(E)=E[1_{Y in E} exp(i t q_I(X_I))]`,

`nu_{J,t}(E)=E[1_{Z in E} exp(i t q_J(X_J))]`.

They have densities `F_t,G_t`. Since `P` is square orthogonal, `Y=P^T X_I` is just an orthogonal change of variables of the `r` original independent coordinates. Its density is

`rho_I(y)=product_{i in I} f_i((Py)_i)`,

so `rho_I<=1`, `int rho_I=1`, and therefore

`||F_t||_2^2 <= int rho_I^2 <= 1`.   (1.4)

For `Z=R^T X_J`, Livshyts--Paouris--Pivovarov gives

`||rho_J||_infinity <= 2^{r/2}`.

The total variation of `nu_{J,t}` is dominated by the law of `Z`, hence

`||G_t||_2^2 <= ||rho_J||_infinity int rho_J <= 2^{r/2}`,

so

`||G_t||_2 <= 2^{r/4}`.   (1.5)

Using the Fourier convention `hat G(xi)=int exp(i xi.z)G(z)dz`, independence gives

`phi_Q(t)=exp(i t c) int F_t(y) hat G_t(2 t S y) dy`.

Cauchy--Schwarz, the change of variables `xi=2tSy`, and Plancherel yield, for `t!=0`,

`|phi_Q(t)|`
` <= ||F_t||_2 (2|t|)^{-r/2} Delta^{-1/2} ||hat G_t||_2`
` = pi^{r/2}|t|^{-r/2}Delta^{-1/2}||F_t||_2||G_t||_2`
` <= 2^{r/4} pi^{r/2} Delta^{-1/2}|t|^{-r/2}`.

This proves (1.1) after also using `|phi_Q|<=1`.

Set

`D=2^{r/4} pi^{r/2} Delta^{-1/2}`, `alpha=r/2>1`.

On each half-line the exact integral of `min(1,D t^{-alpha})` split at `t_0=D^{1/alpha}` equals

`D^{1/alpha} alpha/(alpha-1)`.

Therefore

`||phi_Q||_1 <= 2 D^{2/r} r/(r-2)`
` = 2 sqrt(2) pi r/(r-2) Delta^{-1/r}`.

Fourier inversion gives

`||p_Q||_infinity <= (2pi)^{-1}||phi_Q||_1`
` <= sqrt(2) r/(r-2) Delta^{-1/r}`.

Since `phi_Q in L^1`, the inverse Fourier representative is continuous and vanishes at infinity. Averaging the uniform conditional density bound over `X_K` completes the proof. QED.

### Relation to the fresh interactive cross-block theorem

The correction theorem `QFORM-CROSSBLOCK-RANK-r-FOURIER-v1` allows both cross-block sides to have arbitrary cardinality. It must pay the `2^{r/2}` marginal-density bound on both projected sides and obtains constant `2r/(r-2)`. Here one side consists of exactly `r` original independent coordinates, so its complex density has `L^2` norm at most `1` without a projection loss. This saves exactly one factor `sqrt(2)` in the final density constant.

If `J` also has exactly `r` original coordinates and `B` is square invertible, the same proof has `||G_t||_2<=1`, so it sharpens further to

`boxed( ||p_Q||_infinity <= r/(r-2) |det B|^{-1/r}. )`   (1.6)

In particular, an invertible physical `3x3` cross block gives

`boxed( ||p_Q||_infinity <= 3 |det B|^{-1/3}. )`   (1.7)

No zero-pivot assumption is needed when `r=3`. This is fully compatible with `QFORM-CROSSMINOR-ALONE-FALSE`: its falsifier is rank `2`, where the same calculation stops at the nonintegrable `|t|^{-1}` threshold. The B09 zero-pivot theorem is stronger at rank two because it uses extra structure not present here.

A useful numerical coincidence is now source-valid: the fresh lower-bound correction proves every universal target constant must satisfy `C>=3sqrt(2)`. Thus on the scoped branch `r=3`, `Delta>=1`, (1.3) attains that lower barrier exactly. This does **not** imply that the global optimum is `3sqrt(2)`, because the target hypotheses do not force such a physical cross block.

## 2. Localized three-eigenspace row: an endpoint smoothing dichotomy

The cross-block theorem gives full `L^1` Fourier control when three physical pivots jointly see a quantitatively nondegenerate outside block. The complementary leverage-heavy case admits another exact reduction that remains valid with arbitrary additional eigenvalues.

Choose any three orthonormal eigenvectors of `A` whose eigenvalues have modulus at least `1`, and let `U` be the corresponding `n x 3` matrix. Let `u_i^T` be row `i` of `U`. Suppose for some physical coordinate `i`,

`a=||u_i|| > 1/2`.

Put

`d=A_ii`,

`sigma=(sum_{j!=i} A_ij^2)^{1/2}`.

Because the full eigenbasis is orthonormal,

`d^2+sigma^2 = ||Ae_i||^2 = sum_k lambda_k^2 u_{ik}^2 >= a^2 > 1/4`.   (2.1)

Thus, using threshold `1/4`, either

`|d|>=1/4`,   (D)

or

`sigma>=sqrt(3)/4`.   (C)

This simple dichotomy survives all extra eigenvalues; there is no cancellation in `||Ae_i||^2`.

### Branch (D): a universal `L^{3/2}` density credit

Condition on every coordinate except `X_i`. Write

`Q=d X_i^2+2L X_i+R`
` = d(X_i+L/d)^2 + R-L^2/d`.

For any density `f<=1` of mass one and any shift `h`, the density `g` of `d(X+h)^2` obeys

`||g||_{3/2} <= 2 |d|^{-1/3}`.   (2.2)

Proof of (2.2): for `d>0` (reflection handles `d<0`), put `F(r)=f(r-h)+f(-r-h)`. Then `0<=F<=2` and `int_0^infinity F(r)dr=1`. The square pushforward satisfies

`int g^{3/2}`
` = (2d)^{-1/2} int_0^infinity F(r)^{3/2} r^{-1/2}dr`
` <= d^{-1/2} int_0^infinity F(r) r^{-1/2}dr`
` <= 2sqrt(2) d^{-1/2}`,

where the last inequality is the bathtub maximum under `0<=F<=2`, `int F=1`, attained by filling nearest zero. Raising to the `2/3` power gives (2.2).

Minkowski for the mixture over the conditioned coordinates yields

`||p_Q||_{3/2} <= 2 |d|^{-1/3} <= 2*4^{1/3}`.   (2.3)

Hence Hausdorff--Young also gives a universal `L^3` characteristic-function credit in this branch. This is not yet an `L^infinity` density bound.

### Branch (C): random-linear averaging restores valid `|t|^{-1/2}` decay

Write

`L=sum_{j!=i} A_ij X_j`.

After normalizing the coefficient vector by `sigma`, Rudelson--Vershynin Theorem 1.2 gives a density `g_L` with

`||g_L||_infinity <= sqrt(2)/sigma`.   (2.4)

For `t!=0`, define

`I_t(l)=int f_i(x) exp(i t(d x^2+2 l x)) dx`.

The false route correction forbids a uniform pointwise bound on `I_t(l)` at fixed `l`. Instead average it over the genuinely random independent linear aggregate `L`. With

`h_t(x)=f_i(x)exp(i t d x^2)`,

angular-frequency Plancherel gives exactly

`int_R |I_t(l)|^2 dl`
` = pi |t|^{-1} ||f_i||_2^2`
` <= pi/|t|`.   (2.5)

Conditioning on the other coordinates and using Jensen,

`|phi_Q(t)|^2`
` <= E |I_t(L)|^2`
` <= ||g_L||_infinity int |I_t(l)|^2dl`
` <= pi sqrt(2)/(sigma |t|)`.

Therefore

`boxed( |phi_Q(t)| <= (pi sqrt(2)/sigma)^{1/2}|t|^{-1/2}. )`   (2.6)

Under branch (C),

`boxed( |phi_Q(t)| <= 2 sqrt(pi) (2/3)^{1/4}|t|^{-1/2}. )`   (2.7)

This does not contradict `QFORM-POINTWISE-DECAY-FALSE`: cancellation is being supplied by an independent random linear aggregate whose density has a source-valid uniform bound. The exponent is the rank-one endpoint and is not integrable by itself.

### Consequence of Section 2

Every target matrix whose selected three-large-eigenvalue subspace has a row of leverage norm greater than `1/2` receives one of two dimension-free endpoint credits:

- universal output `L^{3/2}` control from a quantitatively large physical diagonal pivot; or
- universal weak-`L^2`/`|t|^{-1/2}` Fourier control from a quantitatively large physical cross-row aggregate.

This is valid even when `A` has arbitrary additional eigenvalues. It complements the exact-rank-three diffuse Fourier theorem rather than discarding those extra directions.

## 3. What is now paid, and the first unpaid implication

The integrated-Fourier mechanism now has a clean three-dimensional physical threshold:

1. A rank-`r>2` original-coordinate cross block gives integrable `|t|^{-r/2}` decay. If one side consists of exactly `r` physical coordinates, the new constant is `sqrt(2) r/(r-2) Delta^{-1/r}`; if both sides are exactly `r`, it is `r/(r-2)|det B|^{-1/r}`.
2. Rank two is correctly excluded: it gives only `|t|^{-1}`, matching the live B09 falsifier.
3. A leverage-heavy row in a chosen three-large-eigenvalue subspace cannot disappear into arbitrary extra spectral directions: it forces either a physical square pivot or a random linear cross pivot with the explicit endpoint estimates (2.3)/(2.7).

The **first unpaid implication** for this pathway is therefore structural, not Fourier algebra:

`QFORM-THREE-PIVOT-OR-RESIDUAL-CURVATURE-v1` — starting only from three eigenvalues `|lambda|>=1`, prove that either there is a disjoint physical pivot set `I` of size three and a block `J` for which the cross-block singular product `Delta(A[I,J])` is bounded below by a universal constant, or use the localized endpoint dichotomy plus the residual two spectral directions to supply the missing additional smoothing. The alternative diffuse regime must be aggregated rather than selecting one fixed minor, because the Walsh/Hadamard examples have individually tiny fixed-size physical minors.

The live `QFORM-CROSSMINOR-ALONE-FALSE` correction is respected: no rank-two cross-minor is treated as closure. The fresh lower-bound correction `C>=3sqrt(2)` is also respected; no `C=pi` claim remains.

## 4. Status

`ESSENTIAL_STEP_APPLIED`.

The full arbitrary-matrix conjecture remains OPEN. The theorem in Section 1 is a target-level conditional implication with an explicit universal density constant and an actual uniform integrated characteristic-function bound. Section 2 gives a new target-wide localized-row reduction with exact endpoint smoothing credits. No numerical experiment, histogram, random vector surrogate, post-rotation independence assumption, or fabricated partner result is used.
