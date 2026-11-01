Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0487 — finite-cone corrector bridge, additive Poisson reduction, and an infinite-state obstruction

Date: 2026-09-20 UTC  
Worker: C04 / R7-05  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Status: **PROVED PARTIAL**; the full Drewitz--Ramírez implication remains open in this work.

## 1. Source target and inherited gap

Target: Alexander Drewitz and Alejandro F. Ramírez, *Selected Topics in Random Walks in Random Environment* (2014), Open Question 3.20. Under an i.i.d. uniformly elliptic nearest-neighbor environment on `Z^d`, `d>=2`, assume the limiting velocity has positive component in a direction `ell`. Does this imply the polynomial ballisticity condition `(P)_M|ell` at the standard large-`M` threshold? Later work of Guerra--Ramírez proves equivalence among `(T)`, `(T')`, `(T)_gamma` (for some `gamma`) and `(P)_M` for `M>=15d+5`, but does not derive them from positive velocity alone.

The preceding R7-05 run proved two complementary bridges:

1. if the pre-first-regeneration backward radius `R_u` has an `M`-th moment for every `u` near `ell`, then `(P*)_M|ell` follows;
2. if a tilted environment-space operator admits a positive corrector with any positive and negative moments, then the back face of every polynomial-volume box has arbitrarily high polynomially small exit probability.

The unresolved defect in item 2 was lateral exit: one tilt in direction `u` does not penalize side faces. This run removes that defect completely by using a finite cone of nearby tilted correctors. It then gives two exact constructions/reductions for such correctors and a countable-state obstruction showing why positive mean drift alone is insufficient in infinite state space.

The literature check this run was deliberately targeted rather than a repeated admission loop. The 2014 source definition of `(P*)_M` requires, for some neighborhood `V_ell`, every `u in V_ell` and every fixed `b>0`,

`L^M P_0(H_{bL}^{-u}<H_L^u) -> 0`.

No later source located in the bounded check supplies the missing implication from positive velocity; this is negative evidence only.

---

## 2. Setup: tilted environment operator

For a unit vector `u`, define the environment-space Markov operator

`(P_env f)(omega) = sum_{|e|=1} omega(0,e) f(tau_e omega)`

and the tilted operator

`(K_{theta,u} h)(omega)
 = sum_{|e|=1} omega(0,e) exp(-theta e.u) h(tau_e omega)`.

A positive function `h` satisfying

`K_{theta,u} h <= h`                                           (2.1)

produces the quenched nonnegative supermartingale

`M_n = exp(-theta X_n.u) h(tau_{X_n} omega)`.                 (2.2)

The previous run proved that if

`E[h^s] < infinity` and `E[h^{-q}] < infinity`                 (2.3)

for some `s,q>0`, then on any polynomial-volume box, exits through a face lying at `x.u <= -cL` have probability `o(L^{-M})` for every prescribed `M`.

The point below is that a *finite family* of such correctors automatically controls every non-front face and therefore the infinite slab event itself.

---

## 3. New theorem I — a finite cone of integrable correctors closes the lateral-exit gap

### Theorem 3.1 — finite-cone corrector criterion

Fix a unit target direction `v`. Choose an orthonormal basis

`v, e_2, ..., e_d`.

Assume there is an `eta>0` such that for the finite star of directions

`F(v,eta) = {v} union {u_j^+,u_j^- : 2<=j<=d}`,

where

`u_j^+ = (v + eta e_j)/sqrt(1+eta^2)`,
`u_j^- = (v - eta e_j)/sqrt(1+eta^2)`,                         (3.1)

there exist numbers `theta_u>0` and measurable positive functions `h_u` satisfying

`K_{theta_u,u} h_u <= h_u`                                    (3.2)

and, for each `u in F(v,eta)`, some positive exponents `s_u,q_u` with

`E[h_u^{s_u}] + E[h_u^{-q_u}] < infinity`.                    (3.3)

