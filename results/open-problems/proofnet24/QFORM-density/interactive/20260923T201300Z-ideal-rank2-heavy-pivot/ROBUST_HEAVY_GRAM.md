# Robust two-direction finite-heavy pivot

**Status:** proved exact-rank-three theorem. It allows arbitrary transverse light leakage, unbounded top eigenvalues, and arbitrary original-coordinate affine terms. The full QFORM bounded-density conjecture remains open.

## Theorem

Let \(A=U\Lambda U^{\mathsf T}\), where \(U\) is \(n\times3\), \(U^{\mathsf T}U=I_3\), \(\Lambda=\Lambda^{\mathsf T}\) is invertible, and \(s_3(A)=s_3(\Lambda)\geq\sigma>0\). Let \(H\) be a set of \(h\geq2\) original coordinates. Put \(G_H=U_H^{\mathsf T}U_H\), and suppose its second largest eigenvalue obeys \(\lambda_2(G_H)\geq\kappa>0\).

Then either
\[
\max_{i\in H}|A_{ii}|\geq\frac{\kappa\sigma}{2h},
\tag{1}
\]
or
\[
\max_{\{i,j\}\subset H}
\left|\det A_{\{i,j\},\{i,j\}}\right|
\geq\frac{3\kappa^2\sigma^2}{4h(h-1)}.
\tag{2}
\]
There is no upper bound on \(\|\Lambda\|\), no bound on \(\lambda_3(G_H)\), and no exact light/heavy orthogonality assumption.

For independent cap-one original-coordinate densities and every deterministic original-coordinate affine term \(b^{\mathsf T}X+c\), the exact-rank-three form \(Q=X^{\mathsf T}AX+b^{\mathsf T}X+c\) has a density bounded by
\[
\|p_Q\|_\infty
\leq\frac1{\sigma}
\max\left\{
128\sqrt{\frac{2h}{\kappa}},
\frac{40}{\sqrt3\,\kappa}\sqrt{h(h-1)}
\right\}.
\tag{3}
\]
For \(h\leq432\) and \(\lambda_2(G_H)\geq1/2\), this is less than \(20000/\sigma\).

## Proof of the physical pivot

Let \(E\) be the two-dimensional top eigenspace of \(G_H\). With respect to \(E\oplus E^\perp\), the matrix \(\Lambda-P_E\Lambda P_E\) has block form
\[
\begin{pmatrix}0&u\\u^{\mathsf T}&d\end{pmatrix},
\]
so it has rank at most two. The best-rank-two approximation inequality yields
\[
\|P_E\Lambda P_E\|\geq s_3(\Lambda)\geq\sigma.
\tag{4}
\]

The heavy principal block \(B=A_{HH}=U_H\Lambda U_H^{\mathsf T}\) has the same nonzero eigenvalues as \(G_H^{1/2}\Lambda G_H^{1/2}\). Indeed, use the polar decomposition \(U_H=V G_H^{1/2}\), where \(V\) is an isometry on \(\operatorname{range}G_H\). As \(E\) is a spectral subspace of \(G_H\), the \(E\)-compression of \(G_H^{1/2}\Lambda G_H^{1/2}\) equals
\[
(G_H|_E)^{1/2}(P_E\Lambda P_E)|_E(G_H|_E)^{1/2}.
\]
The least eigenvalue of \(G_H|_E\) is at least \(\kappa\). For any invertible positive matrix \(D\), \(\|DBD\|\geq s_{\min}(D)^2\|B\|\), by writing \(B=D^{-1}(DBD)D^{-1}\). Thus (4) implies
\[
\|A_{HH}\|\geq\kappa\sigma.
\tag{5}
\]
This is an exact principal-compression argument, so arbitrarily large cross coefficients in \(\Lambda\) cannot cancel it.

Set \(c_0=\kappa\sigma\). If \(|\operatorname{tr}A_{HH}|\geq c_0/2\), then \(\operatorname{tr}A_{HH}=\sum_{i\in H}A_{ii}\) gives (1). Otherwise
\[
\operatorname{tr}(A_{HH}^2)\geq\|A_{HH}\|^2\geq c_0^2.
\]
The second elementary symmetric polynomial is
\[
e_2(A_{HH})
=\sum_{\{i,j\}\subset H}\det A_{\{i,j\},\{i,j\}}
=\frac{(\operatorname{tr}A_{HH})^2-\operatorname{tr}(A_{HH}^2)}2
\leq-\frac{3c_0^2}{8}.
\]
One of its \(\binom h2\) summands has modulus at least \(3c_0^2/[4h(h-1)]\), proving (2). Every spectral signature is covered.

## Density receiver and affine terms

Normalize \(A,b,c\) by \(\sigma\). In case (1), exact-rank-three [rank-two fusion, Corollary 8.2](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md) gives \(128/\sqrt{|\widetilde A_{ii}|}\), including an arbitrary original-coordinate affine term. In case (2), the unconditional original-coordinate pair-pivot receiver in [structure.tex](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/structure.tex) gives \(20/\sqrt D\) for \(D=|\det\widetilde A_{\{i,j\},\{i,j\}}|\): the definite pair has a bounded conditional density; the indefinite pair has a logarithmic conditional kernel, paid by a Schur remainder with \(N_S(1)\geq1\). This pair argument is unconditional even though the larger no-pivot-equivalence theorem in that source has a conjectural premise. Both receivers allow all induced affine terms. Substituting (1) or (2) and scaling back gives (3). At \(h=432,\kappa=1/2\), the two branch bounds are respectively \(5320.861\ldots/\sigma\) and \(19930.118\ldots/\sigma\).

## Consequence and limit

In a finite-heavy reduction with at most 432 original heavy rows, the exact-rank-three case \(\lambda_2(G_H)\geq1/2\) is solved, including arbitrary affine null directions. A remaining finite-heavy obstruction has \(\lambda_2(G_H)<1/2\): the selected heavy rows capture at most one spectral direction to this quantitative level. This does not solve the near-coloop model with overlapping light projections. No claim is made for matrices with additional nonzero eigenvalues.
