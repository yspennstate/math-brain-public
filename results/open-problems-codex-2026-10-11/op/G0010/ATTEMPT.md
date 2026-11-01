# G0010 ? research record, 2026-10-12

## Exact target and present scope
For every finite simple undirected graph G, fixed 0<epsilon<1 and bond retention p <= (1-epsilon)/lambda(G), determine the tight typical worst-case largest-component upper bound as a function of n, Delta and lambda, across all regimes. The verified source Question 5.2 is on PDF/printed page 20. This record does NOT solve that full question.

## Latest result from the reopened attempt
The two-point-operator/BK diagram argument proves a universal cubic logarithmic upper bound under p min(Delta-1,lambda^2/4)<=1, a logarithmic bound under a fixed gap below one, and explicit higher-moment upper bounds in part of the complementary regime. An infinite family of exact triples, including (Delta,lambda,epsilon)=(10,6,1/3), has matching worst-case Theta((log n)^3) bounds for all large n. Full proofs are in Sections 12-20. The full source question remains PARTIAL.

## Result obtained: critical complete trees have cubic logarithmic extremes
Let b>=5 be a fixed integer, T_{b,h} the complete b-ary rooted tree of height h, n_h=(b^{h+1}-1)/(b-1), and epsilon_b=1-2/sqrt(b). Its spectral radius is lambda_h=2 sqrt(b) cos(pi/(h+2)), its maximum degree is b+1 for h>=2, and the source-boundary parameter is p_h=1/[b cos(pi/(h+2))]. We prove

    P(c_b h^3 <= L_1((T_{b,h})_{p_h}) <= C_b h^3) -> 1.

Equivalently the scale is Theta((log n_h)^3). This strengthens the prior recorded Omega((log n)^2) lower bound. Complete proofs and hostile checks are being saved below.


## 1. Spectral and percolation parameters
Throughout, a tree height counts edges. Put theta_h=pi/(h+2). The positive vector with value

    x_j = b^{-j/2} sin((j+1)theta_h)

on level j satisfies A x = 2 sqrt(b) cos(theta_h) x, including the two boundary equations (sin(0)=sin((h+2)theta_h)=0). It is strictly positive for 0<=j<=h, so its eigenvalue is the spectral radius: for example, conjugating A by the positive diagonal matrix with entries x makes every row sum equal that eigenvalue; the infinity operator norm then bounds every eigenvalue in modulus. This proves the exact formula without assuming that radial symmetry captures the top eigenvector.

For b>=5, epsilon_b=1-2/sqrt(b) lies in (0,1). For h>=2, p_h=1/[b cos(theta_h)] lies in (0,1) and satisfies p_h lambda_h=1-epsilon_b exactly. The critical parameter q=1/b is smaller than p_h and is also permitted by the source hypothesis.

## 2. A uniform binomial window lemma, proved without an asymptotic limit theorem
**Lemma 1.** Fix any integer b>=2. For every integer z>=64, let X have law Bin(bz,1/b). If integers a,l satisfy z<=a, a+l<=z+4 sqrt(z), and l=floor(sqrt(z)), then

    P(a<=X<=a+l) >= q_* := exp(-30)/8.

**Proof.** The variance is (1-1/b)z<=z. Chebyshev gives probability at least 3/4 to the interval |X-z|<2 sqrt(z). There are at most 4 sqrt(z)+2<=6 sqrt(z) integers in that interval. The binomial mode is z, since floor((bz+1)/b)=z. Thus P(X=z)>=1/[8 sqrt(z)].

For completeness, the mode formula here also follows directly from the mass ratios: P(X=z)/P(X=z-1)=1+1/((b-1)z)>1, while P(X=z+1)/P(X=z)=z/(z+1)<1, and successive mass ratios decrease with the index. Thus z is indeed the maximizing atom used in the Chebyshev argument.

For an integer r with 0<=r<=4 sqrt(z), the successive-mass ratio gives

    P(X=z+r)/P(X=z)
      = product_{i=1}^r [1-(i-1)/((b-1)z)]/[1+i/z].

Here (i-1)/((b-1)z)<=4/((b-1)sqrt(z))<=1/2. Use log(1-u)>=-2u for 0<=u<=1/2 and log(1+v)<=v for v>=0. The logarithm of the product is at least

    -[1+2/(b-1)] r(r+1)/(2z) >= -30,

