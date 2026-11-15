# Periodic orbits with repeated vertices and at most eight turns

Fix the directed edge \(e=((0,0),(1,0))\). Put \(q=1-p\), \(d=2-p=1+q\),
and \(r=q^2\). A turning visit is one passage through a mirror. A mirror
visited twice counts as two turning visits and one distinct mirror.

Let \(A\) be the event that the orbit through \(e\) is periodic, repeats
a vertex during one period, and has at most eight turning visits.

**Proposition.** For \(0<p<1\),
\[
\begin{aligned}
 C(p):=\mathbb P_p(A)
 ={}&\frac{p}{16d^4}+\frac{9pq^2}{64d^7}\\
 &+\frac{pq^3(15+34q^2+17q^4)}
                 {32d^7(1+q^2)^2}.                         \tag{1}
\end{aligned}
\]
The same formula holds at \(p=1\). In particular,
\[
 \lim_{p\downarrow0}\frac{C(p)}p=\frac{37}{4096},
 \qquad C(1/2)=\frac{164}{18225},\qquad C(1)=\frac1{16}.    \tag{2}
\]

Let \(B_{12}(p)\) be the preceding session's exact probability of a
vertex-simple periodic orbit with at most twelve mirrors. Those events
are disjoint from \(A\), so
\[
 \mathbb P_p(e\text{ has a periodic orbit})\geq B_{12}(p)+C(p).
                                                               \tag{3}
\]
Thus
\[
\begin{aligned}
 \liminf_{p\downarrow0}
 \frac{\mathbb P_p(e\text{ has a periodic orbit})}{p}
 &\geq\frac{669595}{16777216},\\
 B_{12}(1/2)+C(1/2)&=\frac{1969564021}{56687040000},\\
 B_{12}(1)+C(1)&=\frac{387}{2048}.
\end{aligned}                                                   \tag{4}
\]
Formula (1) is an exact restricted-family probability. It is not the
probability of all periodic orbits with at most eight distinct mirrors.
The finite classification below is computational: two exhaustive
constructions agree on all 62 rank circuits, including their local states
and strip weights. The complete corner lists are in repeated_data.json.

## 1. Finite orbits and compatible circuits

At each lattice vertex the local state pairs its four incident edge ends.
The empty state pairs opposite ends; each mirror state pairs adjacent ends,
in one of the two possible ways. Form an auxiliary graph whose vertices are
the undirected lattice edges. Join two of these vertices when the
corresponding edges are paired at a lattice vertex.

Each vertex of the auxiliary graph has degree two: a lattice edge has one
partner at each endpoint. Traversing a ray follows this graph without
backtracking. Upon entering a lattice edge through one endpoint, it leaves
through the other endpoint, so its next partner differs from its preceding
partner. A finite component of a degree-two graph is a cycle. Therefore
every periodic ray traverses each undirected lattice edge in its period
exactly once. In particular it visits each lattice vertex at most twice.

Conversely, consider a closed lattice walk using each undirected edge at
most once, with no immediate reversal. At every visited vertex require
that all its passages use one common local state. When this holds, prescribing
those states makes the ray follow the entire circuit. The period cannot be
shorter, since no edge occurs twice. Call such a walk a compatible circuit.
Starting position and reversal of traversal do not distinguish circuits.

A vertex visited twice uses all four edge ends. If it is empty, the two
passages cross straight through. If it carries a mirror, the two passages
use the two pairings of that same mirror. A vertex cannot be both straight
and turning: those passages would require different states.

Suppress straight visits to obtain a cyclic list of corners and straight
sides of positive integer length. Horizontal and vertical sides alternate.
Thus the number \(k\) of turning visits is even. Closure requires both
positive and negative displacement on each used axis, so \(k\geq4\).
A four-turn closed orthogonal walk is a rectangle and is vertex-simple.
Only \(k=6,8\) can contribute to \(A\).

Write \(t\) for the number of mirror vertices visited twice and \(c\) for
the number of empty vertices visited twice. A period of length \(L\) has
\(k-t\) distinct mirror vertices. Its straight visits number \(L-k\);
the number of distinct empty vertices is \(L-k-c\). Its required states
therefore have probability
\[
             (p/2)^{k-t}q^{L-k-c}.                          \tag{5}
\]
States away from the circuit are unrestricted. Distinct circuits through
\(e\) give disjoint events: the environment determines the unique
continuation from that directed edge.

## 2. Ranks, positive gaps and rooting

