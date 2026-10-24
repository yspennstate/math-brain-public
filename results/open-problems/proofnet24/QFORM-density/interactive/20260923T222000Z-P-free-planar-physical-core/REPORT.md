# A P-free planar source core resolves arbitrary remaining tail overlap

**Status:** Proved signed canonical all-level theorem for a fixed planar physical core. It allows the complementary original coordinates to feed all three light projections and to have arbitrary fragmented or infinite-variance laws. The remaining problem can have no such planar core.

Let \(H,X_1,\ldots,X_n\) be independent real variables with densities at most one. Let \(\ell,v,p\in\mathbb R^n\) be orthonormal and define \(L=\ell\cdot X\), \(V=v\cdot X\), \(P=p\cdot X\). Suppose there exists \(R\subset[n]\) such that \(p_i=0\) for all \(i\in R\) and
\[
 G_R=\sum_{i\in R}\begin{pmatrix}\ell_i\\v_i\end{pmatrix}
                    \begin{pmatrix}\ell_i&v_i\end{pmatrix}
 \succeq cI_2\qquad(c>0).
\]
Then, for **every** \(\beta,\varepsilon\in\mathbb R\),
\[
 \bigl\|p_{2HL+\beta L^2+V^2+2\varepsilon LP}\bigr\|_\infty
 \le\frac12+\frac{8\sqrt2}{c}.
 \tag{1}
\]
The constant does not depend on the number, laws, or support diameters of the complementary variables.

**Proof.** Write \(T=R^c\) and condition on \(X_T\). The values \(l_T,v_T,p_T\) contributed to \(L,V,P\) by these variables are now fixed, while \(P=p_T\), because \(p_R=0\). The random planar vector \((L_R,V_R)\) is a two-dimensional linear projection of the independent cap-one originals \(X_R\). Whitening by \(G_R^{-1/2}\) yields an orthonormal projection with joint density bounded by two, so the density of \((L_R,V_R)\), and thus of \((l_T+L_R,v_T+V_R)\), is bounded by \(2/\sqrt{\det G_R}\le2/c\). Independently, \(H+\varepsilon p_T\) has density at most one. The conditional quadratic equals
\[
 2(H+\varepsilon p_T)L+\beta L^2+V^2.
\]
Apply the proved two-dimensional square-root-kernel lemma: for an independent cap-one hub and a planar light pair with joint density cap \(K\), the quadratic \(2HL+r(L)+V^2\) has density at most \(1/2+4\sqrt2K\), for arbitrary measurable \(r\). Take \(K=2/c\) and \(r(L)=\beta L^2\); the conditional bound is (1) for every frozen \(X_T\), so averaging proves (1).

The complete square-root-kernel lemma appears in the exact physical spectral coloop report at commit c8542016844451bfa5585e5e15a89ed84f1602cb. When every original feeding a substantial planar portion of \((L,V)\) also has \(p_i\ne0\), a P-free core need not exist; unbounded fragments of \(P\) then cannot be frozen without losing planar smoothing. This theorem makes no assertion in that case.
