Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; no successor Section-B method is credited because no new source crossed admission.**

# NM13-11 — successor admission screen 1 after H0003 handoff

Date: 2026-09-18 UTC  
Track: `NM13-11`  
Category: `HARD OUTSIDE`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Own namespace: `proofnet24/NM13-11/`  
Required selection residue: `int(SHA256(UTF-8 canonical dedup_key),16) mod 13 = 10`

## 1. Runtime/model disclosure and control-plane status

The prompt requests GPT-6 with maximum reasoning. That is **not** the runtime I can verify. This invocation identifies as **GPT-5.6 Sol** and exposes no authenticated reasoning-effort telemetry, so the reasoning level is **UNVERIFIED**.

The exposed scheduler/task-control surface still provides prompt/title, schedule or relative-start fields, enabled state, and timing mode, but **no bindable model-family selector and no reasoning-effort selector**. `GPT-6 / maximum` therefore remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing those selectors together with authenticated per-run model/effort attestation.

The historical P26 response `You cannot modify this task` is treated as an authorization-context boundary. Repository history also records a later successful P26 update from another authorized context. The legitimate workaround is the task-owning/otherwise authorized scheduler context or platform/admin support, not task duplication or access-control bypass. This invocation did not create, modify, disable, or duplicate any schedule.

## 2. Authoritative continuity recovered before screening

The newest own report recovered was

`proofnet24/NM13-11/runs/2026-09-18/2026-09-18T04-00-00Z__H0003-stuck-recovery-1-handoff.md`.

That report preserves H0003 as the predecessor assignment, records the source-as-written supercritical support obstruction, selects **MOVE TO THE NEXT PROBLEM IN QUEUE.md** as stuck-recovery action 1, and leaves NM13-11 in successor `ADMISSION_PENDING`. It explicitly does **not** self-release `operations/claims/H0003.md`; owner/P26/shared-state reconciliation remains required. I therefore did not create a second claim on another problem from the same source and did not treat the handoff as permission to steal or duplicate ownership.

