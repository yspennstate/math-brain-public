Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0429 — exact cubic threshold for every service law with a positive atom

## Cumulative state and methods

Target: Mor Harchol-Balter, *Open problems in queueing theory inspired by datacenter computing* (Queueing Systems 97, 2021), Section 5 limited fork–join asymptotic-independence threshold, with the precise model from Wang–Harchol-Balter–Jiang–Scheller-Wolf–Srikant, *Delay Asymptotics and Bounds for Multi-Task Parallel Jobs*.

Previous R7-01 artifact `2026-09-18T232700Z__P0429_cubic_threshold.md` proved:

1. for every source-admissible service law `G` with finite second moment,
   \[
   k^3/n\to0 \quad\Longrightarrow\quad
   d_{\rm TV}(P_{n,k},\pi_\lambda^{\otimes k})\to0;
   \]
2. deterministic unit service gives the converse, so the frozen universal power exponent is exactly `M_alpha=1/3`.

The frozen metric is therefore already saturated at `1/3`; this run is **NO MOVEMENT** on `M_alpha` even though the obstruction theorem is substantially strengthened.

This run uses three methods different from the preceding B2/B24/B11 triple:

- **B1 — change category:** reinterpret the obstruction as a singular-support statement for the stationary workload law, rather than as a peculiarity of deterministic service.
- **B5 — add a parameter:** expose an arbitrary positive service atom through its location `x>0` and mass `q=G({x})`, and track the obstruction continuously in `q`.
- **B30 — one scale at a time:** isolate the critical window `k^3/n -> tau` and compute the exact first-order rate of tagged multi-hit jobs, giving an explicit nonzero total-variation lower bound.

No finite checker is applicable: the new claims are theorem-sized and the proofs are written below.

---

## Model and notation

There are `n` FCFS unit-speed queues. Parent jobs arrive as a Poisson process of rate

\[
\Lambda_n=\frac{n\lambda}{k}.
\]

Each parent job chooses a uniformly random `k`-subset of the `n` queues and sends one task to every selected queue. Task sizes are iid with law `G`, finite mean `m_1>0`, finite second moment, and

\[
\rho=\lambda m_1<1.
\]

Fix a tagged set `K` of `k` queues. Let `P_{n,k}` be their joint stationary workload law. Let `\pi_\lambda` be the stationary workload law of one M/G/1 queue with task rate `\lambda` and service law `G`.

For a parent job with selected server set `S`, put

\[
N=|S\cap K|.
\]

Then `N` is hypergeometric. Define

\[
p_n=P(N\ge2),\qquad
R_n=\Lambda_n p_n=\frac{n\lambda}{k}p_n.
\]

Thus `R_n` is the Poisson rate of parent jobs that hit at least two tagged queues.

For a fixed tagged queue `i`, conditional on `i\in S`, the other `k-1` destinations form a uniform `(k-1)`-subset of the other `n-1` servers. Hence

\[
a_{n,k}:=
\frac{\binom{n-k}{k-1}}{\binom{n-1}{k-1}}
\]

is the probability that the job hits no other tagged queue, and the singleton-only stream into `i` has rate

\[
\lambda_e=\lambda a_{n,k}.
\]

Poisson marking by the intersection `S\cap K` makes the multi-hit stream and all singleton streams mutually independent.

---

# Theorem 1 — atomic-service exact cubic threshold

Assume the source hypotheses above and, in addition, that the service law has a positive atom: there exist

\[
x>0,\qquad q:=G(\{x\})>0.
\]

Then

\[
\boxed{
 d_{\rm TV}(P_{n,k},\pi_\lambda^{\otimes k})\to0
 \quad\Longleftrightarrow\quad
 k^3/n\to0.
}
\]

This holds for every load `rho<1`; the earlier deterministic-service restriction `lambda<1/2` is unnecessary.

Consequently the source threshold is exactly cubic for every admissible service law having any positive atom, including deterministic service, finite-support service, lattice service, and mixtures with at least one positive point mass.

## Proof: sufficiency

This is exactly the general finite-second-moment theorem proved in the preceding cumulative artifact. With

\[
H_G=\frac{m_1}{1-\rho}
+\frac{\lambda m_2}{2(1-\rho)^2},
\]

that theorem gives

