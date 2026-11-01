Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; Section-B methods #2/#8/#11 remain unspent because no successor source crossed admission.**

# NM13-05 research invocation — post-D0004 successor admission screen 1

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-05`  
Category: `CLOSABLE OUTSIDE`  
Selection shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 4`  
Current target: **NONE ADMITTED**  
Current state: **ADMISSION_PENDING**

## 1. Runtime and control disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed to this report, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The task/scheduler control surface exposed to this worker still has task content/title, schedule/timing, timing mode and enabled-state controls, but **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface that exposes persistent model and reasoning controls together with authenticated per-run runtime attestation.

The historical P26 `You cannot modify this task` event remains an authorization-context boundary in repository history. The legitimate workaround is to use the owning/otherwise authorized task context or an authorized product/admin/API/support surface. It is not legitimate to clone the task, bypass permissions, or infer that inaccessible ownership has been released. This run did not modify any schedule or permission.

## 2. Authoritative continuity: D0004 remains handed off and is not reopened

The newest prior NM13-05 report is

`proofnet24/NM13-05/runs/2026-09-18/2026-09-18T05-23-00Z__d0004-continuous-quantile-handoff.md`.

That immutable report records the sixth consecutive unchanged CLOSABLE run on D0004, with frozen metric `epsilon_sep = 3/5 -> 3/5`, and therefore triggers the owner's mandatory six-unchanged-run rotation rule. Its explicit successor state is `ADMISSION_PENDING`. I preserved that handoff exactly:

- D0004 was **not** researched again;
- `operations/claims/D0004.md` was **not** treated as released;
- the old D0004 metric was **not** inherited by a successor;
- no successor stagnation or recovery counter was started merely because screening took place.

The D0004 handoff also preserves useful mathematical history — in particular the finite weak-majorization / continuous-quantile reduction for law-determined norms — but none of that history authorizes silently narrowing or reviving D0004.

## 3. Required repository read and access limits

Before attempting selection I reread or targeted-recovered the current authoritative state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the newest NM13-05 handoff report;
- newest neighboring NM13-04 and NM13-06 reports;
- relevant canonical claims, source rows, attempts, handoffs, campaign status and current ownership evidence encountered during this screen.

The newest neighboring states relevant to continuity were:

- NM13-04 / P0457: deterministic co-degree metric moved from `S_exact=4` to `UNBOUNDED`, but the source-level result remains `PROVED-CANDIDATE / AUDIT-PENDING`; its naming NM13-05 as an eventual auditor is not an audit pass and does not create ownership here.
- NM13-06 / P0195: frozen metric remains `n_edge^* >= 6`; the newest report records three consecutive unchanged runs and requires a Section-I stuck recovery on its next invocation. That source remains exclusively NM13-06's.

Large JSONL ledgers and some root files are connector-truncated when rendered wholesale. I therefore do **not** claim a semantic reread of every one of the roughly 780 intake rows from one giant response. Exact rows, canonical keys, claims, attempt records, and path-scoped history used below were recovered directly. Missing or truncated history was not interpreted as absence.

The last fresh master observed immediately before final ownership rechecks in this screen was `84922e0f873072e7b346b21142dba7de681410d5` (2026-09-18 07:01:29 UTC). It already includes a new NM13-11 claim on E0082; that does not release any NM13-05 candidate.

## 4. Shard discipline and D-series preservation

A source can be selected only from the canonical residue-4 shard. An intake ID or title is not substituted for the canonical dedup key when a canonical identity exists.

The old D0004 key remains

`complete_mixability_open_2014::open_problem_4`,

which is a residue-4 identity, but D0004 is excluded by the mandatory handoff above.

The other currently retained Wang complete-mixability queue leads do not fall in this worker's residue-4 shard under their canonical identities:

- Open Problem 7: residue 7;
- Open Problem 8: residue 1;
- Open Problem 9: residue 8;
- Open Problem 10: residue 8;
- Open Problem 12: residue 9.

Thus no alternate queued D-series mixability lead can lawfully be taken merely because it matches NM13-05's subject focus. Existing D-series ownership/closures were preserved and no D claim was created or edited.

## 5. Primary successor screen: current C intake, canonical aliases first

The strongest currently visible focus-fit candidate in the residue-4 C intake is **C0035**, Russell Lyons's determinantal block-factor question.

Its current canonical key is the literal key `C0035`; the exact shard calculation is

`SHA256("C0035") = 702e3e8dca4d0d478639a1065ff96821abbf26bba0baad5ca6b149fffb17245b`,

with residue `4 mod 13`.

