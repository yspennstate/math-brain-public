# All-beta finite-P support density addendum

Date: 2026-09-23. Status: **proved scoped theorem**. This extends the [finite-P Fourier receiver](https://github.com/yspennstate/math-open-problems/blob/44cd716d0814a830c27feeba380a03f62da38c6b/proofnet24/QFORM-density/interactive/20260923T205630Z-finite-p-support-fourier/REPORT.md) from beta zero to arbitrary beta for the pure canonical quadratic law. The unrestricted original-product theorem remains open.

## Theorem

Let H have an independent probability density bounded by one. Let A=(L_A,V_A,P_A) and B=(L_B,V_B,P_B) be independent random vectors with probability densities a,b bounded by M_A,M_B. Suppose P_A and P_B belong almost surely to arbitrary measurable sets E_A,E_B of finite Lebesgue measures R_A,R_B. The sets can be unbounded and fragmented. Put (L,V,P)=A+B. For every real beta and epsilon,

\[
Q=2HL+\beta L^2+V^2+2\varepsilon LP
\]

has an essentially bounded density, uniformly over all the stated data, with

\[
\boxed{\quad
\|p_Q\|_\infty\le 3\,2^{2/3}
(R_A R_B M_A M_B)^{1/3}.
\quad}
\]

This also applies when each bank vector is a linear projection of genuine independent original coordinates. The extra finite-measure P-support condition is not automatic in the full RMT/QFORM problem.

## The slice-cap input

Let F=a*b be the density of (L,V,P), and F_p(l,v)=F(l,v,p). Write

\[
m(p)=\int_{\mathbb R^2}F_p(l,v)\,dl\,dv,
\qquad
M(p)=(2\pi)^{-2}\int_{\mathbb R^2}|\widehat{F_p}(\xi)|\,d\xi.
\]

The planar Fourier transform convention is \(\widehat g(\xi)=\int e^{-i\xi\cdot x}g(x)\,dx\). The finite-P slice Wiener argument in the linked report proves

\[
\int m(p)\,dp=1,\qquad
\int M(p)\,dp
\le\sqrt{R_A R_B M_A M_B}<\infty.
\tag{1}
\]

In particular, planar Fourier inversion gives \(0\le F_p(l,v)\le M(p)\) for almost every \((p,l,v)\). At almost every p, F_p is a nonnegative planar subprobability density of mass m(p).

## Beta-uniform coarea bound for a planar subprobability

Let g(l,v) be any nonnegative planar density of mass m and cap M. Let H be independent with density at most one. For any real beta,c and any R>0, the output

\[
2HL+\beta L^2+V^2+2cL
\]

formed with the subprobability measure g has density bounded almost everywhere by

\[
\frac{m}{2R}+4\sqrt2\,M\sqrt R.
\tag{2}
\]

Indeed, on \(|l|>R\), conditioning on (l,v) and changing the h variable costs at most \(m/(2R)\). On \(0<|l|\le R\), change the v variable through the square map. Its two branches give
\[
\int g(l,v)\,\delta(s-2hl-\beta l^2-v^2-2cl)\,dv
\le M\,[s-2hl-\beta l^2-2cl]_+^{-1/2}.
\]
The one-sided inverse square-root bathtub bound, using only \(0\le f_H\le1\) and \(\int f_H=1\), gives
\[
\int f_H(h)[s-2hl-\beta l^2-2cl]_+^{-1/2}\,dh
\le\sqrt{2/|l|}.
\]
Integrating this over \(|l|\le R\) yields \(4\sqrt2 M\sqrt R\). This is the same calculation as in the [beta-uniform one-hub two-light theorem](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T203100Z-beta-uniform-one-hub-square/REPORT.md), with arbitrary split R and subprobability mass retained. For zero or infinite M the bound follows by limiting arguments; in the present application M(p) is finite almost everywhere.

## Proof of the theorem

Condition on P=p. Since H is independent of the entire light vector, H+epsilon p is still a cap-one hub. Apply (2) to g=F_p with c=epsilon p. Then integrate the resulting nonnegative output sublaws over p. Equations (1) and (2) give, for every R>0,

\[
\|p_Q\|_\infty
\le \frac{1}{2R}+4\sqrt2\,\sqrt R
\int M(p)\,dp.
\tag{3}
\]

More formally, (2) bounds the probability of every output interval by the displayed constant times its length; Tonelli then gives (3) without needing a p-independent exceptional set of output values.

Set \(W=\int M(p)dp\), which is finite and positive. The minimum of the right side of (3) occurs at \(R^{3/2}=1/(4\sqrt2 W)\), and equals \(3\,2^{2/3}W^{2/3}\). The bound in (1) finishes the proof. It is uniform in beta and epsilon. It asserts an essentially bounded density; this coarea argument does not claim a continuous version.

## Renyi-tail extension

Partition the P-axis into unit intervals I_k=[k,k+1), and write
\[
m_{A,k}=\Pr(P_A\in I_k),\qquad m_{B,j}=\Pr(P_B\in I_j).
\]
If \(\sum_k m_{A,k}^{2/3}\) and \(\sum_j m_{B,j}^{2/3}\) are finite, the same all-beta conclusion holds with
\[
\boxed{\quad
\|p_Q\|_\infty
\le 3\,2^{2/3}(M_A M_B)^{1/3}
\Big(\sum_k m_{A,k}^{2/3}\Big)
\Big(\sum_j m_{B,j}^{2/3}\Big).
\quad}
\]
To see the exponent, restrict bank A to one P-bin of mass alpha and bank B to one P-bin of mass delta. The resulting planar slice measures have total mass alpha delta. The finite-P Wiener calculation, with unit P-support measures and L2 norms of subprobability bank densities, gives \(\int M_{k,j}(p)dp\le\sqrt{M_A M_B\alpha\delta}\). Optimizing (2) after integrating p yields
\(3\,2^{2/3}(M_A M_B)^{1/3}(\alpha\delta)^{2/3}\).
The whole output measure is the positive sum over bank-bin pairs, so these bounds sum.

## Scope

This all-beta argument uses the positive square-map coarea estimate. The arbitrary bank-local phase extension in the linked beta-zero Fourier report is a **separate** result: bank-local phases can change the v-square map, so the present all-beta conclusion does not include them. Conversely, beta can be arbitrarily large here; the finite P support is imposed on the original bank P coordinates, with no beta-dependent shear. Neither bound controls arbitrary unrestricted P tails from the original conjecture.
