# β-uniform one-hub square receiver with arbitrary joint planar light

Status: **proved scoped analytic theorem; overlapping third light projection remains open**. This is an elementary receiver for the exact three-variable core with zero hub square, retaining any real coefficient of `L²`. It makes no assumption that the two light coordinates are independent.

## Theorem

Let `H` have probability density `f_H≤1` and be independent of a random pair `(L,V)` with arbitrary joint density `g(l,v)≤M`, where `M>0`. For `t,λ∈R\{0}` and any `β∈R`, put
```
Q=2tHL+βL²+λV².
```
Then `Q` has an essentially bounded density satisfying
```
∥p_Q∥∞ ≤ 1/2 + (4sqrt(2)M)/(|t|sqrt(|λ|)).             (1)
```
In particular, `∥p_{2HL+βL²+V²}∥∞≤1/2+4sqrt(2)M` uniformly in `β`. Any deterministic affine term in `H,L,V` can be removed by translations because the 3-by-3 active quadratic core is invertible; these translations preserve the hub independence and the planar joint density cap. The statement does not include an additional random light term `2εLP` with `P` dependent on `(L,V)`.

### Mixed light term

The same bound covers `Q=2tHL+βL²+2εLV+λV²` for arbitrary `ε∈R`: set `V'=V+(ε/λ)L`. The light-only shear has determinant one, so `(L,V')` retains joint density cap `M` and remains independent of `H`. It changes `β` to `β−ε²/λ` and leaves `t,λ` unchanged. Hence (1) applies verbatim. In particular, a nominal third light projection `P` that actually lies in the span of `(L,V)` is paid by this two-dimensional receiver; genuinely transverse overlapping `P` remains outside its scope.

## Proof

The interval formulation below can be justified first by mollifying the output or by the standard change-of-variables density formula; all integrands are nonnegative, so Tonelli applies. Fix an output value `s` outside the usual null exceptional set, and split on `|L|>1/|t|`.

On this first region, condition on `(L,V)`. For `l≠0`, the map `h↦2tlh+βl²+λv²` has derivative `2tl`. Therefore the conditional output density is at most `1/(2|tl|)`, and integration over `|l|>1/|t|` costs at most `1/2`.

On `0<|l|≤1/|t|`, condition on `(H,L)` and use `g(l,v)≤M`. The two-branch square-map Jacobian yields, for any fixed `h,l`,
```
∫_R g(l,v) δ(s−2tlh−βl²−λv²)dv
 ≤ [M/sqrt(|λ|)] [sgn(λ)(s−2tlh−βl²)]_+^{−1/2}.
```
Here the expression is interpreted as zero when its argument is negative; its infinite value at zero affects a null set and the subsequent integration is finite. For fixed nonzero `l`, the expression inside the positive part is an affine function of `h` with slope of absolute value `2|tl|`. Since `0≤f_H≤1` and `∫f_H=1`, the bathtub bound for the decreasing one-sided inverse square-root kernel is
```
∫ f_H(h) [sgn(λ)(s−2tlh−βl²)]_+^{−1/2}dh
 ≤∫_0^1 (2|tl|u)^{−1/2}du
 =sqrt(2/(|tl|)).
```
This estimate is independent of `s`, `β`, and the support of the hub law. Integrating over `|l|≤1/|t|` gives
```
(M/sqrt(|λ|))∫_{|l|≤1/|t|}sqrt(2/(|tl|))dl
 =4sqrt(2)M/(|t|sqrt(|λ|)).
```
Add the first region. This proves (1). Bounded interval probabilities follow by integrating the resulting a.e. density bound; no continuity assertion is needed.

To remove an arbitrary affine function `a_HH+a_LL+a_VV+a_0`, first note that the active matrix `[[0,t,0],[t,β,0],[0,0,λ]]` has determinant `−t²λ≠0`. Its critical-point translation shifts `H` by a scalar and `(L,V)` by a fixed vector; it does not mix the hub with light variables, so their independence and caps survive.

## Scope in the exact-rank-three structural split

If a physical hub is independent of a two-dimensional light projection `(L,V)`, this theorem pays the `a=0` core, including arbitrary `βL²` and deterministic affine terms. The [general small-hub-square four-region receiver](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T191000Z-small-hub-square-coarea/GENERAL_3D_CORE.md) separately covers a normalized `|a|<1/64` with `s_3(T)≥1` for **any** active 3-by-3 quadratic core. The present estimate does not require a spectral normalization on `β`; it requires an explicit nonzero hub/light cross coefficient `t` and a nonzero light square `λ`.

Neither theorem establishes density stability under a third light projection `P` that overlaps the originals defining `(L,V)`. This is the genuine near-coloop leakage gap.
