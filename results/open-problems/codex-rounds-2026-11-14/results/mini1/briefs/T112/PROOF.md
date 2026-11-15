# An exact census of cyclically joined triples of chains

Let \(m\) be a positive integer. Begin with three disjoint chains
\[
A_1<\cdots<A_m,\qquad B_1<\cdots<B_m,\qquad C_1<\cdots<C_m.
\]
For a tuple \(g=(a,b,c,d,e,f)\in\{1,\ldots,m\}^6\), add
\[
A_a<B_b,\qquad B_c<C_d,\qquad C_e<A_f.
\]
If the resulting directed graph is acyclic, let \(P(m,g)\) be its
transitive closure. Different tuples can present isomorphic posets.
All counts below count tuples, not isomorphism classes.

For a nonchain poset \(P\), write
\[
\delta(P)=\max_{x\ne y}\min\{\Pr(x<y),\Pr(y<x)\},
\]
where the probabilities refer to a uniform linear extension.
Comparable pairs contribute zero.

## Finite result

For every acyclic nonchain presentation \(P(m,g)\) with \(1\le m\le8\),
\(\delta(P(m,g))\ge1/3\). There are 364,392 such presentations.
Among the 347,718 presentations having width three, the exact minimum is
\[
\frac{137}{344}>\frac13.
\]
It is attained at \(m=3\), \(g=(1,1,3,3,1,3)\).
This example has 344 extensions and
\(\Pr(A_3<B_3)=137/344\). Every pair has balance at most this value.

The exact minima by chain length are as follows. An ordinal-indecomposable
poset means one that cannot be written as an ordinal sum of two nonempty
posets.

| m | Nonchain presentations | Width-three presentations | Minimum over all nonchains | Minimum at width three | Minimum at width three, ordinal-indecomposable |
|---|---:|---:|---|---|---|
| 2 | 34 | 13 | 5/13 | 11/24 | 11/24 |
| 3 | 507 | 360 | 1/3 | 137/344 | 137/344 |
| 4 | 3,087 | 2,592 | 1/3 | 36/85 | 3/7 |
| 5 | 12,238 | 11,020 | 1/3 | 17/40 | 7599/17770 |
| 6 | 37,380 | 34,875 | 1/3 | 313/715 | 13082/29735 |
| 7 | 95,679 | 91,098 | 1/3 | 3/7 | 32763/74260 |
| 8 | 215,467 | 207,760 | 1/3 | 125/286 | 22205/49566 |

For \(m=1\) the only presentation is cyclic. The finite result above is
established by the exhaustive integer computation described below; it is
not an assertion for arbitrary chain lengths.

## Rejection and coverage

A directed cycle must use all three added relations, since chain edges
stay on their own chains and each joining edge advances from one chain to
the next in the cyclic order \(A,B,C,A\). The segment from \(B_b\) to
\(B_c\) exists exactly when \(b\le c\); similarly the other two segments
require \(d\le e\) and \(f\le a\). Consequently a presentation is cyclic
if and only if
\[
b\le c,\qquad d\le e,\qquad f\le a.
\]
There are therefore exactly \([m(m+1)/2]^3\) cyclic presentations.

There are exactly \(3(m-1)\) acyclic chain presentations. To see this,
consider their unique linear extension and mark the chain of each element.
Every change of chain between consecutive elements requires a joining
edge: a longer directed path would have an intermediate element between
them. Thus the changes follow the cyclic order and there are at most
three changes, one for each joining edge. There must be at least two
changes to include all three chains. Exactly two changes would put each
chain in one contiguous block; the third joining edge, from the last
chain to the first, would then be violated. There are exactly three
changes. Up to cyclic rotation, the extension has the form
\[
A_1,\ldots,A_t,\ B_1,\ldots,B_m,\ C_1,\ldots,C_m,
\ A_{t+1},\ldots,A_m,
\quad 1\le t<m.
\]
Its three changes force
\(a=t,b=1,c=m,d=1,e=m,f=t+1\). Conversely these parameters force exactly
that total order. This proves the count.

