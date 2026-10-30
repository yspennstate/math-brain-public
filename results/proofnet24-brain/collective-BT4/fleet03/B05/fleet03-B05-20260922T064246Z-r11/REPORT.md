# BT4 fleet03/B05 report — connector-rank obstruction and third-support wall

Outcome: `ESSENTIAL_STEP_APPLIED` with one local splice inference refuted.  
Target status: `OPEN_NOT_PROVED`.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Controlling scope

Target: every finite loopless simple digraph with minimum outdegree at least 7 contains four vertex-disjoint directed cycles; digons are allowed.

Exact fleet03/B05 assignment: prove the disjointness-preserving exchange promised by the current two-partition or linkage candidate; averages do not replace minimum-degree hypotheses. Assigned partner: `fleet04/B06`.

Fresh active control remained owner revision `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. No later applicable stop or reassignment was observed before publication of this report.

## Exact source-bound inputs actually used

1. Team lead `fleet02/B04`, handoff commit `3d1cdc39d7512ad857e134f23740c027ef879764`, candidate `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`. Its current hard local state has two packed cycles `A,B`, a third retained packed cycle `C`, four distinct old ports `p,a` on `A` and `b,q` on `B`, an `A->B` path `P: p->x->b` with `x` in the remainder, and a direct `B->A` cross `Q:q->a`. A further domination ladder can coalesce at old ports, producing a direct cross `c->w` and a second endpoint-matched path `c->...->w` through the remainder. The lead correctly leaves the resulting disjointness-preserving splice unpaid.

2. Named OTHER-account result `fleet04/B05`, handoff commit `66f76a628ae4fea4a5074e548f1e65926e4efa12`, candidate `BT4-HT-EQUALITY-COLLAR-ELIMINATION-v1`. It eliminates the two residual equality collars in the exact heavy-triangle cage and forces the relevant branch into a genuine cross-packed transition (or its compatible Hall-side alternative). I use that conclusion only to justify that the current debt is genuinely a cross/linkage exchange rather than an equality-collar case.

The assigned partner `fleet04/B06` had no current BT4 artifact that I could source-bind on fresh main; the latest directly identified `fleet04/B06` record was a pre-reallocation brain-role start under revision `2026-09-21.1`. Per the collective order, a missing peer does not justify waiting, so I used the named current OTHER-account BT4 result above and will hand this result to `fleet04/B06`.

## New lemma 1 — connector-rank necessity

Let `A,B` be vertex-disjoint directed cycles. A connector is a directed path having one endpoint on `A`, one on `B`, and all internal vertices outside `A union B`. Call it forward if it runs `A->B` and reverse if it runs `B->A`.

**Lemma.** Suppose `Z1,Z2` are vertex-disjoint directed cycles contained in `A union B` together with a specified connector family, and each `Zi` meets both `A` and `B`. Then the connector family contains at least two pairwise vertex-disjoint forward connectors and at least two pairwise vertex-disjoint reverse connectors.

**Proof.** Every directed cycle that meets both supports must leave `A` for `B` at least once and later return from `B` to `A` at least once. Thus each `Zi` uses at least one forward and one reverse connector. Since `Z1,Z2` are vertex-disjoint, the connector used by `Z1` in a given direction is vertex-disjoint, including endpoints, from the connector used by `Z2` in that direction. Hence two vertex-disjoint connectors are necessary in each direction. QED.

Equivalently, if `nu_AB` and `nu_BA` denote the maximum cardinalities of pairwise vertex-disjoint specified connectors in the two directions, two disjoint mixed replacement cycles require `min(nu_AB,nu_BA) >= 2`.

## Application to the lead's four-port coalescence

The inherited clean pair gives one forward connector `P:p->x->b` and one reverse connector `Q:q->a`. The coalesced domination output gives a direct connector `D:c->w` and a second path `L:c->...->w` with the *same* endpoints `c,w`, all four endpoints lying in `{p,a,b,q}`.

The pair `D,L` has connector matching number one in its direction because it shares both endpoints. Therefore the family `{P,Q,D,L}` cannot have two vertex-disjoint connectors in both directions:

- if `D,L` are forward, there is still only the single reverse connector `Q`;
- if `D,L` are reverse, there is still only the single forward connector `P`;
- using both `D` and `L` in two different cycles is impossible because they share `c,w`.

Hence **the finite coalesced four-port geometry alone cannot produce two vertex-disjoint mixed replacement cycles**. This refutes the tempting local inference “direct cross + endpoint-matched remainder path closes the two-cycle splice.” It does *not* refute BT4, the lead theorem, or the existence of a different exchange using a fresh port, a same-support bypass, the third packed support, or a cycle in the exchanged remainder.

This is the disjointness issue the B05 assignment specifically requires preserving: edge/path multiplicity is not enough; endpoint-disjoint connector rank is the relevant first invariant.

## New lemma 2 — direct-reverse port avoidance forces a fresh connector or third-support mediation

Now use the inherited minimal-counterexample normal form in which `D` is 3-vertex-strong and the lead's reverse cross is the direct arc `Q:q->a`, with `q in B`, `a in A`, and `A,B,C` the three packed cycles.

**Lemma.** There is a directed `B->A` path `W` in `D-{q,a}`. After trimming `W` from its last `B` vertex before its first subsequent `A` vertex, exactly one of the following holds:

1. `W` has all internal vertices in the remainder `R = V(D) \ (V(A) union V(B) union V(C))`. Then it is a `B->A` connector vertex-disjoint from the direct connector `Q`, with fresh endpoints different from `q,a`.

2. `W` meets the third packed cycle `C`. Then trimming at the first and last `C` hits yields a source-valid connector chain `B -> C -> A` avoiding `q,a`; in particular the failure to freshen the reverse connector outside `C` is converted into an explicit third-support mediation wall.

**Proof.** Since `D` is 3-vertex-strong, deleting the two vertices `q,a` leaves a strongly connected digraph. The cycles have surviving vertices, so choose `b0 in B-{q}` and `a0 in A-{a}` and a directed `b0->a0` path in `D-{q,a}`. Let `s` be the last vertex of `B` on the path before its first later vertex `t` of `A`, and restrict to the subpath `sWt`. Its interior avoids `A union B` by construction. If it also avoids `C`, every internal vertex lies in `R`, giving (1). Otherwise split at its first/last `C` hits to obtain the `B->C` and `C->A` pieces in (2). Because `Q` is the direct arc `q->a` and `W` avoids both endpoints, case (1) is vertex-disjoint from `Q`. QED.

## Consequence — the unpaid implication is narrower

The current hard branch cannot be closed by recycling the same four ports. A legal two-cycle exchange must obtain at least one of:

- enough **fresh-port connector rank** to reach two vertex-disjoint connectors in each direction, followed by the still-required support-order splice;
- a **same-support bypass/chord cycle** so that one replacement cycle need not be mixed;
- a **cycle in the exchanged remainder** after forming one mixed cycle; or
- an exchange routed through the **third packed support `C`**, as forced by Lemma 2 when port-avoidance cannot freshen the direct reverse connector.

Thus the first source-valid next problem is no longer “splice the coalesced four-port pair somehow.” It is the sharper `BT4-FRESH-PORT-OR-C-WALL` implication: in the lead's exact clean heavy-triangle state, use the seven-outdegree/arc-domination budget to show that the port-avoiding path from Lemma 2 either combines with a genuinely endpoint-disjoint forward connector to give a legal two-cycle exchange, or that the resulting `B->C->A` mediation forces a strict packing decrease / exchanged-remainder cycle / SIX exit.

The separate global SIX, bounded F2/F3 short-support, and seven-remainder pinwheel debts remain open. No full BT4 proof or novelty claim is made.

## Status label

`ESSENTIAL_STEP_APPLIED`: the current coalescence debt is reduced to an exact connector-rank/fresh-port or third-support wall, and a false disjointness-preserving splice inference is ruled out before it can enter the proof chain.
