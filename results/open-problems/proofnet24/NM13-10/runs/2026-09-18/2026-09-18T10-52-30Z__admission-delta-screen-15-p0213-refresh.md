Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; Section-B methods #2/#11/#30 were NOT ATTEMPTED because no source crossed admission.**

# NM13-10 — admission delta screen 15: POSTED delta and P0213 refresh

Date: 2026-09-18 UTC  
Track / namespace: `NM13-10` / `proofnet24/NM13-10/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Exclusive selection shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 9`

## 1. Runtime, controls, and authoritative continuity

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, hour-long execution, or a support escalation.

The exposed task-control surface still provides task identity, title/prompt, schedule or relative-start fields, timing mode, and enabled state, but **no bindable model-family selector and no bindable reasoning-effort selector**. GPT-6/maximum therefore remains prompt text only. Making it enforceable would require an owner-authorized product/workspace/API/admin scheduler surface exposing persistent model-family and reasoning-effort controls together with authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` result remains an authorization-context boundary; repository policy records a later successful P26 update from another authorized context. The lawful workaround is the owning/otherwise-authorized scheduler context or an authorized platform/admin/support path for that same task, never duplication or permission bypass. This invocation did not create, edit, disable, duplicate, or probe any schedule.

This run continues from the newest immutable NM13-10 report:

`proofnet24/NM13-10/runs/2026-09-18/2026-09-18T09-53-00Z__admission-delta-screen-14-p0063-claimed.md`,

creation commit `f1c6621be7f21f6f5992232087ed0eb931222bea`, readback blob `b4bb54ae126fa642dcbe390fad6932163b95d915`.

That report preserved the completed static residue-9 screen through the archived Codex frontier P0488, recorded P0063 as newly ownership-blocked by HARD10-01, and installed a strict delta-only admission cursor. No source-specific research counter is running while admission is pending.

Before deciding admission I reread or targeted-recovered the required current state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the newest own report above;
- newest neighboring NM13-09 report `2026-09-18T10-45-30Z__post-p0245-admission-delta-screen-4.md`;
- newest neighboring NM13-11 report `2026-09-18T09-52-33Z__e0082-stuck-recovery-2-argmin-threshold.md`;
- the changed canonical claims and the newly added P04 six-run handoff;
- P0213's canonical identity, intake/source row, prior-attempt record, exact claim-path absence, and current public source/status check.

Large append-only JSONL source/attempt ledgers and root files can be connector-truncated if rendered wholesale. I therefore used the predecessor's already completed canonical residue-9 cursor plus an exact commit-range comparison and exact candidate-specific searches, rather than pretending a truncated aggregate display was a fresh byte-for-byte reread of every historical row. This preserves continuity rather than resetting it.

Pre-write `master` head: `ec26f17e86517145a37e7712e0026ece4f6d8fc7` (2026-09-18T10:51:41Z).

## 2. Exact repository delta since screen 14

The exact comparison

`f1c6621be7f21f6f5992232087ed0eb931222bea .. ec26f17e86517145a37e7712e0026ece4f6d8fc7`

is **118 commits ahead and 0 behind**.

The decisive source-selection surfaces in that delta are:

- `QUEUE.md`: unchanged;
- `RESULTS.md`: unchanged;
- `probability_campaign_2026_09/INDEX.md`: unchanged;
- `probability_campaign_2026_09/RANKING.md`: unchanged;
- all previously screened `probability_1000_intake_*/problems.jsonl` source ledgers: unchanged;
- archived Codex source ledger through P0488: unchanged;
- controlling owner/NM13 policy files: unchanged;
- `POSTED.md`: **changed**, but only by strengthening exclusion/posting documentation, not by releasing an open source.

The current `POSTED.md` adds dated ResearchGate posting confirmation for Aldous--Fill 4.49(ii), a private-repository full-text reading catalogue for displayed ResearchGate papers, and Bradley Question 5 manuscript availability. These are exclusion/documentation updates. They do not create a free residue-9 source or reverse any current ownership exclusion.

Canonical ownership changes in the delta are additions, not releases:

- `operations/claims/C0021.md` — active P13 CLOSABLE claim;
- `operations/claims/D0039.md` — active R14 HARD claim;
- `operations/claims/I0006.md` — active R7-06 HARD claim.

No canonical claim deletion and no explicit owner-authorized **non-exhausted** release/reassignment creates residue-9 inventory. The new P04 report is a mandatory six-run I0101 handoff/rotation, but it expressly says `operations/claims/I0101.md` remains in place and is not released; its successor state is an admission hold. It therefore cannot be treated as free inventory under another ID.

The newly added NM13-08 report concerns its own P0093/QSO source and does not create a residue-9 release. NM13-09 remains successor-admission pending. NM13-11 remains on its exclusively claimed E0082 hard target and has used its second/final stuck recovery; no E0082 release is recorded in this delta.

## 3. Fresh retained residue-9 lead: P0213 / Bacon-and-eggs batch scheduling

With P0063 now canonically owned elsewhere, I refreshed the strongest still-unclaimed residue-9 source from the completed raw-Codex screen that has an explicit constant in the source question rather than rerunning the entire static inventory.

Canonical row:

- ID: `P0213`;
- canonical dedup key: `constant-factor_online_scheduling_with_subadditive_batch_durations`;
- SHA-256: `9781b1c074b5af5af3282a880371a755e16752f680c40ecd124322499809126f`;
- residue: `9 mod 13`;
- source: David Aldous's author-maintained open-problem page, **“Bacon and eggs: task scheduling into batches”**, problem posted March 2009.

The source model is exact: tasks arrive as a rate-1 Poisson process, task types are uniform on `[0,1]`, batch service time `S(B)` is monotone and strictly subadditive on disjoint batches, a task of type `a` incurs holding cost rate `c(a)`, `W` is long-run average waiting cost for an online algorithm, and `W_*` is the optimum over online algorithms under the assumption `W_*<infinity`. The source asks whether there exists an explicit algorithm, allowed to depend on `S` and `c`, and a **universal constant `C`** such that

`W / W_* < C`

for every admissible `S,c`. The live page also says that in the special `c=1` context, greedy “put everything in one batch” has finite `W` whenever any algorithm does.

Public source checked 2026-09-18:

`https://www.stat.berkeley.edu/~aldous/Research/OP/bacon.html`

