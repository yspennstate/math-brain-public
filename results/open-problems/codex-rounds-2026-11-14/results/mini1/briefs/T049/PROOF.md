# A finite plaquette bound for nearest-neighbor connectivity

Let F be the free minimal spanning forest of the nearest-neighbor lattice Z^d,
with independent uniform [0,1] edge labels. On Z^d this is also the wired
minimal spanning forest. Write u~_F v when u and v belong to the same tree.
All arguments below take place on the probability-one event that the labels
are distinct.

For m>=1, let H_m be the following multigraph. Its vertices are 0,1,2,3,*.
Its four non-spoke edges are

    01, 12, 23, 30,

and each vertex i in {0,1,2,3} has m distinct parallel edges to *.
All 4+4m labels are independent uniform random variables. Let

    a_m = P(the MST of H_m contains 01,12,23).

An exact finite-sum formula for a_m is given below.

## Proposition

For every integer d>=2 and every nearest-neighbor edge e={u,v},

    P(u~_F v, e not in F) >= 2(d-1) a_(2d-2),

and consequently

    P(u~_F v) >= 1/d + 2(d-1) a_(2d-2).

In particular, for d=3,

    a_4 = 5521/658350,
    P(u~_F v, e not in F) >= 11042/329175,
    P(u~_F v) >= 120767/329175 = 0.366877800562... .

These bounds do not assert that F is connected or that it is disconnected.

## 1. Finite cuts

For a finite nonempty vertex set S, let delta(S) denote the edges with exactly
one endpoint in S. The unique edge f of least label in delta(S) belongs to F.
Indeed, a finite simple cycle containing f must cross delta(S) again. Its other
crossing edge has larger label than f. Thus f cannot be the largest-labeled
edge of any finite cycle. The cycle definition of F retains f.

In particular, F has no finite component: if S were the vertex set of such a
component, its least boundary edge would belong to F and leave S. The cycle
definition also makes F acyclic, since the greatest edge of any finite cycle
is deleted.

Now take any finite vertex set Q and identify all vertices outside Q with *.
Retain each original edge meeting Q, with its original label, including
parallel edges to *. Discard edges with both endpoints outside Q. Let T be
the MST of this finite connected multigraph. Every edge f of T whose two
endpoints lie in Q belongs to F.

To see this, delete f from T and let S be the vertex set of the resulting
component that does not contain *. Then S is a finite subset of Q. The edge f
is the unique least-labeled edge of delta(S): a lighter edge crossing the cut
would replace f and decrease the total weight of T. This cut in the finite
multigraph has exactly the original edges of the lattice cut delta(S), with
the same labels. The first paragraph therefore applies. No assertion about
the behavior of paths outside Q is needed.

## 2. The edge-inclusion probability

Lattice symmetries and the independent identical label law imply that
p=P(e in F) is the same for every edge. For n>=1 put B_n={-n,...,n}^d and
V_n=(2n+1)^d. The number of lattice edges internal to B_n is

    M_n = d(2n)(2n+1)^(d-1).

This follows by choosing an axis, one of 2n positions along that axis, and
one of (2n+1)^(d-1) transverse positions. Independently, summing the 2d
lattice degrees over B_n and subtracting the 2d(2n+1)^(d-1) edges leaving
B_n gives 2M_n, with the same result.

Let K_n be the number of components of the induced forest F[B_n], including
isolated vertices. Since a finite forest has vertices minus components edges,

    |F[B_n]| = V_n - K_n.

Every component of F[B_n] meets the inner vertex boundary of B_n. Otherwise
one could start in that component and follow a path in its infinite F
component to the first exit from B_n; the initial path lies in the same
component of F[B_n] and reaches its boundary, a contradiction. Distinct
components contain distinct boundary vertices. Therefore

    1 <= K_n <= (2n+1)^d - (2n-1)^d.

Taking expectations yields

    (2n-1)^d <= p M_n <= (2n+1)^d - 1.

Divide by (2n+1)^d and let n tend to infinity. Since
M_n/(2n+1)^d=d(2n)/(2n+1) tends to d, both bounds tend to 1.
Thus p=1/d.

## 3. Disjoint plaquette certificates

There are exactly 2(d-1) elementary squares Q containing e: choose one of the
d-1 perpendicular coordinate directions and one of its two signs. In each
such square order the four vertices as 0,1,2,3 so that e=30 and the remaining
three edges form the path P_Q=(01,12,23).

Each of these four vertices has exactly two neighbors inside Q and 2d-2
neighbors outside Q. The multigraph obtained by wiring its complement is
therefore H_(2d-2). Let A_Q be the event that its MST contains P_Q. Then

    P(A_Q)=a_(2d-2).

The total incident-edge count is 4+4(2d-2)=8d-4. As a second count, the
four vertex degrees sum to 8d, of which the four internal edges account
for eight incidences. There are 8d-8 external edges and four internal ones.

By Section 1, A_Q forces all three edges of P_Q into F. It follows that
u~_F v and e not in F: otherwise the four edges of Q would form a cycle in F.

For two different squares Q and Q' containing e, the paths P_Q and P_Q' have
disjoint interiors. Their union is a simple six-edge cycle. Hence A_Q and
A_Q' are disjoint, since F cannot contain that cycle. These events need not
be independent; their incompatibility is what permits addition.

Their disjoint union has probability 2(d-1)a_(2d-2) and is contained in
{u~_F v, e not in F}. The event {e in F}, of probability 1/d by Section 2,
is also disjoint from this union and implies u~_F v. This proves both
inequalities of the proposition.

## 4. An exact formula for the finite probability

