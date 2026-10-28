SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T13:33:32Z.
attacking: replace arbitrary fragmented cap-one laws by monotone 1-expanding quantile maps of the unit cube, then isolate the common-Hessian geometric slab problem and apply account04/B13 at an actual inequality.

# account03/B13 r27 — quantile-cube purification and common-Hessian slab geometry

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: extremal product laws / STRUCTURE  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**  
Full continuity: **OPEN**.

## 1. Fresh scope and sources actually used


The designated partner result actually used is the latest completed `account04/B13` report:

`yspennstate/math-open-problems@master`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260923T121154Z-account04-B13-nonattained-bathtub-r1/REPORT.md`.

Its Theorem 3.1 proves, for every nonnegative measurable kernel `K`, the exact no-attainment identity

`sup_{0<=f_i<=1, int f_i=1} int K(x) prod_i f_i(x_i) dx
 = sup_{|E_i|=1} int_(prod E_i) K(x) dx`.                         (1.1)

In the same report, after applying the completed exterior-energy estimate, every slab ratio `rho` obeys for every integer `m>=5`

`D_m^perp(A) <= (C_m/rho)^(2m),`
`C_m=2 sqrt(2e) m/(m-4)`,                                       (1.2)

and therefore for every disjoint original-coordinate cross block `M=A[I,L]`,

`s_m(M) <= C_m/rho`.                                             (1.3)

At `m=5`, `C_5=10 sqrt(2e)=23.316439815971...`.

The live corrections were refreshed before the argument. Nothing below assumes law-uniform pointwise quadratic-phase decay, post-rotation independence, an arbitrary-joint rank-three coarea bound, a conditional projection-density cap, a bounded support diameter, a fixed number of support fragments, or a centered/single-interval extremizer.

## 2. Exact quantile representation of the whole cap-one class

Let

`F={f:R->[0,1] measurable : int_R f=1}`.

For `f in F`, let

`F_f(x)=int_{-infinity}^x f(s) ds`

and define the generalized quantile on `(0,1)` by

`T_f(u)=inf{x in R : F_f(x)>=u}`.                                (2.1)

Because `F_f` is continuous, nondecreasing and onto `(0,1)`,

`F_f(T_f(u))=u`, `0<u<1`.                                        (2.2)

Since `f<=1`, the CDF is 1-Lipschitz:

`F_f(y)-F_f(x) <= y-x`, `x<y`.                                  (2.3)

Hence for `0<u<v<1`,

`v-u
 =F_f(T_f(v))-F_f(T_f(u))
 <=T_f(v)-T_f(u)`.                                                (2.4)

Thus `T_f` is nondecreasing and **1-expanding**.

### Theorem 2.1 — `QFORM-CAP1-QUANTILE-EXPANSION-v1`

A probability law on `R` has a density bounded by one if and only if it is the pushforward of Lebesgue measure on `(0,1)` by a nondecreasing 1-expanding map `T`:

`T(v)-T(u)>=v-u` for `0<u<v<1`.                                  (2.5)

#### Proof of the converse

Let `U~Unif(0,1)` and `mu=T_#Leb`. For every open interval `(a,b)`, its preimage under a monotone map is an interval, up to endpoints. If `u<v` both belong to that preimage, then by (2.5)

`v-u <= T(v)-T(u) < b-a`.

Therefore

`mu((a,b)) <= b-a`.                                               (2.6)

By countable disjoint decomposition of open subsets of `R` into intervals, `mu(G)<=|G|` for every open set `G`. Outer regularity then gives `mu(B)<=|B|` for every Borel set `B`. Hence `mu<<Leb`, and the Radon--Nikodym density is at most one almost everywhere. Its total mass is one. QED.

Consequently the entire original QFORM target can be written exactly as

`X_i=T_i(U_i)`,                                                   (2.7)

where the `U_i` are independent `Unif(0,1)` and every `T_i` is nondecreasing and 1-expanding. No rotation is performed; this is a coordinatewise transport in the original independent coordinates.

## 3. Extreme laws are pure-gap maps, not intervals

Let `E` be a bounded finite union of disjoint ordered intervals

`E=union_(k=1)^N [a_k,b_k]`,
`ell_k=b_k-a_k`, `sum_k ell_k=1`,
`b_k<=a_(k+1)`.                                                   (3.1)

Put

`s_0=0`, `s_k=sum_(j<=k) ell_j`.

The quantile of the unit-density law `1_E dx` is, for `s_(k-1)<u<s_k`,

`T_E(u)=a_k+(u-s_(k-1))=u+c_k`,
`c_k=a_k-s_(k-1)`.                                                (3.2)

Moreover

`c_(k+1)-c_k=a_(k+1)-b_k>=0`.                                    (3.3)

Thus

