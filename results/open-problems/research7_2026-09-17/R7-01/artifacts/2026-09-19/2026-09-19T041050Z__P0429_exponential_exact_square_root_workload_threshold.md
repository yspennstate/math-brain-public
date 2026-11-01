Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0429 — exponential service: exact square-root threshold for the full stationary workload law

Slot: `R7-01`  
Native ID: `6aabe777361481919c9e614646464772`  
Canonical target: `P0429`  
Source: Mor Harchol-Balter, *Open problems in queueing theory inspired by datacenter computing*, Queueing Systems 97 (2021), Section 5, with the limited fork–join model of Wang–Harchol-Balter–Jiang–Scheller-Wolf–Srikant, *Delay Asymptotics and Bounds for Multi-Task Parallel Jobs*, Queueing Systems 91 (2019), arXiv:1710.00296.  
Fresh pre-artifact master: `abdc16b93f53772f30b62737732e46dc0dc35d93`.  
Status: **PARTIAL relative to the full finite-second-moment source problem.**

## 1. Theorem proved in this artifact

Let the parent job size be `K=K_n`. There are `n` FCFS unit-speed servers. Parent jobs arrive at rate

\[
\Lambda_n=\frac{n\lambda}{K},
\]

and each parent chooses a uniform `K`-subset of the servers and sends one iid task to each chosen server. In this artifact task sizes are iid exponential with rate `\mu`, and

\[
\rho:=\lambda/\mu\in(0,1).
\]

Let `P^W_{n,K}` be the stationary joint workload law of any `K` tagged servers and let `Q^W_K` be the `K`-fold product of the one-server stationary M/M/1 workload law.

The result is

\[
\boxed{
 d_{\rm TV}(P^W_{n,K},Q^W_K)\longrightarrow0
 \quad\Longleftrightarrow\quad
 \frac{K^2}{n}\longrightarrow0.
}
\tag{1.1}
\]

The sufficient direction is the dimension-uniform `L^2`/Dirichlet-form theorem proved in the immediately preceding R7-01 artifact: for exponential service,

\[
d_{\rm TV}(P^W_{n,K},Q^W_K)=O_\rho(K^2/n)
\quad\text{when }K^2/n\to0.
\tag{1.2}
\]

The new work here proves the converse. It deliberately avoids the invalid growing-dimensional perturbation step withdrawn in the earlier busy-projection erratum. The proof below uses perturbation estimates only for **fixed 3- and 4-coordinate marginals**, with constants never allowed to depend on a growing selected dimension.

This theorem does **not** close the original source problem, whose service law is only assumed to have finite second moment. The source-wide frozen metric therefore remains `M_alpha=1/3` because the already proved atomic-service obstruction forces the cubic scale in the universal class.

---

## 2. B25 — exact workload/busy covariance by counting the same stationary drift twice

Write `W_i` for the stationary workload at server `i` and

\[
B_i:=\mathbf 1_{\{W_i>0\}},\qquad
S:=\sum_{i=1}^n W_i,\qquad
B:=\sum_{i=1}^n B_i.
\]

Each marginal queue is exactly M/M/1 with arrival rate `\lambda` and service rate `\mu`. Hence

\[
E B_i=\rho,
\qquad
\bar w:=E W_i=\frac{\rho}{\mu(1-\rho)}.
\tag{2.1}
\]

Between parent arrivals total workload decreases at rate `B`. At a parent arrival, total workload jumps by

\[
Y=X_1+\cdots+X_K,
\qquad X_a\stackrel{iid}{\sim}{\rm Exp}(\mu),
\]

so

\[
E Y=\frac K\mu,
\qquad
E Y^2=\frac{K(K+1)}{\mu^2}.
\tag{2.2}
\]

Stationarity of `S` gives

\[
0=-E B+\Lambda_n E Y,
\]

and therefore

\[
E B=n\rho.
\tag{2.3}
\]

Apply the stationary generator to `S^2`. The deterministic service drift contributes `-2SB`; a parent arrival contributes `2SY+Y^2`. Since the new service marks are independent of the pre-arrival state,

\[
0=-2E[SB]+\Lambda_n\bigl(2E[S]E[Y]+E[Y^2]\bigr).
\]

Using (2.2) and `\Lambda_n=n\lambda/K`,

\[
E[SB]
=n\rho E[S]+\frac{n\rho(K+1)}{2\mu}.
\]

Together with (2.3), this yields the exact finite-`n` identity

