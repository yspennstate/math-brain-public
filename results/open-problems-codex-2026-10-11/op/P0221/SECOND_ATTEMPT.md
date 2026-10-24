# P0221 — second serious attempt, 2026-10-11

## Remaining gap inherited from the first attempt

ATTEMPT.md establishes finite Poisson uniqueness, zero-state continuity and limsup P_n <= (63-3 exp(-4/3))/32. It does not prove convergence, the value of a limit, or C_n-P_n->0. In particular the draft's proposed one-sided transfer C_n<=P_n+o(1) has not been used because its conditional exchangeability/completion argument is incomplete.

## Two approaches not previously pursued

**A. Truncated mean-field optimal control.** Fix a positive time-to-go and a bounded scaled-weight cutoff, retain only component sizes up to M, and formulate a finite-dimensional density-dependent controlled Markov process. Try to apply Kurtz-style generator convergence and relaxed-control compactness, then remove the component-size and time cutoffs using the first attempt's reciprocal-state tail bound. This directly attacks existence of the Poisson limit. The difficult new obligation is a uniform approximation of *optimal*, possibly global-history-dependent controls: prescribed-kernel Smoluchowski convergence by itself is insufficient. Tail mass and the singular deadline are additional genuine obstacles.

**B. Causal rare-offer simulation and robust-cut repair.** Build a Poisson process of cheap offers online from the single Uniform offer per edge, with only O(n^2 b^2) virtual cheap offers. Simulate a compressed optimal Poisson tree; purchase just the offers that correspond to available physical edges of weight <=b. Bound missing tree edges by costly accepted virtual edges and virtual cheap offers. Then repair the resulting o(n)-component forest using a fresh argument that controls every cut of every remaining random-order graph, rather than assuming exchangeability conditioned only on accepted edges. This attacks the model-transfer gap and would also transfer the proved Poisson upper bound to the combinatorial model.

I pursue B. The intended conclusion is one-sided transfer, not full asymptotic equivalence or existence of a limit. Every required lemma and any failure will be recorded below.

## First new lemma: an exact causal cheap-offer simulator

Let 0<b<=1. For one edge, the physical input consists of a single point (T,W), with independent Uniform[0,1] coordinates. Discard it if W>b, including its identity from the virtual policy's observations. If W<=b, at its actual time T retain it with independent probability 1-bT. At that same physical low-offer time T, whether retained or not, start an independent Poisson process on (T,1] x [0,b] of intensity dt dw. Retained physical offers and the later virtual offers together form a Poisson process of intensity dt dw on [0,1] x [0,b].

Here is a direct proof, avoiding an unproved point-process characterization. Let V be the first output time, or infinity if none by time 1. For r in [0,1], no physical low offer before r has probability 1-br. A physical low offer at t<=r has unconditional time density b dt. If it is retained then V<=r; otherwise it is discarded with probability bt and the new rate-b Poisson process contributes no point before r with probability exp[-b(r-t)]. Consequently

    P(V>r)=1-br+b^2 int_0^r t exp[-b(r-t)]dt
           =1-br+br-(1-exp(-br))=exp(-br).

Whenever the first output occurs, the physical low-offer time has already occurred. If the first output was retained, all future outputs are the independent Poisson process started at that time. If it was virtual, all future outputs are the independent increments following its first point. In either case, conditional on the entire history up to the first output, the future output is a fresh rate-b Poisson process on the remaining interval. The first mark and all later marks are independent Uniform[0,b]: the retention coin depends on time only, and the new process uses independent uniform marks. This proves the asserted marked Poisson law, including the event of no output before 1.

The construction is causal: future virtual offers are started only after a physical low offer already seen. No future edge identity or weight is read to decide an earlier purchase. It is crucial that it thins with 1-bT, not 1-T. The latter would generate order n^2 b unavailable cheap offers rather than order n^2 b^2.

An independent full-law verification is useful because a one-interval count distribution would not alone prove independent increments. Fix finitely many disjoint time-mark rectangles, assign a variable z_j in [0,1] to each rectangle, and assign 1 outside them. Let f(t) be the average of these variables over a uniform mark in [0,b] at time t. Thus f is a piecewise constant function in [0,1]. Conditional on a physical cheap point at t<=h, the retained-point factor is (1-bt)f(t)+bt, and the subsequent phantom Poisson factor is exp[b integral_t^h(f(s)-1)ds]. Therefore the joint count generating function is

    1-bh + integral_0^h b[(1-bt)f(t)+bt]
                  exp[b integral_t^h(f(s)-1)ds]dt
      = exp[b integral_0^h(f(s)-1)ds].

