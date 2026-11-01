VERDICT: PASS (correct and complete)

Independent audit of P0334, 12 October 2026. I read the claimant's STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md without modifying them. References below are to the line numbers of that ATTEMPT.md. I found no mathematical error or missing hypothesis requiring a correction. This verdict concerns the written theorem and proof, not a claim of formal verification or priority.

## Exact claim and fit to the problem

ATTEMPT.md, lines 15–19, claims the following. For every Borel probability P on R and every fixed finite real 1<p<infinity, with Q its standard left-continuous quantile and Q_n the quantile of n iid observations,

    sqrt(n)(Q_n-Q) => Y in L^p(0,1)

if and only if Q is locally absolutely continuous and

    K_p(Q) = integral_0^1 [t(1-t)]^(p/2) |Q'(t)|^p dt < infinity.

The limit has the law of -Q'B, where B is a standard Brownian bridge. The conditions imply Q belongs to L^p. This is a distribution-by-distribution criterion for the entire finite p>1 family, not just a smooth-density or bounded-support case. Atoms and singular components are allowed subject to the quantile conditions; a point mass is included. It does not claim convergence simultaneously in multiple spaces, a bootstrap theorem, or a p=infinity result.

I independently downloaded arXiv:2505.19104, obtaining the 43-page July 2026 revision. Problem 2 on PDF page 29 asks precisely for necessary and sufficient conditions for this standard quantile process to converge weakly in L^p. Theorem 2.4 on page 9 has the endpoint monotonicity assumption. The claimant's criterion answers the remaining finite p>1 question and removes that assumption. The supplied problem caveat already excludes the established p=1 case from the remaining task.

## External results checked against original documents

The source downloads and extracted text are in this audit folder; URLs and HTTP outcomes are recorded in source_fetch_log.json. They were fetched independently rather than copied from the claimant's folder.

1. **Bobkov–Ledoux input, lines 23–27.** The author-hosted original MEMO.pdf has 140 pages. Theorem 5.3 on page 46 gives the claimed upper bound

       E W_p(mu_n,mu)^p <= (5p/sqrt(n+2))^p J_p(mu).

   Corollary A.22 on page 109 equates J_p to the weighted quantile derivative integral when the quantile is absolutely continuous. Proposition A.17 on page 104 explicitly concerns the density of the absolutely continuous *component*, permitting additional discrete or singular continuous components. Page 51 explicitly states the local convention for absolute continuity. I also checked Proposition B.13 on page 125, which gives the underlying derivative bound for arbitrary absolutely continuous functions. No endpoint monotonicity or strict quantile increase is required. A constant auxiliary H is harmless: its transport distance and derivative integral are both zero, independently of any nondegeneracy convention in Proposition A.17.

2. **Beare–Kaji input, line 29.** The downloaded arXiv:2502.01254v4 has 22 pages. Property Q on page 1 is local absolute continuity and finiteness of the weighted Stieltjes integral. Theorem 3.1 on page 16 gives the L^1 limit -qB; Theorem 3.2 on the same page proves necessity under Q in L^1. These are exactly the inputs used. They do not settle the p>1 task on their own.

3. Donsker with asymptotic equicontinuity and Fernique for a Gaussian random element in separable L^p are standard results with the applicable hypotheses here. The proof establishes Gaussianity before invoking Fernique. It does not require a new version of either theorem.

## Step-by-step mathematical checks and possible failure points

**Lemma 1, lines 35–41: endpoint integrability.** I re-derived the weighted Holder estimate. On (0,1/2), insert s^(1/2) into r' and its reciprocal into the integration factor, using s(1-s) comparable to s. The conjugate exponent is p*=p/(p-1). If p>2, p*/2<1 and the remaining integral is uniformly bounded. If p=2, it is logarithmic. If 1<p<2, its (p-1)-st power is bounded by a constant times t^(p/2-1). This exponent exceeds -1. Thus the bound is integrable in all three cases; reflection handles the other endpoint. Local absolute continuity is sufficient, because each fundamental-theorem calculation is on an interior interval. This proves L^p membership for signed r as well as for Q. In particular, the observation at line 128 that p>2 forces bounded Q is consistent with the calculation.

