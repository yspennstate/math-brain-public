# F0072: continuous SOS entropic repulsion

Date: 2026-10-12. All results below concern real heights and V(s)=|s|, with each unoriented nearest-neighbour edge counted once and inverse temperature 1. They do not assert a result for every non-uniformly strictly convex potential.

## Exact target and scope

For B_N={-N,...,N}^d, zero exterior heights, and A=B_floor(epsilon N), the source conditions the Gibbs measure on phi>=0 on A. Open Problem 5 asks for analogues of Section 3.2, allowing non-sharp constants and allowing different scales when the tail of V changes. The Gaussian d>=3 height is order sqrt(log N); the Gaussian d=2 height is order log N. The continuous SOS interaction has exponential rather than Gaussian tails.

The complete written proofs below establish order-log-N heights for every d>=2 in the full-wall bulk, and on strict interior subboxes of a partial wall. They also establish a uniform upper bound at all wall sites; in d>=3 that bound is O(log M) independently of the ambient volume. Higher-dimensional zero-boundary subsequential free laws and their finite-wall conditionings satisfy the corresponding partial results. The averaged lower bound applies to the whole wall region. The uniform pointwise lower bound at the edge of a partially constrained wall is not proved, so this is a PARTIAL result rather than a solution of the source's full quantifiers.

## Lemma 1: boundary/contact identity and averaged logarithmic lower bound

Let Lambda be a finite set of lattice sites with every component connected by nearest-neighbour edges to the zero exterior, let A be a nonempty subset, and let Q be the normalized density exp(-H(phi)) restricted to phi_i>=0 for i in A. Write q=2d and let b(A) be the number of edges with exactly one endpoint in A (including edges to the pinned exterior). Let f_i denote the one-site probability density under Q, using its continuous right limit at zero for i in A. Then

    sum_{i in A} f_i(0) = E_Q[sum_{i in A} partial_i H] <= b(A),

and for every h>=0,

    sum_{i in A} Q(phi_i<=h) <= b(A) (exp(qh)-1)/q.

Proof. H is coercive in finite volume: choose a path from each site to the exterior; the triangle inequality bounds every |phi_i| by a finite constant times H. Thus the density is integrable, its slices tend to zero at infinity, and integration by parts below is legitimate. For each constrained coordinate, the fundamental theorem for locally absolutely continuous functions gives

    integral_0^infinity partial_i(exp(-H)) dphi_i = -exp(-H)|_{phi_i=0}.

The derivative exists almost everywhere despite the kinks of |s|, and |partial_i H|<=q almost everywhere. Integrating the other coordinates and dividing by the partition function proves f_i(0)=E_Q partial_i H. Summation cancels the two derivatives of every edge within A. Each crossing edge contributes sign(phi_i-phi_j)<=1, proving the bound. A crossing edge to the exterior has phi_j=0. No assertion that every other crossing-edge contribution is positive is needed.

For t>=0 and fixed other coordinates, changing phi_i from 0 to t changes H by an amount between -qt and qt. The support of the other coordinates does not depend on t. Integrating their densities therefore gives f_i(t)<=exp(qt) f_i(0). Integration from 0 to h and the identity prove the second inequality. There are no atoms at zero, so <=h and <h have the same probability.

For A=B_r, b(A)=q(2r+1)^(d-1) and |A|=(2r+1)^d. Consequently the mean over constrained sites of Q(phi_i<=h) is at most (exp(qh)-1)/(2r+1). For h=a log r and a<1/q this tends to zero. This proves a lower bound for the height of a uniformly sampled wall site, and convergence in probability of the fraction of low wall sites to zero by Markov's inequality. It does not by itself prove a pointwise bound at the edge of A.

## Lemma 2: monotonicity in boundary values and wall constraints

On a fixed finite graph with exterior heights fixed, increasing those heights or imposing positivity on additional sites stochastically increases the field. More precisely, expectations of bounded increasing functions increase.

