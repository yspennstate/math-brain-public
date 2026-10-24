# P0452 second attempt: full proof

Date: 2026-10-12. Initially recorded as a proposed proof; final audit and verdict are recorded at the end.

Target: P is a probability law on positive integers, E D<infinity, P(D=1)<1. Budgets are IID P, independent of symmetric IID Exp(rate 1/n) costs on the complete graph. An edge is retained iff its rank at each end is at most that end's budget (clipped to n-1). Let L1 be the largest retained component. Prove L1/n -> rho(P) in probability, where rho(P) is the EWT survival probability. Also treat deterministic budget arrays satisfying the source's weak empirical convergence assumption. The prior attempt proved the upper bound in probability and fixed-k mass concentration. This proof supplies a different lower-bound route.

Two new approaches were recorded in ATTEMPT.md: temporal coagulation with active vertex counts, and local active-vertex coverage followed by time sprinkling. We pursue the latter. No theorem identifying this exact giant in print is invoked.

## 1. Time representation and augmented local limit

Expose each edge at its cost, once. Let H_n(t) contain all exposed edges, and let G_n(t) contain exposed edges whose rank at both ends is <=budget. A vertex is active at t if deg_H_n(t)(v)<d_v. An arriving edge is accepted iff both endpoints are active immediately before its arrival. This counts ALL earlier arrivals at a vertex, not just accepted edges. Later arrivals never delete accepted edges. Thus G_n(t) increases with t and its union is the original La--Kabkab graph.

For fixed t, H_n(t) is an ER graph with p_n=1-exp(-t/n). Conditional on presence, costs have density exp(-x/n)/(n p_n), 0<x<t, converging uniformly to 1/t. Its marked local limit is a Poisson(t) Galton--Watson tree with IID uniform [0,t] edge costs and IID P budgets. This statement includes all incident edges in the observed finite radius, not merely the accepted ones. A direct proof: explore a fixed radius. Expected number of discovered vertices is bounded by sum_{j<=r}(n p_n)^j; use Markov to restrict to at most M explored vertices. On that event repeated targets or edges within the explored set have probability O(M^2/n). Fresh offspring laws are Bin(n-O(M),p_n) -> Poisson(t); fresh weights converge as above. For deterministic budgets with weakly converging empirical law, finitely many distinct uniform targets sample budgets without replacement, whose joint law converges to independent P. Let n tend to infinity, then M to infinity. This also proves the IID formulation. Unbounded budget marks are harmless, since only finitely many marks are used and their laws are tight.

At cost <=t, preference rank is determined entirely by incident edges of H_n(t). Therefore G_n(t), its active labels, and any fixed-radius bounded-degree-path event are determined by a finite-radius enlargement of H_n(t). Their local limits follow by the same coupling. The limit retained component is denoted T(t); it is the EWT with all edges of cost >t removed. To identify it, use the rate-one Poisson incident costs: the root with budget D has threshold Gamma(D+1) and D uniform potential edge costs below that threshold. At a non-root reached at cost y, the OTHER incident costs form an independent rate-one Poisson process; it accepts the parent iff its Dth other cost exceeds y. That threshold has Gamma(D) law, and its D-1 other potential costs are uniform below it. This is exactly the source's backbone/pruning construction, with the cutoff added. Activity is marked using the number of ALL incident costs <=t, including rejected proposals. It cannot be inferred from retained degree alone.

Write rho_t=Pr(|T(t)|=infinity), and p_{t,k}=Pr(|T(t)|>=k).

Fixed-k mass concentrates at this cutoff. Resampling one cost changes the two preference lists in at most four edges, with a possible additional change in that edge's cutoff status; thus G_n(t) differs in at most five edges and |Delta F_k|<=10(k-1). If both old and new costs exceed t, G_n(t) is unchanged. The probability of a possible change is <=2t/n. Efron--Stein gives Var(F_k|d)<=50 n t (k-1)^2. For IID budgets, changing one budget changes only incident retained edges; the number is at most deg_H_n(t)(v). Hence the difference of the conditional weight means g(d) is <=2(k-1) E deg_H_n(t)(v)<=2t(k-1). Another Efron--Stein inequality and total variance give

Var(F_k(G_n(t))/n) <= (k-1)^2(50t+2t^2)/n.

For deterministic arrays omit the budget variance term. The augmented local limit yields convergence of expectations, so F_k(G_n(t))/n ->p_{t,k} in probability.