because 1+2/(b-1)<=3 and r(r+1)<=16z+4 sqrt(z)<=20z. (For r=0 the empty product is 1.) All these masses are in the support: z+4 sqrt(z)<=bz for z>=64, b>=2. Each mass in the requested window is therefore at least exp(-30)/[8 sqrt(z)]. There are floor(sqrt(z))+1>=sqrt(z) masses, proving the lemma. The logarithmic inequalities follow by differentiating their two sides, so no local central limit theorem is needed. QED.

## 3. A rare critical process with cubic area
Let Z_0=1 and, given Z_j=z, let Z_{j+1} have law Bin(bz,1/b). Let S_H=sum_{j=0}^H Z_j.

**Lemma 2.** For each fixed b>=5 there is a_b>0 such that, for every integer H>=16,

    P(S_H>=H^3/8) >= a_b q_*^H.

**Proof.** The particular population path

    Z_0=...=Z_5=1, Z_6=3, Z_7=13, Z_8=64

has a strictly positive probability a_b. Every transition is feasible: 3<=b, 13<=3b, and 64<=13b for b>=5. Given any j>=8 and integer j^2<=z<=4j^2, set a=max(z,(j+1)^2), l=floor(sqrt(z)). Then

    0<=a-z<=2j+1<=3 sqrt(z),
    a+l<=z+4 sqrt(z),
    (j+1)^2<=a<=a+l<=4(j+1)^2.

For the last inequality, both z and (j+1)^2 are at most 4j^2, and l<=2j. Lemma 1 thus shows, uniformly over all states in the band, that the conditional probability of reaching the next band is at least q_*. Multiplying conditional probabilities, the event

    j^2<=Z_j<=4j^2 for every 8<=j<=H

has probability at least a_b q_*^{H-8}>=a_b q_*^H. On this event, sum over j=ceil(H/2),...,H: there are at least H/2 such terms and each is at least H^2/4. Hence S_H>=H^3/8. QED.

This event is deliberately rare: its probability is exponentially small in H. That cost is the point; the host has exponentially many independent launch subtrees. The typical critical surviving process has area of order H^2, which alone does not determine its largest component among those many trials.

## 4. Cubic lower bound for the tree's largest component
Let ell=log b and d_*=log(1/q_*). Choose the fixed positive fraction

    eta = ell/[2(ell+d_*)] < 1,
    H = floor(eta h).

At depth h-H of T_{b,h} there are M=b^{h-H} vertices. Their descendant subtrees of height H have disjoint edge sets. Under bond percolation at q=1/b, the descendant cluster of each root is exactly the process in Lemma 2 and these M trials are independent. Each success produces a connected set of at least H^3/8 vertices, regardless of the state of the edge to its parent. Consequently

    P_q(L_1 < H^3/8)
       <= (1-a_b q_*^H)^M
       <= exp(-a_b b^{h-H} q_*^H)
       <= exp(-a_b exp(h ell/2)) -> 0.

The last step uses H<=eta h. For large h, H>=eta h/2, so H^3/8>=eta^3 h^3/64. The event L_1>=K is increasing in retained edges, and p_h>=q, so the same bound holds at the source-boundary parameter p_h. Thus the lower constant c_b=eta^3/64 works. Merging two successful descendant sets through ancestors only increases the largest component; no closed-parent condition is needed for the lower bound.

## 5. A finite-depth generating-function lemma
**Lemma 3.** Let H>=80 be an integer, and let a branching process have offspring Bin(d,p) with d>=1 and 0<=p<=1, satisfying mu=dp<=1+10/H^2. Let S_k be its total population through generation k from one particle. For t=1/(128H^2),

    log E exp(t S_k) <= (k+1)/(64H^2),  0<=k<=H.

In particular log E exp(t S_H)<=1/(32H).

**Proof.** Write x_k=log E exp(t S_k). Independence of descendants gives the exact finite-depth recurrence

    x_0=t,
    x_{k+1}=t+d log(1+p(exp(x_k)-1)).

All x_k are nonnegative and finite, since finite-depth offspring are bounded. For 0<=x<=1, the exponential series gives exp(x)-1<=x+x^2: indeed the terms of degree at least two sum to at most x^2 sum_{m>=2}1/m! = (e-2)x^2 < x^2. Also log(1+u)<=u for u>=0. Since mu<=2, whenever x_k<=1,

    x_{k+1} <= t+x_k+10 x_k/H^2+2 x_k^2.