Proof. First truncate unconstrained coordinates to [-K,K] and constrained coordinates to [0,K]. Conditional on the neighbours a_1,...,a_q, the single-site density is proportional to exp(-sum_j |x-a_j|) on its interval. If b_j>=a_j, the ratio of the b-density to the a-density is a nondecreasing function of x: |x-a|-|x-b| has derivative sign(x-a)-sign(x-b)>=0 almost everywhere. A nondecreasing likelihood ratio implies stochastic ordering. To see this without a comparison theorem, for increasing functions r,g and any probability density p,

    Cov_p(r,g) = (1/2) integral integral (r(x)-r(y))(g(x)-g(y)) p(x)p(y) dx dy >= 0.

Apply this with the likelihood ratio r and an indicator g=1_{x>t}. Conditioning a distribution on x>=0 also increases it; increasing the neighbour values and then conditioning proves the comparison when a wall is added at that site. Thus common uniform random variables in the inverse conditional distribution functions give an ordered coupling of systematic Gibbs sweeps, starting from ordered configurations.

For completeness these coupled sweeps converge to the desired truncated measures. On the compact product of their intervals, all single-coordinate conditional densities have a strictly positive lower bound depending on the graph, boundary values and K. The full sweep kernel therefore minorizes a fixed positive multiple of product uniform measure. The usual elementary regeneration argument then contracts total variation by a factor at most 1-delta per sweep: write each kernel as delta times that fixed measure plus (1-delta) times a Markov kernel. The Gibbs density is invariant under each coordinate update, and hence is the unique invariant law and the limit of the sweeps. Passing their ordered coupling to the limiting laws proves the comparison at finite K. Finally, the truncated Gibbs densities converge in total variation to the untruncated densities as K tends to infinity, by integrability and monotone convergence of their normalizing constants. This proves the assertion.

The same reasoning permits conditioning on an exterior configuration: inside a domain D entirely covered by the wall, nonnegative neighbour heights outside D stochastically dominate zero boundary values.

## Proposition 3: a uniform pointwise logarithmic lower bound inside the wall

Let Q_N be the full-wall measure on B_N. If r>=1, then

    Q_{2r}(phi_0<=h) <= (exp(2dh)-1)/(2r+1), h>=0.       (L)

For each j in B_r, the translated box D_j=B_r-j contains 0 and is contained in B_{2r}. Conditional on the heights outside D_j under Q_{2r}, the neighbours of D_j have nonnegative heights or are exterior zeros. Lemma 2 implies that the conditional field in D_j dominates its zero-boundary full-wall measure. Translation gives

    Q_{2r}(phi_0<=h) <= Q_r(phi_j<=h).

Averaging over j and applying Lemma 1 proves (L).

More generally let the original measure be on B_N, conditioned positive only on A=B_M. If a box i+B_{2r}, together with its nearest exterior neighbours, lies in A, the conditional field in this box dominates its full-wall zero-boundary measure. Hence the same upper bound (L) holds for Q(phi_i<=h). It follows that for every fixed 0<eta<epsilon<=1, M=floor(epsilon N), and every 0<a<1/(2d),

    sup_{i in B_floor(eta N)} Q(phi_i<=a log N) -> 0.

Indeed choose r=floor((epsilon-eta)N/3), decreasing it by 1 if necessary; for sufficiently large N the required box and neighbours lie in A. The bound is O(N^(2da-1)). When epsilon=1, exterior neighbours on the boundary of B_N are pinned zero and the same argument works without requiring them to lie in A. Integrating the lower tail, or simply using nonnegativity at the sites concerned, also gives

    liminf_N inf_{i in B_floor(eta N)} E_Q phi_i / log N >= 1/(2d).

This last statement follows by first fixing any a<1/(2d), using E phi_i>=a log N Q(phi_i>a log N), and then sending a up to 1/(2d).

## Lemma 4: exact Gaussian mixture and auxiliary edge domination

For all s in R,

    exp(-|s|) = integral_0^infinity (2 pi t)^(-1/2) exp(-s^2/(2t)-t/2) dt.      (G)

