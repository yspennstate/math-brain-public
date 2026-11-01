# Addendum — nonalternating-port gap freshening

This is a second same-run strengthening of the rank-two order analysis. It uses the inherited 3-vertex-strong normal form and fleet04/B05's pairwise-interior-disjoint rank-two connector state.

## Candidate `BT4-RANK2-NONALTERNATION-GAP-FRESHEN-v1`

Let

`F_1,F_2 : A -> B`, with packed endpoints `alpha_i in A`, `beta_i in B`,

and

`G_1,G_2 : B -> A`, with packed endpoints `gamma_j in B`, `delta_j in A`,

be the pure rank-two state: connector interiors lie in `R-{x}` and are pairwise disjoint after the already-paid opposite-intersection branch. Assume all relevant packed endpoints are distinct; endpoint collisions are handled by `BT4-RANK2-ENDPOINT-COLLISION-LIFT-v1`.

On `A`, call the two open directed intervals between `delta_1,delta_2` the **return gaps**. On `B`, call the two open directed intervals between `gamma_1,gamma_2` the **source gaps**. The `A` endpoint types alternate exactly when `alpha_1,alpha_2` lie in different return gaps; the `B` endpoint types alternate exactly when `beta_1,beta_2` lie in different source gaps.

Then:

1. If `A` is nonalternating, `B` is alternating, and the `A` return gap containing neither `alpha_i` has an internal vertex, the state can be rerouted to a rank-two state alternating on **both** supports, unless a genuine `CROSS`, a distinct-port remainder `BYPASS`, or third-support mediation is produced first.
2. If both `A` and `B` are nonalternating and both empty gaps have internal vertices, the same conclusion holds.

Combining this with the main parity theorem and the endpoint-collision addendum, the only genuinely new cyclic-order obstruction left by fleet04/B05 is therefore a **consecutive-port wall**: on at least one nonalternating support, the gap containing neither endpoint of the other direction is empty of internal vertices, so its two opposite-direction ports are consecutive on that packed cycle.

The symmetric statements with `A,B` interchanged hold as well.

## 1. One-sided nonalternation

Assume `alpha_1,alpha_2` lie in the same return gap on `A`. Relabel so the other open gap is

`I_A = A(delta_1,delta_2)`

and contains no `alpha_i`. Assume `I_A` contains a vertex `u`.

Delete `delta_1,delta_2`. By inherited 3-vertex-strongness, `D-{delta_1,delta_2}` is strongly connected, so there is a directed path from `u` to `B`. Stop at the first `B` vertex and let `s` be the last `A` vertex before it.

If before that first `B` hit the path leaves `I_A` and later reenters `A` outside `I_A`, consider the first such reentry. Because both boundary vertices `delta_1,delta_2` are deleted, the transfer cannot occur by simply following the support cycle across a boundary. Between two consecutive `A` hits the path either meets `H`, giving a genuine cross/third-support mediation, or has all internal vertices in `R`, giving a distinct-port same-support `A`-bypass. Hence, after excluding already-useful outputs, the last `A` vertex `s` remains in `I_A`.

Trim from `s` to the first `B` hit `b`. If this trimmed path meets `H`, it is already a cross through the third support. Otherwise its internal vertices lie in `R`. If it meets an interior vertex of one of the reverse connectors `G_j`, take the first such intersection and then follow the suffix of `G_j` to `delta_j`; this gives a same-support `A`-bypass with remainder interior. Thus, outside the useful branches, we obtain an `A->B` connector

`Q : s -> R -> b`

whose source `s` lies in the previously empty return gap and which is internally disjoint from both `G_1,G_2`.

Now assume `B` was already alternating, so `beta_1,beta_2` lie in opposite `gamma`-gaps.

- If `Q` is internally disjoint from both old `F_i`, choose the old `F_k` whose endpoint `beta_k` lies in the `gamma`-gap opposite `b`. Then `Q,F_k` are disjoint; their `A` sources lie in opposite return gaps and their `B` targets lie in opposite source gaps.
- Otherwise let `r` be the first intersection of `Q` with `F_1 union F_2`, say `r in F_i`, and let `k!=i`. The spliced connector

  `Q* = Q[s,r] + F_i[r,beta_i]`

  is internally disjoint from `F_k`: the prefix of `Q` meets neither old `F` before `r`, and the old `F` interiors are disjoint. Its source `s` is in the empty `A` gap while `alpha_k` is in the old occupied gap; its target `beta_i` is in the `B` gap opposite `beta_k`. Hence `Q*,F_k` give a rank-two `A->B` family alternating on both supports.

