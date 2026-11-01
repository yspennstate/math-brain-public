Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0487 — replica-overlap posterior lemma and sliding-window reduction

Role: R7-05 / C04 Random Environment Ballisticity, native ID `6aabe805f32881919992996e1c5cfad6`.

Run-start master snapshot: `702032d0b96a60b8701d0a51232ea03c0151041a`.
Pre-write master snapshot after concurrent peer work: `5e0289b2503129b17d109897faf5a28de2ca1337`.

Target: Drewitz--Ramirez, *Selected Topics in Random Walk in Random Environment*, Open Question 3.20. In i.i.d. uniformly elliptic nearest-neighbour RWRE on `Z^d`, `d>=2`, does a nonzero limiting velocity `v` with `v.ell>0` imply the source polynomial ballisticity condition `(P)_M|ell` for `M>15d+5`? Status in this work: **PROVED PARTIAL; full source implication not proved**.

A bounded current-primary-literature check was done once this run. Drewitz--Ramirez still state Open Question 3.20 in the above form; Guerra's polynomial criterion supplies the degree-`d-1` downstream bridge to `(T)` in the i.i.d. setting; Guerra--Ramirez's equivalence theorem identifies `(T)`, `(T')`, suitable `(T)_gamma`, and the standard `(P)_M` regime, but does not derive them from positive velocity alone. Search failure is not an independent proof of openness.

## 1. Inherited finite-horizon corrector

Fix a unit direction `u` in a compact cone with `v.u>0`. For a finite horizon `n`, put `theta=alpha/n` and

`(K f)(omega)=sum_e omega(0,e) exp(-theta e.u) f(tau_e omega)`.

Write

`Z=K^n 1`,

`H=sum_{j=0}^{n-1} K^j 1`.

The inherited rate-free LLN construction says that, for every prescribed `rho>0`, one may first choose `alpha>0` and then some finite `n` so that

`E_P Z <= rho`

uniformly on the chosen compact cone. Also, with

`a=max_{|e|_1=1}|e.u|`,

`s_alpha=(1-exp(-alpha a))/(alpha a)`,

`t_alpha=(exp(alpha a)-1)/(alpha a)`,

one has deterministically

`n s_alpha <= H <= n t_alpha`,

and the exact defect identity

`K H = H-1+Z`.

Define

`r=(K H)/H`, `c=log r`, `g=c_+`.

Then

`M_m = exp(-theta X_m.u) H(tau_{X_m}omega) exp(-sum_{k<m} c(tau_{X_k}omega))`

is an exact quenched martingale, and

`0 <= g <= Z/(n s_alpha)`.

For the wrong-way slab event

`A_L^u={tilde T_{-bL}^u < T_L^u}`

and `tau_L=tilde T_{-bL}^u wedge T_L^u`, the inherited stopping argument yields

`P_0(A_L^u) <= exp(alpha a) exp(-alpha bL/(2n)) + P_0(G_{tau_L}>alpha bL/(2n))`,   (1)

where

`G_m=sum_{k<m} g(tau_{X_k}omega)`.

The preceding report tried to control `G` by a posterior bound using the number of past positions in the radius-`n` dependency neighbourhood. The first result below shows that that particular reduction is intrinsically too coarse.

## 2. Decisive obstruction to the radius-n recycling count

For every nearest-neighbour path, define as in the preceding report

`E_t^(n)=sum_{k<t} 1_{ {|X_k-X_t|_1 <= n-1} }`.

### Lemma 2.1
For every nearest-neighbour path and every `t`,

`E_t^(n) >= min(t,n-1)`.

### Proof
For each `j=1,...,min(t,n-1)`, nearest-neighbour motion gives

`|X_t-X_{t-j}|_1 <= j <= n-1`.

Thus each of the previous `min(t,n-1)` positions is counted. QED.

Consequently, if the preceding exposure threshold satisfies `m<n-1`, then its heavy-recycling count obeys pathwise

`R_N^(n,m) >= (N-(n-1))_+`.                                      (2)

Thus the event called `heavy recycling` there is linear even for the most orderly ballistic path; it is not diagnosing exceptional trapping. To make the event nontrivial one must take `m>=n-1`. But the preceding posterior estimate then pays at least the factor `kappa^{-(n-1)}`. Therefore that proof architecture would require a relation of the schematic form

`rho << kappa^n`.                                                 (3)

The rate-free LLN construction gives only: for each `rho`, there exists some sufficiently large `n=n(rho)`. It supplies no relation between `rho` and `n(rho)` strong enough to imply (3). This is not an obstruction to P0487; it is a rigorous obstruction to the particular neighbourhood-exposure closure attempted in the preceding run.

## 3. Exact posterior factorization with overlap, not neighbourhood size

The correct posterior quantity is an actual-path/virtual-path intersection functional.