Here is an elementary verification. Set t=u^2 in the integral; its value is sqrt(2/pi) times J(|s|), where J(a)=integral_0^infinity exp(-(u^2+a^2/u^2)/2) du. For a>0 differentiation under the integral is justified on compact subsets of (0,infinity). Substitution v=a/u gives integral u^(-2) exp(-(u^2+a^2/u^2)/2) du=J(a)/a. Thus J'(a)=-J(a). Dominated convergence at zero gives J(0)=sqrt(pi/2), proving (G), including a=0.

Apply (G) independently to each edge, with t_e>0 and all exterior coordinates zero. Tonelli's theorem gives a joint positive density on (phi,t). Conditional on t, phi is centered Gaussian with precision

    L(t)=sum_e t_e^(-1) b_e b_e^T,

where b_e is the signed incidence vector restricted to the free vertices (a boundary edge has only one nonzero entry). L is positive definite because every component is grounded. Integrating phi yields the t-density, up to a finite normalizing constant,

    (det L(t))^(-1/2) product_e t_e^(-1/2) exp(-t_e/2).       (T)

Fix all edges except one. Multilinearity of the determinant and the rank-one form of that edge imply

    det L(t)=A+B/t_e,

with A>=0 and B>0. To check signs and the potentially singular edge-deleted graph, write L_0 for its positive semidefinite matrix. If L_0 is positive definite, A=det L_0>0 and B=det L_0 b_e^T L_0^(-1)b_e>0. If it is singular, adding one rank-one matrix restores positive definiteness, so its nullity is exactly one. Orthogonally diagonalize L_0 as diag(0,lambda_2,...,lambda_n), lambda_j>0. The component of b_e along the null vector is nonzero, and determinant expansion gives A=0 and B=(that component)^2 product_{j>=2} lambda_j>0. The one-dimensional case is included with an empty product equal to 1. (For a nonzero incidence vector in the positive definite case B>0.)

Consequently the conditional t_e density is proportional to

    exp(-t_e/2) (A t_e+B)^(-1/2).

The second factor is nonincreasing, so this conditional law is stochastically dominated by an exponential random variable of rate 1/2. Proof: its expectation of an increasing bounded g is E[g(X)w(X)]/E[w(X)]<=E[g(X)], since the double-integral covariance formula in Lemma 2 has the opposite sign when one function decreases. Here X is rate-1/2 exponential and w(t)=(At+B)^(-1/2), bounded because B>0.

This conditional bound remains true when only some other t coordinates are specified: integrate the full conditional expectation against the conditional distribution of the remaining coordinates. Enumerating the edges and using successive conditioning, for any nonnegative c_e<1/2,

    E exp(sum_e c_e t_e) <= product_e (1-2c_e)^(-1).       (D)

To justify the unbounded functions, first truncate exp(c_e t_e), apply conditional stochastic domination to the last edge, and iterate; then use monotone convergence. In particular no independence of the actual t_e's is asserted or needed.

## Lemma 5: deterministic flow bound for free heights

Let theta be any real unit flow from i to the grounded exterior, meaning sum_e theta_e b_e=delta_i, and set E(theta)=sum_e theta_e^2. Then for |lambda| max_e |theta_e|<1,

    E_free exp(lambda phi_i) <= product_e (1-lambda^2 theta_e^2)^(-1).

Indeed put u=L(t)^(-1)delta_i and R_t=delta_i^T L(t)^(-1)delta_i>0. The identities R_t=sum_e (b_e^T u)^2/t_e and R_t=sum_e theta_e b_e^T u, followed by weighted Cauchy-Schwarz, give R_t<=sum_e t_e theta_e^2. Conditional Gaussian integration gives E[exp(lambda phi_i)|t]=exp(lambda^2 R_t/2). Apply (D) with c_e=lambda^2 theta_e^2/2 to get the claimed bound. If |theta_e|<=1 and |lambda|=1/2, -log(1-x)<=x/(1-x) for 0<=x<1 gives

    E_free exp(plus_or_minus phi_i/2) <= exp(E(theta)/3),
    P_free(|phi_i|>=h) <= 2 exp(E(theta)/3-h/2).          (F)

