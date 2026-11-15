# Vertex-simple periodic orbits with twelve mirrors

Fix \(e=((0,0),(1,0))\), and put \(q=1-p\), \(d=2-p=1+q\).
A periodic orbit is vertex-simple if its vertices in one period are distinct,
apart from its closing return. Mirrors are counted only on that orbit.

**Proposition.** For \(0<p<1\), the probability that the orbit through \(e\)
is vertex-simple and periodic with exactly twelve mirrors is

\[
 R_{12}(p)=\frac{p\,H(q^2)}{2048d^{11}(1+q^2)^5},                 \tag{1}
\]

where

\[
\begin{aligned}
 H(r)={}&3+129r+1928r^2+10326r^3+28484r^4\\
        &+45522r^5+43964r^6+25510r^7+8121r^8+1093r^9.
\end{aligned}
\]

Consequently the exact probability of a vertex-simple periodic orbit with
at most twelve mirrors is

\[
\begin{aligned}
 B_{12}(p)={}&\frac{p}{8d^3}+\frac{pq^2}{4d^5}
       +\frac{pq^2(10+23q^2)}{64d^7}\\
       &+\frac{pq^2(12+110q^2+312q^4+405q^6+247q^8+58q^{10})}
                    {128d^9(1+q^2)^3}
       +R_{12}(p).                                            \tag{2}
\end{aligned}
\]

It is a lower bound on the probability of periodicity. In particular,

\[
 \lim_{p\downarrow0}\frac{B_{12}(p)}p
       =\frac{518043}{16777216},\qquad
 B_{12}(1/2)=\frac{1459458421}{56687040000}.                     \tag{3}
\]

The formulas extend to \(p=1\), with
\(R_{12}(1)=3/2048\) and \(B_{12}(1)=259/2048\).
The finite classification in this proof is an exhaustive computation.
Two independent constructions agree on all 9,901 individual rank polygons
and their strip weights; the full lists and scripts accompany the proof.

## Polygon events and the root

At a mirror the ray turns by a right angle, and at an empty vertex it goes
straight. Suppress straight vertices in a vertex-simple periodic orbit.
The resulting boundary is a simple orthogonal polygon with positive integer
side lengths; its corners are exactly the mirrors of the orbit.
Conversely any such polygon is followed when each corner has its uniquely
required mirror and every straight boundary vertex is empty.

A polygon of perimeter \(L\) and \(k\) corners has \(L\) distinct boundary
vertices. Independence gives the probability of these prescribed states as

\[
 (p/2)^k q^{L-k}.                                             \tag{4}
\]

Other vertices are unrestricted. Distinct polygons through the fixed
directed edge give disjoint events: the environment determines a unique
continuation from that edge.

Count polygons up to translation, retaining rotations and reflections
unless their normalized boundaries coincide. Starting corner and traversal
direction do not distinguish boundaries. Let \(F_k(r)\) count these
translation classes with weight \(r^{L/2}\). Perimeter is even because
eastward and westward lengths agree, as do northward and southward lengths.

If a boundary has \(h\) horizontal unit edges, exactly \(h\) of its
translates contain the undirected edge underlying \(e\). Translate each
horizontal edge onto that edge. Two edges cannot produce the same translate,
since a finite nonempty boundary has no nonzero translation symmetry.
For each translate exactly one traversal follows \(e\) eastward.
There is no further traversal factor.

At perimeter \(2m\), coordinate interchange exchanges horizontal and vertical
edge counts and preserves the collection of translation classes. Their
summed horizontal edge counts therefore equal \(m\) times the number of
classes. If \(N_k(2m)\) counts polygons containing \(e\), it follows that

\[
 G_k(r):=\sum_m N_k(2m)r^m=rF_k'(r),\qquad
 R_k(p)=(p/2)^kq^{-k}G_k(q^2).                                \tag{5}
\]

The gap products below converge for \(0<r<1\); their finite sum also
converges and can be differentiated there. This justifies the use of
the generating functions in (5).

## Rank compression and positive gaps

