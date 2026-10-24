Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0429 — exponential-service stationarity defect, pair linear response, and the n^(1/2) fluctuation scale

## Scope and cumulative context

Target: `P0429`, Mor Harchol-Balter, *Open problems in queueing theory inspired by datacenter computing* (Queueing Systems 97, 2021), Section 5 limited fork-join threshold, with the exact model from Wang–Harchol-Balter–Jiang–Scheller-Wolf–Srikant, *Delay Asymptotics and Bounds for Multi-Task Parallel Jobs* (Queueing Systems 91, 2019).

The preceding R7-01 work already proved under the full source class (iid service law with finite second moment, marginal load `rho<1`) that

\[
k^3/n\to0
\quad\Longrightarrow\quad
 d_{TV}(P_{n,k},\pi_\lambda^{\otimes k})\to0,
\]

and showed that the universal power exponent `1/3` cannot be improved because any positive service-time atom gives an exact cubic obstruction. Thus the frozen source-wide metric remains

`M_alpha = 1/3`.

This artifact does **not** redefine that metric. It attacks the remaining atomless special case requested by the previous report, beginning with exponential service.

For exponential service with rate `mu`, write

\[
\rho=\lambda/\mu\in(0,1).
\]

The source paper itself singles out this regime. Its Section 5.5 says the displayed `o(n^(1/4))` theorem can be improved, with more delicate estimates, to

\[
k=o\!\left(\frac{n^{1/3}}{\log^m n}\right)
\]

for some `m`, and then asks whether there is a critical growth scale for `k`. Its simulations report very accurate independence at `k=n^(1/3)`, an apparently diminishing job-delay gap at `k=n^(1/2)`, an unclear picture at `k=n^(2/3)`, and clear divergence at `k=n^(9/10)`. Those simulation statements concern job delay, not total-variation convergence of the entire `k`-workload vector.

The new calculations below isolate a rigorous smooth-dependence scale at `k^2/n`, without claiming that this alone proves the full TV threshold.

---

## B4 — prove a complete atomless special-case statement: exact stationary product defect for M/M/1 queue lengths

### 1. The tagged queue-length process is autonomous

Under exponential service the queue-length vector of the `k` tagged queues is itself a continuous-time Markov chain on `Z_+^k`.

A parent job arrives at rate

\[
\Lambda_n=\frac{n\lambda}{k}.
\]

If its chosen `k`-subset of servers intersects the tagged set `K` in the exact nonempty subset `A`, then every coordinate in `A` receives one customer. For a fixed `A` of size `a`, the event rate is

\[
r_A
=\Lambda_n
\frac{\binom{n-k}{k-a}}{\binom nk}.
\]

Each nonempty queue has departures at rate `mu`. The one-coordinate marginal arrival rate is exactly `lambda`, so every marginal stationary queue-length law is geometric:

\[
\pi(m)=(1-\rho)\rho^m,
\qquad m\ge0.
\]

Let

\[
q=\pi^{\otimes k}
\]

be the independent product candidate.

### 2. Compare the true arrival generator with the independent generator

Let `L` be the true tagged generator and `L_0` the generator of `k` independent M/M/1 queues, each with arrival rate `lambda` and departure rate `mu`.

The departure parts agree exactly. Only the arrivals differ.

For a state `x=(x_1,...,x_k)`, define

\[
B_i(x)=1_{\{x_i>0\}},
\qquad
Z_i(x)=\frac{B_i(x)}{\rho}-1.
\]

Under `q`, the variables `Z_i` are independent, centered, and

\[
E_q Z_i^2
=v:=\frac{1-\rho}{\rho}.
\]

For an arrival hitting `A`, the adjoint of the jump operator applied to the constant density `1` contributes

\[
\rho^{-|A|}\prod_{i\in A}B_i-1
=
\prod_{i\in A}(1+Z_i)-1.
\]

Subtracting the independent singleton-arrival contribution gives the exact stationarity residual

\[
g_{n,k}:=\frac{L^*q}{q}
=
\sum_{A\ne\varnothing}r_A
\left(\prod_{i\in A}(1+Z_i)-1\right)
-
\lambda\sum_{i=1}^k Z_i.
\]

Expand the products. For every nonempty `B subseteq K`, the coefficient of `prod_{i in B} Z_i` is the total parent-job rate of jobs that hit every queue in `B`, regardless of what happens to the other tagged queues. If `|B|=b`, that rate is

\[
\gamma_b
=
\Lambda_n\frac{(k)_b}{(n)_b}
=
\lambda\frac{(k-1)_{b-1}}{(n-1)_{b-1}}.
\]

For `b=1`, `gamma_1=lambda`, so the entire first-order term cancels **exactly**. Therefore