Let the single-site environment law be `mu`, supported on uniformly elliptic transition vectors `p=(p(e))`, with `p(e)>=kappa>0`. For a finite observed path

`gamma=(x_0,...,x_t)`,

let

`N_z(e)=#{j<t: x_j=z, x_{j+1}-x_j=e}`

and `|N_z|=sum_e N_z(e)`. For a deterministic virtual length-`n` path

`eta=(y_0=0,y_1,...,y_n)`,

translated to start from `x_t`, let `M_z(e)` denote its departure counts from the lattice site `z`, and `|M_z|=sum_e M_z(e)`.

For a count vector `A`, write

`L_A(p)=product_e p(e)^{A(e)}`,

`Phi(A)=int L_A(p) mu(dp)`.

The i.i.d. site structure gives the exact posterior site law

`d mu_{N_z}/d mu (p)=L_{N_z}(p)/Phi(N_z)`.

Therefore the conditional annealed likelihood of the virtual path is exactly

`prod_z Phi(N_z+M_z)/Phi(N_z)`,                           (4)

whereas its fresh annealed likelihood is

`prod_z Phi(M_z)`.                                        (5)

For every site with both `|N_z|>0` and `|M_z|>0`, uniform ellipticity gives two bounds:

`Phi(N_z+M_z) <= Phi(M_z)` and `Phi(N_z)>=kappa^{|N_z|}`,

hence

`[Phi(N_z+M_z)/Phi(N_z)] / Phi(M_z) <= kappa^{-|N_z|}`;

and, symmetrically,

`Phi(N_z+M_z) <= Phi(N_z)` and `Phi(M_z)>=kappa^{|M_z|}`,

hence

`[Phi(N_z+M_z)/Phi(N_z)] / Phi(M_z) <= kappa^{-|M_z|}`.

Define the symmetric departure-overlap count

`I(gamma,eta)=sum_z min(|N_z|,|M_z|)`.                         (6)

Multiplying the sitewise bounds proves:

### Theorem 3.1 — replica-overlap posterior bound
For every finite observed path `gamma` and every virtual path `eta`,

`P(eta | gamma) <= kappa^{-I(gamma,eta)} P_fresh(eta)`.         (7)

In particular, with `Z=K^n1`,

`E[ Z(tau_{X_t}omega) | gamma ]
 <= E_0[ exp(-theta Y_n.u) kappa^{-I(gamma,Y_{0:n})} ]`,        (8)

where the expectation on the right is over a fresh annealed length-`n` RWRE path `Y` started at zero, and the overlap is computed after translating that virtual path to `X_t`.

Because `g<=Z/(n s_alpha)`, the same right-hand side divided by `n s_alpha` bounds the conditional mean defect.

The key improvement over the previous `kappa^{-E_t^(n)}` estimate is exact: an old site that lies geometrically near `X_t` but is not actually used by the virtual path costs nothing. Only shared departure sites are charged.

### Strict-record specialization
Suppose `t` is a strict `u`-record time:

`X_s.u < X_t.u` for every `s<t`.

Then any shared site used by the translated virtual path must occur at a virtual location `y` with `y.u<0`. Hence

`I(gamma,Y) <= N_-^u(Y):=#{0<=j<n:Y_j.u<0}`.                  (9)

Thus (8) implies

`E[ Z(tau_{X_t}omega) | gamma ]
 <= E_0[ exp(-theta Y_n.u) kappa^{-N_-^u(Y)} ]`.              (10)

Equivalently, separating the fresh term,

`<= E_0 exp(-theta Y_n.u)
   + E_0[exp(-theta Y_n.u)(kappa^{-N_-^u(Y)}-1)]`.            (11)

The first term can be made `<=rho` by the inherited mesoscopic LLN construction. The second is a pure overlap/backtracking penalty. This shows exactly where i.i.d. spatial geometry must enter: the problem is no longer all local recycling, but intersections of the current past with a virtual future that has to backtrack behind a strict record to meet that past.

No claim is made here that (10) is small under positive velocity alone; that would require an additional theorem on the weighted backtracking/intersection term.

## 4. Stronger simplification after annealing: exact sliding-window identity

At the level of the first moment of the accumulated defect, even the posterior bound can be bypassed completely.

Let `F_t` denote the path history through time `t`. Quenched Markov property gives, for every `t`,

`Z(tau_{X_t}omega)
 = E_{0,omega}[exp(-theta (X_{t+n}-X_t).u) | F_t]`,           (12)

where on the right the same quenched walk is simply continued for `n` further steps.

Therefore, for every stopping time `T`,

`E_0[ 1_{t<T} Z(tau_{X_t}omega) ]
 = E_0[ 1_{t<T} exp(-theta (X_{t+n}-X_t).u) ]`.               (13)

Using `g<=Z/(n s_alpha)` and Tonelli, for `T=tau_L wedge N`,

