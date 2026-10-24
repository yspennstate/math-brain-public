# BT4 report — Menger rank lift and opposite-connector intersection collapse

Run: `20260922T070806Z-b06-bt4-coll11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Role: account04/B06  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Candidate: `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and current source boundary

Target: prove the genuine `k=4` Bermond--Thomassen statement: every finite loopless digraph, with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven, contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are permitted, so digons count.

The current source check remains consistent with the team boundary. Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), states that the genuine conjecture remains unresolved for every `k>=4`; their theorem at the `2k-1` threshold permits a cycle which becomes directed after reversing one arc, so it does not settle BT4. The genuine `k=3` input used below is Lichiardopol--Pór--Sereni, *A Step toward the Bermond-Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992.

No novelty claim is made from a search miss. This report is an internal proof attempt.

## 2. Exact inherited state actually consumed

### Lead account02/B04

I read the complete lead report at

`proofnet24/collective-BT4/account02/B04/20260922T0619Z-b04-bt4-r11/report.md`,

creation commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`, and its shared handoff blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`.

The inherited normal form is a hypothetical oriented exact-outdegree-seven BT4 counterexample `D`, arc-dominated and 3-vertex-strong, with three pairwise disjoint directed cycles chosen lexicographically: first minimize total packed order and then maximize the arc count of the acyclic remainder. The packed cycles are chordless. In the aligned four-remainder heavy-triangle branch they are denoted `H,A,B`, with `H=h0 h1 h2 h0` a directed triangle and old remainder `R={x,r0,r1,r2}` acyclic.

The lead's corrected clean light-support pair is

`P : p -> x -> b`  (`A -> B`),

`Q : q -> a3`      (`B -> A`),

where `a3=p+++`, the four packed ports `p,a3,b,q` are distinct, and `x` is the old remainder sink. The lead proved `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`: the mixed cycle formed from `P,Q` and support segments forces another genuine packed-to-packed CROSS or a distinct-port same-support remainder BYPASS, but the result by itself does not give two replacement cycles.

### Named OTHER-account partner account01/B04 — actually applied

I read and apply account01/B04 `BT4-SHORTEST-MIXED-CYCLE-PORT-COLLAPSE-v1`, canonical report commit `6c8161e81c755382994814f67272705af0134caa`, report blob `84a4f2e7929cbe4844f2421240a3dc8eb822d431`, shared handoff blob `2ce9d6f84ecd3a6d78489f03938e1d0493874697`.

Its source-valid conclusion is: after choosing a shortest genuine mixed cycle `K*` made from the two light supports and the clean switching geometry, cross-chord descent plus the genuine `k=3` deletion theorem forces either

1. a packed-to-packed CROSS whose source is outside the working mixed cycle; or
2. a distinct-port same-support BYPASS carrying the minimum-packing tax.

The partner explicitly leaves the next implication `BT4-FRESH-CROSS-BYPASS-SPLICE-v1`: convert the new fresh-source cross or bypass into a legal two-cycle exchange / smaller minimum packing / cyclic exchanged remainder / SIX / compatible bypass family.

### Adversarial compatibility check used

I also used account03/B05 `BT4-FOUR-PORT-CONNECTOR-RANK-WALL-v1`, shared handoff blob `5801ef39fc9f7cd699678cdd0803b7d525bfe5b1`. It correctly points out that an endpoint-matched direct/path pair has connector matching number one and therefore cannot, by itself, justify two vertex-disjoint mixed replacement cycles. Its next target is to freshen a reverse connector or force third-support mediation. This report directly attacks that rank-one obstruction.

## 3. Compact conditional end-to-end route

The campaign-level route retained from the lead is:

1. Reduce a minimal counterexample to the oriented exact-seven normal form; the genuine `k=3` theorem gives a three-cycle packing with acyclic complement.
2. Choose the packing globally minimum and then remainder-arc-maximal; inherited work gives chordlessness, arc domination and 3-vertex-strongness.
3. Pair-deletion / fan-deficit analysis splits into SIX and global NO-SIX states. Existing workers reduce the principal no-six sink states to `(3,2,2)`, exact-five witnesses, reciprocal crosses, neutral pivots, or short-support boundaries.
4. In the four-remainder heavy-triangle branch, the aligned long-support state reaches the clean pair `P,Q`. The lead and account01/B04 now guarantee a further CROSS or BYPASS without the invalid old two-packed-vertex inference.
5. If every resulting cross/bypass interface can be converted into either a strict smaller three-packing, a cyclic exchanged remainder, a fourth cycle, a SIX exit, or a compatible bypass family covered by the condensation theorem, this heavy-triangle branch closes.
6. Full BT4 additionally still requires the separate global SIX closure, bounded F2/F3 short-support states, and the remaining support-carried seven-remainder branch.

The first local unpaid arrow entering this run was therefore not existence of another interface. It was connector rank / disjointness: a single extra cross may still have matching number one relative to the opposite direction.

## 4. New theorem A — three-linkage dichotomy between two packed supports

### Statement

Let `D` be 3-vertex-strong. Let `A,B,H` be three pairwise vertex-disjoint directed cycles and put

`R = V(D) \ (V(A) union V(B) union V(H))`.

Assume `|A|,|B|>=3` (automatic here). For either ordered pair `(X,Y)=(A,B)` or `(B,A)`, one of the following holds:

**R2.** There exist two pairwise vertex-disjoint directed `X -> Y` paths whose internal vertices all lie in `R`.

**H2.** There exist two pairwise vertex-disjoint directed `X -> Y` paths, with interiors disjoint from `X union Y`, each of which meets `H`.

If in addition `H` is a triangle, then in case H2 at least one of those two paths meets `H` in exactly one vertex. If all three Menger paths meet `H`, each meets `H` in exactly one distinct vertex.

### Proof

Use the vertex form of directed Menger between the vertex sets `X` and `Y`.

There are three pairwise vertex-disjoint directed `X -> Y` paths. Indeed, if not, Menger gives a vertex set `S` with `|S|<=2` meeting every `X -> Y` path. Since `|X|,|Y|>=3`, choose `x in X\S` and `y in Y\S`. But `D-S` is strongly connected by 3-vertex-strongness, so it contains an `x -> y` path avoiding `S`, contradiction.

Take three such disjoint paths and trim each from its last vertex on `X` to its first later vertex on `Y`. The trimmed paths remain pairwise vertex-disjoint, and their internal vertices avoid `X union Y`. The only old packed vertices available internally are therefore vertices of `H`; all other internal vertices lie in `R`.

If at most one trimmed path meets `H`, the other two have all internal vertices in `R`, giving R2. Otherwise at least two trimmed paths meet `H`, giving H2.

When `H` is a triangle, the two H2 paths are vertex-disjoint and hence meet disjoint nonempty subsets of the three vertices of `H`. Therefore at least one of the two uses exactly one `H` vertex. If all three trimmed Menger paths meet `H`, their three nonempty pairwise-disjoint traces partition the three vertices of `H`, so each trace is a singleton. QED.

### Why this matters

The connector-rank-one wall is not a terminal state. In each direction between `A` and `B`, either the remainder itself carries a rank-two linkage, or third-support mediation occurs at rank at least two. In the heavy-triangle branch the latter contains a connector pinned through a single `h_i`, not an amorphous path wandering through the entire third support.

This is stronger than obtaining one fresh path from 3-connectivity: it localizes the entire failure of remainder rank two to two vertex-disjoint `H`-mediated routes.

## 5. New theorem B — a prescribed direct cross always freshens, or hits the third support

### Statement

Under the same hypotheses, let `e=c->w` be a direct cross with `c in X`, `w in Y`, `X!=Y` and `X,Y in {A,B}`. Then there is a second directed `X -> Y` connector `J` vertex-disjoint from the two-vertex path `e` such that either

1. every internal vertex of `J` lies in `R`; or
2. `J` meets `H`.

### Proof

Delete the two endpoints `c,w`. Since `D` is 3-vertex-strong, `D-{c,w}` is strongly connected. Both `X-{c}` and `Y-{w}` are nonempty. Choose any `x in X-{c}` and `y in Y-{w}` and an `x -> y` path in `D-{c,w}`. Trim it from its last `X` vertex to its first subsequent `Y` vertex. Its endpoints avoid `c,w`, its interior avoids `X union Y`, and it is vertex-disjoint from the direct edge `e`. If its interior avoids `H` it lies wholly in `R`; otherwise it is third-support-mediated. QED.