To check equality, the integrand is the negative derivative, away from finitely many subdivision endpoints, of (1-bt)exp[b integral_t^h(f(s)-1)ds]. This continuous, piecewise differentiable function can be integrated interval by interval; the endpoint terms telescope. The resulting generating function is product_j exp[area(rectangle_j)(z_j-1)]. This is exactly the joint generating function of independent Poisson counts of the specified means. Generating functions determine distributions of nonnegative integer vectors (their power-series coefficients are the probabilities). Since finite rectangle-count distributions characterize a point process, this supplies a second complete proof of the marked Poisson law.

The expected number of virtual, rather than retained physical, offers before any deterministic h<=1 is

    b int_0^h P(T<=s,W<=b)ds = b^2 h^2/2.

Apply independently to every edge. The physical independent-time representation is equivalent to random order: draw N=binomial(n,2) independent Uniform times and sort them, obtaining an independent uniform permutation of the edges. An online implementation can instead draw the ordered times independently of the actual input permutation and attach the next time to each arriving edge. It exposes to the virtual policy only retained cheap points and internally generated virtual points, not unused raw times, high-weight observations, arrival indices, or future timestamps. Thus the virtual cheap processes are independent rate-one marked Poisson processes per edge even though the physical algorithm has a private record of all revealed edge identities for later repair and safety checks.

High-weight virtual offers can be generated independently on [0,1] x (b,infinity). Their union with the simulated cheap offers has exactly the source's full Poisson law. The source's optimal Markov policy is fed only that union. A private physical history is not passed to it. Its decisions depend only on current virtual components and virtual time. This distinction is essential: the full physical filtration contains information absent from the Poisson filtration, and no false assertion of a deterministic intensity relative to that larger filtration is made.

## Second new lemma: every large remaining graph has all cuts available

Let N=binomial(n,2), and R_m be the graph consisting of the last m edges of the physical uniform random order, for every m=1,...,N. For L=ceil(n^(4/3)), define G_n to be the event that, simultaneously for every m>=L and every nonempty proper vertex set A,

    |R_m intersect cut(A)| >= [m/(2N)] |A|(n-|A|).

We prove that Q_n=P(G_n^c) is smaller than every fixed inverse power of n. For a fixed m,A, the cut count X is hypergeometric, with success proportion q=|A|(n-|A|)/N and mean mu=mq. Here is a self-contained exponential bound. Write Y=m-X and view the m ordered draws as indicators I_j of a non-cut edge. Expanding the product of (1+(exp(lambda)-1)I_j), for lambda>=0, gives

    E exp(lambda Y)
      =sum_{j=0}^m binomial(m,j)(exp(lambda)-1)^j (N-C)_j/(N)_j
      <= [q+(1-q)exp(lambda)]^m,

where C=|A|(n-|A|), and (r)_j is a falling factorial. The ratio is at most ((N-C)/N)^j: each factor (N-C-i)/(N-i) is at most (N-C)/N until the numerator vanishes, after which the probability is zero. All coefficients in the expansion are nonnegative. Consequently

    E exp(-lambda X) <= [1-q+q exp(-lambda)]^m
                      <= exp[-mu(1-exp(-lambda))].

Markov's inequality with lambda=1 yields

    P(X<=mu/2) <= exp[mu(exp(-1)-1/2)] <= exp(-mu/8).

The last step uses exp(1)>1+1+1/2+1/6=8/3, hence exp(-1)<3/8. The cases q=0 or q=1 satisfy the same bound (and here q>0).

By replacing A with its complement assume a=|A|<=n/2. Since N<=n^2/2, mu>=ma/n>=La/n. A union bound over all m>=L and all such A gives, with r_n=n exp[-L/(8n)],

    Q_n <= N sum_{a=1}^{floor(n/2)} binomial(n,a)exp[-La/(8n)]
         <= N sum_{a>=1} r_n^a = N r_n/(1-r_n)

for sufficiently large n with r_n<1. Because L/n>=n^(1/3), this is O(n^3 exp[-n^(1/3)/8]), which is o(n^(-d)) for every fixed d. No independence of different cuts or different remaining graphs is assumed.

