# Rank-two physical leaf core, even with all three projection coefficients present

**Status:** Proved all-level canonical theorem with a dimension-free bound under a rank-two physical source core. Complementary originals may contribute to all three light projections and have arbitrary tails. Unlike a P-free core, the core itself may have nonzero coefficients in all three projections, provided its third coefficient row is an exact linear combination of the first two.

Let \(H,X_1,\ldots,X_n\) be independent real variables with densities bounded by one. Let \(L=\ell\cdot X\), \(V=v\cdot X\), and \(P=p\cdot X\) for arbitrary coefficient vectors. Assume a subset \(R\subset[n]\) has
\[
 G_R=\sum_{i\in R}\begin{pmatrix}\ell_i\\v_i\end{pmatrix}
                    \begin{pmatrix}\ell_i&v_i\end{pmatrix}\succ0,
 \qquad d_R=\sqrt{\det G_R}>0,
\]
and there are real \(\alpha,\rho\) with \(p_i=\alpha\ell_i+\rho v_i\) for every \(i\in R\). Then for all \(\beta,\varepsilon\in\mathbb R\),
\[
 \bigl\|p_{2HL+\beta L^2+V^2+2\varepsilon LP}\bigr\|_\infty
 \le3\cdot2^{4/3}d_R^{-2/3}.
 \tag{1}
\]
For the canonical orthonormal \((\ell,v,p)\), the simpler sufficient gate \(G_R\succeq cI_2\) gives \(d_R\ge c\) and bound \(3\cdot2^{4/3}c^{-2/3}\), uniformly in the total dimension and all original-product laws.

**Proof.** Condition on the complementary original variables \(X_T\), \(T=R^c\). Their contributions \(l_T,v_T,p_T\) become constants. The two-dimensional product projection \((L_R,V_R)\) has density bounded by \(2/\sqrt{\det G_R}=2/d_R\): whiten its two coefficient rows with \(G_R^{-1/2}\) and apply the standard planar orthonormal original-product projection bound two, then undo the determinant \(d_R\). Translation by \((l_T,v_T)\) preserves this bound for the conditional full pair \((L,V)\).

The exact linear relation on \(R\) implies, for the same frozen \(X_T\),
\[
 P=\alpha L+\rho V+p_0,
 \qquad p_0=p_T-\alpha l_T-\rho v_T.
\]
Consequently
\[
 \begin{split}
 Q&=2(H+\varepsilon p_0)L+(\beta+2\varepsilon\alpha)L^2
       +V^2+2\varepsilon\rho LV\\
  &=2(H+\varepsilon p_0)L+
       (\beta+2\varepsilon\alpha-\varepsilon^2\rho^2)L^2
       +(V+\varepsilon\rho L)^2.
 \end{split}
\]
The shear \((L,V)\mapsto(L,V+\varepsilon\rho L)\) has Jacobian one, so the conditional planar cap remains \(K=2/d_R\). The shifted hub \(H+\varepsilon p_0\) is independent of the unfrozen \(X_R\) and has density cap one. The optimized planar square-root lemma, established in the physical-pair report, gives density at most \(3\cdot2^{2/3}K^{2/3}=3\cdot2^{4/3}d_R^{-2/3}\). Average over \(X_T\).

When \(R\) consists of two original coordinates with nonzero \((\ell,v)\) minor, the relation \(p_R=\alpha\ell_R+\rho v_R\) is automatic, and the exact product-pair Jacobian sharpens the planar cap from \(2/d_R\) to \(1/d_R\); this recovers \(3\cdot2^{2/3}d_R^{-2/3}\). When \(p_R=0\), this strengthens the earlier P-free planar-core theorem. Generic fully overlapping triples of leaf coefficient rows span three dimensions on every substantial source core; their additional third-direction dependence is untouched.
