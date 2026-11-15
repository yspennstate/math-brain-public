# Proofs audited for D0068

Standard inputs: the existence of the square-lattice connective constant μ₀;
the Bernoulli bond threshold p_c(Z²)=1/2; almost-sure uniqueness of the
supercritical infinite cluster; Harris association for independent Bernoulli
coordinates; and translation ergodicity of product measure. The proofs below
do not assume the unproved quenched ordinary limit. They are elementary
consequences, not claims of new literature priority.

## 1. Root-independent limsup on any bounded-degree connected graph

Write c_n(x) for rooted counts, c_0(x)=1, and U(x)=limsup c_n(x)^(1/n).
On an infinite locally finite connected graph there is an infinite simple ray
from each vertex (take a branch of the finitely branching tree of finite
simple paths), so c_n(x)≥1. If maximum degree is Δ, c_n(x)≤Δ(Δ−1)^(n−1).

For adjacent x,y split n-step paths from x into those avoiding y and those
first visiting y at time k. Prepending y gives an injection of the avoiding
paths into (n+1)-step paths from y. Reversal bounds the number of k-step
x-to-y prefixes by c_k(y). Ignoring mutual avoidance of prefix and suffix,

    c_n(x) ≤ c_{n+1}(y) + Σ_{k=1}^n c_k(y)c_{n−k}(y).             (1)

For any a>U(y), there is C<∞ with c_j(y)≤Ca^j for all j≥0.
The right-hand side of (1) is at most Ca^(n+1)+nC²a^n. Its nth-root
limsup is at most a. Let a↓U(y) and interchange x,y to obtain equality.
Connectedness extends equality to all vertices. Denote the common value U(G).

For the percolation cluster I, U(I) is translation invariant: translating
the environment translates the unique cluster and merely changes its root.
Ergodicity therefore makes U(I)=U(p) deterministic, simultaneously at all
v∈I. Measurability follows from local finite counts and a countable root
selection, e.g. the first cluster vertex in a fixed enumeration of Z².

The alternative tail proof uses finite changes. Adding a leaf preserves
U by counting at its attachment vertex for n≥2. Adding an edge (a,b)
inside a connected graph gives, when counting at a,

    c_n(a) ≤ c'_n(a) ≤ c_n(a)+c_{n−1}(b),

because a simple path can use the new edge only at its first step. Thus U
is unchanged. Every finite connected attachment can be built using leaves
and internal edges, so it also preserves U. For p∈(1/2,1), take the
probability-one set on which uniqueness holds after every finite edge flip;
it has probability one by finite energy and countability of finite flips.
A finite alteration then changes the infinite cluster by finitely many
edges/vertices: deletion produces only finitely many components, of which
one is infinite and all others finite; addition joins only finitely many
finite components. Compare both clusters through their union to use the
finite-attachment argument. U is consequently a tail variable and is
deterministic by Kolmogorov's zero-one law. At p=1 the graph is deterministic.

This establishes U, not any limit of c_n^(1/n). Inequality (1) is an upper
bound on a convolution; taking liminf does not turn it into an inequality
between the individual liminfs.

## 2. Simultaneous lower bound on liminf by thinning

Fix p>1/2 and a deterministic q∈(1/(2p),1). Sample ω at density p and,
independently, η at density q; retain an edge iff ω_eη_e=1. This is iid
bond percolation of density pq>1/2, hence has an infinite component a.s.
By Fubini, for almost every ω, independent q-thinning has some infinite
component with conditional probability one. All such infinite components
are subsets of the original unique I(ω).

For a fixed such ω, put t_q^ω(u)=P_η(u belongs to an infinite retained
component). Some u∈I has t_q^ω(u)>0, since the event that some vertex
percolates is the countable union of the events for individual vertices.
For any v∈I choose an open finite path π from v to u of length d.
The event that π is retained and the event that u percolates are increasing
in η. Harris association gives

    t_q^ω(v) ≥ q^d t_q^ω(u)>0.                                  (2)

