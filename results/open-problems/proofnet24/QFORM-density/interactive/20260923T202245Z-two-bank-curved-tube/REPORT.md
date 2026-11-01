# Two-bank curved tube bounds with unrestricted transverse coordinate

**Date:** 2026-09-23. **Status:** proved analytic lemma; scope limited to a nonzero coefficient of the third light coordinate. The estimates do not by themselves prove the full QFORM density conjecture.

## Theorem

Let \(A=(L_A,V_A,P_A)\) and \(B=(L_B,V_B,P_B)\) be independent random vectors in \(\mathbb R^3\), with joint densities \(g_A,g_B\). Suppose their \((L,V)\) marginal densities \(m_A,m_B\) satisfy
\[
\|m_i\|_\infty\le M_{2,i},\qquad
\|g_i\|_\infty\le M_{3,i}\quad(i=A,B).
\]
Put \((L,V,P)=A+B\), \(K_j=(M_{j,A}M_{j,B})^{1/2}\), and
\[
T_{r,a}(b,c,d,\gamma)=
\left\{r\le |L|\le2r,\ 
\left|bP+c+dL+\frac{\gamma+V^2}{2L}\right|\le a\right\}.
\]
There is an absolute constant \(C\), uniform in \(r,a>0\), \(b\ne0\), and \(c,d,\gamma\in\mathbb R\), such that
\[
\tag{1}
\Pr(T_{r,a})\le C a r^{3/2}|b|^{-1/2}(K_2+K_3)
\quad(0<r\le1).
\]
If \(|\gamma|\ge1\), the stronger bound holds for all \(r>0\):
\[
\tag{2}
\Pr(T_{r,a})\le C a r^2
\left[K_2\{1+\log_+(1/(|b|r))\}+K_3\right].
\]
In particular, with \(b=1\), (1) gives the requested dyadic gain \(\alpha=1/2\) with no restriction on \(V\) and no moment assumption. For \(|\gamma|\ge1\), (2) gives every exponent \(\alpha<1\) at \(0<r\le1\), but the logarithm at \(\alpha=1\) is generally necessary. The displayed \(b\) dependence is material; (2) is not uniform as \(b\to0\).

## Smooth majorant and oscillatory bound

Choose nonnegative smooth compactly supported \(\chi_+,\chi_-\) on the positive and negative \(l/r\) dyadic intervals, respectively, such that \(\chi_+(l/r)+\chi_-(l/r)\ge1\) whenever \(r\le|l|\le2r\). Their supports stay a fixed distance from zero. Let \(\theta(u)=e^{1-u^2}\), so \(\theta\ge1\) for \(|u|\le1\). For \(h>0\), let \(G_h(v)=e^{-hv^2}\), and write
\[
F(l,v)=-c-dl-\frac{\gamma+v^2}{2l},
\qquad
W_h(l,v,p)=\left[\chi_+(l/r)+\chi_-(l/r)\right]
 G_h(v)\theta\!\left(\frac{bp-F(l,v)}a\right).
\]
For each \(h>0\), \(W_h\) is nonnegative and Schwartz, and
\(W_h\uparrow W_0\ge{\bf1}_{T_{r,a}}\) as \(h\downarrow0\).
We use \(\widehat f(\xi)=\int e^{-i\xi\cdot x}f(x)\,dx\).

