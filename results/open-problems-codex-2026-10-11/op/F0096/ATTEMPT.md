# F0096: attempt and referee record

Date: 2026-10-12. Verdict: PARTIAL. The full Hamiltonicity conjecture is not proved or disproved here.

Second-attempt update: see REATTEMPT.md. It proves that raw planted-cycle likelihoods fail both before and after fixing degrees, and records an important correction to the proposed unconditional configuration-model route below.

## 1. Exact question and admissibility

Write G(n,m;3) for the uniform labelled simple graph on [n] with exactly m edges and minimum degree at least three. For every fixed real c>3/2, use m_n=floor(cn), or any admissible integers with m_n/n→c. The requested conclusion is P(G(n,m_n;3) Hamiltonian)→1. At c=3/2 the source uses exactly m=3n/2, hence even n, and the distribution is the uniform cubic graph. The source's conjecture and the later bound are recorded in LITERATURE.md. Odd-n empty sample spaces are not a counterexample.

The later Anastos–Frieze theorem covers c>2.662...; this attempt does not enlarge that Hamiltonicity range. Literature coverage is bounded and OpenAlex was inaccessible (HTTP 429); no full solution in print was verified.

## 2. Deterministic obstruction to a cubic scaffold (proved)

**Lemma 2.1.** A simple graph containing a vertex v of degree four all of whose neighbors have degree three has no spanning cubic subgraph.

**Proof.** In a spanning cubic subgraph H, each degree-three vertex u must retain all three incident edges of G: H can only delete edges and must leave degree three at u. Thus every edge vu must remain, since u is degree three. The four neighbors of v are distinct in a simple graph, so v would have degree at least four in H, contradicting cubicity. This proves the lemma. The finite cardinality contradiction is formalized in ForcedDegree.lean; the surrounding graph-to-neighbor-set argument is the proof just given, not formalized there.

This is not an obstruction to Hamiltonicity. In a Hamilton cycle each degree-three vertex retains two edges, so the forcing argument fails.

## 3. Exact local pairing moments (proved)

Fix labelled vertex degrees d_1,...,d_n with even total S=sum d_i. Pair their distinguishable half-edges uniformly. Let n_3 and n_4 be the numbers of degree-three and degree-four vertices, and A=3n_3. For a degree-four vertex v let I_v indicate that all four partners of its half-edges belong to degree-three vertices. Repeated neighbors are allowed in this definition before conditioning on simplicity. Set X=sum_{d_v=4} I_v. For fixed k define

P_k(A,S) = (A)_k / product_{j=0}^{k-1}(S-(2j+1)),

where (A)_k is a falling factorial (zero if A<k).

**Lemma 3.1.** E I_v=P_4; for distinct degree-four vertices v,w, E(I_v I_w)=P_8. Consequently

E X=n_4 P_4,

Var X=n_4 P_4(1-P_4)+n_4(n_4-1)(P_8-P_4^2).

**Proof.** Order the four half-edges of v. Expose the partner of the first; it is uniform among S-1 available half-edges, of which A belong to degree-three vertices. On success, the next ordered half-edge of v is still unpaired, and has S-3 possible partners, with A-1 favorable partners. Continue to obtain the four factors. For two vertices, order their eight half-edges. On the joint event no source half-edge can be paired to another source half-edge, since source vertices have degree four, so exactly the same sequential exposure applies to eight factors. Summing indicators and covariances gives the variance identity. This also explains why using independent partner choices would be wrong at finite n.

**Proposition 3.2.** Suppose a deterministic degree sequence has S/n→mu>0, n_3/n→a>0, and n_4/n→b>0. Then in the configuration model

X/n → b(3a/mu)^4 in probability.

**Proof.** Since A and S are both linear in n, for each fixed k=4,8,

(A)_k=A^k(1+O(1/n)),

product_{j=0}^{k-1}(S-(2j+1))=S^k(1+O(1/n)).

