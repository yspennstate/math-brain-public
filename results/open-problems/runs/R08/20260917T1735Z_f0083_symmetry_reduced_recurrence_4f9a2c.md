Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MOVEMENT in active F0083: `1/2 -> 1/2`, unchanged count `2`; I0082 remains RETIRED/FROZEN at `2/3`, retirement count `6`. New theorem-sized movement outside the frozen metric: a symmetry-reduced recurrence criterion proves uniqueness for the flat-face and edge tangent configurations of the admitted F0083 tube candidate, while the triple-corner tangent is the first periodic tangent not covered because its quotient is three-dimensional and transient. Methods actually used: B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, B21 ASK WHO ELSE HAS THIS SHAPE, B22 READ THE FAILURES NOT THE SUCCESSES.** GPT-6 / maximum was requested in prompt text, but the exposed runtime has no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — F0083 symmetry-reduced recurrence and the corner threshold

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. The six-unchanged handoff controls operationally: I0082 remains frozen at `2/3` with retirement count `6`. The old R08 FPP route remains retired.

The active exclusive R08 claim is `operations/claims/F0083.md`, sourced to Christopher Hoffman, Alexander E. Holroyd and Yuval Peres, *A stable marriage of Poisson and Lebesgue*, Ann. Probab. 34 (2006), arXiv:math/0505668v4, open problem (i): whether some discrete set of centers in Euclidean space admits two stable Lebesgue allocations differing on a nonnull set.

The frozen explicit candidate remains

\[
m_n=\lfloor(1+|n|)^{3/4}\rfloor,
\qquad
H=\{(n,a,b,c)\in\mathbb Z^4:1\le a,b,c\le m_n\},
\qquad
\Xi_*=\mathbb Z^4\setminus H,
\]

with appetite one. The two frozen obligations remain:

1. candidate admissibility plus exact local/transient mechanism — **PROVED** in the admission run;
2. prove that this exact `Xi_*` has two stable appetite-one Lebesgue allocations differing on positive measure — **OPEN**.

Therefore the source-sized metric remains `1/2`. This is the second consecutive run without movement of that frozen metric, so `unchanged_count = 2`. The present theorem changes the route substantially but does not count as obligation 2.

At run start I recovered the campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current F0083 claim, the newest R08 report/commit, the F0083 intake/history, and the newest neighboring R09 state. There is no ownership overlap. The shared root ledger remains stale for the R-series, so this run records only its own immutable `ledger_delta` and does not edit shared roots or peer files.

## 2. Source/current-literature and ownership refresh

The source was reread directly. Theorem 2 states uniqueness when every bounded-distance graph on the centers is recurrent. In the contradiction proof, two different stable allocations produce a directed disagreement graph `G`; Lemma 10 proves it has no directed cycles, Lemma 11 proves incoming capacity is at most outgoing capacity, Lemma 12 gives uniformly bounded edge lengths and a uniform bound on the sum of capacities along every directed path from a fixed starting disagreement edge, and Proposition 13 converts those conditions into transience. The proof of Theorem 2 then contradicts recurrence because the disagreement graph is a subgraph of a recurrent bounded-distance graph.

For the extremal allocations needed below, the source also states that the site-optimal and center-optimal Gale--Shapley algorithms are isometry-equivariant. Lemma 15 sandwiches every stable allocation between those two extremals. Thus it is enough to prove that the two equivariant extremals coincide.

Fresh bounded searches dated 2026-09-17 used the exact title/authors together with `two stable allocations`, `discrete set`, `deterministic`, `nonuniqueness`, `periodic`, `recurrent quotient`, and related stable-allocation terminology. They recovered the original paper, Hoffman--Holroyd--Peres' later tail-bounds paper, and general stable-allocation / optimal-transport follow-ups, but no later primary source claiming to resolve the exact deterministic Euclidean question or stating the quotient-recurrence criterion proved below. This is bounded negative evidence only: worldwide open status and publication novelty remain **UNVERIFIED**.

Ownership remains exclusive to R08 under the current F0083 claim.

## 3. B22 first: isolate exactly where the source uniqueness proof fails

