# Fixed nonzero target extension of the two-bank one-hub receiver

This note extends the source-pinned outer-target receiver
https://github.com/yspennstate/math-open-problems/blob/f0d3e4df297cf45c4f8a0298051cef186faf1de4/proofnet24/QFORM-density/interactive/20260923T203000Z-two-bank-outer-density/REPORT.md .
It does **not** remove the loss as the negative target approaches zero, and it is not a full proof of the density conjecture.

Let \(H\) have any density \(f_H\leq1\), independent of \(Y=Y_A+Y_B\), where \(Y_A,Y_B\) are independent \((L,V,P)\)-valued banks. Assume each bank's planar \((L,V)\) density is bounded by \(M_A,M_B\). There is no moment or support assumption and no restriction on the dependence of \(P\) on \((L,V)\) within a bank. For
\[
Q=2HL+\beta L^2+V^2+2\varepsilon LP,
\]
with \(\varepsilon\ne0\), the output density satisfies, for almost every \(s\ne0\),
\[
p_Q(s)\leq\frac12+
 C\sqrt{M_A M_B}\left(1+\sqrt{\log_+\frac1{|s|}}\right).
\]
Here \(C\) is an absolute constant; in particular the bound is uniform in \(\varepsilon\) and \(\beta\). The \(|L|>1\) contribution is at most \(1/2\). For \(|s|\geq1\), this recovers the earlier outer-target theorem. At \(\varepsilon=0\), the separate two-light coarea argument controls all \(s\).

## Dyadic kernel

Fix dyadic \(r=2^{-j}\), \(j\geq1\), and set \(\chi_r(l)=\mathbf1_{\{r\leq|l|<2r\}}\). These cutoffs partition \(0<|l|<1\). On either sign interval the amplitude \(\chi_r(l)/\sqrt{|l|}\) has bounded variation \(O(r^{-1/2})\), which is enough for the second-derivative van der Corput lemma. After integrating \(H\), the kernel at output target \(s\) is
\[
W_{r,s}(l,v,p)
 =\frac{\chi_r(l)}{2|l|}
 f_H\!\left(\frac{s-v^2-\beta l^2}{2l}-\varepsilon p\right).
\]
Initially take \(f_H\) smooth and compactly supported and the bank densities smooth Schwartz. Regard \(W_{r,s}\) as a tempered distribution. Fourier transformation first in \(p\), then the exact Fresnel transform in \(v\), gives (up to harmless signs and constants)
\[
\widehat W_{r,s}(\xi_L,\xi_V,\varepsilon\eta)
 =\frac{\phi_H(\eta)}{|\varepsilon|\sqrt{|\eta|}}
 \int \frac{\chi_r(l)}{\sqrt{|l|}}\,
 \exp i\left\{
 \frac{\eta s}{2l}
 +l\left(\frac{\xi_V^2}{2\eta}
       -\frac{\beta\eta}{2}
       -\xi_L\right)\right\}\,dl .
\]
The linear-in-\(l\) coefficient, including the \(\xi_V^2/(2\eta)\) term, has zero second derivative. Taking the absolute value of the \(l\)-integral gives the elementary Fresnel estimate; applying the second-derivative van der Corput lemma to the phase \(\eta s/(2l)\) gives
\[
\tag{1}
\sup_{\xi_L,\xi_V}
|\widehat W_{r,s}(\xi_L,\xi_V,\varepsilon\eta)|
 \leq
 \frac{C|\phi_H(\eta)|}{|\varepsilon|}
 \min\left\{\sqrt{\frac r{|\eta|}},
             \frac r{\sqrt{|s|}\,|\eta|}\right\}.
\]
Both signs of \(l\) are treated separately. All estimates are uniform in \(\beta\), because its phase contribution is linear in \(l\). The kernel is locally integrable in Fourier variables at \(\eta=0\), so there is no omitted delta mass.

## Bank factor and summation

Writing \(g_A,g_B\) for bank densities, set
\[
S(\zeta)=\int_{\mathbb R^2}
  |\widehat g_A(\xi,\zeta)\widehat g_B(\xi,\zeta)|\,d\xi .
\]
Planar Plancherel and Cauchy--Schwarz yield
\[
\tag{2} S(\zeta)\leq (2\pi)^2\sqrt{M_A M_B}
\]
for every \(\zeta\); multiplication by \(e^{i\zeta P}\) only changes the complex phase of each planar bank density. Fourier inversion, (1), and the substitution \(\zeta=\varepsilon\eta\) therefore bound the dyadic contribution by
\[
D_r(s)\leq C\sqrt{M_A M_B}
 \int_{\mathbb R}|\phi_H(\eta)|
 \min\left\{\sqrt{\frac r{|\eta|}},
             \frac r{\sqrt{\gamma}\,|\eta|}\right\}d\eta,
\qquad \gamma=|s|.
\]
Use \(|\phi_H|\leq1\) and \(\int|\phi_H|^2=2\pi\int f_H^2\leq2\pi\).

For \(0<\gamma<1\), split the \(\eta\)-integral at \(1\) and \(r/\gamma\). If \(r\geq\gamma\), the ranges \((0,1)\), \((1,r/\gamma)\), and \((r/\gamma,\infty)\) give respectively
\[
D_r(s)\leq C\sqrt{M_A M_B}\,\sqrt r
 \left(1+\sqrt{\log(r/\gamma)}\right).
\]
If \(r\leq\gamma\), the ranges \((0,r/\gamma)\), \((r/\gamma,1)\), and \((1,\infty)\) give
\[
D_r(s)\leq C\sqrt{M_A M_B}\,
 \frac r{\sqrt\gamma}\left(1+\log(\gamma/r)\right).
\]
The geometric dyadic sums over \(r\geq\gamma\) and \(r\leq\gamma\) are bounded by \(C(1+\sqrt{\log(1/\gamma)})\). For \(\gamma\geq1\), only the second pattern occurs and the sum is bounded by an absolute constant.

For rough \(f_H\leq1\), truncate it and convolve with a nonnegative smooth probability mollifier; its cap remains one and its mass tends to one. A bank need not have a full three-dimensional density: convolve its probability law in \(\mathbb R^3\) with a smooth compact probability mollifier and then truncate by a cutoff at most one. Its planar \((L,V)\) density cap is preserved under convolution and truncation, and the resulting smooth compact bank sublaw has mass tending to one. Apply the estimate to these approximants and pass to weak limits of their \(Q\)-laws. On each interval avoiding zero, the variable bound displayed above is bounded and continuous in the target up to a harmless fixed majorant; the corresponding interval-probability bound passes to the limit. This justifies the a.e. density statement without assumptions on supports, moments, full bank densities, or density regularity.

**Remaining gap.** The bound grows like \(\sqrt{\log(1/|s|)}\) as \(s\to0\), while, in the original-product light setting with its additional all-plane projection caps and full three-dimensional bank caps, the positive/zero-target ruled-line receiver and a separate continuity estimate cover \(s\geq-|\,\varepsilon\,|\). The unresolved region for arbitrary rough hubs and overlapping original-product \(P\) is \(|\varepsilon|\ll -s\ll1\). Projection caps alone cannot settle it: a dependent-light fake has unbounded negative-target density despite all-plane projection caps.
