Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0429 — a low-dimensional singular service component forces the exact cubic threshold

## 1. Source, cumulative state, and scope

Target: Mor Harchol-Balter, *Open problems in queueing theory inspired by datacenter computing* (Queueing Systems 97, 2021), Section 5 limited fork–join asymptotic-independence threshold, with the precise model from Weina Wang, Mor Harchol-Balter, Haotian Jiang, Alan Scheller-Wolf and R. Srikant, *Delay Asymptotics and Bounds for Multi-Task Parallel Jobs* (2017 preprint / 2019 publication).

Fresh bounded literature check: **2026-09-19**. The source theorem still found in current retrieval is the Wang et al. sufficient regime `k=o(n^(1/4))`; Harchol-Balter's 2021 article explicitly asks how much larger `k` may be while retaining asymptotic independence. Bounded searches for a later exact stationary threshold did not recover a source-matching resolution. This is negative search evidence only, not a novelty certificate.

Cumulative R7-01 results used noncircularly here:

1. for every source-admissible service law `G` with finite second moment,
   \[
   k^3/n\to0
   \quad\Longrightarrow\quad
   d_{\rm TV}(P_{n,k},\pi_\lambda^{\otimes k})\to0;
   \]
2. deterministic service, and then every law with a positive atom, gives the converse, so the frozen full-source exponent is already exactly
   \[
   M_\alpha=1/3;
   \]
3. exponential service has a different, exact square-root threshold
   \[
   d_{\rm TV}(P^W_{n,k},Q^W_k)\to0
   \iff k^2/n\to0.
   \]

The point of this artifact is to determine whether the atomic cubic obstruction disappears merely when the service law becomes atomless. It does **not**.

The new theorem below is source-valid but restricted to a broad singular class. It does not move the frozen universal metric, so the honest source status remains **PARTIAL**.

Methods used in this run:

- **B5 — add a parameter and differentiate/locate the boundary:** parameterize the support geometry by its upper Minkowski dimension `d`; the proof works for `d<1/2` and becomes exactly critical at `d=1/2`.
- **B6 — deform to a point you can solve:** construct atomless Cantor service laws `X=a+epsilon Y_r` converging weakly and in every bounded moment to deterministic service as `epsilon->0`, while the cubic obstruction survives for every `epsilon>0`.
- **B23 — do what the proposer did not expect:** attack the natural heuristic that “atomless service should behave like exponential service.” A singular-continuous atomless law retains the cubic threshold.

No numerical checker is relevant: the claim is theorem-sized and the proof is complete below.

---

## 2. Model and notation

There are `n` FCFS unit-speed queues. Parent jobs arrive according to a Poisson process of rate

\[
\Lambda_n=\frac{n\lambda}{k}.
\]

Each parent independently chooses a uniformly random `k`-subset of the `n` queues and sends one task to every selected queue. Task sizes are iid with law `G`, mean `m_1>0`, finite second moment, and load

\[
\rho=\lambda m_1<1.
\]

Fix a tagged set `K` of exactly `k` queues. Let `P_{n,k}` be the stationary joint workload law of those tagged queues and `\pi_\lambda` the stationary workload law of a single M/G/1 queue with task rate `\lambda` and service law `G`.

For a parent job with selected server set `S`, let

\[
N=|S\cap K|,
\qquad
p_n=P(N\ge2),
\qquad
R_n=\frac{n\lambda}{k}p_n.
\]

Thus `R_n` is the rate of parent jobs hitting at least two tagged queues.

For a fixed tagged queue `i`, conditional on `i\in S`, the other `k-1` destinations are a uniform `(k-1)`-subset of the remaining `n-1` servers. Hence

\[
a_{n,k}=\frac{\binom{n-k}{k-1}}{\binom{n-1}{k-1}},
\qquad
\lambda_e=\lambda a_{n,k}
\]

is the rate of the parent stream whose tagged intersection is exactly `{i}`. Poisson marking by `S\cap K` makes the multi-hit stream and all singleton tagged-intersection streams independent.

---

# Theorem 1 — low-dimensional component exact cubic threshold

Assume the source hypotheses above. Suppose there is a compact set

\[
C\subset(0,\infty)
\]

such that

\[
q:=G(C)>0
\]

and the upper Minkowski dimension of `C` satisfies

\[
\overline{\dim}_{M}(C)<\frac12.
\]

Then

