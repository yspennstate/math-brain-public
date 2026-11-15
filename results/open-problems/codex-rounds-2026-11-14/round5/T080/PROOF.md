# A triangular-lattice interface invisible to a coarse occupation test

Centers have exclusion distance one. A square is axis parallel and may be translated arbitrarily. Write \(t_+=\max\{t,0\}\), and let

\[
\Lambda_s=s\{(m+n/2,\sqrt3 n/2):m,n\in\mathbb Z\},\qquad
\rho_s=\frac{2}{\sqrt3 s^2},\qquad R=\frac{s}{\sqrt3}.
\tag{1}
\]

The construction below concerns packings and finite configurational volumes. It does not assert the existence of a Gibbs state with an interface.

## 1. Statement

Choose \(s>1\), \(\delta>0\), and \(g>0\) such that

\[
s-2\delta>1,\qquad g-2\delta>1.
\tag{2}
\]

Fix two angles \(\theta_-,\theta_+\) and arbitrary translations \(t_-,t_+\in\mathbb R^2\). Let \(O_\theta\) denote rotation by \(\theta\), and retain the sites

\[
P_-=(t_-+O_{\theta_-}\Lambda_s)\cap\{x_1<-g/2\},\qquad
P_+=(t_++O_{\theta_+}\Lambda_s)\cap\{x_1>g/2\}.
\tag{3}
\]

For each \(p\in P=P_-\cup P_+\), choose any vector \(u_p\) with \(|u_p|<\delta\), and set

\[
X=\{p+u_p:p\in P\}.
\tag{4}
\]

Every such \(X\) is a packing. Its center-free strip includes
\(\{|x_1|<g/2-\delta\}\), of width \(g-2\delta\). For every square \(Q\) of side \(\ell>0\),

\[
\boxed{\quad
N_X(Q)\geq
\rho_s(\ell-2\delta-2R)_+
          (\ell-2\delta-g-4R)_+.
\quad}
\tag{5}
\]

The inequality is simultaneous for all squares, phases, angles, and choices of the displacements. Distinct nominal orientations are obtained whenever
\(\theta_+-\theta_-\notin(\pi/3)\mathbb Z\).

In particular, take

\[
\theta_-=0,\quad\theta_+=\pi/6,\qquad
s=g=\frac{101}{100},\quad\delta=\frac1{400}.
\tag{6}
\]

Every square of side four contains at least three centers. Consequently every translated grid of four-by-four boxes has no boxes with at most two centers, although (3) joins two non-equivalent triangular orientations across a bounded strip. The explicit planar underoccupation detector in round 4 therefore need not detect such an interface.

## 2. Lattice cells and a rectangle count

A basis for \(\Lambda_s\) is \(a=(s,0)\), \(b=(s/2,\sqrt3 s/2)\). Its fundamental area is

\[
A=|\det(a,b)|=\frac{\sqrt3 s^2}{2}=\rho_s^{-1}.
\tag{7}
\]

Here is also a direct cell description. The six shortest nonzero lattice vectors are \(\pm a,\pm b,\pm(b-a)\). Their perpendicular bisectors bound a regular hexagon centered at zero, with inradius \(s/2\) and circumradius \(R=s/\sqrt3\). To check that no further lattice vector cuts this hexagon, a vector \(w=ma+nb\) has

\[
|w|^2=s^2(m^2+mn+n^2).
\]

The positive integer \(m^2+mn+n^2\) equals one only for the six listed vectors. Indeed \((2m+n)^2+3n^2=4\) first restricts \(n\) to \(-1,0,1\), and enumerating these three cases gives precisely the six vectors. All other nonzero vectors have length at least \(\sqrt2s>2R\). For a point \(x\) in the hexagon,

\[
x\cdot w\leq |x||w|\leq R|w|<|w|^2/2
\]

for every such further vector. These are exactly the inequalities asserting that \(x\) is closer to zero than to \(w\). The hexagon is therefore the Voronoi cell of zero. Its area, computed from six triangles of base \(s/\sqrt3\) and height \(s/2\), is \(\sqrt3s^2/2\), in agreement with (7).

Nearest-site cells cover the plane, their interiors are disjoint, and their boundaries have area zero. Existence of a nearest site follows from discreteness and boundedness of each distance sublevel set. The cells are translates of this hexagon; rotations and translations preserve their area and radius.

