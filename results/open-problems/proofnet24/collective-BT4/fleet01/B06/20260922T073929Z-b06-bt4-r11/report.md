# BT4 B06 report — parity-mismatch rank-two linkage collapse

Run: `20260922T073929Z-b06-bt4-r11`  
Campaign: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Target: genuine Bermond--Thomassen `k=4`  
Role: directed rerouting/linkage lemmas for the lead deficient packing  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact inherited state consumed

I use the latest complete campaign-lead state from fleet02/B04, candidate `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1` (scientific commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`, report blob `713053330313bf5906035c7bfd5841eb4e6b88ef`). Its inherited normal form is a hypothetical oriented exact-outdegree-seven counterexample `D`, arc-dominated and 3-vertex-strong, together with a lexicographically chosen three-cycle packing `(A,B,H)` minimizing total packed order and then maximizing the number of arcs in the acyclic remainder `R`. Packed cycles are chordless. In the live heavy-triangle cage, `|R|=4` and the distinguished old remainder sink is `x`.

The lead's corrected four-port theorem says that the clean mixed state emits a genuine packed-to-packed `CROSS` path with all internal vertices in `R`, or a distinct-port same-support `BYPASS` with the minimum-packing tax. The remaining lead debt is to splice the resulting interfaces, including coalesced old-port outputs, rather than to pretend a cross already is a fourth cycle.

The named OTHER-account theorem applied here is fleet04/B05 `BT4-BIDIRECTIONAL-RANK2-ORDER-WALL-v1` (scientific report blob `47bb1d2b3a2d01f6821e639310290557b3a54bc2`, shared handoff blob `f553a1086caaea875705c6f8c5d3f268bda1d3c3`). After excluding third-support mediation and intersecting opposite connectors, it supplies two vertex-disjoint `A->B` connectors

`F_i : alpha_i -> ... -> beta_i`, `i=1,2`,

and two vertex-disjoint `B->A` connectors

`G_j : gamma_j -> ... -> delta_j`, `j=1,2`,

whose interiors lie in `R-{x}`; after the intersection-collapse output is excluded, all four connector interiors are pairwise disjoint. When the four endpoints on each support are distinct and alternate by direction type, each support has a unique pairing parity that makes the two directed support-return arcs disjoint. If the `A` and `B` parities agree, fleet04/B05 already constructs two vertex-disjoint mixed replacement cycles and gives its exact support-omission/interior-usage tax. Its explicit remaining combinatorial wall included disagreement of those two parities.

I also use fleet04/B06 `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1` (shared blob `47d7e7c2fd312fd647604bf61113c46fd980a237`) for the fact that an opposite-direction interior intersection is already converted into a same-support bypass or bounded short-support output, so the parity analysis may be performed in the pure pairwise-interior-disjoint state.

## 2. Compact conditional end-to-end route

The current conditional proof architecture is:

1. Reduce a hypothetical BT4 counterexample to the inherited exact-seven oriented, arc-dominated, 3-vertex-strong normal form and choose the minimum three-cycle packing `(A,B,H)` with acyclic remainder.
2. The lead's sink/fan reductions split into `SIX` and global `NO-SIX`; the heavy-triangle long-support branch produces a clean four-port interface and, by the latest lead theorem, a genuine `CROSS/BYPASS` object.
3. Fleet04/B05 upgrades the pure two-support interface to rank two in both directions. Opposite-interior intersections are already useful by fleet04/B06. With distinct alternating ports, parity agreement gives two legal mixed replacement cycles.
4. The theorem below pays the *parity-disagreement* part of the rank-two order wall: disagreement itself forces another `CROSS/BYPASS` interface (or the forbidden four-pack) via one canonical four-connector directed cycle and the genuine `k=3` deletion theorem.
5. Thus a complete BT4 proof no longer needs an independent parity-mismatch case. The live local order debt is reduced to endpoint collisions/nonalternation and then the already-known splice/exchange accounting for the compatible pair. Global `SIX`, bounded F2/F3, and support-carried larger-remainder debts remain separate.

No legal two-cycle replacement is counted here as BT4 closure.

## 3. First essential missing implication attacked

### Candidate `BT4-RANK2-PARITY-MISMATCH-LIFT-v1`

Assume the rank-two pure `A,B,R` state above. Assume further:

- the four ports on each of `A` and `B` are distinct;
- source/return types alternate on both supports;
- the four connector interiors are pairwise disjoint and lie in `R-{x}`;
- the unique disjoint pairing parity on `A` and the unique disjoint pairing parity on `B` disagree.

Then one of the following occurs:

1. `D` already has four vertex-disjoint directed cycles; or
2. there is a genuine packed-to-packed `CROSS` path whose internal vertices all lie in `R`; or
3. there is a genuine distinct-port same-support `BYPASS` whose internal vertices all lie in `R`, carrying the exact minimum-packing tax `ell >= d_T(c,w)`.

Consequently, in a residual branch in which a new `CROSS/BYPASS` is by definition sent back to the established lead splice frontier, pairing-parity disagreement is not a terminal order obstruction. If the parities agree, fleet04/B05 supplies the legal two-cycle splice. Hence the rank-two order wall reduces to endpoint collision/nonalternation plus the exchange/tax closure of the resulting splice.

## 4. Proof

Relabel the two reverse connectors if necessary so that on `A` the unique disjoint pairing is the identity. Thus the two directed support arcs

`A[delta_1,alpha_1]`, `A[delta_2,alpha_2]`

are vertex-disjoint. Since the parity on `B` is opposite, the two vertex-disjoint directed arcs there are

`B[beta_1,gamma_2]`, `B[beta_2,gamma_1]`.

Consider

`K = F_1 + B[beta_1,gamma_2] + G_2 + A[delta_2,alpha_2]
       + F_2 + B[beta_2,gamma_1] + G_1 + A[delta_1,alpha_1]`.

All concatenations are direction-consistent. The two chosen `A` arcs are disjoint, the two chosen `B` arcs are disjoint, all four connector interiors are pairwise disjoint, and connector interiors avoid the packed supports. All packed ports are distinct. Hence `K` is a genuine simple directed cycle. It is disjoint from the third packed cycle `H`, and because all connector interiors lie in `R-{x}`, the old sink `x` is not on `K`.

Suppose there is no four-pack. If every vertex outside `K` had at most two outneighbors on `K`, then deleting `K` from the exact-outdegree-seven digraph would leave minimum outdegree at least five. The genuine `k=3` theorem would then give three pairwise vertex-disjoint directed cycles in `D-K`; together with `K` these would be four disjoint directed cycles, contradiction. Therefore there is a vertex

`v notin V(K)`

with at least three distinct outneighbors on `K`.

We show that such a witness always yields `CROSS/BYPASS`.

### Case A: `v` is on the third packed support `H`

Every packed vertex of `K` lies on `A` or `B`. A hit from `v` to such a vertex is already a cross-support arc. If instead a hit lands at an internal remainder vertex of one of `F_i,G_j`, follow the directed suffix of that connector to its packed endpoint. This gives a directed path from `H` to `A` or `B` with all internal vertices in `R`, again a genuine `CROSS`. Thus this case is paid immediately.

### Case B: `v` lies in the old remainder `R`

The cycle `K` uses only vertices of `R-{x}` in its connector interiors. Since `|R|=4`, if `v!=x` then both `v` and `x` are outside `K`, so `K` contains at most two remainder vertices. Three distinct hits therefore include a packed target `w` on `A` or `B`.

If `v=x`, old-remainder sinkhood gives no arc from `x` to another vertex of `R`, so every hit of `x` on `K` is packed. Thus in all cases there is a direct arc

`v -> w`

with `w` packed.

Apply the inherited arc-domination ladder exactly as in the lead's four-port witness-lift theorem. Repeatedly dominate the arc into the fixed packed target `w`. The chain cannot remain forever in finite acyclic `R`, so it terminates at a packed apex `c` and gives a directed path

`J : c -> R -> ... -> v -> w`

whose internal vertices all lie in `R`. The endpoints are distinct because the terminal domination step also gives the direct arc `c->w`, and loops are forbidden. If `c,w` lie on different packed supports, `J` is `CROSS`. If they lie on the same support `T`, `J` is a distinct-port same-support bypass. Replacing the forward support segment `T[c,w]` by `J` while keeping the other two old cycles shows, by global minimum of packed order,

`ell(J) >= d_T(c,w)`.

Thus this case yields the advertised taxed bypass or cross.

### Case C: `v` lies on `A`

Chordlessness of the packed cycle `A` implies that `v` has at most one outneighbor on `A`, namely its support successor. Since `v` has at least three hits on `K`, at least two hits are not own-support hits. Any one such hit already suffices:

- if it is a packed vertex of `B`, the hit is a direct `A->B` cross;
- if it is internal to an `A->B` connector `F_i`, follow the suffix of `F_i` from that hit to `beta_i`; together with the hit from `v`, this is an `A->B` packed-to-packed path with all internal vertices in `R`, hence `CROSS`;
- if it is internal to a `B->A` connector `G_j`, follow the suffix to `delta_j`; this is a same-support path from `v` to the distinct packed vertex `delta_j`, with all internal vertices in `R`, hence a genuine `BYPASS` and, by minimum packing, it satisfies the same tax `ell>=d_A(v,delta_j)`.

There are no other vertices of `K`. Therefore `CROSS/BYPASS` is forced.

### Case D: `v` lies on `B`

This is symmetric. A hit to `A`, or to an internal vertex of a `B->A` connector `G_j`, gives `CROSS`; a hit to an internal vertex of an `A->B` connector `F_i` gives a same-support `B`-bypass; and chordlessness allows at most one own-support hit. Again `CROSS/BYPASS` is forced.

These cases exhaust `V(D)-V(K)`. This proves `BT4-RANK2-PARITY-MISMATCH-LIFT-v1`.

## 5. What this pays and what it does not

The result pays one exact part of fleet04/B05's `BT4-BIDIR-ORDER-WALL-CLOSE-v1`: **pairing-parity mismatch is no longer an independent terminal geometry**. In the endpoint-distinct, type-alternating rank-two state, either the parities match and the B05 two-cycle construction applies, or they mismatch and the canonical four-connector cycle above forces a `CROSS/BYPASS` output (possibly coalesced at old ports after a remainder domination lift), returning to the lead's existing splice frontier.

This does not pay:

- endpoint collisions between opposite connector families;
- nonalternating source/return order on either packed support;
- the distinction between a legal neutral replacement and a strict lexicographic improvement once the two-cycle splice exists;
- `SIX`, bounded F2/F3, or the support-carried larger-remainder branches.

The first local unpaid implication is therefore narrower than the B05 order wall:

`BT4-RANK2-COLLISION-NONALTERNATION-CLOSE-v1` — in the same four-remainder heavy-triangle normal form, after opposite-interior intersections and parity mismatch have been routed into the existing bypass/cross frontier, show that an endpoint collision or nonalternating port order forces either a legal two-cycle replacement with useful strict/neutral exchange information, a cyclic exchanged remainder, a compatible bypass family, `SIX`, bounded short support, or the fourth directed cycle.

A natural next move is to use a shortest mixed return cycle through the colliding/nonalternating ports and repeat the lead's deletion-witness lift, but with the rank-two unused connector treated as an additional forced chord rather than assuming it is disjoint.

## 6. Honest status

Outcome: `ESSENTIAL_STEP_APPLIED`. The pairing-parity component of the rank-two order wall is reduced to already-existing `CROSS/BYPASS` machinery or the B05 compatible splice. BT4 itself remains `OPEN_NOT_PROVED`; no novelty or publication claim is made. No computation was required. No authenticated brain retrieval/context use occurred.
