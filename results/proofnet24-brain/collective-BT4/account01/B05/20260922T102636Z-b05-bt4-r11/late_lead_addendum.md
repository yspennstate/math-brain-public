# Late-lead reconciliation — direct off-trace rank in the no-third-support R4 branch

Status: `ESSENTIAL_STEP_APPLIED`; target remains `OPEN_NOT_PROVED`.

After the initial immutable B05 report was written, a newer complete campaign-lead report became visible: account02/B04 `BT4-TRACE-TRANSVERSAL-ESCAPE-v1`, report blob `180efea97f9e427143959c7274a9bd2bba810021`.  It already proves the earlier existence debt `BT4-OFF-TRACE-OR-EXIT-v1` in greater generality.  This addendum does not alter the initial report.  Instead it applies the initial degree observation to the lead's *new* first debt, `BT4-OFF-TRACE-RANK-SPLICE-v1`.

Named OTHER-account guard retained: account02/B06 `BT4-RANK2-PORT-PARITY-v1`, handoff blob `9f8fdd21cec8929827f1223f71985600bc638f13`.  That result forbids promoting connector rank alone to a splice: endpoint order can still be `BLOCK` or parity-mismatched.

## Theorem — BT4-R4-NOC-DIRECT-OFFTRACE-RANK2-v1

Work in the inherited exact four-remainder clean state with globally minimum packed cycles `A,B,C`, acyclic `R`, `|R|=4`, oriented exact outdegree seven, and the primitive `A,B` trace of the lead.  Exclude third-support mediation through `C`.

Then:

1. there are no arcs from `A union B` to `C`;
2. every `a in A` has at least two **direct** outneighbors in `B`, and every `b in B` has at least two direct outneighbors in `A`;
3. every vertex of `A` is the source of a direct off-trace `A->B` arc, and every vertex of `B` is the source of a direct off-trace `B->A` arc;
4. the direct off-trace `A->B` arcs contain a matching of size at least two, and the direct off-trace `B->A` arcs contain a matching of size at least two;
5. the full direct `A->B` arc family and full direct `B->A` arc family each have matching number at least three.

Thus, after excluding the lead's recognized third-support exit, the new `OFF-TRACE-RANK-SPLICE` debt has **no remainder-interior coalescence obstruction at rank two**: endpoint-disjoint rank-two off-trace connector families already exist as single arcs in both directions.  What remains is cross-direction port collision / cyclic order / parity, exactly the obstruction isolated by account02/B06.

### Proof

Global minimum makes each packed support chordless: a non-successor arc inside a packed cycle would shorten that cycle while leaving the other two untouched.  Hence every packed vertex has exactly one outneighbor on its own support.

First take `c in C`.  It has one support successor and at most four outneighbors in `R`, so exact outdegree seven gives

`|N+(c) cap (A union B)| >= 2`.

If some `x in A union B` satisfied `x->c`, orientation forbids `c->x`.  Since `c` has at least two outneighbors in `A union B`, choose `y != x` there with `c->y`.  Then

`x -> c -> y`

is a genuine third-support mediation/excursion (if `x,y` lie on the same support they are distinct).  This contradicts the present no-`C` branch.  Therefore

`E(A union B,C)=emptyset`.

Now let `a in A`.  It has exactly one outneighbor in `A`, none in `C`, and at most four in `R`.  Hence

`|N+(a) cap B| >= 7-1-4 = 2`.

Similarly every `b in B` has at least two outneighbors in `A`.

Primitive-trace source uniqueness says that a fixed support vertex is the source of at most one direct primitive-trace cross arc in the relevant direction: plus states use every `A` source coordinate once and minus states use every `B` source coordinate once.  Since each source has at least two direct cross targets, every source has at least one direct **off-trace** target.

Let `F` be the bipartite graph of direct off-trace `A->B` arcs, forgetting orientation only for matching terminology.  Every `a in A` is incident with at least one edge of `F`.  Suppose `nu(F)=1`.  Because `A` is a genuine cycle in the oriented reduction, `|A|>=3`.  Take off-trace edges from two distinct `A` sources; with no matching of size two they share a common `B` endpoint `b*`.  Any off-trace edge from any other `A` source must meet each of those two edges, hence also ends at `b*`; the same is true for any additional off-trace edge from either original source, otherwise it is disjoint from the edge of the other source.  Thus every `a in A` satisfies `a->b*`.  Orientation then forbids `b*->a` for every `a in A`, contradicting the already-proved bound `|N+(b*) cap A|>=2`.  Hence `nu(F)>=2`.  The reverse direction is symmetric.

For the full direct `A->B` family, suppose its matching number were at most two.  By Konig's theorem it has a vertex cover of size at most two.  A cover by two `A` vertices is impossible because `|A|>=3` and every `A` vertex has two cross outneighbors.  A cover by one `A` vertex and one `B` vertex is impossible because every other `A` vertex would have all of its at least two cross outneighbors at the single covered `B` vertex.  A cover by two `B` vertices forces every `a in A` to point to both of them, and orientation then leaves each covered `B` vertex with zero outneighbors in `A`, contradicting its required cross outdegree at least two.  Therefore the full direct family has matching number at least three.  Symmetry gives the same for `B->A`.  QED.

## Exact consequence for the current lead debt

The latest lead theorem guarantees an off-trace connector or recognized exit by 3-vertex-strongness.  In the exact R4 clean branch, the theorem above sharpens its no-third-support alternative to a much denser statement:

`no C mediation => direct off-trace rank >=2 each way, direct total rank >=3 each way`.

So `BT4-OFF-TRACE-RANK-SPLICE-v1` can now discard all arguments devoted solely to obtaining two internally disjoint off-trace paths in each direction: their interiors are empty.  The first unpaid local implication becomes

`BT4-R4-DIRECT-PORT-ORDER-CLOSE-v1`:

> From direct off-trace matching rank at least two in both directions (and total direct matching rank at least three in both directions), plus global minimum and the existing clean four-port geometry, force compatible non-BLOCK parity, or turn every collision/order mismatch into a strict or neutral exchange, cyclic exchanged remainder, SIX, third-support mediation, or the fourth cycle.

Account02/B06 shows this order step is genuinely necessary; rank alone cannot be silently promoted to a legal two-cycle splice.

## Honest boundary

This closes a real part of the latest lead's first missing implication, but not all of it.  No compatible port order is yet forced, and no four-cycle packing is claimed.  Global SIX, bounded F2/F3, and seven-remainder branches also remain open.
