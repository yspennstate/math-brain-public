# Hub lookup Hessian: an exact product-coordinate curvature identity

Date: 2026-09-23 UTC.

This algebraic note is a potential input to an arbitrary-target estimate; it is **not** such an estimate and does **not** settle the mixed-sign density problem.

Let \(L(Y)=a\cdot Y\), \(V(Y)=v\cdot Y\), \(P(Y)=p\cdot Y\) for original independent real coordinates \(Y_i\), with \(a,v\) orthonormal. The hub lookup for
\(Q=2HL+\beta L^2+V^2+2\varepsilon LP\) at target \(s\), on the region \(L\ne0\), is
\[
 g_s(Y)=\frac{s-\beta L^2-V^2-2\varepsilon LP}{2L}
       =\frac{s-V^2}{2L}-\frac{\beta}{2}L-\varepsilon P.
 \tag{1}
\]
Thus its entire Hessian in the physical \(Y_i\) coordinates is independent of \(\beta,\varepsilon,p\). In particular, every four-corner mixed difference in distinct physical inputs cancels both additive terms exactly.

Define \(m_i=L v_i-V a_i\). Direct differentiation gives, for all \(i,j\),
\[
 \partial_i\partial_j g_s
 =\frac{s a_i a_j-m_i m_j}{L^3}.
 \tag{2}
\]
Indeed the Hessian of \((s-V^2)/(2L)\) in \((L,V)\) is
\[
 \begin{pmatrix}
  (s-V^2)/L^3 & V/L^2\\
  V/L^2 & -1/L
 \end{pmatrix}.
 \tag{3}
\]

Let \(T\) denote the numerator matrix in (2). With \(U\) the \(n\times2\) matrix whose columns are \(a,v\),
\[
 T=UCU^\top,\qquad
 C=\begin{pmatrix}s-V^2&LV\\LV&-L^2\end{pmatrix}.
 \tag{4}
\]
Since \(U^\top U=I_2\),
\[
 \|T\|_F^2=\|C\|_F^2=(s-V^2)^2+2L^2V^2+L^4\ge L^4.
 \tag{5}
\]
Write \(\kappa=\max_i(a_i^2+v_i^2)\). For each diagonal entry,
\[
 |T_{ii}|\le\|C\|_F(a_i^2+v_i^2)\le\kappa\|C\|_F.
\]
Using \(\sum_i(a_i^2+v_i^2)=2\), it follows that
\[
 \sum_i T_{ii}^2\le2\kappa\|T\|_F^2.
\]
Consequently, if \(\kappa<1/2\), the physical off-diagonal Hessian obeys
\[
 \sum_{i\ne j}|\partial_i\partial_j g_s|^2
 \ge\frac{(1-2\kappa)\|T\|_F^2}{|L|^6}
 \ge\frac{1-2\kappa}{L^2}.
 \tag{6}
\]
At \(\kappa\le1/4\), this is at least \(1/(2L^2)\), uniformly in \(s,V,\beta,\varepsilon\). On a dyadic strip \(|L|\asymp r\), it identifies aggregate mixed curvature at scale \(1/r\) even with an arbitrarily correlated linear \(P\).

**What (6) does not prove.** A pointwise Frobenius lower bound need not produce a lower bound for any particular finite rectangle difference: the Hessian can change sign across that rectangle. Moreover, the information that all four hub-lookup values belong to an arbitrary fragmented Borel set \(E\) gives a restriction in \(E-E-E+E\), whose Lebesgue measure is not controlled by \(|E|\). Turning (6) into the needed dyadic restricted weak-\(L^2\) inequality therefore requires an additional argument that preserves the additive energy of \(E\) or another direct measure bound. No such argument is established here.