\[
\boxed{
\operatorname{Cov}(S,B)=\frac{n\rho(K+1)}{2\mu}.
}
\tag{2.4}
\]

The use of the unbounded test `S^2` is justified by truncation: for fixed `n`, every workload marginal has all moments under exponential service, and `S^2\le n\sum_i W_i^2` is integrable.

Now

\[
W_iB_i=W_i,
\]

so by (2.1)

\[
\operatorname{Cov}(W_i,B_i)
=E W_i(1-\rho)
=\frac\rho\mu.
\tag{2.5}
\]

Exchangeability gives one common off-diagonal covariance `c_{WB}`. Expanding (2.4),

\[
\frac{n\rho(K+1)}{2\mu}
=n\frac\rho\mu+n(n-1)c_{WB}.
\]

Therefore, for every `i\ne j`, exactly

\[
\boxed{
\operatorname{Cov}(W_i,B_j)
=\frac{\rho(K-1)}{2\mu(n-1)}.
}
\tag{2.6}
\]

Set

\[
\eta_n:=\frac{K-1}{n-1}.
\tag{2.7}
\]

Then the source-observable cross covariance is simply `\rho\eta_n/(2\mu)`. This is the linear signal that will be aggregated at the square-root window.

---

## 3. B14 — fixed-coordinate symmetry/cluster lemma, with no growing-dimensional constants

The earlier withdrawn converse attempted a Neumann expansion on a selected block whose dimension itself diverged. That was invalid because the constants had not been proved uniform in that dimension. The repair is to use the perturbation theory only on at most four coordinates.

### Lemma 3.1 (fixed `r` density control)

Fix `r\le4`. Let `N_1,\ldots,N_r` be any `r` tagged stationary queue lengths and let

\[
q_r=\pi^{\otimes r},
\qquad
\pi(m)=(1-\rho)\rho^m,
\]

be the independent M/M/1 product law. As `\eta_n\to0`, the true `r`-coordinate stationary queue-length law has density `1+h_r` with respect to `q_r` satisfying

\[
\|h_r\|_{L^2(q_r)}=O_{r,\rho,\mu}(\eta_n).
\tag{3.1}
\]

For `r=4`, if `\Pi_4` denotes projection onto the pure four-coordinate ANOVA sector, then in fact

\[
\boxed{
\|\Pi_4 h_4\|_{L^2(q_4)}
=O_{\rho,\mu}(\eta_n^2).
}
\tag{3.2}
\]

#### Proof

Let `U_i=S_i-I`, where `S_i` increments queue `i`. The projected `r`-queue process is autonomous because arrivals and exponential departures of tagged queues do not depend on outside queue lengths. Its generator is exactly

\[
L^{(r)}=L_0^{(r)}+W_r,
\]

where `L_0^{(r)}` is the generator of `r` independent M/M/1 queues and

\[
W_r
=
\sum_{b=2}^r\gamma_b
\sum_{\substack{A\subseteq[r]\\|A|=b}}
\prod_{i\in A}U_i,
\tag{3.3}
\]

with

\[
\boxed{
\gamma_b
=\lambda\frac{(K-1)_{b-1}}{(n-1)_{b-1}}.
}
\tag{3.4}
\]

Indeed, the coefficient of a prescribed `b`-fold increment equals the parent rate times the probability that the prescribed `b` tagged servers all belong to the parent's `K`-subset:

\[
\frac{n\lambda}{K}\frac{(K)_b}{(n)_b}
=\lambda\frac{(K-1)_{b-1}}{(n-1)_{b-1}}.
\]

For fixed `b`, (3.4) gives

\[
\gamma_2=\lambda\eta_n,
\qquad
\gamma_b=O_b(\eta_n^{b-1}),\quad b\ge3.
\tag{3.5}
\]

The base product chain is reversible. Put

\[
H_r:=-L_0^{(r)},\qquad K_r:=W_r^* \text{ in }L^2(q_r),\qquad D_r:=K_r1.
\]

The one-coordinate shifts have bounded adjoints on `L^2(\pi)`, while `H_r^{-1}` is bounded on the centered subspace by the M/M/1 spectral gap

\[
g_\rho=(\sqrt\mu-\sqrt\lambda)^2>0.
\]

Because `r\le4` is fixed, (3.3)-(3.5) imply

\[
\|H_r^{-1}K_r\|_{2\to2}=O_{r,\rho,\mu}(\eta_n).
\tag{3.6}
\]

For sufficiently small `\eta_n` this norm is below `1/2`. The stationary adjoint equation for a density `1+h_r` is

