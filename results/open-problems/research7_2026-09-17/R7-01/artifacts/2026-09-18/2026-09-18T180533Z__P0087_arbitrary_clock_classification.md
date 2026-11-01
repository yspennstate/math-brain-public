Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0087: arbitrary-clock classification and the precise meaning of the singular interacting Wright–Fisher heuristic

Date: 2026-09-18.  
Worker: R7-01 (`6aabe777361481919c9e614646464772`).  
Captured start master: `c6a42e9f8e2b7bb8b3fb5578a9827e4a212e4e4e`.  
Fresh pre-write master: `faef3a064e4ebc94c0414d616fd4da79138e3008`.  
Source: G. Aletti et al., *Open Problems in Stochastic Reinforcement Models*, Open Problem 16, printed pp. 14–16, DOI `10.1007/978-3-031-76738-8_29`.  
Status: mathematical source answer strengthened; operationally **PARTIAL** pending independent audits / final prior-art reconciliation / source-scoped paper packaging. Novelty remains **UNVERIFIED**.

## 1. Why this is the final mathematical recovery for P0087

The previous STUCK2 diagnosis isolated one source-facing question not yet stated as a theorem: could some scalar clock other than the already analyzed `epsilon^{-1}` and `epsilon^{-2}` clocks retain both a finite network-interaction term and a nondegenerate Wright–Fisher noise term? The source's printed heuristic contains precisely that apparent coexistence.

This artifact executes the single recovery selected there, using the prescribed nonrepeating methods:

- **B1 — change mathematical category:** rewrite the problem in semimartingale-characteristic / singular-perturbation language and classify arbitrary scalar clocks;
- **B20 — find why the obvious algorithm fails:** prove that the recipe “choose a clock which keeps both effects of order one” is algebraically impossible;
- **B23 — do what the proposer did not expect:** assume the printed finite-dimensional interacting-diffusion heuristic has no ordinary Itô interpretation and prove the strongest correct lower-dimensional alternative, including the over-accelerated regime.

No finite checker is relevant: every claim below is theorem-sized and is proved on the page.

The frozen owner metric remains `M_clause(P0087)=2/2`; it is already saturated and is **not** redefined here.

---

## 2. Model and cumulative inputs

Write

\[
\varepsilon=r_r,\qquad f_\varepsilon=r_f,\qquad Q=A^T,
\]

and assume the source-critical relation

\[
\frac{f_\varepsilon}{\varepsilon^2}\longrightarrow c\in[0,\infty).
\tag{2.1}
\]

The exact recursion is

\[
Z_{n+1}^\varepsilon
=Z_n^\varepsilon+
\varepsilon(Q-I)Z_n^\varepsilon
+f_\varepsilon(p-Z_n^\varepsilon)
+\varepsilon\xi_{n+1}^\varepsilon,
\tag{2.2}
\]

where, under the source network convention, conditional on `F_n` the coordinates of `X_{n+1}` are independent Bernoulli variables with mean `QZ_n`, and

\[
\xi_{n+1}^\varepsilon=X_{n+1}^\varepsilon-QZ_n^\varepsilon,
\qquad
E[\xi_{n+1}^\varepsilon\mid\mathcal F_n]=0.
\]

Let `pi` be the strictly positive stationary probability vector of the fixed irreducible row-stochastic matrix `Q`:

\[
\pi^TQ=\pi^T,\qquad \pi^T\mathbf1=1.
\]

Put

\[
Y_n^\varepsilon=\pi^TZ_n^\varepsilon,
\quad
P=I-\mathbf1\pi^T,
\quad
W_n^\varepsilon=PZ_n^\varepsilon,
\quad
\bar p=\pi^Tp,
\quad
\kappa=\sum_j\pi_j^2.
\tag{2.3}
\]

On `H={w:pi^T w=0}`, set

\[
B=(I-Q)|_H.
\]

All eigenvalues of `B` have strictly positive real part, so for some fixed `C,a>0`,