## 2. Every infinite cutoff component contains an active vertex

Let a_t=Pr(D>=2) exp(-t)>0. Test potential children sequentially in a breadth-first search of T(t), testing only candidate edges whose cost y<=t. At such a test, the child's budget, Gamma(D) threshold z, and potential outgoing costs are fresh independent backbone variables, conditional on the history and y.

There is an event of probability exactly a_t on which the child is accepted and is an active leaf at time t: D>=2, and all of its OTHER incident costs exceed t. Equivalently in backbone variables, z>t and all D-1 uniform potential costs exceed t. Conditional on D=k>=2, this probability is

integral_t^infinity [exp(-z) z^(k-1)/(k-1)!] (1-t/z)^(k-1) dz
 = exp(-t).

On this event z>t>=y, so the parent edge is accepted. Only the parent has arrived at this non-root vertex by time t, so it is active because k>=2; it has no other cutoff neighbors. This calculation is unconditional in the fresh child's variables, given the already known candidate cost y. It does not condition incorrectly on a previously accepted child.

On {|T(t)|=infinity}, infinitely many eligible candidate tests occur. The probability of avoiding the active-leaf event through the first N eligible tests, with those tests existing, is at most (1-a_t)^N by conditioning successively; the next test's eligibility is known before its fresh child's variables are tested. Therefore

Pr(|T(t)|=infinity and T(t) has no active vertex)=0.

Every vertex of the augmented limit tree has finite degree in H(t), almost surely. Consequently, on the infinite-component event, the root has a finite retained path to an active vertex, with all vertices on that path having H(t)-degree bounded by some finite integer.

## 3. Active coverage gives capacity in every macroscopic union

Fix t and an error tolerance eta>0. For integers R,B define a root as covered if it has a retained path of length <=R to an active vertex, all path vertices having H_n(t)-degree <=B. This is a fixed-radius event in the augmented local limit. Put C=1+B+...+B^R. Each active vertex can cover at most C roots: every covering path lies in the subgraph induced by H_n(t)-degree <=B vertices, which has maximum degree <=B.

For every zeta>0 choose R,B and then k sufficiently large that

Pr(|T(t)|>=k and root not covered) < eta zeta/8.

Justification: split into finite components of size >=k, whose probability tends to zero as k grows, and infinite components whose root is not covered; the latter probability tends to zero as R and then B increase by Section 2 and local finiteness. Increasing k further preserves the inequality.

By augmented local convergence, expected fraction of uncovered roots in size>=k components has the same limit. Markov's inequality therefore gives, with limsup failure probability <=zeta/4, at most eta n/2 such uncovered roots in the finite graph. On this event, EVERY union of size>=k components having at least eta n vertices contains at least a n active vertices, where a=eta/(2C). Indeed at least eta n/2 of its roots are covered and each covering active vertex belongs to the same component and covers at most C roots. This is a simultaneous deterministic implication, not a concentration claim about any one component's empirical active density.

## 4. Time sprinkling joins macroscopic unions

Condition on the complete arrival history up to t, including rejected arrivals. Let delta=a/4. All unseen costs have independent residual Exp(rate 1/n) times by memorylessness. The number N_delta of new first arrivals during (t,t+delta] is stochastically dominated, conditional on the history, by Poisson(delta n/2). Thus

Pr(N_delta>delta n | history) <= exp[-delta n(log 2-1/2)].

At most two active vertices can cease being active per arrival. On N_delta<=delta n, each initially a n-active union has at least a n/2 active vertices throughout the interval.

Take any bipartition A,B of the old components of size>=k, with each side having at least eta n vertices. Stop at the first accepted cross edge or at the first time total new arrivals exceed delta n. Until this stop, there are at least a n/2 active vertices on each side. Every pair of such vertices has an unseen edge: an earlier edge between vertices still active now would have been accepted at its arrival, contradicting either their different old components or the absence of a new cross edge. Hence their independent residual clocks have total rate at least a^2 n/4, and an arrival on one of these pairs is accepted.

The survival function for the stopped event (no cross edge AND no arrival-limit stop) has hazard at least a^2 n/4. Equivalently, integrate the finite-state conditional transition rates or use the stopped counting-process compensator. Therefore

Pr(no accepted cross edge in the interval AND N_delta<=delta n | history)
 <= exp(-delta a^2 n/4).