Then for every `M>0` and every `b>0`,

`L^M P_0(H_{bL}^{-v}<H_L^v) -> 0`.                            (3.4)

Thus a finite directional star of integrable tilted correctors implies the asymptotic polynomial slab estimate in direction `v` to *arbitrary* polynomial order.

#### Proof

Fix `M,b`. Let `R>2/eta` and define the finite rectangular box

`B_L = {x in Z^d:
        -bL < x.v < L,
        |x.e_j| < R L for j=2,...,d}`.                         (3.5)

Its volume is `O(L^d)`.

Consider the first exit time `T_L` from `B_L` (including a one-step boundary layer when applying the corrector estimate). If

`H_{bL}^{-v}<H_L^v`,

then the first exit from `B_L` cannot be through the front face `x.v >= L`: hitting that face would already realize `H_L^v` before the backward hit. Therefore

`{H_{bL}^{-v}<H_L^v}`

is contained in the union of the back-face exit event and the `2(d-1)` side-face exit events. We estimate those faces separately.

**Back face.** If `x.v <= -bL`, then with `u=v`,

`x.u <= -bL`.                                                  (3.6)

The previous `L^p` corrector estimate applied to `h_v` gives back-face probability `o(L^{-M})`.

**Positive `e_j` side.** Suppose the exit point satisfies

`x.e_j >= R L` and `x.v < L`.

Use the *opposite* tilted direction `u_j^-`. Then

`x.u_j^-
 = [x.v - eta x.e_j]/sqrt(1+eta^2)
 <= [1-eta R]L/sqrt(1+eta^2)
 = -c_* L`,                                                   (3.7)

where

`c_*=(eta R-1)/sqrt(1+eta^2)>0`.

Hence the `h_{u_j^-}` supermartingale makes this side exit `o(L^{-M})`.

**Negative `e_j` side.** If `x.e_j <= -R L`, use `u_j^+`; exactly the same computation gives

`x.u_j^+ <= -c_*L`.                                           (3.8)

Again the side-exit probability is `o(L^{-M})`.

There are only `2d-1` non-front faces. A finite union therefore gives (3.4). QED.

### Corollary 3.2 — open-cone version implies `(P*)_M`

Suppose there is an open neighborhood `U` of `ell` such that **every** `u in U` admits a corrector satisfying (3.2)--(3.3) (the exponents and corrector may depend on `u`). Then, after shrinking to a smaller neighborhood `V` with closure inside `U`, each `v in V` has a finite star `F(v,eta_v)` contained in `U`. Theorem 3.1 therefore gives, for every `v in V`, every `b>0` and every `M>0`,

`L^M P_0(H_{bL}^{-v}<H_L^v) -> 0`.

That is,

`(P*)_M|ell` holds for every `M>0`.                            (3.9)

For any `M` above the standard effective threshold, the established Berger--Drewitz--Ramírez / Guerra--Ramírez implications then yield the source polynomial ballisticity condition.

### Significance

The lateral-confinement condition left open in the preceding report is **not an independent obligation**. It can be eliminated by tilting in finitely many nearby directions. Thus the corrector route has been reduced to a single structural question:

> Does positive velocity provide sufficiently integrable positive tilted correctors on an open cone of directions around `ell`?

No extra exit-time or transverse-displacement estimate is needed once such a cone exists.

---

## 4. New theorem II — additive Poisson correctors exponentiate to the required multiplicative correctors

The finite-state proof from the earlier run can be reinterpreted through an additive Poisson correction. The same algebra gives a clean infinite-state bridge.

For a direction `u`, let

`d_u(omega)=sum_e omega(0,e) e.u`.

### Theorem 4.1 — additive-to-multiplicative corrector bridge

Assume there exists a measurable `chi:Omega->R`, constants `delta>0`, `C<infinity`, such that for `P`-a.e. `omega`,

`d_u(omega) + (P_env chi)(omega) - chi(omega) >= delta`,       (4.1)

