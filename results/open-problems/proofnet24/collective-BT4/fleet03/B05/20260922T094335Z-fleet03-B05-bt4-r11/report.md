# BT4-F3-ZIP-LANE-COLLISION-FORCING-v1

**Run:** `20260922T094335Z-fleet03-B05-bt4-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Role:** fleet03/B05 disjointness-preserving exchange  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Target status:** `OPEN_NOT_PROVED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and control boundary

BT4 asks whether every finite loopless simple digraph with minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles; opposite arcs are allowed in the original target, hence digons count. This run remains inside the inherited oriented minimal-counterexample branch after the standard digon reduction. No reversed-arc cycle from the relaxed 2026 theorem is counted as a target cycle.

Fresh owner control remains revision `2026-09-22.2`, active programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The exact B05 assignment is to prove the disjointness-preserving exchange promised by the current linkage/two-partition candidate. The assigned other-account partner is `fleet04/B06`. Old installation/benchmark work is superseded.

## 2. Exact peer mathematics consumed

### Assigned partner fleet04/B06

Consumed `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`, shared handoff commit `f3d4000bb1350abc6bbcf4432fc5f087f4fe0d4a`, whose canonical report is `proofnet24/collective-BT4/fleet04/B06/20260922T070806Z-b06-bt4-coll11/report.md` (reported blob `ff7bbac3a8211262bc273f6fa02b102d3ace16dd`). Its usable conclusion is that, in the long-support/no-bypass/no-third-support-mediation residual, both ordered directions between the two light supports can be taken to have rank-two remainder connector families; opposite-direction remainder intersections already collapse to same-support bypasses or a bounded short-support output. Therefore another bare rank increment is not the missing argument: only packed-port compatibility remains in that branch.

### Current port-order boundary

The previous B05 theorem `BT4-MONOTONE-QUADRANT-RANK-WALL-v1` showed that rank two in both directions still does not automatically give two vertex-disjoint mixed cycles. In the monotone same-quadrant order the two supports require opposite connector pairings. The positive two-splice criterion needs an inverted forward pair together with a reverse endpoint in the matching open gaps.

### Fresh other-account mechanism change

Because repeated B05 runs had reached the same port-order debt, this run changes mechanism on the same BT4 target rather than adding another linkage. It applies fleet04/B04 `BT4-F3-R3-GUARD-ZIPPER-v1`, canonical report commit `212e68c6c1b6020e7b819ef0a933cea81a097776`, blob `fd5d9dc2174c0a254784a8243c19ffa9dabaeb6a`.

In its residual-three F3 defect-one branch, outside SIX, cyclic remainder/four-pack, exact R4, strict packing decrease and triangular/short-support exits, a mixed long-support tight-pivot orbit becomes a strict alternating zipper. Writing `P_i` for mature pivots and `h_i` for the fresh hole freed by `P_i`, it proves

`R_i = {h_{i-2},h_{i-1},h_i}`,

`sink(P_i)=h_{i-3}`,

and, crucially, the original digraph contains

`h_j -> h_{j+3}`                                                    (1)

for every mature index `j`. The heavy packed cycle `H` is untouched throughout this zipper.

## 3. New theorem: lane recurrence forces collision or an actual four-pack

### Theorem (`BT4-F3-ZIP-LANE-COLLISION-FORCING-v1`)

Assume the mature ZIP branch above persists and let

`L_r = (h_{r+3k})_k`,  `r in {0,1,2}`,

be its three hole lanes. Then either

1. there is a **cross-lane recurrence** `h_i=h_j` with `i not congruent j (mod 3)`, or
2. the original digraph already contains four pairwise vertex-disjoint directed cycles.

More quantitatively, putting `N=|V(D)\V(H)|`, any no-exit mature ZIP prefix of `3(N+1)` pivots already forces one of these two outcomes.

### Proof

Assume there is no cross-lane recurrence. Hence the sets of vertices occurring in `L_0,L_1,L_2` are pairwise disjoint.

Consider the first `3(N+1)` mature holes. Each lane contributes `N+1` occurrences, all lying in the finite set `V(D)\V(H)`, which has only `N` vertices. Thus every lane contains a repeated vertex. For each residue `r`, choose a first repeated value along that lane,

