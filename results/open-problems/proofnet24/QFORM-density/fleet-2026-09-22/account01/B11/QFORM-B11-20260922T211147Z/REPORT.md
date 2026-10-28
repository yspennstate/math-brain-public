SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-22T21:11:47Z.
attacking: indefinite heavy-row residual-leverage compiler via exact Schur determinant accounting and normalized-row recursion.

# QFORM B11 report — null-scalar determinant smoothing at the unit-leverage endpoint

Outcome: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL TARGET OPEN**. Execution: **WITHOUT_VERIFIED_BRAIN**.

## Sources consumed


Assigned partner actually used: account02/B11 run `20260922T192814Z-b11-qform-70f57503`, canonical mathematics `yspennstate/math-open-problems@2c065b1bb6a45a479bd2ac5d3405cd59e7bafe8f`. Its exact-ray aggregation step gives a normalized exact-ray aggregate density cap `sqrt(e)` while retaining independence between disjoint ray classes. Earlier completed projection-product machinery supplies the standard two-dimensional orthonormal product-projection cap `e`; the present proof only uses such caps after a genuine original-coordinate support separation.

Fresh peer context also consumed: account03/B19 run `20260922T210216Z-account03-B19-QFORM-r18`, canonical mathematics `yspennstate/math-open-problems@4caa949abfce263bcfdcdf7fe175a4a999ae35b5`, proving the sequential two-original-pivot third-source estimate. It is used only as an exit in the conditional synthesis below, not as a premise of the new lemma.

Corrections respected: no arbitrary-joint 3D coarea bound, no conditional-cap-as-independence step, no law-uniform pointwise quadratic-phase decay, no perturbative deletion of small coefficients under unbounded supports, and no assertion that one fixed physical minor is uniformly good.

## Theorem 1: dependence-safe null-scalar / arbitrary-pair quadratic smoothing

Let `Z` be independent of the pair `(V,W)`. Assume `Z` has a probability density `f` with `||f||_infinity<=L`, and `(V,W)` has a joint probability density `g` with `||g||_infinity<=M`. Let `alpha beta !=0`. For arbitrary real `gamma,delta` and arbitrary affine terms, put

`T = 2 alpha Z W + beta V^2 + 2 gamma V W + delta W^2 + affine(Z,V,W)`.

Then `T` has an essentially bounded density and

`||p_T||_infinity <= 3*2^(2/3) (L M)^(2/3) |alpha|^(-2/3) |beta|^(-1/3).`  (1)

No independence between `V` and `W` is assumed.

### Proof

The affine `Z` term can be absorbed by translating `W`; this preserves the joint density cap `M` and independence from `Z`. Remaining affine pair terms are retained in the pair polynomial. Write

`P(v,w)=beta v^2+2 gamma v w+delta w^2+ell_1 v+ell_2 w+c`.

For `w!=0`, conditioning on `(V,W)=(v,w)` and changing variables through `Z` gives, for a.e. `t`,

`p_T(t)=integral integral g(v,w) [1/(2|alpha w|)] f((t-P(v,w))/(2 alpha w)) dv dw.`  (2)

Fix `r>0` and split at `|w|=r`.

For `|w|>r`, use `f<=L` and `integral g=1`:

`I_far <= L/(2|alpha| r).`  (3)

For `|w|<=r`, use `g<=M` and integrate first in `v`. Completing the square in `v`, the argument of `f` has the form `A(w,t) +/- lambda(w) x^2`, where

`lambda(w)=|beta|/(2|alpha w|)`.

For every probability density `f<=L`, every `A`, and every `lambda>0`,

`integral_R f(A +/- lambda x^2) dx <= 2 sqrt(L/lambda).`  (4)

Indeed, after `y=lambda x^2` the left side is `lambda^(-1/2) integral_0^infinity f(A +/- y)y^(-1/2)dy`; among functions bounded by `L` with mass at most one, the latter integral is maximized by placing mass `L` adjacent to `y=0`, giving `2 sqrt(L)`.

Substituting (4) into (2),

`I_near <= [sqrt(2) M sqrt(L)/sqrt(|alpha beta|)] integral_{|w|<=r}|w|^(-1/2)dw`
`        = 4 sqrt(2) M sqrt(L) sqrt(r)/sqrt(|alpha beta|).`  (5)

Thus

`p_T(t) <= A sqrt(r)+B/r`,
`A=4 sqrt(2) M sqrt(L)/sqrt(|alpha beta|)`, `B=L/(2|alpha|)`.

Optimizing at `sqrt(r)=(2B/A)^(1/3)` gives

`min_r [A sqrt(r)+B/r] = 3*2^(-2/3) A^(2/3)B^(1/3)`
`=3*2^(2/3)(LM)^(2/3)|alpha|^(-2/3)|beta|^(-1/3)`, proving (1).

The key point is that the pair may be arbitrarily dependent internally; only the scalar-versus-pair independence is used.

## Corollary 2: coordinate-free null determinant identity

