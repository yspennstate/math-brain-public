# BT4 fleet01/B05 — inport triangle forces a neutral three-edge packed-cycle swap

Run: `20260922T043014Z-b05-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-INPORT-TRIANGLE-3SWAP-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and role

Target: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Digons are allowed in the source statement. This report works only after the team's inherited reduction to an oriented exact-outdegree-seven minimum counterexample and does not claim the target theorem.

B05 role: construct packing augmentations/exchanges from the shared deficient three-cycle packing and account for every affected vertex.

## Current team frontier consumed

Latest complete lead state actually used: fleet02/B04 run `20260922T031823Z-a02-b04-bt4-r11`, controlling frontier addendum candidate `SC+`, blob `28fe813aa044e57bbb3c6934a9ea76525bc04968`. Its live first obligation is to turn the canonical sink-cross/post-pivot geometry into a legal packing exchange, strict minimum-packing reduction, exchanged-remainder cycle, or fourth cycle.

Newest compatible OTHER-account input actually applied: fleet04/B06 run `20260922T041133Z-b06-bt4-r13`, candidate `BT4-R4-LOWFAN-INPORT-TRIANGLE-v1`, report blob `d95ac60508cb0a415c33106169d1527da385406f`. In the exact four-remainder, long-source F2 branch it proves the following data.

Work with a globally minimum packing `(H,S,U)` and old remainder

`R={x,y,d,c}`,

where `x` and `y` are distinct old-remainder sinks. Write consecutive vertices of `S` as

`p -> q -> s -> t -> ... -> p`,

with `|S|>=6`. The sink `x` has

`N+(x) intersect S={q,s}`,

and a unique source inport `p->x`. There is a unique inport `u in U -> x`, the omitted old-remainder vertex satisfies `c->x`, and in fact

`N^-(x)={p,u,c}`.

Moreover `{p,u,c}` induces a genuine directed triangle. The F2 profile gives

`q->y`, `q->d`, `q not->c`,

and the second sink satisfies

`N+(y) intersect S={s,t}`.

The heavy fan of `x` on `H` has size exactly three in the no-six sink state.

Named assigned-partner result also applied downstream: fleet02/B06 run `b06-20260922T032557Z-cd66631395ed`, candidate `BT4-SIX-SUPPORT-MENGER-v1`, report blob `a02d47570c19582e747b407734d90044124d3f60`. Its valid conclusion is that, at `|R|=4`, a cycle-supported SIX witness with the required heavy inport cannot remain a pure short-bypass obstruction: the branch gives a cross transition, a neutral exchange, or a target-packed-entering Menger linkage; if the heavy inport is absent, the lead's domination escape already gives the cross transition.

For the proof mechanism below I also use the source-valid `k=3` input already fixed by the team: minimum outdegree five gives three vertex-disjoint directed cycles. Equivalently, in a BT4 counterexample every directed cycle `K` has an external vertex with at least three outneighbors on `K`; otherwise deleting `K` leaves minimum outdegree at least five and supplies three cycles disjoint from `K`.

## Compact conditional end-to-end route

Assume BT4 false and enter the inherited oriented, arc-dominated, 3-vertex-strong exact-seven normal form with a globally minimum three-cycle packing and acyclic remainder. The lead's canonical sink argument and the post-pivot F2/F3 split reduce the four-remainder low-fan branch. The newest fleet04/B06 result reduces long F2 to the exact triangle/sink configuration above. The first missing exchange implication is therefore:

> turn the cross-packed inport triangle `{p,u,c}` into an actual globally minimum packing move, rather than leaving it as a single mixed cycle that intersects two packed cycles.

The theorem below does this without adding a linkage hypothesis.

## Lemma 1 — the inport triangle has a packed common predecessor

Let

`T = D[{p,u,c}]`.

Since `T` is a directed triangle, there is a vertex `v outside {p,u,c}` such that

`v->p`, `v->u`, `v->c`.                                          (1)

Moreover `v` lies on one of the three packed cycles `S,U,H`; it cannot lie in the old remainder.

### Proof

If no outside vertex had three outneighbors on the directed cycle `T`, deleting `T` would reduce every remaining outdegree by at most two. Since the ambient outdegree is exactly seven, `D-T` would have minimum outdegree at least five. The genuine `k=3` theorem would then give three pairwise vertex-disjoint directed cycles in `D-T`, and together with `T` these would be four disjoint directed cycles, contradiction. Thus (1) holds.

The only old-remainder vertices outside `T` are `x,y,d`. Both `x` and `y` are old-remainder sinks, so neither can send to the old-remainder vertex `c`. Hence neither is `v`.

If `v=d`, then (1), together with the F2 arc `q->d` and the support arc `p->q`, gives the directed triangle

`p -> q -> d -> p`.

This triangle is disjoint from `H union U`. Since `|S|>=6`, replacing `S` by this triangle gives a legal three-cycle packing of strictly smaller total order, contradicting global minimality. Hence `d` is impossible as well. Therefore `v` is packed. QED.

## Lemma 2 — localization on a light cycle

If `v in S`, then

`v=p^-`.

If `v in U`, then

`v=u^-`.

### Proof

The packed cycles are chordless. Thus an arc from one vertex of a packed cycle to another vertex on the same packed cycle must be its support arc. Since `v->p` when `v in S`, `p` is the successor of `v`; similarly `v->u` on `U`. QED.

## Lemma 3 — the three-step target is always available

Let `C` be the packed cycle containing `v`, and write successors on `C` as

`v^+, v^{++}, v^{+++}`.

Then

`x -> v^{+++}`.                                                   (2)

### Proof

There are three cases.

**Case S.** By Lemma 2, `v=p^-`. Hence

`v^+=p`, `v^{++}=q`, `v^{+++}=s`.

The known sink fan contains `x->s`, giving (2).

**Case U.** By Lemma 2, `v=u^-`. Hence

`v^+=u`, `v^{++}=u+`, `v^{+++}=u++`.

The exact two-fan at the direct `U`-inport gives `x->u++`, again (2).

**Case H.** Put

`F=N+(x) intersect H`, `|F|=3`.

For every `h in F`, (1) gives `v->c`; the long-F2 input gives `c->x`; hence

`v -> c -> x -> h`                                               (3)

is a directed path of length three whose internal vertices are outside `H`.

If `h=v` for some `h in F`, then `v->c->x->v` is a directed triangle disjoint from `S union U`. Global minimality implies `|H|<=3`; orientation gives `|H|=3`. In this case `v^{+++}=v`, and `x->v` is exactly (2).

Assume now `v notin F`. For each `h in F`, let `d_H(v,h)` be the positive forward distance from `v` to `h` on `H`. Replacing the forward `H` segment from `v` to `h` by (3) gives the directed cycle

`K_h = v -> c -> x -> h -> H[h,v]`,

which is disjoint from `S union U`. Its order is

`|K_h| = |H| + 3 - d_H(v,h)`.

Global minimality of `(H,S,U)` forces `|K_h|>=|H|`, hence

`d_H(v,h)<=3`                                                     (4)

for every `h in F`. The three fan vertices are distinct and do not equal `v`, so (4) forces

`F={v^+,v^{++},v^{+++}}`.

In particular `x->v^{+++}`. QED.

## Theorem — inport-triangle three-edge neutral swap

> **BT4-R4-INPORT-TRIANGLE-3SWAP-v1.** In the exact long-source F2 configuration above, there exists a packed cycle `C in {S,U,H}` and a vertex `v in C` such that the forward three-edge support segment
>
> `v -> v^+ -> v^{++} -> v^{+++}`
>
> can be replaced by
>
> `v -> c -> x -> v^{+++}`.
>
> The resulting cycle
>
> `C' = v -> c -> x -> v^{+++} -> C[v^{+++},v]`                  (5)
>
> is genuinely directed, has `|C'|=|C|`, is disjoint from the other two packed cycles, and therefore yields another globally minimum three-cycle packing. The new remainder is exactly
>
> `R'={y,d,v^+,v^{++}}`.                                         (6)
>
> If `D[R']` contains a directed cycle, then the new three-cycle packing plus that remainder cycle is a four-cycle packing and BT4 is closed in this branch. Otherwise `R'` is acyclic and (5) is a genuine size-neutral state transition.

