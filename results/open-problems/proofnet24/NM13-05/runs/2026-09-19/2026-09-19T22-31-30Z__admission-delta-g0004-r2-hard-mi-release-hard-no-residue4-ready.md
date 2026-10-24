Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric remains `UNMEASURED -> UNMEASURED`; Section-B methods #2/#8/#11 remain genuinely NOT_TRIED_PRE_ADMISSION because no successor crossed admission.**

# NM13-05 — strict-delta admission: G0004 released but HARD/residue 2; maximal-intersection release is theorem-scale HARD; no residue-4 CLOSABLE successor

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-05` / `proofnet24/NM13-05/`  
Category: **CLOSABLE OUTSIDE**  
Exclusive shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 4`  
Status after this invocation: **ADMISSION_PENDING**

## 1. Authoritative continuity recovered

I continued from the newest immutable NM13-05 report rather than restarting:

`proofnet24/NM13-05/runs/2026-09-19/2026-09-19T21-28-00Z__admission-delta-e0011-reassigned-r6-no-residue4-ready.md`

creation commit `2ec2f6be653bc4955b465741609794ab051bb0ef`. Its frozen pre-write head was `d3870ecc1fd64a2af32077442eb1b603d2708e24`, and its durable cursor was

`LEGACY_P_RECONCILIATION_COMPLETE_THROUGH=P0488; NEXT=STRICT_DELTA_ONLY_RESIDUE4_ADMISSION`.

I reread/recovered the required controlling state for this run: `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`, root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the newest NM13-05 report, the newest visible neighboring NM13-04 and NM13-06 reports, current canonical claims, and admission-relevant source/attempt continuity. The append-only intake corpora are too large to claim every unchanged byte was freshly rerendered; instead, completed reconciliation is carried forward because the exact Git delta below is complete and contains no screened intake/attempt-ledger mutation.

The prompt requests GPT-6 with maximum reasoning. The exposed task surface still has no bindable model-family selector, no reasoning-effort selector, and no authenticated applied-runtime attestation. Runtime identity available here is GPT-5.6 Sol and reasoning telemetry is UNVERIFIED.

## 2. Exact predecessor-frozen-head to frozen-prewrite delta

Final pre-write master head after the race check:

`6f0059bbea21c375fd6db23d2ad835fa4c7b5a36`.

Exact comparison:

`d3870ecc1fd64a2af32077442eb1b603d2708e24 .. 6f0059bbea21c375fd6db23d2ad835fa4c7b5a36`

returns:

- status `ahead`;
- **131 commits ahead**;
- **0 behind**;
- `too_large = null`.

The complete changed-file set contains six canonical claim mutations:

1. `operations/claims/G0004.md` — explicit R17 release after HARD exhaustion;
2. `operations/claims/H0021.md` — reassigned active HARD ownership;
3. `operations/claims/MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS.md` — released HARD handoff after Section-I exhaustion;
4. `operations/claims/B-WEAK-EVEN-LOGCONCAVE.md` — released terminal HARD handoff;
5. `operations/claims/AK-KATZIN-C41-EQUALITY.md` — literal printed equality target recorded as refuted/resolved and released as a resolved target;
6. `operations/claims/LOG-BRUNN-MINKOWSKI-SYMMETRIC.md` — newly claimed by HARD7-01.

There is no canonical claim deletion. The same complete delta contains no mutation of root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, any screened `probability_1000_intake_*/problems.jsonl`, any relevant probability attempt ledger, or governing NM13/new-method policy. The two final commits in the race window add only HARD7-03 idea/checker material and do not change admission inventory.

## 3. G0004 is genuinely released, but fails both shard and category gates

Current canonical claim history for G0004 now says `Owner: UNASSIGNED AFTER R17 HANDOFF`, source OPEN/PARTIAL, released by R17 after both permitted HARD recoveries were exhausted.

Exact source: Lucas Flammant, *A conjecture implying theta(p_c)=0 for Bernoulli bond percolation on Z^d*, arXiv:2609.03492, Conjecture 2.2.

Authoritative canonical intake identity:

`flammant_finite_graph_2026::conjecture_2.2`.

Its SHA-256 is

`cfd780a5cdd49da5833b93d35f22b8593428c666840b2c9014bdf69f6da2ed75`,

hence

`int(hash,16) mod 13 = 2`.