Replace the distinct corner x coordinates by their ordered ranks, and do
the same for y. There are \(k/2\) vertical and \(k/2\) horizontal sides;
every corner x coordinate is a vertical side coordinate, and every corner
y coordinate is a horizontal side coordinate. Hence the number of distinct
coordinates on either axis lies between two and \(k/2\).
For \(k\leq8\) every rank circuit lies in the vertex grid
\(\{0,1,2,3\}^2\).

Strictly increasing piecewise linear changes of the two coordinates are
homeomorphisms of the plane. They preserve intersections, edge overlaps,
the order of visits and required mirror states. In particular they preserve
compatibility and the values of \(k,t,c\). Every intersection of a horizontal
and vertical side has its x coordinate from a vertical side and its y
coordinate from a horizontal side, so these intersections are retained by
corner-coordinate compression. Every choice of positive integer gaps
between successive ranks stretches a rank circuit to a compatible lattice
circuit. The distinct corner coordinates uniquely recover the rank circuit
and its gaps. This parametrizes circuits up to translation.

Across a strip between consecutive x ranks, horizontal sides cross equally
often in the positive and negative directions. The total is positive, since
the closed circuit has points on both sides. There are at most four horizontal
sides, so the crossing count is \(2w\), with \(w=1\) or \(2\).
Define the same weights for y strips. A positive gap of width \(s\) in a
weight-\(w\) strip contributes \(ws\) to semiperimeter \(L/2\). Its sum is
\[
        \sum_{s\geq1}r^{ws}=\frac{r^w}{1-r^w}.
\]
Write
\[
              T=\frac r{1-r},\qquad U=\frac{r^2}{1-r^2}.     \tag{6}
\]
A rank circuit with \(a\) weight-one gaps and \(b\) weight-two gaps
contributes \(T^aU^b\).

For fixed \(k,t,c\), let \(F_{ktc}(r)\) be the sum of \(r^{L/2}\)
over translation classes. Rotations and reflections are retained unless
the normalized circuits coincide. If a circuit has \(H\) horizontal unit
edges, exactly \(H\) of its translates contain the undirected edge underlying
\(e\). Distinct edges give distinct translations; the circuit uses no edge
twice. Each translate has one traversal following \(e\) eastward.
There is no extra orientation factor.

Coordinate interchange preserves \(k,t,c,L\) and exchanges horizontal
and vertical edge counts. At perimeter \(2m\), the sum of horizontal
edge counts over all translation classes is therefore \(m\) times the
number of classes. Consequently the rooted counting series is
\[
 G_{ktc}(r)=rF_{ktc}'(r).
\]
All the gap products converge for \(0<r<1\); their finite sums can be
differentiated there. By (5), the probability contribution is
\[
 P_{ktc}(p)=(p/2)^{k-t}q^{-k-c}G_{ktc}(q^2).               \tag{7}
\]

## 3. Exhaustive classification

Here is the full table of non-simple rank circuits. Each row counts
circuits with the indicated multiplicities of strip weights.

| \(k\) | \(t\) | \(c\) | Ones \(a\) | Twos \(b\) | Count |
|---:|---:|---:|---:|---:|---:|
| 6 | 0 | 1 | 4 | 0 | 2 |
| 8 | 0 | 1 | 4 | 1 | 8 |
| 8 | 0 | 1 | 4 | 2 | 4 |
| 8 | 0 | 1 | 5 | 1 | 16 |
| 8 | 0 | 1 | 6 | 0 | 12 |
| 8 | 0 | 2 | 4 | 1 | 4 |
| 8 | 0 | 2 | 5 | 1 | 8 |
| 8 | 0 | 2 | 6 | 0 | 2 |
| 8 | 0 | 3 | 4 | 2 | 4 |
| 8 | 1 | 0 | 4 | 0 | 2 |
| Total | | | | | 62 |

The following two finite rules specify and verify the table.

For the first, put \(n=k/2\). List the length-\(n\) words surjective onto
\(\{0,\ldots,j-1\}\), for every \(2\leq j\leq n\), with unequal cyclic
neighbors. There are \(2,6,38\) words for \(k=4,6,8\), respectively.
For each pair \(x,y\) form the corner list
\[
 (x_i,y_i),\ (x_{i+1},y_i),\qquad i\pmod n.                 \tag{8}
\]
Every rank circuit has such a representation: start at a corner with a
horizontal outgoing side. Nondegeneracy is exactly the unequal-neighbor
condition.

Expand its sides into unit edges and vertices. Reject a repeated undirected
edge. For each visit to a vertex, compare incoming direction \((u,v)\)
with outgoing direction. The possible local rules are
\[
 (u,v)\mapsto(u,v),\qquad
 (u,v)\mapsto(v,u),\qquad
 (u,v)\mapsto(-v,-u).
\]
Reject an immediate reversal or visits demanding different rules at one
vertex. These tests are necessary and sufficient for a compatible circuit.
Count repeated vertices by their states, giving \(c,t\), and count unit
horizontal and vertical edges across each strip, giving the two weight lists.

