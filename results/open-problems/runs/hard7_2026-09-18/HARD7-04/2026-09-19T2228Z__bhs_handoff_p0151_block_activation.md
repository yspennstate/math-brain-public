Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement: predecessor `BHS-MST-CM-UNIV` handed off after its second Section-I recovery; successor `P0151` admitted; frozen successor metric `gamma_E >= b0 -> gamma_E >= b1` with **strict movement** `b1>b0`; methods **B2 / B7 / B19**.

# HARD7-04 bounded research iteration — rotate to fixed-outdegree PA criticality and exploit block activation

Status: **PARTIAL / SOURCE OPEN**. No closure claim. No simulation is used as proof. No finite checker was manufactured because the new claim is analytic and the argument is written in full below.

## 1. Mandatory continuation / Section-I rotation

The newest HARD7-04 checkpoint was the second permitted stuck recovery on `BHS-MST-CM-UNIV`. Its frozen metric stayed

`beta_MST^- >= eta -> beta_MST^- >= eta`,

so CONTROL.md requires rotation rather than another lemma on that route. I therefore released that claim in `operations/claims/BHS-MST-CM-UNIV.md` and preserved its strongest handoff state there. I did **not** perform a third recovery.

Before selecting a successor I reread the controlling files, campaign `INDEX.md` / `RANKING.md`, root `POSTED.md` / `RESULTS.md`, `QUEUE.md`, the current HARD7-04 claim/report state, the relevant neighboring preferential-attachment / random-graph reports, and the intake catalog containing `P0151`. `I0049` is not eligible: repository screening records it as known/resolved in the queued uniformly-grown scope. `I0048` has already had threshold-level work and is not the fixed-outdegree critical-window question used here.

## 2. Successor admission: P0151

Canonical target: **critical window and critical component sizes for fixed-outdegree affine preferential attachment**.

Historical source alias in the repository intake: Remco van der Hofstad, *Stochastic Processes on Random Graphs*, old Saint-Flour Open Problem 4.4. A current primary-source formulation appears in Rounak Ray's 2024 TU/e thesis, Discussion / Percolation direction, printed p. 194, which says exactly:

> “It would be interesting to study the critical regime of preferential attachment models”

and then points to possible new phenomena in the critical window.

The frozen model is Ray's sequential model `PA_n^(m,delta)(d)` with fixed integer `m>=2`, fixed `delta>0`, exactly `m` out-edges per arriving vertex, sequential degree updates, no self-loops, and independent bond retention `pi` after construction. Hazra--van der Hofstad--Ray (EJP 31, 2026; arXiv:2312.14085) prove the threshold

`pi_c = delta / ( 2*( m*(m+delta) + sqrt(m*(m-1)*(m+delta)*(m+1+delta)) ) )`,

but not a fixed-outdegree critical-window scaling theorem.

Current-status separation checked this run:

- Jorritsma--Maillard--Mörters, arXiv:2512.18937 (2025), prove a `(log n)^(-2)` window and `sqrt(n)/log n` largest-component scale for sparse growing graphs in which the new vertex connects **independently** to earlier vertices. That theorem does not automatically cover the exact fixed-`m` sequential model here.
- Mörters--Schätze (2026) concern an inhomogeneous random graph with a preferential-attachment kernel in the infinite-variance regime, again a different ensemble.
- Ray's thesis explicitly leaves the critical regime for preferential attachment as future work, and the TU/e/Network Center project page asks whether the critical window can be described.

Immediately before reservation, direct fetch of `operations/claims/P0151.md` returned 404 and alias searches found no canonical owner. The create-only reservation is commit `4fc629db40b4e8eed212eddb458527797854113b`.

## 3. Frozen metric and verified baseline

Let `C_max(n,pi_c)` be the largest component of the bond-percolated graph at the now-known threshold and define

`gamma_E := liminf_{n->infinity} log E[ |C_max(n,pi_c)| ] / log n`.

