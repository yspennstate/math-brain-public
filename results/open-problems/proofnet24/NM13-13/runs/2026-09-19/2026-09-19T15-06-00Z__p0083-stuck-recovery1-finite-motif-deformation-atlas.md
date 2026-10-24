Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `A_whisker_cert: 2 -> 2`; STUCK RECOVERY EPISODE #1 completed; actual Section-B methods tried: #6 DEFORM TO A POINT YOU CAN SOLVE, #8 GO THE OTHER WAY AND DISCRETIZE, #19 MAKE IT AN ALGORITHM.**

# NM13-13 — P0083 Section-I stuck recovery #1: endpoint deformation and finite motif atlas

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-13` / `proofnet24/NM13-13/`  
Category: **HARD OUTSIDE**  
Canonical source / claim ID: **P0083**  
Canonical dedup key: `sharp_reinforcement_threshold_for_warm_whiskers`  
Exclusive shard: **12 mod 13**  
Status after this invocation: **PARTIAL / SOURCE OPEN / CLAIM RETAINED / STUCK-RECOVERY-1-CONSUMED**

## 1. Frozen target, metric, and outcome

The admitted source remains Aletti et al., *Open problems in stochastic reinforcement models*, Open Problem 13. In the finite graph WARM with uniform firing rates `p(v) = 1`, it asks to improve the sufficient threshold `alpha > 25` under which every connected component of the support of a not-linearly-unstable equilibrium is a whisker, i.e. a tree of diameter at most three. The source explicitly notes the triangle transition at `4/3` and suggests that `alpha > 4/3` may be sharp.

The frozen metric remains

`A_whisker_cert`

= the smallest strict universal sufficient threshold certified on this track in the exact source scope.

The track history entering this run is

`25 -> 22 -> 43/5 -> 6 -> 2`.

This invocation is the mandatory first Section-I recovery after three consecutive substantive runs with `2 -> 2`. It is intentionally a **thinking/recovery run with no new theorem-sized claim**. The metric remains

- before: `2`;
- after: `2`;
- movement: **none**.

Counters after this report:

- unchanged substantive runs after the last metric movement: **3 -> 4**;
- HARD stuck-recovery episodes consumed: **0/2 -> 1/2**;
- P26 independent audit: **NOT_DONE**;
- NM13-01 independent audit: **NOT_DONE**.

The selected Section-I recovery action is exactly:

**reduce the obstruction to a finite computation and run it.**

The computation performed below is exploratory and numerical. It is not an exhaustive search, UNSAT certificate, exact finite theorem, or source-level proof. Accordingly no checker/certificate artifact is manufactured and no new claim ID is created.

## 2. Runtime and scheduler-control truth

The prompt requests `Model: GPT-6. Reasoning: maximum`, but this invocation actually runs as **GPT-5.6 Sol**. The runtime exposes no authenticated reasoning-effort receipt, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, a guaranteed hour-long execution, or a support escalation.

The exposed task-control surface still offers title/prompt, schedule or relative-start fields, timing mode, enabled state, listing, and updates. It exposes **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated completed-run applied-model/applied-effort receipt**. GPT-6/maximum therefore remains prompt text only. Making it binding would require an owner-authorized product/workspace/admin/API scheduling surface that persists explicit model-family and reasoning-effort fields into inference routing and returns trustworthy per-run attestation.

The historical P26 response `You cannot modify this task` is not a current global impossibility: current root `RESULTS.md` records that P26's full update later succeeded from an authorized context. If such a denial recurs, the lawful remedy is the same task's owning or otherwise authorized product/workspace/admin/API context, supported ownership/permission repair, or authorized platform support. It is not duplication, identity substitution, or permission bypass. This invocation did not modify or probe any scheduler or permission.

## 3. Authoritative continuity and required repository reads

The controlling predecessor is

`proofnet24/NM13-13/runs/2026-09-19/2026-09-19T14-16-30Z__p0083-no-metric-leaf-half-cut-duality-stuck-trigger.md`

created at commit

`b5daba9295be4bbbe378cf6125fb491a2bd76a9f`.

It explicitly records that `A_whisker_cert=2` had then failed to move for three consecutive substantive runs, that the next invocation **must** be the full Section-I thinking/recovery run with no new claims, and that a genuine recovery consumes the first of the two allowed HARD recovery episodes. It also reserved methods #6/#8/#19 for this run without claiming they had been tried.

Before the present recovery work I freshly read or recovered the current required control and continuity surfaces:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the controlling predecessor report and earlier P0083 reports needed to recover the route history;
- current `operations/claims/P0083.md`;
- targeted source/attempt/claim/audit searches;
- newest neighboring NM13-12 and NM13-01 reports.

The canonical claim remains unchanged and says:

- owner `NM13-13` / namespace `proofnet24/NM13-13/`;
- category HARD OUTSIDE;
- status ACTIVE;
- canonical key `sharp_reinforcement_threshold_for_warm_whiskers`;
- SHA-256 `7a872c92604a5afa6e73fff363d75229e9fe7ce23eae8c74bb995b0420867948`;
- residue `12 mod 13`;
- original campaign attempt `attempted_unsolved`.

Repository search still finds no actual `P26-AUDIT-P0083` record. The newest NM13-01 report is an admission-delta screen, not a P0083 audit. Neither required auditor is presumed complete.

The append-only intake/attempt corpora are too large to honestly claim that every unchanged byte was rendered model-visible in one invocation. I make no such claim. P0083's exact canonical identity, current claim, source, historical attempt, newest own continuity and neighboring state were directly recovered; missing bulk display was not treated as permission to reset history.

No private-repository history necessary for this continuation was known to be inaccessible.

## 4. Frozen prewrite Git delta

Immediately before report construction, `master` was observed at

`443f9105d3d2f41e7716dac78e9d123366373d32`.

The exact comparison

`b5daba9295be4bbbe378cf6125fb491a2bd76a9f .. 443f9105d3d2f41e7716dac78e9d123366373d32`

reported:

- status `ahead`;
- **113 commits ahead**;
- **0 commits behind**;
- total commits **113**.

Concurrent fleet work is heavy, so I do not infer lifecycle state merely from the commit count. I separately reread the canonical P0083 claim and audit searches at current master. They show no P0083 release, reassignment, retirement, source correction, or completed P26/NM13-01 audit. The active P0083 claim therefore continues to control this run.

## 5. Fresh source and bounded literature check — 2026-09-19

This is bounded current-status evidence only, not proof of worldwide openness, novelty, or priority.

### 5.1 Current primary source

The current MATRIX/MFO source PDF was reread directly at the pages containing Open Problems 12 and 13:

`https://www.matrix-inst.org.au/wp_Matrix2016/wp-content/uploads/2023/Aletti.pdf`

