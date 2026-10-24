Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime does not authenticate GPT-6 or a maximum-reasoning selector, so I do not claim that configuration. **NO SOURCE-METRIC MOVEMENT: `beta_fast = 2 -> 2`; D0093 no-movement count `4 -> 5`; methods actually tried: B1 CHANGE THE CATEGORY, B9 RANDOMIZE, B27 SWAP THE QUANTIFIERS. STUCK RECOVERY 1 continues.**

# P13 — D0093 fifth research run: periodic regenerative queue accounting removes the maximum-scale penalty in the abstract trap surrogate

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Own root: `proofnet24/P13-outside-successor`.  
Canonical claim: `operations/claims/D0093.md`.  
Source: Leonardo T. Rolla, *Activated Random Walks on Z^d*, Probability Surveys 17 (2020), arXiv:1906.05037v2, Section 6.2, second Open Problem after Theorem 6.1 / estimate (6.3).  
Status after this run: **OPEN / PARTIAL / STUCK RECOVERY 1**.

## 1. Continuity, ownership, exclusions, and frozen metric

The former P13 I0051 Aldous--Janson clade-covariance target remains RETIRED and was not reopened. P0082 remains handed off after its six-run CLOSABLE rotation and was not reopened. The exclusive current P13 claim remains D0093 under native slot `6aa7b253b37c8191b693d8dc79298d37`.

The controlling predecessor is

`proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T05-02-46Z__d0093-full-replay-clean-flush.md`.

That report proved the two-sided chronological full-replay cleanup: a sacrificed Proposition-6.5-style exploration can consume every revealed instruction, leave its mass only at the source and hit barriers, restore fresh stack tails at a stopping line, and do so in `O(r^3)` work with exponentially high probability. It left one source-native obstruction: **how to glue the resulting random left/right boundary flux without imposing a direction on symmetric random-walk instructions**. It scheduled B1/B9/B27 for this run.

The source-faithful metric remains

\[
\beta_{\rm fast}:=\inf\left\{\beta\ge0:\exists\kappa<\infty,\delta>0,
\ \mathbb P\!\left(T\le \kappa n(\log n)^\beta\right)\ge1-n^{-\delta}
\text{ for all large }n\right\}
\]

under the exact source finite cycle, i.i.d.-Poisson initial law, symmetric nearest-neighbor walks, and the fast-regime parameter domain used for (6.3). The certified source frontier remains `beta_fast=2`; the source asks for the order-`n` estimate. The queue theorems below are **auxiliary reductions**, not source-domain bounds, so

\[
\boxed{\beta_{\rm fast}:2\to2}.
\]

This is the fifth consecutive unchanged D0093 run. Under the owner's CLOSABLE rule, one further unchanged source-metric run requires handoff/rotation rather than a seventh D0093 research run.

## 2. Required repository and source reread

Before new mathematics I reread the owner directive at anchor commit `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md` and `QUEUE.md`, the current D0093 claim, the newest P13 report, D0093 intake/attempt material, and current ownership/audit hits. The root `RESULTS.md` P13 row remains historical relative to the later create-only D0093 claim and immutable D0093 reports; it is not used to reset history. Repository-wide current search still shows D0093 exclusively owned by this P13 slot. No source-level D0093 P26 audit or distinct OTHER-track end-to-end audit was found; that is expected because the source target is not proved.

The original intake row records D0093 as Rolla's second Open Problem after Theorem 6.1 and asks to improve

\[
\mathbb P(T\le \kappa n\log^2n)\ge1-n^{-\delta}
\]

to order `n`. Its old attempt correctly identified odometer tails as a barrier, but its assertion that no useful tail theorem was known is now obsolete because Johnson--Richey (2025) proves stretched-exponential subcritical odometer tails for i.i.d. Bernoulli data on `Z`.

I rechecked Rolla's source. Section 6.2 chooses

\[
p:=\frac{\lambda}{1+\lambda}>\zeta'>\zeta,
\]

