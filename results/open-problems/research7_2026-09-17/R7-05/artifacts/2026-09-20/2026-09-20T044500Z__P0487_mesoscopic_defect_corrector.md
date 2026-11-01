Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0487 — mesoscopic defect-corrector bridge from positive velocity

## Status

Target: Drewitz–Ramírez, *Selected Topics in Random Walks in Random Environment* (2014), Open Question 3.20.  In an i.i.d. uniformly elliptic nearest-neighbour environment on `Z^d`, `d>=2`, assume the ballistic strong law

`X_n/n -> v`  `P_0`-a.s., with `v·ell>0`.

The source asks whether this implies the source polynomial ballisticity condition `(P)_M|ell` for the standard threshold `M>15d+5`.

This artifact is **PROVED PARTIAL**.  It does not prove the full implication.  It constructs a genuinely infinite-environment, mesoscopic positive corrector with controlled deterministic oscillation away from a rare set of environment defects, and gives an exact supermartingale that charges only the local time spent on those defects.  Thus the remaining problem is reduced to a rare-defect occupation estimate.

The fixed source metric remains

`FULL_SOURCE_IMPLICATION: 0 -> 0`.

## 1. Setup

Fix a unit direction `u` with `v_u:=v·u>0`.  Write

`a_u := max_{|e|_1=1} |e·u|`.

Thus `0<a_u<=1` and, pathwise,

`|X_n·u| <= a_u n`.

For `theta>=0`, introduce the tilted environment operator

`(K_{theta,u} f)(omega)
 := sum_{|e|_1=1} omega(0,e) exp(-theta e·u) f(tau_e omega)`.

Then for each integer `j>=0`,

`K_{theta,u}^j 1(omega)
 = E_{0,omega}[exp(-theta X_j·u)]`.                         (1.1)

The previous R7-05 work obtained a global corrector if a fixed positive `theta` has a negative annealed exponential growth rate.  That requirement can be too strong in a nestling regime.  Here the tilt is instead mesoscopic: `theta=alpha/n`.

## 2. Positive velocity gives arbitrarily strong mesoscopic contraction

### Theorem 2.1 (rate-free mesoscopic tilted contraction)

Let `U` be any compact set of unit directions satisfying

`c_U := inf_{u in U} v·u >0`.

For every `rho in (0,1)` there exist `alpha>0` and an integer `n_0` such that for every `n>=n_0` and every `u in U`, with `theta_n=alpha/n`, one has

`E_P[K_{theta_n,u}^n 1] = E_0[exp(-alpha X_n·u/n)] <= rho`.   (2.1)

No quantitative rate in the LLN is assumed.

### Proof

Put

`Delta_n := ||X_n/n-v||_2`.

The ballistic strong law gives `Delta_n->0` almost surely.  Since a nearest-neighbour walk has `||X_n/n||_2<=1` and `||v||_2<=1`, we have `Delta_n<=2`.  Hence for each fixed `alpha`, dominated convergence gives

`E_0[exp(alpha Delta_n)] -> 1`.                              (2.2)

For any `u in U`,

`-alpha X_n·u/n
 = -alpha v·u - alpha (X_n/n-v)·u
 <= -alpha c_U + alpha Delta_n`.

Therefore

`sup_{u in U} E_0[exp(-alpha X_n·u/n)]
 <= exp(-alpha c_U) E_0[exp(alpha Delta_n)]`.                (2.3)

First choose `alpha` so large that `exp(-alpha c_U)<rho/2`; then choose `n_0` so that the second factor in (2.3) is at most `2` (or, more sharply, so the product is below `rho`).  This proves (2.1).  QED.

### Consequence 2.2 (arbitrarily sparse tilted defects)

Fix a finite directional star `S subset U` and `q in (0,1)`.  Define

`Z_{n,u}(omega):=K_{alpha/n,u}^n 1(omega)`

and call a site `x` `u`-good when

`Z_{n,u}(tau_x omega)<=q`.

Call it `S`-good when it is `u`-good for every `u in S`.

By Markov's inequality and Theorem 2.1,

`P[x is not u-good] <= rho/q`,                              (2.4)

and

`P[x is not S-good] <= |S| rho/q`.                          (2.5)

Since `rho` in Theorem 2.1 is arbitrary, the marginal density of defects can be made arbitrarily small.

