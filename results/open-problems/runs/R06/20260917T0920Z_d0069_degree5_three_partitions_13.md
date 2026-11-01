Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `C5: 0/5 -> 3/5` rigorously covered nonsimple degree-5 parallel-class types; methods #2 ATTACK THE NEGATION, #18 SAY IT IN ANOTHER LANGUAGE, #26 HUNT THE SPORADIC CASE.**

# R06 CLOSABLE OUTSIDE — D0069 degree-5 multigraph connective bound

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler mutation.

## 1. Continuity before dispatch

I did not reopen the stale prompt target I0056. The authoritative I0056 handoff is `runs/R06/20260916T2020Z_i0056_rotation_i0079.md`: after six unchanged runs its frozen `H_{5,5}` interval width was already zero, so the controlling CLOSABLE rule required rotation. The exact Lyons--Peres source question remains:

> **Question 6.20.** What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The preserved R06 regular/co-regular candidate was

`Phi_V(H_{d,f})=(d-2)*sqrt(1-4/((d-2)(f-2)))` for the `f>=5` branch reached through the edge-to-vertex closure theorem, with the frozen `H_{5,5}` value `sqrt(5)`. That remains a **PARTIAL** answer to the full Question 6.20; Haslegrave--Panagiotis triangular/quadrangular cases are KNOWN and are not relabelled as new. I0056 stays retired from this hourly slot.

I0079 likewise reached its six-unchanged rotation threshold and remains preserved. P0189 was then admitted but, on the following prior-art pass, the literal Brown-measure-convergence principle was found to be already refuted in the literature; that target was retired as KNOWN in the relevant scope. Thus the state entering this run was again `SUCCESSOR_ADMISSION_REQUIRED`.

Before claiming a successor I refreshed the current campaign index/ranking, root `POSTED.md`, `RESULTS.md`, current `QUEUE.md`, newest R06 history, latest neighbor R07 report, current task-health admission screen, relevant intake rows and canonical ownership searches. The newest coordinator screen had recently assigned D0044, D0038, D0047 and H0011 elsewhere and explicitly left one honest CLOSABLE successor-admission gate rather than filling it with a broad target.

The large intake JSONL files are connector-truncated when rendered wholesale. This run therefore used exact-ID/source searches and direct reads for the relevant candidate and neighboring rows; it does not claim a byte-for-byte manual rendering of every intake ledger.

## 2. Successor admission — D0069

I recovered a source-exact unowned CLOSABLE candidate in intake D:

- **D0069**;
- Geoffrey R. Grimmett and Zhongyang Li, the question recorded in the 2017 survey *Self-avoiding walks and connective constants*, Question 2.2, Section 2.2;
- underlying original theorem/question: Grimmett--Li, *Bounds on connective constants of regular graphs*, Theorem 4.1(b).

The source setup is an infinite, connected, loopless, vertex-transitive `Delta`-regular **multigraph**. Self-avoiding walks are vertex-self-avoiding walks in the multigraph, so different parallel copies of an edge count as distinct choices. The source proves

`mu(G) >= sqrt(Delta-1)`

when `G` is simple, and when `G` is nonsimple with `Delta<=4`, and asks whether the nonsimple conclusion extends to larger degree. The bridge graph `B_Delta` has equality `mu(B_Delta)=sqrt(Delta-1)`, so the constant is sharp if the extension is true.

A create-only canonical ownership file was successfully created at

`operations/claims/D0069.md`

(commit `89f4ca50bb58a0819f8c2b547432f516a169fedc`). No prior canonical D0069 owner was found in the bounded current repository search. The claim does not promote D0069 to READY or closed.

### Frozen source-valid first regime

The first unresolved degree is

`Delta=5`,

so the target is

`mu(G) >= 2`.

At any vertex, list the multiplicities of the distinct neighbors. Vertex transitivity makes the resulting integer partition of 5 independent of the vertex. Excluding the simple type `[1,1,1,1,1]`, which is already source-known, the five nonsimple types are

