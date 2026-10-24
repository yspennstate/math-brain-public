# Two-bank fixed-target density update

The all-target rough-hub canonical branch remains open. A new source-pinned theorem controls each nonzero target, with a logarithmic loss near zero:

https://github.com/yspennstate/math-open-problems/blob/9c34c5b1ab2ba2d84a75c6ecc86a79ab17cb77d5/proofnet24/QFORM-density/interactive/20260923T204600Z-fixed-target-two-bank-density/REPORT.md

For \(Q=2HL+\beta L^2+V^2+2\varepsilon LP\), \(\varepsilon\ne0\), arbitrary cap-one independent physical hub \(H\), and light \(Y=Y_A+Y_B\) with independent banks whose planar \((L,V)\) marginal caps are \(M_A,M_B\),
\[
p_Q(s)\le \tfrac12+C\sqrt{M_A M_B}
 \bigl(1+\sqrt{\log_+(1/|s|)}\bigr)
\quad\text{for a.e. }s\ne0.
\]
No \(P\) projection cap, hub support bound, moment, or regularity is needed. The exact Fresnel transform followed by van der Corput in the dyadic \(L\) variable gives
\[
\sup_{\xi_L,\xi_V}|\widehat W_{r,s}(\xi_L,\xi_V,\varepsilon\eta)|
\le \frac{C|\phi_H(\eta)|}{|\varepsilon|}
\min\{\sqrt{r/|\eta|},\,r/(\sqrt{|s|}|\eta|)\}.
\]
Planar bank Plancherel bounds the bank Fourier product uniformly at each \(\varepsilon\eta\). Split frequencies at \(1,r/|s|\) and sum dyadic \(r\). The proof has a careful distributional Fourier and singular-bank regularization argument.

In the original-product orthonormal-light setting, separate all-plane coarea covers \(s\ge0\); the two-bank center-continuity bound covers \(-|\varepsilon|\le s\le0\). The unresolved negative range is \(|\varepsilon|\ll-s\ll1\), with a rough fragmented \(H\) and an overlapping \(P\). The dependent-light negative-shell fake shows all-plane projection caps alone do not close this.

A separate restricted weak-\(L^2\) sufficient target and proved independent-transverse-leakage case are here:
https://github.com/yspennstate/math-open-problems/blob/62f9d598de628104d39ed19a9851b60f6eccded5/proofnet24/QFORM-density/interactive/20260923T204500Z-restricted-weak-l2-hub-target/REPORT.md

**Do not mark the full QFORM-density problem solved.** There is no proved uniform estimate across the remaining negative range and no verified original-product counterexample.