Replace distinct corner x coordinates, in increasing order, by
\(0,\ldots,a-1\), and do the same for y coordinates with
\(0,\ldots,b-1\). The result is the rank polygon. Twelve corners give six
vertical and six horizontal sides. Every corner x coordinate is that of
a vertical side, and every corner y coordinate that of a horizontal side.
Thus \(2\leq a,b\leq6\). All twelve-corner rank polygons fit in a
five-by-five box of unit cells.

Compression preserves simplicity: the coordinate maps extend to strictly
increasing piecewise linear homeomorphisms of each axis, and their product
is a homeomorphism of the plane. Conversely any positive integer gaps
between successive ranks stretch a rank polygon into a simple lattice
polygon. Recovering its distinct corner coordinates recovers the rank
polygon and every gap uniquely. Hence this is a bijective parametrization
of translation classes.

In a vertical strip between consecutive x ranks, the number of horizontal
sides crossing it is positive and even. Positivity follows because the
closed boundary has points on both sides; rightward and leftward crossings
balance. There are only six horizontal sides, so this number is \(2c\)
with \(c\in\{1,2,3\}\). The same holds for horizontal strips.
A gap of width \(s\geq1\) with weight \(c\) contributes \(cs\) to
semiperimeter. Its gap sum is

\[
 \sum_{s\geq1}r^{cs}=\frac{r^c}{1-r^c}.                       \tag{6}
\]

There are \(j=a+b-2\leq10\) gaps. If the combined list contains \(a_1\)
ones, \(a_2\) twos and \(a_3\) threes, its full gap contribution is
\(t^{a_1}u^{a_2}v^{a_3}\), where

\[
 t=\frac r{1-r},\qquad u=\frac{r^2}{1-r^2},\qquad
 v=\frac{r^3}{1-r^3}.                                       \tag{7}
\]

## Exhaustive finite classification

The complete grouped classification is the following. A row counts rank
polygons up to translation only, with the stated multiplicities of
half-crossing weights.

| Ones \(a\) | Twos \(b\) | Threes \(c\) | Count \(M_{abc}\) |
|---:|---:|---:|---:|
| 6 | 0 | 0 | 1 |
| 5 | 1 | 0 | 4 |
| 4 | 2 | 0 | 2 |
| 7 | 0 | 0 | 32 |
| 6 | 1 | 0 | 176 |
| 5 | 2 | 0 | 56 |
| 4 | 3 | 0 | 8 |
| 6 | 0 | 1 | 4 |
| 8 | 0 | 0 | 252 |
| 7 | 1 | 0 | 932 |
| 6 | 2 | 0 | 616 |
| 5 | 3 | 0 | 216 |
| 4 | 4 | 0 | 44 |
| 7 | 0 | 1 | 16 |
| 6 | 1 | 1 | 28 |
| 5 | 2 | 1 | 4 |
| 9 | 0 | 0 | 580 |
| 8 | 1 | 0 | 1456 |
| 7 | 2 | 0 | 1364 |
| 6 | 3 | 0 | 736 |
| 5 | 4 | 0 | 272 |
| 4 | 5 | 0 | 48 |
| 7 | 1 | 1 | 72 |
| 6 | 2 | 1 | 48 |
| 5 | 3 | 1 | 8 |
| 4 | 4 | 1 | 8 |
| 10 | 0 | 0 | 394 |
| 9 | 1 | 0 | 696 |
| 8 | 2 | 0 | 756 |
| 7 | 3 | 0 | 576 |
| 6 | 4 | 0 | 292 |
| 5 | 5 | 0 | 96 |
| 7 | 2 | 1 | 84 |
| 5 | 4 | 1 | 24 |
| Total | | | 9901 |

Here are two exhaustive rules producing the table.

For the first rule, list all length-six words surjective onto
\(\{0,\ldots,a-1\}\), for \(a=2,\ldots,6\), with unequal cyclic
neighbors. There are respectively \(2,60,480,1080,720\) such words.
These counts can also be calculated by inclusion-exclusion:

\[
 S_a=\sum_{j=0}^a(-1)^{a-j}\binom aj\bigl((j-1)^6+j-1\bigr).
\]

