# Exact-rank-three positive semidefinite quadratic forms: a uniform all-level density bound

**Status: proved scoped theorem and alternate derivation.** This handles arbitrary original-coordinate affine terms. The assembled manuscript already proves the stronger [full arbitrary-rank semidefinite theorem](https://github.com/yspennstate/math-open-problems/blob/d6f59993e85da91da39942ae96d92481abbaf541/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/semidefinite.tex) with bound 17100/σ, and an exact-rank-three bound 58/σ. The argument below gives another proof with constant 234/σ; it does not address indefinite matrices.

Let \(X_1,\ldots,X_n\) be independent real random variables with densities bounded by one. Let \(A\succeq0\) have **exact rank three** and \(s_3(A)\ge\sigma>0\). For arbitrary \(b\in\mathbb R^n\) and \(c\in\mathbb R\), the random variable
\[
Q=X^TAX+b^TX+c
\]
has an essentially bounded density satisfying
\[
\|p_Q\|_\infty<234/\sigma.
\]

## Proof

Write \(A=U\Lambda U^T\), where \(U^TU=I_3\) and all three diagonal entries of \(\Lambda\) are at least \(\sigma\). Put \(c_i=\|U_{i,\cdot}\|^2\), so \(\sum_i c_i=3\). Set \(\delta=3/10\).

**Heavy row.** If some \(c_i\ge\delta\), positivity gives
\[
a=A_{ii}=U_{i,\cdot}\Lambda U_{i,\cdot}^T\ge\sigma c_i>0,
\qquad \det\Lambda\ge\sigma^3.
\]
The arbitrary-affine, exact-rank-three Schur consequence of the [rank-two half-Riesz theorem](https://github.com/yspennstate/math-open-problems/blob/e542b1a6ef471b329e4e88a6553e1aacb45acc1a/proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md), Equation (1.2), gives
\[
\|p_Q\|_\infty\le128(c_i a\det\Lambda)^{-1/4}
\le {128\over\sigma\sqrt{c_i}}
\le {128\over\sigma\sqrt{3/10}}
<234/\sigma.
\]
For clarity, the Schur step conditions on the other originals only to identify the physical hub; it then completes the square in \(X_i\). The rank-two Schur residual retains arbitrary affine terms in the other original coordinates, which the cited half-Riesz theorem explicitly allows. No independence of spectral coordinates is asserted.

**Diffuse rows.** Otherwise every \(c_i<\delta\). Choose independent random signs \(\eta_i\) and let \(T=\sum_i\eta_i U_{i,\cdot}^TU_{i,\cdot}\), a \(3\times3\) matrix. Then
\[
\mathbb E\|T\|_F^2=\sum_i c_i^2\le\delta\sum_i c_i=9/10.
\]
Thus some signing has \(\|T\|_{\rm op}\le\|T\|_F\le\sqrt{9/10}\). Its positive and negative original-coordinate banks \(S,T_{\rm bank}\) obey
\[
U_S^TU_S,\ U_{T_{\rm bank}}^TU_{T_{\rm bank}}
\succeq c_0 I_3,\qquad
c_0={1-\sqrt{9/10}\over2}>0.
\]
The [exact-rank-three two-bank Fourier theorem](https://github.com/yspennstate/math-open-problems/blob/ded875c2199e63eebfc49dd25d3ca4d349723301/proofnet24/QFORM-density/interactive/20260923T193700Z-diffuse-rank-three-fourier/REPORT.md) applies with arbitrary affine \(b\) and gives
\[
\|p_Q\|_\infty\le{6\over c_0\sigma}
={12\over(1-\sqrt{9/10})\sigma}
<234/\sigma.
\]
In the heavy-row case, the cited Schur theorem asserts essential boundedness; the diffuse Fourier receiver gives a bounded continuous representative. Together they prove the stated essential bound.

## Scope and remaining gap

The heavy-row inequality \(A_{ii}\ge\sigma c_i\) uses positive semidefiniteness. It fails for mixed-sign eigenvalues through Rayleigh cancellation. Exact rank three is used twice: in the Schur residual's rank-two half-Riesz estimate and in the two-bank Fourier expansion, where any extra spectral tail creates additional cross-bank terms. The present proof is limited to rank three. The cited assembled manuscript settles arbitrary-rank semidefinite matrices by a different induction and Gram-volume argument. The unrestricted mixed-sign three-singular-value conjecture remains open.