**Lemma 2, lines 45–56: the crucial signed residual bound.** A signed residual need not be a quantile, so direct use of the transport theorem on r would be invalid. The proof avoids that error. For H(t)=integral_(1/2)^t |r'(s)|ds, on every interior interval

    |r(v)-r(u)| <= integral_min(u,v)^max(u,v) |r'| = |H(v)-H(u)|.

H is finite and continuous at every interior point, nondecreasing, locally absolutely continuous, and in L^p by Lemma 1. Its derivative integral is exactly K_p(r). I checked the inverse identity in line 54: x>=H(t) gives F_H(x)>=t; for x<H(t), continuity supplies t_0<t with H(t_0)>x, so F_H(x)<=t_0<t. This works on flat segments as well. Sorting the transformed sample, including ties, gives empirical quantile H(V_n). Consequently the expected transport bound applies to H on the same uniform sample. Multiplication by n^(p/2) gives the factor (n/(n+2))^(p/2)<=1. The first-moment estimate then follows from Holder on the probability space. This closes the potential endpoint approximation gap; it does not merely bound norms of the original processes.

**Lemma 3, lines 60–71: reference convergence.** With the stated convention at t=0 and no uniform-sample ties, G_n(V_n(t))=ceil(nt)/n for t>0, and the discrepancy at t=0 is 1/n. Hence the inversion identity and the 1/sqrt(n) error bound hold, including the endpoint conventions. The displayed bound on V_n-id follows immediately. Asymptotic equicontinuity then replaces alpha_n(V_n) by alpha_n uniformly in probability. A C^1 extension of Q_0 to [0,1] exists because g_0 vanishes near the endpoints. The fundamental theorem gives the stated modulus-of-continuity remainder. The conclusion in L^p follows from the uniform reference-process limit. The proof's phrase “usual uniform empirical-process sense” is the standard Donsker interpretation; no assertion that the raw empirical process is a Borel random element of the full nonseparable sup-norm space is needed. Its final L^p processes are measurable.

**Sufficiency, lines 75–95: tightness and passage to the limit.** Truncation followed by nonnegative convolution does give nonnegative smooth compactly supported approximants in the weighted L^p derivative norm. There is no regularity assumption on g being smuggled into this step. The map T_n is linear in its function argument on the common uniform sample, so Lemma 2 applies exactly to Q-Q_m. The errors in (E) tend to zero uniformly over n. Independently, E|B(t)|^p=M_p[t(1-t)]^(p/2); Tonelli gives both equalities in (G) and L^p-valuedness of gB. The three-term bounded-Lipschitz comparison at line 93 is valid: the middle term tends to zero for fixed m, and the other two terms are at most 5p a_m and M_p^(1/p)a_m. Letting m tend to infinity proves weak convergence in separable L^p. This is a valid convergence-by-approximation argument, not an inference of tightness from bounded moments. The final quantile-transform and sorting identities cover arbitrary P.

**Necessity, lines 99–116: Gaussianity, moments, and identification.** For any finite sample on R, Q_n is in L^p. Thus the assumed L^p-valued differences force Q in L^p, and the continuous inclusion into L^1 makes Beare–Kaji applicable. This yields local absolute continuity, finite J_1, and the L^1 law of -gB.

For bounded measurable h, Minkowski gives an L^2 bound by ||h||_infinity J_1 for the integral against gB. Interior truncations converge in L^2. On each interior interval, uniform mean-square continuity of B and integrability of hg justify finite Gaussian approximations, so the integral is centered Gaussian. Equality of L^1 laws transfers this assertion to integral hY. Bounded truncations are dense in L^(p*) because p* is finite; Holder gives almost sure convergence of the corresponding functionals of Y. A weak limit of centered Gaussian real variables is centered Gaussian, with tightness excluding diverging variances. Thus every continuous linear functional of Y is Gaussian, establishing a Gaussian Radon law in separable L^p. Fernique now legitimately supplies E||Y||_p^p<infinity.

