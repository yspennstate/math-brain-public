# BT4 fleet01/B04 — universal deletion/contraction deficit hierarchy and dynamic exchange persistence

Run: `20260922T004551Z-b04-bt4-f73bb16e`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Candidate: `BT4-MCR-v3-dynamic-deficit`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and current source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem and a digon counts as a directed cycle.

The current primary source remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract explicitly says the exact Bermond--Thomassen conjecture remains unresolved for every `k>=4` and proves at threshold `2k-1` only a near-directed relaxation. No near-directed cycle is treated below as a directed cycle.

The lower-k input used below is the established `k=3` theorem `delta^+>=5 => 3` vertex-disjoint directed cycles, together with the stronger Lichiardopol--Por--Sereni `k=2` theorem: if every vertex has outdegree at least three except at most two vertices of outdegree two, then two vertex-disjoint directed cycles exist. These are the same exact inputs already source-checked in the current BT4 lead state.

## Other-account mathematics actually consumed

I consumed the campaign lead's latest complete fleet02/B04 version:

- `proofnet24/collective-BT4/fleet02/B04/20260922T001806Z-b04-bt4-a1ceeb3c/report.md`, blob `d82fc84180bc66fd660c6c79f9a7f26332bdae72`, plus correction blob `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`.

The surviving normal form is a minimum-order BT4 counterexample, sparsified to an oriented spanning counterexample `D0` with every outdegree exactly seven, retaining a globally minimum-total three-cycle packing and an acyclic remainder. Every arc is dominated, `D0` is 3-vertex-strong, sink fans have the exact eight degree-seven types, and every deletion of two *chosen packed cycles* yields either a six-fan witness or three five-fan witnesses. The correction also records the essential support split: a witness on the complementary packed cycle cannot be treated as a remainder witness.

I also consumed the newer OTHER-account candidate `fleet03/B05`, `BT4-TCEX-v2.1-linkage`:

- parent report blob `1e08cd4e6a3db142c86033d9a63a0566f7bed172`;
- linkage addendum blob `f1545c2e4a546d17150bb20bbc59650a29eb2672`.

Its proved segment-exchange inequality says that an `R`-internal bypass around a packed-cycle segment `S` containing a marked heavy witness with fan size `m` must have length at least `m+|S|-1`; equality produces a new globally minimum-total three-cycle packing with an explicitly exchanged acyclic remainder. Its 3-connectivity trichotomy forces either reverse avoidance, such a quantified `R`-bypass, or two internally disjoint linkages through the other packed cycles. This run applies that equality exchange rather than merely citing it.

The fleet03/B06 exact constrained example is also retained as a warning: local U1 tight-fan geometry plus degree seven alone does not contradict BT4; the no-four-cycle condition must enter through the exchanged remainder/global packing. I therefore do not try to close the branch by another fan-only count.

## Compact conditional end-to-end route

Assume BT4 false and work in the exact-seven normal form `D0`. Let `(C1,C2,C3)` be a globally minimum-total three-cycle packing and `R` its nonempty acyclic remainder.

The current conditional route is:

1. use the lead's pair-deletion amplification to obtain six-fan or three-five-fan witnesses;
2. use the support-correct segment exchange of `BT4-TCEX-v2.1-linkage` whenever a cycle-supported witness admits an `R` bypass;
3. at strict inequality obtain a packing reduction; at equality pass to the new minimum packing and its acyclic exchanged remainder;
4. reapply the deletion witnesses and linkage machinery to the **new packing**, rather than assuming the original witness system survives;
5. close either by a strict exchange/fourth cycle, or prove that a neutral-exchange orbit cannot persist.

The missing point in Step 4 was that the earlier six/three-five statements were written only for the initially selected packing. The first result below removes that dependence completely: the whole degree-deficit hierarchy holds for **every** one-, two-, or three-cycle packing in `D0`, hence automatically after every neutral exchange.

## Lemma 1 — universal packing-deletion deficit hierarchy

Let `D0` be the exact-outdegree-seven counterexample above.

### One cycle

For every proper directed cycle `C` of `D0`, there exists a vertex `x outside C` such that

`|N^+(x) intersect V(C)| >= 3`.                                  (1)

Equivalently,

`delta^+(D0-C) <= 4`.                                             (2)

**Proof.** If every outside vertex had at most two outneighbors on `C`, then every vertex of `D0-C` would retain outdegree at least five. The known `k=3` theorem would give three disjoint directed cycles in `D0-C`; together with `C` these are four disjoint directed cycles in `D0`, contradiction. QED.

The point is that `C` need not be one of the originally selected packed cycles. Every proper directed cycle created by a later exchange obeys (1).

### Two cycles

For every pair of vertex-disjoint directed cycles `C1,C2`, put

`H=D0-(V(C1) union V(C2))`.

If `H` is nonempty, then it has no two vertex-disjoint directed cycles, and therefore

