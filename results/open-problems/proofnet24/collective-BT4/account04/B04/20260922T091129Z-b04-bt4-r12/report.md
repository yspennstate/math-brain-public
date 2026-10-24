# BT4-F3-R3-GUARD-ZIPPER-v1

**Run:** `20260922T091129Z-b04-bt4-r12`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Role:** account04/B04 structural case split  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Target status:** `OPEN_NOT_PROVED`  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source boundary

BT4 asks: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are permitted in the original statement, so digons count.

The current public source check remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract explicitly states that the genuine conjecture remains unresolved for every `k>=4`; its theorem allows a cycle to become directed after reversing one arc, so it does not settle BT4.

The inherited normal form used here is the team lead's oriented exact-outdegree-seven minimal-counterexample state: after the standard digon reduction, choose a three-cycle packing lexicographically by minimum total packed order and then maximum arc count in its acyclic remainder. The surviving packed cycles are chordless; the working reduction is arc-dominated and 3-vertex-strong. I do not re-prove the complete normal-form chain in this report.

## 2. Source-bound inputs actually consumed

### Team lead

Latest complete lead source read this run: account02/B04, `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, report

`proofnet24/collective-BT4/account02/B04/20260922T0619Z-b04-bt4-r11/report.md`,

creation commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`.

The lead's compact global tree remains: exact-seven/oriented minimal counterexample -> three-cycle minimum packing -> `SIX` versus `NO-SIX`; the live NO-SIX sink states reduce to `(3,2,2)` fan geometry and packing exchanges. The lead's own four-remainder heavy-triangle debt has been narrowed to coalesced packed ports after a source-valid CROSS/BYPASS witness lift. Separate global debts remain SIX, bounded F2/F3 short-support states, and the seven-remainder pinwheel/support-carried branch.

### Assigned OTHER-account partner

Newest partner snapshot consumed: account01/B05 `BT4-F3-R3-PIVOT-GUARD-v1`, shared handoff blob `b2ece782eca132cc525fcb53af5633627a0d7a81` (09:06Z handoff). It states the two guard facts used below for the residual-three F3 defect-one pivot orbit:

1. after a tight light-support pivot, its fresh hole cannot be a residual sink in a NO-SIX/no-R4 survivor; and
2. that old hole cannot become a sink while the new support edge joining the old return port to the inserted sink remains intact; a later pivot on that support can break the guard only at the return port or its predecessor.

The handoff advertises canonical scientific commit `7f56e338eba93850130bb51d86a84182ced1b520`, but that commit/path did not resolve in the authorized mathematical archive during this run. I therefore do **not** claim an independent read of that advertised canonical report. To prevent this provenance gap from becoming a proof dependency, Section 4 below re-derives exactly the guard facts needed from the earlier source-bound defect-one collar and the current packed-support geometry.

Earlier compatible partner snapshot `BT4-F3-R3-DEFECT1-PIVOT-v1`, shared blob `01189044d46ddcb506113e0207f75506c33248fa`, supplies the defect-one collar and the legal tight-pivot alternative. Separately, account01/B05 has source-readable canonical earlier work in the mathematical archive, including the common-port reverse-cross theorem at commit `5f4ad4452b7b940cbe8f9106a934745496a75a36`; it is background compatibility evidence, not a hidden premise of the new lemma.

### Independent cyclic-order compatibility check

I also read the source-valid account03/B05 result `BT4-MONOTONE-QUADRANT-RANK-WALL-v1`, canonical mathematical commit `91a121c586b602b83a9d15d6c7937cdea3d665d8`. It proves that merely raising clean connector rank does not close the long two-support exchange when forward ports remain monotone in the same cyclic quadrant; the positive splice needs an inverted forward pair plus a reverse endpoint in the matched gaps. This matters for the remaining zipper leaf: the next step must force an inversion or a recognized exit, not merely manufacture another path.

## 3. Compact conditional end-to-end route

A complete BT4 proof would follow from the shared reductions if the remaining explicit leaves were closed:

1. reduce a minimal counterexample to the oriented exact-seven, arc-dominated, 3-vertex-strong normal form;
2. choose a globally minimum three-cycle packing, with acyclic remainder and chordless supports;
3. split into SIX and NO-SIX and use the existing deficit/five-witness reductions;
4. close the lead's four-remainder coalesced-port branch and the remaining bounded F2/F3 and seven-remainder branches;
5. in the residual-three F3 defect-one branch, close the finite tight-pivot orbit.

This run attacks item 5. The previous B04 split was `MONO` versus `TRI`: either the orbit eventually stayed on one light support, or a support switch forced a triangular light support after a further same-support return. The new result replaces the still-vague mixed-support side by a much sharper **alternating guard zipper** with a three-lane directed hole ladder.

## 4. Re-derivation of the guard used in this report

Work in the residual-three F3 defect-one state. The current three-cycle packing covers `n-3` vertices while the global minimum three-packing covers `n-4`. Let `t` be a residual sink. Outside SIX, its packed fan profile is `(3,2,2)`. The heavy support does not return to `t` outside the exact-R4 exit; at least one light support does return, and a surviving light return is tight.

Let a light support before a pivot contain the directed segment

`c -> x -> y -> ... -> c`,

where `x=c+`, `y=c++`, with `c->t` and

`t->x,y`.

The tight pivot replaces the support segment by

`c -> t -> y -> ... -> c`

and frees `x` into the three-vertex remainder. The original graph arcs `c->x` and `t->x` remain.

### Guard lemma

In a NO-SIX/no-R4 survivor, `x` cannot be a residual sink while the packed support still contains the edge `c->t`.

**Proof.** Suppose `x` were a residual sink. The returning packed support gives two in-neighbors `c->x` and `t->x`. Orientedness therefore forbids `x->c,t`.

The defect-one collar says that, from the return arc `c->x`, every target of `x` on this support lies within forward support distance at most three from `c`. In the current support, the distance-one vertex is `t`, which `x` cannot hit. Hence at most the distance-two and distance-three positions are eligible. A three-fan on this support is impossible. If the support is one of the two light supports, its required two-fan must use both eligible positions, including the distance-three position, which is exactly the defect-one equality compression to an `n-4` three-packing with four-vertex complement: either the complement is cyclic and BT4 is already obtained, or this is the recognized exact-R4 restart. The heavy three-fan case is even more immediately impossible because only two eligible positions remain. Thus no NO-SIX/no-R4 survivor has `x` as sink while `c->t` survives. QED.

A pivot on another packed support does not change `c->t`. A later pivot on this same support changes/removes `c->t` only if its pivot site is `c` (which frees/removes `t`) or the current predecessor `c^-` (which frees/removes `c`). Therefore:

> **Guard-breaking rule.** The old hole `x` cannot become a sink until a later pivot on this support occurs at `c` or `c^-`.

This is exactly the part of account01/B05 `BT4-F3-R3-PIVOT-GUARD-v1` needed below, now source-independent of its unavailable advertised canonical file.

## 5. New lemma — two-generation guard break forces a triangle

### Statement

Start with the tight pivot above at port `c`, inserting sink `t` and freeing `x`. Suppose a later pivot on the **same** support is the first pivot that breaks `x`'s guard. Let its port be `d` and inserted sink be `v`. Thus

`d in {c,c^-}`.

Suppose `x` subsequently becomes a residual sink and, before an exit to SIX/cyclic remainder/exact R4, `x` pivots on this same support in a way that breaks the fresh hole's guard from the `d`-pivot. Let its port be `e`; then

`e in {d,d^-}`.

Then the original digraph contains the genuine directed triangle

`T = t -> x -> v -> t`.

### Proof

The first pivot gave the ambient arc

`t -> x`.                                                     (1)

At the guard-breaking `d`-pivot, `v` is the residual sink and therefore hits the first two successors of `d` on the current light support.

- If `d=c`, those first two successors are `t` and the vertex following `t`.
- If `d=c^-`, those first two successors are `c` and `t`.

Hence in either case

`v -> t`.                                                     (2)

After this `d`-pivot, the support has the local directed segment

`d -> v -> ...`.

