from pathlib import Path
s=r'''

## 1. A fully proved fixed-round quenched special case

Let d>=3, 2<=r<=d, and t>=0 be fixed integers. (For E0089, r=d-k+1>=3.) Independently mark vertices vacant with probability q_n, where q_n->q in (0,1) is deterministic. On a graph G delete in each round every currently vacant vertex with fewer than r currently vacant neighbours. Let Y_v(t) be its vacancy indicator after t rounds, and H_t=sum_v Y_v(t). Let h_t(q) be the survival probability of the root after t rounds on the infinite d-regular tree.

**Theorem A (fixed-round quenched CLT and replica factorization).** On a uniform simple d-regular graph G_n, for fixed t, there is a deterministic sigma_t(q)^2>0 such that

  P((H_t-n h_t(q_n))/sqrt(n)<=a | G_n)
    -> Phi(a/sigma_t(q)) in probability over G_n,

for every real a. For two independently seeded processes on the same G_n, their two normalized counts converge jointly to independent N(0,sigma_t(q)^2) variables. In particular the graph variance of each conditional distribution function tends to zero. Also

  Var_G(E(H_t|G))=O_{d,t}(1),
  Cov(H_t,H'_t)=O_{d,t}(1),

where the second covariance is annealed and the seeds are independent given G. The constants are uniform in q_n. This theorem permits q_n=1-p0_n in the critical window. It is not a theorem about FINAL core emptiness.

Here are complete proofs, including the ingredients often hidden in a local-CLT appeal.

### 1.1 Bounded moments of the number of non-tree balls

For a fixed radius L let B_L(G) count vertices whose induced radius-L neighbourhood is not a tree, and put S_L=1+d sum_{j=0}^{L-1}(d-1)^j. A breadth-first tree plus one extra edge in such a ball yields a simple cycle of length at most 2L+1, and the centre is within distance L of that cycle. Consequently

  B_L <= S_L sum_{ell=3}^{2L+1} ell C_ell,                (A1)

where C_ell is the number of simple ell-cycles. Empty sums are zero (L=0).

For completeness, E(C_ell C_j)=O_{d,ell,j}(1) can be proved directly in the configuration model. The union of two specified cycles, allowing all possible identifications of vertices and edges, has finitely many possible graph types U, with v vertices and e edges. Every vertex of U has degree at least 2, so e>=v. The number of embeddings into n labelled vertices is at most n^v, choices of distinct half-edges for the embedded edges are at most d^(2e), and the probability that the e specified disjoint half-edge pairs occur in the uniform pairing is

  [(nd-1)(nd-3)...(nd-(2e-1))]^-1 = O_{d,e}(n^-e).

If a half-edge choice is inconsistent its probability is zero, so overcounting does no harm. Summing these finitely many O(n^(v-e)) bounds proves the assertion, including identical cycles and overlapping cycles. Loops/parallel edges do not enter the simple-cycle count. For fixed d, the configuration pairing is simple with probability tending to exp(-(d^2-1)/4)>0; conditional on simplicity its graph is uniform simple d-regular. The positivity needed here is the standard simplicity theorem (verified source: Janson, The probability that a random multigraph is simple, fetched PDF). Dividing by this positive probability transfers the upper moment bounds. Equation (A1), Cauchy-Schwarz, and the finite number of lengths therefore give

  E_G B_L^2=O_{d,L}(1).                                 (A2)

This is a fixed-L assertion. No uniform-in-growing-L version is being assumed.

### 1.2 Universal conditional mean and variance

Y_v(t) is a deterministic function only of vacancy bits in the radius-t ball: induction on rounds proves this, because at each new round only the previous status of v and its neighbours is consulted. If that ball is a tree, the function has exactly the same distribution as the root function on the d-regular tree. Since 0<=Y_v<=1,

  |E(H_t|G)-n h_t(q_n)| <= B_t(G).                       (A3)

Its graph variance is bounded by E B_t^2 (variance is at most mean-square error about any constant), proving the O(1) assertion.

Two vertex functions are independent given G when their centres have distance greater than 2t, because they use disjoint sets of independent bits. For centres at tree distance s<=2t let c_{t,s}(q) be their covariance in the infinite tree, and define

  sigma_t(q)^2 = c_{t,0}(q)
             + sum_{s=1}^{2t} d(d-1)^(s-1)c_{t,s}(q).     (A4)

Each covariance is a polynomial in q, hence continuous. If the radius-3t ball around v is a tree, it contains every radius-t ball around every w within distance 2t of v, and every sphere up to 2t has exactly d(d-1)^(s-1) vertices. The sum of covariances involving v is therefore exactly (A4). For any other v there are at most S_{2t} terms, each of absolute value at most 1; the universal expression is also bounded by S_{2t}. Summing proves

  |Var(H_t|G)-n sigma_t(q_n)^2| <= 2 S_{2t} B_{3t}(G).     (A5)

Thus conditional variance/n converges in probability to sigma_t(q)^2.

Positivity is not being inferred from a formal Gaussian approximation. Expand H_t in the orthonormal biased product basis of vacancy bits. It is increasing in each vacancy bit. If all other bits in the radius-t ball of v are vacant, setting the v-bit to vacant ensures that v survives every one of these t rounds; setting it nonvacant makes its survival indicator zero. Hence the influence of the v-bit on Y_v(t), and therefore its nonnegative influence on H_t, is at least q_n^(S_t-1). Its degree-one coefficient is at least sqrt(q_n(1-q_n)) q_n^(S_t-1). Parseval gives

  Var(H_t|G) >= n q_n(1-q_n) q_n^(2(S_t-1)).              (A6)

Combining with (A5) along typical graphs shows sigma_t(q)^2>=q(1-q)q^(2(S_t-1))>0. Notice that this lower bound can be extremely small for large fixed t; uniformity in t is not claimed.

### 1.3 Conditional CLT without importing an unverified theorem

Fix a graph and centre each variable W_v=Y_v(t)-E(Y_v(t)|G). They have absolute value at most 1. The graph on centres joining pairs at distance <=2t (including equality for repeated indices) is a dependency graph, with at most D=S_{2t} choices within any centre's dependence range. For each fixed moment order m, expand E[(sum_v W_v)^m|G] over ordered m-tuples of centres.

Connect positions in a tuple when their corresponding variables lie in dependence range. Components of positions involve independent groups of variables, by the disjoint-bit description. If a component has size one the term vanishes, because that factor is centred. For any connected block of b positions, the number of choices of their centres is at most n times a constant depending only on b and D: choose a spanning tree of that block, the first centre (n choices), and each other centre within dependence range of its parent (at most D choices). Thus a position graph with j components contributes O_{m,D}(n^j).

If m is odd, all nonzero tuples have at most (m-1)/2 components, and therefore their normalized moment is O(n^-1/2). If m=2j, terms having a component of size at least 3 have at most j-1 components, and contribute O(n^(j-1)). Remaining tuples have exactly j components of size two, whose expectation is the product of their pair covariances. Sum over the (2j-1)!! pairings of positions. For each fixed pairing, the unrestricted sum of products of pair covariances is Var(H_t|G)^j. Terms in this unrestricted sum with a link between two distinct pairs have at most j-1 connected components, so their absolute sum is O_{j,D}(n^(j-1)). If a pair itself is outside dependence range its covariance is zero. Removing the linked-pair terms therefore counts the remaining tuples exactly once, with their unique component pairing. We obtain

  E[(H_t-E(H_t|G))^(2j)|G]
      = (2j-1)!! Var(H_t|G)^j+O_{j,D}(n^(j-1)),          (A7)

uniformly over all graphs of maximum degree d. The odd-moment bound is uniform as well.

On graph sequences satisfying B_t/sqrt(n)->0 and B_{3t}/n->0, (A3), (A5), and (A7) give all Gaussian moments for (H_t-n h_t(q_n))/sqrt(n). The method of moments yields convergence in distribution: bounded higher even moments give uniform integrability and tightness, and the Gaussian moment sequence is determinate (its Carleman sum diverges). This proves the deterministic conditional CLT on every such sequence. By (A2), random regular graphs satisfy both conditions with probability tending to one. To justify the in-probability conclusion without an illicit exchange of quenched and annealed limits, suppose it failed and choose, from a subsequence of the positive-probability failure sets intersected with the structural good sets, deterministic graphs with B_t/sqrt(n)->0 and B_{3t}/n->0. The just-proved deterministic theorem contradicts failure of the conditional CDF convergence at the chosen a. Thus the quenched CDF assertion follows.

Conditional independence of the two seed sets now gives their joint conditional CDF as the product of their single conditional CDFs. Each converges in probability to a deterministic continuous Gaussian CDF and is bounded by 1, so the annealed joint CDF converges to the product as well. Bounded convergence in probability also gives convergence in L2 of a single conditional CDF, hence its graph variance tends to zero. Finally the law of total covariance gives Cov(H_t,H'_t)=Var_G(E(H_t|G)), establishing the second O(1) assertion. This completes the proof of Theorem A.

### 1.4 An exact cancellation for one round, and an explicit variance

For t=1 the conditional mean is universal on EVERY simple d-regular graph, even when a radius-1 ball has triangles:

  E(H_1|G)=n h_1(q),  h_1(q)=q P(Bin(d,q)>=r).             (A8)

Indeed only the d distinct neighbour bits and the root bit are used. Thus independent replicas satisfy Cov(H_1,H'_1)=0 exactly, for every graph distribution supported on simple d-regular graphs. This alone does not imply independence of their counts; Theorem A supplies the stronger asymptotic independence for random regular graphs.

Let A_j=P(Bin(d-1,q)>=j). On the infinite tree adjacent roots both survive with probability q^2 A_{r-1}^2: conditioning both roots vacant leaves d-1 independent neighbours on each side. Roots at distance two share exactly one middle vacancy bit. Conditioning it gives joint probability q^2[(1-q) A_r^2+q A_{r-1}^2]. Consequently

  sigma_1^2=h_1(1-h_1)
      +d[q^2 A_{r-1}^2-h_1^2]
      +d(d-1)q^3(1-q)[P(Bin(d-1,q)=r-1)]^2.             (A9)

The last simplification uses h_1=q[(1-q)A_r+q A_{r-1}] and expands the square. This is also a direct finite algebra check of the covariance argument.

## 2. Why fixed rounds do not close the original gap

At any fixed t and any q in (0,1), h_t(q)>0: all bits in the finite radius-t ball can be vacant with positive probability. The conditional variance is at most n S_{2t}, by the bounded dependency range. Equations (A2)-(A3) and Chebyshev therefore show P(H_t=0)->0 for q_n->q>0.

In particular take the deterministic annealed critical p0_n from ATTEMPT.md and q_n=1-p0_n->1-p*. The final complete-occupation indicator F has annealed probability exactly 1/2; the t-round complete-occupation indicator F_t=1_{H_t=0} satisfies F_t<=F and P(F_t=1)->0. Therefore

  E|F-F_t|=1/2-P(F_t=1)->1/2.                           (A10)

This rules out approximating the critical event in L1 by completion in ANY fixed number of rounds. It does not rule out some other observable of a finite-round process correlating with F.

For graph-specific q_G the same conclusion holds: q_G->p* in probability, while (A3) uniformly at the chosen vacancy density 1-q_G gives mean/n bounded away from zero on typical graphs; the variance bound is still valid. Then P(F_t=1)->0, whereas E(F|G)=1/2 exactly. Thus (A10) holds on that reading too. No independence of q_G from G has been assumed.
'''
p=Path('SECOND_ATTEMPT.md');p.write_text(p.read_text(encoding='utf8')+s,encoding='utf8')