\[
d_{\rm TV}(P_{n,k},\pi_\lambda^{\otimes k})
\le
2\lambda H_G\,k
\left(1-a_{n,k}\right)
\le
2\lambda H_G\frac{k(k-1)^2}{n-1}.
\]

Therefore `k^3/n -> 0` implies total-variation convergence.

The rest of this artifact proves necessity.

---

## Lemma 2 — two tagged queues are simultaneously idle with probability at least `(1-rho)^2`

At a stationary parent-job arrival epoch, let `i,j` be any two distinct tagged queues selected independently of the pre-arrival state. Then

\[
P(W_i(0-)=0,\,W_j(0-)=0)\ge(1-\rho)^2.
\]

### Proof

Wang et al. prove that the steady-state workload vector in the limited fork–join system is **associated**. Thus for coordinatewise nondecreasing `f,g`,

\[
\operatorname{Cov}(f(\mathbf W),g(\mathbf W))\ge0.
\]

The idle indicators

\[
I_i=1_{\{W_i=0\}},\qquad I_j=1_{\{W_j=0\}}
\]

are coordinatewise nonincreasing. Hence `-I_i` and `-I_j` are nondecreasing, and association gives

\[
\operatorname{Cov}(I_i,I_j)
=
\operatorname{Cov}(-I_i,-I_j)
\ge0.
\]

Each marginal queue is exactly an M/G/1 queue with task-arrival rate `lambda`, so its stationary idle probability is `1-rho`. Therefore

\[
P(W_i=0,W_j=0)
=E[I_iI_j]
\ge E[I_i]E[I_j]
=(1-\rho)^2.
\]

The multi-hit parent stream is a state-independent Poisson thinning of the parent Poisson process, and its routing mark is independent of the pre-arrival workload. PASTA therefore gives the same bound immediately before a multi-hit arrival, even after choosing a pair from its hit set by independent auxiliary randomization. ∎

---

## Lemma 3 — one M/G/1 stationary workload has no positive atoms

Under the source assumptions, `pi_lambda` has an atom of mass `1-rho` at zero and has no atom at any `y>0`.

### Proof

The Pollaczek–Khinchine geometric-sum representation writes the stationary workload as

\[
W\overset d=\sum_{r=1}^{J}Y_r,
\]

where `J` is geometric with `P(J=0)=1-rho` and, conditional on `J`, the `Y_r` are iid with the equilibrium service distribution

\[
F_e(t)=\frac1{m_1}\int_0^t \overline G(s)\,ds,
\qquad t\ge0.
\]

The function `F_e` is absolutely continuous with respect to Lebesgue measure, regardless of whether `G` itself has atoms. Hence every convolution of one or more `Y_r` is absolutely continuous. The only atom of the geometric mixture comes from `J=0`, namely the atom at zero. ∎

A direct consequence is that under the product law `pi_lambda^{otimes k}`, for every finite `k`,

\[
P(\exists i<j:\ 0<W_i=W_j)=0.
\]

---

## Lemma 4 — an atomic service law turns one recent common parent into a singular diagonal event

Fix `epsilon` with

\[
0<\epsilon<x.
\]

Define

\[
D_n:=\{\exists i<j:\ 0<W_i(0)=W_j(0)\}.
\]

Then

\[
\boxed{
P_{n,k}(D_n)
\ge
(1-\rho)^2q^2
\frac{R_n}{R_n+2\lambda_e}
\left(1-e^{-(R_n+2\lambda_e)\epsilon}\right).
}
\]

### Proof

If `R_n=0` the inequality is trivial. Assume `R_n>0` and let `U` be the backward age from time zero to the most recent parent job that hit at least two tagged queues. Since these jobs form a Poisson process of rate `R_n`,

\[
P(U\in du)=R_ne^{-R_nu}\,du.
\]

At that parent job, choose uniformly one unordered pair from the tagged queues hit by it, using an auxiliary random variable independent of everything else. Exchangeability of the tagged labels makes the chosen pair a uniform tagged pair; routing and service marks are independent of the pre-arrival workload state.

By Lemma 2, the chosen pair is simultaneously idle immediately before this arrival with probability at least `(1-rho)^2`. The two task sizes sent to this pair are iid `G`, so both are exactly `x` with probability `q^2`.