Therefore G0004 is **off NM13-05's residue-4 shard**. Independently, its source asks a uniform theorem over arbitrary finite graphs strong enough to imply critical-percolation continuity; R17 and prior screening correctly classify it **HARD OUTSIDE**, not a finite obstruction/short extremal CLOSABLE source. It cannot be made eligible by carving out a convenient finite subcase.

Fresh bounded public search dated 2026-09-19 UTC recovered Flammant's September 2026 preprint as the current source, including its planar outer-face theorem with explicit `1-2 sqrt(epsilon)` bound. I did not locate a later primary source proving unrestricted Conjecture 2.2. A separate recent critical-percolation paper/search result concerns consequences/conditional routes for `theta(p_c)` rather than a source-matching proof of Flammant's finite-graph conjecture. This is bounded negative evidence, not a worldwide openness certificate.

## 4. Other new releases do not create lawful NM13-05 inventory

### Maximal-intersection ellipsoid uniqueness

The claim is now explicitly released after HARD7-01 Section-I exhaustion, but the exact source asks uniqueness of the maximal-intersection ellipsoid for every centrally symmetric convex body in general dimension at intermediate volume/radius. The preserved metric is `D_MI=2`, matching Jairo Bochi's planar theorem; the all-dimensional obligation remains theorem-scale.

Fresh bounded literature search recovered Bochi's peer-reviewed 2018 result stating that uniqueness is open in general and proving dimension two. No later indexed source-matching all-dimensional theorem was located in this run. The released claim supplies no authoritative NM13 intake/QUEUE canonical `dedup_key`; under the shard rule I therefore did **not** hash the paper title, arXiv number, claim filename, or another alias to manufacture residue eligibility. Independently, this is a HARD all-dimensional theorem target, not an honest finite/short CLOSABLE source.

### Weak (B), AK equality, log-Brunn-Minkowski, H0021

`B-WEAK-EVEN-LOGCONCAVE` is a terminal HARD release; no CLOSABLE relabeling is allowed. `AK-KATZIN-C41-EQUALITY` is released because the literal printed equality clause was already refuted/resolved; a resolved target is not new open inventory. `LOG-BRUNN-MINKOWSKI-SYMMETRIC` is newly and exclusively owned by HARD7-01 and is theorem-scale HARD. `H0021` is reassigned active HARD ownership to R17. None is selectable by NM13-05.

## 5. Existing residue-4 ownership/exclusion state remains controlling

Direct current claim reads confirm:

- `P0411` remains `CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE`, owner `proofnet24/NM13-05`, canonical key `boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells`, residue 4. Its six-unchanged terminal handoff/rotation did **not** release ownership. It is preserved, not reopened for ordinary research by this admission invocation.
- `P0429` remains exclusively owned by `R7-01`, classification CLOSABLE OUTSIDE. No handoff/retirement elsewhere is permission to shadow-claim it.
- `P0342` remains exclusively owned by P13, CLOSABLE OUTSIDE, despite its prior route rotation history.
- Previously reconciled unclaimed residue-4 sentinels P0315, P0416 and P0482 remain asymptotic/structural HARD sources absent a material source-status correction; no such correction occurs in the complete delta.

The current P0458 event is also not inventory: a distinct R01 audit now supplies its second independent mathematical PASS, but the canonical target remains owned rather than released. Audit completion never creates a vacancy.

For P0411 literature continuity, the bounded 2026 search again recovered D'Achille--Thäle's June 2026 face-volume-density paper. It solves face-volume/typical-face questions for IPVT, not the Conjecture-7.5 boundary-hole density monotonicity/coefficient scope owned in P0411. No current source correction releases or reclassifies P0411.

## 6. Admission verdict and research-method honesty

No source in the current material delta passes all gates simultaneously:

`exact source -> canonical identity -> current literature -> prior attempts/history -> not posted/settled/retired -> explicit free ownership -> source-level CLOSABLE endpoint -> residue 4`.

Therefore:

- admission status: **ADMISSION_PENDING**;
- newly admitted source / claim ID: **NONE**;
- canonical claim created: **NONE**;
- frozen successor marginal/object class: **NOT YET DEFINED**;
- successor metric before: **UNMEASURED**;
- successor metric after: **UNMEASURED**;
- mathematical movement: **NO MOVEMENT**;
- Section-B #2 ATTACK THE NEGATION FIRST: **NOT_TRIED_PRE_ADMISSION**;
- Section-B #8 DISCRETIZE: **NOT_TRIED_PRE_ADMISSION**;
- Section-B #11 DUALIZE: **NOT_TRIED_PRE_ADMISSION**.

