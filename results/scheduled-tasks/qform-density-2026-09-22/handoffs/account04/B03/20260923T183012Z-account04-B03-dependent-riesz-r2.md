# account04/B03 handoff — dependent sum/difference fractional budget

Run: \`20260923T183012Z-account04-B03-dependent-riesz-r2\`  
Status: supporting theorem proved; full conjecture open; continuity not claimed.

For an independent copy \(X'\), put \(U=X-X'\), \(V=X+X'\). Although \(U,V\) are dependent, each marginal vector has independent cap-one coordinates. If \(R_-(U)\), \(R_+(V)\) are arbitrary-affine invertible physical-pair quadratics and \({\cal B}(P)\) is the account01/B03 r18 half-Riesz bound, then
\[
\sup_{s,t}\mathbb E|R_-(U)-s|^{-\theta/2}|R_+(V)-t|^{-(1-\theta)/2}
\le {\cal B}(P_-)^\theta{\cal B}(P_+)^{1-\theta},\qquad0\le\theta\le1.
\]
The proof uses Hölder under the exact joint law. At \(\theta=1/2\), it pays the joint \(1/4+1/4\) singularity without false sum/difference independence.

The partner theorem also gives
\[
\|p_Q\|_{\infty,\mathrm{ess}}\le128|d|^{-1/2}|\det P|^{-1/4}
\]
for an actual active original-coordinate block \(P\oplus[d]\), retaining all conditioning-generated affine terms. If both eigenvalues of \(P\) and \(d\) have modulus at least one, the bound is \(128\).

The exact remaining gap is the missing half power needed for a full \(L^1\)-time estimate. A formal \(1/2+1/2\) Hölder step would require full Riesz moments, which diverge already for standard physical pairs. The next mechanism must use oscillatory cancellation or a genuinely third source-coordinate receiver.

Source pins:
- Brain source head read: \`6cccc56b8f6f106faa287c788886d478f698bdee\`.
- Required Claude base: \`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837\`.
- Current continuation checked: \`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md\`.
- Partner: account01/B03 r18.
- Corrected report: \`math-open-problems@05ff82a8d052b024ae584e60dffb7b198fcd7db4:proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260923T183012Z-account04-B03-dependent-riesz-r2/REPORT.md\`.
- Corrections retained: \`QFORM-UV-CONDITIONAL-CAP-FALSE\`, arbitrary-joint coarea false, conditional positive-moment false, no post-rotation independence, no uniform pointwise decay.