The source asks whether every stationary determinantal process whose symbol is a trigonometric polynomial of degree `m` is an `(m+1)`-block factor of an iid process. This is an unusually good thematic fit for NM13-05 because it is a dependence/coupling problem with finite-overlap obstruction routes.

However, **C0035 is not available**. At the fresh master above, canonical claim `operations/claims/C0035.md` exists with status `CLAIMED / CLOSABLE OUTSIDE / current-open-looking` and exclusive owner native slot `6aa7b454b5808191bb00d87697d89388`, rooted at

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-12/successors/C0035/`.

The claim explicitly forbids duplicate ownership or transfer without an immutable release/handoff. No such release exists in the bounded current check. Therefore NM13-05 did not touch C0035 despite its strong fit.

I also refreshed its current literature status because source-open status is an admission gate, not something ownership alone establishes. Bounded 2026-09-18 searches recovered:

- Lyons's ICM 2014 source question;
- the degree-one theorem of Broman, *One-dependent trigonometric determinantal processes are two-block-factors*;
- current Lyons / Lyons-Steif material still presenting the all-degree question;
- later determinantal-process papers that do not state the all-degree `(m+1)` block-factor theorem.

No source-matching all-degree resolution surfaced in this bounded search. That is negative evidence only and is not a worldwide openness or novelty certificate. In any event the live canonical owner independently blocks admission.

### Other recovered canonical residue-4 C rows

The bounded literal-key shard pass recovered the following additional rows. None passed the combined source/closability/ownership gate:

- `C0012` — subdiffusive upper bound for Liouville random walk on the DGFF. This is an asymptotic random-environment theorem, not an honest finite/short CLOSABLE endpoint.
- `C0041` — transience in a direction implies ballisticity for uniformly elliptic iid RWRE in `d>=2`. Global asymptotic RWRE theorem; HARD, not a source-valid finite certificate target.
- `C0095` — convergence of the honeycomb SAW holomorphic observable to its conformal covariant. Scaling-limit problem; HARD.
- `C0123` — bridge/island structure between near-maximal peaks in the NK fitness landscape. Source quantifiers are asymptotic/global; the preserved attempt does not reduce it to one finite source-closing certificate.
- `C0131` — recurrence/transience dichotomy for iid uniformly elliptic excited random walks in dimensions at least two. Infinite-process theorem; HARD.
- `C0143` — exponential decay for large finite clusters touching an infinite cluster on transitive graphs. Infinite-volume percolation theorem; HARD.
- `C0157` — recurrence of linearly reinforced random walk on `Z^2`. The intake now marks this row resolved in later literature; excluded.
- `C0159` — cluster repulsion for nonunimodular transitive graphs. Infinite transitive-graph theorem; HARD.

One important canonical-alias correction prevents a false shard assignment: nominal row `C0023` shares the canonical key

`theta_pc_zero_intermediate_dimensions`

with another alias row. Its canonical SHA-256 is

`1db08619b51a9a5c5f6ac0fb46b420d85c70c1bf177c7f33bb554ad941cf0cc8`,

whose residue is **5**, not 4. Therefore C0023 is not an NM13-05 target even though hashing the alias ID would have put it in a different bucket. This is exactly why the owner requires canonical identity recovery before hashing.

I do **not** call the entire C intake exhaustively residue-screened in this report: some older rows use custom canonical keys rather than their visible C IDs, and the large ledger is connector-bounded. The durable cursor below keeps those custom-key rows in scope rather than pretending they were eliminated.

## 6. Supplemental Codex source-ledger residue-4 reconciliation

Targeted reads of the older Codex probability source ledger recovered four explicit canonical residue-4 identities relevant to the current source pool:

1. `P0004` — `supercritical_planar_cluster_saw_connective_limit`; SHA256 `95de026d6e32dbd7b14cf68844ffedefada8b97541203fdaaa9845161187e184`, residue 4. This asks for existence of a quenched connective limit on an infinite percolation cluster and is asymptotic/HARD rather than CLOSABLE.
2. `P0101` — `classification_of_flat_fpp_boundary_pieces`; SHA256 `6dcb93d7d99f6e99215f76de9e20d1d8bc33afc20e776da8c58f9ca57f845687`, residue 4. This is a global planar FPP shape classification, not a short finite endpoint.
3. `P0161` — `potts_free_energy_for_general_configuration-model_degrees`; SHA256 `a9a32466825d4a9a93be5dbdff4380c741b4256648b1bc65ef935f7f68b3892c`, residue 4. This is a broad asymptotic statistical-mechanics extension.
4. `P0174` — `free_brownian_sharp_support_diameter_unimodality_threshold`; SHA256 `c62c1d1d17a845066b7926850b98b28ccd662204a9cebd100162b82b63ddb46b`, residue 4. This result is already represented as settled/campaign work and is excluded by the instruction not to recycle posted or settled unimodality work.

These rows supply no lawful successor. Because the large Codex ledger was rendered in bounded page ranges, I record these as recovered shard matches rather than falsely claiming a complete row-by-row audit of every historical record in one invocation.

## 7. Why no claim was created

No candidate passed all admission gates simultaneously.

The closest subject/source fit, C0035, is actively and exclusively claimed elsewhere. The other recovered residue-4 sources are either already settled or theorem-sized asymptotic/infinite problems that would have to be artificially narrowed to look CLOSABLE. The owner explicitly forbids that.

Accordingly:

- no `operations/claims/<ID>.md` was created;
- no admission record was created for a successor;
- no checker or substantive mathematical artifact was manufactured;
- no successor baseline was invented;
- no Section-B method was reported as mathematically attempted.

The prescribed first successor triple **#2 ATTACK THE NEGATION FIRST, #8 DISCRETIZE, #11 DUALIZE** remains unspent until a source actually crosses admission. Admission-shape screening is not re-labelled as target mathematics.

## 8. Durable screening cursor

A later NM13-05 invocation should **not** restart D0004, and should not repeat the already-disposed literal-key C rows absent a material source/ownership change.

The durable successor cursor is:

1. first reconcile any repository/source/claim delta since this report;
2. continue through **custom-dedup C rows** not captured by literal-ID hashing, recovering aliases before hashing;
3. continue the E/F/G/H/I intake surfaces for canonical residue 4;
4. for rows lacking `dedup_key`, recover the source's canonical identity from exact `source_id + locator` / alias relations before computing a shard; never hash a title or convenient alias merely to obtain residue 4;
5. prefer a literal source problem decidable by one exact counterexample, a finite exhaustive obstruction, an explicit extremizer, or a short theorem; reject broad asymptotic targets rather than invent a proxy metric.

For I and other newer intake rows that omit explicit dedup keys, canonical identity recovery remains an active obligation. Their absence from this run's admitted set is not an assertion that they were exhaustively screened.

## 9. Scheduler/model and ownership safeguards

No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, external script execution, or schedule creation/modification occurred. No shared root (`RESULTS.md`, `QUEUE.md`, `POSTED.md`) and no peer namespace was edited. The report is the only intended repository write of this invocation.

A disabled or inaccessible scheduler would not release an owner; all live and historical claim evidence remains controlling until an explicit authorized release/handoff says otherwise.

## 10. `ledger_delta`

```yaml
ledger_delta:
  track: NM13-05
  category: CLOSABLE_OUTSIDE
  source_id: null
  claim_id: null
  target_state: ADMISSION_PENDING
  mathematical_status: NO_TARGET_ADMITTED
  metric_name: successor_extremal_coupling_or_feasibility_metric
  metric_before: UNMEASURED
  metric_after: UNMEASURED
  movement: false
  methods_tried: []
  methods_reserved_for_first_admitted_successor: [2, 8, 11]
  unchanged_runs: 0
  recoveries_used: 0
  previous_target:
    id: D0004
    state: MANDATORY_SIX_UNCHANGED_RUN_HANDOFF_PRESERVED
    revived: false
    inherited_metric: false
  strongest_current_focus_fit:
    id: C0035
    canonical_dedup_key: C0035
    shard_mod_13: 4
    disposition: BLOCKED_BY_LIVE_EXCLUSIVE_CLAIM
    current_owner: 6aa7b454b5808191bb00d87697d89388
  canonical_alias_correction:
    row: C0023
    canonical_dedup_key: theta_pc_zero_intermediate_dimensions
    actual_shard_mod_13: 5
    disposition: NOT_THIS_SHARD
  screened_literal_C_residue4:
    - C0012
    - C0035
    - C0041
    - C0095
    - C0123
    - C0131
    - C0143
    - C0157
    - C0159
  supplemental_codex_residue4:
    - P0004
    - P0101
    - P0161
    - P0174
  claim_created: false
  target_artifacts_created: false
  admission_screening_counts_as_mathematical_progress: false
  next_cursor: "custom-dedup C rows, then E/F/G/H/I canonical residue-4 rows; resolve missing dedup identities before hashing"
  next_step: "Reconcile deltas, continue the canonical residue-4 screen, and admit only a genuinely unassigned source-valid CLOSABLE target. If admitted, create the canonical claim create-only, read it back, then actually attempt B2/B8/B11."
  required_eventual_auditors_if_a_successor_closes:
    - P26
    - NM13-06
  audits_presumed_passed: false
```

No candidate passed admission in this invocation, so the correct terminal state is **ADMISSION_PENDING**, not a fabricated target and not an inherited D0004 continuation.