The previous run proved directly that the flat four-dimensional half-space tangent is unique even though its original bounded-distance graph is transient. That suggested that applying the source recurrence test in the ambient dimension throws away too much symmetry.

The source proof itself shows what must be preserved: if two allocations differ, the disagreement capacities force a **transient directed subgraph with bounded Euclidean steps**. For a configuration carrying a translation symmetry, the two Gale--Shapley extremals inherit that symmetry. Therefore the disagreement flow also inherits it. The right graph on which to test recurrence is not necessarily the ambient center graph, but the graph after quotienting the translation directions.

The next theorem makes that precise for periodic lattice subsets.

## 4. Symmetry-reduced recurrence criterion

### Theorem 1

Let `Xi subset Z^d` and let `Gamma <= Z^d` be a subgroup acting on `Xi` by translations. For `b<infinity`, define the quotient bounded-distance graph `Q_b(Xi,Gamma)` as follows:

- vertices are the `Gamma`-orbits `[xi]` in `Xi/Gamma`;
- two distinct orbit vertices are adjacent if there are representatives at Euclidean distance at most `b`.

Assume that for every finite `b`, `Q_b(Xi,Gamma)` is locally finite and recurrent for simple symmetric random walk. Then for appetite one, `Xi` has an `L`-a.e. unique stable Lebesgue allocation.

The same proof works for any fixed finite appetite after the harmless rescaling used in the source; appetite one is all that is needed for F0083.

### Proof

Let `psi^s` and `psi^c` be the site-optimal and center-optimal Gale--Shapley allocations. The source states that both algorithms are isometry-equivariant. Since every translation in `Gamma` preserves `Xi`, both allocations are `Gamma`-equivariant.

Suppose for contradiction that `psi^s` and `psi^c` differ on a nonnull set. Apply the source's Section 3 construction to this pair. For centers `xi,eta`, let

\[
q(xi,eta)=L F(xi,eta),
\]

using the source's disputed/preferred sets `F(xi,eta)`, and let `G` have a directed edge `xi -> eta` when `q(xi,eta)>0`.

Because both allocations are `Gamma`-equivariant, all of the sets entering the construction translate equivariantly, hence

\[
q(xi+gamma,eta+gamma)=q(xi,eta)
\qquad(gamma\in Gamma).
\tag{4.1}
\]

By the source's Lemma 10, `G` has no directed cycles. By Lemma 11,

\[
\sum_u q(u,v)\le \sum_w q(v,w)
\tag{4.2}
\]

at every vertex.

Choose any directed disagreement edge `e_0=(zeta,zeta')`. Let `H` be exactly the forward graph used in the source: `e_0` together with every vertex and edge reachable by a directed path from `zeta'`. By the source's Lemma 12 there are constants `B,K<infinity`, depending on `e_0`, such that

1. every edge of `H` has Euclidean length at most `B`;
2. every directed path in `H` beginning with `e_0` satisfies

\[
\sum_i q(e_i)\le K.
\tag{4.3}
\]

Project the reachable part of `H` to `Xi/Gamma`. The key point is that reachability plus translation equivariance **saturates all outgoing translates**. If `u` is a reached lift and `u_0 -> v_0` is any disagreement edge whose tail lies in the orbit `[u]`, translate that edge so that its tail becomes exactly `u`. Equation (4.1) gives another disagreement edge with the same capacity; because its tail is reached, the translated edge is itself in `H`. Consequently every outgoing disagreement type from a reached orbit is represented in `H`, and by Lemma 12 every such translated edge has length at most `B`.

For reached orbit vertices `U=[u]`, `V=[v]`, define

\[
\bar q(U,V)
  =\sum_{\gamma\in Gamma:\ q(u,v+\gamma)>0} q(u,v+\gamma),
\tag{4.4}
\]

where `u,v` are any fixed representatives and we retain only orbit vertices reached from the projected root edge. This is well defined by (4.1). It is a **finite** sum: all terms have `|u-(v+gamma)|<=B`, and a discrete translation lattice has only finitely many elements in a bounded ball. Moreover there is a uniform finite number

\[
M=M(B,Gamma)
\tag{4.5}
\]

of possible summands for any ordered pair of quotient vertices.

