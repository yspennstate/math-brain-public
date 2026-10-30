# BT4 fleet01/B04 — corrected path-fan proof and amplified pair-deletion witnesses

Run: `20260922T001115Z-b04-bt4-r11`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and current-source check

For every finite loopless digraph D with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven, prove that D contains four vertex-disjoint genuinely directed cycles. Opposite arcs are allowed and a digon counts as a directed cycle.

Current primary source rechecked this run: Bessy, Muis, Sereni, Steiner and Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract explicitly states that the exact conjecture remains unresolved for every k>=4 and proves only the near-directed relaxation at threshold 2k-1. Thus the source-matching k=4 target remains open as of this check.

Two older exact inputs were also rechecked: Lichiardopol, Por and Sereni, SIAM J. Discrete Math. 23 (2009), prove (i) minimum outdegree five forces three vertex-disjoint directed cycles and, more strongly, (ii) a digraph in which every vertex has outdegree at least three except at most two vertices of outdegree two contains two vertex-disjoint directed cycles. Bang-Jensen, Bessy and Thomasse prove the Bermond-Thomassen bound for tournaments, in fact k disjoint directed triangles at tournament minimum outdegree 2k-1.

The assigned cross-account partner is `fleet02/B05`. No finalized post-reallocation BT4 mathematical artifact from that partner was available in the shared handoff directory when this report was derived; I therefore continued the exact shared candidate instead of waiting. The preceding fleet01/B04 candidate is `BT4-MCR-v1`, report `20260921T234516Z-b04-8fd1d4`.

## Inherited candidate and notation

Assume a counterexample exists and choose D with minimum |V(D)| and, subject to that, maximum |A(D)|. The previous report proved the following source-matching reductions:

1. D has no digon, hence is oriented.
2. D is strongly connected.
3. D is not a tournament, and arc-maximality supplies three disjoint directed cycles leaving at least three vertices uncovered.
4. Choose such a packing C1,C2,C3 minimizing total covered vertices. Put S=V(C1) union V(C2) union V(C3), R=V(D)\S. Then D[R] is a DAG and every Ci is chordless.
5. Deleting one packed cycle forces an outside vertex with at least three outneighbors on it; deleting two forces an outside vertex with at least five outneighbors in their union; a sink of R sends all at least seven of its outgoing arcs into C1 union C2 union C3.
6. If x in R has at least three outneighbors on a packed cycle C, then C has no arc directly to x.

This run found and repaired a gap in the written proof of the path-fan strengthening, and then strengthened the two-cycle deletion obstruction using the full 2009 degree-sequence theorem.

## Lemma 1 — corrected path-fan lemma

Let C be one of the packed cycles, of length r. Let x in R and suppose there is a directed path

    P: b=p0 -> p1 -> ... -> p_L=x

with b in C and p1,...,p_L in R. Put

    A = N_D^+(x) intersect V(C),   m=|A|.

Then every such path satisfies

    L >= m-1.

### Proof

For any a in A with a != b, concatenate P, the arc x->a, and the directed segment of C from a forward to b. This is a directed cycle, disjoint from the other two packed cycles. If t is the forward distance on C from b to a, its length is

    L+1+(r-t).

Minimality of the total packing size forces this length to be at least r, hence t<=L+1. Therefore every member of A other than possibly b lies among the first L+1 successors of b on C.

The previous report silently included the exceptional possibility a=b in that successor count. That was not justified. It is disposed of separately: if x->b, then P together with x->b is a directed cycle of length L+1. If L+1<r, replacing C by this cycle would strictly reduce the total packing size, impossible.

Now suppose toward contradiction that L<=m-2. Since m<=r,

    L+1 <= m-1 < r,

so x->b is impossible by the preceding paragraph. Hence all m members of A lie among only L+1 successors of b, giving

    m <= L+1 <= m-1,

contradiction. Thus L>=m-1. QED.