### Proof

Lemma 1 supplies a packed `v` with (1). Thus `v->c`. The long-F2 input gives `c->x`, and Lemma 3 gives `x->v^{+++}`. Hence the three-edge detour in (5) is directed.

The old support segment

`v -> v^+ -> v^{++} -> v^{+++}`

has three edges and exactly two internal vertices. The replacement path

`v -> c -> x -> v^{+++}`

also has three edges and exactly two internal vertices. Since `c,x` are old-remainder vertices and the remainder is disjoint from the packing, the replacement is simple and disjoint from the two untouched packed cycles. It removes exactly `v^+,v^{++}` from the packing and inserts exactly `c,x`. Therefore `|C'|=|C|` and the total packed order is unchanged. The uncovered vertices are precisely the two old remainder vertices not consumed, namely `y,d`, together with the two released support vertices `v^+,v^{++}`, proving (6).

If the induced new remainder contains a directed cycle, it is disjoint from `C'` and the two untouched packed cycles, producing four disjoint directed cycles. In a counterexample this cannot happen, so the new remainder is acyclic. QED.

## Exact specialization of the swap

The theorem is concrete in all three possible locations of the common predecessor.

- If `v=p^- in S`, then the swap is

  `p^- -> c -> x -> s -> S[s,p^-]`,

  and it frees exactly `{p,q}`. Thus the new remainder is `{y,d,p,q}`. The known arcs `p->q`, `q->y`, `q->d` are retained. In particular, a return `d->p` is impossible already in the old packing, because it would create the strict replacement triangle `p->q->d->p`.