\[
\boxed{
 d_{\rm TV}(P_{n,k},\pi_\lambda^{\otimes k})\to0
 \quad\Longleftrightarrow\quad
 k^3/n\to0.
}
\]

In particular, a positive atom is **not** necessary for the cubic obstruction. There exist bounded, atomless, singular-continuous service laws satisfying the theorem with `q=1`.

## Proof: sufficiency

This is exactly the previously proved full finite-second-moment theorem. With

\[
H_G=\frac{m_1}{1-\rho}
+\frac{\lambda m_2}{2(1-\rho)^2},
\]

R7-01 established

\[
d_{\rm TV}(P_{n,k},\pi_\lambda^{\otimes k})
\le
2\lambda H_G\,k(1-a_{n,k})
\le
2\lambda H_G\frac{k(k-1)^2}{n-1}.
\]

Thus `k^3/n->0` implies TV convergence for every law in the present class. It remains only to prove necessity.

---

## 3. A null singular surface generated by the service support

Set

\[
a:=\min C>0.
\]

Fix once and for all `epsilon` with

\[
0<\epsilon<a.
\]

Define the subset of the positive quadrant

\[
E_{C,\epsilon}
=
\{(x-t,y-t):x,y\in C,\ 0<t<\epsilon\}.
\]

### Lemma 2 — `E_{C,epsilon}` has two-dimensional Lebesgue measure zero

\[
\boxed{\operatorname{Leb}_2(E_{C,\epsilon})=0.}
\]

### Proof

Choose `d` with

\[
\overline{\dim}_{M}(C)<d<\frac12.
\]

By the definition of upper Minkowski dimension, there exist constants `A<infinity` and `delta_0>0` such that for all sufficiently small `0<delta<delta_0`, the set `C` is covered by at most

\[
A\delta^{-d}
\]

intervals of length `delta`.

Cover `(0,epsilon)` by at most `1+epsilon/delta` intervals of length `delta`. Therefore

\[
C\times C\times(0,\epsilon)
\]

is covered by at most

\[
A^2\delta^{-2d}\left(1+\frac{\epsilon}{\delta}\right)
=O(\delta^{-2d-1})
\]

rectangular boxes of side length at most `delta`.

The map

\[
\Phi(x,y,t)=(x-t,y-t)
\]

is Lipschitz. The image of each such three-dimensional box is contained in a two-dimensional square of area at most `C_0\delta^2` for an absolute constant `C_0`. Hence `E_{C,epsilon}` has a two-dimensional cover with total area at most

\[
O(\delta^{-2d-1})\,O(\delta^2)
=O(\delta^{1-2d}).
\]

Because `d<1/2`, this tends to zero as `delta->0`. Therefore `Leb_2(E_{C,epsilon})=0`. ∎

The dimension `1/2` is exactly where this elementary covering mechanism becomes critical: at `d=1/2`, the area estimate no longer decays.

---

## 4. The independent stationary M/G/1 product gives the singular surface zero mass

### Lemma 3 — the positive part of the M/G/1 stationary workload law is absolutely continuous

Under the source assumptions, `pi_lambda` has its usual atom `1-rho` at zero, while its restriction to `(0,infinity)` is absolutely continuous with respect to Lebesgue measure.

### Proof

The Pollaczek–Khinchine geometric-sum representation writes a stationary workload as

\[
W\overset d=\sum_{r=1}^{J}Y_r,
\]

where `P(J=0)=1-rho` and, conditional on `J`, the `Y_r` are iid with the equilibrium service distribution

\[
F_e(t)=\frac1{m_1}\int_0^t\overline G(s)\,ds.
\]

The equilibrium distribution is absolutely continuous, with density `\overline G(t)/m_1`, regardless of whether `G` itself is discrete, singular or absolutely continuous. Every convolution containing at least one `Y_r` is therefore absolutely continuous. Thus the only atom is the mass at zero. ∎

Because `E_{C,epsilon}\subset(0,infinity)^2` and has two-dimensional Lebesgue measure zero, Lemmas 2 and 3 imply that for every fixed pair `i!=j`,

\[
(\pi_\lambda\otimes\pi_\lambda)
\bigl(\{(W_i,W_j)\in E_{C,\epsilon}\}\bigr)=0.
\]

For each finite `k`, define

\[
A_{n,\epsilon}
=
\bigcup_{1\le i<j\le k}
\{(W_i,W_j)\in E_{C,\epsilon}\}.
\]