and for every nearest-neighbor step with positive transition probability,

`|e.u + chi(tau_e omega)-chi(omega)| <= C`.                   (4.2)

Assume also that for some `r>0`,

`E[exp(r |chi|)] < infinity`.                                 (4.3)

Then for all sufficiently small `theta>0`,

`h_theta(omega)=exp(-theta chi(omega))`                        (4.4)

satisfies

`K_{theta,u} h_theta <= h_theta`,                              (4.5)

and has both a positive and a negative moment. Consequently, if such additive correctors exist for every direction in an open cone around `ell`, then `(P*)_M|ell` holds for every `M>0` by Corollary 3.2.

#### Proof

Set

`Y_e(omega)=e.u + chi(tau_e omega)-chi(omega)`.

Then (4.1) says

`sum_e omega(0,e) Y_e(omega) >= delta`,                       (4.6)

while (4.2) gives `|Y_e|<=C`.

Using (4.4),

`(K_{theta,u} h_theta)(omega)/h_theta(omega)
 = sum_e omega(0,e) exp[-theta Y_e(omega)]`.                  (4.7)

For `|y|<=C`, Taylor's theorem with a uniform remainder gives

`exp(-theta y)
 <= 1-theta y + (theta^2 C^2/2) exp(theta C)`.                (4.8)

Average (4.8) using `omega(0,e)` and (4.6):

`K_{theta,u}h_theta/h_theta
 <= 1-theta delta + (theta^2 C^2/2) exp(theta C)`.             (4.9)

Choose `theta>0` sufficiently small that

`(theta C^2/2) exp(theta C) <= delta`.

Then the right side of (4.9) is at most one, proving (4.5).

Finally, choose positive `s,q` so small that

`s theta < r` and `q theta < r`.

Then

`h_theta^s <= exp(s theta |chi|)`,
`h_theta^{-q} <= exp(q theta |chi|)`,

and both expectations are finite by (4.3). QED.

### Interpretation

For finite-state environment chains, the Poisson equation can be solved with bounded `chi`, so positive stationary mean drift is enough to obtain the multiplicative Perron corrector. In the true i.i.d. RWRE environment space, Theorem 4.1 isolates the missing regularity requirement: one needs a pointwise positive **corrected** drift with controlled coboundary increments and an exponentially integrable additive corrector.

This is a more structured target than searching directly for an arbitrary positive eigenfunction.

---

## 5. New exact construction — the Feynman--Kac potential is a canonical multiplicative corrector whenever finite

There is also a canonical candidate requiring no Poisson equation.

For `theta>0`, define

`H_{theta,u}(omega)
 = sum_{n=0}^infinity (K_{theta,u}^n 1)(omega)
 = sum_{n=0}^infinity E_{0,omega}[exp(-theta X_n.u)]`.          (5.1)

### Proposition 5.1

If `H_{theta,u}<infinity` almost surely, then

`K_{theta,u} H_{theta,u}=H_{theta,u}-1 <= H_{theta,u}`.        (5.2)

Also `H_{theta,u}>=1`, so every negative moment is automatically bounded by one. Hence if for some `s>0`,

`E[H_{theta,u}^s]<infinity`,                                  (5.3)

then `H_{theta,u}` satisfies the complete moment hypothesis of Theorem 3.1.

#### Proof

All summands in (5.1) are nonnegative, so monotone convergence permits applying the positive operator termwise:

`K H = sum_{n>=0} K^{n+1}1 = H-1`.

The `n=0` term of `H` equals one, proving `H>=1` and thus `H^{-q}<=1` for every `q>0`. QED.

Therefore another exact route to P0487 is:

`positive velocity`

`=> for every u in an open cone, some theta_u>0 has`

`E[(sum_n E_{0,omega} exp(-theta_u X_n.u))^{s_u}] < infinity`. (5.4)