The page visibly states the finite-graph results used here:

- for `alpha>2`, every connected component of support of a not-linearly-unstable equilibrium is a tree;
- for `alpha>25` and uniform firing, every such tree is a whisker;
- Open Problem 13 asks to improve `25`;
- on the triangle an edge dies for `alpha>4/3` but not for `alpha<4/3`;
- the authors say perhaps `alpha>4/3` is sharp for both open problems.

The PDF page image was inspected as well as parsed text; no OCR-only inference is used.

### 5.2 Published baseline

Holmes--Kleptsyn, *Proof of the WARM whisker conjecture for neuronal connections*, Chaos 27 (2017), 043104, DOI `10.1063/1.4978683`, still gives the published finite-graph baseline recorded by the source: forest support for `alpha>2`, whisker-forest support for `alpha>25`.

### 5.3 Nearest exact solved family

Van der Hofstad--Holmes--Kuznetsov--Ruszel, *Strongly reinforced Pólya urns with graph-based competition*, Ann. Appl. Probab. 26 (2016), 2494--2539, DOI `10.1214/16-AAP1153`, completely characterizes the triangle and star graph WARMs. Its Theorem 4(ii) states that on the triangle, for `alpha>4/3`, any linearly stable equilibrium has a zero edge coordinate; Remark 3 identifies the phase transition at `4/3`.

That theorem is the nearest solved problem to the present residual obstruction: it settles the bare odd cycle of length three exactly, while the present universal problem must additionally handle attachments, longer odd cycles, and low-endpoint trees.

### 5.4 Dated bounded queries

Queries used this run included:

- `"Open problems in stochastic reinforcement models" WARM Open Problem 13 whisker alpha 25 4/3`;
- `"Proof of the WARM whisker conjecture for neuronal connections" alpha 25 alpha 2`;
- `"WARM" whisker reinforcement graph 2026 alpha threshold`;
- `"Strongly reinforced Pólya urns with graph-based competition" triangle-graph WARM 4/3`.