The current Aldous open-problems index still lists “Bacon and eggs: task scheduling into batches” as an active problem:

`https://www.stat.berkeley.edu/~aldous/Research/OP/index.html`

Fresh bounded queries on 2026-09-18 included the exact title, `constant-factor online scheduling subadditive batch durations`, and the source ratio notation `W/W_*`. They recovered the maintained source and unrelated scheduling literature, but no later primary paper stating a complete resolution of this exact universal-competitive-ratio problem. This is **bounded negative evidence only**, not proof of worldwide openness or publication novelty.

### Prior attempts and ownership

The repository's old P0213 attempt is explicitly only a structural obstruction to a naive greedy step: it constructs a fixed two-job queue where greedy batching can be arbitrarily poor when holding costs differ. The archived note itself says the missing step is embedding that bad queue event into a stable Poisson-arrival system while controlling its frequency and other arrivals. It is **not** a steady-state counterexample to the source problem and it does not refute existence of another universal-competitive algorithm.

Current exact ownership search finds no `operations/claims/P0213.md`; a direct fetch at current `master` returns `404 Not Found`. Repository-wide canonical-key search recovers the intake/catalogue, old attempt summary, and NM13-10's earlier screen, but no current exclusive owner or release-conflict claim.

### Admission disposition

Despite being source-live-looking, currently unclaimed in the recovered state, and correctly in residue 9, **P0213 still does not cross the NM13-10 CLOSABLE admission gate**.

The reason is not merely difficulty. The exact surviving source obligation is to design one algorithm with a universal competitive factor over the full infinite-dimensional class of monotone strictly subadditive service-time functions and holding-cost functions. No finite source clause, fixed proposed sharp constant, exact finite witness, or short analytic endpoint is supplied by the source. The prior two-job obstruction attacks one candidate policy only. Treating that as an “explicit counterexample” to the source would be the same error the owner directive forbids: falsifying a stronger/invented algorithmic statement is not refuting the source.

A future admission would require a material source-faithful reduction, for example a theorem that the full problem is equivalent to a finite/extremal subclass with a frozen competitive constant, or an actual source-level impossibility family against **every** online algorithm. Neither was recovered here. Therefore P0213 remains **PENDING / OPEN-LOOKING / UNCLAIMED-BUT-NOT-READY**, not an admitted assignment.

## 4. Admission decision

**Decision: `ADMISSION_PENDING`. No canonical claim was created.**

No candidate in the material delta passes all gates simultaneously:

`canonical residue 9 + exact source + current literature status + prior-attempt recovery + exclusive unassigned ownership + non-retired/non-exhausted status + honest CLOSABLE finite/sharp-constant/counterexample/short-theorem endpoint`.

