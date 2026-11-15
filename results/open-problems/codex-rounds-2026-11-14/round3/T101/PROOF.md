# Vertex-simple periodic orbits with at most eight mirrors

Fix the directed edge \(e=((0,0),(1,0))\). Write \(P_p\) for the law of the
independent mirror environment, \(q=1-p\), and \(d=2-p\). A periodic orbit is
vertex-simple if the vertices during one period are distinct, apart from the
closing return. Mirrors below are counted only on that orbit.

**Proposition.** For \(0<p<1\), the probability that the orbit through \(e\)
is vertex-simple, periodic, and has exactly eight mirrors is

\[
 R_8(p)=\frac{p q^2(10+23q^2)}{64d^7}.                 \tag{1}
\]

The probability that it is vertex-simple, periodic, and has at most eight
mirrors is therefore

\[
\begin{aligned}
 B_8(p)
 &=\frac{p}{8d^3}+\frac{p q^2}{4d^5}
        +\frac{p q^2(10+23q^2)}{64d^7}\\
 &=\frac{p(8+32q+74q^2+64q^3+47q^4)}{64(1+q)^7}.
                                                               \tag{2}
\end{aligned}
\]

Consequently

\[
 P_p(\text{the orbit through }e\text{ is periodic})\geq B_8(p),
 \qquad
 \liminf_{p\downarrow0}
 \frac{P_p(\text{the orbit through }e\text{ is periodic})}{p}
 \geq\frac{225}{8192}.                                  \tag{3}
\]

In particular, \(R_8(1/2)=7/3888\) and \(B_8(1/2)=95/3888\).
The formulas extend to \(p=1\), where \(R_8(1)=0\) and \(B_8(1)=1/8\).
The finite classification in Section 4 is given explicitly and is also checked
by two exhaustive enumerations in the accompanying scripts.

## 1. From trajectories to polygons

An empty vertex continues a ray straight; a mirror turns it through a right
angle. Suppressing the straight vertices of a vertex-simple closed orbit gives
a simple orthogonal lattice polygon with positive integer side lengths. Its
corners are precisely its mirrors. Conversely, a simple orthogonal lattice
polygon can be followed by the ray when each corner has the unique required
mirror and every other boundary vertex is empty.

Let such a polygon have \(k\) corners and \(L\) unit boundary edges. There are
exactly \(L\) distinct boundary vertices. The probability of the required
boundary states is

\[
 (p/2)^k q^{L-k}.                                      \tag{4}
\]

States away from the boundary are unrestricted. Distinct polygons through
\(e\) give disjoint events, because the continuation from a directed edge in
a fixed environment is unique. Thus their probabilities can be summed.

Orient a simple polygon with its interior on the left. If \(C\) and \(R\)
denote its convex and reflex corner counts, the total turning is \(2\pi\),
so \(C-R=4\). Hence \(k=C+R\) is even and at least four. The cases with
at most eight corners are exactly \(k=4,6,8\).

## 2. Translation classes and rooting

A translation class of polygons has a unique representative whose smallest
x and y coordinates are both zero. Rotations and reflections are retained
as separate polygons unless their normalized boundaries coincide. Reversing
the traversal or choosing another starting corner does not create a new
polygon.

For \(k=4,6,8\), define the generating function

\[
 F_k(r)=\sum_{\gamma}r^{L(\gamma)/2},\qquad 0<r<1,       \tag{5}
\]

where the sum is over translation classes with \(k\) corners. The perimeter
is even: total eastward and westward lengths agree, as do total northward and
southward lengths.

Write \(H(\gamma)\) and \(V(\gamma)\) for the numbers of horizontal and
vertical unit boundary edges. Precisely \(H(\gamma)\) translates of a polygon
contain the undirected edge underlying \(e\): translate each horizontal unit
edge to that edge. These translates are distinct, since a finite boundary
cannot be invariant under a nonzero translation. Each has exactly one
traversal that follows \(e\) eastward, so there is no additional direction
factor.

Coordinate interchange is a bijection on translation classes, preserves
perimeter, and exchanges \(H\) with \(V\). At perimeter \(2m\), it follows
that

\[
 \sum_{L(\gamma)=2m}H(\gamma)
 =\sum_{L(\gamma)=2m}V(\gamma)
 =m\,\#\{\gamma:L(\gamma)=2m\}.                         \tag{6}
\]

