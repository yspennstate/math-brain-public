# Two physical hubs and a disjoint transverse quadratic block

**Status:** proved sufficient receiver for arbitrary dense quadratic terms among the remaining light coordinates. The full spectral QFORM conjecture remains **OPEN**: this result requires an actual disjoint physical block and quantitative crossing projections.

## The square theorem

Let \(H\in\mathbb R^2\) be independent of \((V,W)\), with a joint probability density \(f_H\le L\). Let \(V\) be an independent original-coordinate scalar of density \(f_V\le1\), independent also of \(W\). Let \(Y=Y(W)\in\mathbb R^2\) have a joint probability density \(m(y)\le M\). There is no restriction on the joint law of any other statistics of \(W\). For finite measurable functions \(R(H),F(W),G(W)\) and \(\lambda\ne0\), set
\[
 Q=R(H)+2H\cdot Y(W)+\lambda V^2+2V G(W)+F(W).
 \tag{1}
\]
Then \(Q\) has a continuous \(C_0\) density satisfying
\[
 \boxed{\ \|p_Q\|_\infty
 \le C_*(LM)^{2/5}|\lambda|^{-1/5}
 <16(LM)^{2/5}|\lambda|^{-1/5}\ },
 \quad C_*=\frac5\pi
 \left(\frac{\pi\sqrt{30}\,2^{1/4}}
 {8(1-2^{-1/4})}\right)^{4/5}<14.682.
 \tag{2}
\]
For two untouched original cap-one hubs, \(L=1\). If \(Y=TW\), \(W\) consists of independent cap-one original coordinates, and \(T\) has rank two, the product-marginal estimate gives \(M\le2/\sqrt{\det(TT^{\mathsf T})}\).

The point of (1) is that **\(F(W)\) is completely arbitrary**. In particular it may contain every dense, indefinite quadratic term among the coordinates of \(W\). Likewise \(G(W)\) may contain every mixed quadratic interaction \(V W_j\). Only the hub-light coupling must be confined to \(2H\cdot Y(W)\); \(V\) is absent from this coupling.

### Proof

Write the disintegration of \(W\) over \(Y(W)\) as a finite positive kernel \(\nu_y(dw)\) of mass \(m_y=m(y)\), so \(d\mathbb P_W(w)=\nu_y(dw)\,dy\) under the map \(Y\). For almost every \(y\), push the positive measure \(\nu_y(dw)f_V(v)\,dv\) forward under
\[
 (w,v)\longmapsto F(w)+2vG(w)+\lambda v^2
\]
and call the resulting finite measure \(\mu_y\). Its mass is \(m_y\). For any interval \(I\) of length \(r>0\), completing the square *separately for each \(w\)* shows
\[
 \mu_y(I)\le 2m_y\sqrt{r/|\lambda|}.                 \tag{3}
\]
No conditional density of \(W\) given \(Y=y\) is bounded or invoked. The only scalar cap used here is \(f_V\le1\). In particular the center of the square may move arbitrarily with \(w\).

Put \(G_t(y)=\widehat\mu_y(t)\). Then \(\|G_t\|_1\le1\), and independence of \(H\) gives
\[
 \varphi_Q(t)=\int f_H(h)e^{itR(h)}
                    \widehat G_t(2th)\,dh .
\]
Two-dimensional Plancherel, \(\|f_H\|_2^2\le L\), and Cauchy--Schwarz yield
\[
 |\varphi_Q(t)|\le\pi L^{1/2}|t|^{-1}\|G_t\|_2
 \quad\text{for almost every }t\ne0.                  \tag{4}
\]

