# A uniform outer-level receiver for a one-hub form with overlapping light projections

**Status:** proved scoped theorem. It does not control central target levels uniformly and does not settle the full QFORM density conjecture.

## Theorem

Let \(H\) have an arbitrary probability density \(f_H\leq1\). Let
\[
(L,V,P)=(L_1,V_1,P_1)+(L_2,V_2,P_2),
\]
where the two three-component banks are independent of one another and of \(H\). The bank components within either bank may be arbitrarily dependent. Suppose each planar marginal \((L_j,V_j)\) has a probability density \(g_j\leq M_j\). No density assumption on \(P_j\) or on the full three-component bank is required. Then, for every real \(\beta,\varepsilon\), the random variable
\[
Q=2HL+\beta L^2+V^2+2\varepsilon LP
\tag{1}
\]
has a density satisfying
\[
\operatorname*{ess\,sup}_{|s|\geq1}p_Q(s)
 \leq \frac12+C\sqrt{M_1M_2},
\tag{2}
\]
where \(C\) is an absolute finite constant, independent of \(\beta,\varepsilon\), all supports, and all bank laws. If \(\varepsilon=0\), the earlier [beta-uniform one-hub coarea theorem](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T203100Z-beta-uniform-one-hub-square/REPORT.md) controls every target level, with the global planar density cap at most \(\min(M_1,M_2)\).

This theorem is especially useful for overlapping \(P\): both \(P_j\) may be formed from the same original leaves as \(L_j,V_j\). The only independence invoked is between the two banks and the physical hub.

## Planar Fourier slice bound

Use the Fourier convention \(\widehat f(\xi)=\int e^{-i\xi\cdot x}f(x)\,dx\). Write
\[
\Phi_j(\xi,\zeta)
 =\mathbb E\,e^{-i(\xi_1L_j+\xi_2V_j+\zeta P_j)},
 \qquad \xi\in\mathbb R^2,\ \zeta\in\mathbb R.
\]
For fixed \(\zeta\), \(\Phi_j(\cdot,\zeta)\) is the Fourier transform of a complex planar density \(g_{j,\zeta}\). Disintegration gives
\[
|g_{j,\zeta}(l,v)|\leq g_j(l,v),\qquad
\|g_{j,\zeta}\|_2^2\leq M_j.
\]
Thus, by planar Plancherel and Cauchy–Schwarz,
\[
S(\zeta):=\int_{\mathbb R^2}
 |\Phi_1(\xi,\zeta)\Phi_2(\xi,\zeta)|\,d\xi
 \leq (2\pi)^2\sqrt{M_1M_2}
\quad\text{for every }\zeta.
\tag{3}
\]
This is where the two-bank independence enters: the characteristic function of the sum is the product \(\Phi_1\Phi_2\). The estimate uses no marginal cap for \(P\).

## Oscillatory kernel lemma

Fix a nonnegative smooth cutoff \(\chi\) supported on \(1/2\leq|t|\leq3\) and equal to at least one on \(1\leq|t|\leq2\). Let \(r\in(0,1]\), \(\eta>0\), \(\varepsilon\ne0\), and for the moment take a smooth compactly supported hub subdensity \(0\leq h\leq1\), \(\int h\leq1\). Put
\[
u_0(l,v)=\frac{s-v^2-\beta l^2}{2l},
\qquad
W_{r,\eta}(l,v,p)
 =\frac{\chi(l/r)e^{-\eta v^2}}{2|l|}
    h(u_0(l,v)-\varepsilon p).
\tag{4}
\]
The function \(W_{r,\eta}\) is nonnegative, integrable, and smooth with rapid decay. Its Fourier transform in \(p\) gives
\[
\widehat W_{r,\eta}(\xi,\zeta)
 =\frac{\widehat h(-\zeta/\varepsilon)}{|\varepsilon|}
 \int_{\mathbb R^2}
   \frac{\chi(l/r)e^{-\eta v^2}}{2|l|}
   e^{-i\xi_1l-i\xi_2v-i(\zeta/\varepsilon)u_0(l,v)}
 \,dl\,dv.
\tag{5}
\]

