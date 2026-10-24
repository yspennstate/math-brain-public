SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-23T02:15:59Z.
attacking: exact countable translation/localization of the full small-ball constant, with matrix discretization only after compact extreme-product reduction.

# account01/B14 r27 — exact countable localization preserving the full QFORM constant

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `NEW SUPPORTING LOCALIZATION THEOREM / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

## 1. Target and sources actually used

The full target remains: for every dimension `n`, every independent real input `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three singular/eigenvalue magnitudes at least one, prove a universal bound for the essential density of `Q=X^TAX`, or give a valid counterexample. No moments, connected support, bounded support, identical laws, Gaussianity, log-concavity, or post-rotation independence may be inserted.

Fresh owner control remained revision `2026-09-22.15`. The full target is still open. The current correction set rules out, among other things, law-uniform pointwise quadratic Fourier decay, bounded-diameter localization, a universal fixed fragment-count bathtub reduction, and coefficient-perturbation continuity for arbitrary unbounded/remote-fragment laws.

Assigned partner result actually applied: account02/B14 r23,
`yspennstate/math-open-problems@ae5a1d83e5434d0c318a53da7095cebe8ec6f17e:proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T015809Z-account02-B14-QFORM-r23/REPORT.md`.
Its simultaneous convex-envelope localization theorem is the first step below.

