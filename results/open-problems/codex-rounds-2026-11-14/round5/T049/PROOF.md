# Enlarging the wired region around a square

Let F be the free minimal spanning forest of the nearest-neighbor lattice
Z^d, d>=2, with independent uniform edge labels. The free and wired forests
agree on this lattice. Work on the event of distinct labels, which has
probability one. Put e={0,e_1} and m=2d-2.

For a finite vertex set Q, let H(Q) be the finite multigraph obtained by
identifying its complement to a vertex *. Retain separately all original
edges with at least one endpoint in Q, and discard edges with both endpoints
outside Q. Let T(Q) denote its minimum spanning tree, using the original
labels. For a finite simple lattice path P, write V(P) for its vertices and

    a(P,d) = P(P is contained in T(V(P))).

Let D_j(d) be the finite set of simple paths of length j from 0 to e_1
that avoid e. Define

    B_7(d) = 1/d + sum_(P in D_3(d) union D_5(d) union D_7(d)) a(P,d).  (1)

This is the bound evaluated in the preceding report. Its numerical value
in dimension three is

    B_7(3) = 21272798694838039662654613
             / 56120415572268307260000000.                         (2)

The definitions in (1), rather than a graph classification, suffice to
specify B_7 in every dimension.

## 1. The enlarged region and the result

An elementary square through e has a three-edge detour P, whose vertices
are numbered 0,1,2,3 along P. The lattice origin is vertex 0, and e_1 is
vertex 3. Its internal edges are

    01,12,23,03.

Choose any k of the m neighbors of vertex 0 outside the square and add
them to its vertex set. Call the resulting region Q_k, choosing the added
vertices in a nested order as k increases. Its internal graph is the square
with k pendant vertices at 0. There are no other induced edges. In H(Q_k),
vertex 0 has m-k edges to *, the other three square vertices each have m,
and every added vertex has m+1 edges to *. This describes its law without
reference to which k neighbors were chosen. Put

    a_(m,k) = P(01,12,23 are all in T(Q_k)),  0<=k<=m.

In particular a_(m,0) is the earlier square probability. The result is

    P(0 and e_1 are in the same F component)
        >= B_*(d) := B_7(d)+m[a_(m,m)-a_(m,0)] > B_7(d).           (3)

Here is an exact finite formula for the new probabilities. Let q_m(s) be
the probability that an MST contains 01,12,23 in the graph on 0,1,2,3,*
whose square-edge labels are independent rate-one exponentials and whose
four root-edge labels are independent exponentials of rates s,m,m,m.
All eight labels are independent. Then

    a_(m,k) = sum_(b,c>=0; b+c<=k)
                 (-1)^c binomial(k,b) binomial(k-b,c)
                 q_m(m+mb+(m+1)c).                              (4)

Section 4 gives a 96-term rational formula for q_m(s). Thus (3)-(4)
specify a strict improvement for every integer d>=2, not just the
dimensions computed below.

For d=3 the exact enlarged square probability and gain are

    a_(4,4) = 7175020914436910477/722017042450235532000,

    4[a_(4,4)-a_(4,0)]
        = 1120101659682220157/180504260612558883000
        = 0.006205402885677299232... .                            (5)

Consequently

    B_*(3) = 237831533319331629226140743
              / 617324571294951379860000000
            = 0.385261731637275377254... .                        (6)

The other first two dimensions give

| d | a_(m,m) | B_*(d) |
|---|---|---|
| 2 | 31323563/857656800 | 0.592724316686007828922... |
| 4 | 49379135333103832888884678763/12338499338299390985163843408000 | 0.280202821595373250359... |

Exact fractions for all d=2,...,12 are in extension.json. These are local
connection bounds and imply no conclusion about the number of components.

## 2. Finite cuts, monotonicity and disjoint paths

The unique minimum-label edge f of a finite lattice cut delta(S) belongs
to F. Indeed, every finite simple cycle containing f crosses this cut
again, at an edge with larger label. Thus f is not the maximum edge of any
finite cycle, so the cycle definition of F retains it.