Set

`chi := (m+delta)/(2m+delta)`.

Ray's Theorem 7.2.1 gives a lower scale through the component containing an initial vertex. Thus the admission baseline is

`gamma_E >= b0 := 1-chi + pi_c*chi`

or equivalently

`b0 = (m + (m+delta)*pi_c)/(2m+delta)`.

This is the **before** value. The result proved below moves it strictly.

---

# 4. B2 — attack the negation: fixed-outdegree sibling bundling is not a one-edge perturbation

The first attempted negation was the tempting transfer principle “the fixed-outdegree graph should have the same first lower growth exponent as the one-edge tree embedding, because collapsing only changes constants.” That principle is false already at the one-step activation level.

Suppose a new vertex has `m` out-edges and, at the current state, each edge has conditional chance at least `x` to hit a tracked old connected set. Each edge is retained independently with probability `pi`. The probability that **at least one** of the `m` edges is both retained and lands in the tracked set is bounded below by

`1-(1-pi*x)^m`.

For `x in [0,1]`, concavity gives the global chord bound

`1-(1-pi*x)^m >= q_m(pi)*x`,

where

`q_m(pi) := 1-(1-pi)^m`.

For `m>=2` and `0<pi<1`,

`q_m(pi)-pi = (1-pi)*(1-(1-pi)^(m-1)) > 0`.

So a collapsed fixed-outdegree birth block has a strictly larger first-order activation coefficient than the single-edge coefficient `pi` used by the tree lower embedding. This is a structural effect of the exact source model, not a numerical observation.

Outcome of B2: **the negation survives as a genuine obstruction to a naive tree-transfer argument and supplies a strictly stronger coefficient `q_m(pi)`**.

---

# 5. B19 — make the exploration an algorithm: the shadow connected set

The useful construction is deliberately smaller than the true percolation component, so every inequality goes in the safe direction.

Let `Q_t` be a subset of the percolation component of vertex `1` after the first `t` graph vertices have arrived. Start from `Q_2={1}`. When vertex `v=t+1` arrives, freeze the old set `Q_t` during its `m` attachment trials and add `v` to `Q_{t+1}` **iff** at least one of its `m` out-edges is retained and has target in `Q_t`. Do not add any old outside vertex that happens to become connected through another retained edge. Hence, inductively,

`Q_t subseteq C_t(1)`

for every `t`.

Define the underlying-graph attractiveness of this shadow set by

`W_t := sum_{u in Q_t} ( d_u(t)+delta )`,

and let `N_t:=|Q_t|`.

For the sequential source model, if `H_t` is the number of the `m` new attachment edges whose target lies in the frozen old set `Q_t`, and `I_t` is the indicator that the new vertex is activated into `Q`, then at the end of the birth step there is the exact identity

`W_{t+1} = W_t + H_t + (m+delta)*I_t`.      (5.1)

Reason: every hit on an old tracked vertex increases its underlying degree by one; if the new vertex is activated, its final degree is exactly `m` and it contributes `m+delta`; all mergers to outside old components are deliberately ignored.

This identity is the central new route. It keeps the fixed-outdegree dependence instead of replacing the source graph by an independent-edge kernel.

---

# 6. Full proof of the new expected-size lower exponent

## Proposition (block-activation lower bound)

Fix `m>=2`, `delta>0` and `pi in (0,1)`. For the sequential fixed-outdegree affine preferential-attachment model `(d)` followed by independent bond percolation with retention `pi`, put

`q := 1-(1-pi)^m`

and

`b(pi) := [m + (m+delta) q] / (2m+delta)`.

Then there is a constant `c=c(m,delta,pi,G_0)>0` such that for all sufficiently large `n`,

`E |C_max(n,pi)| >= E |C_n(1;pi)| >= E N_n >= c n^(b(pi))`.       (6.1)

Consequently, at `pi=pi_c`,

