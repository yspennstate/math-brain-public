Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; Section-B methods #2/#11/#24 remain unspent because no source crossed admission.**

# NM13-01 — successor admission screen 3

Date: 2026-09-18 UTC  
Track / namespace: `NM13-01` / `proofnet24/NM13-01/`  
Category: `CLOSABLE OUTSIDE`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Exclusive shard: `int(SHA256(UTF-8 canonical_dedup_key).hexdigest(),16) mod 13 = 0`

## 1. Runtime disclosure and controlling continuity

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still has ordinary task fields such as title/prompt, schedule/relative start, timing mode and enabled state, but no bindable model-family selector and no bindable reasoning-effort selector. Making GPT-6/maximum enforceable would require an owner-authorized product/workspace/API/admin surface exposing those controls together with authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` response remains an authorization-context boundary; repository history also records a later P26 update succeeding from another authorized context. The lawful workaround is the owning/otherwise-authorized surface or platform/admin support, not cloning or bypassing access controls. No schedule was modified in this invocation.

The controlling predecessor is the immutable NM13-01 report

`proofnet24/NM13-01/runs/2026-09-18/2026-09-18T05-10-30Z__admission-screen-2.md`

at creation commit `ef32a3a9c6e2fc22b971bee3050af75601044c19`. It preserves the P0292 six-unchanged-run handoff and explicitly forbids reopening P0292. It also completed the canonical residue-0 Codex P0001--P0488 screen and the F0001--F0037 intake screen. Its durable next cursor was F0038.

Before advancing that cursor I reread/recovered the owner-required current surfaces: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the newest own report above; newest neighboring NM13-02 and stochastic-process-adjacent NM13-09 reports; the F/G/H problem and attempt ledgers; current claim/history searches; and the current branch head. Just before this report write, `master` was at `9ecfcce03409512f7c8b4b1e7287969fc24c120d` (2026-09-18T06:12:23Z). Concurrent commits since the previous NM13-01 report added ownership/claim material elsewhere but no owner-authorized release relevant to the candidates below.

Large JSONL files are connector-bounded when rendered wholesale. I therefore advanced from the immutable prior cursor using exact line-range fetches, literal canonical `dedup_key` values where present, the intake README/attempt ledgers, and fleet-established canonical fallback for H. I do not claim a byte-for-byte reread of every historical file in one connector response.

## 2. F intake F0038--F0140: shard screen completed through EOF

The F ledger supplies explicit canonical `dedup_key` fields, so no title alias was hashed. The prior report had completed F0001--F0037. I screened F0038--F0140 and found exactly nine additional residue-0 rows:

| ID | canonical dedup key | SHA-256 | disposition |
|---|---|---|---|
| F0046 | `talagrand_small_2016::conjecture_8.1` | `ccf852eeb6201c9eb01e792c79c48cfedca408a29cd219aac3006f0e2a507880` | **EXCLUDED / resolved in literature** in the intake |
| F0051 | `lps_minimal_spanning_forests_2006::question_6.7` | `3eadb48ab2c26a7d4b27688f838b8d2608a89989dee97ea251aed00b8e13d616` | **EXCLUDED / resolved in literature** in the intake |
| F0067 | `janson_simply_generated_2012::problem_20.7` | `6ad6488fb20faf552d19d381db0e0d627b6ce59e8299d425a7495a6d86506207` | asymptotic subcritical-tree height theorem; prior attempt/partial literature; **HARD, not CLOSABLE** |
| F0076 | `velenik_interfaces_2006::open_problem_10` | `e78a2e556677b5b14f293c8a0d56422e4282d46501e00d6a3facb754daaea510` | 2D continuous-interface wetting transition; **HARD/infinite-volume** |
| F0101 | `talagrand_prizes_2016::convolution_problem_cube` | `eaed9e97e7568356f2de221ab8583ed34ac2eb43e498d1b7dddc17ca0c13f3aa` | global dimension-free convolution inequality; **HARD**, not a finite certificate target |
| F0108 | `talagrand_small_2016::conjecture_8.5` | `4cffc1022bead84a2ea319b7cb9a1e737c94140e03f76411bfd91f42417b795a` | universal domination inequality over spread measures; **HARD** |
| F0117 | `mossel_info_flow_trees_2004::conjecture_3_below_ks_potts` | `60c61d87886fe691bf212b2b1ae0eef3ac6e86d2c1090d196c56aaed8ef3223f` | partially resolved reconstruction threshold; residual small-degree q=3/4 problem is **HARD**, not source-faithful CLOSABLE |
| F0118 | `mossel_info_flow_trees_2004::conjecture_4_monotone_in_q` | `aee0608a4a7de1230bcac05e279c0b6d2c305c12f9c810314c6ec58ba54c5bb3` | universal monotonicity in Potts state count; **HARD** reconstruction theorem |
| F0134 | `guionnet_ld_rmt_2004::conjecture_5.1_genus_expansion` | `2179ab4b91fd226e135a2d8124bdfea0312629ada83e697d50bd9f4aa90fe2a3` | **EXCLUDED / resolved by Ercolani--McLaughlin** in the intake |

The F README records one substantive attempt for every admitted F row, so none of the six unresolved residue-0 F rows above is genuinely previously unattempted. That is not by itself fatal, but it weakens them relative to the owner's preference and matters because all six also fail the honest-CLOSABLE shape gate.

### Closest subject-fit F candidate: F0117

F0117 is the closest new residue-0 source to this worker's Markov/probability focus. The source is Mossel's 2004 survey conjecture that for every Potts state count q>=3 there should be some regular-tree branching factor and channel below the Kesten--Stigum bound where reconstruction remains solvable. Later work proves non-sharpness for q>=5 and proves Kesten--Stigum tightness/non-reconstruction below the bound for q=3 and q=4 in sufficiently large-degree regimes. A fresh bounded 2026-09-18 search recovered Mossel--Sly--Sohn, *Exact Phase Transitions for Stochastic Block Models and Reconstruction on Trees* (Annals of Probability 53 (2025), arXiv:2212.03362), which explicitly states the q=3/4 large-degree result and q>=5 non-sharpness. I found no source-matching theorem in this bounded search closing the residual small-degree q=3/4 existence question.

That does **not** make F0117 CLOSABLE. A positive answer in the residual regime requires an infinite-depth reconstruction theorem for an explicit channel/tree pair; a negative answer for q=3/4 requires a theorem across all remaining branching factors/parameters. A finite-depth numerical witness is not the source statement. I therefore did not invent a finite proxy metric and did not claim F0117.

## 3. G intake G0001--G0015: one residue-0 row, but present-status gate fails

The G ledger also supplies explicit canonical `dedup_key` values. Exactly one of G0001--G0015 hashes to residue 0:

`G0005 = flammant_finite_graph_2026::kozma_nitzan_conjecture_3`

with

`SHA256 = 1cdf631650d26b1e12ee5ef6df2c0e039694816cd76c14a86d9e7c6aee1af990`.

The row is Flammant's restatement of Kozma--Nitzan's finite-graph continuity consequence: for every eta>0 there should be delta(eta)>0 such that `P[o<->A]>1-delta` and `P[a<->z]>1-delta` for every a in A imply `P[o<->z]>1-eta`. The intake README explicitly warns that G0005 was recorded from Flammant's restatement rather than the original Kozma--Nitzan paper. The underlying original source is Kozma--Nitzan, *A reduction of the theta(p_c)=0 problem to a conjectured inequality* (arXiv:2401.12397). I therefore preserved that source alias instead of treating the Flammant row as a separate problem.

The historical substantive attempt `G0005-A001` is also preserved. It proves by a union bound plus FKG that

`P[o<->z] >= 1 - delta - delta E[N_A]`,

where `N_A` is the number of A-points joined to o, so the conjecture follows when `E[N_A]` is bounded. The attempt explicitly identifies the obstruction: in the intended large-boundary instances `E[N_A]` can grow, so the union bound is wasteful.

### Fresh 2026-09-18 current-status correction

A bounded current web search materially changes the admission posture. A September 3, 2026 technical report, *on the continuity of the percolation phase transition*, describes a pinned August 28, 2026 `anthropics/formal-math` Lean 4 artifact which it says proves a new finite weighted-graph covariance inequality, settles the Kozma--Nitzan finite-graph conjecture, and consequently proves `theta(p_c)=0` for nearest-neighbour Bernoulli bond percolation in every d>=2. The report is explicit that this is an **unrefereed formal artifact** and that correspondence between the formal statement and intended percolation objects still requires expert audit. Public MathDB pages crawled on 2026-09-18 still list the Kozma--Nitzan conjecture as unresolved, so the public status is not yet fully reconciled.

That discrepancy is exactly why G0005 cannot be admitted today: there is now a concrete source-matching solution claim requiring reconciliation, so the `present literature status` admission gate does not pass. Independently, G0005 is a universal theorem strong enough to imply `theta(p_c)=0` in all dimensions, and prior fleet screens already classify it as HARD rather than a finite-certificate CLOSABLE target. No canonical G0005 claim was created.

This status correction should be reconciled by a shared-root writer/P26 or coordinator; NM13-01 does not edit shared ledgers.

## 4. H intake H0001--H0025: aliases recovered before shard use

H rows do not carry a `dedup_key`. Following the established fleet fallback, I first formed exact `source_id::locator` identities, but then checked aliases against earlier canonical rows before treating a nominal residue as selectable. The fleet-established H residue sequence shows two nominal residue-0 fallback identities: H0010 and H0013.

### H0010 is not a residue-0 canonical problem

The fallback identity

`arxiv_2608_21125::Conjecture 3.2 (Uniform integrability of the derivative martingale ⇒ Bramson delay); Section 3.2`

hashes to residue 0 (`b6921aa8dc1c253b738542872aa7a21af05cf5c8b60b16c39e011924a641f9bc`). But H0010 is the **same exact source conjecture** already represented as G0014, whose explicit canonical dedup key is

`kumar_dudeja_threshold_cascades_2026::conjecture_3.2`,

and that canonical key hashes to residue **9**, not 0. Under the owner's alias rule H0010 therefore cannot create residue-0 ownership for NM13-01. It is an alias, not a new candidate.

### H0013 is residue 0 but already settled in campaign state

The exact fallback identity

`arxiv_2607_07410::Remark 5.3(ii), first case (L^{w1+W}); Section 5`

hashes to

`89e49c9c007191ca00ee9569a89f857200ca28cf014fd7371fc72681e99704e0`, residue 0.

However campaign `INDEX.md` already records the Shiozawa--Wang Levy-drift compactness Remark 5.3(ii) scope (H0013/H0014) as settled: **NO for every confinement power**. It is therefore excluded from new ownership. The H verification ledger also explicitly marks H0001/H0015/H0016 as duplicates of earlier canonical problems, which is further evidence that H aliases must not be treated as fresh identities.

Thus H0001--H0025 contains no admissible residue-0 source after canonical alias reconciliation.

## 5. Admission verdict

**ADMISSION_PENDING. No canonical claim was created.**

This invocation screened 143 additional nominal rows (F0038--F0140, G0001--G0015, H0001--H0025) without counting that screening as mathematical progress. No candidate simultaneously passed:

1. canonical identity and residue exactly 0 after alias reconciliation;
2. exact source statement presently unresolved at a sufficiently reconciled status;
3. no current/historical ownership, handoff, retirement, posted/settled exclusion, or duplicate identity;
4. honest `CLOSABLE OUTSIDE` shape with a plausible exact constant, finite counterexample/certificate, or short theorem endpoint;
5. no exhausted source reopened under a new ID.

Therefore:

- source ID: **none**;
- claim ID/path: **none**;
- metric before: **UNMEASURED**;
- metric after: **UNMEASURED**;
- mathematical movement: **none**;
- Section-B methods credited: **none**;
- #2 ATTACK THE NEGATION FIRST: **not tried**;
- #11 DUALIZE: **not tried**;
- #24 FIND THE EXTREMAL OBJECT: **not tried**;
- successor unchanged-run counter: **0 / not started**;
- successor stuck-recovery counter: **0 / not started**;
- P26 audit: **not applicable**;
- NM13-02 audit: **not applicable**.

No checker, theorem artifact, certificate, paper folder, audit request, claim file, shared-root edit, peer edit, workflow, permission change, public post, email/Drive action, paid compute, or schedule modification was made.

## 6. Durable screening cursor

The canonical NM13-01 cursor now stands at:

- Codex P0001--P0488: complete from preceding immutable screens;
- F0001--F0140: complete through EOF;
- G0001--G0015: complete through EOF;
- H0001--H0025: complete through EOF, with H aliases reconciled before selection;
- successor research counters: not started because no source has been admitted.

The next invocation should **not** restart F/G/H. It should first delta-check queue/intakes/claims/handoffs/status corrections since this report, then advance into intake I by recovering canonical identities/aliases before hashing. Intake-I rows often lack explicit `dedup_key`, so title strings or I-numbers must not be hashed as aliases. Existing I ownership/retirement exclusions from prior screens (including I0010, I0027 and I0032) remain preserved. If no I source passes, retain an exact I cursor and continue; do not manufacture a proxy metric.

## 7. Bounded literature checks recorded

Date: 2026-09-18. Scope was intentionally bounded and is **not** a proof of worldwide openness or novelty.

- F0117 queries: `Mossel information flow trees Conjecture 3 Potts reconstruction q=3 q=4 small degree Kesten Stigum 2026` and variants. Recovered Mossel--Sly--Sohn (2025) for q=3/q=4 sufficiently large degree and q>=5 non-sharpness; no source-matching residual small-degree closure found in the returned results.
- G0005 queries: `Kozma Nitzan finite graph percolation conjecture solution theta pc 2026 Lean covariance inequality` and variants. Recovered Kozma--Nitzan's original arXiv:2401.12397, current MathDB pages still marking the conjecture unresolved, and the September 3, 2026 report of the August 28 Lean artifact claiming a solution. Because the artifact is explicitly unrefereed and statement correspondence is not independently audited here, I record a **present-status conflict**, not a closure verdict.

Access limitation: web search and repository connectors provide bounded indexed views; I did not obtain an independent line-by-line referee audit of the external Lean development in this invocation.

## 8. Structured ledger delta for P26

```yaml
ledger_delta:
  task: NM13-01
  category: CLOSABLE_OUTSIDE
  run_status: ADMISSION_PENDING
  shard_residue_required: 0
  source_id: null
  canonical_dedup_key: null
  claim_id: null
  claim_path: null
  metric:
    name: UNFROZEN_UNTIL_ADMISSION
    before: UNMEASURED
    after: UNMEASURED
  mathematical_progress: false
  methods_attempted: []
  reserved_first_methods: [2, 11, 24]
  successor_unchanged_research_runs: 0
  successor_stuck_recoveries_used: 0
  predecessor:
    source_id: P0292
    state: HANDED_OFF_AFTER_SIX_UNCHANGED_RUNS
    must_not_resume_by_NM13_01: true
  screening_delta:
    F0038_F0140:
      complete: true
      residue0: [F0046, F0051, F0067, F0076, F0101, F0108, F0117, F0118, F0134]
      admitted: []
      resolved_exclusions: [F0046, F0051, F0134]
      hard_or_nonclosable: [F0067, F0076, F0101, F0108, F0117, F0118]
    G0001_G0015:
      complete: true
      residue0: [G0005]
      G0005: PRESENT_STATUS_CONFLICT_EXTERNAL_UNREFEREED_SOLUTION_CLAIM_AND_HARD_SHAPE
    H0001_H0025:
      complete: true
      nominal_residue0_fallback: [H0010, H0013]
      H0010: ALIAS_OF_G0014_CANONICAL_RESIDUE9
      H0013: SETTLED_CAMPAIGN_SCOPE
      admitted: []
  bounded_literature_check_date: 2026-09-18
  audits:
    P26: NOT_APPLICABLE
    NM13-02: NOT_APPLICABLE
  next_screening_cursor: >-
    Delta-check source/status/ownership surfaces, then reconcile canonical identities
    and aliases in intake I from its unscreened front before hashing; never hash I-title
    aliases merely to force shard membership.
  new_claim_created: false
  substantive_artifact_created: false
  shared_root_edits: NONE
  peer_edits: NONE
```

This file is the single immutable NM13-01 run report for this invocation.