# A zero-level semidefinite remark (proof handoff)

**Status:** proved consequence of the product-measure marginal theorem; it does not settle the unrestricted three-eigenvalue density conjecture. This is a separate remark for the semidefinite section of the assembled manuscript.

Let \(X_1,\ldots,X_n\) be independent with Lebesgue densities \(0\le f_i\le1\). Let \(A\succeq0\) and \(\theta=\lambda_3(A)>0\). For \(Q=X^{\mathsf T}AX\) and all \(t\ge0\),
\[
 \mathbb P(Q\le t)\le \frac{4\pi}{3}\,2^{3/2}\frac{t^{3/2}}{\sqrt{\lambda_1(A)\lambda_2(A)\lambda_3(A)}}\le\frac{4\pi}{3}\,2^{3/2}(t/\theta)^{3/2}. \tag{1}
\]
The same conclusion holds for \(Q=X^{\mathsf T}AX+b^{\mathsf T}X+c\) when \(b\in\operatorname{ran}A\), with \(Q\le t\) replaced by \(Q\le m+t\), where \(m=c-h^{\mathsf T}Ah\) and \(2Ah=b\).

**Proof.** Let \(E\) be the span of three orthonormal eigenvectors of \(A\) with eigenvalues \(\lambda_1(A),\lambda_2(A),\lambda_3(A)\), and let \(P_E\) be orthogonal projection onto \(E\). Since \(A\succeq0\), \(Q\ge\sum_{j=1}^3\lambda_j(A)\langle u_j,X\rangle^2\) pointwise. The Livshyts–Paouris–Pivovarov marginal-density theorem gives \(\|p_{P_E X}\|_\infty\le 2^{3/2}\) for arbitrary independent cap-one coordinate laws. Hence
\[
 \mathbb P(Q\le t)
 \le \mathbb P\!\left(\sum_{j=1}^3\lambda_j(A)\langle u_j,X\rangle^2\le t\right)
 \le \frac{2^{3/2}\operatorname{vol}(B_3)t^{3/2}}{\sqrt{\lambda_1(A)\lambda_2(A)\lambda_3(A)}},
\]
which is (1). For the affine extension, write \(Q=(X+h)^{\mathsf T}A(X+h)+m\); translation preserves independence and the density caps. \(\square\)

Thus the right derivative of the distribution function at the algebraic minimum is zero. The assembled manuscript's fixed-matrix continuity theorem (Theorem fg:fixed-matrix-continuity) gives a continuous density when \(\operatorname{rank}A\ge3\), and that version satisfies \(p_Q(m)=0\). The pointwise comparison with the three-eigenvector truncation establishes only this zero-level conclusion; it neither identifies the full output law with the truncated law nor bounds the density at other levels. If \(b\notin\operatorname{ran}A\), the affine extension above does not apply.

The exponent \(3/2\) is sharp: for \(A=I_3\) and independent \(X_i\sim\mathrm{Unif}[-1/2,1/2]\), equality \(\mathbb P(Q\le t)=(4\pi/3)t^{3/2}\) holds for \(0\le t\le1/4\).

**Primary input:** G. Livshyts, G. Paouris, and P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877–889, arXiv:1507.07949, Theorem 1.1. Manuscript context: proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/. The unrestricted indefinite target remains open, particularly the uniform rough-law adapted-hub endpoint and quantitative coverage of all no-pivot matrices.
