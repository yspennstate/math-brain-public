VERDICT: PASS (correct and complete)

# Independent audit of C0119

Audit date: 2026-10-12. Read-only claimant directory: `~/brain_workers/TRIO_1011/op/C0119`. All downloaded papers, scripts, and results for this audit are in this audit directory. I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl, and LITERATURE.md. Line references below refer to the claimant's ATTEMPT.md as read during this audit; `attempt_numbered.txt` preserves those references locally.

The written argument proves the precisely stated Gaussian results using valid published variance theorems. I found no failed mathematical step and no substantive gap requiring repair. This verdict concerns mathematical correctness and coverage of the cited source question, not originality or comprehensive coverage of all possible meanings of “random environment.”

## What is claimed, and whether it answers the source question

ATTEMPT.md lines 7–11 claim the following. For iid standard Gaussian vertex weights on the positive-coordinate directed lattice in dimension k >= 3, let P_n be the maximum-weight path starting at the origin and containing n vertices, with free endpoint. Under the coupling X^t = exp(-t)X + sqrt(1-exp(-2t))Y,

    E|P_n(X) intersect P_n(X^t)| / n
        <= C_k / ((1-exp(-t)) log n),  n >= 3, t > 0.

Consequently, for every positive sequence t_n tending to zero with t_n log n tending to infinity, normalized expected overlap tends to zero. The same proof covers k = 2, whereas the single-path k = 1 model does not exhibit chaos. The coordinatewise mean-square perturbation is 2(1-exp(-t_n)), which tends to zero. Ground-state delta measures have total variation tending to one in mean and probability (lines 110–112).

Lines 13–23 additionally claim a finite-temperature result for iid standard Gaussian time-site weights and free-endpoint nearest-neighbor paths in every fixed spatial dimension d >= 1, hence d >= 3. For each fixed beta > 0 the two-environment replica overlap Q_n(t) obeys the same logarithmic bound, with constant depending on d and beta. At every fixed beta > sqrt(2 log(2d)),

    Q_n(0)/n >= 1 - sqrt(2 log(2d))/beta > 0,

whereas Q_n(t_n)/n tends to zero for the stated noise sequences. The expected total variation of the Gibbs measures has liminf at least this positive constant (lines 157–165).

I independently downloaded https://arxiv.org/pdf/0810.4221 into `source.pdf` and extracted `source.txt`. Page 59, Section 12(2), actually asks:

> Prove chaos in directed polymers in dimensions >= 3. Certain parts of the current proof do not work in higher than 2 dimensions, but other parts are okay. Since the Benjamini-Kalai-Schramm approach is inherently dimension-free, this seems to be a more doable open problem.

Pages 37–38, Section 8, explicitly define iid standard Gaussian weights, positive-coordinate paths with n vertices including the origin, free endpoint, and a maximum-weight ground state. They use exactly the OU perturbation and vertex-overlap observable above. Thus the Gaussian ground-state theorem answers the exact source question in its stated model. The words “at low temperature” and “polymer measure” in the intake are paraphrases, not additional conditions appearing in Section 12(2). The claimant nevertheless proves a conventional finite-temperature Gaussian statement as well. The dimension conventions are handled correctly: k is the positive-coordinate lattice dimension; d in the extra theorem is the spatial dimension of a space-time polymer.

## Step-by-step mathematical checks

1. **OU identity and monotonicity, Section 2, lines 29–58, equations (4)–(8).** I re-derived the identities directly. With a = exp(-t) and b = sqrt(1-a^2), differentiating E f(ax+bY) gives -a x dot E grad f + (a^2/b) E[Y dot grad f]. Gaussian integration by parts turns the second term into a^2 E Delta f, hence the OU generator Delta-x dot grad. Integration by parts against the Gaussian measure then gives

       d/dt Cov(f(X),f(X^t))
           = -exp(-t) sum_j E[partial_j f(X) partial_j f(X^t)].

   Bounded gradient implies Lipschitz continuity and L2 convergence at both required endpoints, so integration over t gives the variance identity without an omitted boundary term. Self-adjointness and the semigroup law give A_f(t) = sum_j ||T_(t/2) partial_j f||_2^2. Gaussian invariance and Jensen give L2 contraction, proving that A_f is nonnegative and nonincreasing. Integrating only from 0 to t therefore gives Var(f) >= (1-exp(-t)) A_f(t). The sign, factor exp(-t), and denominator are correct.

