Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; Section-B methods #2/#11/#30 were NOT ATTEMPTED because no source crossed admission.**

# NM13-10 — admission delta screen 16

Date: 2026-09-18 UTC  
Track / namespace: `NM13-10` / `proofnet24/NM13-10/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Required selection shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 9`

## 1. Runtime disclosure, control surface, and continuity

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still provides title/prompt, schedule/start fields, timing mode, enabled state, and task identity, but **no bindable model-family selector and no bindable reasoning-effort selector**. GPT-6/maximum therefore remains prompt text only. Making it enforceable would require an owner-authorized product/workspace/API/admin scheduler surface exposing persistent model-family and reasoning-effort controls together with authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` result was an authorization-context boundary; current repository state records that a later P26 update succeeded from another authorized context. The lawful workaround is the owning/otherwise-authorized scheduler context or an authorized platform/admin/support path for that same task, never duplication or permission bypass. This invocation did not create, modify, disable, duplicate, or probe any schedule.

This run continues from the newest immutable own report:

`proofnet24/NM13-10/runs/2026-09-18/2026-09-18T10-52-30Z__admission-delta-screen-15-p0213-refresh.md`,

creation commit `0f39f179f2920571a519be8cfda84fa0da4858fc`.

That report preserved a completed static residue-9 canonical screen through archived Codex P0488, kept P0063 ownership-blocked by HARD10-01, and retained P0213 only as an open-looking but non-READY near-lead. Its durable rule was delta-only admission: do not pretend to redo the exhausted static catalog unless a source row/status, ownership release, later Codex row, or source-faithful finite reduction materially changes.

Before admission I reread or targeted-recovered the current required state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the newest own report;
- newest neighboring NM13-09 report `proofnet24/NM13-09/runs/2026-09-18/2026-09-18T11-43-27Z__post-p0245-admission-delta-screen-5.md`;
- newest neighboring NM13-11 report `proofnet24/NM13-11/runs/2026-09-18/2026-09-18T10-52-29Z__e0082-mandatory-handoff-successor-screen.md`;
- the current canonical-claim delta and direct P0213 claim path;
- the retained P0213 intake/history hits and fresh public source/literature checks below.

Large append-only JSONL ledgers are connector-bounded if rendered wholesale. I therefore preserved the predecessor's completed canonical source/attempt cursor and used an exact changed-file compare for the intervening delta, plus targeted source/attempt/claim recovery. I do not treat a truncated rendering, search miss, or stale `admitted=true` field as admission authority.

## 2. Exact repository delta: no source release or new residue-9 inventory

Immediately before this write, the observed master head was

`031b245cd49721142921139f6e1efd89cff76c14`

(commit time 2026-09-18T11:53:36Z).

The exact comparison

`0f39f179f2920571a519be8cfda84fa0da4858fc .. 031b245cd49721142921139f6e1efd89cff76c14`

was **86 commits ahead and 0 behind**.

Its changed-file list contains **no** modification to:

- root `QUEUE.md`;
- root `POSTED.md`;
- root `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- any previously screened `probability_1000_intake_*/problems.jsonl` source ledger;
- the archived Codex `problems.jsonl` through P0488;
- any probability-1000 attempt ledger;
- `FLEET_RULES.md`, `OWNER_DIRECTIVE.md`, `NEW_METHODS_2026-09-16.md`, or the NM13 deployment amendment;
- any pre-existing NM13-10 claim, because NM13-10 still has no admitted source claim.

The only `operations/claims/` path added in this 86-commit delta is create-only `operations/claims/P0087.md`, owned by R7-01 and classified HARD OUTSIDE. It explicitly says it does not release or replace another task. Thus it can only **shrink** free inventory; it does not create a residue-9 release.

The delta also contains terminal handoffs for other workers (including E0082, P0072, and F0106), but the controlling lifecycle rule is explicit: a handoff or disabled/inaccessible schedule does **not** self-release canonical ownership. No explicit owner-authorized non-exhausted residue-9 reassignment appeared.

The queue still distinguishes 60 listed sourced candidates from **zero newly certified READY entries**. No populated later Codex `P0489+` source row or materially changed residue-9 source row appears in the exact delta.

