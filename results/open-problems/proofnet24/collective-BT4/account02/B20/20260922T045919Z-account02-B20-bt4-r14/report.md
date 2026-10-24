# account02/B20 BT4 research report — remainder-heavy fan escape

Run: `20260922T045919Z-account02-B20-bt4-r14`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Target: BT4  
Classification: `ESSENTIAL_STEP_APPLIED`  
FULL_TARGET_CHANGE: `NONE`  
MECHANISM_CHANGE: `YES — the lexicographically forced remainder-supported five-witness is converted immediately to the already-live genuine cross interface, so long-source four-remainder F2 no longer has a separate five-witness deficit branch.`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

No full BT4 proof or novelty claim is made.

## Source-exact target and controlling inputs

BT4 asks: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven has four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs and digons are allowed in the source theorem. The argument below uses the team's inherited oriented exact-seven minimal-counterexample normal form only after the valid digon/lower-k reduction.

Fresh campaign lead actually consumed:

- account02/B04 controlling strengthening, scientific commit `1277bd8435045651114cb6500f47674603f3f522`, candidate `BT4-HT-PREDECESSOR-SPLICE-v1` with v2 strengthening. Its current four-remainder heavy-triangle frontier is a two-port light-inport cover or a double heavy-fan escape cage; the first global unpaid interface is port-disjointness/splicing, plus the separate SIX closure.

Named OTHER-account partner actually consumed:

- account04/B06 `BT4-R4-LOWFAN-INPORT-TRIANGLE-v1`, run `20260922T041133Z-b06-bt4-r13`, scientific commit `caf1e01c679dd319fb80fc434bf5c9707c722f92`, report blob `d95ac60508cb0a415c33106169d1527da385406f`. In its long-source F2 branch (`|R|=4`, `|S|>=6`) it proves two distinct old remainder sinks `x,y`, adjacent source inports `p->x`, `q->y`, shifted source two-fans, an exact inport triangle around `x`, and two canonical sink-cross interfaces with disjoint singleton remainder interiors.

Newest compatible other-account reduction actually applied:

- account01/B04 `BT4-R4-MAX-REMAINDER-ARC-COLLAPSE-v1`, scientific commit `c6f43034c0e20bc92d12ea98e091867ae134173e`. Refine the globally minimum-total three-cycle packing by maximizing the number of arcs induced by its remainder. In the compatible long-F2 double-pivot state this rules out the high-exit branch and forces one newly freed remainder vertex to have `e<=1`: `e=0` is a SIX witness and `e=1` is an exact five-witness for the complementary packed pair.

The last three B20 substantive reports used different mechanisms: collision-funnel localization (`9565c809...`), aligned ladder-ray exchange tax (`23156aec...`), and lowfan return collapse (`e37b86df...`). Hence there is no three-unchanged-run trigger. This run changes method again by exploiting global minimum directly at a remainder-supported heavy fan and then arc domination.

## Compact conditional end-to-end route

Assume BT4 false. Use the inherited reduction to an oriented, exact-outdegree-seven, arc-dominated, 3-vertex-strong counterexample with a globally minimum-total packing `P=(C1,C2,C3)` of three vertex-disjoint directed cycles and nonempty acyclic remainder `R`. Refine the choice of `P`, without changing its minimum total order, to maximize `|A(D[R])|` as in account01/B04.

The current lead/partners reduce the live four-remainder branches to explicit SIX states, genuine packed-to-packed cross transitions, heavy-triangle port cages, and the long-F2 double-pivot state. In that long-F2 state the maximal-remainder-arc argument forces SIX or a remainder-supported exact five-witness. The lemma below shows that the five-witness alternative is already a genuine cross transition. Thus the long-F2 branch contributes no additional deficit-witness closure: it feeds the same `SIX/CROSS` frontier as the lead's heavy-triangle double-escape cage.

