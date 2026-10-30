# fleet04/B18 — Schur-pivot square smoothing for fully coupled quadratic blocks

**Run:** `20260922T113729Z-fleet04-B18-qform-r1`  
**Owner control:** revision `2026-09-22.5` (later redirect; supersedes the FEI assignment)  
**Classification:** `ESSENTIAL_STEP_APPLIED / COUPLED_BLOCK_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and source state

The active target is the universal bounded-density conjecture for quadratic forms: independent real variables have densities at most one, and a real symmetric quadratic form has at least three eigenvalues of magnitude at least one. The goal is one density bound independent of the dimension, input laws, and form.

This run uses two completed source-valid inputs.

1. fleet01/B08, scientific commit `b2c957c85ef2209345efc63e1357b075fe32a845`, proves the one-square endpoint and the coordinate-diagonal theorem, and refutes law-uniform pointwise Fresnel decay.
2. fleet04/B15, scientific commit `b7da5d28befd49f3a773ca376576d34824138d7e`, proves that a definite physical `2 x 2` principal block `S` gives density at most `pi/sqrt(det S)`, while Hadamard examples rule out extracting one uniformly nondegenerate physical pair from the spectral hypothesis.

A fresh result completed during this run: fleet02/B15, scientific commit `d5392d73398e2811f58b612fb8f191aa79d8ee5e`, proves the general physical-principal-triple estimate `||p_Q||_infinity <= (2pi+3sqrt(3))/sigma_min(B)`. The theorem below is not needed for mere boundedness when one such triple is already quantitatively nonsingular; instead it gives a sharper determinant-sensitive constant, a reusable dependent-smoothing lemma, and an exact inertia branch. On the explicit block in Section 4, the fleet02/B15 constant is below `11.48`, whereas the new bound is `2sqrt(pi)/(1+sqrt(2))<1.47`.

The result below uses the B15 elliptic estimate as a base density and adds a third, fully coupled coordinate without assuming independence after completing the square.

## 2. Dependent square-smoothing lemma

### Lemma 2.1 — `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`

Let `R` be a real random variable with density `p_R` satisfying

`||p_R||_infinity <= M`.

For almost every `r`, let `V_r` be a real random variable whose conditional density `h_r` satisfies `||h_r||_infinity <= 1`. No independence between `R` and `V_R` is assumed. If `a != 0` and

`T = R + a V_R^2`,

then `T` is absolutely continuous and

`boxed( ||p_T||_infinity <= 2 sqrt(M/|a|) ).`

### Proof

Assume first `a>0`. Conditional on `R=r`, the density `k_r` of `aV_r^2` is, for `y>0`,

`k_r(y) = [h_r(sqrt(y/a))+h_r(-sqrt(y/a))]/[2 sqrt(a y)] <= 1/sqrt(a y).`

Therefore

`p_T(t) <= a^(-1/2) integral_{r<t} p_R(r) (t-r)^(-1/2) dr.`

Among all functions `0<=p<=M` of mass at most one, the last integral is maximized by filling the decreasing kernel next to `t`. The bathtub principle gives

`integral_{r<t} p(r)(t-r)^(-1/2)dr
 <= M integral_0^(1/M) u^(-1/2)du = 2 sqrt(M).`

This proves the result for `a>0`. For `a<0`, reflect the output and integrate over `r>t`; the same calculation applies. The displayed domination also constructs an `L^infinity` density for `T`. QED.

The point is that the square variable may be translated by a random amount depending on the base variable. Only the conditional density cap survives; convolution independence is unnecessary.

## 3. Main theorem: scalar pivot with definite Schur complement

Let `I={i,j,k}` be three original independent coordinates and write their principal block, after ordering `k` first, as

`B = [[a, b^T],[b,C]]`,

where `a != 0`, `b in R^2`, and `C` is symmetric `2 x 2`. Define the Schur complement

`S = C - b b^T/a.`

### Theorem 3.1 — `QFORM-SCHUR-PIVOT-SMOOTHING-v1`

Suppose `S` is positive definite or negative definite. For independent real `X_1,...,X_n` with densities bounded by one and arbitrary real symmetric ambient matrix `A` whose principal block on `I` is `B`, the full quadratic form `Q=X^TAX` has a density satisfying

`boxed(
 ||p_Q||_infinity
 <= 2 sqrt(pi) / ( |a| |det B| )^(1/4).
)`

All couplings from the selected triple to the remaining coordinates are arbitrary.

### Proof

Condition on all coordinates outside `I`. They generate only linear and constant terms. Denote the scalar selected variable by `Z` and the other two by `U in R^2`. For every fixed outside value `w`, completing the square only in `Z` gives

`Q_w(Z,U)
 = a ( Z + m_w(U) )^2 + R_w(U),`

where `m_w` is affine and `R_w` is a quadratic polynomial whose quadratic matrix is exactly `S`.

By the definite physical-pair theorem, `R_w(U)` has a density bounded uniformly in `w` by

`M = pi/sqrt(|det S|).`

Disintegrate the law of `U` over the value `R_w(U)=r`. Because `Z` is independent of `U` before conditioning, the conditional law of

`V_r = Z + m_w(U)`

is a mixture of translations of the density of `Z`. Hence it has a density bounded by one for almost every `r`. Lemma 2.1 applies even though `V_r` depends on `r`, and yields

`||p_{Q_w}||_infinity
 <= 2 sqrt( pi / ( |a| sqrt(|det S|) ) ).`

Since `det B = a det S`, this is

`2 sqrt(pi)/( |a| |det B| )^(1/4).`

The bound is uniform in the outside conditioning value. Averaging the conditional densities preserves it, proving the theorem. QED.

### Inertia interpretation

For an indefinite `3 x 3` block with inertia `(2,1)`, the hypothesis holds whenever the pivot `a` has the minority sign: Sylvester inertia additivity gives a positive-definite Schur complement. The order-dual statement holds for inertia `(1,2)`. Thus the theorem pays every physical triple with a minority-sign diagonal pivot, quantitatively in `|a det B|`.

If `|a|>=1` and `|det B|>=1`, the explicit bound is

`||p_Q||_infinity <= 2 sqrt(pi).`

## 4. Strictly new fully coupled target example

The theorem is not contained in either the definite-pair theorem or the pure hyperbolic-pair-plus-square normal form. Let

`B0 = [[-1,1,1],[1,0,-1],[1,-1,0]].`

Its scalar pivot is `a=-1`, its Schur complement is `I_2`, and `det B0=-1`. Every physical `2 x 2` principal determinant equals `-1`, so there is no definite physical pair. All three off-diagonal entries are nonzero, so no permutation gives the decoupled block `2aXY+lambda Z^2`.

The characteristic polynomial factors as

`(lambda-1)(lambda^2+2lambda-1)`,

so the eigenvalues are `1,-1+sqrt(2),-1-sqrt(2)`. Scale by `c=1+sqrt(2)` and put `B=cB0`. Its eigenvalue magnitudes are

`1, 1+sqrt(2), 3+2sqrt(2),`

so it meets the owner's three-large-eigenvalue threshold exactly. Yet it still has no definite physical pair and no decoupled hyperbolic-plus-square block. The theorem gives

`boxed( ||p_{X^T B X}||_infinity <= 2 sqrt(pi)/(1+sqrt(2)) ).`

This is a genuine fully coupled three-dimensional instance of the target.

## 5. Exact boundary and unpaid implication

The theorem does not close the full conjecture. The exact uncovered `3 x 3` sign branch is visible already in the Hadamard-type matrix

`H=[[1,1,1],[1,1,-1],[1,-1,1]],`

which has inertia `(2,1)` but all three diagonal entries have the majority sign. No scalar pivot has the minority sign, so every scalar Schur complement is indefinite. This is also the geometry in which fixed definite-pair extraction can fail.

The first unpaid implication is therefore narrower than generic rotation-stable Fourier decay:

> control a fully coupled physical `3 x 3` block of inertia `(2,1)` or `(1,2)` when every nonzero diagonal pivot has the majority sign, or aggregate such blocks across coordinate charts without selecting one minor. The argument must survive flat Hadamard eigenvectors and cannot use the refuted law-uniform pointwise Fresnel estimate.

The full arbitrary-dimensional conjecture remains open. No easy subclass is promoted as a solution.

## 6. Status

* `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`: proved.
* `QFORM-SCHUR-PIVOT-SMOOTHING-v1`: proved.
* Fully coupled scaled `B0` target instance: covered with explicit constant.
* Full universal theorem: open / not proved.