Direct fetch of `operations/claims/P0213.md` still returns 404. That confirms only that this particular canonical claim path is absent; by itself it is not enough for admission, so the historical assignments/attempts and source shape remain part of the gate.

## 3. Fresh 2026-09-18 source/literature refresh: P0213 remains PENDING, not READY

Retained lead:

- source ID: `P0213`;
- canonical dedup key: `constant-factor_online_scheduling_with_subadditive_batch_durations`;
- SHA-256: `9781b1c074b5af5af3282a880371a755e16752f680c40ecd124322499809126f`;
- shard: `9 mod 13`;
- source: David Aldous, **“Bacon and eggs: task scheduling into batches”**, maintained Berkeley open-problem page, problem posted March 2009.

I recomputed the hash from the canonical key rather than hashing the display title; it remains residue 9.

The maintained source page still poses the same universal question: tasks arrive at rate one; batch processing time is a monotone strictly subadditive function `S`; type-dependent holding costs are `c`; `W_*` is the optimum long-run waiting-cost rate over online algorithms; and the problem asks for an explicit online algorithm with a **universal constant-factor bound** `W/W_* < C` for all admissible `S,c`. The maintained Aldous open-problems index still lists “Bacon and eggs: task scheduling into batches” as an active item.

Dated 2026-09-18 bounded web queries included:

- exact title `"Bacon and eggs: task scheduling into batches"`;
- `"W/W_*" "Bacon and eggs" Aldous`;
- `"constant factor" online batching subadditive service function holding cost Aldous bacon eggs`;
- `"task scheduling into batches" subadditive online algorithm`;
- `Aldous "task scheduling into batches" algorithm`.

These searches recovered the maintained source and unrelated batching/scheduling approximation literature, but **no source-matching complete resolution** of Aldous's universal online problem surfaced. This is bounded negative evidence only; it is not a proof of worldwide openness or novelty, and I did not claim an exhaustive citation-database review.

Repository intake/history search still marks P0213 as previously attempted rather than genuinely unattempted. The preserved attempt-level lesson is narrow: a fixed two-job construction can make one natural greedy batching policy bad, but that does not produce a steady-state counterexample to the source's existence of *some* universal-competitive online algorithm. No new attempt-ledger row appeared in this run's exact Git delta.

**Admission decision for P0213 remains: PENDING / NOT READY.** The reason is source shape, not merely uncertainty about openness. The surviving obligation quantifies over an infinite-dimensional class of monotone strictly subadditive service functions and holding-cost functions and asks for existence of a universal online approximation algorithm. The source does not freeze a proposed numerical constant, finite witness size, or finite subclass whose complete resolution would answer a printed source clause. Admitting P0213 into this CLOSABLE lane would therefore relabel a broad algorithm-design problem as a short sharp-constant problem. I did not do that.

P0063 remains separately ownership-blocked by HARD10-01 and was not reopened under an alias.

## 4. Admission decision and method accounting

**Decision: `ADMISSION_PENDING`. No canonical claim was created.**

No candidate in the material delta passes all gates simultaneously:

`canonical residue 9 + exact source + present literature status + prior-attempt recovery + exclusive unassigned ownership + non-retired/non-exhausted state + honest CLOSABLE finite/counterexample/sharp-constant/short-theorem endpoint`.

Because no source crossed admission, there is no lawful successor baseline to freeze and no mathematical attack to count:

- source ID: `NONE`;
- canonical dedup key: `NONE`;
- claim ID/path: `NONE`;
- successor metric before: `UNMEASURED`;
- successor metric after: `UNMEASURED`;
- mathematical movement: none;
- successor unchanged-run counter: not started;
- successor stuck-recovery counter: not started;
- P26 audit: not applicable without a successor claim;
- NM13-11 audit: not applicable without a successor claim.

The prescribed first mathematical moves remain genuinely unspent:

- #2 **ATTACK THE NEGATION FIRST** — not attempted on an admitted successor;
- #11 **DUALIZE** — not attempted on an admitted successor;
- #30 **DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME** — not attempted on an admitted successor.

Canonical hashing, changed-path comparison, ownership reconciliation, source-status refresh, and bounded literature screening are admission bookkeeping, not mathematical progress.

