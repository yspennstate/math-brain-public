# C0159 — research attempt, 2026-10-11

## Exact target and notation

Let G be an infinite connected locally finite transitive graph, with independent Bernoulli bond percolation at a fixed p in [0,1]. For distinct infinite open clusters C,D and an integer R>=1, put A_R(C,D)={x in C: d_G(x,D)<=R}. The intake asks whether, almost surely, every such pair has finite A_R for every finite R. Fixed-p almost sure quantifiers are intended; no assertion simultaneous over all real p is made here. The papers define the original neighboring-clusters conjecture at R=1. The stronger intake formulation and the R=1 question are kept separate throughout this attempt.

Write w(x)=m(Gamma_x)/m(Gamma_o)>0 for stabilizer Haar weights of a closed transitive group Gamma. Write W(S)=sum_{x in S} w(x), a nonnegative countable sum. Light means W(S)<infinity; heavy means W(S)=infinity. Countability follows from connectedness and local finiteness. All results below concern bond percolation.

## 1. Finite-weight contacts imply finite superlevel contacts

Lemma. If W(S)=M<infinity, then for every epsilon>0,

    |{x in S:w(x)>=epsilon}| <= floor(M/epsilon).

Proof. Every finite subset F of that superlevel set has |F|epsilon <= sum_F w <= M. If the superlevel set were infinite, it would contain a finite subset of integer size greater than M/epsilon, a contradiction. The same inequality bounds its cardinality when finite. Consequently every sequence of distinct points of S has weights tending to zero: for each epsilon only finitely many terms have weight at least epsilon. Conversely, W(S)<infinity does not imply S finite: the infinite set of positive integers with w(n)=2^(-n) has total weight 1. This is a counterexample to the proposed *logical implication*, not a counterexample to percolation repulsion.

Corollary to Bell–Chu–Rodgers–Terlov–Tserunyan Theorem 1.2. Almost surely, for every distinct pair of heavy clusters C,D, A_1(C,D) meets every modular superlevel {w>=epsilon} in finitely many vertices, with the displayed bound. In particular, if its weights are bounded below, its contact set is finite. This is a consequence of the cited theorem, not a solution published for C0159.

## 2. Light sets have light finite-radius neighborhoods

Lemma. For each finite R there are finite constants B_R,K_R such that |B(x,R)|<=B_R and w(x)/w(y)<=K_R whenever d(x,y)<=R. Thus W(N_R(S))<=B_R K_R W(S).

Proof. Transitivity gives a common finite ball size. The relative weight cocycle is invariant under simultaneous application of Gamma. Transport y to o: the ratios w(x)/w(y) then occur among the finitely many ratios w(z)/w(o), z in B(o,R). Their maximum is K_R. For every x in N_R(S), choose y(x) in S within R. A y has at most B_R preimages. Nonnegative summation and the ratio bound give

    sum_{x in N_R(S)} w(x) <= K_R sum_{y in S} |{x:y(x)=y}| w(y)
                             <= K_R B_R W(S).

No independence or percolation is used. If either C or D is light, A_R(C,D) is light: use A_R subset C if C is light, and A_R subset N_R(D) otherwise. Combined with Theorem 1.2, *every pair* of distinct clusters has a light R=1 contact set (heavy/heavy uses the paper; every other case uses this elementary lemma). This does not upgrade light to finite, or handle heavy/heavy R>1.

## 3. Grandparent graph: closed-cone separators and lightness

Fix b>=2. Let T be the (b+1)-regular tree with a distinguished end xi. Each vertex has one parent toward xi and b children away from xi. The grandparent graph H has all tree edges plus {x,parent(parent(x))} for each x. Use the closed transitive end-preserving group Gamma=Aut(T)_xi, acting on H. Its stabilizer weights satisfy w(parent(x))=b w(x): the common edge stabilizer has index 1 in Gamma_x and index b in Gamma_parent(x). Thus at depth n below a, every vertex has weight w(a)b^(-n), and the b^n vertices of that level have total weight w(a).

Let T_a be the descendant cone of a. Its H-edge boundary consists exactly of:

