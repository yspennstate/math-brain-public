# A nearest-neighbor bound from every seven-edge detour

Let F be the free minimal spanning forest on the nearest-neighbor lattice
Z^d with independent uniform [0,1] edge weights. On this lattice the free
and wired forests agree. Write 0~e_1 when these vertices are in the same
component, and put e={0,e_1}. All comparisons are on the probability-one
event that the countably many edge weights are distinct.

The result below adds all seven-edge detours to the three-edge and
five-edge bound of the preceding report. The graph multiplicities in the
result are finite enumeration results, verified by two exhaustive algorithms.
The probability evaluations use exact rational arithmetic.

## 1. Statement and finite graphs

For n>=2 and an internal edge set I on {0,...,n-1} containing the path

    P_n = {01,12,...,(n-2)(n-1)},

form H(I,d) by adding a vertex * and m_v=2d-deg_I(v) separate edges v* at
each vertex v. Only cases with m_v>=0 and connected H(I,d) are used. Define

    q_n(I,d) = P(P_n is contained in the MST of H(I,d)).

Edges with a common pair of endpoints are still distinct independent edges.
A zero spoke multiplicity is allowed.

Define the previously used graphs

    C_4 = P_4 union {03},
    C_6 = P_6 union {05},
    A_6 = C_6 union {14},
    B_6 = C_6 union {03}.

The preceding bound is

    B_5(d) = 1/d + 2(d-1) q_4(C_4,d)
                 + 4(d-1)(d-2) q_6(C_6,d)
                 + 2(d-1)(2d-3) q_6(A_6,d)
                 + 4(d-1)(2d-3) q_6(B_6,d).                    (1)

For the new graphs start with C_8=P_8 union {07}. The table specifies
additional edges J_i and coefficients c_(i,1), c_(i,2), c_(i,3). In the
edge notation 03, for example, the endpoints are path positions 0 and 3,
not coordinate directions. Put I_i=C_8 union J_i.

| i | J_i | c_(i,1) | c_(i,2) | c_(i,3) |
|---|---|---:|---:|---:|
| G01 | 03,05 | 4 | 48 | 96 |
| G02 | 03,16,25,47 | 0 | 8 | 0 |
| G03 | 03,36 | 4 | 48 | 96 |
| G04 | 03,47 | 2 | 24 | 48 |
| G05 | 03 | 0 | 32 | 96 |
| G06 | 05,14,27,36 | 0 | 8 | 0 |
| G07 | 05,14 | 4 | 48 | 96 |
| G08 | 05,25 | 4 | 48 | 96 |
| G09 | 05 | 0 | 32 | 96 |
| G10 | 14,16 | 4 | 48 | 96 |
| G11 | 14 | 0 | 32 | 96 |
| G12 | 16,25 | 2 | 24 | 48 |
| G13 | 16 | 0 | 16 | 48 |
| G14 | 25 | 0 | 16 | 48 |
| G15 | empty | 4 | 64 | 336 |

Use binomial(a,k)=0 for k>a, where a is a nonnegative integer, and set

    N_i(d) = sum_(k=1)^3 binomial(d-1,k) c_(i,k).

Then, for every integer d>=2,

    P(0~e_1) >= B_7(d)
              := B_5(d) + sum_(i=1)^15 N_i(d) q_8(I_i,d).         (2)

The last sum is strictly positive for every d>=2. In particular,

    B_7(3) = 21272798694838039662654613
             / 56120415572268307260000000
           = 0.379056328751598078021... .                         (3)

The added contribution is

    B_7(3)-B_5(3)
       = 146118665900743508898613
         / 56120415572268307260000000
       = 0.002603663290992226709... .                            (4)

The other first two dimensions evaluated give
B_7(2)=0.582979463810902852976... and
B_7(4)=0.276251488917593282094... . These are local lower bounds, with no
conclusion about the number of components.

## 2. Finite cuts force forest edges

For a finite nonempty vertex set S, let delta(S) be its lattice edge
boundary. Its minimum-weight edge f belongs to F: every finite simple cycle
containing f must cross delta(S) at another edge, which has greater weight.
Thus f is not the maximum-weight edge of any finite cycle. The cycle
definition of the free MSF retains it. It follows also that F has no finite
component, since the minimum boundary edge of such a component would leave
it. The same cycle definition implies that F is acyclic.

