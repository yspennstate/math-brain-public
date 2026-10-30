# BT4 fleet02/B04 — exact-seven sink normal form and robust two-cycle obstruction

Run: `20260922T001806Z-b04-bt4-a1ceeb3c`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source state

Target: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four vertex-disjoint directed cycles. Opposite arcs are allowed in the source problem and a digon counts as a directed cycle.

Current source check: Bessy–Muis–Sereni–Steiner–Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (2026-08-13), proves at the same threshold `2k-1` only a packing of `k` cycles each directed or made directed by reversing one arc, and explicitly leaves every `k>=4` directed case unresolved. I do not promote a near-directed cycle to a directed one.

The exact lower-k inputs used here are:

- Lichiardopol–Pór–Sereni, *A step towards the Bermond-Thomassen conjecture about disjoint cycles in digraphs* (SIAM J. Discrete Math. 23 (2009), preprint at `https://iti.mff.cuni.cz/series/2007/339.pdf`): minimum outdegree five gives three disjoint directed cycles; and, more sharply, every digraph in which all vertices have outdegree at least three except at most two vertices of outdegree two has two disjoint directed cycles. The same source proves for a minimum counterexample that every arc is dominated and notes an oriented sharp obstruction with one degree-one vertex: all other vertices may have outdegree three and yet there need not be two disjoint cycles.
- Bai–Manoussakis, *On the number of vertex-disjoint cycles in digraphs*, arXiv:1805.02999v2, Claim 1: in the minimum `k=3` counterexample there is no digon, every arc is dominated, and every inneighborhood contains a directed cycle. I reprove below the parts that transfer to `k=4` rather than assuming they transfer automatically.

## Exact other-account input consumed

I used the complete fleet01/B04 candidate `BT4-MCR-v1`, scientific commit `8a71d11efa2a3110db78c39684ea4c9cce03a28b`, scientific blob `05c8cc232a9706214937f6eff31b85464a498859`; its compact coordination handoff has blob `0b02eaf6776b8f39efe8d3ec4dd92cfea1ad2fe7`.

That candidate proves, for a minimum-total three-cycle packing with acyclic remainder `R`, the directed exchange inequality: if `x in R`, `C` is a packed cycle, and there is an `R`-internal path of length `L` from `b in C` to `x`, then

`|N+(x) ∩ C| <= L+1`.

Its first unpaid implication was to force, for a sink `x` and a heavy packed cycle with `m=|N+(x)∩C|>=3`, a return path of length at most `m-2`, or an equivalent global exchange. I attack exactly that gap below.

## Conditional end-to-end route retained

If the fleet01 short-return implication holds for one sink/heavy-cycle pair, the proof closes immediately: the path-fan inequality gives `m <= L+1 <= m-1`, contradiction. All reductions preceding it are source-valid. Thus `BT4-MCR-v1 + short-return` is a complete conditional proof of BT4.

The purpose of this run is not to rename that gap. I strengthen the counterexample normal form around it, import the full robust `k=2` input rather than only the threshold-three corollary, and identify a neutral exchange at the equality boundary `L=m-1`. These give a new mechanism for the cases where strict short return is unavailable.

## Step 1. Choose a global minimum packing, not merely a packing with a prescribed remainder

Assume BT4 false. Choose a counterexample `D` with minimum order, and subject to that with maximum number of arcs.

Exactly as in `BT4-MCR-v1`, `D` has no digon: deleting a digon lowers every remaining outdegree by at most two, leaving minimum outdegree at least five, so the known `k=3` theorem gives three more cycles. `D` is strongly connected by the sink-SCC argument. It is not a tournament, since the Bermond–Thomassen statement is known for tournaments.

Choose a nonadjacent pair `u,v` and add the missing arc `u->v`. Arc maximality forces four disjoint directed cycles in the augmented graph, and at least one uses the new arc. Because `v->u` is absent, that cycle has length at least three. The other three are already cycles of `D` and leave at least three vertices uncovered.

Now choose **globally among all three-cycle packings in `D`** a packing

`P=(C1,C2,C3)`

minimizing `|C1|+|C2|+|C3|`. The preceding packing shows the global minimum has total size at most `|V(D)|-3`, so its remainder

`R = V(D) \ (V(C1)∪V(C2)∪V(C3))`

has at least three vertices. This global choice is slightly stronger than minimizing only among packings already known to leave three vertices: every later three-cycle replacement, with any remainder size, is now legitimately comparable to `P`.

As before, each `Ci` is induced/chordless (a chord gives a shorter directed replacement cycle) and `D[R]` is acyclic (a cycle in `R` would be a fourth disjoint cycle).

## Step 2. Exact-seven sparsification retaining the optimal packing

For each vertex, retain exactly seven outgoing arcs, and for each vertex on a `Ci` require its cycle-successor arc to be among the retained arcs. Let the resulting spanning subdigraph be `D0`.

Then:

1. every vertex of `D0` has outdegree exactly seven;
2. `D0` is still a counterexample, since deleting arcs cannot create four directed cycles;
3. it has the same minimum possible order as `D`, so every smaller digraph of minimum outdegree seven has four disjoint cycles;
4. `P` remains a globally minimum three-cycle packing in `D0`, because every packing in `D0` was already a packing in `D`;
5. the same remainder `R` is acyclic in `D0`.

This exact-seven reduction is useful because all deletion losses become equalities rather than lower bounds.

## Step 3. Every arc of `D0` is dominated

Claim: for every arc `u->v` of `D0`, there exists `z` distinct from `u,v` with `z->u` and `z->v`.

Proof. Suppose `u->v` is not dominated. `D0` is oriented because the original minimum counterexample has no digon. Delete every outgoing arc of `u` except `u->v`, then contract `u,v` to one vertex `w`. Since no outside vertex sends arcs to both `u` and `v`, contraction does not merge two outgoing neighbors of any outside vertex. Thus all outside outdegrees remain seven. The outneighbors of `w` are exactly the former outneighbors of `v`, so `d+(w)=7`. The contracted digraph has minimum outdegree seven and fewer vertices, hence has four disjoint directed cycles by minimality. A cycle through `w` lifts either through `v`, or through `u->v` if its entering arc came from an arc into `u`; the other cycles lift unchanged. This gives four cycles in `D0`, contradiction. QED.

Consequently every inneighborhood contains a directed cycle. Indeed, strong connectivity gives `N-(x)` nonempty. For every `y in N-(x)`, domination of `y->x` gives `z in N-(x)` with `z->y`; hence the induced digraph on `N-(x)` has minimum indegree at least one and therefore contains a directed cycle.

## Step 4. `D0` is 3-vertex-strong

Claim: deleting at most two vertices cannot destroy strong connectivity of `D0`.

Proof. Suppose a set `S` with `|S|<=2` separates `D0`. In `D0-S` choose a sink strong component `B`; then no arc leaves `B` for another component. Hence every `v in B` has

`d+_{D0[B]}(v) >= 7-|S| >= 5`,

so the known `k=3` theorem gives three vertex-disjoint directed cycles inside `B`.

Pick `a` in another strong component of `D0-S`. Since `B` is a sink component, no vertex of `B` sends an arc to `a`. The preceding inneighborhood-cycle property supplies a directed cycle contained in `N-(a)`, and this cycle is disjoint from `B`. It is therefore disjoint from the three cycles in `B`, producing four cycles in `D0`, contradiction. QED.

This is the exact `k=4` analogue of the connectivity pressure used in the short `k=3` proof, and it is available for later linkage arguments.

## Step 5. Every remainder sink has a direct return from a light packed cycle

Let `x` be a sink of the DAG `D0[R]`. Since `d+_{D0}(x)=7` and `x` has no outneighbor in `R`, define

`mi = |N+(x) ∩ V(Ci)|`, so `m1+m2+m3=7`.

Call `Ci` heavy for `x` if `mi>=3`.

The fleet01 one-vertex exchange is valid verbatim in `D0`: if `b in Ci` has `b->x`, then global packing minimality forces

`N+(x)∩Ci ⊆ {b+, b++}`,

so necessarily `mi<=2`. In particular **no heavy cycle sends an arc to `x`**.

On the other hand, the induced digraph `D0[N-(x)]` contains a directed cycle `Q`. Since `R` is acyclic, `Q` is not contained in `R`; hence some vertex `b` of some packed cycle `Cℓ` lies on `Q`, and `b->x`. By the preceding paragraph,

`mℓ <= 2`.

Thus every sink has a **light-return cycle**: a packed cycle that sends an arc directly to the sink and receives at most two arcs back from that sink. This is a genuine consequence of arc domination and is the first new inference applied directly to the fleet01 short-return obstruction.

A useful extra statement is that if two cycles are heavy for `x`, then the inneighborhood cycle `Q` is disjoint from both of them, so it lies in the subdigraph induced by the unique light cycle together with `R`.

## Step 6. The exact sink fan types are only eight

After sorting `(m1,m2,m3)` in nonincreasing order, exact outdegree seven and the light-return lemma leave only

`(3,2,2), (3,3,1), (4,2,1), (4,3,0), (5,1,1), (5,2,0), (6,1,0), (7,0,0)`.

The exact bookkeeping script was:

```python
out=[]
for a in range(8):
    for b in range(a+1):
        for c in range(b+1):
            if a+b+c==7:
                out.append((a,b,c,sum(t>=3 for t in (a,b,c))))
print(out)
```

Output:

```text
[(3, 2, 2, 1), (3, 3, 1, 2), (4, 2, 1, 1), (4, 3, 0, 2),
 (5, 1, 1, 1), (5, 2, 0, 1), (6, 1, 0, 1), (7, 0, 0, 1)]
```

So there are at most two heavy cycles. The only two-heavy types are `(3,3,1)` and `(4,3,0)`; in those cases the direct-return cycle is the unique light cycle and its fan is at most one.

This finite split is not a finite-order proof; it is only the exact local sink classification forced by the infinite-graph argument above.

