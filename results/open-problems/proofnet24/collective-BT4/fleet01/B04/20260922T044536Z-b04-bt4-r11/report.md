# BT4 fleet01/B04 — maximal-remainder-arc potential collapses the double-pivot high-exit wall

Run: `20260922T044536Z-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-MAX-REMAINDER-ARC-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and role

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs and digons are allowed in the source problem. This report works only after the team's inherited reduction to an oriented exact-outdegree-seven minimum counterexample; it does not replace the source statement by the oriented special case.

My assigned role is to derive minimal-counterexample reductions that preserve the degree-seven and vertex-disjointness requirements, and to account exactly for what deletion, contraction, and packing exchanges lose.

The current literature boundary remains source-valid: Lichiardopol--Por--Sereni prove the genuine `k=3` case `delta^+ >= 5 => 3` vertex-disjoint directed cycles, while the 2026 Bessy--Muis--Sereni--Steiner--Wiederrecht relaxation still records genuine `k>=4` as unresolved and allows one reversed arc per cycle. No nearly-directed cycle is counted here.

## Team state actually consumed

Latest complete campaign-lead state actually used:

- fleet02/B04, controlling heavy-triangle strengthening, run `20260922T041847Z-b04-bt4-r11`, scientific commit `1277bd8435045651114cb6500f47674603f3f522`, shared handoff commit `d2a8f6e35cf92aa59fd540bd7a7fdacd2b595451`, candidate `BT4-HT-PREDECESSOR-SPLICE-v1` with the controlling v2 strengthening.

Its current global normal form is an oriented, exact-outdegree-seven, arc-dominated, 3-vertex-strong counterexample with a globally minimum-total three-cycle packing `(H,S,U)` and nonempty acyclic remainder `R`; packed cycles are chordless. In the four-remainder global-`NO-SIX` heavy-triangle branch, the lead reduces the obstruction to a two-port light-inport cover or a double heavy-fan escape cage. The remaining general frontier is packed-port splice/disjointness plus the separate `SIX` closure.

Named OTHER-account partner result actually consumed and applied:

- assigned partner fleet02/B05, run `20260922T042100Z-b05-bt4-e5df42d4`, candidate `BT4-R4-DOUBLE-PIVOT-CONFLUENCE-v1`, scientific commit `e979878752af60b802243237fee75f6d9ddb81f7`.

I use its exact long-source F2 state and simultaneous neutral pivot, not merely its outcome label.

## Compact conditional end-to-end route

Assume BT4 false. Strengthen the team's first minimization choice as follows:

1. among all three-cycle packings, minimize total packed order;
2. subject to that minimum, **maximize the number of arcs induced by the remainder**.

This secondary extremality is legitimate because all minimum-total packings leave the same number of remainder vertices. Every inherited argument that uses only minimum total packed order remains valid for this lexicographically chosen packing.

Run the lead's `SIX/NO-SIX` and canonical sink reductions on this packing. The lead already reduces `NO-SIX` to explicit sink-cross/pivot geometries. In the four-remainder long-source F2 branch, the assigned partner performs two commuting neutral pivots and exposes two newly freed vertices. The partner left a high-exit branch `e_s,e_v >= 2`, subsequently bounded by `|S|=6` or `|U|<=4`. The theorem below shows that, for the lexicographically chosen packing, that entire high-exit branch is impossible. Hence long-source F2 necessarily falls immediately into the partner's `SIX` or five-witness deficit interface.

The remaining target-level obligations are still the lead's genuine `SIX`/five-witness closure and packed-port splice closure. Therefore this is an essential reduction, not a full BT4 proof.

## Exact deletion and contraction accounting

For later use, if `C` is a directed cycle in the exact-seven normal form and

`a_C(v)=|N^+(v) intersect C|` for `v outside C`,

then deletion gives exactly

`d^+_{D-C}(v)=7-a_C(v)`.

If `C` is contracted to one vertex `c_C`, then for every outside vertex

`d^+_{D/C}(v)=7-a_C(v)+1_{a_C(v)>0}`,

while

`d^+_{D/C}(c_C)=|N^+(C) \ C|`,

the number of **distinct** external heads of `C`. Thus deletion loses every fan arc, while contraction refunds only one outgoing arc at an outside vertex that hit `C` and can still fail at the contracted vertex because repeated external heads collapse. A neutral packing exchange used below loses neither total packed order nor the number of remainder vertices, but it can alter the internal arc count of the remainder. That change is exactly what the secondary extremal potential controls.

## Lemma 1 — maximal-remainder-arc potential

Let `P=(H,S,U)` be a globally minimum-total three-cycle packing chosen, among all such packings, to maximize

`Phi(P)=|A(D[R_P])|`,

where `R_P` is its remainder. If `P'` is any other three-cycle packing with the same total packed order, then