Let Q be a finite vertex set. Wire its complement to *, retain all edges
meeting Q, and discard edges with both endpoints outside Q. Let T(Q) be
the MST of this finite multigraph, with the original weights. If an edge
f of T(Q) has both endpoints in Q, remove it and let S be the component
of T(Q)-f not containing *. This S is a finite subset of Q. Every edge
of delta(S) has the same representative and weight in the finite graph.
The edge f is the minimum across this cut: any lighter crossing edge would
replace it to give a spanning tree of lower weight. The preceding paragraph
therefore gives f in F.

For a simple path P from 0 to e_1 avoiding e, let Q be its vertex set and
let A_P be the event P is contained in T(Q). The wiring graph is H(I,d),
where I is the full induced edge set in path order. Indeed, a vertex v has
deg_I(v) neighbors in Q and exactly 2d-deg_I(v) edges to its complement.
Each such edge is retained separately, even if exterior endpoints coincide.
Consequently

    P(A_P)=q_n(I,d),    and    A_P implies P is contained in F.    (5)

The event A_P implies 0~e_1 and e not in F. Otherwise P union {e} would
be a cycle in F. Two different simple paths between the same endpoints
cannot both lie in a forest. For completeness, choose an edge of one path
not on the other. Its endpoints have a walk between them in the union
without that edge: go back along the first path to 0, along the second
path to e_1, then back along the first path to the chosen edge. Erasing
loops in this walk gives an alternative path, and hence a cycle. Thus the
events A_P are pairwise disjoint, across different lengths as well as within
one length. They are also disjoint from {e in F}.

## 3. The direct edge and the earlier contribution

Lattice invariance makes p=P(f in F) the same for every lattice edge f.
For B_R={-R,...,R}^d there are V_R=(2R+1)^d vertices and
M_R=d(2R)(2R+1)^(d-1) internal lattice edges. Let K_R be the number of
components of the induced forest F[B_R], counting isolated vertices.
Every such component meets the inner vertex boundary: a path in its
infinite F component from a vertex in B_R to outside B_R has an initial
segment in that induced component reaching the boundary. Distinct induced
components have distinct boundary vertices. Hence

    1 <= K_R <= (2R+1)^d-(2R-1)^d.

Since a finite forest has its number of vertices minus its number of
components edges, expectation gives

    (2R-1)^d <= p M_R <= (2R+1)^d-1.

Divide by V_R and let R tend to infinity. Both bounding ratios tend to 1,
while M_R/V_R tends to d. Thus p=1/d.

The three-edge detours number 2(d-1), one per elementary square containing
e. Five-edge detours close with e to form six-cycles. The planar ones are
boundaries of 2-by-1 rectangles: per transverse axis there are two with
e along a short side and four with e along a long side. Their induced
graphs are respectively A_6 and B_6.

A nonplanar six-cycle uses three axes, each once in each direction, and
lies in a unit cube. There are 4*binomial(d-1,2) such cubes containing e.
Six vertices on a cube cycle leave out one vertex of each parity. If these
omitted vertices are antipodal, the remaining induced graph is a chordless
six-cycle; there are four such omissions per cube. If they are adjacent,
the induced graph is two squares sharing one chord; there are twelve such
omissions. Each antipodal omission contributes six cycle edges. Each
adjacent omission contributes two distinguished edges of type A_6 and
four of type B_6. By symmetry over the twelve cube edges, the numbers
through a fixed cube edge are 4*6/12=2, 12*2/12=2 and 12*4/12=4.

Combining cube and rectangle contributions gives respectively
4(d-1)(d-2), 2(d-1)(2d-3) and 4(d-1)(2d-3), as in (1).
Section 2 and the direct edge identity prove the bound B_5(d).

## 4. Complete seven-edge enumeration and extension to all d

Closing a seven-edge detour by e produces a simple eight-cycle. Every used
axis contributes an equal positive number of steps in its two directions,
and therefore at least two steps. There are at most four used axes. Axis 1
is among them because the closing edge has direction -e_1. There is at
least one transverse axis, since a one-dimensional nearest-neighbor graph
has no cycle. Thus the number k of used transverse axes is 1, 2 or 3.

For a prescribed set of k transverse axes, delete all identically zero
coordinates and relabel the chosen transverse coordinates in increasing
order. This is a bijection with detours in Z^(k+1) using all k transverse
axes. It preserves the induced edge set in path order. In particular,
there is no factor of k! or 2^k to add: the axes are already ordered and
both signs occur in the enumeration. Choosing the transverse axis set
proves the formula for N_i(d) from the table of c_(i,k).

