# BT4 fleet01/B04 — minimal-counterexample reductions and exact cycle-loss accounting

Run: `20260921T234516Z-b04-8fd1d4`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target

For every finite loopless digraph D with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven, prove that D contains four vertex-disjoint directed cycles. Opposite arcs are allowed in the source problem and a directed digon counts as a directed cycle.

Current primary source checked: Bessy, Muis, Sereni, Steiner and Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (2026-08-13), https://arxiv.org/abs/2608.12948 . The paper states the exact Bermond-Thomassen conjecture is known for k<=3 and remains unresolved for every k>=4; its new theorem at threshold 2k-1 gives k vertex-disjoint **near-directed** cycles, not k directed cycles. Tournament cases are known and are used below only as an input.

The assigned partner is `fleet02/B05`. At the time this argument was derived, no finalized post-reallocation BT4 artifact from that partner was yet available in the coordination repository; its newest observed run artifact predated the collective-research directive. I therefore reconstructed the smallest source-exact candidate and did not wait.

## Candidate BT4-MCR-v1

Assume a counterexample exists. Choose D first with minimum n=|V(D)| and, subject to n, with maximum |A(D)|. The following deductions are valid for this D.

### Lemma 1 — D has no digon

If x<->y is a directed 2-cycle, delete x and y. Every remaining vertex loses at most two outgoing neighbors, hence

    delta^+(D-{x,y}) >= 5.

The known k=3 Bermond-Thomassen theorem then gives three vertex-disjoint directed cycles in D-{x,y}; together with the digon xy this gives four in D, contradiction. Thus D is oriented: between every pair there is at most one of the two possible directions.

### Lemma 2 — D is strongly connected

If D is not strongly connected, take a sink strongly connected component S. No arc leaves S, so every vertex of S has all at least seven outneighbors inside S and

    delta^+(D[S]) >= 7.

Because S is a proper induced subdigraph, vertex-minimality gives four disjoint directed cycles in D[S], contradiction. Hence D is strongly connected.

### Lemma 3 — D contains three disjoint directed cycles leaving at least three vertices uncovered

The Bermond-Thomassen conjecture is known for tournaments, so D is not a tournament. Since D is oriented, there are nonadjacent vertices x,y. Add the missing arc x->y. The resulting digraph has the same vertex set, minimum outdegree at least seven, and more arcs. Arc-maximality of D implies D+x->y has four vertex-disjoint directed cycles.

At least one of those four cycles uses x->y, otherwise D itself already has four. Since y->x is absent, that cycle has length at least three. The other three cycles lie entirely in D and therefore cover at most n-3 vertices. Thus D contains a packing C1,C2,C3 of three vertex-disjoint directed cycles with at least three vertices outside the packing.

Among all such three-cycle packings, choose C1,C2,C3 minimizing total covered vertices. Let

    S = V(C1) union V(C2) union V(C3),   R = V(D) \ S.

Then |R|>=3.

### Lemma 4 — every packed Ci is chordless as a directed cycle

If Ci contains an extra arc between two nonconsecutive vertices, that chord plus one of the two directed sections of Ci forms a strictly shorter directed cycle. Replacing Ci by this shorter cycle preserves disjointness from the other two cycles and decreases |S|, contradicting minimality. Therefore the induced digraph on V(Ci) has exactly the directed cycle arcs.

### Lemma 5 — R is acyclic

If D[R] contained a directed cycle, it together with C1,C2,C3 would form four vertex-disjoint directed cycles. Hence D[R] is a DAG. In particular R has a sink.

## Exact deletion obstruction hierarchy

Let t in {1,2,3}. Take t vertex-disjoint directed cycles with union S and nonempty remainder T=V(D)\S. If every v in T retained

    d^+_{D-S}(v) >= 2(4-t)-1,

then the already-known cases k=4-t (namely k=3,2,1) would supply 4-t disjoint directed cycles in D-S, and together with the t kept cycles would give four in D. Therefore, in a BT4 counterexample, for every such chosen t-cycle set there exists v outside S with

    d_D^+(v) - |N_D^+(v) intersect S| <= 6-2t,

hence

    |N_D^+(v) intersect S| >= d_D^+(v)-(6-2t) >= 2t+1.

So:

- t=1: some external witness has residual outdegree <=4 and sends at least 3 arcs into the selected cycle.
- t=2: some external witness has residual outdegree <=2 and sends at least 5 arcs into the two selected cycles.
- t=3: some external witness has residual outdegree 0 and sends all its outgoing arcs into the three selected cycles; it has at least 7 such arcs.

For a directed triangle C, the t=1 witness can hit at most all three vertices of C. Consequently it must have d_D^+=7 and dominate every vertex of C. Thus every directed triangle in a minimal counterexample has an external degree-exact-seven vertex dominating the triangle.

## Lemma 6 — one-vertex exchange geometry

Fix a packed directed cycle Ci of length r and x in R. Write

    A = N_D^+(x) intersect V(Ci).

Suppose b in V(Ci) has an arc b->x. For a in A, combine b->x->a with the directed segment of Ci from a forward to b. This is a directed cycle of length

    2 + d_C(a,b),

