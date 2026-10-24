# P0221: reverse-transfer investigation, 2026-10-11

The direct fixed-band first-offer construction in SECOND_ATTEMPT.md fails. A different construction uses causal reassignment of physical labels within virtual components and between components of equal size. This file proves P_n<=C_n+O(n^(-1/100)). With the independently proved forward direction it gives asymptotic equivalence of the two normalized models. It does not prove limit existence or determine a limit.

## Parameters and quantitative statement

Let beta=9/10, gamma=3/25, kappa=4/25 and alpha=rho=1/100. Put

    b=n^(-beta), eta=n^(-gamma), M=ceil(n^kappa),
    epsilon=n^(-alpha), delta=n^(-rho), h=1-delta,
    t_0=h(1-eta), a=(1+3epsilon)/h.

All subsequent assertions concern sufficiently large n. The error is O(n^(-1/100)), with logarithmic factors on terms of strictly smaller order. The already proved forward transfer gives C_n<=5 eventually; use a virtual combinatorial policy of expected cost c<=C_n+1/n<=6. Its rule sees the usual random-order labels and weights, not the auxiliary clock. An approximately optimal policy exists by the definition of the infimum, purchases only intercomponent edges and finishes a spanning tree. No attainment theorem for the combinatorial infimum is required.

## Uniform upper graph estimates needed

Give the virtual single offer per edge an independent uniform time s in [0,1]. Its remaining graph R(s) has independent Bernoulli(1-s) edges at every fixed s. Set p=1-s and D=2n^(3/2). With failure probability Q_n smaller than every fixed inverse power of n, simultaneously for all s<=1-eta:

1. For every two disjoint sets A,B with |A|,|B|>=M,

       R(s;A,B) <= (1+2epsilon)p |A||B|.

2. For every pair of disjoint sets A,B, and every induced set A,

       R(s;E) <= (1+epsilon/100)p |E| + D,

   where E is the potential complete bipartite edge set between A,B or the potential induced edge set within A.

Here is a full proof. If X is a sum of C independent Bernoulli(p) variables, then for lambda>=0,

    E exp(lambda X) <= exp[Cp(exp(lambda)-1)].

For 0<epsilon<=1, choose lambda=epsilon/2. For 0<=lambda<=1/2, exp(lambda)-1-lambda<=lambda^2: integrate the second derivative exp(u)<=2 over [0,lambda], using exp(1/2)<2 (the exponential series is strictly less than the geometric series there). Markov's inequality gives

    P(X>(1+epsilon)Cp) <= exp[-epsilon^2 Cp/4].

The additive estimate is P(X>Cp+D)<=exp[-2D^2/C], with the C=0 case trivial. To prove it, the centered one-Bernoulli log moment psi(lambda)=log(1-p+p exp(lambda))-p lambda has psi(0)=psi'(0)=0 and psi''(lambda)=q_lambda(1-q_lambda)<=1/4. Integrating twice gives psi(lambda)<=lambda^2/8. Independence and Markov, optimized at lambda=4D/C, give the stated bound. The boundary cases p=0,1 are direct.

Use a deterministic grid of spacing u=epsilon eta/100, including its lower endpoints g<=1-eta. There are K<=2+100/(epsilon eta) grid points relevant to the interval. At a grid point p_g>=eta. For disjoint sets of sizes v,w>=M the multiplicative failure probability is at most exp[-epsilon^2 eta vw/4]. There are at most n^(v+w) pairs of these sizes, and vw>=M(v+w)/2. Since epsilon^2 eta M=n^(1/50)+o(1), for sufficiently large n its eighth part exceeds 4 log n. Thus the union bound over all sizes and grid points is at most K n^2 n^(-6M), a superpolynomially small quantity.

The additive bound at grid points, for all disjoint-set or induced-set choices, fails with probability at most K 4^n exp(-16n), because C<=N=n(n-1)/2 and 2D^2/N>=16n. This is exponentially small. For arbitrary s choose the preceding grid point g, so R(s) is contained in R(g) and p_g<=p+u<=(1+epsilon/100)p. The additive bound follows immediately. The multiplicative factor becomes (1+epsilon)(1+epsilon/100)<=1+2epsilon. This proves both uniform estimates and their failure probability. No adaptive partition or future good event is conditioned upon.