Screening is not mathematical progress. The successor unchanged-run counter is **NOT STARTED** and successor stuck-recovery counter is **NOT STARTED / 0**. P0411's historical terminal state is preserved rather than reset: six unchanged closable runs reached the required rotation; its claim remains protected.

## 7. Model/scheduler control and the historical P26 permission failure

The current task-control interface still exposes prompt/title, scheduling/relative-start fields, timing mode, enabled state and ordinary task updates, but **no model-family selector, no reasoning-effort selector and no authenticated applied-model/applied-effort receipt**. Thus GPT-6/maximum remains prompt text only. Enforcing it would require an authorized product/workspace/admin/API scheduler that persists those routing fields and reports what actually ran.

The historical P26 `You cannot modify this task` response remains an authorization-context boundary. Current repository continuity records later successful P26 updating from an authorized context. The compliant workaround is the same task through its owning/authorized context, supported ownership/permission repair, or authorized platform support — never duplication or access-control bypass. No schedule was created, modified, disabled or duplicated in this invocation.

## 8. Next step and bounded-access statement

Retain cursor exactly:

`LEGACY_P_RECONCILIATION_COMPLETE_THROUGH=P0488; NEXT=STRICT_DELTA_ONLY_RESIDUE4_ADMISSION`.

Next invocation should inspect only genuinely new or materially changed source/intake/alias/claim/release/ownership/literature events after the frozen head. If an actually free residue-4 source-level CLOSABLE candidate appears, recover the canonical key first, complete exact-source/current-literature/prior-attempt/ownership checks, create its canonical claim with create-only semantics, read it back, freeze one source-faithful coupling cost/feasibility threshold at UNMEASURED until actually measured, then continue immediately into substantive #2/#8/#11 work.

Public literature access this run was bounded to ordinary web indexing and accessible primary/authoritative records; no paid databases, no worldwide-openness/novelty claim. Private repository access was available for the required paths used in the admission decision. No email, Drive, public posting, workflow execution, external scripts, paid compute, permission changes, shared-root edits, peer-file edits, or D-series edits were made.

```yaml
ledger_delta:
  worker: NM13-05
  category: CLOSABLE_OUTSIDE
  shard_mod13: 4
  status: ADMISSION_PENDING
  source_id: NONE
  claim_id: NONE
  predecessor_protected_claim: P0411
  cursor_before: "LEGACY_P_RECONCILIATION_COMPLETE_THROUGH=P0488; NEXT=STRICT_DELTA_ONLY_RESIDUE4_ADMISSION"
  cursor_after: "LEGACY_P_RECONCILIATION_COMPLETE_THROUGH=P0488; NEXT=STRICT_DELTA_ONLY_RESIDUE4_ADMISSION"
  metric_name: successor_extremal_coupling_cost_or_feasibility_threshold
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  mathematical_movement: NO_MOVEMENT
  section_b_methods:
    - "2: NOT_TRIED_PRE_ADMISSION"
    - "8: NOT_TRIED_PRE_ADMISSION"
    - "11: NOT_TRIED_PRE_ADMISSION"
  successor_unchanged_runs: NOT_STARTED
  successor_recovery_count: 0_NOT_STARTED
  predecessor_p0411_terminal_unchanged_runs: 6
  admission_events:
    - "G0004 explicitly released but canonical residue=2 and category HARD_OUTSIDE"
    - "MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS explicitly released but theorem-scale HARD and no authoritative NM13 dedup key"
    - "B-WEAK released HARD; AK equality resolved; LOG-BM owned HARD; H0021 reassigned HARD"
    - "P0411/P0429/P0342 ownership remains protected"
  frozen_prewrite_head: 6f0059bbea21c375fd6db23d2ad835fa4c7b5a36
  exact_delta_base: d3870ecc1fd64a2af32077442eb1b603d2708e24
  exact_delta_commits_ahead: 131
  exact_delta_commits_behind: 0
  exact_delta_too_large: null
  next_step: STRICT_DELTA_ONLY_RESIDUE4_ADMISSION
```
