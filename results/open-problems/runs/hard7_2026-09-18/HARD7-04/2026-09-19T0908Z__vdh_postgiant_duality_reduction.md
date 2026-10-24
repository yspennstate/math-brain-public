Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO MOVEMENT in the frozen metric `lim Delta_dual,n`: `0 -> 0`; methods actually used: B1 CHANGE THE CATEGORY, B28 REPLACE “FOR ALL” WITH “FOR TYPICAL”, B30 ONE SCALE / ONE DIRECTION AT A TIME. Source status: PARTIAL / OPEN.**

# HARD7-04 bounded research iteration — post-giant stopping-time duality reduction

Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity and exact target

I did not restart from the old I0049 queue seed. Repository task-health already records I0049 as **KNOWN / RESOLVED IN QUEUED SCOPE**. The preceding HARD7-04 target P0157 was explicitly released after its two Section-I recoveries. The current exclusive claim is

`operations/claims/VDH-8.3-DUALITY.md`,

owned by HARD7-04 and still OPEN / ADMITTED.

The canonical source is Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated 4 August 2026, Notes on Section 8.3, printed p. 245 / PDF p. 255:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

In the finite-third-moment barely-supercritical configuration model the source asks, after discussing the second-largest component and the expected removal of high-degree vertices into the giant:

> “Does the discrete duality principle still hold?”

The frozen exact scope remains deterministic-degree configuration models with

\[
\nu_n=1+\varepsilon_n,\qquad
\varepsilon_n\downarrow0,\qquad
\varepsilon_n n^{1/3}\to\infty,
\]

finite convergent third degree moment and a nondegenerate critical limiting degree law. Fixed-supercritical duality, Erdős--Rényi duality, the 2D Hamming-graph result and independent-edge inhomogeneous duality are prior art, not this claim.

The frozen source-relevant metric from admission is

\[
\Delta_{\rm dual,n}:=
\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|.
\]

Admission baseline was `UNMEASURED`. The immediately preceding mathematical checkpoint

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T0838Z__vdh_duality_parameter_reduction.md`

already proved `Delta_dual,n -> 0` for the ideal branching-process tilted degree law. Thus the frozen metric entering this iteration is already the exact asymptotic value `0`, and it stays `0`. **NO MOVEMENT** in that fixed metric is claimed. The progress below is a graph-level lift of the same reflection identity, not a redefinition of the metric.

Before working I reread the controlling policy files, root `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, `QUEUE.md`, the current claim, the P0157 handoff state, current HARD7-04 artifacts, intake/search hits around I0049 and related random-graph problems, and neighboring critical-window work including R12's H0006 random-regular finite-size report. No canonical ownership collision was found for `VDH-8.3-DUALITY`.

## 2. Fresh source/current-literature check — 19 September 2026

The current-status screen was refreshed rather than inferred from the claim file.

Primary and directly relevant sources checked:

1. van der Hofstad, 4 August 2026 monograph above — the question is still posed there in the notes to Section 8.3.
2. R. van der Hofstad, S. Janson, M. Luczak, *Component structure of the configuration model: Barely supercritical case*, Random Structures & Algorithms 55 (2019), 3--55, DOI `10.1002/rsa.20837`. This proves the barely-supercritical unique giant and the exploration estimates used below, but not the sharp source-requested second-largest scaling. The full text itself notes that even concentration of the barely-subcritical largest component was not then known in the generality under discussion.
3. M. Coulson, G. Perarnau, *Largest component of subcritical random graphs with given degree sequence*, Electronic Journal of Probability 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`. It gives general upper bounds in the (barely) subcritical configuration model, asymptotically tight for certain degree sequences, rather than a universal sharp scaling theorem closing the 2026 question.
4. R. van der Hofstad, M. J. Luczak, J. Spencer, *The second largest component in the supercritical 2D Hamming graph*, Random Structures & Algorithms 36 (2010), DOI `10.1002/rsa.20288`. This is a different model and explicitly presents its result as evidence for a discrete-duality principle.

Bounded web searches on 19 September 2026 included the exact phrase `"Does the discrete duality principle still hold?"`, `barely supercritical second largest configuration model`, and later `barely subcritical configuration model largest component` searches. I found the sources above and model-specific neighboring results, but no later paper closing the precise deterministic-degree finite-third-moment barely-supercritical configuration-model question. This is bounded negative evidence, not a worldwide novelty certificate.

## 3. Previous checkpoint and the obstruction it left

The prior artifact proved, for the ideal dual law tilted by extinction probability `xi_n`,

\[
q_n:=1-\xi_n\sim\frac{2\varepsilon_n}{\kappa},
\qquad
1-g_n'(\xi_n)=\varepsilon_n+o(\varepsilon_n),
\]

and an exact fixed-component deletion lemma. It left two apparent graph-level obligations:

1. control the random residual degree law after the giant;
2. avoid conditioning the complement on the future event that the removed component is the largest.

This run changes the route. The full histogram is unnecessary, and the future-largest conditioning can be eliminated entirely by stopping the standard exploration at an observable giant-scale component boundary.

---

# 4. B1 — CHANGE THE CATEGORY: from residual histograms to a weighted empirical process

Give every half-edge an independent `Exp(1)` maximal lifetime, as in the 2019 exploration. For vertex `i`, let `E_i` be the minimum of its `d_i` half-edge lifetimes, so

\[
E_i\sim\operatorname{Exp}(d_i)
\]

independently. Define

\[
A_n(t)=\sum_i d_i\mathbf 1_{\{E_i>t\}},
\qquad
B_n(t)=\sum_i d_i(d_i-1)\mathbf 1_{\{E_i>t\}}.
\]

Instead of controlling every residual degree count, I proved the weighted half-line empirical-process inequality

\[
\mathbb E\sup_t\left|
\sum_i w_i(\mathbf 1_{\{E_i>t\}}-\mathbb P(E_i>t))
\right|
\le 4\Bigl(\sum_iw_i^2\Bigr)^{1/2}.
\tag{4.1}
\]

The proof is on the page in the artifact: symmetrize, condition on the clocks, order vertices by decreasing clock value so the half-line class becomes prefixes, then apply the `L^2` maximal inequality to the weighted Rademacher partial sums.

For `w_i=d_i`, (4.1) is `O(n^{1/2})`. For `w_i=d_i(d_i-1)`, third-moment convergence implies

\[
d_{\max}^3/n\to0,
\qquad
\sum_i d_i^4\le d_{\max}\sum_i d_i^3=o(n^{4/3}),
\]

and hence

\[
\sup_t|A_n(t)-\mathbb EA_n(t)|=o_p(n\varepsilon_n),
\qquad
\sup_t|B_n(t)-\mathbb EB_n(t)|=o_p(n\varepsilon_n).
\tag{4.2}
\]

This is uniform over **every** time, so the evaluation time may depend on the exploration; no optional-stopping estimate is needed for these empirical sums.

**Outcome B1:** success. The random residual-histogram problem is reduced to two weighted sums.

Full proof:

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T0855Z__vdh_random_time_weighted_residual.md`

creation commit `23651c21f9e2fdfb24f5e13aa5bf4e7a8f8bcb65`.

---

# 5. B28 — REPLACE “FOR ALL” WITH “FOR TYPICAL”: a lawful post-giant stopping remainder

The naive statement “condition on deleting the largest component” is awkward because largestness depends on the unexplored future. The 2019 theorem gives a way around this.

Let `H(C)` be the half-edge volume of component `C`. In the source regime,

\[
H(G_n)=\Theta_p(n\varepsilon_n),
\qquad
\max_{C\ne G_n}H(C)=o_p(n\varepsilon_n).
\]

Choose deterministic `eta_n downarrow0` slowly enough that w.h.p.

\[
\max_{C\ne G_n}H(C)<\eta_n n\varepsilon_n<H(G_n).
\]

Now stop the sequential exploration at the end of the **first completed component whose observed half-edge volume exceeds** `eta_n n epsilon_n`. This is a genuine stopping rule. With probability `1-o(1)` it is exactly the end of the giant component.

At every completed-component stopping boundary there are no active half-edges. By deferred decisions, conditional on the revealed history, the still-unpaired half-edges are a **uniform perfect matching**. Hence the unexplored remainder is exactly a configuration model on its random sleeping degree sequence. No future-largest conditioning is present.

There is also no hidden loss of the actual second-largest component. Conditional on the final graph, the exploration order of components is size-biased by edge/half-edge volume. Therefore