`Phi(P') <= Phi(P)`.

This is immediate from the choice of `P`, but it is useful because every size-neutral source pivot or three-edge swap is now a one-sided potential move rather than merely an equality move.

## Imported double-pivot state

Use the exact long-source F2 state from fleet02/B05. The old remainder is

`R={x,y,z,c}`,

where `x,y` are sinks of `D[R]`. On the source packed cycle write consecutive vertices

`p -> q -> s -> t -> ... -> p`,

with `|S|>=6`. The imported relations include

- `p->x`, with `N^+(x) intersect S={q,s}`;
- `q->y`, with `N^+(y) intersect S={s,t}`;
- a unique light inport `u in U -> x`, with `N^+(x) intersect U={u+,u++}`;
- `c->x` and `N^-(x)={p,u,c}`;
- `{p,u,c}` induces a directed triangle;
- `q->z` and `q not->c`;
- crucially, the imported long-F2 proof gives that `z` cannot send to `x` or `c` inside the old remainder (and `y` is already a sink).

The partner simultaneously pivots at `y` and `x`:

`S_y = q -> y -> t -> S[t,q]`,

`U_x = u -> x -> u++ -> U[u++,u]`.

These are disjoint, preserve the two cycle orders, and leave `H` unchanged. Thus

`P'=(H,S_y,U_x)`

is another globally minimum-total packing, with new remainder

`R'={c,z,s,v}`,  where `v=u+`.

In a counterexample `D[R']` is acyclic. The exact degree accounting proved by the partner is

`N^+(s) intersect S_y={t}`,

`N^+(v) intersect U_x={u++}`.

Putting

`e_s=d^+_{D[R']}(s)`, `e_v=d^+_{D[R']}(v)`,

one gets

`d^+_{H union U_x}(s)=6-e_s`,

`d^+_{H union S_y}(v)=6-e_v`.

Thus `e=0` is a SIX witness, `e=1` is an exact five-witness, and the previously unresolved local wall is `e_s,e_v>=2`.

## Theorem — BT4-R4-MAX-REMAINDER-ARC-COLLAPSE-v1

> In the imported four-remainder long-source F2 double-pivot state, if the original minimum-total packing is chosen to maximize the number of arcs induced by its remainder, the simultaneous neutral double pivot cannot satisfy `e_s>=2` and `e_v>=2`.
>
> Consequently at least one of the two freed vertices satisfies `e<=1`: the branch produces either a SIX witness (`e=0`) or an exact five-witness (`e=1`) for the complementary packed pair. The partner's residual high-exit alternative `|S|=6 or |U|<=4` is therefore unnecessary in this lexicographic normal form.

### Proof

First bound the old remainder. Since `x` and `y` are sinks, neither has an outgoing arc in `R`. The imported long-F2 relations exclude

`z->x` and `z->c`.

Therefore every arc of `D[R]` belongs to the four-element set

`{ c->x, c->y, c->z, z->y }`.

Hence

`Phi(P)=|A(D[R])| <= 4`.                                      (1)

Now suppose for contradiction that the high-exit branch holds:

`e_s>=2`, `e_v>=2`.                                           (2)

In the new remainder `R'={c,z,s,v}`, the `e_s` arcs with tail `s` and the `e_v` arcs with tail `v` are distinct directed arcs, because they have different tails. Therefore

`Phi(P')=|A(D[R'])| >= e_s+e_v >= 4`.                          (3)

