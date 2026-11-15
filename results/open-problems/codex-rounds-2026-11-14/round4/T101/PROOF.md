# Vertex-simple periodic orbits with ten mirrors

Fix the directed edge \(e=((0,0),(1,0))\), and write \(q=1-p\) and
\(d=2-p=1+q\). An orbit is vertex-simple if its boundary vertices in a
period are distinct, except for the closing return. Mirror counts refer
only to vertices on the orbit.

**Proposition.** For \(0<p<1\), the probability that the orbit through
\(e\) is vertex-simple, periodic, and has exactly ten mirrors is

\[
 R_{10}(p)=
 \frac{p q^2\bigl(12+110q^2+312q^4+405q^6+247q^8+58q^{10}\bigr)}
 {128d^9(1+q^2)^3}.                                      \tag{1}
\]

Consequently the exact probability of a vertex-simple periodic orbit
with at most ten mirrors is

\[
 B_{10}(p)=
 \frac{p}{8d^3}+\frac{p q^2}{4d^5}
 +\frac{p q^2(10+23q^2)}{64d^7}+R_{10}(p).                \tag{2}
\]

This is a lower bound on the periodicity probability, strictly larger
than the corresponding eight-mirror bound for every \(0<p<1\). Moreover,

\[
 \lim_{p\downarrow0}\frac{B_{10}(p)}p=\frac{1943}{65536},
 \qquad
 B_{10}(1/2)=\frac{497923}{19683000}.                      \tag{3}
\]

The finite classification used below is an exhaustive calculation:
all 528 polygons are recorded in ten_data.json, and two independent
enumerations agree on their individual boundaries.

## 1. Polygon events and rooting

A mirror turns the ray by a right angle, whereas an empty vertex continues
it straight. Suppressing straight vertices in a vertex-simple periodic
orbit therefore gives a simple orthogonal polygon with positive integer
side lengths. Its corners are exactly its mirrors. Conversely, such a
polygon is followed if its corners have the uniquely required mirror
orientations and its other boundary vertices are empty.

A polygon of perimeter \(L\) and \(k\) corners has \(L\) distinct boundary
vertices. Its required environment has probability

\[
 (p/2)^k q^{L-k}.                                       \tag{4}
\]

The environment outside these boundary vertices is unrestricted.
Different polygons containing \(e\) give disjoint events, since a fixed
environment has a unique continuation from a directed edge.

Count polygons up to translation only. Rotations and reflections remain
distinct unless their boundaries coincide after translation. Traversal
direction and starting vertex do not distinguish polygons. Let

\[
 F_k(r)=\sum_{\gamma}r^{L(\gamma)/2}
\]

sum over these translation classes with \(k\) corners. Perimeter is even,
since total eastward and westward lengths agree, as do total northward
and southward lengths.

For a polygon with \(H\) horizontal unit edges, there are exactly \(H\)
translates containing the underlying undirected edge of \(e\): translate
each horizontal unit edge onto it. The translates are distinct, because
a finite nonempty boundary has no nonzero translation symmetry.
Each translate has exactly one traversal following \(e\) eastward.
There is no additional direction factor.

Coordinate interchange preserves perimeter and exchanges horizontal and
vertical edge counts. At perimeter \(2m\), summing \(H\) over all
translation classes therefore gives \(m\) times the number of classes.
Thus the number \(N_k(2m)\) of polygons containing \(e\) satisfies

\[
 G_k(r):=\sum_m N_k(2m)r^m=rF_k'(r).
\]

The finite gap sums below converge for \(0<r<1\), justifying
differentiation. Substituting (4) gives

\[
 R_k(p)=(p/2)^k q^{-k}G_k(q^2),\qquad 0<p<1.             \tag{5}
\]

## 2. Finite rank polygons and gap sums

Replace the distinct corner x coordinates by consecutive ranks
\(0,\ldots,a-1\), in order, and do the same for the y coordinates.
This produces the rank polygon. A ten-corner orthogonal polygon has
five vertical and five horizontal sides. Every corner x coordinate
is the coordinate of a vertical side, and every corner y coordinate
is the coordinate of a horizontal side. Hence \(a,b\leq5\).
Every ten-corner rank polygon fits in a four-by-four box of unit cells.