There are at most 2^(n/k) bipartitions. Increase k, after choosing R,B, so log(2)/k < delta a^2/8. Conditional union bounding gives an exponentially small probability that ANY macroscopic bipartition stays without a new accepted cross edge, on the event N_delta<=delta n. The Poisson-tail failure is counted once, outside this union bound.

Let S=F_k(G_n(t)) denote the number of vertices in old large components. If S>=3 eta n, and no final component contains at least S-eta n of those vertices, a bipartition of final components produces two unions of old large components of size >=eta n: if a final block has mass between eta n and S-eta n, choose it; otherwise all final blocks have mass <eta n and greedily accumulate until the sum is between eta n and 2 eta n, leaving at least eta n. Such a partition has no new cross edge, a contradiction. If S<3 eta n the lower bound below is trivial. In all cases the absence of such a partition implies

L1(G_n(t+delta)) >= S-3 eta n.

The fixed-k mass law gives S/n >=rho_t-eta with probability tending to one. Since the final graph contains G_n(t+delta), we obtain

limsup_n Pr(L1(G_n(infinity))/n <rho_t-4 eta) <=zeta/4.

The argument holds for every zeta>0, with R,B,k,delta allowed to depend on it. Thus the limsup is zero. For EVERY finite t and eta>0, the final giant fraction is asymptotically at least rho_t-4 eta. No budget bound or exponentially growing exploration is used here.

The analytic issue is rho_t increasing to rho. Sections 5-7 prove it under the finite first moment alone.

## 5. Compact return process: finite mean prevents survival escaping through types

Ordinary non-root types are s=(m,x), where m=D-1>=0 is the potential child count and x>0 is the threshold. Let mu be the probability measure

mu({m} x dx)=P(m+1) exp(-x)x^m/m! dx.

Conditional on a parent (m,x), each of its m slots has an independent candidate type (r,z)~mu, accepted with probability h(x,z)=min(x,z)/x. Equivalently draw an independent uniform cost on [0,x] and compare it with z. Child subtrees are independent conditional on their types. Finite mean gives integral m mu(ds)=E(D-1)<infinity.

Choose B<infinity and 0<a<b<infinity such that

K={ (m,x): 1<=m<=B, P(m+1)>0, a<=x<=b },

epsilon=integral_{K^c} m mu(dm,dx)<1.

This is possible by integrability and compact exhaustion; include at least one fertile m in K. Take epsilon strictly positive if convenient by slightly enlarging the complement. Regard K as a finite disjoint union of compact intervals with measure mu_K, which has full support and positive continuous density on each interval.

Kill a particle whenever it first enters K. For an outside particle with potential m, the expected total potential of its outside children is

m integral_{K^c} r h(x,z) mu(dr,dz) <=m epsilon.

Thus for a starting particle of potential m, the expected outside potential at generation j is <=m epsilon^j. Expected number of births in generation j+1 is <=the previous potential; so the entire family stopped on hitting K has finite expected number of vertices, <=1+m/(1-epsilon), including its first K hits. It is finite almost surely, for every finite starting type. This rules out type escape in the killed process; no exponential moment is used.

For a particle in K, let its RETURN children be its first strict descendants in K along each line, exploring through outside types and stopping a line at its first K hit. There are finitely many such children almost surely. Their disjoint descendant subtrees are independent conditional on their types. This defines a branching process on compact K, whose mean kernel has a density R(s,u) relative to mu_K(du).

The direct-child term is m h(x,z). Terms with j>=1 outside ancestors are bounded pointwise by B epsilon^j: expected outside potential at depth j is <=B epsilon^j, and each slot's final target density h(.,z) is <=1. Therefore

a/b <=R(s,u)<=B/(1-epsilon), for every s,u in K.

The series of kernel terms converges uniformly. Each term is continuous on K x K, by dominated convergence of the finite path integrals (the same potential bound is a dominating integral). For parent x and endpoint z in [a,b], h is uniformly Lipschitz in those coordinates, even when intermediate thresholds approach zero: if an intermediate threshold is <a then h(.,z)=1 throughout z in [a,b]. Consequently uniform continuity and compactness are also immediate. Thus R is a continuous, uniformly strictly positive bounded kernel. We obtain its positive principal eigenfunction from a SELF-ADJOINT operator, not by incorrectly applying the source's self-adjoint Krein--Rutman statement to an arbitrary nonsymmetric operator.