* {a,parent(a)};
* {a,parent^2(a)};
* {c,parent(a)} for each of the b children c of a.

Indeed an H-edge has endpoints related by one or two parent steps. It can leave a descendant cone only from depth 0 by either type or from depth 1 by the two-step type. Therefore the boundary has b+2 edges. This classification concerns the infinite graph, not just a finite approximation.

At p<1, the probability that all boundary edges are closed is q=(1-p)^(b+2)>0. Boundaries of nested cones with roots spaced by three parent steps are disjoint: crossing the shallower boundary requires endpoints at depths -2,-1,0,1 relative to its root, whereas crossing the deeper boundary, three levels down, requires depths 1,2,3,4; an edge cannot cross both (a crossing of the shallower boundary must have an endpoint outside it). Equivalently a jump of at most two cannot cross both nested boundaries whose root depths differ by three. Events that these boundaries are closed are independent.

Proposition 3.1. For every fixed p<1, almost surely every open cluster is contained in a descendant cone and hence has height bounded above.

Proof. For a fixed vertex v, take cones rooted at parent^(3k)(v), k>=1. Each contains v. Their boundary-closed events are independent with probability q. The probability that none of the first N occurs is (1-q)^N, tending to zero. An occurring event prevents the open cluster of v from leaving that cone. Apply this conclusion to the countable vertex set to obtain it for all clusters. The argument also gives infinitely many closed boundaries for each fixed ascending ray, by applying the same calculation to every tail. At p=1 the conclusion is false; it is not claimed.

Proposition 3.2. For every fixed p<1, almost surely every open cluster of H is light with respect to Gamma.

Proof. First fix a and v in T_a, and let d be the tree depth of v below a. For a vertex x at depth n>d below a, look at the cones rooted along the a-to-x ray at depths d+1,d+4,d+7,..., not exceeding n. There are k=ceil((n-d)/3) such cones. Each contains x and excludes v, since its root has depth greater than d. Every H-path from v to x, including paths leaving T_a, must cross every one of these edge boundaries. Thus if v is connected to x, none of these boundaries is wholly closed. Disjointness and independence imply

    P_p(v connected to x) <= (1-q)^ceil((n-d)/3).

For n<=d use the bound 1. By Tonelli's theorem and the total level weights,

    E_p W(C(v) intersect T_a)
       <= w(a)[d+1 + sum_{m>=1}(1-q)^ceil(m/3)]
        = w(a)[d+1 + 3(1-q)/q] < infinity.

The series identity groups m=3j-2,3j-1,3j for j>=1. A nonnegative extended random variable of finite expectation is finite almost surely: P(X>=t)<=E[X]/t, and let t tend to infinity. There are countably many pairs (a,v) with v in T_a, so the finiteness assertion holds simultaneously for all of them. By Proposition 3.1, for every v its full cluster is contained in some such T_a. On that countable intersection event, W(C(v))=W(C(v) intersect T_a)<infinity. This proves the proposition.

This graph-specific result uses Gamma weights; the proof does not need an identification of the full automorphism group. The weight ratio and the closed subgroup are specified explicitly. It is not claimed as a new literature theorem: prior-art coverage has not been exhaustively checked. It shows that the earlier ledger's proposed upward parallel-cluster mechanism cannot work, and that the weighted heavy-cluster theorem supplies no nonvacuous information for this example at p<1. It does not rule out infinitely many light contacts downward.

## 4. Distance-one information alone is not a deterministic radius reduction

On the transitive graph Z x C4, open only horizontal edges in layers 0 and 2. Close all vertical edges and all horizontal edges in layers 1 and 3. There are two infinite open rails C,D and singleton clusters at the remaining vertices. No two distinct clusters have infinitely many adjacent contacts: C,D are not adjacent; each singleton has at most one neighbor on either rail; singleton pairs each contain only one vertex. Yet every vertex of C is at graph distance two from D. This configuration has probability zero under Bernoulli(p) for 0<p<1, because infinitely many prescribed horizontal rail edges must all be open; it is not a stochastic counterexample.