## Physical-to-virtual label coupling

Maintain a bijection from physical vertices to virtual vertices. Each physical accepted-tree component lies entirely inside one virtual accepted-tree component (called its bundle). Initially both forests are empty. A virtual component of size i has a physical bundle of exactly i vertices, possibly consisting of several disconnected physical forest components. Two permissible relabelings preserve this invariant:

- permute virtual names inside a bundle;
- exchange whole physical bundles assigned to two virtual components of the same size.

The accepted physical forest itself is unchanged by these bookkeeping relabelings. There is no requirement that its edges match the virtual tree edges or that past physical edge labels match virtual labels. The virtual policy sees only its virtual single-offer history. Every future physical pair still has the original independent Poisson law conditional on the actual past. Thus, under the current bijection, cross-bundle offers have rate equal to their number of unordered physical vertex pairs. Relabeling after an event changes only future bookkeeping and uses no future offer.

Classify the virtual intercomponent edges as follows. Every component of size >=M is a separate large bundle. Components of each size i<M form one small size class S_i (the union of their virtual vertex sets). A pair of large bundles is one offer class; a large bundle and a small size class is one class; a pair of small size classes is one class. Within a diagonal small class, only pairs belonging to distinct virtual components are included. Internal virtual-component offers can be supplied entirely by private virtual randomness; they are never purchased.

Let T be the number of potential intercomponent pairs in a class and R the number of its unrevealed virtual edges. At physical time t=h s, exact virtual cheap offers need rate

    d=bR/(h-t)=bR/(hp),

with independent marks Uniform[0,b] and uniform selection among the R unseen virtual edges in the class. Actual Poisson offers in weight band [0,ab] have class rate ell=abT. If ell>=d, retain each physical candidate with probability d/ell. If ell<d, retain all such candidates and add independent virtual-only cheap offers of rate d-ell. Map the physical mark w to the virtual mark w/a. For retained candidates, select the virtual unseen target edge uniformly, independently of the mark, and reassign bundles and internal names so that its virtual endpoints name the observed physical endpoints.

Such a reassignment is always possible. For a large-large class, only internal bundle names need move. For a large-small class, exchange equal-size small bundles if necessary. For a small-small class, exchange bundles in the two size classes; on a diagonal class there are two distinct equal-size components on each side, so a permutation assigns both desired components simultaneously. Then adjust internal names. These operations preserve every physical forest component within a virtual bundle. If the virtual policy purchases this retained cross-bundle offer, buy the physical edge. Its endpoints lie in distinct virtual bundles and hence in distinct physical components, so no cycle is created. The ensuing virtual merger joins the two bundles. A virtual-only purchased edge joins bundles in the bookkeeping but leaves their physical forest components disconnected; the invariant still holds.

Supply high virtual offers independently at rate (1-b)/(h-t) per unrevealed virtual edge, with marks Uniform[b,1]. Supply internal-component offers similarly, split into cheap and high marks. Remove each virtual edge from the unseen set when its sole offer occurs. Together the virtual offers give exactly rate 1/(h-t) per unseen virtual edge with independent Uniform[0,1] marks. To verify the law, conditional on the whole actual past each class construction has exactly the stated total rate and uniformly chosen target edge. Hence each unseen edge has the specified deterministic clock hazard and mark law even in the enlarged filtration. The corresponding single-offer survival from 0 to hs is exp[-integral_0^(hs)dt/(h-t)]=1-s. The joint generator is the sum of these single-edge hazards; it determines the finite nonexplosive jump process on each compact interval t<h (successive waiting laws and target probabilities specify its law recursively). Thus the virtual offers are independent uniform-time, uniform-mark single offers, with a uniform random order, as required.

For this coupling, the physical policy uses only current actual Poisson candidates and its private virtual randomness. Candidate target selection and bundle reassignment occur after observing the current physical candidate, before the virtual purchase decision; future bijections depend only on the past. The virtual policy is not given that private actual history.

