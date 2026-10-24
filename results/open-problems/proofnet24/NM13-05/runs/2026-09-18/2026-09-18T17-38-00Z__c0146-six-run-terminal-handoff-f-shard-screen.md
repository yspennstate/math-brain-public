Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: C0146 `m_cert = 9 -> 9`; this is the sixth consecutive unchanged run, so C0146 is terminally handed off under the CLOSABLE rotation rule. Successor status: ADMISSION_PENDING; Section-B #2/#8/#11 were not attempted because no successor crossed admission.**

# NM13-05 — C0146 terminal six-run handoff and complete intake-F residue-4 successor screen

Run date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-05/`  
Category: **CLOSABLE OUTSIDE**  
Exclusive selection shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 4`

## 1. Runtime and control-plane disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task/automation control schema still contains prompt/title, schedule/start, timing mode, enabled state, and task identity, but no bindable model-family selector and no bindable reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model/effort fields plus authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` event is an authorization-context boundary; the lawful workaround is an owning/otherwise-authorized context or authorized platform/admin support, never task duplication or access-control bypass.

No schedule was modified in this run.

## 2. Authoritative continuity recovered before acting

I started from the newest immutable NM13-05 report:

`proofnet24/NM13-05/runs/2026-09-18/2026-09-18T16-32-00Z__c0146-stuck-recovery-2-audit-kernel.md`

creation commit:

`84e82ef2a6a10fafd61694dbbff71d5b07eb101d`.

That report had already reached:

- source: **C0146 / Pete Question 13.2**;
- source mathematical status: **REFUTED**;
- frozen metric: `m_cert = 9`;
- `unchanged_runs = 5`;
- `stuck_recoveries = 2`;
- exact closure blocker: source-level independent PASS from **both P26 and NM13-06**;
- explicit instruction that one more unchanged invocation triggers terminal six-run handoff and rotation, not another C0146 lemma.

