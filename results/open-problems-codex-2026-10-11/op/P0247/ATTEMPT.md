# P0247: fixed-start final discovery

Date: 2026-10-12. Source verification and literature search pending.

## Statement being investigated

For every sequence of finite connected undirected simple vertex-transitive graphs G_n with |V(G_n)| tending to infinity, and any initial vertices x_n, does the law of the last first-visited vertex L_n of simple random walk have total-variation distance tending to zero from the uniform law on V(G_n)? Connectedness is required for L_n to exist; the source's precise formulation will be checked separately. Periodicity does not prevent eventual coverage. The initial vertex counts as visited at time zero.

## Proposition 1: the final-discovery kernel is doubly stochastic

For a finite connected vertex-transitive graph with N >= 2, let K(x,y)=P_x(L=y). Then K is stochastic, K(x,x)=0, and K(gx,gy)=K(x,y) for every graph automorphism g. In particular every column has sum one and a uniform initial vertex gives an exactly uniform L.

Proof. Finite irreducibility implies that each vertex is hit almost surely: from every vertex a given target can be reached in at most N-1 steps with probability bounded below by a positive constant, so successive blocks imply a geometric bound on avoiding that target. A finite union gives finite coverage almost surely. Exactly one vertex is discovered last, so the rows sum to one. The initial vertex is already visited and cannot be last. An automorphism preserves transition probabilities, paths and first-visit order, giving equivariance. For y,z choose an automorphism g with gy=z. Substituting x=gu in the column sum gives sum_x K(x,z)=sum_u K(gu,gy)=sum_u K(u,y). All columns have the same sum; the total sum of all entries is N, so each column sums to one. Multiplying K by the uniform row vector proves the assertion. QED.

Limitation: equivariance and double stochasticity alone do not imply small row total variation. Even adding zero diagonal does not suffice: on an even cycle, the permutation kernel that deterministically sends x to its antipode is equivariant, has zero diagonal, and has row total variation 1-1/N. This is NOT the walk's last-discovery kernel and NOT a counterexample to P0247.

## Proposition 2: exact law on cycles

For simple random walk on C_N, N >= 3, started at x, K(x,x)=0 and K(x,y)=1/(N-1) for every y != x. Thus total variation from uniform equals 1/N.

Proof. Fix y != x and cut the cycle at y. Up to the first hit of y, the walk is the symmetric nearest-neighbor walk on the integers {0,...,N}, stopped at 0 or N, with both endpoints representing y and the distinct other cycle vertices represented by 1,...,N-1. The starting coordinate is a in this interior. Let sigma be the first visit to {1,N-1}; sigma is finite and precedes any endpoint hit. This includes sigma=0 if a is already one of these vertices. To discover all other vertices before y is precisely to visit both 1 and N-1 before the first endpoint hit: a nearest-neighbor path visiting both traverses every interior integer, and coverage of the interior necessarily visits both.

If X_sigma=1, the required remaining event is to hit N-1 before 0, which has probability 1/(N-1). Indeed, for the walk on {0,...,N-1}, the hitting probability h(i) solves h(0)=0, h(N-1)=1 and 2h(i)=h(i-1)+h(i+1). Its successive differences are constant, so h(i)=i/(N-1). The stopping time is almost surely finite by the same finite-block argument used above, justifying these boundary equations; uniqueness follows by a maximum principle or the difference recurrence. The probability from N-1 to reach 1 before N is also 1/(N-1), by reflection. The strong Markov property at sigma and the fact that its two possible values exhaust probability one now give P_x(y is last)=1/(N-1). In particular the case N=3 is included: the two interior vertices are adjacent and distinct. Finally total variation is
  (1/2)[1/N+(N-1)(1/(N-1)-1/N)]=1/N.
QED.

## Proposition 3: graphs with a transitive point stabilizer

If the subgroup fixing x acts transitively on V minus {x}, equivariance implies K(x,y)=1/(N-1) for y != x. Proof: all those values are equal, their sum is one, and K(x,x)=0. This includes complete graphs. Its total variation is 1/N by Proposition 2's arithmetic. QED.

## Referee audit so far

- All proofs concern finite connected undirected simple graphs and ordinary discrete-time simple random walk. No mixing argument is used, so bipartiteness causes no issue.
- The cycle cut uses two copies of the TARGET, not two copies of the starting vertex.
- On the cycle, visiting the two interior extremes really covers all interior vertices, by nearest-neighbor steps. This equivalence fails on general graphs.
- Double stochasticity does not solve the fixed-start question, even with a zero diagonal and automorphism equivariance.
- No numerical evidence or literature status is asserted before inspecting the corresponding outputs.

## Proposition 4: a finite mixing/discovery bound

Let G be any connected undirected simple vertex-transitive graph with N >= 2 vertices and degree d. Let P be its ordinary simple-random-walk matrix, Q=(I+P)/2 its lazy matrix, and K its last-discovery kernel. For t a nonnegative integer, set D_x(t)=TV(Q^t(x,.),uniform). Then

  TV(K(x,.),uniform) <= D_x(t) + sum_{r=1}^t b_r
                         <= D_x(t) + t/d,

