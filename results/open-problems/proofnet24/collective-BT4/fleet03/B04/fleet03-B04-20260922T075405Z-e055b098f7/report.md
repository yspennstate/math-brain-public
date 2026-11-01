# BT4 fleet03/B04 — rank-three short-mixed-cycle bypass of the rank-two order wall

Run: `fleet03-B04-20260922T075405Z-e055b098f7`  
Candidate: `BT4-R4-RANK3-SHORT-MIXED-BYPASS-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact source state consumed

The target is the k=4 Bermond–Thomassen conjecture in the fleet's simple-arc formulation: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four vertex-disjoint genuine directed cycles; digons are allowed in the target statement.

This run directly consumed the assigned other-account partner result:

- fleet04/B05, `BT4-BIDIRECTIONAL-RANK2-ORDER-WALL-v1`, shared handoff blob `f553a1086caaea875705c6f8c5d3f268bda1d3c3`, canonical report blob `47bb1d2b3a2d01f6821e639310290557b3a54bc2`.

Compatible controlling inputs also consumed:

- fleet02/B04 lead, `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, shared handoff blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`;
- fleet01/B04, `BT4-SHORTEST-MIXED-CYCLE-PORT-COLLAPSE-v1`, shared handoff blob `2ce9d6f84ecd3a6d78489f03938e1d0493874697`.

The partner's first unpaid implication was `BT4-BIDIR-ORDER-WALL-CLOSE-v1`: after obtaining two A->B and two B->A connectors in `D-x`, close endpoint collision, nonalternation, and parity mismatch. The result below does not solve those cyclic-order cases one by one. Instead it changes mechanism on the same four-remainder configuration: use 3-connectivity before deleting `x`, escalate both directional linkages to rank three, then use the four-vertex remainder budget and a shortest mixed cycle. This bypasses the rank-two order wall as the next necessary obstruction.

## Inherited normal form used

As in the controlling BT4 reports, work in a putative minimum counterexample reduced to the following normal form:

- `D` is oriented and exactly 7-outregular;
- `D` is 3-vertex-strong and arc-dominated;
- `(A,B,C)` is a globally minimum packing of three pairwise vertex-disjoint chordless directed cycles;
- `R = V(D) \ (V(A) union V(B) union V(C))` is acyclic;
- this theorem concerns the current four-remainder cage `|R|=4`.

The standard k=3 Bermond-Thomassen theorem used below is the known result that minimum outdegree at least five forces three vertex-disjoint directed cycles. Thus, in a k=4 counterexample, deleting any genuine directed cycle `K` leaves a digraph with some vertex of outdegree at most four.

## New theorem — BT4-R4-RANK3-SHORT-MIXED-BYPASS-v1

Fix two packed cycles `A,B`, with `C` the third packed cycle, in the inherited `|R|=4` state. Then at least one of the following occurs:

1. a trimmed A->B or B->A connector passes through `C`, giving genuine third-support mediation;
2. opposite-direction connectors meet internally in `R`, giving the same-support return/bypass of fleet04/B05 Lemma 3;
3. there exists a genuine A/B mixed directed cycle `K` with at most one vertex of `R`, and after choosing such a cycle shortest, the exact-seven deletion argument forces either
   - a packed-to-packed CROSS whose packed source lies outside `K`, or
   - a distinct-port same-support bypass.

Consequently the rank-two endpoint-order/parity wall is not a terminal obstruction in the four-remainder cage. One can obtain a fresh-source cross or bypass without first resolving the rank-two cyclic order. This is a reduction, not a BT4 closure.

### Step 1 — rank three in each direction before deleting the old sink

Because `D` is 3-vertex-strong and `|A|,|B|>=3`, no set of at most two vertices separates `A` from `B`: after deleting such a set, at least one vertex of each support remains and the digraph is strongly connected. Directed vertex-Menger therefore gives three pairwise vertex-disjoint A->B paths. Trim each path from its last `A` hit to its first later `B` hit. The three trimmed paths still are pairwise vertex-disjoint and their interiors avoid `A union B`.

Do the same in the reverse direction, obtaining three pairwise vertex-disjoint B->A paths.

If any trimmed path meets `C`, alternative 1 holds. Hence assume no trimmed path meets `C`. Then all six connector interiors lie in `R`.

### Step 2 — either an interior collision is useful, or six interiors share only four vertices

Within each direction the three connectors are pairwise vertex-disjoint. If an A->B connector and a B->A connector share an internal remainder vertex, fleet04/B05's same-order/acyclicity argument applies verbatim: two common remainder vertices cannot appear in opposite order because that would create a directed cycle inside `R`; splicing at the last common vertex emits a same-support return/bypass (or the coincident-endpoint one-support cycle). Thus alternative 2 holds.

Exclude that output. Then the internal-vertex sets of all six connectors are pairwise disjoint subsets of the four-vertex set `R`.

Let `f_i` be the number of internal remainder vertices on the three A->B connectors and `g_j` the analogous numbers for the three B->A connectors. Pairwise disjointness gives

`sum_i f_i + sum_j g_j <= 4`.

Therefore

`min_i f_i + min_j g_j <= 1`.

Indeed, if both minima were at least one, the sum would be at least six; and if one minimum is zero while the other were at least two, the three connectors in the latter direction alone would use at least six remainder vertices.

Choose connectors `F:A->B` and `G:B->A` realizing these minima. Their interiors are disjoint and together use at most one remainder vertex.

### Step 3 — a genuine mixed cycle with at most one remainder vertex

Write the endpoints as

`F: alpha -> ... -> beta`, with `alpha in A`, `beta in B`,
`G: gamma -> ... -> delta`, with `gamma in B`, `delta in A`.

Concatenate

`F + B[beta,gamma] + G + A[delta,alpha]`.

Because the connector interiors are disjoint and avoid the packed supports, this is a genuine directed cycle. If `alpha=delta` or `beta=gamma`, the corresponding support segment is the single common endpoint; this does not create a repeated internal vertex. The cycle meets `R` in at most one vertex.

Hence the family `M` of genuine A/B mixed cycles using exactly two support switches, connector interiors in `R`, no vertex of `C`, and at most one vertex of `R` is nonempty. Choose `K` in `M` of minimum order and put

`r = |V(K) intersect R|`, so `r in {0,1}`.

If `r=0`, both support switches of `K` are direct packed-to-packed arcs. If `r=1`, one switch is a two-edge path through the unique remainder vertex and the other switch is direct. Thus `K` has exactly `2-r` direct packed-to-packed switching edges.

### Step 4 — cross-chord descent on the shortest mixed cycle

Let `c,w` be vertices of `K` on different packed supports. Suppose `c->w` is a direct arc not equal to one of the direct switching edges used by `K`.

Because `c,w` lie on opposite supports, the directed segment `K[w,c]` contains exactly one of the two support switches. Therefore

`c->w + K[w,c]`

is again a genuine A/B mixed cycle with at most the same one remainder vertex. Since `c->w` is not an edge of `K`, the complementary part of `K` has a nonempty interior, so this new mixed cycle is strictly shorter than `K`, contradiction.

Hence every direct cross-support arc whose two endpoints lie on `K` is one of the `2-r` direct switching edges of `K`.

### Step 5 — exact seven plus the genuine k=3 theorem forces a fresh cross or bypass

If `D-K` contained three vertex-disjoint directed cycles, together with `K` they would be four disjoint directed cycles, contrary to the assumed counterexample. By the known k=3 theorem, `D-K` therefore has a vertex `v` of outdegree at most four.

Since `D` is exactly 7-outregular, `v` has at least three distinct outneighbors on `K`.

**Packed witness.** Suppose first that `v` is packed. On its own packed chordless cycle, `v` can hit at most its cycle successor among vertices of `K`; `K` contains at most one remainder vertex. Thus among at least three hits on `K`, at least one is a vertex on a different packed support. This gives a direct packed-to-packed CROSS with source `v` outside `K`. This is the desired fresh-source cross.

**Remainder witness.** Suppose `v` lies in `R-V(K)`. At most `r` of its hits on `K` can be the unique remainder vertex of `K`, so at least `3-r` distinct hits have packed targets `w` on `A union B`.

For each such arc `v->w`, apply the inherited arc-domination lift used in the lead's `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`: repeatedly dominate the arc into the same packed target. Acyclicity of `R` forces this backward chain to terminate at a packed apex `c`, producing a path

`c -> ... -> v -> w`

with all internal vertices in `R`, together with the direct terminal arc `c->w`.

If `c,w` lie on the same packed support, the longer lifted path is a distinct-port same-support bypass, and we are done. Otherwise `c->w` is a direct CROSS.

Assume for contradiction that every one of these cross outputs has its source `c` on `K`. Then, by Step 4, every `c->w` must be one of the direct switching edges of `K`. The `3-r` packed targets `w` are distinct, so they would have to be distinct heads of direct switching edges. But `K` has only `2-r` such edges. Thus

`3-r <= 2-r`,

impossible.

Therefore at least one lifted output is either a same-support bypass or a packed-to-packed CROSS whose packed source lies outside `K`.

This proves the theorem.

## What changed relative to the assigned partner result

The partner's rank-two theorem correctly isolated a cyclic endpoint-order/parity wall after deleting a distinguished remainder vertex `x`. The new argument shows that in the four-remainder cage this wall need not be solved as a standalone cyclic-order classification:

- do not delete `x` initially;
- 3-vertex-strongness raises both directional connector matchings from two to three;
- if no useful opposite-direction interior collision occurs, six connector interiors fit into only four remainder vertices;
- therefore one A->B connector and one B->A connector together use at most one remainder vertex;
- a shortest mixed cycle built from them reactivates the exact-seven/k=3 deletion mechanism and forces a fresh-source cross or bypass independently of endpoint alternation or pairing parity.

Thus `BT4-BIDIR-ORDER-WALL-CLOSE-v1` is bypassed as the first necessary implication in this branch. This does **not** assert that the endpoint-order wall is false, nor that a fresh cross alone completes BT4.

## First remaining implication

`BT4-FRESH-CROSS-BYPASS-SPLICE-v2`:

Combine the fresh-source packed CROSS or distinct-port same-support BYPASS obtained above with the lead's clean four-port pair and the partner's existing equality-collar / bidirectional-linkage information. Prove one of:

1. two genuinely vertex-disjoint replacement directed cycles plus a strict decrease of the globally minimum three-packing;
2. a neutral exchange whose exchanged remainder contains a genuine directed cycle;
3. third-support mediation that closes to a legal disjoint splice;
4. SIX; or
5. a fourth directed cycle disjoint from the current three-packing.

The global SIX, bounded F2/F3, and seven-remainder support-carried branches remain separate debts.

## Honesty / scope

This is `ESSENTIAL_STEP_APPLIED`, not a full proof candidate. It uses the exact-seven hypothesis in Step 5, 3-vertex-strongness in Step 1, chordlessness and acyclicity explicitly, and preserves vertex-disjointness at every linkage/interior-counting step. No claim is made that BT4 is solved or that this lemma is novel in the literature. No code result is needed for the proof. No scheduler mutation, e-mail, Drive action, public workflow, paid API/model, credential, private transcript, or unrelated data was used.
