Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; Section-B methods #2/#4/#8 remain genuinely unspent because no successor crossed admission.**

# NM13-11 — legacy-P cursor repair, residue-10 screen 17

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: `HARD OUTSIDE`  
Exclusive shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 10`

## 1. Runtime truth and task-control surface

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. The exposed runtime gives no authenticated reasoning-effort telemetry, so reasoning is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control API still has prompt/title, schedule or relative-start data, timing mode, enabled state, listing and update operations, but **no bindable model-family field, no bindable reasoning-effort field, and no authenticated per-run attestation of the applied model/effort**. Thus `GPT-6 / maximum` remains prompt text only in this scheduler surface. Making it binding would require an authorized product/workspace/API scheduler surface that persists model-family and reasoning-effort fields into inference routing and exposes trustworthy run attestation.

The historical P26 `You cannot modify this task` response is treated as an authorization/context boundary. The lawful workaround is the task-owning or otherwise-authorized workspace/account/API/admin context (or authorized platform support), not task duplication or permission bypass. This run did not test that boundary by modifying any schedule because schedule changes are expressly forbidden here.

## 2. Continuity recovered and a material correction to the old cursor

The controlling NM13-11 predecessor is

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T03-57-00Z__post-static-admission-delta-screen-16-p0169-owned-offshard.md`

at creation commit

`cb75861303619fae5a804f20f1093b4261a2de65`.

Its durable state is preserved except for one screening-cursor correction proved below:

- status `ADMISSION_PENDING`;
- successor metric `UNMEASURED`;
- Section-B methods #2 ATTACK THE NEGATION FIRST, #4 PROVE SOMETHING WEAKER COMPLETELY, #8 DISCRETIZE genuinely unspent;
- successor unchanged-run / stuck-recovery counters `NOT_STARTED` because no successor is admitted;
- E0082 remains terminal for NM13-11, ownership-preserved, with historical `unchanged_runs=4` and `stuck_recoveries=2/2 consumed`; it is not reopened;
- F0072 and E0107 remain retained `PENDING / NOT READY` sentinels, not claims.

I reread the required policy and fleet surfaces: `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/NEW_METHODS_2026-09-16.md`, later owner-authorized deployment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`, root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md` and `RANKING.md`, the newest own report, newest visible neighboring NM13-10 and NM13-12 reports, candidate-specific source/attempt material, dedup index, and current claims.

A neighboring NM13-04 repair report exposed a real defect in the old static P-series reconciliation: an older legacy row (P0169 for that worker) had been omitted from its supposedly complete static sentinel set. NM13-04 therefore rehashed the authoritative legacy Codex P tranche P0162--P0223 from the canonical keys rather than trusting the earlier cursor. Its exact residue sequence shows that **NM13-11 had also skipped four residue-10 rows**:

- P0165;
- P0167;
- P0187;
- P0197.

This invalidates NM13-11's old `STRICT_DELTA_ONLY_RESIDUE_10` cursor as a completeness certificate. The correction is operational, not mathematical progress. The repaired cursor after this run is

`LEGACY_P_RECONCILIATION_NEXT=P0224`.

No screening below is counted as source-metric movement.

## 3. Canonical identity and shard recomputation

I recovered the canonical dedup keys from the campaign/dedup ledgers before hashing; no display title or ID alias was hashed.

| ID | canonical dedup key | SHA-256 | mod 13 |
|---|---|---|---:|
| P0165 | `optimal_odd_functions_for_many-player_correlation_distillation` | `48351e02df296bfc684d81501304d7cfb6051cbc76f47ded41f081eb07f9452a` | 10 |
| P0167 | `minimum_correlation_of_symmetric_gaussian_sets` | `e56fa47f45473a1be7d7248466a312cfd2f947d4f79ad5d0bbce945cb81f33d2` | 10 |
| P0187 | `optimal_edge-fluctuation_scales_for_arbitrary_random-matrix_polynomials` | `8846b1ec02e75f883ab9dcb00f8e429685f774a0bb8efc9dfa5b589413f72b67` | 10 |
| P0197 | `relation_between_ising_relaxation_and_mixing_on_transitive_graphs` | `443ec859abf93124821601786782b53e9a423e8332798f8f83a49d8c1f4ad18d` | 10 |

The P-series canonical-source record is the Codex campaign ledger; the F intake dedup index independently recovers the same normalized keys. The old Claude rank sheet is an attempt-summary surface, not the canonical identity authority.

## 4. Ownership and historical-attempt gate

Direct current claim-path checks for `operations/claims/P0165.md`, `P0167.md`, `P0187.md`, and `P0197.md` are absent / 404. Exact-ID and exact-key repository searches recovered intake/catalog/attempt history and the NM13-04 cursor-repair reference, but no current proofnet24 owner, owner-slot assignment, nonterminal handoff, or canonical claim for these four IDs. In particular, exact searches for `P0165 proofnet24`, `P0167 proofnet24`, and `P0187 proofnet24` returned no owner report; `P0197 proofnet24` recovered the NM13-04 reconciliation rather than an assignment.