For a current forest with k positive integer component sizes x_i and total n, on the cut condition for R_m the number of available edges crossing components is at least

    [m/(4N)]sum_i x_i(n-x_i) >= [mn/(4N)](k-1).

Indeed, with a_i=x_i-1>=0, sum a_i=n-k and sum a_i^2<=(n-k)^2. Thus sum x_i^2<=(n-k+1)^2+k-1, so n^2-sum x_i^2>=(k-1)(2n-k)>=n(k-1). Each intercomponent edge is counted twice in the sum of component cuts. Conditional on the full physical past, the next edge is uniform among the m unrevealed edges and its unobserved weight is independent Uniform[0,1]. Therefore its conditional probability p of crossing current components satisfies

    p >= n(k-1)/(4N) >= (k-1)/(2n).

This statement is made when the *current* remaining graph satisfies the cut condition, which is measurable from the known complete graph and revealed edge identities. We never condition on the future event G_n to make the next-edge calculation.

## Third new lemma: inexpensive repair of an arbitrary adaptive forest

Start with k components and m_0 unrevealed physical edges, with m_0>=L and the current cut condition holding. The starting forest and revealed identities can depend arbitrarily on the past weights and private independent randomization. Choose B=12, and at a step with m>L remaining edges accept an intercomponent edge exactly when its weight is at most

    gamma_m=Bn/(m-1).

Assume n is sufficiently large that gamma_m<=1 for m>L. At any failure of the current cut condition, switch to greedy completion. At m=L, also switch to greedy completion if unfinished. A separate feasibility safeguard, defined below, guarantees completion even on bad orders.

The nonnegative repair potential is

    H(k,m)=Bn(k-1)/m.

At a live threshold step, put z=k-1, a=Bn/(m-1), and let p be the conditional probability of an intercomponent edge. The expected payment is p a^2/2, and the expected potential after the ordinary threshold decision is H(k,m-1)-p a^2. Consequently

    E[payment+next H | past]-H(k,m)
       =Bn z/[m(m-1)]-p B^2 n^2/[2(m-1)^2]
       <= [Bn z/(m(m-1))][1-Bm/(4(m-1))] <=0.

The first inequality uses p>=z/(2n). The second holds since B>=4. If the next state is killed because a safeguard/cut-failure stops the threshold policy, set its live potential to zero; this only lowers the potential. Spending after that stopping event is charged to the fallback, not to this estimate. A finite supermartingale summation therefore bounds the expected *threshold* expenditure before stopping by H(k,m_0).

Similarly, the acceptance probability at a live step is p gamma_m >= Bz/[2(m-1)]. Let Y_m be the number of excess components k_m-1 if the threshold phase is still live at state m, and zero if it has stopped, including at a failure. Killing a state only decreases Y. Thus

    E[Y_{m-1}|past] <= [1-B/(2(m-1))]Y_m.

Iterating for fixed initial history and m_0 gives

    P(unfinished and live at L | initial history)
       <= E Y_L <= (k-1) product_{j=L}^{m_0-1}(1-B/(2j))
       <= (k-1)(L/m_0)^(B/2) = (k-1)(L/m_0)^6.

The product bound follows from 1-v<=exp(-v) and sum_{j=L}^{m_0-1}1/j>=log(m_0/L). At the terminal cutoff, “live” means no earlier abort, before applying the mandatory cutoff fallback. This interpretation avoids inadvertently setting Y_L to zero before counting unfinished policies.

Feasibility safeguard: maintain that the union of the accepted forest and all unrevealed edges is connected. It is true initially when the remaining graph satisfies the cut condition. Before rejecting a current edge, check whether removing that edge from this union would disconnect it. If so, accept the edge and switch to greedy completion; the accepted edge joins distinct current forest components. On switching to greedy, every subsequent intercomponent edge is accepted. The connected-union invariant ensures the final accepted forest spans; its total additional cost is at most n because all physical weights are <=1 and at most n-1 mergers are accepted. At a forced acceptance, that edge's cost is charged to the fallback.

On G_n, no safeguard or cut-failure stop occurs for m>L: even after the step the remaining graph R_{m-1} is connected while m-1>=L. At L its remaining graph is likewise connected. Therefore the probability of a fallback is at most Q_n plus the unfinished-live probability. We apply this unconditionally at the actual starting point, not by conditioning the drift calculation on G_n.

