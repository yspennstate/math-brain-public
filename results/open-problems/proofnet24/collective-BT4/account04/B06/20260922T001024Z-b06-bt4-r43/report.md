# BT4 account04/B06 — missing-arc saturation and forced-exit refinement

Run: `20260922T001024Z-b06-bt4-r43`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Candidate: `BT4-MCR-v2`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and inherited candidate

The target is the k=4 Bermond-Thomassen statement: every finite loopless digraph D with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four vertex-disjoint directed cycles. Opposite arcs and directed digons are allowed by the source problem.

Current primary source: Bessy, Muis, Sereni, Steiner and Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract states that the exact conjecture remains unresolved for k>=4 and proves a relaxation in which each packed cycle may instead become directed after reversing one arc. Nothing below substitutes that relaxation for a genuine directed cycle.

This run consumed the exact other-account result `account01/B04`, candidate `BT4-MCR-v1`, canonical report commit `8a71d11efa2a3110db78c39684ea4c9cce03a28b`. I use its proved reductions only in their stated scope. Thus, if D is a counterexample chosen first vertex-minimal and then arc-maximal, then:

1. D has no digon and is strongly connected.
2. D is not a tournament.
3. D has three vertex-disjoint directed cycles C1,C2,C3 leaving at least three vertices uncovered. Choose such a packing minimizing total covered vertices S, and put R=V(D)\S. Then D[R] is a DAG and every Ci is chordless.
4. If x is a sink of R, all d+(x)>=7 outgoing arcs enter C1 union C2 union C3, so for some packed cycle Ch the fan size mh=|N+(x) intersect V(Ch)| is at least three.
5. The one-vertex exchange lemma from v1 implies that when mh>=3, no vertex of Ch sends an arc to x.
6. Its path-fan lemma says that if a directed path from a vertex of Cj to x has length L and all internal vertices lie in R, then mj:=|N+(x) intersect V(Cj)| <= L+1.

The v1 unpaid arrow was to force a short return from a heavy cycle to x, or an equivalent disjointness-preserving global exchange. The present run attacks exactly that arrow by exploiting arc-maximality at a missing arc.

## Lemma 8 — missing-arc saturation gives a fan-avoiding return path

Let x,b be nonadjacent vertices of D, meaning neither x->b nor b->x is an arc. Then there exist three vertex-disjoint directed cycles K1,K2,K3 in D and a directed path

    P: b = p0 -> p1 -> ... -> pL = x

in D, vertex-disjoint from K1 union K2 union K3, such that

    (V(P) \ {x}) intersect N+(x) = emptyset.

### Proof

Add the missing arc x->b. The new digraph has the same vertex set, still has minimum outdegree at least seven, and has one more arc than D. By arc-maximality of D among vertex-minimal counterexamples, D+x->b has four vertex-disjoint directed cycles.

At least one of those cycles uses the new arc, since otherwise D itself would already contain four disjoint directed cycles. At most one can use it. Call that cycle Q. Removing x->b from Q leaves a directed path P in D from b to x. The other three cycles K1,K2,K3 lie entirely in D and are vertex-disjoint from P.

Suppose some y in V(P)\{x} satisfied x->y in D. Then x->y followed by the suffix of P from y to x would be a directed cycle in D. It is vertex-disjoint from K1,K2,K3, producing four disjoint directed cycles in D, contradiction. Hence P avoids every outneighbor of x except its endpoint x. QED.

This conclusion is stronger than mere strong connectivity: the return path obtained from saturation is forced to avoid the entire out-neighborhood of x.

## Corollary 9 — gateway bound for a sink-heavy fan

Retain the minimum-total packing C1,C2,C3 and let x be a sink of R. Let Ch be heavy with mh>=3. For every b in V(Ch)\N+(x), Lemma 5 of v1 gives b not->x, while b notin N+(x) gives x not->b. Hence b and x are nonadjacent, and Lemma 8 applies.

For the resulting saturation path P and cycles K1,K2,K3, the absence of b->x implies |V(P)|>=3. Consequently K1,K2,K3 leave at least three vertices uncovered, so the global minimum-total choice of C1,C2,C3 gives

    |S| <= |K1|+|K2|+|K3| <= |V(D)|-|V(P)|.

Since |R|=|V(D)|-|S|,

    |V(P)| <= |R|.