Let \(L=t+O_\theta\Lambda_s\), and let \(D\) be an open rectangle of side lengths \(w,h\geq0\). The set of points of \(D\) at distance greater than \(R\) from its complement has area

\[
|D^{\ominus R}|=(w-2R)_+(h-2R)_+.
\]

For almost every point \(x\) in this eroded rectangle, the cell containing \(x\) has its lattice site \(p\) at distance at most \(R\). The strict erosion margin gives \(p\in D\). Hence the cells of the sites in \(L\cap D\) cover \(D^{\ominus R}\), up to a null set. Comparing areas gives

\[
\#(L\cap D)\geq \rho_s(w-2R)_+(h-2R)_+.
\tag{8}
\]

This estimate holds for every phase and orientation. Empty and degenerate rectangles have zero on the right. Open or half-open boundary conventions do not affect the erosion area argument.

## 3. Separation and the count in a square

Two distinct sites on the same side have distance at least \(s\). Their perturbed positions have distance greater than \(s-2\delta>1\). Sites on opposite sides have first-coordinate difference greater than \(g\), so their perturbed positions have distance greater than \(g-2\delta>1\). This proves exclusion and injectivity of (4). Uniform separation also proves local finiteness. The strip assertion follows by subtracting the maximum horizontal displacement \(\delta\) from the original half-plane margins.

Let \(Q\) have side \(\ell\). If \(\ell\leq2\delta\), the right side of (5) is zero, so suppose \(\ell>2\delta\). Its open erosion \(Q^{\ominus\delta}\) is a square of side \(L=\ell-2\delta\). Every site inside it remains inside \(Q\) after its displacement. Intersect it with each of the two half-planes in (3). The resulting rectangles have height \(L\) and widths \(w_-,w_+\geq0\). The omitted central interval has length at most \(g\), so

\[
w_-+w_+\geq L-g.
\tag{9}
\]

Applying (8) separately to the two lattices gives

\[
N_X(Q)\geq\rho_s(L-2R)_+
          \bigl[(w_--2R)_++(w_+-2R)_+\bigr].
\tag{10}
\]

For nonnegative \(w_-,w_+\), the bracket in (10) is nonnegative and at least \(w_-+w_+-4R\). By (9) it is at least \((L-g-4R)_+\). Substitution into (10) proves (5). Sites initially outside \(Q^{\ominus\delta}\) may enter \(Q\); ignoring them only weakens the lower bound. The proof covers squares wholly on one side and squares straddling any portion of the strip.

## 4. Exact constants for four-by-four boxes

For (6), both lower bounds in (2) equal \(201/200>1\). The rational inequalities

\[
\frac{303}{175}<\sqrt3<\frac{26}{15}
\tag{11}
\]

follow from \(91809<91875\) and \(675<676\), respectively. They imply

\[
R<\frac{7}{12},\qquad
\rho_s>\frac{150000}{132613}.
\tag{12}
\]

Indeed \((101/100)(175/303)=7/12\), while
\(2/[(26/15)(101/100)^2]=150000/132613\).
At \(\ell=4\) both factors of (5) are positive. Using (12) in the decreasing radius factors yields

\[
\begin{aligned}
N_X(Q)
&>\frac{150000}{132613}
 \left(4-\frac1{200}-\frac76\right)
 \left(4-\frac1{200}-\frac{101}{100}-\frac73\right)\\
&=\frac{150000}{132613}\frac{1697}{600}\frac{391}{600}
 =\frac{3317635}{1591356}
 =2+\frac{134923}{1591356}>2.
\end{aligned}
\tag{13}
\]

Since the particle count is an integer, it is at least three. No rounding or sampled lattice count is used in (13).

The six nearest-neighbor directions of an unperturbed triangular lattice are separated by \(\pi/3\). Thus an orientation difference \(\pi/6\) cannot be removed by a translation or a lattice rotation symmetry. Small displacements in (6) also preserve a local distinction far from the strip. An original nearest-neighbor vector of length \(s\) changes by less than \(2\delta\). Its direction changes by at most \(\arcsin(2\delta/s)\), since its perturbed endpoint lies in the radius-\(2\delta\) disk about the original endpoint, whose extreme viewing angle is the tangent angle. Here \(2\delta/s=1/202<\sin(\pi/12)\); the two families of possible directions are disjoint. To check this last comparison without decimals, \(\sin(\pi/12)=(\sqrt6-\sqrt2)/4>(2-3/2)/4=1/8>1/202\).

