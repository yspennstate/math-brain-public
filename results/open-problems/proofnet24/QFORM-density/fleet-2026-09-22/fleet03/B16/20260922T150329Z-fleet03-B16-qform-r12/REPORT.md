# fleet03/B16 — conditional-product L3 and light-cone Schur smoothing

**Run:** `20260922T150329Z-fleet03-B16-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Projection-product interaction  
**Classification:** `PROVED_SUPPORTING_LEMMA / TARGET_RELEVANT_BRANCH / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and corrections used

The full target remains OPEN: for independent real variables `X_i` with densities `0<=f_i<=1` and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one universal finite bound on the density of `X^T A X`.

This report does **not** use law-uniform pointwise stationary phase, independence after rotation, receiver-only projection-density control, or a fiberwise indefinite trace bound. Those routes are explicitly corrected/refuted in the current programme state.

The completed partner mathematics actually used is fleet04/B18, scientific commit `441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`. Its dependent square-smoothing lemma proves the exact conditional square-kernel domination

`p_{R+aV^2}(t) <= |a|^{-1/2} int p_R(r) |t-r|^{-1/2} dr`

on the appropriate one-sided half-line whenever the conditional density of `V` given `R=r` is at most one. The present run extends that same inequality from an `L^infinity` base density to an `L^3` base density and couples it to an original-coordinate product estimate.

The designated fleet04/B16 handoff directory was absent at the fresh control snapshot, so no result is attributed to that slot.

## 2. Conditional-product L3 theorem

### Theorem 2.1 — `QFORM-CONDITIONAL-PRODUCT-L3-v1`

Let `Y` have a probability density `g` with `0<=g<=1`. For almost every `y`, suppose the conditional law of `W` given `Y=y` has a density `h_y` satisfying `0<=h_y<=1`. No independence of `Y` and `W` is assumed. For `c != 0`, put

`Z = c Y W`.

Then `Z` is absolutely continuous and

`||p_Z||_3 <= 6 * 2^(-1/3) * |c|^(-2/3)`.

In particular, for `c=2b`,

`boxed( ||p_{2bYW}||_3 <= 3 |b|^(-2/3) ).`

### Proof

Condition on `Y=y`. For `y != 0`, the conditional density is

`k_y(z) = |cy|^(-1) h_y(z/(cy))`.

It has mass one and essential supremum at most `|cy|^(-1)`. Therefore

`||k_y||_3^3 <= ||k_y||_infinity^2 ||k_y||_1 <= |cy|^(-2)`,

so

`||k_y||_3 <= |cy|^(-2/3)`.

Minkowski's integral inequality gives

`||p_Z||_3 <= |c|^(-2/3) int g(y)|y|^(-2/3) dy`.

Among all probability densities `0<=g<=1`, the last integral is maximized by the bathtub rearrangement on the centered interval of length one. Hence

`int g(y)|y|^(-2/3)dy <= int_{-1/2}^{1/2}|y|^(-2/3)dy = 6*2^(-1/3)`.

This proves the theorem. Notice that arbitrary `Y`-dependent translations of `W` are allowed.

## 3. L3-to-square L-infinity smoothing

### Theorem 3.1 — `QFORM-L3-DEPENDENT-SQUARE-SMOOTHING-v1`

Let `R` have probability density `p_R` with `||p_R||_3 <= M`. Suppose that for almost every `r`, the conditional law of `V` given `R=r` has a density at most one. For `a != 0`, put

`T = R + a V^2`.

Then `T` has an essentially bounded density and

`boxed( ||p_T||_infinity <= [8/3^(3/4)] |a|^(-1/2) M^(3/4) ).`

### Proof

The conditional square-density calculation from fleet04/B18 gives, after reflecting when `a<0`,

`p_T(t) <= |a|^(-1/2) int_0^infinity p_R(t-u) u^(-1/2) du`.

For any `H>0`, split at `H`. On `(0,H)`, Holder with exponents `3` and `3/2` gives

`int_0^H p_R(t-u)u^(-1/2)du
 <= M [int_0^H u^(-3/4)du]^(2/3)
 = 4^(2/3) M H^(1/6)`.

On `(H,infinity)`, probability normalization gives

`int_H^infinity p_R(t-u)u^(-1/2)du <= H^(-1/2)`.

Thus

`p_T(t) <= |a|^(-1/2)[4^(2/3) M H^(1/6)+H^(-1/2)]`.

The minimizing choice is

`H = [3/(4^(2/3)M)]^(3/2)`.

Substitution yields

`||p_T||_infinity <= [8/3^(3/4)] |a|^(-1/2) M^(3/4)`.

## 4. New light-cone Schur theorem for a fully ambient quadratic form