where b_r=sum_z Q^r(u,z)K(z,u), independent of u. In fact the last bound can use (t-1+2^(-t))/d when t>=1.

Proof. Laziness leaves the distribution of the sequence of genuine moves unchanged. In a finite graph, infinitely many genuine moves occur almost surely (independent Bernoulli choices), so K is also the last-discovery kernel of Q. Let (X_s) be a lazy walk started at x. On the same infinite path let L be the last-discovery vertex counting from time zero, and let Z be the last-discovery vertex of the suffix (X_t,X_{t+1},...). Both are well-defined by finite irreducibility. If Z does not occur in the prefix {X_0,...,X_t}, then Z is first visited by the full walk at exactly its suffix first-visit time, later than the first visit of every other vertex. Consequently L=Z on that event. This statement remains valid if full coverage happened before t: then Z necessarily belongs to the prefix and the implication has an empty antecedent. The coupling inequality and union bound give

  TV(law(L),law(Z)) <= P(Z in {X_0,...,X_t})
                       <= sum_{s=0}^t P(Z=X_s).

For any u, condition on X_s=u. The Markov property at s and t gives

  P(Z=X_s | X_s=u) = sum_z Q^(t-s)(u,z) K(z,u).

Conditional probabilities here are needed only for u with positive probability; the displayed right-hand side is defined for every u. Both Q and K are automorphism-equivariant, so the function u -> sum_z Q^r(u,z)K(z,u) is constant by transitivity: if g maps u to v, substituting z=gw gives precisely the same sum. Call it b_r. Therefore P(Z=X_s)=b_(t-s), for EVERY initial x. Also b_0=K(u,u)=0. Hence the union bound is sum_{r=1}^t b_r.

The suffix law is Q^t(x,.)K. Because uniform K=uniform by Proposition 1, the contraction of total variation under a stochastic kernel gives TV(law(Z),uniform)<=D_x(t). For completeness, if a,b are two probability row vectors, sum_y |sum_z(a_z-b_z)K(z,y)| <= sum_z |a_z-b_z| sum_y K(z,y)=sum_z |a_z-b_z|, proving contraction directly. The triangle inequality proves the first bound.

It remains to bound b_r. For k>=1, every entry of P^k is at most 1/d: this is true for P, and induction uses P^(k+1)(u,z)=sum_w P^k(u,w)P(w,z)<= (1/d)sum_w P(w,z)=1/d. The column sum of P is one because G is d-regular. Expanding Q^r=2^(-r)sum_{k=0}^r binom(r,k)P^k, for u!=z the k=0 term is zero, whence Q^r(u,z)<=(1-2^(-r))/d. The diagonal term contributes nothing to b_r, since K(u,u)=0. Proposition 1 gives sum_z K(z,u)=1, so b_r <= (1-2^(-r))/d. Summing and using sum_{r=1}^t 2^(-r)=1-2^(-t) proves the asserted bounds. For t=0 the empty sum is zero and the first inequality is just TV(K(x,.),uniform)<=TV(delta_x,uniform), also established by contraction. QED.

Corollary. For a graph sequence with degrees d_n, if there are integer times t_n with t_n/d_n -> 0 and D_(x_n)(t_n) -> 0, fixed-start asymptotic uniformity holds. This is a sufficient condition, not a consequence of vertex-transitivity alone.

Example corollary. If the lazy spectral gaps are bounded below by a positive constant and d_n/log N_n -> infinity, the sufficient condition holds. Indeed Q is real symmetric, all its eigenvalues are nonnegative, and its constant eigenvector has eigenvalue one. If all other eigenvalues are at most lambda<1, the Euclidean norm of delta_x Q^t - uniform is at most lambda^t sqrt(1-1/N), by expansion in an orthonormal eigenbasis. Cauchy-Schwarz gives D_x(t)<=sqrt(N)lambda^t/2. Taking t=ceil(log(N)/(-log lambda)) makes this at most 1/(2sqrt(N)), while t/d ->0. If lambda=0 take t=1 instead. QED.

Referee checks of Proposition 4: no independence is assumed between the prefix and Z; their overlap is handled by an explicit conditional computation. K is not assumed symmetric. The column sum is essential in the degree estimate. Ordinary discrete-time mixing is deliberately replaced by lazy mixing, while discovery order is unchanged. The bound can be useless for cycles (mixing order N^2 with d=2), and it does not resolve bounded-degree expander families.

## Finite computations completed

`compute.py` computes the entire finite-state discovery recursion, rather than estimating it by Monte Carlo. For each nonempty visited set S, with current vertex x in S, store F_S(x,y), the probability that y will be last. If |S|=N-1 this is the unit mass on the one unvisited vertex. Otherwise the one-step equation is
  (I-P_SS)F_S = R_S,
  R_S(x,.) = sum_{z notin S} P(x,z)F_(S union {z})(z,.).
