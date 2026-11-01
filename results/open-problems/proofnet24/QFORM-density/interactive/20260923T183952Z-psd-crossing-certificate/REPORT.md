# A random-sign crossing certificate for semidefinite matrices

**Status:** proved structural lemma and scoped density corollary. The unrestricted positive semidefinite density theorem is already known in the assembled manuscript; the first lemma below improves the quantitative cross-block existence criterion but does not on its own control crossing leverage. It gives no theorem for general indefinite matrices.

## Structural lemma

Let \(A\succeq0\) be symmetric, \(\lambda_k(A)\ge\sigma>0\), and \(\max_i A_{ii}\le d\). If \(kd<\sigma\), there exists a partition \(I\sqcup J=[n]\) of ORIGINAL coordinates such that
\[
 s_k(A_{I,J})\ge\frac{\sigma-kd}{4}. \tag{1}
\]
No rank restriction and no upper bound on the remaining eigenvalues are needed.

**Proof.** Let \(U\) contain orthonormal eigenvectors for the top \(k\) eigenvalues, so \(AU=U\Lambda\) with \(\Lambda\succeq\sigma I_k\). Let \(S=\operatorname{diag}(\varepsilon_1,\ldots,\varepsilon_n)\) have independent symmetric signs and put \(B_S=U^{\mathsf T}SASU\succeq0\). Then
\[
 \mathbb E\operatorname{tr}B_S
 =\sum_i A_{ii}\|U^{\mathsf T}e_i\|_2^2
 \le kd.
\]
Fix a sign choice with \(\operatorname{tr}B_S\le kd\); hence \(0\preceq B_S\preceq kd I_k\). Set \(D_I=(I_n+S)/2\), \(D_J=(I_n-S)/2\), and \(R=U^{\mathsf T}SU=R^{\mathsf T}\). The compression of the physical crossing block is
\[
 T=U^{\mathsf T}D_IAD_JU
  =\tfrac14(\Lambda-\Lambda R+R\Lambda-B_S).
\]
Because \(-\Lambda R+R\Lambda\) is skew symmetric, the symmetric part of \(T\) is \((\Lambda-B_S)/4\succeq(\sigma-kd)I_k/4\). Thus \(\|Tz\|_2\ge(\sigma-kd)\|z\|_2/4\) for every \(z\). Since \(T=U_I^{\mathsf T}A_{I,J}U_J\) and both \(U_I,U_J\) are contractions, the singular-value variational principle gives \(s_k(A_{I,J})\ge s_k(T)\), proving (1). \(\square\)

## A bounded-spectrum consequence

If \(\lambda_3(A)\ge1\), \(\|A\|_{\rm op}\le M\) for \(M\ge1\), and \(\max_i A_{ii}\le1/(400M)\), then every quadratic form \(Q=X^{\mathsf T}AX+b^{\mathsf T}X+c\) with independent cap-one coordinates satisfies
\[
 \|p_Q\|_\infty<52. \tag{2}
\]

Indeed, (1) supplies a cut \(B=A_{I,J}\) with \(s_3(B)\ge\sigma_c=(1-3/(400M))/4\ge\sigma_*=(1-3/400)/4=0.248125\). Each crossing row obeys
\[
 \|B_{i,J}\|_2^2\le(A^2)_{ii}\le M A_{ii}\le1/400,
\]
because \(A^2\preceq M A\). At \(\gamma=\sigma_c/\sqrt6\), the ridge leverage \(K_\gamma=B(B^{\mathsf T}B+\gamma^2 I)^{-1}B^{\mathsf T}\) satisfies
\[
 \max_{i\in I}(K_\gamma)_{ii}
 \le\frac6{400\sigma_c^2}
 \le\frac6{400\sigma_*^2}<0.244<\tfrac12.
\]
Corollary four:ridge-three in the assembled manuscript applies despite arbitrary quadratic terms inside \(I,J\) and arbitrary affine terms. It gives
\[
 \|p_Q\|_\infty\le\frac{9\sqrt{3e}}{2\sigma_c}
 \le\frac{9\sqrt{3e}}{2\sigma_*}
 =51.7905\ldots<52.
\]
This corollary is a quantitative subcase of the existing all-rank semidefinite theorem, not a resolution of the indefinite target. For indefinite \(A\), the positive-definite sign of the symmetric compression used above is unavailable; its direct signed analogue is unjustified.

**Dependencies:** the ridge Fourier density criterion in proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/fourier.tex (Corollary four:ridge-three). The random-sign certificate and the displayed subcase proof are elementary.