The logarithm inequality follows by integrating 1/(1-s)<=1/(1-x) from 0 to x, so no asymptotic approximation is involved.

## Lemma 6: an explicit flow on a box

For every i in B_N and d>=2, there is a unit flow with |theta_e|<=1 and

    E(theta) <= K_d(N),
    K_2(N)=1+log(4N+2), and K_d(N)=2 for d>=3.

Construct a monotone random path starting at i, stepping only in the d positive coordinate directions, and stop on first exit from B_N. Before stopping, if its displacement is x with sum_j x_j=k, choose direction j with probability (x_j+1)/(k+d). In the un-stopped path the displacement is uniform among the M_k=binomial(k+d-1,d-1) weak compositions of k. Proof by induction: an endpoint y at level k+1 receives probability sum_{j:y_j>0} (1/M_k) y_j/(k+d)=(k+1)/(M_k(k+d))=1/M_{k+1}. The starting level k=0 is immediate.

Let theta on an oriented positive edge be the probability that the stopped path uses it. Conservation of these probabilities gives a unit flow: each visited interior vertex other than the source has matching entrance and exit probability, and the total exit probability is 1. For the last assertion, the path exits in at most d(2N+1) steps, since each coordinate can increase by at most 2N before one additional increase exits. At shell k, each edge's probability is at most its un-stopped probability, which is at most 1/M_k; the sum over the shell is at most 1. Thus the sum of its squared edge probabilities is at most 1/M_k. Summing over k=0,...,d(2N+1)-1 proves the energy bound. For d=2 this is the harmonic sum H_{4N+2}<=1+log(4N+2). For d>=3, M_k>=binomial(k+2,2), and the infinite sum of 2/((k+1)(k+2)) is 2, by telescoping. This also proves |theta_e|<=1.

## Proposition 7: logarithmic upper bound under any wall subset

For d>=2 let n=(2N+1)^d and K=K_d(N). Set

    h_N=2(log(4n)+K/3).

By (F) and a union bound, the free zero-boundary field has probability at least 1/2 to lie above -h_N at every site. The free field with exterior boundary h_N is exactly h_N plus the zero-boundary free field, because the Hamiltonian depends only on differences. Its probability of satisfying the full wall is therefore at least 1/2.

Write Q_N^b for the full-wall measure with constant exterior value b. Lemma 2 gives Q_N^0<=_st Q_N^{h_N}. For a site i and s>=0,

    Q_N^0(phi_i>=2h_N+s)
      <= Q_N^{h_N}(phi_i>=2h_N+s)
      <= 2 P_free(phi_i>=h_N+s)
      <= 2 exp(K/3-h_N/2-s/2)
      = (1/(2n)) exp(-s/2).                            (U)

The first inequality is stochastic comparison; the second uses the at-least-1/2 denominator just proved. The same bound holds if only A subset B_N is constrained: adding the wall elsewhere stochastically increases the field by Lemma 2. The inequality also applies to any site, constrained or not.

For a maximum probability tending to zero, replace h_N by h_N+2 log(N+2). The denominator remains at least 1/2, and the union of (U) over all n sites has probability at most 1/(2(N+2)). Thus for a constant C_d,

    Q_A(max_{i in B_N} phi_i > C_d log(N+2)) -> 0.

For expectations, integration of (U) gives E_Q phi_i<=2h_N+1/n for constrained sites, since these heights are nonnegative. The same upper bound holds for E phi_i at any site by bounding E(phi_i)_+; the negative part has finite expectation in finite volume. In particular, the upper bound is O(log N), including at the boundary of a partially constrained wall.

## Proven special case and precise remaining gap

Combining Propositions 3 and 7 proves: for every d>=2, 0<eta<epsilon<=1, a<1/(2d) with a>0, and M=floor(epsilon N),

    sup_{i in B_floor(eta N)} Q_A(phi_i<a log N or phi_i>C_d log(N+2)) -> 0,
    c_{d,eta,epsilon} log N <= E_Q phi_i <= C_d log N

uniformly over that inner box for sufficiently large N. This is a complete qualitative logarithmic repulsion theorem for the full-wall model at bulk sites, and for sites a fixed macroscopic distance inside a partially constrained wall. No sharp constant or concentration around a single leading constant is claimed.

