# account03/B18 r31 early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

I am attacking the exact-rank-three null-hub heavy-anchor survivor left after account04/B18 r4. Its normal form is

\[
Q=2(X_0+\ell\cdot X_L)(g\cdot X_L)+d(\beta\cdot X_L)^2,
\qquad \|\beta\|_2=1,\quad \beta\cdot g=0,
\]
with \(\gamma=\|g\|_2\), and heavy score
\[
q_i=\beta_i^2+g_i^2/\gamma^2>1/2.
\]
The partner has already paid the N3(1/64) subbranch \(|g_i|\ge1/64\), with
\[
\|p_Q\|_\infty<64.1795826152.
\]
The live survivor therefore has a heavy anchor with \(|g_i|<1/64\).

## New primary-source transfer: the residual pair has an exact cap

Put \(\alpha_i=g_i/\gamma\), delete coordinate \(i\), and consider the two linear aggregates
\[
C_i=\left(\beta_-\cdot X_-,\;\frac{g_-}{\gamma}\cdot X_-\right).
\]
Their coefficient Gram matrix is exactly
\[
G_i=
\begin{pmatrix}
1-\beta_i^2&-\alpha_i\beta_i\\
-\alpha_i\beta_i&1-\alpha_i^2
\end{pmatrix}.
\]
Because \(\beta\cdot g=0\), direct calculation gives
\[
\det G_i=1-\alpha_i^2-\beta_i^2=1-q_i,
\qquad \operatorname{spec}(G_i)=\{1,1-q_i\}.
\]
If \(q_i<1\), whiten the coefficient rows by \(G_i^{-1/2}\). This is a genuine two-dimensional orthogonal projection of the ORIGINAL product block \(X_-\). Theorem 1.1 of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), gives density cap 2 for that whitened projection. Undoing the deterministic two-dimensional linear map therefore gives
\[
\boxed{\ \|p_{C_i}\|_\infty\le \frac{2}{\sqrt{1-q_i}}.\ }
\]
Equivalently,
\[
\boxed{\ \left\|p_{(\beta_-\cdot X_-,\,g_-\cdot X_-)}\right\|_\infty
\le \frac{2}{\gamma\sqrt{1-q_i}}.\ }
\]
No independence of the two projected coordinates is claimed.

Choosing the quantitative split \(q_i\le3/4\) gives the dimension-free cap \(\|p_{C_i}\|_\infty\le4\). If \(q_i>3/4\), the residual transverse covariance has eigenvalues \(1\) and \(1-q_i<1/4\): the survivor is an explicit near-coloop collar rather than an arbitrary heavy-row state.

Thus, after the completed account04/B18 r4 payment, the N3 null-hub heavy state reduces to: (A) paid moderate edge \(|g_i|\ge1/64\); (B) tiny edge plus a residual dependent pair of joint density cap at most 4; or (C) tiny edge plus a quantitatively near-coloop transverse frame \(q_i>3/4\). The missing step is a curved-kernel estimate in branch (B), or a near-coloop compiler in branch (C); a joint-density cap alone is not being treated as sufficient.

Latest-Claude side gate to retain in the full-matrix extension: the volume-stability theorem at scale \(a=1/64\) gives a continuous density bound \(<23/a=1472\) whenever a rank-three original-coordinate cross core \(M_0\) has \(s_3(M_0)\ge1/64\), range leverage at most 1/2, and perturbation norm at most \(1/1024\). Hence the still-unpaid full-matrix continuation must fail that gate as well.
