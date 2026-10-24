# BT4 account02/B04 addendum — four-remainder trident and sink-drop mechanism

Run: `20260922T011943Z-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Source boundary and exact inputs

The target is the exact `k=4` Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered vertex pair and minimum outdegree at least seven has four vertex-disjoint genuinely directed cycles; digons are allowed in the source statement.

The literature boundary remains unchanged. Bessy--Muis--Sereni--Steiner--Wiederrecht, arXiv:2608.12948 (13 August 2026), explicitly state that the exact conjecture remains unresolved for every `k>=4` and prove at threshold `2k-1` only the relaxation in which each packed cycle is directed or becomes directed after reversing one arc. The exact lower-k input is Lichiardopol--Por--Sereni, SIAM J. Discrete Math. 23 (2009), 979--992: `delta^+>=5` gives three vertex-disjoint directed cycles, and if every vertex has outdegree at least three except at most two vertices of outdegree two then there are two disjoint directed cycles.

This addendum continues the immutable lead report in this run, blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`. It substantively consumes the newer OTHER-account result account04/B06, `BT4-SINKLINK-v1`, report blob `44774a85169331dcf5b4cc7d79f3bef31ccb6dbc`. The exact facts used from that report are:

1. in the global no-six branch every remainder sink has fan type `(3,2,2)`;
2. a heavy packed cycle has no return arc into the sink, while each light cycle has at most one return vertex;
3. every no-six sink has an inneighbor in the remainder;
4. with exactly three sinks and no packed pair already carrying three sink-supported five-witnesses, the three sinks have distinct heavy labels.

The dynamic pair-deletion input is account01/B04 `BT4-MCR-v3-dynamic-deficit`, blob `f073bf10037d0c0961265275170680b13070b833`: after deletion of any two disjoint directed cycles, either a residual vertex has outdegree at most one (a six-fan), or at least three distinct residual vertices have outdegree exactly two (five-fans). The equality exchange used below is the lead report's proved completion of the repaired path-fan bound. The named partner account03/B05 corrected linkage package remains bound by blobs `f1545c2e4a546d17150bb20bbc59650a29eb2672` and `f19feaaea52a2a892e510bd8fe03dbb18290fcb5`; no peer outcome label is used as a theorem.

## Setup: the smallest surviving three-sink no-six core

Work in the inherited oriented exact-outdegree-seven minimum counterexample `D0`, with a globally minimum-total three-cycle packing `(A,B,C)` and acyclic nonempty remainder `R`.

Assume the persistent global no-six branch, `|R|=4`, and exactly three sinks. Also assume no packed pair already has three sink-supported five-witnesses, since that is a separate favorable witness-concentration branch. By the account04/B06 result the three sinks have distinct heavy labels; write them

`x_A, x_B, x_C`,

where `x_A` is heavy on `A`, etc. Let `u` be the fourth remainder vertex.

Because every no-six sink has an inneighbor in `R`, and the three sinks have no outgoing arc in `R`, the only possible remainder predecessor is `u`. Therefore

`u -> x_A,  u -> x_B,  u -> x_C`.                              (1)

Since `d^+(u)=7`, exactly four outarcs of `u` go to `A union B union C`.

## Lemma 1 — each packed cycle carries a forced third-cycle five-witness

For each packed cycle, say `C`, there is a vertex `z_C in C` such that, after deleting the other two packed cycles `A union B`, the residual outdegree of `z_C` is exactly two. Consequently `z_C` sends exactly five arcs into `A union B`, has only its cycle successor as an outneighbor on `C`, and has exactly one additional residual outarc

`z_C -> e_C`,  with `e_C in R`.                                 (2)

The analogous vertices `z_A in A` and `z_B in B` exist.

### Proof

Delete `A union B`. In the global no-six branch the strengthened `k=2` theorem forces at least three residual degree-two vertices.

The sinks `x_A` and `x_B` are two of them: their fan into `A union B` is respectively `3+2=5` and `2+3=5`, so exact outdegree seven leaves residual degree two. The third sink `x_C` is not one: its fan into `A union B` is only `2+2=4`, so its residual degree is three. The nonsink `u` is not one either, because (1) already gives it three residual outneighbors in `R` before counting any outneighbor on `C`.

Hence a third residual degree-two witness must lie on `C`; call it `z_C`. Global minimum makes each packed cycle chordless, so `z_C` has exactly one outneighbor on `C`, its successor. Residual degree two therefore leaves exactly one further outneighbor in `R`, proving (2). The same argument after deleting the other two pairs gives `z_A,z_B`. QED.

