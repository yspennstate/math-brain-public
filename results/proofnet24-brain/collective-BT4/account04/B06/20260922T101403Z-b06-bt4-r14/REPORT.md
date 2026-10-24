# BT4 B06 attempt — two-defect necessity for the primitive-trace wall

Outcome: `CANDIDATE_REFUTED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Run: `20260922T101403Z-b06-bt4-r14`

## 1. Scope and source-bound inputs

Target: the exact `k=4` Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered vertex pair and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles; digons are allowed and all finite orders are included.

Fresh owner control remains revision `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; new brain-installation and benchmark work is superseded for B06.

Public theorem boundary checked this run: Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948, 13 Aug 2026, explicitly states that the original conjecture remains unresolved for every `k>=4`; their theorem allows one reversed arc and therefore is not BT4.

Exact repository mathematics consumed:

1. **Team lead account02/B04**, run `account02-B04-20260922T094740Z-bt4-r11`, theorem `BT4-PRIMITIVE-TRACE-MIXED-PACKING-ONE-v1`, report blob `b768e00ab1e7f22e0cfd56d6f95ffbc36b3a1c60`. Its reverse-gap/TRACE-ORDER argument proves that a primitive domination trace supports no two vertex-disjoint trace-respecting mixed cycles, even with trace-parallel connector detours. It leaves `BT4-OFF-TRACE-OR-EXIT-v1` as the first local obligation.

2. **Assigned partner account01/B04**, run `20260922T0744Z-b04-bt4-r11`, candidate `BT4-DOMINATION-TORUS-CYCLE-v1`, shared handoff blob `cb129c6d88e9d77cf4ca1d2ee483da53a6031236`. It forces a predecessor-closed mixed torus staircase of direct `A<->B` cross states in the long-support residual, but leaves the block splice unpaid.

3. **OTHER-account account03/B05**, result `BT4-FRESH-PORT-OR-C-WALL`, report blob `060eddbca21de4d78c8059e71398a7d1833d9f64`. In the clean heavy-triangle state, deleting the endpoints of a direct reverse cross produces either a fresh remainder-internal reverse connector or an explicit path through the third packed support `C`.

The lead result is applied, not merely cited: the proof below extracts a stronger hitting consequence from its reverse-gap lemma and uses it to test the lead's first unpaid implication.

## 2. Compact conditional end-to-end state

The inherited exact-seven, arc-dominated, 3-vertex-strong globally minimum three-cycle-packing programme reduces the target to recognized interfaces. The lead currently isolates four global debts: `SIX`, bounded `F2/F3`, the seven-remainder pinwheel/support-carried case, and the clean heavy-triangle coalescence case.

For the last case, account01/B04 forces the monotone primitive torus trace, account03/B05 forces a fresh reverse connector or third-support mediation, and account02/B04 proves that all switches staying on the primitive trace have mixed packing number one.

The lead's first local obligation was phrased as forcing an order-breaking off-trace connector or a recognized exit. This run tests the strongest possible one-connector version of that idea. It is false: **one off-trace support switch can never suffice while all other support switches remain trace states.** The correct local obligation needs at least two effective off-trace switches, or a recognized non-two-support exit.

## 3. Definitions

Let `A=(a_i)` and `B=(b_j)` be the two directed support cycles of a primitive trace word `w`. A signed trace occurrence authorizes either an `A->B` endpoint pair (`+`) or a `B->A` endpoint pair (`-`) as in the lead's primitive-trace model.

For any directed cycle `Z` avoiding the third support `C`, decompose every excursion between `A` and `B` into a **support-switching segment**: a maximal directed subpath whose endpoints lie one on `A` and one on `B` and whose internal vertices avoid `A union B`.

A support-switching segment is **trace** if its direction and ordered endpoint pair equal a signed primitive-trace state. Its interior may be an arbitrary trace-parallel detour. It is a **defect** if its signed endpoint pair is not a state of the primitive trace.

A two-support mixed cycle is **trace-respecting** if all its support-switching segments are trace segments and on `A,B` it follows positive support direction. Same-support bypasses and visits to `C` are deliberately excluded: they are already recognized exits from the primitive-trace obstruction.

## 4. New trace-hitting lemma

**Lemma (`TRACE-HITTING`).** Let `Z` be a trace-respecting simple mixed cycle. Every signed trace occurrence has at least one of its two support endpoints on `Z`. Consequently every trace-parallel support-switching segment meets `Z` at a support endpoint.

**Proof.** Use the lead's `TRACE-ORDER` theorem. The trace occurrences selected by `Z`, in their cyclic reverse-word order, partition the primitive word into gaps between successive selected occurrences.

If a trace occurrence `u` is selected, its connector endpoint is already on `Z`. Otherwise `u` lies strictly inside one such gap from selected state `s` to selected state `t`. Successive support-switching signs on `Z` alternate.

If the gap has signs `+,-`, the lead's reverse-gap lemma says that the `B`-coordinate of every occurrence strictly inside the reverse gap lies on the positive `B` support segment used by `Z` from the `+` connector to the `-` connector. Hence the `B` endpoint of the trace occurrence `u` lies on `Z`.

If the gap has signs `-,+`, the same reverse-gap lemma on `A` puts the `A` endpoint of `u` on the positive `A` support segment used by `Z`.

Thus every signed trace state has a support endpoint on `Z`. A trace-parallel connector with that endpoint pair therefore intersects `Z` at that endpoint. QED.

This is strictly stronger than the statement "two trace-respecting cycles cannot be disjoint": it says a fixed trace-respecting mixed cycle hits **every** trace connector state.

## 5. New theorem — two defects are necessary

