Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-04 frozen metric no movement, `Q_n=sigma_n^2/(d_max delta_n) -> sigma_n^2/(d_max delta_n)`; methods B6 / B11 / B24.**

# HARD7-04 bounded research iteration — P0157 finite-population hub LLN

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source OPEN by current source plus bounded literature review.** This is the third P0157 run and the second consecutive no-movement run for the frozen metric after its exact identification. It is therefore not yet a section-I stuck run.

## 1. Continuity, ownership, and repository state

I resumed the exact admitted claim `operations/claims/P0157.md`, owned exclusively by HARD7-04. I did not restart admission or substitute I0049.

Before research I read/recovered:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- latest own checkpoint `runs/hard7_2026-09-18/HARD7-04/2026-09-18T22-28-37Z__p0157_maxroot_cycle_defect.md`;
- newest neighboring HARD7-03 report `runs/hard7_2026-09-18/HARD7-03/20260918T2121Z__d0025-two-slow-site-bellman-envelope.md`;
- newest neighboring HARD7-05 report `runs/hard7_2026-09-18/HARD7-05/2026-09-18T2237Z_theta_quarter_exact.md`;
- repository searches over the intake/claim ledgers, including the intake tier entry `P0157|3|two competing scales, barely subcritical CM`.

Fresh collision searches still show `P0157` owned by HARD7-04, with neighboring admission screens explicitly treating it as unavailable to other tracks. I found no release, duplicate owner, posted equivalent, or canonical-alias collision.

The preceding run had already eliminated the surplus-edge obstruction for a chosen maximal-degree root, proving its component is a tree with probability `1-o(1)` and is tight on the scale `d_max/delta_n`. Its remaining graph-vs-branching obstruction was finite-population degree depletion. This run attacks that obstruction directly rather than adding another certificate to the unchanged metric.

## 2. Exact source and current-status refresh

I re-read the current primary source itself, not an old intake paraphrase:

Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF page 255:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

The current page contrasts Janson's strictly subcritical high-degree law with the Erdos--Renyi barely-subcritical scale and says, in the author's words, **“This suggests that a phase transition occurs within the subcritical regime”** for finite-third-moment configuration models. The current monograph also states the finite-third-moment critical theory under `E[D_n^3] -> E[D^3] < infinity`.

The canonical P0157 residual therefore remains:

\[
\delta_n:=1-\nu_n\downarrow0,\qquad n\delta_n^3\to\infty,
\]

with finite-third-moment degree sequences, and determine when

\[
H_n:=\frac{d_{\max}}{\delta_n}
\quad\hbox{versus}\quad
E_n:=\delta_n^{-2}\log(n\delta_n^3)
\]

governs the largest component, including the crossover.

I also refreshed the closest published later result:

- Matthew Coulson and Guillem Perarnau, *Largest component of subcritical random graphs with given degree sequence*, EJP 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`.

Their Theorem 1.3 gives an Erdos--Renyi-type upper bound under `Delta |Q|=o(R)` and a barely-subcritical condition; their more general Theorem 1.5 uses an MGF hypothesis and `Delta<=n^(1/6)`. These do not state the full finite-third-moment two-scale crossover retained as open in the 4 August 2026 monograph.

Bounded dated searches in this run used the phrases

- `barely subcritical configuration model finite third moment phase transition`,
- `largest barely subcritical component configuration model d_max`,
- `2025 2026 barely subcritical configuration model largest component finite third moment`,

and recovered Coulson--Perarnau plus adjacent models, but no theorem closing the exact P0157 residual. This is a bounded current-status check, **not** proof of worldwide absence or novelty.

## 3. Frozen metric — before/after

The source-linked frozen metric remains the branching-surrogate fluctuation ratio

\[
Q_n:=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

Before:

\[
Q_n=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

After:

\[
Q_n=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

**No movement.** The run nevertheless makes source-route progress: it proves that in the regime `d_max delta_n -> infinity`, the *actual configuration-model component* of a maximal-degree vertex obeys the same hub law of large numbers, without an iid branching coupling.

## 4. B6 — deform the exact graph exploration to the solvable drift

The obvious coupling route asks the finite-population exploration to look iid for `d_max/delta_n` steps. That is unnecessarily strong and obscures the effect of consuming high-degree vertices.

Instead I kept the exact active-half-edge exploration. Let `A_t` be the active queue, `tau` its extinction time, and `U_t` the unseen vertices. With `ell_n=sum_i d_i`,

\[
D_t=\ell_n-2t-1,
\]

and the exact conditional drift is

\[
b_t
=\frac{\sum_{i\in U_t}d_i(d_i-2)-2(A_t-1)}{D_t}.
\tag{4.1}
\]

Since

\[
\sum_i d_i(d_i-2)=-\ell_n\delta_n,
\]

if `R_t` is the discovered non-root set and `s_i=d_i(d_i-2)`, then

\[
\boxed{
 b_t+\delta_n
 =\frac{-\delta_n(2t+1)-d_{\max}(d_{\max}-2)
       -\sum_{i\in R_t}s_i-2(A_t-1)}{D_t}.
}
\tag{4.2}
\]

Thus the graph problem is deformed into the solvable deterministic drift `-delta_n`, plus an explicit finite-population error.

The key new device is a size-biased depletion budget

\[
g_i=d_i+|d_i(d_i-2)|,
\qquad G_t=\sum_{i\in R_t}g_i.
\]

Because `d_i g_i <= 2d_i^3`, the finite-third-moment assumption gives a **uniform O(1) expected cost per discovery step**. On the horizon

\[
M_n=\left\lceil 2d_{\max}/\delta_n\right\rceil,
\]

choose

\[
a_n=\sqrt{\frac{n\delta_n^2}{d_{\max}}}\to\infty.
\]

Then

\[
\mathbb P(G_{M_n\wedge\tau}>a_nM_n)=o(1).
\tag{4.3}
\]

The same finite-third-moment bound gives `d_max=O(n^(1/3))`. Since `n delta_n^3 -> infinity`, writing `x_n=n^(1/3)delta_n` gives `x_n->infinity` and

\[
\frac{d_{\max}^2}{n\delta_n}=O(x_n^{-1})=o(1),
\qquad
\frac{d_{\max}}{n\delta_n^2}=O(x_n^{-2})=o(1).
\tag{4.4}
\]

On the good event in (4.3), (4.2) therefore gives uniformly before extinction

\[
\sup_{t<M_n\wedge\tau}|b_t+\delta_n|=o(\delta_n).
\tag{4.5}
\]

So the finite-population deformation closes at the exact extremal third-moment scale; no additional `d_max=o(n^(1/3))` hypothesis is needed.

**Outcome of B6: success.** It replaces the unproved long iid coupling by an exact drift identity plus a one-line size-biased budget.

## 5. B11 — dualize component size into a queue first-passage problem

The exact conditional second moment of the queue increment is

\[
q_t
=\frac{\sum_{i\in U_t}d_i(d_i-2)^2+4(A_t-1)}{D_t}.
\tag{5.1}
\]

Under the same stopped budget, `q_t=O(1)` uniformly. Write the Doob decomposition

\[
A_t=d_{\max}+\sum_{s<t}b_s+\mathcal M_t.
\]

If `d_max delta_n -> infinity`, Doob's inequality gives

\[
\max_{t\le M_n}|\mathcal M_t|=o_{\mathbb P}(d_{\max}),
\tag{5.2}
\]

because the quadratic variation is `O(M_n)` and

\[
M_n/d_{\max}^2=O((d_{\max}\delta_n)^{-1})=o(1).
\]

Combining (4.5) and (5.2), uniformly up to extinction,

\[
A_t=d_{\max}-\delta_nt+o_{\mathbb P}(d_{\max}).
\tag{5.3}
\]

The extinction time is therefore squeezed between `(1-eps)d_max/delta_n` and `(1+eps)d_max/delta_n`, for every fixed `eps>0`:

\[
\boxed{
\frac{\tau}{d_{\max}/\delta_n}\xrightarrow{\mathbb P}1.
}
\tag{5.4}
\]

The preceding run's cycle-defect argument can be made simultaneously on these assumptions; the self-contained artifact repeats it and obtains

\[
\mathbb P(C(v_{\max})\text{ cyclic})=o(1).
\tag{5.5}
\]

Therefore `|C(v_max)|=tau+1` with probability `1-o(1)` and

\[
\boxed{
\frac{|C(v_{\max})|}{d_{\max}/\delta_n}
\xrightarrow{\mathbb P}1
\quad\text{whenever }d_{\max}\delta_n\to\infty.
}
\tag{5.6}
\]

The complete theorem and proof are archived in

`artifacts/hard7_2026-09-18/HARD7-04/p0157_finite_population_hub_lln.md`

at substantive artifact commit

`3c3002481b1df39370810be2bbf93c58d9ca18b6`,

which was read back successfully before this report was written.

**Outcome of B11: success.** The dual object is the active-queue hitting time, and its martingale scale is exactly smaller than the deterministic hub drift under `d_max delta_n -> infinity`.

No finite exhaustive claim was made, so I did not manufacture an exact-arithmetic checker. The theorem-sized claim is written on the page.

## 6. B24 — extremal allowed degree identifies the real boundary

I deliberately tested the worst degree size permitted by the source's finite-third-moment condition rather than a bounded-degree toy case.

The extremal constraint is

\[
d_{\max}=O(n^{1/3}).
\]

At that boundary, the two dangerous finite-population ratios are exactly

\[
\frac{d_{\max}^2}{n\delta_n}
\lesssim \frac1{n^{1/3}\delta_n},
\qquad
\frac{d_{\max}}{n\delta_n^2}
\lesssim \frac1{(n^{1/3}\delta_n)^2}.
\]

The source's barely-subcritical condition `n delta_n^3 -> infinity` is precisely what drives both to zero. Thus the extremal object does **not** create a hidden depletion obstruction.

More importantly, in the strong hub-dominant regime

\[
\frac{H_n}{E_n}
=\frac{d_{\max}\delta_n}{\log(n\delta_n^3)}\to\infty,
\]

we automatically have `d_max delta_n -> infinity`. Hence (5.6) applies throughout that whole source-relevant regime and gives the graph-level lower half of the predicted hub behavior:

\[
|C(v_{\max})|=(1+o_{\mathbb P}(1))H_n,
\qquad
L_1\ge(1-o_{\mathbb P}(1))H_n.
\tag{6.1}
\]

**Outcome of B24: success.** The worst finite-third-moment hub is still benign; the remaining obstacle is global extreme-component control, not local depletion or cycles.

## 7. What changed mathematically

The frozen metric did not move, but the source-route obstruction changed materially.

Before this run:

- the ideal independent Galton--Watson hub forest was known here to self-average when `d_max delta_n -> infinity`;
- the actual maximal-degree component was only known here to be tree-like with high probability and tight on `d_max/delta_n`;
- finite-population degree depletion remained an explicit gap.

After this run:

- the actual maximal-degree component satisfies the full graph-level law of large numbers (5.6);
- therefore the source's strong hub-dominant regime already contains a component of asymptotic size `H_n`;
- finite-population depletion and surplus edges are no longer candidate obstructions for that rooted law.

This is still **PARTIAL**, not source closure. It does **not** prove that no other component exceeds the hub, does not derive the Erdos--Renyi extreme asymptotic under the full source assumptions, and does not settle the order-one crossover.

The nearest next obligation is now sharply global:

\[
\text{control }L_1\text{ from above when }H_n/E_n\to\infty,
\]

then attack the `H_n/E_n -> 0` and order-one transition regimes. The Coulson--Perarnau bounds suggest that the low-hub side should be attacked through an exponential-change-of-measure or exploration-tail argument, but their stated hypotheses do not simply cover the full source crossover.

## 8. Prior-art and capability honesty

The active-half-edge queue, Doob decomposition, and size-biased exposure estimates are standard random-graph technology. I do **not** claim (5.6) is literature-new merely because the bounded search did not surface this exact formulation. The result is recorded as a self-checked route theorem pending independent review.

The scheduler/interface limitation remains unchanged in this run. The exposed automation controls are title, prompt, schedule, timing mode, and enabled state. There is **no model selector, no reasoning-effort selector, no authenticated reasoning telemetry, and no guaranteed execution duration**. GPT-6/maximum is therefore only requested in prompt text here. Changing that requires a platform/API surface with native model/reasoning controls or authenticated runtime metadata; it cannot be fixed by a GitHub edit or prompt assertion.

Repository policy records historical native probes in some contexts returning `You cannot modify this task` for P26/P01/P03, while another authorized context later succeeded for P26. The lawful workaround for any still-denied scheduler ID is an authorized owner/workspace context or platform support. I did not bypass a denial, clone a task, reactivate anything, or create/modify another schedule.

## 9. Ledger delta / next checkpoint

```yaml
track: HARD7-04
canonical_claim: P0157
owner: HARD7-04
source_status: OPEN_BY_CURRENT_SOURCE_AND_BOUNDED_SEARCH
research_status: PARTIAL
frozen_metric: Q_n = sigma_n^2/(d_max * delta_n)
before: sigma_n^2/(d_max * delta_n)
after: sigma_n^2/(d_max * delta_n)
movement: false
unchanged_count_on_P0157: 2
methods_this_run: [B6, B11, B24]
auxiliary_progress:
  maximal_root_graph_lln: "tight only -> |C(v_max)|/(d_max/delta_n) -> 1 when d_max*delta_n -> infinity"
  strong_hub_lower_bound: "unproved graph LLN -> L1 >= (1-o_P(1)) H_n when H_n/E_n -> infinity"
  finite_population_depletion: "open route obstruction -> controlled at o(delta_n) relative drift"
closure: false
audits_requested: 0
next_obligation: "global upper bound for L1 in hub-dominant regime, then ER-dominant/order-one crossover"
next_candidate_methods: [B5, B19, B27]
artifact_commit: 3c3002481b1df39370810be2bbf93c58d9ca18b6
```

No shared root ledger was edited; per policy this worker records only its structured `ledger_delta`. No email or Drive action was taken, and no schedule was created, modified, disabled, or reactivated.