There is an absolute \(C_0\) such that, for \(|s|\geq1\), all \(\zeta\ne0\), all \(\xi,\eta,\beta,\varepsilon,r\),
\[
|\widehat W_{r,\eta}(\xi,\zeta)|
 \leq \frac{C_0|\widehat h(-\zeta/\varepsilon)|}{|\varepsilon|}
 \min\left\{\left(\frac{|\varepsilon|r}{|\zeta|}\right)^{1/2},
              \frac{|\varepsilon|r}{|\zeta|}\right\}.
\tag{6}
\]
The bound is independent of the Gaussian cutoff parameter \(\eta\).

Here are the oscillatory details. Split \(l>0\) and \(l<0\), and write \(l=\pm rt\) with \(t\in[1/2,3]\). Let \(\lambda=\zeta/(\varepsilon r)\). Fourier-expand \(e^{-\eta v^2}\) in \(v\). Its Fourier transform has \(L^1\) norm \(2\pi\), independent of \(\eta\). For each Fourier frequency \(\omega\), the full-line Fresnel integral in \(v\) has modulus at most \(C|\lambda|^{-1/2}t^{1/2}\). Its remaining phase in \(t\) is a linear function of \(t\) plus a constant multiple of \(\lambda s/t\). The linear coefficient may involve \(\beta,\xi,\omega,\lambda\), but its value never enters the estimate. The \(t\)-amplitude is a fixed smooth function supported in \([1/2,3]\), with uniformly bounded supremum and total variation. The trivial \(t\)-integral proves \(C|\lambda|^{-1/2}\). The second derivative of the nonlinear \(t\)-phase has modulus at least \(c|\lambda s|\) on this interval. Weighted second-derivative van der Corput gives a further factor \(C|\lambda s|^{-1/2}\); since \(|s|\geq1\), the resulting bound is \(C|\lambda|^{-1}\). Integrate the Fourier expansion of the Gaussian cutoff against its \(L^1\) norm and sum the two signs of \(l\). This proves (6), including both signs of \(s,\varepsilon\).

## Density proof and rough hub laws

Because \(H\) is independent of the light variables, conditioning on \(L,V,P\) gives the density formula for \(L\ne0\):
\[
p_Q(s)=
\mathbb E\left[\frac{1}{2|L|}
 h\!\left(\frac{s-V^2-\beta L^2}{2L}-\varepsilon P\right)\right].
\tag{7}
\]
The planar bank assumptions ensure \(L\) has no atom at zero. On \(|L|\geq1\), (7) is at most \(1/2\).

On \(r\leq|L|\leq2r\), (7) is bounded by \(\mathbb E W_{r,\eta}(L,V,P)\) after passing \(\eta\downarrow0\). For each \(\eta>0\), ordinary Fourier inversion applies to the smooth rapidly decaying \(W_{r,\eta}\). Independence of the two banks gives
\[
\mathbb E W_{r,\eta}(L,V,P)
 \leq (2\pi)^{-3}\int_{\mathbb R}
      \sup_{\xi\in\mathbb R^2}
          |\widehat W_{r,\eta}(\xi,\zeta)|
      S(\zeta)\,d\zeta.
\tag{8}
\]
The integral is finite by (3), (6), and the following hub Fourier estimate. Substitute \(u=\zeta/\varepsilon\) in (8). The factor \(|\varepsilon|^{-1}\) cancels exactly, leaving
\[
C\sqrt{M_1M_2}\int_{\mathbb R}
 |\widehat h(u)|
 \min\left\{\sqrt{\frac r{|u|}},\,\frac r{|u|}\right\}\,du.
\tag{9}
\]
For \(|u|\leq1\), \(|\widehat h(u)|\leq\|h\|_1\leq1\). For \(|u|>1\), Plancherel and \(h\leq1,\ \int h\leq1\) give \(\|\widehat h\|_2\leq\sqrt{2\pi}\). Split the integral at \(|u|=r\) and \(|u|=1\):
\[
\int_{|u|\leq r}\sqrt{r/|u|}\,du=O(r),\quad
\int_{r<|u|\leq1}r/|u|\,du=O(r\log(1/r)),\quad
\int_{|u|>1}|\widehat h(u)|r/|u|\,du=O(r).
\]
Consequently each dyadic contribution is at most
\[
C\sqrt{M_1M_2}\,r(1+\log(1/r)).
\tag{10}
\]
The sum over \(r=2^{-k}\), \(k\geq1\), is finite. Together with the \(|L|\geq1\) contribution this proves (2) for smooth compact hub subdensities.