### Application to the named partner result

Account01/B04 gives, in the non-bypass branch, a fresh-source packed CROSS from the shortest mixed-cycle argument.

- If this CROSS already uses `H` as one endpoint, the branch has entered explicit third-support mediation.
- If it is a direct `A <-> B` cross, Theorem B says its direction has connector rank at least two unless a second route necessarily goes through `H`.
- Independently, Theorem A applied in the opposite ordered direction yields either rank two through `R` or two `H`-mediated connectors.

Thus the partner's fresh cross cannot leave the branch with only the old endpoint-matched rank-one geometry.

## 6. New theorem C — an opposite-connector intersection is itself a bypass/short-support event

The remaining possible objection is that two rank-two linkage families in opposite directions may intersect in `R`. In the acyclic remainder this is productive rather than silent.

### Statement

Let

`P : alpha -> ... -> beta` be an `A -> B` connector,

`Q : gamma -> ... -> delta` be a `B -> A` connector,

and suppose every internal vertex of both paths lies in the acyclic remainder `R`. Suppose `P` and `Q` share at least one internal remainder vertex.

Then:

1. the common internal vertices occur in the same order along `P` and along `Q`;
2. for any common internal vertex `z`, the concatenations

   `J_A = P[alpha,z] + Q[z,delta]`,

   `J_B = Q[gamma,z] + P[z,beta]`

   are simple directed paths with all internal vertices in `R`;
3. if `alpha!=delta`, `J_A` is a genuine distinct-port same-support `A`-bypass, so if `ell_A` is its edge length and `d_A(alpha,delta)` is the forward support distance, global minimum forces

   `ell_A >= d_A(alpha,delta)`;

   if `alpha=delta`, `J_A` is a directed cycle meeting the old packing in exactly that one `A` vertex, and replacing `A` by `J_A` in the three-packing forces

   `|A| <= |V(J_A)| <= |R|+1`;
4. symmetrically, if `gamma!=beta`, `J_B` is a genuine distinct-port `B`-bypass with its exact minimum-packing tax; if `gamma=beta`, then `|B|<=|R|+1`.

### Proof

If two common internal vertices `u,v` appeared in opposite orders on the two paths, say `u` before `v` on `P` but `v` before `u` on `Q`, then `P[u,v] union Q[v,u]` would be a directed cycle wholly contained in `R`, contradicting acyclicity. This proves the common-order property.

Fix a common internal vertex `z`. Because all common vertices have the same order, no internal vertex appearing before `z` on `P` can reappear after `z` on `Q`, and no vertex appearing before `z` on `Q` can reappear after `z` on `P`. Hence both concatenations displayed above are simple. Their internal vertices lie in `R`.

If the two endpoints on a support are distinct, switching the corresponding forward support segment with the new remainder path yields a directed replacement cycle. A shorter path would make a three-cycle packing of strictly smaller total order, contradicting global minimality; hence the stated distance tax.

If the support endpoints coincide, the concatenation itself is a directed cycle using one packed vertex and at most all `|R|` remainder vertices. Replacing the old support by this cycle while leaving the other two packed cycles unchanged is a valid three-cycle packing, so global minimum gives the displayed short-support bound. QED.

### Heavy-triangle consequence

Here `|R|=4`. Therefore any coincident-endpoint output in Theorem C forces the corresponding light support to have order at most five. That branch is not generic long-support splice debt any more; it is transferred to the already explicit bounded short-support programme.

If the endpoints are distinct, an intersection of opposite remainder connectors automatically emits exactly the same kind of same-support BYPASS needed by the existing compatible-bypass condensation programme.

Hence, **in the long-support / no-bypass subbranch, opposite-direction remainder connector families may be assumed internally disjoint across directions.**

## 7. What the new result pays, and what it does not

Combine the partner's shortest-mixed-cycle output with Theorems A--C.

### Partner BYPASS output

This already enters the compatible-bypass selection/condensation frontier. No new claim of compatibility or full `R` coverage is made.