Let `bar H` be the directed support of `bar q` in the projected reachable graph, with root `rho=[zeta]` and the projected initial edge retained.

#### (a) `bar H` is locally finite and lies in `Q_B(Xi,Gamma)`

Every outgoing edge from a reached lift has length at most `B`, and a lattice ball contains finitely many centers. Hence each quotient vertex has finite degree and the undirected support of `bar H` is a subgraph of `Q_B(Xi,Gamma)`.

#### (b) `bar H` has no directed cycles

Suppose a directed quotient cycle existed. For each edge of that cycle choose one positive lifted displacement type. Starting from any reached lift of the first quotient vertex, translation equivariance lets us concatenate those chosen types. Repeating the quotient cycle gives an infinite directed path in `H`. If one traversal returns to the identical lift we have an actual directed cycle in `G`, contradicting Lemma 10. Otherwise the path advances by a nonzero element of `Gamma`; repeating the cycle repeats the same finite list of **positive capacities** forever. Its capacity sum therefore diverges, contradicting (4.3). Thus `bar H` is acyclic.

#### (c) increasing capacity descends to the quotient

Fix a nonroot reached orbit `V` and a reached lift `v`. Every quotient incoming edge represented in `bar H` is one of the full disagreement edges entering the orbit of `v`, whereas every full disagreement edge leaving `v` belongs to `H` by the outgoing-saturation observation. Summing (4.2) over displacement types therefore gives

\[
\sum_U \bar q(U,V)\le \sum_W \bar q(V,W).
\tag{4.6}
\]

The projected root has no incoming edge inside `bar H`, because such an edge together with the projected initial edge and reachability would give a projected directed cycle. Its projected initial outgoing capacity is positive.

#### (d) path summability descends to the quotient

Take any directed path

\[
U_0,U_1,U_2,\ldots
\]

in `bar H` beginning with the projected root edge. For each quotient edge choose a lifted displacement type with maximal capacity. Because there are at most `M` summands in (4.4),

\[
\bar q(U_i,U_{i+1})\le M q(e_i).
\tag{4.7}
\]

Starting at `zeta`, translate the chosen type at each step so that its tail equals the current lifted endpoint. The outgoing-saturation observation makes the resulting sequence a genuine directed path in `H`. Hence (4.3) and (4.7) imply

\[
\sum_i \bar q(U_i,U_{i+1})\le MK<\infty.
\tag{4.8}
\]

Thus `bar H`, with capacities `bar q`, satisfies every hypothesis of the source's Proposition 13. Its underlying undirected graph is therefore transient.

But by (a), the undirected `bar H` is a subgraph of the recurrent graph `Q_B(Xi,Gamma)`. The source itself uses the standard fact that a subgraph of a recurrent graph is recurrent. Contradiction.

Therefore `psi^s=psi^c` a.e. Finally, the source's Lemma 15 sandwiches every stable allocation between these two extremals; exactly as in the source's Theorem 3 argument, equality of the two extremals forces every stable allocation to agree with them a.e. This proves Theorem 1. QED.

### Audit note on the new step

The genuinely new ingredient relative to the source is not Proposition 13; it is the **projection of the source disagreement flow through a deterministic translation symmetry while preserving acyclicity, increasing capacity, and path summability**. The bounded-length conclusion of Lemma 12 is crucial: it makes each quotient capacity a finite sum and gives the uniform multiplicity `M` in (4.7).

I found no exact statement of this quotient criterion in the bounded literature search. It should nevertheless be treated as an adaptation of the HHP proof until independently audited, not as certified publication novelty.

## 5. B17 — the number that appears elsewhere is the recurrence dimension threshold

Apply Theorem 1 to the three periodic tangent geometries of the admitted tube candidate. Coordinates are `(n,a,b,c)`, where `n` is the tube axis and `(a,b,c)` are transverse.

### 5.1 Flat-face tangent: quotient dimension one

Deep inside a large flat face, the local center set is

\[
\Xi_{face}=\{(n,a,b,c)\in\mathbb Z^4:a\le0\}.
\]