**Theorem (`BT4-PRIMITIVE-TRACE-TWO-DEFECT-NECESSITY-v1`).** Suppose `Z_1,Z_2` are vertex-disjoint directed cycles, each meeting both `A` and `B`, neither visiting the third packed support, and each decomposed into positive support segments plus support-switching segments as above. Then the union `Z_1 union Z_2` contains at least **two defect support-switching segments**.

Equivalently: augmenting the primitive trace by at most one arbitrary off-trace support switch can never create two vertex-disjoint mixed directed cycles if every other switch remains trace-parallel.

**Proof.** Suppose instead that the two cycles contain at most one defect in total. Then one of them, say `Z_1`, contains no defect and is trace-respecting.

Because `Z_2` is mixed, it must switch between `A` and `B` at least twice. With at most one defect available in the entire pair, `Z_2` therefore contains at least one trace support-switching segment. By `TRACE-HITTING`, that trace segment has a support endpoint on `Z_1`. Hence `Z_1` and `Z_2` share a vertex, contradicting their assumed vertex-disjointness. QED.

No parity or canonical-two-splice assumption is used. A mixed cycle may have arbitrarily many alternating support switches. The result is therefore compatible with the lead's explicit counterexample showing that a vertex-minimal mixed cycle can have four cross edges.

## 6. Sharpness — two defects really can suffice

The lower bound two cannot be raised on primitive-trace information alone, even when both defects have the **same direction**.

Take `m=n=2` and primitive word

`w = +-+-`.

Using the lead's exact state recurrence, the signed states are

- `+(0,0)`: `A0 -> B0`,
- `-(0,1)`: `B1 -> A0`,
- `+(1,1)`: `A1 -> B1`,
- `-(1,0)`: `B0 -> A1`.

Add exactly the two off-trace forward arcs

`A0 -> B1` and `A1 -> B0`.

Then

`A0 -> B1 -> A0`

and

`A1 -> B0 -> A1`

are vertex-disjoint directed digons. Each uses one defect forward arc and one old trace reverse arc. Digons are allowed in the BT4 target. Thus two defects are best possible as a purely trace-combinatorial threshold.

## 7. Application to the cross-account candidate

### Partner account01/B04

`BT4-DOMINATION-TORUS-CYCLE-v1` forces a long predecessor-closed staircase of **trace** cross states. The lead subsequently proves that no amount of pure trace-parallel routing yields two disjoint mixed cycles. The theorem above goes one step further: even adding a single order-breaking cross to that staircase cannot close the two-cycle replacement while all remaining switches stay trace-parallel.

Therefore `BT4-TORUS-BLOCK-SPLICE-v1` cannot be discharged by finding only one exceptional block-boundary cross. Two effective defects, or a recognized exit, are necessary.

### account03/B05

`BT4-FRESH-PORT-OR-C-WALL` supplies, after deleting the endpoints of one direct reverse cross, either:

1. a path through `C`, which is already a recognized third-support exit; or
2. a fresh remainder-internal `B->A` connector.

In case (2), if the fresh connector's endpoint pair is a primitive trace state, it contributes no defect. If its endpoint pair is off-trace, it contributes exactly one defect. **Neither possibility alone can yield the desired two mixed replacement cycles** in the otherwise trace-parallel branch. A second effective defect (or a same-support bypass, `C`-mediation, exchanged-remainder cycle, strict packing decrease, `SIX`, or the fourth disjoint cycle) is still required.

This is the first essential correction to the current end-to-end candidate.

## 8. Decisive finite audit

A checker derived from the lead's exact state recurrence exhaustively tested every normalized primitive word with `2<=m,n<=5`, then added every single signed off-trace direct cross arc and enumerated all simple mixed cycles. It tested `12,238` one-defect augmentations and found `0` with two vertex-disjoint mixed cycles.

The same checker verifies the sharp `+-+-` two-defect witness above.

This computation is an audit only; the arbitrary-order theorem is proved analytically in Sections 4--5. Exact code and output are committed beside this report as `one_defect_check.py` and `one_defect_output.txt`.

## 9. First unpaid implication after this run

The prior lead obligation `BT4-OFF-TRACE-OR-EXIT-v1` is too weak if interpreted as a single off-trace connector. The source-valid replacement is:

**`BT4-TWO-DEFECT-OR-EXIT-v1`.** In the exact clean heavy-triangle/primitive-trace coalescence state, use minimum outdegree seven, arc domination, acyclic remainder, 3-vertex-strongness, and minimum-packing inequalities to force either

- at least two effective off-trace support-switching segments with geometry that yields two vertex-disjoint replacement cycles; or
- a same-support bypass; or
- third-support mediation through `C`; or
- a directed cycle in the exchanged remainder / strict lexicographically smaller three-packing; or
- a `SIX` exit; or
- directly a fourth vertex-disjoint directed cycle.

The theorem here does **not** prove that two arbitrary defects automatically splice; the sharp witness only shows that two is the minimum possible number. Endpoint order/disjointness remains to be paid.

The separate global debts `SIX`, bounded `F2/F3`, and seven-remainder pinwheel/support-carried states remain open. BT4 is not proved.

## 10. Status

`CANDIDATE_REFUTED`.

The refuted candidate is the one-defect version of the lead's off-trace closure: one order-breaking `A<->B` connector plus an otherwise primitive trace cannot produce two vertex-disjoint mixed cycles. The surviving route is strictly sharper: force two effective defects or leave the two-support primitive-trace mechanism through one of the already recognized exits.

Scoped privacy/secret review: manual PASS for this report and companion checker/output; no credentials, scheduler identifiers, machine paths, unrelated private material, benchmark gold, email, or Drive content are present.
