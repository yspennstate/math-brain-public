Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO FIXED I0056 MOVEMENT / NO SUCCESSOR ADMISSION: frozen `H_{5,5}` interval width `0 -> 0`; completed auxiliary `ROMERO-2025-SPLIT8` remains `PROVED / AUDIT-COMPLETE / PACKAGED`; successor-admission metric `E_ready: 0 -> 0`; methods #11 DUALIZE, #12 FIND WHAT IS CONSERVED, #19 MAKE IT AN ALGORITHM.**

# R06 CLOSABLE OUTSIDE — hard-release delta gives no lawful CLOSABLE successor

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R06.  
Lane: CLOSABLE OUTSIDE.  
Date checked: 2026-09-19 UTC.

## 1. Continuity: I0056 stays frozen and the full source stays PARTIAL

I continued from the newest immutable R06 report

`runs/R06/20260919T2126Z_successor_gate_e0011_consumed_no_free_ready_73_d9f2.md`

created at commit

`fb98991a17a0ecb5ff1fd354a4b6a00c8212333e`.

I did not restart I0056 or the completed Romero layer. The canonical I0056 claim remains `operations/claims/I0056.md`, which fixes:

- source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake `I0056`;
- graph class: regular, co-regular plane graphs, with the source's second clause retaining more general transitive plane graphs;
- frozen regime: `H_{5,5}` / Schlaefli `{5,5}`;
- degree / face-degree pair: `(d,d^dagger)=(5,5)`;
- normalization:
  \[
  \Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ K\text{ finite}}
  \frac{|\partial_VK|}{|K|},
  \qquad
  \partial_VK=\{x\notin K:\exists y\in K,\ x\sim y\};
  \]
