# A local orientation detector forces a defect separator

Centers have mutual distance at least one. All balls below are open. The result concerns planar packings with two prescribed crystalline orientations outside a bounded strip. It gives no Gibbs probability estimate.

## 1. A detector determined by a bounded window

Fix

\[
t=\frac{11}{10},\qquad \alpha=\arcsin\frac1{100},\qquad
R_o=2+t=\frac{31}{10}.
\tag{1}
\]

For an angle \(\theta\), let \(C_\theta\) be the union of the six closed angular cones of half-angle \(\alpha\) about the directions \(\theta+k\pi/3\), \(k=0,\ldots,5\). Only nonzero vectors belong to these cones. Use the two families

\[
C_A=C_0,\qquad C_B=C_{\pi/6}.
\tag{2}
\]

They are disjoint. Indeed, the minimum angular distance between their axes is \(\pi/6\). Also

\[
\sin(\pi/12)=\frac{\sqrt6-\sqrt2}{4}
>\frac{2-3/2}{4}=\frac18>\frac1{100},
\]

so \(\alpha<\pi/12\), and two cone half-angles do not bridge that distance.

For a packing \(X\), an anchor \(c\in\mathbb R^2\), and \(p\in X\cap B(c,2)\), define

\[
\mathcal N(p)=\{q\in X:0<|q-p|\leq t\}.
\]

Call \(c\) **A-good** if the following three conditions hold:

1. \(X\cap B(c,1)\ne\varnothing\).
2. For every \(p\in X\cap B(c,2)\), the set \(\mathcal N(p)\) is nonempty.
3. For every such \(p\) and every \(q\in\mathcal N(p)\), one has \(q-p\in C_A\).

Define B-good by replacing \(C_A\) with \(C_B\). Call the anchor defective if it has neither good label. These definitions depend only on \(X\cap B(c,R_o)\): for a tested \(p\), every possible neighbor lies at distance strictly less than \(2+t\) from \(c\). Separation makes this window finite, so the tests are finite and measurable. They require no lattice-site labels.

An anchor cannot be both A-good and B-good. Condition 1 supplies \(p\in B(c,1)\), condition 2 supplies a bond from it, and condition 3 would place that bond in the disjoint sets (2).

