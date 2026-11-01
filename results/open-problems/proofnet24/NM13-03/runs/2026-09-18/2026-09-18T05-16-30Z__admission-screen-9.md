Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: metric `UNMEASURED -> UNMEASURED`; Section-B methods #2/#6/#18 were NOT attempted because no source crossed admission.**

# NM13-03 — ninth admission screen (delta-only)

Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: `CLOSABLE OUTSIDE`  
Own namespace: `proofnet24/NM13-03/`  
Run date: 2026-09-18 UTC

## 1. Runtime, policy, and authoritative continuity

The requested `GPT-6 / maximum` setting remains prompt text only. The task-control interface exposed to this worker supports title/prompt, schedule or relative-start fields, enabled state, and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-effort telemetry**. This invocation therefore reports the model actually exposed to it, GPT-5.6 Sol, with reasoning level `UNVERIFIED`; it does not claim GPT-6 maximum. Enforcing GPT-6/maximum would require an authorized product/workspace/API/admin surface that exposes persistent model and reasoning controls together with authenticated per-run runtime attestation.

The historical P26 `You cannot modify this task` refusal remains an authorization/context boundary. `RESULTS.md` records that a later P26 update succeeded from another authorized context, so a future refusal is handled through the owning/authorized account/workspace/product/admin/API surface or platform support, not by duplicating the task or bypassing access controls. No support escalation is claimed here.

I continued from the immutable eighth screen:

`proofnet24/NM13-03/runs/2026-09-18/2026-09-18T04-18-00Z__admission-screen-8.md`,

creation commit `b4ec29d011ca7b71dc7b0121d2680ad124270f4b`.

Its authoritative state was:

- `ADMISSION_PENDING`;
- no canonical claim;
- no frozen mathematical source metric;
- no Section-B research method spent;
- residue-2 catalog screening exhausted through the then-current D/E/F/G/H/I/C inventories and Codex P0001-P0488;
- strict **delta-only** screening cursor for newly populated/materially changed rows, real source-status corrections, or legitimate non-exhausted ownership releases.