For a general rough cap-one hub density \(f_H\), take \(h_k=\rho_{1/k}*(f_H\mathbf1_{[-k,k]})\), where \(\rho_{1/k}\) is a nonnegative smooth compact approximate identity. Then \(0\leq h_k\leq1\), \(\int h_k\leq1\), each \(h_k\) is smooth compact, and \(h_k\to f_H\) in \(L^1\). The associated subprobability pushforwards converge in total variation because the difference of their input measures has total variation at most \(\|h_k-f_H\|_1\). A uniform density bound passes to the limiting measure. This proves (2) as an essential bound for every permitted \(f_H\).

## Product-source bank partition

There is a direct way to obtain the planar bank hypothesis from a diffuse two-dimensional original-product frame. Let \(w_i\in\mathbb R^2\) be the coefficient row of original light coordinate \(X_i\) in \((L,V)\), with
\[
\sum_i w_iw_i^{\mathsf T}=I_2,
\qquad
\max_i\|w_i\|^2\leq1/144.
\tag{11}
\]
Assign independent random signs \(\epsilon_i\in\{-1,1\}\), and put
\(S=\sum_i\epsilon_iw_iw_i^{\mathsf T}\). The exact second-moment identity is
\[
\mathbb E\|S\|_F^2
 =\sum_i\|w_i\|^4
 \leq \frac{2}{144}=\frac1{72}.
\]
Hence some sign choice has \(\|S\|_{\mathrm{op}}\leq1/\sqrt{72}\). Its two banks have
\[
G_1=\frac{I_2+S}{2},\qquad G_2=\frac{I_2-S}{2},
\qquad G_j\succeq c_0I_2,\quad
c_0:=\frac{1-1/\sqrt{72}}2>0.44.
\]
For each bank, whitening its planar projection gives an orthonormal two-dimensional projection of independent cap-one original variables. The standard planar product-projection density cap \(2\), used elsewhere in this programme, gives
\[
M_j\leq 2/\sqrt{\det G_j}\leq 2/c_0<4.55.
\tag{12}
\]
The same argument works for a \(d\)-dimensional Parseval frame with row leverage at most \(\kappa\): some sign partition has both bank Grams at least \((1-\sqrt{d\kappa})I_d/2\), when \(d\kappa<1\).

The \(P\) coefficient rows can be distributed to the same banks arbitrarily; no restriction on their size or overlap with \(w_i\) is imposed. Hence (2) applies to this diffuse planar product configuration.

## Exact limit

The second \(t\)-oscillation in (6) comes from the term \(s/l\). As \(s\to0\), the van der Corput factor becomes \(|\lambda s|^{-1/2}\), and at \(s=0\) only the Fresnel \(|\lambda|^{-1/2}\) bound remains. In (9) that leaves a high-frequency integral with weight \(|u|^{-1/2}\), which is at the divergent endpoint for an arbitrary \(L^2\) hub characteristic function. Thus this argument gives no uniform bound for \(|s|<1\). Adding a small physical hub-square term \(aH^2\) also changes the Fourier-p factor and is not covered. These are genuine scope limits of the theorem, not a density counterexample.

The bank partition is only guaranteed under (11), or an equivalent quantitative planar-bank split. The report does not assert such a split for every exact-rank-three matrix with small cross-volume. The full QFORM conjecture remains open.
