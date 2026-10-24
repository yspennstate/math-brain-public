Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. TERMINAL HANDOFF / ROTATION: no metric movement, `d_bad = +∞ -> +∞`; Section-B methods #4, #20, and #28 were genuinely attempted as diagnostic routes, and the sixth consecutive unchanged CLOSABLE run now retires P0411 from active NM13-05 research.**

# NM13-05 run report — P0411 terminal handoff at six unchanged runs

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-05` / `proofnet24/NM13-05/`  
Category: **CLOSABLE OUTSIDE**  
Canonical source / claim ID: `P0411`  
Canonical dedup key: `boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells`  
Canonical SHA-256: `55ed478fc4a65273f15d74d172f46ee938595061ac9a7d82ad3a03afcfd6c1cc`  
Selection shard: **4 mod 13**  
Frozen source family: `R_d = d_H(o, ∂C_d)`, `d >= 2`, the origin-to-boundary distance in the IPVT zero cell  
Frozen metric: `d_bad = min{d >= 2 : g_d is not nonincreasing on [0,∞)}`, with `d_bad = +∞` if there is no such dimension  
Metric before / after: **`+∞ -> +∞`**  
Mathematical progress this run: **NO MOVEMENT**  
Unchanged-run counter: **`5 -> 6`**  
Stuck-recovery counter: **`1 -> 1`**  
Research disposition after this run: **TERMINAL_HANDOFF / ROTATED_FROM_ACTIVE_P0411_RESEARCH**  
Successor status: **ADMISSION_PENDING**, successor metric **`UNMEASURED -> UNMEASURED`**

## 1. Runtime / scheduler truth

The prompt requests GPT-6 at maximum reasoning, but that setting is not bindable from the exposed scheduler/task-control surface. The actual runtime model visible to this report is **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or an escalation.

The exposed task controls still provide prompt/title, schedule/start, timing mode, enabled state, listing, and update operations, but no model-family selector, no reasoning-effort selector, and no authenticated applied-runtime attestation. Enforcing GPT-6/maximum would require an authorized product/workspace/API/admin surface that persists explicit model/reasoning fields and returns applied-runtime telemetry. The historical P26 `You cannot modify this task` event was authorization-context specific: the current `RESULTS.md` records that a later authorized context successfully updated P26. The compliant remedy for a future denial is therefore the owning/otherwise-authorized context or authorized platform/admin support, never duplication or permission bypass. No schedule/control-plane mutation was attempted in this run.

## 2. Required continuity read and frozen pre-write state

This invocation re-read the current controlling and exclusion state before acting:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later deployment/amendment material, including `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0411.md`;
- newest NM13-05 report;
- newest neighboring NM13-06 report;
- newest P26 audit report;
- relevant intake/campaign source and attempt history and current claim/search hits.

The preceding NM13-05 creation commit was `1b6d281759afa57ce85eb2a0def0b955dfbbe068`. The final frozen pre-write `master` used for the delta check was `a2dd73bebc651e9f6393d757d6e78d01deee8d18`. Exact Git comparison reports **101 commits ahead, 0 behind, `too_large = null`**, so the changed-file set is complete. That delta contains substantial fleet work but no edit or deletion of `operations/claims/P0411.md`, no P0411 audit report from P26 or NM13-06, and no authorized P0411 ownership release.

The canonical P0411 claim therefore remains protected. **This terminal handoff is not an ownership release.** A disabled/inaccessible task never releases ownership, and this report does not make P0411 freely assignable under another ID. It records that NM13-05 must stop active research on this target under the six-unchanged-run rule. Any later release/reassignment must be an explicit authorized ownership action, not inference from inactivity or this handoff.

## 3. Why this run must rotate rather than add another lemma

The preceding report explicitly recorded unchanged counter `4 -> 5` and warned that the next unchanged P0411 invocation would hit the CLOSABLE six-run rotation threshold. No closure-enabling event arrived in the complete delta:

- P26 P0411 full-proof audit PASS: **absent**;
- NM13-06 P0411 full-proof audit PASS: **absent**;
- source-author correction / erratum changing the displayed-variable interpretation: **not recovered**;
- frozen density metric improvement beyond `d_bad=+∞`: mathematically impossible under the frozen metric because `+∞` is already the terminal value.

The owner directive and `RESULTS.md` require CLOSABLE targets to retire/rotate after six unchanged runs. Therefore this invocation does **not** manufacture a seventh P0411 lemma. It freezes a handoff and returns the worker to successor admission.

## 4. Section-B diagnostic methods actually attempted

### #4 — PROVE SOMETHING WEAKER, COMPLETELY

I reduced the source-matching closure package to the weakest claim that already decides the literal positive-coefficient clause: the archived exact `d=2` coefficient obstruction. Under the source's displayed-`u` reading,

`[u^6] e^{-u}/H_2(u) = 61/240 - 4/(5π) = (61π-192)/(240π) < 0`.

That finite statement is sufficient to refute the literal even-dimensional positive-coefficient assertion; the later all-even Pringsheim theorem, exact Maclaurin radius, and infinite sign-change theorem are strengthenings, not prerequisites for the source-level refutation. Outcome: **the minimal mathematical route is already present; another owner-track proof does not move the frozen metric or remove the audit gate.** No new theorem is claimed this run.

### #20 — FIND WHY THE ALGORITHM FAILS

The closure algorithm fails after owner-track mathematics for a precise non-mathematical reason: the protocol requires two independent outside audits, and neither designated auditor has supplied a P0411 PASS. The source-interpretation risk is likewise external: the paper literally uses `u`, while a hypothetical author clarification to a transformed variable would be a different claim; no such correction was recovered. Outcome: **the remaining blockers are independent validation and source-intent confirmation, not an identified missing NM13-05 lemma.** Repeating owner proofs is therefore the wrong algorithm.

### #28 — REPLACE “FOR ALL” WITH “FOR TYPICAL”

I tested whether a weaker “typical dimension” or “eventually/typically positive coefficient” interpretation could rescue the source without an author correction. It cannot: that would replace the source's literal universal even-dimensional positive-coefficient clause with a new statement. Moreover the existing exact `d=2` witness already kills the literal conjunction. Outcome: **reject the weakening as source-invalid rather than relabeling it a solution.**

These are genuine diagnostic uses of new Section-B moves. They produced no theorem-sized new claim, as required at the rotation boundary.

## 5. Terminal mathematical handoff for P0411

### Exact source status carried forward

The source is D'Achille–Curien–Enriquez–Lyons–Ünel, *Ideal Poisson–Voronoi tessellations on hyperbolic spaces*, published in *The Annals of Probability* 54(2) (2026), DOI `10.1214/25-AOP1781`. The campaign records P0411 as partial/reduced rather than posted/closed. The canonical claim was admitted by NM13-05 only after residue, ownership, source, attempt, and exclusion checks.

### Preserved prior campaign result, not NM13-05 discovery

Campaign attempt `P0411-A001` and `probability_campaign_2026_09/codex_20h_20260906/proofs/IPVT_boundary_hole_partial.md` already record the exact `d=2` negative sixth Maclaurin coefficient under the displayed-`u` interpretation. That earlier result must remain attributed to the campaign and must not be re-labelled as an NM13-05 discovery.

### NM13-05 mathematical package to hand off

The immutable NM13-05 reports contain, in order:

1. all-dimensional decreasing boundary-distance density, proving the frozen value `d_bad=+∞`;
2. strict IFR / strict log-concavity of survival, hazard bounds and endpoint/tail asymptotics;
3. an all-even-dimensional positive-coefficient obstruction via the branch point and Pringsheim;
4. exact Maclaurin radius `π/2` and infinitely many coefficient sign changes in every even dimension;
5. a source-reading/stuck diagnosis isolating the literal-`u` interpretation and audit blocker;
6. an exact small-even self-check, independently from the radial integral, certifying first negative coefficient degrees `6,17,28,40` for `d=2,4,6,8` and reproducing the exact `d=2` coefficient.

The exact self-check artifacts are:

- `proofnet24/NM13-05/artifacts/2026-09-19/p0411_small_even_audit.py`;
- `proofnet24/NM13-05/artifacts/2026-09-19/p0411_small_even_audit.out`, ending `ALL_EXACT_CHECKS_PASS`.

They are **self-checks**, not independent audits.

### Honest mathematical/protocol labels at handoff

- frozen density metric: **PROVED candidate**, `d_bad=+∞`;
- literal even-dimensional positive-coefficient clause in displayed `u`: **REFUTED under the literal source reading** by the exact `d=2` coefficient, with stronger all-even support in NM13-05;
- full source package / fleet protocol status: **NOT CLOSED**;
- independent audits: **0/2**;
- P26 audit PASS: **missing**;
- NM13-06 audit PASS: **missing**;
- prior-art status: bounded checks only, no worldwide novelty certificate;
- source-interpretation risk: retained until an author correction/erratum or authoritative clarification is found.

### Remaining obligations for any authorized future closer

A future authorized continuation should not restart the mathematics. It should first obtain independent full-proof audits of the minimal source-matching package from P26 and NM13-06 (or another explicitly authorized independent auditor if policy changes), including: (i) source wording and displayed variable; (ii) exact `d=2` coefficient sign; (iii) the all-dimensional density proof if that theorem is to be packaged; (iv) separation between prior campaign work and NM13-05 strengthenings; and (v) bounded prior-art search with folklore/classical ingredients labelled as such. Only then can protocol closure or paper packaging be considered.

## 6. Fresh bounded literature / source-status check — 2026-09-19

Queries were bounded to the original title/authors, IPVT boundary-distance / hole monotonicity, Conjecture 7.5, positive coefficients, erratum/correction, later author papers, and citing/related 2026 IPVT papers. Recovered items include:

- the original Annals publication, DOI `10.1214/25-AOP1781`, publication date recorded as 2026-03-06;
- D'Achille–Thäle, *Face volume densities of Poisson hyperplane tessellations and ideal Poisson–Voronoi tessellations*, 2026-06-24 — a different face-volume problem;
- D'Achille–Khezeli, *Convergence towards Ideal Poisson--Voronoi tessellations with a focus on Diestel--Leader graphs*, arXiv:2606.30517, 2026-06-29 — convergence / graph applications, not this boundary-distance coefficient clause;
- Mellick, *Indistinguishability of cells in Poisson–Voronoi tessellations*, 2026 — a different source question.

No retrieved item supplied an erratum, transformed-variable correction, or source-matching resolution of the P0411 boundary-distance coefficient clause. This is **bounded negative evidence only**, not proof of worldwide openness, novelty, or priority.

## 7. Successor admission state after rotation

No successor claim is created in this run. Rotation does not license opportunistic ownership: every successor must again pass exact-source, current-literature, prior-attempt, dedup/alias, historical/current ownership, handoff/retirement, POSTED/campaign exclusion, and residue-4 checks before `operations/claims/<ID>.md` is created.

The durable static legacy screening cursor recovered before P0411 admission was:

`LEGACY_P_RECONCILIATION_NEXT=P0286`.

That cursor is restored as the lawful successor-screening continuation point. The successor state is therefore:

- status: **ADMISSION_PENDING**;
- successor metric: **`UNMEASURED -> UNMEASURED`**;
- successor mathematical progress this run: **none**;
- screening cursor: **`LEGACY_P_RECONCILIATION_NEXT=P0286`**;
- initial successor Section-B methods #2, #8, #11: **NOT TRIED** and must remain so until an eligible residue-4 source actually crosses admission;
- no claim file created, overwritten, or released.

The next invocation should continue canonical legacy P-series reconciliation from P0286, then reconcile newer intake/delta candidates, always hashing the source's canonical `dedup_key` rather than an alias. If no candidate passes, retain an advanced screening cursor and continue to report ADMISSION_PENDING without counting screening as mathematics.

## 8. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  worker: NM13-05
  namespace: proofnet24/NM13-05
  category: CLOSABLE_OUTSIDE
  source_id: P0411
  claim_id: P0411
  canonical_dedup_key: boundary-hole_monotonicity_and_coefficient_positivity_for_ideal_cells
  shard_mod_13: 4
  run_disposition: TERMINAL_HANDOFF_ROTATE
  metric_name: d_bad
  metric_before: +infinity
  metric_after: +infinity
  mathematical_movement: false
  unchanged_runs_before: 5
  unchanged_runs_after: 6
  stuck_recoveries_before: 1
  stuck_recoveries_after: 1
  methods_attempted:
    - 4
    - 20
    - 28
  method_outcomes:
    4: minimal source-matching d=2 refutation already complete; no new theorem needed
    20: closure algorithm blocked by missing independent audits and source-intent confirmation, not owner mathematics
    28: typical/eventual weakening rejected as source-invalid
  mathematical_status:
    density_metric: PROVED_CANDIDATE
    literal_u_positive_coefficient_clause: REFUTED_LITERAL_READING
    fleet_closed: false
  audit_status:
    P26: MISSING
    NM13_06: MISSING
    independent_passes: 0
    required_passes: 2
  ownership:
    canonical_claim_unchanged: true
    released: false
    steal_permission_created: false
  successor:
    status: ADMISSION_PENDING
    metric_before: UNMEASURED
    metric_after: UNMEASURED
    cursor: LEGACY_P_RECONCILIATION_NEXT=P0286
    initial_methods_2_8_11_tried: false
  bounded_literature_check_date: 2026-09-19
  source_correction_found: false
  next_step: continue canonical residue-4 successor reconciliation from P0286; create no claim until exact source/current-status/prior-attempt/exclusive-ownership gates pass
  scheduler_changed: false
  shared_roots_edited: false
  peer_files_edited: false
  D_series_edited: false
  public_posting: false
  email_or_drive: false
  paid_compute: false
```

## 9. End state

P0411 is now a **terminal handoff from active NM13-05 research because the sixth consecutive unchanged frozen-metric run has occurred**. The mathematical record is preserved; ownership is not silently released; protocol closure is not claimed; and no more P0411 lemmas should be generated by this lane absent a later explicit authorized reassignment. NM13-05 returns to **ADMISSION_PENDING** with cursor `LEGACY_P_RECONCILIATION_NEXT=P0286`.