Fourier transformation in \(p\) contributes
\[
\frac{a}{|b|}\widehat\theta(a\zeta/b)
\exp[-i(\zeta/b)F(l,v)].
\]
For either sign of \(l\), put \(l=\sigma rt\) with \(t\) in a fixed positive interval \([c_0,C_0]\), and \(\lambda=\sigma\zeta/(br)\). All occurrences of \(c,d\), and the \(l,v\) Fourier frequencies enter only as constant or linear phases. Apart from such phases, the remaining oscillatory integral is
\[
I_h(\lambda,k,\nu)=
\iint \chi(t)e^{-hv^2}
\exp\!\left(i\left[kt+\nu v+
\lambda\frac{\gamma+v^2}{2t}\right]\right)\,dv\,dt.
\]
The Gaussian Fourier transform has uniformly bounded \(L^1\) norm:
\(\|\widehat G_h\|_1=2\pi\). Fourier expansion of \(G_h\), followed by the full-line Fresnel formula, gives a constant of modulus \(C(t/|\lambda|)^{1/2}\) times
\[
\int\widehat G_h(\omega)
\int \chi(t)t^{1/2}
\exp\!\left(i\left[
\frac{\lambda\gamma}{2t}
+\left(k-\frac{(\nu+\omega)^2}{2\lambda}\right)t
\right]\right)\,dt\,d\omega.
\]
Consequently, for \(\lambda\ne0\),
\[
\tag{3}
|I_h(\lambda,k,\nu)|\le C|\lambda|^{-1/2}.
\]
The constant is independent of \(h,k,\nu,\gamma\). To justify Fresnel expansion and exchange of integrations, first multiply the \(v\) integrand by \(e^{-\tau v^2}\), compute the resulting complex Gaussian, and let \(\tau\downarrow0\). Its modulus is at most \(C|\lambda|^{-1/2}\), uniformly in the linear frequency, so \(\widehat G_h\in L^1\) supplies domination.

When \(|\gamma|\ge1\), the \(t\) phase in the last display has second derivative \(\lambda\gamma/t^3\). Weighted second-derivative van der Corput on the fixed interval gives \(C|\lambda\gamma|^{-1/2}\), independently of its linear coefficient. Therefore, for \(|\lambda|\ge1\),
\[
\tag{4}
|I_h(\lambda,k,\nu)|\le C|\lambda|^{-1}.
\]
Combining (3) and (4), uniformly in the first two Fourier frequencies,
\[
\tag{5}
|\widehat W_h(\xi_l,\xi_v,\zeta)|
\le C\frac{ar}{|b|}
\left|\widehat\theta(a\zeta/b)\right|
\begin{cases}
(|b|r/|\zeta|)^{1/2},&\zeta\ne0,\\
\end{cases}
\]
and, if \(|\gamma|\ge1\), replace the rightmost factor by
\[
\tag{6}
K(|\zeta|/(|b|r))=
\begin{cases}
(|b|r/|\zeta|)^{1/2},&0<|\zeta|\le |b|r,\\
|b|r/|\zeta|,&|\zeta|\ge |b|r.
\end{cases}
\]
The estimate at \(\zeta=0\) is irrelevant to the subsequent integral. Although the bound in (5) diverges there, its singularity is integrable. The factor \(|\widehat\theta|\) is uniformly bounded and will be discarded.

## Bank Fourier energies and integration

Let \(\phi_A,\phi_B\) be the bank characteristic functions, and define
\[
S(\zeta)=\int_{\mathbb R^2}
|\phi_A(\xi_l,\xi_v,\zeta)\phi_B(\xi_l,\xi_v,\zeta)|
\,d\xi_l\,d\xi_v.
\]
For each fixed \(\zeta\), \(\phi_i(\xi_l,\xi_v,\zeta)\) is the two-dimensional Fourier transform of
\(h_{i,\zeta}(l,v)=\int e^{i\zeta p}g_i(l,v,p)\,dp\), and
\(|h_{i,\zeta}|\le m_i\). Thus two-dimensional Plancherel and Cauchy–Schwarz give
\[
\tag{7}
S(\zeta)\le(2\pi)^2K_2.
\]
Three-dimensional Plancherel gives
\[
\tag{8}
\int_\mathbb R S(\zeta)\,d\zeta
\le(2\pi)^3K_3.
\]
Indeed, \(\|m_i\|_2^2\le M_{2,i}\) and
\(\|g_i\|_2^2\le M_{3,i}\), since each density has mass one.

Fourier inversion for the Schwartz \(W_h\) and the convolution law of \(A+B\) gives
\[
\mathbb E W_h(A+B)
\le(2\pi)^{-3}\int_\mathbb R
\sup_{\xi_l,\xi_v}|\widehat W_h(\xi_l,\xi_v,\zeta)|S(\zeta)\,d\zeta.
\]
No positivity of the Fourier integrand is asserted; the inequality follows after taking its absolute value. Using (5), split at \(|\zeta|=1\). By (7),
the part \(0<|\zeta|\le1\) is at most \(C ar^{3/2}|b|^{-1/2}K_2\). By (8), the rest is at most \(C ar^{3/2}|b|^{-1/2}K_3\). This proves (1).

