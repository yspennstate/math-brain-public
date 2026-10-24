# account02/B18 — literature transfer audit: bounded spectral marginals are not enough; a physical definite 2x2 block is enough

**Programme:** QFORM-DENSITY-3EIG-20260922, owner revision 2026-09-22.5  
**Assignment:** Literature-to-proof transfer, complementary constructions/source-valid counterexamples  
**Partner:** account03/B18  
**Full target:** OPEN / NOT PROVED

## 1. First unpaid implication

The most tempting exact literature transfer is the sharp theorem of Livshyts–Paouris–Pivovarov (LPP) on low-dimensional marginals of product measures. It gives a dimension-free L-infinity cap for the three-dimensional spectral projection of the product input. This run proves that **that cap alone cannot control the quadratic pushforward, even for the positive form |y|^2 in dimension three**. Therefore the first unpaid implication is not another marginal-density theorem. It is a source-preserving curvature estimate that uses the fact that the spectral marginal and its complement arise jointly from an original-coordinate product law.

Concretely, one needs a bound on the actual product-provenance quadratic trace/conditional average, not a statement of the form

`||g_E||_infinity <= C  =>  || law(q_E(Y)) ||_infinity <= C'`.

The latter implication is false by the shell construction in Section 3 below.

## 2. Primary-source theorem and exact hypothesis transfer

### 2.1 Livshyts–Paouris–Pivovarov

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877–889; arXiv:1507.07949.

Their Theorem 1.1 states: for `1 <= k < n` and every k-dimensional subspace `E`, there are `gamma_i in [0,1]`, `sum gamma_i=k`, such that for any one-dimensional probability densities `f_i`,

`|| pi_E(prod_i f_i) ||_infinity
 <= min((n/(n-k))^((n-k)/2), 2^(k/2)) prod_i ||f_i||_infinity^(gamma_i).`

Thus, under the present cap-one product hypothesis,

`||pi_E f||_infinity <= 2^(k/2)`.

For `k=3` this gives `2^(3/2)` whenever `n>3`; for `n=3`, the full product density is already at most one. No moment, centering, support, identical-law, Gaussian, or log-concavity hypothesis is present. The theorem is therefore genuinely source-matching for **linear orthogonal marginals** of the present input.

What it does *not* state is a bound on the pushforward of such a marginal by a quadratic form, nor a conditional density bound after revealing the orthogonal complement.

### 2.2 Nearby literature that does not transfer to the full target

Carbery–Wright's polynomial anti-concentration theorem is for log-concave measures and yields a degree-dependent sublevel estimate; arbitrary cap-one product densities here may be highly fragmented and need not be log-concave. It therefore does not match the full law class.

Choudhary–Kuchibhotla (arXiv:2606.25441, 24 June 2026) prove Levy concentration bounds for weighted sums of noncentral chi-square variables, i.e. quadratic polynomials of independent standard Gaussians. Their signs and arbitrarily small quadratic coefficients are flexible, but Gaussianity is essential to the stated model. A general cap-one product law is not rotation invariant, so this theorem cannot be transferred by diagonalizing A.

The previously transferred Meka–Nguyen–Vu Bernoulli-polynomial theorem remains valid for the selector-switching reduction recorded in the preceding B18 run, but it supplies a large-matching anti-concentration regime rather than the desired universal linear small-ball estimate.

## 3. New counterexample: a bounded 3D marginal density does not control even |Y|^2

### Theorem 3.1 — `QFORM-SPECTRAL-MARGINAL-CAP-ALONE-FALSE-v1`

For every `M>0` there is a probability density `g` on `R^3` with `||g||_infinity=1` such that, for `Y~g`, the density of `|Y|^2` has essential supremum larger than `M`.

#### Proof

Fix `R>0` and define

`R_+ = (R^3 + 3/(4 pi))^(1/3)`.

Let

`S_R = { y in R^3 : R <= |y| <= R_+ }`

and let `g_R = 1_{S_R}`. Its integral is exactly

`(4 pi/3)(R_+^3-R^3)=1`,

so `g_R` is a probability density and `||g_R||_infinity=1`.

Put `T=|Y|^2`. By polar coordinates (equivalently coarea), for

`R^2 < s < R_+^2`,

`p_T(s) = area(S^2_{sqrt(s)})/(2 sqrt(s)) = 2 pi sqrt(s)`.

Hence

`||p_T||_infinity = 2 pi R_+`,

in the essential-supremum sense, which tends to infinity with `R`. QED.

### Consequence for the LPP transfer

The LPP three-dimensional marginal cap is at most `2^(3/2)`, while the shell already has the stronger cap `1`. Thus **no argument that forgets everything except the L-infinity bound of the three-dimensional spectral marginal can prove the target**, even for a positive rank-three quadratic form.

This is not a counterexample to QFORM: the shell coordinates are dependent and no claim is made that this shell is an orthogonal marginal of a cap-one product law. It is a counterexample to the information-loss step that replaces product provenance by a generic bounded joint density after rotation/projection.

It strengthens the existing `QFORM-NO-INDEPENDENCE-AFTER-ROTATION` warning in a quantitative way: preserving a good low-dimensional marginal density cap still does not suffice.

## 4. New positive branch: any physical definite 2x2 principal block pays by coarea

### Theorem 4.1 — `QFORM-PHYSICAL-DEFINITE-2X2-v1`

Let `X_1,...,X_n` be independent with one-dimensional probability densities bounded by one, and let `A` be real symmetric. Suppose two original coordinates `I={i,j}` have a definite `2 x 2` principal block

