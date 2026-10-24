# An exact rank-three diffuse spectral case

**Status:** A proved special case of the density conjecture. It does not establish the full conjecture, which includes concentrated eigenvectors, extra spectral directions, and the overlapping negative-target receiver.

## Statement

Let \(X_1,\ldots,X_n\) be independent real random variables, each with a probability density at most one. Let \(A\) be a real symmetric matrix of **exact rank three**, whose three nonzero eigenvalues have absolute value at least one. Choose an orthonormal eigenvector matrix \(U\in\mathbb R^{n\times3}\), and suppose its physical-coordinate leverages obey
\[
 \kappa:=\max_i\|U_{i,*}\|_2^2\le\frac1{24}.
\]
Then \(Q=X^\top A X+b^\top X+c\) has a continuous density vanishing at infinity, with
\[
 \|p_Q\|_\infty\le 24\sqrt e.\tag{1}
\]
The same estimate holds after replacing both within-bank terms arising from \(Q\) by **arbitrary measurable real functions** of the respective independent original-coordinate banks described below. Thus the estimate is insensitive to arbitrary quadratic self interactions, affine terms, and conditioned contributions that remain bank local.

## A deterministic cut

Write \(A=U\Lambda U^\top\), where \(U^\top U=I_3\) and \(|\det\Lambda|\ge1\). Independently mark each original coordinate for a bank \(I\) with probability \(1/2\), putting all remaining coordinates into \(J\). Let \(u_i=U_{i,*}^\top\) and \(G_I=U_I^\top U_I=\sum_{i\in I}u_i u_i^\top\). Then
\[
 \mathbb E G_I=\tfrac12I_3,
 \qquad
 \mathbb E\|G_I-\tfrac12I_3\|_F^2
   =\tfrac14\sum_i\|u_i\|_2^4
   \le\tfrac34\kappa\le\tfrac1{32}<\tfrac1{16}.
\]
Consequently some actual partition satisfies \(\|G_I-I_3/2\|_{\rm op}\le1/4\) (indeed, strict inequality can be obtained). For that partition, both \(G_I\) and \(G_J=I_3-G_I\) lie between \(I_3/4\) and \(3I_3/4\).

The cross-bank matrix is \(M=A[I,J]=U_I\Lambda U_J^\top\). Its squared 3-minor volume, by two applications of Cauchy–Binet, is
\[
 Z_3(M):=\sum_{|S|=|T|=3}\det M[S,T]^2
   =\det(\Lambda)^2\det(G_I)\det(G_J)
   \ge 4^{-6}.\tag{2}
\]
Moreover its squared-3-minor row-inclusion probability is
\[
 \alpha_i
   =\frac{\sum_{S\ni i,\,|S|=3}\det(U_S)^2}{\det(G_I)}
   =u_i^\top G_I^{-1}u_i
   \le4\|u_i\|_2^2\le\tfrac16
   \quad(i\in I).\tag{3}
\]
In the first equality, the independent column-minor sum and factor \(\det(\Lambda)^2\) cancel. The second equality is the derivative of the Cauchy–Binet identity \(\det(\sum_{i\in I}t_i u_i u_i^\top)=\sum_{|S|=3}\det(U_S)^2\prod_{i\in S}t_i\) at all \(t_i=1\).

## Anticoncentration on the physical cut

We invoke the proved mixed Fourier-power volume estimate for an independent-original-coordinate physical cut: if \(Z_3(M)>0\) and all 3-volume row marginals \(\alpha_i\le1/2\), then any
\[
 F(X_I)+2X_I^\top M X_J+G(X_J)
\]
with arbitrary real measurable bank-local phases \(F,G\) has a continuous density bounded by
\[
 \|p\|_\infty\le 6\sqrt e\,Z_3(M)^{-1/6}.\tag{4}
\]
For clarity, this consequence follows by Cauchy–Schwarz over the independent \(I\)-bank, then expanding a difference of independent \(J\)-bank copies, applying the 3-volume Brascamp–Lieb/Fourier-power estimate to obtain
\[
 |\phi(t)|^2\le e^{3/2}(2\pi)^3|t|^{-3}Z_3(M)^{-1/2}.
\]
Integrate \(\min\{1,C|t|^{-3/2}\}\) in Fourier inversion to get (4). The \(J\)-difference coordinates have densities at most one, and no independence is assumed between orthogonal projections of a bank. A fully detailed proof of the mixed-volume estimate appears in the companion *One concentrated cross row with a diffuse rank-two remainder* note.

Since (3) meets its leverage hypothesis and (2) gives \(Z_3(M)^{-1/6}\le4\), (4) yields (1). For the original quadratic, set \(F(x_I)=x_I^\top A_{II}x_I+b_I^\top x_I\) and \(G(x_J)=x_J^\top A_{JJ}x_J+b_J^\top x_J+c\). Conditional outside variables merely modify these bank-local functions if all cross terms involving the outside variables are absorbed as affine terms.

## Scope of the structural reduction

The theorem requires **exact rank three** to factor \(M=U_I\Lambda U_J^\top\). When \(A\) has additional spectral directions, their cross-bank contributions can cancel this cross matrix, and (2) need not hold. If a third eigenvector is concentrated on a physical hub, every cut may have cross rank at most two in the zero-leakage limit; this case requires a crossing-plus-square receiver rather than a 3-cross-volume argument. The unresolved full conjecture contains both complications, including the small-leakage overlapping negative-target case.