So the *statement* used in `BT4-MCR-v1` survives, but its proof required this exceptional-case repair. In particular the current short-return obligation remains exact: if global structure forces an R-internal path C->x of length at most m-2 for a sink x with m outneighbors on C, the minimum packing is contradicted.

## Lemma 2 — arc-maximal saturation certificate

For every missing ordered arc u->v of D, there exist three pairwise vertex-disjoint directed cycles Q1,Q2,Q3 in D and a directed path P from v to u in D such that P is vertex-disjoint from Q1,Q2,Q3.

### Proof

Add u->v. By arc-maximality of the chosen counterexample, D+u->v has four pairwise vertex-disjoint directed cycles. At least one uses the new arc, since otherwise D itself already has four. Exactly one can use it. Delete u->v from that cycle; what remains is a directed v-to-u path P in D. The other three cycles avoid the entire new-arc cycle and therefore are disjoint from P. QED.

This is stronger information than merely saying every missing arc is saturated: each nonarc carries an explicit three-cycle-plus-opposite-path certificate. It may be useful when a heavy sink x has no incoming arc from a heavily hit cycle C: every missing b->x, b in C, then yields a path x->b disjoint from another 3-packing.

## Lemma 3 — pair-deletion amplification from the exact k=2 degree-sequence theorem

Fix two packed cycles Ci,Cj, let

    U = V(Ci) union V(Cj),   H=D-U.

Then at least one of the following holds:

(A) there exists z in V(H) with

    d_H^+(z) <= 1,

and therefore

    |N_D^+(z) intersect U| >= d_D^+(z)-1 >= 6;

or

(B) there are at least three distinct vertices z1,z2,z3 in V(H) with

    d_H^+(z_s)=2,

and consequently each satisfies

    |N_D^+(z_s) intersect U| = d_D^+(z_s)-2 >= 5.

### Proof

H cannot contain two vertex-disjoint directed cycles, because those two cycles together with Ci,Cj would give four in D. Suppose (A) fails. Then every vertex of H has outdegree at least two. If at most two vertices had outdegree exactly two, all remaining vertices would have outdegree at least three, and the strengthened Lichiardopol-Por-Sereni k=2 theorem would force two disjoint cycles in H, contradiction. Hence at least three vertices have outdegree exactly two, proving (B). QED.

This strictly strengthens the previous generic `five-fan witness` statement. For every pair of packed cycles, either there is a **six-fan** witness into their union, or there are **three distinct five-fan witnesses**.

Each such five-fan witness has at least three outgoing neighbors on one of Ci,Cj. Therefore a useful exact case split is:

- if any pair-deletion witness lies in R, it heavily hits one of the two cycles; by the one-vertex exchange lemma that heavily hit cycle has no direct arc to the witness;
- otherwise all witnesses for that pair lie on the third packed cycle Ck, forcing either one vertex of Ck to send at least six arcs into Ci union Cj or three distinct vertices of Ck to send at least five arcs each into Ci union Cj.

This is a genuine concentration constraint on any minimum three-cycle packing, not a finite-search observation.

## Corollary 4 — amplification of the hard sink pattern

Let x be a sink of R and write

    a_i = |N_D^+(x) intersect V(C_i)|,
    a_1+a_2+a_3=d_D^+(x)>=7.

If a_k=2 and {i,j,k}={1,2,3}, then after deleting Ci and Cj the sink x has d_H^+(x)=2. Lemma 3 says that either:

- some (possibly different) vertex has residual outdegree at most one, hence sends at least six arcs into Ci union Cj; or
- there are at least two additional vertices y,z distinct from x with residual outdegree exactly two, hence each sends at least five arcs into Ci union Cj.

In particular, in the extremal degree-seven fan pattern (3,2,2), each of the two cycle-pairs whose complementary coordinate is 2 cannot have x as its sole five-fan obstruction: each pair generates either a stronger six-fan or at least two further five-fan witnesses. This removes a major weakness of the earlier single-witness deletion hierarchy.