Thus if \(N_k(2m)\) counts polygons with \(k\) corners containing the fixed
edge, their generating function is

\[
 G_k(r)=\sum_m N_k(2m)r^m=rF_k'(r).                    \tag{7}
\]

The formulas below express \(F_k\) as finite sums of products of geometric
series, so they converge for \(0<r<1\) and may be differentiated there.
Combining (4) and (7), with \(r=q^2\), gives

\[
 R_k(p)=(p/2)^kq^{-k}G_k(q^2).                         \tag{8}
\]

## 3. Coordinate compression and gap weights

List the distinct corner x coordinates in increasing order, and replace them
by \(0,1,\ldots,a-1\). Do the same for the y coordinates, using
\(0,1,\ldots,b-1\). Call the resulting polygon its rank polygon. Every coordinate
level of a rank polygon contains a corner. An orthogonal \(k\)-corner polygon
has \(k/2\) vertical sides and \(k/2\) horizontal sides. Each x coordinate is
the coordinate of a vertical side, and each y coordinate is that of a
horizontal side. Hence

\[
 2\leq a,b\leq k/2.                                  \tag{9}
\]

Compression and stretching preserve simplicity. Indeed, strictly increasing
piecewise linear maps of the two coordinate axes extend the change of
coordinates to a homeomorphism of the plane. Conversely, every choice of
positive integer gaps between adjacent rank coordinates stretches a rank
polygon to a unique translation class. The original rank polygon and gaps
are recovered from its corner coordinates, so this parametrization is a
bijection.

For a vertical strip between adjacent x ranks, let \(2c\) be the number of
horizontal sides that cross it. This number is positive and even: each
crossing to the right must be balanced by a crossing to the left. A stretched
gap of width \(s\geq1\) contributes \(2cs\) to horizontal perimeter, hence
\(cs\) to semiperimeter. Define the corresponding weights for horizontal
strips in the same way, from vertical sides. If the combined list of
half-crossing numbers is \(c_1,\ldots,c_j\), its contribution to (5) is

\[
 \prod_{i=1}^j\sum_{s\geq1}r^{c_i s}
 =\prod_{i=1}^j\frac{r^{c_i}}{1-r^{c_i}}.              \tag{10}
\]

For eight corners each strip is crossed by at most four sides, so each
\(c_i\) is either 1 or 2. Put

\[
 t=\frac{r}{1-r},\qquad u=\frac{r^2}{1-r^2}.           \tag{11}
\]

## 4. Complete finite classification for eight corners

By (9), every eight-corner rank polygon fits in a three-by-three box of unit
cells. Its interior is a union of these cells. This gives the following
finite classification. A row word specifies occupied cells from left to
right, and slash-separated rows are listed from bottom to top. Translates
are normalized to have minimum cell coordinates zero. The word \(1^j\) in
the weight column denotes a list of \(j\) ones.

| Cell-box width and height | Half-crossing list | All cell row words | Count |
|---|---|---|---:|
| \(2,3\) | \(1^5\) | `01/11/01`, `01/11/10`, `10/11/01`, `10/11/10` | 4 |
| \(2,3\) | \(1^4,2\) | `11/01/11`, `11/10/11` | 2 |
| \(3,2\) | \(1^5\) | `010/111`, `011/110`, `110/011`, `111/010` | 4 |
| \(3,2\) | \(1^4,2\) | `101/111`, `111/101` | 2 |
| \(3,3\) | \(1^6\) | `001/011/111`, `001/111/011`, `001/111/100`, `010/011/111`, `010/110/111`, `011/010/110`, `011/111/001`, `011/111/110`, `100/110/111`, `100/111/001`, `100/111/110`, `110/010/011`, `110/111/011`, `110/111/100`, `111/011/001`, `111/011/010`, `111/110/010`, `111/110/100` | 18 |
| \(3,3\) | \(1^5,2\) | `001/101/111`, `011/001/111`, `100/101/111`, `110/100/111`, `111/001/011`, `111/100/110`, `111/101/001`, `111/101/100` | 8 |

Here is an exhaustive rule to verify the table, requiring only 511 nonempty
cell sets. It also specifies which degeneracies are excluded.