`[4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1]`.

The frozen metric is

`C5 = number of these five types for which mu(G)>=2 is proved for every graph of that type`,

with the covered set retained. Baseline: `0/5`. Even `C5=5/5` would remain **PARTIAL** for the full source question because degrees `Delta>=6` would still remain.

## 3. Current-source and later-literature screen

The 2026-09-17 bounded search checked the original theorem/question, the 2017 survey, later Grimmett--Li weighted-SAW work and current search variants for nonsimple degree `>=5`, degree 5, parallel-edge multiplicity types and the bridge graph. I found no source-matching published theorem resolving the nonsimple `Delta>=5` question, and no publication matching the partition-class arguments below. Current secondary summaries still describe the larger-degree nonsimple extension as open.

This is negative bounded search evidence only. **Novelty is UNVERIFIED.** The known simple-graph theorem, the nonsimple `Delta<=4` theorem and `B_Delta` equality example are all prior art and are not claimed as R06 results.

## 4. Idea before code — method #18: weighted simple graph language

Replace every parallel class between distinct vertices `x,y` by one underlying simple edge carrying integer weight

`w(xy)=number of parallel copies of xy`.

A vertex-self-avoiding path `v_0,...,v_n` in the underlying simple graph contributes exactly

`prod_{i=0}^{n-1} w(v_i v_{i+1})`

multigraph SAWs, because each step independently chooses one of the parallel copies. Thus the multigraph connective constant is exactly the exponential growth rate of this weighted SAW count.

At the frozen target `mu>=2`, the natural critical generating-function point is `z=1/2`: it is enough to construct infinitely many disjoint families of self-avoiding paths whose total weighted contribution to

`sum_n sigma_n z^n`

at `z=1/2` has a positive lower bound. This language exposed a block identity not visible in the raw multigraph description.

## 5. Theorem R06-D0069-T1 — three of the five degree-5 types

**Theorem.** Let `G` be an infinite, connected, loopless, vertex-transitive 5-regular multigraph. If its parallel-class partition is one of

`[4,1], [3,2], [2,2,1]`,

then

`mu(G)>=2`.

For `[4,1]` equality is attained by the degree-5 bridge graph.

This is a theorem on the page below; full D0069 remains PARTIAL.

### 5.1 Types `[4,1]` and `[3,2]`

For either type the underlying simple graph has degree 2. An infinite connected vertex-transitive degree-2 simple graph is the bi-infinite path. Label its vertices by the integers and write `m_i` for the multiplicity of the edge `{i,i+1}`.

Five-regularity gives at every vertex

`m_{i-1}+m_i=5`.

Hence the multiplicities alternate between some `a` and `5-a`, where `a` is one of `1,2,3,4`.

A self-avoiding walk on the underlying line chooses left or right on its first step and thereafter is forced to continue in the same direction. Therefore for even length `2k`, independently of the starting parity,

`sigma_{2k}=2 [a(5-a)]^k`.

Taking `2k`-th roots,

`mu(G)=sqrt(a(5-a))`.

For `a=1,2,3,4`,

`a(5-a)=4,6,6,4`,

so `mu(G)>=2`. The `a=1` or `4` case is type `[4,1]` and gives equality `mu=2`; `a=2` or `3` is type `[3,2]` and gives `mu=sqrt(6)>2`.

That proves the first two partition types exactly.

### 5.2 Type `[2,2,1]`: invariant 2-factor plus matching

Now assume every vertex has two distinct neighbors joined to it by double edges and one distinct neighbor joined by a single edge.

Let `H` be the spanning simple subgraph consisting of the two double-edge neighbor classes. Every vertex has degree 2 in `H`, so every component of `H` is a cycle or a double ray. The single edges form a perfect matching `M` on the vertices of `G`.

Because edge multiplicity is preserved by every automorphism and `G` is vertex-transitive, all components of `H` are of the same type. If they are finite, they all have the same length `L>=3`.

#### Case A: `H` has double-ray components