At this invocation I reread/recovered the required current state, including:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/C0146.md`;
- newest NM13-06 report;
- newest P26 report;
- current intake-F canonical ledger `probability_1000_intake_F_20260908/problems.jsonl`;
- intake-F attempt/search history for the residue-4 candidates encountered below;
- current claim/search surfaces for C0146 and the successor candidates.

The canonical C0146 claim still reads `Status: CLAIMED`, owner `proofnet24/NM13-05`; there is no owner-authorized release. A terminal rotation does **not** silently release ownership, and I did not edit the claim.

A pre-write master observation was

`2b5e2075600449e237cc7db776810248348c8301`

at 2026-09-18T17:36:24Z. Relative to the preceding NM13-05 report commit, master had advanced heavily; the relevant fresh changes included a new P26 run and a new NM13-06 admission-screen run, but neither contained a C0146 PASS.

## 3. C0146 terminal handoff

### 3.1 Canonical identity

- canonical problem / claim: `C0146`;
- claim path: `operations/claims/C0146.md`;
- source: Gábor Pete, *Probability and Geometry on Groups*, Question 13.2;
- exact source question: whether there is a monotone coupling `(omega_p)_{p in [0,1]}` of `FK(p,q)` for every `q in [0,1)`;
- canonical dedup key: `fk_q_less_than_1_monotone_coupling`;
- SHA256: `dd817e3ec8169668456ed767e35982573675498dec1367239155a22daa3f4ec6`;
- shard: `4 mod 13`.

### 3.2 Frozen metric and terminal counters

The frozen metric remains exactly the one established at admission:

`m_cert` = largest integer `m` for which NM13-05 has a rigorous source-valid certificate that every finite simple graph with at most `m` edges is stochastically monotone in `p` for every `q in (0,1)`.

This invocation makes no mathematical C0146 claim and does not redefine the metric.

- metric before: `9`;
- metric after: `9`;
- movement: **none**;
- unchanged-run counter: **`5 -> 6`**;
- stuck-recovery counter: **`2 -> 2`**;
- source status: **REFUTED -> REFUTED**;
- fleet closure: **NOT CLOSED — two independent audit PASSes still not recovered**.

Therefore the CLOSABLE six-unchanged rule now applies. NM13-05 must stop attacking C0146. This handoff preserves the work and ownership history; it is not an automatic release of the canonical claim.

### 3.3 Minimal source-level audit kernel

A future authorized auditor does not need the later sharpness/minimality work. The source is already refuted by the following exact finite witness.

Take the 7-vertex, 10-edge simple graph

`E = {(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,6),(5,6)}`

and the increasing event

`A = {(0,1) is open}`.

Use

`q = 1/40000`,

`p1 = 1/2001 < p2 = 1/1601`.

Exact exhaustive enumeration gives

`P_{p1,q}(A) = 72488985858351 / 205113593435351`,

`P_{p2,q}(A) = 108671022567040625 / 307499119349131441`,

with exact positive difference

`395372934751065824378379416 / 63072249347906220400541234970791`.

Thus an increasing event has *larger* probability at the smaller `p`. Stochastic domination fails, hence no monotone coupling can exist for this fixed positive `q`. This directly refutes Pete Question 13.2 as stated.

Primary exact checker / output:

- `proofnet24/NM13-05/artifacts/2026-09-18/c0146_qsmall_edge_counterexample.py`
- `proofnet24/NM13-05/artifacts/2026-09-18/c0146_qsmall_edge_counterexample.out`

The checker enumerates all `2^10 = 1024` configurations using exact integer/Fraction arithmetic and ends `ALL_EXACT_CHECKS_PASS`.

The full written argument is in:

`proofnet24/NM13-05/runs/2026-09-18/2026-09-18T12-02-00Z__c0146-positive-q-refutation.md`.

### 3.4 Supporting same-track results already preserved

The following are useful refinements but are **not needed** to audit the source refutation:

1. **All finite simple graphs with at most 9 edges are monotone in p for every q in (0,1).** This certifies `m_cert = 9` and makes the 10-edge witness edge-minimal within finite simple graphs.
2. The same 10-edge witness has an exact positive-q nonmonotonicity interval, first certified through `q <= 1/40000` and then sharpened through `q <= 1/32618`.
3. For the distinguished-edge marginal on that fixed graph, exact elimination/Sturm analysis gives an algebraic threshold `q_*` with `1/32618 < q_* < 1/32617`, and that marginal is nonmonotone iff `0 < q < q_*`.
4. Every 10-edge simple graph with at most six non-isolated vertices was exactly certified monotone, so among 10-edge simple counterexamples the minimum number of non-isolated vertices is exactly 7.

Relevant immutable reports, in chronological order:

- `2026-09-18T08-22-00Z__c0146-m5-monotone-coupling.md`
- `2026-09-18T09-23-00Z__c0146-m8-bernstein-transport.md`
- `2026-09-18T10-23-51Z__c0146-m9-graphic-matroid-bernstein.md`
- `2026-09-18T12-02-00Z__c0146-positive-q-refutation.md`
- `2026-09-18T12-39-00Z__c0146-q-interval-sharpening-prior-art.md`
- `2026-09-18T13-36-00Z__c0146-algebraic-edge-threshold.md`
- `2026-09-18T14-35-00Z__c0146-ten-edge-minimal-vertex.md`
- `2026-09-18T15-31-00Z__c0146-stuck-recovery-1-audit-priorart.md`
- `2026-09-18T16-32-00Z__c0146-stuck-recovery-2-audit-kernel.md`.

### 3.5 Prior-art boundary to preserve

The bounded literature record must remain conservative.

Noah Halberstam's 2023 Cambridge thesis states that finite-graph arboreal gas is not stochastically monotone in its edge-weight parameter, crediting Rémy Poudevigne via **private correspondence**. Arboreal gas is the `q -> 0`, `p = beta q` random-cluster limit. Therefore NM13-05 must **not** claim novelty for the qualitative q→0/small-positive-q nonmonotonicity mechanism.

What this track makes explicit and exactly reproducible is the particular 7-vertex/10-edge graph, rational positive-q parameters, exact event probabilities, nine-edge lower theorem, and subsequent finite/algebraic refinements. Publication novelty of those explicit refinements remains **UNVERIFIED**, because the private antecedent is inaccessible and a bounded search is not proof of worldwide novelty.

Fresh 2026 context also remains logically separate: Tang-Zhang (2026-09-10) treat q<1 negative correlation on high-degree regular graphs, and Park (2026-08-09) treats wired regular trees. Neither is a general all-finite-graph monotone-in-p coupling theorem.

### 3.6 Audit status at terminal handoff

Fresh repository recovery found:

- newest P26 report: it audits a P04 finite-field Fourier claim, **not C0146**;
- newest NM13-06 report: it is post-P0195 successor admission screening, **not a C0146 audit**;
- fresh exact repository searches for `C0146`, `C0146 PASS`, and the exact witness numerators did not recover an independent source-level PASS.

Hence:

`P26(C0146) = NOT PASSED`

and

`NM13-06(C0146) = NOT PASSED`.

The mathematical source statement is REFUTED, but fleet closure is not certified. Same-track work cannot manufacture the missing independent audits.

## 4. Forced successor rotation — canonical intake-F residue-4 screen

The pre-C0146 successor cursor had already exhausted the earlier custom-C backlog and the explicit-key E-series residue-4 screen. The next canonical cursor was intake F. I therefore resumed there rather than restarting from scratch.

I read all **140 canonical records** in

`probability_1000_intake_F_20260908/problems.jsonl`,

recovered each canonical `dedup_key` from the ledger, and hashed the canonical key itself — never an alias or problem ID. Exactly six canonical F records fall in NM13-05's residue-4 shard.

### 4.1 F0053 — excluded: resolved in literature

- problem_id: `F0053`
- dedup key: `borodin_gorin_integrable_2012::conjecture_7.6`
- SHA256: `58bd6c263ad5422306192b5e24d144fed555b4d4360be670c47cc7d5efbcf5a7`
- residue: `4`

The canonical intake marks this resolved by later literature (Matveev 2019 / Kerov conjecture line). It is not eligible and was not reopened.

### 4.2 F0056 — excluded: campaign-settled source problem

- problem_id: `F0056`
- dedup key: `janson_simply_generated_2012::problem_18.9`
- SHA256: `e83c19ac9090b23aa73149cbb3d74a815ef126735631695b56056e5e33db3dfe`
- residue: `4`

The campaign contains a complete-answer memo for Janson Problem 18.9 and the campaign index records the answered result. This is settled/attempted campaign history, not a fresh successor.

### 4.3 F0065 — excluded from CLOSABLE: genuine asymptotic HARD problem

- problem_id: `F0065`
- dedup key: `janson_simply_generated_2012::conjecture_20.5`
- SHA256: `b7f5220c2d818c2b98a5777eb648dede1c9557e2e2d80a133c656b2c8ca54911`
- residue: `4`

Literal source target: for critical simply generated trees with infinite variance, prove `H(T_n)/sqrt(n) ->_p 0`.

Later work gives only a polylogarithmically weaker general upper bound, while stable-domain subclasses are known. The universal remaining endpoint is an asymptotic height theorem, not a finite obstruction/short theorem/explicit extremizer target. Another fleet screen independently classifies it as asymptotic HARD. NM13-05 does not relabel it CLOSABLE merely to fill the slot.

### 4.4 F0116 — excluded from CLOSABLE: critical reconstruction asymptotic

- problem_id: `F0116`
- dedup key: `mossel_info_flow_trees_2004::conjecture_2_census_critical`
- SHA256: `adca15cb670230d5b0c8a38cea8f6df9fb3a735c5cba2f739e31cd9a768df33d`
- residue: `4`

Literal target: for a general finite-state channel on the b-ary tree at the Kesten-Stigum equality `b|lambda_2(M)|^2 = 1`, prove census reconstruction is impossible. Special model classes are known, but the source asks a general depth-asymptotic theorem. The intake also carries a prior attempt. No finite computation can by itself certify the universal n→∞ statement. This is a HARD reconstruction problem, not a CLOSABLE finite endpoint.

### 4.5 F0127 — excluded from CLOSABLE: broad mean-field coalescence classification

- problem_id: `F0127`
- dedup key: `aldous_social_dynamics_2013::open_problem_2_coalescence`
- SHA256: `a97fc06fb71f639077f6e606c47a8b1a12434f2586072bce4ccdafd3bab18b38`
- residue: `4`

The source asks, under an asymptotic typical-pair meeting-time condition, **what further conditions** imply `E T^coal ~ 2 tau_meet`. Oliveira gives important sufficient mean-field regimes, but the remaining problem is a broad asymptotic classification, not one frozen finite threshold or obstruction whose exact certificate can close the source. The intake contains prior work. This is not a clean CLOSABLE successor.

### 4.6 F0138 — excluded: positively reconciled as KNOWN/resolved

- problem_id: `F0138`
- dedup key: `quastel_spohn_kpz_2015::conjecture_2.9_two_point_airy2`
- SHA256: `5fc2e6132204af192193360d28bf4c589834cb9a259eff4c561d9a48644895a4`
- residue: `4`

Although the old intake row says unverified/open, later repository reconciliation has already positively identified this narrow-wedge KPZ two-point Airy2 limit as following from published KPZ fixed-point convergence (Quastel-Sarkar/JAMS line). Current fleet reports explicitly mark F0138 KNOWN/resolved. It is therefore excluded and not reopened under stale intake status.

## 5. Successor admission result

After completing the canonical intake-F residue-4 screen, **no F candidate passes the CLOSABLE architecture/status gate**:

- `F0053`: resolved;
- `F0056`: campaign-settled;
- `F0065`: genuine asymptotic HARD;
- `F0116`: genuine asymptotic HARD / previously attempted;
- `F0127`: broad asymptotic classification / previously attempted;
- `F0138`: later positively reconciled as KNOWN/resolved.

Therefore:

**SUCCESSOR ADMISSION = ADMISSION_PENDING.**

No new canonical claim was created. No ownership conflict was risked. Screening is not counted as mathematical progress.

The durable successor cursor advances to:

`probability_1000_intake_G_* / first unscreened canonical record (G0001)`.

The next invocation should begin from that cursor, first checking delta changes to claims/POSTED/campaign status and then screening canonical residue-4 G identities. It must not restart C0146 and must not rescan F unless a material owner/status delta appears.

## 6. Section-B accounting

This run is a mandatory terminal handoff plus admission screen, not a mathematical attack run.

The successor's initial reserved methods remain:

- **#2 ATTACK THE NEGATION FIRST**;
- **#8 DISCRETIZE**;
- **#11 DUALIZE**.

They were **not attempted** because no successor crossed admission. I do not misreport screening as mathematical progress or credit these methods prematurely.

No additional C0146 method was attempted because the six-run rotation rule forbids extending a stalled CLOSABLE target with another lemma after the terminal counter is reached.

## 7. Operational safeguards / mutations

This invocation created exactly one immutable file: this report.

I did **not**:

- modify `operations/claims/C0146.md` or any other canonical claim;
- create a successor claim;
- edit `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign roots, or any shared root;
- edit any peer namespace;
- create a checker or theorem artifact merely to fill the run;
- run workflows or external scripts;
- use email, Gmail, Drive, public posting, paid compute, or permission changes;
- create, edit, disable, or duplicate a schedule.