The source's equation (20) takes a supremum over the entire wall subbox, including its boundary. The proof above does NOT establish its lower bound on the outer layer B_M minus B_floor(eta N), when epsilon<1. Lemma 1 gives an averaged lower bound on all wall sites, but does not bound their maximum contact density. Establishing such a lower bound uniformly over the wall subbox, together with fully identifying the source's d>=3 infinite-volume law and any intended broader class of potentials, remains necessary for an answer with the source's full scope. There is no counterexample here and no assertion that these remaining conclusions fail. Proposition 8 below improves the higher-dimensional upper bound and supplies subsequential infinite-volume results without resolving this lower-bound obstruction.

## Proposition 8: ambient-volume-uniform upper bound when d>=3

For any nonempty A subset B_N, put m=|A| and h=2(log(4m)+K_d(N)/3). Denote by Q_{N,A}^b the measure with wall only on A and constant exterior boundary b. Lemma 2 directly compares Q_{N,A}^0<=_st Q_{N,A}^h; it is unnecessary to add the wall on all of B_N. The free boundary-h measure satisfies the wall on A with probability at least 1/2, by (F) and a union bound over A rather than B_N. Thus, for every site i and s>=0,

    Q_{N,A}^0(phi_i>=2h+s) <= (1/(2m)) exp(-s/2).       (U_A)

The proof repeats (U), with that wall event as the conditioning denominator. If d>=3, K_d(N)=2, so h depends only on m, not N. Consequently every wall-site mean is at most 4(log(4m)+2/3)+1/m. For A=B_M this is O(log(M+2)), uniformly over all N>=M, and uniformly over all wall sites including their boundary.

For completeness one can pass these partial results to subsequential infinite-volume laws at fixed M in d>=3. Lemma 2 also gives Q_{N,A}^0>=_st P_{N,free}^0, so its negative tail at every site is at most 2 exp(2/3-t/2). Combined with (U_A), this gives uniformly exponentially bounded tails for both signs at every fixed coordinate, independently of N for fixed A. Finite-dimensional laws are tight. Taking successive subsequences for an enumeration of the lattice and a diagonal subsequence yields consistent finite-dimensional limiting laws, and hence a probability law on the countable product (equivalently use tightness on a product of coordinate compact intervals, obtained by allocating error delta/2^k to coordinate k). Nonnegativity on A passes to the limit because it is a closed finite-coordinate event. The exponential tail bounds give uniform integrability, so one-site expectations also converge along the subsequence.

These limits have the expected finite-set Gibbs specifications: for a fixed finite D, its conditional kernel depends on finitely many exterior neighbours and the fixed wall membership in D. For exterior values in a compact set, its density is continuous in those values and dominated by C exp(-c sum_{i in D}|phi_i|), using fixed paths within D to its exterior and the triangle inequality. Its partition function is continuous and bounded away from zero on that compact set. Thus the kernel applied to any bounded continuous cylinder function is continuous in the exterior values. The finite-volume specification identity, tested against bounded continuous exterior cylinder functions, passes to the weak limit; a monotone-class argument extends it to bounded measurable cylinder functions. This proves the Gibbs specification without a uniqueness claim.

Proposition 3 gives a lower bound uniformly in N on every i in B_floor(eta M), eta<1, by taking r proportional to (1-eta)M. These bounds therefore pass to all the subsequential limits just constructed. Sending M to infinity establishes order-log-M heights on strict interior subboxes in this infinite-volume formulation. At ALL wall sites we have the upper bound and the averaged lower bound, but still lack a uniform pointwise lower bound at the wall-region edge.

