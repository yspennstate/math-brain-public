Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. ADMISSION_PENDING / NO MATHEMATICAL MOVEMENT: successor metric `UNMEASURED -> UNMEASURED`; Section-B methods #2/#6/#30 remain genuinely unspent because no successor crossed admission.**

# NM13-12 — post-E0086 successor admission delta screen 13: P0219 gains a discrete Hammersley bridge but remains PENDING / NOT READY

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-12` / `proofnet24/NM13-12/`  
Category: `HARD OUTSIDE`  
Exclusive selection shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 11`

## 1. Runtime truth and model-control surface

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. The exposed runtime provides no authenticated reasoning-effort telemetry, so reasoning is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed scheduler/task-control surface still provides task title/prompt, schedule or relative-start data, timing mode, enabled state, listing and update operations. It exposes **no model-family selector, no reasoning-effort selector, and no authenticated completed-run receipt of the applied model/effort**. Thus `GPT-6 / maximum` remains prompt text only. A real fix would require an owner-authorized product/workspace/API/admin scheduler surface with persistent model-family and reasoning-effort fields, propagation of those fields into inference routing, and trustworthy per-run attestation.

The historical P26 response `You cannot modify this task` remains an authorization/context boundary. Current repository continuity records that a later authorized context did successfully update P26. The lawful remedy for a denied task is the owning/authorized product/workspace/API/admin context or platform support; do not duplicate the task, bypass permissions, or treat a repository edit as native scheduler repair. This invocation makes **no scheduler modification**.

## 2. Authoritative continuity recovered

The controlling predecessor is the immutable NM13-12 report

`proofnet24/NM13-12/runs/2026-09-19/2026-09-19T02-02-30Z__post-e0086-admission-delta-screen-12-p0219-pending.md`,

creation commit

`a45c226c429b9865f986ee4933e1885dc2ac0805`.

Its durable state is preserved:

- `ADMISSION_PENDING`;
- successor metric `UNMEASURED`;
- screening cursor `STRICT_DELTA_ONLY_RESIDUE_11_AFTER_SCREEN_12`;
- successor Section-B methods #2/#6/#30 unspent;
- successor unchanged-run and stuck-recovery counters `NOT_STARTED` because no successor is admitted;
- P0483 and E0086 remain under binding terminal HARD handoffs and are not restartable by this worker absent an explicit owner-authorized reassignment.

Before the admission decision I reread/recovered current state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment/deployment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the preceding NM13-12 report above;
- current neighboring NM13-11 and NM13-13 admission state;
- current P0219 screens from R01, R06 and related admission reports;
- current R15 retained-screen work on F0111;
- current P26 report/model-control evidence;
- canonical claim lookup for P0219;
- candidate-specific canonical identity/prior-attempt continuity from the intake/campaign records;
- current source/literature evidence for P0219 and the F0111 sentinel;
- and the exact predecessor-to-prewrite Git comparison.

The intake/source/attempt JSONLs are large append-only ledgers. I do not claim to have visually rerendered every historical byte this run. The completed static residue-11 reconciliation from prior NM13-12 reports is carried forward only because the exact repository delta below contains no mutation to any `probability_1000_intake_*/problems.jsonl`, attempt ledger, queue root, or canonical claim file. Candidate-specific P0219 identity and prior-attempt state were rechecked. A search miss, absent claim path, stale `admitted:true`, disabled scheduler, or terminal handoff is never treated as proof of free ownership.

## 3. Exact repository delta since screen 12

Final prewrite `master` snapshot inspected:

`69185f9c1bb3bce500c5cabe1c819cbc5f763180`.

The exact GitHub comparison

`a45c226c429b9865f986ee4933e1885dc2ac0805 .. 69185f9c1bb3bce500c5cabe1c819cbc5f763180`

is **68 commits ahead and 0 behind**, with `too_large=null`.

The complete changed-file set contains research reports and substantive artifacts from other tracks, but **no mutation** to:

- root `QUEUE.md`;
- root `POSTED.md`;
- root `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- any `probability_1000_intake_*/problems.jsonl` source ledger;
- any probability attempt ledger;
- any controlling policy/amendment file;
- any `operations/claims/*.md` canonical claim file.

Accordingly there is no new source row, dedup correction, canonical claim creation, claim deletion, explicit release, or owner-authorized reassignment in this interval. No static corpus rerun is justified merely to manufacture activity.

Neighbor continuity also remains non-releasing: the current NM13-11 and NM13-13 reports remain `ADMISSION_PENDING` in their own shards, with their successor metrics unfrozen and their predecessor hard-source handoffs preserved.

## 4. Material residue-11 update: P0219 now has a closer discrete Hammersley bridge, but admission is still blocked

The strongest subject-matching residue-11 lead remains

`P0219 — High-density oriented percolation flow asymptotics`.

Canonical continuity remains:

- source/problem ID: `P0219`;
- source: David Aldous, *A discrete Hammersley process as an extreme case of oriented percolation flows*;
- canonical dedup key: `high-density_oriented_percolation_flow_asymptotics`;
- SHA-256: `77b9c00d0e9ccd64917689dc1ffb6ba9918efbf2d5975a913593b39da40ac3ea`;
- canonical shard: **11 mod 13**;
- historical campaign state: `attempted_unsolved`;
- current same-ID canonical claim path `operations/claims/P0219.md`: **absent / 404**.

The missing claim file is still **not** free ownership because current repository lifecycle evidence keeps P0219 as a live `PENDING_NOT_READY` replenishment lead. The owner policy is explicit that PENDING is not READY.

### Exact source target

Aldous defines a maximum open flow `V(n,p)` through the oriented square and the deterministic limiting density `v(p)` by

`V(n,p)/(2n) -> v(p)` in `L^1`,

and conjectures the explicit high-density asymptotic

`1 - v(p) ~ sqrt(2(1-p))` as `p -> 1`.

Equivalently, writing `q=1-p`, the source rewrites the deficiency through `U(n,1-q)`, the minimum number of boundary-to-boundary oriented paths that cover all closed directed edges, and explains the coefficient by a rare-defect Hammersley heuristic. The source itself warns that the difficult step is an interchange between the infinite-volume and high-density limits.

### New R01 prior-art bridge

The material delta since NM13-12 screen 12 is R01's fresh identification of Timo Seppäläinen, *Increasing sequences of independent points on the planar lattice*, Annals of Applied Probability 7 (1997), DOI `10.1214/aoap/1043862416`.

For independent Bernoulli marks of density `r` on the planar lattice, Seppäläinen gives an exact diagonal shape function whose interior formula reduces to

`Psi_r(1,1) = 2 sqrt(r)/(1+sqrt(r)) = 2 sqrt(r) + O(r)`.

This is much closer to Aldous's model than the previous continuum-Poisson-only heuristic. It suggests that the coefficient `sqrt(2)` could potentially be obtained from a discrete shape theorem before sending `q -> 0`.

R01 also isolates a precise deterministic comparison. If `W(n,q)` is the width of the reachability poset on the closed directed edges and `U(n,1-q)` is Aldous's edge-disjoint path-cover number, then

`W(n,q) <= U(n,1-q)`.

The missing source-level transfer separates into two obligations:

1. a Bernoulli-width asymptotic with the correct `2 sqrt(2q)` first-order coefficient; and
2. a routing-tax estimate

`U(n,1-q) - W(n,q) = o(n sqrt(q))`

in the source's sequential limit.

The exact bridge is not yet proved because Aldous's defects live on two edge orientations / an edge-midpoint periodic lattice, strict versus weak comparability matters, and an abstract chain cover does not automatically extend to a simultaneously edge-disjoint family of lattice paths. Those connector conflicts are invisible to the poset width.

R06's subsequent prior-art gate independently retains P0219 as `PENDING_NOT_READY` and states that a responsible READY certificate now must identify or sharply distinguish Aldous's two-orientation functional from the solved strict/weak Bernoulli Hammersley/LPP models and settle the routing-tax scope, rather than merely note that the source looks open.

This is a **real screening improvement** but **not NM13-12 mathematical progress**: no source metric is frozen, no source claim exists, and NM13-12 has not spent its prescribed methods.

## 5. F0111 sentinel: new second-order obstruction, still an R15 pending screen

The other standing residue-11 lead remains

`F0111 — Talagrand, Are Many Small Sets Explicitly Small?, Problem 10.9`,

canonical key `talagrand_small_2016::problem_10.9`.

It has prior attempt history and remains R15's active retained screen: `PENDING / NOT READY / SELF_CHECK_ONLY`. It is not lawful NM13-12 inventory.

R15's newest report adds an exact second-order necessary gate for positive quadratic `C_1` contacts in the heterogeneous cardinality-two problem. In normalized coordinates, the contact masses must satisfy a positive-semidefinite Hessian matrix condition `M(e) >= 0`. R15 then gives an analytic `n=16` two-level family that rigorously kills its preceding curvature-aligned rank-one pair-mass candidate despite nonnegative contact coefficients, while showing that a different curvature-sparing positive quadratic contact can pass the complete local Hessian gate on the same family.

This is useful progress in identifying why the current local compiler fails, but it does not solve Talagrand's universal-constant Problem 10.9, does not provide an ownership release, and does not make F0111 READY for NM13-12.

## 6. Fresh source and literature checks, dated 2026-09-19 UTC

P0219 checks included:

- Aldous's maintained open-problem page for *A discrete Hammersley process as an extreme case of oriented percolation flows*;
- exact-formula searches for `1-v(p)` and `sqrt(2(1-p))`;
- title/phrase searches for later work on the same oriented-percolation-flow functional;
- Seppäläinen 1997 and related Bernoulli Hammersley/LPP terminology.

The maintained Aldous page remains accessible and still states the conjecture and the interchange-of-limits obstacle. Seppäläinen 1997 is genuine exact prior art for an independent Bernoulli lattice Hammersley model. The bounded search did not recover a later primary paper explicitly identifying Aldous's two-orientation edge-disjoint cover with that solved model or proving the exact source asymptotic. That is **bounded negative evidence only**, not proof of worldwide openness or publication novelty.

For F0111 I also repeated an exact-label/source-title check around Talagrand Problem 10.9. The recent surrounding Talagrand threshold/discrete-convexity program remains active, but the bounded query did not surface an explicit source-matching resolution of the retained Problem 10.9. Again, this is negative bounded evidence only.

## 7. Admission decision

**Decision: `ADMISSION_PENDING`. No canonical successor claim is created.**

No candidate in the material delta simultaneously clears all mandatory gates:

1. exact source and canonical identity recovered before hashing;
2. canonical residue exactly 11;
3. literal source statement preserved without inventing a residual problem;
4. current source/literature compatible with unresolved exact scope under bounded checks;
5. prior attempts, historical assignments, handoffs, claims, POSTED/campaign exclusions, and current screens reconciled;
6. genuinely unassigned and **READY**, not merely absent from `operations/claims/` and not merely PENDING;
7. a realistic source-faithful HARD quantitative/finite milestone;
8. one stable source metric that can be frozen without inventing a zero baseline.

P0219 passes the source, subject, canonical identity, shard and quantitative-shape gates, but still fails gate 6: current fleet continuity explicitly retains it as `PENDING_NOT_READY`, and the new Seppäläinen bridge adds a prior-art/model-identification obligation rather than removing it. F0111 likewise fails gate 6 as an active R15 retained screen. No new residue-11 source or release appeared in the exact repository delta.

Therefore:

- successor source ID: `NONE`;
- successor canonical dedup key: `NONE`;
- successor claim ID/path: `NONE`;
- successor metric before: `UNMEASURED`;
- successor metric after: `UNMEASURED`;
- mathematical movement by NM13-12: **none**;
- screening counted as mathematical progress: **no**;
- successor unchanged-run counter: `NOT_STARTED`;
- successor stuck-recovery counter: `NOT_STARTED`;
- P26 audit: `NOT_APPLICABLE_NO_SUCCESSOR_CLAIM`;
- NM13-13 audit: `NOT_APPLICABLE_NO_SUCCESSOR_CLAIM`.

### Section-B accounting

No Section-B mathematical method was legally attempted by NM13-12 because no successor passed admission. Source reading, hashing, ownership reconciliation, Git-delta inspection and literature screening are admission/bookkeeping, not mathematical attacks.

The prescribed first successor triple therefore remains genuinely **unspent**:

- #2 **ATTACK THE NEGATION FIRST** — not attempted on an admitted successor;
- #6 **DEFORM TO A POINT YOU CAN SOLVE** — not attempted on an admitted successor;
- #30 **DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME** — not attempted on an admitted successor.

R01's use of #6/#20/#29 on its P0219 screen and R15's use of its own methods are neighboring-track research; they do not count as NM13-12 attempts.

No checker, finite certificate, theorem artifact, paper folder or audit request is warranted for `UNMEASURED -> UNMEASURED`.

## 8. Durable cursor and next lawful trigger

Admission-screen count advances **12 -> 13**. This is a screening counter only and is **not mathematical progress**.

New durable cursor:

`STRICT_DELTA_ONLY_RESIDUE_11_AFTER_SCREEN_13`

Do not rerun the completed static corpus merely to create activity. Re-enter the full admission gate only on a material trigger such as:

- a new or materially corrected canonical source row whose recovered dedup key hashes to residue 11;
- an owner-authorized, non-exhausted release/reassignment of an eligible residue-11 source;
- a formal coordinator/owner **READY promotion** of P0219 after the Bernoulli-Hammersley identity/distinction and routing-tax scope are responsibly settled, while the source remains unclaimed;
- a current-literature correction changing the exact source status;
- or a canonical dedup/alias correction exposing previously mis-sharded genuinely unassigned residue-11 inventory.

If P0219 later lawfully crosses admission, freeze the source process exactly and choose one source-level quantitative metric before doing mathematics. A natural source metric is the proved leading high-density coefficient in

`(1-v(1-q))/sqrt(q)`,

with baseline `UNMEASURED` unless a genuine certified bound is recovered. Then begin #2 by hunting source-valid edge environments or finite routing obstructions; #6 by deforming to the exact Bernoulli Hammersley model while writing the required error term; and #30 by proving one complete density/scale inequality, with any multiscale induction and summable error displayed explicitly.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: NM13-12
  category: HARD_OUTSIDE
  status_before: ADMISSION_PENDING
  status_after: ADMISSION_PENDING
  predecessor_report: proofnet24/NM13-12/runs/2026-09-19/2026-09-19T02-02-30Z__post-e0086-admission-delta-screen-12-p0219-pending.md
  predecessor_commit: a45c226c429b9865f986ee4933e1885dc2ac0805
  inspected_prewrite_master: 69185f9c1bb3bce500c5cabe1c819cbc5f763180
  repository_delta:
    ahead_by: 68
    behind_by: 0
    too_large: null
    source_ledgers_changed: false
    attempt_ledgers_changed: false
    queue_changed: false
    posted_changed: false
    results_changed: false
    campaign_index_or_ranking_changed: false
    canonical_claim_files_changed: false
    owner_policy_changed: false
  shard:
    modulus: 13
    residue: 11
  screening_count_before: 12
  screening_count_after: 13
  screening_cursor: STRICT_DELTA_ONLY_RESIDUE_11_AFTER_SCREEN_13
  successor:
    source_id: null
    claim_id: null
    claim_path: null
    metric_name: UNMEASURED
    metric_before: UNMEASURED
    metric_after: UNMEASURED
    movement: false
    unchanged_runs: NOT_STARTED
    stuck_recoveries: NOT_STARTED
  prescribed_first_methods: [2, 6, 30]
  methods_actually_attempted_on_admitted_successor: []
  prescribed_methods_remaining_unspent: [2, 6, 30]
  candidates:
    P0219:
      canonical_dedup_key: high-density_oriented_percolation_flow_asymptotics
      sha256: 77b9c00d0e9ccd64917689dc1ffb6ba9918efbf2d5975a913593b39da40ac3ea
      residue_mod_13: 11
      historical_status: attempted_unsolved
      same_id_claim: ABSENT_404
      lifecycle: PENDING_NOT_READY
      source_endpoint: "1-v(p) ~ sqrt(2(1-p)) as p -> 1"
      new_delta: "Seppalainen 1997 exact Bernoulli lattice Hammersley bridge; W<=U reduction; routing-tax U-W=o(n sqrt(q)) remains unproved/source-critical"
      admission_blocker: "PENDING is not READY; exact model identity/distinction plus routing-tax/current prior-art gate remains"
    F0111:
      canonical_dedup_key: talagrand_small_2016::problem_10.9
      residue_mod_13: 11
      lifecycle: R15_ACTIVE_PENDING_SCREEN_NOT_READY
      new_delta: "exact quadratic-contact SDP gate and analytic rank-one no-go on n=16 two-level family; source still unsolved"
  predecessor_handoffs_preserved: [P0483, E0086]
  audit_partners_if_completed: [P26, NM13-13]
  audits_requested: []
  checker_created: false
  theorem_artifact_created: false
  literature_checks_utc: 2026-09-19
  scheduler_modified: false
  shared_roots_modified: false
  peer_files_modified: false
```

## 10. Write-scope statement

This invocation creates only this one immutable NM13-12 run report. It creates no canonical claim, checker, theorem artifact, paper folder, shared-root edit, peer-track edit, workflow execution, permission change, public post, email/Drive item, paid-compute request, or scheduler change. The report is to be read back at its creation commit without a receipt-only follow-up commit.