Therefore:

- source ID: `NONE`;
- canonical dedup key: `NONE`;
- claim ID/path: `NONE`;
- successor metric before: `UNMEASURED`;
- successor metric after: `UNMEASURED`;
- mathematical movement: none;
- source-specific unchanged-run counter: not started;
- source-specific stuck-recovery counter: not started;
- P26 audit: not applicable without an admitted claim;
- NM13-11 audit: not applicable without an admitted claim.

The prescribed first mathematical methods remain genuinely unspent:

- #2 **ATTACK THE NEGATION FIRST** — not attempted on an admitted target;
- #11 **DUALIZE** — not attempted on an admitted target;
- #30 **DO ONE PRIME / SCALE / DIRECTION AT A TIME** — not attempted on an admitted target.

Hashing, changed-path inspection, ownership checks, attempt recovery, and bounded source/literature screening are admission bookkeeping, not mathematical progress. No checker, theorem artifact, certificate, paper folder, audit request, or invented baseline was manufactured.

P0063 remains ownership-blocked by HARD10-01. P0213 remains unclaimed but fails the honest-CLOSABLE shape gate. Neither state authorizes an alias claim.

## 5. Durable screening cursor

Keep NM13-10 on **strict delta-only residue-9 admission**. Do not rerun the already completed static C/D/E/F/G/H/I plus Codex P0001--P0488 catalogue absent a material trigger.

Re-enter the full gate only if one of the following occurs:

1. a genuinely new or materially changed canonical source row appears in `QUEUE.md` or a `probability_1000_intake_*/problems.jsonl` source ledger;
2. a genuinely populated later Codex `P0489+` row appears;
3. an explicit immutable owner-authorized **non-exhausted** release/reassignment creates genuinely free residue-9 inventory;
4. a material source-status correction or source-faithful finite reduction changes a previously screened residue-9 lead's CLOSABLE disposition.

For P0213 specifically, wake the gate only if later primary work/source clarification produces a finite/extremal reduction, a fixed source-relevant competitive-factor milestone, or an actual source-level impossibility route—not merely another counterexample to one heuristic policy.

For the first candidate that really crosses admission: recover canonical aliases before hashing; check original source, current primary/later-author/citing literature, all prior attempts, current and historical claims/assignments/handoffs, POSTED and campaign exclusions; create `operations/claims/<ID>.md` create-only and read it back; freeze the exact source normalization at `UNMEASURED` unless actually measured; then immediately spend the substantive research portion on #2/#11/#30 in the same invocation.

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
    previous_report_commit: f1c6621be7f21f6f5992232087ed0eb931222bea
    prewrite_master_head: ec26f17e86517145a37e7712e0026ece4f6d8fc7
    commits_ahead: 118
    commits_behind: 0
  source_surface_delta:
    queue_changed: false
    results_changed: false
    campaign_index_changed: false
    campaign_ranking_changed: false
    intake_problems_changed: false
    codex_source_ledger_changed: false
    posted_changed: true
    posted_change_creates_release: false
    owner_policy_changed: false
  ownership_delta:
    claims_added: [C0021, D0039, I0006]
    claim_deletion_found: false
    non_exhausted_release_found: false
    conflict_overwritten: false
  retained_lead_refresh:
    source_id: P0213
    canonical_key: constant-factor_online_scheduling_with_subadditive_batch_durations
    canonical_sha256: 9781b1c074b5af5af3282a880371a755e16752f680c40ecd124322499809126f
    residue: 9
    claim_file_current: ABSENT
    source_status: OPEN_LOOKING_ON_CURRENT_AUTHOR_PAGE
    bounded_literature_result: NO_SOURCE_MATCHING_COMPLETE_RESOLUTION_SURFACED_2026_09_18
    prior_attempt_scope: GREEDY_POLICY_OBSTRUCTION_ONLY
    admission_disposition: REJECT_HONEST_CLOSABLE_GATE
    caveat: bounded_negative_search_is_not_worldwide_openness_or_novelty
  preserved_blocked_lead:
    source_id: P0063
    disposition: OWNERSHIP_BLOCKED_BY_HARD10_01
  artifacts_created: []
  next_step: strict_delta_only_residue_9_admission
```

## 7. Write discipline

This invocation creates exactly this one immutable own-namespace run report. No canonical claim, shared root, peer namespace, source/attempt ledger, checker, theorem artifact, workflow, permission, public surface, email/Drive item, paid-compute resource, or schedule is modified. Read back this report at its creation commit; do not create a receipt-only follow-up commit.
