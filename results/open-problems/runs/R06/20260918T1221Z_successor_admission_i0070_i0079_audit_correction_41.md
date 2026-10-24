Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. SUCCESSOR-ADMISSION NO MOVEMENT: `E_ready: 0 -> 0`; preserved I0056 interval width `0 -> 0`; AUDIT STATUS MOVED: the previously missed P26 audit is real, so the frozen `H_{5,5}` subtarget / regular-co-regular clause package is audit-complete as a proved source-partial result. Methods #8 GO THE OTHER WAY AND DISCRETIZE, #12 FIND WHAT IS CONSERVED, #24 FIND THE EXTREMAL OBJECT.**

# R06 — I0056 audit correction and successor-admission cursor I0070–I0079

Repository / branch: `yspennstate/math-open-problems` / `master`  
Lane: **CLOSABLE OUTSIDE**  
Operational state: **SUCCESSOR_ADMISSION_REQUIRED**  
Current mathematical successor: **NONE**

## 1. Continuity: do not reopen exhausted research tracks

This run continues from the immutable R06 report

`runs/R06/20260918T1124Z_successor_admission_h55_animal_normalization_40.md`

created at commit

`4e3eb0918cdc25d3188d4f2260c9a87638ae92e7`.

I did **not** reopen I0056, I0079, BENJ-2026-FS3, or P0025 as attacking targets. Their mathematical history remains preserved. The current job is successor admission plus required correction of repository facts discovered while rereading the audit tree.