Let `I={i,j,k}` be three original independent coordinates. After conditioning on every coordinate outside `I`, write the physical `3 x 3` principal block in scalar-pivot form

`B = [[a, r^T],[r,C]]`,

with `a != 0`, and let

`S = C - rr^T/a`

be the `2 x 2` Schur complement in the **original residual coordinates**. Assume that, after merely permuting those two residual coordinates (no rotation),

`S = [[0,s],[s,c]]`,  with `s != 0`.

### Theorem 4.1 — `QFORM-LIGHTCONE-SCHUR-v1`

For arbitrary couplings of the chosen triple to all outside coordinates and arbitrary independent input densities bounded by one, the full quadratic form has an essentially bounded density satisfying

`boxed( ||p_Q||_infinity <= 8 / (|a det B|)^(1/4) ).`

### Proof

Fix the outside coordinates. Completing the square only in the pivot variable `Z` gives

`Q_w = a (Z + m_w(U,V))^2 + R_w(U,V)`,

where the quadratic part of `R_w` is exactly `S`. Thus

`R_w(U,V)=2sUV+cV^2+alpha U+beta V+gamma`.

Translate `V` by `alpha/(2s)` and absorb constants. With `Y=V+alpha/(2s)`,

`R_w = 2s Y [ U + (c/(2s))Y + delta ] + constant`.

Because `U` and `V` were independent original coordinates, `Y` has density at most one and, conditional on `Y=y`,

`W := U + (c/(2s))Y + delta`

is only a translation of `U`; hence its conditional density is at most one. Theorem 2.1 therefore gives, uniformly in the outside conditioning value,

`||p_{R_w}||_3 <= 3 |s|^(-2/3)`.

Now `Z` is independent of `(U,V)` before conditioning. Consequently, conditional on any value `R_w=r`, the variable

`Z+m_w(U,V)`

is a mixture of translations of the density of `Z`, and so its conditional density is still at most one. Theorem 3.1 applies with `M=3|s|^(-2/3)`:

`||p_{Q_w}||_infinity
 <= [8/3^(3/4)] |a|^(-1/2) [3|s|^(-2/3)]^(3/4)
 = 8 / sqrt(|as|).`

Since `det S=-s^2` and `det B=a det S`,

`(|a det B|)^(1/4)=sqrt(|as|)`.

Hence

`||p_{Q_w}||_infinity <= 8/(|a det B|)^(1/4)`.

The bound is uniform in the outside coordinates, so averaging the conditional densities proves the ambient statement.

## 5. Why this is target-relevant

This theorem covers a genuine indefinite Schur branch that the fleet04/B18 definite-Schur theorem does not cover. It also preserves the original product geometry exactly: the only transformations are coordinate translations, scalar completion of one physical pivot, and a translation of one residual physical coordinate. No residual rotation is used.

The result is especially relevant to a heavy-coordinate / light-cone configuration: if a physical pivot is quantitatively usable and the residual indefinite Schur form contains a physical null direction, the logarithmic rank-two singularity is paid in `L^3` and the pivot square upgrades it to `L^infinity`.

This is not the full conjecture. The remaining branch already appears when the indefinite Schur complement has **both physical diagonal entries nonzero**. A bounded joint projection density alone still cannot pay that trace, and the current theorem does not justify rotating the residual pair to an isotropic basis. A second unresolved issue is obtaining a dimension-free physical pivot/minor payment in delocalized matrices; the current regularized-determinant theorem handles the entire-range diffuse branch but does not yet provide the exhaustive heavy/light bridge.

## 6. Next attack

The next projection-product implication should be one of the following equivalent-strength advances:

1. prove a universal `L^3` bound for an arbitrary nondegenerate **indefinite binary quadratic polynomial** of two independent cap-one coordinates, with scale `|det S|^(-1/3)`, while allowing arbitrary linear terms; or
2. prove a perturbative extension of Theorem 4.1 when the nominally zero physical Schur diagonal is merely small relative to the cross coefficient, with a constant that remains finite as that diagonal passes through zero.

Either result would enlarge the scalar-pivot closure beyond the current exact light-cone branch without using any retired pointwise-Fourier claim.

## 7. Status

- `QFORM-CONDITIONAL-PRODUCT-L3-v1`: **PROVED**.
- `QFORM-L3-DEPENDENT-SQUARE-SMOOTHING-v1`: **PROVED**, using the exact conditional square kernel from fleet04/B18.
- `QFORM-LIGHTCONE-SCHUR-v1`: **PROVED supporting target branch**.
- Continuous representative for this full ambient branch: **not separately proved here**; the result establishes absolute continuity with an essentially bounded density.
- Full universal QFORM theorem: **OPEN**.