For (2), write \(\rho=|b|r\). If \(\rho\le1\), split the \(\zeta\) integral at \(\rho\) and \(1\). Formulae (6)–(8) give respectively
\[
C ar^2K_2,\qquad
C ar^2K_2\log(1/\rho),\qquad
C ar^2K_3.
\]
If \(\rho\ge1\), split at \(1\): on \(|\zeta|\le1\), (7) gives
\(C ar^2K_2/\sqrt{\rho}\); on \(|\zeta|\ge1\), (8) and
\(K(|\zeta|/\rho)\le\sqrt{\rho}\) give
\(C ar^2K_3/\sqrt{\rho}\). Both are bounded by the right side of (2).
All estimates are independent of \(h\). Monotone convergence \(h\downarrow0\) completes the proof.

## Original-coordinate product corollary

Suppose \(Y_j\) are independent variables with densities bounded by one and \(U\in\mathbb R^{n\times3}\) has \(U^\top U=I_3\). Partition rows into two banks so that each bank Gram matrix satisfies \(U_i^\top U_i\succeq\kappa I_3\), and let \((L,V,P)=U^\top Y\). The standard bounded-density projection inequality supplies \(M_{3,i}\le C\kappa^{-3/2}\) and \(M_{2,i}\le C\kappa^{-1}\). Thus (1) and (2) apply with constants depending only on \(\kappa\), even when every original-coordinate row has nonzero coefficients in all three columns. This corollary only invokes the projection-density inequality; the analytic tube theorem above assumes the caps directly.

## Sharpness and limits

For \(b=1,\gamma=0,c=d=0\), take any two-bank example whose convolution density is bounded below near the origin. Restrict \(l\in[r,2r]\), \(|v|\le c_0\sqrt r\), and \(|p+v^2/(2l)|\le a\), with sufficiently small fixed \(c_0,a\). The resulting volume is comparable to \(ar^{3/2}\), so (1)'s exponent is sharp.

The logarithm in (2) is necessary even with overlap in every original row. Take six iid \(Y_j\sim\mathrm{Unif}[-1/2,1/2]\), with three in each bank, and use the coefficient matrix \(R/\sqrt2\) for each bank, where
\[
R=\frac13\begin{pmatrix}1&2&2\\2&1&-2\\2&-2&1\end{pmatrix}.
\]
This \(R\) is orthogonal with no zero entry. The full frame is Parseval, each bank Gram is \(I_3/2\), and the convolution density is bounded below on a ball about zero. Set \(\gamma=-1\), \(l_0=3r/2\), \(d=-1/(2l_0^2)\), \(c=1/l_0\). Then
\[
F(l,v)=\frac{[(l-l_0)/l_0]^2-v^2}{2l}
=\frac{uw}{2l},\qquad
u=(l-l_0)/l_0+v,\quad w=(l-l_0)/l_0-v.
\]
For sufficiently small \(r,a\), a region
\(|u|,|w|\le h_0,\ |uw|\le c_0r,\ |p-F(l,v)|\le a\)
lies in the fixed ball and the dyadic tube. Its \(u,w\) area is comparable to \(r\log(1/r)\), and \(dl\,dv=(l_0/2)\,du\,dw\). Hence its probability is at least \(c\,ar^2\log(1/r)\). This proves sharpness of the endpoint logarithm under genuine three-column row overlap.

For the canonical expression \(2HL+\beta L^2+V^2+2\varepsilon LP\), inversion in \(H\) produces a different integral with the hub density as a weight. Applying (2) directly to \(\varepsilon P\) costs \(\log(1/(|\varepsilon|r))\); applying (1) costs \(|\varepsilon|^{-1/2}\). No uniform-in-\(\varepsilon\) full density claim follows from this tube lemma alone. The case \(b=0\) is outside the theorem.