takes a deterministic block radius `r=K log n`, routes particles to block sources, and invokes a two-sided trap-confinement estimate whose local failure probability is exponential in `r`. The global `log n` scale is chosen so *every* source block succeeds under a union bound, and the crude diffusive work per particle then produces the second logarithm. Section 4 supplies the other source-native fact needed here: successive one-sided trap spacings are i.i.d. geometric with parameter `p`, and the revealed-but-unused corruption is shielded behind the newest trap.

A fresh bounded literature pass dated 2026-09-18 used variants of

- `Rolla Activated Random Walks on Z^d Section 6.2 log^2 finite cycle Poisson`,
- `activated random walk finite cycle Poisson linear topplings O(n) 2026`,
- `The odometer in subcritical activated random walk Johnson Richey`,
- `activated random walk cycle odometer linear time subcritical 2025 2026`,
- `activated random walk periodic configurations upper bound odometer`.

It recovered Rolla's survey (arXiv:1906.05037v2), Basu--Ganguly--Hoffman--Richey's cycle paper (arXiv:1709.09163), Johnson--Richey (arXiv:2510.05514, 2025), and the later slow-phase ring work. Johnson--Richey prove a stretched-exponential odometer tail for **Bernoulli** initial data on `Z` and explicitly say their upper-bound proof *should* extend nearly verbatim to other light-tailed i.i.d. laws and should work for periodic configurations; those are author remarks, not a proved finite-cycle Poisson theorem. I found no checked primary source stating Rolla's exact finite-cycle Poisson order-`n` bound. This remains **bounded negative evidence only**, not proof of worldwide openness or publication novelty.

The arXiv PDF itself was opened. Required screenshot attempts on the relevant Section 4 and Section 6 pages both failed with a cache-miss error. I therefore record `PDF_VISUAL_ACCESS_FAILURE`; the source text extraction was readable, and no argument below depends on a figure.

P13's secondary directed audit duty remains P14. No new P14 2026-09-18 theorem/report was found that would justify repeating previously completed P13->P14 component audits.

## 3. Idea before code

The fixed-radius proof pays for the **maximum local scale**: choose one `r` so large that no block fails. The previous run showed that a failed local attempt can instead be cleaned exactly, so it is now legitimate to ask whether the system can be organized by **random local regeneration lengths** and pay their aggregate work rather than the square of their maximum.

B1 changes categories: forget ARW for a moment and look at the trap surplus as a periodic reflected random walk / Lindley queue. B9 uses the strict source slack `zeta<p` to thin trap opportunities to an arbitrary service density

\[
\zeta<\theta<p.
\]

B27 then swaps the quantifiers. The source proof says, in effect,

> choose one deterministic radius `r` such that every block is good.

The new surrogate says

> for each realized environment, let the negative-drift queue choose its own regeneration cells, and prove that the **sum** of cubic cell costs is linear.

The key point is that this aggregate statement is true on a finite cycle with polynomially high probability. What remains is no longer a probabilistic accounting problem; it is a source-native **ARW realization** problem.

No checker was written before the idea: the claims this run are analytic and receive full proofs below.

## 4. B1 — change category to a periodic negative-drift queue

Write

\[
p=\frac{\lambda}{1+\lambda}.
\]

Fix any

\[
\zeta<\theta<p.
\]

Consider the following *surrogate* microscopic fields on an `n`-cycle:

\[
A_i\stackrel{\rm iid}{\sim}{\rm Pois}(\zeta),\qquad
Y_i\stackrel{\rm iid}{\sim}{\rm Bernoulli}(\theta),\qquad
X_i=A_i-Y_i,
\]

all independent. Think of `A_i` as arriving particles and `Y_i` as one retained trap opportunity. The word *surrogate* is essential: Section 4 gives geometric trap gaps along its adaptive exploration, but this run does **not** identify the static `Y_i` field with already-valid ARW traps.

The increment has negative drift

\[
\mathbb E X_i=\zeta-\theta<0.
\]

Its exponential moment is

