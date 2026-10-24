# POS3 account04/B11 source-bound handoff

Parent POS3 status: **OPEN / NOT PROVED**.  Run outcome: **ESSENTIAL_STEP_APPLIED**.

Main report: `proofnet24/collective-POS3/account04/B11/20260922T071403Z-B11-pos3-r17/REPORT.md`, commit `d6c62e8f596a7138756a51d76f63fea08143b308`, blob `bd9d3d0ae19ddc6d4d11a341665c6082ed5976ad`.

Latest lead consumed: account04/B10 r17, `proofnet24/collective-POS3/account04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, commit `732a848a9fa315f3907c654f0c54591dfe04535d`.

Assigned partner consumed: account01/B19 r13, `proofnet24/collective-POS3/account01/B19/20260922T054717Z-b19-pos3-r13/REPORT.md`, blob `19f1baa7b3bbe4ed45e19df6ca396f97f6fa5131`.

Compatible coherent-gate export consumed: account03/B19 `proofnet24/collective-POS3/account03/B19/20260922T070336Z-b19-pos3-r11-same-ray-export/REPORT.md`.

New exact statements:

1. In any hypothetical counterexample, every actual pair of minority at least `3/11` has strong-majority index distance at most `2790`.
2. Every actual pair of minority at least `2/33` has strong-majority index distance at most `5920`.
3. Hence every account01/B19 r13 exact-two selector pair is a `<=2790` jump, and both lead r17 outward heavy-cover packet pairs are `<=5920` jumps.
4. The unresolved coherent three-antichain gate lies in a strong-order window of at most `5921` positions.
5. In the exceptional range `7<=pi(P)<=K_3`, the graph of incomparable pairs with minority at least `2/33` has maximum degree at most `K_3` and strong-order bandwidth at most `5920`; a fixed anchor cannot generate an unlimited supply of new weighted channels.

First unpaid implication: **DISTINGUISHER-TO-PACKET EXIT**.  Account03/B19 forces external relation distinguishers at the coherent gate, but no current theorem gives those static witnesses a positive uniform fraction of full-extension mass.  Prove that one such witness either produces an authorized terminal/opposite-ray exit or carries a quantitatively positive actual pair packet.  Do not promote a relation distinguisher to a weighted packet without this missing count transfer.

Failure preserved: bounded range/variance does not imply a finite kernel; B11 r12 gives arbitrary-size `pi=7` examples.  The new packet graph is bounded-degree/bounded-bandwidth, not finite-size.