Lemma (finite-intermediate-cluster reduction). Suppose every pair of distinct clusters in a locally finite configuration has finitely many distance-one contacts. Fix C,D,R. Choose a path of length <=R for each x in A_R(C,D). If all vertices of these paths belong to a single finite collection of open clusters, A_R(C,D) is finite.

Proof. For any fixed pair of distinct clusters in the collection, finite contact vertices and local finiteness give finitely many graph edges crossing between them. There are finitely many pairs, so the union E_* of all such edges is finite. Each chosen path from C to D crosses at least one edge in E_*, since its endpoint clusters differ. Its starting point lies within distance R of an endpoint of E_*. A finite union of finite-radius balls in a locally finite graph is finite, giving the assertion. The ladder configuration demonstrates that infinitely many intermediate singleton clusters prevent this reduction. No finite-intermediate-cluster property is established for Bernoulli percolation here.

## 5. Sprinkling gives the full finite-radius statement away from countably many parameters

The following completes the elementary continuity reduction mentioned in the 2025 paper, including the intake's arbitrary finite radius.

Proposition 5.1. On any countable connected locally finite graph, put phi_uv(p)=P_p(u connected to v). For p<1 and fixed u,v,R, let E_uvR(p) be the event that C_p(u),C_p(v) are distinct infinite clusters and A_R(C_p(u),C_p(v)) is infinite. Then

    P_p(E_uvR(p)) <= phi_uv(p+) - phi_uv(p),

where phi_uv(p+)=lim_{q down to p, q>p} phi_uv(q). Consequently the all-finite-radius repulsion assertion holds almost surely at every p outside a countable deterministic set. In particular it holds whenever all two-point connectivity functions are right-continuous at p.

Proof. Couple Bernoulli percolation at p and q>p by first sampling independent p-open indicators X_e, then sampling independently independent Bernoulli(t) indicators Y_e with t=(q-p)/(1-p)>0, and declaring e q-open if X_e=1 or Y_e=1. The resulting marginal is independent Bernoulli(q), since P(X_e=1 or Y_e=1)=p+(1-p)t=q.

Fix a p-configuration in E_uvR. For every x in its infinite contact set choose a graph path from x to C_p(v) of length between 1 and R (length zero is impossible because clusters are disjoint). There are infinitely many pairwise vertex-disjoint such paths. To construct them, fix enumerations of vertices and finite paths and use a greedy choice. After finitely many paths have been selected, their vertex union F is finite. A candidate of length <=R meeting F must start in the finite set N_R(F), since the graph is locally finite. Infinitely many contact starts remain outside that set, and their paths avoid F. Repeat. The fixed enumerations make these choices measurable functions of the p-configuration; alternatively the conditional probability bound below holds for every configuration with this property.

For each selected path, the probability that all its edges are q-open, conditional on X, is at least t^R: only the X-closed edges need Y=1, and their number is <=R. These events are independent conditional on X because the paths have disjoint edge sets. Therefore the conditional probability that none of the first N paths is q-open is at most (1-t^R)^N, tending to zero. A successful path joins the two p-clusters, so u and v are q-connected with conditional probability one. They were not p-connected. Thus P_p(E_uvR)<=P(u connected at q but not at p)=phi_uv(q)-phi_uv(p). Taking q down to p proves the inequality.

For a fixed monotone bounded function phi, the set of positive right jumps is countable. Indeed jumps at finitely many increasing locations have total size <=1: each phi(p_i+)<=phi(p_{i+1}) so the increments telescope to a bound by the range. Thus at most k right jumps can have size >1/k (using an arbitrary finite subset if necessary). Every positive jump exceeds 1/k for some k, giving a countable union of finite sets. Taking the countable union over u,v gives a deterministic countable exceptional set D. At p not in D, the displayed inequality gives probability zero for every E_uvR; take the countable union over u,v and integer R. Any offending cluster pair contains vertices u,v, so this proves the assertion. At p=1 there is a unique cluster and it is vacuous; at p=0 no infinite open clusters exist. This proves the proposition in all the stated cases.

The proof establishes an actual restriction on every proposed counterexample: at a bad fixed p some two-point function must have a positive right jump. It does not prove those jumps absent on nonunimodular transitive graphs. Sprinkling alone merges the offending clusters at a *different* parameter and supplies no contradiction at p; that is exactly why continuity is needed.