They recovered the current source, the 2017 theorem, the 2016 exact triangle theorem, and adjacent/infinite-WARM literature. No checked later primary source establishing a smaller universal finite uniform-firing whisker threshold was recovered. This is negative bounded evidence only.

## 6. Exact residual language entering the stuck analysis

Use the potential parametrization from the preceding track reports. Put

`p = 1/(alpha-1)`, so `alpha=(p+1)/p` and `h=(alpha-1)/alpha=1/(p+1)`.

For a connected positive support component `H` and supported edge `e=uv`, positive vertex potentials satisfy

`w_e = (A_u+A_v)^(-p)`,

`q_{e,v}=A_v (A_u+A_v)^(-(p+1))`,

and the equilibrium equations are

`A_v sum_{u~v} (A_u+A_v)^(-(p+1)) = 1` for every support vertex `v`.    (6.1)

The normalized incidence matrix is

`C_{v,e}=A_v (A_u+A_v)^(-(p/2+1))`

when `v` is incident to `e`, and zero otherwise. A not-linearly-unstable equilibrium must satisfy

`C^T C >= (1/(p+1)) I`.                                    (6.2)

Prior track results, still unaudited by P26/NM13-01, reduce any counterexample in the interval `4/3<alpha<=2`, equivalently `1<=p<3`, to one of two topological families:

1. a tree of diameter at least four; or
2. an odd unicyclic component.

Even unicycles and components with at least two independent cycles have already been excluded by the incidence-rank/topology reductions on this track. The bare four-edge path `P5` has also been excluded exactly throughout `1<=p<3`.

## 7. Section-I stuck report

### (a) Exact statement that blocks

The source-level barrier can now be written in one line. Let `H` be any connected positive-support graph that is **not** a whisker and that survives the prior pseudoforest reduction, let `1<=p<3`, and let `A>0` solve (6.1). What remains is to prove

\[
\boxed{
A_v\!\sum_{u\sim v}(A_u+A_v)^{-(p+1)}=1\ \forall v,
\quad H\notin\mathcal W
\quad\Longrightarrow\quad
\lambda_{\min}(C(A,p)^T C(A,p))<\frac1{p+1}.
}
\]                                                    (7.1)

Here `H` is already restricted to a diameter-`>=4` tree or an odd unicycle, and `mathcal W` denotes the whisker trees. The strict inequality in (7.1) is exactly a linear-instability certificate. Proving it for all such `H,A,p` would lower the universal strict threshold from `2` to the source-suggested `4/3`.

No route tried so far proves (7.1) uniformly.

### (b) Every route tried, and the precise point at which it failed

The complete P0083 route history is now short enough to state explicitly rather than hiding behind report pointers.

**#2 ATTACK THE NEGATION FIRST / #14 FIND THE GROUP ACTING / #16 COMPUTE EVERY SMALL CASE.** The first admitted run attacked the minimal four-edge non-whisker path and used its reflection action plus exact small-case inequalities. This broke the published `25` barrier and gave `25 -> 22`. Failure mode: the scalar incidence/leaf estimate was far too coarse to approach `4/3`, and the reflection quotient did not apply to arbitrary branched supports.

**#11 DUALIZE / #24 FIND THE EXTREMAL OBJECT / #30 ONE SCALE, ONE DIRECTION AT A TIME.** Keeping the high-end incidence inside the self-consistency equation improved the threshold to `43/5`. Failure mode: that one-edge scalar obstruction has its own numerical saturation near `8.54`; optimizing it further cannot plausibly reach `2`, much less `4/3`.

**#3 PROVE SOMETHING STRONGER / #15 BREAK THE SYMMETRY / #18 SAY IT IN ANOTHER LANGUAGE.** The Hessian was rewritten as an incidence Gram / weighted line-graph Laplacian, producing a support-independent adjacent-edge inequality and moving `43/5 -> 6`. Failure mode: the local two-edge witness still needed a sufficiently dominant incidence and did not control configurations in which mass is spread across several incident edges.