\[
(H_r-K_r)h_r=D_r,
\]

hence on the centered subspace

\[
h_r=(I-H_r^{-1}K_r)^{-1}H_r^{-1}D_r.
\tag{3.7}
\]

Since `\|D_r\|_2=O(\eta_n)`, (3.1) follows from the convergent Neumann series. As in the preceding R7-01 full-workload artifact, the `L^2` solution defines a finite signed invariant measure of mass one; irreducibility and positive recurrence identify it with the unique stationary probability, so (3.7) is the actual stationary density.

For (3.2), use the product ANOVA decomposition. `H_4^{-1}` preserves coordinate support. Also `D_4=K_41` decomposes into pure support levels `b=2,3,4`, with norms respectively

\[
O(\eta_n),\qquad O(\eta_n^2),\qquad O(\eta_n^3),
\]

because `U_i^*1` is centered and (3.5) holds. Let

\[
u:=H_4^{-1}D_4,\qquad A:=H_4^{-1}K_4.
\]

Then `\|u\|_2=O(\eta_n)`, `\|A\|=O(\eta_n)`, and the pure level-four part of `u` is `O(\eta_n^3)`. From

\[
h_4=u+Au+A^2u+\cdots
\]

we obtain

\[
\|\Pi_4h_4\|_2
\le O(\eta_n^3)+O(\eta_n^2)+O(\eta_n^3)
=O(\eta_n^2).
\]

This proves the lemma. `\square`

### Workload transfer

Under exponential service, conditional on the queue-length vector, every unfinished task has an exponential residual/service requirement by memorylessness, and the service marks of distinct tasks are independent. Thus both the true system and the independent M/M/1 product system map queue lengths to workloads through the same coordinatewise kernel: given `N_i=m`, the workload is `Gamma(m,\mu)` (with `Gamma(0,\mu)=0`).

Consequently, if a workload observable involving at most four coordinates is square-integrable under the product law, its conditional expectation given the queue lengths is an `L^2(q_r)` function. Lemma 3.1 therefore controls its expectation under the true stationary workload marginal.

Two consequences used below are:

1. any fixed three-coordinate product whose expectation is zero under the workload product law differs from zero by `O(\eta_n)`;
2. any fixed four-coordinate observable that is a product of four one-coordinate **centered** functions differs from zero by `O(\eta_n^2)`, because its conditional expectation is pure ANOVA level four and pairs only with `\Pi_4h_4`.

All constants here depend only on `\rho,\mu` and the fixed observable pattern, never on the growing block size introduced next.

---

## 4. B17 — replace a critical-window CLT by a bounded-second-moment separating statistic

A beta-binomial/Curie-Weiss style critical-window CLT would be one way to convert weak pair dependence into total-variation separation, but it is much more than is needed. A general moment inequality suffices.

For probability laws `P,Q` and a measurable `F` with finite second moments,

\[
\boxed{
|E_PF-E_QF|^2
\le
2d_{\rm TV}(P,Q)\bigl(E_PF^2+E_QF^2\bigr).
}
\tag{4.1}
\]

To see this, dominate both laws by `\nu`, with densities `p,q`. Then Cauchy-Schwarz gives

\[
\left|\int F(p-q)d\nu\right|^2
\le
\left(\int F^2(p+q)d\nu\right)
\left(\int\frac{(p-q)^2}{p+q}d\nu\right),
\]

and

\[
\frac{(p-q)^2}{p+q}\le|p-q|,
\qquad
\int|p-q|d\nu=2d_{\rm TV}(P,Q).
\]

Thus a statistic with a nonzero mean shift and uniformly bounded second moments already forces positive TV distance. No CLT and no growing-dimensional resolvent bound is required.

---

## 5. The aggregate cross statistic

Define centered workload and busy variables

\[
A_i:=W_i-\bar w,
\qquad
C_i:=B_i-\rho.
\tag{5.1}
\]

For a block of `m` servers, set

\[
\boxed{
T_m:=\frac1m\sum_{\substack{1\le i,j\le m\\i\ne j}}A_iC_j.
}
\tag{5.2}
\]

Let `P_m` be the true stationary workload marginal on these `m` servers and `Q_m` the product M/M/1 workload law.

Under `Q_m`, independence and centering give

\[
E_{Q_m}T_m=0.
\tag{5.3}
\]

Under `P_m`, (2.6) gives the **exact** mean

\[
\boxed{
E_{P_m}T_m
=(m-1)\frac{\rho\eta_n}{2\mu}.
}
\tag{5.4}
\]

