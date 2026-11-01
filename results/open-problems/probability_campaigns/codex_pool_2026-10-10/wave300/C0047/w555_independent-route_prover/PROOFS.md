# C0047: finite separators, block branching, and the limit of this route

Author w555, 2026-10-10. All arguments below await independent mathematical review. No claim of solving C0047.

## L1. A disjoint-cutset bound

Let G be a connected, locally finite graph, x,y vertices, and F_1,...,F_n finite, pairwise edge-disjoint sets. Suppose deleting F_i disconnects x from y for every i. In independent Bernoulli bond percolation with parameter p,

P_p(x connected to y) <= product_i [1-(1-p)^|F_i|].

Proof. Every x-y path uses at least one edge of each F_i. Thus the connection event is contained in the intersection of the events A_i that F_i contains an open edge. Each A_i is measurable with respect to the edge variables indexed by F_i. These sigma-fields are mutually independent because their index sets are disjoint in the product Bernoulli measure. P(A_i)=1-(1-p)^|F_i|, proving the bound. This multiplies independent events, not unrelated conditional means.

If |F_i| <= K then the upper bound is [1-(1-p)^K]^n, which tends to zero as n tends to infinity for every p<1.

## L2. A uniqueness obstruction

Suppose G is infinite, connected, locally finite and vertex-transitive. Suppose there are a fixed vertex o, an integer K and vertices y_n with n pairwise edge-disjoint o-y_n cutsets of size at most K. Then p_u(G)=1.

Proof. Fix p<1 and suppose there is exactly one infinite cluster almost surely. By countability, an infinite cluster existing almost surely forces some vertex to belong to one with positive probability; transitivity makes this probability theta_p>0 the same for every vertex. Harris positive association gives

P_p(o and y_n both belong to infinite clusters) >= theta_p^2.

The two events are increasing; finite-radius approximations and monotone limits extend the product-measure Harris inequality to them. Uniqueness makes their intersection a subset of {o connected to y_n}. L1 would imply theta_p^2 <= [1-(1-p)^K]^n for all n, a contradiction. At p=1 the connected graph is its unique infinite cluster, so p_u=1. This proof needs no claim about the number of clusters at p_c.

## L3. Bounded cuts cannot implement L2 on a one-ended nonamenable graph

Let G be an infinite, connected, locally finite, one-ended graph of maximum degree d<infinity. Assume its unnormalized edge isoperimetric constant

h_E = inf{|boundary_E A|/|A| : A nonempty finite subset of V(G)}

is positive. Fix an integer K>=1 and set R=ceil(K/h_E)+1. For any vertices x,y, the number n of pairwise edge-disjoint x-y cutsets of size at most K is bounded by

n <= d (|B_R(x)| + |B_R(y)|).

Consequently, if G is vertex-transitive, this is a finite bound independent of x,y. The hypothesis of L2 cannot hold on such a graph.

Proof. Replace each cutset by an inclusion-minimal subset which still separates x,y; disjointness and the size bound survive. An inclusion-minimal x-y edge cut F disconnects G into exactly two components, containing x and y respectively. Indeed, restoring any edge of F must reconnect x and y, so every edge of F joins those two components; any third component would have an incident edge in F which cannot have that property. Thus F is exactly the edge boundary of either of its two components.

One-endedness implies that at least one component A is finite: if both were infinite, deleting the finitely many endpoints of F would leave at least two infinite components. Since F=boundary_E A, h_E|A|<=K, hence |A|<=K/h_E. A contains x or y and is connected. Every vertex in A is within distance |A|-1 of that endpoint by a simple path within A; every edge of F is incident to A, and therefore lies in the collection of edges incident to B_R(x) or B_R(y). That collection contains at most d(|B_R(x)|+|B_R(y)|) edges. The reduced cuts are nonempty and edge-disjoint, so their number cannot exceed this edge count. This proves the assertion without assuming nested cuts.

