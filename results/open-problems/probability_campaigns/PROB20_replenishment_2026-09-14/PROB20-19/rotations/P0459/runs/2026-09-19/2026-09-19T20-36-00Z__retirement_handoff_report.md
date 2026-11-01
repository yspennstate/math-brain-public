Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not authenticated GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT: `E_conc: 1 -> 1`; P26 audit `1/1`; distinct OTHER audit `0/1`; post-P26 no-transition gate count `5 -> 6`. Lifecycle action: `RETIRED_AFTER_SIX_POST_TRANSITION_NO_MOVEMENT`. Final audit-gate methods: B5 / B10 / B14. No new theorem, checker, audit request, or theorem artifact was created.**

# P0459 immutable retirement / handoff after six post-P26 no-transition gates

- Native slot: `6aa7b517489c8191a5250c9384e9b33c`.
- Canonical target: `P0459`, simultaneous concentration of bilateral-preference degrees.
- Classification: `CLOSABLE OUTSIDE`.
- Outside source: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552–579, DOI `10.1017/jpr.2025.10051`, §1.1, printed p. 554 / source PDF p. 3, second additional question.
- Source target: find conditions under which Theorem 8 can be generalized to concentration of node degrees around the mean degree in the exact `LK(n,k)` model.
- Task-frozen target: a simultaneous relative all-vertex mean-centered sufficient-condition theorem in that exact model.
- Canonical claim: `operations/claims/P0459.md`.
- Own root: `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-19/rotations/P0459/`.
- Frozen metric: `E_conc in {0,1}`; admission baseline `0`; final/current value **1**. Never lower, reset, redefine, or transfer this metric.
- Mathematical status at retirement: **PROVED-CANDIDATE AT TASK LEVEL / broader source question PARTIAL**.
- Operational status: **RETIRED_AFTER_SIX_POST_TRANSITION_NO_MOVEMENT / NOT CLOSED**.
- Historical initial current-target Section-B triple: **B2 / B4 / B18**.
- Previous report: `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-19/rotations/P0459/runs/2026-09-19/2026-09-19T19-44-00Z__report.md`.
- Previous creation commit: `e0097d3f30f8701a566241e9623968c869bb2b1a`.
- Previous exact blob: `201163e392e54009fbd08b37a7830b4bd319488f`.
- Captured `master` before this run's research: `ea0b5618bd6064914dfce7f26b8e268018ba7420`.

## 1. Final material-transition screen

This run continued from the newest own-root report by path-scoped history and did not restart from admission or from D0044. Before applying the six-run retirement rule, it screened for the only events that can interrupt retirement:

1. a genuinely distinct non-owner, non-P26 full-claim P0459 audit;
2. a concrete auditor-discovered defect in the scoped theorem;
3. a source-status change;
4. material direct prior art or source-intent evidence changing the theorem's status.

Repository-wide searches for `P0459`, `P0459 audit`, `distinct OTHER P0459`, `bilateral degree concentration audit`, and recent commit history found the owner reports, the qualifying P26 audit, coordinator/admission screens, and unrelated audits, but **no distinct non-owner, non-P26 end-to-end P0459 audit**. A recent-commit sweep after the previous owner report also showed no P0459 second-audit commit; contemporaneous audit activity concerned other targets.

Fresh 2026-09-19 literature searches again recovered the current Dabirian–Subramanian article and the exact-model Erlang-weighted-tree lineage, but no later direct theorem matching all of: exact `LK(n,k)`, growing `k`, simultaneous maximum over all vertices, and deterministic-mean centering. The current Cambridge record still lists the final article in volume 63(2), June 2026, pp. 552–579, and the source question remains present. The bounded negative literature search is **not** a novelty certificate.

Therefore **no qualifying material transition occurred**. The post-P26 no-transition count is supported as `5 -> 6`, so the CLOSABLE lifecycle requires retirement rather than a seventh ordinary owner-side gate.

## 2. Preserved theorem — do not re-prove during retirement

Let `G_n ~ LK(n,k(n))`, let `D_v` be the degree of vertex `v`, and let `mu_n = E[D_v]`. The proved scoped theorem is:

```text
if 1 <= k(n) <= n-1 and k(n)/log n -> infinity,
then max_{1<=v<=n} |D_v-mu_n| / mu_n -> 0 in probability.
```

With `delta_n = sqrt(6 k log n)`, the historical threshold/Chernoff component gives, for all sufficiently large `n`, a common event with probability at least `1-2/n^2` on which

```text
k - 2 delta_n <= D_v <= k    for every vertex v.
```

P0459's new mean-centering bridge is

```text
mu_n >= (k - 2 delta_n)(1 - 2/n^2),
```