Induct on k. The initial inequality is immediate. If k<=H-1 and x_k<=(k+1)/(64H^2), then x_k<=1/(32H)<=1. Furthermore

    10 x_k/H^2 <= 10/(32H^3) <= 1/(256H^2),
    2 x_k^2 <= 1/(512H^2).

Together with t=4/(512H^2), the increment over x_k is at most 7/(512H^2)<=1/(64H^2), proving the induction. Finally (H+1)/(64H^2)<=1/(32H). QED.

The Lean file CriticalTree.lean isolates the polynomial increment inequality with r=1/H, rather than claiming to formalize independence or the whole percolation theorem.

## 6. Matching cubic upper bound at the source boundary
For h>=80, put x=pi/(h+2), so x^2<=1. From cos(x)>=1-x^2/2 and

    (1+x^2)(1-x^2/2)>=1,

we get sec(x)<=1+x^2. Hence

    b p_h=sec(theta_h)<=1+pi^2/(h+2)^2<=1+10/h^2.

Every descendant-root cluster through at most h generations is distributed as the branching process Bin(b,p_h) truncated at that depth, and is stochastically bounded by the height-h version. Lemma 3 and exponential Markov give, uniformly over all host vertices v,

    P(descendant cluster at v has size >=K)
        <= exp(1/(32h)-K/(128h^2)).

Each connected component of a rooted tree has a unique highest vertex. The whole component is precisely the open descendant cluster of that vertex: any other vertex of the component must be its descendant, since the unique path to a non-descendant would first visit an ancestor. Thus a union bound over the n_h possible highest vertices bounds L_1. Since n_h<=2b^h, choosing

    C_b=256(log b+1), K=C_b h^3

gives

    P(L_1>=C_b h^3)
       <=2 exp(1/(32h)+h log b-2h(log b+1)) ->0.

Together with Section 4 this proves the stated Theta(h^3)=Theta((log n_h)^3) result, including its probability quantifier and exact source-boundary parameter.

## 7. A universal critical-wedge upper bound
**Theorem 4 (partial answer for arbitrary hosts).** Let G be any finite simple graph on n>=2 vertices, with Delta>=2 and adjacency spectral radius lambda>0. Fix 0<epsilon<1, let p<=min(1,(1-epsilon)/lambda), and define

    a=-log(1-epsilon),
    H=max(80, ceil(3 log(n)/a)).

If p(Delta-1)<=1+10/H^2, then, for K=128H^2(3 log(n)+1),

    P(L_1(G_p)>=K) <= 2 n^{-2}.

In particular p(Delta-1)<=1 implies L_1=O_epsilon((log n)^3) a.a.s. The theorem includes a quantified vanishing supercritical window for maximum-degree branching. Its constants depend on epsilon only through H.

**Proof.** Let E be the event that there is an open simple path with H+1 edges. The number of oriented simple paths of that length is at most the total walk count 1^T A^{H+1}1. Because A is real symmetric, its Euclidean operator norm is lambda (the largest absolute eigenvalue equals its Perron eigenvalue), and therefore this count is at most n lambda^{H+1}. Every simple path has distinct edges and is open with probability p^{H+1}. The first moment bound gives

    P(E)<=n(p lambda)^{H+1}<=n exp(-a(H+1))<=n^{-2}.

Fix a vertex v. Breadth-first exploration, stopped at distance H from v, is stochastically bounded in total population by a process with root offspring Bin(Delta,p) and other offspring Bin(Delta-1,p). To see the domination, at the root there are at most Delta untested incident edges. Every discovered nonroot vertex has at most Delta-1 other edges after its discovering edge is removed; after all previously tested edges and previously discovered endpoints are omitted, there are even fewer candidates. Conditional on the exploration history, the remaining tested edges are independent Bernoulli(p). Complete each list of candidates to the appropriate degree with independent artificial Bernoulli trials and treat all successful trials as new distinct particles. Process particles in breadth-first order; ignored artificial particles get independent full offspring lists. This constructs the stated dominating finite-depth process. Each real edge is tested at most once; collisions suppress vertices and cannot invalidate the domination.

