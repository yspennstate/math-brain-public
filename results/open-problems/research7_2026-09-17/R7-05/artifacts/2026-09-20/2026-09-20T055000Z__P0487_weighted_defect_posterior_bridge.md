Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0487 — weighted mesoscopic defect potential and an exact posterior anti-selection identity

Date: 2026-09-20 UTC  
Worker: C04 / R7-05  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Status: **PROVED PARTIAL**. The full Drewitz--Ramírez implication remains open in this work.

## 1. Source target and inherited point

Outside source: Alexander Drewitz and Alejandro F. Ramírez, *Selected Topics in Random Walks in Random Environment* (2014), Open Question 3.20. In an i.i.d. uniformly elliptic nearest-neighbour environment on `Z^d`, `d>=2`, assume

`X_n/n -> v` almost surely, with `v.ell>0`.

The source asks whether this forces the effective polynomial ballisticity condition `(P)_M|ell` at the standard threshold `M>15d+5` (equivalently, through the later Guerra--Ramírez theorem, one of the standard `(T)/(T')/(T)_gamma` ballisticity conditions).

A targeted literature check on 2026-09-20 rechecked Enrique Guerra, *On the connection between transient and ballistic behaviours for RWRE* (arXiv:2006.00570v3), Definition 1.4 and Theorem 1.9, and Guerra--Ramírez, *A proof of Sznitman's conjecture about ballistic RWRE* (published 2019/2020). Guerra proves that the asymptotic degree-`d-1` condition `(mathcal P^(d-1))|ell` implies `(T)|ell` in the i.i.d. case. This does not supply the missing implication from positive velocity. The bounded check did not produce a later primary theorem resolving that implication; this is negative search evidence only, not a worldwide-openness certificate.

The immediately preceding R7-05 report constructed a scale-dependent tilt from the ballistic LLN. Fix a compact cone `U` with

`c_U := inf_{u in U} v.u >0`.

For any `rho>0`, one can choose `alpha>0` and then a finite `n` such that, uniformly in `u in U`, with `theta=alpha/n`,

`E_P[ K_{theta,u}^n 1 ] = E_0 exp(-alpha X_n.u/n) <= rho`.      (1.1)

Here

`(K_{theta,u} f)(omega)
 = sum_e omega(0,e) exp(-theta e.u) f(tau_e omega)`.

The preceding report then thresholded `Z:=K^n1` into a sparse bad-site field and paid a constant worst-case penalty at every bad visit. The new result below is stronger: keep the exact defect size, exploit the full `n`-term corrector, and charge only the **positive part of the logarithmic multiplicative defect**. Its static mean is of order `rho/n`, not merely its support probability.

---

## 2. Deterministic sharp bounds for the finite-horizon corrector

Fix one direction `u`, put

`a=a_u:=max_{|e|_1=1}|e.u|`, `theta=alpha/n`,

`Z(omega):=K^n 1(omega)`,

and

`H(omega):=sum_{j=0}^{n-1} K^j 1(omega)`.                     (2.1)

For every environment and every `j<=n`,

`K^j1(omega)=E_{0,omega}[exp(-theta X_j.u)]`.

Since `|X_j.u|<=aj`,

`exp(-theta a j) <= K^j1 <= exp(theta a j)`.                  (2.2)

Define

`s_alpha := (1-exp(-alpha a))/(alpha a)`,

`t_alpha := (exp(alpha a)-1)/(alpha a)`.

Summing (2.2), and using `1-exp(-x)<=x` and `exp(x)-1>=x`, gives the deterministic bounds

`n s_alpha <= H(omega) <= n t_alpha`.                          (2.3)

In particular

`t_alpha/s_alpha = exp(alpha a)`.                             (2.4)

Also

`exp(-alpha a) <= Z(omega) <= exp(alpha a)`.                  (2.5)

The exact resolvent identity is

`K H = H - 1 + Z`.                                             (2.6)

This sharper lower bound `H>=n s_alpha` is important. The preceding run used only `H>=1`, which made a bad visit look `n` times more expensive than necessary.

---

## 3. Main theorem A — an exact weighted-defect martingale

Define the local multiplicative ratio

`r(omega):=(K H)(omega)/H(omega)
          =1+(Z(omega)-1)/H(omega)`,                            (3.1)

and its logarithmic positive defect

`g(omega):=[log r(omega)]_+`.                                  (3.2)

Let

`c(omega):=log r(omega)`.

