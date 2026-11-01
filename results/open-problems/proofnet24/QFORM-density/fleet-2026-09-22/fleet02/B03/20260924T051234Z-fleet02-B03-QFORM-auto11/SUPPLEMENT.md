# Supplement — exact r49 beta sharpens the C5 partner application

The main report's `8 sqrt(2)` bound for the `C5` stress used only the coarse r49 specialization `q>=1/2, |beta|>=s`. It is valid, but the exact residual geometry gives a stronger partner application.

For the Schur residual

\[
S=\begin{pmatrix}
0&1&-1\\
1&0&1\\
-1&1&0
\end{pmatrix},
\]

take the first physical residual coordinate as the null pivot. In r49 notation `q=1`, `M=S`, and

\[
|\beta|^2=\|Me_1\|_2^2=2,
\qquad |\beta|=\sqrt2.
\]

Therefore the exact r49 Theorem 4.1 gives

\[
H_{1/2}(R)
\le 2^{11/4}|\beta|^{-1/2}
=2^{11/4}2^{-1/4}
=2^{5/2}=4\sqrt2.
\]

The outer physical edge has `mu=1`, so r49's hyperbola transducer yields

\[
\boxed{\|p_{X^T A_5X}\|_{\infty,\mathrm{ess}}\le\sqrt2(4\sqrt2)=8.}
\]

Consequently

\[
\boxed{
\int_{\mathbb R}|t|^{-1/2}|\phi_{A_5}(t)|^2dt
\le4\sqrt{8\pi}=8\sqrt{2\pi}
=20.0530261970\ldots .}
\]

Thus the newest fleet03/B03 r49 route is actually numerically stronger on `C5` than the independent pinned-Theorem-A plus `L^3` route `(432 sqrt(pi))^(1/3)=9.14856...`. The latter remains useful because it is an equation-level application of the required pinned `e5f71d79...` source and because `QFORM-HYPERBOLA-PAID-RESIDUAL-L3-v1` applies to any already-paid residual density, not only the r49 null-pivot class.

No theorem statement in the main report is invalidated; this supplement only sharpens the concrete `C5` constants and corrects the comparison language.
