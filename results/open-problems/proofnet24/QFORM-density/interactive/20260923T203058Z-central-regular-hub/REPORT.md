# Central QFORM density with a regular hub, and the critical Fourier obstruction

**Date:** 2026-09-23. **Status:** conditional central theorem proved; the arbitrary cap-one hub case remains open in this argument.

## Conditional theorem

Let \(H\) be independent of \(Z=(L,V,P)=A+B\), with density \(f_H\le1\). Let \(A,B\) be independent \(\mathbb R^3\) bank vectors, each with a joint bounded density and with \((L,V)\)-marginal density bounded by \(M_{2,A},M_{2,B}\). Put \(K_2=(M_{2,A}M_{2,B})^{1/2}\) and
\[
N_{1/2}(H)=\int_{\mathbb R}
\frac{|\phi_H(t)|}{\sqrt{|t|}}\,dt,\qquad
\phi_H(t)=\mathbb E e^{itH}.
\]
If \(N_{1/2}(H)<\infty\), then for any \(\varepsilon\ne0\), any \(\beta\in\mathbb R\), and
\[
Q=2HL+\beta L^2+V^2+2\varepsilon LP,
\]
the density of \(Q\) obeys
\[
\tag{1}
\|p_Q\|_\infty\le\frac12+C K_2 N_{1/2}(H).
\]
The constant is independent of \(\varepsilon,\beta\), the locations of bank supports, and all moments. For each dyadic \(0<r\le1\), the contribution
\[
D_r(s)=\mathbb E\left[
\frac{{\bf1}_{r\le|L|\le2r}}{2|L|}
f_H\left(\frac{s-\beta L^2-V^2}{2L}-\varepsilon P\right)\right]
\]
satisfies
\[
\tag{2}
D_r(s)\le C K_2\sqrt r\,N_{1/2}(H).
\]
For \(\varepsilon=0\), a direct physical-space coarea argument gives (1) with an absolute \(CK_2\) in place of \(CK_2N_{1/2}(H)\), for every cap-one \(f_H\), including rough ones.

The hypothesis \(N_{1/2}(H)<\infty\) holds, for example, if \(f_H\) has bounded variation, since \(|\phi_H(t)|\le\min(1,\operatorname{TV}(f_H)/|t|)\). It also holds for a uniform density on an interval.

## Proof of the \(\varepsilon\ne0\) estimate

Smooth \(f_H\) by a Gaussian of variance \(\tau>0\), and use a smooth dyadic majorant \(\chi(l/r)\) supported away from \(l=0\), together with \(e^{-hv^2}\), \(h>0\). For the resulting nonnegative kernel \(W(l,v,p)\), Fourier transformation in \(p\) gives
\[
\widehat W(\xi_l,\xi_v,\zeta)
=\frac1{|\varepsilon|}\phi_H(\zeta/\varepsilon)
e^{-\tau(\zeta/\varepsilon)^2/2}
\int\frac{\chi(l/r)}{2|l|}e^{-hv^2}
e^{-i(\xi_l l+\xi_v v)}
e^{-i(\zeta/\varepsilon)(s-\beta l^2-v^2)/(2l)}
\,dl\,dv.
\]
For either sign \(l=\sigma rt\), the factor \(dl/(2|l|)\) becomes a fixed smooth amplitude in \(t\) on an interval away from zero. The \(v\) phase is quadratic with coefficient proportional to \((\zeta/\varepsilon)/r\). Expand the Gaussian \(e^{-hv^2}\) into its Fourier transform, whose \(L^1\) norm is \(2\pi\), and use the full-line Fresnel formula. The remaining \(t\) integral is bounded trivially. Uniformly in \(\xi_l,\xi_v,h,s,\beta\), this gives
\[
\tag{3}
\sup_{\xi_l,\xi_v}|\widehat W(\xi_l,\xi_v,\zeta)|
\le\frac C{|\varepsilon|}
|\phi_H(\zeta/\varepsilon)|
e^{-\tau(\zeta/\varepsilon)^2/2}
\sqrt{\frac{|\varepsilon|r}{|\zeta|}}
\quad(\zeta\ne0).
\]
The Fresnel exchange is justified by an additional Gaussian regulator, then dominated convergence; the complex Gaussian modulus is bounded by the right-hand square-root factor.