The double pivot preserves total packed order. By Lemma 1,

`Phi(P') <= Phi(P)`.                                           (4)

Combining (1), (3), and (4) gives the exact chain

`4 <= Phi(P') <= Phi(P) <= 4`.

Thus equality holds everywhere:

`Phi(P')=Phi(P)=4`, and `e_s=e_v=2`.                           (5)

Because every old-remainder arc is among the four possible arcs listed above, `Phi(P)=4` forces all four of them to exist. In particular,

`c->z`.                                                        (6)

On the other hand, (5) and `e_s+e_v=4` show that **all four** arcs of the new remainder already have tail `s` or `v`. Hence no arc of `D[R']` can have tail `c` or `z`. In particular,

`c not->z`.                                                    (7)

But `c` and `z` are unchanged vertices and the neutral pivot does not modify the digraph. The arc `c->z` from (6) must still be present in the induced new remainder `D[R']`, contradicting (7).

Therefore (2) is impossible. At least one of `e_s,e_v` is at most one, and the partner's exact budget formulas give the asserted SIX/five-witness output. QED.

## Why the secondary extremality is essential

The argument is not valid for an arbitrary minimum-total packing. If the old remainder had only the mandatory arc `c->x`, a neutral pivot could in principle increase the internal-remainder arc count to four without contradicting total-order minimality. The new contradiction comes specifically from selecting, at the outset, a maximum-`Phi` member of the already minimum-total packing class. Thus this is a genuinely different mechanism from the previous port-routing/cross-splice attempts, not a renaming of the same unpaid linkage statement.

## Consequence for the current team frontier

The assigned partner's long-source F2 branch now has the sharper source-bound conclusion:

`long F2 + |R|=4  =>  SIX witness or exact five-witness`,

provided the team's globally minimum packing is refined by maximum remainder-arc count. The former high-exit continuation through `|S|=6` or `|U|<=4` cannot occur for this canonical packing.

This has two immediate uses.

1. The lead can choose the lexicographic packing at the very start without invalidating its existing minimum-total proofs, so every subsequent neutral pivot inherits a monotone potential constraint.
2. The four-remainder F2 orbit no longer needs a separate bounded-cycle branch before returning to the common deficit-witness machinery.

The first essential unpaid implication after this reduction is now the **deficit-witness closure**: convert the forced SIX/five-witness supplied above, together with the lead's reciprocal/third-port interfaces, into two vertex-disjoint replacement cycles, a strict smaller three-packing, a directed cycle in an exchanged remainder, or a fourth disjoint directed cycle. The heavy-triangle two-port/double-escape splice remains a separate live interface.

## Failure and boundary checks

- The theorem uses the exact imported fact `z not->x,c`. Without that fact the old remainder may have more than four arcs, and the potential squeeze fails.
- It uses only genuine directed cycles and the genuine `k=3` input already built into the team's normal form; no one-reversed-arc relaxation is promoted.
- It assumes the inherited oriented normal form only after the valid digon reduction; it does not claim the source problem itself forbids digons.
- Acyclicity of both remainders is automatic in a BT4 counterexample: a remainder cycle would be disjoint from the three packed cycles and give the fourth cycle.
- No computation or finite census is used; the proof is exact.

## Exact source dependencies

- N. Lichiardopol, A. Por, J.-S. Sereni, *A Step toward the Bermond-Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979-992, DOI 10.1137/080715792: genuine `k=3` theorem and strengthened `k=2` input.
- S. Bessy, J. Muis, J.-S. Sereni, R. Steiner, S. Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026): current open-status boundary and near-directed relaxation only.
- fleet02/B04 controlling lead strengthening: scientific commit `1277bd8435045651114cb6500f47674603f3f522`; shared handoff commit `d2a8f6e35cf92aa59fd540bd7a7fdacd2b595451`.
- assigned partner fleet02/B05 `BT4-R4-DOUBLE-PIVOT-CONFLUENCE-v1`: scientific commit `e979878752af60b802243237fee75f6d9ddb81f7`.

No full BT4 proof, novelty claim, brain-assisted retrieval claim, public release, or automatic truth promotion is made.