By definition of `U`, there is no later multi-hit parent job. Every later arrival to either member of the chosen pair must therefore come from that queue's singleton tagged-intersection stream. The two singleton streams are independent Poisson processes of rate `lambda_e`, so conditional on `U=u`, the probability of no later arrival to either chosen queue is

\[
e^{-2\lambda_e u}.
\]

On the intersection of these events, if `u<epsilon<x`, both queues started from zero, both received workload exactly `x`, and neither received another task. Since both servers work at unit speed, their time-zero workloads are both exactly

\[
x-u>0.
\]

Thus `D_n` occurs. Integrating over `0<u<epsilon` gives

\[
\begin{aligned}
P_{n,k}(D_n)
&\ge
(1-\rho)^2q^2
\int_0^\epsilon R_ne^{-(R_n+2\lambda_e)u}\,du\\
&=(1-\rho)^2q^2
\frac{R_n}{R_n+2\lambda_e}
\left(1-e^{-(R_n+2\lambda_e)\epsilon}\right).
\end{aligned}
\]

∎

---

## Corollary 5 — explicit TV obstruction

Lemma 3 gives `pi_lambda^{otimes k}(D_n)=0`, while Lemma 4 gives positive mass under the actual tagged workload law. Therefore

\[
\boxed{
 d_{\rm TV}(P_{n,k},\pi_\lambda^{\otimes k})
\ge
(1-\rho)^2q^2
\frac{R_n}{R_n+2\lambda_e}
\left(1-e^{-(R_n+2\lambda_e)\epsilon}\right)
}
\]

for every `0<epsilon<x`.

If total variation tends to zero, then necessarily

\[
R_n\to0.
\]

Indeed, if `limsup R_n>0`, take a subsequence on which `R_n>=r_0>0`. Since `0<=lambda_e<=lambda`, the displayed lower bound is uniformly bounded below there by a strictly positive constant depending only on `r_0,rho,q,epsilon,lambda`.

---

## Lemma 6 — `R_n -> 0` forces `k^3/n -> 0`

This is the combinatorial part of the preceding deterministic-service obstruction, included here to make the theorem self-contained.

Let

\[
Y=(N)_2=N(N-1).
\]

Hypergeometric factorial moments give

\[
E[(N)_r]=\frac{(k)_r^2}{(n)_r},\qquad r=2,3,4,
\]

and

\[
Y^2=(N)_4+4(N)_3+2(N)_2.
\]

For `n>=6`, putting `a=k^2/n`,

\[
\frac{E(N)_3}{E(N)_2}
=\frac{(k-2)^2}{n-2}\le2a,
\]

and

\[
\frac{E(N)_4}{E(N)_2}
=\frac{[(k-2)(k-3)]^2}{(n-2)(n-3)}\le4a^2.
\]

Hence

\[
EY^2\le8(1+a)^2EY.
\]

For `k>=2`, `(k-1)>=k/2`, so

\[
EY=\frac{[k(k-1)]^2}{n(n-1)}\ge\frac{a^2}{4}.
\]

Since `{Y>0}={N>=2}`, Paley–Zygmund at level zero gives

\[
p_n\ge\frac{(EY)^2}{EY^2}
\ge\frac{a^2}{32(1+a)^2}
\ge\frac1{128}\min(a^2,1).
\]

Therefore

\[
R_n=\frac{n\lambda}{k}p_n
\ge
\frac{\lambda}{128}\frac nk
\min\left(\frac{k^4}{n^2},1\right).
\]

If `k^2/n<=1`, then

\[
R_n\ge\frac{\lambda}{128}\frac{k^3}{n}.
\]

If `k^2/n>=1`, then

\[
R_n\ge\frac{\lambda}{128}\frac nk\ge\frac{\lambda}{128},
\]

because `k<=n`. Hence `R_n->0` is possible only if `k^3/n->0`. Combined with Corollary 5, this proves necessity and completes Theorem 1. ∎

---

# Theorem 7 — critical-window collision asymptotics and explicit separation

Suppose

\[
k\to\infty,\qquad \frac{k^3}{n}\to\tau\in(0,\infty).
\]

Then

\[
\boxed{R_n\to\frac{\lambda\tau}{2}},
\qquad
\boxed{\lambda_e\to\lambda}.
\]

