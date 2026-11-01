Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: frozen I0056/H_{5,5} outer-vertex interval width `0 -> 0`; successor-admission metric `E_ready: 0 -> 0`; material admission-side update: F0138 is now positively KNOWN/RESOLVED_IN_LITERATURE_2026 and therefore removed from the possible successor frontier; methods #6 DEFORM TO A POINT YOU CAN SOLVE, #13 FIND WHAT ONLY INCREASES, #19 MAKE IT AN ALGORITHM.**

# R06 — successor-admission delta after the closed H55 metric: F0138 positive resolution

Date: 2026-09-18 UTC  
Worker: R06  
Lane: CLOSABLE OUTSIDE  
Repository: private `yspennstate/math-open-problems`, branch `master`

## 1. Continuity and frozen source state

I continued from the newest immutable R06 report

`runs/R06/20260918T1420Z_successor_admission_delta_i0130_h0021_43.md`

and did **not** reopen Lyons--Peres I0056. The attacking lifecycle on I0056 already rotated after six unchanged runs.

The exact source remains Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20:

> What is `Phi_V(G)` for regular co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive plane graphs `G`?

The frozen normalization is the outer vertex boundary

\[
\partial_VK=\{x\notin K:\exists y\in K,\ x\sim y\},\qquad
\Phi_V(G)=\inf_{0<|K|<\infty}\frac{|\partial_VK|}{|K|}.
\]

For the Schlaefli `{5,5}` tessellation `H_{5,5}` the preserved result is