The filtration contains only physical and auxiliary points revealed by the current time and fresh coins already used. It contains no unused future auxiliary points or random seeds encoding them. Decision rules are restricted to this causal information. On the truncated interval, the overall relevant actual-plus-auxiliary event rate is at most Nab+N/(h eta). Consequently two relevant jumps in a dt interval have probability O(dt^2), for each fixed n. While the virtual unseen set U is unchanged, conditioning over intervening rejected physical candidates leaves its total next-virtual-event hazard exactly |U|/(h-t). The conditional no-virtual-event probability solves g'(t)=-|U|g(t)/(h-t); its target edge is uniform in U and mark independent uniform. Successive waiting laws prove the joint input law, not just separate time marginals.

In particular, reassigning virtual names changes only the physical-to-virtual bijection. The virtual graph, vertex labels, past observations and accepted forest remain fixed. Past physical forest edges need only have both endpoints assigned inside one virtual connected component. The two source-bundle assignments to the two distinct desired target bundles extend to a permutation within each small size class: remaining source and target bundle counts agree. Each within-bundle endpoint assignment extends to a vertex bijection because source and target cardinalities agree. These two finite facts justify the relabeling step.

## Expected unavailable cheap offers before truncation

Stop the physical simulation at t_0 or at the first time a current graph count reaches either of the slightly looser thresholds (1+5epsilon/2)p|A||B| for large sets, or (1+epsilon/50)p|E|+D for the additive test. Ignore zero-size potential edge sets. These buffered thresholds are strictly above the proved good-event bounds, so even a continuous-clock boundary hitting stop is contained in the failure event of probability Q_n. Both tests use the current remaining virtual graph and clock only, never future graph information. After a failure, wait until t_0 and repair; for analysis continue the virtual policy with independent correct single-offer transitions, not by peeking at future physical offers. This ensures the full virtual tree and its cost have the proper law.

While live, two large bundles, or a large bundle and a small class containing at least M vertices, require no cheap phantom offers: R<=(1+5epsilon/2)pT and ell=(1+3epsilon)bT/h>=d. Classes with T=0 also have R=0 and are simply omitted.

For a large bundle and a sparse small class |S_i|<M, supply all cheap offers virtually if convenient. The total number of potential pairs in these classes is at most nM^2: fewer than M size classes, each with fewer than M vertices, paired with total large-bundle mass at most n. Consequently their total virtual-only intensity is at most bnM^2/(hp).

For two distinct small classes, the live additive test implies the excess rate (d-ell)_+<=bD/(hp). For a diagonal class of size i, put v=|S_i| and T=(v^2-iv)/2. Since R_cross<=R_induced(S_i) and binomial(v,2)-T=(i-1)v/2<=Mn/2, the live additive test and 1+epsilon/50<=2 give

    (d-ell)_+ <= (b/h)(D/p+Mn).

There are at most M^2 small-small classes. Summing and integrating the stopped intensities on t<=t_0 proves that the expected number Z of cheap phantom offers before the stop is at most

    E Z <= b M^2[D log(1/eta)+Mn] + b n M^2 log(1/eta).

This is a stopped compensation calculation, not an expectation conditioned on the future good graph event. All rates are finite on this interval, and the integrated deterministic bound is finite.

## Final count and cost estimate

Let k be the physical component count at t_0. Every retained virtual purchase is one physical merger. Complete the virtual tree hypothetically and count its n-1 purchases. On a non-failure path, unrealized purchases are: high purchases (number at most total virtual cost divided by b), accepted cheap phantom offers before truncation (at most Z), or cheap purchases after virtual time 1-eta (at most all cheap offers in that interval). The last count has unconditional expectation eta N b by the exact uniform input law. On a failure path, k-1<=n. Therefore

    E(k-1) <= c/b + E Z + eta N b + nQ_n.

The parameters make these respectively O(n^(9/10)), O(n^(23/25) log n), O(n^(49/50)), and superpolynomially small. Repair after t_0 has at least delta physical time remaining. The explicit source-normalized supersolution J in ATTEMPT.md gives F<=4k/n, so conditional optimal repair cost is at most 4k/(n delta), independently of the virtual history. Prefix physical expenditure is at most a times total virtual expenditure. Hence the construction yields

    P_n <= a(C_n+1/n) + [4/(n delta)]
             [1+c/b+E Z+eta N b+nQ_n].