Moreover, `Z_{n,u}(tau_x omega)` only depends on environment variables at sites reachable from `x` in fewer than `n` nearest-neighbour steps.  Thus the good/bad field is finite-range dependent: site indicators with `l^1` separation greater than `2n` are independent under the i.i.d. environment law.

This is the first genuinely infinite-environment renormalization seed in this R7-05 line: positive velocity alone produces, at a sufficiently large finite scale, an arbitrarily high-density finite-range field of sites carrying a strict tilted contraction.

## 3. A finite-horizon corrector with deterministic oscillation bound

Fix `u`, `alpha`, `n`, and write `theta=alpha/n`, `a=a_u`.  Define

`H_{n,u}(omega)
 := sum_{j=0}^{n-1} K_{theta,u}^j 1(omega)`.                 (3.1)

This is positive and obeys the deterministic bounds

`1 <= H_{n,u}(omega) <= n exp(alpha a)`                     (3.2)

for every environment, because `K_{theta,u}^j1 <= exp(theta a j)<=exp(alpha a)`.

The resolvent identity is exact:

`K_{theta,u} H_{n,u}
 = H_{n,u}-1+Z_{n,u}`.                                       (3.3)

Hence on a `u`-good site,

`K_{theta,u} H_{n,u} <= H_{n,u}-(1-q) <= H_{n,u}`.          (3.4)

At an arbitrary site, using `Z_{n,u}<=exp(alpha a)` and `H>=1`,

`K_{theta,u}H_{n,u}
 <= H_{n,u}-1+exp(alpha a)
 <= exp(alpha a) H_{n,u}`.                                  (3.5)

Thus positive velocity has produced a positive corrector whose oscillation is controlled by the deterministic factor `n exp(alpha a)`.  It is genuinely superharmonic on the high-density good set and loses at most a fixed multiplicative factor on a defect.

## 4. Global defect-charged supermartingale

Let

`B_m^u := sum_{k=0}^{m-1} 1_{ {X_k is not u-good} }`         (4.1)

be the local time, up to time `m`, spent at tilted-defect sites.  Define

`M_m
 := exp(-theta X_m·u)
    H_{n,u}(tau_{X_m}omega)
    exp(-alpha a B_m^u)`.                                   (4.2)

### Theorem 4.1

For every fixed environment, `(M_m)_{m>=0}` is a nonnegative quenched supermartingale.

### Proof

Condition on `X_m=x` and the past.  If `x` is good, then `B_{m+1}=B_m` and (3.4) gives

`E_{0,omega}[M_{m+1}|F_m] <= M_m`.

If `x` is bad, then `B_{m+1}=B_m+1`.  The extra factor `exp(-alpha a)` exactly compensates the worst-case factor in (3.5):

`exp(-alpha a) K_{theta,u}H_{n,u} <= H_{n,u}`.

Again the conditional expectation is at most `M_m`.  QED.

This avoids the main flaw of a purely local corrector: the walk is allowed to enter bad regions.  Every visit is simply charged in the martingale.

## 5. Exact reduction of wrong-way slabs to rare-defect occupation

For `b,L>0`, let

`tau_L := tilde T_{-bL}^u wedge T_L^u`

and let

`A_L^u := {tilde T_{-bL}^u < T_L^u}`.

Because `v·u>0`, the forward level is reached almost surely under the annealed law, so standard truncation at `tau_L wedge N` and Fatou justify optional stopping below.

For every integer `m>=0`, on

`A_L^u intersect {B_{tau_L}^u <= m}`

we have

`M_{tau_L}
 >= exp(theta bL) exp(-alpha a m)`,                          (5.1)

since `H>=1`.  On the other hand

`M_0=H_{n,u}(omega)<=n exp(alpha a)`.

Therefore both quenched and annealed probabilities satisfy

`P_0(A_L^u, B_{tau_L}^u<=m)
 <= n exp(alpha a)
    exp(-alpha bL/n + alpha a m)`.                           (5.2)

Taking

`m_L=floor( bL/(2an) )`                                      (5.3)

gives the clean estimate

`P_0(A_L^u)
 <= n exp(alpha a) exp(-alpha bL/(2n))
    + P_0(B_{tau_L}^u > bL/(2an)-1)`.                        (5.4)

Equation (5.4) is the main bridge obtained in this run.

### Corollary 5.2 (source-facing closure criterion)

Suppose there is a neighborhood `U` of `ell` with `inf_{u in U}v·u>0` such that, after choosing the common mesoscopic parameters above, for every `b>0` and each `u in U`,

