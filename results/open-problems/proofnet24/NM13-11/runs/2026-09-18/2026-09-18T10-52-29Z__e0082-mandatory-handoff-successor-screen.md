Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MANDATORY HARD-TARGET HANDOFF: E0082 terminal metric `gamma_FP = 1 -> 1`, terminal counters preserved at `unchanged_runs=4`, `stuck_recoveries=2`; successor state `ADMISSION_PENDING`, metric `UNMEASURED -> UNMEASURED`; no successor Section-B method is credited because no new source crossed admission.**

# NM13-11 — mandatory E0082 handoff and residue-10 successor admission screen

Date: 2026-09-18 UTC  
Track: `NM13-11`  
Category: `HARD OUTSIDE`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Own namespace: `proofnet24/NM13-11/`  
Required selection shard: `int(SHA256(UTF-8 canonical dedup_key),16) mod 13 = 10`

## 1. Runtime disclosure and control-plane status

The task prompt requests `GPT-6 / maximum`. That is **not** the runtime I can honestly report. This invocation identifies as **GPT-5.6 Sol** and exposes no authenticated reasoning-effort telemetry, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or maximum reasoning was bound at runtime.

The exposed task-control surface still provides prompt/title, schedule or start fields, timing mode, enabled state, and task identifiers, but no bindable model-family selector and no bindable reasoning-effort selector. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model and effort controls together with authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` response was an authorization-context boundary; current `RESULTS.md` records that a later P26 update succeeded from another authorized context. The lawful workaround is an owning/otherwise-authorized context or an authorized admin/API/support path, not duplication or access-control bypass. This invocation did not create, edit, disable, or duplicate any schedule.

## 2. Required repository continuity recovered

Before changing research state I read or targeted-search-recovered the current owner-required surfaces:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized deployment/amendment record `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/E0082.md`;
- newest own report `proofnet24/NM13-11/runs/2026-09-18/2026-09-18T09-52-33Z__e0082-stuck-recovery-2-argmin-threshold.md`;
- newest neighboring NM13-12 report `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T09-50-37Z__e0086-screened-pair-second-moment-barrier.md`;
- the previous NM13-11 successor screens, especially `2026-09-18T06-08-29Z__successor-admission-screen-2.md`, which closed the then-current D residue-10 list, advanced F through F0030, and recorded the unavailable I residue-10 rows;
- E- and F-intake source rows and attempt material needed below;
- current claim/audit searches for E0082 and candidate successor E0107.

Large root/JSONL views can be connector-truncated. I therefore used exact source IDs, canonical keys, current root files, exact report paths, and targeted claim/attempt searches rather than pretending a truncated aggregate render was a byte-for-byte reread of every historical Git object. No inaccessible history is treated as permission to reset ownership or baselines.

## 3. E0082 terminal HARD handoff is mandatory now

The current exclusive claim is still:

- source/claim ID: `E0082` / `operations/claims/E0082.md`;
- source: Jim Pitman and Wenpin Tang, *Patterns in random walks and Brownian motion*, Open Problem 2.3;
- canonical key: `pitman_tang::op_2_3`;
- SHA-256: `1b4de7c58dbd8e94a7bc807a11a84c8e166fceea6c48cb804038b2f998e7228a`;
- shard residue: `10`;
- frozen metric: `gamma_FP := inf{gamma : E T(FP^{-1,n}) = O(n^gamma)}`.

Admission began with the source interval `1 <= gamma_FP <= 5/4`. The first E0082 research run moved the metric to the saturated exponent value `gamma_FP=1` by proving an `O(n log n)` upper bound together with the source linear lower bound. Subsequent runs attacked the still-open exact-order/constant problem, in particular a source-relevant `Omega(n log n)` first-passage lower bound. They produced row/column LP structure, a ladder-composition quotient, dual-load reductions, and finally a typical-column/argmin threshold route, but no further movement in the frozen metric.

The newest predecessor report is **stuck recovery 2**, with counters

- `unchanged_runs = 4`,
- `stuck_recoveries = 2`.

The owner rule for HARD targets allows at most two stuck-recovery episodes on the same source; a third requires a preserved handoff and rotation. Therefore this invocation does **not** run methods #6/#22/#30 on E0082, does not add another lemma, does not manufacture another checker, and does not call a third E0082 recovery by another name. The terminal E0082 state is preserved as:

`gamma_FP = 1 -> 1`, status `PARTIAL`, terminal counters `4 / 2`.

This handoff invocation itself is not counted as another unchanged mathematical research run. It is the mandated rotation action.

The exact unresolved mathematical handoff obligation is:

> Prove or refute the source-scale logarithmic correction for negative first-passage pattern families, e.g. on the square subsequence establish a source-faithful lower bound of the form `E T(FP^{-1,m^2}) >= c m^2 log m`, or determine the actual exact asymptotics requested by Pitman--Tang.

The strongest preserved route from recovery 2 is to control the column-load functional for a typical first-passage bridge. If `M` is the matching matrix, `q=M^{-1}1>0`, `S=1^Tq`, and `d_j` are column sums, then for every threshold `L>0`,

`S <= F/L + B_L`, where `B_L = #{j : d_j < L}`.