Here is an exhaustive construction of that finite table. For k=1,2,3,
start at the origin in Z^(k+1) and successively append each of the
2(k+1) nearest neighbors of the current vertex. Reject repeated vertices,
the direct edge e, and any arrival at e_1 before step seven. With l steps
remaining, reject a partial path whose distance to e_1 is greater than l
or has parity different from l. These rejections cannot remove a valid
completion: each nearest-neighbor step changes distance by one. At seven
steps retain exactly the paths ending at e_1. Each direction sequence has
one branch in this recursion, so no path is duplicated or missed.

Retain paths using all k transverse axes. On their eight vertices test
every pair for lattice distance one to form the full induced graph.
Identify an edge set only with its reversal i -> 7-i, taking the smaller
sorted list of pairs. Reversal preserves q_8 by relabeling H(I,d).
The complete output is the 15-row table in Section 1. Its column sums are
28, 496 and 1296. Representative coordinates for each row and the full
induced edge lists are in graphs.json; the recursion is walks() followed
by enumerate_graphs() in seven.py.

An independent exhaustive enumeration checks this table. Fix the last
step of the closed cycle to be -e_1. Let a_j be the number of positive
steps along axis j; there must also be a_j negative steps in the whole
cycle. The conditions are

    sum_j a_j=4,    a_1>=1,    a_j>=0.

For each such vector, the first seven steps have direction multiplicities
a_1 positive and a_1-1 negative along axis 1, and a_j of each sign along
every other axis. Enumerate every distinct permutation of this multiset.
Build its entire path, and only then reject words with repeated vertices.
The endpoint is necessarily e_1. Each simple detour has exactly one vector
of counts and one direction word in this enumeration, and is retained.

The number of raw words for each vector is checked against the multinomial
coefficient 7! divided by all direction-multiplicity factorials. The full
induced graph is obtained separately by neighbor lookup in the coordinate
set, rather than by pairwise distance tests. This gives the following
checks; every graph count, not just the totals, agrees with N_i(d).

| d | raw direction words | simple detours | induced graph classes |
|---:|---:|---:|---:|
| 2 | 1225 | 28 | 8 |
| 3 | 7455 | 552 | 15 |
| 4 | 23765 | 2868 | 15 |
| 5 | 55195 | 8272 | 15 |

The d=5 check is beyond the dimensions used to construct the table.
The total count in any dimension is therefore

    N_7(d) = 28(d-1)+496 binomial(d-1,2)+1296 binomial(d-1,3)
           = 4(d-1)(54d^2-208d+207).                            (6)

The first expression follows by summing the table. To verify the second,
put x=d-1 and expand: 28x+248x(x-1)+216x(x-1)(x-2)
=216x^3-400x^2+212x=4x(54x^2-100x+53).

All seven-edge certificate events are disjoint from one another and from
the earlier events by Section 2. Adding their probabilities to (1) proves
(2). Each finite probability is positive: if all seven desired path edges
are lighter than every other edge of H(I_i,d), Kruskal accepts them.
This event has probability 1/binomial(16d-|I_i|,7)>0 because H(I_i,d)
has |I_i|+sum_v(2d-deg_I_i(v))=16d-|I_i| edges. At least one of the
positive first-column counts occurs for every d>=2. This proves strict
improvement over B_5(d) in every such dimension.

## 5. Exact finite probability formula

The following formula defines the probabilities in (2) in every dimension,
without a numerical approximation. For a vertex r with m_r>0 choose one
specified spoke r*, and put T_r=P_n union {r*}. A tree containing P_n
must be exactly of this form: P_n already joins all n non-root vertices,
and a spanning tree on n+1 vertices has n edges. There are m_r choices
of the specified spoke.

For a subset S of T_r, write pi(S) for its connected-component partition
and set

    D_r(S) = sum_(ab in I) 1{pi_a(S) != pi_b(S)}
             + sum_v m_v 1{pi_v(S) != pi_*(S)}.

For an ordering sigma of the n edges of T_r, let S_j be the first j edges,
with S_0 empty. Then

    q_n(I,d) = sum_(r:m_r>0) m_r
                 sum_(sigma in permutations(T_r))
                    product_(j=0)^(n-1) 1/D_r(S_j).             (7)

To prove this formula, replace every uniform label U by -log(1-U). The
labels become independent rate-one exponentials and all edge comparisons
are preserved. At a stage of Kruskal's algorithm, each edge joining two
different current components has not yet been examined; otherwise its
endpoints would have merged. Conditional on the elapsed time and the past,
the residual exponential clocks on crossing edges are independent with
rate one. Thus each particular crossing edge is next accepted with
probability the reciprocal of the number of crossing edges, D_r(S_j).
Edges internal to a component can be ignored forever. The n edges in T_r
never form a cycle in a proper prefix. Multiplication gives the probability
of a specified accepted-edge sequence. Sum over all sequences, spoke
choices and r; the resulting MSTs and their accepted-edge orders are
disjoint outcomes. This proves (7).

