VERDICT: PASS

The claimed finite-p theorem is correct and complete on the stated assumptions. I found no failed mathematical step and no required correction. This verdict concerns the proof, not priority or publication status.

## Exact claim and fit to P0334

ATTEMPT.md lines 15?19 claim: for every Borel probability P on the real line and every fixed finite 1<p<infinity, the standard iid empirical quantile process sqrt(n)(Q_n-Q) converges weakly in L^p(0,1) if and only if Q is locally absolutely continuous and

    K_p(Q) = integral_0^1 [t(1-t)]^(p/2) |Q'(t)|^p dt < infinity.

The conditions also imply Q belongs to L^p. The limit is -Q'B for a standard Brownian bridge, with the same law as +Q'B. The quantile is the standard generalized inverse, not an endpoint-trimmed or modified quantile.

I independently downloaded the source arXiv:2505.19104, checked Theorem 2.4 on PDF page 9 and Problem 2 on PDF page 29. This is the correct process and topology. The result covers the whole remaining finite p>1 family, not just smooth densities, and removes endpoint monotonicity. The known p=1 result is used as an ingredient and not presented as new. Infinity is expressly excluded; the source's J_p formulation and the supplied problem concern the finite-p family. No simultaneous-in-p assertion is needed.

## Issues found

None requiring a fix. The potentially fatal points below were checked against the actual proof and original sources. The claimant's numerical and Lean reports were not used as proof or accepted as independent verification.

## Independent mathematical checks

1. **Integrability at both endpoints ? lines 35?41.** Re-derived weighted Holder with conjugate exponent q=p/(p-1). On (0,1/2), the second factor is [integral_t^(1/2) s^(-q/2) ds]^(p-1). It stays bounded for p>2, is log((1/2)/t) for p=2, and is bounded by a constant times t^(p/2-1) for 1<p<2. The last exponent is greater than -1. Reflection treats the other endpoint. This establishes L^p-valuedness before any transport theorem is used; it also applies to signed functions and the increasing envelope. For p>2 it implies boundedness, as noted at line 128.

2. **The published uniform bound and its scope ? lines 23?27, 50?56.** Independently retrieved Bobkov?Ledoux from the author's exact MEMO.pdf URL. Theorem 5.3, PDF page 46, states E W_p(mu_n,mu)^p <= (5p/sqrt(n+2))^p J_p(mu). Corollary A.22, page 109, gives precisely the weighted quantile derivative identity used here. Proposition A.17, page 104, explicitly permits discrete and singular continuous components and requires positivity only of the absolutely continuous component on the support interval. Local absolute continuity is explicit on pages 104 and 51. Thus no assumption of a wholly absolutely continuous measure, strictly increasing quantile, or endpoint monotonicity was lost. Proposition B.13, page 125, additionally confirms the corresponding weighted bound for general absolutely continuous functions. A constant envelope is a point mass and the bound is trivially zero; the nondegeneracy language of Proposition A.17 causes no exception to the argument.

3. **Signed-envelope reduction ? lines 45?56.** For interior u<v, the fundamental theorem gives |r(v)-r(u)| <= integral_u^v |r'| = H(v)-H(u). Reversing the order gives the same comparison. The oriented primitive is finite on every interior point even when endpoint total variation is infinite. Its derivative has exactly the weighted p-integral of r'. For every interior t, monotonicity gives F_H(H(t))>=t, whereas continuity from the left gives F_H(x)<t when x<H(t). Hence H really is the standard quantile of H(U), including flat portions. Sorting and the empirical quantile formula remain valid with ties. Multiplication by n^(p/2) in Theorem 5.3 introduces [n/(n+2)]^(p/2)<=1. This proves both estimates (A). A signed residual itself is never incorrectly treated as a quantile.

4. **Smooth reference convergence ? lines 60?71.** Re-derived the empirical inverse identity. With no uniform-sample ties, G_n(V_n(t))=ceil(nt)/n for t>0 and G_n(V_n(0))=1/n under the stated extension. The error from t is at most 1/n, including endpoints. Consequently beta_n=-alpha_n composed with V_n+e_n with ||e_n||_infinity<=n^(-1/2). Tightness of alpha_n's uniform norm gives V_n-id=o_P(1), and empirical-process asymptotic equicontinuity gives alpha_n composed with V_n-alpha_n=o_P(1). The Taylor remainder bound by ||beta_n||_infinity times the derivative modulus follows directly from integration. Donsker is used in its usual empirical-process sense; the final conclusion concerns measurable random elements in separable L^p. No illegitimate L^p point evaluation is used.

5. **Approximation and full sufficiency ? lines 75?95.** Compact truncation removes arbitrarily small weighted derivative mass; on the retained interval the weight is bounded away from zero. Nonnegative mollification and a diagonal sequence give the asserted smooth approximation without extra derivative regularity. The residual is locally absolutely continuous, so item 3 bounds its process uniformly over all n on the same uniform sample. Tonelli and E|B(t)|^p=M_p[t(1-t)]^(p/2) give both identities (G). These identities supply a measurable L^p-valued Gaussian candidate and convergence of its approximants. For each bounded 1-Lipschitz test function, the three-term comparison gives exactly the constant 5p+M_p^(1/p) in line 93. Letting m increase proves weak convergence. This is a valid approximation argument, not an inference of tightness from bounded moments. Finally monotone transformation of the uniform order statistics reproduces the actual empirical quantiles, including atoms.

