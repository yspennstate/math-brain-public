# Square certificates from both endpoint neighborhoods

Let F be the free minimal spanning forest on the nearest-neighbor lattice
Z^d, d>=2, with independent uniform [0,1] edge labels. The free and wired
forests agree on this lattice. Write u~_F v if u and v belong to the same
component. All comparisons below are on the probability-one event that
the countably many labels are distinct.

For a finite vertex set Q, form H(Q) by identifying its complement to a
root *, retaining every original edge meeting Q, with its original label.
Discard edges with both endpoints outside Q. Parallel edges remain separate
independent edges. Let T(Q) be the minimum spanning tree of H(Q).

Put e={0,e_1} and m=2d-2. For an elementary square through e, let P be
its three-edge detour from 0 to e_1. Write its vertices in path order as

    v_0=0, v_1=e_2, v_2=e_1+e_2, v_3=e_1.

Coordinate permutations and reflections give all other squares through e.
Let N(x) denote the set of nearest neighbors of x, and define

    Q^- = V(P) union N(0),
    Q^+ = V(P) union N(0) union N(e_1),
    a_d = P(P subset T(Q^-)),
    b_d = P(P subset T(Q^+)).

The probability a_d is the one-end enlargement in the preceding report.
The probability b_d is the new two-end enlargement.

For j=3,5,7 let D_j(d) be the finite set of simple length-j paths from
0 to e_1 avoiding e. Put

    B_7(d) = 1/d + sum_(P in D_3 union D_5 union D_7)
                          P(P subset T(V(P))),

and let a_d^0=P(P subset T(V(P))) for a square detour. The previous bound is

    B_*(d) = B_7(d)+m(a_d-a_d^0).

## Proposition

For every integer d>=2,

    P(0~_F e_1) >= B_**(d) := B_*(d)+m(b_d-a_d) > B_*(d).       (1)

The quantities b_d are rational and have the explicit finite recurrence
in Section 4. Exact evaluations give

    b_2 = 1434277211177/33731641944000,

    b_3 = 106821527499174906671287753163603
            / 8994156750072383564239397632800000.                (2)

Consequently,

    B_**(2) = 84815746280753023/140256167203152000
            = 0.604720262731141741422...,

    B_**(3) = 265115546365736108233965694737821273
                / 674561756255428767317954822460000000
            = 0.393018939937276498777... .                       (3)

These are local lower bounds. They give no conclusion about the number
of components of F.

## 1. Finite cuts and enlargement

The unique minimum-label edge f of a finite lattice cut delta(S) belongs
to F. Every finite simple cycle containing f crosses that cut again, at
an edge with greater label. Thus f is not the maximum edge of any finite
cycle; the cycle definition of the free forest retains it. The same
definition implies that F is acyclic. It has no finite component, since
the minimum boundary edge of such a component would belong to F and leave it.

Suppose f is an edge of T(Q) with both endpoints in Q. Delete f from T(Q)
and let S be the vertex set of the resulting component not containing *.
Every lattice edge of delta(S) is represented with its original label in
H(Q). The edge f minimizes that cut: any lighter crossing edge would
replace f and reduce the tree weight. Hence f belongs to F.

If Q is contained in R, the same cut delta(S) is represented in H(R).
Every finite MST contains the unique minimum of a cut. Indeed, if it did
not, adding that minimum to the tree creates a cycle with another cut
edge of greater label, whose removal lowers the weight. Therefore f is
also in T(R). Applied to each edge of P, this proves

    {P subset T(Q^-)} subset {P subset T(Q^+)}.                  (4)

To see that this inclusion is strict in probability, take

    x=2e_1, f={v_2,v_3}, g={e_1+e_2,2e_1+e_2}.

The vertex x is in Q^+ but not Q^-. The other endpoint of g is outside
Q^+. Give the four edges {v_3,x}, g, {v_0,v_1}, {v_1,v_2} labels in
(0,1/4), give f a label in (1/3,1/2), and give every other edge meeting
Q^+ a label in (3/4,1). These are finitely many independent requirements
on distinct edges, so the event has positive probability.

In H(Q^-), the two edges {v_3,x} and g are root spokes giving a path
from v_3 to v_2 lighter than f. Kruskal therefore rejects f. In H(Q^+),
the edges below 1/2 are exactly the five specified edges. They form a
tree on v_0,v_1,v_2,v_3,x,* and contain P. They are accepted before any
other edge. Thus the event belongs to the right side of (4) but not the
left, proving b_d>a_d in every d>=2.

## 2. Adding the certificates

Each event {P subset T(Q)} with V(P) contained in Q forces P into F by
Section 1. For two distinct simple paths with the same endpoints, their
union contains a cycle: follow their first divergence up to their next
common vertex. Hence two such paths cannot both lie in F. Their certificate
events are disjoint, including paths with different lengths and overlapping
interiors. Each is also disjoint from {e in F}, since adding e to a detour
would form a cycle.

