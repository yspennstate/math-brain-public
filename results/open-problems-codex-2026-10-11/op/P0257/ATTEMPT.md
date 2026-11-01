# P0257 — working mathematical record, 12 October 2026

## Exact objects and scope

Aldous, arXiv:1912.13175v2 (PDF internal date 26 August 2021), p.2, defines distances by shortest paths in a positive-weight undirected graph. The discovery order is a permutation v_0,...,v_{n-1}; its length is L=sum_{i=0}^{n-2} d(v_i,v_{i+1}). There is no return to the start. All results below hold for every start simultaneously.

The proposed first-order programme concerns (a) n uniform points in the square of area n, with Euclidean distances; (b) an m by m grid with iid positive edge weights, normalized by m^2; and (c) K_n with independent exponential edge weights of mean n, using shortest-path distances, normalized by n. The source p.9 Eq.(4) writes a random limit for (a), p.11 explicitly conjectures convergence in probability for (b), and pp.14,20 discuss expected-length limits for (c) and the three models. These are related but not identical convergence assertions. We seek deterministic probability limits and expectation limits where integrability permits.

The source p.11 states only positivity for grid weights. Its exponential FPP estimate (5), p.12, requires additional distributional assumptions; positivity alone cannot imply it. We do not silently add a hypothesis, nor treat refutation of the unrestricted grid assertion as resolution of the Euclidean or exponential mean-field questions.

## 1. Deterministic two-distance lower bound (proved)

Let n>=3 and let a_v<=b_v be the first and second smallest distances from v to distinct other vertices. Let Y_v=(a_v+b_v)/2. For a Hamiltonian ordering with endpoints s,t,

    L >= sum_v Y_v - (b_s+b_t)/2.

Proof. At every interior vertex, its two incident ordering edges join distinct other vertices, so the sum of their lengths is at least a_v+b_v. At an endpoint, the one incident ordering edge is at least a_v. Summing these inequalities counts each ordering edge twice, giving 2L>=sum_v(a_v+b_v)-b_s-b_t. Division by two proves the claim. No greedy property is used and no graph edge is confused with a metric distance.

For R>0 define Y_v^R=(min(a_v,R)+min(b_v,R))/2. The same argument gives

    L >= sum_v Y_v^R - R.                                      (1)

Indeed the missing second-distance term at each endpoint is at most R. This form has a deterministic bounded endpoint error. For n=2 the untruncated definition of b is unavailable; this case is excluded and irrelevant to limits.

## 2. Mean-field lower bound 5/4 in probability (proved)

In the exact source mean-field model, for every epsilon>0,

    P(L_n/n < 5/4-epsilon) -> 0,
    liminf_n E[L_n]/n >= 5/4.                                 (2)

This is a lower bound, not a limit theorem for L_n.

The proof also gives a finite-size lower-deviation estimate. Define

    mu_R=5/4-(3/2)exp(-R)+(1/4)exp(-2R).

For n>=3, R>0 and delta>0,

    P(L_n/n < mu_R-R/n-delta)
       <=4(n-1)R^3 exp(2R)/(n^2 delta^2).                    (2a)

To verify the expression for mu_R, convolution of Exp(1) and Exp(2) gives P(S_1+S_2>t)=2exp(-t)-exp(-2t). Integrating the two clipped survival functions gives the displayed formula. The finite-n exponential rates in (3) are both smaller than their limiting rates, so coupling with the same two independent unit exponentials yields EY_v^R>=mu_R. Chebyshev applied to (4), followed by (1), proves (2a).

### Distribution of the first two metric distances

Explore first-passage distances from a fixed root. Initially n-1 independent rate-1/n exponentials compete, so a_v=S_1 has rate (n-1)/n. At its first arrival, one new vertex has joined the explored set. By the exponential memoryless property, all n-2 remaining root edges have fresh rate-1/n residuals. The n-2 edges from the newly reached vertex to outside are independent fresh rate-1/n exponentials. Thus the next time increment S_2 is independent of S_1 and has rate 2(n-2)/n. The choice of the first neighbor is uniform and independent of S_1; its unrevealed outgoing edges are independent of the revealed root edges. Consequently

    a_v=S_1,  b_v=S_1+S_2,
    E Y_v = n/(n-1) + n/[4(n-2)] -> 5/4.                       (3)

These are metric distance order statistics. Using the two smallest original incident edge weights would be incorrect.

### Concentration of the bounded local score

Set F_R=sum_v Y_v^R. We prove

    Var(F_R) <= 4(n-1) R^3 exp(2R).                           (4)