\[
\boxed{
 g_{n,k}
 =
 \sum_{b=2}^k
 \gamma_b
 \sum_{\substack{B\subseteq K\\|B|=b}}
 \prod_{i\in B}Z_i.
}
\]

This cancellation is the main structural difference between smooth exponential service and the previous singular-support atomic obstruction: the product law is not wrong at first order in any one-coordinate marginal. The defect begins at genuine interactions.

### 3. Exact orthogonal norm of the defect

If `B != C`, then the monomials `Z_B=prod_{i in B} Z_i` and `Z_C` are orthogonal under `q`: a coordinate in the symmetric difference appears to the first power and has mean zero. Hence

\[
\boxed{
 \|g_{n,k}\|_{L^2(q)}^2
 =
 \sum_{b=2}^k
 \binom{k}{b}\gamma_b^2 v^b.
}
\]

In particular, the pair term is

\[
T_2
=
\binom{k}{2}
\lambda^2\left(\frac{k-1}{n-1}\right)^2
v^2.
\]

For fixed `rho` and any regime `k=o(n^(2/3))`, the higher-order terms are negligible compared with `T_2`. Indeed, for `b>=2`,

\[
\frac{T_{b+1}}{T_b}
=
\frac{k-b}{b+1}
\left(\frac{k-b}{n-b}\right)^2 v,
\]

so uniformly over the range contributing non-negligibly this ratio is `O(k^3/n^2)=o(1)`; summing the tail gives `sum_{b>=3}T_b=o(T_2)`.

Therefore

\[
\boxed{
 \|g_{n,k}\|_{L^2(q)}^2
 =
 \frac{\lambda^2}{2}
 \left(\frac{1-\rho}{\rho}\right)^2
 \frac{k^4}{n^2}
 (1+o(1))
}
\]

whenever `k=o(n^(2/3))`, and hence

\[
\boxed{
 \|g_{n,k}\|_{L^2(q)}
 =
 \frac{\lambda}{\sqrt2}
 \frac{1-\rho}{\rho}
 \frac{k^2}{n}
 (1+o(1)).
}
\]

So the exact product **stationarity defect** first becomes order one at the square-root scale `k asy sqrt(n)`, not at the cubic collision-count scale `k asy n^(1/3)`.

This is a complete identity about the M/M/1 queue-length chain. It is **not yet** a theorem that workload TV convergence fails at `sqrt(n)`: converting a generator residual into a static TV lower bound requires a stability/inverse-generator argument that stays uniform when the total interaction-event rate is large.

---

## B21 — import the sparse-mixture / orthogonal-score viewpoint: exact two-queue linear response

The preceding defect decomposition says that pair interactions are the first nonzero orthogonal score. The two-coordinate marginal can be solved to first order rigorously.

### 4. Exact two-queue generator

Fix two tagged queues. A parent job hits both at rate

\[
\gamma
=\gamma_2
=\lambda\frac{k-1}{n-1}.
\]

Each coordinate has total arrival rate `lambda`, so arrivals hitting only the first queue occur at rate `lambda-gamma`, and likewise for the second queue. The pair queue-length generator is therefore

\[
L_\gamma=L_0+\gamma W,
\]

where `L_0` is the product M/M/1 generator and

\[
(Wf)(x,y)
=f(x+1,y+1)-f(x+1,y)-f(x,y+1)+f(x,y).
\]

Let `q_2=pi otimes pi`. Because `L_0` is reversible in `L^2(q_2)`, its restriction to mean-zero functions has a bounded inverse `(-L_0)^(-1)`. The perturbation `W` is bounded on `L^2(q_2)`: each forward shift has norm at most `rho^(-1/2)` per shifted coordinate. Thus, for sufficiently small `gamma`, the normalized stationary density `h_gamma=dp_gamma/dq_2` has an ordinary convergent perturbation expansion in `L^2(q_2)`.

The adjoint score is

\[
W^*1
=
\rho^{-2}B_1B_2-ho^{-1}B_1-ho^{-1}B_2+1
=Z_1Z_2.
\]

Writing `h_gamma=1+gamma u+O(gamma^2)` in `L^2(q_2)` and using stationarity,

\[
0=(L_0+\gamma W)^*h_\gamma,
\]

gives

\[
(-L_0)u=Z_1Z_2,
\qquad
u:=u=(-L_0)^{-1}(Z_1Z_2).
\]

Therefore

\[
\boxed{
E_{p_\gamma}[Z_1Z_2]
=
\gamma C_{\rho,\mu}+O(\gamma^2)
}
\]

with the strictly positive constant

\[
\boxed{
C_{\rho,\mu}
:=
\langle Z_1Z_2,(-L_0)^{-1}Z_1Z_2\rangle_{q_2}.
}
\]

