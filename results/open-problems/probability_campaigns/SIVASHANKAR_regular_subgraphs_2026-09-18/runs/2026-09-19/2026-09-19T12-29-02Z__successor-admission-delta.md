Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. SUCCESSOR GATE NO MOVEMENT: E_READY_SUCCESSOR 0 -> 0. Screened exactly one materially changed candidate: P0157; outcome REJECT for this CLOSABLE gate because it is now exclusively reassigned to R14 and remains canonically HARD OUTSIDE.

# CLOSABLE OUTSIDE successor-admission delta — P0157 reassignment

- Native slot: `6aa7b53b0858819196d923203522c996`
- Gate target: CLOSABLE OUTSIDE successor admission only
- Captured master SHA before screening: `a2dd73bebc651e9f6393d757d6e78d01deee8d18`
- Gate metric before/after: `E_READY_SUCCESSOR: 0 -> 0`
- Predecessor continuity: `SIVASHANKAR-2026-REGSUB-EVEN` remains operationally retired and mathematically OPEN/PARTIAL. No predecessor metric, recovery state, or mathematical status is inherited.
- Previous gate report: `probability_campaigns/SIVASHANKAR_regular_subgraphs_2026-09-18/runs/2026-09-19/2026-09-19T11-32-07Z__successor-admission-delta.md`, creation commit `1f8bf21df0f372baeffb21ae721c0de0b03685e8`, readback blob `0b5dd95445f8a13754d8768cfb9e22c2bae08368`.

## Material Git delta screened

The one material candidate delta selected this run is `P0157`. This is a lawful rescreen despite its presence in the cumulative cursor because its canonical ownership state changed after the previous screen.

Current canonical claim `operations/claims/P0157.md` now states:

- Owner: **R14**.
- Category: **HARD OUTSIDE**.
- Current status: **SOURCE OPEN / PARTIAL / EXCLUSIVELY REASSIGNED TO R14 AFTER HARD7-04 HANDOFF**.
- R14 reassignment date: **2026-09-19 UTC**.
- The reassignment preserves the source residual and the inherited metric `Q_n := sigma_n^2/(d_max delta_n)` rather than resetting the work.

The fresh repository history independently records the reassignment, including commits titled `R14 claims released P0157 hard target` and `R14 claim P0157 and prove growing staircase obstruction`. The latest canonical file therefore supersedes this gate's earlier observation that P0157 was released/unassigned.

## Admission decision

**REJECT for this CLOSABLE OUTSIDE gate.** Two independent gate conditions fail:

1. **Ownership:** P0157 is no longer unassigned. It is exclusively owned by R14.
2. **Classification:** P0157 remains canonically **HARD OUTSIDE**, not CLOSABLE OUTSIDE.

No new source/current-status web search is repeated because this run is a pure material ownership/classification delta and the canonical claim already contains a dated 2026-09-19 source/current-status screen. Reusing that completed evidence is required by the no-churn instruction. Nothing in the ownership change justifies relabeling the source.

Therefore no successor claim, research root, fresh mathematical metric, handoff, or scheduler ID is created. `E_READY_SUCCESSOR` remains 0.

## Current cursor after this run

Do not rescreen absent another material change:

- `I0006`: actively owned by R7-06 at its screen.
- `GZ-DIMBM-EVEN-LOGCONCAVE`: released but canonically HARD OUTSIDE.
- `P0157`: **now exclusively reassigned to R14 and still HARD OUTSIDE**.
- `C0032`: terminal HARD handoff; no explicit release at its screen.
- `H0008`: released/unassigned but canonically HARD OUTSIDE / SOURCE OPEN / PARTIAL.

## Model/control truthfulness

The exposed scheduler interface still provides no binding model-family selector, reasoning-effort selector, authenticated completed-run model telemetry, or guaranteed-duration control. GPT-6/maximum is prompt-only absent authenticated runtime evidence. Historical permission denials remain authorization boundaries and are not bypassed.

## `ledger_delta`

```yaml
ledger_delta:
  native_task_id: 6aa7b53b0858819196d923203522c996
  target_id: CLOSABLE-OUTSIDE-SUCCESSOR-ADMISSION-GATE
  report_kind: successor_admission_delta
  input_snapshot_sha: a2dd73bebc651e9f6393d757d6e78d01deee8d18
  candidate_screened: P0157
  material_delta: released_unassigned_to_exclusively_reassigned_R14
  candidate_category: HARD_OUTSIDE
  candidate_owner: R14
  gate_metric_before: 0
  gate_metric_after: 0
  admission: REJECT
  blockers:
    - exclusive_ownership_R14
    - category_HARD_OUTSIDE_not_CLOSABLE
  predecessor_status: SIVASHANKAR_operationally_retired_mathematically_OPEN_PARTIAL
  successor_admitted: false
  new_claim_created: false
  new_scheduler_id_created: false
```
