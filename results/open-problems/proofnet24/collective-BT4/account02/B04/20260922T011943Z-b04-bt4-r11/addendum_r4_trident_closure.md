# BT4 account02/B04 second addendum — the three-sink four-remainder orbit must escape

Run: `20260922T011943Z-b04-bt4-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

This addendum strengthens `addendum_r4_trident.md` (blob `22e0b70fe2cfa33cc7a380eb9097329113d6b522`). It uses no new hypothesis beyond that addendum's smallest distinct-heavy hard core and the account04/B06 sink-inneighborhood localization, report blob `44774a85169331dcf5b4cc7d79f3bef31ccb6dbc`.

## Escape theorem

Assume a globally minimum-total three-cycle packing `(A,B,C)` in the exact-outdegree-seven counterexample has a four-vertex acyclic remainder

`R={u,x_A,x_B,x_C}`

in the global no-six branch, with exactly three sinks `x_A,x_B,x_C`, having distinct heavy labels `A,B,C`, respectively. As in the first addendum, this is the three-sink hard core after separating the branch in which some packed pair already has three sink-supported five-witnesses.

Then **at least one** of the three support-distinct neutral exchanges forced by the first addendum leaves this three-sink hard core: after that exchange either the new packing is no longer in the global no-six branch, or its four-vertex remainder has at most two sinks.

Equivalently, there is no closed neutral state in which all three forced support moves return to another no-six four-remainder/three-sink state.

### Proof

From the first addendum, `u` is the unique nonsink and

`u->x_A, u->x_B, u->x_C`.                                      (1)

For each support cycle `C_i in {A,B,C}`, the pair-deletion deficit theorem forces a cycle-supported residual-degree-two witness `z_i in C_i`. Chordlessness gives exactly two residual outarcs after deleting the other two packed cycles:

- the support successor `y_i=z_i^+`;
- one unique remainder exit `z_i->e_i`.

The exit cannot be the own-heavy sink `x_i`.

If some `e_i=u`, the heavy equality move `z_i->u->x_i` is available. Lemma 3 of the first addendum proves that if its new packing remains no-six, its new remainder has at most two sinks. So this is already the required escape.

It remains to assume

`e_i` is a non-own sink for every `i`.                           (2)

Then all three forced moves are one-vertex light pivots. Suppose for contradiction that **each** of these three pivots remains in the global no-six branch and still has three remainder sinks.

Fix the pivot supported on `C_i`, whose exit is `z_i->x_j` with `j!=i`. It replaces the sink `x_j` on the remainder side by `y_i=z_i^+`; the other two old sinks remain in the new remainder together with `u`. By (1), `u` still sends to those two old sinks, so `u` is certainly a nonsink in the new four-vertex remainder. If that remainder has three sinks, `u` is therefore its unique nonsink and `y_i` is one of its sinks.

Account04/B06 proves that every no-six sink has an inneighbor in the remainder. The other three vertices besides `u` are sinks and hence have no remainder outarcs. Therefore the required predecessor of `y_i` can only be `u`:

`u -> y_i`.                                                       (3)

Since we assumed all three support pivots preserve the three-sink no-six state, (3) holds for every support cycle:

`u -> y_A, u -> y_B, u -> y_C`.                                 (4)

Now return to the **original** state. Account04/B06's sink-inneighborhood localization becomes especially rigid when `|R|=4` and there are three sinks. For any sink `x_j`, its heavy cycle contributes no return vertex, each light cycle contributes at most one return vertex, and among remainder vertices only `u` can point to `x_j`. The directed cycle in `D[N^-(x_j)]` is therefore forced to be a directed triangle consisting of

`u` and the unique return vertices from the two light cycles.    (5)

For each selected witness `z_i`, (2) makes `z_i` exactly one of those light return vertices for its target sink `x_j`. But `z_i` has residual outdegree exactly two after deleting the other packed pair, namely

`z_i -> y_i` and `z_i -> x_j`.

In particular

`z_i -/> u`.                                                       (6)

The triangle (5) contains both `u` and `z_i`. Since the edge of that directed triangle between them cannot be `z_i->u` by (6), it must be

`u -> z_i`.                                                       (7)

Again this holds for every support witness:

`u -> z_A, u -> z_B, u -> z_C`.                                 (8)

The nine heads in (1), (4), and (8) are pairwise distinct: the three `x_i` lie in the remainder, the three support cycles are disjoint, and on each directed cycle `z_i != y_i=z_i^+`. Thus (1), (4), and (8) give at least nine distinct outneighbors of `u`.

This contradicts the exact-outdegree-seven normal form.

Hence our assumption that all three light pivots preserve the no-six three-sink state is impossible. Together with the heavy-exit case, at least one of the three forced neutral support moves must escape: it either creates a six-fan somewhere in the regenerated pair deficits (or otherwise leaves global no-six), or leaves a four-vertex remainder with at most two sinks. QED.

## What this pays

The previous lead state had a potentially closed neutral orbit of length at least three. The first addendum reduced the smallest three-sink remainder to three forced support ports. The theorem above now proves that **the `|R|=4,s=3` distinct-heavy no-six core cannot be closed under those ports at all**.

So the long-orbit obligation no longer contains this smallest three-sink core. Every such state has a source-valid move into one of two strictly different mechanisms:

1. the six-fan / non-no-six branch; or
2. a four-vertex no-six remainder with at most two sinks.

The theorem does not close either destination branch. It does, however, remove the possibility that the proof is trapped forever among three-sink four-remainder neutral packings.

## Conditional route after this improvement

The end-to-end conditional proof from the lead report can now replace its generic long-neutral-orbit clause by the following sharper split in the smallest remainder:

- `|R|=3` with three sinks was already excluded by account04/B06;
- `|R|=4,s=3` with distinct heavy labels must escape by the theorem above;
- if heavy labels are not distinct, the existing sink-witness concentration branch is triggered;
- therefore any persistent smallest-remainder obstruction after the forced exchanges lies in the `s<=2` no-six branch or in the six-fan branch.

For `|R|>=5`, the broader neutral/cross-linkage problem remains. No claim is made that the full BT4 conjecture is proved.

## Adversarial checks

- The argument counts **outneighbors**, not arcs with repeated heads. All nine heads are distinct for the reasons stated above.
- The implication `z_i -/> u` uses the exact residual degree-two conclusion for the third-cycle witness: its only residual heads are its support successor and its unique remainder exit.
- The implication `u->z_i` uses the actual directed triangle inside `N^-(x_j)`, not merely pairwise adjacency.
- If two selected witnesses return to the same sink, the same triangle argument is even more restrictive; the proof does not require their target sinks to be distinct.
- A pivot is used only as an alternative packing move; the three pivots are not asserted to be simultaneously vertex-disjoint.
- The result is confined to the exact directed-cycle target and does not use near-directed cycles or edge-disjoint substitutes.

Outcome: `ESSENTIAL_STEP_APPLIED`.
