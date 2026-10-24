Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; Section-B methods #2/#14/#19 remain genuinely NOT_TRIED because no successor crossed admission.**

# NM13-04 — legacy P-series reconciliation repair through P0223

Date: 2026-09-19
Track: `NM13-04`
Category: `CLOSABLE OUTSIDE`
Owner namespace: `proofnet24/NM13-04/`
Selection shard: `int(SHA256(UTF-8 canonical_dedup_key).hexdigest(),16) mod 13 = 3`
Status: **ADMISSION_PENDING**

## 1. Runtime / model-control truth

The prompt requests GPT-6 with maximum reasoning. This run does not have authenticated evidence that GPT-6 or a maximum-reasoning binding actually ran. The exposed runtime identifies the model as GPT-5.6 Sol; reasoning level is not exposed as a verifiable setting, so it is reported as `UNVERIFIED`.

The exposed task-control surface still has no model-family selector and no reasoning-effort selector. It exposes prompt/schedule/timing/enabled-state style controls, not a binding `model` or `reasoning` field. Therefore `GPT-6 / maximum` remains prompt text only. Changing that would require a product/runtime surface that actually exposes those controls (or an authorized platform/admin capability); none is available in this run, and no support escalation is claimed. The historical P26 `You cannot modify this task` event remains an authorization-context issue; repository continuity records that P26 was later updated from an authorized context. The compliant workaround is the owning/authorized product/workspace/API/admin context, not duplication or bypass.

## 2. Continuity and why this run was a repair run

Newest predecessor read first:

`proofnet24/NM13-04/runs/2026-09-19/2026-09-19T03-23-30Z__strict-delta-admission-no-source-claim-release.md`

creation commit `f43588f4385fb320b20a868992193cd0c0430f5e`.

That report discovered a real defect in the old cursor. `P0169` was an older legacy P-series source already present in the intake corpus, had canonical key `linear_fourier_mass_versus_boolean_degree`, and hashes to residue 3, but it had not been included in NM13-04's retained static P-series sentinel set. R7-02 created the exclusive claim before NM13-04 could lawfully do so. Therefore the previous `STRICT_DELTA_ONLY_RESIDUE3_ADMISSION` cursor is suspended: this run repairs the older P-series reconciliation instead of pretending the static catalog was complete.

Preserved terminal predecessor: `P0457` remains exhausted/retired for this track at six unchanged CLOSABLE runs and two stuck recoveries. It was not reopened.

## 3. Mandatory state reads and authoritative continuity