Canonicalize the corner list by taking the lexicographic minimum over its
cyclic shifts and reversal. Repeated corner coordinates are allowed.
The numbers of candidate pairs are \(4,36,1444\); the numbers of retained
representations are \(4,36,784\). Every circuit has \(k\) representations:
there are \(k/2\) possible starting corners with horizontal outgoing side
in each traversal direction. No two representations coincide, since a
coinciding cyclic segment list would repeat an undirected edge. The counts
of compatible rank circuits are therefore \(1,6,98\). The vertex-simple
subsets number \(1,4,38\), leaving the 62 circuits in the table.
The script repeated.py implements this rule.

For the independent rule, enumerate rays by revealing local states along
unit steps in the vertex grid \(\{0,1,2,3\}^2\). At the first visit to a
vertex choose any of the three states; at a later visit use its already
chosen state. Start by traversing upwards each of the three unit edges
on \(x=0\), separately, with each possible state at the starting vertex.
Every normalized rank circuit has a vertical side on \(x=0\), so some
choice of this root and traversal direction finds it.

Reject departures outside the grid, more than eight turning visits, or a
repeated undirected edge. The sole permitted repeated edge is the original
directed edge, which records closure without adding another copy. Cap the
length at 24, the total number of grid edges. No compatible circuit in this
grid can exceed that cap. Manhattan distance to the initial vertex is a
lower bound on the number of remaining steps, and supplies an additional
safe pruning test.

At closure, extract the turning vertices, normalize translation, and retain
only circuits using every integer corner coordinate level between their
extremes. This is exactly the rank condition. Identify a circuit by its
unordered set of maximal straight sides and required mirror states at their
endpoints. These determine its local pairings and hence its traversal.
Compute strip weights directly from unit edge counts. The search visits
21,590 prefixes and recovers exactly the same 62 circuits and both strip
lists. It uses no coordinate words. The script audit_repeated.py implements
this rule.

These exhaustive constructions cover repeated mirror vertices, transverse
empty crossings, contacts, and parallel overlaps. Contacts demanding different
states or a repeated edge are rejected by the local compatibility rule,
rather than by imposing vertex simplicity.

## 4. Gap sums and the probability formula

The table gives
\[
\begin{aligned}
 F_{601}&=2T^4,\\
 F_{801}&=8T^4U+4T^4U^2+16T^5U+12T^6,\\
 F_{802}&=4T^4U+8T^5U+2T^6,\\
 F_{803}&=4T^4U^2,\\
 F_{810}&=2T^4.
\end{aligned}
\]
Using (6), these become
\[
\begin{aligned}
 F_{601}=F_{810}&=\frac{2r^4}{(1-r)^4},\\
 F_{801}&=\frac{r^6(20+40r+24r^2)}{(1-r)^6(1+r)^2},\\
 F_{802}&=\frac{6r^6}{(1-r)^6},\\
 F_{803}&=\frac{4r^8}{(1-r)^6(1+r)^2}.                     \tag{9}
\end{aligned}
\]
For the second identity, the numerator over its displayed denominator,
after removing \(r^6\), is
\[
 8(1-r^2)+4r^2+16r(1+r)+12(1+r)^2=20+40r+24r^2.
\]
For the third, the numerator over \((1-r)^6(1+r)\), after removing
\(r^6\), is \(4(1-r)+8r+2(1+r)=6(1+r)\).
The other identities follow immediately from (6).

For \(F=N/[(1-r)^a(1+r)^b]\), differentiation gives
\[
 rF'=\frac{r\{N'(1-r^2)+N[(a-b)+(a+b)r]\}}
                    {(1-r)^{a+1}(1+r)^{b+1}}.
\]
Applying it to (9) and cancelling common factors yields
\[
\begin{aligned}
 G_{601}=G_{810}&=\frac{8r^4}{(1-r)^5},\\
 G_{801}&=\frac{8r^6(15+45r+49r^2+17r^3)}
                            {(1-r)^7(1+r)^3},\\
 G_{802}&=\frac{36r^6}{(1-r)^7},\\
 G_{803}&=\frac{16r^8(2+r)}{(1-r)^7(1+r)^3}.
\end{aligned}                                                   \tag{10}
\]
All numerator identities in (9) and (10) are also expanded independently
by the audit script.