### 5. Semigroup representation and explicit positive bounds

Let `P_t` be the one-dimensional M/M/1 semigroup and write

\[
c(t)=\langle Z,P_tZ\rangle_\pi.
\]

Because the product semigroup factorizes,

\[
\boxed{
C_{\rho,\mu}
=
\int_0^\infty c(t)^2\,dt.
}
\]

This immediately proves positivity.

There are also explicit two-sided bounds. First,

\[
c(0)=v=\frac{1-\rho}{\rho}.
\]

The Dirichlet form of `Z` has only the edge `0<->1` contributing, and

\[
\langle Z,-L_1Z\rangle_\pi
=(1-\rho)\lambda\left(\frac1\rho\right)^2
=\mu v.
\]

By the spectral theorem, `c(t)/v` is the Laplace transform of a probability measure on the nonnegative spectrum whose mean is `mu`. Since `theta -> exp(-theta t)` is convex,

\[
c(t)\ge v e^{-\mu t}.
\]

The exact M/M/1 `L^2` spectral gap is

\[
\operatorname{gap}=(\sqrt\mu-\sqrt\lambda)^2,
\]

so also

\[
c(t)\le v e^{-\operatorname{gap}t}.
\]

Consequently

\[
\boxed{
\frac{v^2}{2\mu}
\le
C_{\rho,\mu}
\le
\frac{v^2}{2(\sqrt\mu-\sqrt\lambda)^2}.
}
\]

### 6. Observable consequence for workloads: busy-indicator covariance

The busy indicator is the same whether one observes queue length or workload:

\[
B_i=1_{\{N_i>0\}}=1_{\{W_i>0\}}.
\]

Every marginal remains M/M/1 with `P(B_i=1)=rho`, hence

\[
E[Z_1Z_2]=\frac{\operatorname{Cov}(B_1,B_2)}{\rho^2}.
\]

Thus

\[
\boxed{
\operatorname{Cov}(B_1,B_2)
=
\rho^2 C_{\rho,\mu}\,\gamma
+O(\gamma^2)
}
\]

as `gamma downarrow 0`. Since `gamma=lambda(k-1)/(n-1)`, any regime `k=o(n)` gives

\[
\boxed{
\operatorname{Cov}(B_1,B_2)
=
\rho^2 C_{\rho,\mu}\lambda\frac{k}{n}
(1+o(1)).
}
\]

In particular, using the lower bound for `C_{rho,mu}`, for all sufficiently small `gamma`,

\[
\operatorname{Cov}(B_1,B_2)
\ge
\frac{(1-\rho)^2}{4\mu}\,\gamma.
\]

This proves that continuous exponential service does **not** eliminate the dependence created by common parent arrivals. It changes its nature: the dependence is smooth and of first order in the specific-pair common-arrival rate `gamma ~ k/n`, rather than a singular positive-diagonal mass visible from the total multi-hit rate.

---

## B28 — replace “all collisions” by a typical-pair/global-fluctuation statistic

### 7. Busy-count variance

Let

\[
S_k=\sum_{i=1}^k B_i
\]

be the number of busy queues among the tagged `k` queues. Exchangeability gives the exact identity

\[
\operatorname{Var}(S_k)
=
k\rho(1-\rho)
+k(k-1)\operatorname{Cov}(B_1,B_2).
\]

Using the pair linear-response theorem and `gamma=lambda(k-1)/(n-1)`, uniformly along any sequence `k=o(n)`,

\[
\boxed{
\operatorname{Var}(S_k)
=
k\rho(1-\rho)
+
\rho^2 C_{\rho,\mu}\lambda
\frac{k(k-1)^2}{n-1}
+O\!\left(\frac{k^4}{n^2}\right).
}
\]

Hence, when `k->infinity` and `k=o(n)`,

\[
\boxed{
\operatorname{Var}(S_k)
=
k\rho(1-\rho)
+
\rho^2 C_{\rho,\mu}\lambda
\frac{k^3}{n}(1+o(1)).
}
\]

Dividing by the independent-product variance gives

\[
\boxed{
\frac{\operatorname{Var}(S_k)}{k\rho(1-\rho)}
=
1+
A_\rho\frac{k^2}{n}
+o\!\left(\frac{k^2}{n}\right),
\qquad
A_\rho:=\frac{\rho\lambda C_{\rho,\mu}}{1-\rho}>0.
}
\]

The preceding bounds on `C` give

\[
\boxed{
\frac{1-\rho}{2}
\le
A_\rho
\le
\frac{1+\sqrt\rho}{2(1-\sqrt\rho)}.
}
\]

Therefore:

