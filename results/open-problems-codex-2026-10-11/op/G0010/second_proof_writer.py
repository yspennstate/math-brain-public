from pathlib import Path
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf-8');s+=r'''

## 12. Reproved deterministic input: nonbacktracking growth
Let G be a finite simple graph with n vertices, maximum degree Delta>=2 and adjacency spectral radius lambda. Put B=min(Delta-1,lambda^2/4)>0. For j>=1 let S_j(u,v) count nonbacktracking walks of length j from u to v, and S_0=I. Reversal shows S_j is symmetric; these matrices are entrywise nonnegative, and S_j<=A^j entrywise.

**Lemma 5.** Every row sum of S_j is at most 4 B^j for j>=1, and ||S_j||_{2->2}<=lambda^j.

**Proof of the spectral row bound.** Fix a host root v in a connected component with spectral radius lambda_v<=lambda. The component has a positive Perron vector x. Form the finite rooted tree of all nonbacktracking walks starting at v through depth j: an edge appends one allowed host edge, and the root is the empty walk. Its level-i population N_i is exactly the row sum of S_i at v. Give each tree vertex the positive weight x at its terminal host vertex. Every nonroot vertex has its parent plus its allowed child continuations; their host labels run through the full host neighbor set, except that continuations at the last level have been omitted. At the root the full neighbor set also appears. Thus the lifted vector y satisfies A_T y<=lambda_v y.

For every real vector f on this finite tree, use |f| and the inequality

    2 |f_u f_w| <= (y_w/y_u) f_u^2 + (y_u/y_w) f_w^2

on each edge. Summing gives |f^T A_T f|<=lambda_v ||f||_2^2. Hence ||A_T||_2<=lambda_v, with no assumption about boundedness of an eigenfunction on an infinite cover.

If N_j=0, the required row bound is immediate. Otherwise all N_i for 0<=i<=j are positive. Compress A_T to the orthonormal vectors N_i^{-1/2} 1_{level i}. The compression is the weighted adjacency matrix of a path with j edges, whose i-th weight is w_i=sqrt(N_{i+1}/N_i). Its norm, which is its positive top eigenvalue L, is at most lambda_v. Let a_i>0 be its Perron vector and define

    t_i=w_i a_{i+1}/(L a_i),  0<=i<j;
    t_j=0.

The first endpoint equation gives t_0=1. The interior Perron equations give 0<t_i<1 for 1<=i<j and

    w_i^2/L^2 = t_i(1-t_{i+1}).

Consequently

    N_j=product_{i=0}^{j-1} w_i^2
       =L^{2j} product_{i=1}^{j-1} t_i(1-t_i)
       <=L^{2j}/4^{j-1}
       <=4(lambda^2/4)^j.

The empty product handles j=1. The inequality t(1-t)<=1/4 follows from (t-1/2)^2>=0; all factors are nonnegative. Independently, maximum degree gives N_j<=Delta(Delta-1)^{j-1}<=2(Delta-1)^j. Combining these two bounds yields N_j<=4 B^j.

For the l2 norm, for every f we have |S_j f|<=A^j |f| entrywise. Monotonicity of the l2 norm and ||A^j||_2=lambda^j prove the assertion. This uses entrywise positivity, not an invalid implication of Loewner ordering. QED.

This lemma was already in the historical records; its proof here is verification and an input to the new operator/diagram argument, not a novelty claim. Its sharp weighted-path product core is checked separately in SpectralFlow.lean.

## 13. Two-point operator bounds by interpolation
Let T have entries tau(u,v)=P_p(u connected to v), with tau(u,u)=1. A union bound over simple open paths gives the entrywise inequality

    T <= sum_{j>=0} p^j S_j.

Although S_j counts some walks with repeated edges and vertices, only simple paths are used as witnesses in this union bound. Each such path is nonbacktracking and has j distinct edges, so its probability is p^j. The extra counted non-simple walks merely enlarge the numerical upper bound; no claim is made that their open probability is p^j.

