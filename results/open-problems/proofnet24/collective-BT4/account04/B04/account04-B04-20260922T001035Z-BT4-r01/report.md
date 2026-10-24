# BT4 account04/B04 — remainder-sink structural split and return-collar lemma

Run: `account04-B04-20260922T001035Z-BT4-r01`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target

For every finite loopless digraph D with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven, prove that D contains four vertex-disjoint directed cycles. Opposite arcs are allowed in the target and a directed digon counts as a cycle.

A bounded fresh literature check on 22 September 2026 found Bessy–Muis–Sereni–Steiner–Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), still explicitly stating that the exact conjecture remains unresolved for every k>=4. Its theorem at threshold 2k-1 gives near-directed cycles, not genuinely directed cycles. This bounded check is not an exhaustive worldwide novelty certificate.

Primary source: https://arxiv.org/abs/2608.12948 . In its introduction, Conjecture 1 is the exact directed-cycle statement; the paper records k=2 and k=3 as known and k>=4 as open, and Theorem 1 proves only the near-directed relaxation.

## Other-account input actually used

I consumed and applied account01/B04's finalized candidate `BT4-MCR-v1`, scientific commit `8a71d11efa2a3110db78c39684ea4c9cce03a28b`, report `proofnet24/collective-BT4/account01/B04/20260921T234516Z-b04-8fd1d4/report.md`.

The exact facts inherited from that report are the following. In a counterexample D chosen first vertex-minimal and then arc-maximal:

1. D has no digon and is strongly connected.
2. D is not a tournament. There exist three vertex-disjoint directed cycles C1,C2,C3 leaving at least three vertices uncovered.
3. We may choose such a 3-packing minimizing the total number of covered vertices. With S=V(C1) union V(C2) union V(C3) and R=V(D)\S, D[R] is a DAG and every packed cycle is chordless.
4. If x is in R, C is one packed directed cycle, and m=|N+(x) intersect V(C)|, then every directed path from a vertex b of C to x whose internal vertices lie in R has length at least m-1. Equivalently, an R-internal return path of length L forces m<=L+1. In particular m>=3 implies there is no direct arc C->x.
5. A sink x of R has all at least seven outneighbors on the three packed cycles, hence is heavy on at least one packed cycle C: m=|N+(x) intersect C|>=3.

The first unpaid implication in `BT4-MCR-v1` was to force, for some heavy sink-cycle pair (x,C), an R-internal return path C->x shorter than m-1, or an equivalent global exchange. Strong connectivity alone does not force that, because a path from C to x may pass through another packed cycle before its final entry into R.

The assigned account04/B04 task is to derive the structural case split needed to close that minimal-counterexample route. The named partner is account01/B05. No finalized post-reallocation BT4 output from that partner was available at the time of this run; the argument below therefore applies the complete account01/B04 snapshot rather than waiting.

## Refinement of the extremal packing

Among all three-cycle packings that minimize

    |V(C1)|+|V(C2)|+|V(C3)|,

choose one for which the maximum number of vertices on a directed path in D[R] is as large as possible. This secondary choice preserves every lemma above, because none of them used anything beyond minimum total coverage.

Let

    P = p0 -> p1 -> ... -> ph = x

be a longest directed path in D[R]. Since R is a DAG, x is a sink of R: an arc x->z to a vertex z outside P would extend P, while an arc from x to an earlier vertex of P would create a directed cycle in R.

Because x is a sink and d+(x)>=7, all its outneighbors lie on C1,C2,C3. Fix a packed cycle C for which

    m := |N+(x) intersect V(C)| >= 3.

By the inherited path-fan lemma, C has no arc directly to x, and every C-to-x path with all internal vertices in R has length at least m-1.

## Lemma A — unique-sink return collar

Assume x is the unique sink of R. For v in R let dist_R(v,x) be the length of a shortest directed v-to-x path in R. Then every vertex v of R reaches x, and for every arc b->v with b in C,

    dist_R(v,x) >= m-2.                                             (1)

### Proof

In a finite DAG, following outgoing arcs from any vertex eventually reaches a sink. Since x is the unique sink, every v reaches x.

If b->v is an arc from C into R, concatenate it with a shortest v-to-x path in R. This gives a C-to-x path with internal vertices in R of length

    L = 1 + dist_R(v,x).

The path-fan lemma gives m<=L+1, hence

    m <= dist_R(v,x)+2,

which is exactly (1). QED.

Thus the heavy cycle C has a return-free collar around x: it cannot send an arc to any R-vertex whose distance to x is 0,1,...,m-3.

This yields an exhaustive unique-sink trichotomy.

- U0 (cross-cycle return): C has no arc at all into R. Since D is strongly connected, every path from C to x must pass through another packed cycle before its final entry into R.
- U1 (tight collar): C has an arc b->v with dist_R(v,x)=m-2. Then the induced C-to-x return has the minimum permitted length m-1, so the path-fan inequality is tight. In the proof of the inherited lemma, the m vertices of N+(x) intersect C exhaust the allowable successor window of size m around b (with the all-of-C saturation case kept separate when m=|C|). Thus a shortest permitted return forces a rigid consecutive-fan configuration rather than an arbitrary fan.
- U2 (strict collar): every arc C->v into R satisfies dist_R(v,x)>=m-1. The heavy cycle is separated from x by at least one additional R layer beyond the bare path-fan bound.