Compression preserves simplicity: strictly increasing piecewise linear
maps of each axis give a homeomorphism of the plane. Conversely, choose
any positive integer gap between each successive pair of rank coordinates.
Stretching by these gaps gives a simple orthogonal lattice polygon.
Its rank polygon and its gaps are uniquely recoverable, so these
choices parametrize translation classes without repetition.

In a vertical strip between two consecutive x ranks, the number of
horizontal sides crossing is positive and even. It is positive because
a closed boundary visits coordinate levels on both sides of the strip;
it is even because crossings to the right and left balance.
There are only five horizontal sides, so this number is either two or
four. Write it as \(2c\), where \(c\in\{1,2\}\). A gap of width
\(s\geq1\) contributes \(cs\) to semiperimeter. Apply the same definition
to horizontal strips using vertical sides.

If the combined half-crossing list is \(c_1,\ldots,c_j\), then the
contribution of all its gap stretches to \(F_{10}\) is

\[
 \prod_{i=1}^j\sum_{s\geq1}r^{c_i s}
 =\prod_{i=1}^j\frac{r^{c_i}}{1-r^{c_i}}.                \tag{6}
\]

There are at most eight gaps, since
\(j=(a-1)+(b-1)\leq8\). Put

\[
 t=\frac{r}{1-r},\qquad u=\frac{r^2}{1-r^2}.
\]

## 3. Exhaustive classification

The complete gap table is as follows. A row with \(a\) ones and \(b\)
twos contributes the displayed count times \(t^a u^b\).

| Ones \(a\) | Twos \(b\) | Number of rank polygons |
|---:|---:|---:|
| 6 | 0 | 16 |
| 5 | 1 | 32 |
| 7 | 0 | 80 |
| 6 | 1 | 120 |
| 5 | 2 | 32 |
| 4 | 3 | 8 |
| 8 | 0 | 84 |
| 7 | 1 | 88 |
| 6 | 2 | 52 |
| 5 | 3 | 16 |
| Total | | 528 |

Here is the exhaustive rule producing the table.

1. Take every nonempty subset of the sixteen cells
   \(\{0,1,2,3\}^2\).
2. Take the symmetric difference of their four-edge boundaries.
   These are exactly the boundary edges of the cell union.
3. Require every boundary vertex to have degree two, and require the
   boundary graph to be connected. The resulting graph is a single
   cycle. Unit lattice edges meet only at endpoints, so its embedded
   boundary is simple. Disconnected components, holes, and contacts
   at a vertex are rejected.
4. Traverse the cycle, remove vertices at which it continues straight,
   and require exactly ten remaining corners.
5. Normalize minimum corner coordinates to zero. If the boundary box
   has width \(w\) and height \(h\), require that the corner x coordinates
   are exactly \(\{0,\ldots,w\}\), and the corner y coordinates are exactly
   \(\{0,\ldots,h\}\). This is the rank condition.
6. Record each normalized boundary once, and count the half-crossings
   in its coordinate strips.

There are \(2^{16}-1=65535\) cell subsets. Every rank polygon occurs:
its bounded interior is a union of cells in this box. Conversely, every
retained cell set gives a rank polygon. A boundary determines its cell
interior uniquely: occupancy is zero outside the boundary, changes
across a boundary edge, and is constant across every other cell edge.
Normalization removes repeated translates.

ten_cells.py implements precisely these rules, using Gray-code order to
toggle one cell boundary at a time. Its output gives every corner list,
horizontal and vertical strip weight, and binary cell row word, as well
as the grouped table.

An independent enumeration in audit_ten.py verifies the same finite set
without using cell interiors. A ten-corner polygon can be represented by
cyclic sequences \(x_0,\ldots,x_4\) and \(y_0,\ldots,y_4\), with sides

\[
 (x_i,y_i)\longrightarrow(x_{i+1},y_i)
 \longrightarrow(x_{i+1},y_{i+1}),
 \qquad i\pmod5.                                       \tag{7}
\]

Each sequence is surjective onto its rank set and has unequal cyclic
neighbors. Enumerating the \(a^5\) words for \(a=2,3,4,5\) gives
respectively \(0,30,120,120\) such sequences. The first count is zero
because an odd cycle cannot alternate between two values.
For three ranks, the multiplicities must be \(2,2,1\): choose the
singleton value and position in \(3\cdot5\) ways; the remaining four
positions must alternate between the other two values, in two ways.
This gives 30. For four ranks, choose the repeated value in four ways,
its nonadjacent positions in five ways, and place the remaining three
values in \(3!\) ways, giving 120. Five ranks give \(5!=120\).