Before research/admission decisions I reread or targeted-recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` and the NEW-METHODS owner directive tree;
- canonical `operations/claims/I0056.md` and `operations/claims/I0079.md`;
- the newest prior R06 report;
- the newest coordinator/task-health report;
- the newest relevant neighboring successor-admission report, especially R02's exact `I0060–I0069` cursor screen;
- current P26 audit history and the distinct R05 I0056 audit;
- exact-ID claim/history evidence for the next admission block `I0070–I0079`.

The intake JSONL corpus is too large for a useful single connector rendering. I therefore use exact-ID retrieval plus immutable prior cursor screens and do **not** pretend a truncated connector response is a fresh byte-for-byte reread of every historical row.

## 2. Important correction: the P26 I0056 audit exists

Several recent R06 admission reports stated that the I0056 closure package still lacked the required P26 end-to-end audit. That statement was wrong. A fresh exact repository search recovered the P26 report

`proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_08-59-22__run-report.md`.

Its audit ID is

`P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15`

and its verdict is

**`PASS_FULL_MATHEMATICAL_PROOF / REGULAR-COREGULAR-FIRST-CLAUSE / SOURCE_PARTIAL / PRIOR_ART_UNVERIFIED`.**

P26 explicitly audits the package

- `R06-I0056-CLOSURE-01`, and
- `R06-I0056-COR-F5`,

and gives an independent two-defect/Lyapunov proof of the closure theorem rather than merely replaying the owner's derivation.

The genuinely distinct OTHER-track audit is R05:

`R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z`

with verdict

**`PASS_MATH_SCOPE / NOVELTY_UNVERIFIED`.**

P26 explicitly read that R05 audit and counted the R06 theorem package exactly once, moving P26's own audit-completion metric `12 -> 13`.

Therefore the frozen I0056 package now satisfies the contract's two-auditor requirement. The exact finite/local certificate also already exists:

- `artifacts/R06/20260916T151735Z_i0056_closure_hardening_exact.py`;
- `artifacts/R06/20260916T151735Z_i0056_closure_hardening_exact.out`, ending `PASS`.

No duplicate checker was manufactured this run.

## 3. What this correction changes — and what it does not

The canonical I0056 source is Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20. Its two clauses ask:

1. determine `Phi_V(G)` for regular, co-regular plane graphs;
2. determine `Phi_E(G)` and `Phi_V(G)` for more general transitive plane graphs.

The frozen R06 regime is the regular tessellation

`H_{5,5} = {5,5}`,

with degree `d=5`, face degree `f=5`, and the **outer vertex boundary** normalization

`Phi_V(G)=inf_{0<|K|<infinity} |partial_V K|/|K|`.

The preserved result is

`Phi_V(H_{5,5}) = sqrt(5)`,

hence

`[L,U]=[sqrt(5),sqrt(5)]`, `U-L=0`.

The R06 theorem package in fact proves the regular/co-regular `f>=5` branch, while Haslegrave–Panagiotis supply the already-published `f=3,4` branch. P26's audit therefore says the **first regular/co-regular clause is mathematically accounted for by the R06 package plus prior art**.

This does **not** close the full source Question 6.20. The more general transitive-plane-graph clause remains outside the proved package. Honest status is therefore:

- frozen `H_{5,5}` subtarget: **PROVED / audit-complete**;
- R06 regular/co-regular first-clause package: **PROVED mathematically, prior-art priority still UNVERIFIED**;
- full Lyons–Peres Question 6.20: **PARTIAL**, not PROVED.

The earlier rotation remains valid: recovering a missing audit receipt does not authorize a new attack on an exhausted predecessor.

## 4. Fresh 18 September 2026 source / prior-art check

I repeated a bounded current-literature check rather than relying only on the 17 September P26 search.

### Haslegrave–Panagiotis exclusion remains exact

John Haslegrave and Christoforos Panagiotis, *Site percolation and isoperimetric inequalities for plane graphs*, Random Structures & Algorithms 58 (2021), DOI `10.1002/rsa.20946`, explicitly state that they establish the vertex isoperimetric constant for the triangular and quadrangular hyperbolic lattices and that the second halves of their Theorems 4 and 5 answer Lyons–Peres Question 6.20 for face degrees `3` and `4`.

Those regimes remain excluded prior art and are not R06 novelty.

### 2025 hyperbolic-animal paper remains a different normalization

Érika Roldán and Rosemberg Toalá-Enríquez, *Isoperimetric Formulas for Hyperbolic Animals*, Graphs and Combinatorics 41:38 (published 19 February 2025), gives

`P_min^{p,q}(n) = (p-2-2/beta_{p,q}) n + O(1)`

with an explicit bounded error term. For `{5,5}` the leading coefficient is `sqrt(5)`. But their `n` counts tiles and `P_min` counts boundary **edges** of a tile union. Under duality this is an edge-boundary quantity, not automatically the distinct outside-neighbor vertex boundary used by I0056. It therefore remains important adjacent prior art, not an independent resolution of the R06 vertex-normalized claim.

Fresh queries for `H_{5,5}` / `{5,5}` vertex-isoperimetric constants and Question 6.20 did not surface a later primary publication explicitly stating the R06 `f>=5` vertex formula. This is bounded negative evidence only; publication priority remains **UNVERIFIED**.

## 5. Repository delta since the previous R06 report

A direct compare from the previous R06 creation commit

`4e3eb0918cdc25d3188d4f2260c9a87638ae92e7`

to current `master` found **103 commits ahead, 0 behind** at the captured comparison.

The source-selection roots `QUEUE.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, and the intake problem ledgers did not change in that compare. The new traffic is overwhelmingly peer mathematics, audits, admission screens, artifacts, and additional ownership. In particular, `KNSV-2026-LOOPY-U` is a new CLOSABLE READY claim owned by R20; it shrinks rather than expands free inventory.

The newest coordinator report still records `newly_certified_READY: 0` in its bounded CLOSABLE admission screen, with a durable I-series cursor at `I0060`. R02 subsequently completed the exact block `I0060–I0069` and found zero lawful free full-source CLOSABLE successors there. I use that as the immediately preceding durable cursor instead of rescanning it for ceremony.

## 6. Method #8 — GO THE OTHER WAY AND DISCRETIZE: screen exactly I0070–I0079

Rather than making a vague global claim that “nothing is free,” I reduced successor admission to the next ten exact source IDs and checked ownership/lifecycle/category/scope evidence one by one.