Let x=log E exp(t S_{H-1}) for the nonroot process, with t=1/(128H^2). Lemma 3 gives 0<=x<=1/(32H). The root process R_H has logarithmic MGF

    log E exp(t R_H)
       =t+Delta log(1+p(exp(x)-1))
       <=t+(p Delta)(exp(x)-1).

Since Delta>=2, p Delta<=2p(Delta-1)<=4, and x<=1, this is at most t+8x<=1/H. Therefore

    P(R_H>=K)<=exp(1/H-K/(128H^2)).

On E^c every vertex in C(v) is at graph distance at most H from v in the retained graph: a larger distance would supply a simple path with H+1 edges. Thus on E^c the breadth-first search truncated at H includes all of C(v). It follows that

    P(L_1>=K)<=P(E)+sum_v P(truncated search from v has size >=K)
       <=n^{-2}+n exp(1/H-3 log(n)-1)
       <=2n^{-2}.

No conditioning on E^c was inserted into the branching law: the last bound uses the unconditional truncated-search domination. This is essential for independence to remain valid. QED.

For Delta<=1 all components have size at most 2 deterministically, so those excluded degenerate cases need no probabilistic theorem.

**Sharpness within the critical wedge.** On T_{b,h}, at the allowed parameter p=1/b, p(Delta-1)=1. The lower bound of Section 4 still applies; the upper bound of Section 6 applies with mu=1, or Theorem 4 may be used directly. Thus the power three in the universal critical-wedge theorem cannot be replaced by a smaller power uniformly over its host class. This is a restricted-class sharpness statement, not the full answer to Question 5.2.

This sharpness holds for **every** fixed epsilon in (0,1): choose a fixed integer b>=5 with 2/sqrt(b)<=1-epsilon, and set p=1/b on T_{b,h}. Then p lambda_h=(2/sqrt(b))cos(theta_h)<=1-epsilon and p(Delta-1)=1. The constants of the lower example may depend on epsilon through b; this is permitted. The source-boundary parameter p_h in Sections 1–6 instead uses the particular epsilon_b and is proved separately.

### Relation to the source's near-regular prompt
If Delta<= (1+delta)lambda with fixed delta<epsilon/(1-epsilon), then p Delta<1 by a fixed gap and the ordinary maximum-degree branching argument gives O(log n). That easy strict-gap case is already available from standard branching. Theorem 4 addresses the equality/window of maximum-degree branching rather than solving arbitrary near-regular regimes. It should not be presented as a full resolution of the source's near-regular suggestion.

## 8. Hostile-referee checklist and remaining gap
1. The source question concerns all finite hosts: neither the complete-tree theorem nor Theorem 4 is presented as a complete solution.
2. Time scale and independence: lower trials use disjoint descendant edges and never require the original root to connect to a trial root. Upper domination uses unconditional exploration; conditioning on short diameter would be invalid.
3. Spectral normalization: lambda is the unnormalized adjacency spectral radius. The positive eigenvector checks the exact finite-tree spectral value, including both boundary levels.
4. Rare versus typical processes: H^3 is obtained from exponentially rare quadratic population growth multiplied by exponentially many trials; it is not inferred from typical surviving H^2 area.
5. Uniform window estimate: the binomial ratio proof controls every population in the band, not just its endpoints or an asymptotic Gaussian approximation.
6. Probabilities: constants b and epsilon_b are fixed while h tends to infinity; all p_h lie in [0,1] for h>=2. The lower bound extends by monotone coupling; its particular trajectory need not be increasing.
7. MGF induction: t is of order H^{-2}; the cumulative x is of order H^{-1}, and the quadratic error is accounted for at every step. The recurrence is exact before being bounded.
8. Small graphs: theorems are asymptotic for the tree; the finite universal estimate remains true even if its size threshold exceeds n. Delta<=1 is handled separately.
9. Formal scope: Lean checks only two algebraic steps. The written proofs supply the probability, graph, analytic and asymptotic arguments.

The remaining gap is a matching worst-case scale for arbitrary (n,Delta,lambda), particularly fixed-gap p(Delta-1)>1 and arbitrary multiscale degree/Perron profiles. The universal critical-wedge result and complete resonance family settle a boundary regime but not that gap. Nothing here refutes the source question, which asks for a characterization rather than proposing a formula.


## 9. Numerical validation record
The script checks.py completed successfully. Its raw structured results are numerical_checks.json. These calculations are diagnostic checks, not substitutes for the proofs.