\[
\phi(t):=\mathbb E e^{tX_i}
 =\exp\{\zeta(e^t-1)\}\bigl(1-\theta+\theta e^{-t}\bigr).
\tag{4.1}
\]

Since `phi(0)=1` and `phi'(0)=zeta-theta<0`, there is `t_0>0` such that

\[
\rho:=\phi(t_0)<1.
\tag{4.2}
\]

Consequently, for every interval of `ell` distinct sites,

\[
\mathbb P\left(\sum_{j=1}^{\ell}X_j\ge0\right)
\le \rho^{\ell}.
\tag{4.3}
\]

This is the Cramer inequality that will replace the all-block union bound.

### Lemma P13-D0093-CYCLIC-LINDEY-CUT-09

Let `x_1,...,x_n` be any real numbers with

\[
S:=\sum_{i=1}^n x_i<0.
\]

Then after a cyclic rotation there exists a periodic nonnegative workload satisfying

\[
Q_{i+1}=(Q_i+x_i)_+,
\qquad Q_n=Q_0=0.
\tag{4.4}
\]

In particular, every positive busy component is bracketed by zeros.

#### Proof

Let `s_0=0` and `s_j=x_1+...+x_j`. Choose `m in {0,...,n-1}` minimizing `s_m` over `s_0,...,s_{n-1}` and rotate the increments to

\[
y=(x_{m+1},...,x_n,x_1,...,x_m).
\]

Let `t_k` be its partial sums, with `t_0=0`. For the part before wrapping, every partial sum ending before `x_n` is `s_{m+k}-s_m>=0`; the one ending at `x_n` is `S-s_m>=S` because `s_m<=0`. After wrapping,

\[
t_{n-m+\ell}=S-s_m+s_\ell\ge S
\]

because `s_ell>=s_m`. Finally `t_n=S`. Hence `S` is a minimum of the rotated partial sums and is attained at the final time.

Starting `Q_0=0` and applying the Lindley recursion gives the standard reflection formula

\[
Q_k=t_k-\min_{0\le j\le k}t_j.
\]

At `k=n`, the minimum is `t_n=S`, so `Q_n=0`. Rotating the resulting workload back gives (4.4) on the original cycle. `square`

The lemma is deterministic. In the Poisson/Bernoulli surrogate, (4.3) gives

\[
\mathbb P\left(\sum_{i=1}^nX_i\ge0\right)\le\rho^n,
\tag{4.5}
\]

so the cyclic queue exists with exponentially high probability.

## 5. B9 — randomize by thinning the source's geometric trap opportunities

Rolla's Section 4 states that successive one-sided trap spacings are i.i.d. geometric with parameter `p=lambda/(1+lambda)`. Equivalently at the level of the spacing law, each new lattice site is a Bernoulli-`p` opportunity for the next trap.

Introduce independent auxiliary coins and retain each such opportunity with probability

\[
q=\frac{\theta}{p}\in(0,1).
\]

At the level of this *spacing process*, the retained opportunities are Bernoulli-`theta`, so their gaps are geometric with parameter `theta`. This random thinning buys an arbitrary strict margin

\[
\mathbb E(A_i-Y_i)=\zeta-\theta<0
\]

instead of operating at the edge of the source capacity `p`.

This move succeeds **probabilistically** but not yet **physically**. The Section-4 Bernoulli opportunity is defined through the last/second-last instructions seen by an adaptive explorer. It is not a pre-existing static independent service bit that may simply be revealed everywhere before toppling. Treating `Y_i` as a literal source trap map would silently swap an adaptive source construction for a different model. Thus B9 gives a legal surrogate/coupling target, not an ARW theorem.

That distinction is exactly where the remaining proof obligation lives.

## 6. B27 — swap the fixed-radius quantifier for random regeneration cells

The next theorem shows that if local ARW repair can be made to follow the queue cells, **the aggregate cubic work is already linear with polynomially high probability**. No `max cell length` appears.

### Theorem P13-D0093-PERIODIC-QUEUE-CUBIC-ACCOUNTING-10

Let `X_1,...,X_n` be i.i.d. increments satisfying, for some `t_0>0`,