\[
\|e^{-sB}\|\le Ce^{-as},\qquad s\ge0.
\tag{2.4}
\]

The exact projected recursions are

\[
Y_{n+1}^\varepsilon-Y_n^\varepsilon
=f_\varepsilon(\bar p-Y_n^\varepsilon)
+\varepsilon\eta_{n+1}^\varepsilon,
\qquad
\eta_{n+1}^\varepsilon=\pi^T\xi_{n+1}^\varepsilon,
\tag{2.5}
\]

and

\[
W_{n+1}^\varepsilon
=T_\varepsilon W_n^\varepsilon
+f_\varepsilon Pp
+\varepsilon P\xi_{n+1}^\varepsilon,
\qquad
T_\varepsilon=I-\varepsilon B-f_\varepsilon I.
\tag{2.6}
\]

The cumulative R7-01 record has already proved:

1. the fixed-parameter convergence classification;
2. on the `epsilon^{-2}` clock, `Y` converges to the Jacobi/Wright–Fisher diffusion
   \[
   dY_t=c(\bar p-Y_t)dt+\sqrt{\kappa Y_t(1-Y_t)}\,dB_t;
   \tag{2.7}
   \]
3. transverse collapse on positive slow times;
4. the `epsilon^{-1}` deterministic synchronization layer and its transverse OU fluctuation;
5. the uniform matched decomposition through time zero;
6. finite-step Wasserstein contraction and the critical stationary limit.

Those theorems are used below as pinned cumulative inputs rather than rederived.

---

## 3. B20: the exact clock obstruction

Let `m_epsilon>0` be an arbitrary deterministic number of discrete steps per unit macroscopic time and define

\[
\widetilde Z^\varepsilon(t)
=Z^\varepsilon_{\lfloor m_\varepsilon t\rfloor}.
\tag{3.1}
\]

The three relevant characteristic scales per unit macroscopic time are

\[
D_\varepsilon:=m_\varepsilon\varepsilon
\quad\text{(network drift)},
\]

\[
V_\varepsilon:=m_\varepsilon\varepsilon^2
\quad\text{(martingale quadratic variation)},
\]

and

\[
F_\varepsilon:=m_\varepsilon f_\varepsilon
\quad\text{(forcing drift)}.
\]

By (2.1), identically along every sequence,

\[
\boxed{
V_\varepsilon=\varepsilon D_\varepsilon,
\qquad
F_\varepsilon=(f_\varepsilon/\varepsilon^2)V_\varepsilon
\sim cV_\varepsilon.
}
\tag{3.2}
\]

Therefore

\[
\boxed{\frac{V_\varepsilon}{D_\varepsilon}=\varepsilon\to0.}
\tag{3.3}
\]

This already proves the qualitative impossibility statement: no scalar clock can have simultaneously

\[
D_\varepsilon\to d\in(0,\infty)
\quad\text{and}\quad
V_\varepsilon\to v\in(0,\infty).
\tag{3.4}
\]

Thus no ordinary finite-dimensional Itô limit can preserve both a finite network drift and nondegenerate Wright–Fisher noise as separate order-one terms. The rest of this artifact proves the complete finite-clock alternatives and the source-critical lower-dimensional limit.

---

# 4. B1: arbitrary scalar-clock classification

Assume throughout this section that

\[
Z_0^\varepsilon\longrightarrow z_0\in[0,1]^N,
\qquad
y_0=\pi^Tz_0,
\qquad
w_0=Pz_0.
\tag{4.1}
\]

All convergences of initial data may be read in probability; deterministic initial data are a special case.

## Theorem 4.1 (complete classification through finite slow quadratic-variation scale)

Along any subsequence on which `D_epsilon` and `V_epsilon` have limits, the following hold.

### Regime A: finite network clock

If

\[
D_\varepsilon\to d\in[0,\infty),
\tag{4.2}
\]