This is stronger than merely knowing that some five-witness lies on a complementary cycle: in the four-remainder/three-sink core, **every support cycle is forced to carry one**.

## Lemma 2 — every forced witness is a neutral-exchange port

For each `i in {A,B,C}`, the unique remainder exit of `z_i` cannot go to its own-heavy sink `x_i`. If it goes to one of the other two sinks, it gives a neutral one-vertex light pivot. If it goes to `u`, it gives an equality path to `x_i` and hence a neutral two-vertex heavy exchange.

### Proof for `z_C`

There are only four possible exit vertices.

* `e_C=x_C` is impossible. The sink `x_C` is heavy on `C`, and the one-vertex minimum-packing exchange already proves that a heavy cycle has no arc back into its sink. Thus no vertex of `C`, in particular `z_C`, can send an arc to `x_C`.

* If `e_C=x_A` or `x_B`, then `C` is light at that sink. Suppose `z_C->x_A`. The light fan has size two, and the lead's one-vertex exchange restriction gives

  `N+(x_A) intersect C = {z_C^+, z_C^{++}}`.

  Therefore

  `z_C -> x_A -> z_C^{++} -> C -> z_C`

  is a directed cycle of exactly the same order as `C`, replacing the single vertex `z_C^+` by `x_A`. This is the neutral light pivot.

* If `e_C=u`, then (1) supplies `u->x_C`. Thus

  `z_C -> u -> x_C`

  is an `R`-internal return path from `C` to the heavy sink `x_C`. Its length is `L=2`, while the heavy fan is `m_C(x_C)=3`. Hence `L=m-1`, equality in the repaired path-fan inequality. The equality-completion lemma in the lead report therefore gives a globally minimum size-neutral exchange on `C`. Concretely it swaps `u,x_C` for the first two successors of `z_C` (with the saturated triangle case handled by the same equality lemma).

The arguments for `A,B` are identical. QED.

### Consequence

The four-remainder/three-sink no-six state has **three support-distinct available neutral exchanges**, one generated on each of `A,B,C`. Thus this smallest hard core is not a single reversible light flip: its neutral exchange graph branches in all three support directions.

## Lemma 3 — a heavy `u`-exit exchange cannot preserve the three-sink hard core

Assume `z_C->u`, perform the neutral heavy exchange from Lemma 2, and suppose the new packing remains in the global no-six branch. Then its new four-vertex remainder has at most two sinks.

### Proof

Write

`y_1=z_C^+`,  `y_2=z_C^{++}`

on the old cycle `C`. The equality exchange replaces `u,x_C` on the remainder side by `y_1,y_2`; hence the new remainder is

`R'={x_A,x_B,y_1,y_2}`.                                         (3)

The old cycle arc `y_1->y_2` is still present, so `y_1` is not a sink of `R'`.

Suppose for contradiction that `R'` still has three sinks. Since it has four vertices, `y_1` must be its unique nonsink, and therefore `x_A,x_B,y_2` are sinks.

The account04/B06 no-six localization applies to the new globally minimum packing as well: every no-six sink has a remainder inneighbor. Since `y_1` is the only nonsink, it must be that

`y_1 -> x_A` and `y_1 -> x_B` (and of course `y_1->y_2`).         (4)

Return now to the old packing. Cycle `C` was light for `x_A`. The arc `y_1->x_A` in (4) makes `y_1` the unique return vertex from `C` to `x_A`. The light-return restriction therefore forces

`x_A -> y_1^+ = y_2`.                                            (5)

But both `x_A` and `y_2` belong to the new remainder `R'`, so (5) says that `x_A` has an outneighbor in `R'`, contradicting the assumption that `x_A` is a sink there.

Thus a persistent no-six heavy equality move from `z_C->u->x_C` cannot keep three sinks. The same holds cyclically for `A,B`. QED.

This is a genuine sink-monotonicity step unavailable in the previous lead report: the two-vertex equality move is not merely another state in a possible three-sink orbit; it necessarily drops the sink count (unless the move exits the no-six branch by creating a six-fan, which is already a separate closure branch).

## Corollary 4 — sink-minimal `|R|=4,s=3` states have a `(2,1,1)` nonsink port pattern

Choose, among globally minimum packings in the persistent no-six `|R|=4` component, one with the minimum possible number of remainder sinks. Suppose this minimum is still three.

Then none of the forced witnesses `z_A,z_B,z_C` can exit to `u`, by Lemma 3: such an exchange would remain a minimum packing and, if it stayed no-six, would lower the sink count; if it ceased to be no-six, the proof has entered the six-fan branch instead.