`delta^+(H) <= 2`.                                                (3)

More sharply, the strengthened `k=2` theorem gives the exact dichotomy

- some `x in H` has `d_H^+(x)<=1`, hence sends at least six arcs into `C1 union C2`; or
- at least three distinct vertices `x1,x2,x3 in H` have `d_H^+(xi)=2`, and each sends exactly five arcs into `C1 union C2`.                  (4)

**Proof.** Two cycles in `H` together with `C1,C2` would be a forbidden four-pack. If every vertex of `H` had degree at least two and at most two vertices had degree exactly two, then every other vertex would have degree at least three and the strengthened `k=2` theorem would force two disjoint cycles in `H`. Contraposition proves (4), and (3) follows. Exact outdegree seven converts residual degrees `<=1` and `=2` into pair-fan sizes `>=6` and `=5`. QED.

Thus the lead's six-fan/three-five-fan amplification is not tied to the chosen minimum packing: it is valid for **every disjoint pair of directed cycles** in `D0`.

### Three cycles

For every three vertex-disjoint directed cycles `C1,C2,C3` with nonempty remainder

`R_C=D0-(V(C1) union V(C2) union V(C3))`,

`R_C` is acyclic. Hence it has a sink `x`, and since `d^+_{D0}(x)=7`,

`|N^+(x) intersect (C1 union C2 union C3)|=7`.                     (5)

Again, no minimum-total assumption is needed for (5); no fourth directed cycle is the only global input.

Combining the three cases gives the exact residual threshold pattern

`j=1: delta_res <=4,   j=2: delta_res <=2,   j=3: delta_res=0 at a sink`,

and therefore forced fan losses `3,5,7` from an exact-seven vertex.

## Lemma 2 — exact contraction-loss hierarchy

Let `C1,...,Cj` be `j in {1,2,3}` vertex-disjoint directed cycles with nonempty remainder, and contract each `Ci` to a separate vertex `ci`, deleting loops and merging duplicate arcs. For an outside vertex `x`, write

`a(x)=|N^+(x) intersect union_i V(Ci)|`

and let `h(x)` be the number of the contracted cycles that `x` hits. Then the quotient outdegree is exactly

`d_Q^+(x)=7-a(x)+h(x)`,                                           (6)

where `0<=h(x)<=j`.

Applying Lemma 1 supplies an outside witness with

`a(x)>=3,5,7` for `j=1,2,3`, respectively. Hence some outside vertex in the corresponding quotient satisfies

`j=1: d_Q^+(x)<=5`,
`j=2: d_Q^+(x)<=4`,
`j=3: d_Q^+(x)<=3`.                                               (7)

For the robust two-cycle branch, a six-fan witness even gives quotient degree at most three.

**Proof.** Every original head outside the contracted cycles survives separately. The `a(x)` heads inside the deleted union collapse to exactly `h(x)` distinct contracted heads. This is (6). Insert the universal witnesses from Lemma 1 to obtain (7). QED.

This is the exact answer to what naive cycle contraction loses in the exact-seven normal form. Contracting one cycle already merges at least three heads of some outside vertex to one and loses at least two units of outdegree; contracting two or three packed cycles can force losses of at least three or four. Thus contraction cannot serve as a hidden induction preserving the threshold seven.

## Lemma 3 — safe path contraction obstruction

There is nevertheless a useful class of contractions that *would* preserve degree seven and is therefore forbidden.

Let

`P=v0 -> v1 -> ... -> vt`, `t>=1`,

be a directed path in `D0`. Assume the terminal vertex has no outneighbor back in the path:

`N^+(vt) intersect V(P)=emptyset`.                                (8)

Then some vertex `y outside P` has at least two outneighbors in `P`:

`|N^+(y) intersect V(P)| >= 2`.                                  (9)

**Proof.** Suppose instead every outside vertex hits `P` at most once. For each `i<t`, delete all outgoing arcs of `vi` except the path successor arc `vi->v(i+1)`, then contract all of `P` to one vertex `p`.

No outside vertex loses outdegree: by assumption at most one of its seven distinct heads is merged into `p`. The contracted vertex has exactly the seven external outneighbors of `vt`, because the earlier path vertices retain only internal successor arcs and (8) says none of `vt`'s seven outneighbors becomes a loop. Hence the smaller quotient still has minimum outdegree seven.

By vertex-minimality of `D0`, the quotient has four vertex-disjoint directed cycles. At most one contains `p`. If a quotient cycle enters `p` through an arc that originally entered `vi` and exits through an arc originally leaving `vt`, replace its passage through `p` by

`vi -> v(i+1) -> ... -> vt`.

The other three quotient cycles avoid `P`, so all four lift vertex-disjointly to `D0`, contradiction. QED.

Consequences:

- every directed path of positive length inside the DAG remainder has an external double-hitter, since acyclicity implies its terminal vertex cannot point backward into the path;
- every proper consecutive segment of a chordless packed cycle has an outside vertex hitting at least two vertices of that segment;
- the two-vertex case recovers arc domination for cycle edges, but the path statement is strictly stronger than an edge-by-edge domination assertion.

## Corollary 4 — two small global normal-form upgrades

First, every vertex of `D0` has indegree at least three. If a vertex had only one inneighbor, domination of that incoming arc creates a second. If it had exactly two inneighbors `a,b`, domination of `a->v` forces `b->a`, while domination of `b->v` forces `a->b`, a forbidden digon in the oriented normal form.

Second, `|V(D0)|>=16`. Since `D0` is oriented and has exactly `7n` arcs,

`7n <= n(n-1)/2`,

so `n>=15`. Equality at `n=15` would make `D0` a tournament. The tournament case of the Bermond--Thomassen bound is already known at threshold seven, so a counterexample cannot have `n=15`.

These are auxiliary reductions, not a solution.

## Application to the newest neutral segment exchange

Now apply the universal hierarchy to the exact fleet03/B05 equality exchange. Suppose `BT4-TCEX-v2.1-linkage` replaces `(A,B,C)` by another globally minimum-total packing `(A*,B*,C)` and remainder `R*`, with `R*` explicitly proved acyclic and of the same cardinality as `R`.

The new point is that **all amplified witnesses regenerate automatically after the exchange**:

1. deleting `A*` forces an external triple-fan into `A*`;
2. deleting `A*` together with `B*` forces either one six-fan witness or three five-fan witnesses into `A* union B*`;
3. the same dichotomy holds for `(A*,C)` and `(B*,C)`;
4. because `R*` is nonempty and acyclic, a sink of `R*` sends all seven outgoing arcs into `A* union B* union C`.

Thus a neutral equality exchange cannot be treated as a terminal exceptional configuration or as having “used up” the pair-deletion obstruction. It moves the proof to a new minimum packing carrying a **fresh complete 3/5/7 deficit system**. This is the first essential implication derived in this run from the other-account segment exchange.

The fleet03/B06 finite example explains why this does not itself close BT4: one neutral exchange can coexist with all local degree-seven geometry. What is now ruled out is a proof strategy that freezes the witness system to the original packing. Any legitimate iterative exchange proof may reselect witnesses after every equality move without re-proving the lower-k inputs.

## Updated first unpaid implication

The surviving target is now a dynamic, rather than static, exchange statement:

> Starting from any globally minimum-total three-cycle packing reachable by the support-correct neutral segment exchanges, use its freshly regenerated universal six-fan/three-five-fan systems and the 3-connectivity linkage trichotomy to prove that either a strict exchange/fourth cycle occurs, or a secondary extremal parameter changes strictly. Equivalently, rule out a closed orbit consisting entirely of neutral minimum-packings carrying fresh deficit witnesses.

The `R`-internal path-contraction obstruction above supplies an additional source-valid tool inside every such remainder: every nontrivial directed remainder path must be double-hit from outside that path. A next splice argument may therefore combine the fresh pair witnesses with these forced double-hitters rather than rely on average degree.

I do **not** claim that the dynamic-orbit implication is proved here. It is the honest remaining step after the universalization.

## Adversarial checks

- Lemma 1 is applied only when the stated remainder is nonempty. The live minimum packing and every equal-cardinality exchange under discussion have the same nonempty remainder, so this covers the active route.
- No witness is silently moved from a complementary packed cycle into the remainder; the lead's support correction remains in force.
- Quotient degree formula (6) counts distinct contracted heads after duplicate merging; it does not assume contraction preserves degree.
- Lemma 3 deletes outgoing arcs only from path vertices before contraction, and explicitly requires the terminal vertex to have no outneighbor back into the path. These are the exact conditions needed for the degree-seven quotient and lifting argument.
- No numerical search, edge-disjoint surrogate, near-directed cycle, or finite-order claim is used as target-level evidence.
- Full BT4 is not claimed proved, and no novelty claim beyond the repository candidate is made.

## Outcome

`ESSENTIAL_STEP_APPLIED`, not a full proof.

The main new reusable result is the **universal 3/5/7 deletion-deficit hierarchy**, valid for every one-, two-, and three-cycle packing in the exact-seven counterexample, together with the exact `5/4/3` contraction-degree losses and the arbitrary-path safe-contraction obstruction. Applied to the newest OTHER-account neutral segment exchange, it proves that the full amplified witness system regenerates after every equality move. This turns the current candidate from a one-shot packing argument into a dynamic exchange problem with a precise next obstruction: exclude neutral exchange orbits while preserving support and disjointness.

Next recipients: campaign lead `fleet02/B04`, assigned partner `fleet02/B05`, and exchange/linkage workers `fleet03/B05` and `fleet04/B06`.