- if `k^2/n -> 0`, the busy-count variance has the same first-order size as under independence;
- if `k^2/n -> tau in (0,infinity)`, the variance is inflated by the nonzero factor `1+A_rho tau+o(1)`;
- if `k^2/n -> infinity` while `k=o(n)`, the covariance contribution dominates the independent variance.

This makes `k^2/n` a rigorous **smooth-dependence fluctuation parameter** for exponential service.

### 8. Why this still does not close the TV threshold

A second-moment discrepancy alone is not a TV lower bound at the square-root scale because `S_k^2` is unbounded with `k`. The trivial bounded-support conversion only gives

\[
d_{TV}(P_{n,k},\pi^{\otimes k})
\gtrsim
\frac{|\operatorname{Var}_{P}S_k-\operatorname{Var}_{q}S_k|}{k^2}
\asymp \frac{k}{n},
\]

which vanishes at `k asy sqrt(n)`.

To turn the variance inflation into a sharp TV obstruction one needs one additional ingredient, for example:

1. a uniform fourth-moment / uniform-integrability estimate plus a CLT for `S_k` in the critical `k^2/n=Theta(1)` window;
2. a bounded degenerate U-statistic whose true law has controlled variance and whose mean shift is order one after normalization; or
3. a static likelihood-ratio / chi-square expansion that remains stable even though the **total** number of common-parent events may diverge.

The exact orthogonal defect formula above suggests the third route: its leading `L^2(q)` size is order `k^2/n`, exactly the square-root parameter. But the old Neumann-series perturbation around the full `k`-dimensional product generator is only automatically uniform when the total interaction operator norm is small, essentially the already-known cubic regime. Removing that mismatch is the next mathematical obstacle.

---

## What moved mathematically, and what did not

Frozen source metric:

\[
M_\alpha: \frac13\to\frac13.
\]

**NO MOVEMENT** because the universal exponent was already saturated by the atomic-service obstruction.

Substantive new results:

1. exact product-stationarity residual for the full tagged M/M/1 queue-length chain;
2. exact orthogonal norm identity
   \[
   \|g_{n,k}\|_2^2=\sum_{b\ge2}\binom kb\gamma_b^2v^b;
   \]
3. pair-dominance asymptotic `||g||_2 ~ const * k^2/n` for `k=o(n^(2/3))`;
4. rigorous two-queue stationary linear response with positive coefficient `C_{rho,mu}` and explicit two-sided bounds;
5. rigorous busy-indicator covariance asymptotic of order `k/n`;
6. rigorous tagged busy-count variance inflation controlled by `k^2/n`.

These results identify the square-root scale as the first natural smooth-dependence scale for exponential service, but **do not yet prove** that `sqrt(n)` is the TV threshold.

---

## Dated literature/source check — 2026-09-19

Fresh bounded searches used the exact titles and combinations of `limited fork-join`, `asymptotic independence`, `growing batch size`, `n^(1/2)`, and the Wang/Harchol-Balter author set. They recovered the 2019 source paper, the 2021 open-problems article, and later work on adjacent parallel-job scheduling, but no later primary theorem resolving the exact stationary-independence critical scale surfaced. This is negative evidence only, not a novelty certificate.

Primary sources rechecked:

- Wang, Harchol-Balter, Jiang, Scheller-Wolf, Srikant, *Delay Asymptotics and Bounds for Multi-Task Parallel Jobs*, Queueing Systems 91 (2019), arXiv:1710.00296 / CMU PDF.
- Harchol-Balter, *Open problems in queueing theory inspired by datacenter computing*, Queueing Systems 97 (2021), Section 5.

The 2019 paper explicitly records the stronger unpublished-in-detail sufficient regime `o(n^(1/3)/log^m n)` and leaves a critical-scale question open; this artifact therefore does not misstate the displayed `1/4` theorem as the strongest observation already made by the proposers.

---

## Next attack

Do not repeat B4/B21/B28 on the next ordinary research run.

The most useful next triple is:

- **B12 (find what is conserved):** exploit exchangeability of the full `n`-server busy vector and condition on the total number of busy servers; the tagged busy pattern is then exactly hypergeometric, which may convert the problem to the fluctuation law of the global busy fraction.
- **B7 (take the limit):** prove a CLT, or at minimum a fourth-moment bound, for the global/tagged busy count in the critical `k^2/n=Theta(1)` window.
- **B18 (say it in another language):** rewrite the stationary M/M/1 interaction as a high-temperature complete-graph perturbation and seek a cluster/cumulant expansion whose connected `r`-point term is `O((k/n)^(r-1))`.

The nearest concrete theorem target is: establish enough uniform integrability/CLT control for `S_k` to convert the explicit variance inflation above into a bounded-test TV lower bound when `k^2/n -> tau>0`, or else produce a counterexample showing that the variance signal can be hidden in vanishing TV mass.