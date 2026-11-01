# E0089 second attempt — 2026-10-12

Remaining gap from ATTEMPT.md: establish a fixed-K quenched conditional-success bound, or equivalently a sufficient independent-two-initial-set factorization, for complete bootstrap occupation in the critical n^-1/2 window. The first attempt only proved an abstract sufficient criterion and threshold tightness.

Two genuinely new approaches:

A. **Finite-round core peeling, local weak convergence, and dependency-graph CLTs.** Replace final core emptiness by the number of vacant vertices after t fixed rounds. On tree neighbourhoods its conditional mean and covariance are universal local polynomials. Show that graph fluctuations of that conditional mean are O(1), while seed fluctuations have order sqrt(n); obtain actual quenched Gaussian limits and independent-replica factorization for this local statistic. Then ask whether t can grow enough to resolve the critical bottleneck. For d=4,k=2 compute the critical recursion and its relaxation rate exactly.

B. **Two-colour density-dependent exploration of the configuration model.** Run two independent seed/core processes on one pairing, track the joint type of each half-edge (degrees remaining in each process), and try to apply a multivariate martingale CLT at the common saddle-node. A zero cross-covariance theorem for the limiting exploration noises would imply the desired graph concentration. Unlike the first attempt this would construct the actual coupled exploration, rather than merely restating the replica identity. The difficulty is that adaptive discovery in one process changes the conditional pairing law seen by the other, and there is no verified theorem here identifying or cancelling that covariance.

Selected approach: A. It permits a full theorem for a stronger local special case, a precise algebraic test at the smallest admissible (d,k), and a rigorous assessment of the depth needed to bridge to final occupation. Approach B remains a separately identified lead, not an asserted result.

Math-store query on the gap: "quenched bootstrap percolation random regular graph independent replicas k-core concentration Janson Luczak". Returned no applicable theorem; local/dependency-graph methods will be checked independently. Results and exact requests will also be logged in LITERATURE.md.


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


## 3. Exact critical dynamics in the smallest target case d=4, k=2

Here r=d-k+1=3 and q denotes initial vacancy density (occupied density is 1-q). The core message recursion on the infinite 4-regular tree is

  x_0=q,
  x_{t+1}=q P(Bin(3,x_t)>=2)=q(3x_t^2-2x_t^3),
  h_0(q)=q,
  h_t(q)=q P(Bin(4,x_{t-1})>=3)
        =q(4x_{t-1}^3-3x_{t-1}^4), t>=1.               (B1)

Justification of the message recursion, including its relation to peeling. On any graph define directed messages b^0_{u->v}=Z_u and

  b^{j+1}_{u->v}=Z_u 1{sum_{w in N(u)\{v}} b^j_{w->u}>=r-1}.

They decrease in j. Let a^0_v=Z_v and a^j_v=Z_v 1{sum_{u in N(v)}b^{j-1}_{u->v}>=r} for j>=1. We prove a^j equals the true j-round vacancy indicator by induction. This is immediate at j=0,1. If v survives the true jth round, then it was initially vacant and has at least r neighbours u with a^{j-1}_u=1. For j>=2 the latter have r incoming messages at time j-2, so after excluding v they have at least r-1 and b^{j-1}_{u->v}=1. This gives a^j_v=1.

Conversely if a^j_v=1, then a^{j-1}_v=1 by monotonicity, and there are at least r neighbours u with b^{j-1}_{u->v}=1. For j=2, the initially vacant v supplies one extra support to each such u in addition to its r-1 other initially vacant neighbours, hence a^1_u=1. For j>=3, excluding u from v's at least r incoming messages at time j-1 leaves at least r-1 messages; by monotonicity they are also present at time j-3. Thus b^{j-2}_{v->u}=1. Together with the r-1 supports at time j-2 supplied by b^{j-1}_{u->v}=1, this gives a^{j-1}_u=1. In either case v has at least r true surviving neighbours at round j-1 and itself survived that round, so survives round j. This completes the induction. On the infinite tree the r-1 forward subtrees for a directed edge are independent, giving (B1).

The critical values are q*=8/9, x*=3/4, p*=1/9: q*(3x*^2-2x*^3)=x*, and the derivative in x is 1. Write z_t=x_t-x* at q=q*. Then z_0=5/36 and the following identity is exact:

  z_{t+1}=z_t-(4/3)z_t^2-(16/9)z_t^3.                  (B2)