The constants are uniform when A/n and S/n are bounded above and below by fixed positive constants. Thus P_4→(3a/mu)^4 and P_8-P_4^2=O(1/n). As n_4≤n, the variance identity gives Var X=O(n) (bounding the covariance term by its absolute value). Chebyshev gives P(|X-E X|>epsilon n)=O(1/n) for every fixed epsilon>0. Dividing its expectation by n proves the assertion. No maximum-degree hypothesis is used in this proposition.

If simplicity has probability bounded below, the same convergence holds after conditioning on simplicity, because P(B | simple)≤P(B)/P(simple). On simplicity I_v is exactly the graph event in Lemma 2.1.

## 4. Exact reduction to truncated Poisson and simplicity (proved)

For lambda>0 let

f_3(lambda)=sum_{j≥3} lambda^j/j!,

p_j(lambda)=lambda^j/(j! f_3(lambda)), j≥3,

mu(lambda)=sum j p_j(lambda)=lambda f_2(lambda)/f_3(lambda).

**Lemma 4.1.** For each mu>3 there is a unique lambda>0 with mu(lambda)=mu.

**Proof.** Differentiating p_j gives p'_j=p_j(j-mu)/lambda, and hence mu'=Var(D)/lambda>0; both degrees three and four have positive probability. Termwise differentiation is justified by the factorially convergent series on compact positive lambda intervals. As lambda↓0 the first term dominates and mu→3. As lambda→∞, f_2/f_3→1 and mu→∞. Continuity and strict increase prove existence and uniqueness.

For m_n/n→c>3/2 choose lambda_n with mu(lambda_n)=2m_n/n. Then lambda_n→lambda, where mu(lambda)=2c. Sample independent D_i with law p_j(lambda_n), condition on sum D_i=2m_n, and pair the resulting half-edges uniformly. Call this multigraph Q_n.

**Lemma 4.2 (exact law).** Conditional on being simple, Q_n has exactly the law G(n,m_n;3).

**Proof.** On the prescribed total, the degree-vector probability is proportional to product_i 1/d_i!, since lambda_n^{2m_n}/f_3(lambda_n)^n is constant. For a fixed simple labelled graph g with that degree vector, the number of pairings of labelled half-edges that produce g is product_i d_i!: at each vertex assign its distinguishable half-edges bijectively to its incident edges, after which the pairing is determined. The total number of pairings is (2m_n-1)!!, independent of the degree vector. Multiplying the two weights cancels product_i d_i!, giving the same probability to every admissible simple graph. Normalizing proves the exact conditional law. This is not a claim that Q_n is simple with probability tending to one.

**Lemma 4.3 (degree concentration under total conditioning).** Under the degree law before pairing,

n_j/n→p_j(lambda) for j=3,4,

n^{-1} sum D_i^2 → E_lambda D^2,

max_i D_i≤n^{1/8} with probability tending to one.

**Proof.** First, the total-conditioning probability is asymptotic to

P(sum D_i=2m_n) ~ (2 pi n Var_{lambda_n}(D))^{-1/2}.

Here is a direct justification of the local estimate so that conditioning on a probability of order n^{-1/2} is accounted for. For phi_n(t)=E exp(itD), Fourier inversion gives the probability as (2pi)^{-1} integral_{-pi}^{pi} phi_n(t)^n exp(-it 2m_n) dt. The parameters lambda_n stay in a compact positive interval. The law has span one because p_3,p_4>0; on every compact set bounded away from t=0 in [-pi,pi], |phi_n(t)|≤rho<1 uniformly. Uniform third moments give, near zero,

exp(-it mu_n) phi_n(t)=1-sigma_n^2 t^2/2+O(|t|^3),

with sigma_n^2 bounded away from zero and infinity. Its modulus is at most exp(-K t^2) on a sufficiently small fixed interval, uniformly in n. Substitute t=u/sqrt(n). For fixed u the integrand converges to exp(-sigma^2 u^2/2); the bound exp(-K u^2) permits dominated convergence. The rest of the integral is exponentially small by the span-one bound. Since 2m_n=n mu_n exactly, there is no residual phase. The Gaussian integral gives the displayed asymptotic (equivalently with sigma_n tending to sigma).

