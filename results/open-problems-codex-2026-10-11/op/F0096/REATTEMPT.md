# F0096: second serious attempt

Date: 2026-10-12. The original ATTEMPT.md remains the record of the first attempt.

## Two approaches not previously tried

1. **Plant a Hamilton cycle and prove likelihood-ratio contiguity.** A planted model automatically has a Hamilton cycle. If the target law is contiguous with respect to the planted law, this would settle the conjecture. Its likelihood ratio is a normalized Hamilton-cycle count. First test the annealed planted degree law against the target; if degree bias destroys contiguity, freeze the degree vector and study conditional moments or reweight the planting. This directly attacks the missing existence estimate rather than trying to embed a cubic graph.
2. **Split high-degree vertices into cubic gadgets, with forced traversal constraints.** A degree-d vertex can be replaced by a tree of d-2 cubic vertices with d external half-edges; internal edges form a prescribed forest. Contracting this forest recovers the original graph. A Hamilton cycle using every forest edge would contract to a Hamilton cycle of the original graph. For d>=5 a branching tree cannot have all internal edges on a cycle, so path gadgets and suitable external-port restrictions are required. Even with path gadgets the split graph is not an unconstrained uniform cubic graph. Near the cubic endpoint, where only degree-four defects occur, the prescribed forest is a matching; a theorem on random cubic Hamilton cycles containing a prescribed matching might give a boundary special case. This must be verified, not inferred from ordinary cubic Hamiltonicity.

Approach 1 is selected: it yields an exact likelihood identity and directly exposes which second-moment estimate is needed. Approach 2 has an additional forced-traversal theorem before it can transfer even a boundary case. Neither was pursued in the first attempt, which computed only a first moment and the failure of spanning-cubic augmentation.

## Brain queries

Read-only math_recall.py queries:
- “Hamilton cycles prescribed degree sequence small subgraph conditioning Robinson Wormald Cooper Frieze”;
- “random graph minimum degree three Posa rotation expansion truncated Poisson Hamiltonicity”.
Returned cards concerned Dirac/Ore, unrelated Robinson arithmetic, and a useful warning that conditioning on a rare lattice event requires relative local control. No card resolved the Hamiltonicity gap. These are hints, not certificates.

## Work in progress

Compute the exact planted degree law, compare its limiting statistics with the target, and test the fixed-degree likelihood normalization on finite pairing spaces. Save each resulting identity and check below.

## Immediate referee correction: unconditional configurations cannot be Hamiltonian w.h.p.

ATTEMPT.md Corollary 4.5 is a logically correct sufficient implication, but its premise P(Q_n Hamiltonian)→1 is impossible for the stated unconditioned multigraph model. It should not be treated as a viable route to the conjecture.

For a fixed degree vector let L count loops at degree-three vertices. Each such vertex has three candidate pairs of half-edges. Then

E L = 3 n_3/(S-1),

E (L)_r = (n_3)_r 3^r / product_{j=0}^{r-1}(S-2j-1).

Proof: a degree-three vertex cannot contain two disjoint loops; select r distinct degree-three vertices and one of their three stub pairs each. The prescribed r disjoint pairs occur with the reciprocal denominator shown. Sum over ordered choices. If n_3/n→a>0 and S/n→mu, these factorial moments converge to kappa^r, kappa=3a/mu. Bonferroni inclusion-exclusion for the event L=0, first at a fixed number of terms and then letting that number grow, gives P(L=0)→exp(-kappa). The alternating Poisson series converges and brackets the limit. The bounds are uniform on typical degree vectors, so averaging over the degree law in ATTEMPT.md Lemma 4.3 yields the same result with a=p_3(lambda).

A degree-three loop leaves only one half-edge from that vertex to other vertices. A spanning cycle through distinct vertices requires two edges to other vertices when n>=3. Thus P(Q_n Hamiltonian)≤exp(-3p_3/(2c))+o(1)<1. At the cubic endpoint the loop-free upper bound is exp(-1). This is a multigraph obstruction, removed by conditioning on simplicity; it does not refute F0096.

Any corrected fixed-degree second-moment argument must handle these short-cycle obstructions before transferring a probability-one statement to the simple model.

## Exact planted likelihood and degree bias (proved)

