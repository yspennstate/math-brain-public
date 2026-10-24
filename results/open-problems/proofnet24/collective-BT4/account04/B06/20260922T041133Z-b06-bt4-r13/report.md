# BT4 account04/B06 — low-fan collapse to an inport triangle and a second sink port

Run: `20260922T041133Z-b06-bt4-r13`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-LOWFAN-INPORT-TRIANGLE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and current source boundary

The target is the genuine `k=4` Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven has four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem, hence directed digons count.

The current primary source boundary remains Stéphane Bessy, Matthijs Muis, Jean-Sébastien Sereni, Raphael Steiner and Sebastian Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948, submitted 13 August 2026. Its abstract explicitly says the genuine conjecture remains unresolved for every `k>=4`; its theorem at threshold `2k-1` allows a cycle that becomes directed after reversing one arc. No such relaxed cycle is counted below.

The inherited lower-`k` input is Nicolas Lichiardopol, Attila Pór and Jean-Sébastien Sereni, *A Step toward the Bermond-Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992, DOI `10.1137/080715792`: minimum outdegree five forces three vertex-disjoint directed cycles, and the strengthened `k=2` theorem allows all vertices to have outdegree at least three except at most two vertices of outdegree two.

## Exact team state consumed

Latest complete team-lead state actually read:

- account02/B04 `20260922T031823Z-a02-b04-bt4-r11`, primary report blob `17d49d472779d5304d30b93c07ce89c289ab20d1`;
- controlling frontier addendum blob `28fe813aa044e57bbb3c6934a9ea76525bc04968`.

The frontier addendum is controlling. It supersedes the older globally-no-cross residual: every acyclic-remainder sink already yields a canonical packed-to-packed cross. The current lead interface is `SC+`: after the exact neutral source pivot, use the resulting sink-cross / x-free cross geometry to obtain a legal two-cycle replacement, a strict globally-minimum packing reduction, a directed cycle in an exchanged remainder, or a fourth disjoint directed cycle.

Named OTHER-account partner result actually applied:

- account01/B04 `BT4-MCR-v5-sink-cross-collapse`, run `20260922T024418Z-b04-bt4-r11`, report blob `bbf3afa52d8d0587ae5e210eecaacb7017ac672e`.

Its exact theorem used here is: in the inherited normal form every sink `x` of the acyclic remainder has a direct packed inport `p in S -> x`; the source fan satisfies `m_S(x)<=2`; a heavy target cycle `H` has fan at least three and no vertex of `H` sends to `x`; and in global `NO-SIX` the sink fan pattern is exactly `(3,2,2)` after relabeling. In that branch `m_S(x)=2`, and the path-fan equality gives

`N+(x) intersect S = {p+,p++}`.                                 (1)

Compatible frontier inputs also read and used in their proved scope:

- account04/B04 `BT4-R4-FREED-PROFILE-v1`, run `account04-B04-20260922T034321Z-BT4-r12`, which after the neutral source pivot reduces the four-remainder post-pivot no-new-heavy-cross state to exact profiles `F2=(2,2,1,2)` and `F3=(2,1,1,3)`;
- account01/B06 `BT4-R4-POSTPIVOT-TWOARM-SATURATION-v1`, run `20260922T033708Z-b06-bt4-r12`, plus its basin refinement, which identifies the exact four-remainder post-pivot strict-arm geometry and shows that long source cycles force multiple old-remainder sink basins.

No peer outcome label is used as proof. Only the source-bound statements above are imported.

## Inherited normal form and notation

Assume BT4 false. Work in the campaign's inherited minimum-counterexample normal form. Thus `D` is oriented, every vertex has outdegree exactly seven, `(H,S,U)` is a three-cycle packing of globally minimum total order, the remainder

`R = V(D) \ (V(H) union V(S) union V(U))`

is nonempty and acyclic, the packed cycles are chordless, every arc is dominated, and `D` is 3-vertex-strong.

Here an arc `a->b` being dominated means that there is a vertex `d` with both `d->a` and `d->b`. The inherited 3-vertex-strongness implies in particular

`d^-(v) >= 3`                                                     (2)

for every vertex `v`: otherwise deleting all in-neighbors of `v`, fewer than three vertices, leaves `v` unreachable.

Take an old remainder sink `x`. In global `NO-SIX` choose its canonical source inport

`p in S -> x`.

Write consecutive vertices of `S` as

`p -> q -> s -> t -> ... -> p`,                                 (3)

so by (1)

`q=p+`, `s=p++`, and `x->q,x->s`.                               (4)

The neutral source pivot is

`S* = p -> x -> s -> S[s,p]`,                                   (5)

