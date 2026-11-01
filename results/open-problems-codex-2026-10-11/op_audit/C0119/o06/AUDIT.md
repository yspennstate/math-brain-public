VERDICT: PASS (correct and complete)

Independent audit of C0119, 12 October 2026. I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md in the claimant's folder without modifying them. Locations below refer to the current ATTEMPT.md line numbers. The verdict accepts the precisely stated Gaussian results and the actual source question. It does not certify a theorem for arbitrary random environments or originality.

## Exact claim and match to the source

ATTEMPT.md Section 1, lines 7–25, makes two distinct assertions:

1. For iid standard Gaussian vertex weights and free-endpoint positive-coordinate paths with n vertices in Z_+^k, k>=3 (indeed k>=2), the unique maximizing paths in environments X and X^t=e^(-t)X+sqrt(1-e^(-2t))Y satisfy

   E|P_n(X) intersection P_n(X^t)|/n <= C_k/[(1-e^(-t))log n], n>=3, t>0.

   Hence overlap vanishes for every positive sequence t_n->0 with t_n log n->infinity. The coordinatewise perturbation has mean-square size 2(1-e^(-t_n))->0. Ground-state measures have total variation tending to one in probability and expectation.

2. For free-endpoint nearest-neighbor polymers in spatial Z^d, iid standard Gaussian space-time disorder, fixed d>=1 and fixed beta>0, the corresponding independently sampled Gibbs replicas have Q_n(t)/n <= C(d,beta)/[(1-e^(-t))log n]. For beta>sqrt(2 log(2d)), Q_n(0)/n >= c=1-sqrt(2 log(2d))/beta>0. Thus Q_n(t_n)/Q_n(0)->0 on the same noise scales; liminf E TV of the two Gibbs measures is at least c.

I independently downloaded https://arxiv.org/pdf/0810.4221 and inspected PDF pages 37–38 and 59. Section 12(2) actually says: "Prove chaos in directed polymers in dimensions >= 3." Its contextual model in Section 8 is exactly iid Gaussian positive-coordinate paths, a free endpoint, and the maximum-weight ground state, with the same OU perturbation and vertex-overlap observable. The supplied phrase "at low temperature" is not in that source question. Section 8 Theorem 8.1 gives the two-dimensional version of the claimant's bound. Consequently the first assertion answers the source question in its own sense, rather than substituting a special disorder law for an explicitly general-law theorem. The second assertion additionally addresses the conventional finite-temperature Gaussian interpretation, in every requested spatial dimension and at all sufficiently large fixed inverse temperatures.

No claim is proved for every disorder distribution, every endpoint constraint, or every definition of chaos. These restrictions are explicit in the submission, not hidden omissions.

## Step-by-step mathematical checks

**Section 2, lines 29–58: OU identity and monotonicity.** I re-derived these independently. Combining Gaussian variances gives the semigroup law. Symmetry of the joint Gaussian pair gives self-adjointness; Jensen and stationarity give L2 contraction. Differentiation yields grad(T_t f)=e^(-t)T_t grad f. With a=e^(-t), b=sqrt(1-a^2), b'=a^2/b, differentiating the kernel and integrating by parts in Y yields L T_t f. Gaussian integration by parts therefore gives C_f'(t)=-e^(-t) sum_j <partial_j f,T_t partial_j f>. The factor e^(-t) and its sign are correct.

For the stated growth hypotheses these calculations and Gaussian boundary terms are legitimate. Lipschitz continuity gives f(X^t)->f(Y) in L2, so integration gives Var(f)=integral_0^infinity e^(-s)A_f(s) ds. Self-adjointness and the semigroup give A_f(s)=sum_j ||T_(s/2) partial_j f||_2^2; contraction then proves monotonicity. In particular Var(f)>=(1-e^(-t))A_f(t). No sign assumption on individual gradient coordinates is needed.

