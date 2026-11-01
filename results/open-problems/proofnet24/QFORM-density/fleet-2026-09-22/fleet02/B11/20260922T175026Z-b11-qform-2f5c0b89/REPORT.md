# fleet02/B11 — translation-uniform zero-pivot triple smoothing and diffuse null-frame obstruction

Run: `20260922T175026Z-b11-qform-2f5c0b89`

Status: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM + SOURCE-VALID-MECHANISM-COUNTEREXAMPLE**. The full universal QFORM conjecture remains **OPEN / NOT PROVED**.

Execution status: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval is source retrieval, not verified native learned-memory ingestion.

## 1. First unpaid implication and conditional end-to-end route

The later owner proof-first continuation asks the B10/B11/B16 geometry roles to attack the zero/near-isotropic physical-pivot branch and to preserve original-coordinate product provenance. The exact target remains: for independent scalar inputs with densities at most one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal density bound for `X^T A X`, or give a genuine target counterexample.

A current conditional route is now:

1. If an original-coordinate nonzero scalar pivot exposes an exact rank-two residual with determinant scale, apply the completed orientation-free affine half-Riesz theorem
   `sup_t E|R-t|^{-1/2} <= 128 |det Lambda|^{-1/4}`.
2. If instead a physical principal `3 x 3` block is invertible and has a **zero diagonal entry**, apply the new theorem below. It is translation-uniform and survives arbitrary outside quadratic coefficients by conditioning.
3. For an exact-rank-three indefinite truncation, apply the designated partner fleet03/B11 on the majority-sign half-line: `||p_Q|| <= pi e/sqrt(2)`.
4. What remains is a product-preserving aggregate compiler when every usable physical determinant packet is individually tiny, plus the separate arbitrary-extra-spectrum debt.

The first unpaid B11 implication is therefore:

**AGGREGATED ZERO-PIVOT MINORITY TRACE.** In the many-small-null-triangle regime, aggregate the physical determinant mass before paying a reciprocal determinant power, while retaining enough original product provenance to control the minority two-sheet trace. The live two-sheet X-ray correction proves that a generic two-dimensional-marginal/X-ray cap is not enough.

Section 5 gives an exact rotated `(+,+,-)` family in which every diagonal entry is zero and every physical `3 x 3` determinant is at most `54/m^3`; hence no one-triple use of the theorem below can be dimension-free. The designated partner nevertheless controls the whole majority-sign half-line of that same family.

## 2. Source-pinned premises actually applied

The designated partner result actually applied is fleet03/B11:

- repository `yspennstate/math-open-problems`
- commit `6ce69d3584ae62a4f08532971c950fb625235c93`
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260922T171058Z-fleet03-B11-r11/REPORT.md`.

It proves that if all orthogonal two-dimensional marginals of `Y in R^3` have density cap `K`, then
`S=Y_1^2+Y_2^2-Y_3^2` has majority-sign density at most `pi K/sqrt(2)`. Applied to an exact-rank-three QFORM with eigenvalue magnitudes at least one, the product-projection theorem gives `K=e`, hence
`||p_Q||_{L^infinity(0,infinity)} <= pi e/sqrt(2)` for signature `(+,+,-)`, and the reflected statement for `(+,-,-)`.

The completed orientation-free rank-two affine half-Riesz theorem used in the conditional route is:

- repository `yspennstate/math-open-problems`
- commit `e542b1a6ef471b329e4e88a6553e1aacb45acc1a`
- path `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

It allows an arbitrary original-coordinate affine term and is therefore compatible with conditioning outside a physical block.

