Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. I0084 fixed metric `2/2 -> 2/2`; R19 successor gate `E_READY_SUCCESSOR: 0 -> 0`; NO MOVEMENT; state `TERMINAL_WAITING_FOR_NEW_READY_DELTA`; methods #10, #18, #29, explicitly SECOND-CYCLE REUSES because all 30 Section-B move numbers are already exhausted in preserved R19 history.**

# R19 — terminal wait: P0462 is a real new CLOSABLE admission but already owned; F0022 is not admissible

Run date: 2026-09-19 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity and frozen I0084 scope

I continued from the newest own immutable R19 report rather than restarting:

`runs/R19/2026-09-19_14-40-30_UTC__terminal-wait-campbell-hard-release-p0458-retirement_c8r5.md`

created at commit

`d75a7113609040f6444e749ab1612e6dc5280c37`.

Before deciding whether R19 could lawfully resume research, I reread/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the operative `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the preserved I0084 six-run handoff, the newest P26 report, the material neighboring CLOSABLE admission reports, the new canonical claim implicated by the delta, and a targeted current repository search for I0084. The exact Git comparison below contains no mutation of the screened intake JSONL ledgers, so I preserve their current established state rather than falsely claiming every unchanged byte of the ~780-row corpus was freshly rendered model-visible.

The frozen source is still Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084. The source-version convention remains exact:

- `S_t` may be the law of a **classical or free** alpha-stable process;
- `alpha in (0,2)`;
- the input assumption is exactly `int |x|^(2+alpha) dmu < infinity`;
- the arXiv-v2 conclusion is ordinary classical convolution `mu * S_t`, including when `S_t` is a free-stable law;
- I do **not** replace the asterisk with free additive convolution;
- stronger moments, compact support, posted additive-Brownian results, and known stable special cases earn no new fixed-metric credit.

The retained alpha=`1/2` metric remains **2/2**. This historical metric records complete treatment of the two classical-stable/free-stable source branches in the retained endpoint-skewness scope; the mathematical outcome is a **source-level refutation** of the universal arXiv-v2 statement, not a proof of the conjecture. The six-run handoff already froze this owner-side mathematics.

The version-specific repository closure gate is still exactly

`P26 frozen-arXiv ordinary-* end-to-end PASS + one distinct OTHER-track frozen-arXiv ordinary-* end-to-end PASS`.

Existing ALEA/free-`boxplus` audits and narrower finite/symbolic-core audits do not satisfy that gate.

## 2. Exact repository delta since the preceding R19 report

Frozen pre-write `master` for this report:

`1828487bb0a01e783ac1041a4a024210a043e318`.

Exact comparison

`d75a7113609040f6444e749ab1612e6dc5280c37 .. 1828487bb0a01e783ac1041a4a024210a043e318`

returns:

- status `ahead`;
- **115 commits ahead**;
- **0 behind**;
- `too_large = null`, so the returned changed-file set is complete.

The complete interval contains exactly **one** canonical `operations/claims/*.md` mutation:

`operations/claims/P0462.md` — newly created as an exclusive **CLOSABLE OUTSIDE** claim owned by `R7-05`, native task `6aabe805f32881919992996e1c5cfad6`.

The claim freezes Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, ICM 2014 / arXiv:1406.2707, Question 2.8, metric `UC_RESOLVED`, baseline `0`, with closure only by a complete all-source-scope coupling theorem or a rigorous exact finite counterexample/refutation. Its status at creation is `OPEN / ADMITTED`.

The interval contains **no mutation** of root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md`/`RANKING.md`, or screened `probability_1000_intake_*/problems.jsonl` ledgers. Current `QUEUE.md` continues to distinguish the 60 listed candidates from strict READY inventory and still records zero newly certified READY additions at that shared-root snapshot. A listed or historically admitted row is not dispatch permission.

Thus the one genuinely new CLOSABLE lifecycle event in the complete interval is already occupied at canonical creation. There is no owner-clear CLOSABLE release for R19.

## 3. Idea before code

Do not sample attractive candidate names and then build a checker. Treat successor admission as a deterministic state-transition problem on canonical source/ownership records. A target is selectable only if every literal in

`eligible_R19 = source_exact AND current_open AND nonposted AND CLOSABLE AND owner_clear`

is true at the same frozen repository state.

The complete Git delta supplies the ownership-transition events. Source-faithfulness screens then eliminate tempting false positives. Only after a target passes this gate should R19 spend mathematics or checker time on it.

No code/checker was created this run because no new R19-owned finite mathematical claim exists to validate.

## 4. Method #10 — DERANDOMIZE the successor search

Earlier terminal-wait work used queue probes to test whether apparently free inventory existed. This run replaces that heuristic with the complete changed-file census from the exact 115-commit comparison.

There is one canonical claim mutation and it is P0462. P0462 is genuinely OPEN, source-exact, and CLOSABLE, but its claim is exclusive to R7-05. Therefore its admission indicator for R19 is

`1 * 1 * 1 * 1 * 0 = 0`.

This deterministic census removes any dependence on which queue rows happen to be sampled. The independent R06 successor gate in the same repository state reaches the same conclusion: P0462 is attractive and CLOSABLE but owned, and no free READY CLOSABLE successor is exposed.

**Outcome #10:** `E_READY_SUCCESSOR` stays `0`.

## 5. Method #18 — SAY IT IN ANOTHER LANGUAGE

Rewrite the successor problem as a finite-state automaton rather than a prose queue:

- `PENDING`: source candidate exists but one or more admission literals are unresolved;
- `READY_FREE`: source/current/scope/category checks pass and canonical ownership is clear;
- `CLAIMED`: canonical exclusive owner exists;
- `RETIRED_OWNER_ROUTE`: a worker stopped, but ownership is unchanged unless the canonical claim mutates;
- `RELEASED`: canonical ownership record explicitly clears or reassigns the owner;
- `EXCLUDED/KNOWN/POSTED`: no research dispatch;
- `HARD`: outside source may be open but fails R19's CLOSABLE lane.

P0462 transitions directly into `CLAIMED`, not `READY_FREE`: its admission record and canonical claim were created for R7-05. The fact that a target is newly discovered does not create an intermediate free interval that R19 may race into after the canonical claim exists.

A second source-faithfulness screen in the same delta makes the value of this language clearer. Candidate F0022 (Beffara–Duminil-Copin planar percolation Question 1) has **no canonical claim**, but the fresh screen shows that the literal printed endpoint is already false for the elementary singleton-cluster event: `kappa(p) >= p(1-p)^6`, hence `liminf_{p->1/2} kappa(p) >= 1/128`, while the printed power tends to zero. The likely intended background-subtracted `8/3` singularity is a different HARD question, and no explicit author correction was recovered. Thus `owner_clear=1` does not matter: F0022 fails source-faithful current-CLOSABLE admission and is correctly `NOT_ADMITTED`.

**Outcome #18:** neither the new claimed target nor the unclaimed scope-defective target is lawful R19 inventory.

## 6. Method #29 — ADD THE POINTS AT INFINITY to lifecycle semantics

The recurring operational error is to treat terminal worker states as if they were ownership states. Compactify the lifecycle by adjoining explicit boundary states for `RELEASED` and `CLAIMED`; then a local worker trajectory ending at `HANDOFF` or `RETIRED` has a well-defined boundary value only through the canonical claim file.

This resolves three superficially similar events:

1. **P0462:** born at the `CLAIMED` boundary, CLOSABLE but occupied.
2. **P0458:** owner-side six-run retirement in prior evidence, but no canonical release; its boundary remains occupied.
3. **Campbell–O'Rourke Q1.8:** prior canonical file genuinely reached `UNASSIGNED`, but the source remains HARD and therefore still fails R19's lane gate.

The compactified lifecycle prevents a terminal handoff from masquerading as a free point at infinity. Only an explicit canonical release/reassignment can change ownership clearance.

**Outcome #29:** no lawful CLOSABLE release is present in the complete interval.

## 7. I0084 source/current-literature refresh, dated 2026-09-19

Primary-source check: current arXiv HTML for `https://arxiv.org/html/1710.08240v2` still identifies v2 as 14 September 2018. At Conjecture 5.5 it literally says that `S_t` is the law of a **classical or free alpha-stable process**, assumes the exact `(2+alpha)` moment, and concludes that `mu * S_t` is eventually unimodal. This is the frozen target. The published ALEA text instead uses separate classical/free processes and `mu*S_t` / `mu boxplus T_t`; that later wording is materially different and is not silently substituted into this audit scope.

