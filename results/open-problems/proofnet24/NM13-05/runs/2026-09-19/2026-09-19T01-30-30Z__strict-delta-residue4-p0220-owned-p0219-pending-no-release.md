Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; Section-B methods #2 ATTACK THE NEGATION FIRST, #8 GO THE OTHER WAY AND DISCRETIZE, and #11 DUALIZE were NOT ATTEMPTED because no successor crossed admission.**

# NM13-05 strict-delta residue-4 admission — P0220 owned off-shard, P0219 pending off-shard

Date: 2026-09-19 UTC
Track: NM13-05
Category: CLOSABLE OUTSIDE
Namespace: `proofnet24/NM13-05/`
Selection shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 4`
Status: `ADMISSION_PENDING`
Durable cursor: `STRICT_DELTA_ONLY_RESIDUE4_ADMISSION`

## 1. Outcome

No genuinely free residue-4 CLOSABLE source crossed admission in this invocation. No canonical claim was created, no source metric was invented, and screening is not counted as mathematical progress. The already completed static canonical source screen was not restarted: this invocation inspected the strict repository delta, ownership/status changes, current source/campaign ledgers, neighboring reports, and fresh bounded literature only.

The only newly created canonical claim in the predecessor-to-prewrite delta is `P0220`, but its recovered canonical identity hashes to residue 6 and it is already owned by R7-04. A new report-level replenishment lead `P0219` hashes to residue 11 and is explicitly `NOT_READY`; it has no canonical claim. The fresh C0134 terminal handoff is residue 10 and does not release ownership. None is selectable by NM13-05.

## 2. Authoritative continuity recovered

At current `master` I read/reconciled the required control and fleet state, including:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md` and the current task-health owner reconciliation;
- `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the newest NM13-05 report and current neighboring NM13-04 / NM13-06 reports;
- current canonical claims, relevant historical assignment/handoff evidence, task-health admission state, and the source/attempt-ledger delta.

No controlling owner-policy file changed in the screened delta. No populated intake `problems.jsonl`, QUEUE, POSTED, RESULTS, campaign INDEX/RANKING, or attempt-ledger file changed in that delta either. Therefore there is no new canonical source identity or corrected dedup key requiring a static-corpus rescan.

C0146 continuity is preserved: it is terminally handed off after six unchanged runs, mathematically `REFUTED_NOT_FLEET_CLOSED`, and is not an admission candidate. A terminal handoff is not an ownership release.

## 3. Exact strict delta

Previous NM13-05 creation commit:

`d29e9ab553041ad69ca0f383a5e0720265dfeaea`

Frozen pre-write head after refresh:

`90a5e5f0bf438d6c84201d317cb7f8c9481bea2b`

GitHub compare result:

- status: `ahead`
- commits ahead: `104`
- commits behind: `0`
- total commits: `104`
- changed-file list returned completely (no `too_large` condition)

Selection-relevant path changes in that complete delta:

- added canonical claim: `operations/claims/P0220.md`;
- added R7-04 P0220 admission/research material;
- added R01 report-level P0219 replenishment lead;
- added R7-02 C0134 six-run handoff/report;
- added NM13 and task-health reports confirming admission reconciliation;
- **no** claim deletion or explicit ownership release;
- **no** `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign INDEX/RANKING, intake `problems.jsonl`, attempt-ledger, or owner-policy modification.

The coordinator's current bounded READY-CLOSABLE quantity remains `0 -> 0`.

## 4. Canonical identity, shard, and ownership reconciliation

### P0220 — reject: residue 6 and already owned

Source title: **Explicit stationary law of the leftmost Hammersley drift-jump particles**.

Canonical dedup key recovered from the R7-04 admission / NM13 reconciliation:

`explicit_stationary_law_of_the_leftmost_hammersley_drift-jump_particles`

SHA-256:

`06aa486153de472a20fa8c5040de6f9304f3989debc1e8f6c596655c3bf4d05c`

Residue:

`int(SHA256(key),16) mod 13 = 6`

Current canonical claim: `operations/claims/P0220.md`, owner R7-04, status `CLAIMED / ACTIVE`, category `CLOSABLE OUTSIDE`.