## Lemma 5 — exact cycle-contraction obstruction

For completeness, the contraction loss assigned to this slot can be stated as a rigorous minimal-counterexample lemma, not just a degree formula.

Let C be any directed cycle of D and form D/C by contracting V(C) to a single vertex c, deleting loops and merging duplicate arcs. For x outside C put a_C(x)=|N_D^+(x) intersect V(C)|. Then

    d^+_{D/C}(x)=d_D^+(x)                    if a_C(x)=0,
    d^+_{D/C}(x)=d_D^+(x)-a_C(x)+1           if a_C(x)>0,

and

    d^+_{D/C}(c)=|N_D^+(V(C))\V(C)|.

Moreover, D/C cannot have minimum outdegree at least seven.

Indeed, if delta^+(D/C)>=7, vertex-minimality gives four disjoint directed cycles in D/C. At most one uses c. A quotient cycle through c lifts to a genuine directed cycle of D: if its predecessor enters c through p->a with a in C and c exits through b->q with b in C, replace p->c->q by p->a, the directed C-segment a->...->b, and b->q. The other quotient cycles avoid C, so disjointness is preserved. Thus four quotient cycles would lift to four in D, contradiction.

Consequently every directed cycle C satisfies at least one exact contraction obstruction:

    |N_D^+(V(C))\V(C)| <= 6,

or there is x outside C with

    a_C(x) >= d_D^+(x)-5 >= 2.

For a chordless cycle C, if the first alternative holds then it is completely rigid: each vertex of C has only its successor as an internal outneighbor and at least six external outneighbors, so the external union must have size exactly six, every vertex of C has outdegree exactly seven, and every vertex of C has the same six external outneighbors.

For the already chosen packed cycles the one-cycle deletion obstruction supplies an even stronger >=3 fan, so this contraction lemma is not counted as closing the current gap; its value is exact loss accounting and a reusable reduction for other cycles created by exchanges.

## Updated conditional chain and first unpaid implication

The surviving route is now:

1. vertex-minimal, arc-maximal, oriented, strongly connected counterexample;
2. minimum-total 3-packing C1,C2,C3 with DAG remainder R;
3. corrected path-fan lemma: a sink x with m outneighbors on heavy C cannot be reached from C through R in fewer than m-1 arcs;
4. every pair of packed cycles has either one six-fan witness or three distinct five-fan witnesses;
5. in the hard degree-seven sink pattern (3,2,2), the two residual-2 pair deletions generate additional high-fan vertices automatically;
6. missing arcs carry three-cycle-plus-opposite-path saturation certificates.

The first unpaid universal implication is therefore sharpened from `BT4-MCR-v1` to `BT4-MCR-v2`:

> Starting from the pair-witness multiplicity in Lemma 3, prove that either (i) one of those witnesses in R forces an R-internal return path to its heavily hit packed cycle shorter than its fan size minus one, or (ii) witnesses concentrated on the third packed cycle admit a two-cycle rerouting/exchange that reduces the total packed vertex count or creates four disjoint cycles.

This is more constrained than the previous request for an unexplained short return: each cycle-pair now supplies at least three threshold witnesses unless a strictly stronger six-fan exists. The next recipient should attack the concentration-on-third-cycle case and the R-witness case separately, using the saturation certificate rather than merely strong connectivity.

## Status

`ESSENTIAL_STEP_APPLIED`, not a full proof. The path-fan statement was repaired without weakening it; the pair-deletion obstruction was strengthened from one five-fan witness to a six-fan-or-three-five-fans dichotomy, and the hard (3,2,2) sink configuration now forces additional witnesses. No novelty claim is made. Full BT4 remains open on the evidence checked this run.

Next recipient: `fleet02/B05` and BT4 lead `fleet02/B04`, candidate `BT4-MCR-v2`.
