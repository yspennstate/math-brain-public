# Early checkpoint — Gaussian-mixture variation barrier for fragmented cap-one laws

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260923T183045Z-account02-B14-QFORM-auto11
Status: proved supporting obstruction; full QFORM remains open.

Let
\[
E_N=\bigcup_{j=1}^N[4j,4j+N^{-1}],\qquad f_N=\mathbf 1_{E_N}.
\]
This is the latest designated partner account03/B14 finite-fragment law, of total mass one and density cap one.

Suppose a probability density g is a Gaussian location-scale mixture
\[
g(x)=\mathbb E\,\varphi_{T}(x-M),\qquad
\varphi_T(u)=(2\pi T)^{-1/2}e^{-u^2/(2T)},
\]
with H=E T^{-1/2}<\infty. Then g is BV and
\[
\operatorname{Var}(g)\le \mathbb E\|\varphi_T'\|_1
=\sqrt{2/\pi}\,H.
\tag{1}
\]
Indeed \(\|\varphi_T'\|_1=\sqrt{2/\pi}\,T^{-1/2}\), and distributional differentiation plus Tonelli gives (1).

Since \(f_N\) is the indicator of N disjoint compact intervals,
\[
\operatorname{Var}(f_N)=2N.
\]
Consequently any exact Gaussian-mixture representation of \(f_N\) satisfies
\[
\boxed{\mathbb E T^{-1/2}\ge N\sqrt{2\pi}.}
\tag{2}
\]
In particular the checked full-matrix Gaussian-mixture QFORM theorem, whose hypothesis is \(E T^{-1/2}\le\sqrt{2\pi}\) coordinatewise, cannot contain any \(f_N\) with \(N\ge2\), despite \(f_N\le1\).

There is also a quantitative approximation obstruction. Choose a compact piecewise-C1 test \(\psi_N\), \(|\psi_N|\le1\), which rises linearly from -1 to +1 on each component of \(E_N\), falls back from +1 to -1 across each gap, and tapers outside; then \(\|\psi_N'\|_\infty\le2N\) and
\[
\int f_N\psi_N'=2N.
\]
For every BV density g,
\[
\operatorname{Var}(g)\ge\left|\int g\psi_N'\right|
\ge 2N-2N\|g-f_N\|_1.
\]
Combining with (1),
\[
\boxed{
H\ge N\sqrt{2\pi}\,(1-\|g-f_N\|_1).
}
\tag{3}
\]
Thus under the mixture-theorem budget \(H\le\sqrt{2\pi}\),
\[
\boxed{\|g-f_N\|_1\ge1-1/N.}
\tag{4}
\]
So the full Gaussian-mixture theorem cannot be extended to arbitrary rough cap-one laws by a uniform inverse-scale-budget approximation argument: even the compact finite-fragment extreme class is separated from that mixture class by order-one L1 distance as N grows.

This is a proof-interface obstruction, not a QFORM counterexample. A target-valid control will be added in the final report using a completed source theorem from math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837.
