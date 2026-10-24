# A pure linear subsource is enough

**Status:** Strengthens the disjoint-linear-source theorem. The coordinates outside the pure subsource may contribute to all three light projections and may have arbitrary fragmented, infinite-variance laws.

Let \(H,X_1,\ldots,X_n\) be independent real variables with density caps one, let \(\ell,v,p\) be orthonormal coefficient vectors, and set \(L=\ell\cdot X\), \(V=v\cdot X\), \(P=p\cdot X\). Suppose some source set \(S\subset\{1,\ldots,n\}\) satisfies
\[
 v_i=p_i=0\ (i\in S),\qquad
 c=\|\ell_S\|_2>0.
\]
Then for all \(\beta,\varepsilon\in\mathbb R\),
\[
 \bigl\|p_{2HL+\beta L^2+V^2+2\varepsilon LP}\bigr\|_\infty
 \le {\sqrt2\over c}(7.2+2\log16)<{19\over c}.
\tag{1}
\]

**Proof.** Write \(T=S^c\). Conditional on \(X_T\), the three numbers \(l_T=\ell_T\cdot X_T\), \(v_T=v\cdot X_T\), and \(p_T=p\cdot X_T\) are fixed. The variable \(L'=L_S+l_T\) is independent of \(H\) and has a density bounded by \(\sqrt2/c\) by the one-dimensional product projection estimate. The conditional quadratic is
\[
 2(H+\varepsilon p_T)L'+\beta(L')^2+v_T^2.
\]
Put \(Y=(\sqrt2/c)L'\); it has density at most one. In the independent original pair \((H,Y)\), the indefinite quadratic preceding \(v_T^2\) has matrix
\[
 \begin{pmatrix}0&c/\sqrt2\\c/\sqrt2&\beta c^2/2\end{pmatrix},
\]
determinant \(-c^2/2\), and critical value zero after translating \(H\) by \(\varepsilon p_T\). The hyperbolic envelope from `geometry.tex`, Theorem `geom:pair`, therefore bounds its conditional density at \(u\ne0\) by
\[
 {\sqrt2\over c}\left(5.2+
   \log_+\frac{16c/\sqrt2}{|u|}\right)
 \le {\sqrt2\over c}\left(5.2+
   \log_+\frac{16}{|u|}\right),
\]
uniformly in \(X_T,\beta,\varepsilon\). Since \(v_S=0\), the variable \(v_T=V\) is a normalized original-product projection and has density at most \(\sqrt2\). Its square satisfies \(\Pr\{|V^2-s|\le r\}\le4\sqrt r\) for every \(s,r\). Layer cake gives
\[
 \sup_s\mathbb E\log_+\frac{16}{|s-V^2|}
 \le\int_0^\infty\min\{1,16e^{-t/2}\}\,dt
 =2\log16+2.
\]
Average the conditional envelope at \(u=s-V^2\) to obtain (1). No distributional assumption on \(p_T\) or the overlapping part \(\ell_T\) was used. Nonnegative output test functions give the same proof without a choice of conditional density versions.

The previous independent-L report is the special case \(c=1\), \(\ell_T=0\). The global mixed-sign canonical problem can have no pure L source row, so this theorem has a distinct scope.
