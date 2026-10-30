# BT4 fleet02/B20 — Hall source collision collapses to SIX/CROSS/BYPASS/short support

Run: `20260922T055931Z-fleet02-B20-bt4-r15`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-HT-HALL-SOURCE-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target

Prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed, so digons are valid directed cycles. Nothing below substitutes edge-disjoint cycles, nearly directed cycles, the one-reversed-arc relaxation, a larger outdegree threshold, a routine subclass, or finite search.

## Fresh team state actually consumed

Latest complete campaign-lead state actually read before this derivation:

- fleet02/B04 run `20260922T051543Z-b04-bt4-r11`;
- primary scientific report commit `07e6d15d1504e1d11d588ee8b637e9b4710a3d7a`, blob `9f1ec8ca9ab3f2737b9dddf98389826f5b926933`;
- same-run controlling strengthening commit `1e394073bccc5d223382ae9c66eb71394ac8964c`, blob `aa71a6d910955a009b020ee77aba4a0da0052cdb`.

The lead retains the source-valid minimum-counterexample normal form: after the inherited reductions, work in an oriented exact-outdegree-seven, 3-vertex-strong, arc-dominated counterexample. Choose a packing `(H,S,U)` of three genuinely directed pairwise vertex-disjoint cycles with minimum total packed order; among those choices maximize the number of arcs induced by the acyclic remainder `R`. Packed cycles are chordless. In the four-remainder heavy-triangle branch,

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

with saturation triangles `hi->ri->x->hi`. The lead has reduced the aligned difficult branch to genuine port-splice inputs or a short light support; the common packed-port splice remains unpaid.

Named completed OTHER-account result actually consumed and used:

- assigned partner fleet04/B06 run `20260922T051305Z-b06-bt4-r14`, candidate `BT4-SIX-DUAL-WALL-LIFT-v1`, scientific commit `94e839f1292a0fc62c8c0ec6d8ab5a1244d99723`, blob `c972d170864b95062330e30dcdeded0f7b76cb1e`.

That theorem treats the corrected cycle-supported exact-six / zero-remainder-exit `C4` state. Under the two-in/two-out dual reachability wall, 3-vertex-strongness forces, for every selected ladder/ray pair, either a genuine packed cross, a distinct-port same-support remainder bypass with the exact minimum-packing tax `ell>=d`, or a support of order at most `|R|+1`. In the all-long regime the wall therefore cannot persist as a separate obstruction. It does **not** close the independent `H5` / multiple-high-witness SIX branch, and I do not use it as if it did.

A second compatible OTHER-account input is used for the exact Hall geometry:

- fleet04/B05 run `b05-20260922t051421z-r34`, candidate `BT4-HT-XFREE-HALL-v1`, canonical report blob `e63f331533e20a4a1231458a6c5c43c7eb5c4bf1`.

It exactifies the lead's four-remainder heavy-triangle cage and proves that `h0,h1,h2,r2` are exact five-witnesses for the fixed light pair `{S,U}`. For every cycle-supported witness `h_i` heavy on a light support `A_i`, it constructs an `x`-free genuine cross path `P_i` ending at a heavy-fan target. Its remainder interior is empty or exactly `{r_{i-1}}`. Hence the three possible remainder interiors are pairwise disjoint. For two witnesses heavy on the same light support `A`, a two-set Hall argument gives either (i) two such paths with distinct target ports and disjoint remainder interiors, or (ii) the explicit exact fan-collision state in which both heavy fans equal the sink's two-port fan plus one common extra target.

No peer outcome label is substituted for these statements.

## Conditional end-to-end route and first unpaid implication

A full proof would follow if the accumulated genuine port interfaces can always be converted into a legal packing improvement or a fourth directed cycle, while the separate SIX/H5, short-support, nonaligned and larger-remainder branches are closed.

This report attacks the first unresolved part of the Hall distinct-port interface. In that interface we have two `x`-free paths

`P_i : s_i -> ... -> a_i`,  `P_j : s_j -> ... -> a_j`,

where `i!=j`, the targets `a_i,a_j` are distinct vertices of a common light support `A`, every internal vertex lies in `R`, and the two remainder interiors are disjoint. Each packed source `s_k` is either the heavy-triangle predecessor `h_{k-1}` or a vertex of the opposite light support `B`.

The previously unpaid possibility was that the two paths could still collide at their packed source. The theorem below eliminates that as an opaque state: distinct sources give fully vertex-disjoint paths, while a common source routes canonically to an existing SIX interface, a genuine cross, a taxed same-support bypass, or an explicit short-support boundary.

