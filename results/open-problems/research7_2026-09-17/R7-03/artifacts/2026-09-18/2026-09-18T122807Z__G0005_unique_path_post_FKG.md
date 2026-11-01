Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum reasoning was requested, but no authenticated runtime model/effort telemetry or binding selector is exposed, so I do not claim otherwise.

# R7-03 admission-side theorem for G0005: exact post-FKG inequality on unique-`o`-`b`-path graphs

Date: 2026-09-18 UTC  
Slot: `R7-03 Boundary-Case Research`  
Native ID: `6aabe7be74008191b526b109ee4e9e80`  
Status: **admission-side mathematics only; G0005 is NOT admitted or claimed by R7-03**.

## 1. Outside source and why this is only an admission-side theorem

Canonical nearby source:

- Gady Kozma and Shahaf Nitzan, *A reduction of the theta(p_c)=0 problem to a conjectured inequality*, 2024, arXiv:2401.12397.
- Source Conjecture 1 (the stronger multiplicative inequality): for a finite graph with arbitrary independent edge-open probabilities, vertices `o,b`, and `A subseteq V`,

  `P(o<->b) >= P(o<->A) min_{a in A} P(a<->b)`.

- Source Conjecture 3 (the weaker uniform-continuity consequence represented by intake ID `G0005`): for every `eta>0` there exists `delta(eta)>0`, independent of the finite graph and of `|A|`, such that

  `P(o<->A)>1-delta` and `P(a<->b)>1-delta` for all `a in A`

  imply

  `P(o<->b)>1-eta`.

The current 2026-09-18 status is not clean enough for new ownership. A September 3, 2026 technical report describes a pinned August 28 Lean 4 release that claims an additive gluing theorem settling Conjecture 3, while public open-problem pages still list the conjecture as unresolved. The report itself explicitly calls the artifact unrefereed and distinguishes the pinned release from the current branch. Therefore R7-03 does **not** classify G0005 as a free OPEN target and does not create `operations/claims/G0005.md`.

The result below is an independently derived boundary-case theorem used to assess the shape of the source and the claimed gluing mechanism. No novelty claim is made.

## 2. The exact boundary-case theorem

### Theorem

Let `G=(V,E)` be a finite graph with independent Bernoulli bond percolation, allowing an arbitrary edge-open probability `p_e in [0,1]` for each edge. Fix vertices `o,b in V` and a nonempty set `A subseteq V`.

Assume that the underlying deterministic graph `G` has a **unique simple path from `o` to `b`**.

Then

`P(o<->b) >= P(o<->A) min_{a in A} P(a<->b)`.

Hence Kozma--Nitzan Conjecture 1 holds on this entire graph class. In particular Conjecture 3 holds there with

`delta(eta) = 1 - sqrt(1-eta)`,

and this modulus is sharp within the class.

This includes every finite tree, but is strictly more general: arbitrary cyclic subgraphs may hang off the unique `o`--`b` path, provided they do not create a second simple `o`--`b` path.

## 3. Proof

Write the unique simple `o`--`b` path as

`P : v_0=o, v_1, ..., v_m=b`,

and let `e_i={v_{i-1},v_i}` have open probability `p_i`.

### Step 1: every off-backbone component has a unique attachment vertex

Remove the vertices of `P`. Let `C` be any connected component of the remaining graph. It can be adjacent to at most one vertex of `P`.

Indeed, if `C` had neighbors at two distinct backbone vertices `v_i` and `v_j`, with `i<j`, then a path through `C` from `v_i` to `v_j` together with the prefix `o...v_i` and suffix `v_j...b` would give a second simple `o`--`b` path, contradicting uniqueness.

Thus every vertex `a` has a well-defined **projection** `rho(a)=v_{j(a)}` onto `P`: if `a` lies on `P`, take `rho(a)=a`; otherwise `rho(a)` is the unique backbone vertex to which the component containing `a` attaches.

### Step 2: prefix and suffix reliabilities

For `0<=j<=m`, define

`S_j = prod_{i=1}^j p_i`,

`T_j = prod_{i=j+1}^m p_i`.

Thus

`P(o<->v_j)=S_j`,

`P(v_j<->b)=T_j`,

and, because the `o`--`b` path is unique,

`P(o<->b)=S_j T_j`

for every `j`.

For `a in A`, let

`r_a = P(a<->rho(a) using only the attached component together with its attachment edges)`.

The branch edges are disjoint from the backbone edges. Any path from `a` to `b` must first reach `rho(a)` and then traverse the unique backbone suffix. Therefore

`P(a<->b)=r_a T_{j(a)} <= T_{j(a)}`.          (1)

### Step 3: choose the earliest projection

Choose `a_* in A` so that `j_*:=j(a_*)` is minimal among all `j(a)`, `a in A`.

If `o` connects to any point of `A`, it must traverse the backbone from `o` at least as far as `v_{j_*}`. Consequently the event inclusion

`{o<->A} subseteq {o<->v_{j_*}}`

holds deterministically, and therefore