For a fertile type s=(m,x), write alpha(s)=m/x and pi(ds)=mu(ds)/alpha(s). Restricted to K, pi is a finite measure with positive continuous density and full support. The mean density relative to pi is F(s,u)=R(s,u)alpha(u). It is symmetric. Indeed a return path with internal outside types s1,...,sj has, relative to pi at its endpoint u, the factor

alpha(s) alpha(u) product_{i=1}^j alpha(si)
 times min(x,x1) min(x1,x2)...min(xj,z)
 times product_{i=1}^j mu(dsi).

Reversing the internal path preserves this expression and the integration domain. Zero-potential types give zero to any nonterminal return path and can be omitted. Uniformly convergent summation preserves symmetry. Consequently A acts as a compact self-adjoint integral operator on L2(K,pi), with continuous strictly positive kernel F. Compactness follows from its bounded Hilbert--Schmidt kernel (or the continuous-kernel approximation by finite rank).

Here is the needed positive-eigenfunction argument. For every real f, the positive kernel gives |<Af,f>|<=<A|f|,|f|>. The compact self-adjoint spectral theorem therefore implies that the operator norm lambda>0 is attained by a nonnegative eigenfunction: take a norm-attaining extremal eigenvector, replace it by its absolute value, and use equality in the Rayleigh bound. Such an extremizer has A|f|=lambda|f|, by the spectral decomposition or the variational characterization. The strict positive lower bound on F then makes v=lambda^{-1}A|f| continuous and strictly positive at every point of K. On compact K, 0<v_min<=v<=v_max<infinity. Thus Av=lambda v with lambda>0. Only the ordinary compact self-adjoint spectral theorem is used here; the positivity and regularity implications have just been proved.

There is a UNIFORM positive probability of zero return children. Put gamma=mu{x<=a/2}>0. For a parent in K, each potential edge cost is >=a/2 with probability at least 1/2, and its fresh child threshold is <=a/2 with probability gamma. Thus each slot has rejection probability >=gamma/2, independently. All m<=B slots are rejected with probability at least d0=(gamma/2)^B>0. This event gives no original children, hence no return children.

If Z_j denotes population size in the return process, then on survival Z_j ->infinity almost surely. Proof: for any fixed L, whenever 1<=Z_j<=L, conditional probability that the next generation is empty is >=d0^L. At successive visits to {1,...,L}, the probability of avoiding extinction at all of the first q visits is <=(1-d0^L)^q, by the branching property and conditioning at visit stopping times. Thus infinitely many such visits have probability zero on survival. Intersect over L.

If lambda<=1, starting from s in K, E sum_{generation j} v(type)=lambda^j v(s), so E Z_j<=v_max/v_min uniformly in j. Fatou's lemma and the preceding divergence on survival imply survival probability zero. Hence positive return survival implies lambda>1.

Because every stopped outside family is finite almost surely, the original ordinary tree is infinite iff its K-return tree is infinite (after the finite forest of first K hits, if the starting type is outside K). There are only countably many such families; their almost-sure finiteness holds simultaneously. A finite return tree gives only finitely many finite stopped families; an infinite return tree contains infinitely many distinct original vertices. For the special EWT root, its finite number of first candidate branches leads to a finite first-return forest by the same argument. If rho>0, some K-return process therefore has positive survival, and lambda>1.

## 6. A bounded-cost subprocess survives whenever the full EWT survives

Choose larger compact L containing K, of the form 1<=m<=B_L and a_L<=x<=b_L for the fertile support types, where tau_L=integral_{L^c} m mu ->0 as L exhausts fertile types. Zero-potential types contribute neither to tau_L nor to further descendants.

Truncate each K-return family by killing outside particles whose type is not in L and by stopping a line once it has more than N outside ancestors before returning to K. Keep direct K children. Let A_{L,N} be its mean return operator. Return offspring are uniformly bounded, e.g. by sum_{j=1}^{N+1} B_L^j. Its continuous kernel is still bounded below by the direct-child kernel a/b.

Its kernels approximate R uniformly. The mean endpoint density of return paths with more than N outside ancestors is <=B epsilon^(N+1)/(1-epsilon). For paths passing through a type outside L, the expected sum of potential at first excluded births is <=B tau_L/(1-epsilon): at every outside generation the expected parent potential is <=B epsilon^j and expected excluded child potential is at most parent potential times tau_L. From any excluded child of potential r, the entire expected subsequent first-return endpoint density is <=r/(1-epsilon). Thus the loss in kernel density is at most B tau_L/(1-epsilon)^2. In particular