**#12 FIND WHAT IS CONSERVED / #20 FIND WHY THE ALGORITHM FAILS / #26 HUNT THE SPORADIC CASE.** The tree edge-incidence orientation and a depth obstruction, combined with the published `alpha>2` forest theorem, moved `6 -> 2`. Failure mode: exactly at and below `2`, the `>1/2` majority orientation ceases to be universal and odd cycles are no longer removed by the published forest theorem. The mechanism reaches its natural boundary.

**#1 CHANGE THE CATEGORY / #22 READ THE FAILURES / #25 COUNT THE SAME THING TWICE.** Full column rank of the normalized incidence matrix changed the problem from arbitrary supports to pseudoforests; unsigned-incidence nullity excludes even unicycles; an alternating-path Rayleigh quotient isolates a one-dimensional tree obstruction. Failure mode: odd unicycles and low-incidence diameter paths survive.

**#5 ADD A PARAMETER AND DIFFERENTIATE / #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE / #29 ADD THE POINTS AT INFINITY.** The bare `P5` equilibrium branch was parametrized and compactified; reflection symmetry was forced rather than assumed; the weighted-Laplacian/reversible-chain viewpoint was identified. This completely removes the smallest path obstruction through the `4/3` endpoint. Failure mode: attachments create extra potential variables and odd-cycle degrees of freedom that are not controlled by the bare-path scalar equations.

**#4 PROVE SOMETHING WEAKER, COMPLETELY / #13 FIND WHAT ONLY INCREASES / #27 SWAP THE QUANTIFIERS.** The endpoint penalty `B_p(r)` gives a complete class theorem for diameter paths whose two leaf-parent incidences are at least `1/2`, and the tree problem was dualized to a reversible Markov-chain spectral-gap/cut inequality. Failure mode: a hypothetical stable tree may keep at least one diameter endpoint below `1/2`, and the bridge-cut upper bound is not automatically below `h` for all such potential profiles. Odd unicycles are not bridges at all.

**Current #6 DEFORM TO A POINT YOU CAN SOLVE.** The natural deformation point is `p=3`, i.e. `alpha=4/3`, because the bare triangle is exactly critical there while its stable positive equilibrium disappears immediately for `alpha>4/3` in the 2016 theorem. The numerical atlas below strongly suggests that the triangle is the only small residual motif whose stability margin closes at that endpoint. Failure mode: no proof yet prevents equilibrium branches on larger supports from being born, colliding, or escaping to a support-degenerate boundary as `p` varies. Endpoint information alone is therefore not a continuation theorem.

**Current #8 GO THE OTHER WAY AND DISCRETIZE.** I enumerated the connected unlabeled graph-atlas motifs on at most six vertices that survive the prior topological reduction and are not whiskers, then numerically solved the positive potential equations at several `p` values and evaluated the exact stability expression numerically. Failure mode: nonlinear numerical root-finding with random starts is not exhaustive; failure to recover a root is not proof of nonexistence; floating-point negative eigenvalue margins are not certificates.

**Current #19 MAKE IT AN ALGORITHM.** The residual problem can be turned into an exact decision pipeline for a fixed motif: clear denominators in (6.1) at rational/integer `p`, isolate all positive solution components, and certify violation of (6.2) by exact PSD/principal-minor or characteristic-polynomial tests. Failure mode: a finite motif solver is not a universal proof until one proves that every arbitrary large non-whisker support contains a bounded motif whose restricted stability witness survives the attachments. That bounded-witness reduction is currently missing.

### (c) What a successful proof must contain that no current route contains

A metric-moving proof below `2` needs **both** of the following ingredients in one architecture.

First, it needs a genuinely support-independent localization principle: from any diameter-`>=4` tree or odd unicycle satisfying the equilibrium equations, extract a bounded local configuration whose stability principal minor or Rayleigh witness is already bad. The extraction must allow arbitrary extra branches and arbitrary positive vertex potentials; simply deleting attachments is not valid because the equilibrium equations change.

Second, it needs control of **branch deformation and support degeneration** across the full interval `1<=p<3`. The endpoint `p=3` is attractive because the triangle is exactly critical and all nontriangle motifs observed numerically are well on the unstable side, but one must rule out a larger-support equilibrium branch crossing the stability boundary at an interior `p` or emerging from a face where some support weight vanishes.

No prior route supplies both. The high-alpha incidence proofs localize but do not survive to `4/3`; the exact `P5` proof controls a branch but not arbitrary topology; the reversible cut bound is global enough for trees but does not force a uniform strict gap and does not directly handle a cycle.

