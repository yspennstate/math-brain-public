# Two-bank curved-tube proof handoff — 2026-09-23

The analytic result is written in the QFORM-density interactive report 20260923T202245Z-two-bank-curved-tube.

Independent bank vectors \(A,B\in\mathbb R^3\) with joint density caps \(M_{3,i}\) and \((L,V)\)-marginal caps \(M_{2,i}\) satisfy, for \(Z=A+B\),
\[
\Pr\{r\le|L|\le2r,\ |bP+c+dL+(\gamma+V^2)/(2L)|\le a\}
\le C ar^{3/2}|b|^{-1/2}(K_2+K_3),\quad 0<r\le1,
\]
for all real \(\gamma\) and \(b\ne0\), where \(K_j=\sqrt{M_{j,A}M_{j,B}}\). If \(|\gamma|\ge1\), stronger
\[
\le C ar^2[K_2(1+\log_+(1/(|b|r)))+K_3].
\]
The latter holds for all \(r>0\). Both estimates are uniform in \(c,d\) and need no \(V\)-window or moments.

Proof: use positive smooth dyadic \(l\) cutoff, Gaussian \(e^{-hv^2}\), and Gaussian majorant of the \(p\)-interval. Full-line Fresnel in \(v\), after Gaussian Fourier expansion, yields \(|\widehat W|\le C(ar/|b|)(|b|r/|\zeta|)^{1/2}\), uniformly as \(h\downarrow0\). For \(|\gamma|\ge1\), \(t=l/r\) van der Corput yields \(C(ar/|b|)(|b|r/|\zeta|)\) above \(|\zeta|=|b|r\). Fixed-\(\zeta\) bank energy \(S(\zeta)=\int_{\mathbb R^2}|\phi_A\phi_B|\le(2\pi)^2K_2\); total \(\int S\le(2\pi)^3K_3\). Integrate frequencies and let \(h\downarrow0\).

These bounds apply to genuine original-coordinate product frames when each bank Gram dominates \(\kappa I_3\), via bounded-density projection caps. Gamma-zero exponent \(3/2\) and hyperbolic nonzero-gamma logarithm are sharp in examples with full row overlap. For the canonical QFORM with coefficient \(\varepsilon P\), this direct tube bound is not uniform in \(\varepsilon\): costs \(|\varepsilon|^{-1/2}\) or \(\log(1/|\varepsilon|)\). Next path: keep the hub density \(f_H\) inside the Fourier integral; its characteristic function should remove the \(\varepsilon\)-loss in the dyadic density.