If f is internal to Q and belongs to T(Q), remove f from this tree and let
S be the vertex set of the component not containing *. Then S is a subset
of Q, and f is the unique minimum edge of delta(S). A lighter edge of that
cut could replace f in T(Q), contradicting minimality. The finite graph
represents every lattice edge of delta(S) with its original label. The
preceding paragraph therefore gives f in F.

There is also a useful monotonicity statement. If Q is a subset of R and
f is an internal edge of T(Q), take the same S. The cut delta(S) is also
represented exactly in H(R), and f is still its unique minimum. Every
finite MST contains the unique minimum of any cut: otherwise adding that
edge creates a cycle with another, heavier cut edge, whose removal reduces
the tree weight. Therefore f belongs to T(R). In particular, under the
coupling using the original lattice labels,

    {P subset T(Q_(k-1))} is a subset of {P subset T(Q_k)}.         (7)

Every square event in (3) forces its three-edge detour into F. Likewise,
each event defining a(P,d) forces P into F. Distinct simple paths between
the same two endpoints cannot both lie in a forest. To verify this when
they overlap, follow their first divergence until the next common vertex;
the different subpaths form a cycle. These events are consequently
pairwise disjoint across all paths in D_3, D_5 and D_7, after the square
events are replaced by their enlargements. Each is also disjoint from
{e in F}, since P together with e contains a cycle. Their probabilities
may therefore be added. No independence is required.

For completeness, P(e in F)=1/d follows from a finite-box count. F has no
finite component, since the minimum edge of the boundary of such a
component would belong to F and leave it. Let B_n={-n,...,n}^d, with
V_n=(2n+1)^d vertices and M_n=d(2n)(2n+1)^(d-1) internal lattice edges.
If K_n is the number of components of F[B_n], every such component meets
the inner vertex boundary of B_n: its infinite F component has a path
leaving the box. Hence

    1 <= K_n <= (2n+1)^d-(2n-1)^d.

By translation and coordinate symmetries the inclusion probability p is
the same for all lattice edges. The identity |F[B_n]|=V_n-K_n gives

    (2n-1)^d <= p M_n <= (2n+1)^d-1.

Divide by V_n and let n increase to infinity to obtain pd=1. There are
exactly m=2(d-1) squares through e, by choosing a transverse axis and a
sign. Replacing all m earlier square terms in (1) proves the first
inequality in (3).

## 3. Geometry and strict improvement

To verify the graph description of Q_k, take the square vertices to be
0, e_j, e_1+e_j, e_1, with j different from 1 and either transverse sign.
All added vertices are neighbors of 0 and have odd parity. Thus no two
are adjacent, and none is adjacent to e_j or e_1, which also have odd
parity. An added vertex cannot be adjacent to e_1+e_j: the only common
neighbors of 0 and e_1+e_j are e_1 and e_j, already in the square.
Its only neighbor inside Q_k is therefore 0. The claimed internal degrees
and external spoke counts follow. In particular Q_m has 2d+2 vertices
and m^2+5m+4 incident edges.

Inclusion in (7) is strict in probability for each k>=1. Let x be the
newly added vertex, f=01 the first desired path edge, and g any one
exterior edge at square vertex 1 in H(Q_k). Such an edge exists because
its exterior degree is m>=2. Consider the following finite event in the
original uniform labels:

    edges 0x, g, 12 and 23 have labels in (0,1/4);
    edge f has label in (1/3,1/2);
    every other edge meeting Q_k has label in (3/4,1).

All listed edges are distinct; independence gives this event positive
probability. In H(Q_(k-1)), the edges 0x and g are spokes to the same
wired root. They give a path from 0 to 1 lighter than f, so f is excluded
from its MST. In H(Q_k), all edges of label below 1/2 are exactly
0x,g,01,12,23. These form a tree on the square, x and the root. They
contain no cycle and are accepted by Kruskal before any other edge.
Thus the enlarged MST contains the whole desired path. This proves

    a_(m,0) < a_(m,1) < ... < a_(m,m),                             (8)

