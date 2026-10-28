SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T12:05:49Z.
attacking: singular-functional localization for translation-uniform fractional traces, after abandoning duplicate positive-completion compactification.

# account03/B14 r34 — singular-kernel localization and nested physical-core splice

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T120549Z-account03-B14-QFORM-r34`  
Status: `NEW SUPPORTING LOCALIZATION THEOREM PROVED / FULL QFORM OPEN / CONTINUITY OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and mechanism change

The exact target remains: for every finite `n`, independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal essential bound on the density of `X^T A X`, or give a valid counterexample. No moment, compact-support, connected-support, centering, Gaussian, log-concave, or post-rotation independence hypothesis is added.


The first route attempted this run was positive-completion tail compactification. A source match ended that duplicate direction: account02/B14 had already proved the exact unnormalized truncation-plus-filler theorem at

`yspennstate/math-open-problems@06301dca1c0a81033d960406f0acc5125f63dd0c:proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T120110Z-b14-qform-localization-r13/REPORT.md`.

That source already removes arbitrary tails with zero constant loss and reduces bounded small-ball functionals to finite unions. I therefore changed mechanism on the same target. The new issue is the one emphasized by the current proof-first control: **translation-uniform fractional traces**. The kernel `|P-t|^{-alpha}` is unbounded, so ordinary total-variation approximation does not by itself preserve its expectation. The theorem below gives an exact extreme-product localization directly for such singular kernels.

The designated partner result actually applied below is account04/B14 r8,

`yspennstate/math-open-problems@e0fd3e5ae1e84a7a7d1eec28949bd962e0ca5bf8:proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T061428Z-account04-B14-affine-physical-core-r8/REPORT.md`.

I also refreshed the newer partner r9 handoff/report (`63ba8e0f106c3bb405f05eb99778039ff47ed47b`); it proves continuum-perspective rough transfer for a logarithmic physical-pair compiler. It does not supersede the singular fractional-trace statement proved here.

## 2. Exact localization for arbitrary nonnegative measurable functionals

Let `D_n` be the class of product probability laws on `R^n` whose marginal densities satisfy `0<=f_i<=1`. Let `E_n` be the subclass of product indicator laws `prod_i 1_{E_i}(x_i) dx` with measurable `E_i subset R`, `|E_i|=1`. Let `F_n` be the subclass for which every `E_i` is a compact finite union of bounded intervals of total length one. No uniform bound is imposed on the number, locations, separation, or diameter of those intervals.

### Theorem 2.1 — `QFORM-SINGULAR-FUNCTIONAL-EXTREME-LOCALIZATION-v1`

For every nonnegative Borel function

`G:R^n -> [0,+infinity]`,

one has the exact extended-real identity

`sup_{mu in D_n} int G dmu
 = sup_{mu in E_n} int G dmu
 = sup_{mu in F_n} int G dmu`.                                  (2.1)

The equality includes the value `+infinity`.

### Proof: arbitrary cap-one densities to measure-one indicators

For `M>=1`, put `G_M=min(G,M)`. Fix an arbitrary admissible product density `prod_i f_i`. Since `G_M` is bounded, fix all coordinates except `i` and define

`w_i(s)=int G_M(x_1,...,s,...,x_n) prod_{j!=i} f_j(x_j) dx_{-i}`.

Then `0<=w_i<=M`. The bathtub principle is used here only in its **supremum** form on the nonatomic line:

`sup_{0<=f<=1, int f=1} int w f
 = sup_{|E|=1} int_E w`.                                       (2.2)

An optimizer need not exist on the infinite line. Accordingly, for any `epsilon>0`, replace coordinate `1` by an indicator of a measure-one set losing at most `epsilon/n`, then coordinate `2`, and so on. After the finite iteration,

`int G_M prod_i f_i
 <= sup_{|E_i|=1} int G_M prod_i 1_{E_i} + epsilon
 <= sup_{mu in E_n} int G dmu + epsilon`.                       (2.3)

Letting `epsilon downarrow0` and then using monotone convergence as `M->infinity` gives

`int G prod_i f_i <= sup_{mu in E_n} int G dmu`.

Taking the supremum over `D_n` yields `sup_D<=sup_E`. The reverse inequality is immediate because indicator densities are admissible. Therefore the first equality in (2.1) holds even when the common value is infinite.