Let S=2m, R=S-2n. Define P as the original degree-weighted configuration law Q_n in ATTEMPT.md (degree vectors have weight product 1/d_i! given their sum). Define P* as follows: sample residual degrees Y_i>=1 with weight product 1/Y_i! conditional on sum Y_i=R; set D_i=Y_i+2; sample a uniform Hamilton cyclic order independently; choose ordered predecessor/successor half-edges at each vertex uniformly; pair these along the cycle, and pair the remaining R half-edges uniformly. This is a planted Hamilton cycle, including stub labels. Let H denote the number of stub-realized Hamilton cycles in a configuration.

**Proposition R1.** dP*/dP=H/E_P H. After conditioning both laws on simplicity, dP*_simple/dP_simple=H/E_{P_simple}H, where H is the ordinary Hamilton-cycle count on the simple space.

**Proof.** A degree vector under P* has weight product 1/(d_i-2)!. A particular ordered stub assignment for a cycle has conditional weight reciprocal product d_i(d_i-1). Their product is product 1/d_i!, exactly the degree weight under P. The numbers of cyclic orders and residual/full pairings depend only on n and S, not the vector. Each matching under P* can arise once for each of its H stub-realized Hamilton cycles. Thus its likelihood relative to P is a constant times H. Summing over all matchings identifies that constant as 1/E_P H. Conditioning on simplicity restricts the same identity to a subset and renormalizes by E[H | simple]. This proves both statements. The label-count cancellation is exact; no asymptotic contiguity is assumed.

As n→∞ with S/n→mu=2c>3, the target degree law has limiting probabilities

p_j=lambda^j/(j! f_3(lambda)), j>=3, with lambda f_2(lambda)/f_3(lambda)=mu.

For every fixed j, the target empirical count n_j/n converges to p_j: the indicator fourth-moment proof in ATTEMPT.md Lemma 4.3 is independent of the particular fixed j (that lemma stated only j=3,4). In particular it applies to j=5 and to any fixed high-degree type used below. Its exponential indicator bounds follow from Hoeffding before total conditioning.

Under planting the limiting probabilities are

q_j=tau^{j-2}/((j-2)! f_1(tau)), j>=3, with tau e^tau/f_1(tau)=mu-2,

where f_1(tau)=e^tau-1. Existence and uniqueness of tau follow by the same variance-derivative argument as ATTEMPT.md Lemma 4.1, now with support starting at one. The degree concentration proof in ATTEMPT.md Lemma 4.3 applies unchanged to Y_i, since it used span one, a compact positive parameter interval, and uniform moments. Consequently the planted empirical degree counts converge to q_j before conditioning on simplicity.

**Lemma R2 (planting has positive simplicity probability).** P*(simple)→exp(-tau/2-tau^2/4-(mu-2))>0.

**Proof.** The residual configuration has degree vector Y_i, mean nu=mu-2, max degree o(sqrt(n)), and average factorial second moment E Y(Y-1)=tau^2 e^tau/f_1(tau). Therefore Janson Corollary 1.5, with Lambda=E Y(Y-1)/(2nu)=tau/2, gives its simplicity probability exp(-tau/2-tau^2/4)+o(1). The uniform planted cyclic order is independent of the residual configuration. The union is simple iff the residual graph is simple and none of its edges belongs to that cyclic order.

For completeness, fix any residual simple graph K with e(K)=nu n/2+o(n), maximum degree=o(n). Let Z be the number of K-edges in a uniform Hamilton cycle. For any r pairwise vertex-disjoint fixed edges, the probability that the cycle contains them is

2^r (n-r-1)!/(n-1)! ~ (2/n)^r.

This follows by contracting each edge into a two-vertex oriented block, choosing an undirected cyclic order of the n-r blocks, and dividing by the total (n-1)!/2 cyclic orders. The number of ordered r-tuples of distinct K-edges sharing a vertex is at most O_r(Delta(K) e(K)^{r-1})=o(n^r): choose a colliding pair (at most sum_v d_K(v)^2<=2 Delta(K)e(K)) and then the other r-2 edges. A non-disjoint tuple has probability zero if it forces vertex degree above two or a proper cycle; otherwise its edges form vertex-disjoint paths, and contraction gives probability 2^{number of paths}(n-r-1)!/(n-1)!=O_r(n^{-r}). Hence its total factorial-moment contribution is o(1). The disjoint tuples give E(Z)_r→nu^r. Bonferroni as in the loop calculation gives P(Z=0)→exp(-nu), uniformly along graph sequences meeting these hypotheses.

The typical residual degree bounds meet these conditions, and remain typical after residual simplicity conditioning because its probability is bounded below. Averaging the uniform-cycle avoidance result over the residual simple graph therefore multiplies its simplicity probability by exp(-nu). This proves the lemma. The independence here is of the vertex cyclic order and residual configuration after relabeling the remaining stubs; it does not claim independence of individual cycle edges.

