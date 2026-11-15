# Simple periodic orbits with at most six mirrors

Fix the directed edge e=((0,0),(1,0)). Start the ray by traversing e eastward. Write C(e) for its orbit and let q=1-p. An orbit is vertex-simple if its vertices in one period are distinct, except for the final return to its starting vertex. Count mirrors only on the orbit; states elsewhere are unrestricted.

**Proposition.** For 0<p<=1, the probability that C(e) is a vertex-simple periodic orbit containing at most six mirrors is exactly

\[
 B(p)=\frac{p}{8(2-p)^3}+\frac{p(1-p)^2}{4(2-p)^5}
     =\frac{p(6-8p+3p^2)}{8(2-p)^5}.
\]

Consequently P_p(C(e) is periodic)>=B(p), and

\[
 \liminf_{p\downarrow0}\frac{P_p(C(e)\text{ is periodic})}{p}
 \geq \frac{3}{128}.
\]

The proposition counts a restricted family and does not assert that other orbits are infinite.

## 1. Shape classification and the probability of a shape

At an empty vertex the ray continues straight, and at a mirror it turns by 90 degrees. A ray never reverses direction in one step. For a vertex-simple periodic orbit, suppress all vertices where it goes straight. The result is a simple polygon whose sides are horizontal or vertical and have positive integer lengths. Its corners are exactly the mirrors on the orbit.

Let C and R be the numbers of convex and reflex corners, respectively. The interior angles are pi/2 at convex corners and 3pi/2 at reflex corners. The angle sum of a simple polygon with C+R corners is (C+R-2)pi; this follows by dividing it into C+R-2 triangles. Thus

\[
 C+3R=2(C+R-2),\qquad C-R=4.
\]

In particular the number of corners C+R is even and is at least four. With at most six corners the possibilities are (C,R)=(4,0) and (5,1).

For four corners, orient the boundary so the interior is to the left. Every corner turns left. Up to rotation its successive side directions are east, north, west, south. Closure forces opposite side lengths to agree, so it is a rectangle of width a>=1 and height b>=1.

For six corners, the same orientation gives five left turns and one right turn. Start at an appropriate corner and rotate the polygon so the side directions are

\[
 E,N,W,N,W,S.
\]

There is precisely one right turn, between the first westward and the second northward side; the remaining five turns are leftward. Conversely, cyclically reading the turns of any such hexagon gives this direction sequence after rotating the picture. Write the successive side lengths as

\[
 a+b,\ c,\ b,\ d,\ a,\ c+d,\qquad a,b,c,d\geq1.
\]

These are the only possible lengths: the two westward lengths sum to the eastward length, and the two northward lengths sum to the southward length. The resulting vertices are

\[
 (0,0),\ (a+b,0),\ (a+b,c),\ (a,c),\ (a,c+d),\ (0,c+d).
\]

This is an L-shaped polygon: a bounding rectangle of width a+b and height c+d with its upper right corner cut out. The other possibilities cut out one of the other three corners. The removed corner and the four positive lengths are unique once the bounding rectangle is placed. Positivity rules out a degenerate side, a touching boundary, or a rectangle counted as a hexagon.

Now fix a vertex-simple lattice polygon gamma containing e, with L unit edges and k corners. There are L distinct boundary vertices. At each corner there is exactly one of the two mirror orientations that pairs the two incident polygon edges. At each of the other L-k boundary vertices the state must be empty. Independence therefore gives

\[
 P_p(C(e)=\gamma)=(p/2)^k q^{L-k}.                 \tag{1}
\]

These boundary states suffice: following e traverses every successive polygon edge and returns to e in the same direction. Interior and exterior states do not affect this trajectory. Conversely, if the trajectory is gamma then those boundary states are necessary.

Two different polygons containing e cannot both be its orbit in the same environment, because the local rule determines a unique continuation from each directed edge. Their events in (1) are therefore disjoint, even if the polygons share vertices. This justifies summing (1) over the countable family without inclusion-exclusion.

## 2. Rectangles

For fixed width a and height b, a rectangle has 2a horizontal unit edges. Translating any one of these edges to the undirected edge underlying e gives a different rectangle containing e. There are therefore exactly 2a translates. The orientation of travel around each rectangle is the one that traverses e eastward; it contributes no extra factor of two.

The perimeter is 2a+2b, so the rectangle contribution is

