# Checks for QFORM-NULLHUB-DIAGONAL-GATED-PAIRLOG-v1

Run: `20260923T162049Z-fleet04-B18-QFORM-r4`.

These are regression checks; the proof is the exact algebra in `REPORT.md`.

## Singular values

For
\[
B=\begin{pmatrix}0&g\\g&a\end{pmatrix},
\]
the characteristic polynomial is \(\lambda^2-a\lambda-g^2\). Since the determinant is negative for \(g\ne0\), the least singular value is the smaller absolute eigenvalue:
\[
\kappa(B)=
\frac{\sqrt{a^2+4g^2}-|a|}{2}
=\frac{2g^2}{\sqrt{a^2+4g^2}+|a|}.
\]

At \(\eta=s=1/64\),
\[
\kappa_0=\frac{\sqrt5-1}{128}
=0.009656781074217108\ldots .
\]

The fleet01 inequality and the heavy-compiler gate \(hDq_i>1/10\) give
\[
8\sqrt2(0.1\kappa_0)^{-1/4}
=8\sqrt2\left(\frac{1280}{\sqrt5-1}\right)^{1/4}
=64.17958261516226\ldots .
\]

## Gate consistency

- \(a_i=A_{ii}\), so \(N3(1/64)\) supplies \(|a_i|<1/64\) directly.
- The new subbranch assumes \(|g_i|\ge1/64\).
- The pair is then invertible and indefinite because \(\det B_i=-g_i^2<0\).
- The LPP projection is supported only on the original coordinates outside \(\{0,i\}\).
- The report claims only an essential density bound, not continuity.