**Theorem R3 (raw planting is asymptotically singular).** For each fixed c>3/2 the simple planted law and G(n,m;3) have total variation distance tending to one. Moreover the raw annealed Hamilton-cycle second-moment ratio for either the degree-random configuration law or its simple conditioning grows at least exponentially in n.

**Proof.** The limiting degree distributions p and q differ for all positive lambda,tau. Indeed, if p_j=q_j for j=3,4,5, their successive ratios would give lambda/4=tau/2 and lambda/5=tau/3, implying lambda=2tau=5tau/3, impossible for tau>0. Thus some j in {3,4,5} has delta=|p_j-q_j|>0. Choose a degree-count event A_n: |n_j/n-q_j|<delta/4. Under planting A_n has probability tending to one, including after simplicity conditioning by Lemma R2. Under the target A_n has probability tending to zero by ATTEMPT.md Lemmas 4.3-4.4. This separating event proves total variation tends to one.

To quantify the second moment, for large n the unconditional iid target indicator mean p_{j,n} differs from p_j by less than delta/8. The event A_n requires a deviation at least 5delta/8 from that mean, so even the weaker threshold delta/2 yields Hoeffding's bound 2 exp(-n delta^2/2). Conditioning on total degree costs only O(sqrt(n)) by the local limit estimate already proved, and conditioning on simplicity costs only a bounded factor. Thus either target law P has P(A_n)<=C sqrt(n) exp(-n delta^2/2). Its planted counterpart has P*(A_n)→1. With L=H/E_P H, Proposition R1 and Cauchy–Schwarz give

(P*(A_n))^2 = (E_P[L 1_{A_n}])^2 <= E_P L^2 P(A_n).

Consequently E_P H^2/(E_P H)^2 >= exp(n delta^2/2)/(4C sqrt(n)) for all sufficiently large n. This proves the exponential lower bound. Hoeffding's inequality is the standard bounded-independent-summand Chernoff bound; the proof uses it only before total-degree conditioning and explicitly accounts for that conditioning.

The theorem invalidates unweighted *annealed* planting as a route to contiguity. It does not invalidate the conjecture: target graphs can have many cycles while their counts still vary exponentially with their degree vectors. The parameter-dependent positive delta may be very small near c=3/2, so a tiny exponent need not be visible in small computations.

## Fixed-degree cycle-overlap second moment (proved exact identity)

Freeze a degree vector d_i>=3 with even S=sum d_i. Let R=S-2n and a_i=d_i-2. Plant a stub Hamilton cycle C_0. For an alternative stub cycle C let T be the set of *actual stub edges* shared with C_0, not merely equal vertex pairs. If T is a proper subset of the n cyclic edges, its components are paths and isolated vertices. Write k=|T|, r=n-k, p(T)=number of nonempty path components, and b_i(T)=number (0,1,2) of shared edges incident with vertex i.

**Proposition R4.** Conditional on this planted cycle and degree ordering,

F(d_1,...,d_n)=E[H | C_0 planted]

= 1 + sum_{T proper subset C_0, 2(n-|T|)<=R}
  [2^{p(T)} (n-|T|-1)! / 2]
  product_i (a_i)_{2-b_i(T)}
  / product_{j=0}^{n-|T|-1}(R-(2j+1)).

The 1 is C=C_0. The exact second moment of H under uniform pairings at this fixed labelled degree vector is

E H^2 = E H * average_{uniform labelled cyclic orders} F,

with E H as in ATTEMPT.md section 6.

**Proof.** For T proper, contract its path components into blocks. There are r blocks, and each of the p nontrivial paths has two possible orientations. Joining the blocks in an undirected cyclic order yields 2^p(r-1)!/2 possible completions before choosing residual stubs. At each vertex the remaining 2-b_i cycle incidences require distinct residual half-edges, giving the falling factorial shown. The r remaining edges must all be paired from the residual matching. They occur with probability reciprocal product_{j=0}^{r-1}(R-(2j+1)), and are impossible if 2r>R. They cannot use an unshared planted stub: its partner is already prescribed, and using it would make that planted edge shared. Thus every alternative cycle is assigned to exactly its actual shared T, even when a residual edge is parallel to a planted edge between the same vertices.