## 6. A complete special case: repulsion on every grandparent graph

Theorem 6.1. On the grandparent graph H of Section 3, for every fixed p in [0,1], almost surely every pair of distinct infinite Bernoulli bond clusters has finitely many contacts at every finite graph radius. This is a graph-specific theorem proved here; no claim of novelty is made.

Proof. We prove continuity of every two-point function and apply Proposition 5.1.

For a vertex a let H_a be the subgraph induced by T_a union {parent(a)}. Let r(p) be the probability that a connects to parent(a) in H_a. It does not depend on a. The graph H_a consists of the direct edge {a,parent(a)}, the b descendant networks H_c for children c of a, and the b additional edges {c,parent(a)}. The H_c edge sets are disjoint, even though their common external terminal a is shared. Each extra edge is independent of those networks and of the direct edge. After deleting parent(a), the child networks meet only at a. A finite open path from a first reaching parent(a) must therefore either use the direct edge or have last edge {c,parent(a)} preceded by an a-to-c connection in H_c. Conversely either event gives the desired connection. It follows exactly, in the infinite network as well as finite truncations, that

    r(p) = F_p(r(p)),   F_p(t)=1-(1-p)(1-p t)^b.

There is a unique solution in [0,1]. For 0<p<1, F_p is concave there (its second derivative is -b(b-1)p^2(1-p)(1-p t)^(b-2)<=0), F_p(0)=p>0, and F_p(1)=1-(1-p)^(b+1)<1. Existence follows from the intermediate value theorem. If 0<r_1<r_2<=1 were two fixed points, concavity applied between 0 and r_2 would give

    F_p(r_1) >= (1-r_1/r_2) F_p(0) + (r_1/r_2) F_p(r_2) > r_1,

contradicting the first fixed point. Zero is not a fixed point for p>0. At p=0 and p=1, F_p is respectively the constant 0 and constant 1, so uniqueness also holds. Consequently r(p) is continuous: for any p_j tending to p, every convergent subsequence of r(p_j) has, by the jointly continuous fixed-point equation, a limit solving the equation at p, which must equal r(p); compactness of [0,1] then makes the full sequence converge.

Next fix a,u,v with u,v in T_a. Let n exceed both depths of u and v below a by at least two. For each x at depth n, consider its whole cone T_x. Its interface with the remaining finite prefix consists of P=parent(x) and Q=parent^2(x). The only edge from T_x to Q is {x,Q}. All other boundary edges lead to P, and the subgraph on T_x union {P} is H_x. Hence there is a connection from P to Q using the cone if and only if {x,Q} is open and x connects to P in H_x. This has probability p r(p). These interface-connection events are mutually independent for different x at depth n: their determining edge sets are disjoint, although their interface terminals may coincide. They are also independent of all prefix edges.

Remove every T_x with depth(x)=n and replace it by an effective edge between its P and Q, retained with probability p r(p). Keep all original H-edges whose endpoints are in the finite prefix of depths 0,...,n-1. Parallel effective edges are allowed and are sampled independently. Connectivity of u and v in the original induced graph H[T_a] is exactly connectivity in this finite replacement network. Indeed a finite path can be split into prefix portions and excursions into the disjoint cones. Any excursion joining two different interface terminals is possible exactly when its effective edge is retained; excursions returning to the same terminal can be dropped. Conversely each retained effective edge has a finite open realizing path by the definition of connectivity in H_x, so any finite replacement path lifts. Thus

    phi_uv^(a)(p)=P_p(u connected to v inside H[T_a])

is a finite reliability polynomial in p and p r(p), and is continuous in p. This replacement is for connectivity probabilities only; it does not claim an iid replacement of the entire percolation configuration.

Finally choose a common tree ancestor s of u and v, and let a_N=parent^(3N)(s). If u is connected to v in H but not inside T_{a_N}, its cluster exits that cone. Exiting it requires crossing each boundary of T_{parent^(3k)(s)}, k=1,...,N. These are disjoint boundaries, so

    0 <= phi_uv(p)-phi_uv^(a_N)(p)
       <= [1-(1-p)^(b+2)]^N.