- Checked 49,738 binomial windows for each b=5,9,25 (149,214 total): every integer population in j^2<=z<=4j^2 for 8<=j<=35, plus 120 evenly spaced populations per larger band through j=80. The minimum probabilities were approximately 0.0118322, 0.0159712 and 0.0194193, respectively, all above the proved uniform q_*=exp(-30)/8?1.1697e-14. The analytic estimate is intentionally conservative.
- Evaluated the exact logarithmic MGF recurrence for b=5,9,25 and h=80,160,320,640 at the actual source-boundary parameter. Every induction bound held; the maximum ratio of the computed x_k to its induction upper bound was 0.515644.
- Sparse symmetric eigenvalue computations on T_{5,2}, T_{5,4}, T_{9,3} agreed with the explicit spectral formula to absolute error below 1.8e-15.
- Jobs used small sparse matrices and short scalar recurrences, well below the 1 GB memory cap. No hour-scale numerical experiment or simulation was used.

The early Lean invocations failed due to a UTF-8 BOM and then a mistyped argument to mul_nonneg; those are checker-file errors, not asserted formal proofs. Only a successful subsequent run will be marked checked. A task-created Lean file was briefly created in the Lean working directory by mistake and moved into the requested problem folder before checking; no external pre-existing file was changed. All retained artifacts are in the problem folder.


## 10. Successful formal check and final scope
The final invocation of

    lake env lean ~/brain_workers/TRIO_1011/op/G0010/CriticalTree.lean

from ~/lean_verify returned exit code 0 and no errors on 2026-10-12. The shared Lean-slot mechanism serialized the checks. CriticalTree.lean imports Mathlib.Data.Real.Basic and Mathlib.Tactic.Linarith only. Both mgf_increment and next_band are checked by ordinary kernel-checked tactic proofs, with no sorry, axiom declarations, native_decide or whole-Mathlib import. The formalized scope is exactly the two algebraic lemmas; the rest of the result is the full written proof in Sections 1?7. No claim of a completely formalized percolation theorem is made.

Final verdict: PARTIAL. The two special-case theorems and their sharpness statements survived the checks above. The general source problem remains unresolved, and the literature search has the API limitations stated in LITERATURE.md.


## 11. Reopened attempt: two new approaches, 2026-10-12
The remaining gap is fixed-gap p(Delta-1)>1 under p lambda<=1-epsilon, with arbitrary multiscale degree/Perron profiles.

A first candidate, weighted-path spectral compression of BFS levels, was discarded when the saved historical reports showed that the same sharp product inequality had already been proved. It is not counted as a new approach or new progress.

New approach 1 (selected): use the two-point matrix tau_p(u,v)=P_p(u connected to v), its entrywise resolvent bound tau_p<=(I-pA)^{-1}, and interpolation between l2 and linfinity operator norms. Combine this with the BK tree-graph inequality for joint connectivity of k terminals. The target is a uniform bound on E sum_components |C|^k, rather than rootwise expected progeny. This may control exceptional-root multiplicity without introducing max susceptibility and its usual square loss. No such interpolation/diagram argument was used in the first attempt.

New approach 2: derive the full critical-to-supercritical crossover for percolation on complete finite trees using Galton-Watson martingale limits and bounded-offspring large deviations, allowing the drift bp-1 to vary with the height. This would test logarithmic corrections beyond the previous exactly critical resonance and distinguish a.a.s. constant bounds from tight-in-probability random martingale scales. This is a stronger special-case approach not pursued in the earlier attempt. It is less promising for an arbitrary-host upper bound, so approach 1 is selected.

Brain gap queries: math_recall.py "finite graph percolation maximum degree spectral radius supercritical branching transient resolvent", then "Hutchcroft two point operator L2 percolation cluster size moment tree graph inequality". Returned cards about the resolvent Neumann series, adjacency normalization, and draft two-point operator facts, but no matching finite-host theorem. They are hints only; no unverified card is used as a proof.

Selected-route candidate: for an integer k>=2, if

    theta_k=p lambda^{2/k} Delta^{1-2/k}<1,

then interpolation and positivity should bound tau_p on every l^r with k/(k-1)<=r<=k by M_k=1/(1-theta_k). A binary-tree diagram with k freely summed terminal labels should then have total mass at most n M_k^{2k-3}. The connectivity inequality would yield

    E sum_components |C|^k <= (2k-5)!! n M_k^{2k-3}.