Choose one direction on a double ray. At every step there are exactly two parallel edge copies to choose from, while the vertex sequence never repeats. Hence for every `n` there are at least `2^n` length-`n` SAWs from a fixed start along that ray. Therefore

`mu(G)>=2`.

#### Case B: `H` has finite cycle components

First, a matching edge cannot join two vertices of the same `H`-cycle. Indeed, the property

`the M-partner of v lies in the same H-component as v`

is invariant under `Aut(G)`. If it held for one vertex, it would hold for every vertex by transitivity. Then every finite `H`-cycle would contain both all double edges at its vertices and all matching edges at its vertices, so it would be a finite connected component of `G`, contradicting that `G` is infinite and connected.

Thus every `M`-edge joins two distinct `H`-cycles. Contract each `H`-cycle to one vertex. The resulting quotient is infinite, connected and locally finite, so it contains a one-way infinite simple ray of distinct contracted cycles

`C_0,C_1,C_2,...`.

For every `i>=1`, let `a_i` be the endpoint in `C_i` of the matching edge arriving from `C_{i-1}`, and `b_i` the endpoint in `C_i` of the matching edge leaving to `C_{i+1}`. Since `M` is a matching, `a_i != b_i`.

Inside the simple cycle `C_i`, there are exactly two simple arcs from `a_i` to `b_i`, of lengths

`r_i` and `L-r_i`, with `1<=r_i<=L-1`.

Every edge on either arc is a double edge in `G`; the departure from `C_i` to `C_{i+1}` is a single matching edge. Therefore the weighted generating polynomial of the two allowed block choices through `C_i` is

`P_i(z)=2^{r_i} z^{r_i+1}+2^{L-r_i} z^{L-r_i+1}`.

At the critical point `z=1/2`, the dependence on the geometry cancels exactly:

`P_i(1/2)=1/2+1/2=1`.

Start at the endpoint in `C_0` of the first matching edge to `C_1` and traverse that first matching edge. For any `k>=1`, then independently choose one of the two arcs in each of `C_1,...,C_k` and finally take the outgoing matching edge. Because the quotient cycles are distinct, every resulting vertex path is self-avoiding in `G`; choices of parallel copies on a double arc give the stated weights.

The total contribution at `z=1/2` from all lifted paths traversing exactly `k` interior quotient blocks is

`(1/2) prod_{i=1}^k P_i(1/2)=1/2`.

Families for different `k` are disjoint because their terminal vertices lie in different quotient cycles. Hence

`sum_{n>=0} sigma_n (1/2)^n = infinity`.

For a vertex-transitive locally finite multigraph the connective constant exists, and the radius of convergence of the SAW generating series is `1/mu(G)`. Divergence at `z=1/2` implies

`1/mu(G) <= 1/2`,

therefore

`mu(G)>=2`.

This proves the `[2,2,1]` type.

Combining the three cases gives

`C5: 0/5 -> 3/5`,

with covered set

`{[4,1],[3,2],[2,2,1]}`.

## 6. Method #2 — attack the negation first

Before trying to prove all five types, I searched for a degree-5 counterexample in the first unresolved multiplicity patterns. No exact counterexample emerged.

The weighted language explains why `[3,1,1]` is the critical-looking remaining class. After traversing an edge of multiplicity `m`, the normalized total weight of all distinct edge classes other than immediate reversal is heuristically

`(5-m)/2`

at `z=1/2`. If `m=3`, this is exactly `1`, so local branching alone has no slack. Simple weighted-ladder experiments stayed above growth 2, but those computations are exploratory only and are **not** a rigorous lower bound or a source claim.

For `[2,1,1,1]`, the local normalized outward total is larger, but globally self-avoidance can lose paths through cycles, so the local surplus is not by itself a proof.

Outcome of #2: no counterexample; it identified the two exact obstruction classes rather than producing a sampled 'bound'.

## 7. Method #26 — first sporadic unresolved degree

Freezing `Delta=5` turns the broad source question into a finite structural classification of multiplicity partitions. The exact five nonsimple partitions are