Fix an edge e={i,j}. Let H be the graph with e deleted, and let W,W' be its old and independently resampled weights. All weights in H are independent of W,W'. A distance truncated at R can change only for roots whose distance in H to at least one endpoint of e is <=R, and only if min(W,W')<=R. To see this, any path of length <=R using e has, up to its first use of e, a prefix in H from its root to an endpoint of e with length <=R. If no such prefix exists, every path relevant to the truncated first two distances avoids e. If W and W' both exceed R, no relevant path can use e. This also covers the case where fewer than two vertices lie at distance <=R.

Write B_H(i,R) for the metric ball, including its root. Each affected Y_v^R changes by at most R, so

    |F_R(W)-F_R(W')| <= R (|B_H(i,R)|+|B_H(j,R)|)
                         1_{min(W,W')<=R}.                    (5)

An FPP ball in H is stochastically dominated in size by a rate-one Yule process Z_R starting with one particle. At a stage with k vertices reached, the active boundary has at most k(n-k) edges of rate 1/n, so its total arrival rate is at most k. Conditional residual weights are exponential by memorylessness. Couple each successive holding time to an independent rate-k exponential: the graph waiting time is at least the Yule waiting time; if the boundary is empty it is infinite. This proves domination at every time, including deletion of e. The Yule distribution is geometric with parameter exp(-R), hence

    E|B_H(i,R)|^2 <= E Z_R^2
                         = 2 exp(2R)-exp(R) <= 2 exp(2R).

The elementary inequality (x+y)^2<=2x^2+2y^2 gives an upper bound 8 exp(2R) for the second moment of the sum of the two ball sizes. Independently,

    P(min(W,W')<=R)=1-exp(-2R/n)<=2R/n.

Thus E(F_R(W)-F_R(W'))^2 <= 16 R^3 exp(2R)/n. Efron–Stein's inequality for the independent n(n-1)/2 edge variables yields (4): one half times the sum of these squared differences.

For each fixed R, (4) and Chebyshev show F_R/n-EY_v^R ->0 in probability. The independent exponentials in (3) converge in law to independent exponentials of rates 1 and 2. Since the clipped score is bounded and continuous,

    E Y_v^R -> mu_R
       := E[(min(S_1,R)+min(S_1+S_2,R))/2],
       S_1~Exp(1), S_2~Exp(2), independent.

Monotone convergence gives mu_R up to 5/4. For a given epsilon choose a fixed finite R with mu_R>5/4-epsilon/2, then let n tend to infinity and use (1). This proves the probability assertion. Taking expectations in (1), then the same two successive limits, proves the expectation assertion. R is not taken to grow with n in the variance estimate.

There is also an actual L1 law of large numbers for the surrogate score: n^(-1)sum_v Y_v ->5/4 in L1. Indeed (4) gives L1 convergence of F_R/n to mu_R for fixed R by Cauchy–Schwarz. Since the untruncated score expectation in (3) tends to 5/4 and EY_v^R tends to mu_R, nonnegativity gives E[(sum Y_v-F_R)/n] ->5/4-mu_R. The triangle inequality bounds the limsup L1 distance from 5/4 by 2(5/4-mu_R), which vanishes as R increases. This LLN is for a local metric functional, not for the NUV length.

## 3. Exponential grid lower bound 1/3 (proved special case)

For iid Exp(1) weights on the source grid, for every epsilon>0,

    P(L_m/m^2 < 1/3-epsilon) ->0,
    liminf_m E[L_m]/m^2 >=1/3.                               (6)

Proof. The first metric arrival from an interior vertex with all its neighbors interior has rate 4. The two-vertex boundary has six edges (the grid has no triangles), so the second increment has rate 6, independent of the first. Therefore EY_v=1/4+1/(2*6)=1/3. All vertices except O(m) have this bulk distribution.

The first two metric distances are functions of the edge weights within combinatorial distance two of their root. Explicitly, let u be the neighbor with least incident root edge of length a. The second distance is the minimum of (i) all other root edges and (ii) a plus each edge from u to vertices other than the root. No longer path can arrive second: any such path contains two distinct vertices before its endpoint. Thus scores with roots at combinatorial distance >4 have disjoint edge supports and are independent.

For fixed R, each clipped score is between 0 and R. A grid root has at most 41 roots within distance four, including itself. Cauchy–Schwarz bounds each possible covariance by R^2, hence Var(sum_v Y_v^R)<=41 m^2 R^2. Boundary vertices contribute at most O(m)R to the expected sum; divided by m^2 this vanishes. Apply Chebyshev and (1), then let R increase after m tends to infinity. Monotone convergence of the bulk score gives 1/3. Taking expectations in (1) proves the expectation bound as well. This argument establishes neither convergence nor an upper bound matching 1/3.

## 4. Literal unrestricted positive-iid grid assertion is false (counterexample)

Give each lattice edge an independent Pareto weight W with

    P(W>t)=1 for 0<=t<1, and t^(-1/8) for t>=1.

All weights are strictly positive and finite almost surely. For an interior vertex let D_v be its smallest incident edge weight. Its nearest other vertex in the shortest-path metric is at distance exactly D_v: every outgoing path starts with an edge of length at least D_v, and the minimizing incident edge reaches its neighbor at that length. Therefore

    P(D_v>t)=t^(-1/2), t>=1,
    E min(D_v,K)=1+integral_1^K t^(-1/2)dt
                   =2 sqrt(K)-1, K>=1.                      (7)

For any discovery ordering, each vertex except the final one departs by a segment of length at least D_v. Consequently, for each fixed K>=1,

    L_m >= sum_v min(D_v,K)-K.                              (8)

Two D_v scores share a weight only if their vertices are adjacent. All nonadjacent scores are independent. There are at most five roots (including itself) possibly covarying with a given root. For clipped scores, Var(sum_v min(D_v,K))<=5m^2K^2. All but O(m) vertices have (7); boundary contributions are between 0 and K. Thus

    m^(-2) sum_v min(D_v,K) -> 2 sqrt(K)-1

in probability for fixed K. Given any finite A, choose K so that 2 sqrt(K)-1>A+1. Equation (8) implies P(L_m/m^2>A)->1. In particular L_m/m^2 tends to infinity in probability, and no finite linear-scale constant exists. Also for m>=4 the expected walk length is infinite: choose two nonadjacent bulk vertices u,v (for instance coordinates (1,1) and (2,2) in zero-based indexing). Their D values are independent, and every ordering departs from at least one of them, so L>=min(D_u,D_v). This minimum has tail t^(-1) for t>=1, whose tail integral diverges.

This exposes a missing hypothesis in a literal universal reading of the grid model; it does not refute the source's Exp(1) simulations or solve the two other models. In particular we do not mark the entire three-model programme SOLVED.

## 4a. Euclidean probability lower bound 5/8 (proved)

In the exact area-n square model, for every epsilon>0,

    P(L_n/n < 5/8-epsilon)->0,
    liminf_n E[L_n]/n >=5/8.                                 (9)

We independently prove this; it does not improve the prior repository's unverified here expectation endpoint 0.629258.

First, in a finite planar configuration in general position, a point p is among the two nearest neighbors of at most twelve other points. Divide the plane around p into six half-open sectors of aperture pi/3. If three candidate roots lie in one sector, take the farthest x. For either closer root z, the cosine rule, the angle <=pi/3, and |z-p|<|x-p| give

    |x-z|^2 <= |x-p|^2+|z-p|^2-|x-p||z-p| < |x-p|^2.

Thus x has two points closer to it than p, a contradiction. Equal radial distances have probability zero for iid continuous points. Therefore at most two roots per sector can have p among their two nearest neighbors.

Let F_R=sum_v Y_v^R. Replace one sample point by an independent one. Among the other indices, only roots having the old point among their old first two neighbors or the new point among their new first two neighbors can change their score. There are at most 12+12 such indices; the replaced index adds one. Each score is between 0 and R, so |Delta F_R|<=25R almost surely; use the looser 26R for convenience. Efron–Stein gives

    Var(F_R)<=338 n R^2.                                    (10)

For a fixed t<=R and a root farther than R from the square boundary, the number of other points within t is Binomial(n-1,pi t^2/n), once n is sufficiently large. Thus

    P(a_v>t | root)= (1-p)^(n-1),
    P(b_v>t | root)= (1-p)^(n-1)+(n-1)p(1-p)^(n-2),
    p=pi t^2/n.

The fraction of possible root locations within R of the boundary is O(R/sqrt(n)) and tends to zero. The score is bounded by R there as elsewhere. Integrating the survival functions, using bounded convergence, proves

    E Y_v^R -> mu_R = (1/2) integral_0^R exp(-pi t^2)(2+pi t^2)dt.

The Gaussian integrals are integral_0^infinity exp(-pi t^2)dt=1/2 and integral_0^infinity pi t^2 exp(-pi t^2)dt=1/4. Hence mu_R increases to 5/8. For fixed R, (10) gives concentration of F_R/n; (1), followed by R increasing only after n tends to infinity, proves (9). Taking expectations in (1) proves its expectation assertion. No stabilization or convergence of NUV itself is assumed.

## 5. Remaining gap and failed routes

The two-distance scores have probability limits because they are local; the NUV walk itself depends on the entire discovery history. No estimate here shows that L is asymptotic to these scores, or to another local score. For the Euclidean model the source reports a candidate near 0.9; our prior-repository reading recovered an unverified-in-this-session lower endpoint near 0.629258. We have not re-proved that endpoint and do not claim it as a new or independently checked result.

Simple subadditivity does not follow from TSP subadditivity: patching optimal tours gives an upper bound on a minimized functional, while NUV follows a prescribed ordering and may change throughout a region when outside points are added. No almost-subadditive inequality or stabilization theorem for this ordering was obtained. The local weak limit of the underlying graph does not by itself determine the visit-history-dependent walk or supply uniform integrability of its step lengths.

A mutual-nearest-pair correction was considered but abandoned as a main target: its simple mean-field bound 9/8 is weaker than classical MST bounds and the 5/4 bound above. It cannot close the existence gap.

To finish the intended programme one still needs convergence and identification in the area-n Euclidean model, the light-tailed grid (including Exp(1)), and exponential mean-field model. For the unrestricted positive-iid grid, a finite constant theorem needs additional integrability/tail assumptions; (7)-(8) disprove that unrestricted version.

## Referee checks to perform

Check metric rather than raw-edge order statistics; endpoint correction; the rate of the two-vertex exploration boundary; independence after edge deletion in (5); Yule domination direction; fixed-R order of limits; finite dependence and boundary counts in the grid; Pareto truncation rather than an unjustified integrable LLN. Numerical checks and a Lean algebraic certificate will be recorded separately. No full NUV LLN is asserted.


## 6. Necessary grid integrability condition (proved)

The proof of (8) applies to any fixed law of positive iid weights W. Put D=min(W_1,W_2,W_3,W_4) for four independent copies. If E D=infinity, then L_m/m^2 tends to infinity in probability, uniformly over starting vertices. Indeed the same clipped finite-dependence variance bound gives the probability limit E min(D,K) for the normalized vertex-score sum, for each fixed K. Monotone convergence makes these limits arbitrarily large, and (8) proves the assertion. Equivalently a necessary condition for a finite probability limit is integral_0^infinity P(W>t)^4 dt<infinity. This condition is not asserted to be sufficient.


## Final verification and disposition

All finite numerical checks passed: 1,755 metric starts, 360 deleted-edge resampling cases, Euclidean replacement and indegree checks, and model/tail consistency samples. Details and limitations are in REFEREE.md and the saved JSON outputs. The final `lake env lean` run on FiniteCharge.lean exited 0 (134.52 seconds), after two missing-import failures preserved in separate logs. Both finite-charge and square-sum theorems compiled with kernel-checked tactic proofs and no sorry/native_decide. This certifies only the stated finite algebraic step, not the probabilistic theorems.

Disposition: DONE / PARTIAL. No matching published solution was verified. The literal unrestricted grid statement is false; the intended Euclidean, light-tailed grid and exponential mean-field existence/identification programme remains unproved. A future concrete attack is to construct a stable, history-aware local approximation to the mean-field NUV ordering and bound its average error; the local-score LLN here does not provide that approximation.


## Second serious attempt, at the user's request (12 October 2026)

The earlier disposition above records the first attempt. The continuation is written in full in SECOND_ATTEMPT.md and audited in SECOND_REFEREE.md. It records two previously untried approaches before pursuing the exact exponential deferred-decisions reduction. The brain was asked specifically about the history/local-state gap, exponential conditional independence and a named fluid-limit method.

New proved results in the exact exponential mean-field model: an explicit conditional transition on growing visited metrics and history thresholds; a Lipschitz/distance-cone formula for those thresholds; an exponential expectation bound on long-step contribution; bounds on all fixed normalized step moments; and an L2 approximation L_n/n=A_n+O_{L2}(n^(-1/2)), where A_n is the explicitly computed predictable drift. The first two steps also have an exact expectation formula, including E L_3=15/4, and a zero-threshold reset incurs a nonzero limiting second-step error of 1/12.

The remaining mean-field gap is now precisely the pair E A_n ->c and Var(A_n)->0, equivalent to the intended deterministic LLN by the proved fourth-moment bounds. No ergodic law for the growing visited-metric state was established. The new reduction controls the martingale noise, not the random predictable drift. The Euclidean and light-tailed grid LLNs remain open within this attempt.

Checks: 6,000 exact finite transitions; 1,140 cone/reconstruction states; 300 covering-count cases; independent hazard quadrature and direct/deferred distribution diagnostics. The final ThresholdUpdate.lean check exited 0. These checks and their limitations are detailed in SECOND_REFEREE.md. Final disposition remains DONE / PARTIAL; no complete solution or publication-level novelty claim is made.