## Lemma 1 — distinct packed sources pay full path disjointness

Assume `s_i != s_j`. Then `P_i` and `P_j` are vertex-disjoint.

### Proof

Their internal vertices lie in `R` and the Hall construction gives disjoint remainder interiors. Their terminal vertices `a_i,a_j` are distinct and lie on `A`. Their initial vertices lie outside `A`, so neither initial vertex can equal either terminal vertex. Finally, each initial vertex is packed while every internal vertex of the other path lies in `R`. Since the initial vertices are distinct, there is no remaining possible intersection. QED.

Thus in the distinct-source Hall branch, **all path-level disjointness is already paid**. What remains is genuinely cyclic-order/splice information on the packed supports; it is not another hidden interior-disjointness problem.

## Lemma 2 — a common Hall source lies on the opposite light support and has four fixed off-support exits

Assume instead that `s_i=s_j=q`. Then `q` lies on the opposite light support `B`, not on `H`. Moreover, besides its unique support successor `q+`, the vertex `q` has four distinct forced outneighbors outside `B`: `h_i`, `h_j`, and two distinct first-step vertices `v_i,v_j` of the two Hall escape paths.

### Proof

For the `i`-escape, fleet04/B05 obtains the path by dominating the heavy-fan arc `h_i->a_i`. If the first dominator is packed, it is the source and sends to both `h_i` and `a_i`. If the first dominator is `r_{i-1}`, a second domination of `r_{i-1}->h_i` supplies the packed source; that source sends to `h_i` and `r_{i-1}`, while `r_{i-1}->a_i`. Thus in either case the packed source sends to `h_i` and to the first vertex after the source on `P_i`. Call the latter `v_i`.

The same holds for `j`. If the common source lay on `H`, the exact cage permits only the distinct support predecessors `h_{i-1}` and `h_{j-1}` as the relevant packed sources, so equality is impossible. Hence `q in B`.

The vertices `v_i,v_j` are distinct. If both paths have empty remainder interior then `v_i=a_i` and `v_j=a_j`, distinct by Hall. If both use a singleton remainder interior then `v_i=r_{i-1}` and `v_j=r_{j-1}`, distinct because `i!=j`. In the mixed case one first step lies on `A` and the other in `R`. Also `h_i,h_j,v_i,v_j` are pairwise distinct across the indicated types. Therefore

`q -> h_i, h_j, v_i, v_j`.

Because `B` is chordless and the graph is oriented in the inherited normal form, `q` has exactly one outneighbor on `B`, namely its directed-cycle successor `q+`. QED.

Since `d+(q)=7`, only two outarcs of `q` remain unaccounted for after these five distinct forced outneighbors.

## Theorem — BT4-HT-HALL-SOURCE-COLLAPSE-v1

In the Hall distinct-port branch of the four-remainder heavy-triangle cage, let `P_i,P_j` be the two `x`-free escape paths described above. Then exactly one of the following source-level alternatives applies.

1. **Distinct-source pair.** `s_i!=s_j`, in which case `P_i,P_j` are fully vertex-disjoint genuine packed-to-packed transitions.
2. **Exact-six routing.** `s_i=s_j=q in B` and `N+(q) intersect R` is empty. Then `q` is a cycle-supported exact-six witness for the complementary packed pair `H union A`, with zero remainder exit.
3. **Genuine cross.** `s_i=s_j=q in B`, `q` has a remainder outneighbor, and a maximal directed continuation through the acyclic remainder first meets `H` or `A`.
4. **Taxed same-support bypass.** The same continuation first returns to a distinct vertex `t in B`. If its edge length is `ell` and `d=dist_B(q,t)` is the forward distance on `B`, then `ell>=d`. Equality is a size-neutral packing exchange; strict inequality is a quantified collar.
5. **Short-support return.** The continuation first returns to `q`, yielding a genuine directed cycle on `{q}` plus remainder vertices. Consequently `|B|<=|R|+1`.

In alternative 2, the source collision has been routed into the campaign's existing SIX system. In the partner's `C4` dual-wall subcase, `BT4-SIX-DUAL-WALL-LIFT-v1` further routes the all-long wall to CROSS/BYPASS or a short support. No claim is made that the partner theorem closes all exact-six states.

### Proof

Only the common-source case requires work. Put `q=s_i=s_j`, so Lemma 2 gives `q in B`.