For either indicator Y_i=1_{D_i=j}, or Y_i=D_i^2, all fourth moments are bounded uniformly in n. If Z_i=Y_i-EY_i, independence and centering imply

E(sum Z_i)^4 = n E Z_1^4 + 3n(n-1)(E Z_1^2)^2 = O(n^2).

Markov bounds a deviation of epsilon n by O(n^{-2}); dividing by the conditioning probability O(n^{-1/2}) gives O(n^{-3/2}) under total conditioning. Expectations converge as lambda_n→lambda, proving all three stated average convergences. Finally uniform sixteenth moments give

P(max D_i>n^{1/8})≤n E D_1^{16}/n^2=O(n^{-1}).

After total conditioning this is O(n^{-1/2}), which tends to zero. All required moments are finite and locally uniform by the factorial series. This proves the lemma.

**Lemma 4.4 (positive simplicity probability).** P(Q_n is simple)→s_lambda>0, where

Lambda_lambda=E_lambda[D(D-1)]/(2 E_lambda D),

s_lambda=exp(-Lambda_lambda-Lambda_lambda^2).

**Proof using an explicitly cited standard theorem.** Janson, arXiv:math/0609802v1, Corollary 1.5, PDF p. 4, says that for a deterministic degree sequence with N=sum d_i/2→∞ and max d_i=o(sqrt(N)), its pairing is simple with probability exp(-Lambda-Lambda^2)+o(1), where Lambda=sum d_i(d_i-1)/(4N). Lemma 4.3 gives these hypotheses with probability tending to one and Lambda→Lambda_lambda. The deterministic theorem also gives convergence in probability for the random degree sequence: if not, select an offending subsequence of deterministic realizations with the stated degree bounds and moment convergence, contradicting that theorem. The simplicity probabilities lie in [0,1], so their expectations converge to s_lambda. This proves the lemma. Janson's theorem is used as a published theorem, not claimed as a new proof here.

**Corollary 4.5 (sufficient reduction, proved).** If Q_n is Hamiltonian with probability tending to one for every fixed c>3/2, then the conjecture follows for those c.

**Referee correction from the second attempt:** this implication is logically true, but its premise is impossible for Q_n as defined. Degree-three loops occur with limiting positive probability and prevent Hamiltonicity. REATTEMPT.md computes their factorial moments and proves P(Q_n Hamiltonian)<=exp(-3p_3/(2c))+o(1)<1. A viable proof must work after simplicity conditioning or account for the short-cycle obstructions; unconditional probability tending to one cannot be the target.

**Proof.** P(G(n,m_n;3) is not Hamiltonian) equals P(Q_n is not Hamiltonian | simple), which is at most P(Q_n is not Hamiltonian)/P(simple)→0 by Lemma 4.4. This is a sufficient transfer. The converse is not established: non-simple configurations have non-vanishing probability, so their behavior is not determined by the conditioned-simple theorem.

## 5. Main partial result: no spanning cubic subgraph (proved)

**Theorem 5.1.** For every fixed c>3/2, G(n,m_n;3) has no spanning cubic subgraph with probability tending to one. More precisely, the number X of degree-four vertices all of whose neighbors have degree three satisfies

X/n → theta(c)=p_4(lambda) [3p_3(lambda)/(2c)]^4 >0

in probability, with lambda from Lemma 4.1.

**Proof.** By Lemma 4.3, the configuration degrees satisfy n_3/n→p_3>0, n_4/n→p_4>0, and S/n→2c. Proposition 3.2 therefore applies conditionally on the degrees. Its O(n) variance estimate is uniform on degree vectors with n_3/n and S/n in compact positive intervals, so averaging the conditional Chebyshev bound and discarding atypical degrees yields X/n→theta(c) for Q_n. Lemma 4.4 and the elementary conditioning inequality transfer this convergence to the simple graph. Its theta is positive for every fixed finite c>3/2. With probability tending to one, X≥theta n/2>0, and Lemma 2.1 excludes a spanning cubic subgraph. This proves the theorem.