The completion factor also holds for r=1 and r=2. For r=1, T is a spanning path, p=1, and there is one way to close its two endpoints, giving 2/2=1. For r=2, at least one block is a nontrivial path since n>=3; orient the paths and divide the two opposite traversals of the resulting cycle by two. The ordered residual-stub assignments at singleton blocks distinguish its two incidences. There is therefore no exceptional extra factor of two. If T is full, the alternative cycle is exactly C_0, counted once.

Finally, for fixed degrees the planted measure has likelihood H/E H by the same counting proof as R1. All first-cycle cyclic orders have equal prior weight because product_i d_i(d_i-1) is independent of the order. Thus E H^2/E H equals the uniform-order average of F. This proves the identity.

The exponentially many subset weights are encoded by a two-state transfer matrix. Put

M_i(x) = [[a_i(a_i-1), 2a_i x], [a_i, x]],

W_k = coefficient of x^k in trace(product_i M_i(x)).

**Lemma R5.** W_k=sum_{T:|T|=k} 2^{p(T)} product_i (a_i)_{2-b_i(T)}.

**Proof.** Index each cyclic edge by its selection bit t_i. The factor at vertex i depends on (t_{i-1},t_i): for 00 it is a_i(a_i-1), for 01 it is 2a_i x, for 10 it is a_i, and for 11 it is x. Multiplying around the trace sums all cyclic bit assignments. Each selected edge contributes x once, and every transition 0→1 contributes a factor two. For a proper nonempty subset the number of such transitions is its number of path runs; for the empty or full subset it is zero. These are exactly the claimed weights. In particular W_n=1. This proves the lemma and reduces F to a sum over n coefficients, replacing all subsets by matrix-polynomial multiplication.

For degree multiset containing n_3 threes and n_4 fours, the average W is computable exactly without sampling cyclic orders. Let B_{a,b} be the sum of ordered matrix products over bit words with a threes and b fours. Then B_{0,0}=I and

B_{a,b}=B_{a-1,b} M_3+B_{a,b-1} M_4,

omitting a negative-index term. Divide trace(B_{n_3,n_4}) by binomial(n,n_4) to obtain the uniform-order mean polynomial. Proof: partition words by their final letter. Trace is invariant under cyclic shifts and this statistic depends only on cyclic adjacency, so averaging all rooted words gives the same mean as uniform labelled cyclic orders. The code stores one DP row; all coefficients are integers and final moment sums are exact rational numbers.

## Why fixing degrees still does not rescue raw cycle planting (proved)

The finite mixed-degree moments motivated checking the degree-pair statistics of the fixed-degree planted model. They expose a second, independent bias.

Assume fixed degree sequences satisfy S/n→mu>3, n_3/n→a>0, sum d_i^2=O(n), and max d_i=o(sqrt(n)). Let E_33 count edges between two distinct degree-three vertices (counting multiplicity in the configuration model).

**Theorem R6.** In the target uniform configuration,

E_33/n → 9a^2/(2mu).

In the fixed-degree uniform-cycle planted configuration,

E_33/n → a^2[1+1/(2(mu-2))].

These statements also hold after conditioning the respective models on simplicity. The difference is

Delta = a^2 (mu-3)^2/[mu(mu-2)] >0.

Consequently these two fixed-degree models are asymptotically singular, and their raw Hamilton-cycle second-moment ratios grow at least exponentially.

**Proof.** For any marked pool of B half-edges in a uniform S-half-edge matching, the number J of pairs with both endpoints marked has mean B(B-1)/(2(S-1)). Generate the uniform matching from a uniform permutation of its half-edges paired in consecutive positions. Transposing two entries changes at most two pair indicators. Expose permutation entries successively. For two possible values of the next entry, couple the remaining permutations by a transposition; their conditional expected J values differ by at most two. Thus every martingale increment is bounded by two. Azuma gives

P(|J-EJ|>=t)<=2 exp(-t^2/(8S)).

For B=3n_3 this counts pairs among degree-three stubs, including loops at such vertices. The expected number of these loops is 3n_3/(S-1)=O(1). Hence their number divided by n tends to zero (Markov), so E_33 has the same limit as J. For exponential concentration around the limit one can instead count only pairs at distinct degree-three vertices directly: its mean is 9 n_3(n_3-1)/(2(S-1)), and the same transposition bound applies. Thus E_33 is exponentially concentrated and has the first stated limit.

