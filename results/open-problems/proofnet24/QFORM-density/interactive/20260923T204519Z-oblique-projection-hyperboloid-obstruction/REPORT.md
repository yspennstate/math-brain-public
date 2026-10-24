# Negative hyperboloid obstruction survives every two-dimensional projection cap

**Scope warning:** this construction is an arbitrary *dependent* three-dimensional law. It is **not** a counterexample to the original-product quadratic-form conjecture. It proves that bounding the full joint density and **every** orthogonal two-dimensional marginal, even by fixed numerical constants, cannot by itself control the convex-side density of an indefinite rank-three form.

## The construction

Let \(q(y)=y_1^2+y_2^2-y_3^2\), so the coefficient matrix is \(\operatorname{diag}(1,1,-1)\) and its third singular value equals one. For \(R\ge100\), set \(\delta=R^{-2}\), \(\xi=(y_1,y_2)\), \(r=|\xi|\), and
\[
S_R=\{y:R\le r\le2R,\ y_3>0,\ |q(y)+1|\le\delta\}.
\]
Let \(m_R=|S_R|\). The coarea calculation below gives \(m_R=O(R\delta)=O(R^{-1})<1\). Pick an axis-aligned rectangular box \(C_R\), disjoint from \(S_R\), of volume \(1-m_R\) with all side lengths at most one. Define the normalized probability density
\[
f_R(y)=\mathbf1_{S_R}(y)+\mathbf1_{C_R}(y)\le1.
\]
For instance a box with side lengths \(1-m_R,1,1\) starting at \((10R,0,0)\) is disjoint from the shell.

## The quadratic output has arbitrarily high density at a fixed negative value

For \(s\in[-1-\delta,-1+\delta]\), the shell's contribution to the density of \(q(Y)\) is
\[
p_{q,S_R}(s)
=\int_R^{2R}\int_0^{2\pi}
\frac{r}{2\sqrt{r^2-s}}\,d\theta\,dr
=\pi\int_R^{2R}\frac r{\sqrt{r^2-s}}\,dr
\ge cR
\]
with universal \(c>0\) (for \(R\ge100\), \(c=\pi/2\) is safe). Thus
\[
\sup_{s\in[-1-\delta,-1+\delta]}p_{q(Y)}(s)\ge (\pi/2)R\longrightarrow\infty,
\]
and this is an **essential** density lower bound on an interval, not a pointwise-version artifact. Integrating the same coarea expression across a width \(2\delta\) gives \(m_R\le C R\delta=O(1/R)\).

## Uniform bound on *all* orthogonal two-dimensional marginals

An orthogonal projection of \(f_R\) onto any plane has density equal to the integral of \(f_R\) along lines normal to that plane. Every line meets \(C_R\) in length at most \(\sqrt3\). We prove that every Euclidean line also meets \(S_R\) in a bounded total length independent of \(R\).

Write \(y=(\xi,z)\), \(h(\xi)=\sqrt{1+|\xi|^2}\). On \(S_R\), \(z\ge R\) and
\[
|z-h(\xi)|
=\frac{|q(y)+1|}{z+h(\xi)}
\le\eta:=\frac\delta{2R}=\frac1{2R^3}.
\tag{1}
\]
Parametrize an arbitrary line by unit arclength \(y(t)=(\xi_0+t w,z_0+t u)\) with \(|w|^2+u^2=1\), and set \(F(t)=z_0+t u-h(\xi_0+t w)\).

- If \(|w|<1/2\), then \(|u|>\sqrt3/2\) and \(|\nabla h|\le1\), so \(|F'(t)|\ge(\sqrt3-1)/2\) with a fixed sign. Its intersection with \(|F|\le\eta\) has length at most \(4\eta/(\sqrt3-1)\).
- If \(|w|\ge1/2\), then throughout the disk \(|\xi|\le2R\), the Hessian of \(h\) has smallest eigenvalue
  \((1+|\xi|^2)^{-3/2}\ge(1+4R^2)^{-3/2}\). Thus
  \[
  F''(t)=-w^TD^2h(\xi_0+t w)w
  \le-\kappa_R,\qquad
  \kappa_R=\frac1{4(1+4R^2)^{3/2}}.
  \]
  On each interval within the disk where \(|F|\le\eta\), midpoint concavity gives a length at most \(4\sqrt{\eta/\kappa_R}\). This ratio is universally bounded because \(\eta=1/(2R^3)\) and \(\kappa_R\asymp R^{-3}\). The annulus \(R\le|\xi|\le2R\) cuts a line into at most two components; on each, a strictly concave function crosses the band \([-\eta,\eta]\) in at most two components. Hence the **total** intersection length is at most \(16\sqrt{\eta/\kappa_R}\), bounded uniformly in \(R\).

For \(R\ge100\), these two cases plus the box give, conservatively,
\[
\sup_{\text{orthogonal planes }E}\|p_{\pi_EY}\|_\infty\le100.
\]
The exact numerical value is irrelevant; it is independent of \(R\). A valid cap-one product law would in fact enjoy a sharp all-plane two-dimensional marginal cap \(2\), but *merely assuming* some universal all-plane marginal cap, joint cap, and normalized mass is still insufficient to pay negative levels.

## What this does and does not show

The hyperboloid packet has only \(O(1/R)\) probability mass, yet its quadratic values lie in a window of width \(O(1/R^2)\), producing density \(\Omega(R)\). Long near-tangent lines have bounded packet intersection because the sheet's radial curvature is of order \(R^{-3}\), the physical normal thickness is of order \(R^{-3}\), and their ratio is fixed.

This disproves a proposed proof route based only on universal projection-marginal bounds, even for the exact signature \((+,+,-)\) at the fixed convex-side level \(-1\). No construction of independent original-coordinate \(X_i\) realizing this law is supplied or claimed. The original-product provenance remains the necessary missing input in that route.