which converts the historical ceiling-centered strip into the source-requested mean-centered simultaneous relative theorem. The owner proof also records the isolated-vertex obstruction below logarithmic scale for the strengthened all-vertex relative formulation.

The theorem is preserved at retirement. Retirement does **not** revoke it, reset it, downgrade `E_conc`, or transfer the metric to a successor.

## 3. Independent audit inventory at retirement

Qualifying P26 audit:

- audit ID: `P26-AUDIT-P0459-BILATERAL-DEGREE-CONCENTRATION-69`;
- verdict: `PASS_FULL_MATHEMATICAL_PROOF`;
- report: `proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_17-00-50__run-report.md`;
- creation commit: `cd6f24fea88ec92d2266be1e9154f3d170677736`;
- exact report blob: `bda31a3933ac37592fd357e72ea9d58a9349c1be`.

P26 independently reconstructed the scoped proof and checked the one-vertex binomial tails, union bound without false inter-vertex independence, deterministic threshold-edge inclusion, expectation bridge, normalization, source scope, and historical/new contribution split.

Final audit inventory:

```text
P26 full-claim audit:        1/1
Distinct OTHER full-claim:  0/1
Total:                       1/2
```

Repeated P26 work, owner self-checks, coordinator/task-health summaries, admission screens, and neighboring P0458 work do not fill the distinct OTHER slot.

## 4. Final audit-gate methods B5 / B10 / B14

No new theorem was sought. These methods were used only as a final defect screen before lifecycle retirement.

### B5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

Parameterize the proved regime by `r_n = k(n)/log n -> infinity`. The proof's relative fluctuation scale is controlled by `2 sqrt(6/r_n)` plus the vanishing `2/n^2` bad-event term. As a function of positive `r`, `sqrt(1/r)` decreases; the worst asymptotic direction is the slowest admissible divergence of `r_n`, already stress-tested in the preceding gate. It still tends to zero.

**B5 outcome:** no defect; no new theorem claimed.

### B10 — DERANDOMIZE

The critical embedding step is pathwise: once edge weights are fixed and every threshold degree is below `k`, each threshold edge has fewer than `k` lighter incident edges at both endpoints and is therefore bilaterally preferred. This implication is deterministic conditional on the weight realization and needs no inter-vertex degree independence. The probabilistic work is only obtaining the common event by one-vertex tails plus a union bound.

**B10 outcome:** no hidden dependence defect; no new theorem claimed.

### B14 — FIND THE GROUP ACTING

The `LK(n,k)` construction with i.i.d. continuous edge weights is invariant under vertex relabeling. Thus all vertex degrees have the same marginal law and the same deterministic mean `mu_n`, validating the single common centering constant in `max_v |D_v-mu_n|`. The simultaneous statement still comes from the common strip event, not from exchangeability alone.

**B14 outcome:** no source/model/centering defect; no new theorem claimed.

## 5. Source and prior-art state frozen at retirement

Fresh checks on 2026-09-19 support the following bounded state:

1. **Current source.** Dabirian–Subramanian remains the final Cambridge article, published online 18 December 2025 and in *Journal of Applied Probability* 63(2), June 2026, pp. 552–579, DOI `10.1017/jpr.2025.10051`. It defines the bilateral `LK(n,k)` model and retains the mean-degree concentration question.
2. **Exact-model predecessor.** La–Kabkab (2015), *A New Random Graph Model with Self-Optimizing Nodes: Connectivity and Diameter*, introduced the bilateral model and studied connectivity/diameter, not the present growing-`k` simultaneous mean-centered theorem.
3. **Exact-model local-limit lineage.** Moharrami–Subramanian–Liu–Sundaresan, *The Erlang weighted tree, a new branching process*, *Random Structures & Algorithms* 64 (2024), 537–624, DOI `10.1002/rsa.21180`, studies the EWT local weak limit/root-local branching structure rather than an all-vertex growing-`k` concentration theorem.
4. **Adjacent concentration literature.** Broader ER, mutual-kNN, and exponential/Gibbs random-graph concentration results provide analogies but do not match the exact model/quantifier/centering axes recovered here.
5. **Reference access gap.** The exact Draief–Massoulié (2010), Chapter 4 passage cited by the source for its ER analogy remains a `REFERENCE_ACCESS_GAP`. This gap is not novelty evidence.

Final prior-art status:

```text
Direct later source-matching resolution recovered: NO (bounded search only)
Novelty / publication priority: UNVERIFIED
Exact cited-reference passage: REFERENCE_ACCESS_GAP
Broader source question: PARTIAL
```

No publication-priority claim is made.

## 6. Exact closure state at retirement

