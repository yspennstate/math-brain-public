# A rank-three product-law obstruction to uniform power Fourier decay

**Scope.** This report refutes a proposed proof route, not the QFORM density conjecture. It constructs independent original coordinates with densities at most one and a real symmetric quadratic matrix with third singular value exactly one, for which the characteristic function has size at least \(c/t\) at an arbitrarily large prescribed frequency \(t\). The example has an exactly linear physical hub, two independent planar light banks, and no affine term. Its quadratic form still has a bounded density by the separate direct two-light coarea theorem.

## Statement

There is an absolute \(c>0\) such that for every sufficiently large \(t\) one can choose five independent real random variables \(H,L_A,L_B,V_A,V_B\), each with a density bounded by one, so that
\[
Q=2H(L_A+L_B)+(L_A+L_B)^2+(V_A+V_B)^2
\]
satisfies
\[
\bigl|\mathbb E e^{itQ}\bigr|\ge \frac{c}{t}.
\]
If \(A\) is the symmetric matrix of \(Q\) in these five original coordinates, then its nonzero eigenvalues are \(1+\sqrt3,\,2,\,1-\sqrt3\). Consequently the quadratic form \(\widetilde Q=Q/(\sqrt3-1)\) has \(s_3(\widetilde A)=1\) and, at the correspondingly rescaled frequency, still has characteristic-function size \(\gtrsim 1/t\).

Thus no bound \(|\phi_{X^\top A X}(t)|\le C|t|^{-1-\eta}\), with \(C,\eta>0\) universal, follows from independent cap-one coordinates and \(s_3(A)\ge1\). In particular, a proof based on a universal pointwise power decay faster than \(t^{-1}\) cannot establish the complete density conjecture. This example does not decide whether some other absolute-Fourier estimate could work.

## Construction

Let \(L_A,L_B\) be independent uniforms on \([-8,8]\), and \(V_A,V_B\) independent uniforms on \([-1/2,1/2]\). Write \(S=L_A+L_B\) and \(T=V_A+V_B\). Their densities are
\[
g_S(s)=\frac{(16-|s|)_+}{256},
\qquad
g_T(v)=(1-|v|)_+.
\]
In particular \(g_S(-h)\ge 3/64\) for \(|h|\le4\), and \(g_T(0)=1\).

For sufficiently large \(t\), the set
\[
G_t=\{h\in[-4,4]:\cos(th^2)\ge 2^{-1/2}\}
\]
has measure greater than one. Indeed the periodic indicator \(1_{\{\cos u\ge2^{-1/2}\}}\) has mean \(1/4\), and a substitution \(u=th^2\), followed by the elementary periodic-mean estimate away from \(h=0\), gives \(|G_t|\to 8/4=2\). Choose any measurable \(E_t\subseteq G_t\) of measure one and let \(H\) have density \(1_{E_t}\). This is a cap-one probability density.

Complete the square:
\[
Q=(H+S)^2-H^2+T^2.
\]
The two triangular densities have integrable Fourier transforms. Fourier inversion of the Fresnel kernel gives, uniformly for \(h\in[-4,4]\),
\[
\int g_S(s)e^{it(h+s)^2}\,ds
 =e^{i\pi/4}\sqrt{\frac{\pi}{t}}\,g_S(-h)+o(t^{-1/2}),
\]
and
\[
\int g_T(v)e^{itv^2}\,dv
 =e^{i\pi/4}\sqrt{\frac{\pi}{t}}+o(t^{-1/2}).
\]
For completeness, if \(g\) has \(\widehat g\in L^1\), the first formula follows from
\[
\int g(x)e^{it(x+h)^2}\,dx
=e^{i\pi/4}\sqrt{\frac{\pi}{t}}\,
\frac1{2\pi}\int \widehat g(\xi)e^{-i\xi h}e^{-i\xi^2/(4t)}\,d\xi.
\]
Dominated convergence makes the error uniform in \(h\), since its absolute bound does not depend on \(h\).

Independence and the square completion now yield
\[
\mathbb E e^{itQ}
=i\,\frac{\pi}{t}
\int_{E_t}g_S(-h)e^{-ith^2}\,dh+o(t^{-1}).
\]
The real part of the integral is at least
\[
\frac{3}{64}\cdot\frac1{\sqrt2}\cdot |E_t|
=\frac{3}{64\sqrt2}.
\]
Hence \(|\mathbb E e^{itQ}|\ge c/t\) for all sufficiently large \(t\), for instance with any fixed \(c<3\pi/(64\sqrt2)\) after increasing the starting frequency.

## Spectral and bank checks

Use orthonormal coordinates \(h=H\), \(\ell=(L_A+L_B)/\sqrt2\), \(v=(V_A+V_B)/\sqrt2\), together with the two difference coordinates. On the active three-dimensional subspace,
\[
Q=2\sqrt2\,h\ell+2\ell^2+2v^2,
\qquad
A_{\rm active}=
\begin{pmatrix}
0&\sqrt2&0\\
\sqrt2&2&0\\
0&0&2
\end{pmatrix}.
\]
The eigenvalues stated above follow; the remaining two eigenvalues are zero. Every original coordinate has density at most one. The two light banks \((L_A,V_A)\) and \((L_B,V_B)\) have independent planar densities bounded by \(1/16\).

For a general two-bank cross-phase notation, the same example has \(C=\operatorname{diag}(2,2)\), \(C_{VV}=2\), bank-local phases \(R_A=L_A^2+V_A^2\) and \(R_B=L_B^2+V_B^2\), and the hub phase is exactly zero. Thus the obstruction survives an exactly linear physical hub.

**Limit.** In the strict small-leakage canonical gate \(|\beta|\le\varepsilon^2\), taking \(\varepsilon=0\) forces \(\beta=0\). The present example has effective \(L^2\) coefficient one and does not address that stricter corner. It gives no unbounded-density construction.