Hardest gap for the parent conjecture. Nonamenability gives h_E>0 but no substitute for the independent, bounded separator events of L1. L3 shows that this exact substitute is unavailable on every one-ended nonamenable Cayley graph. Any extension must control mergers using events other than deterministic uniformly bounded cuts, or allow growing cuts together with a quantitatively different probability argument. The parent implication remains unproved.

## L4. Exact survival and nonuniqueness on a cyclic free product

Let m>=3, Gamma=C_2*C_m=<a,b | a^2=b^m=1>, and use the simple undirected right Cayley graph with S={a,b,b^{-1}}. Its degree is three. Let

mu_m(p)=p [2 sum_{k=1}^{m-1} p^k - (m-1)p^m].

Then p_c is the unique root of mu_m(p)=1 in (0,1), and p_u=1. In particular p_c<p_u. This is a rederived known special case, not a new resolution of C0047; compare Kozakova, arXiv:math/0611668 (2006).

Convention check. Kozakova's paper allows edge multiplicity (printed p2) and its cyclic-factor formula at m=2 gives connection probability 2p-p^2, matching two parallel involution edges. Here the C_2 factor is a single edge, with connection probability p. Thus its modular-group numerical value is not this simple graph's value. The argument below uses the graph stated here, not that table. The multiplicity identification is an inference from the primary formula, to be independently checked.

Proof of the block geometry. Each right coset g<C_m> supports an m-cycle of b-edges. Contract all these cycles. Every a-edge joins two distinct cycles, with one a-edge at each vertex of a cycle, giving a connected m-regular quotient. A nonbacktracking cycle in this quotient would give a nontrivial reduced alternating word a b^{k_1} a b^{k_2} ... a b^{k_r}, with every b^{k_i} nonidentity, equal to a word in <b>; this contradicts the free-product normal form. Distinct a-edges cannot give parallel edges by the same normal-form argument. Hence the quotient is a tree. The a-edges are bridges of the original graph.

Nonamenability check. For any nonempty finite vertex set A, let c be the number of components in its induced subgraph and t the number of complete b-cycles in A. All cycles are b-cycles and they are vertex-disjoint, so |E(A)|=|A|-c+t and t<=|A|/m. Consequently |boundary_E A|=3|A|-2|E(A)|>=(1-2/m)|A|+2c, showing h_E>=1-2/m>0. Thus the example meets the nonamenable side of the target without an extra group-theoretic assumption.

Proof of the offspring law. Orient that quotient tree away from a chosen root cycle. Upon entry through a parent a-edge, expose the open cluster of the entry vertex using only the cycle edges of this new block. Let its size be X. Each of its X-1 other vertices has exactly one outward a-edge. An open outward edge creates a distinct child block. Given X, the number of children Y is Binomial(X-1,p).

Different blocks have disjoint cycle-edge sets and disjoint outgoing bridge sets. The entry point is determined by ancestor edges; the descendant block's variables have not been read. Every possible entry point has the same law by cycle symmetry. Thus successive offspring are independent and identically distributed, producing an actual Galton-Watson process, not just a first-moment comparison. The finitely many root choices do not change its extinction threshold.

For a cycle vertex at distance k in one direction, there are exactly two simple arcs from the entry point, of lengths k and m-k. Their edge sets are disjoint; their union has m edges. Its connection probability is p^k+p^{m-k}-p^m. Consequently

E[X-1] = 2 sum_{k=1}^{m-1} p^k - (m-1)p^m,

so E[Y]=mu_m(p). For p<1 the offspring law is bounded and has positive probability of zero children. The Galton-Watson generating function then has extinction probability one when its mean is <=1, and a fixed point below one when its mean is >1: convexity, F(1)=1 and the sign of F'(1)-1 prove these assertions. For m>=3 and 0<p<1, there is also positive probability of at least two children, so the critical case is nondegenerate. The mean is continuous and strictly increasing from 0 to m-1; strict increase follows from the independent exit-edge factor p and monotonicity and positivity of the nonroot cycle cluster size. It crosses one exactly once in (0,1). At that root there is no infinite cluster; above it survival has positive probability. The existence-of-an-infinite-cluster event is invariant under the group action, and the iid edge process is ergodic (disjoint translates of finite-coordinate events give the usual approximation proof), so positive probability of existence implies almost-sure existence. This matches the a.s. definition of p_c.