For the quenched walk define

`G_m:=sum_{k=0}^{m-1} g(tau_{X_k}omega)`,

`C_m:=sum_{k=0}^{m-1} c(tau_{X_k}omega)`.

### Theorem 3.1

The process

`M_m
 = exp(-theta X_m.u)
   H(tau_{X_m}omega)
   exp(-C_m)`                                                   (3.3)

is an **exact nonnegative quenched martingale**.

### Proof

Conditioning on `X_m=x`,

`E_{omega}[ exp(-theta X_{m+1}.u) H(tau_{X_{m+1}}omega) | F_m ]
 = exp(-theta x.u) (K H)(tau_x omega)`.

Multiplication by `exp(-c(tau_x omega))=H/(K H)` converts this exactly to

`exp(-theta x.u) H(tau_x omega)`.

The already accumulated factor `exp(-C_m)` is `F_m`-measurable. Thus the conditional expectation of `M_{m+1}` equals `M_m`. QED.

The point is that **negative defects help** and are not discarded. Only `G_m`, the cumulative positive part, needs eventual control.

---

## 4. Main theorem B — the positive defect has tiny static mean

From `log(1+x)<=x`, (2.3), and the fact that `g=0` whenever `Z<=1`,

`g(omega)
 <= (Z(omega)-1)_+ / (n s_alpha)
 <= Z(omega)/(n s_alpha)`.                                    (4.1)

Therefore (1.1) implies

`mu_g := E_P[g] <= rho/(n s_alpha)`.                           (4.2)

There is also a deterministic pointwise bound. From (2.5),

`g(omega)
 <= log( 1 + (exp(alpha a)-1)/(n s_alpha) )
 =: g_max`.                                                    (4.3)

Because

`(exp(alpha a)-1)/s_alpha = alpha a exp(alpha a)`,             (4.4)

we have

`g_max <= log(1 + alpha a exp(alpha a)/n)`,                    (4.5)

and hence

`n g_max <= alpha a exp(alpha a)`.                             (4.6)

Thus the relevant static defect is not a Bernoulli event with a constant price. It is a bounded nonnegative potential whose `P`-mean is at most `rho/(n s_alpha)`.

Relative to the spatial tilt `theta=alpha/n`,

`mu_g/theta <= rho/(alpha s_alpha)`.                           (4.7)

For fixed `alpha`, this ratio can be made as small as the contraction parameter `rho` supplied by the LLN construction. This is the first improvement of the run.

---

## 5. Main theorem C — source-facing wrong-way inequality with weighted defects

For `b,L>0`, let

`tau_L := tilde T_{-bL}^u wedge T_L^u`,

`A_L^u := { tilde T_{-bL}^u < T_L^u }`.

Since `C_m<=G_m`, on

`A_L^u intersect {G_{tau_L} <= theta bL/2}`

we have at the stopping time

`exp(-theta X_{tau_L}.u) >= exp(theta bL)`,

`H(tau_{X_{tau_L}}omega) >= n s_alpha`,

and

`exp(-C_{tau_L}) >= exp(-G_{tau_L}) >= exp(-theta bL/2)`.

Initially `M_0=H(omega)<=n t_alpha`. Applying optional stopping first at `tau_L wedge N` and then sending `N` to infinity gives, uniformly in the environment,

`P_{0,omega}( A_L^u, G_{tau_L}<=theta bL/2 )
 <= (t_alpha/s_alpha) exp(-theta bL/2)
 = exp(alpha a) exp(-alpha bL/(2n))`.                          (5.1)

Hence, annealed,

`P_0(A_L^u)
 <= exp(alpha a) exp(-alpha bL/(2n))
    + P_0( G_{tau_L} > alpha bL/(2n) )`.                       (5.2)

This strictly strengthens the binary bad-local-time bound from the preceding report. The remaining random term is now a **weighted positive defect potential with tiny static mean**, rather than a count of every thresholded bad visit.

---

## 6. Main theorem D — exact Bayesian posterior factorization for an annealed RWRE path

The main obstacle is that the walk selects its environment. In the i.i.d. case that selection can be quantified exactly.

Let a finite nearest-neighbour path be

`x_0=0,x_1,...,x_t`.

For every site `z` and nearest-neighbour direction `e`, let

`N_{z,e}(t):=#{0<=k<t: x_k=z, x_{k+1}-x_k=e}`,

`N_z(t):=sum_e N_{z,e}(t)`.

