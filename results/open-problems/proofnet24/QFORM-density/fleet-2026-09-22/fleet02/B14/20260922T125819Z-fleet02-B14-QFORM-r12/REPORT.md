# fleet02/B14 — median-gauge localization, cap-preserving regularization, and subcritical fragment packing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner revision:** `2026-09-22.5`  
**Run:** `20260922T125819Z-fleet02-B14-QFORM-r12`  
**Assignment:** Translations and localization  
**Status:** `TARGET_LEVEL_EQUIVALENCE_PROVED / SUPPORTING_PACKING_LEMMA_PROVED / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target, source state, and first unpaid implication

The target remains: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least `1`, prove one universal finite `C` such that

`P{X^T A X in I} <= C |I|`

for every bounded interval `I`; or construct a valid target counterexample.

The previous fleet02/B14 run proved an exact same-constant reduction to product indicators of bounded finite unions of intervals of measure one. The assigned partner fleet03/B14 subsequently proved exact equality between pure quadratic and range-compatible affine-quadratic small-ball constants for each fixed symmetric `A`, and identified the component-box weighted-congruence debt. Source used here:

`yspennstate/math-open-problems@e6a82375d007069e7e515cb682eaf430d8baa914:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260922T123805Z-fleet03-B14-QFORM-r11/REPORT.md`.

The first unpaid localization implication is therefore not tails, rough densities, or absolute support location. It is **relative multiscale separation of fragments after one global translation gauge**, together with the weighted-congruence interaction that remains when the local scaled matrices lose the three-large-eigenvalue hypothesis.

All current route corrections are respected: no independence is asserted after spectral rotation, no law-uniform pointwise Fresnel decay is used, no naive fiber supremum is used, and no cross-minor alone is treated as sufficient.

## 2. Exact median-gauge reduction for the finite-fragment class

For a fixed real symmetric `A`, let `C_pure(A)` denote the optimal interval small-ball constant over all admissible independent densities. By the previous B14 reduction, the same value is obtained by restricting every input density to `1_{E_i}`, where each `E_i` is a bounded finite union of intervals of total length exactly one.

Call such a set **median-gauged** if

`|E_i intersect (-infinity,0]| = |E_i intersect [0,infinity)| = 1/2`.

Because Lebesgue measure is non-atomic, every measure-one finite union of intervals has a median `m_i` with exactly half its measure on each side; translating by `m_i` preserves finite-fragment structure and total measure.

### Theorem 2.1 — `QFORM-MEDIAN-GAUGE-LOCALIZATION-v1`

For every fixed symmetric `A`, `C_pure(A)` equals the optimal constant for the following normalized class:

- each input is uniform on a bounded finite union `F_i` of intervals with `|F_i|=1` and median zero in the exact half-mass sense above;
- the polynomial is allowed to be

`x^T A x + b^T x + c`

with arbitrary `c in R` and arbitrary `b in Range(A)`.

Hence the full universal QFORM constant is unchanged if one imposes this median gauge and carries the range-compatible linear term.

### Proof

Start with any finite-fragment pure instance `X_i ~ 1_{E_i}`. Choose medians `m_i` and write `m=(m_1,...,m_n)`, `Y=X-m`. The sets `F_i=E_i-m_i` remain bounded finite unions of intervals of total length one and have exact half-mass on each side of zero. Moreover

`X^T A X = Y^T A Y + 2(Am)^T Y + m^T A m`.

Thus every pure finite-fragment instance is represented in the median-gauged range-affine class with `b=2Am in Range(A)`. Therefore the median-gauged affine constant is at least `C_pure(A)`.

Conversely, the assigned partner fleet03/B14 proves that for fixed `A`, allowing arbitrary `b in Range(A)` and `c` does not increase the best constant: if `b=2Aa`, then

`x^T A x+b^Tx+c=(x+a)^T A(x+a)+c-a^TAa`,

and translating each coordinate law preserves independence and the density cap. The same argument preserves finite unions of intervals. Hence every median-gauged affine instance has small-ball constant at most `C_pure(A)`.

The two inequalities give exact equality. `QED`.

### Scope and consequence

This removes **all absolute translations** without paying for `|m|`, support location, or any moment. What remains is invariant relative separation. For example

`F_R=[-R-1/2,-R] union [R,R+1/2]`

already satisfies the median gauge for every `R`, while its diameter tends to infinity. Thus translation alone cannot turn the finite-fragment class into a uniformly bounded box; any further localization must genuinely control relative separation rather than rename it.

## 3. Cap-preserving smooth and analytic regularization with the same target constant

The finite-fragment formulation is optimal for geometric arguments, but analytic workers often want smooth amplitudes. Smoothness can be imposed **without changing the best target constant**, provided no estimate is allowed to depend on the resulting derivative or moment sizes.

### Lemma 3.1 — cap-preserving compact smooth approximation

Let

`D={f in L1(R): 0<=f<=1, int f=1}`.

For every `f in D` and every `eps>0`, there exists `g in C_c^infinity(R)` such that

`0<=g<=1`, `int g=1`, and `||g-f||_1<eps`.

### Proof

Choose `R` so that `delta=int_{|x|>R} f(x) dx<eps/4`. Set

`h=f 1_{[-R,R]} + 1_J`,

where `J` is any interval disjoint from `[-R,R]` of length exactly `delta`. Then `0<=h<=1`, `int h=1`, `h` is compactly supported, and

`||h-f||_1 <= 2 delta < eps/2`.

Let `rho_sigma` be a nonnegative compactly supported probability mollifier. Then

`g=h*rho_sigma`

satisfies `0<=g<=||h||_infinity<=1`, has integral one and compact support, and converges to `h` in `L1` as `sigma downarrow0`. Choose `sigma` so that `||g-h||_1<eps/2`. `QED`.

The same proof with a Gaussian approximate identity produces a real-analytic Schwartz density `g` with `0<g<1`, integral one, and arbitrarily small `L1` distance from `f`.

### Theorem 3.2 — `QFORM-SMOOTH-CORE-LOCALIZATION-v1`

For every fixed symmetric `A`, the optimal pure quadratic small-ball constant over all `f_i in D` is exactly the same if every `f_i` is required to lie in either of the following classes:

1. `C_c^infinity`, `0<=f_i<=1`, `int f_i=1`;
2. real-analytic Schwartz densities, `0<f_i<1`, `int f_i=1`.

The same statement holds for range-compatible affine quadratics.

### Proof

Only the nontrivial direction is needed. Approximate each coordinate `f_i` in `L1` by an admissible `g_i` from the chosen smooth class. The product densities satisfy the telescoping bound

`|| product_i f_i - product_i g_i ||_1 <= sum_i ||f_i-g_i||_1`.

Pushforward by any measurable map, in particular `x -> x^T A x+b^Tx+c`, cannot increase total variation. Hence output probabilities of every Borel set converge uniformly as the coordinate `L1` errors vanish. A common interval bound `C|I|` for the smooth approximants therefore passes to the original product law with the identical `C`. The reverse inequality is immediate because the smooth classes are subclasses of `D`. `QED`.

Combining Theorems 2.1 and 3.2 gives an exact analytic gauge: one may work with **median-zero compact-smooth or analytic-Schwartz coordinate laws, while allowing `b in Range(A)`**, with no change in the full target constant.

If the full conjecture is false, then for every `M` there is already a counterexample with compact-smooth pure input laws whose small-ball ratio exceeds `M`; equivalently there is a median-zero smooth range-affine counterexample. Thus pathological tails, discontinuities and absolute shifts cannot be the source of failure.

## 4. Subcritical fragment packing: a dimension-free compiler for distant pieces

The partner fleet03/B14 component-box identity shows why a scale-only bound on each fragment can lose badly: tiny fragment scales shrink `D_k A D_k`, and summing their reciprocal local constants can depend on the number of components. The missing compensation must use **where the fragments are**, not merely how small they are.

The following exact packing lemma supplies a reusable sufficient mechanism.

Let

`E = disjoint_union_alpha I_alpha`, `|E|=1`,

with interval lengths `ell_alpha>0`. For an anchor `a in R`, put

`r_alpha(a)=dist(a,I_alpha)+ell_alpha`.

### Theorem 4.1 — `QFORM-FRAGMENT-SUBCRITICAL-PACKING-v1`

For every `0<=theta<1`,

`sum_alpha ell_alpha r_alpha(a)^(-theta) <= 2^theta/(1-theta)`.

The bound is independent of the number, location, diameter and separation of the fragments.

### Proof

For every `x in I_alpha`,

`|x-a| <= dist(a,I_alpha)+ell_alpha = r_alpha(a)`.

Therefore

`ell_alpha r_alpha(a)^(-theta)
 <= int_{I_alpha} |x-a|^(-theta) dx`.

Summing over the disjoint intervals gives

`sum_alpha ell_alpha r_alpha(a)^(-theta)
 <= int_E |x-a|^(-theta) dx`.

Among all measurable sets of measure one, the integral of the symmetric decreasing kernel `|x-a|^{-theta}` is maximized by the centered interval `[a-1/2,a+1/2]`. Hence

`int_E |x-a|^(-theta) dx
 <= 2 int_0^{1/2} u^{-theta} du
 = 2^theta/(1-theta)`.

`QED`.

### Product form

If each `E_i` is decomposed into intervals `I_{i,alpha}` of lengths `ell_{i,alpha}`, and component labels have the exact product weights

`w_k=product_i ell_{i,k_i}`

from the fleet03/B14 localization identity, then for any finite coordinate set `J`, anchors `a_i`, and exponents `0<=theta_i<1`,

`sum_k w_k product_{i in J} r_{i,k_i}(a_i)^(-theta_i)
 <= product_{i in J} [2^{theta_i}/(1-theta_i)]`.

This follows by exact factorization of the label sum and Theorem 4.1 coordinate by coordinate.

Thus a fragmentwise shell/coarea estimate whose center dependence is a product of **subcritical one-dimensional singularities** can be averaged over arbitrary fragmentation with a dimension-free constant. This is a concrete way to pay the partner report's weighted-congruence debt without bounding fragment count or diameter.

### Criticality is real

The exponent restriction is sharp for this mechanism. Let

`E_N = union_{k=1}^N [2(k-1)/N,(2k-1)/N]`.

These are `N` disjoint intervals of length `1/N`, total measure one. With anchor `a=0`,

`r_k(0)=(2k-1)/N`,

and at the critical exponent `theta=1`,

`sum_k (1/N) r_k(0)^(-1)
 = sum_{k=1}^N 1/(2k-1)
 ~ (1/2) log N`.

Hence no fragment-count-independent analogue of Theorem 4.1 exists at reciprocal-distance exponent one. Any localization proof that first turns a quadratic fiber into a derivative-only `1/distance` cost and then sums fragments can therefore incur a genuine logarithmic loss. The quadratic curvature or another averaging mechanism must keep the singularity subcritical, or cancel it before componentwise payment.

This is a mechanism counterexample, not a counterexample to the owner conjecture.

## 5. Smoothness does not revive the refuted pointwise Fourier route

The smooth-core reduction must not be misread as permission to reintroduce law-uniform stationary-phase decay. The phase-aligned counterexample can itself be smoothed while keeping the density cap.

Fix `s>0` and `eta>0`. Choose `delta>0` with `cos(delta)>1-eta/2`. The phase bands

`B_k={x>0: |s x^2-2 pi k|<=delta}`

have lengths asymptotic to a positive constant times `k^{-1/2}`, so their total Lebesgue measure diverges. Choose a finite union `E` of subintervals of these bands with `|E|=1`. Then for `f=1_E`,

`Re int exp(i s x^2) f(x) dx >= cos(delta)`.

By Lemma 3.1 choose an admissible `g in C_c^infinity` with `||g-f||_1<eta/2`. Since the oscillatory factor has modulus one,

`Re int exp(i s x^2) g(x) dx
 >= cos(delta)-eta/2 > 1-eta`.

Thus for every fixed large frequency one can find a smooth compact density bounded by one with quadratic characteristic function arbitrarily close to one. The mandatory pointwise-decay correction therefore remains valid even inside the smooth core.

## 6. What moved and what remains

**Target-level movement:** yes.

1. The full constant is unchanged after exact median normalization of every finite-fragment coordinate law, provided the range-compatible affine term is retained. Absolute shifts are fully removed without moments or support bounds.
2. The full constant is unchanged after cap-preserving regularization to compact-smooth or analytic-Schwartz coordinate densities. Therefore roughness and tails are not essential obstructions.
3. Arbitrary fragmentation admits a dimension-free packing compiler for every subcritical distance singularity `theta<1`, while the critical reciprocal-distance cost has an explicit logarithmic fragmentation obstruction.

**Full-problem status:** OPEN.

The first B14 unpaid implication is now sharper:

> Starting from the median-gauged finite-fragment formulation and the partner's exact component-box identity, derive a local shell/coarea estimate whose fragment-center singularities are all subcritical in the sense of Theorem 4.1, or produce a genuine target counterexample. A scale-only or critical `1/distance` fragment estimate is insufficient.

This is distinct from re-running compactification or the earlier bang-bang reduction. No claim is made that the packing lemma by itself proves the universal QFORM bound.

## 7. Source pins and integrity

- Fresh control programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.
- Partner actually applied: fleet03/B14, canonical report commit `e6a82375d007069e7e515cb682eaf430d8baa914`, path stated in Section 1.
- Previous fleet02/B14 localization report used as inherited scope: `yspennstate/math-open-problems@ea75afa89f7764caf119e6b835f9ba56b8d7874b:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260922T120110Z-b14-qform-localization-r13/REPORT.md`.
- Live corrections consumed through the final pre-write control refresh include the pointwise-decay, fiber-supremum, no-independence-after-rotation, cross-minor, universal-pi/diffuse-branch, two-sheet-X-ray, conditional-UV-cap, and single-Schur-rank2-extraction corrections then present.

Changed-file review: this report contains only mathematical derivations, programme/source pins and nonsecret run metadata; no credentials, native scheduler identifiers, machine paths, email content, unrelated private data, benchmark material, public release, paid call, remote workflow or permission change.
