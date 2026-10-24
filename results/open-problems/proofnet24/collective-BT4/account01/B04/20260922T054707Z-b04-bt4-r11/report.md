# BT4 account01/B04 — triangle-boundary collapse by the strengthened two-cycle theorem

Run: `20260922T054707Z-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-HT-TRIANGLE-BOUNDARY-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs, hence directed digons, are allowed in the source statement.

Fresh literature verification in this run retained the same source boundary. Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), state that the genuine conjecture remains unresolved for all `k>=4`; their threshold `2k-1` theorem permits one reversed arc and is not used as a genuine directed-cycle conclusion. The genuine lower-k source used here is Lichiardopol--Pór--Sereni, *A Step toward the Bermond--Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992, DOI 10.1137/080715792. Besides proving the `k=3` case, they prove that a digraph in which every vertex has outdegree at least three except for at most two vertices of outdegree two contains two vertex-disjoint directed cycles.

No literature-search miss is used as a novelty claim.

## Team state actually consumed

Latest complete campaign-lead report actually read: account02/B04 run `20260922T051543Z-b04-bt4-r11`, report blob `9f1ec8ca9ab3f2737b9dddf98389826f5b926933`, candidate “lexicographic heavy-triangle port separation.” I use its exact four-remainder heavy-triangle cage and its lexicographic globally minimum three-cycle packing.

Assigned partner account02/B05 was also read through run `20260922T052219Z-b05-bt4-6f8c7964`, report blob `739678d2c1387571ab1190a53530d1211a2ad1cf`, candidate `BT4-R4-TRIANGLE-LOCK-TRANSPORT-v1`. Its lock-transport state is compatible but is a different four-remainder branch; no partner outcome label is promoted here.

Named OTHER-account result actually consumed and applied: account03/B05 run `20260922T053930Z-account03-B05-r12-bt4`, parent candidate `BT4-HT-SHIFTED-TRIPLE-v1`, report blob `63fc0bf48372601801b40571f6610820ed31e96b`, together with its newer controlling addendum `BT4-HT-FORCED-CLEAN-CROSS-v1`, blob `e1d5aa82bc8d24be39cb7c34a0ef92ccd878dacd`. The parent proves that the aligned heavy-fan branch has either a triangular light support or the exact shifted triple; the addendum closes the long-support shifted triple to a clean four-distinct-port opposite-cross pair. This report attacks the sole short-support boundary left by that result.

I also use the already-proved remainder-heavy fan escape from account02/B20, `BT4-R-HEAVY-CROSS-v1`, report blob `1653289d6d3528ee9df6345871d4a447d43bf46b`; for completeness its short proof is restated below rather than treating the peer label as proof.

## Inherited minimum-counterexample normal form

Assume BT4 false. The inherited reduction first removes digons: deleting the two vertices of a digon lowers every remaining outdegree by at most two, so the genuine `k=3` theorem supplies three further disjoint cycles, which together with the digon would contradict BT4. Thus a minimal counterexample may be taken oriented. Retain exactly seven outgoing arcs at each vertex and use the inherited minimum-counterexample reductions to work in the exact-outdegree-seven, arc-dominated, 3-vertex-strong normal form.

Choose three disjoint directed cycles `(H,A,B)` minimizing total packed order and, among such packings, maximizing the number of arcs induced by the remainder. The remainder is acyclic, and every packed cycle is chordless.

In the lead's exact four-remainder heavy-triangle cage,

`H=h0->h1->h2->h0`,
`R={x,r0,r1,r2}`,

with saturation triangles

`Ti=hi->ri->x->hi`.

The exact old-remainder arcs are

`r0->r1`, `r1->r2`, `r0->x`, `r1->x`, `r2->x`.

For the `T0` deletion witness there is a light support `A` and a vertex `p in A` with

`p->h0`, `p->r0`, `p->x`,

and the sink fan on `A` is

`N+(x) intersect A={p+,p++}`.

Assume the aligned exact five-witness `h1` is heavy on the same support `A`. Account03/B05 now proves the exact dichotomy:

1. `|A|=3`; or
2. `|A|>=4` and a clean opposite `A<->B` cross pair with four distinct packed ports and disjoint remainder interiors is forced.

The long-support case is therefore already at the common port-splice frontier. The new work below eliminates the triangular support as a separate lock.

## New theorem — the triangular aligned boundary is SIX or two remainder-supported cross generators

Assume `|A|=3`. Write

`A=p->p+->p++->p`.

Because `h1` is heavy on `A` and `A` has only three vertices,

`h1->p`, `h1->p+`, `h1->p++`.                              (1)

The ambient arcs `p->r0`, `r0->h1`, `h1->p` form a directed triangle

`C0=p->r0->h1->p`.                                           (2)

It is vertex-disjoint from

`T2=h2->r2->x->h2`

and from the other light packed cycle `B`. Hence

`P0=(C0,T2,B)`                                               (3)

is another three-cycle packing of exactly the same total order as `(H,A,B)`. It is therefore globally minimum. Its remainder is exactly

`R0={h0,r1,p+,p++}`,                                        (4)

which is acyclic, since a cycle in `R0` together with the three cycles in (3) would already give four disjoint directed cycles.

Put

`G=D-(T2 union B)`.                                          (5)

Then `V(G)=V(C0) union R0`. The digraph `G` cannot contain two vertex-disjoint directed cycles, since such two cycles together with `T2` and `B` would be four disjoint directed cycles in `D`.

### Lemma 1 — two vertices of C0 are definitely not degree-two deficit witnesses

We have

`d_G+(p)>=3`, `d_G+(h1)>=4`.                                (6)

Indeed, `p` has the three distinct `G`-outneighbors

`r0`, `h0`, `p+`,

coming respectively from (2), the `T0` witness, and the original support edge of `A`.

Likewise `h1` has the four distinct `G`-outneighbors

`p`, `p+`, `p++`, `r1`,

by (1) and the exact cage identity `h1->r1`. QED.

### Lemma 2 — pair deletion forces two remainder exact-five witnesses unless SIX already occurs

Exactly one of the following holds:

- some vertex of `G` has outdegree at most one, hence sends at least six of its seven outgoing arcs into `T2 union B`; or
- at least two distinct vertices of `R0` have outdegree exactly two in `G`.

Proof. If the first alternative fails, then every vertex of `G` has outdegree at least two. Since `G` has no two vertex-disjoint directed cycles, the strengthened Lichiardopol--Pór--Sereni two-cycle theorem implies that `G` must have at least three vertices of outdegree exactly two: otherwise all vertices would have outdegree at least three except at most two vertices of outdegree two, forcing two disjoint cycles.

The cycle `C0` has only three vertices. By (6), at most its vertex `r0` can have outdegree two. Therefore at least two of the three degree-two vertices lie in the remainder `R0`. QED.

### Lemma 3 — every remainder exact-five witness gives a genuine cross

Let `w in R0` have `d_G+(w)=2`. Since `d_D+(w)=7`, exactly five outneighbors of `w` lie in `T2 union B`. Hence one of `T2,B`, say `Y`, receives at least three outgoing arcs from `w`.

First, `Y` cannot send an arc into `w`. If `y->w` for `y in Y`, choose among the at least three fan targets `a in N+(w) intersect Y` one minimizing the forward directed distance from `a` to `y` on `Y`. Because the normal form is oriented, `a!=y`, and with at least three distinct fan targets this distance is at most `|Y|-3`. Then

`y->w->a->Y[a,y]`

is a directed cycle of order at most `|Y|-1`, disjoint from the other two cycles of the minimum packing (3). Replacing `Y` strictly decreases total packed order, contradiction.

Now dominate one fan arc `w->a`, obtaining `z0->w,a`. Since `Y not->w`, `z0` is not on `Y`. If `z0` is already on one of the other packed cycles, `z0->a` is a genuine cross into `Y`. Otherwise `z0 in R0`. Repeatedly dominate `zi->w` while `zi in R0`. A remainder vertex cannot repeat, because the resulting backward chain would create a directed cycle in the acyclic `R0`. The finite chain therefore first reaches a packed vertex `zt`; the no-inarc conclusion excludes `zt in Y`. Thus

`zt->...->z0->a`

is a genuine packed-to-packed transition ending on `Y` whose internal vertices all lie in `R0`. QED.

### Theorem (`BT4-HT-TRIANGLE-BOUNDARY-COLLAPSE-v1`)

In the lead's aligned four-remainder heavy-triangle branch with `|A|=3`, either

1. there is a SIX witness into the fixed pair `T2 union B`; or
2. there are at least two distinct remainder-supported exact-five witnesses for that same pair, and each independently generates a genuine packed-to-packed cross transition by Lemma 3.

Thus the short-support boundary left by account03/B05 is not terminal. Combined with its controlling addendum, the entire aligned heavy-triangle branch now routes as follows:

- `|A|>=4` -> clean four-distinct-port opposite cross pair;
- `|A|=3` -> SIX, or at least two remainder-supported cross generators.

This is a reduction to the common CROSS/SIX splice frontier, not a proof that either frontier is already closed.

## Exact deletion and contraction accounting

The argument above also exhibits precisely what deletion loses, which is the assigned B04 structural task. For any packed cycle `C` and any outside vertex `v`, write

`a_C(v)=|N+(v) intersect C|`.

In the exact-seven normal form,

`d+_{D-C}(v)=7-a_C(v)`.                                     (7)

If `C` is contracted to one vertex and parallel arcs are coalesced, then

`d+_{D/C}(v)=7-a_C(v)+1_{a_C(v)>0}`.                        (8)

The contracted cycle vertex has outdegree equal only to the number of distinct external heads of `C`, which need not be seven. Thus contraction generally loses `a_C(v)-1` units at an outside vertex that hits `C`, and can also lose degree at the contracted vertex itself.

For two disjoint cycles `C1,C2`, the analogous simplified quotient formula is

`d+_{D/(C1,C2)}(v)=7-a_1(v)-a_2(v)+1_{a_1(v)>0}+1_{a_2(v)>0}`. (9)

The degree-two witnesses in Lemma 2 satisfy `a_{T2}(w)+a_B(w)=5`. Their pair-deletion degree is exactly two, while their two-cycle-contracted degree is only three if all five fan arcs hit one cycle and four if both cycles are hit. This is an explicit reason contraction does not preserve the minimum-outdegree-seven hypothesis at the exact obstruction produced by the proof.

Vertex-disjointness behaves asymmetrically: a family of vertex-disjoint quotient cycles uses a contracted vertex in at most one member, and that one cycle can be lifted through the directed original cycle along the appropriate directed segment. But contraction does not preserve the degree hypothesis needed to invoke BT4 recursively, so this lifting observation does not make contraction an induction step.

## Compact conditional end-to-end route after this run

Assume a BT4 counterexample and enter the inherited oriented exact-seven, arc-dominated, 3-vertex-strong minimum-packing normal form. The genuine `k=3` theorem supplies the initial three packing cycles, and pair deletion plus the strengthened `k=2` theorem supplies SIX/five-witness deficits after neutral exchanges. The lead's lexicographic four-remainder analysis and account03/B05 now reduce the aligned heavy-triangle branch to a clean long-support cross interface or the short triangle. The theorem above sends the short triangle to SIX or two remainder-supported cross generators. Other compatible team work sends the long-F2 exact-five output to CROSS and the all-long exact-SIX dual wall to CROSS/BYPASS or an explicit short-support boundary.

Consequently this branch no longer has an unpaid “triangle lock.” The first essential missing implication here is now the genuinely disjointness-preserving one:

> **BT4-TRIANGLE-TWO-CROSS-SPLICE-v1.** In the four-vertex remainder state (3)--(5), when Lemma 2 supplies two distinct remainder exact-five witnesses for `T2 union B`, use their domination ladders and the exact cage/neutral-packing structure to choose compatible cross transitions with separated packed ports and disjoint remainder interiors, or else prove that ladder coalescence yields a strict smaller three-packing, a cycle in an exchanged remainder, or a SIX witness.

This is narrower than manufacturing a cross: two independent source-valid cross generators are already forced. A cross by itself, or even two generators whose realized paths coalesce, is not counted as two replacement cycles.

The target-level proof still also needs the general SIX closure and the other explicitly retained pinwheel/support-carried branches. No unsupported global closure is inserted here.

## Failure checks and nonclaims

- The theorem is only for the aligned four-remainder heavy-triangle boundary and uses every inherited hypothesis stated above.
- `P0` is a three-cycle packing, not four cycles; it is used only as a neutral minimum-packing exchange.
- The Lichiardopol--Pór--Sereni theorem is applied to the actual induced digraph `G=D-(T2 union B)`, not to an averaged or contracted graph.
- A degree-two vertex in `G` is an exact five-witness because the ambient outdegree is exactly seven.
- The two cross generators are distinct by witness vertex, but their realized domination paths are not asserted to be internally disjoint; that is precisely the next unpaid splice implication.
- The 2026 one-reversed-arc relaxation is never counted as a directed cycle.
- No computation was used.
- Full BT4 remains open and no novelty claim is made.

## Honest outcome

`ESSENTIAL_STEP_APPLIED`.

Before this run, the newest OTHER-account heavy-triangle result forced a clean opposite-cross pair for `|A|>=4` but left `|A|=3` as a genuine short-support boundary. After this run, that boundary is reduced source-validly to SIX or at least two remainder-supported exact-five/cross generators. The next work should attack their four-vertex-remainder collision geometry rather than reopen the triangle-size case.

Model self-report: `GPT-5.6 Sol`. Requested effort: maximum actually supported. Configured/provider reasoning effort and token/time telemetry: `UNKNOWN_NOT_EXPOSED` / null. Elapsed invocation includes repository and web I/O and is not reported as pure thinking time.