Since \(1-r=p d\), substitution in (7) gives the five probabilities
\[
\begin{aligned}
 P_{601}&=\frac{pq}{8d^5},&
 P_{810}&=\frac{p^2}{16d^5},\\
 P_{801}&=\frac{pq^3(15+45r+49r^2+17r^3)}
                         {32d^7(1+r)^3},\\
 P_{802}&=\frac{9pq^2}{64d^7},&
 P_{803}&=\frac{pq^5(2+r)}{16d^7(1+r)^3}.                 \tag{11}
\end{aligned}
\]
For example, \(G_{801}\) contains \(r^6=q^{12}\), while its factor
in (7) is \(p^8q^{-9}/256\). The resulting power is \(pq^3\)
after the factor \((1-r)^7=p^7d^7\) is removed.
For \(P_{810}\), there are seven distinct mirrors, not eight.

The first and last families combine as
\[
       P_{601}+P_{810}=\frac{p(2q+p)}{16d^5}
                     =\frac{p}{16d^4}.
\]
Also
\[
\begin{aligned}
 &(15+45r+49r^2+17r^3)+2r(2+r)\\
 &\hspace{1cm}=15+49r+51r^2+17r^3
              =(1+r)(15+34r+17r^2).
\end{aligned}
\]
Thus \(P_{801}+P_{803}\) is the last term of (1).
Adding \(P_{802}\) proves (1).

There is a separate geometric derivation of \(P_{601}+P_{810}\).
Take two rectangles in diagonally opposite quadrants, meeting at a corner.
Their four widths and heights \(a,b,c,f\) are positive integers.
There are two diagonal placements up to translation; interchanging the
two rectangles does not introduce another placement. Six outer corners
require mirrors. At the common vertex either the empty state or the
joining mirror produces one circuit; the other mirror separates the two
rectangles. The common state's total probability is \(q+p/2=d/2\).
All \(L-8\) other vertices are straight and empty.

The perimeter is \(L=2(a+b+c+f)\) and horizontal edge count \(2(a+b)\).
Summing over both placements and rooting gives
\[
\begin{aligned}
 &(p/2)^6(q+p/2)
   \sum_{a,b,c,f\geq1}4(a+b)q^{2(a+b+c+f)-8}\\
 &\quad=(p/2)^6(q+p/2)\frac8{(1-r)^5}
       =\frac{p}{16d^4}.
\end{aligned}
\]
The identity for the sum follows by separating \(a+b\):
the two differentiated geometric sums contribute
\(2(1-r)^{-3}\), and the remaining two gaps contribute
\((1-r)^{-2}\). This checks the combined weight of an empty crossing
and a mirror visited twice without relying on the rank enumeration.

## 5. Coefficient, probability and endpoint audits

An independent unbounded local-state walk search, with the root \(e\) fixed,
gives the following counts. Length is the number of distinct undirected edges.

| Length | \((6,0,1)\) | \((8,0,1)\) | \((8,0,2)\) | \((8,0,3)\) | \((8,1,0)\) |
|---:|---:|---:|---:|---:|---:|
| 8 | 8 | 0 | 0 | 0 | 8 |
| 10 | 40 | 0 | 0 | 0 | 40 |
| 12 | 120 | 120 | 36 | 0 | 120 |
| 14 | 280 | 840 | 252 | 0 | 280 |
| 16 | 560 | 3392 | 1008 | 32 | 560 |

It visits 524,186 prefixes, reveals local states on first visits, and
follows them on repeated visits. It agrees with all coefficients from
the gap products through length 16.

For a second coefficient calculation, the first and last columns have
coefficient \(8\binom m4\) at length \(2m\), and the middle column
\((8,0,2)\) has \(36\binom m6\). For \((8,0,1)\) and \((8,0,3)\),
write their numerator in (10) as \(r^s\sum_i h_i r^i\). The pairs are
\[
 (s,(h_i))=(6,(120,360,392,136)),\qquad(8,(32,16)).
\]
Expanding the denominator gives the rooted coefficient
\[
 \sum_{\substack{i\\m\geq s+i}} h_i
   \sum_{j=0}^{m-s-i}(-1)^j\binom{j+2}{2}
                         \binom{m-s-i-j+6}{6}.              \tag{12}
\]
These formulas agree through length 80 with a positive dynamic program
that multiplies the geometric gap series one at a time.