This is evidence that the four are presently unclaimed, but **absence of a claim path alone is never treated as READY**. All four have historical campaign state `attempted_unsolved`, so they are not “previously unattempted.” Their prior attempts were read before deciding admission:

- **P0165:** rewrite the r-player agreement probability through `m=T_rho f`; the exact `r=2,3` algebra does not jointly optimize the higher moments required for `r>=4`.
- **P0167:** for fixed `A`, optimize `B` as a sublevel set of `T_rho 1_A`; this eliminates one set but leaves a nonlinear optimization over symmetric `A`.
- **P0187:** a degenerate one-variable quadratic polynomial shows a nondegeneracy qualifier is necessary; it does not establish universal `N^{-2/3}` edge fluctuations for arbitrary noncommutative matrix polynomials.
- **P0197:** at zero interaction the heat-bath spectrum gives the product-chain baseline (`t_rel` of order `n`, `t_mix` of order `n log n`), but vertex transitivity does not control the interacting chain's multiplicities or nonlinear slow observables.

No disabled or inaccessible schedule, stale admission flag, missing claim path, or old attempt status was interpreted as release or ownership.

## 5. Exact source checks and bounded current-literature status

### 5.1 P0197 — strongest subject match, but not admission-ready

This is the closest match to the requested interacting-particle / spin-dynamics focus. The original source is Levin--Peres--Wilmer, *Markov Chains and Mixing Times*, second edition, Chapter 26, Question 4. The live source wording is:

> for the Ising model on transitive graphs, is relaxation time of order `n` if and only if mixing time is of order `n log n`, as temperature varies?

The source notes the two-dimensional torus as known. The PDF text was fetched and the source page was targeted for visual verification; the screenshot backend returned a cache-miss for that external PDF, so visual inspection of that page is an **access limitation** of this run, while the parsed source page/line text itself was accessible.

Fresh 2026-09-19 bounded searches recovered substantial adjacent progress, including optimal/high-temperature Glauber results on bounded-degree graph classes, random-regular-graph phase results, Curie--Weiss/complete-graph results, and 2025--2026 sparse/random-field Ising mixing work. I did **not** recover a checked later primary source explicitly proving the full LPW Question 4 equivalence on all transitive graph families. This is bounded negative evidence only, not a worldwide-openness or novelty certificate.

**Admission failure:** despite its strong subject fit, the literal source asks an asymptotic iff across graph families and temperature regimes. It does not specify a source-fixed critical parameter, interval endpoint, finite certificate, or one scalar whose certified interval NM13-11 can honestly move now. The previous zero-interaction special case is already in the attempt ledger. Choosing an arbitrary graph family or beta interval as the official tracked quantity would silently invent a residual metric rather than freeze one from the source. Therefore P0197 is **PENDING / NOT READY**, not claimed.

### 5.2 P0165 — exact discrete source, but the obvious finite metric would be invented

O'Donnell's 2012 *Open Problems in Analysis of Boolean Functions* gives the exact statement: for fixed `r`, odd `n`, and `0<epsilon<1/2`, does some odd-input Majority `Maj_k` maximize the r-player agreement probability among odd Boolean functions? The source itself records that neither dictator nor full majority need maximize (e.g. `r=10,n=5,epsilon=.26`). The exact source page was visually inspected in this run.

Fresh bounded searches did not recover a checked later paper resolving the full all-`r,n,epsilon` problem. That is not a proof of worldwide openness.

**Admission failure:** finite exact enumeration for one `(r,n,epsilon)` would be a legitimate experiment/special case but not the literal quantified source question, and the natural quantities “largest n verified” or “largest r verified” are not source-fixed metrics. Freezing one would require owner authorization of that special-class milestone. P0165 remains **PENDING / NOT READY**.

### 5.3 P0167 — later positive and negative structure, but still a broad variational function

O'Donnell's source asks, for prescribed `rho,mu,nu`, for the minimum correlated-Gaussian intersection probability under central symmetry. The exact source page was visually inspected. Later primary literature materially changes the naive conjectural picture: Heilman's *Low Correlation Noise Stability of Symmetric Sets* proves one-dimensional small-correlation results and shows in dimension at least two that balls/complements are not always extremizers. A 2023/2024 paper of Fusco--La Manna studies a related symmetric-Gaussian variational conjecture and again shows dimension-sensitive behavior.

**Admission failure:** the source asks for an entire variational function over `(rho,mu,nu,n)`. It does not single out a fixed triple or a finite decision problem. Choosing a convenient parameter triple would be a new subproblem, not recovery of a source-fixed quantitative milestone. P0167 remains **PENDING / NOT READY**.

### 5.4 P0187 — too underspecified for this worker's quantitative gate

The campaign source records a 2025 strong-convergence survey, Section 6.7 p.69, asking under “suitable nondegeneracy assumptions” for the `N^{-2/3}` edge-fluctuation scale and limiting edge law for norms of arbitrary-degree random-matrix polynomials. The prior attempt already identifies that the nondegeneracy qualifier is load-bearing.

