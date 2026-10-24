Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0487 — forced-prefix anti-selection theorem and infinite-environment tilted-cumulant bridge

Status: **PROVED PARTIAL / source problem still OPEN in this work**.

Outside target: Drewitz–Ramírez, *Selected Topics in Random Walks in Random Environment* (2014), Open Question 3.20. In an i.i.d. uniformly elliptic nearest-neighbor environment on `Z^d`, `d>=2`, assume the ballistic law of large numbers `X_n/n -> v` with `v·ell>0`. Does this imply the source polynomial ballisticity condition `(P)_M|ell` for the source range `M>15d+5`? Guerra–Ramírez equivalences among the standard ballisticity conditions do not by themselves supply the missing implication from positive velocity.

The current run does **not** claim that implication. It gives two new reductions and one exact obstruction to the previous level-Palm strategy.

## 1. Setup

Fix a unit vector `u` with

`v_u := v·u > 0`.

Put

`a=a(u):=max_i |u_i| > 0`

and choose a nearest-neighbor step `e_* in {+/-e_1,...,+/-e_d}` with

`e_*·u=a`.

Uniform ellipticity means

`omega(x,e)>=kappa>0`

for every site and nearest-neighbor step.

Use level spacing exactly `a`:

`sigma_m = inf{n>=0 : X_n·u >= m a}`,  `m=0,1,2,...`,

and define the depth before the next level by

`D_m = (m a - inf_{sigma_m <= n <= sigma_{m+1}} X_n·u)_+`.

In particular

`D_0 = (-inf_{0<=n<=sigma_1} X_n·u)_+`.

The spacing `a` is chosen so that `m` consecutive `e_*` steps hit level `ma` exactly and hit no earlier `a`-spaced level prematurely.

## 2. Exact triangular-array reduction of the source wrong-way event

Let

`T_L^u=inf{n:X_n·u>=L}`,

`tilde T_{-bL}^u=inf{n:X_n·u<=-bL}`,

and

`N_L=ceil(L/a)`.

### Lemma 2.1

For every `L>0` and `b>0`,

`{tilde T_{-bL}^u < T_L^u}`

is contained in

`union_{m=0}^{N_L-1} {D_m >= bL + ma}`.

Hence

`P_0(tilde T_{-bL}^u < T_L^u)
 <= sum_{m=0}^{N_L-1} P_0(D_m >= bL+ma)`.                 (2.1)

### Proof

On the wrong-way event, the hit of `-bL` occurs before level `L`, hence before `sigma_{N_L}` because `N_L a>=L`. Let `m<N_L` be the largest completed `a`-level at that time. The hit then occurs after `sigma_m` and before `sigma_{m+1}`. During that same level excursion the projection reaches at most `-bL`, so

`D_m >= ma-(-bL)=ma+bL`.

This proves the inclusion and the union bound. `QED`

This is a source-facing reduction: no regeneration construction and no finite-periodic approximation are used.

## 3. A moment criterion that would close P0487

Equation (2.1) gives a clean sufficient condition.

### Corollary 3.1

If for every `u` in a neighborhood of `ell` there is `p>d` such that

`sup_{m>=0} E_0[D_m^p] < infinity`,                            (3.1)

locally uniformly in `u`, then

`P_0(tilde T_{-bL}^u<T_L^u)=O(L^{1-p})`

for every fixed `b>0`. Therefore the degree-`d-1` polynomial transience condition holds, and the known Guerra bridge yields `(T)|ell`; the Guerra–Ramírez equivalence then yields the source-standard `(P)_M` conclusion.

Indeed, Markov's inequality and (2.1) give

`P_0(tilde T_{-bL}^u<T_L^u)
 <= C sum_{m<N_L}(bL+ma)^(-p)
 <= C' L^(1-p)`.

Multiplying by `L^(d-1)` gives `O(L^(d-p))->0`.

At the endpoint `p=d`, it is enough to have uniform integrability:

