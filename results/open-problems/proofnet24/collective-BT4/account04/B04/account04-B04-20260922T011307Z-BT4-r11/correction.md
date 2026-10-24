# BT4 account04/B04 — correction to `BT4-SINKPORT-v1`

Run: `account04-B04-20260922T011307Z-BT4-r11`  
Corrected candidate: `BT4-SINKPORT-v1.1`  
Outcome: `ESSENTIAL_STEP_APPLIED_WITH_CORRECTION`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

This immutable addendum corrects one overreach in the same run's `report.md` while preserving the sound sink-type, unique-port, domination-cycle, exchange-wall and Menger deductions.

## The overreach

In `report.md`, Lemma 3 correctly fixes a **particular** directed cycle `Q subseteq N^-(x)` and observes that `Q` meets the two light packed cycles in at most one vertex each. Its case P1 means that this particular `Q` meets only one light cycle, say `B`, at its unique B-port `b`.

P1 by itself does **not** imply that the other light cycle `C` has no different vertex `c` with `c->x`; such a C-port could simply be absent from the chosen cycle `Q`.

Therefore the sentence in Lemma 6 saying that a dominator of `x->b^{++}` cannot lie on `C` "because P1 means no vertex of C sends to x" is invalid. The consequent unconditional assertions `d in R`, the fork `d->{x,b^{++}}` with `d in R`, and the unconditional B-to-B bypass (16) are quarantined as stated.

Nothing in Lemmas 1--5 depends on that sentence.

## Corrected Lemma 6 — a one-port domination cycle forces either a cross-light dominator or an R-fork

Retain the P1 hypotheses for the chosen cycle `Q`: `Q` meets the packed cycles only at the unique B-port `b`, and

`N^+(x) intersect B = {b^+,b^{++}}`.

Arc domination of `x->b^{++}` yields a vertex `d` with

`d->x` and `d->b^{++}`.                                    (13')

As before, `d` cannot lie on the heavy cycle `H`, because `H not->x`. It cannot lie on `B`: the unique B-port is `b`, while chordlessness excludes `b->b^{++}`. Thus the exact conclusion is

`                         d in R union V(C)`.                 (14')

This gives a genuine dichotomy.

### D-R: remainder fork

If `d in R`, then the sink geometry contains the canonical fork

`                         d -> {x,b^{++}}`.                   (15')

This is the R-fork originally intended by Lemma 6.

### D-C: cross-light dominator

If `d in C`, then `d->x`, so Lemma 2 makes `d` the **unique C-port**, and the C-fan is exactly

`N^+(x) intersect C = {d^+,d^{++}}`.

In addition, domination supplied the cross-light arc

`                         d -> b^{++}`.                       (16')

Thus failure of the R-fork does not leave an unstructured case: it produces the second light return port together with a directed cross-light attachment into the B two-fan.

The symmetric statement holds after swapping `B,C`.

## Global return-port split

Because some directed cycle exists in `N^-(x)`, at least one of the two light cycles has a direct return port. Lemma 2 proves each light cycle has at most one. Hence every no-six sink has exactly one of the following global return patterns:

- **G1:** exactly one light cycle has a return port;
- **G2:** both light cycles have unique return ports.

In G1, every directed cycle in `N^-(x)` necessarily uses the same unique light port, so the P1 replacement-wall argument applies to any such cycle, and corrected Lemma 6 is automatically in branch D-R. Therefore G1 genuinely has the R-fork `d->{x,b^{++}}`.

In G2, write the two ports as `b in B` and `c in C`. Their fans are the exact consecutive pairs

`N^+(x) intersect B={b^+,b^{++}}`,
`N^+(x) intersect C={c^+,c^{++}}`.

A directed cycle in `N^-(x)` may meet one or both ports; one must not assert without proof that a single such cycle necessarily meets both. For any one-port B-cycle, however, corrected Lemma 6 gives either an R-fork or the explicit cross-light arc `c->b^{++}`. Symmetrically, a one-port C-cycle gives either an R-fork or `b->c^{++}`.

So the sound no-six structural tree is:

1. exact sink fan `3|2|2`;
2. global return pattern G1 or G2;
3. in G1, one-port replacement wall + two Menger excursions + forced R-fork;
4. in G2, exact unique ports and exact consecutive two-fans on both light cycles; any one-port domination cycle yields an R-fork or a cross-light dominator arc, while a domination cycle using both ports is already a cross-light cycle.

## Correction to the predecessor-chain refinement

The original equation (16), claiming an unconditional path

`b -> R -> ... -> d -> b^{++}`,

also depended on assuming every cycle in `N^-(x)` used B rather than C. The correct statement is:

If `d in R`, repeated use of arc domination inside `N^-(x)` yields a directed cycle `Q_d subseteq N^-(x)` and a directed path from `Q_d` to `d`. The cycle `Q_d` meets only light ports. If it meets B only, one obtains the intended B-to-`b^{++}` R-internal bypass. If it meets C (with or without B), one instead obtains a cross-light path from the C-port through `R` to `d->b^{++}`. This is still partner-compatible structure, but the source port must be retained explicitly.

## Surviving new results

The following deductions from `report.md` are unchanged and sound:

- global NO-SIX forces every remainder sink to fan type `(3,2,2)`;
- the heavy 3-fan cycle has no return to the sink;
- each light cycle has at most one direct return port, and any port forces the exact consecutive two-fan `{b^+,b^{++}}`;
- every domination cycle in `N^-(x)` meets only light ports and has one or two packed vertices;
- for a one-port domination cycle `Q` on `B`, replacing `B` by `Q` gives `|Q|>=|B|`, an acyclic exchanged remainder `R'`, and the reachability wall that no vertex of `B-b` reaches `x` in `R'`;
- 3-vertex-strongness then forces two internally vertex-disjoint `b^-`-to-`x` paths in `D-b`, each leaving `R'` through the currently packed objects;
- corrected Lemma 6 upgrades that branch further to D-R or D-C rather than to an unconditional R-fork.

## Remaining essential implication

Full BT4 remains open. The next splice step may now be attacked separately in:

- **G1:** one light return only, where the exchanged-DAG reachability wall, two Menger excursions and R-fork are all simultaneously present;
- **G2:** two unique light ports, where exact consecutive two-fans hold on both light cycles and domination supplies either cross-light cycles/arcs or R-forks;
- the independently preserved six-fan branch, split by witness support and handled with the existing two-cycle bypass/linkage machinery.

No target-level proof or novelty claim is made.
