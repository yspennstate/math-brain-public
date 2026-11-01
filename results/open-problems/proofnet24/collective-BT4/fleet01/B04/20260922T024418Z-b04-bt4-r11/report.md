# BT4 fleet01/B04 — sink-lift collapse to a canonical length-two cross

Run: `20260922T024418Z-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-MCR-v5-sink-cross-collapse`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem, so directed digons count.

The current external source check remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract states that the genuine conjecture remains unresolved for every `k>=4`; its theorem at the same `2k-1` threshold permits a packed cycle to require reversal of one arc. No such relaxed cycle is used below as a directed cycle.

The lower-k source used in the inherited normal form is Lichiardopol--Por--Sereni, *A Step toward the Bermond--Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992, DOI 10.1137/080715792: minimum outdegree five forces three vertex-disjoint directed cycles, and the same paper proves the strengthened two-cycle theorem with all outdegrees at least three except at most two vertices of outdegree two.

## Exact team state consumed

Newest complete campaign-lead package read:

- fleet02/B04 `20260922T022208Z-b04-bt4-r11`, primary report blob `930c6906cc2532269bc35e0d0b0ea8e246eb250b`;
- controlling correction blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`.

The lead's inherited normal form is an oriented exact-outdegree-seven counterexample `D` with a globally minimum-total three-cycle packing `(A,B,C)`, nonempty acyclic remainder

`R = V(D) \ (V(A) union V(B) union V(C))`,

chordless packed cycles, domination of every arc, and 3-vertex-strongness. For an `R`-internal path from a packed cycle `C` to `x in R` of edge-length `L`, if

`m_C(x)=|N+(x) intersect V(C)|`,

the repaired path-fan inequality is

`L >= m_C(x)-1`,

with equality producing an explicit size-neutral globally minimum packing exchange and an acyclic exchanged remainder.

Named OTHER-account partner result actually applied:

- fleet02/B05 `BT4-RSC-v5-two-support-lift`, run `20260922T022612Z-b05-bt4-888b6a96`.

The exact partner lemma used is its finite domination lift: for `z,rho in R` with `z->rho`, repeated domination produces a packed vertex `p` and a directed path `p -> ... -> z` with internal vertices in `R`, while every ladder vertex, including `p`, sends a direct arc to `rho`. In particular, every internal `R` arc `z->rho` yields a packed predecessor `p->rho`.

Compatible newer exchange work also read: fleet03/B05 `BT4-TCEX-v4-switchwall`, run `20260922T024158Z-b05-bt4-r11`, which reduces pairwise linkage overlap and the exact-six dual reachability wall to the same cross/support-exchange interface. No peer outcome label is promoted to a theorem.

## New Lemma 1 — every remainder sink has a packed predecessor

Let `x` be a sink of the acyclic digraph `D[R]`. Then there is a packed vertex

`p in A union B union C`

with a direct arc

`p -> x`.

### Proof

Since `d_D^+(x)=7` and `x` has no outneighbor in `R`, every outneighbor of `x` lies on the packing. Choose any arc

`x -> a`,  `a in A union B union C`.

Every arc is dominated, so there exists a vertex `q` with

`q->x` and `q->a`.

If `q` is packed, take `p=q`.

If `q in R`, apply the named partner's domination-lift lemma to the internal remainder arc `q->x`. It returns a packed apex `p` which, by the exact conclusion of that lemma, sends a direct arc to the target `x`. Hence `p->x` in either case. QED.

The point is that this does not merely give a packed-to-`x` path: it gives a **direct packed inport** to every remainder sink.

## New Lemma 2 — canonical sink-cross theorem

Let `x` be any remainder sink and let `p->x` be the packed inport from Lemma 1. Let `S` be the packed cycle containing `p`. Then

`m_S(x) <= 2`.                                                    (1)

Consequently `x` has at least five outneighbors on the other two packed cycles, and there is a genuinely directed length-two cross-packed path

`p -> x -> y`                                                     (2)

from `S` to a different packed cycle, with unique internal vertex `x in R`.

### Proof

The direct arc `p->x` is an `R`-internal path from the packed cycle `S` to `x` of edge-length `L=1`. The lead's repaired path-fan inequality therefore gives

`1 >= m_S(x)-1`,

which is exactly (1).

Because `x` is a sink of `R` and has exact outdegree seven, all seven outgoing arcs of `x` hit the three packed cycles. At most two hit `S`, so at least five hit `A union B union C - S`. Choose any such target `y`. Then `p->x->y` is a directed path between two distinct packed cycles and its only internal vertex is in the old remainder. QED.

### Strengthening: heavy-target fork

Among the two cycles different from `S`, at least one, say `H`, receives at least three arcs from `x`. Hence every sink-cross state has a canonical heavy target with

`m_H(x)>=3`.

No vertex of `H` can send an arc to `x`: such an arc would be an `H`-to-`x` path of length one, contradicting the same path-fan inequality because `1 < m_H(x)-1` for `m_H(x)>=3`.

Thus the canonical cross is not an arbitrary cross transition. It has a **light source** (`m_S<=2`) and at least one **heavy target** (`m_H>=3`) with no return arc into the sink.

## Corollary 3 — the no-cross branch is empty in the inherited normal form

Every globally minimum three-cycle packing in the inherited normal form has a genuine `R`-internal cross-packed transition. There is no minimum-packing state, SIX or NO-SIX, in which all cross-packed transitions are absent.

This follows immediately from Lemma 2 by taking any sink of the finite acyclic remainder.

This is stronger than the previous small-remainder and witness-specific cross-existence statements. It does not use the pair-deletion SIX/NO-SIX split at all.

## Corollary 4 — exact interaction with the lead's SIX/NO-SIX dynamics

Let `S` be the source cycle of the canonical sink inport.

- If `m_S(x)=2`, then the path-fan inequality is at equality (`L=m_S-1=1`). The lead's equality-completion principle therefore gives an explicit size-neutral globally minimum exchange of `S` through `x`, while the length-two cross (2) is simultaneously present.
- If `m_S(x)<=1`, then `x` sends at least six arcs into the other two packed cycles. Thus `x` is itself a remainder-supported six-or-seven fan witness for that packed pair, again while (2) is present.

Therefore every remainder sink enters the existing proof interfaces in a strictly stronger form:

`canonical length-two cross + (neutral equality exchange OR remainder-supported 6+ fan)`.

In particular, in the global NO-SIX regime every sink inport must have `m_S(x)=2`; hence **every NO-SIX minimum-packing state already contains a canonical length-two cross** in addition to its neutral pivot. The lead's separate long neutral-orbit obstruction is therefore not needed merely to *reach* cross geometry. If the cross-splice closure is proved for the canonical sink-cross, the long-orbit branch disappears from the end-to-end proof.

## Corollary 5 — exact deletion and contraction loss at the canonical source cycle

This records the part relevant to this slot's minimal-counterexample assignment.

For any packed cycle `C` and vertex `v outside C`, write

`a_C(v)=|N+(v) intersect C|`.

Deleting `C` changes the outdegree exactly by

`d^+_{D-C}(v)=7-a_C(v)`.                                         (3)

Contracting all of `C` to one vertex `c` changes the outside outdegree exactly by

`d^+_{D/C}(v)=7-a_C(v)+1_{a_C(v)>0}`,                            (4)

because all `a_C(v)` distinct targets on `C` become one target `c`. The contracted vertex has outdegree equal to the number of distinct external heads hit by vertices of `C`; multiplicity of arcs leaving `C` is lost.

Apply this to the canonical source cycle `S` and sink `x`. By Lemma 2, `a_S(x)<=2`, so

`d^+_{D-S}(x)>=5`,

and

`d^+_{D/S}(x)>=6`.

More precisely, contraction preserves `x` at outdegree seven when `a_S(x)<=1`, while the only possible one-unit loss occurs at `a_S(x)=2`, exactly the equality case in which the lead already supplies a neutral packing exchange. This is a local preservation statement only: arbitrary other outside vertices can have larger `a_S`, and the contracted vertex itself can have fewer than seven distinct external heads. Those are the exact two reasons naive cycle contraction still does not preserve the global minimum-outdegree-seven hypothesis.

## Compact conditional end-to-end proof at the new frontier

The previous lead package required three campaign-level closures: exact-six `H6`, cross-linkage `HX`, and long neutral-orbit/strict-collar `HS`.

The new sink-cross theorem compresses the route.

1. Reduce a hypothetical BT4 counterexample to the inherited exact-seven, oriented, arc-dominated, globally-minimum packing normal form with nonempty acyclic remainder.
2. Choose a sink `x` of `R`.
3. Lemma 1 gives a direct packed inport `p->x` by consuming the partner's exact domination lift.
4. Lemma 2 gives a canonical length-two cross `p->x->y`, with source fan at most two and a heavy target fan at least three.
5. If the source fan is two, equality-completion supplies a neutral exchange as an additional object; if it is at most one, `x` is already a remainder-supported six-or-seven fan as an additional object.

Hence a full proof follows from the following single sharpened splice statement, together with the already-established normal-form reductions:

> **(SC) Canonical sink-cross splice.** In the inherited normal form, whenever `x` is a remainder sink, `p in S` satisfies `p->x`, `m_S(x)<=2`, and `x` has a target on a distinct packed cycle, the canonical length-two cross together with the heavy-target structure forces either two vertex-disjoint replacement directed cycles, a strict reduction of the three-cycle packing, a directed cycle in an exchanged remainder, or a configuration already closed by a proved lower-k input.

This is strictly narrower than the lead's previous general `HX`: the cross has exactly one remainder vertex, that vertex is a sink, the source fan is at most two, the two other fan counts sum to at least five, and at least one target cycle is heavy and has no arc into the sink.

Fleet03/B05 `BT4-TCEX-v4-switchwall` is immediately compatible with this compression: its newest overlap/wall work already exports cross or support-exchange objects, so the next exchange worker can target `(SC)` rather than first manufacturing an arbitrary cross from a long collar.

## First essential missing implication after this run

The decisive unpaid mathematics is no longer existence of cross geometry, no-six neutral-orbit escape, or the isolated exact-six companion interface. It is the disjointness-preserving **splice of the canonical sink-cross**:

Given

`p in S -> x in R -> y in T`, `S!=T`, `x` a sink of `R`,

with

`m_S(x)<=2`, `m_T(x)>=1`, and `max(m_T(x),m_U(x))>=3`,

construct a second compatible return/crossing so that two packed cycles can be replaced by two vertex-disjoint directed cycles, or force a strict packing reduction / fourth cycle. A single cross transition by itself creates only one cross-spliced cycle, so this last implication cannot be skipped.

A useful exact substructure for that attack is:

- every packed in-neighbor of `x` lies on a cycle `C` with `m_C(x)<=2`, by the same length-one path-fan inequality;
- every cycle with `m_C(x)>=3` has no arc to `x`;
- if the source has fan two, the source-side equality exchange is already legal and preserves acyclic remainder;
- if the source has fan at most one, the complementary pair receives at least six arcs from `x`.

This is the canonical local state that the next splice proof should use; it avoids the long-path coalescence ambiguity present in the earlier generic `HX` statement.

## Failure checks and nonclaims

- The original target permits digons; orientation is used only after the inherited minimum-counterexample reduction that already eliminates the digon case using the genuine k=3 theorem.
- The partner domination lift is used with exactly its proved hypotheses: the internal arc is between two vertices of the old acyclic remainder.
- The direct inport `p->x` is essential. A mere packed-to-sink path would not give the same length-one fan bound.
- A cross transition is **not** counted as a two-cycle replacement or a four-packing. `(SC)` remains unpaid.
- Equations (3)-(4) describe exact local degree loss; they do not claim deletion or contraction preserves global minimum outdegree seven.
- No edge-disjoint surrogate, near-directed cycle, finite-order computation, or average-degree replacement is used.
- No full proof or novelty claim is made.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The main new theorem is universal inside the inherited normal form: **every minimum-packing state contains a canonical length-two cross through a remainder sink**. This collapses the task of *reaching* cross geometry and narrows the full BT4 frontier to a highly structured sink-cross splice, with exact local deletion/contraction loss accounting at its source cycle.