More generally, if \(|c-c'|\leq1\), then \(c\) and \(c'\) cannot have opposite good labels. To prove this, suppose \(c\) is A-good and \(c'\) is B-good. Choose \(p\in X\cap B(c,1)\). Then

\[
|p-c'|\leq |p-c|+|c-c'|<2.
\]

A-goodness supplies \(q\in\mathcal N(p)\). The same particle \(p\) is tested at \(c'\), so both goodness conditions apply to the same bond \(q-p\). They put it in \(C_A\cap C_B\), a contradiction. Interchanging the anchors proves the other ordering.

In particular the labels on the unit grid \(\mathbb Z^2\) have no face-adjacent A–B pair.

## 2. Recognition of the two perturbed triangular crystals

Let

\[
\Lambda_s=s\{(m+n/2,\sqrt3 n/2):m,n\in\mathbb Z\},\qquad
s=\frac{101}{100},\quad \delta=\frac1{400}.
\tag{3}
\]

A full jittered crystal of orientation \(\theta\) means

\[
Y_\theta=\{p+u_p:p\in a+O_\theta\Lambda_s\},\qquad
|u_p|<\delta,
\tag{4}
\]

with arbitrary phase \(a\) and simultaneous, arbitrary displacements. It is a packing since distinct nominal sites are at distance at least \(s\), and

\[
s-2\delta=\frac{201}{200}>1.
\tag{5}
\]

Every anchor is A-good in \(Y_0\), and every anchor is B-good in \(Y_{\pi/6}\). Here are the required uniform checks.

First, the triangular lattice has covering radius \(s/\sqrt3\). One direct derivation tiles the plane by equilateral triangles of side \(s\); splitting each triangle by its nearest-vertex regions shows that the largest distance to its nearest vertex is its circumradius \(s/\sqrt3\). Thus some nominal site is within that distance of any anchor. Its displaced center is at distance less than \(s/\sqrt3+\delta<1\). For an explicit bound, \(\sqrt3>5/3\) gives

\[
\frac{s}{\sqrt3}+\delta
<\frac{303}{500}+\frac1{400}=\frac{1217}{2000}<1.
\tag{6}
\]

Second, each site has exactly six nominal neighbors at distance \(s\), with the six directions of its crystal. Their displaced distances are less than

\[
s+2\delta=\frac{203}{200}<\frac{11}{10}=t.
\tag{7}
\]

All other nominal distances are at least \(\sqrt2s\). Indeed, their squared distances divided by \(s^2\) are the positive integers \(m^2+mn+n^2\); value one gives exactly the six neighbors (solve \((2m+n)^2+3n^2=4\)). Every other value is at least two. Consequently these other displaced distances are greater than \(\sqrt2s-2\delta>t\). This last inequality can be checked without a radical approximation:

\[
2s^2=\frac{20402}{10000}
>\left(t+2\delta\right)^2
=\left(\frac{221}{200}\right)^2
=\frac{48841}{40000}.
\tag{8}
\]

Thus the detector's short bonds are precisely the six nominal nearest-neighbor bonds after displacement; in particular they exist at every particle.

Third, a nominal bond \(v\) of length \(s\) changes by a vector of length less than \(2\delta\). Its angular change is less than or equal to \(\arcsin(2\delta/s)\): a disk of radius \(2\delta<s\) about \(v\) subtends this half-angle at the origin, as follows from the right triangle at a tangent point. Here

\[
\frac{2\delta}{s}=\frac1{202}<\frac1{100}=\sin\alpha.
\tag{9}
\]

All six short bonds therefore belong to the appropriate cones. This proves the recognition assertion. The same proof works for any \(s,\delta\) satisfying

\[
s-2\delta\geq1,\quad
s/\sqrt3+\delta<1,\quad
s+2\delta\leq t<\sqrt2s-2\delta,\quad
2\delta/s<\sin\alpha.
\tag{10}
\]

The non-strict first inequality is sufficient because the displacement radii are open. Formula (10) displays the dilation, displacement, and observation-scale restrictions used here. No claim is made for arbitrary dilation or jitter.

## 3. A finite planar separation lemma

Consider the grid rectangle

\[
\mathcal R=\{0,1,\ldots,m\}\times\{u,u+1,\ldots,v\},
\qquad m\geq2,\quad u<v,
\]

whose vertices have labels A, B, or D. Suppose its left column is entirely A, its right column entirely B, and no face-adjacent pair has labels A and B. Then D vertices contain a path from row \(u\) to row \(v\) using eight-neighbor adjacency, that is, steps with coordinate differences at most one. A simple such path has at least \(v-u+1\) vertices.

To prove this, replace each grid vertex by its closed unit square centered there, and draw the common edge of every pair of face-neighbor squares for which one square is A and the other is not A. These drawn edges form a finite graph, with their geometric endpoints as graph vertices.

At an interior geometric vertex, four squares meet. In cyclic order their binary statuses A/not-A change an even number of times, so its drawn-edge degree is 0, 2, or 4. No drawn edge can meet the left outer boundary: both squares at each possible endpoint there are in the A left column. No drawn edge meets the right outer boundary either: both squares there are in the non-A right column. The outer corners have degree zero.

Every drawn-edge endpoint on the top or bottom outer boundary has degree one. The number on the top is odd, because reading the top row from left to right starts in status A and ends in status not-A, so the number of changes is odd. The same assertion holds on the bottom.

In each connected component of the drawn-edge graph, the number of odd-degree vertices is even; this follows by summing degrees, twice the number of edges. Since the total number of top endpoints is odd, some component contains an odd number of top endpoints. Its interior degrees are even and it has no side endpoints, so it contains an odd number of bottom endpoints as well. Choose in it a simple edge path from a top endpoint to a bottom endpoint.

Every edge of this path separates A from a non-A square. That non-A square cannot be B by the hypothesis excluding A–B neighbors; it is D. For consecutive edges, the chosen D squares both contain their common geometric endpoint. They are therefore identical or eight-neighbors. The first D square is in the top row and the last in the bottom row. Remove repetitions and loops to obtain a simple eight-neighbor D path. Each step changes the row coordinate by at most one, so the path visits every row, and has at least \(v-u+1\) distinct vertices. This proves the lemma, including diagonal and degree-four junctions.

## 4. An arbitrarily filled strip

Let \(W\geq0\). Suppose a diameter-one packing \(X\) agrees with one full crystal \(Y_0\) as in (4) in \(\{x_1<-W\}\), and with another full crystal \(Y_{\pi/6}\) in \(\{x_1>W\}\). The phases and displacement fields on the two sides are independent choices. Inside the closed strip \(\{|x_1|\leq W\}\), allow any centers compatible with the packing condition, including rearrangements and extra particles.

Set

\[
M=\lfloor W+R_o\rfloor+1.
\tag{11}
\]

Every anchor \((i,j)\) with \(i\leq-M\) is A-good: its observation ball lies in \(\{x_1<-W\}\), where Section 2 applies. Every anchor with \(i\geq M\) is B-good for the same reason. Thus every defective anchor lies in the finite-width band

\[
-M+1\leq i\leq M-1.
\tag{12}
\]

For any integers \(u<v\), apply Section 3 to the labels in
\(\{-M,\ldots,M\}\times\{u,\ldots,v\}\).
The left and right columns have the required labels, and Section 1 excludes face-adjacent A–B labels. Hence there is an eight-neighbor path of defective anchors from row \(u\) to row \(v\), entirely inside (12), with at least \(v-u+1\) vertices.

There is also one connected component of defective anchors unbounded in both vertical directions. For each \(n\geq1\), take such a path from \(-n\) to \(n\). It intersects row zero, which contains only \(2M-1\) possible defective anchors. Some fixed anchor \(a\) in that row belongs to the selected paths for infinitely many \(n\), with those \(n\) unbounded. Its full defective component then reaches heights at least \(n\) and at most \(-n\) along those paths. This proves the assertion; the component need not contain every defective anchor.

## 5. Relation to the earlier occupation counterexample

In round 5 the nominal half-plane lattices are retained in \(x_1<-g/2\) and \(x_1>g/2\), where \(g=101/100\), and displaced by less than \(\delta=1/400\). Their union \(X_0\) agrees with the corresponding full displaced crystals outside the strip of half-width

\[
W=g/2+\delta=\frac{203}{400}.
\tag{13}
\]

For example, if a displaced full-crystal point has first coordinate below \(-g/2-\delta\), its nominal point has first coordinate below \(-g/2\), so it was retained. Conversely every point of \(X_0\) there is from that same crystal; right-side points cannot be there by their displacement bound. The right half-plane is identical with signs reversed.

Here

\[
W+R_o=\frac{1443}{400},\qquad M=4.
\tag{14}
\]

Consequently the local detector finds a connected defect separator among the seven anchor columns \(-3,-2,\ldots,3\), for every phase and every allowed displacement in that example. The same conclusion holds for every admissible addition of centers inside \(|x_1|\leq203/400\), keeping the original centers. These additions preserve the earlier lower bound of three centers in every square of side four, because counts cannot decrease. Thus the forced defect chain can coexist with the complete absence of underoccupied squares for the earlier threshold of two centers.

## 6. Scope

The defect condition is relative to the two prescribed families (2). A perfectly triangular region at an intermediate orientation can be defective under this definition. The theorem supplies a separator for these two labels, not a count of dislocation cores or a defect cost invariant under every rotation. Empty windows are defective too; the proof does not require positive density in the interpolating strip.

No estimate here bounds the conditional Gibbs probability of a chain of these defects. In particular a defective window can have many particles, and the earlier underoccupation bound cannot be applied to it without another argument. The eight-neighbor adjacency also differs from the face adjacency used in that earlier bound. A continuum partition-function comparison integrating dense defective configurations is still required before a Peierls argument or orientational surface tension can be deduced. There is no freezing or symmetry-breaking conclusion.
