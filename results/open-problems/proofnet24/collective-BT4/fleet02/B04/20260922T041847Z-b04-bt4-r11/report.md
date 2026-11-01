# BT4 fleet02/B04 — heavy-triangle three-hit spill and predecessor-chain collapse

Run: `20260922T041847Z-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-HT-PREDECESSOR-SPLICE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs, and therefore digons, are allowed in the source problem.


The external theorem boundary remains unchanged:

- Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948, submitted 13 August 2026, explicitly says the genuine conjecture is unresolved for all `k>=4` and proves only the one-reversed-arc relaxation. I do not use that relaxation as a directed-cycle theorem.
- Lichiardopol--Por--Sereni, SIAM J. Discrete Math. 23 (2009), 979--992, prove the genuine `k=3` theorem `delta^+>=5 => 3` disjoint directed cycles and the strengthened `k=2` theorem allowing at most two outdegree-two exceptions to minimum outdegree three.

Exact live team mathematics consumed:

1. campaign-lead controlling frontier addendum, fleet02/B04 run `20260922T031823Z-a02-b04-bt4-r11`, blob `28fe813aa044e57bbb3c6934a9ea76525bc04968`; its live gap is `SC+`, the genuine two-cycle/strict-reduction splice after canonical sink-cross geometry is present;
2. named OTHER-account partner fleet03/B05, `BT4-SC2-THIRD-PORT-v1`, run `20260922T034032Z-fleet03-B05-BT4-r13`, report blob `2d667b4e80a54a16bfd9b551baa4cae55ddf93ae`; I apply its source-valid observation that every directed cycle in a BT4 counterexample has an external three-hit witness, and keep its long-light third-port result as a compatible splice input;
3. newer compatible fleet01/B04 `BT4-MCR-v6-reciprocal-staircase`, run `20260922T034517Z-b04-bt4-r11`, report blob `bdaeb50e90bee25dff6fa19a184d7f42f7e5b29f`, which makes the canonical no-six sink cross reciprocal at the interface level and narrows the remaining issue to packed-port compatibility;
4. the controlling fleet02/B04 heavy-fan correction, blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`: a cycle-supported witness heavy on `A` but receiving no arc from `A` forces a genuine cross-packed transition into `A` by a domination ladder.

No peer outcome label is used as proof. The theorem statements above are the consumed content.

## Inherited normal form

Assume for contradiction that BT4 is false and work in the campaign's inherited minimum-counterexample normal form. Thus `D` is oriented and every vertex has outdegree exactly seven; `(H,S,U)` is a globally minimum-total packing of three directed cycles; the remainder

`R = V(D) \ (V(H) union V(S) union V(U))`

is nonempty and acyclic; the packed cycles are chordless; every arc is dominated; and `D` is 3-vertex-strong.

In the persistent global `NO-SIX` sink branch, a sink `x` of `D[R]` has fan pattern `(3,2,2)` up to relabeling, and its heavy cycle `H` sends no arc to `x`. The previous lead addendum reduced the four-remainder branch to three configurations, one of which is the heavy-triangle saturation state. This run attacks that state directly with the named partner's external-three-hit mechanism.

## Compact conditional end-to-end proof after the current team reductions

A complete proof follows once the remaining port-splice closures are established.

1. Reduce a hypothetical counterexample to the exact-seven oriented, arc-dominated, 3-vertex-strong normal form above with a globally minimum three-cycle packing and acyclic remainder.
2. Pair deletion gives the campaign's `SIX` / `NO-SIX` alternatives. Close the separate `SIX` interface by its ladder/ray exchange mechanism.
3. In `NO-SIX`, choose a remainder sink. Existing work gives the exact `(3,2,2)` fan pattern, a direct light inport, the canonical length-two sink cross, and a reciprocal cross avoiding the sink. The neutral source pivot gives the x-free heavy-cross family and additional five-witness structure.
4. In the long-light same-port opposite-cross residual, the named partner `BT4-SC2-THIRD-PORT-v1` forces a third packed port or a quantified same-support bypass. Thus the remaining obstruction is an actual packed-port splice, not existence of a return interface.
5. In the special four-remainder heavy-triangle branch, the theorem below removes the bare triangle as a terminal object: it forces either multiple light three-dominators or an aligned predecessor chain carrying two exact five-witnesses; in the split-heavy subcase, two heavy inports are impossible, so a no-inport branch is forced and the heavy-fan domination escape supplies an additional cross-packed transition.
6. Therefore BT4 follows if the remaining reciprocal/third-port interfaces, the same-heavy collision interface, the new multi-light-dominator interface, and the separate `SIX` interface are each converted into one of: two vertex-disjoint replacement cycles, a strict decrease of the globally minimum three-packing, a directed cycle in the exchanged remainder, or a fourth disjoint directed cycle.

The theorem below pays a genuine part of item 5 and narrows the first missing implication in item 6.

## Lemma 1 — source-valid external three-hit witness