Before deciding this run I reread/recovered the controlling state from `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; this track's newest report; the newest visible neighboring NM13-02 and NM13-04 reports; current claims added since the preceding screen; the relevant P0018 intake/dedup/attempt history; and the current master delta. Aggregate files can be connector-truncated, so the previous immutable exhaustive screen remains continuity evidence and this run advances only the delta cursor rather than pretending a truncated rendering is a byte-for-byte reread of every historical row.

## 2. Repository delta since screen 8

At inspected master head `7e509586e6ff085d05fe0e418cc8547bd3486ce3`, master was **100 commits ahead** of screen 8's creation commit and not behind it.

The compare contains research reports, exact-check artifacts, handoffs, two new canonical claims, and operational task-health material, but **no modification** to the authoritative source-selection corpus:

- no change to root `QUEUE.md`;
- no change to root `POSTED.md`;
- no change to root `RESULTS.md`;
- no change to `probability_campaign_2026_09/INDEX.md` or `RANKING.md`;
- no change to any `probability_1000_intake_*/problems.jsonl` source ledger;
- no change to `probability_campaign_2026_09/codex_20h_20260906/problems.jsonl`;
- no populated P0489+ source row was created in this delta.

Therefore there is no new source row to hash merely because the fleet produced many new research commits.

### Ownership/lifecycle changes checked

The two new canonical claims in this delta are:

1. `F0106`, Michel Talagrand Conjecture 7.9, now exclusively claimed by R7-04 as a CLOSABLE OUTSIDE target;
2. `NEUNHAEUSERER-2026-ENTROPY`, Jörg Neunhäuserer Conjecture 3.1, now exclusively claimed by the PROB20-21 successor lane.

Both are ownership additions, not releases, and neither is selectable by NM13-03.

A newly visible R20 successor screen substantively probes `F0111`, Talagrand Problem 10.9, but does not claim it. The canonical intake identity is

`talagrand_small_2016::problem_10.9`,

whose SHA-256 is

`0081be3910bfaf3700a07feaf7fcd3e286b7cb3471fc6f84931ef8241f02f56f`

and whose residue is **11 mod 13**, so it is outside NM13-03's exclusive residue-2 shard irrespective of its eventual admission status.

The newest neighboring NM13-02 report is now its post-P0037 successor screen and is `ADMISSION_PENDING`; its mandatory P0037 handoff is not a release to this worker and P0037 belongs to residue 1 anyway. NM13-04 remains on its exclusive P0457 source and has not released a residue-2 target. No current/historical handoff inspected in this delta provides a non-exhausted residue-2 CLOSABLE source.

## 3. Strongest focus-fit residue-2 lead P0018 — fresh source/literature reconciliation

The canonical identity remains:

- source ID: `P0018`;
- source: Afonso S. Bandeira, Daniil Dmitriev, Kevin Lucca, Petar Nizić-Nikolac, and Almut Rödder, *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571;
- locator: Conjecture 31 / graph-matrix entry;
- source title in the repository: `Sharp polynomial-logarithmic expected norm of graph matrices`;
- canonical dedup key: `fixed_shape_rademacher_graph_matrix_sharp_polylog_norm`;
- SHA-256: `3175acae6a33f68af5255c6d0d2661108ffe372b1f3f55c9be584dfe4fffe512`;
- shard residue: `2 mod 13`;
- historical repository result state: `attempted_unsolved`, with no current canonical P0018 claim.

The source asks, for every fixed graph-matrix shape `alpha`, for shape-dependent exponents giving

`E ||M_alpha|| = Theta(n^{f(alpha)} (log n)^{g(alpha)})`.

A fresh 2026-09-18 primary-literature check again recovered:

Huibo Xu, Shi Fu, Youming Qiao, Dacheng Tao, **“Sharp Norms from Finite Structure: Graph Matrices and Structured Chaoses,” arXiv:2609.14266v1**, submitted 2026-09-13.

Its current arXiv abstract states that **for every fixed simple graph shape in the dense Rademacher model, including overlapping or empty matrix boundaries**, it proves

`E ||M_alpha|| = Theta_alpha(n^{(v+h-s)/2} (log n)^{a_*/2})`,

with both exponents given by finite structural parameters, and explicitly says the result closes the polylogarithmic gap in separator bounds. The current Randomstrasse manuscript records Conjecture 31 in the same fixed-shape polynomial/logarithmic form. In the bounded search performed this run I found no later correction, withdrawal, or narrower replacement of arXiv:2609.14266, and no citing paper that reopens the source statement.

I did **not** independently referee every proof line of arXiv:2609.14266 in this admission screen. Accordingly the precise disposition remains conservative:

`P0018 = CURRENT_PRIMARY_THEOREM_CLAIMS_SOURCE-MATCHING RESOLUTION / INADMISSIBLE FOR NEW OWNERSHIP PENDING FULL INDEPENDENT PROOF-SCOPE RECONCILIATION`.

That is sufficient to exclude P0018 from admission; it is not a unilateral shared-ledger declaration of fully audited KNOWN/PROVED status.

## 4. Reserve lead P0422 and other completed inventory

The retained residue-2 reserve `P0422` remains a previously attempted structural IPVT/group-action problem. No source, ownership, or literature delta converts it into the requested finite random-matrix inequality, exact moment, sharp spectral constant, explicit counterexample, or short analytic endpoint. It remains a non-READY reserve only.

The prior exhaustive screening of the remaining D/E/F/G/H/I/C and Codex inventories is not reopened absent a material change. In particular, newly written handoff prose is not permission to revive exhausted targets, disabled/inaccessible schedules do not release ownership, and newly created claims reduce rather than enlarge free inventory.

## 5. Admission decision

**Decision: `ADMISSION_PENDING`. No canonical claim was created.**

No candidate newly satisfies all gates simultaneously:

1. canonical source identity recovered before hashing and residue `2 mod 13`;
2. exact source statement presently unresolved in current primary literature;
3. no current/historical ownership, unreleased claim, exhausted handoff, retirement, posted settlement, or completed source package;
4. honest `CLOSABLE OUTSIDE` shape with a plausible finite counterexample/certificate, exact moment/norm/eigenvalue constant, or short theorem endpoint;
5. source-faithful metric can be frozen without inventing a baseline.

The mathematical metric therefore remains unfrozen:

- before: `UNMEASURED`;
- after: `UNMEASURED`.

There is **no mathematical movement**. This ninth screening report is not an unchanged mathematical run on an admitted target, so the post-admission stuck and six-run CLOSABLE rotation counters remain **not applicable**.

## 6. Section-B method accounting

The reserved first research methods remain exactly:

- #2 ATTACK THE NEGATION FIRST;
- #6 DEFORM TO A POINT YOU CAN SOLVE;
- #18 SAY IT IN ANOTHER LANGUAGE.

They were **not attempted** because no source crossed admission. Source screening, dedup recovery, ownership/lifecycle reconciliation, and literature exclusion checks are not mathematical method attempts.

No checker, theorem artifact, audit request, or paper package was created because there is no admitted mathematical claim worth certifying.

## 7. Durable cursor for the next invocation

Keep NM13-03 on a strict **delta-only admission cursor**:

- do not rerun the completed residue-2 D/E/F/G/H/I/C and Codex P0001-P0488 screens absent a material source/status/ownership change;
- inspect newly added or materially changed `QUEUE.md` / `probability_1000_intake_*/problems.jsonl` rows;
- inspect any genuinely populated P0489+ source row;
- inspect explicit immutable releases only when they are non-exhausted and source-valid; handoff/rotation after exhaustion is not an automatic release;
- re-open P0018 only if a later source/proof reconciliation demonstrates that arXiv:2609.14266 does **not** cover the exact Conjecture-31 class;
- retain P0422 only as reserve unless a genuinely finite/short source-valid reduction appears.

If a future residue-2 candidate passes every gate, create `operations/claims/<ID>.md` with create-only semantics, read it back immediately, freeze the exact source ensemble/hypotheses and one source-faithful norm/moment/eigenvalue metric, then begin methods #2/#6/#18 in that same invocation.

## 8. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-03
  category: CLOSABLE_OUTSIDE
  status: ADMISSION_PENDING
  source_id: null
  claim_id: null
  source_target: UNASSIGNED
  metric:
    name: UNFROZEN_UNTIL_ADMISSION
    before: UNMEASURED
    after: UNMEASURED
  mathematical_movement: false
  section_B_methods:
    attempted: []
    reserved_first_after_admission: [2, 6, 18]
  screening_run_count: 9
  unchanged_runs_since_admission: NOT_APPLICABLE_PRE_ADMISSION
  stuck_recovery_count: 0
  delta_since_previous_report:
    compare_base: b4ec29d011ca7b71dc7b0121d2680ad124270f4b
    inspected_head: 7e509586e6ff085d05fe0e418cc8547bd3486ce3
    commits_ahead: 100
    queue_changed: false
    posted_changed: false
    results_changed: false
    campaign_index_changed: false
    campaign_ranking_changed: false
    intake_problem_ledgers_changed: false
    codex_problem_ledger_changed: false
    populated_P0489_plus: false
    ownership_changes_reviewed:
      - F0106: R7-04_CLAIMED_CLOSABLE_NOT_AVAILABLE
      - NEUNHAEUSERER-2026-ENTROPY: PROB20-21_SUCCESSOR_CLAIMED_NOT_AVAILABLE
      - F0111: UNCLAIMED_SCREENING_LEAD_BUT_RESIDUE_11_NOT_2
    neighboring_tracks:
      - NM13-02: POST_P0037_ADMISSION_PENDING; P0037_HANDOFF_NOT_RELEASE
      - NM13-04: P0457_STILL_EXCLUSIVE
  status_alerts:
    - P0018: ARXIV_2609.14266v1_CURRENT_PRIMARY_THEOREM_CLAIMS_SOURCE_MATCHING_RESOLUTION; rechecked_2026-09-18; full_proof_not_independently_audited
  reserve_leads:
    - P0422: RESIDUE_2_BUT_PRIOR_ATTEMPTED_AND_NOT_SHORT_FINITE_READY
  next_cursor: "delta-only: new/materially changed queue/intake rows, populated P0489+, legitimate non-exhausted releases, or material source-status corrections after this report"
  audits:
    P26: NOT_REQUESTED_AS_AN_AUDIT
    NM13-04: NOT_REQUESTED
  shared_root_edits: NONE
  peer_edits: NONE
```

No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, external-script execution, peer-track edit, shared-root edit, or scheduler creation/modification was performed.

**End of complete run report.**