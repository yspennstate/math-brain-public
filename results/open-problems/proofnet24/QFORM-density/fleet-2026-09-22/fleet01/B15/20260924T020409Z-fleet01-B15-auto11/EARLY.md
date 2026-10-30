# Early substantive calculation: the partner semidefinite rank-two constant 2pi is sharp

Programme `QFORM-DENSITY-3EIG-20260922`; run `20260924T020409Z-fleet01-B15-auto11`. Full QFORM remains OPEN.

Let `X1,X2,X3,X4` be independent `Unif[-1/2,1/2]`, and set

\[
Y_1=(X_1+X_2)/\sqrt2,\qquad Y_2=(X_3+X_4)/\sqrt2,
\qquad R=Y_1^2+Y_2^2.
\]

The matrix of `R` in the original independent coordinates is

\[
S_0={1\over2}\begin{pmatrix}1&1\\1&1\end{pmatrix}
\oplus {1\over2}\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

so `S0` is positive semidefinite of rank two and its nonzero eigenvalues are both one (`P=1`). The latest completed designated-partner theorem fleet02/B15 therefore gives the actual inequality

\[
\|p_R\|_\infty\le2\pi.
\]

Here the inequality is sharp. The density of each `Y_j` is

\[
g(y)=\sqrt2(1-\sqrt2|y|)\mathbf1_{|y|\le1/\sqrt2}.
\]

For `0<t<1/2`, the circle of radius `sqrt(t)` stays inside this support in both coordinates, and polar coarea gives

\[
p_R(t)={1\over2}\int_0^{2\pi}
 g(\sqrt t\cos\theta)g(\sqrt t\sin\theta)\,d\theta.
\]

Using

\[
\int_0^{2\pi}(|\cos\theta|+|\sin\theta|)d\theta=8,
\qquad
\int_0^{2\pi}|\sin\theta\cos\theta|d\theta=2,
\]

one obtains exactly

\[
\boxed{p_R(t)=2\pi-8\sqrt{2t}+4t,\qquad0<t<1/2.}
\]

Hence

\[
\boxed{\|p_R\|_{\infty,\mathrm{ess}}=2\pi,}
\]

so the partner constant `2pi/sqrt(P)` cannot be improved in the general rank-two semidefinite product class. Moreover `p_R=0` almost everywhere on `(-infty,0)`, while `p_R(t)\to2pi` as `t downarrow0`; therefore the law has no continuous density representative. This is a sharp bounded-but-not-continuous endpoint, not a counterexample to the rank-at-least-three target.

Next step in this run: add an independent nonconstant quadratic block and prove a same-height `C0` convolution compiler with an explicit modulus. For a square remainder from a fifth cap-one uniform coordinate, compute the resulting target-valid boundary cusp exactly.