For completeness, (2.2) follows from the usual decreasing-rearrangement/layer-cake formula; equivalently, for every admissible `f`, the mass constraint and cap imply `int wf <= int_0^1 w^*(s) ds`, while measure-one superlevel approximants approach the same right side. No attained threshold set is assumed.

### Proof: measure-one sets to compact finite unions

Fix measurable `E_i` of measure one and let

`J=int G(x) prod_i 1_{E_i}(x_i) dx`.

It is enough to show that every finite `L<J` is beaten arbitrarily closely by a member of `F_n`; this also covers `J=+infinity`.

For `M,R>0`, define

`G_{M,R}(x)=min(G(x),M) 1_{[-R,R]^n}(x)`.

As `M,R -> infinity` along an increasing sequence, `G_{M,R}` increases pointwise to `G`. Choose `M,R` such that

`int G_{M,R} prod_i 1_{E_i} > L`.                              (2.4)

Inside `[-R,R]`, approximate each `E_i cap [-R,R]` in symmetric-difference measure by a compact finite union `U_i` of bounded intervals. If `|U_i|>1`, trim interval endpoints until `|U_i|=1`; because `|E_i cap[-R,R]|<=1`, the added symmetric-difference error is at most the original approximation error. Starting with half the desired tolerance therefore lets us arrange simultaneously

`|U_i|<=1`,
`sum_i |U_i Delta (E_i cap [-R,R])| < epsilon/M`.               (2.5)

Because every factor in the product has mass at most one, the telescoping product inequality on the cube gives

`int_{[-R,R]^n} |prod_i 1_{U_i}-prod_i 1_{E_i}| dx
 <= sum_i |U_i Delta (E_i cap [-R,R])|`.                        (2.6)

Consequently (2.4)-(2.6) imply

`int G_{M,R} prod_i 1_{U_i} > L-epsilon`.                       (2.7)

For each `i`, add one compact interval `H_i` outside `[-R,R]` and disjoint from `U_i`, of length exactly `1-|U_i|`. Set `F_i=U_i union H_i`. Then `F_i` is a compact finite union of intervals, `|F_i|=1`, and on the cube it agrees with `U_i`. Since `G>=G_{M,R}>=0`,

`int G prod_i 1_{F_i} >= int G_{M,R} prod_i 1_{U_i} > L-epsilon`. (2.8)

Letting `epsilon downarrow0` and then `L up J` proves `sup_F >= J`. Taking the supremum over `E_n` proves `sup_F>=sup_E`, while `F_n subset E_n` gives the reverse. This completes (2.1). QED.

### What is genuinely different from prior localization

For bounded slab indicators, ordinary bang-bang localization already existed. For convex TV-lower-semicontinuous output norms, my earlier r23 finite-mixture compiler already existed. The present theorem handles **unbounded positive kernels** directly. In particular, total variation alone is not enough for `|P-t|^{-alpha}`: a vanishing amount of mass can be moved into a singularity and change that expectation arbitrarily. The truncation is made in the kernel before bathtub replacement, and the compact finite-union approximation is performed only after cutting both kernel height and physical space. No uniform integrability assumption is smuggled in.

## 3. Translation-uniform fractional-trace compiler

Let `B` be any fixed real symmetric matrix on an actual original-coordinate block `U in R^m`, and let `0<alpha<infinity`. Define

`P_{B,ell,c}(u)=u^T B u+ell^T u+c`.

### Corollary 3.1 — `QFORM-FRACTIONAL-TRACE-LOCALIZATION-v1`

For each fixed `B`,

`sup_{cap-one product laws, ell,c,t}
 E |P_{B,ell,c}(U)-t|^{-alpha}`

is **exactly equal** to the same supremum with every marginal restricted to indicators of compact finite unions of intervals of total length one.                                             (3.1)

This is immediate from Theorem 2.1 with

`G(u)=|P_{B,ell,c}(u)-t|^{-alpha}`

and then taking the supremum over the affine parameters and `t`.

Moreover, suppose a finite constant `K` bounds the finite-fragment side uniformly in `ell,c,t`. Consider any ambient quadratic form whose `U x U` principal block is `B`, and condition on all outside **original** coordinates `V`. The conditional polynomial is

`U^T B U+ell(V)^T U+c(V)`.

For every target `t`, (3.1) gives the conditional expectation at most `K`, pointwise in `V`; averaging yields

`sup_t E |Q-t|^{-alpha} <= K`.                                 (3.2)

