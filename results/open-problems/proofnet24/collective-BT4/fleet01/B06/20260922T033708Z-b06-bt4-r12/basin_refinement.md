# BT4 R4 strict-saturation refinement — unique old-remainder sink collapses the source cycle

Run: `20260922T033708Z-b06-bt4-r12`  
Candidate addendum: `BT4-R4-POSTPIVOT-BASIN-v1`  
Parent report blob: `ef9a39bbecef6997d3f8259ce7526bf31057c088`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target: `OPEN_NOT_PROVED`  
Brain: `WITHOUT_VERIFIED_BRAIN`

## Imported exact configuration

Use the parent report's strict four-remainder saturation obtained by applying fleet02/B05 `BT4-RSC-v6-postpivot-wall` to the campaign lead's current `SC+` source pivot. Before the pivot the old remainder is

`R={x,u,v,w}`,

where `x` is the chosen old `R`-sink. The old source cycle contains

`p -> q -> s -> t -> ... -> p`,

and the sink fan contains both source targets `q=p^+` and `s=p^{++}`. Hence the ambient arc

`x -> q`

exists. After the neutral pivot, the new remainder is

`R'={q,u,v,w}`,

and in the strict two-arm saturation the exact paths are

`p -> q -> u -> s`,

`p -> q -> v -> w -> t`.

In particular the ambient arcs `q->u`, `q->v`, and `v->w` exist.

## Lemma — unique-sink collapse

If `x` is the **unique** sink of the old acyclic remainder `D[R]`, then the source cycle has order at most four:

`|S|=|S'| <= 4`.

### Proof

Because `D[R]` is a finite DAG with unique sink `x`, every vertex of `R` has a directed path inside `R` to `x`. In particular both `u` and `v` do.

Let `d_R(r,x)` be the length of a shortest directed `r`-to-`x` path in `D[R]`. Since `R` has only the four vertices `x,u,v,w`,

`min{d_R(u,x), d_R(v,x)} <= 2`.

Indeed, if (say) a shortest `u`-to-`x` path has length three, then it uses **both** of the other non-`x` vertices `v,w`; whichever order occurs, `v` lies on that path and its suffix to `x` has length at most two. If the `u`-distance is already at most two there is nothing to prove.

Choose `r in {u,v}` with `d_R(r,x)<=2`, and let `Q` be a shortest `r`-to-`x` path in the old remainder. The arcs

`x -> q -> r`

exist by the sink source fan and the strict post-pivot saturation. Therefore

`C = x -> q -> r -> Q -> x`

is a genuine simple directed cycle. Apart from `x,q`, all of its vertices lie in the old remainder, so it is disjoint from the untouched packed cycles `H,U`. Its order is

`|C| = 2 + d_R(r,x) <= 4`.

Consequently `(C,H,U)` is a valid three-cycle packing. Global minimum of the inherited packing gives

`|S|+|H|+|U| <= |C|+|H|+|U|`,

hence `|S|<=|C|<=4`. The neutral pivot preserves source-cycle order, so also `|S'|<=4`. QED.

## Consequences

1. In the strict four-remainder post-pivot saturation, **either** `|S|<=4` **or the old remainder has a second sink** in `{u,v,w}`. Thus for every source cycle of order at least five, the residual `R4-STRICT-SAT+` problem automatically enters a double-sink regime.

2. If `x` is unique and `|S|=4`, global minimum forces equality throughout the construction above: the chosen `r` has shortest old-remainder distance exactly two and the cycle `x->q->r->R->x` is another order-four source replacement. In particular no arc from either chosen distance-one exit directly to `x` can yield a triangle replacement.

3. More generally, if either post-pivot exit `u` or `v` merely reaches `x` in the old remainder, the same argument gives a source replacement of order at most five (because an `r`-to-`x` path in a four-vertex remainder has length at most three). Hence `|S|>=6` forces **both** chosen exits into basins of old sinks other than `x`; since `v->w`, also `w` cannot reach `x` in that regime.

This is compatible with, and gives a concrete entry point for, fleet01/B05's same-hour double-sink support-splice mechanism (`BT4-G1-DOUBLE-SINK-SPLICE-v1`, shared blob `8ba258bb5837fdcbacde932a1fbb7ed31da0cc0c`): the next hard branch is not arbitrary four-remainder linkage, but either the lead's already-small source case `|S|<=4` or a genuine multiple-sink configuration in which two sink fan/cross systems can be compared.

No four-cycle packing is claimed here, and BT4 remains open.