Thus there are \((30+120+120)^2=72900\) coordinate pairs.
Test every pair of nonadjacent closed segments in (7) for intersection,
including touching. Adjacent segments are nondegenerate and perpendicular,
so meet only at their common endpoint. Consequently this test retains
exactly the simple boundaries. It retains 5280 representations.
Each polygon has ten representations: five choices of a starting
corner with outgoing horizontal side for each of the two traversal
directions. Taking unordered boundary segment sets gives 528 polygons,
whose individual boundaries agree with the cell calculation.

## 4. Evaluation

The table and (6) give

\[
\begin{aligned}
 F_{10}(r)={}&16t^6+32t^5u
       +80t^7+120t^6u+32t^5u^2+8t^4u^3\\
       &+84t^8+88t^7u+52t^6u^2+16t^5u^3.               \tag{8}
\end{aligned}
\]

To verify the algebra explicitly, use common denominator
\(D=(1-r)^8(1+r)^3\). In table order, the numerators of the ten
summands are

\[
\begin{aligned}
 &16r^6(1-r)^2(1+r)^3,\quad
 32r^7(1-r)^2(1+r)^2,\\
 &80r^7(1-r)(1+r)^3,\quad
 120r^8(1-r)(1+r)^2,\\
 &32r^9(1-r)(1+r),\quad
 8r^{10}(1-r),\\
 &84r^8(1+r)^3,\quad
 88r^9(1+r)^2,\quad
 52r^{10}(1+r),\quad
 16r^{11}.
\end{aligned}
\]

Adding gives

\[
 r^6(16+128r+332r^2+396r^3+224r^4+48r^5)
 =r^6(1+r)(16+112r+220r^2+176r^3+48r^4).
\]

Cancel one factor \(1+r\), yielding

\[
 F_{10}(r)=
 \frac{r^6 A(r)}{(1-r)^8(1+r)^2},\qquad
 A(r)=16+112r+220r^2+176r^3+48r^4.                      \tag{9}
\]

In particular the pole at \(r=-1\) does not disappear:
\(A(-1)=-4\).

Differentiate (9) and multiply by \(r\):