Thus the full ambient fractional trace inherits **exactly the same constant**, with arbitrary outside dimension, outside quadratic coefficients, cross couplings, translations, distant fragments, unbounded supports and no moments. No rotation of the independent variables occurs.

This is the localization interface needed by scalar-pivot/half-Riesz arguments: one may prove the difficult translation-uniform singular estimate only for finite-fragment extreme products and then lift it losslessly to the original rough target.

## 4. Equation-level application of account04/B14: a nested physical-core bound

I now apply the designated partner theorem to an actual inequality.

Split one actual original coordinate from the rest:

`A = [[a, r^T],[r,C]]`, with `a!=0`, and `X=(X_0,Y)`.

Completing only this physical coordinate gives the exact identity

`Q = a [X_0+a^{-1} r^T Y]^2 + T(Y)`,                           (4.1)

where

`T(Y)=Y^T S Y`,   `S=C-r r^T/a`.                               (4.2)

Assume that the Schur matrix `S` contains an actual original-coordinate `3x3` principal block `B` satisfying

`s_min(B)>=sigma>0`.                                            (4.3)

Account04/B14 r8 applies to the residual form `T` and gives

`||p_T||_infinity <= M := 6 sqrt(pi)/sigma`.                    (4.4)

This already permits every remaining residual coordinate, arbitrary residual spectrum and couplings, rough fragmented/unbounded laws, and all conditioning-generated affine terms.

A probability density bounded by `M` obeys the sharp one-dimensional rearrangement estimate

`sup_t E|T-t|^{-1/2} <= 2 sqrt(2M)`                              (4.5)

(the centered interval of length `1/M` maximizes the integral against `|u|^{-1/2}`). Substituting (4.4) gives

`sup_t E|T-t|^{-1/2}
 <= 4 sqrt(3) pi^(1/4) sigma^(-1/2)`.                           (4.6)

Now condition on `Y=y` in (4.1). Translation of `X_0` preserves its density cap. The density of the shifted square satisfies, almost everywhere,

`p_{a(X_0+h)^2}(u) <= |a|^{-1/2}|u|^{-1/2}`                    (4.7)

on the appropriate sign half-line and is zero on the other side. Averaging the conditional densities in (4.7) over `Y` and applying (4.6) proves:

### Theorem 4.1 — `QFORM-SCALAR-OVER-PHYSICAL3-NESTED-v1`

Under (4.1)-(4.3), for arbitrary independent cap-one inputs,

`boxed:
 ||p_Q||_infinity
 <= 4 sqrt(3) pi^(1/4) / sqrt(|a| sigma).`                       (4.8)

No independence between the completed-square shift `a^{-1}r^T Y` and the residual `T(Y)` is used or needed. The estimate is insensitive to support diameter, translations, tail mass, fragment count, fragment separation, and moments.

The new singular-functional localization theorem means that the half-Riesz obligation (4.6), in future branches where it is not already obtained from a density cap, may be proved only on compact finite-fragment extreme laws and then lifted with exactly the same `K`; ordinary TV localization would not justify that move by itself.

## 5. Scope and remaining structural implication

Theorem 2.1 closes a genuine measure-theoretic gap for the current proof-first programme: **all nonnegative singular trace kernels, including inverse powers and logarithmic kernels, admit lossless finite-fragment extreme localization at the level of their supremum**. There is no fixed fragment-count, diameter, location, moment, or translation tax.

The nested branch (4.8) is supporting, not a solution of the full conjecture. The bare hypothesis `s_3(A)>=1` does not force a scalar physical pivot `a` and a Schur `3x3` principal block satisfying a dimension-free lower bound on `|a| sigma`. The known singleton-plus-two-banks and diffuse families forbid that naive extraction. The remaining debt is therefore structural: synthesize the finite-fragment translation-uniform half-Riesz estimates across the zero/near-isotropic pivot and grouped-bank/ridge branches **before** paying a reciprocal local minor.

Continuity is not obtained by Theorem 2.1 or (4.8); only essential boundedness is claimed in the stated branch.

## 6. Integrity

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- New proved theorem: exact singular-functional extreme localization, including fractional traces.
- Completed designated partner actually applied: account04/B14 r8 at equation (4.4).
- Source-matching prior theorem ended the duplicate positive-completion route before publication.
- No Gaussian, log-concavity, moment, compact-support, connected-support, centered-support, post-rotation independence, uniform pointwise oscillatory decay, or fixed fragment-count assumption is used.
- Repository transport is not native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
