# A contact-count obstruction for comparing lattice trees with site animals

Let a site animal in Z^d be a finite nonempty vertex set S whose induced
nearest-neighbor graph G(S) is connected. Identify sets under translations only.
Write n = |S|, e = |E(G(S))|, and k = e − n + 1. Let tau(S) be the number of
spanning trees of G(S), with tau(S) = 1 for a singleton. A bond tree is a
connected acyclic nearest-neighbor graph, again considered up to translation.
Its size here is its number of vertices.

For a bond tree with vertex set S, the number of nearest-neighbor pairs in S
that are not tree edges is exactly k: every spanning tree has n − 1 edges.
Thus k is the non-bonded contact count, independent of the choice of tree.

## Statement

The following assertions hold.

1. Forgetting the edges of bond trees gives each site animal S multiplicity
   tau(S). In particular, if a_d(n) counts site animals and t_d(n) counts bond
   trees, then

   t_d(n) = sum over |S| = n of tau(S),

   a_d(n) = sum over bond trees T with |V(T)| = n of 1/tau(V(T)).

2. In Z², the smallest n for which two site animals with the same (n,k) have
   different tau is 7. There are examples with k = 2 and tau = 15, 16.
   In Z³, the smallest n is 6, with k = 1 and tau = 4, 6. The same minimum 6
   holds in every Z^d with d >= 3.

3. For every integer r >= 1 there are pairs S_r, R_r in Z² with

   |S_r| = |R_r| = 8r − 1,  k(S_r) = k(R_r) = 2r,
   tau(S_r) = 15^r,  tau(R_r) = 16^r.

   There are pairs in Z³ with

   |S_r| = |R_r| = 7r − 1,  k(S_r) = k(R_r) = r,
   tau(S_r) = 4^r,  tau(R_r) = 6^r.

4. Consequently, no positive function w(n,k) can correct the pushforward of
   uniform bond-tree counting to uniform site-animal counting shape by shape.
   More strongly, no such function can make every corrected shape weight
   w(n,k(S)) tau(S) lie between exp(−epsilon(n)) and exp(epsilon(n)), where
   epsilon(n) = o(n). This remains true if arbitrary size-dependent
   normalization constants are allowed.

These assertions do not determine critical exponents. In particular, they do
not contradict dimensional reduction or universality between tree and animal
ensembles.

## 1. The counting identity

Fix a site animal S. Every bond tree with this vertex set is a spanning tree
of G(S), and every spanning tree of G(S) is a bond tree with vertex set S.
This is a bijection with tau(S) choices. No two different spanning trees on S
become identified by a translation: a translation preserving a nonempty finite
set must be zero. Indeed, a nonzero translation preserving S would imply that
S contains the infinite orbit of any of its points.

Summing the fiber size tau(S) proves the first identity. Giving every element
of that fiber weight 1/tau(S) gives total weight one and proves the second.
This argument does not identify rotations or reflections.

## 2. Elementary graph facts

Every hypercubic lattice is bipartite: the parity of the sum of a vertex's
coordinates changes at each edge. Also, two distinct lattice vertices have at
most two common neighbors. To see this, a common neighbor gives a two-step
path between them. The difference of the endpoints must therefore have
Manhattan length two. If it is ±2 in one coordinate, the midpoint is the unique
common neighbor. If it is ±1 in each of two coordinates, there are exactly two
possible intermediate vertices. In all other cases there are none. Thus no
hypercubic graph contains K_{2,3} as a subgraph.

A connected graph with e = n − 1 is a tree and has tau = 1. A connected graph
with e = n has a unique cycle: remove the edges of a spanning tree and there
is exactly one remaining edge, which creates exactly one cycle. If its cycle
has length l, all off-cycle edges are bridges, and a spanning tree is obtained
by deleting exactly one of its l cycle edges. Hence tau = l.

If connected graphs share only a single vertex, their spanning-tree counts
multiply. Each spanning tree restricts to a spanning tree in each graph:
leaving one restriction disconnected would leave a component unable to reach
the common vertex. Conversely, a union of one spanning tree from each graph
is connected and acyclic. The same multiplication applies to connected graphs
joined by bridges; every bridge must be retained, and the choices within the
components are independent.

For a theta graph consisting of three internally disjoint paths between the
same two endpoints, of lengths a, b, c, the spanning-tree count is

tau = ab + ac + bc.

There are a + b + c edges and a + b + c − 1 vertices, so a spanning tree deletes
two edges. Deleting two edges from the same path isolates an internal segment
or vertex, while leaving the other two paths intact leaves a cycle. Thus a
tree deletes one edge from each of two paths and leaves the third path intact.
Each such choice is connected and has the required number of edges. The three
choices of intact path give respectively bc, ac, ab possibilities.