Let `H` be an invertible real symmetric `3x3` matrix in variables `(Z,Y_1,Y_2)`, with the `Z^2` coefficient exactly zero. Assume `Z` is independent of `Y=(Y_1,Y_2)`, with density caps `L` and `M` as above. Rotate only inside the two-dimensional `Y`-plane so that the cross vector from `Z` is `(0,alpha)`. Then

`H = [[0,0,alpha],[0,beta,gamma],[alpha,gamma,delta]]`

and the exact structural identity is

`det H = -alpha^2 beta.`  (6)

Therefore Theorem 1 gives the invariant estimate

`||p_{(Z,Y)^T H (Z,Y)+affine}||_infinity <= 3*2^(2/3)(LM)^(2/3)|det H|^(-1/3).`  (7)

This covers both signatures `(+,+,-)` and `(+,-,-)` by replacing `H` by `-H`.

## Corollary 3: exact-rank-three, unit-leverage null physical coordinate

Let `A=R M R^T` have exact rank three with `R^T R=I_3`, and suppose an ORIGINAL coordinate row `r_0` satisfies

`||r_0||=1`,  `r_0^T M r_0=0`.

Put `v=r_0`. Since `sum_i r_i r_i^T=I_3`,

`sum_{i!=0}(r_i dot v)^2 = 1-||r_0||^2=0`,

hence every residual row is orthogonal to `v`. Thus the spectral coordinate in direction `v` is exactly the untouched original variable `X_0`, while the complementary two spectral coordinates depend only on the other original variables. This is genuine independence, not a conditional-density surrogate.

The scalar has density cap `L=1`. The complementary orthonormal two-dimensional projection of the residual product law has the standard cap `M<=e`. Applying (7) with `H=M` gives

`||p_{X^T A X}||_infinity <= 3*2^(2/3)e^(2/3)|det M|^(-1/3)`
`                             < 9.276 |det M|^(-1/3).`  (8)

If `sigma_min(M)>=s`, then `|det M|>=s^3`, so

`||p_{X^T A X}||_infinity < 9.276 s^(-1).`  (9)

For the exact target-rank-three normalization `s>=1`, this is `<9.276`.

## Assigned-partner result applied to an actual inequality

Partner account02/B11's exact-ray aggregation theorem says a normalized exact projective ray aggregate built from a disjoint original-coordinate bank has scalar density cap `L<=sqrt(e)`. If such a null scalar ray-bank is independent of a complementary orthonormal two-dimensional bank with joint cap `M<=e`, (7) gives immediately

`||p_Q||_infinity <= 3*2^(2/3) e |det H|^(-1/3)`
`                  < 12.946 |det H|^(-1/3).`  (10)

Thus whenever the partner compiler exposes a complete null scalar ray-bank and the remaining spectral plane is carried by disjoint original coordinates, the whole indefinite rank-three block is paid at a universal determinant scale. This is a direct numerical inequality using the completed partner cap, not a citation-only dependency.

## Why the third direction removes the opposite-sign logarithm

The rank-two saddle `2ZW` has a logarithmically divergent density at zero for ordinary bounded inputs such as uniforms. Formula (2) displays its `1/|w|` kernel. The third transverse quadratic coefficient `beta V^2` changes the near-`w=0` integration through (4): after integrating in `V`, the singularity becomes `|w|^(-1/2)`, which is integrable. The exact determinant identity (6) shows that invertibility of the rank-three null-scalar form is precisely the condition `alpha beta !=0`; the third direction is not decorative, it is the transverse curvature that regularizes the hyperbolic logarithm.

## Conditional local synthesis and first remaining implication

For the exact-rank-three heavy/null chamber, the currently paid pieces are:

1. If, after deleting a heavy original coordinate of leverage `h<1`, every deletion-normalized residual leverage is `<=1/2`, previous B11 theorem `QFORM-HEAVY-DELETE-DIFFUSE-v1` gives the continuous bound `3e[(1-h)|det M|]^(-1/3)`.
2. At the endpoint `h=1` with null physical diagonal, Corollary 3 above gives `<9.276 |det M|^(-1/3)` without any residual-leverage condition.
3. A strong exact ray is covered quantitatively by assigned partner account02/B11's ray-atom theorem.
4. If a genuinely nonzero second original-coordinate Schur pivot appears, account03/B19's sequential two-pivot theorem gives a finite explicit bound without a `sigma_min` loss.

The first unpaid implication is therefore **QFORM-NEAR-UNIT-NULL-OVERLAP-COMPILER-v1**: handle `0<h<1`, especially `h` close to one, when a deletion-normalized residual leverage exceeds `1/2` and no strong exact ray or quantitative second pivot is available. The scalar spectral direction is then contaminated by residual original coordinates, so Corollary 3's exact independence fails. A valid compiler must bridge the `h<1` diffuse deletion theorem to the `h=1` null determinant theorem while retaining original-coordinate product provenance. It may not discard the overlap as a small perturbation, because support/moment bounds are absent, and it may not replace independence by a bounded conditional density. Arbitrary extra spectrum remains a separate full-target interface unless a full-matrix pair/ridge exit applies.

## Status and regularity

This run proves essential boundedness for Theorem 1 and Corollaries 2–3. Continuity is **not proved** by this argument. The full QFORM conjecture and full-target continuity remain OPEN.