### Partner CROSS output touching H

This enters a third-support-mediated branch. Theorem A strengthens that wall: if an ordered `A <-> B` direction does not provide two clean remainder connectors, then two vertex-disjoint routes in that direction meet `H`, and because `H` is a triangle at least one is pinned through a single `h_i`.

### Partner direct A--B CROSS output

Theorem B freshens that direct cross: the same direction has a second connector disjoint from it unless the second route is H-mediated. Theorem A gives the analogous rank-two-or-H2 dichotomy in the opposite direction.

If both directions are in the remainder-rank-two branch, Theorem C removes internal cross-direction intersection as a new obstruction: such an intersection yields a same-support bypass or the bounded support conclusion `|A|<=5` / `|B|<=5`.

Therefore in the all-long, no-bypass, no-H-mediation residual, the local splice problem has been reduced to a **pure packed-port order / endpoint compatibility problem for two internally vertex-disjoint connector families in each direction**. The earlier generic rank-one wall and arbitrary remainder-intersection wall are gone.

This is the exact substantive advance of this run.

## 8. First remaining implication after this run

Call the remaining local statement

`BT4-RANK2-PORT-ORDER-SPLICE-v1`:

> In the aligned four-remainder heavy-triangle state, assume both ordered directions between the light supports admit two internally remainder-disjoint connectors; assume opposite-direction interiors are disjoint (otherwise Theorem C gives BYPASS/short-support); assume no connector is H-mediated; and retain the partner fresh-source condition. Prove that the cyclic order and possible packed-endpoint collisions of the four connector ports force either (i) two legal vertex-disjoint replacement cycles with strict lexicographic improvement or cyclic exchanged remainder, (ii) a same-support compatible bypass family, (iii) SIX, or (iv) the bounded short-support branch.

The only new local obstruction is now on the old packed supports themselves: cyclic port order and endpoint collisions. It is no longer connector matching number one and no longer an uncontrolled intersection inside `R`.

Separate campaign debts remain: global SIX/H5 closure, the bounded F2/F3 short-support states, and the support-carried seven-remainder omitted-sink branch. I do not infer those from this result.

## 9. Adversarial checks and nonclaims

1. **Menger does not give simultaneous two-way 2-linkage.** Theorem A is applied separately in the two directions. It does not say that the chosen `A->B` and `B->A` families are mutually disjoint. Theorem C is precisely the source-valid treatment of an internal intersection; packed-port compatibility is retained as debt.
2. **Two crosses are not two replacement cycles.** Even four internally disjoint connector paths can fail the support cyclic-order compatibility needed for two disjoint mixed cycles. That is the next arrow, not silently assumed here.
3. **Third-support mediation is not closure.** H2 is a structural alternative, not a fourth cycle.
4. **A bypass is not automatically compatible with another bypass.** Existing condensation only applies after its compatibility hypotheses are checked.
5. **The one-endpoint case is not mislabelled.** Theorem C requires an internal remainder intersection. A collision only at a packed endpoint is intentionally left in `BT4-RANK2-PORT-ORDER-SPLICE-v1` rather than being called a remainder bypass.
6. **Digons are respected at target level.** The inherited oriented reduction is used only inside the already established minimal-counterexample normal form; the original theorem permits opposite arcs.
7. **No computation was used.** The result is purely deductive; there is no finite census or numerical closure claim.

## 10. Source/provenance and status

External source boundary checked this run:
- S. Bessy, M. Muis, J.-S. Sereni, R. Steiner, S. Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948, submitted 13 Aug 2026.
- N. Lichiardopol, A. Pór, J.-S. Sereni, *A Step toward the Bermond-Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992.

Internal dependencies are source-bound above by exact report/handoff blobs. The named OTHER-account result actually applied is account01/B04 `BT4-SHORTEST-MIXED-CYCLE-PORT-COLLAPSE-v1`.

Outcome is `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`. BT4 remains open in this work state.

Privacy/scope review: this report contains only scoped graph-theoretic mathematics, public bibliographic metadata, logical worker labels, and source-bound internal artifact identities. It contains no credentials, scheduler identifiers, machine paths, benchmark answers, unrelated private material, email/Drive content, or public-release action.