For completeness, P(e in F)=1/d follows by a box count. Let
B_n={-n,...,n}^d, with V_n=(2n+1)^d vertices and
M_n=d(2n)(2n+1)^(d-1) internal lattice edges. Every component of F[B_n]
meets its inner boundary: its infinite F component has a path to outside
B_n, whose initial segment reaches that boundary within the same induced
component. The number K_n of induced components consequently satisfies

    1 <= K_n <= (2n+1)^d-(2n-1)^d.

By lattice symmetries every edge has the same inclusion probability p.
The forest identity |F[B_n]|=V_n-K_n gives

    (2n-1)^d <= p M_n <= (2n+1)^d-1.

Divide by V_n and let n tend to infinity to obtain pd=1.

There are m squares through e, one for each choice of transverse direction
and sign. Replace their m earlier one-end certificate events by the m
events using Q^+. Retain all the length-five and length-seven certificates.
The resulting collection is still pairwise disjoint and implies connection.
It has probability B_*(d)+m(b_d-a_d). This proves (1), including its strict
inequality by Section 1. Certificates for different regions of the same
path have not been added together.

## 3. The complete induced graph

Besides the square, Q^+ contains the two unmatched vertices -e_1 and
2e_1, and the matched pairs

    s, e_1+s,  for s in S={-e_2} union {+e_j,-e_j:3<=j<=d}.

There are L=|S|=2d-3=m-1 matched pairs. Thus |Q^+|=4+2+2L=4d.
Its internal edges consist of the four square edges, the two unmatched
pendant edges, and three edges for every matched pair:

    {0,s}, {s,e_1+s}, {e_1+s,e_1}.

There are no other induced edges. To check this, distinct elements of S
have lattice distance two. Elements of the same side therefore cannot
be adjacent. Between opposite sides the distance from s to e_1+t is
1+||s-t||_1, equal to one exactly when s=t. The unmatched vertices have
distance at least two from every other added vertex. Neither added vertex
can meet v_1 or v_2: those two vertices have only their two square neighbors
in the region, as follows directly from their coordinates. The stated list
accounts for every pair at distance one.

The endpoint vertices v_0,v_3 have no exterior edges. Each of v_1,v_2
has m exterior edges, each unmatched vertex has m+1, and each matched
vertex has m. Therefore

    internal edges = 4+2+3L = 3m+3,
    boundary edges = 2m+2(m+1)+2Lm = 2m^2+2m+2,
    all edges meeting Q^+ = 2m^2+5m+5.                          (5)

As a second count, 2d|Q^+| minus twice the internal-edge count gives
the boundary count: (m+2)(2m+4)-2(3m+3)=2m^2+2m+2.
For d=2 and d=3 there are respectively 23 and 57 original edges.

Apply the increasing transformation U -> -log(1-U), giving independent
rate-one exponential labels without changing any MST. Replace each bundle
of r parallel root edges by its minimum, an exponential of rate r.
This preserves every nonparallel edge's MST status. The resulting finite
weighted graph consists of:

- the four square edges, each of rate one;
- two edges v_1*,v_2*, each of rate m;
- two unmatched branches, each with an endpoint-to-leaf edge of rate one
  and a leaf-to-root edge of rate m+1;
- L matched branches, each with edges v_0x,xy,yv_3 of rate one and
  edges x*,y* of rate m.

All these exponential labels are independent. In particular, the edge xy
has not been dropped or treated as an independent endpoint spoke.

## 4. A finite exact recurrence

Let E be the weighted edge list in Section 3 and P={01,12,23}. A state
pi is a partition of its 4d+1 vertices reached by accepted edges. Let
C(pi) be the set of blocks containing one or more square vertices, and put

    D(pi) = sum_(h=ab in E; pi_a != pi_b) rate(h).

A crossing edge h=ab is allowed if h belongs to P, or if its two blocks
are not both in C(pi). Define recursively

    h(pi)=1, if the four square vertices have a common block;

    h(pi)= [sum_(crossing allowed ab) rate(ab) h(pi joined at a,b)]
               / D(pi), otherwise.                             (6)

Then b_d=h(pi_0), where pi_0 is the partition into singletons. Every join
reduces the number of blocks, so this is an explicit finite rational
recurrence for every integer d>=2. Denominators are positive because the
weighted graph is connected and a nonsuccessful state has multiple blocks.

Here is why (6) calculates the desired event. Conditional on the elapsed
time in Kruskal's algorithm, unexamined crossing exponential clocks have
independent residual exponential labels of their original rates. The next
crossing edge is therefore chosen with probability its rate divided by
D(pi). Edges already internal to a block can be ignored permanently.

A non-path edge joining two blocks containing square vertices makes success
impossible. The accepted forest already connects each of its endpoints to
a square vertex, without any other square-containing block being merged.
Together with the eventual full path P this new connection would create
a cycle. Conversely, before such a forbidden merge every connection between
square vertices uses only already accepted edges of P; branches may attach
to a single square-containing block. This invariant follows by induction
over allowed joins. It shows both that an unaccepted desired edge cannot
already have its endpoints connected, and that reaching one square block
means all three desired edges have been accepted. Other allowed joins do
not by themselves preclude success; their later outcomes are accounted for
recursively. A forbidden transition contributes zero, an already successful
state contributes one, and conditioning gives (6).