Fresh bounded searches found active 2025--2026 edge-universality work but no checked source-level theorem eliminating the source's broad qualifier for arbitrary matrix polynomials. Again this is bounded negative evidence only.

**Admission failure:** the problem is outside the preferred subject and, more importantly, its hypothesis class itself is not source-frozen (“suitable nondegeneracy”). There is no honest finite/scalar endpoint to track without first redefining the theorem. P0187 is **PENDING / NOT READY**.

## 6. Delta since the predecessor

The final prewrite `master` head captured immediately before this report was

`50b7220ada9c880fc4a7599c7b3dd921c61efe4c`.

The predecessor-to-prewrite compare from `cb75861303619fae5a804f20f1093b4261a2de65` was **105 commits ahead and 0 behind**. The interval contains substantial peer research. The material ownership delta for this shard is negative: P0219 gained a canonical claim owned by another worker and hashes to residue 11, not 10; no claim deletion or owner-authorized source release makes residue-10 inventory available. Root selection surfaces and the legacy candidate source records used here were read at current master.

The key material change for NM13-11 is not a new free claim but the **neighbor-discovered legacy-P cursor defect**, which required reopening static screening rather than continuing delta-only mode.

## 7. Admission decision and methods accounting

**Decision: `ADMISSION_PENDING`. No canonical `operations/claims/<ID>.md` is created.**

P0197 is now the strongest residue-10 subject sentinel because it is genuinely interacting-spin dynamics and apparently unclaimed, but it fails the mandatory frozen-quantitative-milestone gate. P0165 and P0167 are mathematically concrete but would require inventing a fixed sub-parameter metric; P0187 is broader and less suitable. A pending lead is not READY.

Because no successor crossed admission, this invocation did **not** perform Section-B methods #2/#4/#8 on a claimed problem. Marking them “tried” would be false. Screening and literature triage are not counted as mathematical progress. No checker or theorem artifact was manufactured.

The next screening cursor is therefore:

`LEGACY_P_RECONCILIATION_NEXT=P0224`

rather than the now-invalid `STRICT_DELTA_ONLY_RESIDUE_10`. The next invocation should continue deterministic canonical-key reconciliation from P0224 onward before returning to delta-only mode. If a later residue-10 source provides a literal finite or quantitative milestone and passes exact source/current-literature/attempt/ownership gates, claim creation must still be create-only and read back before substantive work begins.

## 8. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  category: HARD_OUTSIDE
  status: ADMISSION_PENDING
  source_id: NONE
  claim_id: NONE
  claim_path: NONE
  metric_name: successor_source_metric
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  mathematical_movement: false
  screening_counts_as_progress: false
  section_B_methods:
    requested: [2, 4, 8]
    actually_tried: []
    state: UNSPENT_NO_ADMITTED_SOURCE
  successor_unchanged_runs: NOT_STARTED
  successor_stuck_recoveries: NOT_STARTED
  terminal_predecessor:
    source_id: E0082
    ownership_preserved: true
    unchanged_runs: 4
    stuck_recoveries: 2
    restart_allowed: false
  cursor_before: STRICT_DELTA_ONLY_RESIDUE_10
  cursor_correction_reason: neighboring_NM13-04_found_legacy_P_static_omission
  repaired_residue10_rows_screened: [P0165, P0167, P0187, P0197]
  candidate_outcomes:
    P0165: PENDING_NOT_READY_metric_not_source_fixed
    P0167: PENDING_NOT_READY_broad_variational_parameter_family
    P0187: PENDING_NOT_READY_hypothesis_class_not_source_frozen
    P0197: PENDING_NOT_READY_strong_subject_match_but_no_source_fixed_quantitative_milestone
  retained_sentinels:
    F0072: PENDING_NOT_READY
    E0107: PENDING_NOT_READY
    P0197: PENDING_NOT_READY
  next_cursor: LEGACY_P_RECONCILIATION_NEXT_P0224
  predecessor_report_commit: cb75861303619fae5a804f20f1093b4261a2de65
  frozen_prewrite_head: 50b7220ada9c880fc4a7599c7b3dd921c61efe4c
  commits_ahead: 105
  commits_behind: 0
  canonical_claim_created: false
  substantive_artifact_created: false
  audits:
    P26: NOT_APPLICABLE
    NM13-12: NOT_APPLICABLE
```

## 9. Scope and safeguards

The external literature searches above were bounded by accessible web indexing and fetched primary/near-primary sources. Failure to find a resolution is not proof of worldwide openness. GitHub code search is also not a substitute for a forensic scan of every historical commit; direct current claim-path checks, exact canonical-key/ID searches, campaign attempt history, current ledgers, and neighboring handoff reports were used together. Any inaccessible history is therefore treated conservatively against admission.

This invocation creates exactly this one immutable own-namespace report. It edits no shared root, peer namespace, canonical claim, schedule, permission, workflow, public surface, email/Drive resource, or paid-compute resource.