With bank characteristic functions \(\phi_A,\phi_B\), define
\[
S(\zeta)=\int_{\mathbb R^2}
|\phi_A(\xi_l,\xi_v,\zeta)\phi_B(\xi_l,\xi_v,\zeta)|\,d\xi_l\,d\xi_v.
\]
At fixed \(\zeta\), two-dimensional Plancherel and Cauchy–Schwarz give
\(S(\zeta)\le(2\pi)^2K_2\): the relevant Fourier inverse is
\(\int e^{i\zeta p}g_i(l,v,p)\,dp\), bounded in absolute value by the bank's \((L,V)\)-marginal density. Pair (3) with \(S\), and substitute \(t=\zeta/\varepsilon\). The factor \(1/|\varepsilon|\) cancels exactly with \(d\zeta\), leaving \(CK_2\sqrt r\,N_{1/2}(H)\). This proves (2) for the regularized density.

Because each bank has a bounded joint density, the light sum has a density. Thus for \(\varepsilon\ne0\) the hub argument is absolutely continuous, and Gaussian smoothing of \(f_H\) converges at almost every sampled argument. The kernels are bounded by the dyadic weight \(1/(2|L|)\); dominated convergence removes \(\tau\). Monotone convergence removes \(h\). Summing (2) over \(r=2^{-j}\), \(j\ge0\), is finite. On \(|L|\ge1\), direct hub inversion gives a contribution at most \(1/2\). This proves (1).

For \(\varepsilon=0\), the \((L,V)\) density of \(Z\) is bounded by \(K_2\) after convolution. At fixed \(l\), substitute \(v=\sqrt{2|l|}\,u\). The elementary estimate
\[
\sup_x\int_{\mathbb R} f_H(x-u^2)\,du\le C
\]
holds for every density \(f_H\le1\), by splitting the equivalent \(z^{-1/2}\) kernel at \(z=1\): use the cap near zero and unit mass away from zero. This gives \(D_r(s)\le CK_2\sqrt r\) and the same dyadic summation.

## Why this does not settle arbitrary cap-one hubs

There is no universal bound on \(N_{1/2}(H)\) from \(f_H\le1\) and \(\int f_H=1\). Here is a constructive unbounded family.

For integers \(N\), take independent Rademacher signs \(\sigma_k\) and
\[
K_N(x)=\sum_{k=1}^N\frac{\sigma_k\cos(kx)}{\sqrt k},
\qquad x\in[0,2\pi].
\]
On any fixed compact subinterval away from \(0\) and \(\pi\),
\(\sum_{k\le N}\cos^2(kx)/k=\tfrac12\log N+O(1)\).
The Khintchine inequality and integration in \(x\) therefore give a sign choice with
\(\int_0^{2\pi}|K_N(x)|\,dx\ge c\sqrt{\log N}\).
Fix such a choice. Let \(m_N=(2\pi)^{-1}\int_0^{2\pi}\operatorname{sgn}K_N(x)\,dx\), and set
\[
f_N(x)=\frac{1+[\operatorname{sgn}K_N(x)-m_N]/2}{2\pi}
\,{\bf1}_{[0,2\pi]}(x).
\]
Then \(0\le f_N\le1/\pi<1\), \(\int f_N=1\), and, because \(K_N\) has mean zero,
\[
\sum_{k=1}^N\frac{|\operatorname{Re}\phi_{f_N}(k)|}{\sqrt k}
\ge\int f_N(x)K_N(x)\,dx
=\frac1{4\pi}\int_0^{2\pi}|K_N(x)|\,dx
\ge c\sqrt{\log N}.
\]
A smooth cutoff equal to one on \([0,2\pi]\) gives the standard sampling estimate
\[
\sum_{k\ge1}\frac{|\phi_f(k)|}{\sqrt k}
\le C\int_{\mathbb R}\frac{|\phi_f(t)|}{\sqrt{1+|t|}}\,dt
\]
for \(f\) supported on that fixed interval: write \(\phi_f=\phi_f*\widehat\chi/(2\pi)\), and sum the rapidly decreasing translates of \(\widehat\chi\). Since the weight \(|t|^{-1/2}\) dominates \((1+|t|)^{-1/2}\), the \(N_{1/2}\) norms of the capped \(f_N\) are unbounded.

This is an obstruction to the absolute-Fourier method, **not** a counterexample to a uniform density bound for QFORM. The unresolved central regime is \(|s|<1\), \(r\gg|\varepsilon|\), with genuinely overlapping \(P\) and a rough capped hub. The two-bank curved-tube theorem in the companion report covers \(r\lesssim|\varepsilon|\), while its direct fixed-hub application loses \(|\varepsilon|^{-1/2}\) for larger \(r\).
