# BT4 account01/B04 — shortest mixed-cycle descent removes terminal endpoint coalescence

Run: `20260922T064247Z-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-SHORTEST-MIXED-CYCLE-PORT-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs, hence directed digons, are allowed in the source statement.

The current source boundary remains unchanged. Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), state that the genuine conjecture remains unresolved for every `k>=4`; their theorem at the `2k-1` threshold permits one reversed arc and is not a genuine directed-cycle conclusion. The lower-k theorem used below is Lichiardopol--Pór--Sereni, *A Step toward the Bermond--Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992, DOI `10.1137/080715792`: minimum outdegree five forces three vertex-disjoint directed cycles. No nearly-directed cycle is counted below.

## 2. Exact inherited mathematics consumed

### Campaign lead: account02/B04

Latest complete lead snapshot actually read: account02/B04 run `20260922T0619Z-b04-bt4-r11`, report blob `713053330313bf5906035c7bfd5841eb4e6b88ef`, candidate `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`.

I use its inherited minimum-counterexample normal form: a hypothetical counterexample may be taken oriented and exact-outdegree-seven, arc-dominated and 3-vertex-strong. Choose three disjoint directed cycles minimizing total packed order and, among those, maximizing the number of arcs in the acyclic remainder. Packed cycles are chordless.

I also use the lead's exact aligned four-remainder heavy-triangle clean-pair state. On two light supports `A,B` there are four distinct packed ports

- `p,a3 in A`, with `a3=p+++`,
- `b,q in B`,

and genuine opposite transitions

`P : p -> x -> b`,
`Q : q -> a3`,

where `x` is the old remainder sink. Thus

`K0 = p -> x -> b -> B[b,q] -> q -> a3 -> A[a3,p] -> p`      (1)

is a genuine directed mixed cycle. The lead correctly rejected an earlier direct use of `BT4-SC2-THIRD-PORT-v1` on (1), because (1) contains whole packed support segments rather than only two packed vertices. The lead then proved that a deletion witness for a mixed cycle produces a genuine packed-to-packed CROSS or a distinct-port same-support BYPASS, but retained the possibility that the lifted cross coalesces at already-used packed endpoints.

### Assigned partner: account02/B05

Named OTHER-account result actually consumed and applied: account02/B05 run `20260922T062431Z-b05-bt4-b744a134`, report blob `bf6b94983890a99c3c8d2e902bfc94fa3f57e22c`, candidate `BT4-R4-ALIGNED-TRIPLE-ABSORPTION-v1`.

Its exact contribution is that the aligned consecutive-triple lock is not terminal. Global minimum forces the aligned support to be a triangle; the canonical neutral source pivot frees `q=p+`, while the lock itself gives a heavy inport `h1->q`, contradicting both low-fan terminal classifications `F2-RONLY` and `F3-SINGLEPORT`. Therefore that aligned lock must exit through an already-existing source-pivot interface. I use this to remove the old triple lock from the branch tree and focus only on the clean mixed-cycle/coalescence frontier.

### Own previous B04 state

The preceding account01/B04 theorem `BT4-HT-TRIANGLE-BOUNDARY-COLLAPSE-v1`, report blob `36c1d8eb86ce397198545a2b021bd6f8effade4b`, reduced the triangular aligned boundary to SIX or at least two remainder-supported exact-five/cross generators. I preserve that result; the present mechanism is different and does not reopen the triangle-size argument.

## 3. Compact conditional end-to-end route

Assume a BT4 counterexample.

1. A directed digon can be deleted; every other vertex loses at most two outgoing neighbors, so the genuine `k=3` theorem would give three additional disjoint cycles. Hence a minimal counterexample is oriented. Retain seven outgoing arcs per vertex to obtain an exact-outdegree-seven spanning counterexample.
2. Use the inherited minimal-counterexample reductions to work in the arc-dominated, 3-vertex-strong normal form. Choose a three-cycle packing minimizing total packed order and then maximizing induced-remainder arcs. The remainder is acyclic and packed cycles are chordless.
3. Pair deletion and deficit analysis split the proof into SIX and global-NO-SIX interfaces. Existing compatible work reduces the relevant four-remainder aligned heavy-triangle branch to the clean mixed cycle (1) or the aligned triple. The named account02/B05 result absorbs the aligned triple into existing source-pivot outputs.
4. The theorem below replaces the lead's terminal endpoint-coalescence possibility for the clean mixed-cycle route by a shortest-cycle descent: after minimizing the mixed cycle itself, every deletion witness forces either a same-support BYPASS or a CROSS whose packed source is outside the working mixed cycle. Thus a shortest mixed cycle cannot support only repeated endpoint-coalesced lifts.
5. Full BT4 still requires closure of the common fresh-CROSS/BYPASS disjoint-splice interface, SIX, the nonaligned support-location branch, the remaining bounded F2/F3 interfaces, and the seven-remainder triangle-pinwheel/support-carried branch. None is assumed here.

## 4. New theorem — shortest mixed-cycle port collapse

### Definition of the mixed-cycle family

Let `M_x(A,B)` be the finite family of genuine directed cycles `K` having the following cyclic decomposition:

- a nonempty forward directed segment of support `A`;
- an `A->B` connector of length one, or of length two with sole internal vertex `x`;
- a nonempty forward directed segment of support `B`;
- a `B->A` connector of length one, or of length two with sole internal vertex `x`;
- the vertex `x` occurs in at most one connector.

Thus every `K in M_x(A,B)` uses only vertices of `A union B union {x}`, meets both supports, and has at most one remainder vertex. The clean cycle `K0` in (1) belongs to `M_x(A,B)`, so the family is nonempty.

Choose

`K* in M_x(A,B)`

of minimum edge length. Let

`r = 1_{x in V(K*)}`.

Exactly two connectors switch between `A` and `B`. If `r=1`, one connector is the length-two connector through `x`, so exactly one cross-support connector edge is direct. If `r=0`, both are direct. Hence the number of direct cross-support edges of `K*` is

`d = 2-r`.                                                   (2)

### Lemma 4.1 — cross-chord descent

If `c,w in V(K*)` lie on different supports and `c->w` is an arc of `D`, then either `c->w` is already a direct connector edge of `K*`, or there is a strictly shorter member of `M_x(A,B)`.

**Proof.** Suppose `c->w` is not an edge of `K*`. Follow `K*` from `w` back to `c` in its directed orientation. Because `c,w` lie on opposite supports, this return path contains exactly the opposite support-switching connector and subsegments of the two support segments; it contains `x` at most once. Therefore

`c -> w + K*[w,c]`

is again a genuine directed member of `M_x(A,B)`. Since the omitted forward path `K*[c,w]` has at least two edges, the new cycle is strictly shorter than `K*`, contradiction. QED.

Thus any direct cross between vertices of `K*` must be one of the `d=2-r` direct connector edges counted in (2).

### Lemma 4.2 — a shortest mixed cycle has a noncoalesced deletion output

In the inherited exact-seven counterexample normal form, `K*` forces at least one of the following:

1. a genuine packed-to-packed CROSS whose source packed vertex lies outside `V(K*)`; or
2. a genuine distinct-port same-support BYPASS with all internal vertices in the old remainder.

For a same-support bypass `J:c->...->w` on support `T`, global packing minimality gives the exact tax

`|E(J)| >= dist_T(c,w)`,                                     (3)

where `dist_T(c,w)` is the forward directed support distance from `c` to `w`.

**Proof.** If every vertex outside `K*` had at most two outneighbors on `K*`, then deleting `K*` would leave minimum outdegree at least five. The genuine Lichiardopol--Pór--Sereni `k=3` theorem would give three disjoint directed cycles in `D-K*`, which together with `K*` are four disjoint cycles. Hence some

`v notin V(K*)`                                             (4)

has at least three distinct outneighbors on `K*`.

First suppose `v` is packed.

- If `v` lies on the third packed cycle, at most `r` of its hits is `x`, so at least `3-r>=2` hits lie on `A union B`; any such arc is a packed-to-packed cross with source outside `K*`.
- If `v in A`, chordlessness of `A` allows at most one outneighbor of `v` on the `A` segment of `K*`; at most `r<=1` further hit can be `x`. Therefore at least one of the three hits lies on `B`, producing a direct `A->B` cross from the packed source `v outside K*`. The case `v in B` is symmetric.

Thus the conclusion holds if the deletion witness is packed.

Now suppose `v` lies in the old acyclic remainder. At most `r` of its hits is the possible vertex `x`, so it has at least

`h >= 3-r`                                                  (5)

distinct packed hit targets `w` on `A union B`.

Fix one such arc `v->w`. Apply the inherited arc-domination property. If a dominator `v1` lies in the remainder, then `v1->v,w`; if it is still in the remainder, dominate `v1->w` and continue. The old remainder is finite and acyclic, so a remainder vertex cannot repeat in this backward chain. Therefore the chain reaches a first packed vertex `c`, giving a path

`J_w : c -> ... -> v -> w`                                  (6)

whose internal vertices all lie in the old remainder. At the final domination step there is also the direct arc

`c -> w`.                                                    (7)

The endpoints are distinct because the graph is loopless.

If `c,w` lie on the same packed support, (6) is a same-support bypass. Replacing the forward support segment `T[c,w]` by `J_w` would strictly decrease total packed order if `|E(J_w)|<dist_T(c,w)`, while leaving the other two packed cycles untouched. This proves (3).

Assume, for contradiction, that no packed hit produces such a bypass and no packed hit produces a cross whose source is outside `K*`. Then for every one of the `h` distinct packed hit targets `w`, the corresponding apex `c` lies on the other support and also belongs to `V(K*)`. By Lemma 4.1, the direct cross arc (7) must be one of the `d=2-r` direct connector edges of `K*`.

Distinct hit targets `w` are distinct heads of these connector edges. Hence

`h <= d = 2-r`.                                             (8)

But (5) gives `h>=3-r`. Combining yields

`3-r <= 2-r`,

impossible. Therefore at least one packed hit yields either a same-support bypass or a packed-to-packed cross whose source lies outside `V(K*)`. QED.

### Corollary 4.3 — the endpoint-coalescence route cannot be terminal

Start from the lead's clean four-port mixed cycle `K0`. Replace it, if necessary, by a shortest member `K*` of `M_x(A,B)`. The deletion-plus-domination argument can no longer end with every output reusing only the packed vertices of the working mixed cycle: Lemma 4.2 forces a third packed source relative to `K*` or a same-support bypass.

This is exactly the structural feature that the corrected third-port strategy was seeking, but it is obtained without the false premise that the mixed cycle meets the old packing in only two packed vertices. I do **not** claim that the third port or one bypass alone already supplies two disjoint replacement cycles.

## 5. Why the pigeonhole is sharp enough

The useful count is the one-unit gap

`packed hits >= 3-r`,
`direct cross connectors = 2-r`.

When `x in K*`, a deletion witness may spend one hit on `x`, but then the cycle has only one direct cross connector. When `x notin K*`, all three hits are packed, but there are only two direct cross connectors. Thus the possible remainder hit and the lost direct connector cancel exactly; in both cases one packed hit must escape connector coalescence.

This count is not available on an arbitrary mixed cycle if one merely labels all arcs between the two support segments as ports. The shortest-cycle choice is what turns every direct cross chord between vertices of the working cycle into a contradiction and leaves only actual connector edges.

## 6. Exact deletion and contraction accounting

The assigned B04 structural accounting remains:

For a packed directed cycle `C` and an outside vertex `u`, put

`a_C(u)=|N+(u) intersect C|`.

In the exact-outdegree-seven normal form,

`d+_{D-C}(u)=7-a_C(u)`.                                     (9)

Thus deleting a cycle loses **exactly** one unit of outside outdegree per distinct outgoing neighbor on that cycle. The `k=3` deletion theorem is applicable precisely when `a_C(u)<=2` for every outside vertex.

If `C` is contracted to a single vertex and parallel arcs are coalesced, then

`d+_{D/C}(u)=7-a_C(u)+1_{a_C(u)>0}`.                        (10)

So contraction recovers at most one of the lost arcs: an outside vertex hitting `C` in `a_C(u)` places still loses `a_C(u)-1` units. Independently, the contracted vertex has outdegree equal to the number of **distinct external heads** of arcs leaving `C`, which can be below seven. Therefore contraction does not preserve the degree-seven induction hypothesis.

For two disjoint contracted cycles `C1,C2`, the outside-vertex formula is

`7-a_1(u)-a_2(u)+1_{a_1(u)>0}+1_{a_2(u)>0}`.                (11)

Vertex-disjointness itself lifts in the expected one-cycle sense: a quotient cycle family can use a contracted vertex in at most one member, and that member can be lifted through an appropriate directed segment of the original directed cycle. The obstruction to recursive contraction is the degree loss in (10)--(11), not an automatic failure of lifting.

The shortest mixed-cycle argument above avoids both losses entirely: it deletes only after proving the exact two-hit condition would suffice, and otherwise it works with genuine arcs/cycles in the original digraph rather than a quotient.

## 7. Applied partner consequence and revised first missing implication

The assigned partner result `BT4-R4-ALIGNED-TRIPLE-ABSORPTION-v1` eliminates the aligned consecutive triple as an independent terminal. The lead's clean long-support branch now has the shortest mixed-cycle theorem above, which eliminates terminal connector-endpoint coalescence relative to the working mixed cycle.

Hence the aligned heavy-triangle route now necessarily enters an existing source-pivot output, SIX, a same-support bypass, or a CROSS with a third packed source relative to the shortest mixed cycle.

The first essential unpaid implication for this route is now:

`BT4-FRESH-CROSS-BYPASS-SPLICE-v1`:

> In the lexicographic four-remainder heavy-triangle state, combine the original clean opposite pair with the fresh-source CROSS or same-support BYPASS supplied by `BT4-SHORTEST-MIXED-CYCLE-PORT-COLLAPSE-v1` to produce two vertex-disjoint replacement directed cycles, a strictly smaller minimum three-packing, a directed cycle in an exchanged remainder, SIX, or a compatible bypass family covered by the existing condensation theorem.

The important change is that this splice no longer needs to handle a terminal case in which **all** lifted cross outputs are connector-coalesced on the working mixed cycle.

## 8. Failure checks and nonclaims

- `K*` is a genuinely directed cycle in the original graph; no reversed-arc relaxation is used.
- The family `M_x(A,B)` is nonempty because it contains the lead's explicit clean cycle (1).
- The cross-chord descent retains one forward segment on each support and at most one use of `x`; it therefore remains inside the same family.
- The deletion witness is source-valid: if it did not exist, `D-K*` would have minimum outdegree at least five and the genuine `k=3` theorem would close BT4.
- The domination lift is finite because the old remainder is acyclic. A repeated remainder apex would create a directed remainder cycle.
- A same-support bypass is not declared a contradiction; equality in (3) is allowed.
- A fresh-source cross is not itself a fourth cycle.
- The theorem does not close SIX, the nonaligned support-location lock, all F2/F3 states, or the seven-remainder pinwheel/support-carried branch.
- No numerical or finite-search certificate is used.
- No novelty claim is made from a search miss. Full BT4 remains open.

## 9. Honest outcome

`ESSENTIAL_STEP_APPLIED`.

The new shortest-mixed-cycle mechanism converts the lead's remaining endpoint-coalescence phenomenon into a strict pigeonhole obstruction: a deletion witness has at least `3-r` packed hits but a shortest mixed cycle has only `2-r` direct connector heads available for coalesced domination lifts. Therefore one lift must escape as a third packed source relative to the working mixed cycle or as a same-support bypass. Together with the named account02/B05 aligned-triple absorption, this removes two formerly separate terminal locks from the aligned heavy-triangle branch, while leaving the genuine disjoint-splice and other global interfaces explicit.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: maximum actually supported. Configured reasoning effort and provider thinking-token/time telemetry: `UNKNOWN` / not exposed. Execution remains `WITHOUT_VERIFIED_BRAIN`.