For a random adaptive starting forest with m_0>=dN, where d>0 can depend on n and dN>=L, expected repair cost on non-aborted valid starts is consequently bounded by

    [Bn/(dN)] E(k-1) + n Q_n + n^2 (L/(dN))^6.

The Q_n term is an unconditional bound for the physical random order; it is not claimed to bound its probability conditional on each starting history. The iteration bound conditional on each history uses m_0>=dN and k<=n, then is averaged. This distinction prevents a conditioning error for adaptive initial forests.

## Next step

Combine the prefix simulation and repair, preserving the feasibility safeguard from the very first physical offer. Test exact finite identities and the simulator law. In particular check that later unseen weights remain independent conditional on the actual past, and that virtual decisions do not use the private physical history.

## 4. Quantitative one-sided transfer

**Theorem.** For the two precisely normalized source models,

    C_n <= P_n + O(n^(-1/6)).

The constant in O is absolute. In particular, the Poisson limsup upper bound proved in ATTEMPT.md also bounds limsup C_n. This is a one-sided comparison, not convergence or asymptotic equality.

**Proof.** Work at sufficiently large n; ignoring finitely many n has no effect on the assertion. Set N=n(n-1)/2, d=n^(-1/6), h=1-2d, b=n^(-2/3), L=ceil(n^(4/3)), and B=12. Thus h>=1/2, dN>=L and L>Bn for sufficiently large n.

Assign independent uniform arrival times to the physical edges. Their increasing order is the prescribed uniform random permutation. Equivalently an online algorithm can attach independently generated uniform order statistics to that permutation, without seeing future labels or weights. This auxiliary random clock does not alter C_n.

Run a virtual optimal Poisson policy compressed to [0,h]. By time rescaling, its expected total cost is c=P_n/h. The source's finite-state optimal policy completes almost surely before its deadline. The elementary bound already proved in ATTEMPT.md implies P_n<=4, so c<=8. Generate its cheap offers w<=b by the exact causal simulator of section 1. Supply independent virtual offers with w>b. The resulting virtual stream has exactly the source Poisson law. The virtual decision rule sees only this stream and its own accepted forest. It does not see high physical offers, discarded cheap offers, physical labels not in the stream, or future auxiliary arrival times.

For completeness, almost-sure predeadline completion also follows directly from Theorem 3's strict differences: while a nontrivial partition is held fixed, its total accepted-merger rate is A/(h-t), where A=sum_{i<j} x_i x_j(F(partition)-F(merged partition))>0. Given no previous merger after time s, the survival probability to q<h is ((h-q)/(h-s))^A, tending to zero as q increases to h. Repeat at the at most n-1 successive partitions. Each merger occurs strictly before h almost surely. Relevant offers have bounded weights on every fixed compact time interval before h; irrelevant arbitrarily large-weight offers need not be enumerated by the policy. Thus the infinite high-mark region poses no implementation or accumulation issue before completion.

Whenever the virtual rule buys an offer that is also a retained actual offer, buy the actual edge. Do not buy other physical edges during the prefix. The accepted physical forest is a subset of the virtual accepted tree; in particular it has no cycles. Enforce the connected-union safeguard from the *first* physical offer. If the safeguard would force acceptance of an edge the simulation wishes to reject, abandon the simulation, accept that edge, and finish greedily. This maintains a spanning-tree output on every sample, not only with high probability.

For analysis, let the unmodified virtual policy continue on the original probability space even on paths where the real policy has abandoned it. This is a mathematical coupling, not permission for the algorithm to inspect future physical data. Let S be its full cost and D the number of its purchased edges absent from the physical forest on non-aborted paths at h. Each missing edge is either a virtual purchase with weight greater than b, or an unavailable cheap virtual offer. Pathwise the former number is at most S/b. The latter is at most the total cheap phantom offers before h. Section 1 gives

    E D <= c/b + N b^2 h^2/2.

On a non-aborted path the physical forest has k components and k-1=D: the virtual tree has n-1 edges, so deleting D of them leaves D+1 components. Prefix expenditure is at most S, even on an aborted path before its forced acceptance; the forced edge and greedy expenditure are charged to the fallback bound n.

Let m_0 be the number of physical offers after h. Marginally m_0 is Binomial(N,2d). The binomial lower-tail estimate proved by the same exponential-moment argument as in section 2 gives

    P(m_0<dN) <= exp(-dN/4).