1. Take each nonempty subset of the nine cells
   \(\{0,1,2\}\times\{0,1,2\}\). Translate its minimum x and y to zero.
2. Start with no boundary edges. For each occupied cell, toggle each of its
   four unit edges: insert an absent edge and remove a present edge. Shared
   edges cancel, leaving precisely the boundary of the cell union.
3. Retain the set only if its boundary graph is connected and every boundary
   vertex has degree two. Such a graph is a single cycle. Since unit grid
   edges can meet only at their endpoints, this cycle is a simple polygon.
   This test rejects disconnected boundaries, holes, and vertex contacts.
4. Delete boundary vertices at which the two successive steps have the same
   direction. Retain exactly eight corners.
5. If the cell-box dimensions are \(w,h\), require the corner x coordinate
   set to equal \(\{0,\ldots,w\}\) and its y coordinate set to equal
   \(\{0,\ldots,h\}\). This is exactly the rank condition.
6. Record the normalized cell set once. For each vertical strip, count its
   horizontal boundary edges and divide by two; use the analogous count for
   each horizontal strip. Sorting these numbers gives the table's list.

Every rank polygon is retained by this rule: its bounded interior supplies
one of the cell sets, and its boundary is simple with all coordinate levels
used. Conversely, every retained set gives a rank polygon. Its cell set is
uniquely determined by its boundary: occupancy changes across a boundary
edge, stays fixed across any other cell edge, and is zero outside the box.
Thus neither extra polygons nor multiple counts enter the table.

For a second finite verification, an eight-corner polygon can be represented
by four horizontal sides, in cyclic order:

\[
 (x_i,y_i)\longrightarrow(x_{i+1},y_i)
 \longrightarrow(x_{i+1},y_{i+1}),\quad i=0,1,2,3,
                                                               \tag{12}
\]

with indices modulo four. Consecutive x coordinates differ, as do consecutive
y coordinates. Each coordinate sequence is surjective onto its rank set.
There are 2 such cyclic sequences on two ranks (the alternating sequences),
12 on three ranks (choose the repeated rank in 3 ways, its opposite pair
of positions in 2 ways, and the other two ranks in 2 orders), and 24 on
four ranks (all permutations). Thus (12) has \(38^2=1444\) candidate pairs.
Expanding their sides into unit edges and rejecting every repeated boundary
vertex retains 304 representations. Each polygon has exactly eight such
representations: four possible starting corners with outgoing horizontal
side in each of the two traversal directions. Canonicalizing by starting
corner and reversal therefore gives \(304/8=38\) polygons. Their individual
corner lists agree with the table's polygons. `eight_corners.py` implements
this verification; `audit_cells.py` independently implements the cell rule.

Applying (10) to the table gives

\[
 F_8(r)=8t^5+4t^4u+18t^6+8t^5u.                       \tag{13}
\]

For comparison, the same rank rule at four corners gives one square with
list \(1,1\); at six corners it gives the four rotations of the L triomino,
each with list \(1,1,1,1\). Exhaustiveness follows alternatively from
\(C-R=4\): no reflex corner forces a rectangle; one reflex corner forces
a rectangle with one corner rectangle removed. A six-corner boundary can
be written, after rotation, with side directions \(E,N,W,N,W,S\); closure
forces lengths \(a+b,c,b,d,a,c+d\), all four parameters positive. Its rank
polygon is exactly one of those four L shapes. Consequently

\[
 F_4(r)=t^2,\qquad F_6(r)=4t^4.                       \tag{14}
\]

## 5. Evaluation of the generating functions

Putting (13) over a common denominator gives

\[
\begin{aligned}
 F_8(r)
 &=\frac{8r^5(1-r)(1+r)+4r^6(1-r)+18r^6(1+r)+8r^7}
          {(1-r)^6(1+r)}\\
 &=\frac{8r^5+22r^6+14r^7}{(1-r)^6(1+r)}\\
 &=\frac{2r^5(4+7r)}{(1-r)^6}.
                                                               \tag{15}
\end{aligned}
\]

The last cancellation uses
\(8+22r+14r^2=(1+r)(8+14r)\). Differentiating gives

\[
\begin{aligned}
 G_8(r)
 &=\frac{(40r^5+84r^6)(1-r)+48r^6+84r^7}{(1-r)^7}\\
 &=\frac{40r^5+92r^6}{(1-r)^7}.
                                                               \tag{16}
\end{aligned}
\]