Let a=4/3, b=16/9, alpha=36/5 and B=1152/569. For 0<z<=5/36,

  1-a z-b z^2 >= 569/729>0,
  a <= 1/[z(1-a z-b z^2)]-1/z
       = (a+b z)/(1-a z-b z^2) <= B.                   (B3)

The first inequality evaluates the decreasing quadratic at 5/36. For the last bound increase the numerator to a+b(5/36)=128/81 and decrease the denominator to 569/729, giving 1152/569. Therefore z_t stays positive, decreases, and telescoping (B3) proves

  1/(alpha+B t) <= z_t <= 1/(alpha+a t).                (B4)

Its limit is zero (a positive limit would force the decrement in (B2) to stay positive). The reciprocal increments in (B3) converge to a, so their averages converge to a; consequently

  t z_t -> 3/4,
  t^2 (x_t-x_{t+1}) -> 3/4.                            (B5)

The root-density expansion is also exact:

  h_t(q*)-21/32
    =(3/2)z_{t-1}-z_{t-1}^2-(40/9)z_{t-1}^3-(8/3)z_{t-1}^4.

Combined with (B5) it gives

  t[h_t(q*)-21/32] -> 9/8.                             (B6)

The asymptotic core density 21/32 is positive. This is fully compatible with finite random graphs having a critical probability of complete occupation of order one: a finite stochastic bottleneck decides which branch is reached after many rounds, and fixed-round limits do not commute with final stabilization.

### 3.1 The scale obstruction, stated precisely

For a perturbed vacancy density q=q*+eta, at x=x* the message-map drift is exactly

  T_q(x*)-x*=(27/32)eta.                                (B7)

More generally, the exact perturbation polynomial is

  T_{q*+eta}(x*+z)-(x*+z)
    =-(4/3)z^2-(16/9)z^3
      +eta[(27/32)+(9/8)z-(3/2)z^2-2z^3].              (B8)

In the n^-1/2 critical window, (B7) has scale n^-1/2. At criticality the residual deterministic message decrement is

  D_t=x_t-x_{t+1} >= (4/3)/(alpha+B t)^2.               (B9)

If one tries to approximate the saddle-node drift to error at most C n^-1/2 using the critical t-step tree recursion, (B9) forces

  t >= [sqrt((4/3)/C) n^(1/4)-alpha]/B.

This is a rigorous lower bound on the depth required by THAT drift-approximation strategy, not a claimed lower bound on the actual finite-graph stabilization time. Equivalently, for t=o(n^(1/4)) the critical deterministic residual dominates n^-1/2.

A tree radius-t ball in a d-regular graph has S_t vertices, so S_t<=n is necessary for any such ball to exist. For fixed d>=3 this forces t=O(log n). Thus the tree-ball conditional-mean argument underlying Theorem A cannot be applied at depths of order n^(1/4): none of those balls is a tree. No uniform-in-t extension of (A2), (A5), or (A7) has been invoked. We have identified a genuine limitation of the selected local approach, rather than incorrectly equating a fixed-round limit with the final event.

### 3.2 Checked and unproved portions

CriticalRecursion.lean checks the rational polynomial identities (B2), the root expansion, and (B8) by `ring`, plus the rational constants in (B3) by `decide +kernel`. It imports only Mathlib.Tactic.Ring. The command `lake env lean ~/brain_workers/TRIO_1011/op/E0089/CriticalRecursion.lean`, run from ~/lean_verify with a one-hour subprocess timeout, exited 0; second_lean_check.txt records the result. These are kernel-checked algebraic statements, not a Lean formalization of Theorem A or the asymptotic argument.

The inequalities, induction, and asymptotics (B3)-(B6) have complete handwritten proofs above. The exact identities were additionally evaluated in Python with rational arithmetic, and the recursion/bounds were checked numerically through 100000 iterations with 40-digit Decimal arithmetic; details are in second_experiments.py and second_experiments.json. Numerics do not replace the proof.


## 4. Pushing the local theorem to a growing number of rounds

The fixed-t proof admits a genuine uniform extension; this is stronger than the first local special case and still stops well before the critical bottleneck.

**Theorem B (slowly growing rounds).** Let d>=3 and 2<=r<=d be fixed. Let t=t_n>=0 satisfy

  (d-1)^{t_n}=o(log n),                                (C1)