## Step 7. Use the full strengthened `k=2` theorem on every pair deletion

Fix distinct `i,j` and put

`H = D0 - (V(Ci)∪V(Cj))`.

`H` cannot contain two disjoint directed cycles, because together with `Ci,Cj` they would give four in `D0`.

Apply the contrapositive of the Lichiardopol–Pór–Sereni strengthened `k=2` theorem. Since `H` has no two disjoint cycles, one of the following must hold:

1. some vertex of `H` has outdegree at most one in `H`; or
2. at least three vertices of `H` have outdegree exactly two in `H`.

Because every vertex has outdegree exactly seven in `D0`, if

`a_ij(v)=|N+_{D0}(v)∩(V(Ci)∪V(Cj))|`,

this is equivalently the sharp dichotomy

- some `v` has `a_ij(v)>=6`; or
- at least three vertices have `a_ij(v)=5`.

This strictly strengthens the earlier `BT4-MCR-v1` pair-deletion statement, which only forced one witness with at least five outgoing arcs into the deleted pair.

For a two-heavy sink, deleting its two heavy cycles lands immediately in the first branch: fan type `(3,3,1)` leaves the sink with residual outdegree one, and `(4,3,0)` leaves residual outdegree zero.

A tempting shortcut would be to extend the strengthened `k=2` theorem by allowing one degree-one vertex. The 2009 source explicitly blocks that: it gives an oriented graph in which every vertex has outdegree three except one of outdegree one, yet there are no two disjoint cycles. Therefore the two-heavy cases cannot be dismissed by an unsupported robustness upgrade. This is a source-valid refutation of that shortcut, not a counterexample to BT4.

## Step 8. Equality in the path-fan bound is an exact neutral exchange

The fleet01 argument sought a strict return of length at most `m-2`. There is also useful information at the boundary `L=m-1`.

Let

`b=p0 -> p1 -> ... -> p_L=x`

be an `R`-internal return path from a packed cycle `C` to `x`. If

`m=|N+(x)∩C| = L+1`,

then the fleet01 counting proof is tight: the `m` outneighbors of `x` on `C` must be exactly the `L+1` allowable successors of `b`. In particular `x` sends an arc to `b^{+(L+1)}`. The cycle

`b -> p1 -> ... -> x -> b^{+(L+1)} -> ... -> b`

has exactly `|C|` vertices. It replaces the `L` cycle vertices `b+, ..., b^{+L}` by the `L` remainder vertices `p1,...,x`. Hence replacing `C` by this cycle preserves the total size of the globally minimum three-cycle packing.

The simplest case is the light-return situation: if `b->x` and `m=2`, then

`N+(x)∩C = {b+,b++}`

and

`b -> x -> b++ -> ... -> b`

is a directed cycle of the same length as `C`, replacing `b+` by `x`. This gives a legal **neutral packing exchange** rather than a contradiction.

This equality exchange is the concrete alternative mechanism when the strict short-return target fails by exactly one edge. What is not yet proved is a monotone secondary parameter forcing repeated neutral exchanges to terminate in a strict short return or in a pair deletion satisfying the strengthened `k=2` hypothesis.

## What this does to the first unpaid implication

The original strict short-return obligation remains unpaid. This run proves that in a minimum counterexample it sits inside a much narrower, source-bound environment:

- one may work in an exact-outdegree-seven, oriented, arc-dominated, 3-vertex-strong spanning counterexample retaining a globally minimum three-cycle packing;
- every remainder sink has a direct return from a light cycle with fan at most two;
- only eight sink fan triples are possible;
- every pair deletion obeys the sharp `>=6`-one-witness / `=5`-three-witness dichotomy;
- the two-heavy sink types are exactly `(3,3,1)` and `(4,3,0)`, and a general degree-one-exception shortcut for `k=2` is source-refuted;
- whenever a return path meets the path-fan bound with equality, there is an explicit size-preserving packing exchange.

This is a direct attack on `BT4-MCR-v1`: it supplies the missing arc-domination/robust-`k=2` pressure and exposes the equality case that the strict-shortening formulation discards.

## First remaining inference for the next worker

A useful next statement, still genuinely unproved, is:

> Starting from the exact-seven global-minimum packing above, use 3-vertex-connectivity plus the sharp pair-deletion dichotomy to show that either a heavy sink/cycle has an `R`-internal return of length at most `m-2`, or a finite sequence of the neutral equality exchanges reaches a pair deletion whose remainder has outdegree at least three except for at most two vertices of outdegree two.

Either outcome closes the counterexample: the first contradicts the path-fan inequality; the second invokes the strengthened `k=2` theorem and adds the deleted pair of cycles.

The named partner `fleet03/B05` should attack precisely the disjointness-preserving linkage/exchange needed here, especially the two-heavy types `(3,3,1)` and `(4,3,0)`. Do not spend the next run reproving arc domination, the eight fan types, or the false degree-one robustness shortcut.

## Status

`ESSENTIAL_STEP_APPLIED`, not a full proof. No target-level truth promotion is claimed, and no near-directed cycle is counted as directed.