Now `x` is the sink at the next same-support guard break. If `e=d`, then `v` is the first successor of `e`; if `e=d^-`, then `v` is the second successor of `e`. Tightness therefore gives

`x -> v`.                                                     (3)

The arcs (1)--(3) are all arcs of the original digraph, so they form the genuine directed triangle `t->x->v->t`. QED.

### Minimum-packing consequence

Let the light support have order `m`. The triangle `T` is disjoint from the other two packed cycles. Replacing this light support by `T` produces a legal three-cycle packing of total order

`(n-3) - m + 3 = n-m`.

The global minimum has order `n-4`, so `m<=4`. If `m=4`, the new packing has exact order `n-4`; its four-vertex complement is either cyclic, giving the fourth directed cycle, or is precisely the existing exact-R4 restart. In the inherited oriented normal form packed cycles have order at least three. Therefore every genuinely surviving no-R4 branch of the two-generation guard-break configuration has

`m=3`.

So a nontriangular light support cannot absorb an old hole and then immediately process the new guard generation on that same support.

## 6. New structural split — mixed long-support orbits are strict alternating zippers

Assume now both light supports `A,B` have order at least four, and exclude SIX, cyclic remainder/four-pack, exact-R4 compression, and a strict smaller three-packing.

Suppose two consecutive tight pivots use different light supports, first `A` then `B`. Let the fresh holes be `h_A,h_B`. Both are guarded, so in the resulting three-vertex acyclic remainder the third retained vertex is the **unique possible sink**.

The next pivot must use `A` or `B`; assume it uses `A`. Let its fresh hole be `h_A'`. Immediately afterwards:

- `h_B` is still guarded because `B` was not changed;
- `h_A'` is freshly guarded;
- a finite acyclic remainder must have a sink.

Thus `h_A` must be that sink. By the guard-breaking rule, the just-completed `A` pivot was forced to occur at the previous `A` return port or its predecessor.

Now the sink is `h_A`. If the next pivot also uses `A`, then after that pivot `h_B` and the newest hole are guarded, so the older hole `h_A'` must become a sink. Hence this second consecutive `A` pivot must break the preceding `A` guard. Section 5 applies and forces `A` to be a triangle (or one of the excluded exits).

Therefore, **if both light supports remain long**, the next pivot must use `B`. The same argument then forces that `B` pivot to occur at the previous `B` return port or its predecessor. Inductively:

> **Alternating guard zipper.** Once a surviving long-support orbit has used both light supports, every subsequent tight pivot alternates strictly
>
> `A,B,A,B,A,B,...`,
>
> and on each revisit to a support its pivot port is either the previous pivot port on that support or that port's current predecessor.

Any violation by repeating the same support forces that repeated support to be triangular (or exits to SIX/cyclic remainder/exact R4/packing improvement).

Thus the mixed part of the old `MONO/TRI` leaf is no longer an unrestricted finite pivot orbit. It is a rank-one local zipper on each directed support.

## 7. Three-lane hole ladder forced by the zipper

The zipper has an additional invariant that is useful for the next recipient.

Index mature alternating pivots by `P_i`, and let `h_i` be the fresh hole freed by `P_i`. After the first three pivots of the zipper, the residual set after `P_i` is

`{h_{i-2}, h_{i-1}, h_i}`.

Because `P_i` breaks the guard from the same-support pivot `P_{i-2}`, the hole `h_{i-2}` becomes the unique sink after `P_i` and is therefore the sink inserted by `P_{i+1}`. Equivalently, for every mature index,

`sink(P_i) = h_{i-3}`.

A tight pivot sink hits the first successor that it frees. Therefore the original digraph contains the directed arc

`h_{i-3} -> h_i`,

or, after reindexing,

`h_j -> h_{j+3}`                                               (4)

throughout the mature zipper.

Hence the holes form three directed lanes modulo three. Immediate sanity consequences are source-valid: `h_j=h_{j+3}` is impossible because it would demand a loop, and `h_j=h_{j+6}` is impossible in the oriented normal form because (4) would create a digon. A later same-lane recurrence of larger period produces a genuine directed hole-cycle in the original graph; I do **not** claim that such a cycle is automatically disjoint from the current three-packing or already proves BT4.