## 3. The planar witnesses and their minimality

Use the following seven-site sets:

```text
A2 = {(0,-1), (0,0), (0,1), (1,0), (1,1), (2,0), (2,1)}
B2 = {(0,0), (0,1), (1,-1), (1,0), (1,1), (2,-1), (2,0)}.
```

The induced graph of A2 is a 3-by-2 array of vertices with a pendant vertex
(0,−1) attached to (0,0). The array has seven edges. Between the endpoints of
its middle cross-edge there are three internally disjoint paths of lengths
1, 3, 3. The pendant edge is a bridge. Therefore A2 has eight edges, k = 2,
and tau(A2) = 1·3 + 1·3 + 3·3 = 15.

The graph of B2 consists of the four-cycle on
{(0,0),(0,1),(1,0),(1,1)} and the four-cycle on
{(1,−1),(1,0),(2,−1),(2,0)}. They meet only at (1,0), and there are no extra
nearest-neighbor edges between their other vertices. Consequently B2 also has
eight edges and k = 2, while tau(B2) = 4·4 = 16.

Here is a size-based proof that no earlier mismatch occurs. For any connected
hypercubic graph on n <= 5 vertices, a bipartition has one side of size at most
two. A part of size one gives at most n − 1 edges. With part sizes 2 and 2
there are at most four edges. With part sizes 2 and 3 there are at most five
edges, since six edges would give K_{2,3}. Thus the graph is either a tree or
unicyclic, and its only possible cycle has length four. Its tau is respectively
1 or 4, determined by k.

Consider now six vertices. A bipartition of sizes 1 and 5 gives a tree. For
sizes 2 and 4, the two vertices in the smaller part have at most two common
neighbors; their neighbor sets have union of size at most four. Their total
degree is therefore at most six. For sizes 3 and 3, eight or more edges would
leave at most one missing edge of K_{3,3}. Two vertices in one part would then
have three common neighbors, which is impossible. Thus e <= 7 in all cases.

If e = 7, the bipartition must have sizes 3 and 3. Exactly two edges of K_{3,3}
are missing. They cannot share an endpoint: that would leave two vertices in
the affected part with three common neighbors. With disjoint missing edges,
there is one degree-three vertex in each part, joined by an edge, and two
further internally disjoint paths of length three between them. This is the
theta graph of lengths 1, 3, 3, so tau = 15.

If e = 6 the graph is unicyclic with cycle length four or six. An induced
six-cycle is impossible in Z². A six-step simple cycle has two horizontal and
four vertical steps, or the reverse. In the first case its horizontal span
is one and its vertical span at most two. Vertical span at most one would
allow at most four vertices. Thus all six vertices occupy the 2-by-3 array of
vertices in their bounding rectangle. The induced graph of that array has
seven edges, including a chord of the proposed six-cycle. The other case is
the same with the coordinates exchanged. Therefore for six planar vertices
the possibilities are precisely tau = 1 for k = 0, tau = 4 for k = 1, and
tau = 15 for k = 2. No mismatch with fixed (n,k) occurs before n = 7.

## 4. The cubic witnesses and their minimality

Take

```text
A3 = {(0,0,0), (1,0,0), (0,1,0), (1,1,0), (0,0,1), (0,0,2)}
B3 = {(0,0,0), (1,0,0), (1,1,0), (1,1,1), (0,1,1), (0,0,1)}.
```

The induced graph of A3 is a four-cycle in the plane z = 0 with a two-edge
pendant path attached at the origin. It has six edges and tau(A3) = 4.
In the displayed order the vertices of B3 form a six-cycle, including the
edge from the last vertex to the first. Each vertex has precisely two
neighbors within B3, so there are no chords; hence tau(B3) = 6. Both sets
have six vertices and k = 1.

The n <= 5 argument in Section 3 holds in every hypercubic dimension and gives
tau = 1 or 4 determined by k. Therefore n = 6 is minimal in Z³. Embedding these
sets in the first three coordinates adds no induced edges and proves the
same assertion in every dimension d >= 3.

## 5. Amplification by bridges

Both planar gadgets have first coordinate between 0 and 2 and contain the
ports L = (0,0), R = (2,0). For either gadget G, place copies

G_j = G + (4j,0),  j = 0,...,r−1,

and add the r − 1 connector vertices c_j = (4j+3,0), j = 0,...,r−2.
Different gadgets have first-coordinate separation at least two, so they
have no edges directly between them. A connector is adjacent to the right
port of G_j and the left port of G_{j+1}. It has no other neighbors in the
union: any candidate must have the same second coordinate and adjacent first
coordinate, and in each of those columns the sole vertex with second
coordinate zero is the port. Connectors are four units apart and hence are
not adjacent to one another. Each of the two edges at a connector is a bridge,
since it is the only connection across the corresponding cut between the
blocks. This also proves connectedness and accounts for every induced edge.