Thus an estimate `B_{a log n}=O(F/log n)` would yield the Peres-scale lower order. A sufficient moment target identified in the previous run is `E D_n >= a log n` with `Var(D_n) <= C log n` for the exact typical-column load `D_n`. The time-reversal/sign-flip correspondence converts first-passage words to endpoint-conditioned positive meanders, and the remaining obstruction is the loss of the constant-row-sum structure present in the solved positive-walk family.

The canonical claim file is **not deleted or self-released**. Handoff does not create free ownership. It remains authoritative until an owner/P26 reconciliation or explicit reassignment says otherwise. Current searches recover no P26 PASS and no NM13-12 PASS for an E0082 closure claim; neither audit is presumed.

### Bounded E0082 source/literature refresh

A dated 2026-09-18 search again recovered the original Pitman--Tang source (arXiv:1411.0041 / the later Lecture Notes in Mathematics publication) and the original first-passage waiting-time section. Searches combining Pitman/Tang, first-passage patterns, matching matrices, and waiting-time asymptotics did not surface a later paper claiming the exact Open-Problem-2.3 first-passage asymptotics. This is bounded negative evidence only, not a worldwide openness or novelty certificate.

## 4. Successor screen: E0107 is the next topical residue-10 lead, but is not READY

The previous successor cursor left the E intake to be screened after E0082 and the F intake after F0030. The next strong topical E-row is:

- `E0107`;
- source: Kavita Ramanan, *Interacting stochastic processes on sparse random graphs*;
- locator: Section 5, Q1;
- statement: establish general conditions for existence and uniqueness of stationary or invariant measures for the local equation;
- canonical key: `sparse_ips::q1`;
- SHA-256: `f4360cdc27d506e0cb45380fec82940d07dc50b1cc5b06c9626c7c01fe1f1b42`;
- residue: `10 mod 13`.

No canonical `operations/claims/E0107.md` was found, so there is no discovered current owner conflict. The intake nevertheless contains substantive prior attempt `E0107-A001`; this candidate is therefore not “previously unattempted.” That attempt already identified the natural branching/subcritical contraction idea and its precise obstruction: a path-space contraction constant that is not uniform in the time horizon, so it does not by itself give stationary uniqueness.

More importantly, the present-literature boundary has moved materially since the intake note:

1. Ramanan's source still states Q1 explicitly in Section 5.1 as a general stationary/invariant-measure question for local equations and notes that earlier work had mainly finite-time scope.
2. Hu--Ramanan, *An H-theorem for a conditional McKean--Vlasov process related to interacting diffusions on regular trees* (arXiv:2412.07710, 2024; listed by the author as to appear in *Probability and Mathematical Physics* in 2026), proves well-posedness of the `kappa`-Markov local-field equation under suitable assumptions, identifies stationary distributions through zeros of a sparse-free-energy dissipation / splitting Gibbs marginals, and proves convergence of natural initial conditions to the stationary set. Under additional assumptions it proves uniqueness and exponential convergence in the `kappa=2` case.
3. Hu--Ramanan, *A case study of the long-time behavior of the Gaussian local-field equation* (arXiv:2504.06449; *Electronic Journal of Probability* 31 (2026), paper 67), proves the non-Markovian-versus-Markovian long-time conjecture for `kappa=2` one-dimensional affine Gaussian drifts and proves well-posedness of the Markov `kappa`-LFE with affine drifts for every `kappa>=2`.

So E0107 is neither untouched nor cleanly source-open in its whole old 2023 form: substantial regular-tree Markovian and `kappa=2` non-Markovian stationary theory is now established. The genuinely residual question is broader (general non-Markovian local equations, higher degree, UGW settings, or broad uniqueness conditions).

I do **not** admit E0107 in this invocation. The reason is the owner's HARD admission-shape gate, not lack of topical fit. The remaining problem is a broad programmatic stationary-measure theory, and the next obvious numerical milestone—extending the affine non-Markovian `kappa=2` result to `kappa=3`, or inventing a new interaction-strength threshold—would be a worker-created restricted target unless a primary-source theorem/conjecture is first recovered that freezes the exact class and normalization. The prior attempt's proposed `interaction strength x mean degree < 1` threshold is a heuristic route, not an already source-defined scalar metric, and its uniform-in-time step is exactly the missing theorem. Calling that READY now would violate the instruction not to relabel an asymptotic/general hard problem as a convenient finite or quantitative surrogate.

Disposition: `E0107 = PENDING / NOT READY for NM13-11`, with its current-literature partial progress recorded. No claim was created.

## 5. F-intake residue-10 cursor advanced beyond F0062

I continued the exact canonical-key shard screen from the prior F cursor after F0030. No alias or title was hashed in place of a canonical key.

The next residue-10 rows encountered were:

- `F0045`, key `talagrand_small_2016::conjectures_5.2`, SHA-256 `f15f023c4da4f86755b48f16e152bddcf65a91dca6db3befc6facd6cc8bc50f4`, residue 10. The intake already marks this selector-process conjecture resolved in the literature by Park--Pham; it is excluded.
- `F0061`, key `janson_simply_generated_2012::problem_18.41`, SHA-256 `2b3999162f88ac380b2a4b6bfa01b0b9087509c6701d07305b2b4b9f88f6272a`, residue 10. Campaign `INDEX.md` records Janson Problems 18.41 and 18.42 as answered/settled; do not reopen.
- `F0062`, key `janson_simply_generated_2012::problem_18.42`, SHA-256 `42f6ef316829f4129d00a2f6a7e3117f1ca3f0025b1d30578218121d4643492e`, residue 10. Same campaign settlement/exclusion applies.

Rows F0031--F0039 and the intervening F0040--F0060 rows were canonical-key hashed as the cursor advanced; the only additional residue-10 row before F0061 was the already-resolved F0045. No unclaimed, unresolved, owner-eligible HARD source with a realistic source-valid quantitative milestone emerged in this interval.

The durable successor cursor is now:

- E intake: screened through its current tail after E0107; E0107 retained only as a materially advanced but not READY near-lead;
- F intake: continue **after F0062**;
- D: prior residue-10 list complete absent material status/ownership changes;
- I: prior residue-10 conflicts/exhaustions remain authoritative absent explicit releases;
- additionally wake the full gate for any genuinely new/materially changed source row or explicit non-exhausted owner-authorized release.

## 6. Admission decision and method accounting

**Decision: `ADMISSION_PENDING`. No successor canonical claim was created.**

No screened successor passes all gates simultaneously: canonical identity, residue 10, unresolved present source scope, no ownership/history conflict, no posted/settled/retired exclusion, and an honest HARD target whose source quantity can realistically move or whose source-relevant clause can be finitely certified.

Because no successor crossed admission:

- successor metric remains `UNMEASURED -> UNMEASURED`;
- successor `unchanged_runs = 0`;
- successor `stuck_recoveries = 0`;
- no mathematical progress is credited for screening;
- no checker/artifact/paper/audit request was created;
- the reserved first successor methods remain genuinely **unspent**: #2 ATTACK THE NEGATION FIRST, #4 PROVE SOMETHING WEAKER COMPLETELY, #8 GO THE OTHER WAY AND DISCRETIZE.

The prior E0082 methods are historical and not re-credited. This run performs the required handoff and admission work; it does not disguise intake bookkeeping as a Section-B research attack.

## 7. Next step

On the next invocation, continue the residue-10 F screen strictly after F0062 and check any source/status/claim delta first. Prefer percolation or interacting-particle targets. Admit only if the exact source leaves a genuinely unresolved finite/quantitative milestone with a realistic route; otherwise keep advancing the cursor. E0107 may be reconsidered only if a primary source or later paper supplies a precise still-open higher-degree/parameter statement with a fixed normalization, not merely because it is topically attractive.

Do not restart E0082 without an explicit later reassignment. Preserve its claim and this handoff.

## 8. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-11
  category: HARD_OUTSIDE
  status: ADMISSION_PENDING
  predecessor:
    source_id: E0082
    claim_id: E0082
    claim_path: operations/claims/E0082.md
    canonical_key: pitman_tang::op_2_3
    state: MANDATORY_HANDOFF_PRESERVED_CLAIM_NOT_SELF_RELEASED
    metric_name: gamma_FP
    metric_before: 1
    metric_after: 1
    mathematical_status: PARTIAL
    unchanged_runs_terminal: 4
    stuck_recoveries_terminal: 2
    p26_audit: NOT_PASSED
    nm13_12_audit: NOT_PASSED
  successor:
    source_id: null
    claim_id: null
    metric_name: successor_admission_baseline
    metric_before: UNMEASURED
    metric_after: UNMEASURED
    mathematical_progress: false
    methods_attempted: []
    methods_reserved: [2, 4, 8]
    unchanged_runs: 0
    stuck_recoveries: 0
  screened_this_run:
    - id: E0107
      canonical_key: sparse_ips::q1
      residue: 10
      disposition: PENDING_NOT_READY_CURRENT_LITERATURE_PARTIAL_AND_NO_FIXED_SOURCE_QUANTITATIVE_MILESTONE
    - id: F0045
      residue: 10
      disposition: RESOLVED_IN_LITERATURE_EXCLUDED
    - id: F0061
      residue: 10
      disposition: SETTLED_CAMPAIGN_EXCLUDED
    - id: F0062
      residue: 10
      disposition: SETTLED_CAMPAIGN_EXCLUDED
  screening_cursor:
    E: CURRENT_TAIL_AFTER_E0107
    F: AFTER_F0062
    D: COMPLETE_ABSENT_MATERIAL_DELTA
    I: PRIOR_OWNERSHIP_EXHAUSTION_FILTERS_PRESERVED
  next_step: CONTINUE_RESIDUE10_F_AFTER_F0062_OR_MATERIAL_NEW_SOURCE_DELTA
```

No shared root, peer namespace, canonical claim, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified by this invocation. This file is the single immutable run report.