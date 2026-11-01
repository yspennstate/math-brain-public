# A countable extreme-product-law test class for the QFORM density conjecture

Status: proved reduction; **no universal density bound follows from this reduction alone**. This is a finite-interval refinement of the existing nonattained coordinatewise purification in [fleet04/B13](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260923T121154Z-fleet04-B13-nonattained-bathtub-r1/REPORT.md), §2–3. In particular, we do not claim the earlier bathtub lemma as new.

## Statement

Fix a finite dimension `n`, any nonconstant real polynomial `q(x)` (especially `q(x)=x^T A x+b^T x+c`), and a bounded interval `I` of positive length. Let `F` be the class of densities `0≤f≤1`, `∫_R f=1`. Let `U` be the class of indicators of finite unions of bounded intervals with total length exactly one, and `U_Q` the subclass whose interval endpoints are rational. Then

```
sup_{f_1,...,f_n ∈ F} P_f{q(X)∈I}
 = sup_{u_1,...,u_n ∈ U} ∫ 1_{q(x)∈I} ∏_i u_i(x_i) dx
 = sup_{u_1,...,u_n ∈ U_Q} ∫ 1_{q(x)∈I} ∏_i u_i(x_i) dx.       (1)
```

Neither supremum is asserted to attain its value. The same equality holds with **any bounded measurable kernel** `0≤K(x)≤1` in place of the slab indicator. The polynomial assumption is used below only to establish interval-boundary null and continuity when coefficients/interval endpoints are approximated.

Consequently, if an interval estimate `P{q(X)∈I}≤C|I|` is established for **all** products of unit-length finite rational interval unions in the original physical coordinates, it holds with the same `C` for all independent cap-one input laws. This does not assert that each optimal unit set consists of one interval, nor that a density estimate is stable under perturbing `A`.

## Nonattained coordinatewise extremization

For any measurable `k:R→[0,1]`, the infinite-line bathtub identity is

```
sup_{0≤f≤1, ∫f=1} ∫ kf = sup_{|E|=1} ∫_E k.                  (2)
```

This is proved without assuming a maximizing threshold: truncate the line to bounded sets, approximate `k` from below by a bounded-support simple function, fill its cells in descending order (add arbitrary outside mass if necessary), and take monotone limits. See the cited B13 proof, Lemma 2.1, which also permits general nonnegative `k`. For fixed other marginals, integrating `K` over them yields a measurable `k_i(x_i)∈[0,1]`. Replace `f_i` successively by `1_{E_i}` with conditional loss at most `ε/n` at each coordinate. Since each replacement leaves a product law and (2) is a supremum identity, the final product indicator has value at least the starting law's value minus `ε`. Send `ε↓0`. This is precisely the established B13 purification theorem; it does not require attainment.

## Approximation by finite rational interval unions

Lebesgue regularity gives: for each measurable `E⊂R` with `|E|=1` and each `η>0`, there is a finite union `F_0` of bounded intervals such that `|E△F_0|<η`. To see finiteness directly, choose a compact `K⊂E` with `|E\K|<η/2`, then a bounded open `O⊃K` with `|O\K|<η/2`; cover `K` by finitely many interval components of `O` and use their union as `F_0`. This allows `E` itself to be unbounded. If `|F_0|<1`, append a bounded interval disjoint from `F_0` with length `1−|F_0|`; if `|F_0|>1`, remove a finite union of subintervals of combined length `|F_0|−1`. The resulting finite union `F` has `|F|=1` and
```
|E△F| ≤ |E△F_0| + ||F_0|−1| < 2η.                           (3)
```
Thus the finite-union unit indicators are dense in all unit indicators in `L¹(R)`.

For a fixed finite disjoint union of positive-length bounded intervals `F` of total length one, rationally perturb the first `m−1` pairs of endpoints and the last left endpoint, preserving the positive lengths and gaps, and set the last right endpoint to
```
last left endpoint + 1 − (sum of the first m−1 perturbed lengths).
```
It is rational, remains close to the original right endpoint, and makes the total length **exactly one**. For `m=1`, choose a rational left endpoint and add one. Hence finite rational interval unions of exactly unit total length are also `L¹` dense.

If `0≤K≤1` and the other marginals are probability densities, replacing `1_E` by `1_F` in one coordinate changes its product expectation by at most `|E△F|`. A telescoping replacement across `n` coordinates costs at most `Σ_i|E_i△F_i|`; choose each error arbitrarily small. This proves (1).

Because `q` is nonconstant, the polynomial zero sets `{q=s}` and `{q=t}` have `n`-dimensional Lebesgue measure zero. Thus every absolutely continuous product law assigns zero mass to either endpoint of `I=[s,t]`; open/closed conventions agree. This boundary-null observation is **not needed** for the `L¹` approximation above.

## Fully countable global testing version

Let `q(x)=x^T A x+b^T x+c`, with `A=A^T` and third singular value `s_3(A)≥1`; let `n≥3`. Define the global slab ratio `R=P\{q(X)∈I\}/|I|`, allowing arbitrary real coefficients, bounded intervals of positive length, and independent cap-one densities. Its supremum equals the supremum after restricting to:

* rational symmetric `A` with `s_3(A)≥1`, rational `b,c`;
* intervals `I=[s,t]` with rational `s<t`;
* each input uniform on a **finite union of bounded rational intervals of total length one**.

Indeed, fix an arbitrary witness and an error. Apply (1) first, obtaining bounded product supports and a ratio as close as desired. Multiply `q` and both interval endpoints by `1+α`, where positive rational `α` is arbitrarily small: the event is unchanged, its ratio is divided by `1+α`, and `s_3((1+α)A)≥1+α`. Approximate all coefficients of the scaled polynomial by rational numbers, preserving `s_3≥1` by the strict gap. Approximate both interval endpoints by rationals while keeping their order and length positive. On the now bounded product support, the polynomials converge uniformly, and the event indicators converge almost everywhere except on the two zero sets of the scaled nonconstant polynomial. Dominated convergence gives convergence of probabilities, and the interval lengths also converge. Thus the rational witness approaches the original ratio arbitrarily closely. The reverse supremum inequality is immediate because rational witnesses are admissible.

The statement also covers a homogeneous-only target by taking `b=c=0` throughout; rational approximation preserves that restriction. One may enumerate this countable class to search for counterexamples. There is no implication that any fixed finite search depth proves a uniform estimate.

## Scope

The reduction preserves the original physical-coordinate product structure. It permits disconnected, arbitrarily distant support intervals, and has no uniform bound on the number of components or their location. It cannot justify replacing a complicated marginal by a single interval, clipping far-away support, or discarding a low-rank leakage term. In particular, the diffuse high-leverage rank-three branch remains unresolved.