and proves the strict inequality in (3).

## 4. Reduction to a weighted square and the finite formula

Replace every original uniform label U by -log(1-U). This preserves all
orders and MSTs and produces independent rate-one exponentials.
Parallel edges can be replaced by their minimum for determining the MST
status of any square edge. The minimum of r independent rate-one
exponentials has exponential rate r.

For a pendant vertex x, let X be the label on 0x and let Y be the minimum
of its m+1 exterior labels. Thus X has rate 1 and Y has rate m+1,
independently. The route from 0 to the root through x is present below
a threshold t exactly when X<t and Y<t. Its effective label is Z=max(X,Y).
For t>=0,

    P(Z>t) = e^(-t)+e^(-(m+1)t)-e^(-(m+2)t).                     (9)

These replacements preserve square-edge MST membership: an edge belongs
to a finite MST exactly when its endpoints are not joined by a path of
strictly lighter edges. Parallel minima and the series maximum preserve
all threshold connections between the square vertices and the root.

After eliminating the k pendant vertices, the effective root label W_0
at 0 is the minimum of m-k independent rate-one spokes and k independent
copies of Z. The other three effective root labels have rate m. These
four labels and the four square labels are independent, since they use
disjoint original edges. Therefore

    P(W_0>t)
      = e^(-(m-k)t) [e^(-t)+e^(-(m+1)t)-e^(-(m+2)t)]^k
      = sum_(b,c>=0; b+c<=k)
          (-1)^c binomial(k,b) binomial(k-b,c)
          e^(-(m+mb+(m+1)c)t).                                 (10)

The index b counts choices of the second term in the bracket, c choices
of the third, and k-b-c choices of the first. Expanding their total
exponent gives m+mb+(m+1)c. Differentiating the finite sum shows that the
density of W_0 is the same signed linear combination of exponential
densities. Condition on all other effective labels and integrate against
this density. Linearity gives (4). The coefficients in (4) can be
negative; it is an exact finite identity, not a mixture assertion.

Here is the promised rational definition of q_m(s). Put R=(s,m,m,m).
For r in {0,1,2,3}, let T_r consist of 01,12,23 and the edge r*. A spanning
tree containing the three desired edges is exactly one of these four.
For any proper subset S of T_r let pi(S) be its component partition and
put

    D_r(S) = sum_(ab in {01,12,23,03}) 1{pi_a(S) != pi_b(S)}
              + sum_(v=0)^3 R_v 1{pi_v(S) != pi_*(S)}.

For an ordering sigma of the four edges of T_r, let S_j(sigma) be its
first j edges. Then

    q_m(s) = sum_(r=0)^3 R_r sum_(sigma in permutations(T_r))
                product_(j=0)^3 1/D_r(S_j(sigma)).               (11)

There are 4*4!=96 summands. To prove (11), run Kruskal with independent
exponential labels of the indicated rates. At a component partition,
the next accepted crossing edge is chosen with probability equal to its
rate divided by the sum of all crossing-edge rates. This follows from
the exponential race and its memoryless property; internal edges can be
discarded. For a particular order of T_r, the product of the four chosen
rates is R_r, since each desired path edge has rate one. The denominators
are precisely D_r(S_j). The accepted-edge orders and final trees are
disjoint outcomes, which proves (11). It also proves that (4) is rational
at every integer m>=2 and k<=m.

For example, k=1 gives the simple check

    a_(m,1) = q_m(m)+q_m(2m)-q_m(2m+1),

and k=0 gives a_(m,0)=q_m(m).

## 5. Independent calculations and numerical audit