`h_{r+3a_r}=h_{r+3b_r}`,  with `a_r<b_r`,

with `b_r-a_r` minimal. By the minimal choice, all intermediate lane vertices are distinct. The zipper arcs (1) therefore give the genuine directed cycle

`C_r = h_{r+3a_r} -> h_{r+3(a_r+1)} -> ... -> h_{r+3(b_r-1)} -> h_{r+3b_r}=h_{r+3a_r}`.

Because there is no cross-lane recurrence, `C_0,C_1,C_2` are pairwise vertex-disjoint.

Every `h_i` is outside `H`: each hole is freed from one of the two light supports, and the ZIP pivots never alter or absorb a vertex of the untouched heavy support `H`. Hence every `C_r` is vertex-disjoint from `H`.

Therefore

`H, C_0, C_1, C_2`

are four pairwise vertex-disjoint genuinely directed cycles of the original digraph, contradicting a BT4 counterexample. This proves the dichotomy. QED.

## 4. First-collision arithmetic

The theorem reduces the indefinitely surviving ZIP branch to a finite cross-lane collision rather than an unbounded port-order orbit. A first such collision also has a useful exact index restriction.

Let `h_i=h_j` be the first later occurrence of the vertex `h_i` and suppose it is cross-lane. The residual identity

`R_k={h_{k-2},h_{k-1},h_k}`

immediately excludes `j-i=1` and `j-i=2`, because either equality would collapse a three-vertex residual set.

Moreover, `h_i` is the sink inserted by pivot `P_{i+3}`. Until its first later occurrence it is not freed, so it remains on the light support used by `P_{i+3}`. The collision occurrence `h_j=h_i` is created precisely when `P_j` frees that vertex, so `P_j` uses that same light support. Since the zipper alternates supports, `j` and `i+3` have the same parity; equivalently `j-i` is odd.

Because the recurrence is cross-lane, `j-i` is not divisible by three. Thus any first cross-lane recurrence satisfies

`j-i >= 5`,  and  `j-i congruent 1 or 5 (mod 6)`.                   (2)

This is not yet a contradiction, but it sharply identifies the next finite interface: a vertex inserted into one light support reappears only when the predecessor-step zipper returns to and frees it after an odd, non-multiple-of-three number of pivot positions.

## 5. Transfer to the disjointness problem

The previous generic linkage route stalled because clean rank-two families can have incompatible port parity. The new theorem supplies a different kind of forcing: a BT4 counterexample cannot support a collision-free zipper for arbitrarily many steps. If the zipper terminates before the quantitative bound, it has already hit one of the recognized outputs in the fleet04/B04 theorem. If it does not terminate, it must create the concrete cross-lane recurrence (2), because the alternative is an actual four-cycle packing, not merely a new connector.

The assigned partner fleet04/B06 remains directly relevant at the boundary: any attempt to resolve the collision by opposite remainder linkages need not re-prove intersection handling, since its theorem already converts such intersections into taxed same-support bypasses or bounded support. Thus the unpaid work is now a packed-support return event, not connector rank or uncontrolled remainder intersection.

## 6. First exact unpaid implication

`BT4-F3-ZIP-CROSS-LANE-COLLISION-CLOSE-v1`:

> In the residual-three F3 strict ZIP normal form, let `h_i=h_j` be the first cross-lane recurrence. Using the predecessor-step evolution on the light support that received `h_i` at `P_{i+3}`, together with (2), prove that the return which frees `h_i` forces either the B05 inverted/matched-gap two-splice criterion, a same-support taxed bypass, third-support mediation, triangular/short support, SIX, cyclic exchanged remainder, exact R4, strict packing decrease, or a fourth directed cycle.

This is a finite return-to-insertion-frontier problem. It is strictly narrower than asking for another clean connector or another Menger rank increment.

## 7. Honest boundary

BT4 is not proved. The MONO branch, triangular bounded branch, lead four-port coalescence, SIX/H5 closures, other bounded F2/F3 states and the seven-remainder branch remain separate debts. This report does not claim a lane cycle alone is a fourth cycle; the four-pack conclusion uses **all three pairwise-disjoint lane cycles together with the untouched heavy cycle**. No computation was required for the new theorem. No authenticated brain retrieval or receiver-context use occurred.