Since \(1-q^2=p(2-p)=pd\), equation (8) becomes

\[
 R_8(p)=\frac{p^8}{256}q^{-8}
          \frac{4q^{10}(10+23q^2)}{(1-q^2)^7}
       =\frac{p q^2(10+23q^2)}{64d^7},
\]

which proves (1). Similarly, differentiating (14) gives

\[
 G_4(r)=\frac{2r^2}{(1-r)^3},\qquad
 G_6(r)=\frac{16r^4}{(1-r)^5}.
\]

Substitution in (8) yields

\[
 R_4(p)=\frac{p}{8d^3},\qquad R_6(p)=\frac{p q^2}{4d^5}.
\]

The events with four, six, and eight corners are disjoint, so their sum is
the exact probability in (2). For its second expression, the common
numerator divided by \(p\) is

\[
 8d^4+16q^2d^2+q^2(10+23q^2)
 =8+32q+74q^2+64q^3+47q^4,
\]

using \(d=1+q\). At \(p\downarrow0\), \(q\to1\), and this numerator tends
to \(225\), while the denominator tends to \(64\cdot2^7=8192\). This proves
(3). At \(p=1/2\), the three terms are \(1/54,1/243,7/3888\), whose sum
is \(95/3888\).

Every listed eight-corner rank polygon has minimum perimeter at least ten,
and thus at least two straight boundary vertices. Its probability at
\(p=1\) is zero. The only contributing four-corner polygons at \(p=1\)
are the two unit squares through \(e\), each with probability \(1/16\).
This verifies the stated endpoint without the factor \(q^{-k}\) in (8).

## 6. Independent coefficient and limiting checks

For \(j\geq0\), the coefficient of \(r^j\) in \((1-r)^{-7}\) is
\(\binom{j+6}{6}\), by counting weak compositions of \(j\) into seven
parts. Equation (16) therefore implies

\[
 N_8(2m)=40\binom{m+1}{6}+92\binom{m}{6},              \tag{17}
\]

where a binomial coefficient is zero when its upper argument is less than
six. In particular:

| Perimeter | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Eight-corner polygons through \(e\) | 0 | 40 | 372 | 1764 | 5936 | 16128 | 37800 |

A direct unit-step self-avoiding walk enumeration through perimeter twenty
agrees with every entry, and with the four- and six-corner counts, without
using rank polygons. It closes walks only on return to the initial vertex,
includes the turn at that vertex, and keeps the initial eastward edge fixed.

The small-density coefficient can also be recovered directly from (13).
As \(r\uparrow1\), \(t\sim(1-r)^{-1}\) and
\(u\sim[2(1-r)]^{-1}\). Only the six-gap terms contribute at linear order
in \(p\). Their leading coefficient in \(F_8\) is \(18+8/2=22\), and in
\(rF_8'\) it is \(6\cdot22=132\). Thus (8) and
\(1-r\sim2p\) give

\[
 \lim_{p\downarrow0}\frac{R_8(p)}p
 =\frac{132}{256\cdot128}=\frac{33}{8192}.
\]

Adding the earlier coefficient \(3/128=192/8192\) gives \(225/8192\)
again. The five-gap terms have a pole of order at most six after
differentiation, and therefore contribute \(O(p^2)\).

Finally, the scripts evaluate the shape sums by exact rational arithmetic
at \(p=1/10,1/4,1/2,3/4\). Separately, summing (17) with the weights (4)
through \(m=500\), including \(p=1\), agrees with (1) within rigorous tail
bounds smaller than \(10^{-30}\). To bound the tail, the successive ratios
of the two nonnegative terms in (17) are at most
\((m+2)/(m-4)\) and \((m+1)/(m-5)\), respectively. After the first omitted
term \(m=M+1\), both ratios decrease, and the larger bound is
\((M+2)/(M-4)\). Multiplication by \(r\) gives a ratio \(\rho<1\) at
\(M=500\) for every tested density. The first omitted weighted term divided
by \(1-\rho\) therefore bounds the whole tail. Exact bounds and execution
commands are recorded in `cell_audit.json` and `LOG.md`.

These conclusions concern only vertex-simple orbits with at most eight
mirrors. They give no upper bound on the probability of an infinite orbit.