In the planted graph, a degree-three vertex has one residual stub. Its residual degree-three-pool pair count therefore has mean n_3(n_3-1)/(2(R-1)), with no loops possible within that pool. It is exponentially concentrated by the same matching argument. Its limit divided by n is a^2/(2(mu-2)). In the uniform independently planted vertex cycle, the expected number of degree-three/degree-three edges is n_3(n_3-1)/(n-1), since each vertex pair occurs with probability 2/(n-1). A transposition of two vertex positions changes at most four cycle-edge indicators; the same permutation exposure argument gives concentration bound 2 exp(-t^2/(32n)). This gives limit a^2. Adding the two independent components proves the planted limit. Independence is not needed merely to add convergences, but holds for this model.

Janson's corollary and the hypotheses give a positive simplicity probability for the target. For the planted model, apply the same corollary to residual degrees d_i-2, whose second moments are bounded and maximum is o(sqrt(n)); their factorial-second-moment parameter is bounded. The cycle-avoidance argument from R2 gives an additional positive factor exp(-(mu-2)). If the residual second moment does not converge, the same argument gives a positive lower bound along every subsequence, using its boundedness. Thus conditioning on simplicity preserves the limits and exponential deviation bounds.

Subtracting the two limits yields Delta by direct algebra. Specifically 2mu(mu-2)+mu-9(mu-2)=2(mu-3)^2. With a separating event |E_33/n-planted_limit|<Delta/4, the planted probability tends to one while the target probability is at most C exp(-k n) for some k>0, by the deviation bounds. The exact likelihood identity at fixed degrees and Cauchy–Schwarz, as in R3, force E H^2/(E H)^2>=c exp(k n). The same reasoning works in either unconditioned or simple-conditioned models, with their respective cycle-count expectations. This proves the theorem. The assertions concern raw unweighted counts; they do not prove non-Hamiltonicity.

For j≠k, the planted-minus-target limiting edge-count difference per vertex is

2 p_j p_k (j-mu)(k-mu)/[mu(mu-2)].

For j=k it is p_j^2(j-mu)^2/[mu(mu-2)]. These identities follow by adding cycle edges (2p_jp_k for distinct types, p_j^2 for one type) and residual edges and subtracting the full pairing expectation. The numerators and the degree-three specialization are formalized in PlantedMixing.lean. Their positive-variance and concentration consequences are in the written proof, not claimed as Lean formalization.

## Attempt to repair the planting: a remaining high-degree obstruction

Could a degree-biased cycle ordering repair R6 while leaving residual pairings uniform? Its required *directed* cyclic edge-type frequencies would be

C_{jk}=p_j p_k [1-(j-mu)(k-mu)/(mu(mu-2))].

They have row sums p_j because sum_k p_k(k-mu)=0. The symmetric matrix would give transition probabilities T_{jk}=C_{jk}/p_j and stationary distribution p. For a degree-3/4 mixture all entries are positive: mu∈[3,4], |j-mu|≤1, and mu(mu-2)≥3. It is therefore an algebraically feasible reversible Markov kernel and matches the desired first edge-type moments. No theorem identifying its planted graph with the target was proved.

For the actual truncated-Poisson law, however, p_j>0 for every integer j>=3. Any integer j>mu+sqrt(mu(mu-2)) gives C_{jj}<0. Thus no cyclic ordering can match the target edge-type means while leaving residual pairings uniform.

Here is a probabilistic version, not just a negative matrix entry. For that fixed j, the uniform residual matching alone has limiting j-j edge count per vertex ((j-2)p_j)^2/(2(mu-2)); the target has (jp_j)^2/(2mu). Their positive difference is

gamma_j = p_j^2 [(j-mu)^2/(mu(mu-2))-1] >0.

Internal residual loops at degree j have mean O(1), and alternatively one can directly count only distinct-vertex pairs as in R6. The corresponding counts are exponentially concentrated. Any added spanning cycle only increases the j-j edge count. Hence no choice of cycle, even one depending on the residual matching, can give a model contiguous to the target if its residual matching stays uniform at the fixed typical degrees. Conditioning that construction on simplicity does not rescue it if its acceptance probability is at least exp(-o(n)): the exponentially unlikely lower-edge-count event stays unlikely after that conditioning. Without an acceptance lower bound no conditioned-law conclusion is claimed. Typical fixed truncated-Poisson degree vectors satisfy all moment assumptions by ATTEMPT.md Lemma 4.3.

This pushes the selected approach beyond freezing degrees: a viable planting must also change the residual matching law or use an appropriately weighted cycle count. Matching the first type moments in the bounded 3/4 toy model does not establish contiguity, and the same first-moment repair is impossible with uniform residual pairing for the unbounded degree support in F0096.