| ID | Current evidence | R06 disposition |
|---|---|---|
| `I0070` | canonical provisional reservation `operations/claims/I0070.md`, owner R10, `PENDING_ADMISSION` | **OWNED / not free** |
| `I0071` | root queue/current admission records mark excerpt/source scope incomplete or ambiguous | **NOT READY; cannot inflate reserve** |
| `I0072` | same incomplete/ambiguous-source-excerpt hold as I0071 | **NOT READY** |
| `I0073` | canonical claim exists; prior HARD no-slip stochastic Navier–Stokes work exhausted both recoveries and handed off without an owner-authorized release | **HARD / unreleased history** |
| `I0074` | no simple live claim, but current-author status correction says Towsner covers the measure-theoretic part and the remaining topology/Feller problem is broad/HARD-shaped; original `UTC` class is underspecified | **NOT READY / not honestly CLOSABLE** |
| `I0075` | canonical reservation exists; previous slot later rotated, but no explicit non-exhausted ownership release | **OWNED/HISTORY-BLOCKED** |
| `I0076` | R15 Burdzy–Scheutzow Problem 7.2 reached its six-run handoff; no explicit release authorizes R06 takeover | **RETIRED-HANDOFF / not free** |
| `I0077` | `operations/claims/I0077.md`, exclusive provisional reservation for R07 | **OWNED** |
| `I0078` | canonical C27 claim, `CLAIMED / READY / HARD OUTSIDE` | **OWNED / HARD** |
| `I0079` | canonical R06 historical claim; already attacked and rotated before later successors | **OWN PREDECESSOR / DO NOT REOPEN** |

Thus

`lawful free full-source CLOSABLE successors in I0070–I0079 = 0`.

This is a bounded cursor result, not proof that no eligible source exists anywhere in the repository.

## 7. Method #12 — FIND WHAT IS CONSERVED: ownership/lifecycle is sticky until an explicit release

The recurring admission mistake across the fleet is to treat

`claim file absent OR old slot rotated`

as equivalent to

`source is free`.

The current block supplies several counterexamples. I0073, I0075, and I0076 all have substantial prior ownership/handoff history; rotation or handoff does not itself create a free non-exhausted successor. I0074 shows the complementary issue: an unclaimed-looking row can still fail admission because the current source scope has changed and the residual problem is no longer CLOSABLE-shaped.

The conserved operational invariant is therefore:

**existing ownership / exhausted-handoff state persists for dispatch purposes unless a current owner-authorized release or reassignment explicitly changes it.**

This is not a mathematical theorem. It is the rule preventing duplicate attacks and fabricated reserve.

## 8. Method #24 — FIND THE EXTREMAL OBJECT: test the strongest unclaimed-looking candidate, I0074

Among `I0070–I0079`, I0074 is superficially the best candidate because it lacks the simple “live claim owned elsewhere” obstruction and originally looked like a compact counterexample/uniqueness problem.

The exact current-author reconciliation defeats that admission. Aldous's live page now credits Towsner with the measure-theoretic limit construction and presents the remaining issue as building a natural complete-separable topology / Feller realization. Towsner's pseudofinite-chain framework also distinguishes raw representative uniqueness from twin-free/saturated measure-theoretic uniqueness. The original note's `UTC` (“unspecified technical condition”) remains underspecified.

So admitting I0074 as a short CLOSABLE uniqueness/counterexample target would silently change the source problem. The honest remaining source shape is broad and HARD. I0074 therefore fails even when deliberately selected as the best local candidate.

## 9. Successor decision

**No canonical successor claim is created.**

R06 remains

`CLOSABLE OUTSIDE / SUCCESSOR_ADMISSION_REQUIRED / NO ACTIVE SUCCESSOR`.

Temporary admission metric:

`E_ready = number of presently evidenced unresolved + source-frozen + full-source CLOSABLE + ownership-clear + non-excluded successors R06 can lawfully claim now`.

For this bounded cursor:

`E_ready: 0 -> 0`.

This is an operational admission metric, not a new source theorem metric and not a mathematical stagnation count. The next successor mathematical metric remains `UNMEASURED` until an actual source is admitted.

The durable cursor is now **through I0079**. Future runs should be delta-first and continue beyond that cursor unless a material source/status/release change occurs earlier.

## 10. No checker / audit theater / shared-root write

No new finite mathematical claim was made, so no checker was manufactured. I did not request another I0056 audit because the two required independent audits already exist. I did not create a paper package because the full source question remains PARTIAL and this invocation did not close a new source.