`T_E(u)=u+tau_E(u)`                                               (3.4)

with `tau_E` a nondecreasing finite-step function. Conversely, if `tau` is a nondecreasing finite-step function on a finite partition of `(0,1)`, then `T(u)=u+tau(u)` maps each partition interval by translation onto an interval of the same length; monotonicity of the step values makes the images ordered and disjoint. Their total length is one, and `T_#Leb` is exactly the indicator density of their union.

### Theorem 3.1 — `QFORM-PURE-GAP-EXTREMAL-TRANSPORT-v1`

For every real symmetric `A` and every interval `J`,

`sup_(cap-one product laws) P(X^T A X in J)`

equals

`sup_(tau_1,...,tau_n finite-step nondecreasing)
 |{u in (0,1)^n:
    (u+tau(u))^T A (u+tau(u)) in J}|`.                            (3.5)

Here `tau(u)=(tau_1(u_1),...,tau_n(u_n))`.

#### Proof

Apply the designated account04/B13 positive-kernel purification (1.1) to

`K(x)=1_{x^T A x in J}`.                                         (3.6)

This reduces the supremum exactly to unit-measure product indicators. For a strict violation, each measurable `E_i` can additionally be approximated in symmetric difference by a bounded finite union of intervals of measure one; because `0<=K<=1`, the product-event error is at most `sum_i |E_i triangle F_i|`. Hence bounded finite unions suffice for the supremum. Equations (3.2)--(3.4) identify those laws exactly with finite-step nondecreasing `tau_i`. QED.

This is an actual use of the designated partner theorem at the target slab inequality. It does **not** reduce to a single interval, a centered uniform law, bounded support diameter, or a bounded fragment count. Arbitrarily many and arbitrarily remote fragments are encoded by arbitrarily many and arbitrarily large upward jumps of `tau_i`.

## 4. Common Hessian on every fragment cell

Fix finite-step `tau_i`, and let the step partitions form Cartesian cells

`R_alpha=prod_i (s_(i,k_i-1),s_(i,k_i))`.                         (4.1)

On the interior of one such cell, `tau(u)=c_alpha` is constant. Therefore

`Q(T(u))
 =(u+c_alpha)^T A (u+c_alpha)
 =u^T A u+2(A c_alpha)^T u+c_alpha^T A c_alpha`.                  (4.2)

### Theorem 4.1 — `QFORM-COMMON-HESSIAN-CELL-v1`

Every finite-union extreme product witness is a uniform-cube slab problem for a piecewise quadratic function whose Hessian is **exactly the same matrix** on every fragment cell:

`nabla_u^2 [Q(T(u))]|_(R_alpha)=2A`.                              (4.3)

All fragment locations and all arbitrarily large gaps enter only through the affine vector `2A c_alpha` and the constant `c_alpha^T A c_alpha`.

This separates the two difficulties that were conflated in support-radius perturbation arguments:

* remote fragments do **not** change or amplify the quadratic Hessian after quantile straightening;
* the remaining hard issue is to obtain an estimate uniform in the cellwise affine terms **without summing a loss over the number of cells**.

Thus a translation-uniform analytic estimate is exactly matched to the extremal geometry. A proof may not condition on a rotated eigencoordinate, but it may work on the independent cube variables `U_i` while retaining the coordinatewise monotone maps.

## 5. Fragment-independent one-coordinate fiber complexity

Fix all coordinates except `u_i`. Put `x_j=T_j(u_j)` for `j!=i`. As a function of the physical coordinate `x_i`,

`Q=a x_i^2+b x_i+c`,
`a=A_ii`,
`b=2 sum_(j!=i) A_ij x_j`.                                       (5.1)

For any interval `J` of length `L`, the inverse image of `J` under a real quadratic polynomial is a union of at most two intervals. Because `T_i` is monotone, its preimage in `u_i` is also a union of at most two intervals, independent of the number of fragments in the original support.

If `a!=0`, completing the square gives the sharp elementary length estimate

`|{x_i: a x_i^2+b x_i+c in J}| <= 2 sqrt(L/|a|)`.                (5.2)

For any 1-expanding monotone `T_i`, the preimage of an interval of x-length `ell` has u-length at most `ell`. Hence every original-coordinate fiber satisfies

`boxed:
 |{u_i in(0,1): Q(T(u)) in J}|
 <= min(1, 2 sqrt(L/|A_ii|))
`                                                                    (5.3)

whenever `A_ii!=0`.

If `A_ii=0` but `b!=0`, the analogous bound is

`|fiber| <= min(1,L/|b|)`.                                       (5.4)

The exponent `1/2` in (5.3) is not enough by itself for the target linear slab estimate; the value is structural: arbitrary fragmented one-dimensional supports become at most **two** intervals on every actual slab fiber. Any future coarea/fractional-trace synthesis can therefore attack a uniformly bounded fiber topology rather than a fragment count.