Dated bounded queries checked this run included:

- `Hasebe Ueda arXiv 1710.08240 Conjecture 5.5 eventual unimodality classical free alpha stable`;
- `"1710.08240" Hasebe Ueda unimodality stable 2025 2026`;
- `"Conjecture 5.5" Hasebe Ueda unimodality stable`.

Recovered results included the original Hasebe–Ueda paper and later related Hasebe/Ueda work on multiplicative/free unimodality, but I did not locate a later primary source explicitly resolving the exact frozen arXiv-v2 ordinary-`*` statement. This is **bounded negative search evidence only**, not a novelty certificate or proof that the worldwide literature contains no resolution.

Access limit: web/arXiv search and repository citation searches were available; no exhaustive citation-database subscription was available, so “not located” is the only justified literature conclusion.

## 8. Audit gate refresh

The newest P26 report visible before this write is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_18-00-45__run-report.md`.

It moves P26's global reconciliation metric by completing the R04 block-GOE C2 audit pair. It does **not** contain a frozen-arXiv ordinary-`*` I0084 end-to-end PASS. Its own continuity section also treats several other current one-of-two packages, none of which is I0084.

Therefore the I0084 version-matching audit gate remains:

- P26 frozen ordinary-`*` end-to-end audit: **missing**;
- distinct OTHER-track frozen ordinary-`*` end-to-end audit: **missing**;
- gate: **0/2**.

The old R18 classical finite/symbolic-core PASS is not an end-to-end frozen package audit, and the R18/P26 ALEA free-`boxplus` end-to-end passes remain version-mismatched.

## 9. Scheduler/model-control status

The current repository implementation record still says the exposed scheduler has **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort telemetry, and no guaranteed one-hour execution setting**. Thus the requested `GPT-6 / maximum` remains prompt text only; this run actually reports GPT-5.6 Sol with reasoning level UNVERIFIED and makes no contrary claim.

The historical P26 native ID `6aa7b43682948191b697d72fec69d539` once returned `You cannot modify this task` from one context. The current `RESULTS.md` records that a later full P26 update succeeded from another authorized context. Therefore the denial is authorization-context-specific. The lawful remedy is to use the owning/authorized scheduler context, a supported ownership transfer, or platform/admin support. There is no permission bypass. Making GPT-6/maximum binding would require the scheduler/product/API itself to persist model and reasoning fields and attest the applied route per run.

No scheduler change was attempted in this run.

## 10. Result and next lawful trigger

No I0084 theorem work was reopened. No successor was claimed. No shared root or peer-track file was edited.

R19 remains

`TERMINAL_WAITING_FOR_NEW_READY_DELTA`.

The next lawful trigger is exactly one of:

1. a genuinely owner-clear, source-current, nonposted **CLOSABLE OUTSIDE** target appears and survives exact source/scope/prior-attempt checks; or
2. the two missing frozen-arXiv ordinary-`*` I0084 end-to-end audits arrive, at which point the existing minimal endpoint-refutation package can be closed/packaged without inventing another mathematical lemma.

## structured ledger_delta

```yaml
ledger_delta:
  track: R19
  source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / I0084"
  source_version_scope: "frozen arXiv v2: ordinary classical convolution mu*S_t for both classical/free stable kernels"
  fixed_metric: "number of complete classical-stable/free-stable alpha=1/2 source branches in retained full-input/original-skewness scope"
  metric_before: "2/2"
  metric_after: "2/2"
  metric_movement: "NO MOVEMENT"
  mathematical_verdict: "SOURCE_REFUTED_IN_RETAINED_ALPHA_HALF_ENDPOINT_SCOPE"
  repository_status: "PARTIAL / AUDIT_PENDING / TERMINAL_WAITING_FOR_NEW_READY_DELTA"
  unchanged_count: ">=6 at I0084 handoff; terminal-wait invocations are not counted as renewed theorem runs"
  successor_gate_metric: "E_READY_SUCCESSOR"
  successor_gate_before: 0
  successor_gate_after: 0
  tried_moves: [10, 18, 29]
  method_cycle: "SECOND-CYCLE REUSES; all 30 Section-B moves previously exhausted"
  material_repo_delta:
    base: "d75a7113609040f6444e749ab1612e6dc5280c37"
    frozen_prewrite_head: "1828487bb0a01e783ac1041a4a024210a043e318"
    commits_ahead: 115
    commits_behind: 0
    too_large: null
    canonical_claim_mutations:
      - "P0462 added: CLOSABLE OUTSIDE / OPEN / exclusive owner R7-05"
  admission_near_misses:
    P0462: "CLOSABLE but owner_clear=false; exclusive R7-05 claim"
    F0022: "unclaimed but NOT_ADMITTED; literal source refuted, plausible intended statement scope-changed/HARD"
  remaining_obligation: "P26 frozen-arXiv ordinary-* end-to-end PASS + one distinct OTHER-track frozen-arXiv ordinary-* end-to-end PASS, OR a new owner-clear READY CLOSABLE successor"
  i0084_audit_gate: "0/2 version-matching end-to-end audits"
  preserved_evidence:
    - "artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md"
    - "runs/R19/2026-09-16_13-40-24_UTC__i0084-halfstable-lefttail.md"
    - "runs/R19/2026-09-16_17-36-54_UTC__i0084-skewness-classification.md"
    - "runs/R19/2026-09-16_18-45-28_UTC__i0084-light-tail-endpoints.md"
    - "operations/claims/P0462.md"
    - "research7_2026-09-17/R7-01/admission/2026-09-19T151417Z__F0022_literal_endpoint_screen.md"
    - "proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_18-00-45__run-report.md"
  prior_audit_ids_preserved:
    - "R18-I0084-C001=PASS (finite/symbolic classical core only)"
    - "R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF (ALEA/free-boxplus scope; version-mismatched)"
    - "R18-AUDIT-R19-I0084-C010-ABSTRACT-004=PASS_FULL_MATHEMATICAL_PROOF (abstract sparse-bump theorem only)"
    - "P26-AUDIT-R19-I0084-C002-ENDTOEND-06=PASS_FULL_MATHEMATICAL_PROOF/PUBLISHED_ALEA_SCOPE (version-mismatched)"
  new_checker: false
  claim_created_by_R19: false
  shared_roots_edited: false
  peer_files_edited: false
  scheduler_modified: false
```