One can also identify these as conditionings of subsequential free laws. The uniform free tails (F) prove tightness of the free measures in d>=3, and the same specification-continuity argument gives an atomless one-site conditional density for any limiting free law P_infinity. Enumerate the m sites of A. At every finite volume, imposing the preceding positivity constraints increases the next coordinate by Lemma 2, while its unconditioned symmetric density has positivity probability 1/2. Thus P_{N,free}(Omega_A)>=2^(-m). Along any free subsequence converging to P_infinity, the boundary of Omega_A has limiting probability zero, because it is contained in the union of m coordinate-zero events and each coordinate is atomless by its Gibbs density. Therefore the conditioning probabilities converge, and for every bounded continuous cylinder function g the numerator E[g 1_{Omega_A}] also converges (its discontinuity set has probability zero). It follows that Q_{N,A} converges along that subsequence to P_infinity(. | Omega_A). The bound 2^(-m) ensures the limiting denominator is positive. This applies to every fixed M along one free subsequence, since each finite-coordinate wall event is a continuity event. The mean and interior lower bounds above therefore apply to these actual conditional free laws, not just unspecified wall-law limits. Uniqueness of P_infinity or convergence along the entire sequence is not proved, but every zero-boundary subsequential free law has the asserted partial results.

## Referee audit

1. Kinks of |s|: only absolutely continuous slice integration and almost-everywhere derivatives are used; their uniform bounds justify Fubini. No V'' or strict convexity is used.
2. Singular edge-deleted precision matrices: covered explicitly in Lemma 4. Ignoring them would incorrectly assume A>0.
3. Dependent auxiliary edges: (D) uses conditional dominance, not independence. Marginal domination alone would not suffice.
4. Flow to an interior shell: the constructed flow stops at the ACTUAL exterior boundary; no interior sink is substituted. Early stopping can only reduce edge probabilities.
5. Wall-conditioning denominator: a free tail estimate is used AFTER shifting the exterior boundary, so it is at least 1/2. Dividing by the original exponentially small wall probability would not prove (U).
6. Lower bound uniformity: translation of full-wall subdomains is legitimate only when the relevant exterior neighbour heights are known nonnegative or pinned zero. This is precisely why the partial-wall edge case remains open here.
7. Quantifiers: the displayed probability is a supremum of individual probabilities, not a probability that EVERY height exceeds a log N. The latter is neither derived nor needed.
8. Source normalization: the paper also includes beta and a symmetric walk kernel p. For uniform nearest-neighbour p=1/(2d), its beta-weighted |s| Hamiltonian is the present one after the positive height rescaling psi=(beta/(2d))phi. The contact coefficient and height constants rescale accordingly; the order log N does not change. No statement is proved here for arbitrary finite-range kernels or arbitrary V.

## Verification appendix and earlier-attempt audit

The finite grounded chain with two free sites has H(x,y)=|x|+|x-y|+|y|. In the positive quadrant H=2 max(x,y), so its positive partition function is 2 integral_0^infinity x exp(-2x) dx=1/2. Each contact density is 1, giving contact sum 2 equal to its two exterior edges. Its positive one-site density is (2t+1)exp(-2t), CDF 1-(t+1)exp(-2t), and mean 3/4. The contact inequality with site degree 2 holds at all tested h. These formulas follow by splitting the y integral at y=x.

In the free chain, integrating y gives marginal density (2/3)(|x|+1)exp(-2|x|), since the integral of exp(-|y|-|x-y|) is (|x|+1)exp(-|x|) and the remaining marginal integral is 3/2. The exact MGF is (2/3) sum_{s=+-1}[(2+s lambda)^(-2)+(2+s lambda)^(-1)]. The unit electrical flow is (2/3,1/3,1/3), with energy 2/3. checks.py compared this MGF with the product bound at 989 lambda values up to 0.989: the maximum of exact minus bound was -2.5000018766263565e-7. This is a numerical check of the analytical bound, not its proof.

checks.py also used exact rational arithmetic to check the explicit stopped flow, including actual boundary exits and shell energy bounds, for d=2,3,4 and N=1,2,3, starting from the centre and each of two opposite corners: all 27 configurations passed. A randomized floating-point check of the two-by-two determinant identity gave maximum absolute error 1.1013412404281553e-13 over 1000 trials. Results are in checks.json.

