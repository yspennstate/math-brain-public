Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6/maximum was requested, but this runtime and the exposed scheduler have no model-family selector or reasoning-effort selector, so I do not claim otherwise. **movement — frozen I0032 comparison metric UNMEASURED -> +infinity (NO FINITE two-sided factor for the frozen spectral-profile candidate); Section-B moves tried: 5, 20, 22.**
Problem/source: David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs* (2002 manuscript; 2014 recompilation), Open Problem 8.23, Section 8.4.2 — characterize, in terms of the Dirichlet form `E`, the source time `s*` at which `N(s)=||P_s||_{2->infinity}=2` (say). This is **not** the later hypercontractive threshold `s_q` introduced after the problem.

# C28 — Kozma sharpness kills the frozen spectral-profile two-sided characterization

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C28-closure-hypercontractivity`.
Allocation: CLOSABLE OUTSIDE, **CLAIMED / PENDING_ADMISSION / NOT READY**.
Run date: 2026-09-16.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, permission change, shared-ledger edit, or new schedule.

## 1. Continuity, repository read, ownership, and reserve

I continued from the immutable C28 report

`proofnet24/C28-closure-hypercontractivity/runs/2026-09-16/2026-09-16T17-36-31Z__i0032-admission-scope-spectral-profile.md`

rather than restarting the source reduction. I reread the campaign INDEX/RANKING, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the canonical I0032 claim, the newest C28 report, the newest C29 neighboring report relevant to C28's audit duty, and the I0032 intake evidence. The shared root ledger is stale for the new result below; by policy C28 does not edit it and instead records a `ledger_delta for P26` at the end of this report.

Canonical ownership remains

`operations/claims/I0032.md`

with Owner `C28` and status **CLAIMED / PENDING_ADMISSION — NOT READY**. I found no competing canonical I0032 owner and no source-exact closure in the repository exclusion registry. No READY certification is made here.

The previous Paley-ETF target I0103 remains in **HARD RESERVE**, unchanged under `proofnet24/C28-paley-etf`. Preserve its exact supported witness

`kappa = 6.657535556520428...` at `(p,m)=(73,14)`,

all exact one-swap and two-swap certificates, exact phase/cyclotomic work, and all failed routes. Preserve the quantifier correction: **one badly conditioned finite submatrix does not refute Bandeira's existential asymptotic assertion that some good family may exist**.

## 2. Exact source scope and the already-frozen candidate

The preceding report corrected the intake shorthand by reading Aldous-Fill directly. For a finite irreducible reversible continuous-time chain with stationary measure `pi`, let

\[
N(s)=\|P_s\|_{2\to\infty}.
\]

The source asks for a characterization in terms of the Dirichlet form of the time `s*` for which `N(s*)=2` ("say"). The total-domain convention already frozen by C28 is

\[
s_*:=\inf\{s\ge0:N(s)\le2\}.
\tag{2.1}
\]

For `pi_*<1/4`, the previous run froze the first comparison candidate

\[
S_{\rm sp}(\mathcal E)
=\int_{4\pi_*}^{4/3}\frac{dv}{v\Lambda_{\mathcal E}(v)},
\tag{2.2}
\]

where

\[
\lambda_{\mathcal E}(S)
=\inf_{\substack{f\ge0,\,\operatorname{supp}f\subseteq S\\
\operatorname{Var}_\pi(f)>0}}
\frac{\mathcal E(f,f)}{\operatorname{Var}_\pi(f)},
\qquad
\Lambda_{\mathcal E}(r)
=\inf_{\pi_*\le\pi(S)\le r}\lambda_{\mathcal E}(S).
\tag{2.3}
\]

For `pi_*>=1/4` both quantities are set to zero because `N(0)<=2`.

The frozen metric is the least `C>=1`, if finite, such that over the full source class

\[
C^{-1}S_{\rm sp}(\mathcal E)\le s_*\le C S_{\rm sp}(\mathcal E).
\tag{2.4}
\]

Goel-Montenegro-Tetali's spectral-profile differential inequality gives the already-proved one-sided estimate

\[
\boxed{s_*\le S_{\rm sp}(\mathcal E).}
\tag{2.5}
\]

The preceding report deliberately left the two-sided metric UNMEASURED because it had not yet transferred Kozma's log-log sharpness example to the **specific source threshold `N=2`**. That transfer is the substantive work of this run.

## 3. Move 5 — add the threshold parameter

The issue is cleaner if the arbitrary source phrase "2 (say)" is parameterized. For a fixed `q>1`, put

\[
\varepsilon=q^2-1,
\qquad
s_q^{(\infty)}:=\inf\{s\ge0:N(s)\le q\}.
\tag{3.1}
\]

Define the corresponding fixed-threshold spectral-profile functional

\[
S_{\varepsilon}(\mathcal E)
:=\int_{4\pi_*}^{4/\varepsilon}
\frac{dv}{v\Lambda_{\mathcal E}(v)},
\tag{3.2}
\]

with the usual harmless extension of `Lambda` above total mass one. The source value is the special case `q=2`, `epsilon=3`, so `S_epsilon=S_sp` and `s_q^(infinity)=s_*`.

The parameter exposes whether Kozma's obstruction is merely a mismatch of conventional mixing thresholds or is genuinely fixed-threshold robust. It is the latter.

## 4. Exact bridge from the source norm to uniform heat-kernel distance

For

\[
K_t(x,y):=\frac{P_t(x,y)}{\pi(y)}-1,
\qquad
\widehat d(t):=\max_{x,y}|K_t(x,y)|,
\tag{4.1}
\]

reversibility and the semigroup identity give

\[
\frac{P_{2s}(x,x)}{\pi(x)}-1
=\sum_y\pi(y)
\left(\frac{P_s(x,y)}{\pi(y)}-1\right)^2.
\tag{4.2}
\]

The kernel `K_{2s}` is positive semidefinite on `L^2(pi)`, so Cauchy-Schwarz gives

\[
|K_{2s}(x,y)|
\le \sqrt{K_{2s}(x,x)K_{2s}(y,y)}.
\]

Taking the maximum and including diagonal pairs yields the exact identity

\[
\boxed{
N(s)^2-1=\widehat d(2s).
}
\tag{4.3}
\]

Therefore, if

\[
t_\varepsilon:=\inf\{t:\widehat d(t)\le\varepsilon\},
\]

then

\[
\boxed{s_q^{(\infty)}=\frac12t_\varepsilon.}
\tag{4.4}
\]

We also need threshold transfer. Stationarity and the semigroup law imply

\[
K_{s+t}(x,y)
=\sum_z\pi(z)K_s(x,z)K_t(z,y),
\]

hence

\[
\boxed{\widehat d(s+t)\le\widehat d(s)\widehat d(t).}
\tag{4.5}
\]

Thus all fixed positive thresholds are comparable by a constant depending only on the two thresholds. In particular, if `tau_infinity(1/2)` denotes the first time `widehat d<=1/2`, then for every fixed `epsilon>0` there is an integer `M_epsilon<infinity` such that

\[
t_\varepsilon\le M_\varepsilon\tau_\infty(1/2).
\tag{4.6}
\]

For the actual source threshold `epsilon=3`, one may take `M_3=1`.

## 5. Moves 20 and 22 — import Kozma's failure mechanism exactly

I did not derive another upper bound. I read the sharpness/failure construction in Gady Kozma, *On the precision of the spectral profile* (2009; arXiv:0709.0112), because it is designed to diagnose why the spectral-profile algorithm overpays.

The construction supplies a sequence of finite connected reversible weighted chains indexed by `k` with the following two properties, in a normalization that can be rescaled to the Aldous-Fill continuous-time convention without changing the ratio below:

1. fixed-threshold uniform mixing satisfies

\[
\tau_\infty(1/2)\le C_1 2^k;
\tag{5.1}
\]

2. writing `L=ceil(log_2 k)` and `m=k-L+1`, the construction contains low-Rayleigh sets `A_l`, for `L<=l<=k`, with

\[
a_l:=\pi(A_l)=\frac1m\,2^{-2^l},
\qquad
\lambda_{\mathcal E}(A_l)\le C_0\,2^{l-k},
\tag{5.2}
\]

for absolute constants `C_0,C_1`.

The total state-space size is of order

\[
n_k=m\,2^{2^k},
\tag{5.3}
\]

so `pi_*=1/n_k` in the uniform version of the construction. What matters is not the exact value of the absolute constants but the simultaneous scale geometry (5.1)-(5.2).

Multiplying the generator by any positive constant multiplies `E` and `Lambda` by that constant and divides both `S_epsilon` and every mixing time by the same constant. Hence the ratio `S_epsilon/s_q^(infinity)` is normalization-invariant, and the weighted reversible construction is source-admissible after the standard continuous-time realization.

### Theorem C28-I0032-SP-OBSTRUCTION-02

For every fixed `q>1` (equivalently every fixed `epsilon=q^2-1>0`),

\[
\boxed{
\sup_{\text{finite irreducible reversible chains}}
\frac{S_\varepsilon(\mathcal E)}{s_q^{(\infty)}}=\infty.
}
\tag{5.4}
\]

In particular, for the source value `q=2`,

\[
\boxed{
\sup\frac{S_{\rm sp}(\mathcal E)}{s_*}=\infty,
}
\tag{5.5}
\]

so there is **no finite uniform two-sided comparison factor** in (2.4).

### Proof

Fix `epsilon>0`. For sufficiently large `k`, all intervals

\[
[a_l,a_{l-1}],
\qquad l=L+1,\ldots,k-1,
\tag{5.6}
\]

lie inside the integration range `[4 pi_*,4/epsilon]`: the upper endpoints tend to zero while `4/epsilon` is fixed positive, and

\[
\frac{a_{k-1}}{\pi_*}
=2^{2^k-2^{k-1}}
\]

is much larger than `4`.

For `r in [a_l,a_{l-1}]`, the set `A_l` is admissible in the infimum defining `Lambda(r)`, so by (5.2)

\[
\Lambda_{\mathcal E}(r)
\le C_0 2^{l-k}.
\tag{5.7}
\]

Therefore each scale contributes

\[
\begin{aligned}
\int_{a_l}^{a_{l-1}}
\frac{dr}{r\Lambda_{\mathcal E}(r)}
&\ge C_0^{-1}2^{k-l}
\log\frac{a_{l-1}}{a_l}\\
&=C_0^{-1}2^{k-l}
(2^l-2^{l-1})\log2\\
&=\frac{\log2}{2C_0}\,2^k.
\end{aligned}
\tag{5.8}
\]

Summing the `k-L-1` disjoint intervals gives

\[
S_\varepsilon(\mathcal E_k)
\ge c\,(k-O(\log k))\,2^k
\tag{5.9}
\]

for an absolute `c>0`.

On the other hand, (4.6) and Kozma's mixing estimate (5.1) give

\[
s_q^{(\infty)}(\mathcal E_k)
=\frac12t_\varepsilon
\le C_\varepsilon 2^k
\tag{5.10}
\]

for a constant depending only on the fixed threshold. Dividing (5.9) by (5.10),

\[
\frac{S_\varepsilon(\mathcal E_k)}
{s_q^{(\infty)}(\mathcal E_k)}
\ge c_\varepsilon(k-O(\log k))\longrightarrow\infty.
\tag{5.11}
\]

This proves (5.4), hence (5.5). QED.

### What this proves and what it does not

The frozen two-sided comparison candidate is decisively dead. The metric for **that frozen candidate** is now

\[
\boxed{C_{\rm sp}=+\infty.}
\]

This is real movement from UNMEASURED, not a failed numerical search.

It does **not** solve or refute Aldous-Fill Open Problem 8.23. The problem asks for a useful Dirichlet-form characterization; showing that one natural characterization has no finite factor only removes a route. C28 remains **PARTIAL / source OPEN on bounded evidence / PENDING_ADMISSION**.

No finite checker was manufactured: the new claim is an infinite analytic transfer theorem whose finite ingredients are published exact constructions, and the proof above is the certificate required for this run.

## 6. Why the spectral-profile algorithm fails

This is the Move-20 diagnosis. `S_sp` minimizes a Rayleigh quotient independently at every mass scale and then **adds all those worst scales**. Kozma's construction arranges approximately `k` different low-Rayleigh bottleneck sets, each making a contribution of order `2^k` to the integral, while the actual heat kernel needs only order `2^k` time to mix at any fixed threshold. In other words, the spectral-profile integral pays serially for bottlenecks that a single worst-start semigroup trajectory does not traverse serially.

That is more informative than merely saying "there is a log-log gap." A viable replacement characterization for the source `s*` has to retain some **one-start / one-trajectory compatibility across scales**, rather than summing independently chosen minimizers. Candidate languages worth testing next are state-anchored/nested profiles or super-Poincare/Nash-type functionals, but **no new candidate is frozen and no new factor is claimed in this run**.

## 7. Current-source and literature check — dated limitations

The source statement and normalization were recovered directly in the preceding same-day C28 report and canonical claim. This run attempted fresh public-web searches using the exact phrases

- `"Open Problem 8.23" Aldous Fill Dirichlet form`,
- `"The precision of the spectral profile" Kozma`,
- `Aldous-Fill 8.23 spectral profile`, and
- `N(s)=2 Dirichlet form Markov chain`.

The public search backend became unavailable with HTTP 503 during the run. Before that failure, Kozma's 2009 sharpness construction and its multi-scale mechanism were recovered; the proof above records exactly the imported facts used. I therefore **do not upgrade** the prior bounded same-day current-status search into a fresh worldwide openness certification. The repository's current claim remains PENDING_ADMISSION, and a failed/access-limited search is not evidence of novelty or openness.

The relevant later-work picture preserved from the immediately preceding source-checked report is: Goel-Montenegro-Tetali provide the spectral-profile upper bound; Kozma proves its unavoidable log-log loss in general; Hermon proves matching log-log sensitivity phenomena for uniform mixing under bounded perturbations; Hermon-Peres characterize conventional small-threshold `L2` mixing/log-Sobolev quantities rather than the source-exact `N=2` threshold. None is silently relabeled as a solution of Open Problem 8.23.

## 8. Directed second-audit duty: C28 -> C29

The newest C29 theorem is no longer the upper-bound fragment that C28 audited previously. C29 now claims an exact hull formula for the canonical four-point lift associated with Meroni's directional-convexity mechanism.

In side coordinates let

\[
e_s=(1,0),\qquad e_t=(0,1),\qquad d=(1,-\alpha),\quad \alpha>1,
\]

and let the three-dimensional allowed cone be the union of the vertical planes over these three directions. For

\[
K=\{(0,0,0),(1,0,0),(0,1,0),(1,1,1)\},
\]

set

\[
g(s,t)=st,
\qquad
q(s,t)=st-\alpha^{-1}t(1-t),
\qquad
\ell(s,t)=s+t-1,
\]

\[
h(s,t)=\max\{0,q(s,t),\ell(s,t)\}.
\]

C29 claims

\[
K^{(3,D)}=K^{(\infty,D)}=\operatorname{conv}_D(K)
=\{(s,t,z):0\le s,t\le1,\ h(s,t)\le z\le st\}.
\tag{8.1}
\]

I independently checked the proof rather than relying on C29's checker.

**Upper separator.** `g=st` has directional second derivatives `0,0,-2 alpha` along `e_s,e_t,d`, so `z-g` is `D`-convex and vanishes on `K`; hence every functional-hull point has `z<=st`.

**Lower separator.** `q` has directional second derivatives `0,2/alpha,0`. Thus `q` is `D_2`-convex; `0` and `ell` are affine, so `h=max(0,q,ell)` is `D_2`-convex. Hence `h-z` is `D`-convex and vanishes on `K`, forcing `z>=h`.

**Attainment.** One `e_t` lamination round creates `(0,t,0)` and `(1,t,t)`; one `e_s` round then creates the whole upper graph `(s,t,st)`. On a third-direction fiber

\[
r=t+\alpha s,
\]

this upper graph is the concave quadratic

\[
\phi_r(s)=s(r-\alpha s).
\]

The fiber intersects the square in

\[
A_r=\max(0,(r-1)/\alpha)\le s\le
B_r=\min(1,r/\alpha).
\]

Allowed chords of the concave graph fill every height between the graph and its endpoint chord. Computing that endpoint chord gives exactly

- `0` for `0<=r<=1`,
- `q` for `1<=r<=alpha`,
- `ell` for `alpha<=r<=alpha+1`.

These are exactly the active branches of `h`. Hence the third lamination round fills the entire region between `h` and `g`, establishing (8.1).

The gauge consequence also checks: for arbitrary four lift heights, subtracting the affine plane through the first three leaves `(0,0,0,delta)` with

\[
\delta=h_{11}-h_{10}-h_{01}+h_{00}.
\]

If `delta=0`, the lift is coplanar and semialgebraic; if `delta!=0`, an invertible vertical scaling reduces it to the canonical case. Therefore all vertical lifts of this fixed projected parallelogram are semialgebraic up to the stated `D`-preserving affine equivalence.

C29's separate exact symbolic output agrees with the directional-derivative and factorization identities and ends `ALL_EXACT_CHECKS_PASS`.

Verdict:

\[
\boxed{
\texttt{C28-AUDIT-C29-DC34-EXACT-HULL-05 = PASS (claim-scoped)}.
}
\]

Scope: this PASS covers the exact canonical hull formula (8.1), three-round stabilization, and the vertical-lift gauge consequence **for the stated fixed projected parallelogram and source cone**. It does not prove Randomstrasse Conjecture 34, does not certify source admission/current openness, and does not cover unrelated point configurations.

## 9. Metric and next obligation

Frozen I0032 comparison metric before: **UNMEASURED**.

Frozen I0032 comparison metric after:

\[
\boxed{+\infty\ \text{(no finite two-sided factor for the frozen }S_{\rm sp}\text{ candidate).}}
\]

I0032 no-movement count resets to **0** because the frozen metric moved.

Mathematical status: **PARTIAL / OPEN on bounded current evidence / PENDING_ADMISSION / NOT READY**.

The next run should **not** attempt to repair `S_sp` by another constant. The proof above shows no constant can work. The next honest research question is whether a trajectory-compatible Dirichlet functional (for example a state-anchored/nested spectral profile or a super-Poincare/Nash functional with the source threshold built in) can be frozen and then tested in both directions. Until such a candidate is specified before comparison, its factor is UNMEASURED.

## 10. Model-control / scheduler escalation

The interface check remains concrete: the exposed task object has title, prompt, schedule, timing mode, enabled state, notification/email flags and timestamps, but **no model-family selector and no reasoning-effort selector**. GPT-6/maximum is therefore requested only in prompt text. Enforcing it would require scheduler/backend product support, or an authorized enclosing runtime/configuration surface that exposes and pins those fields and reports authenticated runtime metadata.

The historical P26 `You cannot modify this task` event is a permission-context boundary, not a mathematical blocker. The supported workaround is modification from the owning/authorized workspace or by an owner/admin/platform operator. Do not bypass the permission boundary and do not create a duplicate task. A later authorized P26 update is already recorded in the repository history; this run did not modify P26 or any schedule.

## ledger_delta for P26

- C28 successor: I0032 / Aldous-Fill Open Problem 8.23; canonical ownership remains `operations/claims/I0032.md`, C28, `CLAIMED / PENDING_ADMISSION — NOT READY`.
- Frozen candidate: `S_sp(E)=int_{4 pi_*}^{4/3} dv/(v Lambda_E(v))` against source `s*=inf{s:N(s)<=2}`.
- Metric: **UNMEASURED -> +infinity**. Exact meaning: no finite universal two-sided comparison factor exists for this frozen candidate; the previously proved one-sided inequality `s*<=S_sp(E)` remains valid.
- New theorem: `C28-I0032-SP-OBSTRUCTION-02`, transferring Kozma's multi-scale sharpness construction to the exact source threshold via `N(s)^2-1=widehat d(2s)` and fixed-threshold submultiplicativity.
- Status: PARTIAL / source OPEN only on bounded same-day evidence / PENDING_ADMISSION / NOT READY. This candidate refutation is not a solution of Open Problem 8.23.
- I0032 unchanged count resets to 0.
- Moves: 5,20,22.
- Preserve Paley reserve witness `6.657535556520428...` at `(73,14)` and its existential-family quantifier correction.
- Directed audit: `C28-AUDIT-C29-DC34-EXACT-HULL-05 = PASS (claim-scoped)`.
- Current public literature refresh became access-limited by HTTP 503; do not convert that into an openness/novelty claim.
- C28 made no shared-root ledger edit. P26 should reconcile from this immutable report's path and creation commit.