The matrix is invertible: the killed walk leaves every proper S almost surely with a finite-block geometric tail, so its Neumann series converges. Processing visited sets by decreasing size supplies all right-hand sides. The initial law is F_{ {0} }(0,.). Computations use NumPy double precision; small residuals certify numerical consistency, not exact rational identities or the general conjecture. Peak array storage for these N<=10 jobs is far below 1 GB.

Results saved incrementally in `computations.json`: C_3 through C_10; K_4,K_6,K_8,K_10; K_(m,m) for m=2,...,5; circulants on 6,8,10 vertices with steps +/-1,+/-2; the 3-cube; prisms C_m square K_2 for m=3,4,5. Across 23 graphs the maximum linear-system residual is approximately 2.22e-16 and the maximum row-sum error approximately 1.33e-15. Cycle formula errors are at most 1.12e-16.

The laws need NOT be uniform off the start. On C_10 with steps +/-1,+/-2, the last probability at a neighbor is approximately .09497571694 (less than the uniform .1), at the antipode approximately .12661769023, and TV approximately .11004856611, exceeding the unavoidable 1/N=.1. On the ten-vertex pentagonal prism, TV is approximately .11393680960. These are finite numerical deviations, not asymptotic counterexamples.

`check_bound.py` separately checks automorphism invariance of b_r, its entrywise degree bound, the first mixing bound and stochastic contraction on cycles, circulants and the cube for t=1,...,20: 240 parameter pairs pass, with maximum invariance discrepancy 5.56e-17. These checks use the numerically computed K, with translation/XOR to obtain all rows; no unproved symmetry under pair swapping is used.

`product_search.py` computed eight further examples through 12 vertices. A thickened cycle means C_m[empty graph on k vertices], with complete bipartite connections between adjacent fibres; a Cartesian example means C_m square K_k, with matching horizontal edges and complete internal fibres. They are connected vertex-transitive simple graphs by translations and fibre permutations (thickened case), or by translations and a common fibre permutation (Cartesian case). On the thickened C_6 with two vertices per fibre, TV is approximately .090555898 versus 1/12=.083333333. On C_4 square K_3 it is approximately .094038119; on C_6 square K_2 approximately .110840256. No asymptotic extrapolation is justified from this data.

One potentially difficult regime is C_m square K_k with m and k both growing: changing the cycle coordinate is rare when k is large, and the degree-only mixing corollary is often ineffective. This is a candidate for further analysis, not a counterexample or a claim of persistent bias. Turning a local-time heuristic into an asymptotic law of the final discovery would require uniform coupon-collection estimates within fibres and a rigorously derived limit; none is supplied here.

The Lean file `FiniteChecks.lean` concerns only the rational arithmetic in the uniform-except-start TV calculation and its N=3 instance. It does not formalize either stochastic proof. `lake env lean` from ~/lean_verify finished with exit code 0; its captured output is `lean_check.txt`. Only a stylistic unnecessary-sequence-focus warning was emitted. There is no `sorry` or `native_decide` in the submitted file. Both stated arithmetic theorems are kernel-checked; no claim of formal verification of the probabilistic arguments is made.

## Remaining gap

No bound tending to zero is proved for arbitrary growing connected vertex-transitive graphs, and no counterexample is established. Proposition 4 resolves sequences admitting lazy mixing times o(degree), but does not establish that condition generally. The cycle argument covers a separate slow-mixing family. General bounded-degree families, arbitrary Cartesian products and intermediate regimes remain outside these arguments.

## Final hostile-referee assessment (2026-10-12)

The results labeled proved above have complete arguments. The general conjecture has neither a proof nor a counterexample in this attempt. No novelty or exhaustive literature-status certification is claimed.

The primary-source check of Berestycki–Hermon–Teyssier is a specific warning against a false closure: their Theorem 4.8, p.39, concerns the last k uncovered points under STATIONARY initialization. Its k=1 conclusion is already exact by symmetry and cannot be used as a fixed-start solution. Their Theorem 1.2, p.4, covers fixed-start uncovered sets at deterministic times in an additional geometric regime; translating it into a stopped final-discovery law requires another argument. No such implication is asserted here. OpenAlex citation traversal and Semantic Scholar searches remain unavailable because of HTTP 429, so the bounded literature search cannot establish current open status.

N=2 boundary check of Proposition 4: the graph is a single edge with d=1, K swaps its two vertices, and TV(K_x,uniform)=1/2. At t=1 the lazy distribution is exactly uniform and b_1=1/2, giving equality in the refined bound D_x(1)+(1-1/2)/d. This independently checks the initial-vertex convention, omission of b_0, and the laziness factor. The t=0 case is separately included in the proof.

The remaining concrete research direction is to analyze final discovery on Cartesian products C_m square K_k with both m and k growing, or to find a discovery-specific estimate controlling sum b_r on arbitrary transitive graphs. This is future work, not a result or a counterexample.
