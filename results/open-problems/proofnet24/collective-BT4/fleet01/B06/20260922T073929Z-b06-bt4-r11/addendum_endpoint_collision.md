# Addendum — endpoint-collision collapse in the same rank-two state

This addendum strengthens `BT4-RANK2-PARITY-MISMATCH-LIFT-v1` from the same run. It uses exactly the same inherited four-remainder heavy-triangle normal form and the same fleet04/B05 rank-two connector family.

## Candidate `BT4-RANK2-ENDPOINT-COLLISION-LIFT-v1`

Let

`F_i : alpha_i -> R -> beta_i`  (`A->B`),

`G_j : gamma_j -> R -> delta_j`  (`B->A`)

be two opposite connector families whose interiors are pairwise disjoint and lie in `R-{x}`, where `|R|=4` and `x` is the old remainder sink. Suppose an opposite-family endpoint collision occurs on one packed support; for example

`alpha_i = delta_j = c in A`.

Then either `D` already has four vertex-disjoint directed cycles, or the collision state emits a genuine packed-to-packed `CROSS` path with remainder interior, or a distinct-port same-support remainder `BYPASS` with the exact minimum-packing tax.

Consequently endpoint collision, like pairing-parity mismatch, is not an independent terminal rank-two order obstruction. After routing both outputs back into the established lead `CROSS/BYPASS` frontier, the only genuinely new cyclic-order part of fleet04/B05's wall is **distinct-port nonalternation**.

## Proof

Form the directed collision cycle

`C = F_i + B[beta_i,gamma_j] + G_j`.

The last vertex of `G_j` is `delta_j=c=alpha_i`, the first vertex of `F_i`, so the concatenation closes. Pairwise interior disjointness and the fact that connector interiors avoid packed supports make `C` a genuine simple directed cycle. It meets `A` only in the single packed vertex `c`; it meets `B` in one directed support segment; all other vertices of `C` lie in `R-{x}`. In particular `C` is disjoint from `H` and avoids the old sink `x`. The degenerate possibility `beta_i=gamma_j` merely makes the `B` support segment trivial and causes no problem.

If every vertex outside `C` had at most two outneighbors on `C`, then deleting `C` would leave minimum outdegree at least five, and the genuine `k=3` theorem would supply three disjoint directed cycles in `D-C`; together with `C` this is the forbidden four-pack. Hence there exists

`v notin V(C)`

with at least three distinct outneighbors on `C`.

We again classify `v`.

1. `v in H`: every packed hit is a direct cross to `A` or `B`; a hit to a connector-interior vertex followed along the connector suffix is an `H`-to-`A/B` packed-to-packed path with all internal vertices in `R`. Thus `CROSS`.

2. `v in R`: the cycle avoids `x`. If `v!=x`, then both `v` and `x` are outside `C`, so with `|R|=4` the cycle contains at most two remainder vertices; three hits include a packed target. If `v=x`, sinkhood forbids hits into `R`, so again there is a packed target. The lead's fixed-target domination ladder lifts that packed hit to a packed-to-packed remainder path. Different support endpoints give `CROSS`; same-support distinct endpoints give `BYPASS`, and global minimum yields `ell>=d`.

3. `v in A`: the collision cycle contains only the one `A` vertex `c`. Chordlessness permits at most one own-support hit. Any hit on `B` is a direct cross; any hit in the interior of `F_i` followed to `beta_i` is an `A->B` cross; any hit in the interior of `G_j` followed to `c` is a distinct-port same-support `A`-bypass. Since there are at least three hits, one of these useful alternatives occurs.

4. `v in B`: chordlessness permits at most one hit on the `B` support segment of `C`. A hit on `c` is a direct `B->A` cross; a hit in the interior of `G_j` followed to `c` is a `B->A` cross; a hit in the interior of `F_i` followed to `beta_i` is a distinct-port same-support `B`-bypass. Again a useful output is forced.

These cases exhaust all possible locations of `v`. The collision-on-`B` statement is symmetric.

## Combined local frontier

Combining this addendum with the main report and fleet04/B05 gives the following exact rank-two cyclic-order reduction:

- opposite-interior intersection -> existing same-support bypass / bounded output (fleet04/B06);
- endpoint collision -> `CROSS/BYPASS` (this addendum);
- distinct endpoints + alternating types + matching parity -> two legal mixed replacement cycles (fleet04/B05);
- distinct endpoints + alternating types + mismatching parity -> `CROSS/BYPASS` (main report);
- therefore the only remaining *new cyclic-order geometry* is distinct-endpoint **nonalternation on at least one support**, plus the already-separate exchange/tax closure after a legal splice.

The next candidate is correspondingly sharpened to `BT4-RANK2-NONALTERNATION-CLOSE-v1`.

BT4 remains `OPEN_NOT_PROVED`; this addendum does not claim that a `CROSS/BYPASS` alone closes the target.