\[
 G_{10}(r)=
 \frac{r^6\bigl[(6A+rA')(1-r^2)+rA(6+10r)\bigr]}
 {(1-r)^9(1+r)^3}.
\]

The polynomial in brackets is

\[
 96+880r+2496r^2+3240r^3+1976r^4+464r^5.
\]

Therefore, writing
\(H(r)=12+110r+312r^2+405r^3+247r^4+58r^5\),

\[
 G_{10}(r)=\frac{8r^6H(r)}{(1-r)^9(1+r)^3}.             \tag{10}
\]

Set \(r=q^2\). Since \(1-q^2=p(2-p)=pd\), (5) and (10)
give

\[
 R_{10}(p)=
 \frac{p^{10}}{2^{10}}q^{-10}
 \frac{8q^{12}H(q^2)}{p^9d^9(1+q^2)^3}
 =\frac{p q^2H(q^2)}{128d^9(1+q^2)^3},
\]

which is (1).

The earlier four-, six-, and eight-corner generating functions are

\[
 F_4=t^2,\qquad F_6=4t^4,\qquad
 F_8=8t^5+4t^4u+18t^6+8t^5u
     =\frac{2r^5(4+7r)}{(1-r)^6}.
\]

The first two arise from rectangles and the four rank L shapes.
The third is independently recovered by the same cell rule in a
three-by-three box, giving exactly the 38 earlier polygons.
Applying (5) gives the first three terms of (2).

A simple orthogonal boundary has total turning \(2\pi\), so its numbers
of convex and reflex corners satisfy \(C-R=4\). Hence its corner count
is even and at least four. The possibilities with at most ten corners
are exactly \(4,6,8,10\). Their events are disjoint, proving (2).
All coefficients of \(H\) are positive, so (1) is strictly positive
for \(0<p<1\), proving the strict improvement.

## 5. Independent coefficients, limits, and tails

Expanding (10), using the binomial series for both factors in its
denominator, gives

\[
 N_{10}(2m)=
 8\sum_{\substack{0\leq i\leq5\\m\geq6+i}}h_i
 \sum_{j=0}^{m-6-i}(-1)^j
   \binom{j+2}{2}\binom{m-6-i-j+8}{8},                  \tag{11}
\]

where \((h_0,\ldots,h_5)=(12,110,312,405,247,58)\).
This signed finite convolution agrees through \(m=30\) with an
independent positive integer dynamic program applied directly to (6).
Direct rooted unit-step self-avoiding walks agree at every even
perimeter through twenty, without using rank polygons or (11):

| Perimeter | 10 | 12 | 14 | 16 | 18 | 20 |
|---|---:|---:|---:|---:|---:|---:|
| Ten-corner polygons through \(e\) | 0 | 96 | 1456 | 10080 | 46440 | 165160 |

For the small-density coefficient, only eight-gap rows of (8) matter.
Indeed, a \(j\)-gap term in \(F_{10}\) has a pole of order \(j\) at
\(r=1\), so \(rF_{10}'\) has a pole of order \(j+1\).
After multiplication by \(p^{10}/2^{10}\), a term with \(j\leq7\)
is \(O(p^2)\). For eight gaps the leading coefficient of \(F_{10}\) is

\[
 84+\frac{88}{2}+\frac{52}{4}+\frac{16}{8}=143,
\]

because \(r^c/(1-r^c)\sim[c(1-r)]^{-1}\).
It follows that

\[
 \lim_{p\downarrow0}\frac{R_{10}(p)}p
 =\frac{8\cdot143}{2^{10}2^9}
 =\frac{143}{65536}.                                   \tag{12}
\]

Independently, \(H(1)=1144\), so substitution into (1) gives
\(1144/(128\cdot2^9\cdot8)=143/65536\) again.
The earlier coefficient is \(225/8192=1800/65536\);
adding proves the first part of (3).
At \(p=1/2\), direct substitution gives

\[
 R_{10}(1/2)=\frac{33971}{39366000},\qquad
 \frac{95}{3888}+\frac{33971}{39366000}
 =\frac{497923}{19683000}.
\]

Exact rational checks at \(p=1/10,1/4,1/2,3/4\) compare (1) with
the gap sums. One computation weights each shape by its horizontal
edge count directly; the other uses the derivative of total
semiperimeter. Both agree exactly.

For a separate infinite-sum check, sum (11) with the probability
weight (4) through semiperimeter \(M=500\). The following positive
majorant bounds the omitted tail without relying on cancellation in
(11). A rank polygon with \(j\leq8\) gaps has at most
\(\binom{m-1}{j-1}\) positive gap assignments of semiperimeter \(m\):
the map \((s_i)\mapsto(c_i s_i)\) injects them into positive
compositions of \(m\) into \(j\) parts. For \(m\geq16\),

\[
 \binom{m-1}{j-1}\leq\binom{m-1}{7},\qquad j\leq8,
\]

by monotonicity of binomial coefficients up to their middle index.
There are 528 rank polygons, and the rooting relation in Section 1
therefore gives

\[
 N_{10}(2m)\leq528m\binom{m-1}{7}.
\]

Let
\[
 T_m=528m\binom{m-1}{7}(p/2)^{10}q^{2m-10}.
\]
For \(0<q<1\),
\[
 \frac{T_{m+1}}{T_m}
 =q^2\frac{m+1}{m-7}.
\]
This ratio decreases with \(m>7\). For the tail \(m\geq M+1\), put
\(\rho=q^2(M+2)/(M-6)\). At every tested density \(\rho<1\),
and the omitted probability is at most \(T_{M+1}/(1-\rho)\).
The script verifies that the closed expression lies between the
partial sum and this upper bound, which is less than \(10^{-30}\).
The exact rational bounds are saved in ten_audit.json.

Finally, (9) has no terms below \(r^6\), so every ten-corner polygon
has perimeter at least twelve and at least two empty boundary vertices.
Thus \(R_{10}(1)=0\). The analogous six- and eight-corner contributions
also vanish at \(p=1\); only the two unit squares through \(e\)
contribute to this restricted family, giving \(B_{10}(1)=1/8\).
This endpoint is checked separately rather than using \(q^{-10}\)
in (5).

These formulas omit polygons with at least twelve corners and every
periodic orbit with repeated vertices. They do not give an upper bound
on the probability of an infinite orbit.
