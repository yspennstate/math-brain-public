Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MATHEMATICAL MOVEMENT: NM13-04 remains ADMISSION_PENDING; successor metric stays `UNMEASURED -> UNMEASURED`; Section-B methods #2/#14/#19 remain genuinely NOT_TRIED_PRE_ADMISSION.**

# NM13-04 — admission delta: G0004 released but HARD/residue 2; P0458 reaches second independent PASS; no residue-3 CLOSABLE release

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-04` / `proofnet24/NM13-04/`  
Category: **CLOSABLE OUTSIDE**  
Selection shard: `int(SHA256(UTF-8 canonical_dedup_key).hexdigest(),16) mod 13 = 3`  
Secondary audit partner after a future completed NM13-04 claim: `NM13-05`, in addition to P26. Neither is presumed to pass.

## 1. Continuity recovered before screening

I re-read the current controlling repository material required by the owner directive: `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, the later owner-authorized NM13 deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`, `QUEUE.md`, `POSTED.md`, `RESULTS.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, the newest NM13-04 report, neighboring NM13-03/NM13-05 run listings, current canonical claims, and the admission-relevant source/attempt continuity.

Newest prior NM13-04 report:

`proofnet24/NM13-04/runs/2026-09-19/2026-09-19T21-24-30Z__admission-delta-e0011-reassigned-r6-p0458-p26-pass-no-residue3-release.md`

That report froze its pre-write comparison at

`b8ce5ae5016c01ecd05bee80d37b8424b8da6424`.

The durable screening cursor remains

`POST_LEGACY_P0488_DELTA_ONLY_RESIDUE3_ADMISSION`.

This means the static legacy P reconciliation through the populated/archived P0488 range is not restarted absent a material source/alias/intake/claim/literature delta. P0457 remains terminally exhausted/rotated and is not reopened. Screenings remain admission work, not mathematical progress.

The latest neighboring NM13-03 run is the 22:19 UTC report whose title records the same new G0004 event as `released-hard-r2-no-closable-admission`. The newest visible NM13-05 run before this invocation remains its 21:28 UTC admission-delta report. No neighboring report supplies a residue-3 ownership release for NM13-04.

## 2. Exact repository delta from the predecessor frozen head

Immediately before this report write I froze `master` at

`25416f1311c7ccbe5727e251c09b827a439bb644`.

Exact compare:

- base: `b8ce5ae5016c01ecd05bee80d37b8424b8da6424`
- head: `25416f1311c7ccbe5727e251c09b827a439bb644`
- status: `ahead`
- ahead: `130`
- behind: `0`
- `too_large = null`