Indeed, on their intersection v and u lie in the same infinite retained
component. The presence of any infinite retained path from v implies an
open retained simple path of each length n. A union bound, conditional
on ω, over the c_n(v) candidate paths gives

    0<t_q^ω(v) ≤ q^n c_n(v),  for every n≥1.                     (3)

Taking nth roots and liminf yields liminf c_n(v)^(1/n)≥1/q for every
v∈I on the same full-measure set. Intersect over a countable sequence
q↓1/(2p). Thus, simultaneously for every v∈I,

    liminf c_n(v)^(1/n) ≥ 2p.                                  (4)

The proof also identifies the independent bond-percolation threshold of
the fixed random graph I as 1/(2p), a.s.: for q below it, the product
configuration has no infinite component and the converse Fubini argument
applies. Use rational q on both sides; no claim at equality is needed.

Harris association here is for the *unconditioned thinning coordinates*
after ω is fixed. There is no assertion that conditioning on membership
in I leaves the original edges independent.

## 3. Annealed rate with the correct conditioning, and log-mean bounds

Let A={0∈I}, θ=P_p(A)>0, and let Z_n count open n-step SAWs from 0 in
the full percolation configuration, even when its cluster is finite.
Then E Z_n=p^n s_n, where s_n is the full-lattice count. Both Z_n and
1_A are increasing. By Harris and the trivial indicator bound,

    p^n s_n ≤ E[Z_n|A] ≤ p^n s_n/θ.                            (5)

Consequently (E[Z_n|A])^(1/n)→pμ₀. This is a conditional ANNEALED
statement, not convergence of the random nth roots.

Put X_n=(log Z_n)/n on the probability space conditioned on A.
Then 0≤X_n≤log 4. Part 2 gives liminf X_n≥log(2p), while Part 1
gives limsup X_n=log U(p). Fatou and reverse Fatou imply

    log(2p) ≤ liminf E[X_n|A] ≤ limsup E[X_n|A] ≤ log U(p).      (6)

In two dimensions Lacoin's strict-gap theorem gives U(p)<pμ₀ for p<1.
Hence the upper bound in (6) is strictly below log(pμ₀). Nothing in
(5) or (6) asserts that E[X_n|A] itself converges.

## 4. All subsequential values form an interval

On any infinite graph of maximum degree four, deleting the last edge
shows c_{n+1}(v)≤3c_n(v) for n≥1. Thus for X_n=log c_n(v)/n,

    X_{n+1}−X_n ≤ log 3/(n+1),

since X_n≥0. Let l=liminf X_n and u=limsup X_n. Each endpoint is a
subsequential limit by boundedness. For l<t<u there are arbitrarily late
indices with X_n<t and subsequent indices with X_n≥t. At the first
upward crossing j, t≤X_j≤t+log 3/j. Taking such crossings with j→∞
gives a subsequence converging to t. No other limit points can lie outside
[l,u]. Exponentiating, the limit-point set of c_n(v)^(1/n) is exactly
[liminf c_n(v)^(1/n), U(G)].

For a fixed environment and root, subsequences realizing either endpoint
can be selected as the first later index within 1/k of that endpoint;
these are measurable environment-dependent indices. This gives neither
a predetermined subsequence converging in probability to U(p) nor a
common subsequence for all roots. It is not a solution to D0068.

## 5. Uniform annealed upper bounds versus a supremum over all roots

For a fixed A₀>0 and b>pμ₀, choose ε>0 so p(μ₀+ε)<b.
For sufficiently large n, s_n≤(μ₀+ε)^n. A union bound and Markov give

 P(max_{x∈[−n^A₀,n^A₀]²} Z_n(x) ≥ b^n)
   ≤ (2 floor(n^A₀)+1)² [p(μ₀+ε)/b]^n.

This is summable. By Borel–Cantelli, the maximum over any polynomial
window has eventual nth-root upper bound b. Intersecting over rational
b>pμ₀ gives upper limsup at most pμ₀. This does not improve to U(p):
the latter would require a quantitative upper-deviation bound at that rate.

In contrast, for each fixed n, almost surely

    sup_{v∈I} c_n(v)=s_n.                                     (7)

