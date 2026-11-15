# Certificates from all three-edge and five-edge detours

Let F be the free minimal spanning forest of the nearest-neighbor lattice
Z^d, with independent uniform [0,1] edge labels. Write u~v when u and v
belong to the same component of F. The free and wired forests agree on this
lattice. All comparisons below take place on the probability-one event that
all edge labels are distinct.

Fix e={0,e_1}. The result is the following local bound, for every d>=2:

    P(0~e_1) >= 1/d + 2(d-1)a(d)
                     + 4(d-1)(d-2)b_C(d)
                     + 2(d-1)(2d-3)b_A(d)
                     + 4(d-1)(2d-3)b_B(d).                         (1)

The finite probabilities a(d), b_C(d), b_A(d), b_B(d) are defined below by
an explicit finite sum. The last three terms are strictly positive in total
for every d>=2. In d=3, (1) reads

    P(0~e_1) >= 347146143557/922150845000
               = 0.376452665460605... .                           (2)

This is a lower bound on a nearest-neighbor connection probability, with no
conclusion about the number of components of F.

## 1. The finite certificate

For a finite nonempty vertex set S, let delta(S) be its lattice edge
boundary. Its unique least-labeled edge f belongs to F. Indeed, every
finite simple cycle containing f crosses delta(S) at another edge. That
edge has larger label than f. Thus f is never the largest edge of a finite
cycle, and is retained in the free minimal spanning forest.

It follows that F has no finite component: the minimum boundary edge of
the vertex set of such a component would leave it and belong to F.
Also F is acyclic, since the greatest edge of every finite cycle is removed.

For a finite set Q, form H(Q) by identifying the complement of Q to one
vertex *, retaining separately every lattice edge with at least one endpoint
in Q. Edges with both endpoints outside Q are discarded. Let T(Q) be its
finite MST. If f is an edge of T(Q) with both endpoints in Q, remove f from
T(Q) and let S be the component not containing *. Then S is a finite
subset of Q. Every edge of delta(S) is represented in H(Q), with its
original label. The edge f is the minimum of this cut, since a lighter
crossing edge could replace f and lower the weight of T(Q). The preceding
paragraph gives f in F.

For a simple path P from 0 to e_1 avoiding e, let Q be its vertex set and
let A_P be the event that T(Q) contains all edges of P. Then

    A_P implies P is contained in F.                              (3)

In particular A_P implies 0~e_1 and e not in F, since P together with e
is a finite cycle.

Two distinct simple paths with the same endpoints cannot both lie in a
forest. To check this even when their interiors overlap, follow the paths
from their first divergence to their next common vertex; the two different
subpaths contain a cycle. Consequently the events A_P are pairwise
disjoint, including paths of different lengths. They are also disjoint from
{e in F}. No independence assertion is needed.

## 2. The direct-edge contribution

By lattice symmetries, p=P(f in F) is independent of the choice of lattice
edge f. Put B_n={-n,...,n}^d. It has V_n=(2n+1)^d vertices and
M_n=d(2n)(2n+1)^(d-1) internal edges. Each component of F[B_n] meets the
inner boundary of B_n: its infinite F component has a path to outside B_n,
whose initial part reaches that boundary. Thus, if K_n is the number of
components of F[B_n],

    1 <= K_n <= (2n+1)^d-(2n-1)^d.

A finite forest has V_n-K_n edges. Taking expectations gives

    (2n-1)^d <= p M_n <= (2n+1)^d-1.

Division by (2n+1)^d and passage to the limit give p d=1. Hence
P(e in F)=1/d.

## 3. The finite graphs and their probabilities

For n=4 or 6, number the path vertices 0,...,n-1, in order along the path.
Let I be the complete set of lattice edges induced by these vertices,
expressed in this numbering. In the associated graph H(I,d), retain I and
add m_v=2d-deg_I(v) separate edges between each vertex v and *. These are
independent edges even when two of the original exterior endpoints agree.
Let q(I,d) be the probability that its MST contains the n-1 path edges.

For n=4, put

    I_4 = {01,12,23,03},             a(d) = q(I_4,d).