Decision: **not selectable**. It fails NM13-05's residue-4 shard and the exclusive-ownership gate. No alias or competing claim may be created.

The original Aldous source still asks for a fairly explicit description of the unique stationary distribution of the leftmost Hammersley drift-jump particle process. That source match does not override ownership or shard rules.

### P0219 — reject: residue 11 and pending, not READY

Source title: **A discrete Hammersley process as an extreme case of oriented percolation flows**.

Canonical dedup key recovered from current R01/NM13 reconciliation:

`high-density_oriented_percolation_flow_asymptotics`

SHA-256:

`77b9c00d0e9ccd64917689dc1ffb6ba9918efbf2d5975a913593b39da40ac3ea`

Residue:

`int(SHA256(key),16) mod 13 = 11`

Current state: report-level replenishment lead only; R01 explicitly labels it `OPEN_LOOKING_REPLENISHMENT_LEAD_NOT_READY`; no canonical claim exists.

Decision: **not selectable**. A pending lead is not READY, and in any case the canonical identity is residue 11, not residue 4. NM13-05 did not create a speculative claim.

### C0134 terminal handoff — reject: no release, residue 10

The fresh R7-02 six-run C0134 handoff is a worker-local terminal handoff, not an ownership release. Its canonical dedup key is `C0134`, which hashes to residue 10, and ownership remains with R7-02 absent an explicit owner-authorized release/reassignment.

Decision: **not selectable**.

### Previously screened residue-4 holdings

No release was found for the previously reconciled residue-4 claimed targets (including P0429, already R7-01-owned CLOSABLE OUTSIDE). A disabled schedule, terminal handoff, or local rotation is not release evidence.

## 5. Fresh bounded source/literature checks — 2026-09-19

These checks are deliberately bounded; a negative search is not proof of worldwide openness or novelty.

### P0220

Queries included the exact title `"A one-dimensional drift-jump particle process"`, stationary distribution, Aldous, Hammersley, and current-source lookup. The current Berkeley open-problem page is live and still states the problem: give a fairly explicit stationary distribution for the drift-jump particle process. The R7-04 admission additionally checked the cited Aldous/Diaconis and Plancherel-related literature and did not identify a source-level resolution. I did not interpret that bounded search as proof of openness; in any event P0220 is unavailable to this worker.

Source checked: `https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html`.

### P0219

Queries included the exact title `"A discrete Hammersley process as an extreme case of oriented percolation flows"`, `1-v(p)`, Hammersley, and oriented-percolation flow asymptotics. The live Aldous source states the conjecture

`1 - v(p) ~ sqrt(2(1-p))` as `p -> 1`

and explicitly identifies the interchange-of-limits step as the difficulty. No later source-level proof surfaced in this bounded check. That is not a worldwide-openness claim, and P0219 remains `NOT_READY` and off-shard.

Source checked: `https://www.stat.berkeley.edu/~aldous/Research/OP/hammersley_flow.html`.

### C0146 / neighboring q<1 random-cluster literature

Fresh searches for 2026 `q<1` random-cluster dependence again recovered Tang--Zhang (submitted 2026-09-10), whose abstract says even pairwise negative correlation remains open on arbitrary finite graphs while proving broad high-degree regular cases, and Park (submitted 2026-08-09), which treats wired trees. These are adjacent fixed-parameter negative-dependence questions, not an independent source-level audit of Pete Question 13.2 or a reason to reopen C0146.

No P26 or NM13-06 source-level C0146 PASS was recovered from the current repository search. Thus C0146 remains `REFUTED_NOT_FLEET_CLOSED` under the fleet closure standard.

Access/scope limits: public web/source pages and repository-accessible papers/reports were checked; private correspondence, paywalled material not exposed through accessible metadata/full text, and an exhaustive worldwide citation graph were not available. No novelty claim is made from these negative searches.

## 6. Model / scheduler control truth

The requested prompt line says GPT-6 with maximum reasoning, but this invocation actually ran on **GPT-5.6 Sol**, and the reasoning level exposed to this report is **UNVERIFIED**.

