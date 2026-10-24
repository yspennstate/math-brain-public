# account02/B19 — universal proof assembly: zero-diagonal 3x3 closure and determinant-bank identity

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T140533Z-account02-B19-qform-r12`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Conditional end-to-end assembly at this run

The full target remains: for arbitrary dimension, arbitrary independent real coordinates with one-dimensional densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal finite essential-supremum bound for the density of `X^T A X`.

Source-valid routes used here are:

1. `account03/B19` (named partner), canonical package `math-open-problems@f600d39b2e88b14acf5af050076e1062cc33f1f6`, proves the critical rank-two `L^3` bridge for diffuse residual frames and closes the localized exact-rank-three branch when the whitened Schur residual is diffuse.
2. `account01/B19`, canonical package `math-open-problems@2a3b747c13a2c39364c59d93f9bb2192b78cde7c`, proves the balanced-cut self/cross resource theorem for any selected three large eigenvectors, retaining arbitrary extra spectrum. Its first unpaid branch is the mixed rank-budget profile (`1 self + 2 cross` or `2 self + 1 cross`) and rank-three-cross with heavy range.
3. The interactive regularized-determinant theorem, canonical package `math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, pays five general cross directions, or three cross directions under the stated fractional leverage condition, and proves the full-spectrum entire-range-diffuse branch.
4. This worker's preceding theorem `QFORM-DEPENDENT-AGGREGATE-HYPERBOLIC-SQUARE-v1`, canonical package `math-open-problems@23b520c19dd0e43cbff0fc0514a4dbfcd637b0f4`, proves

`||p_{2 alpha X Y + H(Y) + beta (Z+theta(Y))^2}||_infinity <= 6 M^(2/3)|alpha|^(-2/3)|beta|^(-1/3)`

when `X` is independent of `(Y,Z)`, `p_X<=1`, and the joint density of `(Y,Z)` is at most `M`.

The conditional full proof therefore reduces to a product-preserving extraction/aggregation theorem that turns the balanced self/cross resources into one already-paid analytic packet. A fixed physical minor, a self-or-cross rank-three dichotomy, generic X-ray control, or post-rotation independence cannot be used because those interfaces are already source-validly refuted.

This run closes one explicit local exception and derives a quantitative determinant bank for the remaining exact-rank-three mixed-leverage geometry.

## 2. New theorem: all-zero-diagonal invertible physical 3x3 blocks are paid

### `QFORM-ZERODIAG-3BLOCK-v1`

Let `X,Y,Z` be independent real random variables with densities bounded by one. Let

`B = [[0,a,b],[a,0,c],[b,c,0]]`

with `abc != 0`, so `det B = 2abc`. For arbitrary real affine coefficients `r,s,t,d`, define

`T = 2aXY + 2bXZ + 2cYZ + rX + sY + tZ + d`.

Then `T` has an essentially bounded density and

`||p_T||_infinity <= 6 |det B|^(-1/3)`.

Consequently, if an arbitrary larger quadratic form is conditioned on every original coordinate outside a physical triple whose principal `3x3` block has zero diagonal and nonzero determinant, the same bound applies uniformly in all outside coordinates and all outside couplings.

### Proof

Set

`u0 = aY+bZ`, `w = aY-bZ`, `u=u0+r/2`.

The linear map `(Y,Z)->(u,w)` has inverse

`Y=(u-r/2+w)/(2a)`, `Z=(u-r/2-w)/(2b)`

and Jacobian absolute value `1/(2|ab|)`. Since `Y,Z` are independent and each input density is at most one, `(u,w)` has a joint density bounded by

`M = 1/(2|ab|)`.

It remains independent of `X`.

Put

`kappa=c/(2ab)`,
`L=s/(2a)+t/(2b)`,
`N=s/(2a)-t/(2b)`.

Direct substitution gives the exact identity

`T = 2Xu + kappa[(u-r/2)^2-w^2] + L(u-r/2) + Nw + d`.

Complete the square in `w`:

`-kappa w^2 + Nw = -kappa (w-N/(2kappa))^2 + N^2/(4kappa)`.

Hence `T` is exactly of the preceding dependent aggregate hyperbolic-square form

`2 alpha X u + H(u) + beta(w+theta)^2`

with `alpha=1`, `beta=-kappa`, and constant `theta=-N/(2kappa)`. The theorem quoted in item 4 therefore gives

`||p_T||_infinity <= 6 M^(2/3)|kappa|^(-1/3)`.

But

`M^(2/3)|kappa|^(-1/3)
 = (2|ab|)^(-2/3) (2|ab|/|c|)^(1/3)
 = (2|abc|)^(-1/3)
 = |det B|^(-1/3)`.

This proves the claim.

### Sign and degeneracy checks

No sign restriction is used: the square coefficient `beta=-c/(2ab)` may have either sign. The only excluded case is `abc=0`, exactly the singular case `det B=0`. Affine terms are fully retained, so conditioning outside a physical triple is legitimate. No post-rotation independence is asserted: only the explicit two-dimensional linear change of the already independent pair `(Y,Z)` is used, and only its joint density cap is needed.

## 3. Application: closes the explicit scalar-pivot exception in account01/B11