which frees `q` and changes the remainder to

`R* = (R-{x}) union {q}`.                                       (6)

The lead's equality-completion theorem makes `R*` acyclic and preserves the total packing size.

This run specializes to the lead's exact four-remainder branch

`|R|=|R*|=4`.                                                    (7)

Write

`R={x,a,b,c}`                                                    (8)

as needed below.

## Imported F2/F3 post-pivot profiles

Account04/B04 proves the following exact split for the freed vertex `q` after (5). Let

`e=d^+_{R*}(q)`.

The vertex `q` has exactly one outneighbor on `S*`, namely `s`, and hence exact outdegree seven gives

`d^+_{H union U}(q)=6-e`.                                       (9)

The SIX or heavy-return-cross outputs already leave the low-fan branch. If neither occurs, only these two profiles remain:

- **F2:** `e=2`, the packed fans are `2+2`, hence relative to `(H,U,S*,R*)` the exact profile is `(2,2,1,2)`. Thus, after naming the old remainder as in (8), we may take

  `q->a`, `q->b`, `q not->c`.                                   (10)

  The imported theorem also says either `c->q` or a packed inport from `H union U` enters `q`.

- **F3:** `e=3`, the packed fans are `2+1`, profile `(2,1,1,3)`, and

  `q->a,q->b,q->c`.                                             (11)

  There is also a packed inport from `H union U` into `q`.

The point of the next two lemmas is that the old sink `x`, which is absent from `R*` but still has the ambient arc `x->q`, forces much more than these reverse-inport alternatives.

## Lemma 1 — F3 forces a three-vertex source cycle

Assume F3. Then

`|S|=3`.                                                         (12)

Moreover at least one old remainder vertex `r in {a,b,c}` satisfies `r->x`, and therefore

`x -> q -> r -> x`                                              (13)

is a directed triangle disjoint from `H union U`. Since `|S|=3`, this triangle is a size-neutral source replacement.

### Proof

By F3, (11) holds, while the old sink fan gives the ambient arc `x->q` from (4).

If some `r in {a,b,c}` sends to `x`, then (13) is a directed triangle. It is disjoint from `H` and `U`, so replacing `S` by this triangle gives a legitimate three-cycle packing. Global minimality of `(H,S,U)` yields

`|S| <= 3`.                                                      (14)

Because `D` is oriented, every directed cycle has order at least three. Hence `|S|=3`.

It remains to show that such an `r` must exist. Suppose none of `a,b,c` sends to `x`. Since `x` is an old remainder sink, it has no outneighbor in `R`; under the present supposition it also has no old-remainder in-neighbor.

The partner theorem gives no inport from the heavy cycle `H` because `m_H(x)=3`. On either light cycle the fan is two. A direct light-cycle inport `v->x` is a path of length one into a fan of size two, so equality-completion applies. It says that the two fan targets are exactly the two successors `{v+,v++}`. A proper consecutive two-vertex block of a directed cycle has a unique predecessor. Therefore:

- on `S`, the only direct inport to `x` is `p` because its fan block is `{q,s}`;
- on `U`, there is at most one direct inport to `x`.

Thus `d^-(x)<=2`, contradicting (2). Hence some old remainder vertex enters `x`, and the first paragraph proves (12)--(13). QED.

### Significance

The post-pivot F3 branch is not an arbitrary `(2,1,1,3)` collision state. It can occur only when the original source cycle is a directed triangle, and it simultaneously supplies another directed triangle through `x`, `q` and an old remainder vertex. Any attempted universal `SC+` splice may therefore treat F3 as a genuinely small-source equality configuration rather than a long-cycle linkage problem.

## Lemma 2 — long-source F2 forces an exact inport triangle

Assume F2 and suppose

`|S|>=4`.                                                        (15)

Then, after naming `a,b` as the two vertices in (10), neither `a` nor `b` sends to `x`. The omitted old remainder vertex necessarily satisfies

`c->x`,                                                          (16)

and there is a unique direct inport

`u in U -> x`.                                                   (17)

Consequently the complete in-neighborhood of `x` is exactly

`N^-(x)={p,u,c}`.                                                (18)

Furthermore the three vertices `{p,u,c}` form a directed triangle.

### Proof

If `a->x`, then `x->q->a->x` is a directed triangle disjoint from `H union U`; global minimality would give `|S|<=3`, contradicting (15). The same argument excludes `b->x`.

As in Lemma 1, there is no inport to `x` from the heavy cycle `H`. On `S`, equality-completion makes `p` the unique direct inport. On `U`, the fan is two, so there is at most one direct inport.