||A-A_{L,N}||_{C(K)->C(K)}
 <=B[epsilon^(N+1)/(1-epsilon)+tau_L/(1-epsilon)^2],

since mu_K(K)<=1. This includes all lost paths; duplicate counting only enlarges the bound.

Choose L,N so the RHS times v_max/v_min is <lambda-1. Then

A_{L,N} v >=lambda' v, for some lambda'>1.

The same path reversal proves A_{L,N} self-adjoint on L2(K,pi): restricting internal types to L and the number of outside ancestors to N preserves the symmetry. The pointwise inequality gives <A_{L,N}v,v>_pi>=lambda' ||v||_pi^2. By the Rayleigh characterization its top positive eigenvalue lambda_{L,N} is at least lambda'>1. The positive-kernel argument of Section 5 produces a continuous positive eigenfunction w, bounded above and away from zero. No spectral-continuity theorem for nonsymmetric operators is needed.

The truncated return process survives with positive probability, from every K type. Here is a proof rather than an appeal to a multitype extinction theorem: if X_j=sum w(type) in generation j, Y_j=lambda_{L,N}^{-j}X_j is a nonnegative martingale. Uniformly bounded offspring and w imply

Var(X_{j+1}|F_j) <=C Z_j <=C X_j/w_min.

Therefore E[(Y_{j+1}-Y_j)^2] <=C' w(s)lambda_{L,N}^{-j-2}. This is summable, so Y_j is bounded in L2 and converges in L2 with E Y_infinity=w(s)>0. Thus Pr(Y_infinity>0)>0. Extinction implies Y_infinity=0, proving survival. The bounds are uniform in the starting K type.

All vertices retained in this truncated return construction have threshold <=b_L. Each accepted original edge along its return paths has cost <=its parent's threshold, hence <=b_L. The entire surviving subprocess is consequently contained in the cutoff EWT T(b_L). Its embedded return edges stand for finite original paths; infinitely many return vertices are infinitely many distinct original vertices. This proves that when rho>0, a finite cutoff t0 exists with positive ordinary-process survival from every K type. The EWT root has a positive chance to reach K at a cost less than min(a,t0), so rho_{t0}>0 as well.

## 7. Survival continuity, with no exponential-moment assumption

For a non-root type s=(m,x) let e_t(s) be the extinction probability under cost cutoff t, and e(s) for the full process. Couple the trees by their actual candidate costs, so e_t decreases with t and e_t>=e. Its generating equation is

e_t(m,x)=[1-integral h_t(x,z)(1-e_t(r,z)) mu(dr,dz)]^m,
h_t(x,z)=min(t,x,z)/x.

Let e_*(s)=lim_{t->infinity} e_t(s). Dominated convergence shows e_* is a fixed point of the full generating operator. If rho=0 the root's cutoff survivals are all zero and continuity is immediate. Suppose rho>0 and use K,t0 from Sections 5-6. Since e_*(s)<=e_{t0}(s)<1 for all s in K,

J=integral_K (1-e_*(u)) mu(du)>0.

For s=(m,x) in K, m>=1 and h(x,z)>=a/b on K. The full fixed-point equation therefore gives

e_*(s) <=1-(a/b)J =1-c, with c>0 uniformly on K.

The full fixed-point identity can be iterated while stopping lines at their first K descendants. The outside family is finite almost surely, so bounded convergence gives

e_*(s)=E_s product_{first K returns u} e_*(u).

For s in K this uses strict returns; for outside s it uses the first-hit forest. Empty products equal one. Thus restriction e_*|K is a fixed point of the return generating operator. Iterate it through j return generations. On extinction of the return process its generation is eventually empty and the product equals one. On survival, Z_j ->infinity by Section 5, and the product is <=(1-c)^{Z_j}->0. Dominated convergence gives e_*|K equal to the return extinction probabilities. Starting from any other finite ordinary type, its finite stopped outside family gives the same first-hit product, so e_*=e on all ordinary types.

For the EWT root, conditional on root potential D=d and threshold x, extinction is the same slot integral raised to d. The root threshold law is Gamma(d+1). D is finite almost surely; all integrands are bounded by one. A final dominated-convergence argument over d,x therefore proves