The source-valid `account01/B11` handoff proves a universal bound for every invertible physical `3x3` block once a nonzero physical diagonal pivot is available, and explicitly leaves the all-zero-diagonal invertible block outside that mechanism. Theorem `QFORM-ZERODIAG-3BLOCK-v1` pays exactly this omitted case.

This does **not** imply that every target matrix contains a uniformly nondegenerate physical triple. The correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` already gives target matrices for which all such triples degenerate with dimension. The new theorem completes the *analytic* treatment of a good physical zero-diagonal triple; it does not manufacture that triple.

## 4. New exact structural identity: sequential-heavy determinant bank

### `QFORM-SEQUENTIAL-HEAVY-DETBANK-v1`

Let `A=U Lambda U^T` have exact rank three, where `U` is an `n x 3` orthonormal frame and `Lambda` is invertible symmetric. Choose a row `i` with

`c=||u_i||_2^2>0`.

Choose spectral coordinates with `u_i=(sqrt(c),0,0)`. For `j!=i`, let `p_j` be the projection of `u_j` onto the last two spectral coordinates. If `d=||p_j||_2^2>0`, rotate the last two spectral coordinates so that

`u_j=(rho,sqrt(d),0)`.

Write every remaining row as

`u_k=(r_k,s_k,w_k)`.

Then

`sum_{k notin {i,j}} |det A[{i,j,k},{i,j,k}]| = |det Lambda| c d`.    (4.1)

Indeed

`det U_{i,j,k}=sqrt(c d) w_k`,
`det A[{i,j,k}]=det Lambda (det U_{i,j,k})^2`,

and the third column of `U` has zero coordinates at `i,j` and unit norm, so `sum_k w_k^2=1`.

Consequences:

- In a target exact-rank-three form, `|det Lambda|>=1`; if `c>=alpha` and `d>=beta`, the total absolute physical-triple determinant mass through the fixed pair `(i,j)` is at least `alpha beta`.
- If every such triple has determinant `<delta`, then

`max_{k notin {i,j}} w_k^2 < delta/(|det Lambda| c d)`.

Thus after two levels of localization, failure of every good physical triple forces the *remaining spectral direction itself* to be quantitatively diffuse over the remaining original coordinates. This is an aggregate statement, not a selection of one minor.

## 5. First unpaid implication after the new pieces

The latest compatible account01/B19 result changes the synthesis residue to a mixed balanced-cut profile even with arbitrary extra spectrum. The exact unpaid implication can now be stated as follows.

### `QFORM-BALANCED-MIXED-AGGREGATION-v2` (OPEN)

There must exist universal constants `delta0,c0>0` such that for every target matrix `A`, after selecting any three eigenvectors with `|lambda|>=1` and applying the source-valid balanced-cut construction, every cut satisfying `G_H,G_L>=delta0 I_3` is paid by at least one of the following product-preserving mechanisms:

1. a general cross packet satisfying the regularized-determinant hypotheses;
2. a localized pivot whose rank-two Schur residual is diffuse, paid by account03/B19;
3. a physical `3x3` block with determinant at least `c0`, including the all-zero-diagonal case now paid by Theorem 2;
4. an aggregate hyperbolic-square or rectangular two-channel packet paid by this worker's preceding theorems; or
5. a quantitatively stated descent that preserves the selected-three spectral resource and reduces to one of 1--4.

The latest account01/B19 six-dimensional family refutes replacing this by the simpler statement “one self block or the cross block has rank three.” The earlier account02/B03 family refutes replacing 3 by a universal fixed-minor extraction. The new determinant-bank identity shows what remains when two localization levels are present: determinant mass cannot disappear; it spreads into a one-dimensional spectral tail. The missing theorem must convert that spread into smoothing without paying the reciprocal of one tiny minor.

A concrete next attack is therefore the `two-heavy + one-diffuse` exact-rank-three model generated by (4.1): prove that the diffuse tail plus the two localized original coordinates yields either a dependent aggregate hyperbolic-square packet or a regularized cross packet with a universal parameter. This is strictly narrower than the previous unstructured mixed-leverage residual.

## 6. Status and nonclaims

**Proved here:**
- `QFORM-ZERODIAG-3BLOCK-v1`, including all affine/outside-conditioned terms, with constant `6|det B|^(-1/3)`;
- `QFORM-SEQUENTIAL-HEAVY-DETBANK-v1`, an exact determinant-mass identity and quantitative diffuse-tail consequence.

**Applied peer result:** newest available named partner `account03/B19` critical rank-two `L^3` bridge and localized diffuse-residual theorem; newest compatible `account01/B19` balanced-cut self/cross resource theorem.

**Not proved:**
- the mixed balanced-cut aggregation implication;
- the two-heavy + one-diffuse smoothing step;
- a universal good physical minor;
- the full arbitrary-matrix conjecture;
- continuity in every direct small-ball branch.

No full-proof claim is made.

## 7. Source pins and corrections

Fresh brain main before publication: `34e2a175ceaf0c92bbec1d77e5e40dc9a1e749cf`, owner revision `2026-09-22.5`.

Consumed live corrections include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, and `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`.

No refuted interface is used as a premise.