\[
\rho:=\mathbb E e^{t_0X_1}<1.
\tag{6.1}
\]

On the event `sum_i X_i<0`, construct a periodic Lindley workload by Lemma 09. Let

\[
L_1,...,L_M
\]

be the lengths of its maximal positive busy components. Then for every fixed `delta>0` there are constants `C_delta<infinity` and `n_0` such that for all `n>=n_0`,

\[
\boxed{
\mathbb P\left(
\sum_{j=1}^M L_j^3\le C_\delta n
\right)\ge1-n^{-\delta}.
}
\tag{6.2}
\]

The probability includes the exponentially unlikely event `sum X_i>=0` as failure.

#### Proof

Put

\[
a=-\log\rho>0.
\]

A busy component of length at least `ell` begins at some site where the workload is zero and then stays strictly positive for `ell` consecutive steps. During those steps the reflection is inactive, so the raw increment sum over the first `ell` steps is positive. Therefore, if `N_ell` denotes the number of busy components of length at least `ell` and `M_ell` denotes the number of cyclic starting sites `i` for which

\[
X_i+X_{i+1}+\cdots+X_{i+\ell-1}>0,
\tag{6.3}
\]

then

\[
N_\ell\le M_\ell.
\tag{6.4}
\]

By (6.1) and Markov's inequality, each event (6.3) has probability at most `rho^ell`.

Fix

\[
R=\left\lceil\frac{\delta+6}{a}\log n\right\rceil.
\tag{6.5}
\]

For `n` large, `R<n/2`. First, by a union bound over the `n` cyclic starts,

\[
\mathbb P(\max_jL_j\ge R)
\le n\rho^R
\le n^{-(\delta+5)}.
\tag{6.6}
\]

Now fix `1<=ell<R`. Discard temporarily the at most `ell` starts whose length-`ell` interval wraps around the chosen linear cut. Partition the remaining starts according to their residue modulo `ell`. Within each residue class, the tested intervals are disjoint, so the corresponding indicators are independent. Each class contains at most `n/ell+1` indicators, each with mean at most `rho^ell`.

For a sum `B` of independent Bernoulli variables with mean `mu`, the standard additive Chernoff bound gives, for `s>0`,

\[
\mathbb P(B>2\mu+s)\le e^{-s/3}.
\tag{6.7}
\]

Take

\[
s=6(\delta+8)\log n.
\]

There are at most

\[
\sum_{\ell<R}\ell=O(R^2)=O(\log^2n)
\]

residue classes over all `ell<R`. Hence, outside an event of probability at most `n^{-(delta+4)}` for all large `n`, simultaneously for every `1<=ell<R`,

\[
M_\ell
\le 3n\rho^\ell+C_\delta\ell\log n,
\tag{6.8}
\]

where the last term also absorbs the at most `ell` wrapping starts.

For every positive integer `L`,

\[
L^3
=\sum_{\ell=1}^L\bigl(\ell^3-(\ell-1)^3\bigr)
\le3\sum_{\ell=1}^L\ell^2.
\tag{6.9}
\]

Thus, on the intersection of (6.6)'s complement and the simultaneous event (6.8),

\[
\begin{aligned}
\sum_{j=1}^M L_j^3
&\le 3\sum_{\ell=1}^{R-1}\ell^2N_\ell\\
&\le 9n\sum_{\ell\ge1}\ell^2\rho^\ell
 +C_\delta\log n\sum_{\ell<R}\ell^3\\
&\le C_0 n+C_\delta'\log^5n\\
&\le C_\delta''n
\end{aligned}
\tag{6.10}
\]

for all sufficiently large `n`. Finally,

\[
\mathbb P\left(\sum_iX_i\ge0\right)
\le\rho^n
\]

by the same exponential-moment bound. Adding the three failure probabilities proves (6.2). `square`

### Corollary for the Poisson/thinned-trap surrogate

For

\[
X_i=A_i-Y_i,
\qquad A_i\sim\operatorname{Pois}(\zeta),
\qquad Y_i\sim\operatorname{Bernoulli}(\theta),
\qquad \zeta<\theta,
\]