Since a-1=O(epsilon+delta), c<=6, and the last displayed count is O(n^(49/50)), this proves P_n<=C_n+O(n^(-1/100)). The terms n^(23/25) log n and n^(9/10) are smaller than n^(49/50), so the logarithm does not weaken the stated error. Together with the forward comparison this proves

    |P_n-C_n| = O(n^(-1/100)).

The physical forest is completed by the source's optimal Poisson continuation, which exists for every finite partition and almost surely finishes before the deadline. All conditional suffix laws use the actual physical past; the hypothetical virtual completion is additional analysis randomness and is not exposed to the real algorithm. Randomized constructions bound the optimal mean infimum by averaging independent seeds. This completes the proof.

Consequently P_n has a limit if and only if C_n has a limit, and their limits, when present, agree. Their liminf and limsup also agree. None of these statements proves that the liminf equals the limsup.

## Hostile-referee audit and checks

- Relabeling changes only the auxiliary bijection, never physical edges, virtual vertices or past observations. The needed invariant is containment of each physical forest component in a virtual component, not equality of trees.
- Whole bundles are reassigned only at equal sizes; internal bijections handle endpoint names. Large bundles stay fixed except for internal names. Assigning two same-size bundles simultaneously extends a partial permutation and cannot cause a target conflict.
- Candidates are classified before reassignment. The virtual target is selected independently of its weight. Future physical Poisson symmetry gives the correct class rates after every update.
- Each unseen virtual edge has hazard 1/(h-t) and independent uniform marks, including internal edges. Successive waiting laws establish the joint input law.
- Sparse small-class offers may be wholly virtual. Internal virtual offers cannot cause purchases but still leave the unseen set correctly.
- Uniform graph upper estimates cover arbitrary vertex sets and therefore adaptive component classes. Only upper estimates are required, since excess actual candidates are thinned.
- No compensator estimate conditions on the global future event. Stopping uses buffered current graph tests; the stopped phantom intensity has a deterministic bound.
- After a failure, missing purchases are bounded by n and the unconditional failure probability by Q_n. No per-history rare-event bound is asserted.
- A retained virtual merger joins distinct bundles and therefore distinct physical components. Physical edges remain acyclic. The excess physical component count equals n-1 minus physical purchases, even though physical edges need not literally be virtual tree edges after reassignments.
- At deterministic t_0, the actual partition's optimal continuation uses fresh physical Poisson increments and at least delta remaining time. Hypothetical virtual completion is never exposed to it.
- Exponent margins: epsilon^2 eta M has exponent 1/50; n^(3/2)bM^2 has exponent 23/25; the late cheap-offer count has exponent 49/50. Repair divides by n delta, giving the dominant error exponent -1/100.
- reverse_checks.py passed, exit code zero: 119,328 exact endpoint/bundle reassignments for every partition on n=2,...,6 with cutoffs 2,3,4; 43,668 cases have both endpoints in the same small size class. The general extension proof above establishes the finite step for every n; the test supports it.
- reverse_simulation.py passed, exit code zero: 2,000 seeded dynamic routing trials each at n=3 and n=5, with changing virtual components, cheap/high offers and phantom mergers. Every update checked that the physical forest stayed acyclic and each physical component stayed inside a virtual component. Input-count means, mean uniform marks and cheap-mark fractions passed the stated numerical tolerances. The bin covariances were also numerically close to their multinomial targets; data are in reverse_simulation.json. This is numerical evidence, not the joint input-law proof.
- Brain query (read-only, 2026-10-11): `Poisson process predictable permutation thinning coupling exchangeability` returned standard Poisson and predictability definitions and Last--Penrose references, not a solution. The conditional-rate and permutation steps are proved directly here.

## Disposition

VERDICT: PARTIAL for P0221. This attempt provides a complete asymptotic comparison of the two models; bibliographic novelty is not certified. Convergence of either (equivalently both) optimal-cost sequences and determination of the limit remain unresolved. General nonzero-state value continuity and the proposed optimal-control limit are unproved. The value near 1.9 remains numerical.