Nearest neighbors remain recognizable: their distances are less than \(s+2\delta\), while every other same-side site has distance greater than or equal to \(\sqrt2s-2\delta>s+2\delta\). The last inequality follows from \(\sqrt2>7/5\), giving \((\sqrt2-1)s>2s/5>4\delta\). In each far half-plane all six neighbors are retained and opposite-side particles are arbitrarily far away. Hence the directional distinction can be read from the packing there, not merely from site labels.

## 5. Dependence on threshold and scale

Fix parameters satisfying (2). Put

\[
a_0=2\delta+2R,\qquad b_0=2\delta+g+4R.
\]

For any \(0<\rho<\rho_s\), the explicit sufficient choice

\[
\ell>\frac{a_0+b_0}{1-\rho/\rho_s}
=\frac{4\delta+g+6R}{1-\rho/\rho_s}
\tag{14}
\]

gives \(N_X(Q)>\rho\ell^2\) for every square of side \(\ell\). In fact (14) implies \(\ell>b_0\geq a_0\), so (5) becomes

\[
N_X(Q)\geq\rho_s(\ell-a_0)(\ell-b_0)
\geq\rho_s\ell^2\left(1-\frac{a_0+b_0}{\ell}\right)
>\rho\ell^2.
\]

Thus raising the threshold to a fixed number density below the bulk density does not by itself repair the geometric implication at all large box scales. The scale bound diverges as \(\rho\uparrow\rho_s\). Since \(\rho_s\to2/\sqrt3\) as \(s\downarrow1\), for any fixed \(\rho<2/\sqrt3\) one can first choose \(s>1\) with \(\rho_s>\rho\), then choose \(\delta,g\) satisfying (2), then choose \(\ell\) by (14). No statement is made for every threshold at a preassigned box size.

The bulk center density of each such packing is \(\rho_s\). For completeness, the Voronoi argument also gives \(\#(L\cap D)\leq\rho_s(w+2R)(h+2R)\), since the cells of sites in \(D\) are disjoint and contained in its radius-\(R\) neighborhood, which lies in the expanded rectangle. In a large square, apply the lower and upper rectangle counts to the two retained half-planes. Removing a fixed-width strip costs area of order the side length. Perturbations change counts only in a fixed-width neighborhood of the square boundary, whose site count is also of that order by the upper rectangle bound. Dividing by the square area gives limiting density \(\rho_s\). This density statement is not needed for (13).

## 6. Continuum volume and Gibbs scope

The displacements need not be frozen. For any finite set of \(M\) selected sites, allow each displacement independently over its open radius-\(\delta\) ball and fix all other sites at their nominal positions. All these choices are admissible by (2). The balls are disjoint. In the bounded sampling region consisting of their union, with all other nominal sites as exterior, the sector with one particle in every ball has unnormalized Gibbs weight

\[
\frac{z^M}{M!}\,M!\,(\pi\delta^2)^M
=(z\pi\delta^2)^M>0.
\tag{15}
\]

Every finite collection of these displacement variables therefore has a genuine positive continuum volume. Equation (15) is a restricted sector weight, not an interface probability or a ratio with an aligned ensemble.

For example, independently choosing all displacements uniformly in their balls gives a probability law on the countable product of balls, supported on the packings (4). It is not a finite-activity hard-disk Gibbs law. Each fixed ball \(U=B(p,\delta)\) contains exactly one particle almost surely; other displacement balls are disjoint. In every finite-activity Gibbs law, however, the DLR equation gives

\[
\Pr(N(U)=0\mid X\cap U^c)=\frac1{Z_U^{X\cap U^c}(z)}
\geq e^{-z|U|}>0,
\]

because dropping exclusion gives \(Z_U^\eta(z)\leq e^{z|U|}\). Averaging contradicts the deterministic occupancy. Thus positive displacement volume removes a singular exact-contact objection but does not establish the Gibbs property.

The interface may still have a particle deficit proportional to its length and may have a positive Gibbs cost. The construction disproves a deterministic implication from differing orientations to boxes detected by the stated underoccupation tests. It neither disproves the earlier Gibbs estimates nor bounds the probability of this interface. A comparison of constrained partition functions with common exterior data remains necessary for a freezing argument.