then `V_epsilon -> 0` and `F_epsilon -> 0`, and for every fixed `T`,

\[
\boxed{
\sup_{0\le t\le T}
\left\|
\widetilde Z^\varepsilon(t)
-e^{dt(Q-I)}z_0
\right\|\xrightarrow{P}0.
}
\tag{4.3}
\]

Thus `d=0` gives the frozen path `z_0`, while `0<d<infinity` gives the deterministic network synchronization flow. There is no forcing and no diffusion at leading order.

### Regime B: between the fast and diffusive clocks

If

\[
D_\varepsilon\to\infty,
\qquad
V_\varepsilon\to0,
\tag{4.4}
\]

then for every `T<infinity`,

\[
\sup_{0\le t\le T}
|\pi^T\widetilde Z^\varepsilon(t)-y_0|
\xrightarrow{P}0,
\tag{4.5}
\]

and for every `0<delta<T`,

\[
\boxed{
\sup_{\delta\le t\le T}
\|\widetilde Z^\varepsilon(t)-\mathbf1y_0\|
\xrightarrow{P}0.
}
\tag{4.6}
\]

If `w_0=0`, (4.6) holds with `delta=0`. If `w_0!=0`, there is no ordinary right-continuous vector limit on `[0,T]` which both preserves the actual initial state and equals the consensus value at every positive time.

### Regime C: finite nonzero diffusive clock

If

\[
V_\varepsilon\to v\in(0,\infty),
\tag{4.7}
\]

then automatically `D_epsilon=V_epsilon/epsilon -> infinity`. The Perron coordinate satisfies

\[
\pi^T\widetilde Z^\varepsilon(\cdot)
\Rightarrow \widetilde Y(\cdot)
\tag{4.8}
\]

where

\[
\widetilde Y_t=Y_{vt}
\]

for the Jacobi diffusion (2.7), equivalently

\[
\boxed{
 d\widetilde Y_t
 =cv(\bar p-\widetilde Y_t)dt
 +\sqrt{v\kappa\widetilde Y_t(1-\widetilde Y_t)}\,dB_t.
}
\tag{4.9}
\]

Moreover, for every `0<delta<T`,

\[
\boxed{
\sup_{\delta\le t\le T}
\|\widetilde Z^\varepsilon(t)-\mathbf1\pi^T\widetilde Z^\varepsilon(t)\|
\xrightarrow{P}0.
}
\tag{4.10}
\]

Hence on every positive-time interval the vector limit is the lower-dimensional process `1 widetilde Y`. If `w_0=0`, the convergence holds on `[0,T]`; if `w_0!=0`, the already-proved matched initial layer is intrinsic.

### Consequence

Every scalar clock with a nondegenerate Wright–Fisher limit necessarily sends the transverse network drift to infinity and constrains the limit to the consensus manifold. Conversely, every scalar clock which keeps the network drift finite kills the diffusion.

### Proof

We prove the three regimes separately.

#### Proof of Regime A

Write

\[
S_\varepsilon=(1-\varepsilon-f_\varepsilon)I+\varepsilon Q
=I+\varepsilon(Q-I)-f_\varepsilon I.
\tag{4.11}
\]

Iteration of (2.2) gives

\[
Z_n^\varepsilon
=S_\varepsilon^nZ_0^\varepsilon
+f_\varepsilon\sum_{j=0}^{n-1}S_\varepsilon^jp
+\varepsilon\sum_{k=1}^nS_\varepsilon^{n-k}\xi_k^\varepsilon.
\tag{4.12}
\]

Because `Q` is row-stochastic and all coefficients in `S_epsilon` are nonnegative for small `epsilon`, its infinity-operator norm is at most `1-f_epsilon<=1`.

For `n=floor(m_epsilon t)` with `D_epsilon -> d<infinity`, standard finite-dimensional Euler convergence gives, uniformly for `0<=t<=T`,