This is a candidate until the treatment of repeated terminals, zero-length paths, all message exponents, and the BK inequality are checked fully.


### Selected-route progress (saved before final validation)
A stronger version uses the historical pointwise nonbacktracking growth inequality, but will reprove it rather than trust the earlier record. Write

    B=min(Delta-1,lambda^2/4),
    rho_k=max(p lambda, (p lambda)^{2/k}(p B)^{1-2/k}).

The nonbacktracking path-count matrices S_j are symmetric, entrywise bounded by A^j, and have row sums at most 4 B^j. Interpolation would therefore imply, if rho_k<1,

    ||tau_p||_{l^r -> l^r} <= 4/(1-rho_k),
    k/(k-1)<=r<=k.

Together with the binary-tree diagram estimate this gives a finite-graph kth component moment bound. In particular p B<=1 and p lambda<=1-epsilon should imply ||tau_p||_{l^k}<=2k/epsilon, yielding moment growth of order (C_epsilon k^3)^k and the universal largest-component upper bound O_epsilon((log n)^3). A fixed gap p B<=1-eta should give O_{epsilon,eta}(log n). This would extend the previous maximum-degree branching wedge to a spectral-effective branching wedge, including graphs with p(Delta-1)>1. The still-hard regime would narrow to p B>1.

Required checks before promoting this: prove the universal-cover spectral domination, prove the weighted-path product inequality, control every l^r exponent in the diagram recursion, and handle repeated terminal vertices without assuming vertex-disjointness.


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


## 18. Matching answer for an infinite family of exact parameter triples
**Corollary 9.** Fix an integer m>=3 and set

    Delta=m^2+1, lambda=2m, epsilon=1-2/m.

Among n-vertex finite graphs with these EXACT maximum-degree and spectral-radius values, at p=1/m^2 the optimal worst-case a.a.s. largest-component upper scale is Theta_m((log n)^3). The upper bound also holds for every p<=1/m^2.

**Proof.** The source parameter bound is p<=(1-epsilon)/lambda=(2/m)/(2m)=1/m^2. For every host with the displayed exact parameters,

    B=min(Delta-1,lambda^2/4)=m^2,
    p B<=1.

Theorem 7 gives the universal cubic logarithmic upper bound.

For the lower bound, put b=m^2 and take the disjoint union of T_{b,h} and the clique K_{2m+1}. The tree has maximum degree b+1 for h>=2 and radius 2m cos(pi/(h+2))<2m. The clique has degree and radius 2m, smaller degree than b+1. Thus their union has EXACT Delta=b+1 and EXACT lambda=2m. At p=1/b the tree is critical in its downward branching and Sections 3?4 give an Omega(h^3) largest component a.a.s. The clique adds a bounded number of vertices and cannot hurt the event.

To cover every sufficiently large n, choose h as the largest integer such that (b^{h+1}-1)/(b-1)+(2m+1)<=n, and pad the union with isolated vertices. This keeps both exact graph parameters and p unchanged. Since the next tree size is at most b times the current size plus a constant, h is asymptotic to log_b n; in particular h=Theta_m(log n). The lower bound therefore holds along all n, not just a subsequence. QED.

For m=3 this settles the worst-case scale at the exact fixed triple (Delta,lambda,epsilon)=(10,6,1/3). It is a matching special-case result, not a solution of Question 5.2 for all triples. The source imposes no connectedness hypothesis, so disjoint unions and padding are admissible.


## 19. A checked neighboring theorem gives an exponential confidence bound
Tom Hutchcroft, *Power-law bounds for critical long-range percolation below the upper-critical dimension*, arXiv:2008.11197v2 (2021), Theorem 2.2, PDF page 14, proves for every countable weighted graph and nonempty finite vertex set Lambda that

    P_beta(|K_max(Lambda)| >= alpha M_beta(Lambda)) <= exp(-alpha/9), alpha>=1,

where M_beta(Lambda)=min{integer j>=0: P_beta(|K_max(Lambda)|>=j)<=e^{-1}}. The same theorem gives a lower-tail estimate in terms of this quantile. It does not characterize the quantile from Delta and lambda and is not a solution in print to Question 5.2.