The script recheck.py evaluates the earlier probabilities through the
finite-MST cycle inequalities. Fix a tree T containing a desired path,
and let L_h be the tree route of a non-tree edge h. T is the MST exactly
when every non-tree label is larger than every label on its route L_h.
Necessity follows by exchanging edges on a cycle. For sufficiency, each
tree edge is then the minimum of its fundamental cut and belongs to the
MST. For uniform labels, conditional independence gives a product of
1-max_(f in L_h) U(f). On an ordering simplex of the tree labels, integrate
these monomials. If S is a suffix of the ordering, its factor is

    1/[|S| + number of non-tree edges whose tree route meets S].

The denominator follows by substituting y=1-U and integrating the ordered
variables from the innermost one outward. Summing over the last removed
edge of each suffix evaluates all ordering simplices by a subset
recurrence. This checks all 202 earlier probabilities and all earlier
bounds. Coordinate enumeration also checks every seven-edge graph
multiplicity in dimensions 2 through 5. For higher dimensions each closed
eight-step walk uses at most four coordinate axes, one being axis 1;
choosing its transverse support extends these counts by binomial factors.

The script enlarge.py evaluates (4) and (11). A separate recursion avoids
effective labels entirely. Its state consists of a square/root partition
and three leaf counts: u unattached, a attached to 0, b attached to the
root. While 0 and the root are separate, these leaves contribute crossing
rate u(m+2)+a(m+1)+b. An unattached leaf next attaches to 0 at total rate u
or to the root at total rate u(m+1). The ordinary root rates are
(m-k,m,m,m). Every crossing square edge is counted in the denominator,
but only desired path edges may be accepted. Root connections between
two square-containing blocks cannot be accepted on a successful outcome,
as they would create a cycle with the eventual full path. Once 0 and
the root coincide, the leaf edges cannot change square connections and
can be discarded. Once the four square vertices coincide, success is
certain. The weighted sum of allowed transitions, divided by all crossing
rates, is the recursion. It agrees with (4) for all 143 pairs (d,k)
computed in d=2,...,12.

The audit.py script also recurses on the full graph partitions, without
grouping leaves, for every k in dimensions 2 and 3. A further check
enumerates the full graph's final trees containing the desired path.
After contracting the path, such a tree either has one direct connection
to the root and every leaf attached to one side, or one bridging leaf
and every other leaf attached to one side. There can be no other type:
two bridges create a cycle, and zero bridges disconnect the root. For
k=m this gives 3*2^m+m*2^(m-1) tree shapes, namely 16 for d=2 and 80
for d=3.

Parallel root edges may be collapsed to their independent exponential
minima in this check. For a fixed resulting tree T with edge rates r_f,
direct integration over an ordering of its exponential labels gives

    product_(f in T) r_f
      / product_(suffixes S)
          [sum_(f in S) r_f + sum_(h not in T; L_h meets S) r_h].   (12)

To derive (12), set each ordered tree label equal to the sum of its
successive nonnegative gaps. A gap is present in a tree label exactly
when that edge lies in the corresponding suffix. It is present in a
non-tree route maximum exactly when the route meets that suffix.
Integrating each gap over [0,infinity) gives its reciprocal coefficient.
The density contributes the numerator product of tree rates. The audit
explicitly enumerates all orderings, giving 11,520 integrals for d=2 and
3,225,600 for d=3. Both exact sums agree with (4).

Finally, integer LCM/GCD additions verify every gain and final bound
independently of the Fraction summations. In (5), the earlier value is
a_(4,0)=5521/658350; inserting it and the displayed a_(4,4) gives the
gain in (5). Adding that gain to (2) gives (6). All comparisons are exact;
no sampling or finite-box extrapolation is used.

## Reference and scope

Russell Lyons, Yuval Peres and Oded Schramm, *Minimal spanning forests*,
Annals of Probability 34 (2006), 1665–1692,
[arXiv:math/0412263](https://arxiv.org/abs/math/0412263),
[full paper](https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf), supplies the
cycle definition and free/wired setting. The formulas above concern finite
wired certificates. They give neither a long-distance connection estimate
nor a transition dimension. Novelty relative to published local bounds
has not been established.