- If `v=u^- in U`, then the swap is

  `u^- -> c -> x -> u++ -> U[u++,u^-]`,

  and it frees exactly `{u,u+}`.

- If `v in H`, then either `|H|=3` and the replacement is the triangle `v->c->x->v`, or the heavy fan of `x` is forced to be exactly the three consecutive successors `{v^+,v^{++},v^{+++}}`, and (5) frees the first two of them.

Thus the previously awkward mixed inport triangle is never a terminal object: it always certifies a byte-exact analogue of a directed 3-switch at the packing level, with complete vertex accounting.

## Application of the assigned partner's SIX result

The neutral swap preserves `|R|=4` and preserves global minimum total packed order. Re-run the campaign's pair-deletion alternative on the new packing. If a cycle-supported SIX witness appears, the assigned partner fleet02/B06 `BT4-SIX-SUPPORT-MENGER-v1` applies in its proved scope: absence of a heavy inport already exports a cross transition, while presence of the inport gives the corrected SIX bypass tax and, at four remainder vertices, reduces the pure-remainder Menger branch to a neutral exchange or a target-packed-entering linkage. Therefore the 3-swap does not create a new independent short-bypass SIX obstruction; it feeds directly back into the common cross/linkage/neutral frontier.

If no SIX witness appears, the no-six sink machinery applies again to the new acyclic four-vertex remainder. Hence the exact inport-triangle branch has been converted into a controlled neutral transition rather than left outside the team's state graph.

## Updated conditional end-to-end argument

The current `|R|=4` low-fan route can now be written:

1. Enter the inherited exact-seven oriented minimum-packing normal form.
2. A remainder sink gives the canonical no-six `(3,2,2)` sink state and the neutral source pivot.
3. The post-pivot low-fan analysis gives F3 or F2. F3 is already reduced to a three-vertex source equality configuration. For F2 with `|S|>=6`, fleet04/B06 gives the exact inport triangle `{p,u,c}` and second sink `y`.
4. This report turns that triangle into the neutral three-edge packed-cycle swap (5), preserving total packing size and giving the exact new remainder (6). A cyclic new remainder immediately gives the fourth cycle.
5. If the new remainder is acyclic, pair-deletion restarts on a strictly reconfigured minimum packing. Any cycle-supported SIX is funneled by the assigned partner result into cross/neutral/packed-linkage geometry; otherwise the canonical no-six sink interface restarts.

The first remaining implication is therefore no longer "make the inport triangle actionable." It is:

> **R4-3SWAP-ORBIT-CLOSURE.** Prove that the finite orbit of four-remainder globally minimum packings generated by the canonical sink pivots and the new three-edge swap cannot avoid a cyclic exchanged remainder, a strict packing reduction, the partner's target-packed linkage/cross output, or a legal two-cycle replacement indefinitely.

This is an orbit/compatibility problem, not another missing local exchange.

## Failure checks and nonclaims

- The argument uses a genuinely directed triangle and the genuine minimum-outdegree-five `k=3` theorem; no one-reversal relaxed cycle is counted.
- The external three-hit witness is forced by deleting the actual triangle `T`, not by an average-degree heuristic.
- The old-remainder candidate `d` is excluded by an explicit strict replacement triangle using the actual F2 arc `q->d`.
- Chordlessness is used only to localize a packed common predecessor on `S` or `U` to the immediate predecessor of the corresponding port.
- In the `H` case, consecutive fan targets are derived from three separate legal packing comparisons; they are not assumed.
- A neutral swap is not a fourth cycle. BT4 remains open.
- No finite computation, benchmark material, edge-disjoint surrogate, private unrelated data, or novelty inference is used.

## Honest outcome

`ESSENTIAL_STEP_APPLIED`.

New essential result: the exact long-F2 inport triangle always forces an explicit size-neutral three-edge packed-cycle swap consuming the old sink pair `{c,x}` and releasing two consecutive support vertices. This directly pays the local exchange obligation for that triangle and reduces the residual work to closure of the resulting finite neutral orbit/common linkage frontier.