## 5. Durable cursor / next step

Keep NM13-10 on **strict delta-only residue-9 admission**. Re-enter the full source gate only if at least one of the following occurs:

1. a genuinely new or materially changed canonical source row appears in `QUEUE.md` or a `probability_1000_intake_*/problems.jsonl` source ledger;
2. a genuinely populated later Codex `P0489+` row appears;
3. an explicit immutable owner-authorized **non-exhausted** release/reassignment creates genuinely free residue-9 inventory;
4. a material source-status correction supplies a precise source-faithful CLOSABLE endpoint for a retained residue-9 lead.

Otherwise do not rerun the completed static D/E/F/G/H/I plus Codex P0001--P0488 catalog. Continue to preserve posted/settled/retired exclusions and every other worker's claim/handoff.

For the first future candidate that actually crosses admission, recover canonical identity and aliases before hashing; verify the exact original statement, current primary/later-author/citing literature, prior attempts, all current/historical assignments/handoffs/claims, POSTED and campaign exclusions; create `operations/claims/<ID>.md` with create-only semantics and read it back; freeze the source metric at `UNMEASURED` unless genuinely recovered; and in that same invocation immediately spend the research portion on methods #2/#11/#30.

## 6. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-10
  category: CLOSABLE_OUTSIDE
  run_status: ADMISSION_PENDING
  source_id: null
  canonical_dedup_key: null
  claim_id: null
  claim_path: null
  shard_residue_required: 9
  metric:
    name: successor_metric
    before: UNMEASURED
    after: UNMEASURED
    moved: false
  mathematical_progress: false
  methods:
    attempted: []
    prescribed_unspent: [2, 11, 30]
  successor_counters:
    unchanged_runs: null
    stuck_recoveries: null
  audits:
    P26: NOT_APPLICABLE_NO_SUCCESSOR_CLAIM
    secondary_NM13_11: NOT_APPLICABLE_NO_SUCCESSOR_CLAIM
  continuity:
    previous_report: proofnet24/NM13-10/runs/2026-09-18/2026-09-18T10-52-30Z__admission-delta-screen-15-p0213-refresh.md
    previous_report_commit: 0f39f179f2920571a519be8cfda84fa0da4858fc
    prewrite_master_head: 031b245cd49721142921139f6e1efd89cff76c14
    commits_ahead: 86
    commits_behind: 0
    source_ledgers_changed: false
    attempt_ledgers_changed: false
    queue_changed: false
    posted_changed: false
    results_changed: false
    campaign_index_or_ranking_changed: false
  ownership_delta:
    new_claim_additions_observed: [P0087]
    claim_deletions_observed: []
    explicit_non_exhausted_residue9_release_found: false
    P0213_claim_path_exists: false
    conflict_overwritten: false
  retained_lead:
    source_id: P0213
    canonical_dedup_key: constant-factor_online_scheduling_with_subadditive_batch_durations
    sha256: 9781b1c074b5af5af3282a880371a755e16752f680c40ecd124322499809126f
    residue: 9
    disposition: PENDING_NOT_READY
    reason: broad_universal_online_algorithm_program_not_honest_closable_endpoint
  literature_check:
    date: 2026-09-18
    retained_lead: P0213
    exact_source_verified: true
    maintained_open_problem_index_still_lists_source: true
    bounded_result: no_source_matching_complete_resolution_found
    caveat: bounded_negative_search_not_worldwide_openness_or_novelty
  scheduler_control:
    model_selector: NOT_EXPOSED
    effort_selector: NOT_EXPOSED
    authenticated_runtime_telemetry: NOT_EXPOSED
    requested_prompt_model: GPT-6
    requested_prompt_reasoning: maximum
    actual_model_reported: GPT-5.6_Sol
    actual_reasoning: UNVERIFIED
  next_step: wait_for_material_residue9_admission_delta_then_run_full_gate
```

## 7. Scope / safeguards

No canonical claim, shared root, peer namespace, checker, theorem artifact, workflow, permission, public surface, email/Gmail item, Drive item, paid compute, or schedule was created or modified in this invocation. No disabled or handed-off target was treated as released. No source was called closed, proved, refuted, or known by this screening run.