It is invariant under translations in `(n,b,c)`, a rank-three subgroup. Quotienting those directions leaves the half-line `Z_{<=0}`. For every finite `B`, the quotient bounded-distance graph is a finite-range graph on a half-line and is recurrent. Therefore Theorem 1 gives

\[
\boxed{\Xi_{face}\text{ has an a.e. unique stable allocation.}}
\tag{5.1}
\]

This recovers the previous run's half-space uniqueness theorem by a completely different mechanism and removes the need for the explicit radius recursion when only uniqueness is wanted.

### 5.2 Edge tangent: quotient dimension two

Deep inside an edge where two faces of the missing tube meet, the local center set is

\[
\Xi_{edge}
 =\mathbb Z^4\setminus
   \{(n,a,b,c):a\ge1,\ b\ge1\}.
\]

It is invariant under translations in `(n,c)`. The quotient is

\[
\mathbb Z^2\setminus\{(a,b):a\ge1,b\ge1\}.
\]

For each finite `B`, its quotient bounded-distance graph is a subgraph of the finite-range graph on `Z^2`, which is recurrent. Hence

\[
\boxed{\Xi_{edge}\text{ has an a.e. unique stable allocation.}}
\tag{5.2}
\]

This is new relative to the previous run: a perfectly periodic **edge** also cannot support an autonomous second stable phase.

### 5.3 Triple-corner tangent: quotient dimension three

At a corner where all three transverse faces meet, the periodic tangent is

\[
\Xi_{corner}
 =\mathbb Z^4\setminus
   \{(n,a,b,c):a\ge1,\ b\ge1,\ c\ge1\}.
\]

Only the tube-axis translation remains. The quotient is

\[
\mathbb Z^3\setminus\mathbb N_+^3.
\]

Already its nearest-neighbor graph is transient: it contains a three-dimensional half-space/octant-type transient subgraph, and adding vertices or edges cannot restore recurrence. Therefore Theorem 1 **does not apply** to the corner tangent.

This is the B17 outcome: the integer `3` is not an accidental geometric count. It is exactly the simple-random-walk recurrence/transience threshold of the symmetry quotient. After quotienting the tangent symmetries,

- face -> effective dimension `1` -> recurrent -> unique;
- edge -> effective dimension `2` -> recurrent -> unique;
- triple corner -> effective dimension `3` -> transient -> first tangent that can evade this uniqueness mechanism.

## 6. B21 — the correct analogue is a boundary-at-infinity problem on the transient corner quotient

The source disagreement proof and Theorem 1 now point to the same structural target. Nonuniqueness cannot be generated by an autonomous periodic phase on a perfectly flat face or a perfectly straight edge. The first periodic tangent with enough room for a finite-energy disagreement flow is the triple-corner quotient, a transient three-dimensional graph.

That has the shape of a Dirichlet/Martin-boundary problem: distinct extremal states, if they exist, should be selected by different data at infinity on a transient quotient. This is also consistent with the admitted candidate's **two-ended** tube geometry. The right next local model is therefore not another flat-face radius perturbation but the corner tangent with two competing boundary conditions at large distance.

This is only a route identification. Transience of the corner quotient does **not** prove nonuniqueness; the previous half-space result already shows that ambient transience alone is insufficient.

## 7. What this does and does not prove about the actual `Xi_*`

Theorem 1 proves exact uniqueness for the infinite periodic tangent models `Xi_face` and `Xi_edge`. It does **not** prove that a finite patch of a slowly varying tube face or edge is immune to arbitrarily remote changes: stable allocations can communicate through long chains, and the actual `Xi_*` has neither exact face-translation nor exact edge-translation symmetry globally.

So the honest conclusion is narrower:

> A source-closing disagreement for the admitted `Xi_*`, if it exists, cannot be explained by an autonomous periodic phase living on the perfect flat-face or perfect edge tangent. The first periodic tangent not ruled out by symmetry-reduced recurrence is the triple-corner tangent, and the actual nonperiodic variation/two-ended coupling may still be essential.

The frozen obligation remains exactly

\[
\boxed{\psi_{site}\ne\psi_{center}\ \text{on a positive-measure set for the exact admitted }\Xi_*}. 
\]

No claim of source closure is made.

