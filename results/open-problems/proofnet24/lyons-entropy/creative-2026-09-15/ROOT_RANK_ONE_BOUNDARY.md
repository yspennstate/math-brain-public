# A comparable-scale neighborhood of every fully supported rank-one three-site face

Root constructive proof, 2026-09-15. This concerns a simultaneous two-eigenvalue degeneracy left outside ROOT_RANK_TWO_SUPPORT.md. It is a restricted boundary theorem, not a full three-site or full Lyons proof. Historical priority is not claimed.

## Statement

Let \(u\in\mathbb C^3\) be a unit vector with every coordinate nonzero, \(Q=uu^*\), \(P=I-Q\), and \(0<p<1\). Let \(J=PJP\) be positive definite on \(u^\perp\). Then the full real nine-dimensional entropy Hessian is negative definite at
\[
K_\epsilon=pQ+\epsilon J
\]
for all sufficiently small positive \(\epsilon\). The conclusion is uniform when \(p\), the three \(|u_i|\), and the two eigenvalues of \(J|_{u^\perp}\) stay in fixed compact subsets of their permitted positive ranges. Hence it includes conical interior tubes with two small comparable eigenvalues, varying eigenvectors, and arbitrary Hermitian directions. It does not assert a whole interior neighborhood allowing an unbounded ratio of the two small eigenvalues. Complementation gives the corresponding rank-one hole family.

## 1. Gauge and tangent decomposition

A fixed diagonal unitary changes no occupation probabilities, so take every \(u_i>0\). Choose a real orthonormal basis of \(u^\perp\). Decompose a Hermitian direction as
\[
A=aQ+uv^*+vu^*+B,\qquad v\perp u,\quad B=PBP.
\]
In the chosen real two-dimensional basis write
\[
B=S+i b\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad S=S^T\in\mathbb R^{2\times2},\quad b\in\mathbb R.
\]
Thus
\[
\operatorname{tr}B=\operatorname{tr}S,\quad
\det B=\det S-b^2,\quad
\|A\|_F^2=a^2+2\|v\|^2+\|S\|_F^2+2b^2.
\]
Put \(d=\det(J|_{u^\perp})\) and, for \(i<j\),
\[
w_{ij}=u_j e_i-u_i e_j,\qquad c_{ij}(B)=w_{ij}^*B w_{ij}.
\]
Each \(w_{ij}\) belongs to the real plane \(u^\perp\). Consequently \(c_{ij}(B)=c_{ij}(S)\), and \(c_{ij}(J)>0\).

The quadratic form
\[
F_J(S)=\sum_{i<j}\frac{c_{ij}(S)^2}{c_{ij}(J)}
\]
is positive definite on the three-dimensional space of real symmetric supported matrices. Indeed the three lines spanned by \(w_{12},w_{13},w_{23}\) are pairwise distinct because every \(u_i\ne0\). A nonzero real homogeneous binary quadratic polynomial has at most two distinct zero lines. Hence vanishing of all three evaluations forces \(S=0\). On compact parameter families there is a uniform \(\lambda>0\) with \(F_J(S)\ge\lambda\|S\|_F^2\).

## 2. Exact atom asymptotics and their derivatives

Write \(p_T\) for the exact subset probabilities. At \(pQ\), the four positive atoms are
\[
p_\varnothing=1-p,\qquad p_{\{i\}}=p u_i^2.
\]
At \(K_\epsilon\), the other four atoms have the exact formulas
\[
p_{ij}=\epsilon p c_{ij}(J)+\epsilon^2(\det J_{ij}-pd),\qquad
p_{123}=\epsilon^2pd.\tag{1}
\]
The pair formula follows from \(\det (pQ+\epsilon J)_{ij}-\det(pQ+\epsilon J)\). The four regular atoms stay uniformly positive on the stated compact families.

Differentiation in the fixed affine direction \(A\) gives
\[
Dp_{ij}(K_\epsilon)[A]=p c_{ij}(S)+O(\epsilon\|A\|_F).
\tag{2}
\]
At the rank-one base, the second derivatives are
\[
D^2p_{123}(pQ)[A,A]=2p\det B,\qquad
D^2p_{ij}(pQ)[A,A]=2\det A_{ij}-2p\det B.\tag{3}
\]
These follow from \(D^2\det K[A,A]=2\operatorname{tr}(K\operatorname{adj}A)\), and the compression identity \(u^*\operatorname{adj}A\,u=\det B\). Their errors at \(K_\epsilon\) are \(O(\epsilon\|A\|_F^2)\).

## 3. The singular Hessian bound