For our finite graph give every host edge weight one, set beta=-log(1-p), and choose Lambda=V(G). This reproduces exactly Bernoulli bond p; p<1 follows from p lambda<=1-epsilon and lambda>=1 for a nonempty host. Put

    Q_k=ceil([e d_k n M_k^{2k-3}]^{1/k}),

using rho_k<1 and M_k=4/(1-rho_k). Equation (13) proves P(L_1>=Q_k)<=e^{-1}, hence the quantile in Hutchcroft's theorem is at most Q_k. The event {L_1>=alpha Q_k} is a subset of {L_1>=alpha M_beta(V)}, and therefore

    P(L_1>=alpha Q_k) <= exp(-alpha/9), alpha>=1.

This is a proved confidence refinement of the new moment bound, using an explicitly verified published theorem with the same finite bond model. It does not change the n^{1/k} scale or remove the remaining tightness gap. The direct upper bounds of Theorems 7?8 need no use of this additional result.

Hutchcroft's *The L^2 boundedness condition in nonamenable percolation*, arXiv:1904.05804v2, Theorem 4.1 (PDF page 14), also verifies the relevance of l^q norm growth: under pc<p_{2->2} on an infinite nonamenable quasi-transitive host, ||T_pc||_{q->q} is of order q as q tends to infinity. Its infinite/quasi-transitive hypotheses are not imported into the arbitrary finite-host proof in Sections 12?15. This is a neighboring-method reference only.


## 20. Parameter-only formulation, verification and final verdict
To express the results using the source's parameters rather than a particular retained p, set c=1-epsilon and

    R=c B/lambda,  B=min(Delta-1,lambda^2/4).

At the largest allowed parameter p=c/lambda, rho_k=max(c,c(B/lambda)^{1-2/k}); smaller p only improves the upper bounds. Thus R<=1 yields the universal O_epsilon((log n)^3) bound for every p in the source range, and R<=1-eta yields O_{epsilon,eta}(log n). For R>1, the integer moment orders available from this method satisfy

    2<=k<2 log(B/lambda)/log(R),

with the explicit finite probability estimate (13). No endpoint or noninteger-moment improvement is asserted. This is an upper-bound architecture with matching results in some regimes, not the full optimal all-regime answer.

The script second_checks.py completed in approximately 8.14 seconds and saved second_checks.json. It exhaustively checked all 1094 nonempty simple labeled host graphs on 2 through 5 vertices, at three retention parameters each (3282 laws), by enumerating every retained edge subset. All 396312 ordered triple and 1968258 ordered quadruple connectivity inequalities passed, including all repeated-terminal patterns. Summed diagrams and eligible operator-moment bounds through order five also passed. The maximum triple ratio was 1 within floating error, while the maximum quadruple ratio was about 0.632091. In addition, 41744 nonbacktracking row bounds through length eight passed; their maximum ratio was 1 within floating error. These are checks, not proofs of the general inequalities.

Weighted-path validation covered 960 random positive weighted paths of lengths 1 through 12 and the exact equality families w_0=w_{h-1}=1/sqrt(2), interior weights 1/2 (single-edge case weight 1). All product bounds passed and equality errors were below 4.9e-15. No job approached the 1 GB memory limit; matrices had at most five host vertices or thirteen path vertices.

The final SpectralFlow.lean invocation from ~/lean_verify completed with exit code 0 and empty diagnostics. It was wrapped with a 3600-second timeout, ran one at a time through the shared Lean checker, and its output is SPECTRAL_LEAN_CHECK.txt. The checked declaration flow_prod_bound proves the arbitrary finite product bound used in the weighted-path optimization. It imports only Mathlib.Data.Fintype.Card, Mathlib.Data.Real.Basic, Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset and Mathlib.Tactic.Linarith. No sorry, native_decide or explicit axiom is used. Earlier diagnostic failures were due to a shell-encoding issue and a missing cardinality import; those invocations are not claimed checked. Formal scope remains algebraic, not the full percolation proof.

Final second-attempt VERDICT: PARTIAL. Sections 12–19 contain full new mathematical derivations and their applicability checks; the historical row bound was explicitly reverified and is not counted as new. The optimal full-source largest-component scale in the effective-supercritical regime R>1 remains uncharacterized. In particular, universal interpolation loses against the regular-tree lower exponent, and arbitrary collision/multiplicity/Perron-profile effects have not been optimized. This remaining gap is real and is not hidden by the matching exact-parameter special cases.