No edits were made to `RESULTS.md`, `QUEUE.md`, `POSTED.md`, campaign roots, peer tracks, historical claim files, email/Gmail, Drive, public posting surfaces, permissions, purchases, workflows, or schedules.

## 11. Model / scheduler / authorization truth

The operative follow-up implementation record still says the exposed scheduler has prompt/title, schedule or relative-start controls, timing mode, enabled state and task identity, but **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed hour-long execution field**. GPT-6 / maximum is therefore prompt text only in this invocation.

The historical P26 response `You cannot modify this task` was an authorization-context boundary. Repository continuity records that another authorized context later succeeded in updating P26. The lawful workaround is the owning/authorized context or product/admin support for that same task, never duplication, alternate-ID bypass, or permission changes. No scheduler change was attempted here.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  run_kind: successor_admission_with_audit_correction
  active_successor: null
  state: SUCCESSOR_ADMISSION_REQUIRED
  preserved_source:
    source_id: I0056
    source: "Lyons-Peres, Probability on Trees and Networks, Question 6.20"
    frozen_graph: H_5_5
    degree: 5
    face_degree: 5
    normalization: outer_vertex_boundary
    interval_before: "[sqrt(5), sqrt(5)]"
    interval_after: "[sqrt(5), sqrt(5)]"
    width_before: 0
    width_after: 0
    subtarget_status: PROVED_AUDIT_COMPLETE
    full_source_status: PARTIAL
  audit_status_delta:
    before_as_recent_R06_reports_mistakenly_recorded: P26_MISSING
    after: TWO_INDEPENDENT_AUDITS_PRESENT
    p26: "P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15 = PASS_FULL_MATHEMATICAL_PROOF / REGULAR-COREGULAR-FIRST-CLAUSE / SOURCE_PARTIAL / PRIOR_ART_UNVERIFIED"
    other: "R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z = PASS_MATH_SCOPE / NOVELTY_UNVERIFIED"
    exact_certificate: artifacts/R06/20260916T151735Z_i0056_closure_hardening_exact.out
  admission_metric:
    name: E_ready
    before: 0
    after: 0
    mathematical_metric_started: false
  repository_delta:
    previous_r06_commit: 4e3eb0918cdc25d3188d4f2260c9a87638ae92e7
    commits_ahead_at_capture: 103
    commits_behind: 0
    newly_certified_READY_in_latest_coordinator_bounded_screen: 0
  bounded_cursor:
    inherited_through: I0069
    screened_this_run: I0070-I0079
    after: I0079
    eligible_successors_found: 0
    dispositions:
      I0070: OWNED_R10_PENDING
      I0071: NOT_READY_INCOMPLETE_SCOPE
      I0072: NOT_READY_INCOMPLETE_SCOPE
      I0073: HARD_HANDOFF_UNRELEASED
      I0074: NOT_READY_CURRENT_AUTHOR_SCOPE_HARD
      I0075: OWNED_HISTORY_BLOCKED
      I0076: SIX_RUN_HANDOFF_UNRELEASED
      I0077: OWNED_R07
      I0078: OWNED_C27_HARD
      I0079: R06_RETIRED_PREDECESSOR_DO_NOT_REOPEN
  methods_this_run: [8, 12, 24]
  method_outcomes:
    8: "localized admission to exact finite block I0070-I0079; zero eligible successors"
    12: "ownership/handoff lifecycle remains blocking until explicit release/reassignment"
    24: "I0074 was strongest unclaimed-looking local candidate; current-author status makes residual problem HARD/not source-clean CLOSABLE"
  remaining_obligation: "Continue delta-first successor admission beyond I0079; claim create-only only after exact source/current-status/prior-history/exclusion/ownership gates all pass"
  evidence_ids:
    - R06-I0056-CLOSURE-01
    - R06-I0056-COR-F5
    - P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15
    - R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z
  scheduler:
    model_selector: NOT_EXPOSED
    reasoning_selector: NOT_EXPOSED
    authenticated_runtime_telemetry: NOT_EXPOSED
    guaranteed_duration: NOT_EXPOSED
  writes:
    own_immutable_report_only: true
    shared_roots: none
    peer_files: none
    scheduler: none
```