Let P={01,12,23}. For each r in {0,1,2,3}, choose one specified spoke r* and
put T_r=P union {r*}. For each of the 24 orderings sigma of the four edges
of T_r, let pi_(r,sigma,k) be the vertex partition obtained by contracting
the first k edges in that ordering, for k=0,1,2,3. At k=0 all five vertices
are separate.

For any such partition pi define

    b(pi) = number of edges in {01,12,23,30} joining different blocks,
    c(pi) = number of i in {0,1,2,3} outside the block containing *.

There are b(pi)+m c(pi) edges of H_m joining different blocks. Then

    a_m = m sum_(r=0)^3 sum_(sigma in S_4)
                  product_(k=0)^3 1/[b(pi_(r,sigma,k))+m c(pi_(r,sigma,k))].   (1)

This has just 96 summands before grouping and is a rational number for every
positive integer m.

Here is a derivation. Replace every uniform label U by -log(1-U). This
strictly increasing transformation preserves all comparisons and hence the
MST, and the new labels are independent exponential variables of rate 1.
Run Kruskal's algorithm. At a given partition, every edge still joining
different blocks has not yet been examined; an examined edge would already
have merged its endpoints. By the memoryless property, the next edge
joining different blocks is uniform among these edges. Edges with both
endpoints in one block can be skipped, since they can never be accepted.

The probability that the successive four accepted edges are one particular
ordering of T_r is consequently the product in (1). A spanning tree
containing P has exactly one spoke and excludes 30: P already connects
the four non-root vertices, and the tree must connect * with one further
edge. There are m choices for the spoke at each r. The accepted-edge
orderings and the resulting trees are disjoint outcomes. Summing their
probabilities proves (1).

For reproducibility, the 96 products in (1) group as follows. Each row
(n; (c_1,b_1),...,(c_4,b_4)) contributes

    n m / product_(j=1)^4 (c_j m+b_j).

```
 n     (c_1,b_1) (c_2,b_2) (c_3,b_3) (c_4,b_4)
 8       (1,2)     (2,3)     (3,4)     (4,4)
 8       (1,2)     (2,3)     (4,3)     (4,4)
 4       (1,2)     (3,3)     (3,4)     (4,4)
 4       (1,2)     (3,3)     (4,3)     (4,4)
12       (1,2)     (4,2)     (4,3)     (4,4)
 4       (2,2)     (2,3)     (3,4)     (4,4)
 4       (2,2)     (2,3)     (4,3)     (4,4)
 4       (2,2)     (3,3)     (3,4)     (4,4)
 4       (2,2)     (3,3)     (4,3)     (4,4)
 8       (2,2)     (4,2)     (4,3)     (4,4)
 4       (3,2)     (3,3)     (3,4)     (4,4)
 4       (3,2)     (3,3)     (4,3)     (4,4)
 4       (3,2)     (4,2)     (4,3)     (4,4)
24       (4,0)     (4,2)     (4,3)     (4,4)
```

The multiplicities sum to 96. Formula (1), rather than the grouped table,
defines the bound independently of any grouping computation.

## 5. Independent evaluation using the cycle inequalities

Fix a particular T_r and assign its four labels x_0,...,x_3. For every edge
h outside T_r, let L_h be the set of tree edges in the unique T_r path
between the endpoints of h. The event that T_r is the MST is exactly

    U(h) > max_{f in L_h} U(f) for every h outside T_r.                 (2)

Necessity follows by replacing a larger tree edge on the cycle made by h.
For sufficiency, delete any tree edge f. Every other edge crossing its
fundamental cut has a tree path containing f, so (2) makes that edge heavier
than f. Thus each tree edge is the unique minimum of its cut and belongs
to the MST.

Conditionally on the four tree labels, independence gives the probability
of (2) as the product, over all non-tree edges h, of

    1 - max_{f in L_h} U(f).

Split the unit four-cube into its 24 ordering simplices, and write the
ordered tree labels as x_(0)<...<x_(3). Let h_i be the number of non-tree
edges whose largest tree-path label is x_(i), counting parallel edges.
On this simplex the conditional probability is

    product_(i=0)^3 (1-x_(i))^h_i.

With y_i=1-x_(i), direct repeated integration over
1>y_0>y_1>y_2>y_3>0 gives the exact integral

    product_(j=0)^3 1/[4-j + sum_(i=j)^3 h_i].                       (3)

For example, integrating y_3 first gives a factor 1/(h_3+1) and adds
h_3+1 to the exponent of y_2; repeating gives (3). Sum (3) over all 24
orders and all four r, and multiply by m for the spoke choices. This
evaluates the same a_m without using the transition probabilities of
Kruskal's algorithm.

The exact calculations by (3) and by a partition recursion agree for
m=2,4,...,22. At m=4 they give 5521/658350. Therefore

    1/3 + 4(5521/658350)
      = 219450/658350 + 22084/658350
      = 241534/658350
      = 120767/329175.

The program `verify.py` also enumerates all 8!=40320 raw edge orders when
m=1. Exactly 3344 produce all three specified path edges, giving
3344/40320=209/2520, in agreement with both methods. This auxiliary check
tests the multigraph calculation; m=1 is not a lattice dimension in the
proposition.

## References and scope

The cycle definition and the equality of the free and wired forests on
Z^d are as in Russell Lyons, Yuval Peres and Oded Schramm, *Minimal spanning
forests*, Annals of Probability 34 (2006), 1665--1692,
[arXiv:math/0412263](https://arxiv.org/abs/math/0412263),
[paper](https://rdlyons.pages.iu.edu/pdf/AOP0151.pdf).

The calculation here is an elementary local bound; no claim is made that
the bound is new. It does not approach probability one or prove infinitely
many components in any dimension. In particular, it does not establish
the proposed critical dimension eight.