The currently exposed scheduled-task control surface still provides task identity, prompt/title, schedule/start, timing mode, and enabled state. It does **not** expose a bindable model-family selector or reasoning-effort selector. Therefore GPT-6 / maximum remains request text, not a setting I can bind or attest from this interface.

To make the requirement enforceable, an authorized product/workspace/API/admin surface would need to expose persistent model-family and reasoning-effort fields for the task, plus authenticated per-run runtime attestation. I cannot manufacture those controls from prompt text.

The historical P26 `"You cannot modify this task"` event is not treated as permission to clone or bypass access controls. Repository history records a later successful authorized-context prompt update. The lawful workaround is the owning/otherwise-authorized task context or authorized platform/admin support; this invocation made no schedule modification.

## 7. Metric, methods, counters, and next step

No target was admitted, so there is still no frozen successor marginal class or extremal coupling cost/feasibility threshold to measure.

- successor metric before: `UNMEASURED`
- successor metric after: `UNMEASURED`
- mathematical movement: `none`
- methods actually attempted: `[]`
- reserved first-run methods: `#2, #8, #11`
- successor unchanged-run counter: `NOT_STARTED`
- successor stuck-recovery counter: `NOT_STARTED`
- next cursor: `STRICT_DELTA_ONLY_RESIDUE4_ADMISSION`

The next invocation should inspect only material post-report changes to canonical source identity/dedup, ownership/release, READY status, QUEUE/campaign/POSTED state, or newly ingested source rows. It should not rescan the completed static corpus without such a delta. If a genuinely free residue-4 CLOSABLE candidate becomes READY, admission must perform exact-source, current-literature, prior-attempt, alias/dedup, and exclusive-ownership checks before create-only claim creation; then the first research run must continue substantively with #2/#8/#11.

## 8. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-05
  source_id: null
  claim_id: null
  status_before: ADMISSION_PENDING
  status_after: ADMISSION_PENDING
  metric_name: successor_frozen_metric
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  mathematical_progress: false
  methods_tried: []
  methods_reserved: [2, 8, 11]
  successor_unchanged_run_counter: NOT_STARTED
  successor_stuck_recovery_counter: NOT_STARTED
  predecessor_terminal_source: C0146
  c0146_math_status: REFUTED_NOT_FLEET_CLOSED
  p26_c0146_source_pass_recovered: false
  nm13_06_c0146_source_pass_recovered: false
  delta_base_commit: d29e9ab553041ad69ca0f383a5e0720265dfeaea
  delta_prewrite_head: 90a5e5f0bf438d6c84201d317cb7f8c9481bea2b
  commits_ahead: 104
  commits_behind: 0
  compare_too_large: false
  new_claims_screened: [P0220]
  p0220_dedup_key: explicit_stationary_law_of_the_leftmost_hammersley_drift-jump_particles
  p0220_residue_mod13: 6
  p0220_owner: R7-04
  pending_leads_screened: [P0219]
  p0219_dedup_key: high-density_oriented_percolation_flow_asymptotics
  p0219_residue_mod13: 11
  p0219_ready: false
  terminal_handoffs_screened: [C0134]
  c0134_residue_mod13: 10
  c0134_release_found: false
  ownership_releases_found: 0
  source_selection_root_changes: 0
  intake_jsonl_changes: 0
  attempt_ledger_changes: 0
  coordinator_ready_closable_before: 0
  coordinator_ready_closable_after: 0
  screening_cursor_before: STRICT_DELTA_ONLY_RESIDUE4_ADMISSION
  screening_cursor_after: STRICT_DELTA_ONLY_RESIDUE4_ADMISSION
  next_step: >-
    Inspect only material post-report source/dedup/ownership/READY deltas; admit only a genuinely free residue-4 CLOSABLE source after full gate checks, then freeze its source metric and execute first-run methods 2, 8, and 11.
```

## 9. Write set / safeguards

This invocation creates exactly this one immutable NM13-05 run report. It creates no claim and no substantive artifact because no successor passed admission. It does not edit shared roots, other tracks, source/attempt ledgers, D-series ownership, workflows, permissions, public surfaces, email/Gmail, Drive, paid compute, or schedules.