The old missing implication is therefore not a generic strong-connectivity problem in the unique-sink case: a counterexample must have U0, the exact tight-window geometry U1, or the strict distance barrier U2.

## Lemma B — multiple-sink exchange restriction

Assume R has a second sink y distinct from x. Put

    q := |N+(y) intersect V(C)|.

Then the following exhaustive alternatives hold.

### B1: q>=3

There is no arc from C to y. This is the one-vertex exchange lemma applied to y. Since m>=3 also forbids C->x, the same heavy cycle C has no direct return arc to either sink.

### B2: q<=2

Because y is a sink of R, all at least seven outneighbors of y lie on the three packed cycles. Hence y has at least

    7-q >= 5

outneighbors on the two packed cycles other than C. In particular y is heavy (at least three outneighbors) on at least one of those other two cycles.

Moreover, suppose b->y is an arc with b in C. Write b+, b++ for the first and second successors of b around the directed cycle C. The inherited one-vertex exchange lemma gives

    N+(y) intersect V(C) subset {b+, b++}.                           (2)

There is an additional restriction coming from the secondary longest-path choice:

    if b++ is in N+(y), then b+ is NOT in N+(x).                    (3)

### Proof of (3)

Assume b++ is in N+(y). The directed cycle

    C* = b -> y -> b++ -> ... -> b

uses y together with every vertex of C except b+. It therefore has exactly |V(C)| vertices. Replacing C by C* keeps three disjoint directed cycles and preserves the minimum total number of covered vertices.

The new remainder is obtained from R by removing y and adding b+. Since y is a sink different from x, y is not a vertex of the longest path P ending at x. Thus P remains in the new remainder. If x->b+ were an arc, P could be extended by the newly freed vertex b+, contradicting the secondary choice of the packing. Therefore x does not see b+, proving (3). QED.

A useful tight consequence is that when q=2 and C has any arc b->y, (2) forces

    N+(y) intersect C = {b+,b++},

and then (3) forces the heavy sink x to avoid b+. Thus the apparent 3+2 (or larger+2) fan configuration is not free: any direct return to the 2-fan sink pins the two fan vertices consecutively and forbids the heavy sink from seeing the vertex that would be freed by the equal-size exchange.

## Complete remainder-sink structural split (`BT4-RSC-v1`)

Every minimal counterexample satisfying `BT4-MCR-v1`, after the harmless secondary extremal choice above, lies in exactly one of the following top-level branches for a longest-path sink x and one heavy cycle C.

1. UNIQUE SINK. R has unique sink x. Then C obeys the return collar (1), and the branch further splits into U0 (no C->R entry, so every return is forced through another packed cycle), U1 (tight entry at distance m-2 with a saturated successor window), or U2 (all C->R entries occur at distance at least m-1).
2. MULTIPLE SINKS. R has another sink y. For each such y, either q>=3 and C has no direct arc to y, or q<=2 and y sends at least five arcs into the other two cycles. Any direct C->y return is confined by (2), and whenever it uses b++ the alignment x->b+ is forbidden by (3). In particular, q=2 plus a direct return has the exact consecutive two-fan / heavy-sink anti-alignment geometry above.

This split is genuinely directed. The 2026 near-directed proof can replace a packed cycle by a transitive triangle created from two same-tail fan arcs; that shortcut is not a directed cycle and is precisely what fails here. The equal-size exchange in Lemma B uses a genuine directed return arc b->y and therefore stays inside the exact BT4 target.

## Why this is progress and what remains unpaid

`ESSENTIAL_STEP_APPLIED`, not a full proof. The shared short-return obligation is now localized to rigid configurations instead of an unconstrained strongly connected graph.

The next decisive step should attack the finite branch geometry rather than redo minimality:

- In U0, use the pair-deletion five-fan witnesses to force a transition from C through another packed cycle and back into R; the goal is to bound the last R-entry distance to x.
- In U1, exploit the saturated consecutive fan window together with chordlessness of C and the five-fan witnesses; any extra admissible return should create a shorter replacement or a two-cycle exchange.
- In U2, combine the strict distance collar with the outdegree-seven budget along the last m-2 R layers. Those layers cannot receive arcs from the heavy cycle, so their seven outgoing arcs must be paid for by R-forward arcs and the other two packed cycles.
- In the multiple-sink branch, the anti-alignment rule (3) is the first genuine two-sink exchange obstruction. Repeating it around all return arcs may force either a second equal-size exchange that extends P or a no-return cut, which can then be attacked by strong connectivity/pair-deletion witnesses.

No target-level conclusion is claimed. No finite search, benchmark answer, brain retrieval, or production-state assertion is used in this argument.