Indeed the number of proper colorings of a six-cycle with \(j\) labeled
colors is the trace of the sixth power of its color-transition matrix.
That matrix has zero diagonal and ones off the diagonal, with eigenvalues
\(j-1\) once and \(-1\) with multiplicity \(j-1\), giving the expression
in parentheses for \(j\geq1\); for \(j=0\) both the count and the displayed
expression are zero. Inclusion-exclusion removes unused colors.

For each pair of words \(x,y\), form the twelve sides

\[
 (x_i,y_i)\longrightarrow(x_{i+1},y_i)
          \longrightarrow(x_{i+1},y_{i+1}),\qquad i\pmod6.
                                                                    \tag{8}
\]

Expand each directed side into its integer vertices, including its start
and excluding its endpoint. Require all these half-open vertex sets to be
pairwise disjoint. This condition is exactly simplicity: every intersection
of lattice-aligned sides occurs at an integer vertex; each boundary vertex
is included at the start of exactly one unit edge. Adjacent sides share
only the intended endpoint because they are nondegenerate and perpendicular.
The final endpoint is correctly identified with the first start.

There are \(2342^2=5484964\) word pairs. The test retains 118812
representations. Each simple boundary has twelve representations in (8):
six choices of a starting corner with outgoing horizontal side in each
of its two traversal directions. Canonicalizing by the least corner and
reversal gives \(118812/12=9901\) rank polygons. Strip crossings give the
table. The script twelve.py implements this rule, representing the
half-open vertex sets as integer bitsets.

For the independent rule, write the polygon interior as occupied cells in
its smallest bounding box, of width and height at most five. Enumerate
nonzero binary cell rows of width \(w\), for every \(1\leq w\leq5\)
and every height \(1\leq h\leq5\). Nonzero rows are necessary: the
connected interior projects onto the full vertical interval of its box.
Place zero rows below and above the box. At each vertex between two rows,
inspect its four incident cells:

- One or three occupied cells give one corner.
- Two diagonally opposite occupied cells give four boundary edges and a
  forbidden vertex contact.
- Zero, four, or two adjacent occupied cells give no corner.

Require at least one corner at every y level, exactly twelve corners in
total, and at least one corner at every x level \(0,\ldots,w\).
During row construction reject forbidden contacts, a missing completed
y level, and prefixes with more than ten corners: any completion has at
least two corners at its top boundary. These are necessary conditions,
so pruning loses no rank polygon.

For each remaining row set take the symmetric difference of occupied
cell boundaries. The local tests ensure degree two at every boundary
vertex. Traverse one component and require that it includes every boundary
vertex. A finite connected degree-two graph is a cycle; grid unit edges
intersect only at their endpoints, so this boundary is simple. This last
test excludes holes and disconnected boundaries. Conversely any simple
rank polygon passes these tests and its cell interior is unique.
Thus the rule gives exactly the required polygons, each once.

The cell rule visits 129988 row prefixes and gives 18525 local candidates.
It rejects 8624 disconnected boundaries and retains 9901 polygons.
The script audit_twelve.py compares each boundary's unordered side set
with the first rule's output; all agree. Strip weights are independently
calculated from cell row differences: horizontal boundary edges in a
column occur precisely where consecutive row bits differ; vertical
boundary edges in a row occur where consecutive column bits differ,
including outside zero bits. Halving these counts gives both oriented
strip lists, which also agree individually.

These finite rules specify every test used for the table; twelve_data.json
records all corner lists and twelve_audit.json all cell rows.

## Exact gap algebra

By (6) and the table,
\[
 F_{12}(r)=\sum_{a,b,c}M_{abc}t^a u^b v^c.                    \tag{9}
\]

A common denominator is
\[
 D=(1-r)^{10}(1+r)^5(1+r+r^2).
\]

The contribution of a table row to the numerator is
\[
 M_{abc}r^{a+2b+3c}(1-r)^{10-a-b-c}
                         (1+r)^{5-b}(1+r+r^2)^{1-c}.
\]