Read at the start of this invocation, with current `master` unless an immutable predecessor commit is named:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized NM13 deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- `QUEUE.md`;
- `POSTED.md`;
- `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- newest NM13-04 predecessor above;
- neighboring current reports including NM13-03 and NM13-05;
- canonical claims, source ledgers, and attempt ledgers relevant to the screened tranche.

`QUEUE.md` remains a candidate list, not dispatch permission; its current READY certification is still zero. `POSTED.md`, the campaign index/ranking, and settled/retired scopes remain exclusions. No missing report was treated as permission to restart a source.

## 4. Correct legacy source ledger and canonical identities

The legacy `P` rows are not in `probability_1000_intake_claude_20260907/problems.jsonl`; that file contains the Claude `C` intake. The authoritative older P-series records used for this repair are in:

`probability_campaign_2026_09/codex_20h_20260906/problems.jsonl`

with their exact `dedup_key`, `source_id`, locator, statement, status, and source-date fields. The corresponding substantive first-pass history is in:

`probability_campaign_2026_09/codex_20h_20260906/attempts.jsonl`.

The same canonical keys are carried by the later intake dedup index, e.g. `probability_1000_intake_F_20260908/raw/dedup_index.json`; this was used only as a cross-check, not as a replacement for source identity.

This run deterministically reconciled **P0162 through P0223 inclusive**. There are 62 IDs in that interval. P0206 and P0207 are already `admitted=false` / resolved-in-literature rows and have no canonical dedup key in the source ledger; they were excluded before any shard decision and were not hashed under an invented alias. The other 60 rows have explicit canonical dedup keys and were hashed exactly as UTF-8 strings.

The only residue-3 identities in this repaired interval are:

| ID | exact canonical dedup key | SHA-256 | mod 13 | disposition |
|---|---|---|---:|---|
| P0168 | `noise-optimal_equal-volume_gaussian_partitions` | `6a5665447057ff5a1fea54b1f54f7a61e5d8943b2ce8273b3d27aa3a5e4ee3fc` | 3 | unclaimed but HARD / not CLOSABLE |
| P0169 | `linear_fourier_mass_versus_boolean_degree` | `0293f8eb2ba63ce7024462fbdedbf656b716ef1f586c9928f67d42d54b55c184` | 3 | already exclusively owned by R7-02, CLOSABLE |
| P0194 | `polynomial_mixing_with_plus_ising_boundary_conditions` | `49fc01449bdd3ed6d77b861b38ef60136aebe5878c43058ed91755988acb313b` | 3 | unclaimed but HARD / asymptotic, not CLOSABLE |

No other row in P0162--P0223 has residue 3. Cross-index searches for the P0168 and P0194 keys recover the same canonical keys in the dedup index and catalog; they do not expose a second canonical problem ID that would create an alias collision. Exact-ID repository-wide searches find their intake/catalog/attempt history but no current `operations/claims/P0168.md` or `operations/claims/P0194.md`, and no owner-slot assignment/handoff. Their lack of ownership does **not** make them admissible because the category gate fails.

For reproducibility, the computed residue sequence over the non-resolved rows was checked directly from each source-ledger key. The relevant local neighborhood is:

- P0162..P0173 residues: `12,5,8,10,1,10,3,3,9,9,0,5`;
- P0174..P0185 residues: `4,12,5,1,1,12,2,2,0,4,7,0`;
- P0186..P0197 residues: `7,10,9,4,1,5,2,9,3,5,6,10`;
- P0198..P0205 residues: `9,12,0,8,8,8,4,11`;
- P0206/P0207: excluded as resolved before hashing;
- P0208..P0219 residues: `5,8,7,9,6,9,11,5,9,12,12,11`;
- P0220..P0223 residues: `6,9,1,0`.

## 5. Residue-3 gate: exact source, history, ownership, literature, category

### P0168 — Standard Simplex / Gaussian noise-stability partition conjecture

Source ledger identity: O'Donnell, *Open Problems in Analysis of Boolean Functions* (2012), PDF p. 9, Standard Simplex Conjecture. The source-level target is to optimize Gaussian noise stability over equal-volume partitions, across the stated correlation signs and admissible cell counts.

Prior repository attempt: `P0168-A001` is a substantive first pass, not a solution. It computes an exact four-cell sign-partition benchmark `[1/2 + arcsin(rho)/pi]^2` and explicitly records that this does not order the competitor against every partition. `full_problem_solved=false`, `novelty=not_claimed`, no independent review.

Ownership: direct canonical claim fetch `operations/claims/P0168.md` returned 404. Repository-wide exact-ID/key searches expose catalog/attempt material but no owner claim or handoff. Thus it appears unassigned, but assignment is not the failing gate.

Fresh bounded literature check on 2026-09-19:

- query: `"Standard Simplex Conjecture" Gaussian noise stability Heilman 2026`, arXiv-focused;
- arXiv:2608.00333, Steven Heilman, *Sharp Hardness for MAX-3-CUT and Quantum MAX-CUT*, submitted 2026-07-31, proves the three-candidate Plurality-is-Stablest result for correlations in `[-1/2,2/5]`; that is a substantial three-cell range, not the full all-cell/all-correlation P0168 statement;
- arXiv:2306.03312 gives an earlier three-cell interval;
- arXiv:2607.14087 resolves a different **Weak Simplex Conjecture** in Gaussian coding; it is not silently identified with P0168's equal-volume Gaussian partition noise-stability conjecture.

Bounded search absence is not a worldwide openness certificate. The source remains nontrivially open in its full scope as far as this bounded check establishes.

**Category decision:** reject for NM13-04. P0168 is a global Gaussian variational conjecture with all admissible cell counts/correlations and no natural finite counterexample-size or exhaustive finite-case metric. It is an honest HARD target, not a finite-certificate / short-theorem CLOSABLE source. Relabeling it CLOSABLE would violate the owner's explicit instruction.

### P0169 — Linear Fourier mass versus Boolean degree

Source identity: O'Donnell 2012, PDF p. 9, “Linear Coefficients versus Total Degree”. The current canonical claim is `operations/claims/P0169.md`, owner `R7-02`, classification `CLOSABLE OUTSIDE`, admission commit `404a944eedf17f4740e9ebf5b4c0792c9db0e144`.

This is the strongest focus-fit residue-3 source in the repaired tranche, but it is unavailable by exclusive ownership. R7-02 has already continued into substantive degree-2/degree-3 exact work. A disabled/inaccessible schedule would not release it; no release is present. NM13-04 therefore did not create a duplicate claim.

### P0194 — polynomial plus-boundary 2D Ising Glauber mixing

Source ledger identity: Levin-Peres-Wilmer, *Markov Chains and Mixing Times*, Chapter 26 Question 1. Target: polynomial-in-`n` Glauber mixing on the `n x n` square with plus boundary at every fixed positive temperature.

Prior repository attempt: `P0194-A001` proves only the high-temperature Dobrushin/path-coupling regime `4*tanh(beta)<1`, with `t_mix(1/4) <= N log(4N)/(1-4 tanh beta)` up to rounding. It explicitly records failure of this method once the contraction coefficient reaches one; `full_problem_solved=false`, `novelty=not_claimed`, no independent review.

Ownership: direct canonical claim fetch `operations/claims/P0194.md` returned 404. Repository-wide exact-ID/key searches expose catalog/attempt material but no current owner claim or handoff. Again, assignment is not the failing gate.

Fresh bounded literature check on 2026-09-19:

- Lubetzky-Martinelli-Sly-Toninelli, JEMS 2013 / arXiv:1012.1271, explicitly describes polynomial mixing for homogeneous plus boundary as conjectured and proves a quasi-polynomial upper bound through the low-temperature regime up to criticality;
- Gheissari-Sly, arXiv:2605.08052, submitted 2026-05-08, *Rapid phase ordering of Ising dynamics on Z^2*, uses a uniform-in-beta quasi-polynomial plus-boundary mixing estimate as an input to a different phase-ordering theorem. Its abstract does not supply the missing polynomial plus-boundary bound.

Again, this is bounded current-status evidence, not a proof of worldwide openness.

**Category decision:** reject for NM13-04. P0194 is an asymptotic mixing-time theorem across arbitrary box size and the full low-temperature regime. It is not a finite graph counterexample/certificate target and has no honest finite cutoff whose verification would settle the source. It is HARD, not CLOSABLE.

## 6. Current repository delta from NM13-04 predecessor

Frozen pre-write `master` for this report: `8071a95e1540fde375816f2cb07d93c6ff0cc276`.

Exact compare from predecessor report commit `f43588f4385fb320b20a868992193cd0c0430f5e` to the frozen head is:

- ahead: **148 commits**;
- behind: **0**.

The only new canonical claim in that interval is `operations/claims/P0219.md`. It is `CLAIMED / MANUALLY ADMITTED / CLOSABLE OUTSIDE` by another native slot. Canonical key `high-density_oriented_percolation_flow_asymptotics` hashes to residue 11, so it is off NM13-04's shard in addition to being owned. There is no claim deletion or release in the interval.

The changed-file set contains no change to `QUEUE.md`, `POSTED.md`, `RESULTS.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, or the source/attempt JSONL ledgers screened here. Thus there is no current-root or source-ledger event that creates a free residue-3 CLOSABLE successor.