A complete BT4 proof still requires converting these cross/SIX interfaces into legal vertex-disjoint cycle replacements or a fourth cycle, and closing the remaining short-source/larger-remainder branches.

## New lemma — remainder-heavy fan escape

**Lemma (`BT4-R-HEAVY-CROSS-v1`).**  Work in the inherited globally minimum three-cycle packing normal form. Let `A` be one packed cycle and let `w` be a vertex of the acyclic remainder. If

`m_A(w) := |N+(w) intersect A| >= 3`,

then there is a genuine packed-to-packed directed transition ending on `A` whose internal vertices all lie in the remainder. In particular, `A` sends no arc to `w`.

### Proof, part 1: a heavy target cannot enter a remainder witness

Suppose for contradiction that some `b in A` satisfies `b->w`.

Choose a fan target `a in N+(w) intersect A` minimizing the forward directed distance

`d = dist_A(a,b)`.

The inherited normal form is oriented, so `b->w` excludes `w->b`; hence `a!=b`. There are at least three distinct fan targets of `w` on `A`, all at distinct positive distances in `{1,...,|A|-1}` from `b`. Therefore

`d <= |A|-3`.

Now

`K = b -> w -> a -> A[a,b]`

is a simple genuinely directed cycle. Its order is

`|K| = d+2 <= |A|-1`.

The vertex `w` lies in the remainder, so `K` is disjoint from the other two packed cycles. Replacing `A` by `K` therefore gives another three-cycle packing whose total order is at least one smaller than `P`, contradicting global minimality.

Thus

`A not-> w`.                                                     (1)

Notice that this uses genuine vertex-disjoint directed cycles and minimum total packing order; it does not use a nearly-directed relaxation or an average-degree surrogate.

### Proof, part 2: domination ladders force a cross

Pick any `a in N+(w) intersect A`. Arc domination of `w->a` gives a vertex `z0` with

`z0->w` and `z0->a`.

By (1), `z0` cannot lie on `A`.

If `z0` lies on either of the other packed cycles, the single arc `z0->a` is already a genuine cross-packed transition into `A`.

Otherwise `z0` lies in `R`. Repeatedly dominate the arc `zi->w`: while `zi in R`, choose `z(i+1)` with

`z(i+1)->zi` and `z(i+1)->w`.

No remainder vertex can repeat. A repetition would produce a directed cycle along the chain inside `R`, contradicting acyclicity. Since `R` is finite, the process reaches a first `zt` outside `R`. Every ladder vertex, including `zt`, sends to `w`, so (1) excludes `zt in A`. Therefore `zt` lies on one of the other two packed cycles.

The directed path

`zt -> z(t-1) -> ... -> z0 -> a`

has endpoints on two distinct packed cycles and every internal vertex in `R`. It is the required genuine cross-packed transition. QED.

## Corollary — the forced five-witness branch is not a separate frontier

Apply the lemma to account01/B04's compatible long-F2 double-pivot conclusion, which is built from the same long-source F2 state isolated by the named partner account04/B06.

After the two neutral pivots the newly freed vertex `w` belongs to the new remainder. In the `e=1` alternative it has one outarc inside the new remainder and one outneighbor on its former/support cycle; exact outdegree seven leaves exactly five outgoing arcs into the complementary pair of packed cycles. Hence one of those two cycles, call it `A`, receives at least three arcs from `w`.

By `BT4-R-HEAVY-CROSS-v1`, a genuine cross-packed transition into `A` follows. Therefore, under the lexicographic minimum-packing choice,

`long-source F2 + |R|=4  =>  SIX OR genuine CROSS`.              (2)

The exact five-witness output produced by maximal-remainder-arc collapse is therefore an interface generator, not an additional terminal obstruction.

This directly uses the named partner's long-F2/two-sink state: its `R4-TWOSINK-SPLICE` branch can first undergo the compatible simultaneous neutral double pivot; the maximal-remainder-arc potential gives `e<=1`; and (2) removes `e=1` into CROSS. What remains is the already-common splice problem, not a special two-sink deficit witness.