**Consequence.** Any procedure that starts with a spanning cubic graph on the same n vertices and only adds edges has support on graphs containing a spanning cubic subgraph. For fixed c>3/2, the uniform conditioned model assigns that support probability tending to zero. Thus such a procedure cannot be contiguous in the direction needed to transfer cubic Hamiltonicity to G(n,m_n;3); the total variation distance between its output law and the target tends to one. Indeed, taking the event “contains a spanning cubic subgraph”, the two probabilities are 1 and o(1). No distributional assumption on the initial cubic graph is needed.

The theorem covers fixed c, not c=3/2+o(1). As c↓3/2 with delta=2c-3, the factorial series gives mu(lambda)=3+lambda/4+O(lambda^2), p_4=lambda/4+O(lambda^2), p_3=1+O(lambda), hence theta(c)=delta+O(delta^2). This expansion does not assert a uniform-in-c probability theorem.

## 6. Hamilton-cycle first moment (proved exact identity; no existence conclusion)

Fix d_i≥2, even S≥2n, n≥3. Let H count Hamilton cycles in the configuration multigraph with distinct parallel-edge realizations counted separately. Then

E H = ((n-1)!/2) product_i [d_i(d_i-1)] / product_{j=0}^{n-1}[S-(2j+1)].

**Proof.** There are (n-1)!/2 undirected cyclic orders of labelled vertices. Orient each order by a fixed canonical choice, and at each vertex choose an ordered pair of distinct half-edges for its predecessor and successor; there are d_i(d_i-1) choices. These choices prescribe n disjoint pairs. A uniform perfect matching contains those pairs with probability (S-2n-1)!!/(S-1)!!, equal to the reciprocal product in the formula, with (-1)!!=1. Summing over cyclic orders and stub choices gives the identity; canonical orientation prevents double counting. Loops do not participate in such cycles. On a simple graph H is the ordinary cycle count.

If S/n→mu>2 and n^{-1}sum log[d_i(d_i-1)]→ell, the formula implies

(1/n) log E H → ell - [mu log mu-(mu-2)log(mu-2)]/2.

**Proof.** Stirling gives log((n-1)!/2)/n=log n-1+o(1). The log denominator divided by n is log n plus a Riemann sum converging to integral_0^1 log(mu-2t) dt. Since mu>2, its integrand is continuous and bounded. The integral is [mu log mu-(mu-2)log(mu-2)-2]/2. Subtracting cancels the -1 and gives the expression.

For truncated-Poisson degrees the ell hypothesis holds by the same fourth-moment conditioning argument as Lemma 4.3, applied to log[D(D-1)]. This is the exponential rate of the pairing expectation conditional on a typical degree sequence; it is not an assertion about the expectation after averaging over all degree sequences or conditioning on simplicity. The computed rates in first_moment.json are positive at the seven tested c values. This is numerical evidence only for those values; no global inequality or second-moment estimate is asserted. An exponentially large expectation alone gives no lower bound tending to one on existence.

## 7. Computations and their scope

Reproducible scripts: search.py, search_more.py, experiment.py, first_moment.py. Raw results: experiments.json and first_moment.json. Jobs used finite searches at n≤16 and pairing spaces≤135135; no job needed 1 GB of memory.

