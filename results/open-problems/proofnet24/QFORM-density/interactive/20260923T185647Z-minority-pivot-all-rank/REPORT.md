# All-rank minority-sign Schur pivot for mixed-sign quadratic forms

**Status:** Proved conditional density theorem. It extends the exact-rank-three minority pivot in fleet01/B11 to arbitrary rank by using the assembled semidefinite second-level concentration theorem. The unrestricted s_3(A)>=1 conjecture remains open because the size of a minority-sign physical diagonal cannot be bounded below from the spectrum alone.

## Theorem

Let X_1,...,X_n be independent real random variables with Lebesgue densities 0<=f_i<=1. Let A be real symmetric with exactly one negative eigenvalue (zero eigenvalues are allowed), and suppose its second largest positive eigenvalue satisfies lambda_2(A)>=1. Suppose that for an original coordinate i,
\[
a:=A_{ii}\le-\delta<0.
\]
Then, for arbitrary b in R^n and c in R, the law of
\[
Q=X^{\mathsf T}AX+b^{\mathsf T}X+c
\]
has a density and
\[
\|p_Q\|_\infty
\le
\frac{3\sqrt{K_2(3+\log K_2)}}{\sqrt{\delta}}
=
\frac{674.400889\ldots}{\sqrt{\delta}},
\qquad
K_2=4\sqrt{600}\cdot4\sqrt{128}
=16\sqrt{76800}<4435. \tag{1}
\]
The conclusion also holds if A has exactly one positive eigenvalue, lambda_2(-A)>=1, and some original diagonal A_ii>=delta, by applying the displayed assertion to -Q.

A useful normalized formulation: if the positive spectrum has at least two eigenvalues >=1 and the negative spectral inertia is one, a minority-sign original diagonal of magnitude at least 1/640 gives \|p_Q\|_\infty<17100.

## Proof

Reorder coordinates so i is first and write
\[
A=\begin{pmatrix}a&v^{\mathsf T}\\v&D\end{pmatrix},
\qquad
S=D-\frac{vv^{\mathsf T}}a=D+\frac{vv^{\mathsf T}}{|a|}.
\]
Block Gaussian congruence sends A to diag(a,S). Since a<0 and A has exactly one negative eigenvalue, S is positive semidefinite, including possible zero modes.

In fact lambda_k(S)>=lambda_k(A) for every positive eigenvalue lambda_k(A)>0. To check this quantitative statement, fix 0<t<lambda_k(A). The scalar upper-left block a-t<0 of A-tI has Schur complement
\[
S_t=D-tI-\frac{vv^{\mathsf T}}{a-t}
=D-tI+\frac{vv^{\mathsf T}}{|a|+t}.
\]
Inertia additivity says S_t has at least k positive eigenvalues, because A-tI does and the scalar a-t is negative. But
\[
S-tI-S_t
=\left(\frac1{|a|}-\frac1{|a|+t}\right)vv^{\mathsf T}\succeq0.
\]
Thus S-tI has at least k positive eigenvalues by eigenvalue monotonicity. Letting t increase to lambda_k(A) proves lambda_k(S)>=lambda_k(A). In particular lambda_2(S)>=1.

Completing the square in the original coordinate X_i writes
\[
Q=a(X_i-m(X_{-i}))^2+R(X_{-i}),
\]
where m is affine and R is a quadratic form with matrix S positive semidefinite and arbitrary affine/constant terms. The density of a(X_i-m)^2, conditional on all other original coordinates, is bounded by
\[
|a|^{-1/2}|y-R(X_{-i})|^{-1/2}.
\]
This holds for either sign of a: the two inverse-image roots together contribute at most that expression. Hence for every nonnegative Borel h,
\[
\mathbb E h(Q)\le |a|^{-1/2}
\mathbb E\int_{\mathbb R}h(y)|y-R|^{-1/2}\,dy. \tag{2}
\]

The assembled manuscript's semidefinite first-two-level theorem (Proposition sd:psd-levels, part 2) applies to R because S is positive semidefinite, lambda_2(S)>=1, and its affine coefficients are unrestricted. It gives
\[
\alpha_2(R):=\sup_{0<u\le1}
\frac{\sup_s\mathbb P(|R-s|\le u)}
{u(1+\log(1/u))}\le K_2.
\]
Its square-root composition lemma (Lemma sd:composition, part 3), applied to (2) with K=|a|^{-1/2}, gives
\[
\|p_Q\|_\infty
\le3|a|^{-1/2}\sqrt{K_2(3+\log K_2)}
\le3\delta^{-1/2}\sqrt{K_2(3+\log K_2)}.
\]
This proves (1). Reflection proves the opposite-sign assertion.

## Scope and relation to existing work

The exact-rank-three minority-sign Schur theorem in proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/20260922T231431Z-fleet01-B11-QFORM-r11/REPORT.md gives a sharper determinant-aware estimate in rank three. Its proof uses an exact rank-two semidefinite Schur remainder. The argument here works at arbitrary rank, including dense residual interactions, because the semidefinite two-level theorem handles every rank and arbitrary affine terms. The bound depends on the original-coordinate pivot magnitude delta. A negative spectral eigenvector can be spread across arbitrarily many coordinates, making every negative physical diagonal small. Spectral information alone does not supply this pivot, and the theorem is not a full resolution.

The inputs are Proposition sd:psd-levels(2) and Lemma sd:composition(3) of proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/semidefinite.tex. This note only proves their combination with the signed Schur comparison; it does not independently reprove the global semidefinite concentration proposition.