This is a concrete quenched Feynman--Kac summability problem. It is still unproved here and may itself encode much of the ballisticity difficulty, but it supplies a canonical object rather than an unspecified eigenfunction.

---

## 6. New obstruction — positive mean drift does not extend the finite-state Perron argument to an infinite state space

The finite-state proof might suggest that one should periodize the environment, solve a Perron problem, and pass to a limit. The following exact Markov-additive model shows why positive mean drift alone gives no compactness: rare arbitrarily long negative phases force every multiplicative corrector to have catastrophic oscillation.

This is **not** an i.i.d. RWRE counterexample. It is a decisive obstruction to an abstract infinite-state extension of the finite-periodic argument.

### Proposition 6.1 — positive speed with no `L^s` tilted corrector

There exists an irreducible positive recurrent aperiodic countable-state Markov chain `J_n` and a bounded additive increment `Z_n in {-1,+1}` such that:

1. both signs occur at every state with probability at least a fixed `kappa>0`;
2. the stationary mean increment is strictly positive;
3. nevertheless, for every `theta>0`, every positive `h` satisfying

   `K_theta h <= h`                                            (6.1)

   has

   `E_pi[h^s]=infinity`                                       (6.2)

   for every `s>0`, where `pi` is the stationary law;
4. on `l^infinity`, the tilted operator has spectral radius strictly larger than one.

#### Construction

Fix `0<kappa<1/2`. The state space consists of one good state `G` and trap states

`T_{n,k}`,  `n>=1`, `1<=k<=n`.

At `G`, with probability `1-epsilon` stay at `G`; with probability `epsilon a_n` enter `T_{n,n}`, where

`a_n = c n^{-3}`                                              (6.3)

and `c` normalizes `sum_n a_n=1`.

Inside a trap the state countdown is deterministic:

`T_{n,k} -> T_{n,k-1}` for `k>=2`,
`T_{n,1} -> G`.                                               (6.4)

This chain is irreducible and aperiodic; it is positive recurrent because

`E[N]=sum_n n a_n<infinity`.

The additive increment is sampled conditionally on the current state, independently of the next-state choice:

- at `G`: `P(Z=+1)=1-kappa`, `P(Z=-1)=kappa`;
- at every trap state: `P(Z=-1)=1-kappa`, `P(Z=+1)=kappa`.

Thus both increment signs have conditional probability at least `kappa` everywhere.

A regenerative cycle consists of a geometric good-state sojourn of mean

`E[J]=1/epsilon`

followed by a trap of mean length `E[N]`. Therefore the stationary good/trap fractions are

`pi_G = E[J]/(E[J]+E[N])`,
`pi_T = E[N]/(E[J]+E[N])`.                                   (6.5)

Choose `epsilon E[N]<1`; then `pi_G>pi_T`. Since the mean increment is `+(1-2kappa)` in `G` and `-(1-2kappa)` in traps,

`mu = (1-2kappa)(pi_G-pi_T) > 0`.                             (6.6)

By the ergodic theorem, the additive coordinate has positive asymptotic speed `mu`.

#### No integrable multiplicative corrector

At a trap state, let

`m_-(theta)=(1-kappa)e^{theta}+kappa e^{-theta}`.              (6.7)

For every `theta>0`,

`m_-(theta)>1`,                                               (6.8)

because `m_-(0)=1` and

`m_-'(theta)=(1-kappa)e^{theta}-kappa e^{-theta}>1-2kappa>0`.

The tilted kernel at `T_{n,k}` is

`(K_theta h)(T_{n,k})=m_-(theta) h(T_{n,k-1})`                (6.9)

(with `T_{n,0}=G`). Thus (6.1) forces

`h(T_{n,k}) >= m_-(theta) h(T_{n,k-1})`,

and iteration gives

`h(T_{n,n}) >= m_-(theta)^n h(G)`.                            (6.10)

In stationarity, each cycle visits `T_{n,n}` exactly once when the chosen trap length equals `n`, so