`[4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1]`.

This is the first degree at which the source theorem no longer applies in the nonsimple case, so it is the correct sporadic stress test. Three are now completely covered, not merely sampled.

### Remaining `[3,1,1]`

The triple edges form an invariant perfect matching; the two single edges form an invariant spanning 2-factor. If the 2-factor consists of finite cycles and one contracts the cycles, the matching connects cycles. But for a fixed entry/exit pair the analogue of the block polynomial is

`3*2^{-(r+1)} + 3*2^{-(L-r+1)}`

at `z=1/2`, which can be less than 1 for long cycles. The fixed quotient-ray proof used for `[2,2,1]` therefore genuinely fails. A proof must exploit the multiplicity of possible exits, transitivity of the quotient, or a different conserved potential; another fixed-route block estimate is insufficient.

### Remaining `[2,1,1,1]`

The double edges form an invariant perfect matching and the single edges form an invariant 3-regular spanning subgraph. Contracting the double matching produces a transitive degree-6 multigraph. At `z=1/2`, crossing a double edge has normalized weight exactly one, suggesting a reduction to single-edge SAW growth on the contracted object. But a naive appeal to the desired general lower bound becomes circular at degree 6. The next proof must use extra structure inherited from the matching contraction rather than invoke D0069 itself one degree higher.

These are the exact remaining obligations for the frozen `Delta=5` metric.

## 8. Exact finite self-check

Only after the proof route was established, I added an exact-arithmetic self-check:

- `artifacts/R06/d0069_degree5_partition_selfcheck.py` @ commit `854b323383a78aaffa34528a799ef5e35c0fc30b`;
- archived output `artifacts/R06/d0069_degree5_partition_selfcheck.out` @ commit `49b9d0bfdcef248c6695acb63828170424589465`.

It was executed in exact rational/integer arithmetic. It verifies:

- all integer partitions of 5 and the exact five nonsimple types;
- the line-type identities `a(5-a)>=4` for `a=1,2,3,4`;
- the cycle-block identity at `z=1/2` for all `3<=L<=100` and every `1<=r<L`, 4949 exact cases.

Archived output ends

`SELF_CHECK_PASS`.

This is explicitly a **self-check**, not a substitute for the infinite-graph proof in Section 5.

## 9. Independent audit of newest R07 package

Newest neighboring theorem checked:

`runs/R07/20260917T0822Z_i0077_periodic_one_sided_barriers_16.md`, theorem `I0077-R07-T17`.

**Audit ID:** `R06-AUDIT-R07-I0077-T17-20260917T0920Z`  
**Verdict:** `PASS_SCOPED / NOVELTY_UNVERIFIED`.

I checked the three substantive steps.

1. In T17(A), the Lamperti transform turns reversed Brownian increments into stationary OU. On each logarithmic gate the killed OU semigroup on `(-infinity,-A)` has `L^2(gamma)` norm `exp(-lambda_A t)`; discarding constraints between gates costs at most one. Periodic gate counting therefore gives the stated polynomial survival exponent `kappa=(tau/P)lambda_A`.
2. The passage from deterministic integer terminal times to arbitrary real terminal times uses a Brownian-modulus event with summable Gaussian tail and a scale `R_n=O(log n)`. When `kappa>1`, the resulting bound is summable. The later FBM transfer uses one deterministic witness index with high probability of a sufficiently remote terminal time; it does not assume the random witness time is a stopping time or independent of the Brownian witness.
3. T17(B) and T17(C) correctly reduce to the source half-line parabolic theorem: if `inf b>-1`, choose a constant `c` between `-1` and `inf b`; for the simultaneous nonnegative-barrier statement use the source pointwise construction for the half-line boundary `0`.

The source Problem 7.8 is open-ended, so R07 correctly retains overall status PARTIAL.

## 10. Model / scheduler control status