For each \(m\), both programs enumerate all six coordinates in the stated
ranges. The independent verifier rejects cycles by Boolean transitive
closure and recognizes chains by comparability of every pair. It requires
exactly one certificate row, with matching coordinates, for each remaining
tuple, and rejects extra rows. As an arithmetic cross-check,
\[
\sum_{m=1}^{8}\left[m^6-\left(\frac{m(m+1)}2\right)^3-3(m-1)\right]
=364392.
\]
The raw total is 446,964; 82,488 presentations are cyclic and 84 are chains.

## Lattice-path extension counts

In an extension prefix, the elements already used on each chain form an
initial segment. Record their lengths as \(s=(i,j,k)\). A linear extension
therefore determines a path from \((0,0,0)\) to \((m,m,m)\), increasing one
coordinate by one at every step. Conversely such a path specifies exactly
one ordering of the labeled elements.

The step inserting \(A_{i+1}\) is allowed precisely when \(i<m\) and
\[
i+1<f\quad\hbox{or}\quad k\ge e.
\]
Indeed the only additional incoming relation on chain A is
\(C_e<A_f\). Before \(A_f\) this gives no condition; from \(A_f\) onward
it requires \(C_e\) to have appeared. The corresponding tests for inserting
\(B_{j+1}\) and \(C_{k+1}\) are
\[
j<m,\quad j+1<b\ \hbox{or}\ i\ge a;
\qquad
k<m,\quad k+1<d\ \hbox{or}\ j\ge c.
\]
These tests enforce every generating relation, hence its transitive
closure. Thus admissible paths and extensions are in bijection.

Let \(F(s)\) count paths from the origin to \(s\), and \(G(s)\) count paths
from \(s\) to the terminal state. Set \(F(0,0,0)=1\) and
\(G(m,m,m)=1\). In increasing coordinate order, add \(F(s)\) to every
allowed successor. In decreasing order, set \(G(s)\) to the sum over its
allowed successors. The total extension count is
\[
E=F(m,m,m)=G(0,0,0).
\]
For an allowed step \(s\to t\), concatenating a prefix path, this step,
and a suffix path gives a bijection with the extensions using that step.
The number of such extensions is exactly \(F(s)G(t)\).

Fix an element \(x\) and another chain \(R\). Let \(H(x,R,q)\) be the sum
of \(F(s)G(t)\) over the steps inserting \(x\) for which the prefix
contains exactly \(q\) elements of \(R\). Every extension inserts \(x\)
once, so \(\sum_q H(x,R,q)=E\). For the element \(R_j\), indexed from
one, \(x\) precedes \(R_j\) exactly when that prefix contains fewer than
\(j\) elements of \(R\). Hence
\[
N(x<R_j)=\sum_{q=0}^{j-1}H(x,R,q).
\]
This computes all cross-chain pair counts. Within-chain pairs are
comparable and contribute zero. The maximum of
\(\min(N(x<y),E-N(x<y))/E\) is therefore exactly \(\delta(P)\).

The first program checks the two identities
\(N(x<y)+N(y<x)=E\) and \(\sum_q H(x,R,q)=E\).
It also compares every comparable cross-chain pair against transitive
closure computed directly from the generating edges.

## Width and ordinal decomposition

Three chains cover the poset, so its width is at most three. The elements
available for insertion at any reachable prefix form an antichain.
Conversely let \(S\) be any antichain, and let \(I\) consist of all strict
predecessors of elements of \(S\). This is an ideal disjoint from \(S\).
After an extension of \(I\), all members of \(S\) are available. Thus
the maximum number of available elements over reachable states equals
the width. The first program uses this test. The independent verifier
instead tests triples containing one element of each chain for pairwise
incomparability. A nonchain not passing that test has width two.

