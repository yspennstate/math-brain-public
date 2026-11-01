# Quantitative physical near-coloop from a small third cross-volume

## Statement

Let \(A=U\Lambda U^{\mathsf T}\) be a real symmetric matrix of **exact rank three**, where \(U^{\mathsf T}U=I_3\) and \(\Lambda\) is an invertible symmetric \(3\times3\) matrix with \(s_3(\Lambda)=s_3(A)\geq1\). Assume the physical-coordinate no-pivot condition

\[
 |a_{ii}|<c=1/64,\qquad
 |a_{ii}a_{jj}-a_{ij}^{2}|<c\quad(i\ne j).
\tag{N3}
\]

Let \(V_3(A)=\sum_{S\cap T=\varnothing,\ |S|=|T|=3}\det A[S,T]^2\), where the pair of triples is ordered. Write \(u_i\in\mathbb R^3\) for row \(i\) of \(U\), \(\ell_i=\|u_i\|^2\), and \(m=\max_i\ell_i\). Then

\[
 p:=\frac{V_3(A)}{\det(\Lambda)^2}
 \geq \kappa(1-m),
 \qquad
 \kappa:=
 \frac{(1-\tau_3)^2}{1+4/(1-\tau_6)}
 >0.04367,
\tag{1}
\]
where
\[
 d=\sqrt{c+c^2}=\frac{\sqrt{65}}{64},\qquad
 \tau_k=c+(k-1)d,
 \quad \tau_3=0.2675705546\ldots,\quad
 \tau_6=0.6454888866\ldots .
\]
In particular, some **original coordinate** \(h\) satisfies
\[
 \|u_h\|^2\geq
 1-22.897\,\frac{V_3(A)}{\det(\Lambda)^2}
 \geq1-22.897\,V_3(A).
\tag{2}
\]
The final inequality uses \(|\det\Lambda|\geq1\); if its right side is negative, the assertion remains formally true.

This is uniform in the size and condition number of \(\Lambda\). The proof does not rotate the independent random input variables.

## Proof

From (N3), \(|a_{ij}|\leq d\) for \(i\ne j\). Consequently, every physical principal block on \(k\) indices obeys
\[
 \|A_{WW}\|_{\rm op}\leq\tau_k=c+(k-1)d.
\tag{3}
\]

**Two-frame-direction lemma.** For every coordinate set \(W\),
\[
 \lambda_2(G_W)\leq \|A_{WW}\|_{\rm op}/s_3(A),
 \qquad G_W:=U_W^{\mathsf T}U_W .
\tag{4}
\]
To see this, take the singular value decomposition of \(U_W\) and let \(E\subset\mathbb R^3\) be the span of its top two right singular vectors. In an orthonormal basis adapted to \(E\), the matrix \(\Lambda-P_E\Lambda P_E\) has block form \(\left(\begin{smallmatrix}0_{2\times2}&b\\b^{\mathsf T}&a\end{smallmatrix}\right)\) and rank at most two. The Eckart–Young variational characterization therefore gives \(\|P_E\Lambda P_E\|\geq s_3(\Lambda)\). On the top two left singular directions of \(U_W\), the corresponding compression of \(A_{WW}\) is \(D(P_E\Lambda P_E)|_E D\), with \(D=\operatorname{diag}(\sqrt{\lambda_1(G_W)},\sqrt{\lambda_2(G_W)})\). Since \(\|D^{-1}\|^2=1/\lambda_2(G_W)\), its norm is at least \(\lambda_2(G_W)s_3(A)\). If \(\lambda_2(G_W)=0\), (4) is immediate. Equations (3)–(4) give \(\lambda_2(G_S)\leq\tau_3\) for every triple and \(\lambda_2(G_{S\cup T})\leq\tau_6<1\) for any two triples.

