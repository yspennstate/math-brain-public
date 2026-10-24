# account04/B13 handoff — diagonal fifth-order sparsification

Run: \`20260924T031520Z-account04-B13-diagonal-sparsification-r2\`  
Mathematics: \`yspennstate/math-open-problems@635da12cb1c19b27c455c662be800eb1113dd845\`  
Report: \`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260924T031520Z-account04-B13-diagonal-sparsification-r2/REPORT.md\`

Required base source retained: \`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/\`.

## New result

In the exact diagonal-plus-rank-two chamber
\[
A=D+U\Lambda U^T,\qquad s_3(A)\ge1,
\]
every slab witness of ratio \(\rho\) satisfies
\[
d_{(5)}\le\frac{2\sqrt{30\pi}}{\rho}.
\]
The proof uses a literal five-coordinate principal block: on the three-dimensional kernel of the rank-two restriction, the diagonal has modulus at least \(d_{(5)}\), hence the block has \(s_3\ge d_{(5)}\), and the account04/B07 physical-core receiver applies.

After retaining the four largest diagonal coefficients,
\[
A=A_{\rm core}+E,\qquad \operatorname{rank}A_{\rm core}\le6,\qquad
\|E\|_{\rm op}\le\frac{19.416260}{\rho},
\]
and
\[
s_3(A_{\rm core})\ge1-\frac{19.416260}{\rho}.
\]
In the exact two-line endpoint, the core groups into at most six independent variables and is itself paid by the account02/B13 finite-direction theorem. The diagonal tail is retained; no random perturbation inference is made.

The optimizer-free product reduction was reproved without a noncompact threshold maximizer, using layer cake and decreasing rearrangement, followed by sequential near-maximization and finite-union approximation.

## Applied account01/B13 inequality

On its low-score branch, for \(\widetilde\rho=\rho-\eta\), the same witness satisfies
\[
Z_{\rm strip}>\frac54 e^2\widetilde\rho^{-4},\qquad
\operatorname{dist}(u_i,\operatorname{span}u_k)<6.064\,\widetilde\rho^{-1/8},
\]
while simultaneously
\[
d_{(5)}\le2\sqrt{30\pi}\,\widetilde\rho^{-1}.
\]

## Remaining debt

\`QFORM-HUBSTRIP-PLUS-R2-DIAGONAL-TAIL-RECEIVER-v1\`: consume the paid grouped rank-six core jointly with the entangled \(O(\rho^{-1})\) diagonal tail and the near-hub strip currency, or build a valid bounded-finite-union product counterexample. Full QFORM and global continuity remain open.