The script both_ends.py implements this recurrence on the entire graph.
It uses 1,958 states for d=2 and 236,132 for d=3. No branch symmetry or
independent effective endpoint labels are assumed in that computation.

## 5. Independent final-tree integration

Contract the three desired path edges to one vertex C, retaining the root R.
Each unmatched leaf then has edges to C and R. Its restriction in a final
spanning tree either contains one of these edges (two nonbridging choices)
or both (one bridging choice).

A matched pair becomes a four-vertex graph on C,R,x,y with five edges
Cx,xy,yC,xR,yR. In a final tree its restriction must be a forest with
every component containing C or R: otherwise an internal vertex cannot
connect to the rest of the graph. If it separates C from R it has two
edges. There are exactly eight choices: four attach x and y separately
to terminals, and four use xy and one of the four terminal edges. If it
connects C to R it is a three-edge spanning tree. Of the ten three-edge
subsets, two are triangles isolating the other terminal; the remaining
eight are trees.

There must be exactly one bridge from C to R. There are three possibilities:
one of the two direct core-root edges; one unmatched leaf; or one matched
pair. All other branches must be nonbridging. This list is exhaustive:
no bridge disconnects C and R, while two distinct bridges form a cycle.
The number of final tree shapes is consequently

    2*2^2*8^L + 2*2*8^L + L*8*2^2*8^(L-1)
      = (12+4L)8^L = (4m+8)8^(m-1).                            (7)

This gives 128 shapes for d=2 and 12,288 for d=3. Root-edge multiplicities
are encoded by exponential rates, not by multiplying this shape count.

Fix one such tree T. For each non-tree edge h let L_h be its unique route
in T. The cycle criterion says that T is the MST exactly when

    X_h > max_(f in L_h) X_f for every h outside T.               (8)

Necessity follows by an edge exchange on the cycle made by h. For
sufficiency, every competitor crossing a tree edge f's fundamental cut has
a tree route containing f; (8) makes f the unique minimum of that cut.
Every tree edge then belongs to the MST.

On a simplex ordering the |T| independent exponential tree labels, let S
range over the successive nonempty suffixes of that ordering. Conditioning
on the tree labels gives the product of their exponential densities and
the survival probabilities in (8). Express the ordered labels as sums of
their successive nonnegative gaps. A gap associated to S appears in the
label of a tree edge exactly when that edge is in S, and in a route maximum
exactly when L_h meets S. Integrating each gap gives

    (product_(f in T) rate(f)) /
       product_(suffixes S) [sum_(f in S) rate(f)
                              + sum_(h outside T; L_h meets S) rate(h)]. (9)

Sum this over every tree-label ordering and every final tree shape.
This is an independent calculation using routes and density integrals,
without the allowed-partition recurrence (6).

The audit enumerates the eight local rooted forests and eight local trees
by testing all two-edge and three-edge subsets. Identical matched branches
can be permuted, and reflection interchanges the endpoints together with
the two middle square vertices. These graph automorphisms preserve rates
and integrals. Grouping by these symmetries gives 64 integrals in d=2 and
1,296 in d=3, with integer multiplicities summing to the counts in (7).
Each retained representative is separately checked to be a spanning tree.
The sum over its ordering simplices is evaluated by a suffix-subset
recurrence; a subset zeta transform sums route constraints. The exact
results agree with (2).

## 6. Arithmetic and scope

The preceding d=3 square probability and bound are

    a_3 = 7175020914436910477/722017042450235532000,

    B_*(3) = 237831533319331629226140743
               / 617324571294951379860000000.

Substitution of (2) into (1) gives

    4(b_3-a_3)
      = 191866255331224667993946415505833
           / 24733931062699054801658343490200000
      = 0.007757208300001121523... .                            (10)

Adding (10) to B_*(3) gives (3). In d=2 the corresponding gain is

    2(b_2-a_2) = 4129009763/344200428000
               = 0.011995946045133912500... .                   (11)

The audit repeats these additions using integer least common multiples
and greatest common divisors, independently of the main Fraction sums.
It also rebuilds every induced edge and boundary multiplicity by lattice
neighbor lookup, independently of the main pair-distance construction.

The recheck.py calculation independently reproduces all 202 earlier
square, six-vertex and eight-vertex path probabilities and their bound
sums for d=2,...,12. It additionally integrates every final tree of the
one-end enlarged graph for each partial enlargement in d=2,3. This
recovers all eight corresponding probabilities, including a_2 and a_3.
Earlier implementations are not imported or executed.

The component question on full Z^d remains unresolved by these calculations.
Neither (1) nor its finite recurrence supplies a long-distance estimate.
Novelty of the local bound relative to published work has not been established.

Reference for the free/wired setting and cycle definition: Russell Lyons,
Yuval Peres and Oded Schramm, *Minimal spanning forests*, Annals of
Probability 34 (2006), 1665–1692,
[arXiv:math/0412263](https://arxiv.org/abs/math/0412263).