\[
S_\varepsilon^{\lfloor m_\varepsilon t\rfloor}
\longrightarrow e^{dt(Q-I)},
\tag{4.13}
\]

because `m_epsilon epsilon -> d` while

\[
m_\varepsilon f_\varepsilon=F_\varepsilon\sim cV_\varepsilon
=c\varepsilon D_\varepsilon\to0.
\]

The forcing term in (4.12) is bounded by

\[
f_\varepsilon n\|p\|
\le CTF_\varepsilon=o(1).
\tag{4.14}
\]

For each fixed coordinate, the final term in (4.12) is a martingale transform with increments bounded by `C epsilon`; for `n<=m_epsilon T`, the sum of squared bounds is at most

\[
C m_\varepsilon T\varepsilon^2=CTV_\varepsilon=O(\varepsilon).
\tag{4.15}
\]

Azuma–Hoeffding followed by a union bound over `O(m_epsilon)=O(epsilon^{-1})` indices implies

\[
\max_{n\le m_\varepsilon T}
\left\|\varepsilon\sum_{k=1}^nS_\varepsilon^{n-k}\xi_k^\varepsilon\right\|
=o_P(1).
\tag{4.16}
\]

Combining (4.12)–(4.16) and (4.1) proves (4.3).

#### Proof of Regime B

From (2.5),

\[
Y_n^\varepsilon-Y_0^\varepsilon
=f_\varepsilon\sum_{k<n}(\bar p-Y_k^\varepsilon)
+\varepsilon\sum_{k<n}\eta_{k+1}^\varepsilon.
\tag{4.17}
\]

The first term is uniformly at most `Cm_epsilon T f_epsilon=O(F_epsilon)->0`. The martingale has predictable quadratic variation at most `Cm_epsilon T epsilon^2=O(V_epsilon)->0`; Doob's inequality therefore proves (4.5).

For the transverse coordinate, iteration of (2.6) gives

\[
W_n^\varepsilon
=T_\varepsilon^nW_0^\varepsilon
+f_\varepsilon\sum_{j<n}T_\varepsilon^jPp
+\varepsilon\sum_{k=1}^nT_\varepsilon^{n-k}P\xi_k^\varepsilon.
\tag{4.18}
\]

The cumulative spectral estimate gives

\[
\|T_\varepsilon^j\|\le Ce^{-a\varepsilon j}.
\tag{4.19}
\]

For `n>=m_epsilon delta`, the initial term is at most

\[
Ce^{-a\varepsilon m_\varepsilon\delta}\|W_0^\varepsilon\|
=Ce^{-aD_\varepsilon\delta}\|W_0^\varepsilon\|\to0.
\tag{4.20}
\]

The deterministic forcing term is uniformly

\[
O(f_\varepsilon/\varepsilon)=O(\varepsilon).
\tag{4.21}
\]

For every fixed `n`, the stochastic convolution in (4.18) has exponentially decaying deterministic coefficients and squared increment bound

\[
C\varepsilon^2\sum_{j\ge0}e^{-2a\varepsilon j}
\le C\varepsilon.
\tag{4.22}
\]

Since `V_epsilon -> 0` implies `m_epsilon=o(epsilon^{-2})`, a union bound over all `n<=m_epsilon T` with Azuma gives a uniform `o_P(1)` bound (indeed the previous cumulative estimate `O_P(sqrt(epsilon log(1/epsilon)))` applies). This proves (4.6). The time-zero assertion follows because `W_0^epsilon->w_0`; a fixed càdlàg limit taking value `z_0` at zero and `1y_0` at all positive times cannot be right-continuous unless `w_0=0`.

#### Proof of Regime C

Define the already-analyzed slow-clock coordinate

\[
Y_{\rm slow}^\varepsilon(s)
=Y^\varepsilon_{\lfloor s/\varepsilon^2\rfloor}.
\tag{4.23}
\]

Then, up to the immaterial integer-floor convention,