`pi(T_{n,n}) = a_n/(E[J]+E[N])`.                              (6.11)

Therefore, for every `s>0`,

`E_pi[h^s]
 >= C h(G)^s sum_{n>=1} a_n m_-(theta)^{sn}
 = infinity`,                                                 (6.12)

since `a_n` has only polynomial decay while `m_-^{sn}` grows exponentially. This proves item 3.

Finally, for every integer `r`, choose a trap with length at least `r`. Starting from its entrance state,

`K_theta^r 1 >= m_-(theta)^r`.

Hence

`||K_theta^r||_{infinity->infinity} >= m_-(theta)^r`,

and the spectral-radius formula gives

`r_infty(K_theta) >= m_-(theta)>1`.                           (6.13)

This proves item 4. QED.

### Consequence for the P0487 strategy

The finite-state Perron proof cannot be extended using only:

- positive stationary mean drift;
- bounded increments;
- even a uniform two-sided lower bound on increment probabilities.

Infinite state space permits rare adverse regions of unbounded length, and these can force any positive tilted corrector to grow exponentially on states whose stationary probability decays only polynomially.

The genuine i.i.d. RWRE proof, if it follows a corrector route, must therefore use *spatial* independence and geometry to rule out this loss of integrability, rather than relying on an abstract environment-process mean drift.

---

## 7. Obligation ledger and exact progress

Full-source metric:

`FULL_SOURCE_IMPLICATION = 0 -> 0`.

No complete proof yet shows that positive velocity alone implies `(P)_M` under every original i.i.d. uniformly elliptic hypothesis.

Useful obligation ledger:

- finite-state / periodic positive-drift exponential corrector: **DONE, inherited**;
- first-regeneration radius moment `=> (P*)_M`: **DONE, inherited**;
- one-direction `L^p` / inverse-`L^q` corrector `=>` arbitrary polynomial back-face decay: **DONE, inherited**;
- lateral-exit gap in the corrector route: **DONE this run** via Theorem 3.1;
- additive controlled Poisson corrector `=>` multiplicative tilted corrector: **DONE this run** via Theorem 4.1;
- canonical Feynman--Kac potential corrector: **DONE this run** via Proposition 5.1;
- abstract infinite-state positive-drift Perron extension: **REFUTED as a method** by Proposition 6.1;
- positive velocity in i.i.d. uniformly elliptic RWRE `=>` an integrable corrector on an open cone, or equivalently a high moment of first-block backtracking radius: **OPEN, principal source gap**.

This run therefore removes one previously explicit auxiliary obligation (lateral confinement) and identifies a sharper functional-analytic target for the remaining source implication.

---

## 8. Next concrete attack

The next run should use the i.i.d. *spatial* structure rather than abstract environment-process ergodicity.

The strongest concrete target suggested by the new lemmas is to build a **scale-dependent cone corrector** from fresh slabs. A useful intermediate statement would be:

> For each direction `u` in a fixed cone around `ell`, construct at some mesoscopic scale `L` a positive random transfer weight `H_{L,u}` whose multiplicative oscillation across one fresh slab has a nonzero positive and negative moment and for which the expected tilted transfer is a strict contraction.

If independent successive fresh slabs make these weights multiplicative, Theorem 3.1 shows that only a finite directional star is needed to control the whole slab, including lateral exits. Proposition 6.1 shows exactly what must be prevented: a polynomially likely sequence of arbitrarily long adverse phases whose required corrector amplification is exponential in phase length.

A second, regeneration-side formulation of the same target is to prove that a depth-`r` initial backtrack either crosses a positive fraction of fresh longitudinal slabs (allowing i.i.d. tensorization) or is trapped in a sublinear longitudinal region whose repeated recycling has sufficiently small probability under positive velocity. Establishing a superlinear tail recursion for the first-block radius remains a valid alternative.

No such final tensorization inequality is claimed here.