(4.1)--(4.2) verify the theorem's hypothesis. Therefore the periodic surrogate has, with probability `1-n^{-delta}`, a regenerative busy-cell decomposition whose cubic aggregate length is `O(n)`.

In particular, **if** a source-valid ARW construction can realize each busy cell using at most `C L^3` acceptable/legal topplings, consume or shield every revealed instruction, and concatenate cells without cross-boundary interference, then summing over cells gives

\[
T\le C\sum_jL_j^3=O(n)
\]

with the required polynomially high probability. The accounting part of that implication is now proved; the italicized realization hypothesis is not.

This is the precise sense in which B27 succeeds: the logarithmic maximum-scale penalty is unnecessary in the negative-drift trap surrogate. It does **not** yet move `beta_fast`, because the surrogate has not been identified with the symmetric finite-cycle ARW.

## 7. Why the source embedding still fails

There are two related but distinct physical obstructions.

### 7.1 The service field is adaptive, not static

Section 4's geometric trap spacing is generated by an explorer that reads the next unexplored source instructions. The fact that the next spacing has geometric law `p` does not authorize an omniscient static Bernoulli trap map independent of all future paths. The thinning in B9 is therefore a coupling target, not yet a sitewise ARW construction.

### 7.2 A symmetric explorer cannot be assigned a direction for free

Even if an abstract queue matches an excess particle to a retained service to its left, the source's symmetric walk does not follow a prescribed left path. A one-sided explorer can wander arbitrarily far to the right before hitting a left barrier. In a finite interval, diffusive exit estimates give the natural `O(L^2)` scale, but only when **both** sides are genuine barriers. This is exactly why Proposition 6.5 uses a two-sided barrier/urn construction.

The previous full-replay theorem solved the instruction-freshness problem after a failed two-sided attempt. It did not turn a random left/right barrier hit into chosen clockwise queue service. Hence it would be invalid to paste Theorem 10 directly onto Rolla's stacks.

## 8. Exact remaining lemma: ARW realization of one regenerative busy cell

The cleanest missing statement is now the following source-native interface.

### `REG-CELL` (unproved)

Given a finite interval/cyclic arc `I` of length `L`, fresh symmetric ARW stack tails, and a particle configuration whose corresponding negative-drift surrogate queue starts and ends at workload zero on `I`, construct an **online** two-sided trap procedure such that:

1. every particle in `I` is either trapped inside `I` or exported only through a boundary variable that concatenates with the next queue cell;
2. every selected trap is a genuine source instruction discovered by the online exploration, not a preassigned Bernoulli bit;
3. all revealed-but-unused instructions are either shielded as in Section 4 or consumed by the proved full-replay cleanup;
4. the unused tails at a successful cell boundary form a stopping line and are fresh for the next cell;
5. the total cell work is at most `C L^3` except with probability `e^{-cL}` (or a summably comparable tail).

If `REG-CELL` holds with constants uniform in `L`, Theorem 10 supplies the global `O(n)` work accounting and closes the main logarithmic mechanism. No `K log n` maximum cell is then needed.

The **simplest unproved case** is one busy component with a single unit of queue crossing one internal interface: two neighboring source intervals, one carrying one excess particle after cleanup, with two clean outer barriers and fresh tails. One must let the symmetric particle choose which neighboring barrier it hits, update the service/queue state accordingly, and finish with fresh tails without leaving the union. This is smaller than the previous arbitrary merged-block problem and is the next place to attack.

## 9. Updated STUCK RECOVERY 1 report

The exact source blocker after five unchanged runs is no longer the old `log^2` union bound and no longer corrupted residual stacks. It is

\[
\boxed{
\text{periodic negative-drift service accounting}
\quad\xrightarrow{\text{missing source-native coupling}}\quad
\text{symmetric two-sided ARW trap realization}.
}
\tag{9.1}
\]