\[
\pi^T\widetilde Z^\varepsilon(t)
=Y_{\rm slow}^\varepsilon(V_\varepsilon t).
\tag{4.24}
\]

The cumulative diffusion theorem gives `Y_slow^epsilon => Y` on every fixed compact interval, and the limit is continuous. Since `V_epsilon -> v`, the continuous-mapping theorem for deterministic time changes yields (4.8). Brownian time change gives exactly (4.9).

Because `D_epsilon=V_epsilon/epsilon -> infinity`, the transverse argument from Regime B applies on every `[delta,T]`; alternatively it follows immediately from the cumulative matched theorem on the bounded slow interval `[0,(v+1)T]`. This gives (4.10) and completes the proof. QED.

---

# 5. B23: the over-accelerated regime and why there is no hidden fourth diffusion

The classification above handles every subsequence with bounded `V_epsilon`. One must still explain what `V_epsilon -> infinity` means; otherwise a putative fourth scalar-clock regime could be hidden there.

For the nondegenerate source case

\[
c>0,\qquad 0<\bar p<1,
\tag{5.1}
\]

there is in fact **no ordinary càdlàg path limit** under such over-acceleration.

## Theorem 5.1 (super-diffusive scalar clocks are not path-tight in the nondegenerate forced case)

Assume (5.1) and

\[
V_\varepsilon=m_\varepsilon\varepsilon^2\to\infty.
\tag{5.2}
\]

Then `{widetilde Z^epsilon}` is not tight in `D([delta,T],[0,1]^N)` for any `0<delta<T`.

### Proof

For every fixed `epsilon` with `f_epsilon>0`, the cumulative coupling theorem gives the exact contraction

\[
W_{1,\pi}(\mu K_\varepsilon^n,\nu K_\varepsilon^n)
\le(1-f_\varepsilon)^nW_{1,\pi}(\mu,\nu),
\tag{5.3}
\]

so there is a unique invariant law `mu_epsilon` and, uniformly in the starting state,

\[
W_{1,\pi}(\delta_zK_\varepsilon^n,\mu_\varepsilon)
\le C(1-f_\varepsilon)^n.
\tag{5.4}
\]

The cumulative stationary theorem for the critical family `f_epsilon/epsilon^2 -> c` gives

\[
\mu_\varepsilon\Rightarrow \nu_c,
\tag{5.5}
\]

where `nu_c` is supported on the consensus line and its Perron coordinate has the nondegenerate beta law

\[
\operatorname{Beta}\left(
\frac{2c\bar p}{\kappa},
\frac{2c(1-\bar p)}{\kappa}
\right).
\tag{5.6}
\]

Take fixed macroscopic times

\[
0<t_1<\cdots<t_k.
\]

Every gap contains asymptotically

\[
m_\varepsilon(t_{i+1}-t_i)
\]

steps, and

\[
f_\varepsilon m_\varepsilon(t_{i+1}-t_i)
\sim cV_\varepsilon(t_{i+1}-t_i)\to\infty.
\tag{5.7}
\]

Thus (5.4) makes every positive-time transition uniformly forget its incoming state. Iterating the Markov property and testing against bounded Lipschitz functions yields

\[
(\widetilde Z^\varepsilon(t_1),\ldots,\widetilde Z^\varepsilon(t_k))
\Rightarrow
(U_1,\ldots,U_k),
\tag{5.8}
\]

where `U_1,...,U_k` are independent with common law `nu_c`.

Suppose for contradiction that a subsequence were tight in `D([delta,T])`. Extract a weakly convergent further subsequence with càdlàg limit `X`. There is a dense set `C subset [delta,T]` of deterministic times at which the evaluation map is almost surely continuous under the law of `X`. Choose `t in C` and `t_j in C` with `t_j downarrow t`, `t_j>t`.

For each fixed `j`, (5.8) forces `X(t)` and `X(t_j)` to be independent with common law `nu_c`. Since `nu_c` is nondegenerate, choose a bounded continuous scalar function `h` with