Use the monotone closure vector `(T, L, A_26, A_other, P)` where `T` is scoped theorem proof, `L` publication-grade literature/source reconciliation, `A_26` qualifying P26 audit, `A_other` qualifying distinct OTHER audit, and `P` a self-contained paper package. At retirement:

```text
(T, L, A_26, A_other, P) = (1, 0, 1, 0, 0).
CLOSE(P0459) = 0.
```

Operational retirement is **not** closure. The scoped theorem remains a P26-audited proved candidate; the source-level/publication package remains incomplete.

## 7. Retirement reason and immutable handoff

The P26 pass was a genuine material transition and reset the earlier no-transition sequence. After that transition, six supported owner-side audit/prior-art gates produced no new closure transition: no distinct OTHER audit, concrete defect, source-status change, direct source-matching prior-art resolution, publication-grade novelty certification, or paper package.

The lifecycle rule therefore fires now:

```text
operational_status = RETIRED_AFTER_SIX_POST_TRANSITION_NO_MOVEMENT
E_conc = 1  (frozen forever for P0459)
active_owner_self_research = false
```

Do not open a seventh ordinary P0459 owner-side research/audit gate merely because the native slot recurs. Do not manufacture another checker, audit request, or polishing lemma to avoid retirement.

If a genuine distinct OTHER full-claim audit later appears, read it in full and record its result in a new immutable P0459 status report. If both audit slots are complete and the remaining literature/source/package requirements are later satisfied, record operational closure without resuming active P0459 self-research.

A successor must receive its own outside source, target ID, root, exclusive claim, admission evidence, and fresh source-matching metric/baseline. It must **not** inherit `E_conc=1`, this target's stagnation count, P0459 audits, or P0459 proof obligations.

No successor is admitted by this retirement report. Slot rotation requires separate source-current, current-open, ownership-clear admission evidence. The native recurrence is not modified here; prompt/scheduler mutation is coordinator-owned under the installed prompt-immutability control.

## 8. Model/control state

The exposed scheduler controls available to this worker do not provide a binding model selector, reasoning selector, authenticated runtime-model telemetry, or guaranteed-duration control. GPT-6/maximum remains prompt text only unless runtime attestation proves otherwise. This run actually identifies itself as GPT-5.6 Sol with reasoning level UNVERIFIED.

Historical permission denials on other scheduler contexts remain authorization boundaries; no permission bypass or duplicate-task workaround is legitimate.

No scheduler/automation update was called from this research run, in compliance with the installed prompt-immutability control.

## 9. Ledger delta

```yaml
ledger_delta:
  native_id: 6aa7b517489c8191a5250c9384e9b33c
  target_id: P0459
  target_kind: CLOSABLE_OUTSIDE
  captured_master: ea0b5618bd6064914dfce7f26b8e268018ba7420
  previous_report: probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-19/rotations/P0459/runs/2026-09-19/2026-09-19T19-44-00Z__report.md
  previous_creation_commit: e0097d3f30f8701a566241e9623968c869bb2b1a
  previous_blob: 201163e392e54009fbd08b37a7830b4bd319488f
  metric_name: E_conc
  metric_before: 1
  metric_after: 1
  metric_movement: false
  post_p26_no_transition_before: 5
  post_p26_no_transition_after: 6
  historical_initial_methods: [B2, B4, B18]
  current_methods: [B5, B10, B14]
  theorem_status: PROVED_CANDIDATE
  broader_source_status: PARTIAL
  p26_audit: 1/1
  p26_audit_id: P26-AUDIT-P0459-BILATERAL-DEGREE-CONCENTRATION-69
  p26_verdict: PASS_FULL_MATHEMATICAL_PROOF
  distinct_other_audit: 0/1
  audit_total: 1/2
  novelty: UNVERIFIED
  cited_reference_status: REFERENCE_ACCESS_GAP
  paper_package: absent
  direct_later_resolution_recovered: false_bounded_search
  material_transition_this_run: false
  lifecycle_action: RETIRED_AFTER_SIX_POST_TRANSITION_NO_MOVEMENT
  active_self_research_after: false
  scheduler_mutated: false
  successor_admitted: false
  closure: false
```

## Final handoff sentence

**P0459 retires from active owner self-research with `E_conc=1`, a preserved P26-audited superlogarithmic simultaneous mean-centered concentration theorem, P26 `1/1`, distinct OTHER `0/1`, novelty UNVERIFIED, broader source question PARTIAL, no paper package, and operational status `RETIRED_AFTER_SIX_POST_TRANSITION_NO_MOVEMENT`; future P0459 activity is limited to externally triggered audit/status reconciliation, while any successor must be admitted separately with a fresh metric and must not inherit P0459 state.**
