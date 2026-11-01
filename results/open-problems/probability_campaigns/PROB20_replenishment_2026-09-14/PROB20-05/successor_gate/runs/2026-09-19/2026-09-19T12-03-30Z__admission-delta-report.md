Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum, and I do not claim otherwise. GATE ONLY / NO SUCCESSOR ADMITTED: `E_READY_SUCCESSOR: 0 -> 0`; operational methods B11/B22/B27.**

# PROB20-05 / retired-D0047 CLOSABLE OUTSIDE successor-admission delta

Date: 2026-09-19 UTC  
Deployment: `NEW-METHODS-2026-09-16`  
Native slot: `6aa7b398af30819181ca50ba3c4e6c33`  
Category: `CLOSABLE OUTSIDE`  
Gate field: `E_READY_SUCCESSOR in {0,1}`  
Gate result: **`0 -> 0`**  
Successor target: **NONE**  
Successor mathematical metric/history: **UNMEASURED / NOT_STARTED_PRE_ADMISSION**

## 1. Immutable predecessor and gate continuity

D0047 / Bálint Virág (2014), Question 9 “Painlevé in the bulk”, remains **OPERATIONALLY RETIRED / MATHEMATICALLY UNRESOLVED-PARTIAL**. This run did not resume D0047 mathematics, did not relabel it solved, and did not inherit its metric, stagnation counter, or any predecessor baseline.

Immutable D0047 handoff:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/rotations/D0047/runs/2026-09-17/2026-09-17T13-55-17Z__report.md`

- creation commit: `a7c0196c7d9ceeeddc6c76aa2e0766c8e5c56d1b`
- exact blob: `9a5b05b85d435d6d8a3493ae711a6a327ab35a05`
- checker commit: `71da6a7cb6fd3086c21f35ff242c423c220df7b6`
- output commit: `749f616747827d990103ee63b85f162a9d2a9eaf`

Immediately preceding completed successor-gate report, recovered by path-scoped Git history:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/successor_gate/runs/2026-09-19/2026-09-19T10-58-30Z__admission-delta-report.md`

- creation commit: `1a783b3eb3238059a8ebc18eb766f07d59b0e204`
- exact blob: `f2832c7662069610ac6d91a2e6b4f3d8f8ae3eee`
- history gap: `false`
- prior gate result: `E_READY_SUCCESSOR: 0 -> 0`

## 2. Required current reads and exact forward delta