\[
\operatorname{Var}_{\nu_c}(h)>0.
\]

Then for every `j`,

\[
E[(h(X(t_j))-h(X(t)))^2]
=2\operatorname{Var}_{\nu_c}(h)>0.
\tag{5.9}
\]

But càdlàg right-continuity gives `X(t_j)->X(t)` almost surely, and bounded convergence makes the left side of (5.9) tend to zero, a contradiction. Therefore no such tight subsequence exists. QED.

### Degenerate qualifications

The no-tightness conclusion uses `c>0` and `0<bar p<1`, which make the critical stationary limit nondegenerate. If `bar p` is 0 or 1, the invariant limit collapses to an endpoint. If `c=0`, the forcing mixing time is longer than `epsilon^{-2}` and an additional relation between `m_epsilon` and `f_epsilon^{-1}` is needed; there is no honest universal statement depending on `V_epsilon` alone. These degenerate extensions are not needed to interpret the source's nontrivial forced critical regime and are deliberately not promoted to a false universal theorem.

---

# 6. Exact interpretation of the printed heuristic

The source writes a formal “interacting Wright–Fisher” dynamics with a usual `dt` forcing term, a network term marked heuristically at `sqrt(dt)` scale, and a Wright–Fisher noise term. The clock identity (3.2) shows why that notation is singular.

On a scalar clock with finite interaction strength,

\[
D_\varepsilon\to d<\infty,
\]

the stochastic quadratic variation satisfies

\[
V_\varepsilon=\varepsilon D_\varepsilon\to0.
\]

On a clock with finite nonzero Wright–Fisher quadratic variation,

\[
V_\varepsilon\to v>0,
\]

the network interaction strength is

\[
D_\varepsilon=V_\varepsilon/\varepsilon\to\infty.
\]

Therefore the network term is not a second ordinary finite coefficient in an `N`-dimensional Itô SDE. It is a **singular restoring drift** which constrains the limit to

\[
\Gamma=\{\mathbf1 y:0\le y\le1\}.
\]

The surviving tangent coordinate is `y=pi^Tz`, and its exact critical diffusion is (4.9). For the source clock `v=1`,

\[
\boxed{
 dY_t=c(\bar p-Y_t)dt
 +\sqrt{\kappa Y_t(1-Y_t)}\,dB_t,
\qquad
\kappa=\sum_j\pi_j^2.
}
\tag{6.1}
\]

Thus the mathematically proper interpretation of the singular heuristic is a fast stable-manifold constraint plus a lower-dimensional Wright–Fisher/Jacobi diffusion, with an explicit initial synchronization layer for nonsynchronized starts.

---

# 7. Katzenberger reconciliation: what is prior art and what remains source-specific

A same-day literature check recovered Gary S. Katzenberger, *Solutions of a Stochastic Differential Equation Forced Onto a Manifold by a Large Drift*, Annals of Probability 19(4) (1991), 1587–1628, DOI `10.1214/aop/1176990225`.

Its abstract treats semimartingales with a vector field whose deterministic flow has an asymptotically stable manifold of fixed points, together with a drift clock which places asymptotically infinite mass on every positive time interval. The resulting limits are forced onto that manifold and may retain lower-dimensional diffusion. That is structurally the same singular-perturbation mechanism seen here.

For P0087 the deterministic vector field is

\[
F(z)=(Q-I)z.
\tag{7.1}
\]

Its fixed manifold inside the cube is exactly

\[
\Gamma=\{\mathbf1 y:0\le y\le1\},
\tag{7.2}
\]

and its deterministic flow is

\[
e^{s(Q-I)}z
=\mathbf1\pi^Tz+e^{-sB}Pz,
\tag{7.3}
\]

so `Gamma` is exponentially attracting in every transverse direction. On the diffusive clock with `V_epsilon -> v>0`, the accumulated interaction clock is

