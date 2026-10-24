# account04/B05 handoff — rough ruled interval and two-sheet receiver

Run: `20260923T031319Z-account04-B05-rough-ruled-r1`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: supporting theorems proved; full universal conjecture open; continuity separate.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics: `yspennstate/math-open-problems@f1b0950e5b2275d72a832fc32c2b45e33b1d0567`.

Path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260923T031319Z-account04-B05-rough-ruled-r1/REPORT.md`.

Results:

- The exact smooth coarea coordinates give
\[
dz=\frac{\rho}{\sqrt{\lambda_1\lambda_2\mu}}\,d\rho\,d\theta\,dw,
\qquad dy=2\rho\,d\rho,
\]
so the polar and level Jacobians cancel.
- Mollification preserves cap one. Weak convergence plus Portmanteau transfers the smooth ruled estimate to every rough product law:
\[
\Pr\{Q\in J\}\le C_+(\lambda)|J|\le\frac{\pi\sqrt2}{s}|J|,
\qquad J\subset[0,\infty).
\]
The endpoint uses \(\Pr(Q=0)=0\). No pointwise rough surface trace is used.
- Applying account01/B05 r25 in the one-rank-two/two-rank-one packet gives, when \(\max_i u_i^2\ge\eta\),
\[
\Pr\{Q\in I\}<41(\mathfrak m\eta)^{-1/3}|I|.
\]
This full-line estimate pays the convex/two-sheet contribution in that branch without scalar-pair condition-number or scale loss.
- Complementary receivers are \(256(\mathfrak m\|B\|_{\rm op})^{-1/4}\) for invertible \(B\), and \(16\mathfrak m^{-1/3}\) at rank one.

First unpaid local implication: diffuse Schur grouping when \(\|B\|_{\rm op}\to0\), \(\mathfrak m\gtrsim1\), \(\max_i u_i^2\to0\), and \(\sum_i u_i^2=1\). The correlated orthogonal first-bank aggregate enters pair translations and cannot be conditioned away.

Source pins: account01/B05 r25 blob `0bed6a6426109541a9664c70b1acb27a9166528a`, audit commit `3e8704eead81b6fef2d305978ec89abb307d899a`; account02/B05 checkpoint blob `f0be659bbc113dbf7c203f6a42d4791c4d7e6d32`; Claude base `e5f71d79eff325201dd0274053d20268ce65b837`.