1. Enumerated all 135135 pairings for degrees (4,4,3,3). The four joint indicator states had counts (124335,5400,5400,0). The marginal is 40/1001, exactly P_4(6,14); the joint is zero, exactly P_8(6,14). This tests the local exposure formula, including depletion and an impossible joint event.
2. Enumerated all 32768 labelled simple graphs on six vertices, retaining minimum degree≥3. By edge count m=9,...,15 there are respectively 70,537,735,395,105,15,1 admissible graphs, all Hamiltonian. At m=10, 45 have the Lemma 2.1 obstruction. Thus the obstruction and Hamiltonicity coexist.
3. An explicit such graph has edges 02,03,04,05,12,13,14,15,25,34. The Hamilton cycle 0-2-5-1-3-4-0 can be checked edge by edge. Vertices 0,1 have degree four, the others degree three, and 0,1 are nonadjacent. There is no spanning cubic subgraph by Lemma 2.1.
4. Sampled 100 accepted simple graphs at each (n,m)=(12,18),(12,19),(12,20),(14,23),(16,26). Hamiltonian counts were 100,100,99,99,100; local cubic-obstruction counts were 0,46,35,40,69. Degree vectors were sampled by dynamic programming weights proportional to product 1/d_i!, then uniformly paired and rejected unless simple. The ideal law is exactly uniform by Lemma 4.2; floating-point weighted sampling introduces unquantified numerical rounding. The samples are numerical evidence, not exact frequencies or a counterexample to an asymptotic conjecture. Seed=96. Hamiltonicity was determined by finite Held–Karp reachability anchored at vertex zero.
5. Enumerated all 10395 pairings of four degree-three vertices and counted stub Hamilton cycles with multiplicities. Their total is 11664 and mean 432/385, agreeing exactly with the first-moment formula. This check guards its orientation factor and treatment of parallel edges.
6. theta(c) evaluated by a positive-term recurrence and bisection is approximately 0.000199723,0.0174245,0.0537456,0.0159304,0.00340156,0.0000213877,0.00000173747 at c=1.5001,1.51,1.6,1.8,2,2.662,3 respectively. No rigorous error bounds were requested or obtained for these illustrative constants; positivity in Theorem 5.1 is analytic.

## 8. Hostile-referee checklist and remaining gap

- Model bias: multiplying degree weights by pairing counts cancels exactly only after simplicity conditioning. Proved in Lemma 4.2; not replaced by a bare contiguity assertion.
- Rare conditioning: ordinary iid LLNs cannot simply be conditioned on sum D_i=2m_n. Lemma 4.3 proves a polynomially strong error bound and the needed local estimate.
- Simplicity: not assumed to tend to one. Janson's cited corollary verifies a positive limit using controlled maximum degree and second moments.
- Partner dependencies: exact P_4 and P_8 formulas retain finite depletion. Their difference is O(1/n); degree-four events are not independent.
- Repeated neighbors: allowed in Q_n's indicators, excluded after simplicity conditioning, precisely where the graph lemma applies.
- Cubic vs Hamilton degrees: Lemma 2.1 forces three edges at a degree-three vertex only in a cubic spanning subgraph. A Hamilton cycle forces two; the same argument cannot disprove Hamiltonicity. The finite witness confirms this distinction.
- Fixed c and finite n: the theorem's positive theta can be tiny and need not be visible in small samples. No assertion for c depending on n is made.
- Boundary parity: c=3/2 refers to admissible even n, where all degrees equal three by the degree-sum identity.
- First moment: large expectation is not a proof of existence, let alone probability 1-o(1). No second moment or small-subgraph conditioning estimate was obtained.
- Lean checked the final finite cardinality contradiction successfully (exit code zero), recorded in lean_check.log; no stronger formal verification is claimed.

**Remaining mathematical gap.** For the conditioned-simple truncated-Poisson pairing model at each fixed 3/2<c≤2.662... not covered by the verified later theorem, prove that a Hamilton cycle exists with probability 1-o(1), or find an obstruction with non-vanishing asymptotic probability. Theorem 5.1 eliminates adding edges to a spanning cubic graph as a distribution-preserving shortcut, but does not supply a replacement construction. Neither the local moment computation nor the first-moment formula bounds P(H=0) from above. REATTEMPT.md pursues a planted likelihood/second-moment method and specifies the additional bias that a successful weighted-count or alternate construction must overcome.