Finally, f -> integral min(|f|^p,K) is continuous on L^1: the scalar truncation is globally Lipschitz with constant p K^((p-1)/p). Its increasing limit is the extended p-integral, hence Borel measurable. Therefore the equality of L^1 laws transfers the distribution of this extended norm without assuming that gB is already L^p-valued. Tonelli yields E||Y||_p^p=M_p K_p(Q), forcing the required finite K_p. This step is not circular and does not assume convergence of prelimit norm moments.

**Issues requiring fixes:** none. The delicate points above all survive independent checking at the cited locations.

## Independent computations and counterexample checks

I wrote and ran independent_checks.py in this folder, without using the claimant's numerical or Lean artifacts. Results are in independent_checks.json.

- Exact rational polynomial integration for r(t)=t^2-t, p=2, n=1 gives E||T_1 r||_2^2=1/90 and K_2(r)=1/30. This tests a genuinely signed derivative.
- For a piecewise linear signed residual with thin endpoint spikes, alternating slopes, and a flat interval, 200,000 independent random (u,v) pairs satisfied the envelope inequality up to maximum floating-point excess 2.22e-16.
- Deterministic split Gauss–Legendre quadrature, integrating the appropriate beta order-statistic densities, tested the expected norm bound for p=1.25,2,4 and n=1,3,20. No violation occurred; the largest ratio to the asserted weakened upper bound was approximately 0.06184. These quadratures are approximate spot checks, not certified estimates or a proof of the infinite-dimensional theorem.
- The inverse-process identity was checked on grids including order-cell boundaries and both endpoints for n=1,3,20,300. Its maximum error was the asserted 1/sqrt(n), up to rounding.
- As an analytic negative control, a nondegenerate Bernoulli quantile has an interior jump and is excluded by local absolute continuity. Its L^p process norm has p-th power n^(p/2)|p_n-p|, of typical order n^((p-1)/2), consistent with failure for p>1. Merely testing its a.e. derivative, which is zero, would incorrectly include it; the theorem retains the necessary absolute-continuity condition. Beare–Kaji pages 2–3 also explicitly discuss irregular quantiles, including a continuous non-absolutely-continuous example. These do not contradict the claim.

## Brief literature search and its limits

I queried the arXiv API for the exact phrase “quantile process,” ordered by last update, and inspected the 40 returned titles and relevant abstracts. I queried OpenAlex for “quantile process Lp,” obtaining ten results, and inspected relevant records. Both searches returned HTTP 200. Raw responses are retained in arxiv_search.response.txt and openalex_search.response.txt.

The arXiv results include Beare–Kaji and arXiv:2606.28222, concerning weighted approximations for uniform increments. The latter abstract does not assert the arbitrary-distribution standard empirical-quantile criterion proved here. OpenAlex also identified Csorgo–Horvath–Shao, “Convergence of integrals of uniform empirical and quantile processes” (1993), and Norvaisa, “The central limit theorem for empirical and quantile processes in some Banach spaces” (1993). I fetched their OpenAlex and Crossref metadata, retained in older_literature.json and older_crossref.json. Neither service supplied their abstracts. Beare–Kaji page 3 explicitly distinguishes the 1993 weighted uniform-process result from the standard empirical-quantile construction and explains its altered endpoint convention. I have not verified the full Norvaisa paper and do not claim to rule out overlap with it.

No earlier solution or known counterexample to this exact theorem was established by this bounded search. That is not proof of novelty. The July 2026 survey still poses this question, but that too is not a priority guarantee. The claimant's SOLVED verdict is supported by its actual argument, not by a SOLVED_IN_LITERATURE attribution.

What is proved: the full finite 1<p<infinity necessary-and-sufficient criterion and the asserted Gaussian limit, using the verified published inputs and standard Donsker/Fernique results. What is not proved by this audit: novelty, an infinity-norm criterion, bootstrap validity, or a complete machine formalization. The computations are supplementary checks only.