\[
\mathbb P(C_{2,n}\text{ is explored before }G_n\mid G_n^{\rm final})
=\frac{H(C_{2,n})}{H(C_{2,n})+H(G_n)}=o_p(1),
\]

so unconditionally this probability tends to zero. Thus w.h.p. the largest component in the exact post-stopping configuration model is the original `C_{2,n}`.

The remaining difference between the exact sleeping set and the independent-clock survivor set comes only from roots forced awake by C1. If `R_n^{root}` is the set of roots through the giant, then

\[
\sum_i d_i^2
|1_{\{i\text{ sleeping at }\tau_n\}}-1_{\{E_i>\tau_n\}}|
\le\sum_{v\in R_n^{root}}d_v^2.
\tag{5.1}
\]

Conditional size-biased component order gives `#R_n^{root}=O_p(epsilon_n^{-1})`. At every C1 call through the giant, a root is selected by a uniform sleeping half-edge, so

\[
\mathbb E[d_{root}^2\mid\text{sleeping set }S]
=\frac{\sum_{i\in S}d_i^3}{\sum_{i\in S}d_i}=O(1)
\]

with high probability: only `o_p(n)` total half-edge mass has been removed and the third-moment sum is `O(n)`. Consequently

\[
\sum_{v\in R_n^{root}}d_v^2=O_p(\varepsilon_n^{-1})
=o_p(n\varepsilon_n),
\tag{5.2}
\]

because `n epsilon_n^2 -> infinity` follows from `epsilon_n n^{1/3}->infinity`.

Combining (4.2), the published stopping-time localization `tau_n=-log(xi_n)+o_p(epsilon_n)`, the ideal drift reflection, and (5.2), I obtain for the **actual exact post-giant configuration-model remainder**

\[
\boxed{
\nu_n^{post}=1-\varepsilon_n+o_p(\varepsilon_n).
}
\tag{5.3}
\]

The remainder also preserves the same limiting degree law and finite third moment: only `o_p(n)` vertices are removed, and deterministic third-moment uniform integrability makes the removed normalized third-moment mass `o_p(1)`.

**Outcome B28:** success. The earlier “largest-conditioning obligation” is removed; the actual second-largest component is w.h.p. the largest component of an exact, genuinely barely-subcritical configuration model with random residual degree sequence.

