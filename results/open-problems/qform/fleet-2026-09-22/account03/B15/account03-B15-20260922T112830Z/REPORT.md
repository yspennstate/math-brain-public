# account03/B15 — bounded-density quadratic form: exact extremal product-set reduction

Status: **PROVED auxiliary reduction; full conjecture OPEN.**

Control revision used: `2026-09-22.4`. The later owner message supersedes the preceding FEI assignment and directs all work to the bounded-density quadratic-form conjecture. Execution status: `WITHOUT_VERIFIED_BRAIN`.

## Target

Let `X_1,...,X_n` be independent real random variables with densities `f_i` satisfying `0 <= f_i <= 1` and `\int f_i=1`. Let `Q(x)=x^T A x`, with `A` real symmetric and at least three eigenvalues of absolute value at least one. The owner target asks for a universal `C` such that the law of `Q(X)` has density at most `C`, independent of dimension, the coordinate laws and `A`.

## Consumed completed peer result

I consume the completed `account03/B17` handoff `account03-B17-20260922T112131Z` (brain commit `5a060b9340b64e27474a5d95d7b4782cfb894382`). It proves two facts used here:

1. the proposed law-uniform one-direction oscillatory estimate is false:
   `sup_{0<=f<=1, int f=1} |int exp(i s x^2) f(x) dx| = 1` for every fixed `s != 0`;
2. the full coordinate-diagonal subclass is closed with the explicit bound `||p_Q||_infty <= pi`, by selecting two same-sign large diagonal coefficients.

Thus a replacement route should work directly at the small-ball/sublevel-set level rather than require a false law-uniform pointwise Fourier envelope.

## Theorem A — exact bathtub/product-set reduction

Let `K:R^n -> [0,1]` be any measurable kernel and

`F = { f:R-> [0,1] measurable : int_R f = 1 }`.

Then

```text
sup_{f_1,...,f_n in F} int K(x) prod_i f_i(x_i) dx
 =
sup_{E_1,...,E_n measurable, |E_i|=1}
    int K(x) prod_i 1_{E_i}(x_i) dx.
```

The right side may equivalently be restricted to **bounded finite unions of intervals** of total length one, with `sup` understood in the approximation sense.

### Proof

Fix all coordinates except `i`. Define

`h_i(t) = int K(x_1,...,x_{i-1},t,x_{i+1},...,x_n) prod_{j != i} f_j(x_j) dx_{-i}`.

Because `0<=K<=1` and every other factor has integral one, `0<=h_i<=1`.

For any measurable `h:R->[0,1]` and any `f in F`, layer cake gives

```text
int f h
 = int_0^1 int_{h>s} f(x) dx ds
 <= int_0^1 min(1, |{h>s}|) ds.
```

The right side is exactly the bathtub supremum

`sup_{|E|=1} int_E h`, 

with arbitrary epsilon-approximation sufficient if a maximizer is not attained. Therefore `f_i` may be replaced by an indicator `1_{E_i}`, `|E_i|=1`, without decreasing the multilinear objective by more than an arbitrarily prescribed error. Iterate over `i=1,...,n`, allocating error `eta/n` to each replacement, and then let `eta downarrow 0`. The reverse inequality is immediate because every unit-measure indicator belongs to `F`. This proves the first equality.

For the bounded finite-union reduction, first truncate any unit-measure `E_i` so that all but `delta` of its measure lies in a bounded interval, then add a bounded measurable set of the missing measure. Approximate that bounded measurable set in symmetric difference by a finite union of intervals. The multilinear functional is Lipschitz in the factors:

```text
|T(E_1,...,E_n)-T(F_1,...,F_n)|
 <= sum_i |E_i triangle F_i|,
```

by telescoping the products and using `K<=1` and unit measure of the untouched factors. Hence the supremum is unchanged.

## Corollary B — exact geometric form of the conjecture

For an interval `I`, take `K_I(x)=1_{Q(x) in I}`. The target conjecture is **equivalent** to the following purely geometric statement:

```text
There exists a universal C such that, for every n, every admissible A,
every interval I, and every measurable E_1,...,E_n with |E_i|=1,

| { x in E_1 x ... x E_n : Q(x) in I } | <= C |I|.
```

Moreover it is enough to prove this when every `E_i` is a bounded finite union of intervals.

### Proof of equivalence

Theorem A shows that for each fixed interval `I`, the largest possible probability `P(Q(X) in I)` over all admissible independent coordinate densities equals the product-set shell-volume supremum above. If the geometric inequality holds, then the pushforward probability measure `nu` of `Q(X)` satisfies `nu(I)<=C|I|` for every interval. Hence `nu<=C Lebesgue` as measures (by the standard interval domination/outer-regularity argument), so `nu` is absolutely continuous and its Radon–Nikodym derivative is at most `C` almost everywhere. The converse is immediate from the indicator densities `f_i=1_{E_i}`.

## Corollary C — extremal-coordinate threshold condition

If a product set `(E_i)` is an exact coordinatewise maximizer for a fixed kernel `K`, define its section score

`h_i(t)=int K(t,x_{-i}) prod_{j!=i} 1_{E_j}(x_j) dx_{-i}`.

Then there is a threshold `a_i` such that, modulo null sets,

```text
h_i >= a_i on E_i,
h_i <= a_i off E_i,
```

with arbitrary choice on the tie level `h_i=a_i` needed to make `|E_i|=1`. Thus any genuine extremal counterconfiguration must satisfy a simultaneous bathtub fixed-point condition in all coordinates.

This does not prove compactness or existence of a global maximizer; it is a necessary condition for an attained coordinatewise extremizer.

## General bounded-density variant

For coordinate bounds `0<=f_i<=M_i` and `int f_i=1`, the same proof gives

```text
sup int K prod_i f_i
 = (prod_i M_i)
   sup_{|E_i|=1/M_i} int_K prod_i 1_{E_i}.
```

This is the exact normalization statement. No unsupported linear-in-`M` scaling of the quadratic-form density is inferred from it.

## Application of the peer diagonal theorem

The consumed B17 theorem now becomes the exact geometric benchmark

```text
| {x in prod E_i : sum_j lambda_j x_j^2 in I} | <= pi |I|
```

for arbitrary unit-measure measurable `E_i` whenever at least three diagonal coefficients satisfy `|lambda_j|>=1`. Indeed among three coefficients two have the same sign; the two-term square convolution has `L^infty` norm at most `pi`, and all remaining independent terms act by convolution and cannot increase `L^infty`.

## Why this is useful for the full rotated problem

The live owner Fourier skeleton cannot be used with a law-uniform per-direction `|t|^{-1/2}` bound; the consumed peer result disproves that intermediate claim even before eigenvector coupling. Theorem A removes arbitrary density shapes from the remaining quantifiers altogether. The unresolved theorem is now a dimension-free **quadratic shell-volume estimate for Cartesian products of one-dimensional unit-measure sets**, with the rotation of the spectral directions relative to those products as the sole geometric difficulty.

This reduction also shows that a source-valid counterexample, if one exists, can be approximated arbitrarily well at the decisive interval by independent uniforms on bounded finite unions of intervals. That gives a finite geometric search/certification target without changing the conjecture.

## Remaining implication

**OPEN:** prove a universal `C` in Corollary B when the eigendirections are arbitrarily rotated relative to the coordinate product structure, under only the assumption that at least three eigenvalues satisfy `|lambda|>=1`.

Promising next mechanisms are product-set shell geometry, nonlinear Brascamp–Lieb/sublevel estimates, or an averaging argument over coordinate sections that uses the exterior-cube mass of the three-large-eigenvalue spectral subspace. Any such step must survive the two-opposite-eigenvalue logarithmic control case and must not reintroduce the refuted law-uniform pointwise Fourier decay.
