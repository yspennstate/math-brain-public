# Fragmented cap-one source beats every unit-interval product source for a rank-three quadratic form

Date: 2026-09-23. Status: **proved counterexample to an interval-extremizer shortcut**, not to the uniform density conjecture.

## Claim

For the positive definite rank-three homogeneous form
\[
q(x,y,z)=x^2+y^2+z^2,
\]
there is a product law of independent cap-one coordinates and a level s for which its output density is strictly larger than the density at s under **every** product law in which each coordinate is uniform on one interval of length one, regardless of the interval locations.

Take any
\[
R>\frac{2}{2/\sqrt3-1}
\]
—for example R=20—and set s=R². Let X have density one on
\[
[R-1/4,R+1/4]\ \cup\ [-R-1/4,-R+1/4],
\]
and let Y,Z be independent and uniform on [-1/2,1/2]. All three inputs have density cap one, and the support of X has total measure one.

For fixed y,z in their supports, the two solutions to \(x^2+y^2+z^2=R^2\) are
\(x=\pm\sqrt{R^2-y^2-z^2}\). Both lie in the support of X. Indeed \(y^2+z^2\le1/2\), and for R≥9/8,
\[
\sqrt{R^2-1/2}\ge R-1/4.
\]
The square-map Jacobian therefore gives
\[
p_{q(X,Y,Z)}(R^2)
=\mathbb E_{Y,Z}\frac1{\sqrt{R^2-Y^2-Z^2}}
\ge\frac1R.
\tag{1}
\]

Now suppose X',Y',Z' are each uniform on an arbitrary interval of length one, with support cube centered at c∈R³. If the cube does not meet the sphere of radius R, the density at R² is zero. Otherwise a point x of the cube has |x|=R. Since |x−c|≤√3/2, we have |c|≥R−√3/2. Hence some coordinate index i satisfies
\[
|c_i|\ge R/\sqrt3-1/2.
\]
Every point in that coordinate's unit interval then satisfies
\[
|x_i|\ge R/\sqrt3-1>0.
\]
Conditioning on the other two coordinates, the map \(x_i\mapsto x_i^2\) has at most one branch in this interval and derivative of absolute value at least \(2(R/\sqrt3-1)\). Thus
\[
p_{q(X',Y',Z')}(R^2)
\le\frac1{2(R/\sqrt3-1)}
<\frac1R,
\tag{2}
\]
where the final inequality is exactly the displayed strict assumption on R.

Equations (1)–(2) disprove a general claim that, at a fixed level, uniform laws on one unit interval per coordinate maximize the output density among independent cap-one inputs. The admissible fragmented law simply collects contributions from both square-map branches. The example has \(s_3(I_3)=1\) and satisfies the original product-source assumptions. Its density is of order 1/R and does **not** contradict a dimension-free universal bound. Coordinatewise quantile maps are expansive, but that fact alone cannot justify replacing their images by single intervals in a density proof.