## 8. Method outcomes

### B17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

**Succeeded.** The face/edge/corner sequence `1,2,3` becomes the quotient random-walk dimension. The recurrence threshold at dimension two explains why faces and edges are rigid under the new criterion while triple corners are the first possible periodic escape.

### B21 — ASK WHO ELSE HAS THIS SHAPE

**Succeeded as route selection.** The remaining mechanism has the shape of a boundary-at-infinity / finite-energy-flow problem on a transient three-dimensional quotient. This suggests studying extremal boundary conditions on finite corner truncations and their limits, rather than refining the flat-face attenuation calculation.

### B22 — READ THE FAILURES, NOT THE SUCCESSES

**Succeeded.** The source proof fails only when its disagreement flow can live on a transient bounded-step graph. Quotienting exact translation symmetries shows that flat and edge tangents cannot realize that failure; the corner tangent can at least pass the graph-theoretic obstruction.

No finite claim was introduced, so no checker-only artifact was manufactured this run.

## 9. Stagnation and next run

Frozen metric: `1/2 -> 1/2`; unchanged count: `2`.

This is not yet the three-run stuck trigger. If the next run again fails to move the frozen obligation, the following run state must invoke the campaign's stuck protocol rather than append another ordinary lemma.

The next unused method triple is deliberately different:

- **B16 COMPUTE EVERY SMALL CASE**: exact finite corner-quotient truncations with two opposite boundary conditions; identify a central observable whose separation either persists or collapses;
- **B9 RANDOMIZE**: put random end/boundary data on the transient corner quotient and test whether two limiting extremal states occur with positive probability;
- **B10 DERANDOMIZE**: if random boundary data finds a separating event, extract one explicit deterministic boundary pattern and then attempt to port it to the slowly varying two-ended tube.

Any finite computation is exploratory only. Movement of obligation 2 requires a uniform positive separation surviving the infinite-volume limit or an exact analytic monotone-limit argument.

## 10. Model/scheduler control status

The exposed task-management surface still provides title, prompt, schedule/timing, and enabled-state controls, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run telemetry**. Thus GPT-6 / maximum can be requested only in prompt text from this surface; it cannot be verified or enforced here.

The current R08 scheduled task is still enabled and still carries the older I0082-centered title/prompt even though repository ownership has operationally rotated R08 to F0083. The owner instruction for this deployment explicitly forbids scheduler changes, so I did not modify it.

The historical P26 `You cannot modify this task` event remains an authorization-context issue. The repository records that a later authorized context succeeded. The legitimate workaround is therefore the owning/authorized context, supported ownership/admin transfer, or platform support—not duplicating or bypassing the task. Enforcing GPT-6 / maximum additionally requires native model/reasoning selectors plus completed-run telemetry in that authorized product/API/workspace.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R08
  active_target: F0083
  source: "Hoffman-Holroyd-Peres, A stable marriage of Poisson and Lebesgue, open problem (i)"
  owner: R08
  status: PARTIAL
  metric:
    name: "number of two frozen obligations proved for the admitted explicit candidate Xi_*"
    before: "1/2"
    after: "1/2"
    movement: "NO MOVEMENT"
    unchanged_count_before: 1
    unchanged_count_after: 2
  retired_target:
    id: I0082
    metric: "2/3"
    retirement_count: 6
    status: RETIRED_FROZEN
  theorem_sized_progress:
    - "Symmetry-reduced recurrence criterion for Gamma-periodic lattice subsets"
    - "Flat-face periodic tangent Xi_face is unique a.e."
    - "Edge periodic tangent Xi_edge is unique a.e."
    - "Triple-corner tangent is the first periodic tangent not covered; its quotient is transient in effective dimension 3"
  methods_used: [B17, B21, B22]
  next_methods: [B16, B9, B10]
  source_closed: false
  candidate_refuted: false
  current_literature_check: "bounded 2026-09-17 search found no source-matching resolution; worldwide status UNVERIFIED"
  novelty: UNVERIFIED
  ownership_check: "exclusive R08 F0083 claim preserved"
  checker_created: false
  shared_roots_edited: false
  peer_files_edited: false
  scheduler_changed: false
```
