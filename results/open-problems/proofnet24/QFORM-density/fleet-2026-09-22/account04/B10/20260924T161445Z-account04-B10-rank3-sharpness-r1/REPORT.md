# Exact rank-three sharpness of the physical Schur completion

## Result

The rank-\(3r\) bound in the current physical Schur-completion argument is
structurally sharp already for \(r=1\). Therefore the nine-direction compiler
cannot be reduced to an eight-direction compiler merely by replacing
\(\operatorname{rank}R\le3r\) with \(\operatorname{rank}R\le2r\).

## Calculation

Take a symmetric matrix on the ordered coordinates \(S=\{1\}\),
\(T=\{2\}\), \(L=\{3\}\):
\[
A=\begin{pmatrix}
a&b&c\\
b&e&d\\
c&d&z
\end{pmatrix},
\qquad b\ne0.
\]
The physical completion used in the overlap proof replaces the \(L\times L\)
entry by
\[
z_* = A[3,2]\,A[1,2]^{-1}\,A[1,3]={cd\over b}.
\]
Thus
\[
R=\begin{pmatrix}
a&b&c\\
b&e&d\\
c&d&cd/b
\end{pmatrix}.
\]
Direct expansion gives the exact factorization
\[
\boxed{\det R
 =-{(ad-bc)(bd-ce)\over b}.}
\]
Both factors may be nonzero. For example,
\[
(a,b,c,d,e)=(0,1,1,2,0)
\]
gives
\[
R=\begin{pmatrix}
0&1&1\\
1&0&2\\
1&2&2
\end{pmatrix},
\qquad
\det R=2.
\]
Hence \(\operatorname{rank}R=3=3r>2r\).

## Consequence for the proof graph

The tail estimate
\[
\|A-R\|_F^2\ge\sum_{j>3r}s_j(A)^2
\]
cannot in general be strengthened to a tail beginning after \(2r\) by a
rank-counting correction. At \(r=2\), the current method genuinely sees only
\(s_7,s_8,\ldots\), which is why the same-seed certificate
\[
\|D\|_F^2+\|E\|_F^2\ge s_7(A)^2+s_8(A)^2
\]
is the correct endpoint under \(s_8(A)\ge1\).

This does not rule out an \(s_8\) theorem. It shows that any such improvement
must use analytic information about the shared-coordinate receiver or an
alternative completion, rather than a formal improvement of the present rank
bound.

## Source pin

The audited completion appears in
\`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex\`
at commit \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\`.

The unrestricted three-eigenvalue conjecture remains open.
