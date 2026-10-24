# QFORM handoff: bilinear Fourier \(L^p\) resonance obstruction

**Status:** proved; scope is a falsified Fourier shortcut, not the quadratic density conjecture.

**Full proof:** https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T194654Z-bilinear-fourier-resonance/REPORT.md

For any \(1\leq p<2\), there is no universal \(L^p(\mathbb R_t)\) bound for \(\psi(t)=\mathbb E e^{2itHL}\) when \(H,L\) are independent with one-dimensional densities capped by one. Explicitly, let \(H_N,L_N\) be i.i.d. with
\[
f_N(x)=b_N(1+\cos(N\log x))\mathbf1_{[1,4]}(x),
\quad b_N^{-1}=3+\int_1^4\cos(N\log x)\,dx.
\]
For \(N\geq6\), this is a probability density \(\leq1\). Their product density contains the coherent term \(\frac12b_N^2 c(z)\cos(N\log z)\), where \(c(z)=\log z\) on \([1,4]\) and \(\log(16/z)\) on \([4,16]\); all other nonconstant Mellin integrals have \(O(N^{-1})\) amplitude. Stationary phase yields \(|\mathbb E e^{itH_NL_N}|\gtrsim N^{-1/2}\) throughout \(t\in[N/3,N/2]\), and hence \(\int|\psi|^p\gtrsim N^{1-p/2}\to\infty\).

**Practical effect:** Do not use an absolute \(L^{3/2}\) norm of the isolated \(HL\) Fourier factor to prove the exact-coloop or diffuse-leakage receiver. This does not preclude signed cancellation after adding \(V^2\) and therefore is not a counterexample to the conjecture.

**Next target:** A product-specific signed oscillatory estimate for the complete phase \(2(H+\varepsilon W)L+V^2\), especially on the nonruled negative-target side.


**Sharp endpoint added to report (commit f34ca21deff2e7fdae04b4b238fdd249ba7f0c80):** If \(g\) is the density of \(HL\), then \(\|g\|_2^2\leq4\), equality for iid uniform \([-1/2,1/2]\). Thus \(\int_{\mathbb R}|\mathbb E e^{itHL}|^2dt\leq8\pi\) and the \(e^{2itHL}\) normalization gives \(4\pi\). The Fourier threshold is exact: uniform \(L^p\) for every \(p\geq2\), failure for every \(p<2\). The same report proves \(g\) has bounded \(L^r\) norm for every finite \(r\); this physical-space fact does not imply a Fourier \(L^p\) bound below two.