For completeness, the energy estimate is as follows. The Gaussian majorant
\(\mathbf1_{\{|t|\le T\}}\le e^{1/4}e^{-t^2/(4T^2)}\)
and the Gaussian Fourier identity give
\[
 \int_{-T}^T|\widehat\mu_y(t)|^2dt
 \le2e^{1/4}\sqrt\pi T
 \iint e^{-T^2(s-s')^2}\,\mu_y(ds)\mu_y(ds').
\]
For fixed \(s\), partition \(s'\) into intervals of length \(1/T\) from \(s\) toward either side. The Gaussian weights are at most \(e^{-j^2}\), \(j=0,1,\dots\), twice, and each interval has \(\mu_y\)-mass at most \(2m_y/\sqrt{|\lambda|T}\) by (3). Since \(2\sum_{j\ge0}e^{-j^2}<3\) and \(2e^{1/4}\sqrt\pi\cdot6<30\),
\[
 \int_{-T}^T|\widehat\mu_y(t)|^2dt
 \le30m_y^2\sqrt{T/|\lambda|}.
\]
Integrating \(y\), and using \(\int m_y^2dy\le M\int m_y\,dy=M\), proves
\[
 \int_{-T}^T\|G_t\|_2^2dt\le30M\sqrt{T/|\lambda|}. \tag{5}
\]
In particular (4) is justified a.e. on each compact frequency interval. On a two-sided dyadic shell \(T\le|t|\le2T\), equations (4)--(5) and \(\int_{\rm shell}|t|^{-2}dt=1/T\) give
\[
 \int_{\rm shell}|\varphi_Q(t)|dt
 \le\pi\sqrt{30LM}\,2^{1/4}|\lambda|^{-1/4}T^{-1/4}.
\]
Sum over \(T=2^jT_0\), bound \(|\varphi_Q|\le1\) below \(T_0\), and optimize:
\[
 \|p_Q\|_\infty\le \frac{T_0}{\pi}
 +\frac{\sqrt{30}\,2^{1/4}}{2(1-2^{-1/4})}
      \sqrt{LM}|\lambda|^{-1/4}T_0^{-1/4}.
\]
This yields (2) and integrability of \(\varphi_Q\), hence a \(C_0\) density. The sign of \(\lambda\), the support geometry, and all moments are unrestricted.

## A disjoint nonsingular physical pair

Let \(V=(V_1,V_2)\) instead consist of **two** independent original cap-one coordinates, disjoint from \(H,W\). Replace the \(V\)-dependent part of (1) by
\[
 V^{\mathsf T}DV+2V\cdot G(W),
 \qquad D=D^{\mathsf T}\in\mathbb R^{2\times2},
 \quad d=|\det D|>0,
\]
where \(G(W)\) is arbitrary and \(F(W),R(H)\) remain arbitrary. Then
\[
 \boxed{\ \|p_Q\|_\infty
 \le C_*\,34^{2/5}(LM)^{2/5}d^{-1/10}
 <61(LM)^{2/5}d^{-1/10}\ }.                           \tag{6}
\]
This holds for either signature of \(D\).

Indeed, the affine-uniform rank-two half-power theorem in the current QFORM manuscript (manuscript/rank_two.tex, Theorem "Rank-two half-power potential") gives, for each fixed \(w\) and every interval \(I\) of length \(r\),
\[
 \mathbb P\{V^{\mathsf T}DV+2V\cdot G(w)+F(w)\in I\}
 \le68\,d^{-1/4}\sqrt r .
\]
For example, center \(I\) at \(s\), use
\(\mathbf1_{\{|Z-s|\le r/2\}}\le(r/2)^{1/2}|Z-s|^{-1/2}\),
and retain the larger stated bound. Mixing over \(\nu_y\) gives the interval cap \(68m_y d^{-1/4}\sqrt r\). Repeating the Gaussian-energy computation gives (5) with \(30|\lambda|^{-1/2}\) replaced by \(15\cdot68d^{-1/4}\); thus repeat the optimization with \(|\lambda|^{-1/2}\) replaced by \(34d^{-1/4}\), obtaining (6).

## Scope

This theorem needs two hub coordinates independent of a **disjoint** physical transverse coordinate or nonsingular pair; the crossed statistic \(Y(W)\) must exclude that block and have a controlled planar density. The spectral condition \(s_3(A)\ge1\) alone does not ensure a diagonal transverse pivot, a nonsingular pair, or a quantitative crossing determinant, and a hub-to-transverse interaction is outside the displayed normal form. The result therefore cannot be cited as a proof of the unrestricted problem.