2. **Gibbs gradient and overlap, Section 3, lines 64–82, equation (9).** Differentiating beta^-1 log Z gives the occupancy p_j, with 0 <= p_j <= 1 and sum_j p_j = n. Thus sum_j p_j^2 <= n and the free energy is sqrt(n)-Lipschitz. Conditional independence of replicas gives overlap sum_j p_j(X)p_j(X^t). Time-site indexing matters: repeated spatial positions at different times correspond to different Gaussian coordinates. The claimant uses this convention correctly. Deterministic positive prior weights enter the Gibbs probabilities but introduce no extra derivative factors. Consequently Var(G_beta) = integral exp(-t) Q(t) dt and Q(t) <= Var(G_beta)/(1-exp(-t)) follow exactly.

3. **Zero-temperature limit, lines 84–92, equations (10)–(11).** For fixed finite path family, 0 <= G_beta-M <= log(K)/beta is a deterministic uniform bound. Distinct paths in each relevant graph have distinct incidence vectors; their weight difference is a nondegenerate Gaussian. The finite union of tie events has probability zero. Therefore occupancy converges to the unique maximizer's indicator in both environments. L2 convergence of the free energies and bounded convergence of overlaps justify passage to the maximum inequality; domination by n exp(-t) also justifies the integral identity. No beta-dependent variance constant is passed to beta = infinity.

4. **Equivalence and limiting quantifiers, lines 94–98 and 110.** With a_n = max(Var(G_n)/n,1/n), t_n = sqrt(a_n), the upper bound on normalized overlap is at most 2 sqrt(a_n) eventually. In the reverse direction, splitting the integral at t_n and using monotonicity gives precisely equation (96). For the claimed logarithmic rate, 1-exp(-t_n) >= t_n/2 eventually, so every stated noise sequence works. Dimensions and finite beta are fixed before n tends to infinity; no uniform-in-beta claim is used.

5. **Ground-state variance input, Section 4, lines 102–114, equation (12).** I downloaded https://arxiv.org/pdf/0909.1352 into `graham.pdf`, extracted `graham.txt`, and directly checked the graph and weight conventions on page 2 and Theorem 6.1 on pages 14–15. Graham defines positive-coordinate edges, excludes the starting vertex from T, and defines S_N = {x in Z_+^k: |x| = N}. The theorem explicitly states Var(T(0,S_N)) = O(N/log N) for iid standard Gaussian weights in every k >= 2. Thus the exact decomposition M_n = X_0 + T(0,S_(n-1)) is correct; X_0 is independent of the second term. Adding its variance 1 and replacing n-1 by n gives equation (12), including small n after enlarging the constant. The second theorem bound explicitly covers the nearest-neighbor space-time graph in k-1 spatial dimensions. Neither endpoint constraints nor a two-dimensional rotation have been substituted into the main proof.

6. **Finite-temperature variance input, Section 5, lines 118–126, equation (13).** I downloaded https://arxiv.org/pdf/2103.09199 into `surface_growth.pdf` and extracted `surface_growth.txt`. Pages 8–9 explicitly allow every spatial d >= 1, fixed beta, and iid environment given by a Lipschitz image of a standard Gaussian. The identity map gives the needed standard Gaussian model. Theorem 2.4(3) states Var(f(t,x)) <= Ct/log t for t >= 2. Its displayed time-reversed representation has the same single-environment law as beta^-1 log Z_t. The paper uses t transitions but weights only its first t vertices. Each claimant path with n weighted vertices has exactly 2d completions by an unweighted final step, so the partition functions differ by the deterministic factor 2d. The claimant needs equality in law only for variance, not equality of coupled quenched measures. These hypotheses and conventions all match. The overlap bound is consequently valid for n >= 2 and t > 0. The display at lines 18–21 could state that domain explicitly; n = 1 has log n = 0 and is irrelevant to the asymptotic theorem. This is a notation clarification, not a gap in the argument.

