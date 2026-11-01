# Independent analytic review: physical phase budget and variance refund

**Reviewed by:** Path A researcher, 2026-09-22 UTC.  
**Target:** `../interference/REPORT.md`, including the final variance-conservation Theorem 6.  
**Result:** **PASS for the stated mathematical scope; no substantive blocker found.**

I read the complete report and independently rederived the packet phase formula, strong-concavity constant, local phase refund, and adaptive-tree cancellations while building the occurrence-credit theorem in Path A. The conclusions apply to actual uniform physical coordinate restrictions and finite adaptive stopping trees. They do not establish the remaining universal packet-entropy payment or full FEI.

## Analytic checks

The packet equality `JS = sum e_T j(q_T)` is correct: the squared child-amplitude ratio and its complement are exactly the two values encoded by `1/2 + sqrt(q_T(1-q_T))`. Thus signs are retained in the selector posterior, and the empty residual packet is included.

For `z=2sqrt(t(1-t))`, the derivative formula

`j''(t) = -4(atanh(z)-z)/((ln 2) z^3)`

is correct. Its power series proves the uniform bound `j'' <= -4/(3 ln 2)`. The first derivative joins continuously at the central point although the second derivative diverges there. The global strong-concavity inequality and both stated refund constants follow. In particular the influence-pair variance is `(a_i-b_i)^2/4`, yielding the coefficient `1/(6 ln 2)` after the strong-concavity factor.

All adaptive-tree identities use genuine node reach probabilities and query only remaining original coordinates. Every nonroot internal term cancels against its parent contribution. This validates arbitrary stopping leaves as well as complete trees. Concavity of `min(t,1-t)` supplies the folded influence budget without a hidden character change at successive nodes.

The new variance conservation is also exact. For `w(t)=t(1-t)`, the local influence-variance drift is

`d(1-d) + sum_{i != r}(a_i-b_i)^2/4`.

The Bernoulli total-variance identity splits its first term into `E_packet[q(1-q)] + Var_packet(q)`. Summing proves the report's `W(root)-E W(leaves)=A_T+V_T+M_T/4`. Since `w(t)<=min(t,1-t)`, the resulting one-root budget is valid. This does not bound a raw sum of all coordinate-pair curvatures at the root, and the report correctly keeps that distinction.

The final branch-closing criterion is a sufficient conditional implication. Subtracting the exact phase drift from entropy gives `F(root)=E F(leaves)+L_T-B_T`; the stated packet payment and leaf inequality then imply the advertised influence bound. The report correctly leaves the universality of that payment unproved. In particular quadratic variance alone is not asserted to control the rare-event logarithm.

## Independent finite checks

Path A's separate integer-Walsh checker reconstructs the same actual physical spectra and tests the local phase refund and complete adaptive phase budgets together with the new occurrence-credit identities. Its completed run checked 25,874 local selector instances and 1,195 adaptive trees on 1,307 functions. The largest identity discrepancy was 1.78e-15, and every tested quantitative phase refund was nonnegative within tolerance. These figures come from `../path_a/CHECK_RESULTS.json`; they are separate from the companion report's own checker. The additional variance-conservation theorem was reviewed analytically above and is not represented as a separate numerical test in the Path A checker.

## Scope of the review

The existing phase function and general restriction framework are not asserted to be new. I did not perform an independent literature priority audit, verify all external source claims, or formalize the proofs in a proof assistant. This review supports the stated intermediate theorems and the cross-path occurrence-credit supermartingale, with full FEI remaining open.