Equivalently, Theorem 10 proves that the *amount of capacity and aggregate cubic geometry are sufficient* in the surrogate. What is missing is an online source-stack algorithm making those service events real without selecting jump directions.

### Routes tried in the D0093 sequence and exact failures

1. **B26/B18/B25, run 1:** multiscale failed-block repair. It identified that the published `log^2 n` is a maximum-block penalty and proved aggregate Poisson pile moments are not an obstruction. Failure: merged blocks were history-dependent.
2. **B3/B12/B30, run 2:** scalar capacity queue. It proved negative-drift queue accounting and aggregate capacity surplus. Failure: it treated trap capacity as static after particles crossed a stack.
3. **B11/B19/B20, run 3:** dual/stopping-line analysis. It proved a stopping-line fresh-tail lemma and found the exact one-site `SJJ` counterexample to persistent static capacity. Recovery selected: port Section 4's corruption-shielding technique.
4. **B6/B16/B25, run 4:** two-sided full replay. It proved that a failed trap attempt can consume every peek, restore fresh tails, and leave clean source/barrier flux in `O(r^3)` work with exponential tail. Failure left: random boundary directions do not implement a chosen scalar queue.
5. **B1/B9/B27, this run:** periodic regenerative queue. It proves that, with any strict service slack, the **sum of cubic busy-cell sizes is linear w.h.p. on the cycle**, so no maximum cell scale is needed in the surrogate. Failure left: realize the service process online in symmetric ARW.

### Missing ingredient

A two-sided, stopping-line, boundary-flux trap gadget satisfying `REG-CELL`.

### Simplest case

One unit of overflow across one interface between two adjacent clean constant/variable-scale cells, with two outer barriers and fresh tails.

### Nearest solved analogues

- the directed ARW counting argument, where the particle count is an exact negative-drift Lindley queue;
- Rolla Section 4, where one-sided trap spacings are i.i.d. geometric and corruption is shielded;
- Rolla Proposition 6.5 / Lemma 6.7, where a centered pile is confined by two moving barriers and an urn estimate;
- P13's preceding chronological full-replay theorem, which restores fresh tails after sacrificing such an attempt;
- Johnson--Richey's stable-odometer/boundary-flow construction on `Z` for Bernoulli subcritical data.

The **single selected recovery remains the same recovery chosen at run 3: PORT THE ANALOGOUS TECHNIQUE**. It has now succeeded on freshness and accounting, but not yet on the symmetric flow realization. I do not reset the stuck counter or rename the metric.

## 10. What the three methods actually did

### B1 — CHANGE THE CATEGORY

Attempt: replace blockwise ARW success by a periodic Lindley queue of arrivals minus retained service.

Outcome: **worked as an exact auxiliary reduction.** Lemma 09 gives the deterministic cyclic cut and Theorem 10 gives linear aggregate cubic busy-cell geometry with polynomially high probability.

Why it does not close the source: the queue service bits are not yet genuine online source traps.

### B9 — RANDOMIZE

Attempt: independently thin the source geometric trap opportunities from rate `p` to a chosen `theta` with `zeta<theta<p`, creating explicit negative drift.

Outcome: **worked distributionally, failed as a direct ARW construction.** It supplies arbitrary service slack and the exact mgf (4.1), but a geometric spacing law along an adaptive explorer is not automatically a static global Bernoulli field.

### B27 — SWAP THE QUANTIFIERS

Attempt: replace `there exists one deterministic r such that all blocks succeed` by `for each realized environment, there exists its queue-defined regenerative tiling`, then sum local costs.

Outcome: **worked completely at the accounting level.** Theorem 10 proves the random tiling pays `O(n)` cubic cost w.h.p. Failure is now solely the source-native realization/concatenation of those cells.

## 11. Literature/current-status limitations

The fresh 2026-09-18 search did not locate a primary paper proving the exact finite-cycle i.i.d.-Poisson `O(n)` fast-phase estimate. Basu--Ganguly--Hoffman--Richey state linear time only up to polylogarithmic factors in the low-density regime. Johnson--Richey prove a stronger infinite-line odometer-tail theorem for Bernoulli subcritical data, but their comments about light-tailed distributions and periodic configurations are expressly prospective. The later ring paper addresses the slow/high-density phase. None is treated here as source closure.

