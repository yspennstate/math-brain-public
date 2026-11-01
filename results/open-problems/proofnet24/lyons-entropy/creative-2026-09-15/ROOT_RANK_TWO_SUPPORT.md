# Entropy concavity on every two-dimensional support, with a generic three-site boundary consequence

Root constructive proof, 2026-09-15. This strengthens ROOT_RANK_TWO_SPECTRAL.md from commuting eigenvalues to every Hermitian direction on a fixed two-dimensional support. No claim of historical priority or full Lyons concavity is made.

## 1. Full support theorem

Let \(V:\mathbb C^2\to\mathbb C^n\) be any isometry. Then
\[
\boxed{M\longmapsto H(P_{VMV^*})\text{ is concave on }0\le M\le I_2.}\tag{1}
\]
The eigenvectors of \(M\) may vary. Thus arbitrary noncommuting endpoints whose combined support is at most two-dimensional are covered. Complementation and C040's projection-block substitutions preserve the result.

At a strict \(2\times2\) base \(M\), for any Hermitian direction \(A\) with \(\delta=\det A>0\),
\[
\boxed{D^2H[A,A]\le-(8-2\log2)\delta<0.}\tag{2}
\]
For two actual measured coordinates the stronger prior constant \(8\delta\) is recovered.

## 2. Exact occupation law and curvature

Write \(v_i\) for row \(i\) of \(V\), and put
\[
t_i=\|v_i\|^2,\quad s_i=t_i/2,\quad
r_{ij}=|\det V_{\{i,j\}}|^2,\quad
d=\det M,\quad d_0=\det(I-M),\quad B=M-dI.
\]
The \(s_i\) form a probability law, the \(r_{ij}\) form a probability law on pairs, and
\(\sum_{j\ne i}r_{ij}=t_i\). If \(0<M<I\), then \(B>0\), since for the two eigenvalues \(p,q\), its eigenvalues are \(p(1-q),q(1-p)\).

The only positive-size atoms are
\[
p_\varnothing=d_0,\qquad p_i=v_i Bv_i^*,\qquad p_{ij}=d r_{ij}.\tag{3}
\]
This follows from the spectral projection expansion or from inclusion moments. Coordinates with zero rows and pairs with zero minors are fixed zero atoms and can be omitted.