Under the product environment law `P=mu^{otimes Z^d}`, the annealed likelihood of the path factors as

`P_0[X_0=x_0,...,X_t=x_t]
 = product_z int [ product_e p(e)^{N_{z,e}(t)} ] mu(dp)`.       (6.1)

Consequently, conditional on the observed path, the site environments remain independent, with one-site posterior

`d mu_{N_z}/d mu (p)
 = [product_e p(e)^{N_{z,e}(t)}]
   / int [product_e q(e)^{N_{z,e}(t)}] mu(dq)`.                (6.2)

This is an exact identity, not an approximation.

Uniform ellipticity gives `p(e)>=kappa`, so for a finite site set `S`, if

`N_S(t):=sum_{z in S} N_z(t)`,

then the Radon--Nikodym derivative of the posterior on `S` relative to the original product law lies between

`kappa^{N_S(t)}` and `kappa^{-N_S(t)}`.                        (6.3)

Therefore, for every nonnegative measurable function `F` depending only on `(omega_z)_{z in S}`,

`E[ F | X_0=x_0,...,X_t=x_t ]
 <= kappa^{-N_S(t)} E_P[F]`.                                  (6.4)

Similarly, for events `E` measurable on `S`,

`P(E | path) <= kappa^{-N_S(t)} P(E)`.                         (6.5)

This gives an exact quantitative form of the previously vague phrase “adaptive selection of bad regions.” The selection bias can only become large after the walk has already accumulated many departures from the relevant dependency set.

---

## 7. Applying the posterior identity to the weighted defect

The variable `g(tau_x omega)` depends only on environment variables at sites that can be used during an `n`-step path from `x`; it is therefore measurable with respect to

`S_x := {z: |z-x|_1 <= n-1}`.                                 (7.1)

For the actual path define the prior exposure of the current dependency neighbourhood by

`E_t^{(n)}
 := sum_{k=0}^{t-1} 1_{ {X_k in S_{X_t}} }`.                  (7.2)

Conditioning only on the annealed path history `F_t^X=sigma(X_0,...,X_t)`, Theorem 6.1 and translation invariance give

`E[ g(tau_{X_t}omega) | F_t^X ]
 <= kappa^{-E_t^{(n)}} mu_g`.                                 (7.3)

Fix an integer exposure threshold `m>=0`. Call time `t` **lightly exposed** if `E_t^{(n)}<=m` and **recycled** otherwise.

For a path stopping time `T` bounded by a deterministic `N`, define

`G_T^light(m)
 = sum_{t<T} g(tau_{X_t}omega) 1_{ {E_t^{(n)}<=m} }`,

and

`R_N^{(n,m)}
 = sum_{t=0}^{N-1} 1_{ {E_t^{(n)}>m} }`.                      (7.4)

Since `{t<T}` and the light-exposure event are `F_t^X`-measurable, (7.3) and the tower property yield

`E[ G_T^light(m) ]
 <= kappa^{-m} mu_g E[T]`.                                   (7.5)

The heavy part satisfies deterministically

`G_T^heavy(m) <= g_max R_N^{(n,m)}`.                          (7.6)

Thus all adaptive-environment difficulty has been reduced to one purely path-geometric statistic: how often the walk stands at a point whose radius-`n` dependency neighbourhood has already accumulated more than `m` prior departures.

---

## 8. Combined inequality — weighted selection reduces to heavy local recycling

Take `N=floor(A L)` for a constant `A>0`. On `{tau_L<=N}`, split `G_{tau_L}` into light and recycled parts. By Markov's inequality, (4.2), and (7.5),

`P( G_{tau_L}^light(m) > theta bL/4, tau_L<=N )
 <= [4 A kappa^{-m} mu_g]/(theta b)
 <= [4 A kappa^{-m} rho]/(alpha b s_alpha)`.                  (8.1)

For the recycled contribution, (4.6) gives

`theta b/(4g_max)
 = alpha b/(4n g_max)
 >= b/(4 a exp(alpha a))
 =: c_rec(alpha,a,b)>0`.                                      (8.2)

Hence

`P( G_{tau_L}^heavy(m) > theta bL/4, tau_L<=N )
 <= P( R_N^{(n,m)} > c_rec L )`.                              (8.3)

Combining (5.2), (8.1), (8.3), and the event `{tau_L>N}` gives the new source-facing reduction