- certified exact value and fixed metric:
  \[
  \boxed{\Phi_V(H_{5,5})=\sqrt5},\qquad
  [L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
  \]

The current maintained Lyons--Peres edition still asks Question 6.20 in the full form: determine `Phi_V(G)` for regular, co-regular plane graphs, and `Phi_E(G), Phi_V(G)` for more general transitive plane graphs. It still annotates the Haslegrave--Panagiotis result only for face/codegrees 3 and 4. Therefore the solved `{5,5}` subclass remains **PARTIAL for the full source question**.

Haslegrave--Panagiotis, *Site percolation and isoperimetric inequalities for plane graphs*, DOI `10.1002/rsa.20946`, remains excluded prior art: it gives the exact vertex constants for the triangular and square hyperbolic lattices, i.e. the source's codegree 3 and 4 cases. Those results are not relabelled as new.

The auxiliary complete `n=8` Romero split-reliability layer remains `PROVED / AUDIT-COMPLETE / PACKAGED` with the independent P26 and R01 full audits and `paper_romero_split8_n8_layer/`. No defect or scope correction in the present delta justifies reopening it.

## 2. Required repository refresh

Before the successor decision I freshly recovered/read:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- canonical ownership `operations/claims/I0056.md`;
- the newest own R06 report above;
- current task-health reconciliation `operations/task_health/runs/2026-09-19T215600Z/status.md`;
- current neighboring CLOSABLE successor-gate evidence, including R08 and R19;
- the current canonical claim records material to the exact predecessor-to-head delta;
- the intake/queue identity for I0056 and the current reserve policy.

The large append-only intake corpora are too large to claim that every historical row was rendered model-visible byte-for-byte in one bounded connector response. I therefore use exact-ID recovery plus the complete Git delta for lifecycle discovery, rather than treating connector truncation as absence evidence.

`POSTED.md` now bibliographically records the already-written *Outer Vertex-Isoperimetry of Regular Plane Tessellations* on ResearchGate. That is an exclusion/publication fact, not a new audit or a new source-level closure, and it is another reason not to restart the frozen I0056 paper route.

## 3. Fresh source / literature boundary check

Dated public-source checks on 2026-09-19 UTC included the exact Lyons--Peres Question 6.20 wording, the Haslegrave--Panagiotis DOI/title, exact `{5,5}` / `H_{5,5}` vertex-isoperimetric searches, `codegree 5` plane-graph vertex-isoperimetric searches, later Panagiotis hyperbolic-graph work, and citing/related hyperbolic isoperimetry searches.

The recovered primary-source boundary is unchanged:

1. the maintained Lyons--Peres source still retains Question 6.20 and records only the codegree-3/4 vertex cases as solved by Haslegrave--Panagiotis;
2. Haslegrave--Panagiotis explicitly prove the triangular and square hyperbolic cases, which remain excluded;
3. later sharp plane-tessellation work recovered in this search concerns edge boundary in the relevant displayed theorem, not the frozen outer-vertex normalization;
4. no later primary source was recovered that independently announces the exact `{5,5}` outer-vertex value `sqrt(5)` or closes the full Question 6.20.

This is **bounded negative evidence only**, not a worldwide novelty, priority, or bibliographic-completeness certificate.

## 4. Exact predecessor-to-prewrite repository delta

Frozen pre-write head:

`aaf4a417b45db59166e995d1f4e4cb091e2e2823`.

Exact comparison

`fb98991a17a0ecb5ff1fd354a4b6a00c8212333e .. aaf4a417b45db59166e995d1f4e4cb091e2e2823`

returns:

- status: `ahead`;
- commits ahead: **172**;
- commits behind: **0**;
- total commits: **172**;
- `too_large = null`, so the returned changed-file set is complete.

No root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md` / `RANKING.md`, or screened intake `problems.jsonl` mutation appears in this exact changed-file set. The admission-relevant canonical claim mutations are eight records:

| Canonical claim | Current lifecycle fact | R06 disposition |
|---|---|---|
| `AK-KATZIN-C41-EQUALITY` | literal equality clause resolved/refuted as printed | `EXCLUDE_RESOLVED_NOT_CURRENT_OPEN` |
| `B-WEAK-EVEN-LOGCONCAVE` | source open but released only after both HARD recoveries; all-dimensional theorem-scale obligation remains | `RELEASED_HARD_NOT_CLOSABLE` |
| `BHS-MST-CM-UNIV` | owner now `UNASSIGNED AFTER HARD7-04 HANDOFF`; source open/partial; surviving MST universality theorem remains HARD | `RELEASED_HARD_NOT_CLOSABLE` |
| `G0004` | owner now `UNASSIGNED AFTER R17 HANDOFF`; source open/partial; unrestricted finite-graph percolation theorem remains HARD | `RELEASED_HARD_NOT_CLOSABLE` |
| `H0021` | active other owner, HARD | `EXCLUDE_ACTIVE_OTHER_OWNER` |
| `LOG-BRUNN-MINKOWSKI-SYMMETRIC` | newly claimed by a HARD track | `EXCLUDE_ACTIVE_OTHER_OWNER` |
| `MAXIMAL-INTERSECTION-ELLIPSOID-UNIQUENESS` | released after two HARD recoveries; surviving all-dimensional uniqueness statement remains theorem-scale HARD | `RELEASED_HARD_NOT_CLOSABLE` |
| `P0151` | newly claimed fixed-outdegree preferential-attachment critical-window target, explicitly HARD OUTSIDE | `EXCLUDE_ACTIVE_OTHER_OWNER_HARD` |

Two of the strongest apparent releases were directly re-read at the current head:

- `operations/claims/BHS-MST-CM-UNIV.md` explicitly says `UNASSIGNED AFTER HARD7-04 HANDOFF`, `SOURCE OPEN / PARTIAL / RELEASED`, while preserving an unsolved heavy-tailed configuration-model MST scaling-limit universality theorem after both hard recoveries;
- `operations/claims/G0004.md` explicitly says `UNASSIGNED AFTER R17 HANDOFF`, `SOURCE OPEN / PARTIAL / RELEASED BY R17`, while preserving the unrestricted Flammant finite-graph percolation conjecture and the exhausted HARD architecture.

`operations/claims/B-WEAK-EVEN-LOGCONCAVE.md` likewise records an open all-dimensional conjecture released after HARD exhaustion, with the verified full-dimensional metric still only `D_B=2`.

Thus the release events are real, but **release is not the same as CLOSABLE admission**.

The current coordinator independently records strict newly certified free READY CLOSABLE additions as **0**. The newest R19 terminal screen classifies the same eight claim mutations and independently finds no source-exact, current-open, nonposted, genuinely CLOSABLE, owner-clear, retirement-route-clear, freshly READY successor. R08's current gate likewise remains at zero after E0011's release was consumed by another owner.

Therefore

\[
\boxed{E_{\mathrm{ready}}=0\longrightarrow0.}
\]

No successor claim is created.

## 5. Three Section-B moves actually tried

The immediately preceding R06 triple was `#6/#8/#21`; I do not repeat it.

### #11 DUALIZE

Instead of asking positively which queue item looks attractive, I dualized the admission problem into a **blocker certificate**. A changed canonical claim is eligible only if it simultaneously satisfies

\[
\text{current-open}\wedge\text{outside}\wedge\text{full-source}\wedge
\text{CLOSABLE}\wedge\text{READY}\wedge\text{owner-clear}\wedge
\text{lifecycle-fresh}.
\]

On the complete 172-commit delta, each of the eight changed claim records has an explicit dual blocker: resolved, HARD, or actively owned. The complement of those blockers is empty.

**Outcome #11:** the dual admission certificate proves there is no lawful successor in the material canonical delta; no mathematical source claim is made by this operational classification.

### #12 FIND WHAT IS CONSERVED

I looked for lifecycle invariants that survive fleet churn. Three are decisive here:

1. a resolved source remains excluded even if its claim is released;
2. a HARD source does not become CLOSABLE merely because the previous HARD owner hands it off;
3. an active exclusive claim remains unavailable to R06 until an explicit release/handoff changes ownership.

These invariants explain why high commit volume and several genuine releases do not change `E_ready`. The hard-release records preserve their theorem-scale obligations; the newly claimed records preserve other ownership; the one compact resolved equality clause preserves its exclusion.

**Outcome #12:** the conserved source/lane/ownership facts keep every changed claim outside the R06 admissible set.

### #19 MAKE IT AN ALGORITHM

I turned the successor screen into an explicit deterministic decision procedure over the complete canonical delta:

1. enumerate changed `operations/claims/*.md` records;
2. reject `RESOLVED/KNOWN/POSTED` source scopes;
3. reject active other owners;
4. reject sources whose surviving literal obligation is still HARD/theorem-scale;
5. reject PENDING rows lacking a canonical READY transition;
6. only then admit a create-only owner-clear CLOSABLE source and freeze its metric before research.

Running this procedure conceptually on all eight mutations returns the empty set. This is more useful than another broad queue scan because it makes the precise failure stage visible for every lifecycle event.

**Outcome #19:** algorithmic admission returns zero candidates. No code/checker is warranted because the inputs are repository/source classifications rather than a new finite mathematical assertion.

## 6. Why no checker was created

This run asserts no new theorem, counterexample, finite enumeration, numerical bound, or mathematical constant. The exact Git comparison and direct claim reads are the evidence for the lifecycle conclusion. Creating an `artifacts/R06/` checker merely to recertify `E_ready=0` would invert the required 90/10 research-to-bookkeeping allocation and would not move any mathematical quantity.

## 7. Scheduler/model-control truth

The installed prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**.

The exposed scheduler/task-control surface provides task identity/title, prompt, schedule/timing mode, enabled state, and run timestamps. It exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/applied-effort receipt, and no guaranteed hour-long execution field**. Therefore `GPT-6 / maximum` remains prompt-only on this surface.

Making it binding requires an owner-authorized product/workspace/admin/API scheduling surface that persists explicit model and reasoning fields into inference routing and returns trustworthy per-run runtime attestation.

The historical P26 attempt that returned `You cannot modify this task` remains an authorization/context boundary. Later repository records show successful updates from a different authorized context. The compliant workaround for any still-denied task is the owning/authorized context, a supported permission repair/transfer, or platform support — not a bypass or duplicate replacement task.

No scheduler or permission mutation was attempted in this invocation.

## 8. Disposition

R06 remains rotated from I0056 and from the completed Romero package. It has no lawful successor assignment at the frozen head.

The exact missing prerequisite is:

> one canonical source-current, current-open, nonposted, full-source **CLOSABLE**, freshly **READY**, owner-clear outside target whose prior attempts and lifecycle do not require restarting an exhausted route.

Until such a material event appears, R06 must not relabel released HARD work as CLOSABLE, take a peer-owned claim, restart frozen I0056, or manufacture a narrower owner-defined source problem merely to produce activity.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  actual_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  requested_model: GPT-6
  requested_reasoning: maximum
  lane: CLOSABLE_OUTSIDE
  report_kind: post_closure_successor_gate

  source:
    authors: "Russell Lyons and Yuval Peres"
    work: "Probability on Trees and Networks"
    locator: "Question 6.20"
    intake: I0056

  frozen_target:
    graph_class: "regular co-regular plane tessellation"
    graph: "H_{5,5} / {5,5}"
    degree: 5
    face_degree: 5
    normalization: "outer vertex boundary |partial_V K|/|K|"

  fixed_metric:
    name: "certified interval width U-L for Phi_V(H_{5,5})"
    before: 0
    after: 0
    interval: "[sqrt(5), sqrt(5)]"
    value: "sqrt(5)"
    movement: NO_MOVEMENT

  source_status:
    frozen_subclass: PROVED
    full_question: PARTIAL
    excluded_prior_art: "Haslegrave-Panagiotis DOI 10.1002/rsa.20946, face/codegrees 3 and 4"

  auxiliary_romero:
    scope: "n=8, m=14..26"
    state: PROVED_AUDIT_COMPLETE_PACKAGED
    audits:
      - P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64
      - R01-AUDIT-R06-ROMERO-SPLIT8-N8-01
    reopened: false

  predecessor_report: "runs/R06/20260919T2126Z_successor_gate_e0011_consumed_no_free_ready_73_d9f2.md"
  predecessor_creation_commit: fb98991a17a0ecb5ff1fd354a4b6a00c8212333e
  prewrite_head: aaf4a417b45db59166e995d1f4e4cb091e2e2823

  git_delta:
    status: ahead
    commits_ahead: 172
    commits_behind: 0
    total_commits: 172
    too_large: null
    canonical_claim_mutations: 8
    queue_mutation: false
    results_mutation: false
    posted_mutation: false
    campaign_index_mutation: false
    campaign_ranking_mutation: false
    screened_intake_problem_jsonl_mutation: false

  changed_claim_blockers:
    AK_KATZIN_C41_EQUALITY: RESOLVED_NOT_CURRENT_OPEN
    B_WEAK_EVEN_LOGCONCAVE: RELEASED_HARD_NOT_CLOSABLE
    BHS_MST_CM_UNIV: RELEASED_HARD_NOT_CLOSABLE
    G0004: RELEASED_HARD_NOT_CLOSABLE
    H0021: HARD_ACTIVE_OTHER_OWNER
    LOG_BRUNN_MINKOWSKI_SYMMETRIC: HARD_ACTIVE_OTHER_OWNER
    MAXIMAL_INTERSECTION_ELLIPSOID_UNIQUENESS: RELEASED_HARD_NOT_CLOSABLE
    P0151: HARD_ACTIVE_OTHER_OWNER

  successor:
    metric: E_ready
    before: 0
    after: 0
    unit: "free source-current owner-clear READY CLOSABLE targets"
    state: SUCCESSOR_ADMISSION_REQUIRED
    canonical_id: NONE
    claim_created: false

  tried_moves:
    - B11_DUALIZE
    - B12_FIND_WHAT_IS_CONSERVED
    - B19_MAKE_IT_AN_ALGORITHM
  preceding_triple_not_repeated:
    - B6_DEFORM_TO_A_POINT_YOU_CAN_SOLVE
    - B8_DISCRETIZE
    - B21_ASK_WHO_ELSE_HAS_THIS_SHAPE

  remaining_obligation: "A genuinely free, source-current, full-source READY CLOSABLE outside target must arise through a lawful canonical lifecycle/admission event."

  evidence:
    - operations/claims/I0056.md
    - operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md
    - operations/task_health/runs/2026-09-19T215600Z/status.md
    - runs/R08/20260919T2134Z_rotation_hold_e0011_consumed_no_ready_6f1a2c.md
    - runs/R19/2026-09-19_22-43-00_UTC__terminal-wait-eight-claim-delta-hard-releases-no-free-ready_b2p24q27.md
    - operations/claims/BHS-MST-CM-UNIV.md
    - operations/claims/G0004.md
    - operations/claims/B-WEAK-EVEN-LOGCONCAVE.md
    - probability_campaign_2026_09/INDEX.md
    - probability_campaign_2026_09/RANKING.md
    - POSTED.md
    - RESULTS.md
    - QUEUE.md
```

## 10. Action audit

No email/Gmail, Drive, public posting, purchase, paid compute, credential use, permission change, scheduler change, shared-root edit, peer-file edit, canonical-claim overwrite, force-push, or duplicate task was performed. The only repository mutation in this invocation is this immutable R06 report.
