# A dimension-free exact-rank-three theorem for diffuse spectral frames

**Status:** Rigorous conditional theorem, valid for arbitrary affine terms and all three-eigenvalue signatures. The diffuse-frame hypothesis and exact-rank-three assumption are essential to the present proof; the unrestricted conjecture remains open.

## Theorem

Let (X_1,\ldots,X_n) be independent real random variables with probability densities (f_i\le1). Let
\[
 A=U\Lambda U^T,\qquad U^TU=I_3,\qquad
 \Lambda=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3),\quad
 |\lambda_j|\ge\sigma>0,
\]
be a symmetric matrix of **exact rank three**. Write (u_i^T) for row (i) of (U), and suppose
\[
 \delta:=\max_i\|u_i\|^2\le\frac1{12}.
\]
Then for all (b\in\mathbb R^n) and (c\in\mathbb R), (Q=X^TAX+b^TX+c) has a bounded continuous density and
\[
 \|p_Q\|_\infty\le \frac{24}{\sigma}.
\]
This includes arbitrary (b) in the null space of (A). No sign condition on (A) is imposed.

More generally, if the original coordinates admit a partition (S\sqcup T=[n]) such that
\[
 G_S=U_S^TU_S\succeq c_0 I_3,\qquad
 G_T=U_T^TU_T\succeq c_0 I_3
\]
for some (c_0>0), then (\|p_Q\|_\infty\le6/(c_0\sigma)).

## A balanced partition for small row leverage

Choose independent random signs (\varepsilon_i\in\{-1,1\}), set
(H=\sum_i\varepsilon_i u_i u_i^T), and let (S=\{i:\varepsilon_i=1\}), (T=S^c). Then
\[
 \mathbb E\|H\|_F^2
 =\sum_i\|u_i u_i^T\|_F^2
 =\sum_i\|u_i\|^4
 \le\delta\sum_i\|u_i\|^2
 =3\delta\le\frac14.
\]
Thus at least one signing has (\|H\|_F\le1/2). For that signing,
\[
 G_S=\tfrac12(I_3+H)\succeq\tfrac14 I_3,\qquad
 G_T=\tfrac12(I_3-H)\succeq\tfrac14 I_3.
\]
This is a deterministic existence proof; it uses only (U^TU=I_3).

## Three-dimensional bilinear Fourier bound

Fix any partition with (G_S,G_T\succeq c_0I_3). The random vectors
\[
 Z=U_S^TX_S\in\mathbb R^3,\qquad W=U_T^TX_T\in\mathbb R^3
\]
are independent. Whitening (Z) by (G_S^{-1/2}) turns it into an orthogonal three-dimensional projection of a product cap-one measure. The LPP orthogonal-projection density estimate gives
\[
 \|p_Z\|_\infty\le\frac{2^{3/2}}{\sqrt{\det G_S}}
 \le 2^{3/2}c_0^{-3/2},\qquad
 \|p_W\|_\infty\le2^{3/2}c_0^{-3/2}. \tag{1}
\]
In particular both projected densities are in (L^1\cap L^2).

Expand (Q) as
\[
 Q=q_S(X_S)+q_T(X_T)+2Z^T\Lambda W+c,
\]
where (q_S=z^T\Lambda z+b_S^TX_S) and (q_T=w^T\Lambda w+b_T^TX_T). Importantly, the affine terms may depend on original coordinates outside the spectral projection. For every real (t), define complex integrable amplitudes by
\[
 \alpha_t(z)=p_Z(z)\mathbb E[e^{itq_S(X_S)}\mid Z=z],\qquad
 \beta_t(w)=p_W(w)\mathbb E[e^{itq_T(X_T)}\mid W=w].
\]
Measurable versions exist by disintegration, and
\[
 |\alpha_t(z)|\le p_Z(z),\quad |\beta_t(w)|\le p_W(w),\qquad
 \|\alpha_t\|_2\|\beta_t\|_2
 \le\sqrt{\|p_Z\|_\infty\|p_W\|_\infty}
 \le2^{3/2}c_0^{-3/2}. \tag{2}
\]
Independence between the banks, followed by Cauchy–Schwarz and three-dimensional Plancherel, yields for (t\ne0),
\[
\begin{split}
 |\varphi_Q(t)|
 &\le\left|\int_{\mathbb R^3}\!\int_{\mathbb R^3}
 \alpha_t(z)\beta_t(w)e^{2it z^T\Lambda w}\,dw\,dz\right|\\
 &\le\frac{(2\pi)^{3/2}}{(2|t|)^{3/2}\sqrt{|\det\Lambda|}}
 \|\alpha_t\|_2\|\beta_t\|_2\\
 &\le \frac{(2\pi)^{3/2}}{(c_0\sigma|t|)^{3/2}}.
\end{split} \tag{3}
\]
The harmless global phase (e^{itc}) is suppressed. Equation (3) needs neither (q_S) nor (q_T) to depend only on (Z,W); that is why arbitrary null-space affine terms cause no difficulty.

Combine (3) with ( |\varphi_Q(t)|\le1). Taking (T_0=2\pi/(c_0\sigma)), Fourier inversion applies because
\[
\begin{split}
 \|p_Q\|_\infty
 &\le\frac1{2\pi}\int_{\mathbb R}\min\{1,(T_0/|t|)^{3/2}\}\,dt\\
 &=\frac{3T_0}{\pi}
 =\frac6{c_0\sigma}.
\end{split}
\]
The (L^1) characteristic function also gives a bounded continuous representative of the density. Set (c_0=1/4).

## Scope / unresolved structural step

The hypothesis (\max_i\|u_i\|^2\le1/12) excludes spectral coloops and high-leverage original coordinates. If (A) has additional nonzero eigenvalues, their cross-bank term is generally not a function of only ((Z,W)) and cannot be absorbed into the separate amplitudes. Proving a universal bound for high-leverage exact-rank-three frames or higher-rank indefinite matrices needs another argument. This theorem is compatible with the separate arbitrary-affine (O(n/\sigma)) physical-triple bound.