rho_t increases to rho as t tends to infinity.                 (7.1)

This is exactly where a generic infinite-type branching process could fail. Here finite mean provides epsilon<1 outside a compact set, and the uniformly nonsingular compact return process prevents the missing fixed-point limit from being the all-one function. Neither property is assumed without proof.

## 8. Conclusion

Section 4 gives the lower bound by each rho_t. For any tolerance u>0 choose t with rho_t>rho-u/2 by (7.1), then eta<u/8. The probability that L1/n<rho-u tends to zero. Combine with the prior attempt's upper bound in probability to obtain L1/n ->rho. Since 0<=L1/n<=1, expectations converge too. The finite-cutoff local-limit argument and sprinkling are valid for the source's deterministic budget arrays with weak empirical limit P; the analytic tree argument depends only on P's finite first moment. Thus the same conclusion holds for those arrays, even if their empirical first moments do not converge.

The proof was recorded provisionally before the audit in Section 9. The final audited verdict follows below.


## 9. Hostile audit: checks and attempted failure modes

1. Temporal monotonicity is specific to increasing cost time. Resampling cheap edges is not monotone and is never used for sprinkling. Preference capacity counts rejected arrivals too.
2. Activity cannot be read off accepted degree or just the source's threshold mark. Section 1 augments via the full ER arrival graph H_n(t), giving exactly the missing information.
3. The active-leaf event is evaluated BEFORE acceptance against fresh child variables. Conditional-on-acceptance offspring laws are biased; the proof never replaces them by an unbiased law after conditioning. On the motif event, acceptance is automatic.
4. Coverage is not an unproved density law within each giant. It is a deterministic count of bounded-degree balls, applied simultaneously to all macroscopic unions after controlling the TOTAL uncovered mass.
5. Unbounded degrees are handled by covered paths through a low-H-degree induced subgraph. No global degree bound is imposed on P or on the finite graphs.
6. The small time interval can depend on t, eta and the coverage parameters. Its constants may be extremely poor. The proof makes an asymptotic statement and claims no uniform quantitative giant threshold.
7. Every current active cross pair must still have an unseen edge. Otherwise that edge was accepted earlier, contradicting the no-cross event. This supplies exact conditional clock rates, rather than incorrectly conditioning independent edge probabilities on random rank thresholds.
8. The global arrival cap is counted once, outside the partition union bound. For each partition the stopping time kills at either a cross edge or excess arrivals; its survival hazard is at least the cross rate. Conditioning on the cap as if the clocks stayed independent would be incorrect and is not done.
9. Large-component partitions count only at most n/k old components, not 3^n arbitrary vertex partitions. Initial components remain intact under time evolution.
10. Infinite-type truncation can fail in a deterministic shifting-type process. Here the killed-outside potential contracts by epsilon<1 because integral m mu is finite. This is checked before using any compact approximation.
11. Compact return offspring need not have a second moment. Subcritical extinction uses only a bounded positive eigenfunction and a uniform zero-offspring probability. L2 survival is applied ONLY after restricting excursion depth and all potential child counts, yielding bounded offspring.
12. The source's Theorem A.7 was not applied to a nonsymmetric kernel. The weighted measure pi=mu/(m/x) makes the return-path kernel symmetric; Section 5 proves the positive eigenfunction from the ordinary compact self-adjoint spectral theorem. Excursion truncations preserve path reversal.
13. Return vertices are first K hits. Their descendant subtrees are independent given type because deciding the stopping line uses type and incoming edge, not that vertex's future outgoing variables. Finite stopped families make both the branching property and fixed-point stopping identity valid.
14. The cutoff-continuity argument is not an exchange of increasing events without proof. It first finds a bounded-cost surviving subprocess, then identifies the limiting fixed point using a uniform gap on K and divergence of the return population on survival.
15. The special root law is Gamma(D+1), rather than Gamma(D). Section 7 integrates its separate slot expression after proving ordinary-type convergence.