### Lemma 5.1 (uniform second moments in the critical block)

For every fixed `c_0<\infty`, there is `C=C(\rho,\mu,c_0)<\infty` such that whenever `\eta_n` is sufficiently small and

\[
m\eta_n\le c_0,
\tag{5.5}
\]

we have

\[
\boxed{
E_{P_m}T_m^2+E_{Q_m}T_m^2\le C.
}
\tag{5.6}
\]

#### Proof

Expand `T_m^2`. Each summand is indexed by two ordered pairs `(i,j)` and `(p,q)`, with `i\ne j`, `p\ne q`. Classify the term by the cardinality of the union

\[
|\{i,j,p,q\}|\in\{2,3,4\}.
\]

**Two distinct coordinates.** There are `O(m^2)` such terms. Since `|C_i|\le1` and every one-server M/M/1 workload moment is finite, Cauchy-Schwarz using the fixed one-coordinate marginals bounds the absolute expectation of each term by a constant depending only on `\rho,\mu`. After the factor `m^{-2}`, their total contribution is `O(1)`.

**Three distinct coordinates.** There are `O(m^3)` such terms. Under the product law every such term has expectation zero: at least one of the two singleton-coordinate factors is centered (indeed the patterns contain two singleton coordinates). The corresponding fixed three-coordinate observable is in `L^2` because the M/M/1 workload has finite fourth moment. By Lemma 3.1 and the workload transfer, each true expectation is `O(\eta_n)`. After division by `m^2`, the total is

\[
O(m\eta_n).
\]

**Four distinct coordinates.** There are `O(m^4)` terms. Each term is a product of four one-coordinate centered functions, one on each distinct coordinate, hence is pure level four under the product law. By (3.2) and the workload transfer, each true expectation is `O(\eta_n^2)`. After division by `m^2`, the total is

\[
O(m^2\eta_n^2)=O((m\eta_n)^2).
\]

Under `Q_m`, all three- and four-coordinate contributions vanish exactly and the two-coordinate contribution is `O(1)`. Combining the three classes and using (5.5) proves (5.6). `\square`

The decisive point is that Lemma 5.1 uses only local `r=3,4` perturbation constants. It does **not** substitute a growing `m` into a fixed-dimensional error term. This is precisely the gap identified by the earlier immutable erratum, now repaired by a different proof architecture.

---

## 6. Necessity of the square-root condition

Assume, toward the contrapositive, that

\[
K^2/n\not\longrightarrow0.
\]

Then along a subsequence there is `\varepsilon>0` such that

\[
K^2/n\ge\varepsilon.
\tag{6.1}
\]

We show that along a further subsequence the full `K`-workload TV distance stays bounded away from zero.

### Case 1: `\eta_n` does not tend to zero

Pass to a further subsequence with `\eta_n\ge\eta_0>0`. Consider the two-coordinate workload statistic

\[
F=(W_1-\bar w)(B_2-\rho).
\]

Under the product law its mean is zero. Under the true law, (2.6) gives

\[
E F=\frac{\rho\eta_n}{2\mu}\ge\frac{\rho\eta_0}{2\mu}>0.
\]

Its second moments under both laws are uniformly bounded because `|B_2-\rho|\le1` and the one-server workload second moment is fixed. Applying (4.1) gives a positive lower bound on the two-coordinate TV distance, hence also on the full `K`-coordinate TV distance by data processing.

### Case 2: `\eta_n\to0`

Keep (6.1). Choose a fixed constant

\[
0<c<\varepsilon/2
\]

and set

\[
m_n:=\left\lfloor\frac c{\eta_n}\right\rfloor.
\tag{6.2}
\]

Then `m_n\eta_n\to c`. Moreover,

\[
\frac{m_n}{K}
\sim
\frac{c}{K\eta_n}
=
\frac{c(n-1)}{K(K-1)}
\le \frac c\varepsilon+o(1)<1,
\]

so `m_n\le K` for all sufficiently large `n` on the subsequence.

By (5.4),

\[
E_{P_{m_n}}T_{m_n}
\longrightarrow
\frac{\rho c}{2\mu}>0,
\qquad
E_{Q_{m_n}}T_{m_n}=0.
\tag{6.3}
\]

Lemma 5.1 gives a uniform bound on the sum of the two second moments. Hence (4.1) implies

\[
\liminf_{n\to\infty}
 d_{\rm TV}(P_{m_n},Q_{m_n})>0.
\tag{6.4}
\]

