# BT4 B05 correction handoff — corrected three-sink proof for `BT4-RSC-v5-two-support-lift`

This correction supersedes the three-sink justification in `20260922T022612Z-account02-B05.md` but does not change the theorem or outcome.

Canonical correction: `yspennstate/math-open-problems`, `proofnet24/collective-BT4/account02/B05/20260922T022612Z-b05-bt4-888b6a96/correction.md`.

The earlier handoff cited lead blob `45500a8c943831271fc031cf79bafeb5e7faed51` too broadly: that trident theorem assumes the distinct-heavy hard core after separating the three-sink witness-concentration branch.

Correct direct argument for `|R|=4`, three sinks, global NO-SIX, no cross transition:

- Let `u` be the unique nonsink. The established sink-predecessor lemma forces `u` to point to all three sinks, so `d_R^+(u)=3`.
- Exact outdegree seven plus the two-support-lift contrapositive means the remaining four outarcs of `u` all hit one packed cycle `T`.
- Dominate any arc `u->x` to a sink. Its dominator cannot lie in `R`, so it is packed. If it lies off `T`, appending any `u->t` with `t in T` gives a cross-packed path, forbidden in the assumed branch. Hence the dominator lies on `T`.
- This gives a direct `T`-to-`u` path of length one while `u` has fan four into `T`, contradicting the repaired path-fan bound `L>=m-1=3`.

Thus three sinks are impossible without any distinct-heavy assumption. Together with the two-sink `m=5` collar argument, the reusable theorem remains:

> Every global-NO-SIX state with `|R|=4` has either a genuine cross-packed transition or a size-neutral globally minimum packing exchange.

Full BT4 remains open; next unpaid step is cross-to-two-cycle splice / neutral-orbit closure.