Since the only possible old-remainder in-neighbor now left is `c`, the indegree lower bound (2) forces both possibilities to occur: `c->x`, and a direct `U`-inport `u->x`. There can be no further in-neighbor by the uniqueness just established, giving (18). Equality-completion at `u->x` also records the exact `U` fan block

`N+(x) intersect U = {u+,u++}`.                                 (19)

Now use arc domination on the three arcs into `x`:

`p->x`, `u->x`, `c->x`.                                        (20)

A dominator of `v->x` must itself be an in-neighbor of `x`; by (18) it is one of the other two vertices of `{p,u,c}`, and it sends an arc to `v`. Hence, in the oriented subdigraph induced by `{p,u,c}`, every vertex has indegree at least one.

An oriented graph on three vertices has at most three arcs. The sum of the three induced indegrees is therefore at most three, while the previous paragraph makes it at least three. Thus it is exactly three and every induced indegree equals one. The only orientation of the complete three-vertex graph with indegree one at every vertex is a directed triangle. QED.

### Significance

This is substantially stronger than the imported F2 conclusion "`c->q` or a packed inport enters `q`". In the long-source branch the old sink itself rigidly identifies:

1. the unique old-remainder inport `c->x`;
2. the unique other-light inport `u->x`;
3. the exact shifted `U` fan block (19); and
4. a genuine directed triangle on one source port, one other-light port and one remainder vertex.

The triangle is a real cross-packed directed cycle, not an edge-disjoint or near-directed surrogate. It is not by itself a four-cycle packing, because it consumes one vertex of each light packed cycle.

## Lemma 3 — if F2 has a long source, a second sink appears at an adjacent source port

Assume F2 and strengthen (15) to

`|S|>=6`.                                                        (21)

Then at least one of `a,b` is a second sink of the old remainder `D[R]`. Call such a sink `y`. Because F2 gives `q->a,q->b`, we have a direct adjacent source inport

`q in S -> y`.                                                   (22)

Global `NO-SIX` then forces

`m_S(y)=2`,                                                      (23)

and equality-completion gives the shifted fan block

`N+(y) intersect S = {s,t}`.                                    (24)

Hence the old packing has two distinct remainder sinks with two distinct adjacent direct source ports:

`p -> x`,  `q -> y`,                                            (25)

and their source fan blocks are

`N+(x) intersect S={q,s}`,  `N+(y) intersect S={s,t}`.          (26)

Each sink separately has a canonical length-two cross to one of the other packed cycles. The two canonical cross interiors are automatically disjoint because they are `{x}` and `{y}`.

### Proof

By Lemma 2, `c->x`, while neither `a` nor `b` sends directly to `x`.

Suppose one of `a,b`, say `a`, has any directed path in the old remainder to `x`. Because `R` has four vertices, a shortest `a`-to-`x` path has edge length at most three. Concatenating it with the ambient arcs

`x->q->a`                                                       (27)

produces a simple directed cycle whose only packed vertex is `q` and whose order is at most five. It is disjoint from `H union U`. Replacing `S` by this cycle contradicts global minimality under (21). Therefore neither `a` nor `b` can reach `x` inside `D[R]`.

Since `c->x`, neither `a` nor `b` can reach `c` either. The old remainder is a finite DAG. Starting from either `a` or `b` and following outgoing remainder arcs must terminate at a sink; the terminal sink cannot be `x` or `c`. Thus at least one of `{a,b}` is itself a sink. Call it `y`.

F2 gives `q->y`. The partner's direct path-fan bound applied to this length-one `S`-to-`y` path gives `m_S(y)<=2`. If `m_S(y)<=1`, then, because `y` is an old remainder sink of exact outdegree seven, at least six of its outgoing arcs hit `H union U`. That is a remainder-supported SIX witness for the pair `{H,U}`, contradicting the global `NO-SIX` hypothesis. Hence (23) holds.

Length one into a fan of size two is equality in the path-fan bound, so equality-completion makes its targets the two consecutive successors of the packed start `q`. In the notation (3), they are exactly `{s,t}`, proving (24). Distinctness in (25) is clear because `p!=q` and `x!=y`. Each sink has a canonical cross by the partner theorem, and their interiors are the distinct singleton remainder vertices `x` and `y`. QED.

### Why this is a useful splice interface

The long F2 branch is no longer a generic reverse-inport wall. It contains a **two-sink, adjacent-two-port ladder**:

- first sink port: `p->x`, source targets `{q,s}`;
- second sink port: `q->y`, source targets `{s,t}`;
- both sinks export canonical length-two crosses with disjoint interiors;
- the first sink simultaneously has the inport triangle `{p,u,c}` from Lemma 2.

