Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / no mathematical movement. Section-B methods #2, #4, #27 were NOT TRIED because no lawful CLOSABLE OUTSIDE source was admitted; screening is not mathematical progress.**

# NM13-09 — second admission screen

Date: 2026-09-17 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Own namespace: `proofnet24/NM13-09/`  
Captured master before delivery: `e3f8790b307b2ee0785f08a5914fbe374a935f1e`

## 1. Runtime/model control

The actual runtime is GPT-5.6 Sol. The reasoning-effort level is not authenticated by an exposed selector or telemetry and is therefore **UNVERIFIED**. The task prompt requests GPT-6 / maximum reasoning, but the exposed automation surface has no binding model selector or reasoning-effort selector. I do not claim the requested model/reasoning was enforced, and I do not claim hour-long execution.

## 2. Continuity recovered

This run continued from the first immutable NM13-09 report rather than restarting:

- `proofnet24/NM13-09/runs/2026-09-17/2026-09-17T20-44-00Z__admission-screen.md`;
- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- current claims and handoffs for candidates that survived the shard screen;
- the newest visible task-health reconciliation available during the run (`operations/task_health/runs/2026-09-17T210000Z/status.md`);
- neighboring NM13 state, including NM13-10's admission-pending report and current claims created by NM13-11/12/13 and other fleet tracks;
- intake ledgers and prior attempts under `probability_1000_intake_D/E/F/G/H_202609*/`.

The current task-health reconciliation reports no free `READY + CLOSABLE + UNASSIGNED` successor at its screened front. That is an operational snapshot, not proof that no deeper intake row can pass admission, so this run advanced the shard cursor rather than stopping.

The first NM13-09 report had already excluded the visible high-priority I-series collisions and Brownian-process conflicts and set the next cursor to non-Brownian F, then E/G/H/C/Codex. This run did not repeat those checks as if they were new.

## 3. Shard rule

This worker may select only a candidate whose **canonical dedup key** satisfies

```text
int(SHA256(UTF-8 canonical_dedup_key).hexdigest(), 16) mod 13 = 8.
```

For rows carrying an explicit `dedup_key`, I hashed that exact UTF-8 string. I did not hash a display title or local alias. H-intake rows lacking a canonical dedup key were not promoted by inventing one; they stay behind the cursor until canonical source identity/deduplication is recovered from authoritative inventory.

## 4. New screening completed in this run

### 4.1 D intake — completed through D0102

The D ledger was screened through its end. The residue-8 candidates recovered in the relevant portions were:

| Candidate | canonical key / scope | disposition |
|---|---|---|
| D0009 | complete-mixability source row | **EXCLUDED / current canonical claim exists**; D-series ownership is preserved. |
| D0010 | complete-mixability source row | **EXCLUDED / current canonical claim exists**; D-series ownership is preserved. |
| D0038 | `bradley_mixing_open_2005::question_10` | **EXCLUDED / claimed and six-run retired handoff** in the current fleet; no reopening of an exhausted source. |
| D0071 | `grimmett_li_saw_2017::question_3.4` | **HARD, not CLOSABLE**: the general golden-mean lower bound for every cubic transitive graph is a theorem-scale infinite-class problem, not a finite certificate/sharp-number target for this slot. |
| D0090 | `ghs_mating_trees_survey_2019::problem_6.11` | **HARD, not CLOSABLE**: conformal welding of two LQG surfaces with distinct gamma parameters is an open structural continuum problem, not an explicit finite construction/counterexample lane. |

No other canonical D row through D0102 had residue 8. In particular, the attractive stochastic-process rows around disordered zero-range processes, KCMs, Bradley mixing, ARW, and Virag operator limits hash to other workers' residues or are already claimed/resolved.

### 4.2 E intake

The residue-8 E candidates recovered in the scan were:

- **E0006** — high-dimensional critical-percolation functional: HARD asymptotic;
- **E0013** — five-species coexistence: HARD interacting-particle-system theorem;
- **E0018** — explicit Markov-process oscillation question: mathematically attractive but **EXCLUDED** because R7-05 already ran the lane to a six-run terminal handoff; no reopening;
- **E0040** — random-matrix fluctuation lower-bound family: broad HARD source scope;
- **E0050** — Matrix Spencer row: excluded by `POSTED.md`/existing Matrix-Spencer work and current ownership/exclusion rules;
- **E0056** — Z2-synchronization SDP tightness: asymptotic HARD threshold theorem;
- **E0076** — polling-discipline classification: broad source classification, no finite source-closing target recovered;
- **E0089** — bootstrap-percolation critical-density concentration: asymptotic HARD;
- **E0113** — Brownian-polymer/KPZ row: HARD and additionally inside the Brownian-family exclusion pressure for this worker.

No E residue-8 row passed the CLOSABLE gate.

### 4.3 F intake

The residue-8 F candidates recovered in the screen were:

- **F0037** — Brownian-family row already excluded in the first NM13-09 report;
- **F0092** — Kalai threshold-circuit/circuit-complexity source: HARD;
- **F0110** — Talagrand's polynomial-majorant problem for up-classes: **source-exact and apparently unclaimed, but not admitted here**; see the fresh check below;
- **F0120** — q-colouring reconstruction on trees: HARD asymptotic phase-classification problem;
- **F0126** — random-walk-in-random-scenery reconstruction for arbitrary recurrent walks: HARD;
- later Sabot–Tournier and KPZ rows checked in the same neighborhood hash to other residues, not residue 8.

#### Fresh source/current-literature check: F0110

Canonical key: `talagrand_small_2016::problem_10.2` (the accessible STOC/preprint version numbers the same statement as Problem 10.3).

Exact source content recovered: for an up-class `A`, define `F_A(t)=-log(1-zeta_t(A))`; `A in C_gamma` means that for every `q` there is a positive square-free polynomial with no constant term majorizing `F_A` globally and satisfying the gamma-scaled tightness inequality at `q`. The source asks whether one universal positive gamma works for **every** up-class. The source itself records that a positive answer would imply its strong spread-measure domination conjecture, and proves only special structural classes via block composition plus the all-coordinates class.

Fresh bounded searches on 2026-09-17/18 used variants of:

- `"C_gamma" Talagrand up-class 2024 2025 2026`;
- `"Problem 10.3" Talagrand up-class C_gamma`;
- `"polynomial majorant" up-class Talagrand C gamma`.

The primary preprint/STOC source was recovered (`https://michel.talagrand.net/preprints/small.pdf`; also an accessible STOC copy). Searches recovered related Kahn–Kalai/Talagrand literature but no later theorem resolving this exact `C_gamma` question. This is **bounded negative evidence only**, not a worldwide-openness claim.

Prior attempt `F0110-A001` was recovered. It already identifies the linear majorant, the real scaled-tightness obstruction, block-composition coverage, and the first genuinely new symmetric threshold case (majority of three). I did not erase that history.

Why no admission: although F0110 is counterexample-shaped in principle, its literal positive direction is a dimension-free theorem over **all up-classes** and is explicitly strong enough to imply a major source conjecture. No source-matching finite witness, sharp constant, or short theorem that could honestly close the literal source was recovered this run, and it is outside the requested stochastic-process focus. Calling it CLOSABLE merely because a finite counterexample could hypothetically exist would violate the portfolio rule. It remains a possible future candidate only if a concrete source-valid finite obstruction or bounded exact subproblem is first established without replacing the original target.

### 4.4 G intake

Two residue-8 rows were recovered:

- **G0002** — canonical claim already belongs to another track and has exhausted/handoff history; excluded;
- **G0007** — current P14 contact-process source; explicitly excluded by this worker's prompt and current claim.

No G admission.

### 4.5 H intake

The H ledger contains several recent stochastic-process candidates but many rows lack a canonical `dedup_key`. I did **not** manufacture hash keys from titles. Current campaign INDEX also records some superficially attractive H rows as already settled/corrected, including the Levy-drift compactness and frog-model factor-four items. H0003 is already owned by NM13-11. The remaining unsolved H rows stay behind the canonical-identity recovery gate.

## 5. Ownership and duplicate-work checks

Repository searches were performed by canonical key, source title, and candidate ID for the survivors above. Current claims and handoffs supersede stale `admitted=true` intake metadata. In particular:

- an exhausted six-run handoff is not an ownership release;
- a disabled/inaccessible schedule is not an ownership release;
- current NM13 claims are excluded from this worker;
- settled/posted campaign rows are excluded even when an older intake row says open;
- Brownian-process assignments remain excluded from NM13-09 as directed.

No `operations/claims/` file was created because no candidate passed every admission gate.

## 6. Mathematical status

There is still **no admitted source problem**, therefore no source-faithful mathematical metric can lawfully be frozen yet.

```text
active_source: NONE
source_status: ADMISSION_PENDING
mathematical_metric_before: UNMEASURED
mathematical_metric_after: UNMEASURED
mathematical_movement: none
```

This is not a zero metric. It is an unmeasured state before admission.

The assigned initial Section-B methods remain reserved for the first admitted target:

- B2 ATTACK THE NEGATION FIRST: **not tried**;
- B4 PROVE SOMETHING WEAKER, COMPLETELY: **not tried**;
- B27 SWAP THE QUANTIFIERS: **not tried**.

Screening and literature checks are not renamed as those mathematical methods.

## 7. Next admission cursor

The cursor now advances beyond:

- the first-run I/Brownian collision screen;
- all accessible E/F/G screening described above;
- the D intake through D0102;
- H rows whose source status/ownership is already decisive.

**Next run:** screen canonical **C-series and Codex/raw-catalog residue-8** rows not already reconciled, prioritizing genuinely `not_attempted` source problems whose literal full statement can plausibly be decided by an explicit process construction, finite-state transition law, finite counterexample, sharp threshold/constant, or a short complete theorem. For H rows without `dedup_key`, first recover canonical source identity from authoritative inventory before hashing. Do not recycle F0110, E0018, G0002, G0007, D0038, D0071, or D0090 absent a material source/ownership/status change.

If no such row passes, retain `ADMISSION_PENDING`; do not lower the CLOSABLE standard simply to fill the slot.

## 8. Delivery/integrity

This is the single immutable run report for this invocation. No checker/artifact was warranted because no mathematical target was admitted. No shared root ledger, peer file, claim, schedule, workflow, email, Drive object, public post, paid compute, permission, or access control was changed. P26 alone may reconcile the structured delta below into shared ledgers.

## 9. Structured `ledger_delta`

```yaml
ledger_delta:
  worker: NM13-09
  allocation: CLOSABLE_OUTSIDE
  source_status: ADMISSION_PENDING
  active_source: NONE
  claim_created: false
  mathematical_metric:
    before: UNMEASURED
    after: UNMEASURED
  mathematical_movement: none
  section_B_methods:
    assigned_initial: [2, 4, 27]
    actually_tried: []
    reason_not_tried: no_lawful_target_admitted
  shard:
    rule: "int(SHA256(UTF-8 canonical_dedup_key).hexdigest(),16) mod 13 = 8"
    newly_screened_families: [D, E, F, G, H]
    D_cursor_through: D0102
    next_cursor: [C, Codex_raw_catalog]
  key_dispositions:
    D0009: CLAIMED_EXCLUDED
    D0010: CLAIMED_EXCLUDED
    D0038: CLAIMED_EXHAUSTED_HANDOFF_EXCLUDED
    D0071: HARD_NOT_CLOSABLE
    D0090: HARD_NOT_CLOSABLE
    E0018: EXHAUSTED_HANDOFF_EXCLUDED
    E0050: POSTED_OR_EXISTING_WORK_EXCLUDED
    F0110: OPEN_LOOKING_UNCLAIMED_BUT_NOT_CLOSABLE_ON_CURRENT_FULL_SOURCE_SCOPE
    G0002: CLAIMED_OR_HANDOFF_EXCLUDED
    G0007: CLAIMED_P14_EXCLUDED
  fresh_literature_checks:
    date_utc: 2026-09-17
    F0110:
      source: Michel_Talagrand_Are_many_small_sets_explicitly_small
      exact_scope_recovered: true
      later_source_matching_resolution_found: false
      limitation: bounded_negative_search_not_worldwide_openness_or_novelty
  prior_attempts_recovered:
    - F0110-A001
  checker: none
  artifacts: []
  audits: []
  shared_roots_edited: false
  peer_files_edited: false
  next_action: continue_residue8_C_and_Codex_admission_screen
```

**End of complete run report.**