Full proof:

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T0900Z__vdh_postgiant_stopping_reduction.md`

creation commit `5791d70f0a20e89b8a71aea722201e1c2b6c4a89`.

---

# 6. B30 — ONE SCALE AT A TIME: why the source window is exactly the usable noise gap

The weighted second-factorial empirical fluctuation in (4.2) is bounded by

\[
o(n^{2/3}).
\]

The reflected-drift signal is

\[
n\varepsilon_n.
\]

Therefore the present route separates signal from clock noise exactly when

\[
\frac{n^{2/3}}{n\varepsilon_n}
=\frac1{\varepsilon_n n^{1/3}}\to0.
\]

This is precisely the finite-third-moment “outside the critical window” condition in the source regime. At the critical scale `epsilon_n asymp n^{-1/3}`, the empirical second-moment noise and drift signal are both order `n^{2/3}` and this proof mechanism cannot identify a deterministic reflected drift.

This is not a necessity theorem for all possible methods. It is a sharp diagnosis of where this specific weighted-clock route stops working.

**Outcome B30:** success. The method's obstruction lands on the canonical `n^{-1/3}` critical scale rather than on an arbitrary technical cutoff.

---

## 7. What moved mathematically despite the frozen metric not moving

The fixed metric could not improve below its already-proved zero asymptotic defect. But the logical distance to the source question decreased substantially.

Before this run, the route theorem only knew the ideal branching-process dual law had the right drift, and it listed random-residual-law plus largest-conditioning as separate unsolved obligations.

After this run:

1. random clock sampling of the first two residual degree moments is uniformly negligible at `n epsilon_n` precision;
2. the exploration can be stopped by an observable component-size rule that identifies the giant w.h.p.;
3. the remaining pairing is conditionally an exact configuration model;
4. the true second-largest component is post-giant w.h.p.;
5. the forced-root discrepancy is `o_p(n epsilon_n)` in the exact degree-square norm needed for criticality;
6. the actual post-giant configuration model has reflected drift `1-epsilon_n+o_p(epsilon_n)` and retains the finite-third-moment class.

The source remains OPEN because the final step is now a sharp barely-subcritical largest-component theorem, uniformly applicable to this random residual sequence. Coulson--Perarnau supply strong upper bounds and tightness for certain sequences, but the fresh literature screen did not establish the full source-requested universal scaling in this exact regime.

## 8. Remaining obligation and next methods

The new blocking statement is no longer “prove duality of the residual law.” It is:

\[
\boxed{
\text{Given a random finite-third-moment degree sequence with }
\nu_n=1-\varepsilon_n+o_p(\varepsilon_n),
\ \varepsilon_n n^{1/3}\to\infty,
\text{ determine the sharp largest-component scaling uniformly enough to apply conditionally.}
}
\]

The simplest source-relevant next test is to take the sharpest Coulson--Perarnau upper/lower hypotheses, verify which are automatically inherited by the post-giant sequence, and identify the single missing tail/extremal condition. Do not spend the next run building another checker unless that analysis produces a finite claim worth certifying.

Next B-triple reserved: **B4** prove the strongest inherited subcritical special case completely; **B21** search the subcritical theorem under alternate names/models; **B24** identify the extremal residual degree profiles saturating the known upper bound.

This is not yet a three-run frozen-obligation streak for the current `VDH-8.3-DUALITY` target: although the frozen numerical metric cannot move below zero, the remaining source obligation changed materially in this run. Section-I stuck rotation therefore does not fire here.

## 9. Model / scheduler-control truth

The requested `GPT-6 / maximum` remains prompt text only in this task environment. The task-management surface available here exposes title/prompt, schedule/timing, enabled state, and notification/email controls; it exposes **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model attestation, and no guaranteed-duration control**. The actual model for this report is GPT-5.6 Sol; reasoning level is UNVERIFIED.

Making GPT-6/maximum binding would require an owner-authorized product/workspace/admin/API control that persists model-family and reasoning-effort fields into execution routing and returns per-run attestation. That control is not exposed here, so I did not pretend to set it.

The historical P26 response `You cannot modify this task` is an authorization boundary. The lawful workaround is modification from the task's owning/authorized context or platform/admin support; duplicating, bypassing, or silently replacing the protected task is not a valid workaround. No scheduler was created, disabled, reactivated, or modified in this run.

## 10. Bookkeeping / evidence

No finite exhaustive claim was introduced in this iteration, so no exact-arithmetic checker was manufactured merely for activity. Both new theorem-sized claims have full written proofs in the two artifacts above.

Fresh literature queries and the exact source status are recorded in Sections 1--2. This report makes no source closure claim and requests no audit yet.

### ledger_delta

```yaml
track: HARD7-04
target: VDH-8.3-DUALITY
owner: HARD7-04
source_status: OPEN
research_status: PARTIAL
metric:
  name: Delta_dual_n = abs((1-nu_dual_n)/epsilon_n - 1)
  admission_baseline: UNMEASURED
  before_this_run: asymptotic_limit_0
  after_this_run: asymptotic_limit_0
  movement: NO_MOVEMENT
methods_tried:
  - B1
  - B28
  - B30
new_graph_level_result:
  postgiant_exact_CM: true_with_probability_1_minus_o1
  C2_is_largest_of_remainder: true_with_probability_1_minus_o1
  nu_post: 1 - epsilon_n + o_p(epsilon_n)
  finite_third_moment_preserved: true_in_probability
remaining_obligation: >-
  Prove/apply a sharp barely-subcritical largest-component scaling theorem
  uniformly for the random post-giant degree sequence; identify exactly which
  residual tail/extremal hypothesis is not automatic.
artifacts:
  - path: artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T0855Z__vdh_random_time_weighted_residual.md
    commit: 23651c21f9e2fdfb24f5e13aa5bf4e7a8f8bcb65
  - path: artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T0900Z__vdh_postgiant_stopping_reduction.md
    commit: 5791d70f0a20e89b8a71aea722201e1c2b6c4a89
runtime:
  actual_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  scheduler_model_selector: NOT_EXPOSED
  scheduler_reasoning_selector: NOT_EXPOSED
```