`P(o<->A) <= S_{j_*}`.                       (2)

Let

`q = min_{a in A} P(a<->b)`.

Using `a_*` in (1),

`q <= P(a_*<->b) <= T_{j_*}`.                (3)

Multiplying (2) and (3),

`P(o<->A) q <= S_{j_*} T_{j_*} = P(o<->b)`.

This is exactly the source's multiplicative inequality. `QED`.

## 4. Exact sharp modulus for Conjecture 3 on this class

Suppose

`P(o<->A)>1-delta`

and

`P(a<->b)>1-delta` for every `a in A`.

The theorem gives

`P(o<->b) > (1-delta)^2`.

Therefore it suffices that

`(1-delta)^2 >= 1-eta`,

or equivalently

`delta <= 1-sqrt(1-eta)`.

Because the hypotheses are strict, the endpoint choice

`delta_*(eta)=1-sqrt(1-eta)`

still yields the strict conclusion `P(o<->b)>1-eta`.

### Sharpness

Take the three-vertex path `o--v--b`, put `A={v}`, and give both edges the same open probability `r`.

Then

`P(o<->A)=r`,

`P(v<->b)=r`,

`P(o<->b)=r^2`.

If `delta>1-sqrt(1-eta)`, choose

`1-delta < r < sqrt(1-eta)`.

Both hypotheses of Conjecture 3 hold with this `delta`, but `r^2<1-eta`. Hence no larger universal `delta(eta)` is possible even on paths.

So `delta_*(eta)=1-sqrt(1-eta)` is the exact optimal modulus for the unique-`o`-`b`-path class.

## 5. Three Section-B admission probes

### B2 — attack the negation first

I tried to create a counterexample inside the smallest structurally flexible class that still has a deterministic bottleneck: graphs with a unique `o`--`b` path but arbitrary cyclic decorations away from that path.

The counterexample search collapses because all relay projections are totally ordered along the unique backbone. The earliest projection `v_{j_*}` forces a single prefix event containing `{o<->A}`, while the same relay's `b`-connection lower-bounds the remaining suffix reliability. This proves the stronger multiplicative inequality rather than producing a counterexample.

Outcome: **full theorem for the unique-path class; no source-level closure.**

### B6 — deform from the solved tree case

The proof does not use acyclicity of the whole graph. It only uses uniqueness of the `o`--`b` path. Cycles may be inserted arbitrarily inside components attached at one backbone vertex. These decorations change the branch factors `r_a` but disappear from the core estimate because `r_a<=1`.

Outcome: the tree argument extends exactly to **all finite graphs with a unique simple `o`--`b` path**.

### B30 — localize the gluing failure

The proof uses exactly one structural property that fails when a second `o`--`b` route is introduced: the relay projections cease to be linearly ordered by a deterministic backbone, so there need not be a single event `{o<->v_*}` containing every realization of `{o<->A}`. Different realizations may reach different relays through different backbones.

Thus the first genuinely cyclic obstruction is not the branch reliability `r_a`; it is the loss of a deterministic **first relay / common prefix**. This matches the architecture described in the September 3, 2026 formal-artifact report: the claimed general proof replaces the deterministic first relay by a conditioned slack/surplus construction designed to control the random first relay without paying an error once per member of `A`.

Outcome: the exact gluing failure is localized to replacing a totally ordered deterministic relay projection by a random relay selector on cyclic graphs.

## 6. Relation to the 2026 claimed general resolution

The September 3 technical report states that the pinned Lean development proves the additive inequality

`P(o<->b) >= P(o<->A) - t`

whenever every relay `a in A` has failure probability `P(a !<-> b)<=t`. Taking `t=eta/2` yields Conjecture 3.

That report also states that the stronger multiplicative Conjecture 1 is **not** proved in general. The theorem above therefore sits in the precise gap between the two statements: on unique-path graphs the full multiplicative conjecture is elementary and has an exact sharp continuity modulus, while general cyclic graphs require the nontrivial relay-gluing mechanism.

This artifact does not validate the full Lean statement surface or the infinite-lattice reduction. Current worldwide status is therefore recorded only as:

`SOURCE-MATCHING FORMAL RESOLUTION CLAIM EXISTS / INDEPENDENT SEMANTIC RECONCILIATION PENDING`.

Public status pages that still mark the conjecture open are not treated as proof that it remains open, and the technical report is not treated as peer review.

## 7. Admission consequence for R7-03

`G0005` satisfies the R7-03 residue-2 ID gate, but it does **not** pass admission:

1. a concrete 2026 source-matching formal solution claim now exists and must be reconciled before any new OPEN assignment;
2. the source is a universal finite-graph theorem strong enough to settle the critical-percolation continuity problem, so it is honestly HARD rather than CLOSABLE for this slot even absent the resolution claim;
3. the theorem proved here is a restricted graph class and therefore cannot be substituted for the full source quantifiers.

No claim file is created, no target metric is initialized, and no source-level PROVED/REFUTED label is asserted by R7-03.
