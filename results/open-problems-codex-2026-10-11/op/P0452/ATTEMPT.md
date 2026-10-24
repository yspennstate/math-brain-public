# P0452 research record

Final verdict, 2026-10-12: SOLVED. The complete matching lower-bound proof is in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md), Sections 1-10. It applies to fixed positive-integer budget laws with finite first moment, and to the source's deterministic arrays with weak empirical limit. This supersedes the first attempt's PARTIAL verdict and its coalescence gap.

The second attempt recorded two new approaches: temporal coagulation, and local active-vertex coverage with time sprinkling. The latter was pursued to completion. Compact-return branching-process arguments establish survival continuity with only a finite first moment. The lower bound combines with the first attempt's upper bound below.

## First-attempt record (historical; partial conclusion superseded)


2026-10-12. Target: for fixed P on positive integers with finite mean and P(1)<1, IID budgets Di~P independent of IID continuous symmetric edge weights, retain edge ij iff its rank at i is <=Di and at j is <=Dj. Show L1(Gn)/n -> rho(P)=Pr(|Er(P)|=infinity) in probability. Work also with deterministic budgets when explicitly stated. No growing-budget connectivity theorem is used.

Current route: prove concentration of the total mass in components of size at least k by a pivotal-probability Efron--Stein argument; reduce the remaining supercritical problem to a pairwise coalescence condition. Investigate whether cost sprinkling supplies it without invalid independence assumptions.

## 1. A finite sensitivity lemma

For an arbitrary graph H on n vertices, put F_k(H)=sum_C |C| 1{|C|>=k}, for integer k>=1. Adding or deleting one edge changes F_k by at most 2(k-1). Proof: addition either leaves the components unchanged or merges components of sizes a,b. If both a,b>=k the change is zero; if exactly one is >=k, the change is the other size <=k-1; if both are <k the change is either zero or a+b<=2(k-1). Deletion is the reverse operation. Thus a symmetric difference of r edges changes F_k by at most 2r(k-1).

With budgets fixed, changing only the weight of edge ij changes the top-di list only at i and the top-dj list only at j. Each list either stays the same or replaces ij with one other edge (or the reverse). Thus their preferred-edge symmetric differences have sizes at most two each; the mutual graph differs in at most four edges. Consequently |Delta F_k|<=8(k-1).

If ij is absent from the preferred lists of both endpoints both before and after resampling, no list changes. For IID continuous edge weights every rank is uniform, so the probability that resampling ij can change the graph is at most 2(di+dj)/(n-1), with the union bound understood even if its RHS exceeds one. Use truncated budgets di<=n-1. Summing over unordered pairs gives at most 2 sum_i di.

## 2. Concentration of large-component mass (proved)

Conditional on deterministic budgets d, Efron--Stein for independent edge weights and the preceding bounds gives

Var(F_k(G_n)|d) <= (1/2) sum_{i<j} [8(k-1)]^2 Pr(change at ij | d)
                    <= 64(k-1)^2 sum_i di.                 (2.1)

In particular F_k/n concentrates about its mean for deterministic arrays with sum_i di=o(n^2), including all arrays with bounded average budget. In fact weak convergence of the empirical budget laws is enough: for every fixed M, sum_i di/n^2 <= M/n + n^{-1}#{i:di>M}. Weak convergence on the positive integers gives limsup_n sum_i di/n^2 <= P(D>M), and tightness lets M tend to infinity. Therefore the concentration conclusion holds for ALL deterministic arrays in the source theorem, without uniform integrability of their empirical first moments. This strengthens annealed local convergence to fixed-k concentration, but does not imply a giant lower bound.

For IID untruncated budgets D_i~P with finite mean mu, independent of edge weights, write g(d)=E_weights F_k. Resampling D_i to an independent D_i' changes the preferred list at i by at most |D_i-D_i'| edges; the graph can therefore differ in at most that many edges. Hence