`sup_m E[D_m^d 1_{D_m>R}] -> 0` as `R->infinity`.            (3.2)

Indeed, for `r_m=bL+ma>=bL`,

`P(D_m>=r_m)
 <= r_m^(-d) E[D_m^d 1_{D_m>=bL}]`,

and summing `O(L)` terms yields `o(L^(1-d))`.

Thus one possible infinite-environment closure target is now explicit: **uniform `d`th-moment integrability of the consecutive-level backtracking depths**. This is stronger than the earlier first-regeneration-radius route, which only needs the `d-1` scale, but it is local in level and directly source-facing.

## 4. Positive speed gives only a first-moment Cesaro budget

For the same `a`-spaced levels there is a deterministic inequality

`2D_m+a <= a(sigma_{m+1}-sigma_m)`.                           (4.1)

To see this, if the minimum during the interval is `ma-D_m`, then the projected path must spend at least `D_m` variation going from level at least `ma` down to that minimum and at least `D_m+a` variation climbing from the minimum to `(m+1)a`. Every step changes projection by at most `a`.

Summing gives

`2 sum_{m<N}D_m + aN <= a sigma_N`.                           (4.2)

The ballistic LLN implies the inverse law

`sigma_N/N -> a/v_u`,

and hence

`limsup_N (1/N)sum_{m<N}D_m
 <= (a/2)(a/v_u-1) < infinity`.                                 (4.3)

So positive velocity gives a first-moment **Cesaro** budget, whereas the direct source closure criterion asks for approximately `d` moments uniformly in the level index. The missing gain must come from spatial i.i.d. structure, not from the LLN alone.

## 5. New forced-prefix minorization: fixed levels cannot regularize a bad initial tail

This is the main structural theorem of the run.

### Theorem 5.1 (forced-prefix anti-selection)

For every integer `m>=0` and every `r>=0`,

`P_0(D_m>=r) >= kappa^m P_0(D_0>=r)`.                         (5.1)

Consequently, for every `p>0`,

`E_0[D_m^p] >= kappa^m E_0[D_0^p]`.                           (5.2)

In particular, if `E[D_0^p]=infinity`, then **every fixed deterministic level** `D_m` also has infinite `p`th moment.

### Proof

Let `F_m` be the event that the first `m` steps are all `e_*`. For each environment,

`P_{0,omega}(F_m) = product_{j=0}^{m-1} omega(je_*,e_*) >= kappa^m`.  (5.3)

On `F_m`, the projected position after `j<m` steps is `ja<ma`, while after step `m` it is exactly `ma`. Therefore `sigma_m=m`.

Starting from `me_*` at time `m`, require the shifted copy of the event `{D_0>=r}`: before the projection gains another `a`, it falls at least `r` below its starting level. The intersection of this shifted event with `F_m` is contained in `{D_m>=r}`.

By the Markov property at the deterministic time `m`, pointwise ellipticity, and spatial translation invariance of the i.i.d. environment law,

`P_0(D_m>=r)
 >= E[ P_{0,omega}(F_m) P_{me_*,omega}(shifted {D_0>=r}) ]
 >= kappa^m E[P_{me_*,omega}(shifted {D_0>=r})]
 = kappa^m P_0(D_0>=r)`.

No independence between the forced prefix and the future environment is required: the prefix factor is bounded below pointwise by `kappa^m`. Integrating the tail inequality gives (5.2). `QED`

### Interpretation

The preceding run produced finite-mean subsequential **level-Palm** limits from the Cesaro budget. Theorem 5.1 shows that this cannot mean that the excursion law eventually acquires a finite moment at some fixed far-ahead level. If the initial law has an infinite `p`th moment, every fixed level retains that infinite moment. Any finite-moment weak Palm limit can arise only through a non-uniform `m->infinity` escape of tail mass.

This turns the previous qualitative phrase "selection bias" into an exact obstruction.