The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` is also binding: a generic 3D density can have uniformly bounded line/X-ray marginals while its minority two-sheet quadratic trace is arbitrarily large. The construction is not a product-projection counterexample, but it prevents discarding product provenance on the unpaid side.

## 3. New theorem: a zero physical pivot gives a full translation-uniform density bound

### Theorem 3.1 — `QFORM-ZERO-PIVOT-TRIPLE-v1`

Let `X,Y,Z` be independent real random variables with densities bounded by one. Let

`B = [[p,a,b],[a,0,c],[b,c,r]]`

be a real symmetric invertible matrix. For arbitrary real affine coefficients `ell_1,ell_2,ell_3,d`, put

`F = (X,Y,Z) B (X,Y,Z)^T + ell_1 X + ell_2 Y + ell_3 Z + d`.

Then `F` has an essentially bounded density and

`||p_F||_infinity <= 3 * 2^(2/3) * |det B|^(-1/3)`
`                  < 4.763 * |det B|^(-1/3)`.                 (3.1)

No sign, centering, moment, support, smoothness, or log-concavity assumption is made.

By permuting the three coordinates, the same theorem holds whenever **any** one diagonal entry of an invertible physical `3 x 3` block is zero.

### Proof, first when `a c != 0`

Define the original-product linear chart

`u = a X + c Z`,  `v = a X - c Z`.                              (3.2)

The map `(X,Z) -> (u,v)` has Jacobian magnitude `2|ac|`. Hence `(u,v)` has a joint density `h` satisfying

`||h||_infinity <= M := 1/(2|ac|)`,  `int h = 1`.              (3.3)

Crucially, `Y` remains genuinely independent of `(u,v)` because the chart uses only the original coordinates `X,Z`.

The `Y`-dependent part is

`2aXY + 2cYZ + ell_2 Y = 2(u+ell_2/2)Y`.                      (3.4)

Write `w=u+ell_2/2`. The part depending only on `X,Z` is a quadratic polynomial in `(u,v)`. The coefficient of `v^2` is

`gamma = (a^2 r - 2abc + c^2 p)/(4a^2c^2)`
`      = - det(B)/(4a^2c^2)`,                                  (3.5)

because

`det(B) = -a^2 r + 2abc - c^2 p`.                              (3.6)

Since `B` is invertible, `gamma !=0`. Complete the square in `v`. A shear/translation
`zeta = v + alpha w + beta`
has Jacobian one and keeps the transformed joint density `H(w,zeta)` bounded by `M`. Thus, after absorbing a quadratic polynomial of `w` and a constant into `P(w)`, we have the exact representation

`F = 2wY + gamma zeta^2 + P(w)`.                               (3.7)

The variables `w,zeta` need not be independent; only the cap `H<=M` and the genuine independence of `Y` are used.

### Lemma 3.2 — square-preimage bathtub bound

If `f` is any probability density with `0<=f<=1`, `beta !=0`, and `alpha` is arbitrary, then

`int_R f(alpha + beta z^2) dz <= 2 |beta|^(-1/2)`.             (3.8)

Indeed, after `s=z^2`, the left side is
`|beta|^(-1/2) int f(alpha +/- t) t^(-1/2) dt`
over one half-line. Among all `0<=f<=1` of total mass one, the integral against the decreasing weight `t^(-1/2)` is maximized by filling the first unit interval. Its value is `int_0^1 t^(-1/2)dt=2`.

### Density split

For `w !=0`, conditioning on `(w,zeta)` gives

`p_F(t)`
` = int H(w,zeta) [1/(2|w|)]`
`       f_Y((t-gamma zeta^2-P(w))/(2w)) dw dzeta`.             (3.9)

Fix `R>0`. On `|w|<=R`, use `H<=M` and Lemma 3.2 with
`beta=-gamma/(2w)`:

`int_{|w|<=R} ...`
` <= M int_{|w|<=R} [1/(2|w|)]`
`      * 2 (|gamma|/(2|w|))^(-1/2) dw`
` = 4M sqrt(2/|gamma|) sqrt(R)`.                               (3.10)

On `|w|>R`, simply use `f_Y<=1` and `int H=1`:

`int_{|w|>R} ... <= 1/(2R)`.                                  (3.11)

Therefore

`p_F(t) <= A_0 sqrt(R) + 1/(2R)`,                              (3.12)

where, by (3.3) and (3.5),

`A_0 = 4M sqrt(2/|gamma|)`
`    = 4 sqrt(2) / sqrt(|det B|)`.                             (3.13)

Take `R=A_0^(-2/3)`. Then

`p_F(t) <= (3/2) A_0^(2/3)`
`        = 3*2^(2/3)|det B|^(-1/3)`.                           (3.14)

The bound is uniform in `t`, proving (3.1) when `ac!=0`.

### Degenerate incident coefficient

If `a=0` or `c=0`, invertibility prevents both incident coefficients from vanishing. Perturb the zero incident coefficient by `epsilon`, keeping the central diagonal entry zero. The perturbed matrices `B_epsilon` satisfy the already proved case for all sufficiently small nonzero `epsilon`, with
`det B_epsilon -> det B`.

For the same input variables, `F_epsilon -> F` almost surely. For every nonnegative compactly supported continuous test function `psi`,

`E psi(F) = lim E psi(F_epsilon)`
` <= lim [3*2^(2/3)|det B_epsilon|^(-1/3)] int psi`
` = 3*2^(2/3)|det B|^(-1/3) int psi`.                          (3.15)

Thus the law of `F` is dominated by the same multiple of Lebesgue measure. This proves the theorem in all invertible cases. QED.

## 4. Ambient corollary: arbitrary extra spectrum is harmless once such a block exists

### Corollary 4.1

Let `A` be any real symmetric `n x n` matrix, with no rank restriction. Suppose some original-coordinate principal triple `I` has invertible block `B=A_{II}` and at least one zero diagonal entry. For independent cap-one inputs,

`||p_{X^T A X}||_infinity`
` <= 3*2^(2/3)|det B|^(-1/3)`.                                (4.1)

Proof: condition on every coordinate outside `I`. The three variables in `I` remain independent with their original density caps, while all cross terms with the frozen outside coordinates become arbitrary affine coefficients and the outside quadratic part becomes a constant. Theorem 3.1 is uniform in those affine coefficients. Averaging the conditional densities preserves the same cap. QED.

This is stronger in ambient scope than an exact-rank-three statement: arbitrary additional eigenvalues and nonseparable outside coefficients are retained.

## 5. Exact diffuse null-frame obstruction to one-triple closure

For `m>=3`, let

`theta_i=2pi i/m`

and define an `m x 3` spectral frame by rows

`r_i = (sqrt(2/m) cos theta_i, sqrt(2/m) sin theta_i, 1/sqrt(m))`. (5.1)

The equally spaced trigonometric identities give `R^T R=I_3`. Put

`Lambda=diag(1,1,-2)`,  `A=R Lambda R^T`.                      (5.2)

Then the nonzero spectrum of `A` is exactly `{1,1,-2}`; this is a genuinely rotated exact-rank-three `(+,+,-)` target. Moreover

`A_ii = 0` for every `i`,                                      (5.3)

and

`A_ij = (2/m)(cos(theta_i-theta_j)-1)`
`     = -(4/m) sin^2((theta_i-theta_j)/2)`.                    (5.4)

For any triple `I`,

`det A_{II} = det(Lambda) det(R_I)^2 = -2 det(R_I)^2`.         (5.5)

Factoring the columns of `R_I`,

`det R_I = (2/m^(3/2))`
`          det [[cos theta_i, sin theta_i,1]]_{i in I}`.       (5.6)

The last determinant is twice the Euclidean area of a triangle inscribed in the unit circle, whose maximum is attained by an equilateral triangle and equals `3sqrt(3)/2`. Therefore

`|det R_I| <= 3sqrt(3)/m^(3/2)`,
`|det A_{II}| <= 54/m^3`.                                     (5.7)

When `3|m`, an equilateral triple of rows exists and equality holds.

Consequently the **best** bound obtained by selecting one null-pivot physical triple and applying Theorem 3.1 grows linearly in `m`:

`3*2^(2/3) (max_I |det A_{II}|)^(-1/3)`
` = 3*2^(2/3) m / 54^(1/3)`.                                 (5.8)

Thus the bare three-large-eigenvalue hypothesis does **not** force a dimension-free determinant scale on one zero-pivot physical triple. This is a source-valid counterexample to that proof mechanism, not to QFORM.

The designated fleet03/B11 theorem applies directly to the same family because its nonzero eigenvalues are `1,1,-2`. Hence, despite (5.7),

`||p_{X^TAX}||_{L^infinity(0,infinity)} <= pi e/sqrt(2) < 6.039`. (5.9)

So the partner theorem completely pays the majority-sign half-line; the hard residue is the minority two-sheet side, exactly where the live X-ray-only correction says generic marginal caps lose essential product information.

Negating `A` gives the dual `(+,-,-)` family and interchanges the two half-lines.

## 6. Rank-two logarithmic singularity and exactly what the third direction does

The theorem does not erase the mandatory rank-two obstruction. In the fully zero-diagonal `3 x 3` case,

`B=[[0,a,b],[a,0,c],[b,c,0]]`, so `det B=2abc`.                (6.1)

If one third coupling tends to zero, `det B` tends to zero and (3.1) blows up. At the endpoint, the form collapses to a rank-two saddle such as

`2Y(aX+cZ)`,                                                   (6.2)

whose product law can have the classical logarithmic density singularity at zero.

When the third coupling is nonzero, the chart (3.2) turns that third direction into the nonzero quadratic coefficient

`gamma=-det B/(4a^2c^2)`.                                     (6.3)

The logarithmic `1/|w|` conditional factor from the saddle is then integrated against the square-preimage gain
`(|gamma|/|w|)^(-1/2)`, changing the small-`w` singularity from `|w|^{-1}` to `|w|^{-1/2}`. The optimized split (3.12) is finite. This is the precise local mechanism by which the third direction removes the rank-two logarithm in the zero-pivot chart.

For the fully zero-diagonal case, (3.1) reads equivalently

`||p_F||_infinity <= 3*2^(1/3)|abc|^(-1/3)`
`                    < 3.780 |abc|^(-1/3)`.                   (6.4)

## 7. Regression computation

The accompanying `VERIFY.py` checks:

1. the exact determinant / `gamma` identity in (3.5)-(3.6) on several numerical coefficient choices;
2. the circular frame identities for `m=6,12,24,48`;
3. `R^T R=I`, zero diagonal, and
   `max_I |det A_{II}|=54/m^3` to floating tolerance;
4. the constants `3*2^(2/3)=4.762203155904598...` and
   `3*2^(1/3)=3.779763149684619...`.

It terminates `QFORM_ZERO_PIVOT_TRIPLE_CHECK_PASS`.

`VERIFY.py` SHA-256:
`8e37a3f1b05277955e14b031c77aba1998f76789355b7903f7b4be5ad98170a5`.

Captured output SHA-256:
`ff83f7aede9dca4786451f141633e059484de2f1e1ee9aba8b4142b6cf8926aa`.

The computation is regression evidence only. The proof is Sections 3-5.

## 8. Integrity status

- New theorem: proved supporting theorem, all arbitrary affine translations, no post-rotation independence.
- Ambient outside spectrum: allowed under the stated physical-block hypothesis.
- Counterexample: refutes one-triple determinant-scale extraction only, not QFORM.
- Named partner fleet03/B11: consumed and applied to equation (5.9).
- Opposite-sign rank-two logarithmic singularity: retained and explained in Section 6.
- Minority two-sheet aggregate in the diffuse null-frame regime: OPEN.
- Full arbitrary-matrix QFORM target: OPEN / NOT PROVED.
- Continuity: not separately proved here.
- Execution: WITHOUT_VERIFIED_BRAIN.