Newest owner-required Claude continuation actually applied: the volume-stability theorem at
`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
Its inequality is inserted in Section 8 after the exact reduction.

## 2. Small-ball functional

For a finite positive Borel measure `eta` on `R`, define

`SB(eta) := sup_{u<v} eta([u,v])/(v-u)`.

This is the extended `L^infinity` norm of the output density: `SB(eta)<infinity` iff `eta<=SB(eta) dx`, and then the essential density norm is exactly `SB(eta)`. It is convex and lower semicontinuous in total variation because it is a supremum of the continuous linear functionals `eta -> eta([u,v])/(v-u)`.

For a measurable output `F` and input law `mu`, write `SB_mu(F)=SB(F_#mu)`.

## 3. The countable skeleton

Let `D_n` be the class of all product probability laws

`mu(dx)=prod_(i=1)^n f_i(x_i) dx_i`,  `0<=f_i<=1`, `int f_i=1`.

Let `F_n` be the compact finite-fragment extreme subclass from account02/B14: each marginal density is `1_E`, where `E` is a compact finite union of intervals of total Lebesgue measure one.

Define the countable subclass `R_n subset F_n` by requiring every endpoint of every interval component to be rational. The total measure is still exactly one.

Let

`A_n^Q := {A in Sym_n(Q): s_3(A)>1}`,

where `s_3(A)` is the third largest singular value (equivalently the third largest absolute eigenvalue for symmetric `A`). Let `I_Q` be all nondegenerate closed intervals with rational endpoints.

Define the full target constant

`C_full := sup_(n>=3) sup_(mu in D_n) sup_(A=A^T, s_3(A)>=1) SB_mu(x^T A x)`.

Define the countable-core constant

`C_count := sup_(n>=3) sup_(nu in R_n) sup_(A in A_n^Q) sup_([r,s] in I_Q)
              nu{r<=x^T A x<=s}/(s-r)`.

Every indexing set in `C_count` is countable.

### Theorem 3.1 — `QFORM-COUNTABLE-EXACT-LOCALIZATION-v1`

`boxed: C_full = C_count.`

Thus a universal density estimate on this countable collection proves the full arbitrary-law, arbitrary-translation-support, arbitrary-real-matrix target with exactly the same constant. Conversely, if the conjecture is false because `C_full=infinity`, then for every `M<infinity` there is already a compact finite-fragment product law with rational endpoints, a rational target matrix satisfying the strict margin `s_3(A)>1`, and a rational output interval whose small-ball ratio exceeds `M`.

There is deliberately no uniform bound on support radius, number of fragments, or fragment separation.

## 4. Step 1: exact law localization before any matrix discretization

Account02/B14 r23 proves the following simultaneous form. If `{P_theta}` is an arbitrary family of measurable scalar outputs and `Phi_theta` are convex TV-lower-semicontinuous output functionals, then

`sup_(mu in D_n) sup_theta Phi_theta((P_theta)_#mu)
 = sup_(nu in F_n) sup_theta Phi_theta((P_theta)_#nu).`       (4.1)

Apply it with the parameter set

`Theta_n={A=A^T real: s_3(A)>=1}`,

`P_A(x)=x^T A x`, and `Phi_A=SB`. This is the required equation-level use of the assigned partner theorem:

`sup_(mu in D_n) sup_(A: s_3(A)>=1) SB_mu(P_A)
 = sup_(nu in F_n) sup_(A: s_3(A)>=1) SB_nu(P_A).`            (4.2)

The order in (4.2) is essential. We first reduce an arbitrary unbounded/fragmented law to a compact finite-fragment extreme product. Only then is it legal to approximate matrix coefficients on that fixed compact support. This avoids the known remote-fragment obstruction to law-uniform coefficient perturbation.

## 5. Step 2: rationalize the matrix with a strict spectral margin

Fix `nu in F_n`. Its support `K` is compact. Put

`R = sup_(x in K) ||x||_2 < infinity`.

Fix a real symmetric target matrix `A` with `s_3(A)>=1`. Choose `eps_m downarrow 0` and rational symmetric matrices `A_m` satisfying

`||A_m-(1+eps_m)A||op < eps_m/2`.                              (5.1)

Such matrices exist because rational symmetric matrices are dense in finite-dimensional matrix space. Weyl's singular-value inequality gives

`s_3(A_m) >= (1+eps_m)s_3(A)-eps_m/2 >= 1+eps_m/2>1`,          (5.2)

so `A_m in A_n^Q`. Also `A_m -> A` in operator norm.

Set

`delta_m = R^2 ||A_m-A||op ->0`.

Then uniformly for `x in K`,

`|x^T(A_m-A)x| <= delta_m`.                                   (5.3)

For any interval `I=[u,v]` of length `h>0`,

`{x: x^T A x in I}
 subset {x: x^T A_m x in [u-delta_m,v+delta_m]}`.              (5.4)

Hence

`nu{x^T A x in I}/h
 <= SB_nu(P_(A_m)) (h+2delta_m)/h`.                            (5.5)

Taking `liminf_m` yields

`nu{x^T A x in I}/h <= liminf_m SB_nu(P_(A_m)).`              (5.6)

Now take the supremum over `I`:

`SB_nu(P_A) <= liminf_m SB_nu(P_(A_m))
             <= sup_(B in A_n^Q) SB_nu(P_B).`                 (5.7)

The reverse inequality is trivial because `A_n^Q` lies inside the real target class. Therefore, for every fixed compact-fragment `nu`,

`sup_(A real, s_3(A)>=1) SB_nu(P_A)
 = sup_(A in A_n^Q) SB_nu(P_A).`                              (5.8)

No support radius enters the final constant. `R` is used only to justify pointwise approximation for one already-fixed compact test law, and disappears after taking the supremum.

### Affine companion

Exactly the same proof applies to

`P_(A,b,c)(x)=x^T A x+b^T x+c`.

After fixing compact `K`, approximate `b,c` by rational `b_m,c_m`; the uniform error is bounded by

`R||b_m-b||_2+|c_m-c|`.

Thus the simultaneous worst-law affine envelope is also unchanged if `A,b,c` are all restricted to rational data and `s_3(A)>1`. This handles arbitrarily large conditioning-generated translations without any support-dependent loss in the final extremal constant.

## 6. Step 3: rationalize finite-fragment supports at zero loss

Fix a marginal extreme density `1_E`, where

`E = union_(j=1)^k [a_j,b_j]`

is a finite union of pairwise disjoint nondegenerate closed intervals and `|E|=1` (zero-length components may simply be removed).

We construct finite unions `E_m` with rational endpoints, exactly `|E_m|=1`, and

`|E_m triangle E| ->0`.                                       (6.1)

For `k=1`, choose rational `q_m -> a_1` and set `E_m=[q_m,q_m+1]`.

For `k>=2`, approximate the two endpoints of the first `k-1` components by rational numbers, preserving their order and disjointness, and approximate the left endpoint of the last component by a rational number `q_m`. Let `L_m` be the total rational length of the first `k-1` approximating components. Define the last right endpoint to be

`q_m + 1 - L_m`,                                               (6.2)

which is rational. For sufficiently close approximations the last length is positive and the components remain disjoint. Equation (6.1) follows.

Let `nu_m` be the corresponding product law when this is done in every coordinate. Since

`||1_(E_m)-1_E||_1 = |E_m triangle E|`,                        (6.3)

the product-density telescoping inequality gives

`||dnu_m/dx-dnu/dx||_1
 <= sum_i |E_(i,m) triangle E_i| ->0`.                         (6.4)

Hence `nu_m -> nu` in total variation. Pushforward contracts total variation, and `SB` is TV-lower-semicontinuous, so for every fixed rational matrix `A`,

`SB_nu(P_A) <= liminf_m SB_(nu_m)(P_A)
             <= sup_(rho in R_n) SB_rho(P_A).`                (6.5)

Since `R_n subset F_n`, this proves

`sup_(nu in F_n) SB_nu(P_A)
 = sup_(rho in R_n) SB_rho(P_A)`.                              (6.6)

The same argument holds for rational affine parameters `(A,b,c)`.

## 7. Step 4: rational target intervals suffice

For every finite positive Borel measure `eta`,

`SB(eta)=sup_(r<s, r,s in Q) eta([r,s])/(s-r).`                (7.1)

Indeed, given `[u,v]`, choose rationals `r_m<u` increasing to `u` and `s_m>v` decreasing to `v`. Then `[r_m,s_m]` decreases to `[u,v]`; continuity from above for finite measures gives

`eta([r_m,s_m]) -> eta([u,v])`, `s_m-r_m -> v-u`.              (7.2)

Thus every interval ratio is a limit of rational-interval ratios. This remains valid when the supremum is infinite.

Combining (4.2), (5.8), (6.6), and (7.1), then taking the countable supremum over dimensions, proves Theorem 3.1.

## 8. Actual application of the newest volume-stability theorem

The newest owner-required volume-stability theorem states: for an ORIGINAL-coordinate cross block `M=A[I,J]`, if

`M=M0+E`, `s_3(M0)>=a>0`,
`max_i (P_Range(M0))_ii <=1/2`, and `||E||op<=a/16`,           (8.1)

then for every cap-one product law and arbitrary affine/self/outside terms,

`||p_(X^TAX+b^TX+c)||inf <= 24 sqrt(3)e/(5a) < 23/a`.         (8.2)

Apply (8.2) to the countable affine skeleton produced above. For every rational skeleton datum satisfying the same matrix certificate,

`sup_(r<s rational)
  P{r<=X^TAX+b^TX+c<=s}/(s-r)
 <= 24 sqrt(3)e/(5a).`                                        (8.3)

By the partner localization and Sections 5–7, there is **no additional localization or translation factor** when passing this branch back to arbitrary cap-one product laws. Thus, on the entire volume-stable branch, the exact full-law worst constant is bounded by the same `24 sqrt(3)e/(5a)` supplied by the analytic theorem. Distant fragments, arbitrarily many finite pieces along an approximating sequence, arbitrary translations, and unbounded original supports do not change the constant.

This is a genuine application, not merely a citation: the localization theorem converts the volume-stability density estimate into a countable, compact extreme-product verification problem while preserving its numerical constant exactly.

## 9. Finite exhaustion and falsification consequence

Because the skeleton is countable, enumerate all tuples

`(n,A,E_1,...,E_n,[r,s])`

appearing in `C_count` as `T_1,T_2,...`, and let

`C_N=max_(1<=j<=N) ratio(T_j)`.

Then

`C_N increasing C_full`.                                      (9.1)

Equivalently one may exhaust by dimension, rational-height/denominator bounds, support-radius bounds, and fragment-count bounds, allowing all of these complexity bounds to tend to infinity.

This does **not** assert that some fixed finite stage suffices. The live corrections rule out a universal fixed support diameter and a universal fixed fragment-count coordinatewise bathtub theorem. The exact statement is only that their union is complete and loses no constant.

If the full conjecture is false by unbounded density constants, (9.1) gives finite rational witnesses with arbitrarily large small-ball ratio. If one proves a uniform `C` on every member of this countable skeleton, Theorem 3.1 transfers exactly the same `C` to the full target.

## 10. Why this is not contradicted by remote-fragment perturbation failures

A known correction shows that `A_m -> A` in operator norm does not imply uniform closeness of the laws `X^T A_m X` and `X^T A X` over arbitrary cap-one inputs: remote fragments can magnify tiny coefficient changes.

The present proof never makes that invalid interchange. The quantifiers are deliberately ordered as

`arbitrary law -> exact partner localization to one compact extreme product -> matrix approximation on that fixed compact support`.

Uniform convergence (5.3) is therefore law-specific and legitimate. No common support bound is introduced, and no statement of law-uniform coefficient continuity is used.

## 11. Scope and remaining implication

What is now paid completely is the **law/translation/localization interface** at the level of the exact global density constant:

- arbitrary cap-one densities reduce with zero constant loss to compact finite-fragment indicator laws;
- the whole unbounded affine family may be localized simultaneously;
- only after compact localization, matrices and affine coefficients may be made rational with a strict target spectral margin;
- fragment endpoints and output intervals may also be made rational;
- hence the full target constant has an exact countable witness skeleton.

What remains unpaid is matrix structural: prove a universal bound on that countable skeleton, equivalently on the full target. In particular the bare condition `s_3(A)>=1` still does not force the volume-stability certificate (8.1), a uniformly good physical minor, or any other already-paid single branch. The diffuse/hub/near-null structural synthesis remains the first missing implication.

Full QFORM therefore remains `OPEN / NOT PROVED / NOT DISPROVED`.