If this shortage occurs, finish greedily at h, using the connected-union invariant. Otherwise, after a non-aborted prefix, invoke section 3's repair with m_0>=dN. If its initial cut test fails, switch to greedy immediately. A hypothetical prefix safeguard stop, or any repair cut/safeguard stop before L, on a path with m_0>=dN, implies G_n fails: on G_n the remaining graph itself is connected at every such step, including after removal of the current offer. Consequently the expected expenditure charged to these exceptional fallback events is at most n[Q_n+exp(-dN/4)]. Terminal unfinished-live fallback has expected cost at most n^2(L/(dN))^6, by the repair lemma conditional on the actual starting history and then averaged.

The threshold expenditure in repair is bounded by its initial potential, averaged on the non-aborted, sufficient-suffix, good-initial-cut starts. On these paths k-1=D, so discarding their indicators and using nonnegativity bounds that expenditure by

    [Bn/(dN)] [c/b+N b^2 h^2/2].

These estimates do not condition the drift or the next-edge distribution on the global event G_n. All conditional calculations use the actual past and the current remaining edge set. Future physical weights remain independent uniforms: internal phantom randomness is independent of all physical weights except that cheap phantoms are activated only after an edge's actual weight has been seen. Unrevealed labels remain in uniform relative order, even when the independent auxiliary clock and the past simulated decisions are included in the actual history. Thus the repair conditional laws remain valid at the adaptive starting forest.

Summing expenditures proves the explicit bound

    C_n <= c + [Bn/(dN)] [c/b+N b^2 h^2/2]
           + n Q_n + n exp(-dN/4) + n^2(L/(dN))^6.

Here Q_n <= N r/(1-r), r=n exp[-L/(8n)], once r<1. For large n, N>=n^2/4 and L<=2n^(4/3). Therefore c-P_n=O(d), c/b+Nb^2h^2/2=O(n^(2/3)), and Bn/(dN)=O(n^(-5/6)). The first two errors are O(n^(-1/6)). Moreover L/(dN)<=8n^(-1/2), so the terminal error is O(n^(-1)); the other errors decay faster than every inverse power of n. This proves the theorem. All algorithms can be randomized: the infimum deterministic expected cost is no greater than the average cost of a randomized policy, since fixing its independent seed gives an admissible deterministic policy and averaging cannot improve the infimum. QED.

**Corollary.** With the normalization of the source,

    limsup C_n <= (63-3 exp(-4/3))/32 = 1.9440377683016505...

Proof: apply the theorem and the proved Poisson limsup bound in ATTEMPT.md. Neither sequence is claimed to have a limit. QED.

The argument supplies full details and an explicit error rate for the direction of the source's Proposition 12, which was presented as a sketch. It does not prove the reverse direction. No claim of bibliographic novelty is made.

## 5. Referee questions and precise remaining gap

1. **Incorrect thinning would break the simulator.** Retention is 1-bT, not 1-T. As an independent check, for z in [0,1] its count probability generating function before h is

       1-bh + integral_0^h b[(1-bt)z+bt] exp[b(h-t)(z-1)] dt
       = exp[bh(z-1)].

   The integrand is the negative derivative of (1-bt)exp[b(h-t)(z-1)]. The first-output argument in section 1, rather than a single count marginal alone, proves independent increments and uniform marks.
2. **The simulated process is not Poisson in the enlarged real filtration.** This is not needed: the virtual policy uses its own Poisson filtration only. Physical-history cut estimates use the physical conditional laws, not a fictitious constant virtual intensity in that history.
3. **Future physical observations are not sampled for the algorithm.** Pre-sampling them defines a coupling only. Implementing each cheap phantom process begins only after the corresponding physical cheap offer has arrived; independent high phantom offers are unrelated to future physical data.
4. **One must not condition on the all-cuts event when applying a transition bound.** The stopped potential uses measurable current cut tests. The rare-event bound is added after the unconditional expectation calculation.
5. **Completion on bad orders is mandatory.** The connected-union safeguard is applied throughout the prefix and repair; rejection of a bridge forces its purchase and greedy continuation. A forest plus remaining edges stays connected at each step. The exceptional branch costs at most n.
6. **There is no asymptotic equality in this proof.** Only C_n-P_n<=o(1) is proved. No lower bound on C_n-P_n, convergence of P_n, or value of a limit is inferred.
7. **The empirical state-continuity/control-limit approach remains unproved.** A fixed-kernel hydrodynamic theorem does not control the unknown n-dependent optimal kernels. The zero-state continuity in ATTEMPT.md does not supply uniform sensitivity at general nonzero states.