## 6. Quantitative cost of converting a Cesaro level law back to the initial law

Define

`nu_N=(1/N) sum_{m=0}^{N-1} Law(D_m)`.

Summing (5.1),

`nu_N([r,infinity))
 >= [(1-kappa^N)/(N(1-kappa))] P(D_0>=r)`.                    (6.1)

Equivalently,

`P(D_0>=r)
 <= [N(1-kappa)/(1-kappa^N)] nu_N([r,infinity))
 <= N nu_N([r,infinity))`.                                   (6.2)

The prior level-Palm strategy sought to compare the initial or failed-attempt tail with a far-ahead averaged tail. Equation (6.2) proves a comparison, but with an explicit factor of order `N`. Thus a weak limit `nu_N=>nu` is not enough; one needs a **joint `N,r` tail estimate** strong enough to absorb this cost.

For example, the exact sufficient diagonal criterion

`N(r) r^(d-1) nu_{N(r)}([r,infinity)) -> 0`                  (6.3)

implies

`r^(d-1)P(D_0>=r)->0`.

This does not yet control all later failed regeneration attempts, but it is a precise Tauberian target rather than an informal law-comparison request.

## 7. Direct source criterion in terms of the triangular level array

Combining (2.1) with the actual level array gives an even more source-specific target:

`L^(d-1) sum_{m<N_L}P(D_m>=bL+ma) -> 0`                      (7.1)

for every fixed `b>0` and every `u` near `ell`.

Condition (7.1) is **exactly sufficient** for the degree-`d-1` Guerra condition. It is weaker than demanding uniform `d`th moments if the tail improves with `m`, and stronger information than the first-moment Cesaro budget (4.3).

Theorem 5.1 shows why a proof of (7.1) cannot simply assert that sufficiently large deterministic levels have a much lighter moment class: any such improvement must be genuinely non-uniform in the tail scale.

## 8. Second new bridge: a negative annealed tilted exponent manufactures an integrable corrector

The previous run's multiplicative-corrector route can be obtained canonically from a fixed-time annealed tilt, if one can prove a negative exponent.

For `theta>0`, define

`g_n(theta)=(1/n) log E_0[exp(-theta X_n·u)]`

and

`Lambda_u(theta)=limsup_{n->infinity}g_n(theta)`.

### Theorem 8.1

If `Lambda_u(theta)<0` for some `theta>0`, then:

1. there are `c,C>0` such that

   `P_0(exists n: X_n·u<=-L) <= C e^{-cL}`;                   (8.1)

2. the canonical environment-space function

   `H_{theta,u}(omega)=sum_{n>=0} E_{0,omega}[e^{-theta X_n·u}]`  (8.2)

   is finite `P`-a.s., satisfies `E[H]<infinity`, and obeys

   `K_{theta,u}H = H-1 <= H`,                                 (8.3)

   where

   `(K_{theta,u}h)(omega)=sum_e omega(0,e)e^{-theta e·u}h(tau_e omega)`;

3. since `H>=1`, all negative moments of `H` are automatic. Thus this supplies exactly the positive integrable tilted corrector required by the earlier finite-cone lemma.

### Proof

Choose `c_0>0` and `n_0` with

`E[e^{-theta X_n·u}]<=e^{-c_0 n}` for `n>=n_0`.

If `X_n·u<=-L`, then `n>=L/a`, and Markov's inequality gives

`P(X_n·u<=-L)<=e^{-theta L}E[e^{-theta X_n·u}]`.

Summing over `n>=L/a` proves (8.1). Also

`E[H]=sum_n E[e^{-theta X_n·u}]<infinity`,

hence `H<infinity` a.s. Finally, one Markov step shifts the series:

`K_{theta,u}H
 = sum_{n>=0} E_{0,omega}[e^{-theta X_{n+1}·u}]
 = H-1`.

`QED`

This is a genuinely infinite-environment corrector, not a finite-periodic Perron eigenvector.