and let deterministic vacancy densities q_n lie in a fixed compact interval [c,1-c], c>0. With h_t and sigma_t defined by the infinite-tree local statistics as above,

  P((H_t-n h_t(q_n))/sqrt(n sigma_t(q_n)^2)<=a | G_n)
       -> Phi(a) in probability over G_n.              (C2)

Independent replicas have independent standard Gaussian limits with this normalization. The graph variance of these conditional CDFs tends to zero. Furthermore

  Var_G(E(H_t|G)) <= n^{o(1)} = o(n).                        (C3)

Here n^{o(1)} means an upper bound, not an asserted asymptotic equality for a possibly zero variance. Complete occupation by t_n rounds has probability tending to zero, uniformly in q_n in the indicated compact interval. Thus in the critical setting the L1 discrepancy from final occupation still tends to 1/2, even at these growing depths.

Proof, with all uniformity checks. Condition (C1) implies t=O(log log n). The cycle counting proof in Section 1.1 can be made explicit for L=3t. For cycle lengths ell,j<=2L+1, their union is specified by identifications of ell+j cycle positions. There are at most (ell+j)^{ell+j} such identifications. Each consistent union has e>=v, e<=ell+j, at most n^v d^{2e} embeddings/half-edge choices, and specified-pair probability at most (2/(nd))^e for all large n, since e=O(L)=O(log log n). Its expected number is therefore at most (2d)^e. It follows that

  E(C_ell C_j) <= exp(O_d(L log(L+2))).

The O constant is uniform in ell,j,L in this range. Multiplying by S_L^2 and summing at most (2L+1)^2 weighted cycle pairs in (A1) preserves this form. Conditioning on simplicity divides by a probability bounded away from zero. Hence

  E B_{3t}^2 <= exp(O_d(t log(t+2)))=n^{o(1)}.           (C4)

For t=0 this is immediate separately. Equations (A3) and (C4) prove (C3). With probability tending to one B_{3t}<=n^{1/8}. Let D=S_{2t}; (C1) gives D=n^{o(1)} (indeed O((log n)^2)). The universal lower bound on sigma_t from (A6), obtained for every finite t and q in Section 1.2, is

  sigma_t(q_n)^2 >=q_n(1-q_n)q_n^{2(S_t-1)} >= exp(-O_c(S_t)).

Since S_t=O_d((d-1)^t)=o(log n), it follows that n sigma_t(q_n)^2>=n^{1-o(1)}. The same degree-one argument gives the unconditional-on-seeds lower bound Var(H_t|G)>=n^{1-o(1)} on every graph. Therefore (A3) and (A5), on the structural good set, imply respectively

  [E(H_t|G)-n h_t(q_n)]/sqrt(n sigma_t(q_n)^2)->0,
  Var(H_t|G)/[n sigma_t(q_n)^2]->1.                     (C5)

Indeed the numerators are bounded by n^{1/8} and 2D n^{1/8}, respectively, while the two denominators have orders at least n^{1/2-o(1)} and n^{1-o(1)}.

The moment proof in Section 1.3 is also uniform at these depths. For each fixed order m, counting spanning trees of the position components gives an upper bound C_m n^j D^m for tuples with j components; C_m depends only on m, not n,t or q. Odd normalized moments are bounded by

  C_m n^{(m-1)/2}D^m/[Var(H_t|G)]^{m/2}
       =n^{-1/2+o(1)}.

At order m=2j, the exceptional linked-pair and non-pair-component terms are at most C_m n^{j-1}D^m; divided by Var(H_t|G)^j they are n^{-1+o(1)}. Thus all conditional moments, normalized by their conditional variance, converge to the standard Gaussian moments uniformly on the structural good set. The same moment-determinacy and conditional sequence argument as before, followed by (C5), proves (C2). Conditional independence and bounded CDFs prove replica factorization and vanishing graph variance.

Finally, h_t(q_n)>=q_n^{S_t}>=n^{-o(1)} since the entire finite ball may be vacant. On the structural good set E(H_t|G)>=n^{1-o(1)}-n^{1/8}, while Var(H_t|G)<=nD=n^{1+o(1)} by bounded dependence. Chebyshev then gives P(H_t=0|G)<=n^{-1+o(1)} on this good set, and its complement has probability tending to zero by (C4). This proves the no-early-completion assertion. The same estimate works at graph-dependent vacancy density 1-q_G, since it is uniform for vacancy densities in a fixed compact interval and q_G lies in such an interval with probability tending to one. Final occupation is balanced at q_G, or annealed-balanced at p0_n, so the monotonicity identity E|F-F_t|=1/2-P(F_t=1) again proves the discrepancy limit. End proof.