## 7. Admission decision

No candidate in the repaired P0162--P0223 tranche passes all gates.

- P0168: residue 3, apparently unassigned, but HARD / wrong category.
- P0169: residue 3 and CLOSABLE, but already exclusively owned by R7-02.
- P0194: residue 3, apparently unassigned, but HARD / wrong category.
- all other non-resolved rows in the tranche are off shard;
- P0206 and P0207 are already resolved/excluded.

Therefore:

**ADMISSION_PENDING.**

No canonical claim is created. No candidate is treated as READY merely because it is unclaimed. No screening event is counted as mathematical progress.

## 8. Methods and metric

There is still no admitted successor problem, so the post-admission source class and finite metric cannot be frozen yet.

Metric before: `UNMEASURED`.
Metric after: `UNMEASURED`.
Movement: **none**.

Section-B methods actually attempted on an admitted source: **none**.

Methods #2 ATTACK THE NEGATION FIRST, #14 FIND THE GROUP ACTING, and #19 MAKE IT AN ALGORITHM remain explicitly reserved and **NOT_TRIED**. Charging them against screening would be false reporting.

P0457 predecessor counters remain historical/terminal and are not repurposed as successor counters. Successor unchanged-run and stuck-recovery counters remain `NOT_STARTED_PRE_ADMISSION`.