Assume p lambda<1. The series on the right converges entrywise: S_j<=A^j and the usual adjacency Neumann series converges. For every real r>=2, Riesz-Thorin interpolation between l2 and linfinity, with Lemma 5, gives

    ||S_j||_{r->r} <= 4^{1-2/r}
                          [lambda^{2/r} B^{1-2/r}]^j,  j>=1.

For 1<r<=2, symmetry and duality give the same estimate with r replaced by r'=r/(r-1)>=2. These are operator norms on counting-measure finite l^r spaces. The finite-dimensional Riesz-Thorin theorem and ordinary Holder inequality are standard functional-analytic inputs; no transitivity or infinite-graph theorem is being assumed.

Fix an integer k>=2 and define

    rho_k=max{p lambda, (p lambda)^{2/k}(p B)^{1-2/k}}.

If rho_k<1, then for every r in [k/(k-1),k], the relevant exponent 2/max(r,r') lies in [2/k,1]. Its logarithmic geometric interpolation is at most the maximum of the two endpoint values, namely rho_k. The prefactor is at most 4. Positivity, the triangle inequality and the geometric sum therefore give

    ||T||_{r->r} <= 1+4 sum_{j>=1} rho_k^j
                  <= M_k:=4/(1-rho_k).

The first identity term is necessary. Entrywise domination controls operator norms here because |T f|<= (sum p^j S_j)|f| and the l^r norm is monotone on nonnegative vectors. No positive-semidefinite comparison is invoked. This argument also avoids the maximum-susceptibility-square loss.

## 14. Tree diagrams control all-terminal component moments
We use the standard finite-product van den Berg-Kesten (BK) inequality: for increasing events witnessed on disjoint edge sets, the probability of disjoint occurrence is at most the product of their probabilities. Its assumptions apply to independent Bernoulli bond edges. Ordinary intersection would have the wrong inequality. Iteration gives the same product upper bound for any finite list of increasing events with mutually edge-disjoint witnesses.

For k>=2 let D_k be the collection of unrooted abstract trees with k distinctly labeled terminal leaves and all other vertices trivalent, up to leaf-label-preserving isomorphism. They have k-2 branch vertices and 2k-3 edges. Their number is

    d_k=(2k-5)!!, with d_2=1.

Indeed, starting from the single two-leaf edge, attach each next labeled leaf by subdividing one of the 2k-3 edges of a k-leaf tree. Removing the new highest-labeled leaf and suppressing the resulting degree-two vertex is a unique inverse. This proves d_{k+1}=(2k-3)d_k.

For terminal host vertices v_1,...,v_k, which need NOT be distinct, the joint connectivity probability is at most the sum, over D in D_k and over assignments of its branch vertices to host vertices, of

    product_{ab in E(D)} tau(phi(a),phi(b)).

**Witness justification, including degeneracies.** If all terminals are connected, choose an open spanning tree of their component and its minimal subtree containing their distinct locations. Prune irrelevant leaves and suppress nonterminal degree-two vertices. If a terminal location is internal, attach a zero-length terminal edge carrying its label. If several labels share a location, attach each label as a separate zero-length leaf. Split each vertex of degree at least four into trivalent vertices at the same host location, linked by zero-length edges. Suppress remaining degree-two vertices. The result is an abstract tree in D_k; its positive-length host paths are edge-disjoint subpaths of the original spanning tree. Its zero-length connections are the certain event {u connected to u}, with the empty witness. Thus each abstract edge's connectivity event has an increasing, edge-disjoint open-edge witness. BK and a union bound prove the diagram inequality. Host vertices may coincide or be shared by path junctions; vertex-disjointness is neither required nor assumed.

Let

    F_k=E_p sum_{C component of G_p} |C|^k.

Expanding |C|^k as the number of ordered k-tuples of its vertices gives exactly F_k=sum_{v_1,...,v_k} P_p(all v_i connected), including repetitions. We now sum one diagram over ALL host labels.

**Lemma 6 (operator-to-diagram transfer).** If a symmetric nonnegative matrix T has ||T||_{r->r}<=M for every r in [k/(k-1),k], then the fully summed mass of each k-leaf binary tree diagram is at most n M^{2k-3}.

**Proof.** For k=2, its mass is 1^T T1<=||1||_2 ||T1||_2<=nM. For k>=3, root the abstract diagram at any trivalent branch vertex. A leaf message to its parent is T1, whose l^k norm is at most M n^{1/k}. A branch message with r_1 and r_2 descendant terminal leaves is T(f_1 f_2), where multiplication is pointwise. Put r=r_1+r_2. Every directed branch message contains at most k-1 leaves, so its exponent k/r is in [k/(k-1),k]. Holder gives

    ||f_1 f_2||_{k/r}
          <=||f_1||_{k/r_1} ||f_2||_{k/r_2},

since r_1/k+r_2/k=r/k. Applying T costs at most a factor M. Inductively, a message with r leaves and e diagram edges beneath and including its connection to its parent has norm at most M^e n^{r/k}. At the root, the three incident subtrees have positive leaf counts summing to k. Three-factor Holder with exponents k/r_i bounds their pointwise product's sum by the product of these norms. The n exponent is exactly one and the edge exponents sum to 2k-3. QED.

Combining the connectivity diagrams, Lemma 6, and Section 13 proves the finite-graph theorem

    F_k <= d_k n [4/(1-rho_k)]^{2k-3},  rho_k<1.      (12)

Hence for every L>0,

    P_p(L_1>=L) <= d_k n [4/(1-rho_k)]^{2k-3}/L^k. (13)

The simultaneous operator estimates at intermediate exponents are essential; a lone l^k bound would not justify the branch products.

## 15. New universal consequences
Keep 0<epsilon<1 fixed, p lambda<=1-epsilon, and B=min(Delta-1,lambda^2/4). If Delta<=1, largest components are at most two, so assume Delta>=2.

**Theorem 7 (larger critical wedge).** If p B<=1, put K=ceil(3 log n), which is at least two for n>=2. Then

    P_p(L_1 >= 8 e epsilon^{-2} K^3) <= n^{-2}.

**Proof.** For every integer k>=2,

    rho_k<=(1-epsilon)^{2/k}.

The concavity/tangent inequality x^a<=1+a(x-1) for x in [0,1] and 0<a<=1 gives 1-(1-epsilon)^{2/k}>=2epsilon/k. Thus M_k<=2k/epsilon. Also d_k<=(2k)^k and M_k>=1. Equation (12) gives

    F_k<=n [8 epsilon^{-2} k^3]^k.

Take k=K in (13), at the displayed size threshold, to get probability at most n e^{-K}<=n^{-2}. QED.

**Theorem 8 (larger strict-gap wedge).** If also p B<=1-eta for a fixed 0<eta<1, set zeta=min(epsilon,eta) and K=ceil(3 log n). Then

    P_p(L_1 >= 32 e zeta^{-2} K) <= n^{-2}.

**Proof.** Both geometric-interpolation endpoints have factors at most 1-zeta, hence rho_k<=1-zeta for every k>=2 and M_k<=4/zeta. Formula (12) gives F_k<=n [32 zeta^{-2} k]^k. Choosing k=K proves the bound as before. QED.

These results are source-valid all-host upper bounds under additional parameter inequalities; they do not identify all optimal scales. They strictly extend the first attempt's p(Delta-1) criterion. For example lambda=3, Delta=9 and p=1/5 satisfy p lambda=3/5, p(Delta-1)=8/5>1, but B=9/4 and p B=9/20<1. Such parameter triples are feasible, e.g. disjoint nine-leaf stars. The theorems apply uniformly to any host with the specified parameter inequalities, not just to this example.

A useful spectral-only corollary is that lambda<=4/(1-epsilon) implies the cubic logarithmic bound at all allowed p, because p B<=p lambda^2/4<=(1-epsilon)lambda/4<=1. A fixed strict gap below that radius threshold gives a logarithmic bound. This is stronger than merely restating the source's unspecified n^{1/2-delta} estimate for bounded radius.

**Sharpness of Theorem 7's logarithmic power.** The critical complete-tree lower bound from Sections 3–4 applies at p=1/b with fixed b sufficiently large for each epsilon. Here B=b cos^2(theta_h) and p B=cos^2(theta_h)<=1, so these trees are in Theorem 7's class. Their largest components are at least c_b (log n)^3 a.a.s. Therefore the exponent three cannot be improved uniformly in this enlarged critical wedge. The exact source-boundary resonance p_h likewise has p_h B=cos(theta_h)<=1 and is covered by Theorem 7. No claim of constant-factor optimality for every triple is made.

## 16. Penetrating the remaining fixed-gap regime
Equations (12)–(13) also apply when p B>1 provided rho_k<1 for some integer k>2. With fixed parameters and a fixed operator margin, they give

    L_1 <= O(n^{1/k} log n) a.a.s.,

or a finite-probability bound at a constant multiple of n^{1/k}. The logarithm here is a convenient diverging factor; a single kth moment does NOT establish a constant-factor O(n^{1/k}) a.a.s. statement.

For the source-boundary complete nine-ary trees with epsilon=1/5, Delta=10, lambda_h=6 cos(theta_h), p_h= (4/5)/lambda_h,

    B_h=9 cos^2(theta_h),
    p_h B_h=(6/5)cos(theta_h) ->6/5>1,
    rho_4=max(4/5,sqrt((24/25)cos(theta_h)))
          <=sqrt(24/25)<1.

The moment theorem therefore proves a uniform O(n_h^{1/4} log n_h) a.a.s. upper bound here, in a genuine fixed-gap branching-supercritical regime. The same formula gives a uniform fourth-moment upper bound for ALL finite hosts with lambda<=6 at epsilon=1/5, since p B<=lambda/5<=6/5 and rho_4<=sqrt(24/25).

This upper bound is NOT claimed tight. For the nine-ary tree the downward mean tends to 6/5, and the established transient lower exponent is log(6/5)/log(9)≈0.082978, much smaller than 1/4. The use of a universal l2 path-count bound lambda^j, rather than the smaller tree-specific scale, leaves a real loss. Arbitrary-host collisions and multiscale profiles are still not optimized.

If p B>1, write g=B/lambda>1. The largest real exponent admitted by this particular interpolation estimate is

    q_* = 2 log(g)/log(p B)>2.

Only integer k<q_* have been used in the tree-diagram proof. Noninteger transfer, any endpoint result, and a matching extremal lower family have not been proved. The full source gap is now explicitly: determine the tight worst-case scale in the effective branching-supercritical regime p min(Delta-1,lambda^2/4)>1, including the missing multiplicity/collision information that would remove the interpolation loss. This is a narrower remaining gap, not a solved source question.

## 17. Referee checks for the second attempt
- Historical sharp row bounds were reproved through finite covers, not assumed from a brain card. The lifted positive vector yields a finite quadratic-form inequality; no unjustified l2 conclusion from an infinite eigenfunction is used.
- Entrywise matrix comparisons are used only with absolute values and positive l^r norms. They are not Loewner comparisons.
- Only simple paths contribute probabilities p^j. Nonbacktracking walks with repeated edges enlarge a deterministic counting bound but are never assigned that open probability.
- The tree-graph construction covers ordered repeated terminals and internal terminal locations by empty witnesses. It uses edge-disjoint occurrence, not ordinary intersection or vertex-disjointness.
- At every internal message, the Holder exponent k/r lies in the operator interval. At the final root it becomes a summable l1 product; no l1 operator estimate is needed.
- The number of diagrams is (2k-5)!!, not an unaccounted constant depending exponentially on n. Its growth is included when optimizing k with n.
- The condition rho_k is a MAXIMUM of both interpolation endpoints. Omitting p lambda when B<lambda would be wrong.
- Constants for the cubic and logarithmic tail estimates are explicit. Critical-wedge sharpness refers to an extremal family, not every feasible parameter triple.
- In the fixed-gap polynomial regime, probability quantifiers are stated correctly; one kth moment alone gives tightness at n^{1/k}, and an added diverging factor gives a.a.s. control.
- Existing results remain intact. The full Question 5.2 remains unproved.
''';p.write_text(s,encoding='utf-8')
print('Full second-attempt proofs saved')