Computational checks: second_checks.py verifies 458,753 ordered-composition/tolerance instances of the finite partition argument. A finite-type proxy of the EXACT slot reproduction mechanism (independent candidate type, acceptance min(x,z)/x) has full mean radius 1.57849, return radius 2.02465 and outside potential contraction epsilon=0.623046. Return truncations converge from below; The primary compact restriction already has supercritical direct reproduction; the additional stress case below checks a subcritical direct restriction. The proxy is not a simulation of the original continuous-type EWT and is not counted as proof. Active-leaf probabilities were independently simulated with 100,000 fresh candidates for each budget 2,3,7 and cutoff 1,3,6; all nine estimates lie within six binomial standard errors of exp(-t). Results are in second_checks.json.

coverage_checks.py builds three original symmetric-cost graphs on 1,536 vertices with budget three, records cutoff components at t=2,4,6,8, activity from ALL arrivals, and uncovered large-component mass at radii 0,1,2,4,8,16 in the H-degree<=12 induced subgraph. It also checks compact-complement potential for the explicit finite-mean/infinite-variance law D=2+Y, Pr(Y=j)=j^-2.5/zeta(2.5). The compact complement has weighted mass <1 for the tested large compact sets, consistent with Section 5. Numerical data are in coverage_checks.json. These jobs use well under 1 GB and seconds to minutes.

Formal verification: Capacity.lean checks the deterministic inequality that two initial a*n capacities losing at most 2*delta*n each, with 4*delta<=a, leave cross-pair product at least (a*n)^2/4. It does not formalize the stochastic process, the continuum branching process, or the spectral theorem.

Capacity.lean passed ordinary Lean kernel verification, exit code 0. Its command and hash are saved in lean_capacity_check.json. This confirms only the finite capacity inequality, not the full theorem.


The additional return_stress.py test uses a smaller compact set: outside potential epsilon=0.980965<1, direct mean radius 0.991811<1, and full return radius 3.93745>1. Allowing one outside ancestor already raises the truncated return radius to 1.42247>1. Weighted symmetry residual is 2.22e-16; all tested truncations preserve symmetry. Results: return_stress.json. This tests the case where direct compact offspring do NOT already establish survival.

For completeness, the stopped-hazard bound in Section 4 can be written with no informal clock conditioning. Conditional on the past, keep the finite Markov state of seen edge pairs, counters and accepted cross-edge flag, with an absorbing state at a cross acceptance or at excess arrivals. For every nonabsorbed state, at least (a n/2)^2 unseen cross pairs have active endpoints and each fires at rate 1/n. If q(u) is probability of nonabsorption by interval time u, the finite forward equations give q'(u)=-sum_x Pr(state x and nonabsorbed at u) k(x), where k(x) is the absorption rate from x. Thus q'(u)<=-(a^2 n/4)q(u), q(0)=1, and q(delta)<=exp(-delta a^2 n/4). The arrival cap has not been conditioned upon; it is part of this absorbing process.

An exhaustive separate check of the unseen-cross-pair fact was run on K4: every one of the 81 positive budget vectors in {1,2,3}^4, all 720 edge arrival orders, and all seven prefixes. At every state, two active vertices in different accepted components have an unseen edge. This is 408,240 prefix states and 2,449,440 pair checks. Results: arrival_history_checks.json. The proof of this fact remains the monotonicity argument in Section 4; enumeration is an independent finite check.

## 10. Final verdict and theorem

VERDICT: SOLVED (author-audited complete proof, 2026-10-12).

For every law P on the positive integers with finite first moment and P(1)<1, the largest component of the La--Kabkab bilateral-preference graph with IID P budgets and IID symmetric continuous costs has vertex fraction converging in probability to the EWT survival probability. The same conclusion holds for the source's deterministic budget arrays with weak empirical limit P and di<=n-2. Convergence of expected vertex fractions follows by boundedness. The case P(1)=1 also holds directly, with fraction zero.

The matching lower bound is proved by Sections 1-4 and 5-7; the known upper bound is written rigorously in ATTEMPT.md Sections 1-3 of the first attempt. No exponential moment and no growing-budget connectivity theorem are used. There is no remaining mathematical gap identified in the audit. The Lean certificates verify finite algebra only; the probabilistic and analytic proof is the written proof above. This is an original proof in this folder, not a claim of a matching solution found in print.

Cost-law clarification: the proof uses Exp(rate 1/n), exactly as in the source. For any other IID continuous cost law, the probability-integral transform followed by u -> -n log(1-u) preserves all finite preference ranks almost surely and gives IID Exp(rate 1/n) costs. Hence the retained graph has the same distribution. Activity and time are used after this transform. This justifies the continuous-cost formulation of the theorem.