Along \(M+\tau A\),
\[
p_\varnothing''=2\delta,\quad p_i''=-2\delta t_i,\quad
p_{ij}''=2\delta r_{ij}.
\]
Consequently, with \(\mathcal I=\sum(p'_S)^2/p_S\),
\[
H''=-\mathcal I+2\delta\Lambda,\qquad
\Lambda=\sum_{i<j:r_{ij}>0}
r_{ij}\log\frac{p_i p_j}{d_0d r_{ij}}.\tag{4}
\]
Indeed the degree identity for \(r\) converts the singleton terms exactly.

The determinant identity \(\det B=dd_0\) and the two-row Gram determinant give
\[
p_i p_j-dd_0r_{ij}=|v_i Bv_j^*|^2\ge0.\tag{5}
\]
Thus \(\Lambda\ge0\). Equations (4)-(5) prove \(H''\le0\) whenever \(\delta\le0\). This includes every indefinite direction and the affine-probability rank-one case.

## 3. Controlling every definite direction

Let \(f_1=\operatorname{tr}B\), \(\nu_i=p_i/f_1\), and
\[
T=\frac{f_1}{2\sqrt{dd_0}}\ge1.
\]
The inequality follows from \(f_1=p(1-q)+q(1-p)\) and
\(f_1^2-4dd_0=(p-q)^2\).

Fairly order a pair with law \(r\). The ordered law has entropy \(H(r)+\log2\) and both marginals \(s\). Subadditivity therefore gives
\[
H(r)+\log2\le2H(s).
\]
Put \(\beta_*=2H(s)-H(r)\), so \(\beta_*\ge\log2\). Rewriting (4) yields the exact identity
\[
\Lambda
=2\log(2T)-\beta_*-2D(s\Vert\nu)
\le2\log T+\log2.\tag{6}
\]
All divergences are finite on the retained coordinates. No assumption that \(s=\nu\), or that the eigenvectors have equal moduli, is used.

For \(\delta>0\), reverse the sign of \(A\) if necessary so that \(A>0\). The empty and all pair atoms alone supply
\[
\mathcal I\ge
\frac{(\operatorname{tr}(\operatorname{adj}M)A)^2}{d}
+\frac{(\operatorname{tr}(\operatorname{adj}(I-M))A)^2}{d_0}.
\]
Define \(P=\operatorname{adj}M/\sqrt d\) and
\(Q=\operatorname{adj}(I-M)/\sqrt{d_0}\). They are positive matrices with determinant one. Cauchy-Schwarz and the two-dimensional trace-determinant inequality give
\[
\begin{aligned}
\mathcal I
&\ge(\operatorname{tr}PA)^2+(\operatorname{tr}QA)^2\\
&\ge\tfrac12[\operatorname{tr}(P+Q)A]^2
\ge2\det(P+Q)\det A
=4(1+T)\delta.\tag{7}
\end{aligned}
\]
The last identity is \(\det(P+Q)=2+2T\), the same elementary identity used in the prior two-coordinate proof. It depends only on \(M\), not on its embedding \(V\).

Combining (4), (6), and (7),
\[
H''\le-4\delta[1+T-\log T-\tfrac12\log2]
\le-(8-2\log2)\delta,
\]
since \(1+T-\log T\ge2\). This proves (2). The better expression retaining \(\beta_*\) is
\(H''\le-[8-4\log2+2\beta_*]\delta\).
For a square isometry \(V\), \(s=(1/2,1/2)\) and \(H(r)=0\), giving the prior constant \(8\).

Together with the indefinite case, the Hessian is nonpositive in every direction. Integration proves (1) for strict endpoints; replacing \(M\) by \((1-2\epsilon)M+\epsilon I_2\) and passing to the limit proves the closed-contraction statement. Impossible higher-cardinality atoms remain zero throughout and are never assigned a frozen infinite logarithm.

## 4. Explicit support-tangent gap when Lambda is positive

Let \(C=8-2\log2\). The count statistic has variance at most \(1/2\), so
\(\mathcal I\ge2(\operatorname{tr}A)^2\). Also
\(2\det A=(\operatorname{tr}A)^2-\|A\|_F^2\).

If \(\delta\le0\), (4) implies
\[
-H''\ge2(\operatorname{tr}A)^2
+\Lambda[\|A\|_F^2-(\operatorname{tr}A)^2]
\ge\min(2,\Lambda)\|A\|_F^2.
\]
If \(\delta\ge0\), combine the two lower bounds
\(-H''\ge C\delta\) and
\(-H''\ge2(\operatorname{tr}A)^2-2\delta\Lambda\).
Weight the second by \(C/(C+2\Lambda)\) and the first by its complementary weight. The determinant terms cancel, and
\[
-H''\ge\frac{2C}{C+2\Lambda}(\operatorname{tr}A)^2
\ge\frac{2C}{C+2\Lambda}\|A\|_F^2.
\]
Therefore if \(\Lambda>0\),
\[
\boxed{-H''\ge
\min\left(\Lambda,\frac{2C}{C+2\Lambda}\right)\|A\|_F^2.}\tag{8}
\]

For three sites, suppose the one-dimensional orthogonal complement of the support is spanned by \(w\), and all \(w_i\ne0\). Complementary minors give \(r_{ij}=|w_k|^2>0\), so all three row vectors are nonzero. If \(\Lambda=0\), (5) would make the three nonzero vectors \(v_iB^{1/2}\) pairwise orthogonal in a two-dimensional space, which is impossible. Hence \(\Lambda>0\) for EVERY strict covariance on this support, not just scalar covariances.

## 5. Consequence for the three-site spectral boundary

C019 proves the general simple-zero-eigenvalue Hessian expansion for
\(K_\epsilon=J+\epsilon ww^*\), where \(J\) is positive on \(w^\perp\) and has eigenvalues below one. Write
\(A=a ww^*+wv^*+vw^*+B\), \(B\) supported on \(w^\perp\).
Its divergent terms are
\[
-\frac{\det(J|_{w^\perp})}{\epsilon}a^2
+2\det(J|_{w^\perp})\log(1/\epsilon)\,
a\,\operatorname{tr}((J|_{w^\perp})^{-1}B)
-2\det(J|_{w^\perp})\log(1/\epsilon)\,
v^*(J|_{w^\perp})^{-1}v,
\]
plus a bounded quadratic form whose restriction to \(B\) is precisely the face entropy Hessian, and the stated vanishing remainder.

When all \(w_i\ne0\), (8) supplies a strict face gap for every such \(J\). Young inequalities absorb the mixed terms: the normal-to-face cross term costs \(O(\epsilon\log^2(1/\epsilon))\|B\|^2\), and bounded \(v\)-to-face terms cost \(O(1/\log(1/\epsilon))\|B\|^2\). These tend to zero; the remaining normal and off-support terms have strict negative coefficients. Therefore
\[
\boxed{\text{Every generic rank-two three-site boundary point has a full-dimensional
interior neighborhood with negative-definite entropy Hessian.}}\tag{9}
\]
Here “generic” means precisely a simple zero eigenvalue, both other eigenvalues in \((0,1)\), and a null vector with every coordinate nonzero. The statement is uniform on compact families satisfying quantitative versions of those conditions, because the face gap (8), the positive proper-atom minima, and C019's expansion constants vary continuously there. Nearby eigenvectors and supported covariances are included by the same uniform bounds. Complementation gives the simple-one-eigenvalue case.

This extends C019's previously proved neighborhoods near scalar rank-two faces to all the specified rank-two faces. No assertion is made for null vectors with zero coordinates, simultaneous spectral degeneracies, a global numerical radius, or the entire three-site interior.

## Sources and scope

The proof combines the prior two-coordinate extreme-Fisher argument (PRIOR_PARTIAL_RESULTS.md section 1), the rank-two projection pair-entropy observation developed in C069 and the root notes, and C019's explicit general boundary expansion. It does not rotate an arbitrary measured kernel without accounting for the changed occupation law: equations (3)-(6) are the required arbitrary-isometry calculation.

C040 implies the exact lifted corollary
\(K^\#=P_L+J(VMV^*)J^*\): its entropy differs by an affine function of \(M\), so the entire noncommuting support theorem is preserved. This gives higher-rank encoded families; arbitrary projection backgrounds remain outside the theorem. Root notes are not counted as additional agent executions.