Finally, choose a path of n edges in the quotient tree and a vertex y_n in its last block. Each of those n a-edges is a distinct single-edge o-y_n cutset. L1 gives tau_p(o,y_n)<=p^n. L2 proves p_u=1. No extra generating set is substituted for S.

## L5. Correct normalization of the elementary spectral sufficient condition

Let G be an infinite connected d-regular undirected vertex-transitive graph. Let P=A/d be the simple-random-walk operator on ell^2(V), and let rho=||P||_{2->2}. For p d rho<1 and r=dist(x,y),

tau_p(x,y) <= (p d rho)^r/(1-p d rho).

Hence p_u(G)>=1/(d rho), and p_c(G)<1/(d rho) is a sufficient condition for p_c<p_u. It is not asserted to be necessary.

Proof. An open x-y connection has a simple open path, so the union bound over simple paths is valid, each with probability p^{length}. Their count is at most the count of all walks of the same length, (A^n)(x,y). This replacement counts walks but does not assign probability p^n to a walk with repeated edges. The matrix-entry bound |(P^n)(x,y)|<=rho^n gives (A^n)(x,y)<=d^n rho^n. There are no length-n paths for n<r. Summing the geometric majorant proves the display. If there were a unique infinite cluster at p d rho<1, Harris would give tau_p(o,y)>=theta_p^2>0 for all y, while vertices arbitrarily far from o make the display tend to zero. Thus no such p has uniqueness, proving the threshold bound. The positive-mean cluster survival part is independent of this walk estimate.

Normalization diagnostic. For the three-regular tree, rho=2 sqrt(2)/3, p_c=1/2 and p_u=1. The prior C0047-A001 description uses normalized rho yet treats p_c<1/rho as a nontrivial sufficient reduction. Here 1/rho=3/(2 sqrt(2))>1, while the valid elementary threshold is 1/(d rho)=1/(2 sqrt(2))<p_c. The prior condition is vacuous on every nonamenable Cayley graph when normalized rho<1; its proposed remaining case p_c>=1/rho cannot occur since p_c<=1. This invalidates the claimed established reduction, not the parent conjecture. No counterexample to the conjecture itself is claimed. The tree's genuine gap demonstrates that L5 is only a sufficient condition.

The diagnostic's tree constants can be derived directly. On the d-regular tree with d>=3, use w(v)=(d-1)^(-dist(o,v)/2). The weighted adjacency row sum divided by w(v) is 2sqrt(d-1) off the root and d/sqrt(d-1)<=2sqrt(d-1) at the root. The weighted Schur bound gives ||A||<=2sqrt(d-1). For f_N equal to w on levels 1,...,N and zero elsewhere, ||f_N||^2=Nd/(d-1) and <f_N,A f_N>=2(N-1)d/sqrt(d-1). Their Rayleigh quotient tends to 2sqrt(d-1), proving equality. Thus rho=2sqrt(d-1)/d. The forward percolation offspring law is Binomial(d-1,p), giving pc=1/(d-1); bridge cuts and L2 give pu=1. These constants require no unverified numerical inference.

## Attempted extension and exact remaining obligation

One possible extension replaces deterministic cuts by adaptively revealed barriers. A sequential product bound would be valid if, for each fixed x,y, the i-th separator were measurable before its own edge variables are exposed, all its variables were fresh independent Bernoulli(p), and it blocked every remaining x-y path. Those conditions give a conditional bound by the tower property. They do not follow from disjointness of the finally selected sets: choosing a cut after seeing its open edges biases its law. Nor does the block offspring calculation survive outside a tree of blocks when distinct children merge.

L3 rules out the deterministic uniformly bounded version on the unresolved one-ended class. No construction of sufficiently many fresh effective barriers, or an alternative quantitative bound on mergers at some p>p_c, is supplied here. That is the single hardest remaining mathematical gap. Current general openness stays UNKNOWN; no novelty or completed-solution claim is made.
