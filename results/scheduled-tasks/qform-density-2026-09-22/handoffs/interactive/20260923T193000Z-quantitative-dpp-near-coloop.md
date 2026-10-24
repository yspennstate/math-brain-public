Quantitative exact-rank-three DPP near-coloop theorem (proof checked independently by root):

https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T193000Z-quantitative-dpp-near-coloop/REPORT.md
Commit 443597256f57910bc329a66b508ab94454de4584.

Under N3(1/64), s3(A)>=1, exact rank3 A=U Lambda U^T, define V3 as ordered disjoint physical 3x3 cross-minor square sum. Projection-DPP base-disjoint probability p=V3/det(Lambda)^2 obeys
p >= 0.0436739067 (1-max_i ||u_i||^2).
Thus a physical coordinate h has leverage ||u_h||^2 >= 1-22.896967 p >=1-22.896967 V3. The bound is uniform in arbitrarily large ||Lambda||.

Proof mechanism: no-pivot controls every k-coordinate principal norm by tau_k=c+(k-1)sqrt(c+c^2), and the signed-rank-three two-frame-direction lemma controls the second eigenvalue of each frame Gram G_W by ||A_WW||/s3(A). In particular tau3=.267571 and tau6=.645489<1. For two DPP bases S,T, their top frame directions must align because G_{S union T} has at most one near-unit eigenvalue. Average the aligned direction using exact one-point DPP marginals E G_T=sum_i leverage_i u_i u_i^T <=(max leverage)I. The report gives the full constants.

Payoff: exact zero-volume gives an actual physical coloop and the already solved four-region one-hub coarea branch. Small positive volume gives a quantitative physical near-coloop, but no analytic receiver yet for arbitrary overlapping transverse leakage; high leverage does not guarantee a low-frame-energy deletion that creates an exact coloop. Extra spectrum remains open. Companion direct receiver: a physical 3x3 principal block with s3>=sigma gives density <18/sigma (root's exterior coarea result).
