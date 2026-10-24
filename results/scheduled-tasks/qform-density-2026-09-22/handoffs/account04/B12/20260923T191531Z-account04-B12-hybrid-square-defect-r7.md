# account04/B12 handoff — hybrid square-defect reserve

Run: 20260923T191531Z-account04-B12-hybrid-square-defect-r7
Status: supporting theorem proved; unrestricted QFORM remains open.

Canonical mathematics:
- repository: yspennstate/math-open-problems
- commit: 3df1475f988c811570dc5c249a7756d24adb51bf
- path: proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T191531Z-account04-B12-hybrid-square-defect-r7/REPORT.md

New theorem:
For commuting replacements \(B=A_0+C\), let \(d_j\) be the ordered losses \((\lambda_j(A_0)^2-\lambda_j(B)^2)_+\). For an arbitrary noncommuting packet \(D\), let \(\nu_j\) be the ordered eigenvalues of \([B^2-(B+D)^2]_+\). After a rank-\(r\) packet and an operator-norm-\(\delta\) tail,
\[
\sqrt{\lambda_k((A^2)[H,H])}
\ge
\left[
\sqrt{\left(\lambda_{k+r+q+p}((A_0^2)[H,H])-d_{p+1}-\nu_{q+1}\right)_+}
-\delta
\right]_+ .
\]
This simultaneously spends commuting and noncommuting destructive profiles while retaining an actual original-coordinate square-Gram gate.

Concrete target-class application:
A 16-dimensional Hadamard baseline permits fourteen arbitrary-sign, arbitrary-magnitude commuting replacements, two severe commuting losses, a full-rank noncommuting packet with rank-two destructive-square defect, an arbitrary rank-one packet, and a dense tail of norm at most \(1/4\). Every eleven-coordinate carrier satisfies
\[
\sqrt{\lambda_6((A^2)[H,H])}\ge7/4,
\qquad s_3(A)\ge7/4.
\]
Applying account02/B12 gives
\[
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}<1198.
\]

Sources:
- account01/B12: ee689fe26770341f205276b7b167b84f62f8f897
- account04/B12 predecessor: c307f81b3196820aa711a5c47f243feeeeb74781
- account02/B12 compiler: e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004
- current brain request blob: 352f1ea2d70f3c0c48379933bb31bdcff1ef5e0
- live corrections blob: 6bdbd9987a4eefeba79d53915cfe7e232263f8ec

Exact remaining gap:
Extract a bounded original-coordinate carrier with six quantitative square modes from \(s_3(A)\ge1\), or route failure into an already paid crossing/pair/ridge/volume mechanism. Continuity is not claimed for this branch.