Hence every `z_i` exits to a non-own sink and gives a neutral light pivot. Put

`y_i=z_i^+`.

Consider the light pivot generated by `z_C->x_A`, for example. Its new remainder is

`{u,x_B,x_C,y_C}`.

The vertex `u` remains a nonsink because it still sends to `x_B,x_C`. Sink-minimality plus the account04/B06 bound `s<=3` in the hard core force the new state, if it stays in the same persistent branch, to have exactly three sinks. Therefore `u` is its unique nonsink and `y_C` is a sink. Every no-six sink needs a remainder predecessor, so necessarily

`u -> y_C`.                                                       (6)

Applying the same argument to the support-distinct pivots on `A` and `B` gives

`u -> y_A,  u -> y_B,  u -> y_C`.                               (7)

Together with the three arcs (1), exact outdegree seven leaves exactly one further packed outarc from `u`. Consequently the packed-cycle fan of `u` is a permutation of

`(2,1,1)`.                                                        (8)

So a sink-minimal persistent four-remainder/three-sink orbit is forced into a sharply finite port pattern: each support cycle has a five-witness `z_i` returning to another sink, its successor `y_i` is hit by the unique nonsink `u`, and `u` has only one packed outarc beyond these three successors.

## Additional localization: the sink inneighborhood cycles are triangles

In the same `|R|=4,s=3` state, the account04/B06 cycle inside `D[N^-(x_i)]` has no room for a longer remainder interior. For `x_A`, neither other sink can lie in `N^-(x_A)` because sinks have no remainder outarcs, while `u->x_A`. Heavy cycle `A` contributes no return vertex and each light cycle contributes at most one. Since the counterexample is oriented, the inneighborhood cycle has length at least three. It follows that it is exactly a directed triangle

`u -- r_{A,B} -- r_{A,C} -- u`,                                 (9)

where `r_{A,B}` and `r_{A,C}` are the unique return vertices from the two light cycles to `x_A`. Analogous triangles exist for `x_B,x_C`.

Combining (7)--(9) leaves a finite compatibility problem: each sink triangle must orient one of its two light return ports out of `u`, while `u` already spends three of its four packed outarcs on the forced successor ports `y_A,y_B,y_C`. Any long neutral orbit in the smallest hard core must therefore realize this port incidence with only one additional packed outneighbor of `u`.

I do not claim that this final finite port compatibility is impossible here; it is the next exact inference.

## Updated conditional end-to-end proof

The lead report's conditional proof still closes BT4 once the six-fan branch, cross-linkage splice, and neutral-orbit branch are closed. This addendum strictly improves the third obligation in the smallest remaining core:

* if `|R|=4` and there are three hard-core sinks, each support cycle supplies a forced neutral-exchange port;
* any port whose unique remainder exit is the common nonsink `u` either enters the six-fan branch after exchange or strictly lowers the number of sinks;
* therefore a sink-minimal persistent three-sink state has only light exits, and its unique nonsink is forced to have packed fan `(2,1,1)` with the three mandatory successor ports (7);
* each sink's arc-domination inneighborhood cycle is then a directed triangle through `u` and its two light return ports.

Thus the previous unrestricted long neutral orbit has been reduced, for the smallest three-sink remainder, to a concrete **pure-light port-triangle compatibility problem**. A contradiction to that finite incidence pattern would eliminate the `|R|=4,s=3` no-six hard core entirely; otherwise the next escape is a state with at most two sinks or a six-fan.

## Adversarial checks and nonclaims

- The argument uses `|R|=4` and exactly three sinks; it does not claim to handle `|R|>=5` or the one-/two-sink branch.
- The distinct heavy labels require the existing exclusion of the branch where one packed pair already has three sink-supported five-witnesses.
- A third-cycle witness is never silently treated as a remainder witness. Its unique residual successor on its support cycle and unique `R` exit are derived explicitly from chordlessness and residual degree two.
- Lemma 3 uses the new packing only after the equality-completion lemma guarantees it is globally minimum with acyclic remainder.
- The sink-predecessor localization is invoked only under persistent no-six; if a neutral exchange creates a six-fan, that is recorded as branch progress, not a contradiction.
- No near-directed cycle, edge-disjoint surrogate, larger degree threshold, finite-order computation, or peer PASS label is promoted to the target.
- Full BT4 is not proved.

Outcome: `ESSENTIAL_STEP_APPLIED`.