All exponents are nonnegative in the table. Adding these polynomials
gives \(r^6P(r)\), where
\[
\begin{aligned}
 P(r)={}&1+38r+528r^2+2945r^3+9118r^4+17942r^5\\
        &+23970r^6+22334r^7+14381r^8+6100r^9+1526r^{10}
          +165r^{11}\\
       ={}&(1+r)(1+r+r^2)A(r),
\end{aligned}
\]
with
\[
\begin{aligned}
 A(r)={}&1+36r+454r^2+1964r^3+4246r^4\\
        &+5068r^5+3378r^6+1196r^7+165r^8.
\end{aligned}
\]

This explicit identity accounts for the cancellation of the factor
\(1+r+r^2\), despite the weight-three strips. Cancelling gives

\[
 F_{12}(r)=\frac{r^6A(r)}{(1-r)^{10}(1+r)^4}.                  \tag{10}
\]

Since \(A(-1)=-20\), its pole at \(-1\) has order four.
Differentiating (10) and using (5) gives

\[
 G_{12}(r)=
 \frac{r^6[(6A+rA')(1-r^2)+rA(6+14r)]}
 {(1-r)^{11}(1+r)^5}
 =\frac{2r^6H(r)}{(1-r)^{11}(1+r)^5}.                        \tag{11}
\]

The last equality follows by expanding the bracket: its coefficients,
from degree zero through nine, are
\[
 (6,258,3856,20652,56968,91044,87928,51020,16242,2186).
\]
Both polynomial identities are also expanded independently in
audit_twelve.py.

Set \(r=q^2\). Since \(1-q^2=p(2-p)=pd\), equations (5) and (11) yield
\[
 R_{12}(p)
 =\frac{p^{12}}{2^{12}}q^{-12}
       \frac{2q^{12}H(q^2)}{p^{11}d^{11}(1+q^2)^5},
\]
which simplifies to (1).

For completeness, the earlier four-, six-, eight-, and ten-corner
translation-class series are
\[
\begin{aligned}
 F_4&=\frac{r^2}{(1-r)^2},&
 F_6&=\frac{4r^4}{(1-r)^4},\\
 F_8&=\frac{2r^5(4+7r)}{(1-r)^6},&
 F_{10}&=\frac{r^6(16+112r+220r^2+176r^3+48r^4)}
                    {(1-r)^8(1+r)^2}.
\end{aligned}
\]
Their derivations are in the earlier folders; the full ten-corner boundary
list, series, probability values, and linear coefficient have been
independently regenerated here. Applying (5) gives the first four terms
of (2). The turning angle of a simple orthogonal polygon is \(2\pi\);
if \(C,R\) are its convex and reflex corner counts, \(C-R=4\).
Its corner count is therefore even and at least four. Thus the cases
with at most twelve corners are precisely \(4,6,8,10,12\), and their
disjoint events prove (2). All coefficients of \(H\) are positive, so
\(R_{12}(p)>0\) for \(0<p<1\): the lower bound strictly improves.

## Coefficients and an independent infinite-sum audit

Write \(H(r)=\sum_{i=0}^9h_i r^i\). Expanding the two denominator factors
in (11) by the binomial theorem gives the finite expression
\[
 N_{12}(2m)=2\sum_{\substack{0\leq i\leq9\\m\geq6+i}}h_i
 \sum_{j=0}^{m-6-i}(-1)^j
       \binom{j+4}{4}\binom{m-6-i-j+10}{10}.                  \tag{12}
\]
For \(m<6\) the outer sum is empty and the count is zero.
This signed expression agrees through \(m=40\) with a positive
coefficient calculation from (9), which sums the geometric series (6)
one gap at a time. An independent search over rooted unit-step
self-avoiding walks gives:

| Perimeter | 12 | 14 | 16 | 18 | 20 |
|---|---:|---:|---:|---:|---:|
| Twelve-corner boundaries through \(e\) | 6 | 294 | 5560 | 51012 | 304800 |

The walk search starts with the fixed eastward edge, permits straight
and left/right turns, and rejects repeated vertices except the closing
return. It includes the closing turn at the starting vertex and the turn
at the endpoint of the root edge. Manhattan distance to the origin bounds
the remaining length. It agrees at every even perimeter through twenty
for all five corner counts \(4,6,8,10,12\).

For a separate probability check, substitute \(p=1/10,1/4,1/2,3/4\)
in the exact gap products. Direct horizontal-root weighting and total
semiperimeter differentiation both give (1). Separately sum (12)
with the weights (4) through semiperimeter \(M=500\).

Here is a rigorous positive bound on the omitted tail. A rank polygon
with \(j\leq10\) gaps and weights \(c_i\) has at most
\(\binom{m-1}{j-1}\) stretches of semiperimeter \(m\): the injection
\((s_i)\mapsto(c_i s_i)\) sends them into positive compositions of \(m\).
For \(m\geq20\), monotonicity of the binomial coefficients up to their
middle gives
\(\binom{m-1}{j-1}\leq\binom{m-1}{9}\).
There are 9901 rank polygons, so the rooting identity in (5) gives
\[
 N_{12}(2m)\leq9901m\binom{m-1}{9}.
\]
Put
\[
 T_m=9901m\binom{m-1}{9}(p/2)^{12}q^{2m-12}.
\]
For \(0<q<1\), its successive ratio is
\[
 \frac{T_{m+1}}{T_m}=q^2\frac{m+1}{m-9},
\]
which decreases with \(m>9\). On the omitted range \(m\geq M+1\),
it is at most \(\rho=q^2(M+2)/(M-8)\).
At all tested densities \(\rho<1\), and
\(T_{M+1}/(1-\rho)\) bounds the whole omitted probability.
The exact closed expression lies between the finite sum and that sum
plus this bound, with bound less than \(10^{-30}\).
The \(q=0\) endpoint is checked directly below; its tail is zero.
All rational tail bounds are stored exactly.

## Small density, the half-density value, and the endpoint

Only the table's ten-gap rows contribute at linear order as
\(p\downarrow0\). Indeed \(r^c/(1-r^c)\sim[c(1-r)]^{-1}\);
a \(j\)-gap product has a pole of order \(j\), and its rooted derivative
a pole of order at most \(j+1\). Multiplication by \(p^{12}\), with
\(1-q^2\sim2p\), makes every \(j\leq9\) contribution \(O(p^2)\).
For the ten-gap rows the leading coefficient of \(F_{12}\) is
\[
 394+\frac{696}{2}+\frac{756}{4}+\frac{576}{8}
 +\frac{292}{16}+\frac{96}{32}
 +\frac{84}{12}+\frac{24}{48}=\frac{4127}{4}.
\]
Thus
\[
 \lim_{p\downarrow0}\frac{R_{12}(p)}p
 =\frac{10(4127/4)}{2^{12}2^{11}}
 =\frac{20635}{16777216}.
\]
Independently \(H(1)=165080\), so (1) gives the same constant
\(165080/(2048\cdot2^{11}\cdot2^5)\).
Adding the earlier coefficient \(1943/65536\) gives
\(518043/16777216\), as in (3).

Direct substitution at \(p=1/2\) gives
\[
 R_{12}(1/2)=\frac{25440181}{56687040000},\qquad
 \frac{497923}{19683000}+R_{12}(1/2)
 =\frac{1459458421}{56687040000}.
\]

At \(p=1\), a positive-probability boundary in this family must have
no straight vertices, hence perimeter twelve. The coefficient of \(r^6\)
in (10) is one: there is one translation class of such polygons, the
boundary of the five-cell cross with rows 010/111/010. It has twelve
corners and six horizontal unit edges, hence six translates through \(e\).
Each has probability \(2^{-12}\), giving
\(R_{12}(1)=6/4096=3/2048\). This also agrees with (1).
The four-corner term contributes \(1/8\); the six-, eight-, and
ten-corner terms have straight vertices and contribute zero.
Therefore \(B_{12}(1)=1/8+3/2048=259/2048\).

The result omits simple orbits with at least fourteen mirrors and every
periodic orbit that repeats a vertex. It provides no upper bound forcing
the probability of an infinite orbit to vanish.