where d_C(a,b) is the number of directed cycle edges from a to b. By minimum total size of the packing, this replacement cycle cannot be shorter than Ci, so

    2 + d_C(a,b) >= r.

Thus d_C(a,b)>=r-2. As a!=b (D has no digons), the only possible outneighbors a of x on Ci are the first and second successors of b. Therefore

    N_D^+(x) intersect V(Ci) subset {b^+, b^{++}},

and in particular

    |N_D^+(x) intersect V(Ci)| <= 2.

Contrapositive: if x has at least three outneighbors on Ci, then **no vertex of Ci sends an arc to x**.

This is a genuinely directed obstruction. Two arcs x->a,x->b do not make a directed cycle, unlike the near-directed transitive-triangle replacement used in the relaxation theorem.

## Lemma 7 — path-fan generalization

More generally, suppose there is a directed path

    b=p0 -> p1 -> ... -> p_L=x

from b in Ci to x in R, of length L, whose internal vertices p1,...,p_{L-1} all lie in R. For every a in A=N_D^+(x) intersect V(Ci), append x->a and the directed Ci segment a->...->b. The resulting directed cycle has length

    L + 1 + d_C(a,b).

Minimality of the three-cycle packing gives

    L + 1 + d_C(a,b) >= r.

Therefore every a in A must lie among at most L+1 successors of b around Ci, so

    |N_D^+(x) intersect V(Ci)| <= L+1.

Equivalently, if x has m outneighbors on Ci, every R-internal directed return path from Ci to x has length at least m-1.

The L=1 case is Lemma 6.

## Sink obstruction and the exact remaining implication

Take a sink x of the DAG D[R]. Because x has no outneighbor in R,

    sum_i |N_D^+(x) intersect V(Ci)| = d_D^+(x) >= 7.

Hence for some i,

    m := |N_D^+(x) intersect V(Ci)| >= 3.

Lemma 6 then says Ci has no direct arc to x. Lemma 7 says even more: any directed path from Ci to x whose internal vertices stay in R has length at least m-1.

Thus the first essential unpaid implication in candidate `BT4-MCR-v1` is:

> **Short-return obligation.** For the minimum-total three-cycle packing above, prove that for at least one sink x of R and one packed cycle Ci with m=|N^+(x) intersect Ci|>=3, there exists a directed path from Ci to x with all internal vertices in R and length at most m-2; or obtain an equivalent disjointness-preserving global exchange contradicting the path-fan inequality.

Such a path would contradict Lemma 7 immediately and close the minimal-counterexample argument. Strong connectivity alone does **not** prove this obligation: a path into x may enter R from a different packed cycle, and the first entrance into R need not be from the heavy cycle. This gap is left explicit.

The t=2 obstruction is a natural next pressure point: deleting any two packed cycles forces a witness with at least five outgoing arcs into those two cycles and residual outdegree at most two. Combining those witnesses across the three pairs may force the missing short return or a cross-cycle rerouting exchange.

## Exact deletion versus contraction loss

For any directed cycle C and v outside C, put a_C(v)=|N_D^+(v) intersect V(C)|. Then deletion gives exactly

    d^+_{D-C}(v) = d_D^+(v) - a_C(v).

If C is contracted to one vertex c, loops are removed and all arcs v->C merge to at most one arc v->c, so

    d^+_{D/C}(v) = d_D^+(v) - a_C(v) + 1_{a_C(v)>0}.

The contracted vertex has

    d^+_{D/C}(c) = |N_D^+(C) \ V(C)|,

counting distinct outside heads, not outgoing arcs with multiplicity.

Hence a witness with a_C(v)>=3 loses at least 3 units of outdegree under deletion and at least 2 under contraction. In the triangle case above, a degree-seven vertex dominating C drops to degree four after deletion and degree five after contraction. This is the exact reason the naive strategy “delete or contract a shortest cycle and invoke the k=3 theorem” fails at the threshold seven.

## Relation to the 2026 near-directed relaxation

The 2026 relaxation obtains k near-directed cycles at minimum outdegree 2k-1. In the minimal-counterexample part of that proof, two outneighbors of an outside vertex on a cycle can yield a transitive triangle, which is accepted as a near-directed cycle and replaces the old cycle. That step does not transfer to the genuine directed problem: a transitive triangle is not directed. Lemma 6 identifies the stronger directed obstruction: once x has three or more outgoing neighbors on a minimum packed directed cycle, minimum-total packing forces every reverse arc from that cycle to x to be absent. The relaxation therefore cannot be upgraded by simply “orienting” its local replacement.

## What was achieved and what remains

`ESSENTIAL_STEP_APPLIED`: the minimal-counterexample structure, exact deletion/contraction losses, a minimum-packing exchange lemma, its path-fan strengthening, and the first source-matching global missing implication are now explicit. This is **not** a proof of BT4 and makes no novelty claim. The next run should attack the short-return obligation directly, preferably by combining the pair-deletion five-fan witnesses with arc-maximality of missing arcs, rather than repeating the basic reductions.