A finite union of null events is null, so

\[
\boxed{\pi_\lambda^{\otimes k}(A_{n,\epsilon})=0.}
\]

---

## 5. The actual limited fork–join law gives the singular surface positive mass

We use two previously verified structural facts from the same source model:

1. Wang et al. prove that the stationary workload vector is associated.
2. Each marginal queue is exactly an M/G/1 queue with load `rho`, so its stationary idle probability is `1-rho`.

If `I_i=1_{\{W_i=0\}}`, association applied to `-I_i` and `-I_j` gives, for any pair selected independently of the pre-arrival state,

\[
P(W_i=0,W_j=0)\ge(1-\rho)^2.
\]

Now assume `R_n>0` and let `U` be the age, measured backwards from time zero, of the most recent parent job that hit at least two tagged queues. Since the multi-hit jobs form a Poisson process of rate `R_n`,

\[
P(U\in du)=R_ne^{-R_nu}\,du.
\]

At that parent job, choose one unordered pair from its tagged destinations by any auxiliary randomization independent of the pre-arrival state. By exchangeability and PASTA, immediately before that arrival the selected pair is simultaneously idle with probability at least `(1-rho)^2`.

The service requirements delivered to the selected pair are iid `G`. Therefore both lie in `C` with probability `q^2`.

By definition of `U`, there is no later multi-hit parent. Every later arrival to either selected queue must belong to that queue's singleton tagged-intersection stream. Those two singleton streams are independent Poisson processes of rate `lambda_e`. Conditional on `U=u`, the probability of no later task arrival to either selected queue is therefore

\[
e^{-2\lambda_eu}.
\]

On the intersection of these events, if `0<u<epsilon<a`, the chosen queues start from zero, receive task sizes `X_i,X_j in C`, receive no later task, and remain strictly positive at time zero. Their workload pair is exactly

\[
(W_i(0),W_j(0))=(X_i-u,X_j-u)\in E_{C,\epsilon}.
\]

Consequently `A_{n,epsilon}` occurs, and integration over `u` yields

\[
\begin{aligned}
P_{n,k}(A_{n,\epsilon})
&\ge
(1-\rho)^2q^2
\int_0^\epsilon
R_ne^{-(R_n+2\lambda_e)u}\,du\\
&=(1-\rho)^2q^2
\frac{R_n}{R_n+2\lambda_e}
\left(1-e^{-(R_n+2\lambda_e)\epsilon}\right).
\end{aligned}
\]

Because the independent product law gives this event probability zero,

\[
\boxed{
 d_{\rm TV}(P_{n,k},\pi_\lambda^{\otimes k})
\ge
(1-\rho)^2q^2
\frac{R_n}{R_n+2\lambda_e}
\left(1-e^{-(R_n+2\lambda_e)\epsilon}\right).
}
\tag{5.1}
\]

Thus TV convergence forces

\[
R_n\to0.
\]

---

## 6. The multi-hit rate vanishes only on the cubic scale

For completeness, repeat the exact combinatorial implication used in the preceding atomic theorem.

Let

\[
Y=(N)_2=N(N-1).
\]

For the hypergeometric intersection of two `k`-subsets of an `n`-set,

\[
E[(N)_r]=\frac{(k)_r^2}{(n)_r},\qquad r=2,3,4,
\]

and

\[
Y^2=(N)_4+4(N)_3+2(N)_2.
\]

Put `b=k^2/n`. For `n>=6`,

\[
\frac{E(N)_3}{E(N)_2}\le2b,
\qquad
\frac{E(N)_4}{E(N)_2}\le4b^2,
\]

so

\[
EY^2\le8(1+b)^2EY.
\]

Also, for `k>=2`,

\[
EY=\frac{[k(k-1)]^2}{n(n-1)}\ge\frac{b^2}{4}.
\]

Since `{Y>0}={N>=2}`, Paley–Zygmund at level zero gives

\[
p_n=P(N\ge2)
\ge\frac1{128}\min(b^2,1).
\]

Therefore

\[
R_n=\frac{n\lambda}{k}p_n
\ge
\frac{\lambda}{128}\frac nk
\min\left(\frac{k^4}{n^2},1\right).
\]

If `k^2/n<=1`,

\[
R_n\ge\frac{\lambda}{128}\frac{k^3}{n};
\]