`B=A_{I,I}`.

Then `Q=X^T A X` has a density satisfying

`||p_Q||_infinity <= pi / sqrt(det B)`,

where `det B>0` for either positive- or negative-definite `B`. In particular, if `det B>=1`, then `||p_Q||_infinity<=pi`.

No assumption is made on dimension, the remaining block, outside couplings, moments, support, or signs/eigenvalues outside `I`.

#### Proof

Condition on all coordinates outside `I`. The two selected coordinates remain independent with joint density at most one. For fixed outside value `z`, the conditional quadratic form is

`q_z(x)=x^T B x + 2 c_z^T x + d_z`, `x in R^2`.

If `B` is positive definite, complete the square:

`q_z(x)=(x+B^{-1}c_z)^T B (x+B^{-1}c_z) + const_z`.

Translate `x` and then set `u=B^(1/2)x`. The transformed two-dimensional density is at most `1/sqrt(det B)`. For `S=|u|^2`, polar coordinates give, for almost every `s>0`,

`p_S(s) = (1/2) integral_{S^1} h(sqrt(s) theta) d theta
          <= pi/sqrt(det B)`.

Translations in the output do not change this bound. If `B` is negative definite, apply the positive-definite argument to `-B` and reflect the scalar output. Thus every conditional density is bounded by the same number `pi/sqrt(det B)`. Averaging over the outside coordinates yields the asserted unconditional density cap. QED.

This theorem works in the **original independent coordinate basis**. It never rotates the input vector.

### Why this branch is supporting rather than a full solution

The three-large-eigenvalue assumption does not force a uniformly good definite physical minor. The source-valid stress family from the correction inbox,

`A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)`,

has spectrum `{1,1,-1}`. Its only nonsingular positive-definite physical `2 x 2` principal blocks pair the scalar `1` coordinate with a coordinate from `J_m/m`, and have determinant exactly `1/m`; the other within-bank principal pairs are rank one, and positive/negative bank pairs are indefinite. Thus Theorem 4.1 gives only `pi sqrt(m)` on that family and cannot be promoted to a spectral extraction theorem.

This agrees with the existing correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, which requires aggregation across coordinate banks rather than one uniformly conditioned principal block.

## 5. Completed partner result actually applied

I read the immutable account03/B18 report at math-open-problems commit

`3bbdd8710e88c2b9b1e1dd9f1ed083395e8f08b7`

and applied its theorem `QFORM-TWOCOORD-CROSS-AVERAGING-v1`.

For independent cap-one `X=(X1,X2)` and `Y`, a physical rank-two matrix `C`, arbitrary `d`, and arbitrary measurable `H(Y)`, the partner proves

`R = 2 X^T(CY+d)+H(Y)`

has a continuous density with

`||p_R||_infinity <= 2 sqrt(2) / sqrt(sigma_1(C) sigma_2(C)).`

The LPP theorem supplies the exact two-dimensional product-marginal cap used in that proof. This partner branch and Theorem 4.1 are complementary:

* Theorem 4.1 pays when the selected physical pair has a definite self-quadratic block; arbitrary outside coupling is harmless after conditioning.
* The partner theorem pays when the selected pair has zero self-quadratic block but a rank-two physical cross map into the remaining coordinates.

Neither branch asserts that the global three-eigenvalue condition forces its local hypothesis. The correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` remains fully respected.

## 6. Synthesis and exact remaining connection

The literature audit now separates three logically different facts.

1. **Linear marginal control is source-valid:** LPP gives `||pi_E f||_infinity<=2^(k/2)` for product cap-one inputs.
2. **Marginal cap alone is insufficient for quadratic curvature:** the shell theorem gives unbounded density for `|Y|^2` despite `||g_Y||_infinity=1`.
3. **Original-coordinate curvature/cross structure can close real branches:** Theorem 4.1 and the completed account03/B18 cross-averaging theorem both give explicit dimension-free density caps without losing product provenance.

Therefore the exact first unpaid implication for this literature-transfer pathway is:

`QFORM-PRODUCT-PROVENANCE-CURVATURE-v1` — derive a dimension-free curved-trace/small-ball estimate for the actual joint pair `(P_E X, P_{E^perp}X)` coming from a cap-one product density, strong enough to exploit three large spectral directions, without replacing it by a generic bounded marginal density or an unjustified conditional density cap.

The newer regularized-determinant theorem closes a low-leverage range-projection branch, while the completed account03/B18 theorem closes a rank-two zero-self physical cross branch. The remaining hard regime is leverage-heavy and nonseparable/aggregated. The shell counterexample shows exactly why an LPP-only spectral-projection reduction cannot bridge it.

## 7. Status

- `QFORM-SPECTRAL-MARGINAL-CAP-ALONE-FALSE-v1`: **PROVED explicit counterexample to a reduction**, not a counterexample to QFORM.
- `QFORM-PHYSICAL-DEFINITE-2X2-v1`: **PROVED supporting target-level branch**, explicit cap `pi/sqrt(det B)`.
- account03/B18 `QFORM-TWOCOORD-CROSS-AVERAGING-v1`: **completed partner theorem consumed and applied** with its exact source scope.
- Full arbitrary-matrix, arbitrary cap-one product-law theorem: **OPEN / NOT PROVED**.

No moment, support, centering, identical-law, log-concavity, Gaussianity, or rotation-independence assumption was inserted into either new theorem. The only dependent construction is explicitly labeled as a counterexample to a reduced information class rather than to the target.
