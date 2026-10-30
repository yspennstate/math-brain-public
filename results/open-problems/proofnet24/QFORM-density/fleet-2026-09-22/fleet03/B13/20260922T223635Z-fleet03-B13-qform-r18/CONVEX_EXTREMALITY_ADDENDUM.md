# Convex output-law extremality addendum

## Theorem — `QFORM-CONVEX-OUTPUT-EXTREMALITY-v1`

Let `T:R^n->R` be any measurable map. Let `D_n` be the cap-one product laws and let `F_n` be the product laws whose marginals are indicators of compact finite unions of rational-grid intervals of total length one. If

`Phi : P(R) -> [0,infinity]`

is convex and lower semicontinuous for total-variation convergence, then

`boxed:
 sup_(mu in D_n) Phi(T_#mu)
 = sup_(nu in F_n) Phi(T_#nu).
`

Thus the extremal-product reduction is not limited to one preselected slab. It applies simultaneously to any convex TV-lower-semicontinuous functional of the **entire output law**.

### Proof

Fix `mu=otimes_i mu_i in D_n`. By the completed fleet04/B14 finite-mixture localization theorem, choose cap-one product laws `mu_m` such that

`||mu_m-mu||_TV ->0`

and each `mu_m` is a finite convex combination

`mu_m=sum_a theta_(m,a) nu_(m,a)`,

where every `nu_(m,a) in F_n`. Measurable pushforward contracts total variation, hence

`T_#mu_m -> T_#mu` in total variation.

By convexity,

`Phi(T_#mu_m)
 =Phi(sum_a theta_(m,a) T_#nu_(m,a))
 <=sum_a theta_(m,a) Phi(T_#nu_(m,a))
 <=sup_(nu in F_n) Phi(T_#nu).`

Lower semicontinuity gives

`Phi(T_#mu)
 <=liminf_m Phi(T_#mu_m)
 <=sup_(nu in F_n) Phi(T_#nu).`

Taking the supremum over `mu` proves one inequality; the reverse is inclusion because `F_n subset D_n`. QED.

## Application 1 — the whole `L^infinity` density norm uses one same extreme law

For a probability measure `eta` on `R`, define

`D(eta)=sup_(a<b) eta([a,b])/(b-a)`.                            (A.1)

This is convex. For each fixed interval the map `eta -> eta([a,b])/(b-a)` is total-variation continuous, so `D`, being their supremum, is TV-lower-semicontinuous.

Moreover:

- `D(eta)<infinity` iff `eta` has an essentially bounded Lebesgue density;
- in that case `D(eta)=||p_eta||_infinity`.

Indeed interval domination `eta(I)<=D|I|` extends to open sets and then Borel sets, giving absolute continuity and density cap `D`; the converse is immediate, and equality with the essential supremum follows from Lebesgue differentiation.

Therefore for every fixed quadratic-affine map `P(x)=x^T A x+2b^T x+c`,

`boxed:
 sup_(mu in D_n) ||p_(P_#mu)||_infinity
 =sup_(nu in F_n) ||p_(P_#nu)||_infinity,
`

with the convention `+infinity` when an output has no bounded density.

This is stronger than selecting a different product-indicator witness for each interval: the **entire density-norm functional** can be extremalized to a single sequence of common finite-grid product laws.

## Application 2 — same-law concentration and Fourier energies

For fixed `r>0`,

`Q_r(eta)=sup_x eta([x-r,x+r])`

is convex and TV-continuous, so its worst cap-one product input is also a finite-grid product indicator in the limiting sense.

Likewise, for `p>=1` and nonnegative Borel `w`,

`Phi_(p,w)(eta)=int w(t)|hat eta(t)|^p dt`

is convex (because `z->|z|^p` is convex) and TV-lower-semicontinuous by pointwise characteristic-function convergence plus Fatou. Hence the fleet02/B13 same-extreme Fourier-power theorem is a special case of this output-law principle.

## Designated fleet04/B13 partner applied

The earlier completed fleet04/B13 fixed-volume random-set theorem at

`yspennstate/math-open-problems@7229e8caa8374eb8e74b07e70cadd0c0ccb05d39`

provides the exact barycentric identity

`T_#mu = int T_#nu_E dPi(E)`

for arbitrary unit-measure extreme products. Applying convexity to the actual density functional `D` gives directly

`D(T_#mu) <= int D(T_#nu_E)dPi(E)
           <= ess sup_E D(T_#nu_E)`.

Thus the designated partner is used on the **full linear-small-ball/density-norm inequality**, not only on a single chosen slab. The fleet04/B14 finite-mixture theorem then safely replaces arbitrary extreme sets by compact rational-grid extreme products at the supremum level, avoiding the later infinite-space threshold nonattainment issue.

## Scope

No centered interval, connected support, bounded diameter, uniform fragment count, compact-support assumption on the original law, or moment condition is introduced. The finite-grid parameters may diverge along an extremizing sequence.

This theorem concerns essential boundedness and other convex output-law functionals. Pointwise continuity of an output density is not such a TV-lower-semicontinuous functional and is not transferred by this finite-grid approximation alone.