\[
\boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad
[L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

The two independent audits remain

- `R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z = PASS_MATH_SCOPE / NOVELTY_UNVERIFIED`;
- `P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15 = PASS_FULL_MATHEMATICAL_PROOF / REGULAR-COREGULAR-FIRST-CLAUSE / SOURCE_PARTIAL / PRIOR_ART_UNVERIFIED`.

Hence the frozen H55 subtarget is **PROVED / audit-complete**. Together with the already-known face-degree `3,4` cases of Haslegrave--Panagiotis, the regular/co-regular first clause is mathematically accounted for. The full two-clause source question remains **PARTIAL** because the more-general transitive-plane-graph clause is not closed here.

No shared root, peer file, existing claim, scheduler, email, Drive object, or public posting is changed in this run.

## 2. Repository and literature read before admission work

I reread/recovered the required current entry points and deltas before acting:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, root `RESULTS.md`, and current `QUEUE.md` evidence;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- newest own R06 report named above;
- current coordinator admission reconciliation `operations/task_health/runs/2026-09-18T150500Z/admission_reconciliation.md`;
- newest neighboring CLOSABLE frontier report `runs/R01/20260918T1504Z_source_frontier_i0130_claimed_i0131_absent_5c8e2a1f.md` and the current R02 admission delta;
- canonical current claims needed for candidate checks, including `G0002`, `G0013`, `H0021`, and `I0130`;
- the G intake `G0001--G0015` and the current F-tail source-status delta.

The current coordinator reconciliation still has

\[
E_{\rm ready}=0,
\]

with I-series source population reaching `I0130`, `I0130` already owned, and no populated `I0131+` source row. The correct action is therefore delta-only screening, not rescanning settled ranges or inventing readiness from a PENDING row.

Fresh dated source checks on 2026-09-18 also retained the I0056 exclusion boundary: Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, explicitly establish the vertex-isoperimetric constants for the triangular and square hyperbolic lattices, i.e. the `d'=3,4` cases. Those remain prior art and are not relabeled as R06 results.

## 3. Idea before code

The successor bottleneck is no longer a lack of titles. It is a filtering problem in which nearly-good candidates fail one exact gate. I therefore attacked a different question:

> Can a newly changed source-status or ownership delta produce a candidate that simultaneously passes exact source, current openness, full-source CLOSABLE scope, ownership clearance, and exclusion checks?

I looked only at changed frontiers and at the G shard newly exposed by the coordinator's cursor. No checker was written because no new finite mathematical claim was found; manufacturing a certificate for an unchanged admission metric would violate the 90/10 rule.

## 4. Method #6 — DEFORM TO A POINT YOU CAN SOLVE

I tested whether the apparently finite G-shard candidates become genuinely CLOSABLE when deformed to their simplest exact endpoint **without changing the source quantifiers**.

- `G0004` is phrased on finite graphs, but its source asks for a universal function `phi(epsilon)->1` uniformly over all finite graphs. A finite graph or fixed epsilon does not close the source; current admission screens correctly classify the program HARD.
- `G0007` asks continuity/derivative behavior at critical percolation thresholds of the upper invariant contact-process measure on a regular tree. Freezing one lambda or finite depth gives only a special case, not the critical source statement; it remains HOLD_HARD.
- `G0010` asks for the tight subcritical largest-component bound over all regimes of `Delta(G)` and `lambda(G)`. A near-regular subclass or one spectral regime is source-PARTIAL, not closure; it remains HOLD_HARD.
- `G0008` has already been classified HARD OUTSIDE and terminally handed off; a fixed `p` or finite distance does not answer monotonicity for the source's full lattice statement.

**Outcome #6:** deformation exposes tractable restricted statements, but none is source-equivalent. No HARD source is relabeled CLOSABLE merely because a special point is solvable.

## 5. Method #13 — FIND WHAT ONLY INCREASES

The useful monovariant in admission is the **positively certified exclusion set**: once a candidate is shown to be resolved in the literature, posted/excluded, or held by an unreleased exclusive claim, it cannot become free READY inventory without a genuinely new source/ownership event.

A material new exclusion arrived after the preceding R06 run:

### F0138 is now positively resolved, not merely a search miss

Canonical intake `F0138` is the Quastel--Spohn 2015 narrow-wedge KPZ two-point conjecture. The older intake deliberately retained it because the 2023 Quastel--Sarkar convergence proof later acquired a declared gap and the alternative routes had not yet been recorded there as refereed publication.

A new source reconciliation now gives positive resolution evidence:

- Xuan Wu, *The KPZ equation and the directed landscape*, **Annals of Probability 54(3) (2026), 1212--1257**, DOI `10.1214/25-AOP1788`, proves convergence of narrow-wedge KPZ solutions to the Airy sheet/directed landscape and convergence to the KPZ fixed point in locally uniform topology.
- The Quastel--Sarkar corrigendum, **JAMS 39 (2026), 1213--1216**, DOI `10.1090/jams/1075`, records the averaging-argument error in the older proof; the F0138 resolution therefore rests on Wu's independent theorem, not on ignoring that gap.

Locally uniform convergence of the narrow-wedge profile immediately implies convergence of any fixed two evaluation coordinates by the continuous-mapping theorem; the limiting one-time profile is Airy_2, whose finite-dimensional distributions are the extended-Airy-kernel determinants requested by the old source conjecture. Thus `F0138` is now correctly classified

`KNOWN / RESOLVED_IN_LITERATURE_2026 / NOT_ADMISSIBLE`.

This is a **positive source-status update**, not a novelty claim by the fleet.

**Outcome #13:** the exclusion monovariant increased by one material source-level item. It shrinks the candidate frontier but does not create a successor.

## 6. Method #19 — MAKE IT AN ALGORITHM

I made the delta-only successor procedure explicit:

1. collect only source/claim/status deltas newer than the preceding R06 report;
2. for each candidate `x`, evaluate

\[
A(x)=S(x)\land O(x)\land C(x)\land U(x)\land N(x),
\]

where `S` = exact outside source recovered, `O` = current-open, `C` = full-source genuinely CLOSABLE, `U` = ownership-clear, `N` = not posted/resolved/retired/excluded;
3. claim create-only only if all five gates pass;
4. otherwise record the exact failed gate and move to the next **new delta**, not the next stale title.

Applying it to the live near-front gives:

- `I0130`: `S,O,C,N = true`, but `U = false`; it is READY/CLOSABLE and already exclusively owned.
- `H0021`: ownership was explicitly released, but `C = false`; the full random-graph tree-universality conjecture is HARD OUTSIDE.
- `G0002`: finite/extremal and legitimately CLOSABLE, but its canonical R09 claim remains unreleased.
- `G0013`: genuinely CLOSABLE continuous-copula Wasserstein problem, but `operations/claims/G0013.md` remains an active exclusive R09 claim.
- `F0138`: `O = false` after the positive Wu 2026 resolution above.
- the remaining newly inspected G rows are either HARD, source-broad, resolved, or already claimed/terminally handed off.

Therefore no candidate has `A(x)=true` and

\[
\boxed{E_{\rm ready}:0\to0}.
\]

The successor's mathematical metric remains **UNMEASURED** and has no manufactured stagnation count.

## 7. Current literature boundary for I0056

A fresh bounded search again recovered Haslegrave--Panagiotis as the explicit resolution for the triangular/square hyperbolic regimes and did not surface a later primary paper explicitly closing the full second clause of Lyons--Peres Question 6.20. This remains negative search evidence only. It does not establish novelty for the R06 `f>=5` bridge, whose priority remains **UNVERIFIED**.

I0056 stays rotated; this literature check is status preservation, not permission to reopen research on it.

## 8. Model / scheduler control

The scheduler/task-control surface available to this worker still exposes task title/prompt, schedule or relative start, timing mode, and enabled state. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated applied-run model/effort telemetry, and no guaranteed hour-long execution field**.

Accordingly, `GPT-6 / maximum` remains a prompt request only on this surface. This run actually identifies as GPT-5.6 Sol and the reasoning level is **UNVERIFIED**; I do not infer it from the prompt.

The historical P26 response `You cannot modify this task` is authorization-context specific: repository evidence records a later authorized context that did modify P26 successfully. The lawful remedy is an owning/admin/product/backend context exposing persistent model/reasoning controls and attested run metadata, not a worker-side bypass or replacement schedule. No scheduler modification was attempted here.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R06
  lane: "CLOSABLE OUTSIDE"
  source:
    id: I0056
    citation: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20"
    original_question: >-
      What is Phi_V(G) for regular co-regular plane graphs G? What are Phi_E(G)
      and Phi_V(G) for more general transitive plane graphs G?
  frozen_subtarget:
    graph: "H_{5,5} = regular Schlaefli {5,5} tessellation"
    degree: 5
    face_degree: 5
    normalization: "outer vertex boundary |partial_V K|/|K|"
  fixed_metric:
    name: "certified interval width U-L for Phi_V(H_{5,5})"
    before: 0
    after: 0
    interval: "[sqrt(5), sqrt(5)]"
    value: "sqrt(5)"
  source_status:
    frozen_subtarget: "PROVED / AUDIT-COMPLETE"
    regular_coregular_first_clause: "mathematically accounted for"
    full_question_6_20: "PARTIAL"
    attacking_lifecycle: "ROTATED / NOT REOPENED"
  successor_admission_metric:
    name: "E_ready = newly lawful free full-source CLOSABLE successors found in this run"
    before: 0
    after: 0
  successor_metric:
    before: "UNMEASURED"
    after: "UNMEASURED"
    unchanged_count: "UNKNOWN/UNMEASURED — no successor admitted"
  tried_moves: [6, 13, 19]
  material_delta:
    F0138:
      before: "admitted/currentness unresolved in old F ledger"
      after: "KNOWN / RESOLVED_IN_LITERATURE_2026 / NOT_ADMISSIBLE"
      evidence: "Xuan Wu, Ann. Probab. 54(3) (2026), DOI 10.1214/25-AOP1788; Quastel-Sarkar corrigendum DOI 10.1090/jams/1075"
  near_front:
    I0130: "CLOSABLE but exclusively owned"
    H0021: "explicitly released but HARD OUTSIDE"
    G0002: "CLOSABLE but unreleased R09 claim"
    G0013: "CLOSABLE but active exclusive R09 claim"
  remaining_obligation: >-
    Wait for and inspect only a genuinely new source/ownership/status delta that yields
    exact source + current-open + full-source CLOSABLE + ownership-clear + non-excluded;
    claim create-only before mathematical work. Do not reopen I0056.
  audit_ids:
    - R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z
    - P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15
```

## 10. Next route

Do not rescan the same I/F/G ranges on the next invocation absent a material delta. If a new source row, explicit owner release, or positive source-status correction appears, apply the five-gate algorithm immediately. If none appears, record no mathematical movement rather than manufacturing a restricted theorem, checker, or successor metric.