## 9. Cursor repair / next invocation

The old `STRICT_DELTA_ONLY_RESIDUE3_ADMISSION` cursor remains suspended until the missed legacy P inventory has been reconciled far enough that delta-only mode is justified again.

Durable cursor after this run:

`LEGACY_P_RECONCILIATION_NEXT=P0224`

Authoritative completed static coverage now includes the previously reconciled E/F/G/H/I material plus this repaired exact-key legacy P tranche **P0162--P0223**. The next invocation should begin at P0224 in the canonical P source ledger, not rescan this tranche unless a source-status correction, alias correction, or ownership release lands.

## 10. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-04
  category: CLOSABLE_OUTSIDE
  status: ADMISSION_PENDING
  source_id: NONE
  claim_id: NONE
  metric:
    name: successor_metric
    before: UNMEASURED
    after: UNMEASURED
    movement: none
  methods:
    attempted: []
    reserved_after_admission: [2, 14, 19]
  successor_unchanged_runs: NOT_STARTED_PRE_ADMISSION
  successor_recovery_counter: NOT_STARTED_PRE_ADMISSION
  predecessor_terminal_state:
    id: P0457
    unchanged_runs: 6
    stuck_recoveries: 2
    reopened: false
  screening:
    mathematical_progress: false
    repaired_range: P0162-P0223
    exact_key_rows_hashed: 60
    resolved_rows_excluded_before_hash: [P0206, P0207]
    residue3_hits: [P0168, P0169, P0194]
    cursor_before: LEGACY_P_REPAIR_FROM_P0162
    cursor_after: LEGACY_P_RECONCILIATION_NEXT=P0224
  audits:
    P26: NOT_APPLICABLE
    NM13-05: NOT_APPLICABLE
  repository_delta:
    predecessor_commit: f43588f4385fb320b20a868992193cd0c0430f5e
    frozen_prewrite_head: 8071a95e1540fde375816f2cb07d93c6ff0cc276
    ahead: 148
    behind: 0
    new_canonical_claims: [P0219]
    ownership_releases: []
```

## 11. Scope / access / integrity notes

- Current literature checks were bounded public-web searches and primary/authoritative source reads where surfaced. They do not prove worldwide openness or novelty.
- No external script was executed. SHA-256 residue calculations were performed locally from exact repository canonical keys; no checker artifact was created because screening is not a mathematical finite claim and the owner's policy says not to manufacture certificates without a substantive idea.
- No claim, shared root, peer namespace, workflow, permission, public post, email/Drive resource, paid compute, or schedule was modified.
- This invocation creates exactly this one immutable run report. It must be read back at its creation commit; no receipt-only follow-up commit is permitted.