The complete changed-file list has **six canonical claim mutations** and no mutation of `QUEUE.md`, `POSTED.md`, `RESULTS.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, any `probability_1000_intake_*/problems.jsonl`, or any probability intake/attempt JSONL. Therefore there is no newly added canonical intake row or source-ledger alias correction to rescan from scratch in this interval.

The six claim mutations are:

1. `operations/claims/G0004.md` — explicit R17 release after HARD two-recovery exhaustion;
2. `operations/claims/H0021.md` — reassigned active HARD ownership;
3. `operations/claims/MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS.md` — HARD7-01 handoff/release after Section-I exhaustion;
4. `operations/claims/B-WEAK-EVEN-LOGCONCAVE.md` — terminal HARD handoff/release;
5. `operations/claims/AK-KATZIN-C41-EQUALITY.md` — literal printed equality target recorded as refuted/resolved and released as a resolved source target;
6. `operations/claims/LOG-BRUNN-MINKOWSKI-SYMMETRIC.md` — newly claimed by HARD7-01.

No canonical residue-3 CLOSABLE ownership marker was released by this delta.

## 3. G0004 is a genuine release, but it fails both category and shard gates

Current canonical claim history:

`operations/claims/G0004.md`

states

- owner: `UNASSIGNED AFTER R17 HANDOFF`;
- status: `SOURCE OPEN / PARTIAL / RELEASED BY R17`;
- source: Lucas Flammant, *A conjecture implying theta(p_c)=0 for Bernoulli bond percolation on Z^d*, arXiv:2609.03492, Conjecture 2.2;
- canonical intake identity: `flammant_finite_graph_2026::conjecture_2.2`;
- R17 class: **HARD OUTSIDE**;
- frozen source-wide metric: `U_F=1`;
- persistent obstruction: adaptive boundary-label switching through shared connectivity together with genuinely global decreasing failure kernels.

I hashed the recovered canonical intake identity, not the display title or `G0004` alias:

`SHA256("flammant_finite_graph_2026::conjecture_2.2") = cfd780a5cdd49da5833b93d35f22b8593428c666840b2c9014bdf69f6da2ed75`,

and

`int(hash,16) mod 13 = 2`.

So G0004 is **off NM13-04's residue-3 shard independently of category**. It is also source-level HARD: although the conjecture is stated on arbitrary finite graphs, the deliverable is a dimension-free theorem over all finite graphs and is explicitly strong enough to imply `theta(p_c)=0` for Bernoulli bond percolation on every `Z^d`, `d>=2`. It is not a finite counterexample/cutoff/short-theorem source that can honestly be relabeled CLOSABLE.

Fresh bounded public search dated 2026-09-19 UTC recovered Flammant's current September 2026 preprint and its stated planar outer-face theorem with explicit `1-2 sqrt(epsilon)` bound, but no later indexed primary source resolving unrestricted Conjecture 2.2. This is bounded negative evidence only, not a worldwide-openness certificate.

Verdict: **released, but HARD and residue 2; not selectable by NM13-04.**

## 4. Other new release/handoff events do not create NM13-04 inventory

### H0021

The claim mutation is a reassignment, not a free target. It remains HARD OUTSIDE under R17. No NM13-04 action.

### Maximal-intersection ellipsoid uniqueness

`operations/claims/MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS.md` now records `HANDOFF / source OPEN / research PARTIAL only / released after Section-I exhaustion`. The literal target asks uniqueness of the maximal-intersection ellipsoid for every centrally symmetric convex body in general dimension at intermediate volume/radius. The frozen finite-dimensional progress is only `D_MI=2`, matching Jairo Bochi's positive two-dimensional theorem.

Fresh bounded literature search recovered Artstein-Avidan--Katzin's maximal-intersection framework and Bochi's 2018 theorem explicitly saying the uniqueness question is open in general and solved in dimension two. I did not find a later indexed source claiming the all-dimensional theorem. Again this is bounded negative evidence only.

This source is theorem-scale HARD rather than a finite counterexample/certificate source, and its released claim does not supply an authoritative NM13 intake `dedup_key`. Under the shard rule I therefore did **not** hash its title, arXiv identifier, or another alias merely to manufacture a residue.

### Weak-B even log-concave target

The claim mutation is a terminal HARD handoff. It is not a CLOSABLE finite target and supplies no lawful residue-3 successor.

### Artstein-Avidan--Katzin Conjecture 4.1 equality clause

The literal printed equality clause has already been recorded as refuted/resolved in another track. A release of a **resolved** target is not permission to reopen it. It remains excluded from new research ownership.

### Symmetric log-Brunn--Minkowski Problem 1.1

This target is newly claimed by HARD7-01 and is theorem-scale HARD. It fails exclusive-ownership and category gates.

## 5. P0458 materially advances to two independent full-proof PASS audits — which makes it less available, not more

P0458 is the strongest graph-shaped residue-3 CLOSABLE sentinel previously encountered by NM13-04. Its canonical dedup key recovered in earlier shard reconciliation is

`the_standardized_degree_law_in_growing_bilateral_preference_graphs`,

whose SHA-256 residue is exactly `3 mod 13`.

The canonical ownership marker still says:

- owner `R7-03`;
- status `ADMITTED_ACTIVE / CLOSABLE OUTSIDE / PARTIAL`;
- exact source: Dabirian--Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2), 552--579 (2026), Section 1.1 open problem on the standardized degree law.

The prior NM13-04 run recorded P26's first source-exact independent full-proof PASS. The current delta now contains R01's distinct second audit report

`runs/R01/20260919T2209Z_p0458_second_audit_2_5_25_c4f8a2d1.md`,

with verdict

`R01-AUDIT-P0458-BILATERAL-DEGREE-LIMITS-ENDTOEND-01 = PASS_FULL_MATHEMATICAL_PROOF`.

R01 explicitly records the independent-audit counter as **`1/2 -> 2/2`** after independently reconstructing the interior regime, fixed-complement mixed-Poisson regime, first-two-moment convergence, boundary gluing, and fixed-finite-`k` prior-art reconciliation.

Fresh bounded public literature checking again recovered the Cambridge final article, published online 18 December 2025 and in the June 2026 issue, as the source that explicitly asks for the limiting law of `(D-E[D])/sqrt(Var[D])`. The bounded public search did not surface a later indexed public theorem matching the repository package; publication priority therefore remains unverified.

Operational consequence for admission: **P0458 is not released and now has both required independent mathematical audits recorded.** Shared-root/owner closure reconciliation may still lag the audit commit, but in no event does this make P0458 free inventory. NM13-04 must not shadow-claim it.

## 6. Other retained residue-3 sentinels

### P0169

`operations/claims/P0169.md` still records owner `R7-02`, class `CLOSABLE OUTSIDE`, source O'Donnell's “Linear Coefficients versus Total Degree,” and no explicit canonical release. Its canonical key

`linear_fourier_mass_versus_boolean_degree`

has SHA-256

`0293f8eb2ba63ce7024462fbdedbf656b716ef1f586c9928f67d42d54b55c184`

and residue `3 mod 13`.

The prior six-run R7-02 handoff/retirement history is not a release. P0169 remains unavailable.

### F0011

`operations/claims/F0011.md` still records exclusive owner `R7-06`, class **HARD OUTSIDE**, and Vu's integral-spectrum asymptotic conjecture. The current delta contains new exact `n=9` census work by R7-06, but the claim itself correctly says finite enumeration is only PARTIAL relative to the source asymptotic. It cannot be relabeled CLOSABLE simply because the finite milestones are exact.

Fresh public search found recent 2026 work on other integral-spectral graph families, but no indexed theorem resolving Vu's random symmetric-Rademacher integral-spectrum asymptotic. This is bounded negative evidence only.

## 7. Admission verdict and methods

No source passes all gates simultaneously:

`exact source -> canonical identity -> current literature -> prior attempts/history -> not posted/settled/retired -> explicit free ownership -> CLOSABLE source endpoint -> residue 3`.

Therefore:

- admission status: **ADMISSION_PENDING**;
- canonical claim created: **NONE**;
- source/claim ID: **NONE**;
- frozen successor graph class: **NOT YET DEFINED**;
- successor metric before: **UNMEASURED**;
- successor metric after: **UNMEASURED**;
- mathematical movement: **NO MOVEMENT**;
- Section-B #2 ATTACK THE NEGATION FIRST: **NOT_TRIED_PRE_ADMISSION**;
- Section-B #14 FIND THE GROUP ACTING: **NOT_TRIED_PRE_ADMISSION**;
- Section-B #19 MAKE IT AN ALGORITHM: **NOT_TRIED_PRE_ADMISSION**.

These methods are not falsely counted as attempted merely because admission screening occurred.

P0457 remains the exhausted predecessor and is not reopened. Screening work does not increment a mathematical unchanged-run counter on a nonexistent successor. The successor unchanged-run count remains **NOT STARTED** and the successor stuck-recovery count remains **0 / NOT STARTED**.

## 8. Scheduler/model-control audit

The requested opening line still cannot be made binding by the exposed scheduler surface. The current task-control interface exposes title/prompt, schedule or relative start, timing mode, enabled state, listing, and ordinary update operations. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated applied-model/applied-effort runtime receipt**.

Therefore `GPT-6 / maximum` remains a prompt-text request only. This report uses the actual runtime information available to the model: **GPT-5.6 Sol; reasoning level UNVERIFIED**.

The historical P26 response `You cannot modify this task` remains an authorization-context boundary, not evidence that duplicating or bypassing the task is permitted. Current `RESULTS.md` records that P26 was later updated successfully from an authorized context. The compliant workaround is to use the same task from its owning/authorized product/workspace/admin/API context, supported permission repair, or authorized platform support. No schedule was created, modified, disabled, or duplicated in this invocation.

## 9. Next step

Retain cursor

`POST_LEGACY_P0488_DELTA_ONLY_RESIDUE3_ADMISSION`.

On the next invocation, inspect only genuinely new or materially changed canonical source/intake/alias/claim/release/ownership/literature events after the frozen head. In particular, treat P0458 as audit-complete/non-free unless an authoritative later owner/shared-ledger event says otherwise; do not interpret a handoff, retirement, disabled schedule, or resolved-target release as free ownership. If an actually free residue-3 CLOSABLE source appears, create its canonical claim with create-only semantics, read it back, freeze its source graph class and one source-relevant exact counterexample-size/exhaustive-cutoff metric at `UNMEASURED` until measured, and continue immediately into substantive methods #2/#14/#19.

## 10. Bounded literature/access scope

Dated public checks: 2026-09-19 UTC (crossing local midnight in the worker's deployment timezone).

Queries included:

- exact Flammant arXiv `2609.03492` / Conjecture 2.2;
- exact Dabirian--Subramanian article title plus `standardized degree`, `limiting distribution`;
- Artstein-Avidan / Katzin / maximal-intersection ellipsoid uniqueness / Bochi;
- O'Donnell linear Fourier mass versus Boolean degree;
- Vu random symmetric matrix integral spectrum, including 2026 follow-up search terms.

Access limits: bounded web indexing and accessible repository history only; no claim of worldwide bibliographic completeness, no paid databases, no external scripts, no workflows, no email/Drive/public posting.

```yaml
ledger_delta:
  worker: NM13-04
  category: CLOSABLE_OUTSIDE
  status: ADMISSION_PENDING
  source_id: null
  claim_id: null
  canonical_dedup_key: null
  selection_residue_required: 3
  metric_name: successor_exact_counterexample_size_or_exhaustive_cutoff
  metric_scope: NOT_DEFINED_BEFORE_ADMISSION
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  mathematical_movement: false
  actual_methods:
    - id: 2
      status: NOT_TRIED_PRE_ADMISSION
    - id: 14
      status: NOT_TRIED_PRE_ADMISSION
    - id: 19
      status: NOT_TRIED_PRE_ADMISSION
  predecessor:
    source_id: P0457
    status: EXHAUSTED_ROTATED_DO_NOT_REOPEN
  screening_cursor: POST_LEGACY_P0488_DELTA_ONLY_RESIDUE3_ADMISSION
  compare:
    base: b8ce5ae5016c01ecd05bee80d37b8424b8da6424
    frozen_head: 25416f1311c7ccbe5727e251c09b827a439bb644
    ahead_by: 130
    behind_by: 0
    too_large: null
  material_events:
    - source_id: G0004
      event: EXPLICIT_RELEASE
      class: HARD_OUTSIDE
      canonical_key: flammant_finite_graph_2026::conjecture_2.2
      sha256: cfd780a5cdd49da5833b93d35f22b8593428c666840b2c9014bdf69f6da2ed75
      residue_mod_13: 2
      selectable: false
      reason: HARD_AND_OFF_SHARD
    - source_id: H0021
      event: REASSIGNED_ACTIVE
      class: HARD_OUTSIDE
      selectable: false
    - source_id: MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS
      event: EXPLICIT_HANDOFF_RELEASE
      class: HARD_THEOREM_SCALE
      canonical_nm13_dedup_key: UNRECOVERED_FROM_AUTHORIZED_SELECTION_SURFACES
      selectable: false
    - source_id: AK-KATZIN-C41-EQUALITY
      event: RESOLVED_REFUTED_RELEASE
      selectable: false
      reason: SETTLED_SOURCE_TARGET
    - source_id: B-WEAK-EVEN-LOGCONCAVE
      event: TERMINAL_HARD_HANDOFF
      selectable: false
    - source_id: LOG-BRUNN-MINKOWSKI-SYMMETRIC
      event: NEW_CANONICAL_CLAIM
      owner: HARD7-01
      class: HARD_OUTSIDE
      selectable: false
    - source_id: P0458
      event: SECOND_DISTINCT_FULL_PROOF_AUDIT_PASS
      canonical_key: the_standardized_degree_law_in_growing_bilateral_preference_graphs
      residue_mod_13: 3
      owner: R7-03
      audits: 2/2
      selectable: false
      reason: OWNED_AND_AUDIT_COMPLETE_NONRELEASE
  unchanged_run_count_successor: NOT_STARTED
  stuck_recovery_count_successor: 0
  next_step: DELTA_ONLY_RESIDUE3_ADMISSION_SCREEN
  shared_roots_edited: false
  peer_files_edited: false
  schedules_modified: false
```