Let `C` be any directed cycle in a BT4 counterexample `D`. Then some vertex outside `C` has at least three outneighbors on `C`.

Indeed, otherwise every vertex of `D-C` loses at most two outneighbors on deleting `C`, so `delta^+(D-C)>=5`. The genuine `k=3` theorem gives three disjoint directed cycles in `D-C`; together with `C` they give four disjoint directed cycles in `D`, contradiction.

This is exactly the fleet03/B05 source-valid deletion input; no relaxed cycle is used.

## Heavy-triangle notation

Assume the four-remainder `NO-SIX` heavy-triangle saturation state. Index modulo three so

`H = h_0 -> h_1 -> h_2 -> h_0`,

`R = {x,r_0,r_1,r_2}`,

and the saturation theorem gives, for each `i`,

`h_i -> r_i -> x -> h_i`.                                      (1)

Write

`T_i = h_i -> r_i -> x -> h_i`.                                (2)

Also `H not-> x`.

Apply Lemma 1 separately to each `T_i`.

## Lemma 2 — a remainder three-hit witness can only be the predecessor

Suppose a three-hit witness for `T_i` lies in `R`. It cannot be `x` or `r_i`, since those lie on `T_i`, so it is `r_j` for one of the other two indices and has

`r_j -> h_i`, `r_j -> r_i`, `r_j -> x`.                         (3)

It cannot be the successor `j=i+1`.

For if `r_{i+1}` satisfies (3), then

`A_i = r_{i+1} -> h_i -> h_{i+1} -> r_{i+1}`                    (4)

is a directed triangle. It is vertex-disjoint from `T_{i+2}`. Hence

`A_i, T_{i+2}, S, U`

are four pairwise vertex-disjoint directed cycles, contradiction.

Therefore every remainder three-hit witness for `T_i` must be the predecessor `r_{i-1}`.

If all three predecessor relations occurred, then (3) would contain

`r_2 -> r_0 -> r_1 -> r_2`,

a directed cycle in `R`, contradicting acyclicity. Consequently at least one `T_i` has a three-hit witness on a light packed cycle `S` or `U`. More sharply, if at most one predecessor relation occurs, then at least two of the three triangles have light three-hit witnesses.

This is already a nontrivial spill from the heavy triangle into the light packed supports.

## Lemma 3 — the maximal predecessor branch forces two exact five-witnesses

Assume exactly two predecessor relations occur. Rotate indices so the missing relation is the one for `T_0`. Then

`r_0 -> r_1, h_1, x`,
`r_1 -> r_2, h_2, x`,                                           (5)

while `T_0` has a light three-hit witness.

Let

`G = D - (S union U) = D[V(H) union R]`.

Because this is global `NO-SIX` for the pair `S union U`, every vertex of `G` has outdegree at least two.

### Terminal vertex

The vertex `r_2` already sends to `x`. Acyclicity/orientation exclude `r_2->r_0`, `r_2->r_1`, and `r_2->h_2`: the first creates an `R`-cycle using (5), the second is opposite `r_1->r_2`, and the third is opposite `h_2->r_2` from (1).

If `r_2->h_1`, then

`r_2 -> h_1 -> r_1 -> r_2`

and

`x -> h_0 -> r_0 -> x`

are two vertex-disjoint directed triangles. Together with `S,U` they give four disjoint cycles. Hence `r_2 not->h_1`.

Since `d_G^+(r_2)>=2`, the only remaining possibility is

`N_G^+(r_2) = {x,h_0}`.                                         (6)

In particular `d_G^+(r_2)=2` exactly.

### Two forced degree-two heavy vertices

The vertex `h_1` already has exactly the two displayed candidates `h_2,r_1` in `G`. Every other possible `G`-outneighbor except `r_2` is excluded by orientation or `H not->x`: `h_0->h_1`, `r_0->h_1`, and `h_1 not->x`. If the remaining arc `h_1->r_2` existed, then

`x -> h_1 -> r_2 -> x`

and

`h_0 -> r_0 -> r_1 -> h_2 -> h_0`

would be two vertex-disjoint directed cycles, again giving four together with `S,U`. Thus

`N_G^+(h_1) = {h_2,r_1}`.                                       (7)

Similarly, the only possible additional `G`-outneighbor of `h_2` beyond `h_0,r_2` is `r_0`. If `h_2->r_0`, then

`x -> h_2 -> r_0 -> x`

and

`h_0 -> h_1 -> r_1 -> r_2 -> h_0`

are disjoint directed cycles. Hence

`N_G^+(h_2) = {h_0,r_2}`.                                       (8)

Exact outdegree seven now gives

`|N+(h_1) intersect (S union U)| = 5`,
`|N+(h_2) intersect (S union U)| = 5`.                           (9)

Thus `h_1,h_2` are two cycle-supported exact five-witnesses on the heavy support `H`, each with only its support successor and the displayed single remainder exit in `G`.

This is substantially stronger than merely knowing that the heavy triangle exists.

