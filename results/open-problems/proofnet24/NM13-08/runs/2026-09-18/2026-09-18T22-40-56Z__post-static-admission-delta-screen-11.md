Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

# NM13-08 — post-static admission delta screen 11

**NO MATHEMATICAL MOVEMENT.** Status: **ADMISSION_PENDING**. Successor metric: `UNMEASURED -> UNMEASURED`. Section-B methods **#2 / #5 / #12 were NOT ATTEMPTED**: no successor source crossed admission, and admission screening is not counted as mathematical progress.

## Scope and ownership gate

- track: `NM13-08`
- namespace: `proofnet24/NM13-08/`
- category: `CLOSABLE OUTSIDE`
- required shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 7`
- admitted source: **NONE**
- canonical claim: **NONE**
- substantive artifact: **NONE**
- screening cursor entering this run: `STRICT_DELTA_ONLY_RESIDUE_7`

I did not create a claim because no candidate passed exact-source scope, current-literature status, prior-attempt history, shard, CLOSABLE-shape, and exclusive-ownership checks simultaneously.

## Continuity recovered before screening

Read/reconciled on `master` before any write:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- `QUEUE.md`, root `POSTED.md`, root `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- newest completed NM13-08 report `2026-09-18T21-46-00Z__post-static-admission-delta-screen-10.md`;
- newest completed neighboring reports for NM13-07 and NM13-09;
- current canonical claim additions and current task-health admission reconciliation;
- targeted source/attempt-index recovery for retained residue-7 near-lead `P0368`, including its historical campaign-attempt record.

The source/attempt corpora are append-only and large; I used targeted indexed recovery for the retained canonical identity and an exact predecessor-to-head changed-file comparison to detect any source/attempt-ledger delta. No source or attempt ledger path changed in this interval.

## Exact repository delta

Predecessor NM13-08 creation commit:

`afd3a32504ef987016add5a414a26ec04ab937f2`

Captured pre-write master head:

`2dc35f4e1534d8e7e5970360c39adafc8e95e10e`

Exact comparison:

- ahead: **84** commits;
- behind: **0** commits.

Admission-controlling surfaces with **no change** in that exact delta:

- `QUEUE.md`;
- `POSTED.md`;
- `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- the previously screened intake `problems.jsonl` / attempt-ledger paths;
- the archived canonical source catalogue used by this track;
- controlling NM13 owner-policy files.

One new canonical claim file appeared: `operations/claims/C0031.md`. It is already `ACTIVE`, owned by `HARD2-01`, category `HARD OUTSIDE`; it consumes inventory and is not a release.

The delta also contains terminal handoffs (including `F0003` and the R06 `NIELSEN-T4` handoff). Under the owner rules, exhaustion/terminal handoff is not permission to reopen a source and does not constitute an unclaimed CLOSABLE successor. No owner-authorized reassignment into NM13-08 appeared.

The latest task-health admission reconciliation likewise records no newly demonstrated free READY CLOSABLE successor. This is corroborating fleet state, not a substitute for NM13-08's own shard and ownership checks.

## Neighboring-track check

- **NM13-07** remains actively owned on `P0282`; its newest completed report keeps the target active. A later idea artifact is present, but no completed handoff/release appeared before the captured head.
- **NM13-09** remains `ADMISSION_PENDING` after its `P0245` handoff; no residue-7 source release is created by that state.

Neither neighbor supplies a lawful successor for NM13-08.

## Canonical retained residue-7 near-lead: P0368

Canonical identity retained and rechecked:

- source ID: `P0368`;
- title: *All bivariate frozen-percolation fixed points and their attraction domains*;
- canonical dedup key: `all_bivariate_frozen-percolation_fixed_points_and_their_attraction_domains`;
- SHA-256: `facec7fb99c46a0b0c2097e2102017f667b2668ba49bc809f61d7b47885fd5dd`;
- shard residue: **7**.

This identity is not an alias hash. Repository history also contains substantive prior P0368 work, so it is not represented as previously unattempted.

### Exact source scope

Primary source: Balázs Ráth, Jan M. Swart, Tamás Terpai, *Frozen percolation on the binary tree is nonendogenous* (Annals of Probability 49 (2021), 2272–2316; arXiv:1910.09213).

Immediately before Problem 7 the authors state that the bivariate RDE has precisely two **scale-invariant** fixed points, say they believe non-scale-invariant fixed points exist, and then ask:

> For frozen percolation on the oriented binary tree, find all fixed points of (1.38) and their domains of attraction.

Thus the literal source target is a **global fixed-point and basin classification**, not a finite coefficient check, bounded degree question, isolated zero-location statement, or short parameter inequality.

### Fresh bounded literature check — 2026-09-18 UTC

Queries/scope checked this run included:

1. `"Frozen percolation on the binary tree is nonendogenous" "Problem 7"`;
2. `"A phase transition between endogeny and nonendogeny" frozen percolation Ráth Swart Szőke`;
3. `"Frozen percolation on the binary tree: asymptotics and discrete approximations"`;
4. source-title / fixed-point / domains-of-attraction combinations surfaced by the same search.

Findings:

- the primary Ráth–Swart–Terpai text still poses Problem 7 exactly as the global classification above;
- Ráth–Swart–Szőke, *A phase transition between endogeny and nonendogeny* (arXiv:2103.14408; EJP 26 (2021), article 126), studies a structured family in which a parameter `theta` governs endogeny versus nonendogeny; it does **not** provide the all-fixed-points/all-domains-of-attraction classification asked in Problem 7;
- Tamás Terpai's later *Frozen percolation on the binary tree: asymptotics and discrete approximations* is an asymptotic/discretization follow-up, not a source-matching global solution surfaced by this bounded search.

No source-matching completion surfaced. This is **negative evidence only**, not proof of worldwide openness.

### Admission judgment

`P0368` remains **PENDING / NOT READY / HARD-shaped**. Relabeling a restricted proxy as the source problem would violate the CLOSABLE gate and the honest-label rule. It is therefore not admitted.

## Historical exclusions preserved

- `P0093` remains retired as **KNOWN VIA TRANSLATION**; it is not reopened.
- `P0408` remains at its mandatory six-unchanged-run CLOSABLE terminal handoff; exhaustion does not release it for silent reuse.
- posted/settled unimodality results remain excluded.
- no paused, posted, retired, exhausted, or another-track-owned source was reopened.

## Section-B methods

Reserved first post-admission methods remain:

- **#2 ATTACK THE NEGATION FIRST** — **NOT ATTEMPTED**;
- **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT** — **NOT ATTEMPTED**;
- **#12 FIND WHAT IS CONSERVED** — **NOT ATTEMPTED**.

Reason: no source was admitted. Screening a source is bookkeeping/admission work, not a mathematical attack on an admitted target.

## Metric and counters

- metric name after admission: exact source inequality plus one proved parameter interval / coefficient bound / degree cutoff;
- before: `UNMEASURED`;
- after: `UNMEASURED`;
- movement: **NO**;
- successor unchanged-run count: **NOT STARTED**;
- successor stuck/recovery count: **NOT STARTED**;
- admission screens are not mathematical unchanged runs.

## Model / scheduler control check

The exposed task-control surface still provides prompt/title, schedule/timing, enabled-state and ordinary update controls, but **no bindable model-family selector and no bindable reasoning-effort selector**. Therefore `GPT-6 / maximum` remains a prompt request only; it was not a binding runtime setting for this report.

To make that request enforceable would require an authorized scheduler/product/API/admin surface that exposes model-family and reasoning-effort fields, plus authenticated per-run runtime attestation. I did not claim or initiate a support escalation.

The historical P26 `You cannot modify this task` event remains an authorization-context boundary. Repository continuity records a later successful P26 update from another authorized context. The lawful workaround is to use the owning/authorized context (or an authorized platform/admin/API path); task duplication, permission bypass, or silent replacement is not a workaround.

## Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-08
  category: CLOSABLE OUTSIDE
  source_id: NONE
  claim_id: NONE
  status: ADMISSION_PENDING
  metric_name: post-admission exact-source interval/coefficient/degree metric
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  movement: NO
  methods_attempted: []
  methods_reserved_after_admission: [2, 5, 12]
  successor_unchanged_run_count: NOT_STARTED
  successor_recovery_count: NOT_STARTED
  screening_cursor_before: STRICT_DELTA_ONLY_RESIDUE_7
  screening_cursor_after: STRICT_DELTA_ONLY_RESIDUE_7
  predecessor_commit: afd3a32504ef987016add5a414a26ec04ab937f2
  prewrite_head: 2dc35f4e1534d8e7e5970360c39adafc8e95e10e
  delta_ahead: 84
  delta_behind: 0
  retained_near_lead: P0368
  literature_check_date_utc: 2026-09-18
  next_step: strict delta-only residue-7 admission; admit only after exact source, current literature, prior attempts, CLOSABLE shape, shard and exclusive ownership all pass
```

## Save discipline

This invocation creates exactly one immutable report in `proofnet24/NM13-08/runs/`. No canonical claim, checker/theorem artifact, shared root, peer namespace, workflow, permission, public surface, email/Drive resource, paid compute, or schedule is modified. Readback is performed at the creation commit; no receipt-only follow-up commit is permitted.
