# fleet03/B03 r36 early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`; full target remains OPEN.  This checkpoint records the first new calculation before the longer endpoint analysis.

## Augment the r35 right-plane Fresnel integral by the genuine physical pivot

Use the exact r35/r27 packet

\[
Q=a^{-1}H^2+2\sigma UV,
\quad H=aX_i+h_L\!\cdot X_L+h_R\!\cdot X_R+h_K\!\cdot X_K,
\]
\[
U=u\cdot X_L,\quad V=v\cdot X_R,\quad h_R=\beta v+m q,
\qquad v\perp q,\ \|v\|=\|q\|=1,
\]
with the original coordinate banks disjoint and independent.  Put `L=||p_U||_infinity`; the weighted product-projection theorem gives `L<=sqrt(e)`.

The rigorous damped-Fresnel identity used in the newest Claude package and in r35 gives, for `t!=0`, after taking absolute values only after the physical product factorisation,

\[
|\phi_Q(t)|\le \sqrt{\frac{|a|}{4\pi |t|}}
\int |\chi_i(as)|\int p_U(u)
\prod_{j\in R}|\psi_j(sh_j+2t\sigma u v_j)|\,du\,ds.
\]

Here the dependence between `U` and the other left-bank linear form remains inside a complex conditional amplitude whose modulus is at most `p_U`; no conditional density cap is asserted.  Therefore `p_U<=L` and `eta=2t sigma u` give

\[
|\phi_Q(t)|\le {L\sqrt{|a|}\over 4\sqrt\pi |\sigma|}|t|^{-3/2}
\ I_{\rm aug},
\]
where
\[
I_{\rm aug}=\int_{\mathbb R^2}|\chi_i(as)|
\prod_{j\in R}|\psi_j(h_js+v_j\eta)|\,ds\,d\eta .
\]

Introduce the **augmented physical frequency rows**
\[
b_0=(a,0),\qquad b_j=(h_j,v_j)=(\beta v_j+m q_j,v_j).
\]
Their Gram matrix is
\[
G_{\rm aug}=\sum_{k\in\{0\}\cup R}b_kb_k^T
=\begin{pmatrix}a^2+\beta^2+m^2&\beta\\ \beta&1\end{pmatrix},
\qquad \det G_{\rm aug}=a^2+m^2.
\]
Let `ell_k=b_k^T G_aug^{-1}b_k`.  A direct computation gives, with
\[
\theta={m^2\over a^2+m^2},
\]
\[
\ell_0=1-\theta,
\qquad
\ell_j=v_j^2+\theta q_j^2.
\]
If
\[
\max\{1-\theta,\max_j(v_j^2+\theta q_j^2)\}\le {1\over2},
\]
then the newest Claude sharp Hausdorff--Young/physical Brascamp--Lieb lemma applies to the **actual augmented original-coordinate rows**, yielding
\[
I_{\rm aug}\le {(4\pi)^2\over\sqrt{a^2+m^2}}.
\]
Consequently
\[
\boxed{
|\phi_Q(t)|\le
\min\!\left\{1,
{4\pi^{3/2}L\sqrt{|a|}\over |\sigma|\sqrt{a^2+m^2}}
|t|^{-3/2}\right\}.}
\]
Fourier inversion gives the continuous-density estimate
\[
\boxed{
\|p_Q\|_\infty\le
3\,2^{4/3}L^{2/3}
\left({\sigma^2(a^2+m^2)\over |a|}\right)^{-1/3}.}
\]
In the one-sided exact-rank-three packet, `m=rho y`, `y^2>1/2`, `gamma=rho^2/|a|`, and the source spectral identity is `gamma sigma^2=s_1s_2s_3>=s_3(A)^3`.  Hence
\[
{\sigma^2(a^2+m^2)\over|a|}\ge
{\sigma^2m^2\over|a|}\ge s_3(A)^3y^2>{1\over2}s_3(A)^3,
\]
and with `L<=sqrt(e)`,
\[
\boxed{
\|p_Q\|_\infty<
3\,2^{5/3}e^{1/3}s_3(A)^{-1}
=13.29238\ldots\,s_3(A)^{-1}.}
\]
Thus adding the genuine pivot row before the absolute two-dimensional Fourier integral closes a nontrivial part of the r35 high-leverage collar and produces true `L^1_t` integrability rather than only finite `L^p` output norms.

The remaining state after this checkpoint is exactly where the augmented leverage gate fails.  The next step is to spend one offending original row separately (Plancherel) rather than revert to an abstract pair-density bound.
