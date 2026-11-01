# Supplement — block Schur transport and pole avoidance

The scalar identity in REPORT.md extends exactly to a physical block pivot. This is useful because a scalar pivot may hit the Möbius pole while a larger physical principal block remains invertible.

Let
\[
B=\begin{pmatrix}P&F\\F^T&D\end{pmatrix},\qquad P\in\mathbb R^{r\times r}\text{ invertible},
\]
and let
\[
E=UCU^T,\qquad U=\binom{U_1}{U_2},\qquad C=C^T.
\]
Put `A=B+E` and assume the actual physical block
\[
P_A:=P+U_1CU_1^T
\]
is invertible. Define
\[
W:=U_2-F^TP^{-1}U_1,
\qquad
C':=C-CU_1^TP_A^{-1}U_1C.
\]
Then
\[
\boxed{
\operatorname{Sc}_{P_A}(A)
=
\operatorname{Sc}_{P}(B)+W C' W^T.
}
\tag{B1}
\]
Consequently
\[
\boxed{
\operatorname{rank}\bigl(\operatorname{Sc}_{P_A}(A)-\operatorname{Sc}_{P}(B)\bigr)
\le \operatorname{rank}C.
}
\tag{B2}
\]
Thus arbitrary low-rank spectral additions retain exactly the same rank budget through any sequence of invertible ORIGINAL-coordinate block Schur eliminations; scalar pivot cancellation does not force the algebraic transport itself to fail if a larger admissible block is used instead.

If `C` is invertible, Woodbury gives
\[
\boxed{(C')^{-1}=C^{-1}+U_1^TP^{-1}U_1}
\tag{B3}
\]
and the matrix determinant lemma gives
\[
\boxed{\det C'=\det C\,\frac{\det P}{\det P_A}.}
\tag{B4}
\]
For `r=1`, (B1)--(B4) reduce exactly to the scalar formulas in REPORT.md.

## Proof of (B1)

Write
\[
S_0=D-F^TP^{-1}F.
\]
The actual Schur complement is
\[
S_A=D+U_2CU_2^T-(F^T+U_2CU_1^T)P_A^{-1}(F+U_1CU_2^T).
\]
Using
\[
C'=C-CU_1^TP_A^{-1}U_1C,
\]
together with the two identities
\[
C'U_1^TP^{-1}=CU_1^TP_A^{-1},
\qquad
P^{-1}U_1C'=P_A^{-1}U_1C,
\]
(which follow by multiplying the Woodbury relation), direct expansion of `W C' W^T` gives exactly `S_A-S_0`.

Equivalently, when `C` is invertible, (B3) is the Woodbury identity
\[
(C^{-1}+U_1^TP^{-1}U_1)^{-1}
=C-CU_1^T(P+U_1CU_1^T)^{-1}U_1C,
\]
and the standard block Gaussian factorization then yields (B1). The polynomial identity extends to singular `C` by continuity, or directly by the displayed expansion.

## Certificate-switch interpretation

The latest `fleet02/B12` rank-one family shows a scalar actual pivot can vanish while the complementary physical three-coordinate block has two eigenvalues exactly `2 sigma`, yielding `||p||_infinity<=C_*/2`. The block identity formalizes the correct rule: do not force a scalar Schur inversion through a pole. Either switch immediately to the partner physical-block density certificate, or—when a larger original-coordinate block is invertible—transport the low-rank spectral remainder through that block using (B1). No spectral rotation or independence of eigen-coordinates is invoked.

This supplement does not by itself produce a universal admissible block from the bare three-large-eigenvalue hypothesis; that structural certificate-selection step remains open.

Finite corroboration: 1,200 random block instances with block sizes 2 and 3 and perturbation ranks 1--3 gave maximum operator-norm residual in (B1) `5.678915016957215e-14`, maximum determinant residual in (B4) `1.8189894035458565e-12`, and zero rank violations.