Consequently, for every `0<epsilon<x`,

\[
\boxed{
\liminf_{n\to\infty}
 d_{\rm TV}(P_{n,k},\pi_\lambda^{\otimes k})
\ge
(1-\rho)^2q^2
\frac{\tau}{\tau+4}
\left[1-e^{-\lambda(\tau/2+2)\epsilon}\right]
>0.
}
\]

### Proof

Let

\[
Z=\binom N2.
\]

Then

\[
EZ=\frac{(k)_2^2}{2(n)_2}.
\]

Since `p_n=P(Z>=1)`,

\[
EZ-p_n=E[(Z-1)1_{\{Z\ge1\}}].
\]

For every integer `N>=2`,

\[
\binom N2-1\le2\binom N3.
\]

(The statement is equality for `N=2,3` where applicable at the endpoints, and after clearing denominators reduces for `N>=3` to an elementary nonnegative polynomial.) Hence

\[
0\le EZ-p_n
\le2E\binom N3
=\frac{(k)_3^2}{3(n)_3}.
\]

Dividing by `EZ` gives

\[
0\le1-\frac{p_n}{EZ}
\le
\frac23\frac{(k-2)^2}{n-2}.
\]

The critical assumption `k^3/n -> tau` implies

\[
\frac{k^2}{n}=\frac{k^3/n}{k}\to0.
\]

Therefore

\[
p_n
=
\frac{(k)_2^2}{2(n)_2}(1+o(1))
=
\frac{k^4}{2n^2}(1+o(1)),
\]

and so

\[
R_n
=\frac{n\lambda}{k}p_n
=\frac\lambda2\frac{k^3}{n}(1+o(1))
\to\frac{\lambda\tau}{2}.
\]

Also

\[
1-a_{n,k}
\le\frac{(k-1)^2}{n-1}\to0,
\]

so `lambda_e=lambda a_{n,k}->lambda`.

Insert these limits into Corollary 5. Since

\[
\frac{\lambda\tau/2}{\lambda\tau/2+2\lambda}
=\frac{\tau}{\tau+4},
\]

the stated lower bound follows. ∎

---

## What this changes mathematically

The earlier obstruction used only deterministic unit service and needed `lambda<1/2` because it lower-bounded simultaneous idleness by the crude union bound `1-2lambda`. The present argument replaces that step with the source paper's association theorem and therefore works at **every stable load** `rho<1`.

More importantly, deterministic service is not the real mechanism. The mechanism is a **positive service atom**: a single recent common parent creates a positive-dimensional family of exact diagonal coincidences. The independent product marginal has no positive diagonal atoms because an M/G/1 stationary workload has an absolutely continuous positive part. Thus the common-parent component is singular with respect to the independent product component and cannot be hidden by mixing.

This gives an exact iff theorem on a broad source-valid subclass, not merely a deterministic example.

The fixed source-wide metric does **not** move: it remains

\[
\boxed{M_\alpha=1/3.}
\]

Before this run it was already `1/3`, and after this run it is still `1/3`.

---

## Remaining blocker for full source closure

The unresolved source-valid case is **atomless service**, with exponential service the cleanest test case. There the common-parent event no longer leaves exact positive equalities: two iid continuous task sizes almost surely differ, so the singular-diagonal detector disappears.

This pinpoints the next mathematical obstruction more sharply than “service-law dependence”:

> a common parent still creates a weak pair dependence, but its pair label is hidden among order `k^2` possible pairs and its continuous mark is absolutely continuous under both hypotheses; total variation can therefore be much smaller than the raw multi-hit rate.

The next attack should quantify that smooth common-input perturbation rather than repeat collision counting.

Proposed next nonrepeating Section-B methods:

- **B4:** prove a complete atomless special case, beginning with exponential service, even if it gives only a one-sided threshold;
- **B21:** import sparse-mixture detection / chi-square or Hellinger ideas to quantify one hidden correlated pair among many possible pairs;
- **B28:** replace the worst singular event by a typical-pair statistic and determine whether first- or second-order accumulation governs total variation.

Status: **PARTIAL**. The source-level problem is not declared solved; independent P26 and distinct OTHER-track audits and a self-contained paper package are also absent.
