# Selector barriers for the negative-target dependent-light shell fake

These are scoped obstructions to realizing the superlacunary shell construction of the [dependent-light fake](../20260923T192452Z-independent-hub-all-projections-fake/REPORT.md) from independent original coordinates. They do **not** rule out collective product constructions without identifiable original-coordinate shell selectors, and they do not prove the full quadratic-form density conjecture.

## One original-coordinate selector

Let \(U\) be an orthonormal three-frame and \(Z=U^\top X=(L,V,P)\), where the original scalar inputs \(X_i\) are independent with density caps \(1\), and every row \(u_i\) of \(U\) has squared norm at most \(1/2\). Fix one original coordinate \(X_i\). After conditioning on \(X_i=x\), the remaining random projection has covariance matrix for its frame
\[
C_i=I_3-u_i u_i^\top,\qquad
\det C_i=1-\|u_i\|^2\ge1/2.
\]
Normalize the remaining frame by \(C_i^{-1/2}\). The dimension-three Livshyts--Paouris--Pivovarov projection-density estimate \(2^{3/2}\), followed by the determinant change of variables, gives the uniform conditional density cap
\[
\|p_{Z\mid X_i=x}\|_\infty
\le 2^{3/2}(\det C_i)^{-1/2}\le4,
\tag{1}
\]
independently of \(x\).

Let \(S_k\) be disjoint measurable events determined by \(X_i\), with \(u_k=\Pr(S_k)\) and \(\sum_k u_k\le1\). The subdensity of \(Z\) contributed by \(S_k\) is pointwise at most \(4u_k\), because it is an average of the translated conditional densities (1).

For numbers \(a_k\in(0,1)\) and centers \(c_k\), consider exactly the fake's graph shells
\[
E_k=\left\{a_k\le l\le1,\quad 0\le v\le1,\quad
\left|p+c_k+\frac{1+v^2}{2l}\right|\le a_k/2\right\}.
\tag{2}
\]
Let \(H\) be independent of \(Z\), with any density bounded by \(1\), and put \(Q=2HL+V^2+2LP\). At target \(-1\), integrate out \(H\) using the slope \(2l\). The contribution from \(S_k\) and \(Z\in E_k\) is at most
\[
\int_{E_k}\frac{4u_k}{2l}\,dl\,dv\,dp
=2u_ka_k\log(1/a_k).
\]
Since \(a\log(1/a)\le1/e\),
\[
\sum_k p_{Q;\,S_k,\,E_k}(-1)\le\frac2e.
\tag{3}
\]
Thus one disjoint original-coordinate selector cannot reproduce the fake's divergent matched-shell contribution under the diffuse row-leverage gate. The same pointwise upper bound holds at every output target because only the cap on the independent hub density was used.

## Two independently matched selectors

Suppose a proposed construction requires disjoint label events \(S_k\) in one original coordinate and \(T_k\) in a different independent original coordinate. Put \(u_k=\Pr(S_k)\), \(v_k=\Pr(T_k)\); both sequences sum to at most \(1\). Suppose further that a positive fraction \(c\,a_k\) of light mass in the \(k\)-th shell is generated only when both labels equal \(k\). Independence then forces
\[
c\,a_k\le \Pr(S_k\cap T_k)=u_kv_k.
\tag{4}
\]
The entropy source driving the dependent fake is now bounded:
\[
\sum_k a_k\log(1/a_k)
\le\frac{2}{e\sqrt c}\sum_k\sqrt{u_kv_k}
\le\frac{2}{e\sqrt c}.
\tag{5}
\]
The first inequality uses \(a\log(1/a)\le(2/e)\sqrt a\); the second is Cauchy--Schwarz. Thus the reported divergent-entropy shell sequence cannot be produced by two independent disjoint matched labels while retaining shell masses comparable below to their thicknesses.

The assumptions in the two statements are deliberately explicit. A product projection might create curved shells through diffuse interactions without a single readable selector or two exactly matched selectors. Neither argument excludes that possibility.
