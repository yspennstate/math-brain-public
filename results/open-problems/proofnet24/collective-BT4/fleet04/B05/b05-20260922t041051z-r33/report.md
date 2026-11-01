# BT4 fleet04/B05 — six-remainder sink-overload exclusion

Run: `b05-20260922t041051z-r33`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-COUNT-v5-SIX-R-SINK-OVERLOAD`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem, so directed digons count.

Current source boundary: Stéphane Bessy, Matthijs Muis, Jean-Sébastien Sereni, Raphael Steiner and Sebastian Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), https://arxiv.org/abs/2608.12948. Its abstract says the genuine conjecture is unresolved for every `k>=4`; the theorem at threshold `2k-1` permits cycles that may each require one arc reversal. No such relaxed cycle is promoted here.

The lower-`k` input is Nicolas Lichiardopol, Attila Pór and Jean-Sébastien Sereni, *A Step toward the Bermond-Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979–992, DOI https://doi.org/10.1137/080715792. The campaign uses its theorem that minimum outdegree five gives three vertex-disjoint directed cycles and its strengthened two-cycle statement: if all vertices have outdegree at least three except at most two vertices of outdegree two, then two vertex-disjoint directed cycles exist.

## Exact inherited state consumed

Newest complete campaign-lead package actually read:

- fleet02/B04, `proofnet24/collective-BT4/fleet02/B04/20260922T022208Z-b04-bt4-r11/report.md`, Git blob `930c6906cc2532269bc35e0d0b0ea8e246eb250b`;
- controlling correction `correction.md`, Git blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`.

The correction is controlling: in a no-cross state, every cycle-supported five-witness heavy on a packed cycle has a genuine inport from that heavy cycle. The invalid earlier invocation of the marked-segment inequality in the no-inport branch is not used.

Named OTHER-account partner result actually applied:

- fleet01/B06, `proofnet24/collective-BT4/fleet01/B06/20260922T013522Z-b06-bt4-r11/report.md`, Git blob `0ffb3fb1b521920e0a9cb3693fda8fd5bbb6a588`, fixed-pair witness staticization / exit-return collars.

Its exact input used here is: an `R`-supported five-witness heavy on a packed cycle with fan `m>=3` yields either a cross-packed transition, a size-neutral equality exchange, or three strict pure-`R` channels forcing

`|R| >= 3m-2 >= 7`.

The partner's newer fleet01/B06 `BT4-GATE-ESCAPE-v1`, report blob `adb2dcf7289ec7290cfc75ad760355ff540dff3d`, was also read. It gives a transverse heavy-cycle gate bypass in the six-remainder core. The new argument below turns out to close that core before needing the transverse bypass.

Immediate predecessor from this slot:

- fleet04/B05 `BT4-COUNT-v4-FIVE-R-EXCLUSION`, `proofnet24/collective-BT4/fleet04/B05/b05-20260922t031519z-r32/report.md`, Git blob `f3d20a757d23ce7d835f8605d3105504b58a7b07`.

That predecessor proved that a global `NO-SIX`, no-cross, no-neutral state with `|R|<=5` is impossible, and characterized `|R|=6` exactly. The present run attacks that first surviving size.

## Inherited normal form

Assume for contradiction that BT4 is false and work in the campaign's minimum-counterexample normal form:

1. `D` is oriented and every vertex has outdegree exactly seven;
2. `(A,B,C)` is a globally minimum-total packing of three directed cycles;
3. `R=V(D)\(V(A) union V(B) union V(C))` is nonempty and acyclic;
4. `A,B,C` are chordless;
5. every arc is dominated;
6. `D` is 3-vertex-strong.

For each deleted packed pair, the strengthened two-cycle theorem yields the campaign deficit alternative: either a surviving vertex has residual outdegree at most one (the `SIX` branch), or at least three distinct surviving vertices have residual outdegree exactly two, equivalently five-cross witnesses in the exact-seven normal form. `NO-SIX` means the latter alternative holds for all three packed pairs.

## Compact conditional end-to-end route

The lead's current honest universal obligations are still:

- `H6`: close the exact six-or-more cross-fan branch;
- `HX`: turn a genuine cross-packed transition / linkage output into a legal two-cycle replacement or strict packing contradiction;
- `HS`: prevent an equality-free, no-cross neutral orbit consisting only of strict collars/bypasses.

The predecessor paid the finite `HS` range `|R|<=5` and reduced `|R|=6` to an exact two-chain collar core. The first essential implication for this run is therefore:

> **Six-remainder closure.** Show that the exact `|R|=6`, global `NO-SIX`, no-cross, no-neutral collar core cannot occur.

The following deterministic counting argument proves it. No independence of witness choices is assumed.

## Lemma 1 — every fixed-pair witness is support-carried at |R|=6

Assume global `NO-SIX`, no genuine cross-packed transition, no size-neutral globally minimum packing exchange, and `|R|=6`.

Fix a deleted packed pair, say `{A,C}`. Pair deletion supplies at least three five-witnesses in the survivor `B union R`.

No such witness can lie in `R`: the named fleet01/B06 fixed-pair collar theorem would give either a cross transition, a neutral equality exchange, or `|R|>=7`, each impossible under the present assumptions.

Hence all at least three fixed-pair witnesses lie on the complementary packed cycle `B`.

The same statement holds cyclically for the other two deleted pairs.

## Lemma 2 — a remainder sink is the exit end of one collar for every support witness