## Computations, hostile checks, and exact scope

Scripts: second_moment.py and planted_degrees.py. Artifacts: second_moment.json, planted_degrees.json, PlantedMixing.lean, and its check log.

- The transfer-matrix coefficients were checked against direct enumeration of every cyclic bit word for degree lists (3,3,3,3), (4,4,3,3), (3,4,5,3,4), and (5,5,5,5,5). The last two are polynomial-identity checks, not necessarily admissible pairing sequences.
- Enumerated all 10395 pairings for degrees (3,3,3,3). Sum H=11664 and sum H^2=42768, so E H=432/385 and E H^2=144/35, exactly matching R4. Among the 1296 simple pairings H=3 always, as expected for K_4. This checks the orientation factor and simple-case interpretation independently.
- Enumerated all 135135 pairings for (4,4,3,3). Sum H=233280 and sum H^2=1073088, yielding E H=1728/1001 and E H^2=39744/5005. Exact agreement with the overlap formula checks actual stub overlap versus parallel vertex edges. There are no simple pairings because degree four exceeds n-1; this example is used only to test the multigraph identity, never as a simple-model experiment.
- Exact mixed-degree second-moment ratios at n=48,96,192 with n_4=n/4 were approximately 2.91185,3.07807,3.56841; at n_4=n/2 they were 2.61471,2.83684,3.41990. These are exact rational evaluations rendered as floats, not Monte Carlo estimates. Ratios at finite n do not establish an asymptotic rate; R6 proves the exponential lower bound independently.
- An initial row n=12,n_4=3 had odd total degree and was inadmissible. The referee check removed it and replaced it with n=12,n_4=2, and the code now asserts even total and residual degree. The rest of the moment rows have even totals. The invalid row supports no claim.
- Parameter bisection and positive-term series in planted_degrees.py illustrate the degree bias. At c=1.6, target (p_3,p_4,p_5)≈(0.827322,0.148512,0.0213273), whereas planted (q_3,q_4,q_5)≈(0.823562,0.155010,0.0194506). Analytic ratio comparisons prove the distributions differ; numerical rounding is not used for that proof. The numerical KL quantities are descriptive and were not used as rigorous rate bounds.
- The loop obstruction was separated from a simple-graph obstruction: conditioning on simplicity removes those loops and all parallel edges. No counterexample to F0096 is inferred from a multigraph failure.
- Both kinds of planted likelihood bias were proved on the correct sample spaces. Annealed planting biases the degree vector; fixing that vector removes this bias but leaves linear differences in degree-pair edge counts. A bounded-degree or high-average-degree Hamiltonicity theorem cannot bypass either issue without its hypotheses being checked.
- The requisite planted simplicity probability was proved through residual simplicity and independent-cycle edge avoidance, rather than assumed from the target model. The acceptance condition for the more general dependent-cycle repair is stated explicitly.
- Azuma was applied to uniform permutations with transposition couplings, yielding bounded martingale increments; no independence of random matching edges was assumed.
- The new Lean file checked both algebraic discrepancy numerators successfully (exit code zero). Its completion is recorded in lean_check.log. It does not formalize concentration, planted likelihoods, or Hamiltonicity.
- All numerical jobs were finite and well below 1 GB; no graph job exceeded n=192, and the largest exhaustive pairing space had 135135 elements. No large-n Hamiltonicity oracle or long-running search was used.

## Result and remaining gap

VERDICT: PARTIAL. No new c interval of Hamiltonicity is proved and no counterexample to the conjecture is found. The second attempt proves new obstructions to three variants of planted-cycle contiguity: raw annealed planting, raw fixed-degree planting, and cycle-order-only repair with uniform residual pairing on the unbounded degree support. It also supplies an exact finite fixed-degree second-moment identity and corrects the unattainable unconditional probability-one premise of the first attempt.

The remaining question is still P(H=0 | simple)=o(1) for every fixed 3/2<c≤2.662... outside the verified theorem's range. Raw first and second moments now have a proved exponential likelihood-bias obstruction, not merely an uncomputed variance. A future route must build a weighted Hamilton-cycle count that neutralizes degree and degree-pair biases while retaining a nonzero-count implication, alter the residual planting law with controlled likelihood, or prove rotations/absorption directly in the conditioned-simple model. No such weight, likelihood bound, or direct construction was established here. The split-cubic-gadget approach remains a separate unpursued proposal requiring a forced-traversal theorem and an exact distributional comparison.