If `N+(q) intersect R` is empty, chordlessness of `B` says that the only outarc of `q` staying on `B` is `q->q+`. Exact outdegree seven therefore puts all six remaining outarcs into `H union A`. This is precisely a cycle-supported exact-six witness with zero remainder exit, proving alternative 2.

Now suppose `q->r_1` for some `r_1 in R`. Starting at `r_1`, extend a directed path inside `D[R]` for as long as possible. Because `R` is finite and acyclic, no remainder vertex repeats. At a terminal vertex of this internal continuation there is no outgoing arc to a new remainder vertex. Exact outdegree seven then guarantees an outgoing arc to the old packing. Choose the resulting path

`P : q -> r_1 -> ... -> r_m -> t`

so that `t` is its first packed vertex after `q`. Every internal vertex of `P` lies in `R`, and `P` is simple.

If `t in H union A`, `P` is a genuine cross-packed transition from `B` to another packed cycle, proving alternative 3.

If `t in B` and `t!=q`, let `ell` be the number of edges of `P` and let `d=dist_B(q,t)` in the forward direction of `B`. Concatenate `P` with the complementary directed segment `B[t,q]`. This is a genuine directed cycle, disjoint from `H` and `A`, whose order is

`|B| + ell - d`.

Replacing `B` by this cycle would strictly decrease total packed order if `ell<d`; global minimum therefore gives `ell>=d`. This proves alternative 4.

Finally, if `t=q`, the path `P` itself closes to a genuine directed cycle containing exactly one packed vertex `q` and otherwise only vertices of `R`. Its order is at most `|R|+1`, and it is disjoint from `H` and `A`. Replacing `B` by it in the three-packing and using minimum total packed order yields `|B|<=|R|+1`, proving alternative 5. QED.

## Consequence for the live port-splice frontier

Before this run, fleet04/B05's Hall alternative paid distinct targets and disjoint remainder interiors, but a common packed source could still be recorded as an unresolved collision. That is no longer necessary.

- If the two Hall paths have different sources, they are genuinely vertex-disjoint paths, so path-level disjointness is complete.
- If they share a source, the state immediately routes to an already named campaign interface: SIX, CROSS, same-support BYPASS with an exact exchange tax, or a support of order at most `|R|+1`.
- The named partner fleet04/B06 then pays the `C4` all-long dual-wall subcase of the SIX routing.

Thus `HT-PORT-CLOSE` has been reduced to **packed cyclic-order/return compatibility for the distinct-source pair**, plus the already explicit exact fan-collision, remaining SIX/H5, and short-support boundaries. A generic "common source" is no longer an independent obstruction.

## First unpaid universal implication after this result

For every source-valid distinct-source Hall pair in the lexicographic minimum packing, with two vertex-disjoint packed-to-packed paths ending at distinct ports of the same light support `A`, prove one of:

1. the available reciprocal/third-port transition can be chosen vertex-disjointly so that two legal replacement directed cycles are formed;
2. the corresponding packing replacement strictly decreases total packed order or, at equal order, increases the remainder-arc potential;
3. the exchanged remainder contains a directed cycle, giving the fourth cycle;
4. the geometry routes to a SIX witness or the explicit exact fan-collision/short-support state already isolated by the team.

All quantifiers remain over arbitrary finite source digraphs in the exact-seven normal form; no finite-order assumption is introduced. This is the next method: work on cyclic order of the four packed ports and the first reciprocal return, rather than on remainder-interior disjointness, which is now paid in the distinct-source branch.

## Failure checks

- A single CROSS is not counted as a fourth cycle.
- Two same-direction cross paths are not by themselves counted as a two-cycle splice.
- The exact-six routing does not silently assert the `H5` branch is closed.
- The bypass inequality uses the actual directed complementary segment of `B`; no reversed arc is used.
- If the continuation returns to `q`, the replacement cycle is genuinely directed and uses only `q` plus remainder vertices.
- Digons remain allowed in the source target; this proof operates only after the inherited valid reduction to the oriented minimum-counterexample normal form.
- No finite search or computation is used as proof.
- No unrestricted Bermond--Thomassen or BT4 closure is claimed.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

`FULL_TARGET_CHANGE = NONE`.

`MECHANISM_CHANGE = YES`: the former Hall source-collision ambiguity is replaced by a source-level continuation dichotomy and exact packing taxes. The surviving first universal debt is now cyclic-order/reciprocal-return splicing for fully vertex-disjoint distinct-source paths, plus separately named fan-collision/SIX/short-support boundaries.