The prior ledger F0072-A001 (2026-09-08), read from the read-only intake, proposed a determinant-tilted Gaussian mixture but left three obstructions: random-environment ellipticity, averaging uniformity, and different potentials. The present finite-volume upper-bound proof avoids an environmental hard-wall theorem entirely: it uses conditional auxiliary-variance domination in the UNCONDITIONED mixture, a deterministic flow, and stochastic comparison after shifting the boundary. Conditioning the Gaussian mixture directly on the wall would introduce P_Gaussian,t(wall) into its mixing density and would require a new domination proof; this is not asserted here. The earlier description of m as a probability mixing law needs normalization: the normalized Laplace density (1/2)exp(-|s|) has Exp(rate=1/2) variance mixture, whereas the unnormalized weight exp(-|s|) in (G) has mixing density exp(-t/2)dt, of mass 2. Edgewise constant factors cancel in the Gibbs density.

The remaining partial-wall edge obstruction was also tested conceptually against the contact identity. Its sum bound permits all contact mass to concentrate in a surface layer of O(N^(d-1)) sites, so it alone cannot yield the uniform lower bound required there. The full-wall translated-domain comparison fails across the partially constrained edge because exterior neighbour heights can be negative. An extension cannot simply reuse that comparison without checking the sign condition.

MixtureAlgebra.lean contains two small algebraic checks, including the determinant of a symmetric two-by-two rank-one update. Its role is limited to that finite algebraic step; the general determinant argument and probability proofs above are written proofs, not Lean formalizations. The Lean verification status is reported separately in lean_check.json once its invocation finishes.

Final Lean result: the corrected MixtureAlgebra.lean passed `lake env lean` from ~/lean_verify (exit code 0). The exact checked source SHA-256 is 901cfb68a1e80f19a6b863606083786877d7a0677bab226f5c72e480bfef2a63. Its two identities use ring proofs checked by Lean; no sorry or native_decide occurs. This formally checks only the finite algebraic identities, not the probabilistic theorem. The first missing-import failure is retained in lean_check_initial.json.

## Second attempt at the wall-edge gap (2026-10-12)

The user's reopening request led to two new approaches: reflected pinning/contact ratios, and exact coarea/subset recursion. The coarea route was selected and pursued. Complete new proofs and the referee audit are in SECOND_ATTEMPT.md.

New proved results: positive-domain partition recursion; exact partial-wall partition/contact/moment formulas; log-supermodularity of positive-domain partitions and their sign-set weights; an attractive pure-death-process representation of positive SOS heights; gamma total energy and temperature-independent sign-law identities; and a sufficient sign-buffer criterion for uniform edge/corner logarithmic repulsion. Exact rational tests ran on three-site, 3x3 and buffered 4x4 lattice domains. The tempting universal reflected-contact inequality was disproved, with a structural reverse inequality on root-separator graphs. An initial hand-integration coefficient error was caught and corrected by the exact recursion before being recorded as a checked claim.

Precise remaining gap after this attempt: for A=B_M and N-M>=delta M, either prove that Z(A union (i+B_R))/Z(A) tends to 1 uniformly over i in A for some R comparable to M^alpha (a sufficient sign-buffer assertion), or directly prove that the attractive death chain with random initial sign set distributed as z(S)z(V minus S)/Z(A), S containing A, retains each i in A until time a log M with probability tending to 1 uniformly (an exact equivalent of the desired pointwise lower-tail bound). Neither assertion is proved. Boolean lattice attractiveness and coarse cut/volume estimates do not supply it; the individual killing rates are nonlocal partition ratios. No general-potential extension is proved. Verdict remains PARTIAL.

Second-attempt quantitative strengthening: the coarea/death-chain route also proves that, for every eta>0 and 0<a<1/(2d), the probability of eta|B_M| or more wall heights <=a log M is bounded by exp(-c M^(d-2da)), uniformly over N>=M for large M. The exact negative-binomial domination and complete proof are in SECOND_ATTEMPT.md, Stronger quantitative partial result. Nine finite generator/analytic checks passed, and the corrected reflection cross multiplication passed Lean. This strengthens the averaged bound without filling the selected-site edge gap. Final verdict remains PARTIAL.
