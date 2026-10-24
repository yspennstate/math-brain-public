# Addendum: determinant refinement of exact-cross-rank density

The exact rank-k physical-crossing proof has a stronger geometric-mean formulation. If $B=A_{S,T}$ has **exact rank $k\ge3$** with nonzero singular values $d_1,\ldots,d_k$, put $g_B=(\prod_j d_j)^{1/k}$. For arbitrary within-bank quadratic coefficients, affine coefficients, and independent cap-one coordinates,
\[
 \|p_{X^TAX+b^TX+c}\|_\infty
 \le \frac{2k}{(k-2)g_B}.
\]
Proof: retain $|\det D|^{-1/2}$ in k-dimensional Plancherel, giving $|\varphi(t)|\le\min\{1,(2\pi/(g_B|t|))^{k/2}\}$; integrate. The prior $2k/[(k-2)s_k(B)]$ follows since $g_B\ge s_k(B)$. Example rank-four crossing singulars $(1,1,1,\varepsilon)$ yields $4\varepsilon^{-1/4}$, still nonuniform as $\varepsilon\to0$. Small extra crossing directions cannot be discarded.

Math report amended: https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T194300Z-exact-cross-rank-fourier/REPORT.md (commit d9b3190196190fff223b48f71d0668dcf07ec702).