For every p_0<1 this upper bound tends uniformly to zero on p in [0,p_0], since (1-p)^(b+2)>=(1-p_0)^(b+2)>0. Therefore phi_uv is a uniform limit of continuous functions on each such compact interval and is continuous at every p<1. At p=1, a fixed finite original tree path from u to v is open with probability p^ell, so phi_uv(p)>=p^ell tends to 1=phi_uv(1); continuity holds there as well. Proposition 5.1 proves the asserted repulsion at every fixed p. The countable union over integer radii and vertex pairs is part of that proposition. This finishes the proof.

Audit of the new step. The one-terminal child networks share a vertex, not edges, so their connection events really are independent. The first-hit-of-parent argument forbids using the parent itself to establish the child connection. The two-terminal cone reduction is valid because the grandparent edge to Q is the *only* edge to that terminal. At the upper cone root, the outside ancestors are excluded in phi_uv^(a_N); their possible effect is bounded by the full cutsets, rather than treated as independent effective edges. The fixed-point uniqueness is not assumed and does not rely on a contraction that could fail near a critical point. None of these arguments extends automatically to arbitrary nonunimodular graphs with wider or infinite interfaces.

## 7. Referee audit and checks

The boundary count must include the b edges from the children to the parent's parent-step endpoint; omitting these would invalidate the barrier. Cone containment alone does not imply lightness: the entire cone has infinite weight. Proposition 3.2 additionally uses exponential connection bounds at every deeper level. Independence is invoked only for disjoint edge sets, without conditioning on selected clusters. The descending ray in that proof is deterministic once a,v,x are fixed; there is no union over uncountably many random ends. All simultaneous conclusions use countable vertex/pair sets. The positivity q>0 fails at p=1, where there is one cluster and the repulsion question is vacuous. At p=0 the argument still applies. The proofs allow paths outside the cone because any path between its inside and outside must cross its full edge boundary.

checks.py enumerates the two boundaries of a b=2 finite rooted grandparent tree, verifies their sizes and disjointness, checks separation after closure, and enumerates all 256 states of their union at p=1/2, verifying joint probability q^2 exactly. It checks the geometric-series upper bound using fractions and independently enumerates all descendant-network configurations at depths 0,1,2, obtaining respectively 1/2,23/32,6511/8192, agreeing with the recursion. These are finite sanity checks only. WeightedContact.lean formalizes the finite weighted-cardinality inequality and positivity of the separator probability, importing only two Mathlib modules; it contains no sorry or native_decide. Lean completed with exit code 0 and no diagnostics; LEAN_CHECK.md records the invocation and scope. The infinite probabilistic argument remains a written proof, not a Lean-verified theorem.

## Remaining gap

The user-requested second attempt is recorded in SECOND_ATTEMPT.md. Its strongest refinement proves that a finite two-point bubble diagram suffices for full finite-radius repulsion, a finite expected rooted-pair contact count, and an O(1/N) tail. It also proves a quantitative bounded-connection-operator continuity criterion and verifies with Hutchcroft's theorem that every nonunimodular transitive graph has repulsion throughout p<p_t (a nonempty interval beyond p_c), more generally at all finite-bubble parameters. Its remaining obstruction is at nonunique parameters with an infinite bubble diagram that also lie in the countable set of two-point right jumps. The original grandparent proof remains useful precisely because it handles parameters beyond these sufficient criteria.

No proof or counterexample to C0159 for arbitrary transitive graphs is obtained. Theorem 6.1 proves its full finite-radius assertion on the grandparent graphs, and Proposition 5.1 reduces possible general failures to a countable set of two-point right-discontinuities. No argument eliminates that set on arbitrary nonunimodular graphs. Outside the grandparent special case, even at distance one, infinite light contact sets with weights tending to zero are not ruled out, whether between light clusters or between heavy clusters. The heavy-cluster theorem still supplies no finiteness conclusion at arbitrary radii. No numerical calculation or Lean check is presented as resolving these gaps.
