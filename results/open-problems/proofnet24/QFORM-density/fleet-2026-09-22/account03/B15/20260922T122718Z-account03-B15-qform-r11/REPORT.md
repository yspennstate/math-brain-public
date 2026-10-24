# account03/B15 — exact extremal transfer for the L-infinity target, with a separate continuity transfer theorem

**Run:** `20260922T122718Z-account03-B15-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
**Assignment:** Absolute continuity and regularity  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL-REDUCTION / FULL_TARGET_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and corrections retained

The owner target is: for every `n`, independent real random variables `X_i` with measurable densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^T A X` has an essentially bounded density with one universal finite constant, or give a valid counterexample. No continuity of the input densities is assumed.

The stronger requested conclusion that the output density have a continuous representative is logically separate. This report keeps that separation throughout.

Current corrections are respected: the law-uniform pointwise quadratic Fourier-decay claim is false; rotation does not preserve independence; naive fiber suprema can lose dimension; a cross-minor alone is not enough; and the universal constant is not known to be `pi`.

Two completed peer results are consumed.

1. `account04/B15`, canonical source `yspennstate/math-open-problems@1d658cd8ef6386a8f8ef7e6b9aaf26fdafe68de3`, proves (among other things) that interval domination is exactly equivalent to an `L^infinity` density, and separates continuity from boundedness by a Steklov criterion.
2. `account01/B13`, canonical source `yspennstate/math-open-problems@f5c63b29011eb394cd621ecc887fe3331aa485af`, proves that the admissible one-dimensional density class
   `D={f in L1(R): 0<=f<=1, int f=1}`
   is the `L1`-closed convex hull of indicators `1_E` of measurable sets of Lebesgue measure one, and therefore product laws are TV limits of finite convex mixtures of product-indicator laws. Its finite-fragment localization, through the cited account04/B14 result, allows the extreme sets to be taken as bounded finite unions of intervals.

The new point below is that the **actual extended output `L^infinity` functional itself** satisfies the convexity and TV-lower-semicontinuity hypotheses of that extremal theorem. Thus the reduction applies directly to the owner's bounded-density target, not merely to an auxiliary Fourier functional.

---

## 2. Extended density constant on arbitrary output measures

For a finite positive Borel measure `mu` on `R`, define

`M(mu) = sup{ mu(I)/|I| : I is a nonempty bounded open interval }`,

with values in `[0,+infinity]`.

### Lemma 2.1 — exact identification with the `L^infinity` density norm

`M(mu)<infinity` if and only if `mu=p dx` for some `p in L^infinity(R)`. In that case

`M(mu)=||p||_infinity`.

### Proof

If `mu=p dx` and `||p||_infinity<=C`, then `mu(I)<=C|I|` for every interval, hence `M(mu)<=C`.

Conversely, suppose `M(mu)=C<infinity`. Every open set in `R` is a countable disjoint union of open intervals, so `mu(O)<=C|O|` for every open `O`. By outer regularity, for every Borel set `B`,

`mu(B)<=C |B|`.

Hence `mu<<dx`, and its Radon-Nikodym derivative satisfies `0<=p<=C` almost everywhere. Therefore `||p||_infinity<=C`. The reverse inequality follows from the Lebesgue differentiation theorem: at almost every point where `p` is within `epsilon` of its essential supremum, sufficiently small interval averages are within `epsilon` of that value. Thus `M(mu)=||p||_infinity`. `QED`.

This lemma already keeps absolute continuity and essential boundedness together at the exact strength needed by the central target. It does not assert continuity.

### Lemma 2.2 — convexity and TV lower semicontinuity

The map `M` is convex on finite positive measures and lower semicontinuous for total-variation convergence.

### Proof

For `0<=theta<=1`, every interval `I` gives

`[theta mu+(1-theta)nu](I)/|I| <= theta M(mu)+(1-theta)M(nu)`.

Taking the supremum proves convexity.

For a fixed interval `I`, the map `mu -> mu(I)/|I|` is continuous in total variation because

`|mu(I)-nu(I)| <= ||mu-nu||_TV`.

`M` is the supremum of these continuous functions, hence is TV lower semicontinuous. `QED`.

---

## 3. Exact extremal reduction for the owner's bounded-density conjecture

Fix `n` and a real symmetric matrix `A`, and let

`Q_A(x)=x^T A x`.

For `f=(f_1,...,f_n) in D^n`, write

`mu_{A,f} = (Q_A)_# [prod_i f_i(x_i) dx]`.

