# E0089 — mathematical attempt (2026-10-12)

## 1. Exact question and source correction

Fix integers d >= 4 and 2 <= k <= d-2, and a resampling probability 0 < eps < 1. Let G be uniformly distributed over labelled simple d-regular graphs on n vertices, along admissible n (nd even). Let F_G(A) be the indicator that k-neighbour bootstrap percolation from A eventually occupies every vertex. A vertex outside the occupied set joins when it has at least k occupied neighbours. Updates can be simultaneous or sequential: monotonicity gives the same final closure. Given G, let q_G be the unique solution P_p(F_G=1)=1/2. Resample each initial bit independently with probability eps, using Bernoulli(q_G). The primary reading of Question 1.4(a) asks whether there is delta=delta(d,k,eps)>0 for which P_G(Corr_qG(F_G(A),F_G(A^eps))>delta) -> 1.

Replacing indicators by the source's {-1,1} functions leaves correlation unchanged. eps=1 is excluded: independent configurations have zero correlation. No epsilon uniformity is intended.

The source defines p_c(n)=p_c(G_n,k) on page 2, suggesting the graph-specific q_G, but its Section 3 proof also uses p_c(n) as a deterministic annealed median in product measures. These should be distinguished. Write p0_n for the solution E_G P_p(F_G=1)=1/2. The main analysis below uses q_G; the replica identity also applies at p0_n. We do not use the source's overloaded notation to substitute one for the other.

