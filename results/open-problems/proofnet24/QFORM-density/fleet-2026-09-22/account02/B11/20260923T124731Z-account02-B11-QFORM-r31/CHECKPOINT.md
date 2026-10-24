# QFORM B11 r31 — first substantive checkpoint

Status: supporting calculation, not the full conjecture.

## First unpaid implication

After the completed account03/B11 r29/r30 two-bank analysis, the exact cross-rank-one null endpoint has (up to the sign-dual relabelling) spectral matrix

\[
M=\begin{pmatrix}\beta&0&\gamma\\0&0&\alpha\\\gamma&\alpha&\delta\end{pmatrix},
\qquad \sigma_{\min}(M)\ge s>0,
\]

and disjoint original-coordinate banks with spectral rows

\[
r_i=(a_i,b_i,0),\ i\in S,\qquad r_j=(0,d_j,c_j),\ j\in T,
\]

such that

\[
\sum_{i\in S}r_i r_i^T=\operatorname{diag}(1,\rho,0),\qquad
\sum_{j\in T}r_j r_j^T=\operatorname{diag}(0,1-\rho,1).
\]

The unpaid task is to use this ORIGINAL-product provenance, not merely the two planar joint-density caps (which partner r30 refuted as sufficient).

## Spectral noncollapse at the null endpoint

Directly,

\[
\det M=-\beta\alpha^2,
\]

and

\[
M^{-1}=\begin{pmatrix}
\beta^{-1}&-\gamma/(\alpha\beta)&0\\
-\gamma/(\alpha\beta)&(\gamma^2-\beta\delta)/(\alpha^2\beta)&\alpha^{-1}\\
0&\alpha^{-1}&0
\end{pmatrix}.
\]

Hence \(\|M^{-1}\|_{op}\le s^{-1}\) implies the two coefficients that matter at the null endpoint do not collapse:

\[
|\beta|\ge s,\qquad |\alpha|\ge s.
\]

Moreover \(\beta>0\) forces signature \((+,+,-)\), while \(\beta<0\) forces \((+,-,-)\): use \(\det M=-\beta\alpha^2\) and the Rayleigh value \(e_1^TMe_1=\beta\) to exclude the definite alternative.

The determinant-one shears

\[
H=Z+(\gamma/\alpha)U,\qquad L=W+(\delta/(2\alpha))V
\]

put the form exactly into

\[
Q=\beta U^2+2\alpha V(H+L),
\]

while preserving the source-plane areas: the left coefficient frame \((a_i,b_i+(\gamma/\alpha)a_i)\) has Gram determinant \(\rho\), and the right frame \((c_j,d_j+(\delta/(2\alpha))c_j)\) has Gram determinant \(1-\rho\). This explains why partner r30's anisotropic planar-cap counterexample cannot be imported merely by making the physical third coefficient tiny: target-scale spectral conditioning already forces \(|\alpha|,|\beta|\ge s\).

## New one-sided product-provenance compiler (calculation)

More generally let \(U=a\cdot X_S\), \(H=h\cdot X_S\), \(V=c\cdot X_T\), with \(S,T\) disjoint original-coordinate banks and \(C=\|c\|_2>0\). Consider

\[
Q=\beta U^2+2\alpha V H+R_T(X_T)+\sum_{i\in S}q_i(X_i),
\]

where \(R_T\) is arbitrary measurable and each \(q_i\) is an arbitrary real one-coordinate phase (in particular arbitrary diagonal quadratic and affine twists are allowed). Let \(I\subseteq S\), let \(v_i=(a_i,h_i)\), and put \(G_I=\sum_{i\in I}v_i v_i^T\). Assume \(G_I>0\) and

\[
v_i^T G_I^{-1}v_i\le\frac12\quad(i\in I).
\]

Then the following bound should hold, and the full derivation is being checked next:

\[
\boxed{\ \|p_Q\|_\infty
\le 3\,2^{5/3}
|\beta|^{-1/3}(|\alpha|C)^{-2/3}\det(G_I)^{-1/3}.\ }
\]

Sketch with constants. Fresnel-linearise \(e^{it\beta U^2}\), condition on the right bank, drop the arbitrary right-bank phase, and use the Rogozin--Ball scalar projection bound \(\|p_V\|_\infty\le\sqrt2/C\). The change of variable \(y=2\alpha tV\) contributes \(\sqrt2/(2|\alpha t|C)\). On the remaining two Fourier variables, geometric Brascamp--Lieb plus the pinned Claude Lemma 1

\[
\int |\widehat f_i|^p\le 4\pi/\sqrt p,\qquad p\ge2,
\]

gives

\[
\int_{\mathbb R^2}\prod_{i\in I}|\widehat f_i(a_i\xi+h_i y)|\,d\xi\,dy
\le(4\pi)^2\det(G_I)^{-1/2}.
\]

Thus

\[
|\phi_Q(t)|\le\min\{1,K|t|^{-3/2}\},\quad
K=4\sqrt2\,\pi^{3/2}|\beta|^{-1/2}(|\alpha|C)^{-1}\det(G_I)^{-1/2}.
\]

Since \((2\pi)^{-1}\int_{\mathbb R}\min(1,K|t|^{-3/2})dt=3K^{2/3}/\pi\), the displayed density bound follows.

For the exact null endpoint, if the whole square-side planar frame has normalized planar leverages at most \(1/2\), then \(C=1\), \(\det G_S=\rho\), and \(|\alpha|,|\beta|\ge s\), so

\[
\|p_Q\|_\infty\le 3\,2^{5/3}\rho^{-1/3}s^{-1}.
\]

At the partner scale \(\rho\ge1/1024\), this is exactly \(\le96/s\). This already allows arbitrary leverage on the right bank and arbitrary right-bank self curvature, so it is not the same as the all-three-mode low-leverage Fresnel theorem.

The remaining chamber is therefore a heavy normalized leverage coordinate on the square-side planar bank. The next step is to isolate its physical-pivot exit and identify the finite shared-direction spike that remains.