For measurable sets `E_i` of measure one, write `mu_{A,E}` for the corresponding product-indicator input law.

### Theorem 3.1 — `QFORM-LINFINITY-EXTREME-TRANSFER-v1`

For every fixed `n` and `A`,

`sup_{f_1,...,f_n in D} M(mu_{A,f})
 = sup_{|E_1|=...=|E_n|=1} M(mu_{A,E}).`

Equivalently, interpreting a singular or unbounded-density output as value `+infinity`,

`sup_{f_i in D} ||p_{A,f}||_infinity^ext
 = sup_{|E_i|=1} ||p_{A,E}||_infinity^ext.`

Moreover, using the completed finite-fragment localization consumed through account01/B13, the right-hand supremum is unchanged when each `E_i` is restricted to a bounded finite union of intervals of total length one.

### Proof

The `>=` direction is immediate because indicators of measure-one sets belong to `D`.

For the other direction, account01/B13 gives, for each marginal `f_i`, finite convex combinations

`f_i^(m)=sum_j alpha_{i,j}^{(m)} 1_{E_{i,j}^{(m)}}`

with `|E_{i,j}^{(m)}|=1` and `||f_i^(m)-f_i||_1 ->0`. Tensorization gives product measures converging in total variation:

`|| tensor_i f_i^(m) dx - tensor_i f_i dx ||_TV ->0`.

Expanding the finite product mixture shows that the approximating product law is a finite convex combination of product-indicator laws. Pushforward by the measurable map `Q_A` contracts total variation, so the output measures `mu_m` converge in TV to `mu_{A,f}`.

By convexity of `M`,

`M(mu_m) <= sup_E M(mu_{A,E}).`

By TV lower semicontinuity,

`M(mu_{A,f}) <= liminf_m M(mu_m)
 <= sup_E M(mu_{A,E}).`

Taking the supremum over `f` proves equality. The finite-fragment restriction is exactly the localization supplied in the consumed extremal theorem. `QED`.

### Corollary 3.2 — exact reformulation of the full central target

Let `A_n` range over all real symmetric matrices having at least three eigenvalues with absolute value at least one. Then the smallest possible universal density constant, allowing `+infinity`, is exactly

`C_* = sup_{n>=1} sup_{A in A_n} sup_{E_i finite-fragment, |E_i|=1} M(mu_{A,E}).`

Therefore the full bounded-density conjecture is true with universal constant `C` **if and only if** the interval small-ball estimate

`P(Q_A(X) in I) <= C |I|`

holds for every target-admissible `n,A`, every interval `I`, and every input whose coordinates are independent uniforms on arbitrary bounded finite unions of intervals of total length one.

No regularity, connectedness, centering, or single-interval assumption is introduced. Fragmentation complexity and separation remain unbounded. In particular, this result does not revive the refuted pointwise Fourier-decay route.

This is a target-level reduction: arbitrary measurable coordinate densities `<=1` create no larger `L^infinity` obstruction than extreme product-indicator laws.

---

## 4. Absolute continuity and essential boundedness are now sharply separated from continuity

The preceding theorem, together with account04/B15's interval-domination equivalence, yields the following exact implication.

### Corollary 4.1 — extreme small-ball theorem implies full AC plus essential boundedness

Suppose one proves, for some finite `C`, that every target-admissible `A` and every product-indicator input satisfies

`mu_{A,E}(I)<=C|I|`

for every interval `I`. Then for **every** admissible collection of merely measurable coordinate densities `0<=f_i<=1`, the law of `Q_A(X)` is absolutely continuous and has a Radon-Nikodym derivative `p_Q` with

`||p_Q||_infinity<=C`.

No separate Fourier inversion, output regularity assumption, or continuity of any `f_i` is needed.

This directly attacks the central unpaid implication by reducing it to the finite-fragment extreme class. The still-unpaid mathematics is the dimension-free interval estimate on that class for fully rotated/indefinite `A`.

---

## 5. Stronger continuous-representative conclusion: a separate transfer theorem

The preceding convex/lower-semicontinuous argument **does not** transfer continuity. Continuity needs a compactness input stronger than a common `L^infinity` bound.

The correct companion statement is an equicontinuity transfer.

### Theorem 5.1 — `QFORM-CONTINUITY-MODULUS-EXTREME-TRANSFER-v1`

Fix `n,A`. Assume there are a finite `C` and a modulus `omega:[0,infinity)->[0,infinity)` with `omega(r)->0` as `r downarrow0` such that every product-indicator output `mu_{A,E}` has a continuous density `p_{A,E}` satisfying