This is the first configuration in the current low-fan frontier where two canonical sink-cross interiors are forced disjoint without an auxiliary Menger choice.

## Updated four-remainder low-fan case tree

Combining the lead, account04/B04, the named account01/B04 partner, and Lemmas 1--3 gives the following exact refinement of the four-remainder post-pivot `SC+` branch.

After the neutral source pivot, one has one of the already-exported branches:

1. **SIX** at the freed vertex;
2. **RETURN-CROSS** from a heavy freed fan;
3. **F3**, but Lemma 1 forces `|S|=3` and a neutral triangle `x->q->r->x`;
4. **F2 with `|S|<=5`**, a genuinely small-source residual;
5. **F2 with `|S|>=6`**, where Lemmas 2--3 force both:
   - the exact inport triangle on `{p,u,c}`; and
   - a second old remainder sink `y` with adjacent source port `q->y`, shifted fan `{s,t}`, and a second canonical cross whose remainder interior is disjoint from the first.

Thus the former F2/F3 low-fan wall has no unrestricted large-source geometry left at `|R|=4`.

## Compact conditional end-to-end k=4 argument after this step

The current campaign proof can be stated compactly as follows.

Assume a counterexample. The inherited reductions give the oriented exact-seven, 3-vertex-strong, arc-dominated minimum-packing normal form. Pick a sink of the acyclic remainder. The account01/B04 theorem gives a canonical direct source inport and sink cross. Source fan at most one enters the SIX interface; source fan two gives the exact neutral pivot. The lead's post-pivot argument and account04/B04 reduce the four-remainder no-new-heavy-cross state to F2/F3. Lemmas 1--3 above then reduce those profiles to short-source equality geometry or to the explicit two-sink adjacent-port state.

Accordingly, in the `|R|=4` part of `SC+`, the first genuinely unpaid implication can now be taken to be:

> **R4-TWOSINK-SPLICE.** In the long-source F2 configuration of Lemma 3, use the two adjacent source ports `p->x`, `q->y`, their shifted two-fan blocks `{q,s}`, `{s,t}`, the disjoint singleton sink-cross interiors `{x},{y}`, and the inport triangle `{p,u,c}` to construct either (i) two legal vertex-disjoint replacement cycles for two packed cycles, (ii) a strict reduction of the globally minimum three-packing, (iii) a directed cycle in an exchanged remainder, (iv) a SIX state, or (v) a fourth directed cycle disjoint from the three packed cycles.

The small-source residual `|S|<=5`, the separate SIX closure, and the lead's larger-remainder branches remain explicit obligations. An opposite or parallel cross pair is not automatically two replacement cycles, so that splice step is not skipped here.

## Failure and adversarial checks

- The source problem allows digons. Orientation is used only after the inherited minimum-counterexample reduction discharges the digon case using the genuine `k=3` theorem.
- F3 uses `e=3`, hence `q` really dominates all three old remainder vertices. Without that exact profile Lemma 1 is false as stated.
- In Lemma 2, `|S|>=4` is essential only to exclude the immediate directed-triangle replacement. The indegree argument then uses genuine 3-vertex-strongness, not an assumed minimum indegree theorem independent of the inherited reduction.
- The light-cycle inport is unique because a direct path of length one into a two-fan is an equality case and fixes a consecutive two-target block; this is not inferred merely from chordlessness.
- The domination-to-triangle argument uses the exact inherited statement that every arc is dominated. It does not assume every pair has a common predecessor.
- Lemma 3 uses `|S|>=6` because an old-remainder path of length at most three together with `x->q` makes a source replacement of order at most five. At source order five this can be neutral rather than strict, so that boundary is deliberately retained in the small-source residual.
- The directed triangle `{p,u,c}` is one cycle, not a two-cycle replacement. The two canonical sink crosses likewise do not yet supply two disjoint replacement cycles because their packed target segments may collide.
- No finite-order computation, edge-disjoint surrogate, near-directed cycle, average-degree replacement, or novelty inference is used.
- No full BT4 proof is claimed.

## Honest classification

`ESSENTIAL_STEP_APPLIED`.

New essential result: in the exact four-remainder low-fan post-pivot branch, F3 forces the original source cycle to have order three; long-source F2 forces an exact directed inport triangle around the old sink; and if the source has order at least six then a second old remainder sink occurs at the adjacent source port with a shifted two-fan block, giving two canonical sink-cross interfaces with automatically disjoint remainder interiors.

BT4 remains open because `R4-TWOSINK-SPLICE`, the source-order-at-most-five residual, the SIX interface and the larger-remainder interfaces are not yet closed.