|g(D)-g(D^(i))| <= min(2(k-1)|D_i-D_i'|, n).

Clipping budgets at n-1 can only decrease this bound. Conditional variance (2.1) has expectation at most 64(k-1)^2 n mu. Efron--Stein applied to g, and total variance, give

Var(F_k/n) <= 64(k-1)^2 mu/n
            + (1/(2n)) E[min(2(k-1)|D-D'|,n)^2].          (2.2)

For k=1 the variance is zero. For fixed k>1 set X=2(k-1)|D-D'|. Then E X<infinity and min(X,n)^2/n <= X, while the LHS integrand tends to zero for each finite X. Dominated convergence proves that the second term tends to zero, without a second-moment assumption on P. Thus F_k/n-E(F_k/n)->0 in L2.

By Theorem 2.1 of the source, E(F_k/n)->p_k:=Pr(|Er(P)|>=k). The event is determined by the radius k-1 unmarked ball: a connected graph with >=k vertices has at least k vertices within that radius, and the converse is immediate. It is an open-and-closed event in the unmarked local topology (integer radius and exact graph structure); forgetting marks preserves the relevant local convergence. Thus

                  F_k(G_n)/n -> p_k in probability and L2.       (2.3)

For IID budgets, application of the deterministic source theorem can be justified by coupling all n through a single IID sequence: the empirical budget law converges almost surely; clipping affects a vanishing fraction. Apply the deterministic theorem along every such sample and bounded convergence. The n-1 threshold convention may be avoided by clipping at n-2: expected number of samples D_i>=n-1 is <=n Pr(D>=n-1)=o(1), since P has finite mean. Hence this distinction disappears with high probability.

Since p_k decreases to rho, and L1/n <=F_k/n+(k-1)/n, (2.3) implies the upper bound in probability: for every epsilon>0, Pr(L1/n>rho+epsilon)->0. If rho=0, it proves L1/n->0, and boundedness gives L1/n->0 in L1 as well. This proves the target equality throughout the extinction regime.

## 3. Exact coalescence criterion (proved reduction; hypothesis unproved)

Define

Q_{n,k} = n^{-2} sum_{C != C', |C|,|C'|>=k} |C||C'|,

where pairs are ordered. Equivalently, E Q_{n,k} is the probability that two independent uniform vertices fall in different components, each of size >=k. Write S=F_k/n, and M=max_{|C|>=k}|C|/n (M=0 if no such component). If a_C=|C|/n over large components, then

Q = S^2-sum_C a_C^2 >= S^2-M S = S(S-M).          (3.1)

The inequality follows term by term from 0<=a_C<=M. Also |M-L1/n|<k/n.

For this fixed finite-mean IID model, and also for the deterministic arrays in the source theorem, the following are equivalent:

(A) L1/n ->rho in probability.
(B) lim_{k->infinity} limsup_{n->infinity} E Q_{n,k}=0.      (3.2)

Proof B=>A: rho=0 was already established. If rho>0, fix epsilon in (0,rho). For fixed k, (2.3) yields Pr(S<rho-epsilon/2)->0 since p_k>=rho. On {L1/n<rho-epsilon, S>=rho-epsilon/2}, M<=L1/n and hence S-M>epsilon/2, so Q>= (rho-epsilon/2)epsilon/2. Markov's inequality bounds the limsup probability of this event by limsup E Q divided by that positive constant. Let k tend to infinity using B. Combine with the upper bound to prove A.

Proof A=>B: for rho=0 use Q<=S^2, so lim_n E Q<=p_k^2 and p_k->0. For rho>0 and fixed k, M-L1/n->0 and M->rho. Furthermore sum a_C^2>=M^2, so Q<=S^2-M^2. Bounded convergence in probability gives limsup_n E Q<=p_k^2-rho^2. Let k tend to infinity. This proves B.

In particular, merely proving L2/n->0 is not enough: mass could be spread over many mesoscopic components. Condition B controls all such dispersed mass.

## 4. A concrete extinction special case (proved)

If E_P D<=2, then rho(P)=0; consequently L1/n->0 in probability and L1 for the fixed-law model.

Proof. The unpruned EWT backbone has finite root offspring D and IID non-root offspring N=D-1. If E N<1, the expected number of backbone vertices in generation l is E D (E N)^(l-1), which tends to zero. The probability that generation l is nonempty is bounded by this expectation, proving extinction. If E N=1 and N is not identically one, its probability generating function f satisfies f(s)>s for 0<=s<1. Indeed s^m>=1+m(s-1) for every integer m>=0, with strict inequality for m>=2 and s<1, and P(N>=2)>0 in the nonconstant mean-one case. Taking expectations gives the strict inequality. Iteration f^l(0) increases to a fixed point q by continuity, and its only fixed point in [0,1] is one. It equals the probability of extinction by generation l. Each of the root's finitely many descendant trees therefore dies almost surely, so pruning also dies.

The sole exception to that backbone argument is D=2 a.s.: it consists of two infinite rays from the root. Along each ray, the non-root thresholds V_j are IID Erlang(2), and the edge to its sole potential child has cost U_j V_j with independent U_j~Uniform[0,1]. Edge j survives iff U_j V_j<V_{j+1}. On the disjoint pairs j=1,3,5,..., the events

V_j>=2, U_j>=1/2, V_{j+1}<=1

are independent and have the same strictly positive probability delta. Every such event rejects its edge (equality has probability zero). The probability all edges on the ray survive is at most (1-delta)^r for every r, hence zero. The root has only two rays, proving rho=0 also here. D=1 a.s., excluded by the source's nontriviality assumption, is an immediate boundary case with components of size at most two.

## 5. Why naive sprinkling is not yet a proof

Increasing budgets coordinatewise is monotone, but decreasing a single edge cost is not monotone for the retained graph: it may displace another edge from either endpoint's top list. Thus independent new cheap edges cannot simply be added to this model while retaining an old giant candidate. Revealing all weights below a deterministic time t does give a monotone-in-time accepted-edge process: an edge at time w is retained iff each endpoint has seen fewer than its budget edges before w, counting all arrivals, even ones rejected by the opposite endpoint. Later arrivals do not remove earlier accepted edges. However joining large components after t requires many vertices in those components whose arrival counters are below budget; this is not supplied by local survival alone. In particular a budget-two component can have only two available endpoints. No uniform linear lower bound on available endpoints has been proved here in the supercritical regime. A conditional ER coupling based on vertex thresholds would be invalid: thresholds depend on precisely the cross-edges one proposes to sprinkle.

The remaining gap is to prove (3.2)(B) for rho>0 under the stated fixed-distribution hypotheses (or find a counterexample in this exact model). No model counterexample has been found. The criterion and concentration results do not fill this gap.

## 6. Extensions and scope audit

For deterministic arrays with weak empirical convergence to P and di<=n-2, Section 2's tightness argument and Theorem 2.1 give (2.3) directly. Thus the upper bound in probability, the extinction-regime equality, and the coalescence equivalence apply to the source's deterministic-array formulation too. No assumption of convergence of the average budgets is needed. This distinction matters because weak convergence alone does not control empirical first moments.

When IID P has finite variance, (2.2) also gives the explicit bound

Var(F_k/n) <= (k-1)^2 [64 E D + 4 Var(D)]/n.

Indeed E(D-D')^2=2 Var(D) and one can discard the minimum in (2.2). For growing k=o(sqrt(n)) this still controls fluctuations about the expectation. It does not give a uniform approximation of that expectation by p_k; the source theorem only treats fixed k.

All probabilistic assertions here use convergence in probability unless an L1/L2 mode is explicitly stated. The source's informal statement on p.10 that extinction gives an O(1) largest component with high probability is not used; local convergence justifies a vanishing vertex fraction, not a bounded component size. The source Corollary 2.2 uses informal O(1) language; the rigorous fixed-k/double-limit formulation is used throughout this attempt.

The pairwise criterion in Section 3 is the same general mechanism as Remco van der Hofstad's almost-local giant criterion. Its short proof here makes all assumptions explicit; no novelty is claimed for this general reduction. It is not a theorem asserting the criterion holds for the La--Kabkab model.

## 7. Direct logarithmic bound when all budgets are at most two (proved)

This is a finite-model bound, stronger than a vanishing giant fraction. For ANY deterministic budgets di in {1,2}, and IID Exp(rate 1/n) edge costs, for every fixed c>2/log(2),

       Pr(L1(G_n) >= ceil(c log n)+1) ->0.                 (7.1)

All logarithms are natural. IID laws supported on {1,2} inherit the same uniform bound. It also covers the boundary D=2 a.s. without any local-limit argument.

Proof. Fix an ordered list of l+1 distinct vertices, with l>=3 and l+1<n, and denote its l path-edge costs x1,...,xl. If this is a retained path, then each of its l-1 internal vertices prefers both adjacent path edges. Since its budget is at most two, every one of its n-l-1 edges to vertices outside the list must have cost greater than max(x_i,x_{i+1}). These outside-edge sets are disjoint across the internal vertices, hence the corresponding costs are independent. Extra chords among the selected vertices can only impose more restrictions and are ignored.

Set alpha=(n-l-1)/n. Conditional on the path-edge costs, the probability of these necessary outside restrictions is

    exp(-alpha sum_{i=1}^{l-1} max(x_i,x_{i+1})).

The joint density of path-edge costs is n^{-l} exp(-sum_i x_i/n), which is bounded above by n^{-l}. Therefore the expected number X_l of ordered retained simple paths of length l is at most

    n I_l(alpha),
    I_l(alpha)= integral_{[0,infinity)^l} product_{i=1}^{l-1}
                      exp(-alpha max(x_i,x_{i+1})) dx.

Define the symmetric integral operator K_alpha on L2([0,infinity),dx) with kernel exp(-alpha max(x,y)). Its Hilbert--Schmidt norm is

    ||K_alpha||_HS^2 = 2 integral_0^infinity y exp(-2 alpha y)dy
                     = 1/(2 alpha^2).

Consequently ||K_alpha||_{2->2} <=1/(sqrt(2) alpha), by Cauchy--Schwarz in the kernel integral. Integrating the first and last coordinates of I_l gives

    I_l(alpha)=<f_alpha, K_alpha^(l-3) f_alpha>,
    f_alpha(x)=integral_0^infinity exp(-alpha max(x,y))dy
              =exp(-alpha x)(x+1/alpha).

This use of the nonintegrable constant function is harmless because the endpoint integrals are evaluated first by Tonelli; f_alpha is in L2. Direct integration gives ||f_alpha||_2^2=5/(4 alpha^3). Thus

    E X_l <= n [5/(4 alpha^3)] [1/(sqrt(2) alpha)]^(l-3).  (7.2)

Take l=ceil(c log n). Then alpha->1 and alpha^{-(l-3)}=exp(O(l^2/n))->1. The RHS is O(n^{1-c log(2)/2}), tending to zero for the stated c. Since the retained graph has maximum degree two, each connected component is a path, a cycle, or a singleton. A component with at least l+1 vertices contains a simple path of l edges, even if the component is a cycle. Markov's inequality and (7.2) prove (7.1).

Checks of possible failure points: outside edges from two distinct internal path vertices are distinct unordered pairs because their other endpoints lie outside the entire selected list; all are independent of the path costs. The necessary restriction uses a budget of AT MOST two; for budget one the two-path-edge event is impossible. Omitting chord restrictions and the exp(-sum x_i/n) density factor increases the upper bound. The diagonal in the Hilbert--Schmidt integral has Lebesgue measure zero. No independently sampled preference orders are substituted for the symmetric costs.

## 8. Computation and hostile-referee audit

`checks.py` exhausts all simple graphs on five vertices, all one-edge toggles, and k=1,...,6: 61,440 cases of the F_k one-edge inequality. It then exhausts every order of the six weights on K4, every budget vector in {1,2,3}^4, and every relocation of each edge to every rank: 2,099,520 cases. All satisfy the four-edge graph-change bound and the corresponding mass sensitivity bounds. Results: finite_checks.json. These are checks of finite claims; they do not prove a stochastic limit.

`simulate.py` uses seed 4521012 and symmetric IID uniform costs (equivalent rankings to exponentials). Laws: D=2, D=3, and Pr(D=1)=0.6, Pr(D=5)=0.4. Each law uses n=256,512,1024,2048 with eight independent graphs per n. Exact top-budget selections are intersected at both endpoints, then components are computed by union-find. S_k and Q_{n,k} are measured for k=16,64,256. Separate EWT samples use the source's gamma thresholds, uniform candidate costs and bilateral pruning, stopping once k vertices have been found; 3,000 independent samples per law/k. Runtime about 108 seconds; maximum arrays are for n=2048, well under 1 GB. All rows are saved in simulation_results.json.

At n=2048, mean largest fractions were 0.01056 (D=2), 0.89142 (D=3), and 0.32520 (mixed law). EWT estimates of Pr(|T|>=256) were 0/3000, 0.88100, and 0.32033 respectively. The nonzero estimates have binomial Monte Carlo standard errors approximately 0.00591 and 0.00852. A zero empirical estimate is not a proof of zero probability (its one-sided 95% binomial upper bound is about 0.001). The small number of graph samples and finite n cannot verify the double-limit coalescence criterion. Independent estimates at different k need not be empirically monotone. They are consistent with the claimed connection, not evidence sufficient to establish it.

`path_integral_checks.json` checks Section 7 by an independent exact calculation: partition the l-dimensional integration region into its l! coordinate-order simplices for l=3,...,8. For each ordering, let c_r count adjacent pairs whose larger coordinate has rank r. Express ordered coordinates as nonnegative spacings; its integral is the product over spacing indices j of 1/(sum_{r>=j} c_r). Sum these rational values using Python Fraction. Obtained I_l(1): 5/4, 23/27, 677/1152, 7313/18000, 218491/777600, 863897/4445280. Every squared value satisfies I_l(1)^2 <= (25/16) 2^{-(l-3)} exactly; this independently checks the Hilbert--Schmidt bound and endpoint integrations for these finite l. The proof in Section 7 covers all l.

Referee checks:

1. Thresholds are dependent on incident costs. All proofs retain these dependencies; only disjoint underlying weights are treated as independent.
2. Resampling one weight can alter preferences at both ends and other retained edges. The four-edge symmetric-difference bound accounts for this; a one-edge Lipschitz assumption would be false.
3. A finite mean is not a finite variance. Equation (2.2) uses a truncated square and dominated convergence, with no second-moment inference.
4. Weak empirical convergence is not average-budget convergence. The deterministic proof uses tightness and di<=n-1, yielding sum di=o(n^2), which is enough for concentration.
5. The giant criterion requires a double limit in k,n; no fixed-k or finite simulation has been substituted for it.
6. Extinction of the backbone fails for D=2 a.s.; that exception is treated by independent rejection opportunities along each ray, and directly by Section 7.
7. Full EWT survival is not automatic survival below a finite cost cutoff. No such interchange of infinite-cluster and cost-cutoff limits is asserted here.
8. No independent-edge theorem is applied conditional on the random preference thresholds.
9. Formal verification covers the finite algebra (3.1) only, not Efron--Stein, local convergence, branching extinction, or coalescence in this model. Lean check result is recorded separately below when available.

Read-only research provenance: recalled the topic and topic mistakes through brain.py; recalled EWT cards, followed the previous-attempt card by ID, and searched the math store for almost-local giant results. The earlier attempt's mesoscopic-cycle example is an obstruction for general local limits, not a counterexample for this model. Intake-ledger P0452 entries were searched and agree with that previous attempt. A read-only origin/master path listing in math-open-problems found no P0452/EWT-specific answer path; its working tree was not changed.

Final mathematical gap: prove lim_{k->infinity} limsup_{n->infinity} E Q_{n,k}=0 for supercritical La--Kabkab graphs under the fixed-law/source-array hypotheses. The available-endpoint argument described in Section 5 is a possible route, but it is not proved. Thus the requested general lower bound is NOT solved by this attempt.

### Concrete next research route (unproved)

A possible way to establish the pairwise criterion is to grow two explorations to n^a vertices for some a in (1/2,1), with a linear number of frontier vertices still having preference capacity in a fixed nonempty cost interval. If the relevant cross costs remain unrevealed, there are order n^{2a} candidate pairs, each with order 1/n chance of an acceptable cross edge. The expected number would diverge. This is only a proposed route: one must prove quantitative exploration domination despite previously revealed rank inequalities, prove the frontier-capacity density, and justify the conditional cross-edge law. A fixed-depth local convergence proof supplies none of those quantitative claims. Neither this argument nor a cost-cutoff survival continuity claim is counted as proved.

Lean verification log: initial invocation reached a shared slot after 930 seconds, then failed before elaboration because `Mathlib.Tactic.Nlinarith` is not an installed module name. Corrected the import to `Mathlib.Tactic.Linarith` (which provides nlinarith); the second invocation is queued. No theorem is described as Lean-checked until that invocation succeeds.

## 9. Quantitative collision estimate from the source exploration (proved bounded-budget reduction)

In Appendix B, Lemma B.4, PDF pp.75?78, the source explores vertices v_l and defines J_l to detect repeatedly touched potential neighbors. Its conditional estimate on p.78 gives, before termination,

Pr(J_l empty | F_{l-1}) >= [max(0,1-(l+sum_{i=0}^l d_{v_i}+2)/n)]^{d_{v_l}+1}.

If all budgets are <=B, put A_l=((B+1)l+B+2)/n. The RHS is at least max(0,1-A_l)^{B+1}. For 0<=A_l<=1 Bernoulli's inequality bounds one minus this expression by (B+1)A_l; for A_l>1 the same upper bound remains valid since it exceeds one. The union bound used by the source therefore yields, for its exploration up to t steps (or its stopping time tau),

Pr(exists l<=t wedge tau with J_l nonempty)
 <= [(B+1)/n] [(B+1)t(t+1)/2 + (B+2)t].       (9.1)

This is a direct complete derivation from the source's conditional inequality and is uniform for bounded-budget arrays and t within the defined finite exploration. It shows collision-free exploration with high probability when t=o(sqrt(n)) and B is fixed. It does NOT supply a quantitative coupling of all marks to independent EWT marks, and does not imply a giant lower bound.

It identifies an explicit barrier to the proposed two-frontier argument: keeping the entire exploration collision-free requires t below sqrt(n) with this estimate, whereas direct joins between two similarly sized frontiers need sizes above sqrt(n). One would need a growth argument tolerating a vanishing proportion of collisions, rather than demanding none, in addition to the unproved capacity and conditional cross-edge lemmas.

Lean second invocation failed because PowerShell pipeline encoding had replaced Unicode tokens by question marks. Rewrote the certificate using ASCII shell text with Python Unicode escapes; also replaced the local quadratic inequality tactic with its direct ordered-multiplication proof. Third invocation checks the corrected UTF-8 file.

Statement-mode clarification: Section 4 question 3 states the proposed giant/extinction relation informally without explicitly prescribing a mode of convergence; Corollary 2.2 phrases its upper bound in expectation. This attempt works on the conventional convergence-in-probability formulation of giant density, which implies convergence of expected fractions by boundedness. The deterministic-array and IID formulations are distinguished above.

## Final verification and verdict

2026-10-12: The corrected Coalescence.lean passed `lake env lean ~/brain_workers/TRIO_1011/op/P0452/Coalescence.lean` from ~/lean_verify, exit code 0. The file contains no sorry and no native_decide; ordinary Lean kernel checking validates the finite algebraic inequality (3.1). Certificate hash and command are in lean_check.json. Earlier failed invocations are documented above and are not counted as verification.

VERDICT: PARTIAL. Sections 1-4, 6-7 and 9 give complete proofs of auxiliary statements and special cases; Section 3 also gives an exact equivalence reducing the target to coalescence. The full positive-survival lower bound is still a conjecture here. No solution in print matching the exact problem was found in the bounded search, with the documented API/access limitations. This attempt is closed; a subsequent research attempt should address collision-tolerant exploration growth and unused-capacity density, or establish the pairwise coalescence criterion by another route.


# Second attempt, 2026-10-12 (reopened at user request)

The gap is the supercritical pairwise coalescence condition in Section 3. Two approaches not pursued in the first attempt:

A. Temporal coagulation: Poissonize edge arrivals, mark each vertex by its remaining preference capacity, and study clusters merging at rates proportional to their numbers of active vertices. This is related to Marcus--Lushnikov coagulation and aggregation with limited arms. A known theorem might yield gelation/uniqueness, but the active-vertex rather than remaining-arm rates and capacity loss to inactive vertices must be checked.

B. Local active-vertex coverage: at a fixed cost cutoff t, show every infinite local-limit component has an active vertex, where active means fewer than D incident costs have arrived. Then for a bounded degree graph, all but a small mass of vertices in large components lie within a fixed radius R of an active vertex. Each active vertex covers at most a fixed number of such roots, giving a linear active-vertex count in every macroscopic union of large components. Sprinkling in TIME is monotone and can join these unions by a union bound over at most 2^(n/k) partitions. Unlike the first attempt's two-frontier method, this does not require collision-free exploration of mesoscopic size.

Pursue B first. Unproved steps to audit: active coverage on the infinite cutoff EWT; convergence of marked finite graphs; preservation of active mass during sprinkling; survival continuity as t tends to infinity; unbounded-budget truncation. No claim of solution is made at this stage.

Brain queried directly for the gap: math_recall.py "pairwise coalescence giant component unused preference capacity collision tolerant exploration". It returned general random-graph and percolation hints, not a theorem establishing this model's coalescence.

Detailed second-attempt proof under audit: SECOND_ATTEMPT.md. Sections 1-4 propose a general lower bound by finite-cutoff survival using local active coverage and time sprinkling. Survival continuity is being treated via a compact return branching process rather than an exponential-moment assumption.

SECOND_ATTEMPT.md now contains a proposed complete proof: active coverage and time sprinkling, followed by compact-return survival continuity using only the finite first moment. Verdict remains PARTIAL while the new proof is audited. The brain supplied a warning about escaping types (card claim_384112882b609aee1c849c5d99f1162ea339ddf0fae347833267572ab6e22713); Sections 5-7 explicitly address that failure mode.


## Final second-attempt summary

The lower bound is now proved. At each finite cost cutoff, every infinite limit component has an active leaf somewhere almost surely. Bounded-degree-path coverage converts this local fact to a simultaneous linear active-count bound on all macroscopic unions of large components. Exact memoryless future clocks and a partition union bound join those unions during a short time interval. A compact return process prevents survival escaping through unbounded types: the outside potential contracts under the finite first moment, compact return kernels have weighted symmetry, and bounded excursions supply a surviving finite-cost subprocess. Identifying the limiting extinction fixed point then proves cutoff-survival continuity. The full proofs, including the operator and stopping arguments, are in SECOND_ATTEMPT.md.

No remaining mathematical gap was found in the hostile audit. The completed checks include 408,240 temporal arrival-prefix states, 458,753 partition cases, return-kernel symmetry and a subcritical-direct/supercritical-return stress example, original-model coverage simulations, and the fresh-child active-leaf identity. Capacity.lean passed ordinary Lean verification; it checks only the finite capacity-product inequality. All previous proof limitations remain as historical records, not current verdicts.

VERDICT: SOLVED.