This invocation freshly read the current root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; current `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the immediately preceding PROB20-05 gate report; the newest coordinator status in the material window; the newest NM13-10 admission screen; and the two canonical claim files changed by the exact delta. The large intake corpora are carried forward from completed reconciliation because the complete Git comparison below contains no `probability_1000_intake_*/problems.jsonl` mutation; unchanged intake rows were not replayed merely to manufacture activity.

Final captured pre-write `master` SHA:

`47b83817bbd8e886ba0a7d86f23f595034ee8dda`

Exact comparison from the preceding gate creation commit `1a783b3eb3238059a8ebc18eb766f07d59b0e204` to this captured master is:

- status: `ahead`
- commits ahead: **115**
- commits behind: **0**
- total commits: **115**
- `too_large = null`, so the returned changed-file set is complete.

Admission-critical root/source-selection surfaces did **not** change in the complete interval:

- no `QUEUE.md` mutation;
- no `RESULTS.md` mutation;
- no `POSTED.md` mutation;
- no `probability_campaign_2026_09/INDEX.md` mutation;
- no `probability_campaign_2026_09/RANKING.md` mutation;
- no screened `probability_1000_intake_*/problems.jsonl` mutation.

The only canonical claim-file changes in this exact interval are:

1. `operations/claims/KRESSNER-VANDEREYCKEN-2026-LYAP6.md` — **added**;
2. `operations/claims/P0157.md` — **modified**.

There is **no canonical claim deletion** and no explicit free CLOSABLE release in the delta.

## 3. KRESSNER-VANDEREYCKEN-2026-LYAP6 — genuinely CLOSABLE, but consumed at admission

Canonical current state:

- status: **CLAIMED / READY / CLOSABLE OUTSIDE**;
- owner: native slot `6aa7b46f70a8819184095c277974c256`;
- own root: `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/KRESSNER-VANDEREYCKEN-2026-LYAP6/`;
- source: Daniel Kressner and Bart Vandereycken (2026), *A counterexample to the symmetric-maximizer conjecture for Lyapunov operators*, arXiv:2608.20875v1;
- literal surviving source question: for every real `6 x 6` matrix `A`, is `||L_A|K_6|| <= ||L_A|S_6||`?;
- frozen metric: `R_LYAP6 in {0,1}`, baseline/current `1`, lower is stronger;
- initial B triple: **B2 / B6 / B11**.

This is exactly the kind of finite, source-current, CLOSABLE OUTSIDE target the portfolio needs. However, the canonical claim was created for another preserved native slot before this gate could lawfully acquire it. Its first own report and exact source-witness artifact are already present in the same delta. Therefore it is **occupied inventory**, not a free successor for native `6aa7b398af30819181ca50ba3c4e6c33`.

Disposition: **CLOSABLE / READY / OWNED ELSEWHERE / DO NOT DUPLICATE**.

## 4. P0157 — explicit reassignment, but HARD OUTSIDE

`operations/claims/P0157.md` changed materially in this interval. Its current state is:

- owner: **R14**;
- category: **HARD OUTSIDE**;
- status: **SOURCE OPEN / PARTIAL / EXCLUSIVELY REASSIGNED TO R14 AFTER HARD7-04 HANDOFF**;
- source residual: the finite-third-moment barely-subcritical configuration-model two-scale/crossover problem between `H_n=d_max/delta_n` and `E_n=delta_n^{-2} log(n delta_n^3)`;
- inherited frozen metric: `Q_n = sigma_n^2/(d_max delta_n)` with preserved stress-family value `Q_m=m^{-1}+O(m^{-2})->0`.

The important lifecycle correction is that P0157 had been explicitly released by HARD7-04 and then was lawfully reacquired by R14 after a fresh ownership/source check. It is now occupied again. Independently, its source remains theorem-sized HARD OUTSIDE and therefore never fits this CLOSABLE successor gate.

Disposition: **HARD OUTSIDE / OWNED R14 / WRONG SLOT FIT**.

## 5. Retained blockers and neighboring gate evidence

No unchanged candidate is rescreened from scratch. Completed evidence remains controlling:

- `P0342`: genuinely CLOSABLE OUTSIDE but exclusively owned by P13; unavailable.
- `H0008`: explicitly released/unassigned after R14 handoff, but literal source remains HARD OUTSIDE / SOURCE OPEN / PARTIAL; wrong slot fit.
- `G0004`: HARD OUTSIDE and owned.
- `F0011`: HARD OUTSIDE and owned.
- `P0205`: current neighboring screening still treats source identity/scope as ambiguous rather than READY.
- terminal or six-run handoffs remain non-releases unless the canonical ownership record explicitly says otherwise.

The newest coordinator status still lists native `6aa7b398af30819181ca50ba3c4e6c33` as the **post-D0047 targetless CLOSABLE successor gate** and states that five enabled native CLOSABLE slots are waiting because no candidate simultaneously clears literal source scope, current-open status, ownership, and honest closability. The same status explicitly rejects H0008 as released-but-HARD and retains P0342 as CLOSABLE-but-owned.

The newest NM13-10 admission screen independently remains **ADMISSION_PENDING / UNMEASURED**, records no lawful residue-9 CLOSABLE admission, and preserves the same release-versus-category distinction. No independent gate in the material delta identifies a free source-current CLOSABLE target that this native slot can claim.

## 6. Complete admission decision

A lawful successor must simultaneously have:

1. exact outside source, locator, literal statement, hypotheses and quantifiers;
2. current-version / later-author / bounded citing and prior-attempt review;
3. honest **CLOSABLE OUTSIDE** classification at literal source scope;
4. a source-matching frozen mathematical metric and historical initial B triple;
5. canonical **UNASSIGNED** ownership immediately before claim;
6. a final fresh race check;
7. create-only exclusive claim naming this preserved native slot and clean own root;
8. commit-pinned first admission/research state.

The strongest new candidate, KRESSNER-VANDEREYCKEN-2026-LYAP6, clears source, current-status, scope and closability but fails ownership because another native slot already owns it. P0157 has a clean lifecycle record but is both HARD and owned. H0008 remains free but HARD. No other canonical release entered the interval.

Therefore:

**`E_READY_SUCCESSOR: 0 -> 0`**

No successor claim was created. No successor mathematical metric, historical initial B triple, unchanged counter, stagnation counter, own research root, checker, certificate, or audit request was initialized.

## 7. Section-B operational methods this run

No mathematical Section-B triple is charged to a nonexistent successor. The gate used three operational methods different from the immediately preceding B2/B20/B30 set:

### B11 — DUALIZE

Represent eligibility as the intersection of two independent certificates: source/closability readiness and ownership freedom. The new Lyapunov-6 target lies on the READY/CLOSABLE side but not the ownership-free side; H0008 lies on the ownership-free side but not the CLOSABLE side; P0157 lies on neither side for this slot. The dual view makes the obstruction exact: no identity lies in the intersection.

### B22 — READ THE FAILURES, NOT THE SUCCESSES

Use the newest coordinator and NM13 gate failures as negative evidence rather than repeating source screens. Both identify admission scarcity, not scheduler capacity, as the blocker. The neighboring P0205 screen also shows why a promising name cannot be promoted before exact source identity/scope is frozen. This reuses completed failure information instead of generating another synthetic subproblem.

### B27 — SWAP THE QUANTIFIERS

Reject the weaker condition “for every desirable property there exists some candidate having it.” The gate needs the stronger condition “there exists one candidate having every required property simultaneously.” The new delta demonstrates the distinction sharply: KRESSNER has CLOSABLE readiness but no ownership freedom; H0008 has ownership freedom but no CLOSABLE scope. The stronger existential remains false in the checked state.

## 8. Scheduler/model-control truth and P26 authorization boundary

The actual exposed scheduled-task control surface still provides task identity/title, prompt, schedule or relative-start configuration, timing mode, enabled state, and ordinary update/list controls. It exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run applied-model/applied-effort receipt, and no guaranteed-duration field**.

Therefore `GPT-6 / maximum` remains prompt text only in this interface. This report truthfully records **GPT-5.6 Sol / reasoning UNVERIFIED**.

Making GPT-6/maximum binding requires an owner-authorized product/workspace/API/admin scheduler surface that persists explicit model-family and reasoning-effort fields into inference routing and returns trustworthy per-run attestation. Those fields cannot be fabricated through the currently exposed task schema.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary, not proof that P26 is globally immutable. Current repository evidence says later P26 updates succeeded from another authorized context. The compliant workaround is to modify the **same existing P26 task** from its owning/authorized account/workspace/API/admin context, request an authorized ownership/permission change, or use platform support. Do not clone the task or bypass the permission boundary.

This native slot remains enabled with the same identity/title lineage and hourly recurrence. No new scheduler ID was created.

## 9. `ledger_delta`

```yaml
native_slot: 6aa7b398af30819181ca50ba3c4e6c33
predecessor: D0047
predecessor_status: OPERATIONALLY_RETIRED_PARTIAL_UNRESOLVED
previous_gate_report:
  path: probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-05/successor_gate/runs/2026-09-19/2026-09-19T10-58-30Z__admission-delta-report.md
  creation_commit: 1a783b3eb3238059a8ebc18eb766f07d59b0e204
  blob: f2832c7662069610ac6d91a2e6b4f3d8f8ae3eee