Let c be the last vertex of S on P, and suppose c lies on Cj. By definition of c, every internal vertex of the suffix P[c,x] lies in R. Lemma 8 also gives c notin N+(x). If L is the length of that suffix, then L<=|V(P)|-1<=|R|-1. Applying the v1 path-fan lemma to Cj and x yields

    mj = |N+(x) intersect V(Cj)| <= L+1 <= |R|.

Thus every missing-arc saturation path started on a heavy cycle has a final old-packing gateway Cj whose x-fan has size at most |R|.

In particular, if mh>|R|, no such saturation path can have Ch as its final old-packing gateway. Every one of these returns must make its final departure into R from one of the other two packed cycles. This is a genuine structural reduction, not yet a contradiction.

## Lemma 10 — boundary blocking forces an exit arc from the old cycle

Use the path P from Lemma 8 and let c be its last vertex in S, with c in Cj. Let p be the predecessor of c on the directed cycle Cj. Suppose p is an outneighbor of x, i.e. x->p is an arc.

Then p lies on one of K1,K2,K3. Moreover the K-cycle containing p must leave Cj immediately from p by an arc whose head lies outside Cj.

### Proof

Because Lemma 8 makes P avoid N+(x), p is not on P. Suppose p were also absent from K1 union K2 union K3. Then

    x -> p -> c, followed by the suffix P[c,x],

is a directed cycle in D. It is disjoint from K1,K2,K3: p is absent from them by assumption and the rest of the new cycle lies on P, which is disjoint from them. This would again give four disjoint directed cycles in D, contradiction. Therefore p belongs to one of the K-cycles.

The old cycle Cj is chordless by the minimum-total packing choice, so the only out-neighbor of p inside V(Cj) is its successor c. But c lies on P and therefore is unavailable to every K-cycle. The K-cycle containing p must therefore leave Cj from p via an outgoing arc to a vertex outside Cj. QED.

This converts a local boundary pattern at the final gateway into a forced, disjointness-compatible exit used by the replacement packing. It is exactly the kind of object needed for a two-cycle splice; unlike an average degree count, it preserves the actual four-cycle certificate supplied by arc-maximality.

## Conditional end-to-end chain after this run

The current candidate is now:

1. Apply the proved v1 minimal-counterexample reductions and choose the minimum-total 3-packing.
2. Choose a sink x of R and a heavy cycle Ch with mh>=3.
3. For any b in Ch\N+(x), use missing-arc saturation to obtain a fan-avoiding return path plus a disjoint replacement 3-packing.
4. The path has at most |R| vertices, and its final old-cycle gateway Cj has mj<=|R|.
5. If the predecessor of that gateway on Cj belongs to N+(x), the replacement packing is forced to use an immediate exit arc from that predecessor.
6. **Remaining unpaid arrow:** combine the t=2 deletion witnesses (which send at least five arcs into each chosen pair of packed cycles) with Steps 3-5 to force either
   - a return whose final gateway is the original heavy cycle with length at most mh-2, contradicting the v1 path-fan inequality, or
   - two compatible forced exits that splice the old cycles/replacement packing into four genuinely directed vertex-disjoint cycles.

I do not have a proof of Step 6. In particular, strong connectivity alone does not identify the final gateway, and the t=2 five-fan count by itself does not guarantee that the relevant predecessor belongs to N+(x). Those are retained as explicit obligations rather than hidden assumptions.

## Adversarial checks

- Lemma 8 does not assume the replacement K-cycles avoid all outneighbors of x; only the saturation path P is proved to do so.
- The path-fan lemma is applied only to the suffix beginning at the last old-packing vertex c, ensuring every internal suffix vertex is genuinely in R.
- The inequality |V(P)|<=|R| uses the global minimum-total condition only after verifying that K1,K2,K3 leave at least three vertices uncovered; this follows from |V(P)|>=3.
- No edge-disjoint surrogate is used: every packing in the argument is vertex-disjoint.
- No claim is made that `BT4-MCR-v2` proves BT4 or that the lemmas are novel in the literature.

## Outcome

`ESSENTIAL_STEP_APPLIED`. The inherited first missing implication has been sharpened by a new arc-maximality mechanism: every suitable missing arc yields a return path avoiding the sink's full out-neighborhood, a bounded final gateway, and, under an explicit boundary condition, a forced exit used by the replacement packing. The arbitrary-order k=4 theorem remains open in this candidate because the final t=2-witness-to-splice implication is not proved.
