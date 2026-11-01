# BT4 fleet04/B05 — bidirectional rank-two / order-wall reduction

Run: `b05-20260922t071405z-bt4`  
Candidate: `BT4-BIDIRECTIONAL-RANK2-ORDER-WALL-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Target and source state

The target is the k=4 Bermond–Thomassen conjecture in the user-selected simple-arc setting: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Digons are allowed in the target statement. The fleet's inherited minimal-counterexample normal form used below is oriented, exactly 7-outregular, 3-vertex-strong, arc-dominated, and equipped with a globally minimum packing of three chordless directed cycles `A,B,C` and acyclic remainder `R`.

External status checked in this run:
- Lichiardopol–Pór–Sereni, SIAM J. Discrete Math. 23 (2009), 979–992, DOI `10.1137/080715792`: minimum outdegree five gives three vertex-disjoint directed cycles.
- Bessy–Muis–Sereni–Steiner–Wiederrecht, arXiv:2608.12948, submitted 2026-08-13: the exact Bermond–Thomassen conjecture is stated there as unresolved for all `k>=4`; their theorem allows each packed cycle to need at most one reversed arc.

Controlling collective inputs actually consumed:
1. team lead fleet02/B04, `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, shared handoff blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`. Its correction is preserved: do not apply `BT4-SC2-THIRD-PORT-v1` directly to the clean four-port mixed cycle.
2. assigned OTHER-account partner fleet01/B06, `BT4-HT-ALIGNED-CROSS-COLLAPSE-v1` plus its common-port strengthening, shared handoff blob `64385bb2e2ad8508a02e9749ac5146f873eff978`.
3. fleet03/B05, `BT4-FOUR-PORT-CONNECTOR-RANK-WALL-v1`, shared handoff blob `5801ef39fc9f7cd699678cdd0803b7d525bfe5b1`. This proves that an endpoint-matched extra path does not by itself pay the two-connector rank needed for two disjoint mixed replacements.
4. fleet01/B04, `BT4-SHORTEST-MIXED-CYCLE-PORT-COLLAPSE-v1`, shared handoff blob `2ce9d6f84ecd3a6d78489f03938e1d0493874697`. A shortest mixed cycle forces a fresh-source cross or a distinct-port same-support bypass.
5. previous fleet04/B05 `BT4-HT-EQUALITY-COLLAR-ELIMINATION-v1`, handoff blob `d420b56ad8d6dc5df86ce7da43407fed0589a274`, with controlling path-scope correction blob `888492c0a6c6cc679c898cc77e72baa936a3f443`. Thus the aligned common-port equality collars remain eliminated and that local branch is forced to a genuine cross.

## Compact conditional end-to-end argument

In a putative BT4 counterexample, the collective reductions seek two legal mixed replacement cycles for two packed supports, or a same-support exchange/bypass, a third-support mediation, a strict smaller three-cycle packing, a cyclic exchanged remainder, or the SIX exit. The fleet03/B05 connector-rank wall shows why one endpoint-matched cross pair is insufficient. This run pays that rank/dependence debt as follows.

Fix two packed cycles `A,B`, the third packed cycle `C`, and a distinguished remainder vertex `x` (in the lead clean branch this is the old remainder sink). Three-vertex-strongness implies, after deleting `x`, two vertex-disjoint `A->B` paths and two vertex-disjoint `B->A` paths. After trimming to the last source-support hit and first target-support hit, either a path visits `C`, giving the required third-support mediation, or its whole interior lies in `R-{x}`. In the no-`C` case this gives rank two in both directions using genuine remainder-internal connectors.

Opposite-direction connector interiors cannot be treated as independent. If an `A->B` connector and a `B->A` connector meet in `R`, acyclicity of `R` forces all of their common vertices to occur in the same order, and a last common vertex splices them into a genuine same-support `A` return/bypass (and symmetrically on `B`). Hence, after excluding that already-useful output, the two directional linkages have pairwise disjoint remainder interiors.

The only remaining dependence is then visible on the cyclic order of the four connector endpoints on each support. If the two endpoint types alternate on both supports with the same pairing parity, the connectors reconstruct two vertex-disjoint mixed directed cycles. Global minimum of the original packing gives an exact tax: the number of omitted support vertices is at most the total number of remainder-interior connector vertices. If alternation fails, or the parities disagree, the residual obstruction is an explicit support-order wall rather than a connector-rank or hidden-independence gap.

Thus the first unpaid implication after this run is no longer connector rank. It is the explicit endpoint-collision / cyclic-order wall described below.

## Lemma 1 — rank two after deleting one remainder vertex

Let `D` be 3-vertex-strong. Let `A,B` be disjoint directed cycles, each of order at least three, and let `x` be outside `A union B`. Then `D-x` contains two vertex-disjoint directed paths from `A` to `B`, and also two vertex-disjoint directed paths from `B` to `A`.

### Proof

Consider `A->B`. If one vertex `s` met every directed `A->B` path in `D-x`, then delete `{x,s}`. Because `D` is 3-vertex-strong, `D-{x,s}` is strongly connected. If `s` lies outside `A union B`, any surviving `a in A` and `b in B` give an `a->b` path avoiding `s`. If `s in A`, choose another vertex of `A` (possible because `|A|>=3`) and a vertex of `B`; if `s in B`, choose a vertex of `A` and another vertex of `B`. In all cases an `A->B` path avoiding `s` exists, contradiction. Therefore the minimum vertex separator between the two sets in `D-x` has size at least two. Directed vertex-Menger gives two fully vertex-disjoint `A->B` paths. Reverse the roles of `A,B` for the other direction. QED.

For each Menger path trim its prefix through the source support and suffix after its first target-support arrival: retain the subpath from its last source-support vertex to the first later target-support vertex. Trimming preserves the pairwise vertex-disjointness and makes the interior avoid `A union B`.

## Corollary 2 — rank two or third-support mediation

In the inherited three-packing `(A,B,C)` with acyclic remainder `R`, fix `x in R`. For each direction `A->B` and `B->A`, either:

- a trimmed Menger path meets `C`; then its first/last `C` hits exhibit a genuine mediation through the third packed support; or
- there are two vertex-disjoint connectors in that direction whose interiors lie entirely in `R-{x}` and whose endpoints on each support are distinct.

Hence, if neither direction has third-support mediation, write the two `A->B` connectors

`F_i : alpha_i -> ... -> beta_i` (`alpha_i in A`, `beta_i in B`, `i=1,2`)

and the two `B->A` connectors

`G_j : gamma_j -> ... -> delta_j` (`gamma_j in B`, `delta_j in A`, `j=1,2`),

with each same-direction pair vertex-disjoint and all interiors contained in `R-{x}`.

This directly upgrades the fleet03/B05 rank-one obstruction: in the pure `A,B,R` branch, connector matching number one cannot be the terminal explanation in either direction.

## Lemma 3 — opposite-linkage intersection emits a same-support return

Assume Corollary 2 is in its pure remainder-internal case. If `F_i` and `G_j` share an internal remainder vertex, then there is a directed path from `alpha_i` to `delta_j` whose internal vertices lie in `R-{x}`. If `alpha_i != delta_j`, this is a genuine distinct-port same-support bypass on `A`; if `alpha_i=delta_j`, it is a directed cycle meeting `A` in that one vertex and otherwise lying in `R-{x}`. The analogous statement holds on `B`.

### Proof

First observe that common remainder vertices of `F_i` and `G_j` have the same order on the two paths. Otherwise there are common vertices `u,v` with `u` before `v` on `F_i` and `v` before `u` on `G_j`; the subpaths `F_i[u,v]` and `G_j[v,u]` form a directed closed walk entirely in `R`, hence contain a directed cycle in `D[R]`, contradicting acyclicity.

Choose the last common remainder vertex `u` in this common order. Concatenate `F_i[alpha_i,u]` with `G_j[u,delta_j]`. The same-order observation and the choice of `u` prevent a repeated internal vertex, so the concatenation is a directed path with all internal vertices in `R-{x}`. Its two endpoint cases are exactly those stated. QED.

A one-support cycle from the coincident-endpoint case is disjoint from the other two packed cycles, so it is an actual packing exchange object. A distinct-endpoint bypass closes with the directed support segment `A[delta_j,alpha_i]` and is likewise an actual one-support replacement object; global minimum supplies the usual length tax. Therefore this output is not being counted as silence.

## Lemma 4 — exact two-linkage reconstruction and support-order criterion

Assume there is no third-support mediation and no output of Lemma 3. Then the four connector interiors are pairwise disjoint. Suppose additionally that there is no cross-direction endpoint collision, so the four support endpoints `alpha_1,alpha_2,delta_1,delta_2` are distinct on `A`, and `beta_1,beta_2,gamma_1,gamma_2` are distinct on `B`.

For a permutation `pi` of `{1,2}` define

`Z_i(pi) = F_i + B[beta_i,gamma_{pi(i)}] + G_{pi(i)} + A[delta_{pi(i)},alpha_i]`.

Each `Z_i(pi)` is a genuine directed cycle. The pair `Z_1(pi),Z_2(pi)` is vertex-disjoint exactly when the two displayed `A`-segments are vertex-disjoint and the two displayed `B`-segments are vertex-disjoint.

On `A`, such a disjoint pairing exists iff the four endpoints alternate by type (`delta,alpha,delta,alpha`) around the directed cycle; when it exists, the pairing `pi_A` is unique. On `B`, such a pairing exists iff the four endpoints alternate by type (`beta,gamma,beta,gamma`), with a unique pairing `pi_B`. Consequently a legal two-cycle mixed reconstruction exists whenever both supports alternate and `pi_A=pi_B`.

### Proof of the cyclic-order assertion

On a directed cycle, two directed segments from two `delta` endpoints to two `alpha` endpoints can be vertex-disjoint only if, after starting at any one endpoint, the endpoint types alternate. If two endpoints of the same type occur consecutively in cyclic order, whichever target is paired to the first source forces one directed segment to pass a distinct endpoint needed by the other segment. Conversely, in alternating order, pair each `delta` with the next appropriate `alpha` before the next `delta`; the two directed segments are disjoint. This pairing is unique. Apply the same argument on `B`. Since connector interiors and endpoints are otherwise disjoint, matching the two support pairings gives the two vertex-disjoint cycles. QED.

This is the exact dependency condition; no probabilistic independence is assumed.

## Lemma 5 — minimum-packing tax for a compatible two-linkage

In the compatible-order case of Lemma 4, put

`S_A = A[delta_{pi(1)},alpha_1] union A[delta_{pi(2)},alpha_2]`,
`S_B = B[beta_1,gamma_{pi(1)}] union B[beta_2,gamma_{pi(2)}]`.

Let `I` be the total number of internal vertices in the four connectors `F_1,F_2,G_1,G_2`. Because the connector interiors are pairwise disjoint and lie in `R-{x}`,

`I <= |R|-1`.

The two reconstructed cycles have total order

`|Z_1|+|Z_2| = |S_A|+|S_B|+I`.

Since `(A,B,C)` was globally minimum among three-cycle packings, replacing `A,B` by `Z_1,Z_2` gives

`|S_A|+|S_B|+I >= |A|+|B|`.

Equivalently,

`(|A|-|S_A|)+(|B|-|S_B|) <= I <= |R|-1`.

Thus a compatible rank-two linkage cannot omit more support vertices than it uses remainder-interior vertices. In the four-remainder cage with distinguished `x`, this specializes to an omitted-support budget at most three. This is a genuine counting consequence, not a closure claim.

## What this pays and what it does not

Paid in this run:

1. The fleet03/B05 connector-rank-one wall cannot persist as a pure `A,B,R` phenomenon after deleting the old sink: 3-vertex-strongness forces rank two in each direction, unless a path is mediated by the third packed support.
2. Dependence between the two directional linkages is handled. An interior collision yields an explicit same-support exchange/bypass; otherwise the interiors are genuinely disjoint.
3. In the fully disjoint case, two-cycle reconstruction is reduced to an exact cyclic-order parity condition on the support endpoints, with an exact minimum-packing tax.
4. For `|R|=4`, any compatible two-linkage can omit at most three total support vertices after `x` is excluded from connector interiors.

Not paid:

- endpoint collisions between opposite-direction connectors;
- nonalternating endpoint order on one support;
- alternating orders with opposite pairing parity on `A` and `B`;
- converting every legal two-cycle replacement into a strict packing reduction or a cycle in the exchanged remainder;
- global SIX closure and the remaining bounded F2/F3 / support-carried seven-remainder states.

## First essential missing implication

`BT4-BIDIR-ORDER-WALL-CLOSE-v1`:

In the lead's clean four-port / aligned-cross branch, combine the lead's genuine cross, the assigned partner's forced-cross output after equality-collar elimination, and the rank-two theorem above. Prove that one of the following must occur:

1. third-support mediation;
2. an interior-intersection same-support exchange/bypass;
3. a cross-direction endpoint collision that yields a legal splice or strict/neutral exchange;
4. compatible alternating orders with matching parity, hence two mixed replacement cycles satisfying the tax; or
5. a contradiction to 3-vertex-strongness / exact-seven domination from the remaining nonalternating or parity-mismatch wall.

The unresolved core is now explicit cyclic port order, not connector matching number or unproved independence.

## Candidate honesty / failure record

Classification: `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

No claim is made that BT4 is solved. No novelty inference is made from a literature search. No auxiliary count is promoted to closure. No code was used for the mathematical claim in this run, so there is no code/output dependency to report. The proof is source-bound to the internal controlling handoffs listed above and the two external literature items listed at the top.

Privacy/scope: this report contains only scoped mathematical statements, public bibliographic references, and logical worker/artifact labels. It contains no credentials, scheduler identifiers, machine paths, private transcripts, benchmark gold, email/Drive material, unrelated private data, or public-posting action.
