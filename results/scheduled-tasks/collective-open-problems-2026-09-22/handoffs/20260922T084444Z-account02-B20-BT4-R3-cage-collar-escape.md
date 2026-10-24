# BT4 shared handoff — account02/B20 r18

Source run: `20260922T084444Z-account02-B20-bt4-r18`  
Canonical report: `proofnet24/collective-BT4/account02/B20/20260922T084444Z-account02-B20-bt4-r18/report.md`  
Classification: **ESSENTIAL_STEP_APPLIED**; BT4 remains open.

## Inputs actually consumed

- account02/B04 latest complete candidate: `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, report commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`.
- named other-account partner account04/B06: `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`, report commit `3e7343cfd9de439c2e6ae8c39e71ddcbc956cde9`, handoff blob `47d7e7c2fd312fd647604bf61113c46fd980a237`.
- account02/B20 r17: `BT4-TORUS-FOURBLOCK-FAN-CAGE-v1`, report blob `f10128d630f2b6596f6d45c5ef1bb7b787d8ece2`.

A newer B04 torus-order checker was inspected but had no complete report at the snapshot; it was not promoted over the latest complete lead.

## New reusable lemma: `BT4-R3-CAGE-COLLAR-ESCAPE-v1`

Let `(A,B,C)` be the inherited globally minimum-total-order three-cycle packing with acyclic remainder `R`, and let `S` be one packed support. If `z in R` has arcs to two distinct vertices `x,y in S`, then any inport `s->z` from `S` forces

`{x,y}={s^+,s^{++}}`.

Proof: for each `t in {x,y}`, `s->z->t->S[t,s]` is a genuine directed replacement cycle disjoint from the other two packed cycles, so minimum packed order gives `d_S(t,s)+2>=|S|`. The two distinct distances must be `|S|-2,|S|-1`.

Hence nonconsecutive `x,y` imply `S->z` is empty. In the inherited arc-dominated branch, dominate `z->x` repeatedly along the arcs into `z`. A predecessor chain cannot repeat inside acyclic `R`; it must leave `R`, cannot leave through `S`, and therefore yields a genuine directed transition from another packed support `T!=S` through `R` to `x`.

## Exact four-block consequence

In the r17 hub cage

`K0=a0->b0->a1->b1->a0`,

an external remainder vertex hitting at least three hubs hits both hubs of one support. The two B-hub gaps are the two plus-block lengths; the two A-hub gaps are the two minus-block lengths. Therefore

`R 3-of-4 witness -> UNIT_BLOCK or packed-to-packed CROSS_TRANSITION`.

If neither relevant torus block has length one, the paired hubs are nonconsecutive and the domination escape applies.

## First unpaid interface

`BT4-TORUS-UNIT-BLOCK-CROSS-SPLICE-v1`:
close the unit-gap cage or pair the forced cross transition with the existing reciprocal/rank-two connector data into a legal strict/neutral descent, a cyclic exchanged remainder, SIX/H5, or four vertex-disjoint genuine directed cycles.

Suggested next attack: for a unit block, treat the adjacent hub pair as a fixed length-two bypass target; for the cross branch, classify the first intersection of the domination ladder with the partner's opposite rank-two connector family. Intersection should create a same-support bypass; disjointness should create the two-splice candidate.

No full BT4 proof is claimed.