Since `m_n\le K`, marginalization can only decrease TV, so

\[
 d_{\rm TV}(P^W_{n,K},Q^W_K)
\ge d_{\rm TV}(P_{m_n},Q_{m_n}).
\]

Thus the full `K`-coordinate TV distance cannot tend to zero.

The two cases exhaust every subsequence satisfying (6.1). Therefore

\[
\boxed{
 d_{\rm TV}(P^W_{n,K},Q^W_K)\to0
 \Longrightarrow
 K^2/n\to0.
}
\tag{6.5}
\]

Combining (6.5) with the preceding R7-01 sufficiency theorem (1.2) proves (1.1). `\square`

---

## 7. What this resolves, and what it does not

The exponential-service subproblem now has an exact answer:

\[
\boxed{
K=o(\sqrt n)
\quad\text{is necessary and sufficient for full stationary workload TV independence.}
}
\]

This is stronger than the earlier busy-projection result and directly concerns the source workload law. It also strictly strengthens the original `o(n^{1/4})` published sufficient regime in this service class.

The complete source still permits every iid service distribution with finite second moment. R7-01 previously proved

\[
K^3/n\to0
\Longrightarrow
\text{full stationary workload TV independence}
\]

for that entire class, while any service law with a positive atom has the exact cubic threshold. Hence service regularity genuinely changes the scale: atomic laws exhibit `n^{1/3}`, while exponential service exhibits `n^{1/2}`.

What remains open in this record is the classification of **atomless non-exponential finite-second-moment laws**, including whether a continuous-law regularity parameter determines an interpolation between the cubic and square-root mechanisms or whether a broader dichotomy holds.

The source-wide frozen quantity remains

\[
\boxed{M_\alpha=1/3.}
\]

No source-level closure, independent audit, or novelty certification is claimed.

---

## 8. Section-B method outcomes

**B14 — FIND THE GROUP ACTING: SUCCESS.** Exchangeability lets the full `K`-coordinate question be tested on a deliberately chosen subblock `m\le K`, while exact fixed-coordinate projected generators provide local estimates whose constants do not grow with `m`.

**B17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: SUCCESSFUL REFRAMING.** Instead of proving a beta-binomial/Curie-Weiss-style critical-window CLT, use the generic two-law moment inequality (4.1). This turns a bounded-second-moment cross statistic into a TV separator and avoids unnecessary limit-distribution machinery.

**B25 — COUNT THE SAME THING TWICE: SUCCESS.** Stationarity of total workload `S` and `S^2` gives the exact workload/busy cross covariance (2.6); counting the square of the aggregate statistic by 2-, 3-, and 4-coordinate overlap patterns then gives the uniform moment bound.

No numerical checker is relevant: every new claim here is theorem-sized and proved on the page.

---

## 9. Dated source / literature check — 2026-09-19

A fresh bounded web search on 2026-09-19 used the exact titles and combinations of `limited fork-join`, `asymptotic independence`, `growing k`, `stationary`, `exponential service`, and `sqrt n`. It recovered:

- Weina Wang, Mor Harchol-Balter, Haotian Jiang, Alan Scheller-Wolf, R. Srikant, *Delay Asymptotics and Bounds for Multi-Task Parallel Jobs*, arXiv:1710.00296 / Queueing Systems 91 (2019), whose abstract states the `k=o(n^{1/4})` asymptotic-independence theorem;
- Mor Harchol-Balter, *Open problems in queueing theory inspired by datacenter computing*, Queueing Systems 97 (2021), Section 5, which explicitly asks how much larger `k` can be while preserving asymptotic independence;
- the authors' conference/full versions stating that `k=Theta(n)` is non-independent and that the intermediate regime remained open there.

The bounded search did not surface a later theorem giving the exact exponential stationary `sqrt(n)` threshold proved above. That is **negative evidence only** and is not a claim of worldwide novelty or priority.

Primary URLs checked:

- `https://arxiv.org/abs/1710.00296`
- `https://www.pdl.cmu.edu/PDL-FTP/CloudComputing/QUESTA21.pdf`

---

## 10. Next mathematical target

Do not re-prove the exponential threshold. The remaining source-level work is continuous non-exponential service.

A useful next split is to test whether the atomic obstruction survives for a **singular continuous** or smooth density through near-diagonal events, versus whether the exponential square-root mechanism extends to all sufficiently regular service densities. The next run should choose three nonrepeating Section-B methods after re-reading this artifact and the current master; no method triple is charged here beyond B14/B17/B25.