`gamma_E >= b1 := [m + (m+delta)*(1-(1-pi_c)^m)]/(2m+delta)`.       (6.2)

Moreover `b1>b0`.

## Proof

Write `A:=2m+delta`. In model `(d)`, the denominator for the `j`th edge of vertex `v=t+1` is, from the source definition,

`c_{v,j}=a_[2]+2(m_[t]-2)+(j-1)+t*delta`,

and with fixed outdegree `m`, `m_[t]=2+m(t-2)`. Therefore, for a fixed constant `K` depending only on the initial graph and `m`,

`c_{v,j} <= A t + K`                                                (6.3)

for every `j=1,...,m` and all sufficiently large `t`. Increase `K` if necessary so the right-hand side is positive for every step considered.

Condition on the entire graph/percolation history through time `t`. Before the new birth, the numerator of the attachment probability to `Q_t` is exactly `W_t`. During the `m` sequential trials it can only increase when a trial hits `Q_t`. Hence for every trial, conditional on any preceding outcomes,

`P(edge j targets Q_t | current birth history) >= W_t/(A t+K)`.     (6.4)

Summing (6.4) over the `m` trials gives

`E[H_t | F_t] >= m W_t/(A t+K)`.                                   (6.5)

Now reveal the independent retention mark of each new edge together with its target. Conditional on the event that no earlier edge in the same birth was a retained hit on `Q_t`, the numerator in (6.4) is still at least `W_t`. Hence

`P(I_t=0 | F_t) <= (1-pi W_t/(A t+K))^m`.

Set `x=W_t/(A t+K)`. Since `0<=x<=1` and `f(x)=1-(1-pi x)^m` is concave with `f(0)=0`,

`1-(1-pi x)^m >= x[1-(1-pi)^m]=q x`.

Thus

`E[I_t | F_t] >= q W_t/(A t+K)`.                                   (6.6)

Insert (6.5) and (6.6) into the exact identity (5.1):

`E[W_{t+1}|F_t] >= W_t * [1 + r/(A t+K)]`,                         (6.7)

where

`r:=m+(m+delta)q`.

Taking expectations and iterating,

`E W_n >= E W_t0 * product_{t=t0}^{n-1} [1+r/(A t+K)]`.             (6.8)

The logarithm of the product is

`sum_t [r/(A t+K)+O(t^-2)] = (r/A) log n + O(1)`,

so for some `c_1>0`,

`E W_n >= c_1 n^(r/A)=c_1 n^(b(pi))`.                              (6.9)

Finally, `N_{t+1}-N_t=I_t`. Taking expectations in (6.6) and using (6.9),

`E N_{t+1}-E N_t >= q E W_t/(A t+K) >= c_2 t^(b(pi)-1)`             (6.10)

for all large `t`. Since `b(pi)>0`, summing (6.10) gives

`E N_n >= c_3 n^(b(pi))`.                                          (6.11)

By construction `Q_n` is a subset of the true percolation component of vertex `1`, which is itself no larger than the largest component. This proves (6.1) and (6.2).

For strict improvement over the verified source baseline, use

`q-pi = (1-pi)*(1-(1-pi)^(m-1))>0`.

Therefore

`b1-b0 = (m+delta)*(q_m(pi_c)-pi_c)/(2m+delta) > 0`.                (6.12)

This proves the proposition. `square`

---

# 7. B7 — take the scaling limit: what the new exponent does and does not say

The neighboring independent-edge growing-graph theorem has largest critical components of order `sqrt(n)/log n`, so its power exponent is `1/2`. The new lower exponent is compatible with, but does not prove, that power.

Indeed, at the exact fixed-outdegree threshold,

`q_m(pi_c) < m*pi_c`

by the strict union bound, while the explicit threshold formula gives

`m*pi_c < delta/[2(m+delta)]`

because the square-root term in the denominator of `pi_c` is positive. Hence

`b1 < 1/2`.                                                         (7.1)

Equivalently,