\[
A_\varepsilon(t)
\asymp D_\varepsilon t
\sim \frac{v}{\varepsilon}t\to\infty,
\tag{7.4}
\]

which is exactly the “large drift onto a stable manifold” geometry.

Because `Gamma` is a linear one-dimensional manifold and the Perron projection `z -> 1 pi^Tz` is linear, there is no curvature-induced Itô correction. The source-specific tangent coefficients are obtained explicitly from the discrete Bernoulli network:

\[
\pi^T(Q-I)=0,
\]

and after collapse `QZ approx y1`, conditional independence gives

\[
E[(\pi^T\xi)^2\mid Z]
\longrightarrow
\sum_j\pi_j^2y(1-y)
=\kappa y(1-y).
\tag{7.5}
\]

The projected forcing is `c(bar p-y)`.

**Prior-art conclusion.** The general forced-stable-manifold mechanism must not be advertised as novel; Katzenberger 1991 is clear structural prior art. The P0087 contribution in the cumulative record is the direct discrete triangular-array proof for this exact source model, the arbitrary-clock trichotomy, the explicit Perron projection and coefficient `kappa=sum pi_j^2`, the matched initial layer, and the finite-step/stationary formulas. A line-by-line verification that P0087 satisfies every technical hypothesis of Katzenberger's full 1991 theorem was not available from the bounded accessible text in this run, so direct theorem-level subsumption remains **UNVERIFIED**. None of the proofs above depends on applying Katzenberger.

The bounded 2026-09-18 follow-up search also found the authors' 2026 work on **interacting innovation processes**, but its stated model is an infinite-color innovation system and its abstract does not state the forced two-action critical limit of Open Problem 16. No source-matching later theorem was located; this is negative evidence only, not a novelty or openness certificate.

---

# 8. Two-agent stress test

Take

\[
Q=\begin{pmatrix}1-a&a\\a&1-a\end{pmatrix},
\qquad 0<a<1.
\tag{8.1}
\]

Then `pi=(1/2,1/2)`, `kappa=1/2`, and on the transverse direction `(1,-1)` the matrix `B=I-Q` has eigenvalue `2a`.

For an arbitrary scalar clock `m_epsilon`, the restoring exponent over macroscopic time `t` is

\[
2aD_\varepsilon t=2am_\varepsilon\varepsilon t,
\]

whereas martingale quadratic variation is order

\[
V_\varepsilon t=m_\varepsilon\varepsilon^2t.
\]

Thus:

- finite `D_epsilon` gives deterministic transverse decay `exp(-2ad t)` and zero diffusion;
- `D_epsilon -> infinity`, `V_epsilon ->0` gives instantaneous consensus with frozen average;
- `V_epsilon -> v in (0,infinity)` gives instantaneous consensus and
  \[
  dY_t=cv(\bar p-Y_t)dt+\sqrt{\tfrac v2Y_t(1-Y_t)}dB_t;
  \]
- there is no fourth clock with both a finite nonzero `2aD_epsilon` and nonzero `V_epsilon`, because `V_epsilon/D_epsilon=epsilon` exactly.

This completely resolves the simplest stress test identified in STUCK2.

---

# 9. Scope, status, and what this does not claim

This artifact does **not** relabel P0087 as operationally PROVED. The owner protocol still requires:

1. final source/prior-art reconciliation beyond bounded search;
2. an actual independent P26 full-proof audit;
3. one distinct OTHER-track independent full-proof audit;
4. a self-contained source-scoped paper package.

The mathematical source-facing clock obstruction selected in STUCK2 is, however, resolved here: the possible scalar clocks are explicitly classified through every bounded quadratic-variation scale, the nondegenerate over-accelerated regime is shown not to possess a càdlàg path limit, and the source heuristic is given a precise singular-manifold interpretation.

Because P0087 is HARD and has already consumed the two permitted stuck recoveries, the next owner-protocol action is an immutable handoff preserving these results, followed by shard-0 successor admission work rather than a STUCK3 cycle.