This is not a novelty certificate. Citation-graph coverage is bounded, and the queue lemmas themselves are elementary renewal/large-deviation facts; no originality claim is made for those abstract facts. The possible new content, if eventually completed, would be the source-native ARW realization and its use to remove Rolla's logarithmic loss.

## 12. Status, rotation horizon, and next attack

Status: **OPEN / PARTIAL / STUCK RECOVERY 1**.  
Frozen metric: `beta_fast = 2 -> 2`.  
Consecutive unchanged D0093 runs: `4 -> 5`.

There is now exactly one further source-metric attempt available under the six-run CLOSABLE rule. If the next run does not prove a source-domain exponent strictly below 2 or otherwise satisfy a legitimate source-metric movement, P13 must preserve this package, hand D0093 off, and rotate rather than manufacture a seventh unchanged run.

The next nonrepeating method triple is:

- **B4 PROVE SOMETHING WEAKER, COMPLETELY:** solve the one-overflow/two-cell `REG-CELL` case as a full source-stack theorem;
- **B16 COMPUTE EVERY SMALL CASE:** only after the algorithm is specified, exactly enumerate the smallest two-sided stack histories to falsify invalid direction/cleanup rules;
- **B30 ONE SCALE, ONE DIRECTION AT A TIME:** isolate the one-interface transfer kernel before attempting a cyclic concatenation.

A finite checker is warranted next run only if B4 first produces a concrete finite algorithm worth checking.

## 13. Closure and audit status

No closure is claimed. `beta_fast` has not moved. There is no source-matching full proof and therefore no basis to solicit or count a source-level closure audit. The required eventual closure gates remain: exact source argument, prior-art review with limitations, P26 end-to-end audit, and a second distinct OTHER-track end-to-end audit.

No shared root ledger, peer report, historical report, claim file, email/Gmail item, Drive item, public post, workflow, permission, credential, or schedule was modified in this run.

## 14. Structured `ledger_delta` for P26

```json
{
  "track": "P13",
  "native_slot": "6aa7b253b37c8191b693d8dc79298d37",
  "claim": "D0093",
  "category": "CLOSABLE OUTSIDE",
  "source_status": "OPEN",
  "research_status_before": "OPEN / PARTIAL / STUCK RECOVERY 1",
  "research_status_after": "OPEN / PARTIAL / STUCK RECOVERY 1",
  "metric_name": "beta_fast",
  "metric_domain": "Rolla Section 6.2 finite cycle, iid Poisson initial law, symmetric nearest-neighbor ARW, source fast-regime hypotheses",
  "metric_before": "2",
  "metric_after": "2",
  "movement": false,
  "unchanged_count_before": 4,
  "unchanged_count_after": 5,
  "methods": ["B1", "B9", "B27"],
  "recovery_episode": 1,
  "recovery_choice": "port the analogous technique",
  "new_auxiliary_results": [
    "P13-D0093-CYCLIC-LINDEY-CUT-09",
    "P13-D0093-PERIODIC-QUEUE-CUBIC-ACCOUNTING-10"
  ],
  "source_metric_credit_for_auxiliary_results": 0,
  "exact_blocker": "realize the negative-drift service/regeneration process by an online symmetric two-sided ARW trap gadget with stopping-line fresh tails and controlled boundary flux",
  "simplest_unproved_case": "one unit of overflow across one interface between two adjacent clean cells with two outer barriers and fresh tails",
  "next_methods": ["B4", "B16", "B30"],
  "rotation_rule": "if the next D0093 run is also source-metric unchanged, hand off and rotate at six unchanged runs",
  "closure_authorized": false,
  "p26_source_audit": "missing / not yet appropriate",
  "distinct_other_source_audit": "missing / not yet appropriate",
  "prior_art_status": "bounded negative search only; novelty UNVERIFIED"
}
```
