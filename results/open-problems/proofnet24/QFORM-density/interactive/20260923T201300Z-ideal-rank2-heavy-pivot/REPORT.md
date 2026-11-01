# Exact heavy-plane split forces a physical pivot

**Status:** proved exact-rank-three theorem. The full QFORM bounded-density conjecture remains open. See the [robust two-direction version](ROBUST_HEAVY_GRAM.md) for a stronger hypothesis-free leakage result.

Let \(A=U\Lambda U^{\mathsf T}\), where \(U\) is \(n\times3\), \(U^{\mathsf T}U=I_3\), and \(s_3(\Lambda)\geq\sigma>0\). Suppose original coordinates split into \(H\cup R\), \(h=|H|\leq432\), and for a spectral plane \(E\),
\[
U_H^{\mathsf T}U_H=P_E,\qquad U_R^{\mathsf T}U_R=P_{E^\perp}.
\tag{1}
\]
Every heavy row then lies in \(E\), and every light row lies in \(E^\perp\).

## Theorem

Either some original heavy diagonal obeys
\[
|A_{ii}|\geq \frac{\sigma}{2h},
\tag{2}
\]
or some original heavy principal pair obeys
\[
\left|\det A_{\{i,j\},\{i,j\}}\right|
\geq \frac{\sigma^2}{2\binom h2}
=\frac{\sigma^2}{h(h-1)}.
\tag{3}
\]
For independent cap-one original-coordinate densities and **arbitrary original-coordinate affine terms** \(b^{\mathsf T}X+c\), the exact-rank-three form \(Q=X^{\mathsf T}AX+b^{\mathsf T}X+c\) consequently satisfies
\[
\|p_Q\|_\infty
\leq \frac1{\sigma}
\max\{128\sqrt{2h},\,20\sqrt{h(h-1)}\}
<\frac{8630}{\sigma}.
\tag{4}
\]

## Proof

Use an orthonormal basis of \(E\oplus E^\perp\) and write
\[
\Lambda=\begin{pmatrix}B&u\\u^{\mathsf T}&\lambda\end{pmatrix},
\qquad B\in\mathbb R^{2\times2}.
\]
The difference \(\Lambda-\operatorname{diag}(B,0)\) has rank at most two, so the rank-two approximation inequality gives \(\|B\|\geq s_3(\Lambda)\geq\sigma\).

The frame identity (1) makes \(U_H:E\to\mathbb R^h\) an isometry. Hence the two possibly nonzero eigenvalues of \(A_{HH}=U_HBU_H^{\mathsf T}\) are exactly the eigenvalues \(\mu_1,\mu_2\) of \(B\). In particular,
\[
\operatorname{tr}B=\sum_{i\in H}A_{ii},\qquad
\det B=\sum_{\{i,j\}\subset H}\det A_{\{i,j\},\{i,j\}}.
\tag{5}
\]
The second formula is the second elementary symmetric polynomial, or Cauchy–Binet; signs of \(B\) do not matter.

Say \(|\mu_1|\geq\sigma\). If \(|\mu_1+\mu_2|\geq\sigma/2\), the trace formula gives (2). Otherwise \(|\mu_2|>\sigma/2\), so \(|\det B|>\sigma^2/2\), and the determinant formula gives (3).

Normalize \(A,b,c\) by \(\sigma\). In case (2), [rank-two fusion, Corollary 8.2](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md) gives \(128/\sqrt{|A_{ii}|/\sigma}\) for the normalized density, uniformly for arbitrary original affine \(b\). In case (3), the unconditional physical pair-pivot argument in [structure.tex](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/structure.tex) gives \(20/\sqrt D\), where \(D\) is the normalized principal pair determinant. The definite pair has a bounded conditional density. The indefinite pair has a logarithmic conditional kernel, paid by the one-large-eigenvalue Schur remainder through the global logarithmic-potential lemma. This pair-pivot argument is unconditional even though the enclosing no-pivot-equivalence theorem has a conjectural premise. Scaling the density back yields (4).

The exact Gram identities (1) are used only for the sharper constant here. The companion robust report handles quantitative heavy two-dimensional Gram mass and unrestricted transverse leakage. Neither report treats a finite-heavy set carrying only one robust spectral direction.