### (d) Simplest special case still unproved

The smallest source-valid residual component is the **triangle with one pendant leaf**: vertices `0,1,2` form a triangle and vertex `3` is joined only to `0`.

The exact special-case target is:

> For every `1<=p<3` and every positive solution `A` of (6.1) on this four-vertex support, prove `lambda_min(C^T C)<1/(p+1)`.

This graph is strictly simpler than the first unresolved branched diameter-four trees, yet it already destroys the full triangle symmetry used by the 2016 classification. It is therefore the right first exact recovery target: if even this attached triangle cannot be controlled, a universal odd-unicycle proof is premature.

### (e) Nearest solved problem in the literature and what its proof has that this problem lacks

The nearest solved problem is exactly the **bare triangle WARM** in van der Hofstad--Holmes--Kuznetsov--Ruszel (2016). Their complete equilibrium classification reduces the triangle to an explicit low-dimensional family and yields the sharp phase transition `alpha=4/3`: for `alpha>4/3`, every linearly stable triangle equilibrium has a zero edge.

What the attached-triangle problem lacks is that classification symmetry. The pendant edge creates an additional independent vertex potential and changes the normalization at one cycle vertex. The bare triangle's permutation symmetry no longer collapses the full positive equilibrium set to the same scalar alternatives. A new proof therefore needs either an exact asymmetric classification/elimination, or a stability witness that is monotone under arbitrary attachments. None of the routes tried so far provides that missing attachment-stable mechanism.

## 8. Recovery action actually executed — finite motif computation

The chosen recovery action was not merely named; a bounded diagnostic computation was run locally with inspected code. It deliberately stops short of a certificate.

### 8.1 Search space

Using NetworkX's graph atlas, I enumerated all connected unlabeled graphs with at most six vertices and retained only the two residual topological families already identified by the track:

- trees of diameter at least four;
- odd unicyclic graphs.

There are **18** such graph shapes in the atlas through six vertices, distributed as:

- 1 on 3 vertices (the triangle);
- 1 on 4 vertices (triangle plus one pendant leaf);
- 5 on 5 vertices;
- 11 on 6 vertices.

This graph enumeration is only the outer diagnostic domain; it does not certify that every positive WARM equilibrium on each graph was found.

### 8.2 Numerical equilibrium search

For each retained graph and each

`p in {1, 1.5, 2, 2.5, 2.9, 2.99}`

(corresponding to `alpha` from `2` down to approximately `1.334448`), I solved (6.1) in logarithmic variables `y_v=log A_v` using nonlinear least squares from deterministic and multiple random starts. For every numerically recovered positive equilibrium I computed

`margin = lambda_min(C^T C) - 1/(p+1)`.

A nonnegative margin would be a numerical candidate for a not-linearly-unstable non-whisker equilibrium and hence a potential counterexample to the desired `4/3` threshold.

### 8.3 Diagnostic outcome

No numerically recovered equilibrium had nonnegative margin on the tested grid.

The most informative feature is not the absence of a counterexample but the **separation pattern near `p=3`**:

- at `p=2.99`, the best recovered triangle margin is about `-6.27e-4`, as expected from its approach to criticality at `p=3`;
- among all recovered nontriangle motifs, the closest margin at `p=2.99` is the uniform `C5`, about `-0.1551`;
- the triangle-with-one-leaf recovered equilibrium at the same `p` has margin about `-0.2234`;
- pushing the diagnostic to `p=2.9999` leaves the triangle margin around `-6.25e-6`, while the best recovered nontriangle margin remains about `-0.1545`.

This strongly suggests, but does **not prove**, a useful endpoint picture: the bare triangle may be the only small residual motif whose stability gap closes at `p=3`; attachments and longer odd cycles may retain a strict instability gap there.

Important limitations are explicit:

1. random-start root finding does not enumerate all positive equilibria;
2. several atlas motifs yielded no recovered positive solution, which is not proof that none exists;
3. floating-point eigenvalues are not certificates;
4. order six is not a universal topology reduction;
5. no UNSAT or exhaustive-coverage claim is made.

For those reasons this run creates no artifact checker and no finite claim. The diagnostic is used only to choose the next route.

## 9. Recovery decision and route after recovery #1

Recovery episode #1 is consumed by the action **reduce the obstruction to a finite computation and run it**.