The remaining target is either: prove convergence and determine the value separately for the source combinatorial sequence C_n; or prove convergence/value for P_n and a reverse asymptotic comparison P_n<=C_n+o(1). The source's suggestion of a value near 1.9 is still numerical, not a certified limit. This second attempt settles neither target.

**Subsequent progress during this same attempt:** the reverse comparison is now proved in [REVERSE_TRANSFER.md](REVERSE_TRANSFER.md), using a different construction from the failed direct first-offer embedding below. It yields P_n<=C_n+O(n^(-1/100)), hence |P_n-C_n|=O(n^(-1/100)). The remaining gap is solely existence and determination of their common limit; general state continuity and the optimal-control limit remain unproved. The earlier paragraph describes the gap at that intermediate stage.

### Why the simplest reverse embedding does not close the gap

I also checked the direct first-offer reversal. In the physical Poisson model, restrict each edge to weights in [0,a] and retain its first such offer. The first times are independent Exponential(a) variables, so their order is a uniform permutation, and their rescaled marks w/a are independent Uniform[0,1]. Thus this does generate a combinatorial stream, but only when one waits for all those first offers. The probability that all N first offers occur before the physical deadline 1 is

    (1-exp(-a))^N <= exp[-N exp(-a)].

For a bounded a this tends to zero. Achieving probability at least 1-epsilon requires a>=log N-log[-log(1-epsilon)], since the displayed upper bound must also be at least 1-epsilon. Purchasing a virtual combinatorial weight U costs aU physically. A choice a=1+o(1), which would preserve mean cost, therefore fails to deliver the full virtual stream with high probability. Choosing a of order log N delivers the stream but loses the desired cost comparison. This rules out this particular direct reverse construction; it is not a counterexample to asymptotic equivalence. A successful reverse comparison would have to avoid requiring the full stream or exploit a more delicate cheap-offer policy reduction.

## Brain queries about the gap

2026-10-11: math_recall.py `controlled coagulation empirical state continuity optimal cost mean field control convergence` and `online random spanning tree Poisson combinatorial asymptotic equivalence Aldous Angel Berestycki`. The latter returned the source and the earlier attempt emphasizing the missing joint value/kernel limit. The former returned related mean-field and empirical-convergence material but no usable theorem resolving this control or transfer problem. Cards are hints only; no recalled claim is used as a proved input.

2026-10-11: math_recall.py `Hoeffding hypergeometric sampling without replacement Chernoff random graph cuts`. Relevant hints included Hoeffding's 1963 concentration result and warnings about finite-population variance. Rather than invoke an unchecked card, section 2 proves the required exponential-moment estimate directly.

## Independent verification record

second_checks.py completed with exit code zero. Its exact checks cover 3,310 hypergeometric moments, 21,808 graph-partition cases among 451 good graphs out of all 1,098 graphs on n=2,...,5, and 2,016 threshold drifts. The generating-function quadrature error was at most 9.992007221626409e-16. All 300,000 seeded single-edge simulator trials completed, including the b=1 boundary. For b=1 the disjoint half-interval means were 0.4999 and 0.4980, with empirical covariance -0.0029802; these are numerical consistency checks only. Full mathematical proofs above do not rely on those statistics.

RepairCheck.lean contains algebraic formalizations of the thinning integrand, partition crossing bound and scaled repair drift. The command was submitted sequentially from the required Lean project. Its actual completion status is recorded in VERIFICATION.md; the stochastic argument is not claimed to be formalized.

## Final disposition

STATE: DONE; VERDICT: PARTIAL. Forward and reverse quantitative model transfer are proved, giving |P_n-C_n|=O(n^(-1/100)); see REVERSE_TRANSFER.md for the subsequent reverse construction and its full proof. The transferred limsup upper bound remains 1.9440377683016505. RepairCheck.lean passed with exit code zero, with no proof holes or native decision evaluation. All finite arithmetic, exhaustive label-reassignment and simulator checks passed. Optimal limit existence and the common limiting value remain unresolved.