## 6. Partner exterior-energy theorem becomes a cell-uniform Hessian inequality

Now apply the second completed result in the designated account04/B13 report to the actual quantile-cube witness. Let its slab ratio be

`rho=P(Q(T(U)) in J)/|J|`.                                       (6.1)

For every `m>=5` and every disjoint original-coordinate banks `I,L`, (1.3) gives

`s_m(A[I,L]) <= C_m/rho`.                                        (6.2)

But by the common-Hessian identity (4.3), on **every** fragment cell,

`partial^2_(u_I,u_L) Q(T(u))=2A[I,L]`.                           (6.3)

Therefore

`boxed:
 s_m(partial^2_(u_I,u_L) Q(T(u))|_(R_alpha))
 <= 2 C_m/rho
`                                                                    (6.4)

simultaneously for every cell `R_alpha`, every disjoint cut, and every `m>=5`.

At `m=5`,

`boxed:
 s_5(partial^2_(u_I,u_L) Q(T(u))|_(R_alpha))
 <= 20 sqrt(2e)/rho
 =46.632879631942.../rho.
`                                                                    (6.5)

Equivalently, the complete disjoint fifth exterior energy of the common cell Hessian divided by two satisfies

`D_5^perp(A) <= (10 sqrt(2e)/rho)^10`.                            (6.6)

This is the useful interface: a putative high-ratio counterexample cannot hide its low-cross-rank structure in different remote fragments. The same near-low-rank mixed Hessian is present on every quantile cell; only affine translations vary from cell to cell.

The latest partner report further records the max-volume consequence that high ratio yields, outside a bounded physical core, a decomposition `A=D+R+E` with `rank R<=28` and `||E||_max<=32 sqrt(2e)/rho`. In the quantile-cell coordinates, the quadratic remainder is always `u^T E u`; the remote gap vector contributes only `2(Ec_alpha)^T u+c_alpha^T E c_alpha`. Thus the old support-radius amplification obstruction is converted into a purely dimension/aggregation obstruction. One still cannot delete `E`: even on a unit cube, `|u^T E u|` can scale like `n^2 ||E||_max`, and cellwise estimates cannot simply be summed over an unbounded number of cells.

## 7. Compact conditional end-to-end argument and exact missing implication

The present B13 front end now has the following exact form.

1. By Theorem 3.1, it is sufficient and necessary to prove the slab inequality for `T_i(u)=u+tau_i(u)` with arbitrary nondecreasing finite-step `tau_i`.
2. By Theorem 4.1, on every fragment cell the Hessian is exactly `2A`; arbitrary fragmentation produces affine translations only.
3. By (6.4), any high-ratio witness has the same quantitative low-cross-rank/exterior-energy profile on every cell.
4. By (5.3), every physical-coordinate slab fiber has at most two components, with the scalar `sqrt(L)` estimate whenever the physical diagonal is nonzero.

The first essential missing implication is therefore:

`QFORM-PURE-GAP-COMMON-HESSIAN-GLUE-v1`:

> Prove a dimension-free linear slab estimate for the unit-cube problem (3.5), uniformly over arbitrary nondecreasing finite-step gap maps, using the common Hessian/exterior-energy structure **without paying the number of cells**; or show that a high-ratio sequence of such maps forces one of the already-paid square/pair/bordered-volume/grouped-bank/ridge certificates.

This formulation removes remote support diameter and fragment count as geometric variables but does not pretend the remaining dimension accumulation is solved.

A particularly concrete next subcase is the partner skeleton `A=D+R+E`, `rank R<=28`, `||E||max=O(1/rho)`: exploit translation-uniform fractional traces for `D+R` while treating `u^T E u` jointly across cells, not perturbatively through the remote translations.

## 8. Status and integrity

Proved in this run:

* exact equivalence between cap-one laws and monotone 1-expanding quantile transports of the unit interval;
* exact identification of finite-union extreme laws with nondecreasing pure-gap step maps `T(u)=u+tau(u)`;
* exact target-slab supremum reduction to those maps by applying account04/B13;
* common-Hessian identity on every fragment cell;
* fragment-independent at-most-two-component coordinate slab fibers and the bound (5.3);
* application of the partner exterior-energy theorem to the actual cell Hessian inequality (6.4)-(6.5).

Not proved:

* no uniform control independent of the number of quantile cells has yet been obtained;
* the low-rank-plus-small-entry residual is not deleted;
* the full universal QFORM density theorem remains OPEN;
* the separate continuous-density conclusion remains OPEN.

No Gaussian, log-concavity, moment, compact-support, connected-support, centered-support, diagonal-basis, post-rotation independence, bounded-diameter, fixed-fragment-count, or Monte Carlo premise was introduced.