The intake's description of theta(G) is incorrect. Remark 3.4 (PDF page 10) defines

  phi(G) := P_pc(n)(C_n | #A_n > r(K,n)).

This is a conditional success probability, not the critical density. The source itself says that Azuma would require the sum of squared step Lipschitz constants to be o(1) and discusses the obstruction at the n^-1/2 pivotal scale. The old attempt's assertion that the source missed the obstruction is false. Its asserted order-n Lipschitz constant is about a different observable, final occupied SIZE, and does not prove anything about phi, which lies in [0,1].

## 2. A proved consequence for the actual graph threshold

Let p* be the tree threshold from source (3.1), so 0<p*<1. Theorem 3.1, pages 7-8, gives annealed success/failure outside p* +/- omega(n)/sqrt(n), for arbitrarily slowly diverging omega. Theorem 3.3 extends this to independent Bernoulli initial sets. The occupied-density convergence in the subcritical conclusion implies failure with probability tending to one, since its limiting vacant proportion is positive for k<=d-2.

**Proposition 1 (threshold tightness).** q_G-p* = O_P(n^-1/2). In particular q_G concentrates around p*, and around its own mean, on the unscaled o(1) scale. This does NOT assert that sqrt(n)(q_G-p*) converges to zero, nor a fixed bounded interval containing it with probability tending to one.

Proof. Write a_G(p)=P_p(F_G=1), an increasing continuous polynomial. Its endpoints are 0 and 1; strict increase on (0,1) follows because a nonconstant monotone event has a pivotal configuration of positive product probability. Thus q_G exists uniquely. For deterministic p_-<p_+,

  P(q_G<p_-) <= 2 E a_G(p_-),
  P(q_G>p_+) <= 2 E(1-a_G(p_+)).                         (1)

Indeed the event in each left side implies that the corresponding nonnegative quantity inside the expectation on the right exceeds 1/2. For every a_n -> infinity choose b_n=min(a_n/2, log log(n+e^e)); b_n diverges and log b_n=o(log n). Apply the annealed theorem at p* +/- b_n/sqrt(n) (eventually these are in (0,1)); (1) shows P(sqrt(n)|q_G-p*|>a_n)->0. This property implies tightness: otherwise some eta>0 and a subsequence n_j increasing have P(sqrt(n_j)|q_G-p*|>j)>eta. Define a_n to increase sufficiently slowly, with a_n<=j at n=n_j; this contradicts the preceding property. Since 0<=q_G<=1, convergence in probability to p* also gives E|q_G-p*|->0, by splitting at a fixed tolerance and then taking that tolerance to zero. Consequently |E q_G-p*|->0 and q_G-E q_G->0 in probability. End proof.

The same Markov argument gives tight O(n^-1/2) graph-specific quantile windows at any two fixed nontrivial success levels. This reproduces a consequence of the existing annealed theorem; it does not settle the noise question.

## 3. A deterministic profile-to-noise estimate

For any nonconstant increasing Boolean function F on n bits define

  g(m) = average F over the m-element subsets, 0<=m<=n.

Couple a uniform m-set with a uniform (m+1)-set by adding a uniformly chosen absent vertex. The marginals are uniform, so monotonicity gives g(m+1)>=g(m). Let I_i=P_p(i is pivotal), I=sum I_i. Differentiating the Bernstein polynomial E_p F=sum_m g(m) binom(n,m)p^m(1-p)^(n-m) yields the exact identity

  I = n sum_{m=0}^{n-1} P(Bin(n-1,p)=m)(g(m+1)-g(m)).     (2)

For completeness the derivative of the mth binomial mass is n times the difference of the (n-1)-bit masses at m-1 and m; shifting the first sum telescopes to (2). Independently, differentiating the product expectation in coordinate i yields E(F|X_i=1)-E(F|X_i=0)=I_i, so this derivative equals I.

The normalized p-biased coordinate chi_i=(X_i-p)/sqrt(p(1-p)) has coefficient E(F chi_i)=sqrt(p(1-p)) I_i. The tensor products chi_S form an orthonormal basis. Resampling acts on chi_S by (1-eps)^|S|, because each centered independent coordinate is kept with probability 1-eps and otherwise has conditional mean zero. Thus

  Cov(F(X),F(X^eps)) = sum_{S nonempty}(1-eps)^|S| hatF(S)^2
  >= (1-eps)p(1-p)sum_i I_i^2
  >= (1-eps)p(1-p) I^2/n.                              (3)

The last inequality is Cauchy-Schwarz. These identities hold for graph-dependent, nonsymmetric F.

**Proposition 2 (finite profile bound).** If a<b and g(b)-g(a)>=gamma>0, put beta=min_{a<=m<b}P(Bin(n-1,p)=m). Then

  Corr_p(F(X),F(X^eps)) >=
    (1-eps)p(1-p) n beta^2 gamma^2 / Var_p(F).             (4)

Proof. In (2) keep only indices a<=m<b. Their increments are nonnegative and telescope to g(b)-g(a), hence I>=n beta gamma. Substitute in (3), and divide by Var_p(F)>0. End proof.

If p belongs to [c,1-c], c>0 fixed, and |a-np|,|b-np|<=C sqrt(n), then beta>=b(c,C)/sqrt(n) for all sufficiently large n. This can be justified directly with Stirling's factorial bounds, as follows. Set N=n-1 and x=m/N. Eventually x is in [c/2,1-c/2] and |m-Np|<=(C+2)sqrt(n). Taylor's theorem applied to D(x||p)=x log(x/p)+(1-x)log((1-x)/(1-p)), whose second derivative is 1/[x(1-x)], gives D(x||p)<=2(x-p)^2/[c(1-c)]. Then N D(x||p)<=4(C+2)^2/[c(1-c)] for n>=2. The usual factorial bounds sqrt(2 pi j)(j/e)^j <= j! <= sqrt(2 pi j)(j/e)^j exp(1/(12j)) give

  P(Bin(N,p)=m) >= sqrt(2/(pi N)) exp(-N D(x||p)-1/6).

Here m,N-m>=1; the two upper factorial error terms sum to at most 1/6. An explicit valid choice is

  b(c,C)=sqrt(2/pi) exp(-1/6-4(C+2)^2/[c(1-c)]).

Consequently, a fixed central profile gap gives a fixed positive lower bound on noise correlation. At the median Var(F)=1/4.

## 4. Conditional tail success is sufficient, with an explicit proof

For a balanced increasing F at p, define M=|X|, U={M>np+K sqrt(n)}, and phi=P(F=1|U). Fix K>=0, 0<c<1/2, and p in [c,1-c]. Suppose phi>=7/8. There is a constant C=C(c,K) for which Proposition 2 applies with gamma=5/28, uniformly for all sufficiently large n.

Proof. The binomial central limit theorem, uniformly for p in [c,1-c], gives alpha=P(U)>=alpha0(c,K)>0 for large n. Choose C>K+2 sufficiently large that 1/(4(C-1)^2)<=min(alpha0/8,1/8). Let a=floor(np-C sqrt(n)) and b=floor(np+C sqrt(n)). Chebyshev's inequality, allowing the rounding error, gives P(M>b)<=alpha/8 and P(M<a)<=1/8. Since g is increasing,

  (7/8)alpha <= E(g(M)1_U) <= alpha g(b)+P(M>b),

so g(b)>=3/4. Balancedness gives 1/2=E g(M)>=g(a)P(M>=a), and therefore g(a)<=4/7. Subtracting yields 3/4-4/7=5/28. The hypotheses of Proposition 2 hold, and (4) gives a fixed positive lower bound depending only on c,K,eps. End proof.

For graph-specific q_G, define phi_K(G) using Bernoulli(q_G) and U_G={M>nq_G+K sqrt(n)}. This is well-defined outside graphs for which U_G is impossible; assign phi_K=0 there. Proposition 1 makes this exceptional event have probability tending to zero for fixed K. It follows that

  P_G(phi_K(G)>=7/8)->1 for some fixed K

would settle the primary graph-specific reading of Question 1.4(a).

Moreover for every eta>0 there exists fixed K with limsup E_G(1-phi_K(G))<=eta. Here is the justification without making q_G independent of G. Choose K0 with limsup P(q_G<p*-K0/sqrt(n))<=eta/2, using Proposition 1. By the fixed-size part of the annealed theorem choose K1 so that, for m_+=ceil(np*+K1 sqrt(n)), limsup E_G(1-g_G(m_+))<=eta/2. Such a fixed K1 exists by the same diagonal-tightness argument used in Proposition 1. Set K=K0+K1+2. On q_G>=p*-K0/sqrt(n), every count in U_G is at least m_+, hence phi_K(G)>=g_G(m_+), provided U_G is nonempty. q_G bounded away from 1 with probability tending to one makes U_G nonempty; its negligible exception can be added to the bound. Thus E(1-phi_K)<=P(q_G<p*-K0/sqrt(n))+E(1-g_G(m_+))+o(1)<=eta+o(1).

This gives arbitrarily large fixed probability of the desired correlation bound, with constants depending on that probability. It does NOT give probability tending to one for one fixed constant.

## 5. Exact replica formulation of the missing concentration

Conditionally on G, sample A and B independently with the law used to define phi_K(G), including its upper-count conditioning (and define the corresponding success indicator to be zero on the exceptional graphs just mentioned). Let Z=F_G(A), W=F_G(B). Conditional independence gives E(ZW|G)=phi_K(G)^2 and E(Z|G)=E(W|G)=phi_K(G). Therefore

  Var_G(phi_K(G)) = P(Z=W=1)-P(Z=1)^2.                  (5)

This is an exact finite identity. The two configurations here are INDEPENDENT given G; they are NOT an eps-noised pair.

A sufficient remaining theorem is: for some fixed K large enough that limsup E(1-phi_K)<=1/32,

  P(Z=W=1)-P(Z=1)^2 -> 0.                              (6)

Indeed eventually E phi_K>=15/16. Chebyshev then gives P(phi_K<7/8)<=256 Var(phi_K)->0. Proposition 1 supplies p=q_G in a fixed compact subinterval with probability tending to one, and Section 4 and (4) supply delta>0. Thus (6) would prove the question. Neither the single-replica annealed threshold theorem nor the computations below prove (6).

## 6. Switching comparison: a valid bound, not an Azuma solution

Let G,H be two simple graphs on the same vertices, with every changed edge having both endpoints in S. If S is initially occupied then the bootstrap evolutions agree: vertices in S remain occupied in both graphs, and all edges incident to V\S are unchanged. Induct on update rounds. In particular

  F_G(A union S)=F_H(A union S)

for every A. Monotonicity implies that if F_G(A) differs from F_H(A), at least one of the two functions increases when S is forced occupied. For any initial-set law mu,

  |E_mu F_G-E_mu F_H|
  <= mu(F_G(A union S)>F_G(A))+mu(F_H(A union S)>F_H(A)).  (7)

For product Bernoulli(p), enumerate S={s_1,...,s_r} and force coordinates sequentially. An increase at step j requires s_j to be initially zero and pivotal after the previous coordinates have been forced. Previous coordinates have their independent product law conditioned to all be one. Therefore its probability is at most (1-p)p^{-(j-1)} I_{s_j}(F), where I is evaluated in the unconditioned product measure. Summing proves

  P(F(A union S)>F(A)) <= (1-p) sum_j p^{-(j-1)} I_{s_j}(F). (8)

For mu=P_p(.|U), divide the unconditioned right side by P_p(U). A degree-preserving two-edge switch has r<=4. This rigorously connects switching sensitivity to vertex influences, but supplies no o(n^-1/2) switching bound and no o(1) martingale quadratic variation.

An explicit finite example at d=4,k=2: G=K_{4,4} with parts {0,1,2,3} and {4,5,6,7}; H deletes edges 04,15 and adds edges 01,45. Both are simple 4-regular. From initial set {0,4}, G stops immediately (every other vertex sees exactly one occupied neighbour). In H, vertices 1 and 5 activate, then all remaining vertices activate. Thus a valid degree-preserving switch changes failure to complete occupation. With S={0,1,4,5}, forcing S makes both occupy everything, in accordance with (7). This finite example is NOT an asymptotic random-graph counterexample and does NOT establish an order-n lower bound on a probability Lipschitz constant.

Exact enumeration of all 256 initial sets in experiments.py gives g_G(2)=12/28=3/7 and g_H(2)=22/28=11/14, with g(0)=g(1)=0 and g(m)=1 for m>=3. Median densities are approximately 0.2682691208 and 0.2243294738. At eps=1/2, exact product-transition summation with numerical median root-finding gives correlations 0.3470825826 and 0.3601818745. These are finite verification, not evidence about the n->infinity assertion. Results are saved in experiments.json.

## 7. A proved obstruction to an abstract annealed-window-only argument

The following counterexample concerns arbitrary random monotone functions, NOT bootstrap percolation on random regular graphs.

**Proposition 3.** An ensemble of increasing Boolean functions can have an annealed threshold window O(n^-1/2), critical densities tending to 1/2, and yet, for every fixed 0<eps<1, fail to have any delta>0 such that its graph-analogue probability of critical noise correlation >delta tends to one.

Construction. Choose an integer J>=1 with P(J=j)=2^-j. For n>=J let B=J and m=floor(n/B). Divide Bm bits into B blocks of size m, ignore unused bits, and let F_{n,B} be the OR of the B block-majority events, with each requiring at least ceil(m/2) occupied bits. If J>n use B=1. For fixed B let q_{n,B} be its product median. Every F is monotone and nonconstant.

Proof of the annealed-window assertion. At p=1/2+s/sqrt(n), fixed B and n->infinity, the elementary binomial CLT gives

  P_p(F_{n,B}=1) -> 1-Phi(-2s/sqrt(B))^B.

Dominated convergence over J gives a limiting annealed success function Psi(s), the 2^-B-weighted sum of these expressions. It is continuous and strictly increasing (each summand is, and the weights sum to one), and tends to 0 and 1 at s=-infinity and +infinity by another dominated convergence. Thus for any fixed 0<a<b<1, constants s_-<s_+ bracket both annealed quantiles for all sufficiently large n. This is an O(n^-1/2) annealed window, and its median tends to 1/2.

Critical noise correlation. Define t_B=Phi^{-1}(2^{-1/B}). Monotonicity and the same CLT, bracketing on both sides of this value, give

  q_{n,B}=1/2-t_B/(2sqrt(m))+o(m^-1/2).

In one block, the standardized initial counts before and after noise converge jointly to standard Gaussians with correlation rho=1-eps. This follows from the two-dimensional CLT for independent bounded bit pairs: their variances are mp(1-p), covariance rho mp(1-p), and p=q_{n,B}->1/2. Different blocks are independent pairs. Hence the probability both outputs fail converges to Phi_2(t_B,t_B;rho)^B. At the median both failure probabilities are exactly 1/2, so

  r_B := lim_n Corr_{q_{n,B}}(F(X),F(X^eps))
       = 4 Phi_2(t_B,t_B;rho)^B-1.                      (9)

We now prove r_B->0 as B->infinity. Put u_B=P(N>t_B)=1-2^{-1/B}, so B u_B->log 2, and v_B=P(N>t_B,N'>t_B). A Gaussian Chernoff bound on N+N', whose variance is 2(1+rho), gives v_B<=exp(-t_B^2/(1+rho)) for t_B>=0. To compare with u_B without assuming an asymptotic formula, integrate the normal density over [t,t+1/t], t>=1, to get u_B>=c exp(-t_B^2/2)/t_B for an absolute c>0. Since B u_B stays bounded, B<=C t_B exp(t_B^2/2). Thus

  B v_B <= C t_B exp(-t_B^2(1-rho)/(2(1+rho))) -> 0,

as t_B->infinity. Finally Phi_2(t_B,t_B)=1-2u_B+v_B. Because u_B=O(1/B), v_B=o(1/B), taking logarithms yields B log(1-2u_B+v_B)->-2log 2. Its Bth power tends to 1/4, proving (9) tends to zero.

Given any delta>0 choose a fixed B with r_B<delta. On the event J=B, which has fixed positive probability 2^-B, the finite-n correlation is eventually <delta. Consequently limsup P(Corr>delta)<=1-2^-B<1. Also q_{n,J}->1/2 in probability by dominated convergence over J. All claims follow. End proof.

This shows precisely why tightness of a narrow annealed threshold window does not, by itself, upgrade a 1-eta assertion to a probability-one assertion, even when each realization is evaluated at its own median. Graph structure or additional concentration is essential.

Numerical quadrature of (9) at rho=1/2 gives r_1=1/3, r_4 approximately 0.2293, r_64 approximately 0.0900, r_1024 approximately 0.0326, and r_1000000 approximately 0.002728. The proof of r_B->0 is analytic and does not rely on these numbers.

## 8. Hostile-referee checks and remaining gap

- Correct observable: phi is a probability, not final occupied size and not critical density.
- Correct graph model: the target is uniform simple fixed-d regular graphs; configuration multigraph arguments require an explicit transfer. No such transfer is asserted here.
- Correct noise quantifiers: delta may depend on fixed eps in (0,1); eps=1 is trivial independence and outside the meaningful question.
- Correct median: q_G is distinguished from deterministic p0_n. All uses of balancedness above refer to q_G.
- Tightness is weaker than probability-one boundedness. Proposition 3 rules out the proposed abstract inference in full generality.
- Monotonicity of profiles follows from uniform subset coupling; it does not require vertex transitivity of a sampled graph.
- Formula (2) uses pivotal probabilities in the unconditioned Bernoulli law. Formula (8) explicitly pays for forcing and conditional-tail conditioning.
- Replica (5) uses conditional independence, not noise coupling. A single-configuration CLT cannot establish the required factorization.
- Finite switching computation exhausts all 256 sets and preserves degree. It is not a counterexample to E0089.
- Lean checks only the explicit finite switching statements, not Propositions 1-3, asymptotic analysis, or the open question. Its result is recorded separately in lean_check.txt.

Precise unresolved assertion: prove a fixed-K quenched lower bound for phi_K, for example the independent-two-initial-set factorization (6), or find an alternative graph-specific estimate giving a fixed central profile gap with probability tending to one. No such bound or counterexample for G_{n,d} has been proved here. The literature search has found no paper stating and proving Question 1.4(a) with these exact quantifiers; incomplete API access limits that negative search conclusion.
## 9. Core duality and completed verification

**Proposition 4 (exact core reduction).** On a d-regular simple graph, the final vacant set under k-neighbour bootstrap percolation is the (d-k+1)-core of the subgraph induced by the initially vacant vertices.

Proof. Set r=d-k+1 and V_0=V\A. If V_t is the current vacant set, a vertex v in it has d-deg_{G[V_t]}(v) occupied neighbours. It becomes occupied precisely when this number is at least k, equivalently deg_{G[V_t]}(v)<=d-k=r-1. Thus the simultaneous vacant update is V_{t+1}={v in V_t:deg_{G[V_t]}(v)>=r}, exactly iterative r-core peeling. The nested finite sets stabilize. At stabilization the induced subgraph has minimum degree at least r. Conversely every subset S of V_0 inducing minimum degree at least r survives every round, by induction: if S is contained in V_t then each vertex of S has at least r neighbours in V_t and stays in V_{t+1}. Therefore the stable set contains every such S and is the unique maximal r-core. In particular complete occupation is equivalent to emptiness of this core. End proof.

For the target range r>=3. This explains why the simple vacant-cycle obstruction in the boundary k=d-1 case does not directly apply. It does not prove any quenched concentration theorem.

Verification finished:

- FiniteSwitch.lean uses only Lean core and three proofs by `decide +kernel`. It checks 4-regularity of both explicit graphs, the seed failure/success pair, and equality after forcing S for all 256 bitmasks. After correcting a UTF-8 byte-order-mark parse failure, `lake env lean ~/brain_workers/TRIO_1011/op/E0089/FiniteSwitch.lean` from ~/lean_verify exited 0. The successful command and elapsed time are in lean_check.txt. No sorry or native_decide is used.
- profile_checks.py exhaustively checks all 166 nonconstant monotone Boolean functions on four bits. At p=eps=1/2 it verifies (2), (3)'s total-influence lower bound, and (4) for every pair of layers a<b, using exact rational arithmetic. All passed; result saved in profile_checks.json. These finite checks support the written general proofs and do not formalize their asymptotic portions.
- Janson's fetched Theorem 5.6, PDF page 33, gives a CLT for the random-order infection hitting count on a CONFIGURATION MULTIGRAPH. The following paragraph explicitly says corresponding simple-graph results were presumed but technical difficulties prevented a proof there. We do not transfer that CLT to the target simple graph, and a one-replica hitting-time CLT would still not establish (6).

Final outcome: PARTIAL. No full proof or counterexample to Question 1.4(a) has survived this attempt. The precise missing fixed-K concentration/replica estimate is stated in Section 5.


## 10. Second serious attempt (2026-10-12)

The new full proofs are recorded in SECOND_ATTEMPT.md. Two previously untried approaches were written down: local finite-round peeling with quenched dependency-graph limits, and a joint two-colour adaptive configuration exploration. The former was pursued and yielded:

- Theorem A: fixed-round quenched Gaussian fluctuations of vacancy counts and independent-replica factorization; graph variance of the conditional count mean is O(1).
- Theorem B: this extends to growing rounds t_n with (d-1)^t_n=o(log n), using uniformly controlled cycle moments, variance bounds, and dependency-connected moment counts.
- Corollary C: local-count CDFs still concentrate under the source's upper-initial-count conditioning, using a joint Gaussian limit with the initial count. It also covers the graph-specific median, with explicitly density-dependent centering.
- At d=4,k=2, exact critical recursion z_(t+1)=z_t-(4/3)z_t^2-(16/9)z_t^3, explicit reciprocal bounds, and t z_t->3/4. The polynomial identities and rational constants passed Lean's kernel check.
- A precise limitation: approximating the critical tree drift on the n^-1/2 scale requires depth Omega(n^(1/4)), beyond tree-ball arguments; early completion even at the allowed growing depths has L1 discrepancy tending to 1/2 from the final critical event.

The gap in Section 5 remains: concentration/factorization of FINAL occupation under the fixed-K conditioned initial law. No solution or counterexample to Question 1.4(a) has been proved. Final verdict remains PARTIAL.