## Lemma 4 — split-heavy double inports are impossible by simultaneous strict surgery

For `i=1,2`, let `A_i in {S,U}` be a heavy target of the five-witness `h_i`, so

`|N+(h_i) intersect A_i| >= 3`.                                 (10)

Assume the heavy targets split:

`A_1 != A_2`.                                                    (11)

Suppose, for contradiction, that both heavy target cycles send an arc into their corresponding witness. Choose

`s_i in A_i` with `s_i -> h_i`.                                 (12)

For each `i`, choose a fan target `y_i in N+(h_i) intersect A_i` minimizing the forward directed distance

`d_i = dist_{A_i}(y_i,s_i)`.

Because `D` is oriented, `h_i->s_i` is impossible, so `y_i!=s_i`. The at least three distinct fan targets in (10) therefore occupy at least three distinct positive distances in `{1,...,|A_i|-1}`. Hence

`d_i <= |A_i|-3`.                                               (13)

Now

`C_i = s_i -> h_i -> y_i -> A_i[y_i,s_i]`                       (14)

is a genuine directed cycle, and

`|C_i| = d_i+2 <= |A_i|-1`.                                    (15)

Because the heavy targets are the two different light cycles, `C_1` and `C_2` are vertex-disjoint. They are also disjoint from the untouched triangle

`T_0 = h_0 -> r_0 -> x -> h_0`.

Therefore `(C_1,C_2,T_0)` is a legal three-cycle packing with

`|C_1|+|C_2|+|T_0| <= (|S|-1)+(|U|-1)+3
                    = |S|+|U|+|H|-2`,

since `|H|=3`. This strictly contradicts global minimum of `(H,S,U)`.

Thus, in the split-heavy branch, **at least one heavy target sends no arc into its witness**.

Apply the controlling heavy-fan domination escape to that witness: a genuine cross-packed transition into its heavy light target follows, with all internal vertices in `R`.

If instead `A_1=A_2`, the two exact witnesses form the campaign's same-heavy support-pair interface and feed the previously proved interval-collision / marked-bypass machinery.

## Theorem — BT4-HT-PREDECESSOR-SPLICE-v1

In the four-remainder global-`NO-SIX` heavy-triangle saturation branch, the bare heavy triangle cannot remain an isolated terminal obstruction. At least one of the following source-valid outputs occurs:

1. **multi-light three-dominator output:** at most one predecessor relation occurs, so at least two of the three triangles `T_i` have light packed vertices that hit all three of their vertices;
2. **same-heavy five-witness output:** exactly two predecessor relations occur and the forced exact five-witnesses `h_1,h_2` are heavy on the same light support;
3. **split-heavy cross output:** exactly two predecessor relations occur, the forced witnesses are heavy on different light supports, and at least one lacks a heavy-target inport, hence the heavy-fan domination escape gives a genuine cross-packed transition into that target.

Moreover, the only way to reach outputs 2 or 3 is through the exact aligned cage

`r_0 -> r_1 -> r_2 -> x`,
`r_0 -> h_1`, `r_1 -> h_2`, `r_2 -> h_0`,

with `h_1,h_2` having exactly two outneighbors in `G=H union R` and exactly five into `S union U`.

The split-heavy branch with two genuine heavy inports is eliminated completely by the simultaneous strict two-cycle surgery of Lemma 4.

## What changed at the live splice frontier

Before this run, heavy-triangle saturation was one of the three unresolved four-remainder `SC+` configurations.

After this run it is no longer a free-standing case. External three-hit witnesses force it into already-recognized port/witness interfaces:

- multiple light ports hitting entire saturation triangles;
- a rigid same-heavy support pair; or
- a split-heavy state with a certified no-inport cross transition.

The proof also supplies an actual two-cycle strict-surgery certificate in the split-heavy/double-inport subcase; it does not merely count arcs.

The first unpaid implication is correspondingly narrower: splice one of these forced interfaces with the universal reciprocal sink-cross / named-partner third-port geometry without reusing packed segments. The separate `SIX` branch remains a second unpaid closure.

## Failure checks and nonclaims

- A single cross or opposite-cross pair is not counted as two replacement cycles.
- Lemma 1 uses the genuine `k=3` theorem, not the 2026 relaxed theorem.
- The successor-witness contradictions display the two disjoint cycles explicitly before adding untouched `S,U`.
- Lemma 4 requires **split** heavy targets. I do not apply its simultaneous surgery when both witnesses are heavy on the same light cycle.
- The heavy-fan escape is used only after a heavy target is proved to have no inarc to its witness.
- No computation is used as proof in this report.
- No full BT4 proof or literature-novelty claim is made.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The current first gap is still the genuine reciprocal/third-port packed-segment splice, but the four-remainder heavy-triangle branch has been reduced to concrete multi-light/same-heavy/cross interfaces, and one substantial split-heavy subcase is eliminated by an explicit simultaneous strict packing reduction.