`E_0 G_T
 <= (1/(n s_alpha))
    sum_{t=0}^{N-1}
    E_0[1_{t<tau_L} exp(-theta (X_{t+n}-X_t).u)].             (14)

Combining (1), Markov's inequality, and the split at `N=floor(A L)` gives the exact source-facing bound

`P_0(A_L^u)
 <= exp(alpha a) exp(-alpha bL/(2n))
    + P_0(tau_L>A L)
    + [2/(alpha b s_alpha L)]
      sum_{t<floor(A L)}
      E_0[1_{t<tau_L} exp(-(alpha/n)(X_{t+n}-X_t).u)]`.       (15)

This is a new and substantially cleaner reduction. It contains no static environment-selection term and no artificial radius-`n` recycling count. The remaining quantity is an annealed moving-window Laplace transform of actual future increments, observed before the slab exit.

### Why (15) does not already solve P0487
The ballistic strong law implies `(X_{t+n}-X_t)/n` is close to `v` on proportional macroscopic windows, but supplies no quantitative rate uniform in the joint scales needed to make the last two terms of (15) `o(L^{-(d-1)})`. In particular:

1. `P_0(tau_L>A L)->0` for `A>1/(v.u)` at the qualitative LLN level, but no polynomial tail follows merely from that convergence.
2. For fixed `alpha` and windows proportional to `L`, the Laplace factor approaches a positive constant of order `exp(-alpha v.u)`, not a polynomially small quantity.
3. Letting `alpha` grow like `log L` would formally create a polynomial factor, but the strong law alone gives no deviation rate strong enough to justify exchanging this growing exponential weight with the limit.

Thus (15) pinpoints a quantitative moving-window/regeneration estimate that is genuinely stronger than the LLN but weaker and more structured than a full pre-assumed `(T)` estimate.

## 5. New bridge criterion

Equation (15) gives a direct sufficient condition for the Guerra degree-`d-1` bridge. For every nearby `u` and every `b>0`, it is enough to find choices `n=n(L)`, `alpha=alpha(L)`, `A>1/(v.u)` such that

`alpha(L) L/n(L) >> log L`,                                  (16)

`L^{d-1} P_0(tau_L>A L) -> 0`,                               (17)

and

`L^{d-2}/alpha(L)
 * sum_{t<floor(A L)}
   E_0[1_{t<tau_L} exp(-(alpha(L)/n(L))(X_{t+n(L)}-X_t).u)]
 -> 0`.                                                       (18)

Then (15) gives

`L^{d-1} P_0(tilde T_{-bL}^u<T_L^u) -> 0`,

i.e. Guerra's degree-`d-1` polynomial condition in the required nearby directions. The known downstream implication then yields `(T)|ell`, and the standard equivalence machinery returns the source `(P)_M` regime for `M>15d+5`.

This criterion is **conditional**, not claimed from positive velocity in this run.

## 6. Interpretation and next mathematical attack

The previous bottleneck `linear occupation of a sparse defect field` was partly an artefact: its chosen exposure statistic is deterministically linear for any nearest-neighbour path once `m<n`. The corrected picture has two exact forms:

1. **quenched/posterior geometry:** only actual-past/virtual-future departure intersections matter, via `I(gamma,eta)`;
2. **annealed first moment:** accumulated defect is exactly controlled by moving-window Laplace transforms of the same walk, via (13)--(15).

This suggests the next useful attack should use regeneration blocks to estimate the moving-window quantity rather than another finite-periodic model. Positive velocity gives finite mean successful regeneration increments under the standard conditioning, so one should split a window `[t,t+n]` according to whether it contains a regeneration and then isolate the exceptional initial/failed block. The desired new lemma is a polynomial estimate for the contribution of windows intersecting an abnormally deep failed block. That would connect directly to the earlier `d-1`-moment initial-backtracking-radius bridge and avoid paying for ordinary nearby path history.

A complementary higher-dimensional route is to retain (8) and exploit actual two-path intersection estimates: at a strict record, any intersection requires virtual backtracking, and in dimensions where two forward ballistic paths have weak intersections the factor `kappa^{-I}` may be controllable without bounding all negative-halfspace occupation. This is explicitly complementary to the regeneration route, not a claim of a full solution.

## Obligation delta

- finite-state/periodic tilted corrector: DONE previously;
- rate-free mesoscopic finite-horizon corrector: DONE previously;
- weighted exact defect martingale: DONE previously;
- radius-`n` heavy-recycling closure: **REFUTED AS A RATE-FREE PROOF ROUTE this run** by Lemma 2.1;
- exact path/virtual-path posterior overlap theorem: **DONE this run**;
- strict-record backtracking specialization: **DONE this run**;
- exact annealed sliding-window identity and source-facing inequality (15): **DONE this run**;
- derive (16)--(18) from positive velocity/i.i.d. geometry: **OPEN; principal bottleneck**;
- full source implication: **OPEN / PROVED PARTIAL**.