Theorem B establishes an actual growing-round version of the replica concentration mechanism. It does not allow t of order n^(1/4), and it does not factorize final-success indicators. It sharpens, rather than closes, the remaining gap.


## 5. Upper-count conditioning: an actual replica theorem for the local surrogate

The source's phi_K conditions the INITIAL OCCUPIED COUNT, whereas Theorems A/B were first proved under product bits. Conditioning cannot simply preserve a dependency graph. We can nevertheless handle it by a joint Gaussian limit, instead of making that false independence assumption.

**Corollary C.** Keep Theorem B's assumptions, and fix K>=0 and a real a. Let M be the INITIAL VACANT count, and put

  U_n={M<nq_n-K sqrt(n)},
  T_n=(H_t-n h_t(q_n))/sqrt(n sigma_t(q_n)^2).

Then Q_G=P(T_n<=a | G,U_n) concentrates in graph probability around a deterministic sequence c_n(a). In particular Var_G Q_G->0, so for two independent initial sets sampled conditionally on G and U_n,

  P(T_n<=a,T'_n<=a)-P(T_n<=a)^2 -> 0.                  (D1)

This is the same conditional-count replica structure as the missing criterion, but with a LOCAL VACANCY COUNT CDF in place of FINAL SUCCESS. It does not prove the missing criterion for F.

Proof. Differentiation of a finite Bernoulli expectation gives the exact identity

  Cov(H_t,M|G)=q_n(1-q_n) d/dq E_q(H_t|G) at q=q_n.      (D2)

To see it, differentiation multiplies each configuration weight by [M-nq]/[q(1-q)], so the derivative is Cov(H_t,M)/[q(1-q)]. A local survival indicator is increasing in at most S_t bits, so its derivative lies between 0 and S_t. At vertices with tree balls that derivative is h'_t(q); other vertices change the derivative by at most 2S_t. Thus

  |d/dq E_q(H_t|G)-n h'_t(q)|<=2S_t B_t.               (D3)

For any finite t,q, the limit of conditional Cauchy-Schwarz on the typical graphs of Theorem A shows

  0<=rho_t(q):=sqrt(q(1-q)) h'_t(q)/sigma_t(q)<=1.       (D4)

This yields a valid deterministic Gaussian covariance parameter for every t, including the subsequently chosen t_n. There is no assumption of its convergence as t grows.

Apply the dependency-graph moment argument to fixed linear combinations of the two local variables (Y_v-EY_v)/sigma_t(q_n) and (Z_v-q_n)/sqrt(q_n(1-q_n)). Their per-vertex magnitudes are n^{o(1)} under (C1), and the dependency degree is still D=n^{o(1)}. The moment-counting errors gain at most n^{o(1)} factors, so after sqrt(n) normalization still vanish: odd orders have error n^{-1/2+o(1)}, and even non-pair terms n^{-1+o(1)}. By (C5), (D2), and (D3), the limiting covariance matrix along any subsequence on which rho_t(q_n)->rho is [[1,rho],[rho,1]]. A linear combination with limiting variance zero tends to zero by Chebyshev; combinations with positive limiting variance have the Gaussian moment limit. Cramer-Wold therefore gives the conditional joint Gaussian limit of

  (T_n, (M-nq_n)/sqrt(nq_n(1-q_n)))

along every such subsequence. Its centering errors vanish as in (C5). If q_n does not converge, additionally pass to a compactness subsequence q_n->q; all prior bounds were uniform on [c,1-c].

Let b_n=-K/sqrt(q_n(1-q_n)), and let (N_1,N_2) be standard Gaussians of correlation rho_t(q_n). Define

  c_n(a)=P(N_1<=a,N_2<b_n)/Phi(b_n).                   (D5)

The denominator is bounded away from zero uniformly in n. The actual denominator P(U_n|G) is deterministic in G, since M is binomial, and converges to Phi(b) on each compactness subsequence by the binomial CLT. Gaussian marginal distributions have no atoms, even if rho=1 and the joint distribution is degenerate; thus the rectangle boundary at T=a or M=b has probability zero. The joint conditional CLT gives Q_G-c_n(a)->0 in graph probability along every subsequence, hence for the full sequence (otherwise extract a contradicting compactness subsequence in q_n and rho_t(q_n)). The Gaussian rectangle probabilities in (D5) are continuous in q and rho, including rho=1, by representing N_1=rho N_2+sqrt(1-rho^2)N_0 and using the zero boundary probabilities.

Since Q_G,c_n(a) lie in [0,1], convergence in probability of their difference implies convergence in L2, and Var_G Q_G<=E[(Q_G-c_n(a))^2]->0. Conditional independence of the two U-conditioned seed sets gives (D1) by the same exact variance identity as ATTEMPT.md equation (5). End proof.

This proof explicitly conditions via a two-dimensional limit; it never treats the U-conditioned vertex bits as independent. At occupied density p_n=1-q_n, U_n is exactly the source's upper-count event |A|>np_n+K sqrt(n). The finite-time completion event H_t=0 still has probability tending to zero under this conditioning: divide its unconditioned probability by the binomial tail probability, which is bounded away from zero. At the critical density, final conditional success may instead be close to one for large K. The local surrogate's conditional replica concentration therefore cannot be substituted for concentration of final occupation.


The graph-specific median version of Corollary C also holds for the locally centred statistic. Define its conditional CDF to be zero on an impossible conditioning event; that exceptional event has probability tending to zero because the median density lies in a fixed compact interval with probability tending to one. To avoid a notation collision, let p_G be the occupied median called q_G in ATTEMPT.md, and q(G)=1-p_G be the vacancy density. Centre and normalize H_t using h_t(q(G)) and sigma_t(q(G)), and condition on M<nq(G)-K sqrt(n). The preceding moment estimates are uniform over q in any fixed compact interval, so they remain valid when q is chosen as a function of G. Their deterministic Gaussian approximation initially uses rho_t(q(G)) and b(q(G)). These parameters converge in graph probability to the deterministic parameters at q*=1-p*:

- ATTEMPT.md Proposition 1 gives q(G)-q*=O_P(n^-1/2).
- |h'_t|<=S_t, |h''_t|<=2S_t^2 follow by differentiating a Boolean expectation coordinate by coordinate. Each covariance in (A4) involves at most 2S_t bits, so its derivative is bounded by 4S_t; consequently |(sigma_t^2)'|<=4S_t S_{2t}.
- On the compact interval sigma_t^2>=exp(-O(S_t))=n^{-o(1)}. Differentiating rho_t=sqrt(q(1-q))h'_t/sigma_t therefore gives a uniform bound |rho'_t|<=n^{o(1)}. Hence rho_t(q(G))-rho_t(q*)=o_P(1); b(q(G))-b(q*)=o_P(1) as well.
- The Gaussian rectangle ratio in (D5) is uniformly continuous for rho in [0,1] and b in the compact interval dictated by c,K, because the denominator is bounded away from zero and both Gaussian marginals have continuous distributions even at rho=1.

Thus Q_G concentrates around (D5) evaluated at q*. This is a median-density local-surrogate analogue of the exact remaining replica criterion. The centre n h_t(q(G)) is explicitly graph-dependent; no claim of concentration around the uncorrected centre n h_t(q*) is made.


## 6. Numerical and finite checks, and a referee audit

All computations ran in seconds to minutes, with local arrays far below 1 GB. No empirical conclusion about final-success concentration is drawn.

- `second_finite_checks.py`: 12288 exact message/peeling equality checks (two 8-vertex 4-regular graphs, all 256 initial sets, r=2,3,4, eight rounds); 303 rational polynomial evaluations; 30 exact joint-survival calculations on adjacent or distance-two tree stars at d=3,4 and several rational densities. All passed. `second_finite_checks.json` records the counts.
- `CriticalRecursion.lean`: six kernel-checked algebraic/constant statements, no sorry and no native_decide; exit 0 in `second_lean_check.txt`. This does not formalize the CLTs.
- `second_experiments.py`: at q=8/9 the exact one-round tree mean is h_1=16384/19683 and tree variance per vertex sigma_1^2=147374080/387420489, approximately 0.38039826025. It sampled six simple 4-regular graphs at each n=64,256,1024 and 2048 independent seed configurations per graph. The sample variance/n ranges were [0.3402,0.4044], [0.3770,0.4029], [0.3493,0.3953]. These modest samples are consistent with the variance calculation, but are not claimed to verify asymptotic convergence.
- For the same 18 graphs, the TWO-round conditional mean was computed exactly, rather than estimated from seeds: enumerate all distinct initial vacancy bits used by each exceptional two-hop neighbourhood; use the tree value only when the forward branches have distinct vertices. Deviations from n h_2 were between -0.337111 and -0.114097. The tree h_2 is the exact fraction 4453232545890304/5559060566555523. This supports the O(1) common-graph mean-fluctuation mechanism, which is proved independently by (A2)-(A3).
- The critical recursion was checked through 100000 iterations with 40-digit Decimal arithmetic against BOTH explicit bounds in (B4). At t=100000, t z_t is approximately 0.749812, approaching the proved limit 3/4.
- `second_replica_example.py` and `check_joint_derivative.py`: exact enumeration checks universal one-round expected counts and (D2) for t=1 on both previous 8-vertex examples.

A useful finite warning for approach B: mix G=K_{4,4} and its 04,15 -> 01,45 switch H with equal probabilities, and take fixed occupied density p=1/4. Their final-success probabilities differ by

  [g_H(2)-g_G(2)]P(Bin(8,p)=2)=10p^2(1-p)^6=3645/32768.

Thus two independently seeded final-success indicators on this shared random graph have annealed covariance

  (3645/32768)^2/4=13286025/4294967296>0.

Yet the independently seeded one-round vacant counts have covariance exactly zero at the SAME vacancy density 3/4, by (A8) (their common mean is 8[4(3/4)^4-3(3/4)^5]=567/128). This demonstrates why neither seed independence conditional on G nor cancellation of local conditional means proves cancellation of final exploration fluctuations. It is a finite fixed-density example, not an asymptotic counterexample and not a graph-specific-median assertion.

Referee issues checked explicitly:

1. The target graph is SIMPLE and fixed-degree. Configuration cycle bounds are transferred only after invoking the verified positive simplicity theorem. No CLT from the configuration multigraph is silently transferred.
2. The process and message variables are distinguished. Their equality by rounds is proved in Section 3 and exhaustively checked on small graphs; the tree recursion uses independent forward branches only on the actual infinite tree.
3. Local dependence is conditional on the fixed graph and uses independent Bernoulli bits. It is NOT asserted for bits conditioned on the global count. Corollary C handles that conditioning by a joint limit, with its denominator bounded away from zero.
4. Graph mean error uses B_t, and variance error uses B_{3t}, not B_t. This larger radius is needed to contain both overlapping balls and is included in all cycle bounds.
5. All constants hidden in the moment argument are controlled when t grows: dependency degree D, per-variable magnitudes after normalization, and cycle-type counts are n^{o(1)} in the specified range. Odd and exceptional even moments vanish with explicit negative powers of n. No uniform theorem at t~n^(1/4) is claimed.
6. Positive variance has a direct degree-one lower bound. Gaussian normalization is not justified by numerical variance or an assumed nondegenerate limit.
7. Limits of paired counts use conditional independence PLUS a quenched distribution theorem. Vanishing covariance alone is not used to infer asymptotic independence.
8. In the graph-specific-median extension, the density is allowed to depend on G, but the moment bounds are uniform in that density; the statistic is centred at its OWN tree mean n h_t(1-p_G). The possible uncorrected random centre is not discarded.
9. Gaussian conditioning remains valid at a degenerate joint limit rho=1 because each marginal has a continuous distribution and the rectangle boundary has zero mass.
10. The fixed-K source observable is final success. The count-CDF replica theorem proves a different, explicitly specified observable; it is not called a solution to E0089.
11. The n^(1/4) result is about the critical TREE DRIFT approximation. It is not asserted as a theorem on finite-graph running time, nor a universal impossibility result.
12. No claim has been promoted from numerical evidence to proof. Lean only certifies the algebra listed in the artifact; all probabilistic claims have handwritten proofs and explicit assumptions.

Precise remaining gap after this second attempt: prove a quenched approximation/factorization for FINAL r-core emptiness in the n^-1/2 critical-density window, at a fixed upper-count cutoff K, such as ATTEMPT.md equation (6). The local conditional replica factorization in Corollary C applies up to (d-1)^t=o(log n), while even early completion at those depths differs from critical final occupation by probability tending to 1/2. A shared-pairing exploration theorem or another global reduction is still required. Approach B identifies the joint adaptive-exposure covariance that would have to be controlled, but no such cancellation is proved.

Final verdict of the second attempt: PARTIAL. Theorems A and B, Corollary C, and the exact critical-recursion bounds are additional proved special cases/reductions. E0089 itself remains unresolved here.