The control limitation remains unchanged. The exposed scheduler/task-management surface supports prompt/title, schedule/timing, enabled state and timing mode, but no model-family selector, no reasoning-effort selector, no authenticated completed-run routing telemetry and no verified full-hour guarantee. Therefore the prompt text `GPT-6 / maximum` does not establish or enforce that runtime.

Actually fixing this requires product/backend support for authorized model and reasoning fields plus per-run routing attestation, or an owning/admin task-control surface that exposes those settings.

The historical P26 response `You cannot modify this task` was an ownership/authorization denial in that context. Repository history also records a later authorized P/C-native context that successfully updated P26, so the denial is context-specific rather than evidence of a universal inability to edit the task. The legitimate workaround is the owning authorized context, ownership/admin transfer if supported, or platform support — not task duplication or bypass. No scheduler mutation was attempted in this run.

## 11. Status and next methods

Current D0069 status is **PARTIAL / PROVED-ON-PAGE FOR 3 OF 5 FROZEN DEGREE-5 TYPES / SELF-CHECK PASS / NOVELTY UNVERIFIED / CLOSURE AUDITS NOT YET REQUESTED**.

The next run must not repeat `#2,#18,#26`. The most promising new triple is:

- **#11 DUALIZE:** formulate the critical `z=1/2` path mass as a flow/capacity inequality on the quotient by invariant multiplicity subgraphs;
- **#14 FIND THE GROUP ACTING:** exploit vertex transitivity on the cycle/matching quotient to force enough exit orbits in `[3,1,1]`;
- **#25 COUNT THE SAME THING TWICE:** count weighted nonbacktracking/SAW extensions by entry class and exit orbit to recover the slack lost by a single fixed quotient ray.

No full-source closure is claimed.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R06
  run_id: 20260917T0920Z_d0069_degree5_three_partitions_13
  continuity:
    I0056:
      source: "Lyons-Peres, Probability on Trees and Networks, Question 6.20"
      state: RETIRED_AFTER_SIX_UNCHANGED
      frozen_metric: "width for Phi_V(H_{5,5})"
      frozen_value: 0
      source_status: PARTIAL
    I0079:
      state: RETIRED_AFTER_SIX_UNCHANGED
    P0189:
      state: RETIRED_KNOWN_IN_LITERAL_SCOPE
  source:
    id: D0069
    citation: "Grimmett-Li, Question 2.2 / Theorem 4.1(b) nonsimple extension"
    full_question: "Does mu(G)>=sqrt(Delta-1) extend to nonsimple infinite connected loopless vertex-transitive Delta-regular multigraphs for Delta>=5?"
    frozen_regime: "Delta=5"
    normalization: "edge-copy-distinct vertex-self-avoiding walks; target mu>=2"
  ownership:
    claim: "operations/claims/D0069.md"
    claim_commit: "89f4ca50bb58a0819f8c2b547432f516a169fedc"
  metric:
    name: C5
    definition: "number of five nonsimple degree-5 multiplicity partitions proved for all graphs of the type"
    before: "0/5"
    after: "3/5"
    unchanged_count: 0
    covered:
      - "[4,1]"
      - "[3,2]"
      - "[2,2,1]"
    remaining:
      - "[3,1,1]"
      - "[2,1,1,1]"
  status: PARTIAL
  tried_moves: [2,18,26]
  next_moves: [11,14,25]
  remaining_obligation: "Prove or refute the two remaining degree-5 types; even 5/5 remains a subclass result for the full Delta>=5 source question."
  evidence:
    - "artifacts/R06/d0069_degree5_partition_selfcheck.py @ 854b323383a78aaffa34528a799ef5e35c0fc30b"
    - "artifacts/R06/d0069_degree5_partition_selfcheck.out @ 49b9d0bfdcef248c6695acb63828170424589465"
  self_check: PASS
  novelty: UNVERIFIED
  closure_audits: []
  outgoing_audit:
    id: R06-AUDIT-R07-I0077-T17-20260917T0920Z
    verdict: PASS_SCOPED_NOVELTY_UNVERIFIED
```