Before screening I reread or targeted-search-recovered the controlling and continuity surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner amendment/deployment record `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- newest own H0003 handoff report;
- newest visible neighboring NM13-10 and NM13-12 reports;
- current G/H/I intake rows relevant to the percolation/interacting-particle focus;
- current claims, source aliases, historical assignments, and attempt records for every candidate advanced below.

The newest visible NM13-10 report is still `ADMISSION_PENDING` and uses a delta-only cursor after finding no new eligible residue-9 source. The newest NM13-12 report remains on its exclusive P0483 RWRE assignment in stuck recovery 2. Neither neighboring report supplies a release or ownership change relevant to NM13-11.

Repository search is connector-bounded. I disclose that I did **not** byte-for-byte rescan every historical blob in the repository; I did recover the authoritative current claim files and relevant historical runs for the candidates below, and no missing-history assumption is used to create ownership.

## 3. Canonical shard recovery and candidate screen

### 3.1 Current G-percolation front: no residue-10 candidate among G0001--G0010

The G intake carries explicit canonical `dedup_key` values, so no alias hash was used. Recomputing SHA256 on the exact UTF-8 keys gives:

| ID | canonical dedup key | residue mod 13 | disposition |
|---|---|---:|---|
| G0001 | `cerf_theta_pc_2026::conjecture_1.4` | 5 | wrong shard; additionally recorded as equivalent to the classical `theta(p_c)=0` obstruction modulo known supercritical tails |
| G0002 | `cerf_theta_pc_2026::conjecture_53.1` | 8 | wrong shard |
| G0003 | `cerf_theta_pc_2026::conjecture_58.2` | 3 | wrong shard and source itself leaves the hypothesis class intentionally undefined |
| G0004 | `flammant_finite_graph_2026::conjecture_2.2` | 2 | wrong shard |
| G0005 | `flammant_finite_graph_2026::kozma_nitzan_conjecture_3` | 0 | wrong shard |
| G0006 | `fernley_jacob_contact_tree_2026::lambda_1_lt_lambda_p_zd` | 12 | wrong shard; same current source family as excluded/claimed contact-process work |
| G0007 | `fernley_jacob_contact_tree_2026::continuity_of_the_two_transitions` | 8 | wrong shard and explicitly excluded by this worker's source guard |
| G0008 | `campos_delima_nonmonotone_2026::monotone_two_point_z2` | 1 | wrong shard; also now has a current canonical claim elsewhere in the fleet |
| G0009 | `christoph_morawski_wigderson_finite_pc_2026::question_5.1` | 3 | wrong shard; H0002 is the same mathematical source question under an H alias |
| G0010 | `christoph_morawski_wigderson_finite_pc_2026::question_5.2` | 4 | wrong shard and historical HARD10-01 work exists |

This eliminates the strongest current percolation-specific front without inventing an alias identity.

The H-intake row H0002 is therefore **not** a residue-10 opportunity: its canonical identity is G0009's `christoph_morawski_wigderson_finite_pc_2026::question_5.1`, which hashes to residue 3. Separately, the same arXiv source `2608.19145` is currently represented by the exclusive R7-07 claim `operations/claims/G0011.md` for the paper's long-cycle conjecture. The present owner instruction says to exclude every other claimed source, not merely exact claim IDs, so no question from that paper is selectable by NM13-11 in this invocation.

The remaining H0004--H0011 cascade questions are all aliases/nearby questions from the same Kumar/Kumar–Duddala threshold-cascade source family as predecessor H0003. Because `operations/claims/H0003.md` remains authoritative pending reconciliation, admitting another question from that source would create duplicate source ownership under a different ID. I did not do so.

### 3.2 Residue-10 candidate I0011: canonical identity recovered, but already exclusively claimed

The I intake does not supply a `dedup_key` field for I0011. Following the owner rule, I first recovered the canonical source identity rather than hashing the short ID or title alias:

`arxiv_2609_06818::Section 1, after Theorem 1.6, citing [3, Conjecture 5.4]`.

Its SHA256 is

`36554917c3d8e76d09cf2e0b425791eee181e1be6bed6174b02f0f127b1fdfdd`,

which is residue **10 mod 13**.

That makes I0011 shard-compatible, but it is unavailable: `operations/claims/I0011.md` is an explicit **P16 exclusive claim** for the unresolved fixed-`d>=5` regular branch of Abdi–Ghorbani Conjecture 5.4. A claimed source is not released by inactivity or schedule state, and a pending/active lead is not READY for this worker. I0011 is therefore excluded without mathematical work.

### 3.3 Residue-10 candidate I0105: canonical identity recovered, but source is already claimed and the row is not READY

For I0105 the intake again lacks a `dedup_key`, so I recovered the exact primary-source identity before hashing:

`reinforcement_matrix_2023::Open Problem 22`.

SHA256 is

`53a774e2ba088c71695bf17357c1c0f658251de9669874936cc5550f08193ad7`,

which is residue **10 mod 13**.

I rechecked the primary source visually. Open Problem 22 in *Open Problems in Stochastic Reinforcement Models* asks for analysis of preferential-attachment models with vertex/edge removal and discusses multiple possible deletion mechanisms rather than freezing one single finite process/constant. A fresh bounded literature search also surfaced 2025 work on preferential-attachment trees with vertex death, including both persistence and lack-of-persistence regimes for the maximum degree, confirming that scope separation is now essential rather than optional.

More decisively, the **same primary source is already under an active canonical claim**: `operations/claims/P0082.md`, owned by P13, for Open Problem 12 on the WARM forest threshold. Under NM13-11's explicit source-level exclusion, that blocks I0105 regardless of whether Open Problem 22 itself has a separate claim file. Current task-health history also labels I0105 `PENDING_SCOPE`, not READY. I therefore did not narrow the broad source question into a synthetic personal project and did not create a claim.

### 3.4 Additional probability/percolation checks

I also canonicalized several nearby probability rows before rejecting them by shard rather than by title intuition:

- I0037, Schramm Problem 2.10: `schramm_2006_v2::Problem 2.10`, residue 2;
- I0038, Schramm Problem 3.2: `schramm_2006_v2::Problem 3.2`, residue 11;
- I0040, Schramm Problem 5.1: `schramm_2006_v2::Problem 5.1`, residue 2;
- I0012, comb collision boundary case: exact source/locator identity, residue 7;
- H0017, competing first-passage percolation: exact source/locator identity, residue 9;
- H0024, interval-activation frog-model critical-line gap: exact source/locator identity, residue 4.

None is in residue 10, so none reaches the ownership/current-literature admission gate for this worker.

## 4. Admission conclusion

**ADMISSION_PENDING.** No candidate in this bounded successor screen passed all required gates simultaneously:

1. exact source and canonical identity recovered before hashing;
2. residue exactly 10 mod 13;
3. genuinely source-posed HARD OUTSIDE target with a concrete quantitative or finite milestone;
4. current-status and prior-attempt scope safe;
5. unclaimed at both exact-target and source level;
6. not retired, exhausted, posted, settled, or held as another worker's pending lead.

The two clean shard-10 identities recovered this invocation, I0011 and I0105, both fail ownership/readiness. The preferred G-percolation front has no residue-10 row through G0010. H0002 is a G0009 alias in residue 3, not a hidden shard-10 candidate.

Accordingly **no `operations/claims/<ID>.md` file was created**, no source baseline was invented, no checker or proof artifact was manufactured, and no mathematical-progress counter is advanced.

The successor screening cursor is now:

- G0001--G0010: canonical residues recovered; no shard-10 candidate;
- H0002: canonical G0009 alias, residue 3, source additionally claimed elsewhere;
- H0004--H0011: same source family as still-authoritative predecessor H0003 claim; do not duplicate under a new ID;
- I0011: residue 10, excluded by current P16 claim;
- I0105: residue 10, excluded by P13 source-level claim and `PENDING_SCOPE` status;
- selected nearby percolation/interacting-particle rows I0037/I0038/I0040/I0012/H0017/H0024: wrong residue.

The next invocation should continue from the **next unscreened canonical residue-10 rows in D/E/F/I**, prioritizing an actually unclaimed interacting-particle/percolation-adjacent target with a real finite/quantitative milestone. It should not rescreen the rows above absent a material ownership or source-status change.

## 5. Metric, methods, counters, and audits

There is no admitted successor, so the successor metric remains honestly

`UNMEASURED -> UNMEASURED`.

Screening is not mathematical progress. No successor unchanged-run counter starts, and no successor stuck-recovery counter starts. H0003's predecessor counters and stuck-recovery history remain attached to the preserved handoff and are not transferred to a successor.

No successor Section-B move is credited. In particular, methods **#2/#4/#8** are **not** reported as tried on a successor merely because they were the originally prescribed first-run triple. H0003's historical method usage remains part of H0003's record; a future admitted successor must report its own actual method use honestly.

No audit is applicable yet. P26 and NM13-12 are not presumed to have audited any successor claim.

## 6. Bounded current-source/literature checks and access limits

Dated 2026-09-18 checks in this invocation included:

- the current intake/source identity for Christoph–Morawski–Wigderson Question 5.1 and the active same-source G0011 ownership;
- the exact current P16 I0011 claim, including its later Zhu-2026 scope reconciliation;
- the primary MATRIX reinforcement source, including a page-image check of Open Problem 22;
- current P13 `P0082` ownership of that same MATRIX source;
- bounded searches for later preferential-attachment-with-death/removal literature, which recovered 2025 vertex-death persistence/non-persistence work.

These are bounded checks, not claims of worldwide bibliographic completeness. I did not perform a source-specific openness search for wrong-shard candidates after their shard failure, because they cannot be selected by this worker regardless of outcome.

## 7. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-11
  category: HARD OUTSIDE
  status: ADMISSION_PENDING
  predecessor_source_id: H0003
  predecessor_claim: operations/claims/H0003.md
  predecessor_state: HANDOFF_PRESERVED_CLAIM_NOT_SELF_RELEASED
  successor_source_id: null
  successor_claim_id: null
  shard_residue_required: 10
  metric:
    name: successor_admission_baseline
    before: UNMEASURED
    after: UNMEASURED
  mathematical_progress: false
  methods_attempted: []
  initial_successor_methods_reserved: [2, 4, 8]
  successor_unchanged_runs: 0
  successor_stuck_recoveries_used: 0
  audits:
    P26: NOT_APPLICABLE
    NM13-12: NOT_APPLICABLE
  screened_this_run:
    - G0001-G0010 canonical shard residues
    - H0002 canonical alias G0009
    - H0004-H0011 source-level duplicate guard
    - I0011 residue-10 but P16-claimed
    - I0105 residue-10 but P13 same-source claimed and PENDING_SCOPE
    - I0037/I0038/I0040/I0012/H0017/H0024 shard checks
  next_step: >-
    Continue from the next unscreened canonical residue-10 rows in D/E/F/I.
    Prefer an unclaimed percolation/interacting-particle or other HARD OUTSIDE
    source with a realistic explicit quantitative milestone. Recheck exact source,
    later literature, historical attempts, aliases, and source-level ownership
    before any create-only claim; otherwise remain ADMISSION_PENDING.
```

No shared root, peer namespace, canonical claim, workflow, permission, public surface, email/Drive item, paid-compute resource, or schedule was modified in this invocation.