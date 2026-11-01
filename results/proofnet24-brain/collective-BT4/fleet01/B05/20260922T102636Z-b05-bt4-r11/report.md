# BT4 B05 proof attempt — primitive-trace degree budget forces a third-support exit

Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## Scope and source-bound inputs

Target: the exact k=4 Bermond--Thomassen statement in the current oriented exact-outdegree-seven minimum-counterexample programme.

This run deliberately changes mechanism from the preceding residual-three pivot-orbit work.  The current lead candidate is fleet02/B04 `BT4-PRIMITIVE-TRACE-MIXED-PACKING-ONE-v1` / debt `BT4-OFF-TRACE-OR-EXIT-v1` (lead report blob `b768e00ab1e7f22e0cfd56d6f95ffbc36b3a1c60`).  Its source-bound predecessor is fleet02/B04 `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1` (handoff blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`).

Named OTHER-account result actually applied: assigned partner fleet02/B06 `BT4-RANK2-PORT-PARITY-v1` (handoff blob `9f8fdd21cec8929827f1223f71985600bc638f13`).  It is used as a hard guard: connector abundance or a single new excursion is not promoted to a two-cycle splice; support order/parity and BLOCK states still have to be paid.

Also used: fleet04/B05 `BT4-BIDIRECTIONAL-RANK2-ORDER-WALL-v1` (handoff blob `f553a1086caaea875705c6f8c5d3f268bda1d3c3`), which records that the present clean heavy-triangle interface sits in the four-remainder cage and that legal rank-two splicing still has an order wall.

## Compact conditional end-to-end state

In the current proof programme, after the standard reduction choose a globally minimum three-cycle packing `(A,B,C)` with acyclic remainder `R`.  In the clean heavy-triangle coalescence branch under discussion, `|R|=4`, the digraph is oriented with every outdegree exactly seven, and the packed supports are chordless by global minimum.  The lead's clean four-port construction reduces the local two-support `A,B` geometry to a primitive trace plus recognized exits.  The lead then proved that no two vertex-disjoint mixed cycles can be made while all support switches remain on that primitive trace, even allowing trace-parallel detours.  Thus the first local obligation is to force an order-breaking `A<->B` connector or an exit through a same-support bypass / third support / packing decrease / cyclic remainder / SIX / fourth cycle.

The theorem below proves a strong direct-arc version of precisely the first dichotomy in the exact four-remainder cage: if all direct `A<->B` arcs remain primitive-trace arcs, a path through the third packed support is forced purely by the degree budget.

## Preliminary fact — packed supports are chordless

Let `T` be one member of a globally minimum three-cycle packing.  If `u->v` is an arc with `u,v in T` and `v != u+` (the successor of `u` on `T`), then

`u -> v -> T[v,u] -> u`

is a directed cycle strictly shorter than `T`.  Replacing `T` by this cycle leaves the other two packed cycles untouched and strictly decreases total packed order, contradiction.  Hence every packed vertex has exactly one outneighbor on its own packed support, namely its successor.

## Primitive-trace source uniqueness

Write

`A=a_0 a_1 ... a_{m-1} a_0`,  `B=b_0 b_1 ... b_{n-1} b_0`.

In the lead primitive-trace word there are exactly `m` plus occurrences and `n` minus occurrences.  Traversing occurrences in reverse order increments the `A` coordinate exactly once at every plus occurrence, so the first coordinates of the plus states run through all residues of `Z_m` exactly once.  Therefore each `a_i` is the source of exactly one primitive-trace `A->B` state.  Symmetrically each `b_j` is the source of exactly one primitive-trace `B->A` state.

Consequently, if **every direct `A->B` arc is a primitive-trace arc**, then

`|N+(a) cap B| <= 1` for every `a in A`.

If every direct `B->A` arc is primitive-trace, then

`|N+(b) cap A| <= 1` for every `b in B`.

## New theorem — BT4-R4-TRACE-DEGREE-THIRD-SUPPORT-EXIT-v1

Assume the exact four-remainder clean state above and assume all direct arcs between `A` and `B` are primitive-trace arcs in their respective directions.  Then:

1. every vertex of `A` has an outneighbor on `C`;
2. every vertex of `B` has an outneighbor on `C`;
3. every vertex of `C` has at least two outneighbors in `A union B`;
4. hence there is a directed two-edge path through `C` of one of the forms

   `B -> C -> A`,  `B -> C -> B`,  `A -> C -> B`,  or `A -> C -> A`,

   with distinct same-support endpoints in the `B->C->B` and `A->C->A` cases.

In particular the pure two-support primitive-trace geometry cannot be a closed local obstruction: either an `A<->B` direct arc is off the primitive trace, or a genuine third-support mediation/excursion exists.

### Proof

Take `a in A`.  By chordlessness, `a` has exactly one outneighbor in `A`.  By primitive-trace source uniqueness, it has at most one outneighbor in `B`.  It has at most four outneighbors in the four-vertex remainder `R`.  Therefore, if `a` had no outneighbor in `C`,

`d+(a) <= 1 + 1 + 4 = 6`,

contradicting exact outdegree seven.  Thus `N+(a) cap C != emptyset` for every `a in A`.  The same argument with `A,B` interchanged gives an outneighbor on `C` for every `b in B`.

Now take `c in C`.  Chordlessness gives exactly one outneighbor of `c` in `C`, and there are at most four remainder outneighbors.  Hence

`|N+(c) cap (A union B)| >= 7 - 1 - 4 = 2`.

Choose any `b in B` and one `c in C` with `b->c`, which exists by the previous paragraph.  Because the digraph is oriented, `c!->b`.  Since `c` has at least two outneighbors in `A union B`, choose such an outneighbor `z` different from `b`.  If `z in A`, then

`b -> c -> z`

is a genuine `B->C->A` mediation.  If `z in B`, then

`b -> c -> z`

is a genuine third-support `B->B` excursion with distinct support endpoints.  Either is an order-breaking exit from the lead's two-support trace class.  Starting from any `a->c'` gives the symmetric `A->C->B` or `A->C->A` alternative.  QED.

## Quantitative form

The same proof gives the arc lower bounds

`e(A,C) >= |A|`,  `e(B,C) >= |B|`,

and

`e(C,A union B) >= 2|C|`.

Thus the third-support wall is not a single accidental connector: in the no-off-trace direct-cross branch it is forced at every `A` and `B` source and has at least two outgoing packed continuations at every `C` vertex.

## How this applies the partner obstruction correctly

Fleet02/B06 `BT4-RANK2-PORT-PARITY-v1` proves that even two endpoint-disjoint connectors in each direction do not automatically yield two vertex-disjoint mixed replacement cycles: each support can be `ID`, `SW`, or `BLOCK`, and compatible parity is required.  Therefore the theorem above is **not** claimed to close BT4 and is not called a two-cycle augmentation.  What it does pay is the lead's first existence-level debt: a pure primitive trace in the exact R4 cage must leak through the third support unless an order-breaking direct `A<->B` arc already exists.

The next packing-level obligation is now narrower:

`BT4-R4-C-WALL-EXCHANGE-CLOSE-v1`:

> Starting from the forced two-edge third-support excursion above, use the already present clean four-port connector(s), global minimum, and the B06 port-order criterion to obtain either two legal vertex-disjoint replacement cycles with complete support accounting, a strict/neutral packing exchange whose new remainder is cyclic or returns to a recognized exact-R4 state, SIX, or the fourth directed cycle.

A single `B->C->A` or `B->C->B` path is not enough by itself because it consumes vertices of the third packed cycle; that support must be repaired in any legal three-packing comparison.  This accounting point is explicit and remains unpaid.

## Honest status

`ESSENTIAL_STEP_APPLIED`.  The direct-arc part of `BT4-OFF-TRACE-OR-EXIT-v1` is closed in the exact four-remainder clean state: **primitive-trace-only direct `A<->B` geometry forces a third-support exit by degree seven**.  The target remains `OPEN_NOT_PROVED`; global SIX, bounded F2/F3, seven-remainder pinwheel, and the new C-wall packing-repair step remain open.