Let `x` be a sink of the acyclic digraph `D[R]`; such a vertex exists.

Take any cycle-supported five-witness `z in B` for deleted pair `{A,C}`. The exact-six structure proved in `BT4-COUNT-v4-FIVE-R-EXCLUSION` says that the two simultaneously extracted support bypasses have the exact forms

`z^- -> r1 -> r2 -> r3 -> z+`,

`z^- -> s1 -> s2 -> s3 -> z+`,

where their internal `R`-vertex sets are disjoint and

`{r1,r2,r3,s1,s2,s3}=R`.

Because `x` is a sink of `D[R]`, it cannot equal `r1` or `r2`, since those vertices have the displayed outgoing arcs to `r2` or `r3` inside `R`. Likewise it cannot equal `s1` or `s2`.

Therefore

`x in {r3,s3}`.

In either case the displayed bypass contains the arc

`x -> z+`.                                                        (1)

Thus every cycle-supported five-witness `z` on `B` forces the same chosen sink `x` to send to the successor `z+` on `B`.

This is a simultaneous consequence of each witness's proved two-bypass partition; it does not treat different witness collars as probabilistically independent.

## Theorem — six-remainder sink overload

Continue under the hypotheses above.

For the deleted pair `{A,C}`, Lemma 1 supplies at least three distinct five-witnesses

`z1,z2,z3 in B`.

By Lemma 2,

`x -> z1+`, `x -> z2+`, `x -> z3+`.

The successor map on a directed cycle is injective, so `z1+`, `z2+`, `z3+` are three distinct vertices of `B`. Hence

`|N+(x) intersect B| >= 3`.                                      (2)

Apply exactly the same argument to the deleted pair `{B,C}`. Its at least three support-carried witnesses lie on `A`, so

`|N+(x) intersect A| >= 3`.                                      (3)

Apply it again to `{A,B}`. Its witnesses lie on `C`, so

`|N+(x) intersect C| >= 3`.                                      (4)

The packed cycles are vertex-disjoint. Equations (2)–(4) therefore give

`d+(x) >= 3+3+3 = 9`,

contradicting the exact normal-form equality `d+(x)=7`.

Therefore the assumed six-remainder featureless core does not exist.

> **BT4-COUNT-v5-SIX-R-SINK-OVERLOAD.** In the inherited oriented exact-outdegree-seven, globally minimum three-cycle-packing normal form, every global `NO-SIX` state with `|R|<=6` contains either a genuine cross-packed transition or a size-neutral globally minimum packing exchange.

The predecessor established the claim for `|R|<=5`; the theorem above closes the remaining size six.

## Additional exact rigidity at the eliminated boundary

For completeness, the exact-six predecessor also forces every cycle-supported five-witness to have heavy fan `m=3`, support bypass length four, and singleton bypassed segment. In the no-cross branch the lead correction supplies the required heavy-cycle inport, so the support-correct marked-segment inequality applies.

For any one of its length-four singleton bypasses, every heavy fan target has positive forward distance at most

`ell+1-s = 4`.

If distance four occurred, the corresponding exchange would have zero total-size change and be neutral, excluded here. Hence the three distinct positive fan distances are at most three and therefore exactly

`{1,2,3}`.

So at the first nominal strict-collar boundary the heavy fan itself is the three consecutive forward successors of its heavy inport. This extra rigidity is not needed for the sink-overload contradiction.

## Updated first unpaid implication

The finite strict-collar frontier moves from six to seven remainder vertices.

At `|R|=7`, the previous counting no longer automatically closes the state:

- an `R`-supported witness becomes possible because the partner bound `|R|>=3m-2` is tight when `m=3`;
- a cycle-supported witness's two strict support collars need cover only six of the seven remainder vertices, so a chosen sink can in principle be the one omitted vertex for many witnesses.

Accordingly the next honest `HS` subproblem is:

> **Seven-remainder omitted-sink closure.** In a global `NO-SIX`, no-cross, no-neutral state with `|R|=7`, prove that the support-collar omissions and any `R`-supported three-channel collar cannot all concentrate on the same acyclic remainder sink; or use that concentration to force a cross transition, neutral exchange, directed cycle in an exchanged remainder, or a `SIX` configuration.

This is not assumed here. The separate `H6` and `HX` obligations also remain open.

## Failure checks and nonclaims

- No independence assumption is made. The two support bypasses for a witness are simultaneous outputs with disjoint interiors, and the sink argument is deterministic.
- Distinct five-witnesses give distinct successors because they lie on the same directed cycle.
- The sink `x` is chosen once and used for all three pair deletions.
- An `R`-supported witness is excluded at size six only through the named fleet01/B06 theorem and the explicit no-cross/no-neutral hypotheses.
- The proof uses exact outdegree seven; a lower bound `d+(x)>=7` alone would not contradict the derived nine arcs.
- Digons are allowed in the original target; orientation is only the inherited counterexample reduction.
- No finite-order restriction, tournament assumption, edge-disjoint substitute or one-reversed-arc cycle is used.
- No computation was used in this run.
- `H6`, `HX`, and the `|R|>=7` part of `HS` remain unpaid. Full BT4 is not proved.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The previous exact six-remainder two-axis core is impossible by a sink-overload count. Therefore the first possible equality-free/no-cross strict-collar state in global `NO-SIX` has at least seven remainder vertices. The next decisive finite boundary is the seven-remainder omitted-sink state, while the campaign-level SIX and cross-linkage closures remain separate obligations.
