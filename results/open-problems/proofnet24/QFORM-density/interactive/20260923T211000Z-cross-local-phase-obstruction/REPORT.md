# Arbitrary bank-local phases obstruct a general planar cross receiver

Date: 2026-09-23. Status: **proved counterexample to an overly broad receiver**, not to the rank-three RMT/QFORM conjecture.

## Explicit example

Let H,X_1,X_2,X_3,X_4 be independent uniforms on [-1/2,1/2]. Define two independent planar light banks
\[
(L_A,V_A)=(X_1,X_2)/\sqrt2,\qquad
(L_B,V_B)=(X_3,X_4)/\sqrt2.
\]
Each bank has a planar density bounded by 2, and each bank's Gram matrix in the original coordinates equals \(I_2/2\). Thus the banks arise from genuine independent cap-one original coordinates with a balanced orthonormal two-frame. Write \(L=L_A+L_B\).

Consider the generalized cross interaction
\[
2H L+2L_A L_B+2V_A V_B,
\]
whose bank-to-bank matrix in the (L,V) coordinates is \(C=\operatorname{diag}(2,2)\), in particular \(C_{VV}=2\). Add the real bank-local and hub-local phases
\[
R_H(H)=H^2,\quad
R_A(L_A,V_A)=L_A^2-V_A^2,\quad
R_B(L_B,V_B)=L_B^2-V_B^2.
\]
The resulting random variable is exactly
\[
Q
=2HL+2L_A L_B+2V_A V_B+R_H+R_A+R_B
=(H+L_A+L_B)^2-(V_A-V_B)^2.
\tag{1}
\]
Put \(U=H+L_A+L_B\) and \(W=V_A-V_B\). They are independent, and each has a continuous density bounded below by a positive constant on some neighborhood of zero. Consequently the output density of \(U^2-W^2\) is unbounded at zero. For example, for small \(s>0\), changing the U variable through its two square branches gives
\[
p_Q(s)
=\int_{\mathbb R}p_W(w)
\frac{p_U(\sqrt{w^2+s})+p_U(-\sqrt{w^2+s})}
{2\sqrt{w^2+s}}\,dw
\ge c\int_{\sqrt s}^{r}\frac{dw}{w}
\ge c'\log(1/s)
\]
for fixed positive c,c',r. Thus \(\|p_Q\|_\infty=\infty\), despite the independent capped sources, balanced planar bank geometry, and \(C_{VV}=2\).

The quadratic form in (1) has **rank two**, so \(s_3=0\). This example does not refute the original conjecture with \(s_3\ge1\). It shows that a general cross-matrix receiver cannot permit arbitrary bank-local quadratic phases based only on \(C_{VV}=2\).

## General matrix diagnosis

For
\[
C=\begin{pmatrix}a&b\\c&2\end{pmatrix},
\]
make bankwise triangular shears
\[
V_A'=V_A+\tfrac b2L_A,\qquad
V_B'=V_B+\tfrac c2L_B.
\]
Their Jacobians equal one, so planar density caps are unchanged. The cross interaction becomes
\[
(L_A,V_A)C(L_B,V_B)^{\mathsf T}
=2V_A'V_B'+dL_A L_B,
\qquad d=a-\frac{bc}{2}.
\]
When d≠0, arbitrary separate quadratic local phases can complete the hub-L interaction \(2H(L_A+L_B)+dL_A L_B\) to a single signed square, and the V cross interaction to a square of the opposite sign, just as in (1). Thus the obstruction is systematic for nonsingular C. The rank-one cross case d=0 has a different structure and is not ruled out by this construction.

## Relation to proved receivers

The [diffuse two-light local-potential theorem](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T205600Z-diffuse-two-light-local-potentials/REPORT.md) assumes the cross interaction induced by \(V^2\), with no additional \(L_A L_B\) term, and therefore is not contradicted. The [all-beta finite-P theorem](https://github.com/yspennstate/math-open-problems/blob/452da6b8207d8886b6ab99cfaf944570035df2a5/proofnet24/QFORM-density/interactive/20260923T205630Z-finite-p-support-fourier/ALL_BETA_ADDENDUM.md) allows beta but does not allow arbitrary bank-local phases. This example explains why those separate assumptions cannot be combined without tracking the full spectral rank.