## 9. What positive velocity gives at theta=0, and the exact analytic gap

Because increments are bounded and `X_n/n->v`, dominated convergence gives

`g_n'(0)=-(1/n)E[X_n·u] -> -v_u<0`.                           (9.1)

The tempting but invalid inference is to exchange `n->infinity` with a fixed positive `theta` and conclude `Lambda_u(theta)<0`.

A sufficient condition is now explicit. Under the tilted law with density proportional to `e^{-theta X_n·u}`,

`g_n''(theta)=(1/n) Var_{n,theta}(X_n·u)`.                    (9.2)

Hence if for some `theta_0,C>0`

`sup_{n large, 0<=theta<=theta_0} g_n''(theta) <= C`,         (9.3)

then Taylor's theorem and (9.1) imply, for a sufficiently small fixed `theta>0`,

`g_n(theta) <= -(v_u/4)theta<0`

for all large `n`. Theorem 8.1 then gives exponential backward control and an `L^1` multiplicative corrector.

Thus a **linear tilted-variance bound** is another concrete infinite-environment bridge. It is probably too strong for the full nestling source class, but it identifies precisely what the finite-state spectral argument was using implicitly.

## 10. Decisive abstract obstruction to derivative-limit interchange

Positive velocity alone cannot justify the step from (9.1) to a negative fixed tilt.

Let `Y_n` be random variables with

`Y_n=vn` with probability `1-e^{-sqrt(n)}`,

`Y_n=-an` with probability `e^{-sqrt(n)}`,

where `a,v>0`. Couple the exceptional events independently. Since

`sum_n e^{-sqrt(n)}<infinity`,

Borel–Cantelli gives

`Y_n/n -> v` almost surely,

and also `E[Y_n]/n->v`.

Nevertheless, for every fixed `theta>0`,

`(1/n)log E[e^{-theta Y_n}]
 -> theta a >0`,                                              (10.1)

because the subexponentially rare negative linear deviation dominates the negative exponential tilt.

This sequence is **not an RWRE and not a counterexample to P0487**. It proves only that an LLN plus bounded linear scale cannot make the fixed-tilt argument work abstractly. The spatial i.i.d. geometry must rule out exactly such subexponentially rare linear wrong-way excursions, or one must use the weaker polynomial route instead. This matches the source's remark that Open Question 3.20 is tied to the behavior/slope of the large-deviation rate function at the origin.

## 11. Progress delta and next attack

New results this run:

- exact source wrong-way event reduction to the triangular array of consecutive-level depths, equation (2.1);
- uniform `d`th-moment integrability criterion implying the Guerra degree-`d-1` condition;
- forced-prefix minorization (5.1), proving that no fixed deterministic far-ahead level can repair an infinite initial moment;
- explicit `N`-factor anti-selection/Tauberian cost (6.2);
- canonical `L^1` multiplicative corrector from a negative annealed tilted exponent, with a precise tilted-variance sufficient condition;
- an abstract rare-event obstruction showing why positive velocity by itself does not imply that fixed-tilt exponent.

The full-source metric remains

`FULL_SOURCE_IMPLICATION: 0 -> 0`.

The strongest next attack is **not** another finite-periodic example. There are now two precise source-relevant targets:

(A) prove, from i.i.d. spatial freshness plus positive velocity, the joint triangular-array estimate (7.1), or enough uniform `d`th-moment integrability to imply it; preferably by a fresh-slab decomposition that controls the cost of revisiting the explored region;

(B) on a finite star of directions near `ell`, prove a weaker block-scale analogue of `Lambda_u(theta)<0` or an integrable multiplicative corrector without requiring the globally exponential fixed-time tilt that nestling slowdown can obstruct.

The forced-prefix theorem rules out treating the previous weak level-Palm limit as if it automatically upgraded any fixed-level moment. Any successful continuation must address the joint tail/level scale or exploit genuinely fresh spatial blocks.