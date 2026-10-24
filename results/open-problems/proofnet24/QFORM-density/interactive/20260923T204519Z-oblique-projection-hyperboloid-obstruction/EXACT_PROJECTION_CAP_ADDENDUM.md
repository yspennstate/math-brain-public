# Matching the sharp product-marginal caps does not rescue the false joint-law claim

The companion [REPORT.md](https://github.com/yspennstate/math-open-problems/blob/44fd60cd4bfc12e9847ec7e332f84c4890aaf70e/proofnet24/QFORM-density/interactive/20260923T204519Z-oblique-projection-hyperboloid-obstruction/REPORT.md) proves that every line meets the thin negative hyperboloid shell \(S_R\) in length at most \(100\), while its quadratic-value density is at least \((\pi/2)R\) throughout \(|s+1|\le R^{-2}\). We can match the **sharp numerical two-dimensional marginal cap** \(2\) that would hold for an actual orthogonal projection of independent cap-one coordinates.

Keep \(S_R\) and its volume \(m_R=O(1/R)<1\). Fix \(\alpha=1/100\), and choose a cube \(D_R\) of side length \(10\), disjoint from the shell (for example start its first coordinate at \(10R\)). Set
\[
\widetilde f_R(y)
=\alpha\,\mathbf1_{S_R}(y)
+\frac{1-\alpha m_R}{1000}\,\mathbf1_{D_R}(y).
\]
This is a normalized probability density with \(\widetilde f_R\le1\). Along every Euclidean line, the shell contribution to the integral is at most \(\alpha\cdot100=1\), while the cube contribution is at most
\[
\frac{1-\alpha m_R}{1000}\operatorname{diam}(D_R)
\le\frac{10\sqrt3}{1000}<0.018.
\]
Therefore **every** orthogonal two-dimensional marginal of \(\widetilde f_R\) is bounded by \(1.018<2\), independent of \(R\). The full three-dimensional density is bounded by one, stronger than the general product-projection cap \(2^{3/2}\).

But the quadratic-value density still satisfies
\[
p_{q(\widetilde Y)}(s)
\ge\alpha (\pi/2)R=(\pi/200)R
\quad\text{for every } |s+1|\le R^{-2},
\]
so its essential supremum diverges. The coefficient matrix remains \(\operatorname{diag}(1,1,-1)\), with three singular values exactly one.

Thus assuming only the *entire numerical family* of full joint and orthogonal two-dimensional marginal caps that actual product projections obey is still insufficient for the negative convex sheet. The law here is deliberately dependent; its matching marginal caps do **not** make it an original-product counterexample. Any proof of the full QFORM target needs more than those caps.