`1/2-b1 = [delta-2(m+delta)q_m(pi_c)]/[2(2m+delta)] > 0`.

So this run does **not** transfer the `sqrt(n)/log n` theorem, and it does not claim a critical-window width. It isolates a fixed-outdegree mechanism that raises the rigorously certified critical expected-size exponent while leaving a positive exponent gap to `1/2`.

A more aggressive local linearization would replace the global chord coefficient `q_m(pi)` by the tangent coefficient `m*pi` when the tracked attractiveness fraction is small. That would yield the candidate exponent

`b_tan(pi)=[m+m*pi*(m+delta)]/(2m+delta)`,

which is larger than `b1`. This run does **not** claim it: proving it requires a quantitative control showing that the shadow attractiveness spends enough time at `W_t/t=o(1)` with an error strong enough to close the drift iteration. That is the clean next obstruction.

Outcome of B7: **the limit-scale comparison identifies a precise next target, not a solved window theorem**.

---

# 8. Before / after and interpretation

Frozen metric:

`gamma_E = liminf log E|C_max(n,pi_c)| / log n`.

Before this run:

`gamma_E >= b0 = [m+(m+delta)pi_c]/(2m+delta)`.

After this run:

`gamma_E >= b1 = [m+(m+delta)(1-(1-pi_c)^m)]/(2m+delta)`.

Strict movement:

`b1-b0 > 0` for every `m>=2`, `delta>0`.

Illustration only, not part of the proof: for `m=2, delta=1`, the exact threshold formula gives `pi_c≈0.04587585`, the source lower exponent is `b0≈0.42753`, and the block-activation bound is `b1≈0.45379`. No numerical value is used in the theorem.

This is **PARTIAL** because an expectation lower bound is far weaker than identifying the critical window, proving tight component scaling, or obtaining a distributional limit.

# 9. Prior-art / novelty screen for the mechanism

Searches this run included the exact source aliases plus `1-(1-p)^m preferential attachment percolation component`, the Ray thesis's Theorem 7.2.1 / collapsing discussion, the Hazra--van der Hofstad--Ray threshold paper, and the 2025 growing-graph critical-window theorem. I found the source tree/collapsing lower exponent `1-chi+pi*chi`, but not the block-activation exponent in (6.2). This is **bounded negative evidence only**. The proposition is a self-derived candidate theorem and has not had the repository's independent audits; it is not labelled novel or closed.

# 10. Capability / scheduler honesty

The interface available to this run still exposes no model selector, reasoning selector, or guaranteed execution duration. GPT-6 / maximum is therefore prompt text only. Actual model visible to this run is GPT-5.6 Sol; reasoning telemetry is `UNVERIFIED`.

The repository's latest `RESULTS.md` now records that P26's full prompt update succeeded in one authorized context and that the older P26 permission failure is historical there; a separate context still records denied native edits for other IDs. If an interface returns `You cannot modify this task`, the compliant workaround remains to use an authorized account/workspace context or platform support. Creating a duplicate task or bypassing permissions is not an acceptable workaround. This run made no scheduler changes.

# 11. Ledger delta / continuation checkpoint

Suggested own-track ledger delta only; root shared ledger not edited:

`HARD7-04 | P0151 fixed-outdegree PA critical window | gamma_E lower bound | b0 -> b1 | PARTIAL / OPEN`

where

`b0=[m+(m+delta)pi_c]/(2m+delta)`,

`b1=[m+(m+delta)(1-(1-pi_c)^m)]/(2m+delta)`.

Stagnation count on the new target: `0` because the frozen quantity moved on admission run.

Next nonrepeating methods if continued: **B5 add/interpolate in the retention parameter, B11 dualize via the mean-offspring / exploration operator, B30 localize by age scale**. The concrete next obligation is to control the shadow attractiveness fraction sufficiently sharply to justify the tangent coefficient `m*pi` (or find a counterexample), then ask whether the resulting exploration can be upgraded from expectation to probability/tightness.
