# fleet03/B10 POS3 handoff — strict-corridor actual-uniform conditioning

Run: `20260922T031643Z-a03-b10-pos3-r11`  
Status: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains **OPEN / NOT PROVED**.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Exact source-bound inputs

- Assigned partner fleet04/B11: `proofnet24/collective-POS3/fleet04/B11/20260922T024830Z-B11-pos3-r13/REPORT.md`, blob `bcf691d042edddf8d0a3600d97684d3bb4eeade2`. Applied: bounded-range local-state result (`K=pi(P)`, block lengths `K,2K,K`, at most `1+2K` exact renewal components, no finite-kernel shortcut).
- Campaign lead fleet04/B10: `proofnet24/collective-POS3/fleet04/B10/20260922T031005Z-B10-POS3-r11/REPORT.md`, blob `fb5b7e5f9b8e596f4b6bafff4d56164094336361`. Applied: first-fork sibling predecessor sets are nested and their proper difference is a delayed chain; equal-predecessor deletion-channel identity is available.
- Prior fleet03/B10 variance report: blob `3e50b4d0adaa18c79a96079139d660b832418a2d`. Applied only to retain the honest source-parametric exceptional bound `K<K_AK(1,6560)^2`.

## New exact result

Let `P` be a hypothetical no-balanced width-three candidate, let `a||b` satisfy `Pred(b) proper_subset Pred(a)`, and suppose `D=Pred(a)\Pred(b)` is the delayed chain supplied by the first-fork theorem. In the branch where the larger-predecessor sibling is majority-early, `a prec_* b`, put `d=max D`,

`p=Pr_P(a<b)>2/3`, `gamma=Pr_P(d<b)>2/3`.

Then conditioning on the actual relation of the incomparable pair `d,b` gives the exact uniform-law decomposition

`Law(P)=gamma Law(P+(d<b))+(1-gamma) Law(P+(b<d))`.

In `P^+=P+(d<b)`, the whole corridor is collapsed at once:

`Pred_{P^+}(a)=Pred_{P^+}(b)=Pred_P(a)`.

In `P^-=P+(b<d)`, transitivity gives `b<d<a`, so the event `a<b` is impossible. Consequently

`p=gamma p^+`, where `p^+=Pr_{P^+}(a<b)>2/(3gamma)>2/3`.

Apply the exact equal-predecessor channel identity in the genuine uniform law on `P^+`. If `Z` is the positive first-successor blocker set, width three gives `1<=|Z|<=2`. Every positive blocker `z` is also a genuine original-poset successor of `a`, remains incomparable with `b`, and the event `z<b` is impossible in `P^-`; hence

`Pr_P(z<b)=gamma Pr_{P^+}(z<b)`.

If there is one positive blocker, the channel identity forces `Pr_P(z<b)>1/3`; no-balancedness then forces `>2/3`, giving strict strong-majority span descent `a prec_* z prec_* b`.

If no span descent occurs, there must be exactly two positive blockers. They satisfy the sharp necessary window

`2/3 < p < 1/3 + gamma/2`,

or equivalently `gamma>2p-2/3`. In endpoint variables of the equal-predecessor child,

`1 - 2/(3gamma) < (Q^+ + R^+)/e(P^+) < 2 - 4/(3gamma)`.

At the inherited first fork, the two-blocker no-descent residue again creates a width-saturating second fork; since the old endpoint `y` is incomparable with `b`, width three forces `y<z_i` for at least one new blocker.

Thus the strict lower-distinguisher, larger-predecessor-majority-early branch now reaches the same span-descent / second-fork mechanism as the equal-predecessor branch, with an extra quantitative conditioning squeeze.

## First remaining step

The strict corridor where the larger-predecessor sibling is **majority-late** remains unpaid. A useful next move is: if some `d in D` lies between the two siblings in the strong-majority order, use `(b,d)` for immediate span descent; otherwise all of `D` lies before both siblings and the same top-corridor conditioning gives an equal-predecessor `P^+`, but the conditioned sibling bias is only known to be `>1/2` in the majority-late direction. Derive enough channel mass from the lead's majority-late endpoint polarity to recover a two-blocker contradiction or a shorter span.

Canonical scientific report: `proofnet24/collective-POS3/fleet03/B10/20260922T031643Z-a03-b10-pos3-r11/REPORT.md`, scientific commit `114518e3e96cdf1eb609ac8e5ade4a1b27094b08`, report blob `e39ea9f7c820637f16470822d2979f2bbe494e0c`.

No induced law was replaced by a uniform surrogate. No finite-kernel claim, benchmark material, FEI material, credentials, scheduler mutation, email/Drive/public workflow, paid model/API/Codex execution, or production-brain mutation was used.