To prove it, the event that all edges of a square [−n,n]² are open and
0∈I has positive probability by Harris. Translation ergodicity implies
that such an event occurs at some translate almost surely: the event that
it occurs somewhere is invariant and has positive probability, hence
probability one. At its center all lattice n-step SAWs are open. The
reverse inequality is automatic; intersect over n. Thus taking a supremum
over all roots restores submultiplicativity but yields μ₀, whereas the
typical-root limsup is U(p)<pμ₀<μ₀ for 1/2<p<1.

## 6. Literal degree-two corridors have only logarithmic length nearby

Fix p∈(1/2,1). A corridor of length L is an open simple path of L edges
whose L−1 internal vertices have open degree exactly two. For a fixed
candidate path, its internal vertices require 2(L−1) incidences of closed
off-path edges. Each edge is counted at most twice, so at least L−1
distinct closed edges are specified, disjoint from its L open edges.
The probability is at most p^L(1−p)^(L−1). There are at most
4·3^(L−1) candidate paths from each start. Therefore, writing
ρ=3p(1−p)<1,

 P(a corridor of length ≥m starts in [−R,R]²)
   ≤ (2R+1)² [4/(3(1−p))] ρ^m/(1−ρ).                       (8)

Choose K>3/|log ρ| and m=ceil(K log R). The bound is summable over
integer R≥2, so Borel–Cantelli gives the almost-sure eventual bound
L<K log R+1 for any such corridor starting in that box. Endpoints and
intermediate path vertices were not required to stay in the box.
This excludes length-proportional-to-distance literal degree-two corridors
as the simple explanation of a failure of convergence. It says nothing
about broader sparse regions, visited-vertex traps, or chemical detours.

## 7. A deterministic Z² example with no limit (not stationary)

Let a_k=(k,k), h_k=(k+1,k), t_k=(k,k+1), for k≥0. Always retain
the two edges a_k−h_k−a_{k+1}. If b_k=1 also retain the other two
edges a_k−t_k−a_{k+1}; if b_k=0 omit them. This is a connected,
one-ended, degree-at-most-four subgraph of Z², a series of squares and
two-edge corridors. Other lattice vertices can be left isolated.
Put B_m=Σ_{k=0}^{m−1}b_k, with b_{−1}=0. Direct classification gives

    c_{2m}(a_0)=2^B_m,
    c_{2m+1}(a_0)=2^B_m(1+b_m+b_{m−1}).                       (9)

Here a path crosses each completed cell along one of its retained arcs.
At an articulation it may move one edge backwards along the unused arc
of the preceding square, but it is then trapped at that arc's midpoint.
These are the only alternatives. Even paths end at a_m; odd paths
either take a forward half-arc (1+b_m choices) or the one unused backward
half-arc when b_{m−1}=1. This proves both formulas, including m=0.

Choose block endpoints N_j=2^(2^j), j≥0. Set b_k=1 on [0,N_0),
and on each [N_{j−1},N_j) set b_k=1 when j is even and 0 when j is
odd. At endpoints of zero blocks B_{N_j}/N_j≤N_{j−1}/N_j→0;
at endpoints of one blocks B_{N_j}/N_j≥1−N_{j−1}/N_j→1.
Since 0≤B_m/m≤1, (9) yields

    liminf c_n(a_0)^(1/n)=1,   limsup c_n(a_0)^(1/n)=sqrt(2).

This verifies an obstruction even for a one-ended planar graph with
polynomial ambient volume. It is NOT a translation-invariant random
graph and is NOT a counterexample to D0068 or to its stationary variant.
A uniform random integer translate of this exceptional sequence/strip is
not a probability distribution. No such stationarization is claimed.

## 8. What is still missing

No argument here proves that L(v)=liminf c_n(v)^(1/n) is constant across
vertices or deterministic individually. Ergodicity does make inf_{v∈I}L(v)
and sup_{v∈I}L(v) deterministic, since these are measurable invariant
quantities (test rational levels and use countability). It does not imply
equality. A stationary random field need not have constant value at all
its vertices. Nor has full convergence in probability, convergence of
E[log c_n(0)|0∈I]/n, a p<1 high-density interval of almost-sure convergence,
or a stationary random-subgraph counterexample been proved here.