Thus a(d) is exactly a_(2d-2) in the earlier report's notation.

For n=6, put

    I_C = {01,12,23,34,45,05},
    I_A = I_C union {14},
    I_B = I_C union {03},
    b_X(d) = q(I_X,d), X in {C,A,B}.

The edge 05 is the excluded direct lattice edge. Type C has m_v=2d-2
for every v. In A the vertices 1,4 have m_v=2d-3; in B the vertices 0,3
have m_v=2d-3. The other four vertices have m_v=2d-2. These multiplicities
are positive for every d>=2.

Here is a finite sum defining all these probabilities. Put

    T_r = {01,12,...,(n-2)(n-1)} union {r*},

where r* is one specified spoke at r. For a subset S of the n edges of
T_r, let pi(S) be the partition of {0,...,n-1,*} into components of S, and
write pi_v(S) for the block containing v. Define

    D(S) = sum_{ab in I} 1{pi_a(S) != pi_b(S)}
             + sum_{v=0}^{n-1} m_v 1{pi_v(S) != pi_*(S)}.

For a permutation sigma of the n edges of T_r, let S_k(sigma) contain its
first k edges, with S_0 empty. Then

    q(I,d) = sum_{r=0}^{n-1} m_r
               sum_{sigma in S_n} product_{k=0}^{n-1} 1/D(S_k(sigma)). (4)

To prove (4), replace every uniform label U by -log(1-U). This preserves
their order and gives independent rate-one exponentials. At any stage of
Kruskal's algorithm, every edge joining different current components has
not yet been examined. Conditional on the past, their residual waiting
times are independent rate-one exponentials. Thus any specified crossing
edge is next accepted with probability 1/D(S). Edges internal to a component
can be skipped, because they can never be accepted later. Multiplying these
conditional probabilities gives the product in (4).

A spanning tree containing all n-1 path edges has exactly one spoke and no
other internal edge: the path already connects all n non-root vertices.
There are m_r choices of that spoke at r. Sum over these choices, over r,
and over every possible accepted-edge order. These outcomes are disjoint,
which proves (4). For n=6 the sum has 6*6!=4320 products, before grouping.

For an independent expression, fix T_r and its n labels x_f. The tree T_r
is the MST exactly when, for every non-tree edge h,

    U(h) > max{x_f : f is on the T_r path joining the endpoints of h}. (5)

Necessity follows by replacing the largest tree edge on the cycle made by
h. For sufficiency, every edge crossing a fundamental cut of a tree edge f
has a tree path containing f, so (5) makes f the unique minimum of its cut.
Each tree edge therefore belongs to the MST.

On a simplex x_(0)<...<x_(n-1), let h_i count the non-tree edges whose
tree-path maximum is x_(i), including all parallel-edge multiplicities.
Conditional independence makes the probability of (5) equal to
product_i (1-x_(i))^h_i. Its integral over that simplex is

    product_{j=0}^{n-1} 1/[n-j + sum_{i=j}^{n-1} h_i].               (6)

For completeness, substitute y_i=1-x_(i). The integration region is
1>y_0>...>y_(n-1)>0. Integrating the last variable contributes
1/(h_(n-1)+1) and increases the preceding exponent by h_(n-1)+1.
Repeating this operation gives each successive denominator in (6).
Sum (6) over all n! orders and all r and multiply each r contribution by
m_r. This gives q(I,d) without using the Kruskal transition calculation.

## 4. Counting the paths

There are 2(d-1) three-edge paths: choose one perpendicular coordinate
axis and one of its two signs. Each path together with e is an elementary
square. Its vertex set induces I_4.

A five-edge simple path together with e is a simple six-cycle. A closed
six-step lattice walk uses each axis equally often in its positive and
negative directions. It cannot be simple if it uses only one axis. If it
uses two axes, their total step counts must be 4 and 2; if it uses three,
their step counts must be 2,2,2. There are no other possibilities.

In the two-axis case, take the axis with two steps as the transverse axis.
There is one step in each transverse direction. Between them, the path
on each of the two parallel lines must be monotone; otherwise it revisits
a vertex. Closure forces these two line segments to have the same length.
Their total length is four, so both have length two. The cycle is therefore
the boundary of a 2-by-1 rectangle.