Thus the union has

n = 7r + (r−1) = 8r−1,
e = 8r + 2(r−1) = 10r−2,
k = e−n+1 = 2r.

By bridge multiplication, choosing G = A2 or B2 gives tau = 15^r or 16^r.

For the cubic gadgets the first coordinate lies between 0 and 1, with ports
L = (0,0,0), R = (1,0,0). Place copies G_j = G + (3j,0,0) and connector
vertices c_j = (3j+2,0,0). The same distance argument shows that the only
inter-gadget edges are the two bridge edges at each connector. In this case

n = 6r + (r−1) = 7r−1,
e = 6r + 2(r−1) = 8r−2,
k = r,

and tau = 4^r or 6^r.

## 6. Consequence for contact-only weights

Assign every bond tree with n vertices and k non-bonded contacts weight
w(n,k) > 0. Section 1 shows that the induced weight of a site animal S is
w(n,k(S)) tau(S). For either pair in Section 5 the factor w is the same for
both shapes. Their corrected weights therefore have ratio (16/15)^r in
dimension two, and (6/4)^r in dimension three. Exact equality of the two
shape weights is impossible already when r = 1.

If both weights lie between exp(−epsilon(n)) and exp(epsilon(n)), their ratio
is at most exp(2 epsilon(n)). Consequently the planar pairs force

epsilon(8r−1) >= (r/2) log(16/15),

and the cubic pairs force

epsilon(7r−1) >= (r/2) log(3/2).

These lower bounds grow linearly in n on the displayed subsequences, contrary
to epsilon(n) = o(n). Any normalization depending on n alone can be absorbed
into w without changing the argument.

The number of occupied-to-unoccupied boundary bonds is 2dn − 2e: count the
2d incident bonds at each occupied vertex, then subtract twice the number of
internal bonds. Since e = n − 1 + k, the same obstruction applies to weights
depending on n and this bond perimeter. The statement does not concern the
number of distinct unoccupied boundary vertices, which need not be determined
by n and e.

## 7. Exact finite certificates

`enumerate_animals.py` enumerates all translation classes in Z² through n = 8
and Z³ through n = 7. It records the joint distribution of (k,tau), not an
estimate of an exponent. Each graph's tau is computed both from an integer
Laplacian cofactor and by explicit enumeration of all (n−1)-edge subsets.
The latter test rejects cycles by disjoint sets. An acyclic n-vertex graph
with n−1 edges is connected, so this test counts exactly spanning trees.

The growth generator is complete because every finite connected graph with
at least two vertices has a vertex whose deletion preserves connectedness:
take a leaf of any spanning tree and retain the rest of that spanning tree.
Adding every boundary vertex therefore generates every animal inductively.
Subtracting the lexicographically least vertex gives one representative of
each translation class; a set removes duplicate growth histories.

The exclusion generator fixes that least vertex at the origin and permits
only lexicographically larger added vertices. At a recursion state it considers
each frontier vertex in order. The branch including a vertex permits all
later frontier vertices and any new neighbors; later branches exclude that
vertex. For any target completion, choose the first current frontier vertex
belonging to it. Earlier frontier vertices are absent from the target and can
be excluded. Connectivity guarantees that such a vertex exists until the
target has been reached. Induction gives one branch to every target, and
excluding each earlier choice prevents another branch from reaching it.
The two generators agree on the entire set of shapes at every computed size.

The separate `audit_obstruction.py` uses rational Gaussian elimination,
squared-distance edge tests, and subset reachability. It checks all four
explicit gadgets, locates them in the enumeration, and verifies the chain
formulas at r = 1, 2, 3, 5, including deletion tests for every bridge.
These finite checks support the formulas; the all-r result follows from
Section 5.

It also enumerates every labeled connected bipartite graph on two through six
vertices, with each possible bipartition size, and rejects graphs containing
two vertices with three common neighbors. Every retained graph has the
(k,tau) values used in the small-graph argument above. This check uses neither
animal generator. Retained graphs need not all embed in a hypercubic lattice;
the condition is used only as a necessary constraint.

## Scope

This is an obstruction to a uniform, shape-by-shape comparison of bond trees
and site animals using only size and non-bonded contacts. It does not rule out
identities after summing over shapes, and it does not show that the exceptional
families have significant probability in either ensemble. No conclusion about
theta in dimension two or three follows. The counting identity is elementary;
no claim of historical novelty is made for it or for this obstruction.