\[
 R_4(p)=\sum_{a,b\geq1}2a(p/2)^4q^{2a+2b-4}.
\]

Put r=q^2<1. The geometric series gives

\[
 \sum_{j\geq1}r^{j-1}=\frac1{1-r},\qquad
 \sum_{j\geq1}j r^{j-1}=\frac1{(1-r)^2}.
\]

For example, the second identity follows by multiplying two copies of the first series: the coefficient of r^{j-1} is j. All terms are nonnegative, so products and rearrangements of the series are valid. Consequently

\[
 R_4(p)=\frac{p^4}{8(1-r)^3}
       =\frac{p}{8(2-p)^3},                       \tag{2}
\]

where 1-r=1-(1-p)^2=p(2-p).

## 3. Hexagons

For fixed a,b,c,d and a specified removed corner, the L-shaped polygon has 2(a+b) horizontal unit edges and perimeter 2(a+b+c+d). The translation count for e is thus 2(a+b). There are four choices of removed corner, giving total multiplicity 8(a+b).

Let s=a+b+c+d. The probability contribution is

\[
 R_6(p)=\sum_{a,b,c,d\geq1}8(a+b)(p/2)^6q^{2s-6}.
\]

Since s>=4, q^{2s-6}=q^2 r^{s-4}. The series factorization is

\[
 \sum_{a,b\geq1}(a+b)r^{a+b-2}
 =\frac{2}{(1-r)^3},\qquad
 \sum_{c,d\geq1}r^{c+d-2}=\frac1{(1-r)^2}.
\]

The first identity separates a+b into its two summands and uses the two geometric identities in Section 2. Hence

\[
 R_6(p)=\frac{p^6q^2}{4(1-r)^5}
       =\frac{p q^2}{4(2-p)^5}.                  \tag{3}
\]

For p=1, every hexagon has at least two straight boundary vertices, which would need to be empty. Its probability is zero, in agreement with (3). In the sums, a zero exponent is interpreted as q^0=1, including q=0.

The classification and disjointness show that (2)+(3) equals the probability in the proposition. Combining the numerators gives (2-p)^2+2(1-p)^2=6-8p+3p^2. Every counted orbit is periodic, giving the stated lower bound. Finally

\[
 \lim_{p\downarrow0}\frac{R_4(p)}p=\frac1{64},\qquad
 \lim_{p\downarrow0}\frac{R_6(p)}p=\frac1{128},
\]

whose sum is 3/128.

## 4. Independent count by perimeter

These counts provide a second derivation of the sums and an explicit finite audit target. Let N_k(2m) count vertex-simple polygons containing e with perimeter 2m and k corners.

For rectangles a+b=m, so

\[
 N_4(2m)=2\sum_{a=1}^{m-1}a=m(m-1),\quad m\geq2.
\]

For hexagons a+b+c+d=m. There are binom(m-1,3) positive compositions. Swapping coordinates shows that each of a,b,c,d has the same total sum over compositions. Since their sum on each composition is m, the total of a+b is (m/2)binom(m-1,3). Thus

\[
 N_6(2m)=4m\binom{m-1}{3}=16\binom m4,\quad m\geq4.
\]

It follows separately from (1) that

\[
 R_4(p)=(p/2)^4\sum_{m\geq2}m(m-1)q^{2m-4},
\]
\[
 R_6(p)=(p/2)^6\sum_{m\geq4}16\binom m4q^{2m-6}.
\]

To evaluate these, the coefficient of r^j in (1-r)^{-k} counts weak compositions of j into k nonnegative parts and is binom(j+k-1,k-1). Taking k=3 and k=5 recovers (2) and (3), respectively. In particular the small-p coefficients can also be read directly as

\[
 \lim_{p\downarrow0}\frac{p^3}{8[p(2-p)]^3}=\frac1{64},\qquad
 \lim_{p\downarrow0}\frac{p^5q^2}{4[p(2-p)]^5}=\frac1{128}.
\]

`audit.py` enumerates rooted self-avoiding walks without this shape classification, compares their four- and six-turn counts to the formulas through perimeter 14, and independently traces all 3^9 environments in a three-by-three box. Its exact rational checks also compare the perimeter sums with (2) and (3), bounding their omitted tails. The data and command appear in `LOG.md` and `audit_data.json`.