## 8. Exact sanity checker

A dependency-free checker was saved beside this report. It enumerates the four local choices

`d in {c,c^-}`, `e in {d,d^-}`

on a support of order four and verifies that the forced tight-pivot arcs always contain

`t->x`, `x->v`, `v->t`.

Saved files:

- `checker.py`, creation commit `fcc42759ac3a1892b5dc6c3fe560d4ee297bf87c`;
- `checker_output.txt`, creation commit `7077801c844d4ce4975f216c6082a90deaa57179`.

Output:

```text
cases= 4
(0, 0, 'c', 'c', 't', 'v', True)
(0, 1, 'c', 'z', 't', 'c', True)
(1, 0, 'z', 'z', 'c', 'v', True)
(1, 1, 'z', 'y', 'c', 'z', True)
all_guard_break_cases_force_triangle=t->x->v->t
```

The checker is only a local sanity check; the proof above is uniform and does not rely on finite computation.

## 9. Interaction with the port-order obstruction

The account03/B05 theorem `BT4-MONOTONE-QUADRANT-RANK-WALL-v1` prevents an invalid shortcut here. Even in the alternating zipper, another clean reverse connector does not by itself yield two disjoint mixed cycles if both support orders remain in the same monotone quadrant. Its positive criterion requires an order inversion and a matched-gap reverse endpoint.

The zipper now supplies exactly the extra structure absent from the generic rank wall: every same-support port changes by at most one predecessor step per visit, and the three-lane hole arcs (4) record the token transport across visits. Thus the next proof should force one of two things:

1. a cyclic-order inversion/matched-gap connector, enabling the source-valid two-cycle splice; or
2. a recognized exit: connector collision, third-support mediation, same-support bypass, triangular/short support, SIX, cyclic remainder, exact R4, or strict packing decrease.

It would be incorrect to relabel another clean path as closure.

## 10. Structural case split after this run

For the residual-three F3 defect-one orbit, outside already recognized exits, the exact remaining alternatives are now:

1. **MONO:** after some point every tight pivot uses one light support. This still needs a one-support token/guard classification.
2. **TRI:** a light support is a directed triangle; use the bounded triangular cyclic-order and CROSS/BYPASS machinery.
3. **ZIP:** both light supports remain long and the orbit is the strict alternating guard zipper of Sections 6--7: each support's port stays fixed or moves one predecessor on every revisit, and mature holes satisfy `h_j->h_{j+3}`.

The previous mixed-support finite-orbit debt has therefore been replaced by a much narrower deterministic local geometry.

## 11. First exact unpaid implication

`BT4-F3-R3-MONO-OR-ZIP-INVERSION-v1`:

> In the residual-three F3 defect-one NO-SIX/no-R4 normal form, prove that either the MONO branch reaches a triangular/short support, cyclic remainder, strict packing reduction, exact R4, SIX, or a source-valid connector splice; or, in the ZIP branch, the predecessor-step port evolution plus the three-lane hole arcs force an inverted two-support port pair with a reverse endpoint in the matched gaps, or one of the same recognized exits.

This statement is deliberately not replaced by the unsupported claim that higher connector rank alone closes the branch.

## 12. Failure checks and honest boundary

- BT4 is **not** proved.
- The partner's newest advertised canonical file was unavailable; its needed guard facts were re-derived here rather than silently trusted.
- A clean CROSS, BYPASS, lane cycle, or rank increment is not counted as a fourth cycle.
- The exact-R4 equality branch remains an explicit restart, not a contradiction.
- The MONO branch is still unpaid.
- SIX, the lead's four-port coalescence, other bounded F2/F3 states, and the seven-remainder branch remain separate global debts.
- No reversed-arc cycle from the 2026 relaxation is counted as a target cycle.

**Outcome: `ESSENTIAL_STEP_APPLIED`.** The mixed long-support residual-three F3 pivot orbit is no longer an arbitrary finite choreography: unless it triangularizes a support or hits a recognized exit, it is a strict alternating predecessor-step zipper carrying the directed three-lane invariant `h_j->h_{j+3}`. This is the structural case split to hand to the splice/inversion workers next.