For each of the d-1 planes containing e, there are six such rectangles
containing e: four where e is one segment of a long side, and two where e
is a short side. The induced graph contains the central rung of the
rectangle. In the short-side case, both endpoints of e have induced degree
two; numbering the path from one endpoint to the other gives type A. In the
long-side case, one endpoint of e has induced degree three and the other
degree two; the result is type B, up to path reversal. Thus the planar
contributions are 2(d-1) of type A and 4(d-1) of type B.

In the three-axis case, each used axis has one positive and one negative
step. All vertices lie in one unit three-cube. A six-cycle uses six of its
eight vertices. It must have three vertices from each bipartition class, so
the omitted pair has opposite parity. Such a pair is either adjacent or
antipodal in the cube.

There are four antipodal pairs. Removing one leaves a connected induced
six-cycle with no chord. Thus there are four type C cycles per cube.
There are twelve adjacent pairs. Removing one leaves two squares sharing
an edge, with four degree-two vertices and two degree-three vertices. The
unique six-cycle is the outside boundary; the shared edge is its chord.
There are therefore twelve chorded six-cycles per cube. Two of the six
cycle edges join two degree-two vertices (type A when distinguished as e),
and four join a degree-two vertex to a degree-three vertex (type B).

Cube symmetries act transitively on its twelve edges. Counting incidences
of cycles and distinguished edges gives, through any fixed cube edge,

    type C: 4*6/12 = 2,
    type A: 12*2/12 = 2,
    type B: 12*4/12 = 4.

The number of unit three-cubes in Z^d containing e is
4*binomial(d-1,2): choose two perpendicular axes and independently choose
their signs. Each nonplanar cycle lies in exactly one such cube. Combining
these counts with the planar rectangles gives

    N_C(d) = 4(d-1)(d-2),
    N_A(d) = 2(d-1) + 4(d-1)(d-2) = 2(d-1)(2d-3),
    N_B(d) = 4(d-1) + 8(d-1)(d-2) = 4(d-1)(2d-3).

Removing e from a cycle gives exactly one path oriented from 0 to e_1.
There is no further factor of two. The total number of five-edge paths is
(d-1)(16d-26). For d=3 the counts are N_C=8, N_A=12, N_B=24.

## 5. Addition and exact evaluation

Apply (3) to every three-edge and five-edge path. Section 1 shows that their
events are disjoint and all imply connectivity without e. Section 2 supplies
the disjoint direct-edge event. Section 4 counts the paths, and Section 3
identifies their finite probabilities. Adding them proves (1).

In d=3, finite sum (4), equivalently (6), gives

    a(3)   = 5521/658350,
    b_C(3) = 187806637/902104087500,
    b_A(3) = 44663374963/205507902600000,
    b_B(3) = 14856501533/67257131760000.

Consequently the new contribution is

    8 b_C(3) + 12 b_A(3) + 24 b_B(3)
       = 8829469757/922150845000,

and the whole bound is

    120767/329175 + 8829469757/922150845000
       = 347146143557/922150845000,

as claimed in (2). Every finite probability is positive: the event that the
path edges precede every other edge of H(I,d) has positive probability and
forces the path into the MST. In particular N_A(d), N_B(d)>0 for d>=2,
so (1) strictly improves the earlier three-edge bound.

The finite rational sums and all path counts for d=2,...,12 are evaluated
in `verify_paths.py`; `extension.json` records the exact values. The file
`audit.py` checks them with a third direct partition recursion, verifies all
1128 pairs among the 48 short d=3 paths contain a cycle in their union,
and re-derives the displayed rational addition using integer least common
multiples. These calculations involve no sampling or volume limit.

## Reference

Russell Lyons, Yuval Peres and Oded Schramm, *Minimal spanning forests*,
Annals of Probability 34 (2006), 1665–1692,
[arXiv:math/0412263](https://arxiv.org/abs/math/0412263),
[full paper](https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf), gives the cycle
definition and the free/wired setting used here.