**Section 3, lines 64–96: overlap and zero-temperature passage.** Differentiating log-sum-exp gives the Gibbs occupancy p_j; sum_j p_j=n and sum_j p_j^2<=n. Independence of replicas conditional on the two environments identifies their overlap with sum_j p_j(X)p_j(X^t). Thus the covariance identity concerns precisely the claimed path overlap, not endpoint overlap or overlap without time indices.

At fixed n the number of paths is finite and the uniform log-sum-exp error is at most log K/beta. Distinct paths in each specified graph have distinct incidence vectors: coordinate sum, or explicit time, determines the vertex order. Their energy differences are nondegenerate Gaussian variables. Therefore ties have probability zero. Occupancies converge to the maximizing-path indicators. Bounded convergence applies both to the finite coordinate sum and, with domination n e^(-t), to the covariance integral. This establishes (11) without differentiating a nonsmooth maximum. Both directions of the superconcentration/chaos equivalence at lines 94–96 follow from the displayed bounds; no circular implication from localization is used.

**Section 4, lines 102–114: first published input.** I downloaded https://arxiv.org/pdf/0909.1352 independently. Graham's Theorem 6.1 on PDF page 14 explicitly gives both Var T(0,S_N)=O(N/log N) and its nearest-neighbor space-time analogue for every lattice dimension >=2, with iid standard Gaussian vertex weights. Page 2 explicitly excludes the initial vertex from T. Page 14 defines S_N as the reachable positive-coordinate level set and uses a free endpoint.

Accordingly M_n=X_0+T(0,S_(n-1)) is an exact equality and its summands are independent. Adding variance one and replacing n-1 by n gives (12), with small n absorbed into the constant. The hat graph has d-1 spatial coordinates, so its lattice dimension >=2 indeed includes every positive spatial dimension. There is no unjustified rotation or dimension transfer. The overlap bound, Markov conclusion, path-equality bound and delta-measure TV conclusion all follow as stated.

**Section 5, lines 118–126: second published input.** I downloaded https://arxiv.org/pdf/2103.09199 independently. Section 2.4 on PDF pages 8–9 allows every spatial d>=1 and Lipschitz images of Gaussian disorder. Theorem 2.4(3), page 9, gives Var f(t,x)<=Ct/log t for t>=2, with dependence on d, beta and the environment law. Its explicit representation makes f(t,x) equal in law to beta^(-1)log Z_t. The identity map covers standard Gaussian disorder.

The cited paths have t transitions but only t weighted vertices: their last step is unweighted. Each n-vertex path in the claimant's convention has exactly 2d final extensions. Hence Z_n^paper=(2d)Z_n^claimant under the matching indexing, a deterministic log shift. The variance transfer is valid. The time-layer reversal is a deterministic relabeling of iid disorder, not a claim of quenched path reversibility. Constants are held at fixed beta, and are never sent through a beta->infinity limit. Thus (13) and (2) are justified.

**Section 6, lines 130–165: low-temperature distinction and TV.** Independently differentiating the occupancy gives partial_j p_j=beta(p_j-p_j^2), since incidence indicators square to themselves. Gaussian integration by parts gives EU_beta=beta(n-Q(0)). Each path energy is N(0,n), even though different paths are correlated. The union mgf bound and Jensen yield EM<=log K/lambda+lambda n/2; optimization gives sqrt(2n log K). The K=1 case is treated separately. With K=(2d)^(n-1)<=(2d)^n, this proves the asserted positive baseline.