No D-series ownership or closure was changed.

## 8. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-05
  namespace: proofnet24/NM13-05
  category: CLOSABLE_OUTSIDE
  selection_shard:
    modulus: 13
    residue: 4
    hash_basis: canonical_dedup_key_utf8_sha256

  outgoing:
    source_id: C0146
    claim_path: operations/claims/C0146.md
    dedup_key: fk_q_less_than_1_monotone_coupling
    source_status_before: REFUTED
    source_status_after: REFUTED
    fleet_closure_before: NOT_CLOSED_AUDITS_PENDING
    fleet_closure_after: NOT_CLOSED_AUDITS_PENDING
    metric:
      name: m_cert
      before: 9
      after: 9
      movement: false
    counters:
      unchanged_runs_before: 5
      unchanged_runs_after: 6
      stuck_recoveries_before: 2
      stuck_recoveries_after: 2
    audits:
      P26: NOT_PASSED
      NM13_06: NOT_PASSED
    disposition: TERMINAL_SIX_UNCHANGED_HANDOFF_ROTATION_REQUIRED
    claim_release: false
    exact_audit_kernel:
      vertices: 7
      edges: 10
      q: 1/40000
      p1: 1/2001
      p2: 1/1601
      increasing_event: edge_01_open
      exact_gap_positive: 395372934751065824378379416/63072249347906220400541234970791

  successor:
    admission_before: ROTATION_REQUIRED
    admission_after: ADMISSION_PENDING
    source_id: null
    claim_path: null
    metric_before: UNMEASURED
    metric_after: UNMEASURED
    mathematical_progress: false
    intake_family_completed: F_20260908
    residue4_records:
      - F0053
      - F0056
      - F0065
      - F0116
      - F0127
      - F0138
    methods_reserved_not_attempted: [2, 8, 11]
    next_screening_cursor: G0001

  shared_root_edits: none
  peer_namespace_edits: none
  claim_mutations: none
  substantive_artifacts_created: none
```

## 9. Next step

On the next NM13-05 invocation:

1. do a delta-only check for any new C0146 independent audit/closure record, but **do not resume C0146 attacking research**;
2. start successor screening at canonical intake G, cursor `G0001`, recovering canonical identities before hashing;
3. enforce residue `4 mod 13`, current/historical ownership, handoff, attempts, POSTED/campaign exclusions, and current literature before any claim creation;
4. if a genuinely CLOSABLE unclaimed source passes, create its canonical `operations/claims/<ID>.md` with create-only semantics, read it back, freeze one metric, and continue in the same invocation with actual methods #2/#8/#11;
5. otherwise retain ADMISSION_PENDING and advance the durable cursor without counting screening as mathematics.