7. **Low-temperature baseline, Section 6, lines 130–155, equations (14)–(15).** I independently differentiated an occupancy and obtained partial_j p_j = beta(p_j-p_j^2). Gaussian integration by parts then gives E U_beta = beta(n-Q(0)). Every path energy has law N(0,n), even though energies of different paths are correlated. The pointwise inequality exp(lambda M) <= sum_p exp(lambda H_p) and Jensen give E M <= log(K)/lambda + lambda n/2. Optimizing at lambda = sqrt(2 log(K)/n) gives sqrt(2n log(K)); the K = 1 case is handled separately. Since U_beta <= M and K <= (2d)^n, the advertised baseline follows with the correct constant and inequality direction. The probability lower bound c/(2-c) follows by bounding an overlap fraction in [0,1] by c/2 on its lower event and by 1 elsewhere. Markov's inequality gives the stated perturbed overlap and quenched-in-probability conclusions.

8. **Sensitivity of the measures, lines 112 and 157–165, equation (16).** Equality of ground-state paths forces overlap n, so its probability is at most expected overlap divided by n. Total variation of two delta masses is exactly the indicator that their locations differ. For finite beta, f_X(s') is a valid [0,1]-valued test function even though it depends on X. For each fixed pair of environments, the difference of its integrals is bounded in absolute value by total variation. Taking expectation yields (Q_n(0)-Q_n(t))/n as claimed. The conclusion is a positive lower bound on expected total variation, not convergence to one or a high-probability lower bound of the same magnitude.

9. **Boundary case, Section 7, lines 169–171.** A positive-coordinate one-dimensional graph has exactly one path. Its Gibbs measure is environment-independent, overlap is always n, and the sum of n independent Gaussian weights has variance n. This correctly defeats the inference “positive overlap alone implies superconcentration” without contradicting the theorem for dimensions >= 3.

## Independent computations and their limitations

I wrote `independent_checks.py` without importing or executing claimant code. `independent_results.json` records a fixed-seed, 200,000-sample experiment in the d = 3, n = 2, beta = 4 nearest-neighbor model, with one common origin and six possible weighted terminal sites. Setting rho uniformly in [0,1] checks the variance identity through the equivalent integral integral_0^1 Q(-log rho) d rho.

- Finite-temperature estimated variance: 1.371312; estimated overlap integral: 1.372391. The paired residual is -0.001086 with standard error 0.004416.
- Ground-state estimated variance: 1.414091; estimated overlap integral: 1.416625. The paired residual is -0.002541 with standard error 0.004623.
- Both sampled overlap curves decrease across t = 0, 0.01, 0.1, 0.5, 2, 10. At large t they approach 1 + 1/6, as required by independent terminal choices and the common origin.
- Central differences give maximum free-energy gradient error 3.15e-11 and maximum diagonal occupancy-derivative error 4.25e-11.
- Explicit enumeration of 36 paths with three weighted vertices and their 216 unweighted-step completions gives a partition-function ratio 5.9999999999999964. An independent positive-coordinate enumeration gives origin-decomposition error 2.23e-16 and distinct incidence sets for distinct paths.
- Mean same-environment overlap is 1.702357, above the baseline lower bound 1.053491.

The Monte Carlo integration-by-parts residual is +0.010902 with standard error 0.003887, approximately 2.805 standard errors. This is recorded rather than discarded. To check the identity by a different method without repeatedly resampling, I wrote `deterministic_checks.py`. Conditional on five competing terminal weights, the sixth-site occupation is logistic(4x-log(sum exp(4w_i))). Gaussian quadrature directly compares E[x p(x)] and E[4p(x)(1-p(x))]. Across 30 fixed conditioned configurations the maximum discrepancy is 6.35e-10 with 256 nodes and 3.67e-14 with 512 nodes. The origin identity is exactly E X_0 = 0 with constant occupancy. This deterministic check supports the analytic integration-by-parts derivation; the Monte Carlo fluctuation is not evidence of a failed identity.

The same script integrates the maximum-of-six density 6 phi(z) Phi(z)^5 and obtains ground-state variance 1.415927109 after adding the independent origin variance, consistent with both sampled estimates. Quadrature error estimates and outputs are in `deterministic_results.json`. These finite-volume computations are numerical checks, not certified asymptotic proofs. The asymptotic result rests on the analytic argument and the cited published theorems.

The claimant's lines 187–199 distinguish computational illustrations and three Lean algebra checks from the probabilistic proof. I did not independently rerun its Lean environment or certify its reported execution logs. Those checks are unnecessary to establish the elementary algebra, which I verified directly above, and do not formalize the covariance identity or either literature theorem.

## Bounded independent literature search

I used Python HTTP requests only, with no built-in web search. Exact URLs and responses are preserved in `search_log.json`, `search_arxiv.txt`, and the downloaded PDFs/texts. The arXiv query was `(all:"directed polymer" OR all:"last passage") AND (all:chaos OR all:"noise sensitivity")`, with a 25-result cap. OpenAlex search for `directed polymers disorder chaos`, capped at 12 results, returned HTTP 429. That failure limits coverage and is not evidence of absence.

The search found Ahlberg–Deijfen–Sfragara, *From stability to chaos in last-passage percolation*, arXiv:2302.11379v2. I fetched `stability_chaos.pdf`, extracted `stability_chaos.txt`, and inspected pages 1–5. Theorem 1.1 proves chaos in dimensions d >= 2 for point-to-point up-right paths, under independent-resampling noise, with nonnegative weights satisfying a tail moment condition and a uniform positive lower bound on conditional tail variances. This is relevant earlier literature but not the exact free-endpoint Gaussian OU statement audited here. In particular its conditional tail-variance assumption does not cover standard Gaussian weights, and its model assumes nonnegative weights. It supplies no counterexample to the claimant's argument.

Other returned papers include *Stability and chaos in dynamical last passage percolation* (arXiv:2010.05837, Brownian LPP), *Enhanced noise sensitivity, 2D directed polymers and Stochastic Heat Flow* (arXiv:2507.10379, critical two-dimensional scaling), and *Temperature chaos in directed polymers* (arXiv:2607.18194, continuum polymer and temperature perturbations). Their abstracts concern different models or perturbations. The downloaded Chatterjee surface-growth paper also explicitly credits Alexander–Zygouras with the finite-temperature variance bound and Graham with all-dimensional zero-temperature superconcentration. Thus the key inputs are established literature, not new claims by this claimant. This bounded search does not establish that no previously printed exact chaos theorem exists.

## Issues and scope limits

No substantive mathematical issue was found. The only display-level clarification is to attach n >= 2, t > 0 to equation (2), as already supplied by the applicable variance theorem and the derivation.

The exclusions at ATTEMPT.md lines 25 and 203 are necessary and accurate. The proof does not establish chaos for every disorder distribution, positive-coordinate finite-temperature paths in every dimension, temperature perturbations, continuum polymers, constrained endpoints, an optimal chaos scale, or every beta in a separately defined entire low-temperature phase. It establishes a sufficient fixed-beta low-temperature regime for the conventional Gaussian model. It also does not establish total variation tending to one at fixed finite beta. None of these stronger assertions is claimed, and none is required by the exact source question once its Section 8 model is read.

Accordingly the Gaussian source problem is proved, and the additional finite-temperature Gaussian theorem is proved with the stated quantifiers and limitations. No unproved conjecture or sketch is needed to obtain those conclusions.