A finite poset is ordinal-indecomposable exactly when its incomparability
graph is connected. One implication is immediate: two ordinal summands
have no incomparability edges between them. For the converse, take two
distinct incomparability components. Every pair between the components
is comparable. If \(u,v\) are adjacent by an incomparability edge and
\(z\) lies in another component, the comparisons with \(z\) have the same
direction. Otherwise \(u<z<v\) or \(v<z<u\), contradicting
\(u\parallel v\). Propagating along paths in both components shows
that all comparisons between them have the same direction. Transitivity
then totally orders the components. If there is more than one component,
they give a nontrivial ordinal-sum decomposition. Both programs compute
connectivity, using different traversal implementations.

## Independent certificate counts and minima

The second program represents a poset by predecessor bitmasks. For a
remaining subset \(S\), define
\[
T(\varnothing)=1,\qquad
T(S)=\sum_{x\in S:\ \operatorname{pred}(x)\cap S=\varnothing}
T(S\setminus\{x\}).
\]
The first element of any extension is exactly one of the eligible
elements in the sum; deleting it gives the indicated extension of the
remaining subset. This proves the recurrence. Immediate generating
predecessors suffice, since respecting them respects every directed path.
Memoization changes only runtime, not the recurrence.

For each certificate \((x,y,E,L)\), the verifier computes \(T(P)=E\)
and \(T(P+(x<y))=L\). Adding the relation selects exactly the extensions
with \(x\) before \(y\). Thus these counts independently check the
certificate probability and the integer inequality
\[
3\min(L,E-L)\ge E.
\]
It passed for all 364,392 rows.

For each class in each row of the table, the certificates give a lower
bound on \(\delta(P)\) for every member. The verifier then checks every
unordered pair of one presentation attaining the claimed minimum, using
the subset recurrence after adjoining that comparison. Its maximum is
the claimed value, giving the matching upper bound. There are 19 distinct
attaining presentations across the table and 2,532 unordered-pair counts.
Their counts are retained in `extrema_pairs.csv`.

A third implementation enumerates all permutations for every presentation
at \(m=1,2\), checks the generating relations directly, and counts every
pair. This checks 65 presentations, comprising 28 cyclic cases, three
chains, and 34 nonchains. It also checks the usual tight three-element
example, which is outside this family.
It additionally enumerates all 1,680 shuffles of three three-element
chains, by choosing the positions occupied by A and then B. Testing the
three gate inequalities leaves exactly 344 shuffles; 137 have A3 before
B3, and every pair has balance at most 137/344. This directly checks the
global width-three minimizer without either counting recurrence.

## Arithmetic and resource bounds

For \(m\le8\), forgetting the gates gives at most
\[
\frac{24!}{(8!)^3}=9465511770
\]
extensions. The multinomial count increases when any chain length
increases, so the same bound applies to all prefix and suffix counts.
Every transition product used in a histogram counts a subset of the
extensions, and is at most \(E\). Every accumulated histogram or pair
count is also at most \(E\). Thus unsigned 64-bit arithmetic suffices
for extension counts. Fraction comparisons use 128-bit products, since
products of two extension counts need not fit in 64 bits.

The path program has at most 729 states. Each predecessor-subset counter
has at most 729 reachable states: remaining sets are complements of ideals
of the original three-chain poset, and an ideal is determined by its three
prefix lengths. Adjoining a comparison only reduces this set of ideals.
The verifier clears its memo table between counts and streams the data.
Measured peak resident memory was 1.969 MiB for the census and 2.828 MiB
for the independent verifier. They ran in 2.514 and 11.035 seconds,
respectively, at inherited nice priority 20. The final permutation and
shuffle audit used 13.859 MiB and 0.090 seconds. All programs are
single-threaded.

The exact commands and full outputs are in `LOG.md`. No conclusion here
concerns arbitrary width-three posets, unequal chain lengths, additional
joining relations, or \(m>8\).