Projection-DPP volume sampling chooses a triple \(S\) with probability \(\det(U_S)^2\). Cauchy–Binet says this is a probability measure, its one-point inclusion probability is \(\Pr(i\in S)=\ell_i\), and for independent draws \(S,T\),
\[
 p=\Pr(S\cap T=\varnothing)=\mathbb E_S\det(I-G_S).
\tag{5}
\]
The determinant identity is Cauchy–Binet applied to \(U_{S^c}\); it also follows directly from the earlier DPP_THIRD_VOLUME.md note. Put \(\delta_S=1-\lambda_1(G_S)\). Since \(0\preceq G_S\preceq I\) and its other two eigenvalues are at most \(\tau_3\),
\[
 p\geq(1-\tau_3)^2\,\mathbb E\delta_S.
\tag{6}
\]

For two sampled triples \(S,T\), set \(W=S\cup T\) and take unit top eigenvectors \(v_S,v_T,w\) of \(G_S,G_T,G_W\), respectively. As \(G_S,G_T\preceq G_W\preceq I\) and \(\lambda_2(G_W)\leq\tau_6\),
\[
 \sin^2\angle(v_S,w)\leq\frac{\delta_S}{1-\tau_6},
 \qquad
 \sin^2\angle(v_T,w)\leq\frac{\delta_T}{1-\tau_6}.
\tag{7}
\]
The operator-norm identity \(\|vv^{\mathsf T}-zz^{\mathsf T}\|=\sin\angle(v,z)\) and the triangle inequality show
\[
 1-\langle v_S,v_T\rangle^2
 \leq
 \frac{2(\delta_S+\delta_T)}{1-\tau_6}.
\tag{8}
\]
This bound is valid even when its right side exceeds one; any choices of eigenvectors suffice in a degenerate case. As \(G_T\succeq(1-\delta_T)v_Tv_T^{\mathsf T}\),
\[
 v_S^{\mathsf T}G_Tv_S
 \geq
 1-\delta_T-
 \frac{2(\delta_S+\delta_T)}{1-\tau_6}.
\tag{9}
\]
On the other hand, the DPP one-point marginals and Parseval give
\[
 \mathbb E_T G_T
 =\sum_i\ell_i u_i u_i^{\mathsf T}
 \preceq m\sum_i u_i u_i^{\mathsf T}
 =mI_3.
\tag{10}
\]
Average (9) first over independent \(T\), then over \(S\), and use (10). This yields
\[
 1-m\leq\left(1+\frac4{1-\tau_6}\right)\mathbb E\delta_S.
\tag{11}
\]
Combining (6) and (11) proves (1). Numerically \(\kappa=0.0436739067\ldots\), hence \(1/\kappa=22.89696698\ldots\).

## What this does and does not pay

At \(V_3=0\), equation (2) gives \(\ell_h=1\), an actual physical coloop; the existing exact matroid classification and one-hub coarea proof pay this branch. At small positive \(V_3\), (2) supplies a **quantitative physical near-coloop**, even for unbounded eigenvalue ratios. For example \(V_3(A)\leq10^{-3}\) gives \(\ell_h>0.9771\).

A high leverage \(h\) does **not** imply there is a set of low total frame energy whose deletion makes \(h\) an exact coloop. The small transverse frame component may overlap many original coordinates that carry the other two full frame directions. The rank-preserving deletion receiver applies only if such a deletion set is independently found. Further analytic control of overlapping light terms is needed to turn (2) alone into a uniform output-density estimate. Likewise, this report addresses exact rank three; it makes no assertion about matrices with extra nonzero eigenvalues.

Separately, a physical principal \(3\times3\) block with \(s_3\geq\sigma>0\) gives a density receiver of size \(<18/\sigma\) by conditioning on other original coordinates, exterior coarea, and Gaussian domination of the central ball. Thus any future structural dichotomy can route a substantial physical core directly to a solved receiver.

## Related notes

- Exact DPP identity: `20260923T191500Z-rank-preserving-near-coloop/DPP_THIRD_VOLUME.md`.
- Exact rank-three/no-crosscut classification: `20260923T190200Z-rank3-matroid-crosscut/REPORT.md`.
- Exact rank-three physical coloop analytic receiver: `20260923T191000Z-small-hub-square-coarea/GENERAL_3D_CORE.md`.
- Rank-preserving deletion receiver under a separately certified low-frame-energy deletion: `20260923T191500Z-rank-preserving-near-coloop/REPORT.md`.