`P_0(A_L^u)
 <= exp(alpha a) exp(-alpha bL/(2n))
    + P_0(tau_L>A L)
    + [4 A kappa^{-m} rho]/(alpha b s_alpha)
    + P_0( R_{floor(AL)}^{(n,m)} > c_rec L )`.                (8.4)

This is the main result of the run.

If `A>1/(v.u)`, the ballistic LLN and inversion of the hitting time imply

`P_0(tau_L>A L) <= P_0(T_L^u>A L) ->0`.                       (8.5)

For each fixed `m`, the third term in (8.4) can be made arbitrarily small by choosing the mesoscopic contraction parameter `rho` sufficiently small before fixing `n`.

Therefore the remaining obstruction has been reduced to the **recycling term**

`P_0( R_{floor(AL)}^{(n,m)} > c_rec L )`.                     (8.6)

Unlike the preceding binary-defect local time, this term no longer mentions the defect field at all. It says that the only way the annealed path can strongly bias itself toward the positive weighted defects, after the posterior correction, is by repeatedly reusing the same radius-`n` environmental neighbourhoods.

This does not yet prove polynomial decay, nor Guerra's finite expected-sup seed. It is a conditional structural reduction.

---

## 9. Why the naive cluster-residence route does not close from a rate-free LLN

The preceding report suggested combining the sparse finite-range defect field with subcritical cluster tails and an elliptic escape estimate. This run checked that route quantitatively.

For an `R`-dependent site field with marginal defect probability `p`, a standard lattice-animal extraction gives exponential cluster-size tails once `p` is sufficiently small as a function of `R`. A uniformly elliptic walk can be forced to leave a finite connected cluster of physical diameter `D` along a prescribed path with probability at least `kappa^{O(D)}`. Mixing these estimates gives polynomial or better residence tails only when the cluster rarity exponent dominates an `O(D log(1/kappa))` residence cost.

For the present defect field, `R` is of order `n`. The rate-free LLN construction gives smallness roughly through `rho ~ exp(-alpha c_U)` at some horizon `n=n(alpha)`, but gives **no quantitative lower bound on `alpha/n`**. Thus the crude cluster/elliptic argument would require a relation of the schematic form

`-log p >> n log(1/kappa)`,                                   (9.1)

which cannot be extracted from the LLN alone. This is not an obstruction to P0487 itself; it is an obstruction to that particular worst-case residence proof. The weighted-posterior route above avoids paying the full worst-case escape cost of every rare cluster and is therefore strictly better aligned with the available hypotheses.

---

## 10. Fixed metric, obligation ledger, and next attack

Fixed full-source metric:

`FULL_SOURCE_IMPLICATION: 0 -> 0`.

Status: **PROVED PARTIAL**.

New obligation delta:

- `O6` positive velocity -> arbitrarily strong mesoscopic tilted contraction: DONE previously.
- `O7` sparse finite-range binary defect field: DONE previously.
- `O8` finite-horizon corrector: DONE previously.
- `O9` binary defect-charged supermartingale: superseded by the stronger weighted result below.
- `O10` exact weighted-defect martingale using `c=log(KH/H)`: **DONE THIS RUN**.
- `O11` deterministic sharp bounds `n s_alpha<=H<=n t_alpha`, `E g<=rho/(n s_alpha)`: **DONE THIS RUN**.
- `O12` exact i.i.d. posterior factorization and `kappa^{-exposure}` selection bound: **DONE THIS RUN**.
- `O13` combined reduction (8.4) from wrong-way exit to heavy radius-`n` path recycling: **DONE THIS RUN**.
- `O14` show the recycling probability in (8.6) is small enough, uniformly through a cone and in a form that yields either `(mathcal P^(d-1))` or Guerra's expected-sup seed: **OPEN; principal bottleneck**.

The next attack should work on `O14`, not return to finite-periodic examples. The natural object is a coarse local-time decomposition for the path into radius-`n` neighbourhoods. One needs an i.i.d.-specific theorem saying that a ballistic walk cannot spend a linear amount of pre-exit time in neighbourhoods that have already been visited more than `m` times without paying a quantitatively small annealed probability. The posterior lemma shows exactly why this is now the only selection mechanism left.

A second route is to apply the posterior factorization at **first entrances of disjoint dependency blocks**. Many spatially separated positive defects then cost multiplicatively, while concentration in only a few blocks is precisely the recycling alternative. This gives a clean fresh-block versus recycling dichotomy for the next run.