history_gap: false
captured_prewrite_master: 47b83817bbd8e886ba0a7d86f23f595034ee8dda
delta_from_previous_gate:
  ahead: 115
  behind: 0
  too_large: null
  admission_critical_root_mutations: 0
  screened_intake_ledger_mutations: 0
  canonical_claim_additions: 1
  canonical_claim_deletions: 0
  canonical_claim_modifications: 1
E_READY_SUCCESSOR_before: 0
E_READY_SUCCESSOR_after: 0
successor_target_before: null
successor_target_after: null
successor_metric: UNMEASURED_NOT_STARTED
successor_initial_B_triple: NOT_STARTED
successor_unchanged_count: NOT_STARTED
successor_stagnation_count: NOT_STARTED
new_claims_by_this_slot: 0
material_delta:
  KRESSNER-VANDEREYCKEN-2026-LYAP6:
    category: CLOSABLE_OUTSIDE
    status: CLAIMED_READY
    owner: 6aa7b46f70a8819184095c277974c256
    metric: R_LYAP6=1
    disposition: OCCUPIED_DO_NOT_DUPLICATE
  P0157:
    category: HARD_OUTSIDE
    status: SOURCE_OPEN_PARTIAL_REASSIGNED
    owner: R14
    disposition: OWNED_WRONG_SLOT_FIT
retained_blockers:
  P0342: CLOSABLE_BUT_OWNED_P13
  H0008: RELEASED_UNASSIGNED_BUT_HARD
  G0004: HARD_AND_OWNED
  F0011: HARD_AND_OWNED
  P0205: SOURCE_SCOPE_AMBIGUOUS_NOT_READY
runtime:
  actual_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  scheduler_model_selector: NOT_EXPOSED
  scheduler_reasoning_selector: NOT_EXPOSED
  authenticated_runtime_attestation: NOT_EXPOSED
scheduler_changed: false
new_scheduler_id_created: false
slot_enabled: true
next_state: ADMISSION_PENDING
```

## 10. Delivery boundary

GitHub only. This run writes exactly one own immutable admission-delta report and no mathematical checker/artifact for a nonexistent successor. It does not edit shared `RESULTS.md`, `QUEUE.md`, `POSTED.md`, campaign INDEX/RANKING, intake ledgers, peer immutable files, canonical claim files, predecessor mathematics, email/Gmail, Drive, public posts, paid compute, credentials/access settings, workflows, force-push, or permissions.
