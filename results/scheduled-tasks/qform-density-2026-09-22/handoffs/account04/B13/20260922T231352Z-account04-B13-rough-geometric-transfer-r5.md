SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B13, 2026-09-22T23:13:52Z.
attacking: rough-law transfer of geometric estimates without an attained bathtub maximizer, followed by the two-sheet slab interface.

# account04/B13 handoff

Status: PROVED SUPPORTING TARGET-LEVEL RESULTS / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN.

Canonical mathematics: yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1, path proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md, blob 63f4e0656fe110e0596254283be8e8e1e8b82ac6.

New results:

1. Repaired the infinite-line bathtub issue. No maximizer or global threshold set is required. Every cap-one mass-one density is an L1 limit of finite convex combinations of indicators of bounded finite interval unions of measure one. Hence for every bounded measurable product kernel K,
\[
\sup_{f_i}\int K\prod_i f_i
=
\sup_{|E_i|=1}\int_{\prod_iE_i}K,
\]
with the right supremum unchanged if the \(E_i\) are bounded finite interval unions. Fragment count and diameter remain unbounded.

2. Applied the repair to Claude's ruled theorem. For arbitrary rough cap-one product inputs and
\[
Q=\lambda_1\langle r_1,X\rangle^2+\lambda_2\langle r_2,X\rangle^2-\mu\langle r_3,X\rangle^2,
\quad \lambda_1,\lambda_2,\mu\ge1,
\]
every interval \(J\subset[0,\infty)\) satisfies
\[
\Pr(Q\in J)\le C(\lambda_1,\lambda_2,\mu)|J|\le\pi\sqrt2\,|J|.
\]
Proof: purify to bounded finite-union indicators, Gaussian-mollify each factor (cap remains one), use the smooth ruled estimate, and pass by product total variation. This is the majority-sign one-sheet half-line, not the two-sheet or full theorem.

3. Applied completed account01/B13 mathematics at an actual inequality. Its exact-graph/null-pivot product-set bound transfers without loss:
\[
\Pr(X^TAX\in J)<335.063|J|,
\qquad
\|p_{X^TAX}\|_\infty\le335.063
\]
under precisely the partner theorem's branch hypotheses.

First unpaid geometric implication: for \(q(y)=y_1^2+y_2^2-y_3^2\), prove uniformly for product unit sets
\[
|\{x\in\prod_iE_i:-a^2-\delta\le q(R^Tx)\le-a^2\}|\le C\delta.
\]
The exact two-sheet coarea trace is curved and has no ruling. Bounded projected density or X-ray norm alone is insufficient; radial truncation gives only \(2\pi M R_0\delta\) and no tail control without forbidden moment assumptions.

Sources consumed: Claude package math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837; completed account01/B13 math-open-problems@680ff828e47704689fde0ca4b1690860a9cbd71f and brain handoff@02f399acc9a279664063574cd2a7a6e088a428f4; bang-bang source math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94. Owner control revision remains 2026-09-22.15.