Let \(L=\log(1/\epsilon)\). The entropy identity is
\[
H''=-\sum_T\frac{(Dp_T[A])^2}{p_T}-\sum_TD^2p_T[A,A]\log p_T.
\]
By (1)-(2), the three pair Fisher terms obey, uniformly for small \(\epsilon\),
\[
\sum_{i<j}\frac{(Dp_{ij}[A])^2}{p_{ij}}
\ge \frac{p}{2\epsilon}F_J(S)-C\epsilon\|A\|_F^2.\tag{4}
\]
For example use \((x+y)^2\ge(3/4)x^2-3y^2\) and \(p_{ij}\le(3/2)\epsilon p c_{ij}(J)\), decreasing the radius if needed. The nonnegative triple Fisher term can be discarded in an upper bound.

The pair logarithms are \(-L+\log(pc_{ij}(J))+O(\epsilon)\), while the triple logarithm is exactly \(-2L+\log(pd)\). Their total growing contribution, by (3), is
\[
2L\left[\sum_{i<j}\det A_{ij}-p\det B\right]
=2L\left[a\operatorname{tr}S+(1-p)(\det S-b^2)-\|v\|^2\right].\tag{5}
\]
Here \(\sum_{i<j}\det A_{ij}=a\operatorname{tr}B+\det B-\|v\|^2\) is the second elementary-symmetric identity in the block decomposition. In particular the two simultaneously vanishing spectral eigenvalues do not leave an uncontrolled imaginary supported direction: its coefficient is \(-2(1-p)Lb^2\).

The four regular atoms contribute a bounded quadratic form converging uniformly to their rank-one-base expression. The constant parts of the singular logarithms also give bounded quadratic forms. Collect these into \(R(A)\). Crucially,
\[
R(aQ)=-\frac{a^2}{p(1-p)}.\tag{6}
\]
For that direction all determinant second derivatives vanish and the only limiting nonzero scores belong to the four regular atoms. Equations (4)-(6) prove
\[
\begin{aligned}
H''\le{}&-\frac{p}{2\epsilon}F_J(S)
+2L\left[a\operatorname{tr}S+(1-p)\det S-(1-p)b^2-\|v\|^2\right]\\
&+R(A)+O\bigl(\epsilon(1+L)\|A\|_F^2\bigr).\tag{7}
\end{aligned}
\]
The finite form \(R\) and error constants are uniform on compact parameter families; every expression above is a finite polynomial or logarithm with the displayed positive leading coefficients.

## 4. Absorption and conclusion

Let \(c=1/[p(1-p)]\). Because \(R\) is bounded and has the strictly negative restriction (6), there is a finite constant \(C_1\) such that
\[
R(A)\le-\tfrac c2 a^2+C_1(\|S\|_F^2+b^2+\|v\|^2).
\tag{8}
\]
This follows by bounding all mixed terms with \(a\) using Young's inequality; all other terms are bounded on the complementary subspace.

The only growing mixed term satisfies
\[
2L|a\operatorname{tr}S|
\le\frac{p\lambda}{8\epsilon}\|S\|_F^2
+\frac{16\epsilon L^2}{p\lambda}a^2.\tag{9}
\]
Also \(2(1-p)L\det S\le(1-p)L\|S\|_F^2\). Since \(\epsilon L\to0\), \(\epsilon L^2\to0\), and \(L\to\infty\), substituting (8)-(9) into (7) gives, after decreasing \(\epsilon_0>0\),
\[
\boxed{H''\le-\frac c4a^2-\frac{p\lambda}{4\epsilon}\|S\|_F^2
-(1-p)Lb^2-L\|v\|^2<0\quad(A\ne0).}\tag{10}
\]
All choices can be made uniformly on the compact families in the statement. Normalizing the two small eigenvalues by their larger value writes every bounded-ratio approach in this form. Spectral projections vary continuously because the surviving eigenvalue stays separated from zero, so varying \(u\) and \(J\) are included in those conical tubes.

The proof supplies all nine real modes: one finite supported-population mode, three pair-Fisher modes of order \(1/\epsilon\), one imaginary supported mode of order \(\log(1/\epsilon)\), and four eigenvector-mixing modes of that logarithmic order. No numerical samples are used as a universal sign argument. The remaining boundary obligations include non-full support of \(u\), unbounded separation between the two small eigenvalues, and simultaneous approaches to both zero and one.

## Reproducible numerical diagnostic

ROOT_RANK_ONE_BOUNDARY_check.py evaluates the analytically scaled nine-dimensional Hessian without subtracting nearly equal full determinants. For u=(1,2,2)/3, p=0.4, and a complex positive supported J, the largest eigenvalue of the limiting form is -0.1367631652. At epsilon=10^-3,10^-6,10^-12,10^-24, all four scaled Hessians are negative definite and their operator distances to the limit are approximately 1.1208,0.5603,0.2802,0.1401. ROOT_RANK_ONE_BOUNDARY_results.json preserves the output. These are finite floating-point diagnostics, separate from the proof above.