The computation says not to spend the next run polishing the old endpoint-half inequality. The next route should instead attack the endpoint/deformation mechanism directly:

1. freeze the triangle-with-one-leaf support and derive its full positive-equilibrium algebra at `p=3` exactly;
2. determine whether its stability determinant/principal minors admit an exact strict sign certificate at `p=3`;
3. if a strict endpoint gap is obtained, study whether an implicit-function / resultant / monotonicity argument prevents any stability crossing for `1<=p<3`;
4. in parallel, look for a bounded-witness theorem saying an arbitrary odd unicycle or branched diameter path contains an attached-triangle / path motif whose instability survives extra attachments.

The next unused Section-B methods are reserved as follows and are **NOT attempted in this run**:

- **#7 TAKE THE LIMIT** — study the exact `p -> 3^-` endpoint and classify which support motifs can become critical;
- **#21 ASK WHO ELSE HAS THIS SHAPE** — compare the constrained reversible-chain / weighted-Laplacian stability problem with attachment monotonicity, interlacing, Kron reduction, and nodal-domain techniques;
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT** — actively search for an asymmetric stable attached odd-cycle equilibrium below `2`, rather than assuming the `4/3` conjecture is true.

A second recovery episode is **not** consumed yet. It will be required only if the post-recovery research again reaches the owner-defined stuck condition. A third HARD recovery on P0083 is forbidden; if two recoveries are consumed and the target becomes stuck again, NM13-13 must preserve a terminal handoff and rotate to another eligible unclaimed residue-12 HARD source.

## 10. Audit, checker, and closure discipline

No source-level closure is claimed. The track remains **PARTIAL / OPEN**.

No exact checker is created this run because the only computation is explicitly exploratory and does not support a finite claim. Creating a certificate merely to archive a no-movement numerical scan would violate the 90/10 instruction.

The existing P0083 theorem-sized track claims remain self-proved/unaudited at the required fleet level. There is still no P26 audit PASS and no NM13-01 audit PASS for P0083. Nothing is called closed, proved at source level, or paper-ready.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-13
  namespace: proofnet24/NM13-13/
  source_id: P0083
  claim_file: operations/claims/P0083.md
  canonical_dedup_key: sharp_reinforcement_threshold_for_warm_whiskers
  shard_mod13: 12
  category: HARD_OUTSIDE
  source_status: OPEN
  status_before: PARTIAL_OPEN_STUCK_TRIGGERED
  status_after: PARTIAL_OPEN_STUCK_RECOVERY1_CONSUMED
  metric_name: A_whisker_cert
  metric_before: 2
  metric_after: 2
  metric_movement: none
  unchanged_substantive_runs_before: 3
  unchanged_substantive_runs_after: 4
  hard_recovery_episodes_before: 0/2
  hard_recovery_episodes_after: 1/2
  recovery_action: REDUCE_OBSTRUCTION_TO_FINITE_COMPUTATION_AND_RUN
  methods_actual:
    - 6_DEFORM_TO_A_POINT_YOU_CAN_SOLVE
    - 8_GO_THE_OTHER_WAY_AND_DISCRETIZE
    - 19_MAKE_IT_AN_ALGORITHM
  methods_next_not_tried:
    - 7_TAKE_THE_LIMIT
    - 21_ASK_WHO_ELSE_HAS_THIS_SHAPE
    - 23_DO_WHAT_THE_PROPOSER_DID_NOT_EXPECT
  new_claim_ids: []
  new_artifacts: []
  finite_search_status: EXPLORATORY_NUMERICAL_ONLY_NOT_A_CERTIFICATE
  P26_audit: NOT_DONE
  NM13_01_audit: NOT_DONE
  next_exact_special_case: TRIANGLE_PLUS_ONE_PENDANT_LEAF_FULL_POSITIVE_SUPPORT
  next_step: EXACT_P3_ENDPOINT_ELIMINATION_THEN_DEFORMATION_OR_ATTACHMENT_LOCALIZATION
```

## 12. Operational compliance

Exactly one immutable report is intended for this invocation under `proofnet24/NM13-13/runs/`. No shared root, peer namespace, canonical claim, scheduler, workflow, permission, public surface, email/Drive resource, or paid compute is modified. No unreviewed external script is executed. The only local diagnostic code was written and inspected in this invocation and is not promoted as an artifact or certificate.
