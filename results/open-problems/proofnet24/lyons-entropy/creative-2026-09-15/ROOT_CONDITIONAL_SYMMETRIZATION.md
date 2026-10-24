# Conditional permutation symmetrization through one uniform coupling mode

Root constructive consequence of C051 and C075, 2026-09-15. This is a global constrained entropy-maximization theorem and a core-direction Hessian theorem, not arbitrary two-endpoint Lyons concavity. No historical priority is claimed.

## 1. Global theorem with an arbitrary coherent exterior

Let a measured core have \(m\ge2\) coordinates and let \(u=\mathbf1/\sqrt m\). Let
\[
K=\begin{pmatrix}A&uv^*\\vu^*&C\end{pmatrix},\qquad 0\le K\le I,
\]
where the exterior covariance \(C\) and vector \(v\) are arbitrary. Define
\[
\lambda=u^*Au,\qquad a=\frac{\operatorname{tr}A-\lambda}{m-1},\qquad
\overline A=a(I-uu^*)+\lambda uu^*,
\]
and retain the entire exterior and cross block:
\[
\overline K=\begin{pmatrix}\overline A&uv^*\\vu^*&C\end{pmatrix}.
\]
Then
\[
\boxed{H(P_{\overline K})\ge H(P_K).}\tag{1}
\]
For strict \(K\), equality holds if and only if \(A=\overline A\).

Both feasibility and the meaning of the operation are explicit: \(\overline K\) is the average of \(K\) over permutations of the core coordinates alone. The cross block is unchanged because each such permutation fixes \(u\). Thus among all cores with fixed \(\operatorname{tr}A\) and \(u^*Au\), and with the displayed exterior and coupling fixed, the exchangeable core uniquely maximizes entropy in the strict domain.

### Exact conditional proof and gap

For strict \(K\), the exterior atom \(Y\) has a positive fixed probability \(q_Y=P_C(Y)\), and the core conditional covariance is
\[
F_Y=A-r_Y uu^*,\qquad
r_Y=v^*(C-I_{Y^c})^{-1}v\in\mathbb R.
\]
Its permutation average is exactly
\[
\overline F_Y=\overline A-r_Y uu^*=a(I-uu^*)+(\lambda-r_Y)uu^*.
\]
Every conditional kernel is strict. The entropy chain rule and C051 give
\[
\boxed{H(P_{\overline K})-H(P_K)
=\sum_Yq_Y\left[D(P_{F_Y}\Vert P_{\overline F_Y})
+\mathcal T_Y(F_Y)\right]\ge0.}\tag{2}
\]
Here \(\mathcal T_Y\ge0\) is exactly C051's determinant-integral gap at the conditional exchangeable average; for a negative exchangeable off-diagonal parameter, use its complementary integral, and for a zero parameter it is zero. Thus no unspecified conditional-acceleration sign is used. If \(A\ne\overline A\), every \(F_Y\ne\overline F_Y\), and C051's strictness makes (2) positive.

The regularization \(K^\epsilon=(1-2\epsilon)K+\epsilon I\) preserves the one-uniform-mode coupling and commutes with core averaging. Continuity proves (1) for closed contractions without assigning finite logarithms to impossible atoms.

## 2. Full Hermitian core directions at the symmetric base

Suppose \(\overline K\) is strict. Vary only its core in an arbitrary Hermitian direction \(B\), keeping \(C,v\) fixed. The exterior probabilities are constant and every conditional path is exactly affine:
\[
F_Y(t)=\overline F_Y+tB.
\]
Therefore the full restricted Hessian, with all \(m^2\) real core directions retained, is
\[
\boxed{D^2H(\overline K)\left[
\begin{pmatrix}B&0\\0&0\end{pmatrix},
\begin{pmatrix}B&0\\0&0\end{pmatrix}\right]
=\sum_Yq_Y D^2H(\overline F_Y)[B,B]\le0.}\tag{3}
\]
C075 proves the last sign at every exchangeable base in every dimension. If either \(v\ne0\) or \(\lambda\ne a\), the inequality is strict for every nonzero \(B\).

Indeed, when \(v\ne0\), the empty and full exterior atoms have positive probabilities and
\[
r_\varnothing=-v^*(I-C)^{-1}v<0,
\qquad r_{\mathrm{full}}=v^*C^{-1}v>0.
\]
Thus not every \(\lambda-r_Y\) can equal \(a\). At least one conditional base is a nonproduct exchangeable kernel, where C075 gives a strictly negative full Hermitian Hessian; all other terms in (3) are nonpositive. If \(v=0\) but \(\lambda\ne a\), every conditional base is the same nonproduct exchangeable core. If \(v=0\) and \(\lambda=a\), the product core has the familiar off-diagonal affine-Hessian null directions, so strictness is not asserted.

Strictness in (3) supplies a neighborhood with a negative full core-direction Hessian for each fixed strict \(C,v\), by continuity and compactness of the unit sphere of core directions. The theorem does not claim negative curvature for simultaneous arbitrary changes of \(C\) and \(v\). Nor does the global maximum (1) by itself prove concavity along every segment from \(A\) to \(\overline A\).