`L^(d-1) P_0(B_{tau_L}^u > bL/(2a_u n)-1) ->0`.             (5.5)

Then

`(mathcal P^(d-1))|ell`

holds.  Guerra's 2020 degree-`d-1` theorem then gives `(T)|ell` in the i.i.d. setting; the established ballisticity equivalences yield the standard source `(P)_M` regime (in particular the Drewitz–Ramírez threshold `M>15d+5`).

Thus the full source problem is reduced to one explicit statement:

> A ballistic i.i.d. uniformly elliptic RWRE cannot spend a linear-in-distance number of visits in the arbitrarily sparse, finite-range tilted-defect field produced by Theorem 2.1, except with `o(L^{-(d-1)})` probability.

## 6. Why this is materially different from the previous fixed-tilt route

The earlier global corrector required a fixed `theta>0` with

`limsup_n n^(-1) log E_0 exp(-theta X_n·u) <0`.

Positive speed does not provide that: subexponentially rare linear backtracking can destroy every fixed negative tilt.

Here `theta=alpha/n` is scale-dependent.  Bounded convergence and the LLN alone give

`E_0 exp(-alpha X_n·u/n) -> exp(-alpha v·u)`,                (6.1)

and the right side can be made arbitrarily small by choosing `alpha`.  There is no large-deviation assumption and no curvature interchange.

The price is also exact: contraction is not pointwise in every environment.  It fails on a sparse finite-range defect field, and Theorem 4.1 shows that **defect local time is the only multiplicative loss**.

This identifies a substantially sharper bottleneck than “construct an infinite-state corrector.”  Such a corrector now exists at mesoscopic scale with deterministic oscillation control; the unresolved theorem is an anti-trapping estimate for its sparse defects.

## 7. Relation to Guerra's seed condition and a caution

Guerra's condition `(W_{c,M})|ell` controls an expected **supremum over all entrance points** of a quenched bad-exit probability in a finite box.  Theorem 2.1 only gives a high-density field of pointwise tilted-contractive sites.  One cannot replace the supremum in `(W)` by a one-point estimate without proof: the random walk can select atypical environment locations, and rare bad clusters can accumulate large local time.

Therefore this artifact does **not** claim that high marginal density of good sites already proves `(W)` or `(T)`.  The precise missing bridge is (5.5), or a finite-scale analogue strong enough to verify `(W)`.

A promising next step is to coarse-grain the defect local time by clusters.  Since the defect field has arbitrarily small marginal and finite dependence range, spatially large defect clusters are amenable to percolative bounds; what remains is to control repeated returns to a small bad cluster.  Uniform ellipticity gives deterministic escape paths but their cost is exponential in cluster size.  Because the defect density can be made arbitrarily small, one should test whether the resulting cluster-size exponent can be made larger than the required `d-1` occupation exponent.  This is now a concrete quantitative calculation rather than an abstract corrector search.

## 8. Obligation ledger delta

- Global finite-periodic corrector: done previously.
- Integrable finite-cone corrector criterion: done previously.
- Regeneration-radius `d-1` bridge: done previously.
- Level-depth triangular reduction and forced-prefix obstruction: done previously.
- Fixed negative annealed tilt -> global `L^1` corrector: done previously, but fixed tilt is stronger than positive velocity.
- **Ballistic LLN -> arbitrarily strong mesoscopic annealed tilted contraction: DONE here.**
- **Mesoscopic contraction -> high-density finite-range good-site field: DONE here.**
- **Finite-horizon corrector with deterministic oscillation bound: DONE here.**
- **Global defect-charged supermartingale and exact wrong-way estimate (5.4): DONE here.**
- Sparse-defect local-time tail (5.5), or a direct finite-scale `(W)` seed: **OPEN; principal bottleneck.**

## 9. Next attack

Do not return to another finite-periodic example.  Analyze the sparse defect field from Theorem 2.1.  The next useful lemma should either:

1. bound the annealed local time accumulated in a connected component of tilted-defect sites by combining a finite-range cluster-size tail with a uniform-elliptic escape estimate, with constants tracked as the defect density tends to zero; or
2. replace site defects by coarse blocks in a way that preserves the pointwise resolvent inequality and makes the number of defect crossings, rather than time spent inside defects, the charged quantity.

The second option would be especially strong because finite-range percolation directly controls long chains of bad blocks, whereas raw local time can be amplified by repeated visits to one rare trap.