if `k^2/n>=1`,

\[
R_n\ge\frac{\lambda}{128}\frac nk\ge\frac{\lambda}{128}.
\]

Hence

\[
R_n\to0
\quad\Longrightarrow\quad
k^3/n\to0.
\]

Combining this with (5.1) proves necessity and therefore Theorem 1. ∎

---

# Corollary 4 — explicit atomless Cantor service laws have the exact cubic threshold

Fix

\[
0<r<\frac14.
\]

Let `C_r subset [0,1]` be the two-branch self-similar Cantor set satisfying

\[
C_r=rC_r\ \cup\ (1-r+rC_r),
\]

and let `nu_r` be its equal-weight Bernoulli self-similar probability measure. Then `nu_r` is atomless and

\[
\dim_M(C_r)=\frac{\log2}{\log(1/r)}<\frac12.
\]

Choose `a>0`, `epsilon_0>0`, let `Y_r~nu_r`, and define

\[
X=a+\epsilon_0Y_r.
\]

Then `X` has a bounded, atomless, singular-continuous service law supported on

\[
C=a+\epsilon_0C_r\subset[a,a+\epsilon_0].
\]

For any task arrival rate `lambda` satisfying `rho=lambda E[X]<1`, Theorem 1 with `q=1` gives

\[
\boxed{
 d_{\rm TV}(P_{n,k},\pi_\lambda^{\otimes k})\to0
 \quad\Longleftrightarrow\quad
 k^3/n\to0.
}
\]

Thus **atomlessness alone does not produce the exponential-service square-root threshold**.

Moreover, with `a` and `r` fixed,

\[
X=a+\epsilon_0Y_r\Longrightarrow a
\qquad\text{as }\epsilon_0\downarrow0
\]

weakly and in every finite moment, yet the exact cubic threshold persists for every `epsilon_0>0`. This gives the B6 deformation from an atomless service law all the way toward the solved deterministic obstruction without losing the asymptotic threshold.

The B5 geometric parameter also exposes a precise boundary of this proof: when `r=1/4`, the Cantor dimension is `1/2` and the elementary covering estimate for `E_{C,epsilon}` becomes scale-neutral rather than decaying. No claim is made here for the critical or higher-dimensional singular support case.

---

## 7. Critical cubic window

The preceding R7-01 factorial-moment calculation also gives, whenever

\[
k\to\infty,
\qquad
\frac{k^3}{n}\to\tau\in(0,\infty),
\]

that

\[
R_n\to\frac{\lambda\tau}{2},
\qquad
\lambda_e\to\lambda.
\]

Therefore (5.1) implies the explicit critical-window separation

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

For the Cantor law above, `q=1`.

---

## 8. Mathematical consequence for the source question

The cumulative picture now contains at least three rigorously different service regimes:

1. **full finite-second-moment class:** universal sufficiency `k=o(n^(1/3))`, and no larger universal power can hold;
2. **positive atoms and, now, positive-mass support components of upper Minkowski dimension `<1/2`:** exact cubic threshold;
3. **exponential service:** exact square-root threshold.

Therefore the service-law dependence is not governed by the binary distinction “atomic versus atomless.” The relevant obstruction is more geometric: sufficiently thin common-parent residual support creates a singular set under the dependent model that is invisible to the independent stationary product.

A genuinely new remaining question is to locate the transition for **smooth non-exponential** service laws, or more generally to identify regularity/nondegeneracy hypotheses under which the cubic singular-support mechanism is impossible and the square-root weak-correlation mechanism controls TV.

That question remains open in this record. Numerics or analogy are not promoted to a theorem.

---

## 9. Frozen metric and lifecycle consequence

The fixed full-source metric is still

\[
\boxed{M_\alpha=1/3.}
\]

Before this run: `1/3`.

After this run: `1/3`.

So this is **NO MOVEMENT** on the frozen metric despite a substantive theorem. The supported ordinary unchanged count therefore advances `5 -> 6`.

Because P0429 is classified **CLOSABLE OUTSIDE**, the owner protocol now requires a six-run immutable handoff/retirement from further R7-01 attacking work. This is an **operational retirement of the R7-01 target after stagnation**, not mathematical source closure: P0429 remains PARTIAL, has not received the required P26 plus distinct OTHER-track source-closure audits, and has no self-contained closure paper package.

No shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md` edit is made by this worker.