6. **Local absolute continuity is necessary ? lines 99?101.** Each empirical quantile has finitely many finite values. Membership of Q_n-Q in L^p therefore forces deterministic Q in L^p, and hence in L^1. The continuous L^p-to-L^1 embedding transfers weak convergence. Independently checked Beare?Kaji arXiv:2502.01254v4, Property Q on page 1 and Theorems 3.1 and 3.2 on page 16: they give exactly local absolute continuity, finite integral sqrt(t(1-t))Q'(t)dt, and the L^1 limit law used here. No density smoothness or absence-of-atoms condition is needed.

7. **Gaussianity, Fernique, and necessary K_p ? lines 103?116.** For bounded h, the L^2 norm of the stochastic integral is bounded by integral |h|Q' sqrt(t(1-t))dt. Truncation to compact intervals and L^2-continuity of the bridge justify approximation by finite Gaussian sums. The L^1 law identifies the bounded integral tests of Y as centered Gaussian. Since p>1 is finite, bounded truncations are dense in the dual L^(p/(p-1)); Holder gives almost-sure convergence of their evaluations on Y. A weak limit of centered normal distributions is centered normal, with tightness excluding unbounded variances. Thus Y has a centered Gaussian Radon law in separable L^p and Fernique applies. The truncated scalar function min(|x|^p,K) is globally Lipschitz, with constant at most p K^((p-1)/p); its integral is continuous on L^1. Therefore the extended p-integral is Borel, and the L^1 law legitimately transfers the p-norm distribution. Tonelli then gives E||Y||_p^p=M_p K_p(Q)<infinity. This does not assume norm-moment convergence of the original empirical processes.

## Independent exact and numerical checks

The newly written independent_checks.py and independent_checks.json record checks made in this audit folder:

- Exact rational beta-order-statistic moments for Q(t)=t at n=1,2,3,10,100 give n E||Q(V_n)-Q||_2^2=1/6=K_2(Q).
- For the signed function r(t)=t-t^2 at n=1, exact integration gives E||r(U)-r||_2^2=2 Var(r(U))=1/90 and K_2(r)=1/30.
- A continuous piecewise linear signed residual with flat portions, alternating slopes, and narrow spikes at both endpoints was tested for p=1.25,1.5,2,4 and n=1,3,16,64, with 150 samples per pair. Process p-integrals were calculated analytically on each intersected linear segment. All 2,400 integrated comparisons obeyed envelope domination. Of 240,000 additional pointwise comparisons, the largest floating-point excess was 4.44e-16. Every sample-average moment was below the claimed bound, whose constant is loose; this is only a finite sanity check.
- For Q(t)=-t^(-a), independently obtained K_p=a^p Beta(1-p(a+1/2),1+p/2), finite exactly when a<1/p-1/2 for a>0. For p=1.5,a=0.1 this is approximately 0.29239715. This agrees with the endpoint exponents in Lemma 1 and permits unbounded quantiles when p<2.
- A Bernoulli quantile has derivative zero almost everywhere but a jump. Its process p-norm to the pth power is n^(p/2)|hat(theta)-theta|, which diverges in probability for p>1 and 0<theta<1 by the binomial CLT. This independently confirms why local absolute continuity cannot be dropped from the criterion despite the zero derivative integral.

These checks support finite identities and comparisons only. The infinite-dimensional convergence conclusion rests on the analytic argument checked above.

## Bounded literature search and limits

All retrievals used Python requests; no built-in web search or image tool was used. Fresh copies of the three PDFs, extracted text, and request records are saved here (fetch_log.json). The arXiv exact-phrase search returned 66 entries; their titles and relevant abstracts were screened. The p=1 Beare?Kaji paper and the recent uniform-increment weighted approximation paper arXiv:2606.28222v2 do not state the claimed full p>1 criterion. The source itself still poses Problem 2.

OpenAlex returned 20 results for "quantile process Lp" and 10 for "necessary sufficient quantile process Lp". Relevant older leads include Csorgo?Horvath?Shao's 1993 "Convergence of integrals of uniform empirical and quantile processes", Norvaisa's 1993 "The central limit theorem for empirical and quantile processes in some Banach spaces", and Csorgo?Shi's 2005 "An Lp-view of the Bahadur-Kiefer Theorem". Crossref verified the latter two titles and authors but supplied no abstracts. Their absence of abstracts limits priority screening; I do not assert that these papers cannot contain overlapping results. Beare?Kaji page 3 describes the 1993 weighted uniform theorem and specifically explains that its endpoint-modified uniform inverse differs from the standard empirical quantile. It cannot simply be substituted for the present process.

Search responses and screening are saved as arxiv_search.txt, openalex_search.txt, literature_screen.json, openalex_exact.json, crossref_1993.json, crossref_2005.json, and followup_log.json. No earlier exact solution or contradicting theorem was established by this bounded search. No claim of exhaustive novelty is proved. This is a PASS on the written SOLVED proof, not a SOLVED_IN_LITERATURE finding.

## What is established and what is not

Established: the stated necessary and sufficient criterion and bridge limit for every fixed finite p>1, without endpoint monotonicity, including all probability measures whose quantiles satisfy the criterion. Together with the separately established p=1 theorem, this answers the finite-p question.

Not established: a p=infinity theorem, simultaneous convergence over varying p, bootstrap extensions in L^p, exact sharp constants in the empirical moment bound, or priority over all earlier literature. None is part of the claim requiring verification.