`||p_{A,E}||_infinity<=C`

and

`|p_{A,E}(s)-p_{A,E}(t)| <= omega(|s-t|)`

for all real `s,t`, with the same `C,omega` for all measure-one sets `E_i`.

Then every admissible product density `f_i in D` produces a continuous density `p_{A,f}` with the same two estimates.

The same conclusion holds if the hypothesis is verified only on the bounded finite-fragment extreme class, provided the consumed localization approximation preserves the stated common modulus on the approximating extreme outputs.

### Proof

Approximate the product input in TV by finite convex mixtures of product-indicator laws as in Theorem 3.1. Let the output densities be `p_m`. Each `p_m` is a finite convex combination of the extreme densities, hence

`||p_m||_infinity<=C`

and

`|p_m(s)-p_m(t)|<=omega(|s-t|)`.

Thus `{p_m}` is uniformly bounded and equicontinuous on every compact interval. By Arzela-Ascoli and a diagonal extraction, some subsequence converges locally uniformly to a continuous function `p`, with the same bound and modulus.

At the same time the output measures converge in total variation to `mu_{A,f}` because input TV convergence survives measurable pushforward. Hence for every compactly supported continuous test function `psi`,

`int psi p_m dx -> int psi d mu_{A,f}`.

Along the locally uniformly convergent subsequence, the left side also converges to `int psi p dx`. Therefore `mu_{A,f}=p dx`. The inherited estimates follow from local uniform convergence. `QED`.

### Why this is genuinely stronger than the bounded-density transfer

It is false in general that TV limits of continuous densities with a common `L^infinity` bound have continuous densities. For example, if `rho_epsilon` is a standard smooth approximate identity, then

`p_epsilon = 1_[0,1] * rho_epsilon`

is continuous, nonnegative, integrates to one, and satisfies `||p_epsilon||_infinity<=1`, while `p_epsilon -> 1_[0,1]` in `L1`; the limit has no continuous representative. The missing ingredient is a common modulus of continuity.

Thus the owner's stronger continuous-density request cannot be obtained merely by proving the central universal `L^infinity` theorem and then invoking convex closure. A uniform Steklov/equicontinuity estimate is a genuinely separate obligation, exactly as account04/B15's regularity ledger suggested.

---

## 6. Relation to the fixed-instance bounded-density theorem

The completed account01/B15/account04/B15 principal-block mechanism gives, for every fixed rank-at-least-three matrix,

`||p_Q||_infinity <= (4*pi+8)/kappa_{3,4}(A)`.

This already proves bounded density instancewise, but `kappa_{3,4}(A)` can tend to zero within the target spectral class, so it does not produce the universal constant. Theorem 3.1 does something orthogonal: it removes arbitrary fractional/measurable marginal densities as a source of additional difficulty while preserving the exact full matrix class. What remains is geometric: prove one dimension-free shell/small-ball bound for extreme fragmented product sets.

For the stronger continuity assertion, Theorem 5.1 identifies a clean sufficient endpoint: obtain a dimension-free common modulus on those extreme fragmented laws. No continuity of the input indicators is required or even available.

---

## 7. Status and next attack

**PROVED in this run:**

* exact convex/TV-lower-semicontinuous extremal reduction of the central output `L^infinity` functional;
* equivalence of the full bounded-density target to the same interval estimate on product-indicator inputs, and via the consumed localization, bounded finite unions of intervals of total length one;
* a separate equicontinuity-modulus transfer theorem yielding continuous representatives for arbitrary admissible measurable input densities;
* an explicit demonstration that continuity does not transfer from extreme laws under a common `L^infinity` bound alone.

**NOT proved:** the dimension-free interval estimate itself; a dimension-free common continuity modulus; the full universal QFORM conjecture.

The first unpaid implication is now especially concrete:

> uniformly over target-admissible rotated/indefinite matrices and products of bounded finite unions of intervals `E_i` with `|E_i|=1`, prove `|{x in prod E_i : x^T A x in I}| <= C|I|` with one dimension-free `C`.

The same finite-fragment class must retain arbitrary component count and separation; replacing it by centered/single intervals is invalid by the consumed extremal/fiber counterexamples.

A useful next recipient is a geometry/small-ball worker (B06/B08/B10/B19), while B15 should next seek a common Steklov modulus from whatever shell estimate those workers prove.

No claim of novelty or publication priority is made. Full QFORM remains **OPEN**.