The probability floor follows by splitting the bounded variable R/n at c/2. Markov proves the cross-environment annealed limit and convergence in probability of the quenched high-overlap probability. Finally the bounded test function f_X(s') gives, pointwise, TV >= (self-overlap minus cross-overlap)/n. Taking expectations proves (16). Its dependence on X is harmless because the inequality holds separately for each environment pair. The finite-temperature conclusion is a positive expected TV lower bound, not TV->1 or convergence in probability to a positive deterministic constant.

**Section 7, lines 169–171:** the one-path counterexample is exact: variance n and overlap n for every perturbation. It illustrates why same-environment localization alone cannot supply the variance gain; it does not contradict either of the audited dimension ranges.

## Independent computational checks

The audit's independent_checks.py enumerates all 36 paths of the d=3, n=3 nearest-neighbor model, retaining 26 separate time-sites (including returns to the same spatial location at another time). It does not run or copy the claimant's numerical programs. At beta=4:

- All 26 occupancy derivatives agree with central differences of beta^(-1)log Z to maximum absolute error 2.2262e-11.
- A predetermined 20,000-sample Gaussian test gives mean residual U-beta(n-sum_j p_j^2) = -0.0098770, standard error 0.0177850, or -0.555 standard errors.
- Mean Q(0)=2.347394 exceeds the analytic baseline 1.580236. Mean cross-overlap at t=0, .05, .2, 1 is respectively 2.347394, 2.187950, 1.909366, 1.431446.
- The pointwise TV test-function bound has nonnegative slack in every tested environment pair (minimum zero at t=0).

I also used the exactly solvable n=2, k=2 ground-state model, M=X_0+max(X_1,X_2). Elementary Gaussian calculations give Var(M)=2-1/pi and Q(t)=3/2+arcsin(e^(-t))/pi, since the maximizing choice is the sign of X_1-X_2. Thus the covariance integral is exactly

  integral_0^1 [3/2+arcsin(r)/pi] dr = 2-1/pi.

Independent numerical quadrature returned 1.681690113816198 versus exact 1.6816901138162093, and the overlap inequality held on 1,000 logarithmically spaced positive t values. These checks support the analytic derivations; finite samples and quadrature are not proofs of the asymptotic result. Results are recorded in independent_checks.json. I did not rerun Lean: the submission explicitly formalizes only three algebraic deductions, and the full audit above does not rely on those formal-check claims.

## Literature search and qualifications

The audit performed fresh bounded arXiv API searches, independently fetched all three decisive PDFs, and attempted an OpenAlex works search. URLs and outcomes are in fetch_log.json and targeted_search_log.json; responses and extracted paper texts remain in this audit folder. OpenAlex returned HTTP 429, so no comprehensive citation-search conclusion is justified.

Graham already supplies the higher-dimensional variance result; the source paper already supplies the same Gaussian variance-to-chaos mechanism in dimension two. Chatterjee's later surface-growth paper supplies the finite-temperature all-dimensional variance result and credits earlier work of Alexander and Zygouras. This is a valid deduction from published results, not evidence of a new discovery. The claimant expressly disclaims novelty.

Fresh arXiv abstracts also identify arXiv:2302.11379, From stability to chaos in last-passage percolation, covering general vertex-weight laws in Z^d with fixed opposite-corner endpoints and independent resampling; arXiv:2010.05837 concerns Brownian LPP and its sharp chaos scale. These are relevant earlier chaos results, but their stated endpoint/perturbation models differ from the exact free-endpoint Gaussian claim audited here. The other inspected abstracts concern geometric LPP, critical two-dimensional polymers, Brownian overlap fluctuations, or continuum temperature chaos. None provides a counterexample to this proof. I do not conclude that no prior exact printed solution exists.

There is one harmless domain convention to make explicit: Section 1 equation (2), line 20, has log n in its denominator and must be read for n>=2 (or n>=3 alongside (1)); it is not a numerical inequality at n=1. Section 5's quoted theorem already says n>=2, and all claimed limits concern n->infinity. This does not leave a mathematical gap in the claimed chaos result.

No failing step or substantive repair was found. The result proves the source's Gaussian ground-state chaos problem and sufficiently-low-temperature fixed-beta Gaussian free-endpoint lattice-polymer chaos in the precise overlap sense stated. General non-Gaussian laws, optimal noise scales, a sharp temperature threshold, and finite-temperature TV->1 remain unproved by this submission.