## Interaction with the current campaign lead

The lead's heavy-triangle double-escape cage already forces cross-packed transitions from cycle-supported heavy witnesses. The new lemma is the exact remainder-supported companion: it does not require a support predecessor, a marked bypass inequality, or the heavy triangle. Thus both major four-remainder mechanisms now feed the same interface:

- cycle-supported heavy witness with no heavy-target inport -> cross by the lead's domination escape;
- remainder-supported heavy witness -> heavy-target inport is impossible by strict packing minimality -> cross by the domination ladder above.

This removes a location mismatch that previously allowed a remainder-supported five-witness to remain a separate named deficit branch.

## First unpaid universal implication after this step

The first essential target-level implication remains a **source-valid packed-port splice**, now in a narrower form.

> **BT4-CROSS-SPLICE / SIX-CLOSURE.** For every finite counterexample in the inherited oriented exact-seven, arc-dominated, 3-vertex-strong normal form, for every lexicographically chosen globally minimum three-cycle packing with acyclic remainder, whenever the current reductions supply either (a) a genuine packed-to-packed directed transition whose internal vertices lie in the remainder (including the canonical sink cross, the heavy-triangle escapes, or (2)), or (b) a remainder-supported SIX witness, prove that the accompanying reciprocal/third-port/fan data force at least one of: two vertex-disjoint replacement directed cycles, a strict smaller three-cycle packing, a directed cycle in an exchanged remainder, or a fourth directed cycle disjoint from the packed three.

A single CROSS is not itself counted as a fourth cycle. The quantifiers remain over arbitrary graph order; the original theorem allows digons; no edge-disjoint or one-reversed-arc substitute is accepted.

For the lead's exact four-remainder heavy-triangle state, the more local unpaid form is its port-disjointness theorem: combine the two-port light-inport cover or double heavy-fan escape cage with the reciprocal sink cross and the account03/B05 third-port interface so that packed target segments do not coalesce.

## Before / after / movement

Before: named-partner long F2 -> explicit two-sink adjacent-port state; maximal-remainder-arc double pivot -> SIX or remainder-supported exact five-witness; lead heavy-triangle -> packed-port disjointness plus SIX.

After: every remainder-supported heavy fan of size at least three forces a genuine CROSS; therefore the exact five-witness alternative in long F2 is absorbed into CROSS, giving the source-bound reduction (2).

Target-level movement: none; BT4 remains open.

Mechanism movement: material; one previously separate deficit-witness branch is eliminated into the common cross interface.

Stagnation: no three-run unchanged implication. The method is different from the last three B20 runs and from the partner's two-sink construction: strict packing minimality is applied directly to a remainder-supported heavy target, then arc domination is iterated.

Next method: attack port coalescence itself. In the four-remainder states, classify the first common remainder vertex of two required cross ladders. If the ladders are internally disjoint, perform the two-cycle splice. If they merge, use the fact that every ladder vertex sends to the same heavy witness (and the lead's exact predecessor-chain identities) to force either a forbidden heavy-target inport, a strict shorter fan-return cycle, or a directed cycle in the exchanged remainder. Preserve the separate SIX branch until this is proved.

## Boundary checks

- Global minimum total packed order is essential in part 1. Without it, `K` need not contradict anything.
- `w in R` is essential to the simple replacement argument: for a cycle-supported witness, replacing `A` by `K` may collide with the witness's support cycle, which is why the lead needed a separate argument.
- Acyclicity of `R` is essential for ladder termination without repetition; in a counterexample it follows because a remainder cycle would itself be the fourth cycle.
- Arc domination is used only in the ladder step.
- The lemma needs only `m_A(w)>=3`; the exact-five application supplies this by pigeonhole from five arcs into two complementary packed cycles.
- The result closes neither the CROSS splice nor the SIX interface and makes no claim about the small-source `|S|<=5` or larger-remainder branches.