There is also a direct environment check, independent of the shape
weights. Exhaust all \(3^9=19683\) states in the vertex box
\(\{-1,0,1\}^2\), trace from \(e\), and retain precisely the orbits in
\(A\) that close before exiting. There are 36 successful full configurations.
Their counts by total mirrors in the box, including unused vertices, are
\(2,10,16,8\) for totals \(6,7,8,9\). Their probability is consequently
\[
 2(p/2)^6q^3+10(p/2)^7q^2+16(p/2)^8q+8(p/2)^9.
\]
The independently counted orbits in the box are two with six mirrors
and one empty vertex and two with seven mirrors and no empty vertex.
Their probability is
\[
                    2(p/2)^6q+2(p/2)^7.
\]
These expressions agree: in the first pair of orbit events two unused
vertices sum out with factor \((q+p)^2=1\), and in the second pair
two unused vertices do the same. Expanding the latter expression with
these unused-vertex factors reproduces the histogram. Exact evaluation
also agrees at \(p=1/4,1/2,3/4,1\).

For each of the five families, direct rational gap sums at
\(p=1/10,1/4,1/2,3/4\) agree with (11). Independently sum (12), or the
nonnegative binomial formula for the other families, with the weights
(5) through semiperimeter \(M=500\). The endpoint \(p=1\) is included.

Here is a bound for the omitted tails. Suppose a family has \(K\) rank
circuits and at most \(J\leq6\) gaps. A rank circuit with \(j\leq J\)
gaps of weights \(w_i\) has at most \(\binom{m-1}{j-1}\) stretches of
semiperimeter \(m\): the map \((s_i)\mapsto(w_i s_i)\) injects its positive
solutions into positive \(j\)-part compositions of \(m\).
For \(m\geq2J\), this is at most \(\binom{m-1}{J-1}\), by monotonicity
of binomial coefficients up to their middle. After summing horizontal
roots by coordinate interchange, the rooted count is at most
\(Km\binom{m-1}{J-1}\). Therefore a tail term is bounded by
\[
 T_m=Km\binom{m-1}{J-1}(p/2)^{k-t}q^{2m-k-c}.
\]
For \(q>0\),
\[
 \frac{T_{m+1}}{T_m}=q^2\frac{m+1}{m-J+1}.
\]
This decreases with \(m\). On \(m\geq M+1\), it is at most
\(\rho=q^2(M+2)/(M+2-J)\). At all tested densities \(\rho<1\),
so the tail is at most \(T_{M+1}/(1-\rho)\).
All 25 family/density sums lie between the closed value minus this
bound and the closed value, and every bound is below \(10^{-30}\).
The exact bounds are stored in repeated_audit.json.
At \(q=0\) the omitted tail is zero.

For the small-density limit, (1) gives
\[
 \frac1{256}+\frac9{8192}+\frac{15+34+17}{32\cdot2^7\cdot4}
       =\frac{37}{4096}.
\]
A second calculation uses the table directly. A term \(nT^aU^b\),
with \(j=a+b\), has leading singularity
\(n/[2^b(1-r)^j]\). Its rooted derivative has leading singularity
\(jn/[2^b(1-r)^{j+1}]\). By (7) its order at small \(p\) is
\(p^{k-t-j-1}\). Only the rows with \(k-t-j-1=1\) contribute to
the linear coefficient. They give
\[
 \frac{2\cdot4}{2^{11}}
 +\frac{4\cdot6}{2^{17}}
 +\frac{16\cdot6}{2^{16}}
 +\frac{12\cdot6}{2^{15}}
 +\frac{8\cdot6}{2^{16}}
 +\frac{2\cdot6}{2^{15}}
 +\frac{4\cdot6}{2^{17}}
       =\frac{37}{4096}.
\]
The repeated-mirror family has four gaps and seven distinct mirrors;
its contribution is of order \(p^2\).

At \(p=1/2\), \(P_{601}+P_{810}=1/162\),
\(P_{802}=1/972\), and
\(P_{801}+P_{803}=131/72900\). Their sum is \(164/18225\).
At \(p=1\), every family with a repeated empty vertex contributes zero.
The only surviving family is \((8,1,0)\). With no straight vertices,
its circuits have length eight; its coefficient in (10) is eight.
Each has seven distinct mirrors and probability \(2^{-7}\), so its
total is \(8/128=1/16\), agreeing with (1).

Finally, the preceding twelve-corner result was rechecked against all its
9,901 boundaries, exact polynomial identities, independent unit walks,
probability values and tails. Its coefficient is \(518043/16777216\),
its half-density value is \(1459458421/56687040000\), and its endpoint
is \(259/2048\). Adding (2) gives (4).

The event counted in (1) omits repeated-vertex orbits with ten or more
turning visits. Bound (3) also omits simple orbits with at least fourteen
mirrors. It provides no upper bound forcing the probability of an infinite
orbit to vanish.
