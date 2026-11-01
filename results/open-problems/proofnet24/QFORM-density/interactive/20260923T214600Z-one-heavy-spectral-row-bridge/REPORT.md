# A quantitative one-heavy-row bridge in exact rank three

**Status:** Proved sufficient case, uniform in dimension, arbitrary original-coordinate cap-one laws, spectral signs, and within-bank interactions. Its bound deteriorates as a physical eigenbasis row approaches an exact coloop. The separate exact-coloop theorem covers the endpoint, but the intermediate small-leakage problem remains open.

## Statement

Let \(A=U\Lambda U^\top\) be symmetric of **exact rank three**, \(U^\top U=I_3\), and every nonzero eigenvalue have absolute value at least one. Fix a physical row \(h\) and \(0<\eta\le1\). Suppose its eigenbasis leverage \(d_h=\|U_{h,*}\|_2^2\le1-\eta\), while every other physical row has leverage \(d_i\le\kappa:=\eta^2/24\). Then for independent original-coordinate real inputs with densities at most one,
\[
 \|p_{X^\top A X}\|_\infty
 \le \frac{40\sqrt e}{3^{1/10}\eta}.
 \tag{1}
\]
The estimate is also insensitive to arbitrary measurable functions of each of the two physical-coordinate banks separately, and thus allows arbitrary affine terms and within-bank quadratic terms.

## A physical cut preserving the two-dimensional residual

Let \(u_i=U_{i,*}^\top\), \(G_0=\sum_{i\ne h}u_i u_i^\top=I_3-u_hu_h^\top\succeq\eta I_3\). Independently assign each \(i\ne h\) to \(I_0\) or \(J\) with probability \(1/2\), and place \(h\) in \(I=I_0\cup\{h\}\). Then
\[
 \mathbb E\|G_{I_0}-G_0/2\|_F^2
 =\tfrac14\sum_{i\ne h}d_i^2
 \le\tfrac34\kappa\le\eta^2/32<\eta^2/16.
\]
Therefore some cut has \(\|G_{I_0}-G_0/2\|_{\rm op}<\eta/4\), whence \(G_{I_0},G_J\succeq(\eta/4)I_3\). Also \(G_I=G_{I_0}+u_hu_h^\top\succeq(\eta/4)I_3\).

The cross matrix \(M=A[I,J]=U_I\Lambda U_J^\top\) obeys
\[
 Z_3(M)=\det(\Lambda)^2\det(G_I)\det(G_J)
 \ge(\eta/4)^6.
 \tag{2}
\]
Deleting its physical \(h\) row gives \(M_0=A[I_0,J]=U_{I_0}\Lambda U_J^\top\). All three nonzero singular values of \(M_0\) are at least \(\eta/4\), so
\[
 Z_2(M_0)=\sum_{k<l}s_k(M_0)^2s_l(M_0)^2
 \ge3(\eta/4)^4.
 \tag{3}
\]

## Verifying both volume-leverage gates

For any rank-\(r\) rectangular matrix \(B\), its squared-\(k\)-minor row-inclusion probability \(\alpha_i^{(k)}(B)\) is no greater than the row-space projection leverage \(\Pi_{ii}\), with \(\Pi\) the orthogonal projector onto \(\operatorname{col}(B)\). To see this, expand the squared minor sums in an SVD \(B=U_B\Sigma V_B^\top\): orthogonality of the right singular-vector minors makes the distribution a mixture over \(k\)-subsets \(K\) of singular directions with weights proportional to \(\prod_{j\in K}s_j(B)^2\). Conditional on \(K\), the physical row-inclusion chance equals \(\sum_{j\in K}U_B(i,j)^2\le\sum_{j=1}^r U_B(i,j)^2=\Pi_{ii}\).

For both \(M\) and \(M_0\), the column spaces are exactly the ranges of \(U_I\) and \(U_{I_0}\), respectively, since \(\Lambda\) and \(U_J^\top\) have rank three. Hence for each \(i\in I_0\),
\[
 \alpha_i^{(3)}(M)\le u_i^\top G_I^{-1}u_i
 \le4\kappa/\eta,
 \qquad
 \alpha_i^{(2)}(M_0)\le u_i^\top G_{I_0}^{-1}u_i
 \le4\kappa/\eta=\eta/6\le1/2.
 \tag{4}
\]
No leverage restriction is needed on the single distinguished row \(h\).

The proved one-concentrated-row mixed-volume theorem for the physical cut therefore applies:
\[
 \|p\|_\infty\le10\sqrt e\,[Z_3(M)Z_2(M_0)]^{-1/10}.
\]
Substitute (2)–(3) to obtain \(10\sqrt e\,[3(\eta/4)^{10}]^{-1/10}=40\sqrt e\,3^{-1/10}/\eta\), proving (1).

The condition on all other leverages becomes stronger as \(\eta\downarrow0\), and the quantitative bound diverges. No continuity of the density norm at \(\eta=0\) follows from this Fourier-volume estimate.