The fixed_tree_probability() computation evaluates (7) by dynamic
programming. If f_r(S) is the sum of products for completions from S, then

    f_r(T_r)=1,
    f_r(S)= [sum_(t in T_r\S) f_r(S union {t})]/D_r(S),
    q_n(I,d)=sum_r m_r f_r(empty).

The separate event_probability() calculation does not fix a final tree.
It recurses on component partitions. A crossing desired path edge may
be accepted; a spoke may be accepted only while the root is isolated.
Other accepted edges preclude success: a non-path internal edge would
make a cycle with the eventual complete path, and two spokes would make
a cycle through the root once the path is complete. Rejected edges inside
components do not affect future partitions. A partition in which all
non-root vertices are connected is successful with probability one,
because its accepted internal edges then comprise the whole desired path.
The recurrence divides the weighted sum of allowed transitions by the
number of all crossing edges. All spoke choices at a vertex have the
same next partition and contribute multiplicity m_v. This derives an
independent recursion for the same event.

For the seven-edge graphs, n=8; each fixed-tree computation has 256 subset
states. Zero-spoke vertices occur in some d=2 graphs and are handled by
omitting those root choices in (7). No positivity of every m_v is assumed.

## 6. Independent cycle-integral check and arithmetic

Fix one T_r and its uniform labels x_f. For every non-tree edge h, let
L_h be the edge set of the unique T_r path between its endpoints. Then

    T_r is the MST iff U(h)>max_(f in L_h) x_f for every h not in T_r. (8)

Necessity follows by exchanging h with the largest edge on its tree path.
For sufficiency, any competing edge crossing the fundamental cut of a
tree edge f has a tree path containing f, so (8) makes it heavier than f.
Each tree edge therefore minimizes its fundamental cut and belongs to the
MST, establishing sufficiency.

Conditional on the tree labels, independence gives the product of
1-max_(f in L_h) x_f over non-tree edges, counting multiplicities. On a
simplex x_(0)<...<x_(n-1), let h_j count the non-tree edges whose largest
tree-path label is x_(j). The integral is

    integral product_j (1-x_(j))^h_j dx
       = product_(j=0)^(n-1) 1/[n-j+sum_(l=j)^(n-1) h_l].       (9)

Indeed, set y_j=1-x_(j), so 1>y_0>...>y_(n-1)>0. Integrating the last
variable gives 1/(h_(n-1)+1) and adds h_(n-1)+1 to the exponent of the
preceding variable. Repeating gives (9). For a suffix S of the tree-edge
label ordering, sum h_l over that suffix counts precisely the non-tree
edges whose tree path meets S; this is how audit.py evaluates the factors.
It uses explicit permutations and tree routes, without component partitions.

For every one of the 15 graphs in d=3, the sum of (9) over all 8!*8=322560
simplices and all spoke choices agrees exactly with both recursions.
The fifteen rational probabilities are recorded individually in audit.txt,
audit.json and extension.json. In all dimensions d=2,...,12, the two
recursions agree on all 158 graph probabilities with nonzero multiplicity.

As a separate overlap check in d=3, enumerate all 600 paths of lengths
3,5,7. Their 179700 unordered pairs all have at least as many edges as
vertices in their connected union, and hence each union has a cycle.
This includes pairs with overlapping edges or vertices.

For the displayed d=3 numbers, summing the 15 exact contributions gives
the numerator and denominator in (4). The previous bound has numerator
347146143557 and denominator 922150845000. The latter denominator divides
the denominator D=56120415572268307260000000 in (4), with

    D / 922150845000 = 60858172908000.

Consequently (3) can also be checked by the integer identity

    347146143557 * 60858172908000 + 146118665900743508898613
       = 21272798694838039662654613.

The script audit.py checks every final rational sum for all 11 dimensions
using only integer LCM/GCD operations, separately from Fraction summation
in seven.py. Its Decimal divisions give the quoted truncated expansions.
All checks pass. Full reproduction commands are in REPORT.md and LOG.md.

## Reference and scope

Russell Lyons, Yuval Peres and Oded Schramm, *Minimal spanning forests*,
Annals of Probability 34 (2006), 1665–1692,
[arXiv:math/0412263](https://arxiv.org/abs/math/0412263),
[full paper](https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf), supplies the
free/wired setting and the cycle definition used above.

This finite certificate extension proves no long-distance connection
estimate and no result on the number of infinite components. It does not
establish a transition dimension. Novelty relative to published local
bounds is not established here.