Any endpoint collision created by this rerouting is already paid by the collision-lift theorem. Any opposite-direction interior intersection is already paid by fleet04/B06. Thus one-sided nonalternation with a nonempty empty gap reduces to the alternating state.

## 2. Two-sided nonalternation

Now suppose also `beta_1,beta_2` lie in the same `gamma`-gap on `B`. Relabel so the empty open gaps are

`I_A=A(delta_1,delta_2)`,

`I_B=B(gamma_1,gamma_2)`,

and assume each contains an internal vertex. Choose `u in I_A` and `w in I_B`.

Delete **two** boundary vertices: `delta_2`, the forward exit from `I_A` into the occupied `A` gap, and `gamma_1`, the forward entry from the occupied `B` gap into `I_B`. By 3-vertex-strongness the remaining digraph is strongly connected, so choose a directed path `P` from `u` to `w` avoiding those two vertices.

Let `b` be the first `B` vertex on `P` and `s` the last `A` vertex before `b`.

### Source-gap forcing

If `s` were outside `I_A`, then starting from `u in I_A` the path would have to leave `A` and reenter the occupied `A` gap: the forward support exit `delta_2` has been deleted. The first such transfer is either a path through `H`/the other packed support, producing a cross/third-support interface, or a same-support `A`-bypass with interior in `R`. Hence outside useful outputs, `s in I_A`.

### Target-gap forcing

If the first `B` hit `b` lay in the occupied `B` gap, then to reach `w in I_B` the path could not stay on the directed support cycle, because the boundary vertex `gamma_1` through which that occupied gap enters `I_B` has been deleted. It must leave `B` and later reenter `B` in `I_B`. The first such transfer either meets `A` or `H`, giving a cross/third-support interface, or has remainder-only interior and is a same-support `B`-bypass. Hence outside useful outputs, `b in I_B`.

Trim to

`Q : s -> R -> b`.

As in the one-sided case, an intersection of `Q` with a reverse connector `G_j` immediately gives a same-support bypass; so in the unresolved branch `Q` is internally disjoint from `G_1,G_2`. Its endpoint bit-pair is `(empty A gap, empty B gap)`, while each old `F_i` has bit-pair `(occupied A gap, occupied B gap)`.

It remains only to remove possible same-direction intersections with `F_1,F_2`.

- If `Q` is disjoint from some `F_i`, then `Q,F_i` themselves are the desired disjoint pair with opposite gap bits on both supports.
- Suppose `Q` meets both old paths. Let `r` be its first intersection with `F_1 union F_2` and `t` its last.
  - If `r` and `t` lie on different old paths, say `r in F_i`, `t in F_j`, `i!=j`, then

    `P_1 = Q[s,r] + F_i[r,beta_i]`,

    `P_2 = F_j[alpha_j,t] + Q[t,b]`

    are vertex-disjoint. The first/last choice makes the two `Q` pieces avoid both old paths outside the displayed switches, and `F_i,F_j` are disjoint. Their source/target gap bits are respectively `(empty,occupied)` and `(occupied,empty)`, so the selected endpoints alternate on both supports.
  - If `r,t` lie on the same old path `F_i`, replace the middle of `Q` by the old segment `F_i[r,t]`:

    `Q' = Q[s,r] + F_i[r,t] + Q[t,b]`.

    Because `r,t` are the first and last intersections with the union, `Q'` is simple and is disjoint from the other old path `F_k`. Thus `Q',F_k` have bit-pairs `(empty,empty)` and `(occupied,occupied)`, again alternating on both supports.

So whenever both empty gaps contain vertices, two-sided nonalternation can be freshened to the fully alternating rank-two state.

## 3. Transfer to the existing parity/splice frontier

After the freshening above, all endpoint types alternate on both supports. If the unique support pairing parities agree, fleet04/B05 constructs two legal mixed replacement cycles and supplies its exact omission/interior tax. If the parities disagree, `BT4-RANK2-PARITY-MISMATCH-LIFT-v1` routes the state into the lead `CROSS/BYPASS` frontier. Endpoint collisions are routed there by the first addendum, and opposite-direction interior intersections by fleet04/B06.

Therefore the rank-two cyclic-order problem has been reduced further to:

`BT4-RANK2-CONSECUTIVE-PORT-WALL-v1` — a nonalternating support for which the gap containing neither opposite-direction port has no internal vertex, so the two boundary ports are consecutive on the packed directed cycle; plus the separate strict/neutral exchange accounting after a legal splice.

This is not a full BT4 proof. Global `SIX`, bounded F2/F3 and larger-remainder support-carried branches remain explicit.
