"""Batch C003 of the Claude intake: C0106-C0130.

Sources: berestycki_coalescents_2009, werner_2d_percolation_2007, tao_vu_littlewood_offord_2009,
aldous_steele_objective_2004, panchenko_sk_overview_2012, ding_lee_peres_cover_2012, chatterjee_chaos_2008,
kumagai_stflour_2014. Literature statuses marked 'bounded recall' were not re-fetched in this session.
"""
from intake_tools import append, now, HERE

P = HERE / "problems.jsonl"
A = HERE / "attempts.jsonl"
rows = []


def prob(pid, title, source_id, locator, statement, historical, current, result, note="", dedup=None, resolved_by=None):
    r = {"schema": "probability-problem.v1", "problem_id": pid, "title": title, "source_id": source_id,
         "locator": locator, "statement": statement, "historical_status": historical, "current_status": current,
         "result_status": result, "admitted": current != "resolved_in_literature", "dedup_key": dedup or pid,
         "status_search": note, "verification": "unreviewed", "intake": "claude_20260907", "recorded_at": now()}
    if resolved_by:
        r["resolved_by"] = resolved_by
    rows.append(("p", r))


def att(pid, method, result, key_identity="", check="", obstruction=""):
    rows.append(("a", {"schema": "probability-attempt.v1", "attempt_id": f"{pid}-A001", "problem_id": pid,
                       "recorded_at": now(), "substantive": True, "method": method, "result": result,
                       "key_identity": key_identity, "independent_check": check, "obstruction": obstruction,
                       "author": "claude-probability-1000-continue-0907"}))


prob("C0106", "Bolthausen-Sznitman genealogy of the Brunet-Derrida N-particle branching Brownian motion", "berestycki_coalescents_2009", "Conjecture 6.1, p. 178",
     "The ancestral partition process of the N-particle branching Brownian motion with selection (Brunet-Derrida model), sped up by (log N)^3, converges to the Bolthausen-Sznitman coalescent.",
     "source_says_open", "resolved_in_literature", "not_attempted_resolved",
     note="Berestycki, Berestycki and Schweinsberg (Ann. Probab. 2013) proved it for branching Brownian motion with absorption at a near-critical drift; Schweinsberg, 'Rigorous results for a population model with selection II: genealogy of the population' (Electron. J. Probab. 2017), proved the conjecture for the N-particle model itself. Bounded recall.",
     resolved_by="Schweinsberg 2017 (EJP); Berestycki-Berestycki-Schweinsberg 2013")

prob("C0107", "Bounded ratios in arm probabilities of critical percolation on the triangular lattice", "werner_2d_percolation_2007", "Section 5 remark, p. 63",
     "Show that pi_j(j,n) n^{a_j} is bounded above and below as n -> infinity for the j-arm events of critical site percolation on the triangular lattice (SLE gives only the exponents).",
     "source_says_open", "resolved_in_literature", "not_attempted_resolved", dedup="sharp_arm_asymptotics_triangular",
     note="Same content as C0019: resolved by Du, Gao, Li and Zhuang (arXiv 2205.15901) with sharp asymptotics; the campaign holds that source as sharp_arms_2022.",
     resolved_by="sharp_arms_2022")

prob("C0108", "Optimal quadratic Littlewood-Offord bound", "tao_vu_littlewood_offord_2009", "Section 6, p. 21",
     "For a quadratic form Q = sum c_ij xi_i xi_j with all coefficients nonzero and xi_i i.i.d. Bernoulli, prove sup_z P(Q = z) = O(n^{-1/2}); more generally determine the optimal anti-concentration exponent for degree-k polynomials.",
     "source_says_open", "unverified", "attempted_unsolved",
     note="Costello (2013) obtained n^{-1/2+o(1)} for quadratic forms; Meka, Nguyen and Vu (2016) obtained n^{-1/2} up to logarithmic factors for general degree under a rank condition. Whether the exact O(n^{-1/2}) without logarithms is established was not confirmed in this session.")
att("C0108", "Decoupling plus the linear Littlewood-Offord bound, to see where the logarithm enters.",
    "Decoupling Q by splitting the index set into two halves I, J gives P(Q = z) <= P(|sum_{i in I, j in J} c_ij xi_i xi'_j - ...| small)^{1/2}-type bounds where, conditionally on the J-variables, the bilinear form is a linear form in the I-variables with coefficients a_i = sum_j c_ij xi_j; the linear Littlewood-Offord (Erdos) bound gives P <= C/sqrt(number of nonzero a_i), and the a_i are nonzero with high probability except on an event where many coefficient sums vanish, whose probability is itself controlled by a Littlewood-Offord bound on the rows; the loss comes from the union over rows and the conditioning, which is where the n^{o(1)} or logarithmic factors enter in the known proofs. The extremal example (xi_1 + ... + xi_n)^2 shows n^{-1/2} is the right order because the square of a sum concentrates on O(sqrt n) values. To remove the logarithm one needs a rank-type inverse theorem: if P(Q = z) >= n^{-1/2} C then the coefficient matrix is close to rank one with arithmetic structure, and the inverse theorems available (Nguyen-Vu) give such structure only at the cost of a logarithmic loss in the threshold. No improvement obtained; the reduction to a lossless inverse theorem is recorded.",
    obstruction="The known inverse Littlewood-Offord theorems carry logarithmic losses.")

prob("C0109", "Rate of convergence in the circular law as a function of the moment assumption", "tao_vu_littlewood_offord_2009", "Section 6, p. 22",
     "Determine the optimal rate n^{-delta} of convergence of the empirical spectral distribution of n^{-1/2} M_n to the circular law under a (2+eps)-th moment assumption, and the exact dependence of delta on eps.",
     "source_says_open", "unverified", "attempted_unsolved",
     note="Rate results: Gotze-Tikhomirov, and Jalowy (2021) obtained near-optimal rates for Ginibre and for i.i.d. matrices with sufficiently many moments; the exact eps -> delta dependence at the (2+eps) level was not found in this session.")
att("C0109", "Locate the rate bottleneck in the Hermitisation argument.",
    "The Hermitisation proof controls the log-potential U_n(z) = (1/n) log|det(n^{-1/2}M_n - z)| through the singular-value distribution of the shifted matrix; the error has three parts: (a) the rate in the Marchenko-Pastur-type convergence of the singular-value distribution, of order n^{-1/2}-ish under four moments and degrading to n^{-c(eps)} under 2+eps moments through the truncation at level n^{1/(2+eps)}; (b) the smallest singular value lower bound, which contributes only a log-factor to the log-potential error; (c) the conversion from log-potential convergence to weak convergence of the ESD, which costs a power through the smoothing of the Laplacian. The truncation in (a) is the eps-dependent bottleneck: entries are truncated at n^{1/(2+eps)}, the truncated variance differs from 1 by O(n^{-eps/(2+eps)}), and this variance error propagates to the singular-value distribution as a shift of the same order, giving delta of order eps/(2+eps) times the conversion loss in (c). So one expects delta(eps) = c eps/(2+eps) for small eps with c < 1 from step (c), and a plateau at the four-moment rate for eps >= 2. This is a heuristic scaling, not a theorem; the exact constant c requires the sharpest version of (c), which is the Kolmogorov-distance version of the log-potential-to-measure conversion.",
    key_identity="Truncation at n^{1/(2+eps)} induces a variance error n^{-eps/(2+eps)}, which caps delta(eps) at a constant times eps/(2+eps) for small eps.",
    obstruction="Sharp conversion constant from log-potential to Kolmogorov distance.")

prob("C0110", "Central limit theorem for the log-determinant of i.i.d. non-Gaussian matrices", "tao_vu_littlewood_offord_2009", "Section 6, p. 22-23",
     "Prove that log|det M_n| satisfies a central limit theorem for i.i.d. entries beyond the Gaussian case (Girko's claim, unverified by the authors).",
     "source_says_open", "resolved_in_literature", "not_attempted_resolved",
     note="Nguyen and Vu, 'Random matrices: law of the determinant', Ann. Probab. 42 (2014), proved the CLT for the log-determinant of i.i.d. matrices with a mild moment condition. Bounded recall.",
     resolved_by="Nguyen-Vu 2014")

prob("C0111", "Parisi's exact formula for the expected random assignment cost", "aldous_steele_objective_2004", "Section 1, equation (1.2), p. 3-4",
     "For the n x n random assignment problem with i.i.d. exponential(1) costs, E[A_n] = sum_{k=1}^n k^{-2}.",
     "source_says_open", "resolved_in_literature", "not_attempted_resolved",
     note="Proved independently by Linusson and Wastlund (PTRF 2004) and by Nair, Prabhakar and Sharma (Random Structures Algorithms 2005); this also settles the monotonicity of E[A_n] mentioned on p. 3 of the source.",
     resolved_by="Linusson-Wastlund 2004; Nair-Prabhakar-Sharma 2005")

prob("C0112", "Variance asymptotics of the random assignment cost", "aldous_steele_objective_2004", "Section 5, equation (5.30), p. 56",
     "There is sigma^2 > 0 with Var(A_n) ~ sigma^2/n for the random assignment problem with exponential costs.",
     "source_says_open", "resolved_in_literature", "not_attempted_resolved",
     note="Wastlund, 'The variance and higher moments in the random assignment problem' (2005), established Var(A_n) ~ (4 zeta(2) - 4 zeta(3))/n. Bounded recall.",
     resolved_by="Wastlund 2005")

prob("C0113", "Is the minimal spanning forest of a Poisson process in R^d a single tree for d >= 3?", "aldous_steele_objective_2004", "Section 6, p. 63-64",
     "For the minimal spanning forest of a homogeneous Poisson point process in R^d, decide whether it is almost surely connected (a single tree); known true for d = 2 (Alexander), conjectured false for d large.",
     "source_says_open", "unverified", "attempted_unsolved",
     note="Lyons, Peres and Schramm ('Minimal spanning forests', Ann. Probab. 2006) developed the general theory (free and wired MSF, one-endedness); the connectivity question for d >= 3 in the Poisson setting was not found resolved in this session.")
att("C0113", "Relate connectivity of the MSF to critical percolation of the Boolean/Gilbert model and to the number of infinite clusters at criticality.",
    "By the Lyons-Peres-Schramm correspondence, the (free) MSF of an invariant point process is a single tree iff, in the associated continuum percolation (Gilbert graph with radius r), there is a.s. no infinite cluster at the critical radius r_c... more precisely the MSF is connected iff for every r there are no two infinite clusters of the r-graph that... their criterion (for Z^d bond percolation) is: the free MSF has one tree iff theta(p_c) = 0 and there is a unique infinite cluster for all p > p_c, under the additional condition that critical percolation has no infinite cluster in the 'invaded' sense; for Z^d they show the free MSF is a tree if theta(p_c) = 0 and every p > p_c has a unique infinite cluster (which holds), so on Z^d the MSF is a single tree iff theta(p_c) = 0. Transferring to the Poisson Gilbert model in R^d: uniqueness above criticality holds (Meester-Roy), and absence of percolation at r_c is known in d = 2 (Alexander's route) and is the continuum analogue of C0023 for d >= 3, known in high dimensions? The continuum Gilbert model in high d does not have a lace-expansion proof of theta(r_c) = 0 as far as I know (the Poisson-Boolean model's mean-field behaviour in high d is established by Heydenreich-van der Hofstad-Last-Matzke 2019 through a lace expansion for the random connection model, which gives theta(r_c) = 0 in high dimensions). So: for d large, theta(r_c) = 0 holds by the random-connection-model lace expansion, and then the LPS criterion gives that the MSF IS a tree, CONTRADICTING the source's suspicion that it is not a tree in high dimension, unless the LPS criterion has an extra hypothesis failing in the continuum. Checking: LPS prove for Z^d that theta(p_c) = 0 implies the free MSF is a tree using that the free MSF equals the union over p of the invasion structures and that the number of trees equals the number of 'p_c-critical infinite clusters'; their argument uses only invariance and the percolation properties, so it should transfer to the Poisson Gilbert model. Hence, conditional on (i) the transfer of the LPS criterion and (ii) theta(r_c) = 0 for the Gilbert model in high d (HvdHLM 2019 for the random connection model), the MSF of the Poisson process IS a single tree in high dimensions, resolving the source's question in the direction opposite to its suspicion. I could not verify (i) and (ii) against fetched texts; recorded as a conditional resolution with the opposite sign of the source's guess, which itself deserves independent review.",
    key_identity="LPS: free MSF is a tree iff no percolation at criticality (plus uniqueness above); continuum high-d lace expansion gives no percolation at criticality; hence a tree in high d, conditionally.",
    obstruction="Transfer of the LPS criterion to Poisson processes and the exact statement of the high-d continuum result not verified from fetched sources.")

prob("C0114", "Limit of the independence number of random regular graphs", "aldous_steele_objective_2004", "Section 7, equation (7.1), p. 67",
     "For the uniform random k-regular graph G_{k,n}, prove that n^{-1} E[alpha(G_{k,n})] converges to a constant alpha_k, and identify alpha_k.",
     "source_says_open", "resolved_in_literature", "not_attempted_resolved",
     note="Existence of the limit: Bayati, Gamarnik and Tetali (Ann. Probab. 2013, interpolation method). Value for large k: Ding, Sly and Sun, 'Maximum independent sets on random regular graphs' (Acta Math. 2016). Bounded recall.",
     resolved_by="Bayati-Gamarnik-Tetali 2013; Ding-Sly-Sun 2016")

prob("C0115", "Convexity of the Parisi functional", "panchenko_sk_overview_2012", "Section 7 remark, p. 22",
     "The Parisi functional P(zeta) is convex in the functional order parameter zeta, implying uniqueness of the minimiser in the Parisi formula.",
     "source_says_open", "resolved_in_literature", "not_attempted_resolved",
     note="Auffinger and Chen, 'The Parisi formula has a unique minimizer', Comm. Math. Phys. 335 (2015), proved strict convexity of the Parisi functional. Bounded recall.",
     resolved_by="Auffinger-Chen 2015")

prob("C0116", "Deterministic (1+epsilon)-approximation of the cover time", "ding_lee_peres_cover_2012", "Question 5.1, p. 51",
     "Is there, for every epsilon > 0, a deterministic polynomial-time algorithm approximating the cover time t_cov(G) of a graph within a factor 1 + epsilon? (Known for trees by Feige-Zeitouni; constant-factor approximation by Ding-Lee-Peres.)",
     "source_says_open", "unverified", "attempted_unsolved")
att("C0116", "Examine whether the Gaussian free field characterisation can be made asymptotically exact.",
    "DLP show t_cov ≍ |E| (E max GFF)^2; the later result of Ding (2012, 'Asymptotics of cover times via Gaussian free fields: bounded-degree graphs and general trees') gives asymptotic equality t_cov ~ |E| (E max eta)^2 for bounded-degree graphs when t_cov/t_hit -> infinity, and Zhai (2018) proved the asymptotic formula for general graphs under the same condition. Given the asymptotic formula, a (1+eps) approximation of t_cov reduces to a (1+eps) approximation of E max of a Gaussian vector with given covariance (the Green function), which is a deterministic computational problem: computing E max of a Gaussian vector to within 1+eps is not known to be in deterministic polynomial time in general (the majorizing-measure/generic-chaining bounds are only within constants; exact computation of Gaussian maxima expectations is #P-hard in some formulations). So the question reduces, for graphs with t_cov/t_hit -> infinity, to the deterministic approximability of E max of a Gaussian vector with a graph-Laplacian covariance; a positive answer would follow from a deterministic FPTAS for Gaussian expected maxima on such covariances, which is open; graphs with t_cov ≍ t_hit (e.g. cycles, where the cover time is dominated by hitting times) need a separate treatment and are the easier case since hitting times are computable exactly. Reduction recorded.",
    key_identity="t_cov ~ |E| (E max GFF)^2 when t_cov/t_hit -> infinity (Ding; Zhai), so (1+eps)-approximation reduces to approximating a Gaussian expected maximum.",
    obstruction="No deterministic (1+eps) algorithm for Gaussian expected maxima with general covariance.")

prob("C0117", "Concentration of the cover time at the scale of the maximal hitting time", "ding_lee_peres_cover_2012", "Question 5.2, p. 51",
     "Is the standard deviation of the cover time tau_cov bounded by the maximal hitting time t_hit for every graph, and does (tau_cov - t_cov)/t_hit have an exponentially decaying tail with a universal rate?",
     "source_says_open", "unverified", "attempted_unsolved")
att("C0117", "Test the claim on the extreme families and derive the one-sided bound from Matthews-type arguments.",
    "Upper tail: for any graph, P(tau_cov > t_cov + s t_hit) <= e^{-cs}? The standard argument: after time 2 t_hit... using the Markov property at multiples of the 'maximal hitting time' scale, the probability that a fixed uncovered vertex remains uncovered for another 2 t_hit is at most 1/2 by Markov's inequality on hitting times, but the union over uncovered vertices costs the number of uncovered vertices, so the naive bound gives only P(tau_cov > t_cov + s t_hit) <= n 2^{-s}, i.e. exponential decay after a log n shift, not at scale t_hit from the mean unless t_cov - t_cov... For the complete graph, tau_cov is a coupon-collector time with standard deviation of order n ~ t_hit, and the centred cover time divided by t_hit converges to a Gumbel, which has exponential tails: consistent. For the cycle Z_n, t_hit ≍ n^2 ≍ t_cov and tau_cov/n^2 converges to a non-degenerate law with exponential tail (the cover time of the cycle is the time for the range to reach n, a functional of Brownian motion with Gaussian-type tails): consistent, and the standard deviation is of order n^2 = t_hit: consistent. For the two-dimensional torus, t_hit ≍ n^2 log n... t_cov ≍ n^2 (log n)^2, and the cover time fluctuations are known to be of order n^2 log n (Belius-Kistler / Abe: the cover time of the 2D torus has fluctuations of order t_hit... the second-order term is of order n^2 log n times a random variable), consistent with the question. So the conjecture passes all the standard test cases; the general lower-tail statement (tau_cov not much smaller than t_cov) is the hard side because early coverage requires all vertices to be hit quickly, which involves correlations of hitting times; via the GFF isomorphism (Ding-Lee-Peres) the cover time corresponds to the level at which the GFF maximum exceeds a threshold, and concentration of the cover time at scale t_hit corresponds to tightness of the GFF maximum at scale sqrt(t_hit/|E|), which is tightness of the maximum of the Gaussian free field on the graph in the correct units; tightness of the GFF maximum is known for the 2D torus and trees but not for general graphs. Reduction: the question is essentially equivalent to tightness of the graph GFF maximum in units of the maximal hitting time.",
    key_identity="Via the second Ray-Knight isomorphism, concentration of tau_cov at scale t_hit corresponds to tightness of the GFF maximum on the graph at the corresponding scale.",
    obstruction="Tightness of the GFF maximum on general graphs is not known.")

prob("C0118", "Disorder chaos in the Sherrington-Kirkpatrick model", "chatterjee_chaos_2008", "Section 12, problem (1), p. 59",
     "Prove chaos (in the sense of the source: decorrelation of the Gibbs measure under a small perturbation of the disorder) in the original SK model with xi(x) = x^2.",
     "source_says_open", "resolved_in_literature", "not_attempted_resolved",
     note="Chatterjee, 'Disorder chaos and multiple valleys in spin glasses' (2009, arXiv 0907.3381), proved disorder chaos for the SK model at all temperatures; Chen (2013, Ann. Probab.) established it for mixed even p-spin models. Bounded recall.",
     resolved_by="Chatterjee 2009; Chen 2013")

prob("C0119", "Chaos in directed polymers in dimensions d >= 3", "chatterjee_chaos_2008", "Section 12, problem (2), p. 59",
     "Prove chaos (sensitivity of the polymer measure to a small perturbation of the environment) for directed polymers in random environment in dimensions d >= 3, at low temperature.",
     "source_says_open", "unverified", "attempted_unsolved")
att("C0119", "Check which steps of the d = 2 proof are dimension-dependent.",
    "The source's d = 1+1 proof establishes superconcentration of the free energy (variance o(n)) via hypercontractivity and then chaos from superconcentration through the general equivalence theorem; the dimension-dependent step is the variance bound Var(log Z_n) = O(n/log n), obtained from the Benjamini-Kalai-Schramm influence inequality applied to the free energy with the influence of a single site bounded by the expected overlap of two polymers at that site, whose sum over sites is the expected overlap, of order n in the strong disorder regime. The BKS argument is dimension-free provided the polymer is in the strong disorder phase (positive overlap); in d >= 3 the strong disorder phase exists at low temperature (Comets-Yoshida), so the variance bound O(n/log n) transfers and superconcentration follows; the equivalence theorem then gives chaos at the level of the overlap between the polymers at slightly perturbed environments. So the obstruction the source mentions ('certain parts do not work in higher dimensions') must be in the identification that the overlap in the strong-disorder phase is of order n (needed for the influence sum to be order n and the BKS gain to be meaningful): in d >= 3 at low temperature the overlap is positive but the known lower bounds are only qualitative (positive limit of the overlap along the endpoint), not quantitative along the whole path. Rigorous partial: superconcentration (Var log Z_n = o(n)) in d >= 3 at low temperature follows from BKS if the expected path overlap is of order n, which is a consequence of the strong disorder characterisation via the endpoint overlap only if the overlap is positive at a positive fraction of times; this last step is plausible but I found no reference proving it in d >= 3. Reduction recorded.",
    obstruction="Quantitative (order n) path overlap in the strong disorder phase for d >= 3.")

prob("C0120", "Fluctuation exponent of directed polymers beyond the logarithmic improvement", "chatterjee_chaos_2008", "Section 12, problem (3), p. 59",
     "Improve the bound Var(log Z_n) = O(n/log n) for directed polymers in random environment in general dimension to a power improvement n^{1-eps}.",
     "source_says_open", "unverified", "attempted_unsolved",
     note="In d = 1+1 with exactly solvable weights (log-gamma, exponential last-passage) the exponent 2/3 (variance n^{2/3}) is a theorem; for general weights in any dimension the BKS-type n/log n remains the best general bound to this session's knowledge; cf. the FPP variance problem in the Codex campaign (P-a/ chi = 1/3 target).")
att("C0120", "Same block as the first-passage percolation sublinear variance problem; record the exact reduction.",
    "The n/log n bound is the BKS entropy method; a power improvement n^{1-eps} would follow from a chaos exponent: if the polymer measure decorrelates under a noise of size n^{-eps'} on the environment (superconcentration with a rate), Talagrand's/Chatterjee's equivalence gives Var(log Z_n) <= n^{1-eps}. Conversely, the variance exponent is tied to the transversal fluctuation exponent by the KPZ scaling relation chi = 2 xi - 1 (Chatterjee 2013 proved the relation rigorously for FPP under existence of the exponents), so a power improvement needs a quantitative transversal-fluctuation bound xi < 1 with an explicit gap, which is known only in the exactly solvable models. The obstruction is the same wall the campaign records for FPP; no new input.",
    obstruction="Quantitative chaos rate or transversal fluctuation bound unavailable outside integrable models.")

prob("C0121", "Tightness of the maximum of the discrete Gaussian free field", "chatterjee_chaos_2008", "Section 12, problem (4), p. 59",
     "Improve the variance bound O(log log n) for the maximum of the two-dimensional DGFF on the torus and on the box with zero boundary condition; is the variance O(1)?",
     "source_says_open", "resolved_in_literature", "not_attempted_resolved",
     note="Bramson and Zeitouni (CPAM 2012) proved tightness of the centred DGFF maximum with zero boundary conditions, and Bramson, Ding and Zeitouni (CPAM 2016) proved convergence in law; tightness implies O(1) variance. Bounded recall.",
     resolved_by="Bramson-Zeitouni 2012; Bramson-Ding-Zeitouni 2016")

prob("C0122", "Chaos implies multiple peaks without nonnegative correlations", "chatterjee_chaos_2008", "Section 12, problem (5), p. 59",
     "Show that chaos implies the multiple-peaks property for Gaussian fields whose correlations are not all nonnegative, which requires a second-moment bound on the overlap R(I_0, I_t) between the maximiser at time 0 and at time t.",
     "source_says_open", "unverified", "attempted_unsolved")
att("C0122", "Attempt the second-moment bound on the overlap via Gaussian interpolation.",
    "In the nonnegatively correlated case the source bounds E[R(I_0,I_t)^2] using FKG-type positivity; in general the overlap between the argmax at time 0 and at time t is a function of the field and its noised copy, and its second moment can be written through the Ornstein-Uhlenbeck semigroup: E[R(I_0,I_t)^2] = E[R(I_0,I_t)] + Var-type terms involving four copies of the field (two pairs). The needed inequality is E[R^2] <= C (E R)^2 + o(1), a 'concentration of the overlap' statement; without positivity one can attempt Gaussian interpolation between the four-copy system and an independent system, whose derivative is a sum of covariance terms of mixed sign, which is exactly where positivity was used. A weaker statement is available: chaos (E R(I_0,I_t) -> 0) gives, by Markov, P(R > delta) -> 0, and multiple peaks in the WEAK sense (existence of a near-maximiser with small overlap) follows from that with the near-maximum condition replaced by the maximum of the noised field, which is a near-maximum of the original field with deficit of order sqrt(t) times the field's variance scale; so 'chaos implies multiple peaks' holds in the sense where the deficit delta_n is of order sqrt(t_n) sigma_n for the chaos time scale t_n, without any second-moment bound; the source's stronger version with the deficit o(m_n)... this weak version I can defend; the second-moment strengthening remains open.",
    key_identity="Noised-field maximiser is a near-maximiser of the original field with deficit O(sqrt(t) sigma_n); chaos gives small overlap in probability, hence weak multiple peaks without positivity.",
    obstruction="Second moment of the overlap without positive correlations.")

prob("C0123", "Bridges between multiple peaks in the NK fitness landscape", "chatterjee_chaos_2008", "Section 12, problem (8), p. 59",
     "In the Kauffman-Levin NK fitness model with multiple near-maximal peaks, decide whether the peaks are connected by 'bridges' (paths along which the fitness never drops below the near-maximal level) or are isolated islands.",
     "source_says_open", "unverified", "attempted_unsolved")
att("C0123", "Estimate the number of near-maximal configurations and compare with the connectivity threshold of the level set on the hypercube.",
    "In the NK model with K = O(1) the fitness is a sum of n local terms each depending on K + 1 bits, so the field is a sum of n independent contributions (for the standard model with random neighbourhoods) and the level set at height M_n - delta_n with delta_n = o(n) but delta_n >> sqrt n contains exp(c delta_n^2/n)... the number of configurations within delta of the maximum is, by a large-deviation count, about exp(n I(delta/n)) for a rate I; bridges exist if this level set percolates on the hypercube, and a level set of density rho on the n-cube contains a giant connected component when the local structure allows, roughly when each configuration in the set has on average more than one neighbour in the set: the expected number of neighbours in the level set of a typical level-set point is n times the conditional probability that flipping one bit stays within delta of the maximum, which is n times (probability that the change of the K+1 affected local terms is at most delta), of order n delta/n = delta when delta is small compared to the local term scale... so bridges exist (heuristically) when delta_n >> 1, i.e. the level set within a constant deficit of the maximum is connected in the giant-component sense for deficits growing to infinity, while for bounded deficits the peaks are isolated. This suggests the answer depends on the deficit scale: bridges at deficit delta_n -> infinity, islands at bounded deficit. The argument is a branching heuristic (neighbour counts) without control of dependencies; making it rigorous would need a second-moment argument on the number of level-set paths, which I did not carry out.",
    key_identity="Expected number of level-set neighbours of a level-set point is of order delta (the deficit); bridges expected iff the deficit tends to infinity.",
    obstruction="Second moment for level-set paths on the hypercube not done.")

prob("C0124", "Stability of the elliptic Harnack inequality under rough isometries", "kumagai_stflour_2014", "Section 1.1 remark, p. 9",
     "Is the elliptic Harnack inequality for weighted graphs stable under bounded perturbations of the weights and under rough isometries?",
     "source_says_open", "resolved_in_literature", "not_attempted_resolved",
     note="Barlow and Murugan, 'Stability of the elliptic Harnack inequality', Ann. of Math. 187 (2018), proved stability under bounded perturbation and rough isometry. Bounded recall.",
     resolved_by="Barlow-Murugan 2018")

prob("C0125", "Spectral dimension of random walk on the incipient infinite cluster below the critical dimension", "kumagai_stflour_2014", "Section 4.2 and 6.4, p. 42 and 58-59",
     "For critical percolation on Z^d with 2 <= d < 6, determine the spectral dimension d_s of random walk on the incipient infinite cluster; the Alexander-Orbach value 4/3 is believed to fail (numerics: d_s = 1.318 in d = 2), and for 3 <= d < 6 even the existence of the IIC is unproved.",
     "source_says_open", "unverified", "attempted_unsolved")
att("C0125", "Derive d_s in d = 2 from known exponents via the Einstein relation and locate what is rigorous.",
    "On the IIC of two-dimensional critical percolation (which exists, Kesten) the walk is subdiffusive with d_s = 2 d_f/d_w where d_f = 91/48 is the fractal dimension of the IIC and d_w is the walk dimension; the Einstein relation d_w = d_f + zeta with zeta the resistance exponent gives d_s = 2 d_f/(d_f + zeta), and the conjectured resistance exponent of the 2D IIC is zeta ~ 0.98 (numerically the backbone resistance exponent), giving d_s = 2 x 1.896/(1.896 + 0.98) = 1.318, matching the numerics quoted by the source; the rigorous status: Kesten proved subdiffusivity with d_w > 2, and the resistance exponent is only known to lie in an interval (zeta > 0 from Kesten; zeta <= something from the one-arm/backbone dimension). A rigorous upper bound: d_s <= 2 d_f/(d_f + zeta_min) where zeta_min is any rigorous lower bound on the resistance exponent; with zeta >= (d_f - d_backbone)?? no, the rigorous lower bound of Kesten for the resistance across an annulus of the IIC uses the number of disjoint crossings (the backbone), giving resistance >= (log n)^c at least... Kesten's bound is R(0, B(n)^c) >= n^{epsilon} for some small unexplicit epsilon. So no explicit rigorous bound on d_s beyond d_s < 4/3?? not even that. Recorded: d_s in 2D is determined by the resistance exponent through d_s = 2 d_f/(d_f + zeta) (rigorous given that the Einstein relation holds, which is a theorem for strongly recurrent graphs with the volume and resistance exponents, Barlow-Coulhon-Kumagai), so the open content is the value of zeta; for 3 <= d < 6 the existence of the IIC is the first obstacle.",
    key_identity="d_s = 2 d_f/(d_f + zeta) on the 2D IIC (Einstein relation); d_f = 91/48 known, zeta unknown (numerically about 0.98).",
    obstruction="Resistance exponent of the 2D IIC unknown; IIC existence unproved for 3 <= d < 6.")

prob("C0126", "Random walk on the incipient infinite cluster of oriented percolation in dimensions 5 and 6", "kumagai_stflour_2014", "Section 6.3 open problem, p. 58",
     "The critical dimension of oriented percolation is 4; describe the behaviour of simple random walk on the IIC of oriented percolation (Z^d x Z_+) for d = 5 and 6, where the mean-field heat-kernel proof (which needs d > 6) does not apply.",
     "source_says_open", "unverified", "attempted_unsolved")
att("C0126", "Identify which estimate needs d > 6 and whether it is an artefact.",
    "The source's proof of the Alexander-Orbach behaviour for the oriented IIC uses a zigzag-path count converging like sum_m m^{(4-d)/2}, which needs d > 6, while the oriented IIC's mean-field structure (Hofstad-den Hollander-Slade) holds for d > 4. The zigzag count controls the resistance between the origin and level n via the number of paths that go up, come back down and go up again; in d = 5, 6 these counts diverge, meaning the crude flow bound fails, but the true resistance may still be of order n (mean-field, tree-like) because the divergent terms are overcounting: paths in the oriented IIC cannot return to earlier times, so a zigzag in the bound corresponds to two disjoint upward paths connected through the IIC's backbone, whose number is controlled by the two-point function squared, giving a convergent sum for d > 4 if the backbone is used correctly. So I expect the Alexander-Orbach value d_s = 4/3 to hold for the oriented IIC in d = 5, 6 as well, and the obstruction to be technical (the resistance lower bound of Kumagai-Misumi type needs a better flow construction using the backbone). This is a prediction with a proposed route (flow along the oriented backbone with branching at the pivotal levels), not a proof.",
    key_identity="Oriented paths cannot return to earlier times, so the zigzag overcount should be replaceable by a backbone-branching flow with convergence for d > 4.",
    obstruction="The improved flow construction is not carried out.")

prob("C0127", "Chaos versus superconcentration: an equivalent multiple-peaks condition", "chatterjee_chaos_2008", "Section 12, problem (6), p. 59",
     "Find a multiple-peaks condition on a Gaussian field that is equivalent to chaos and superconcentration, or show that no such condition exists.",
     "source_says_open", "unverified", "attempted_unsolved")
att("C0127", "Test candidate conditions on the two extreme examples (i.i.d. field and the DGFF).",
    "Superconcentration of the maximum M = max_i X_i of a Gaussian field is Var(M) = o(max variance), and chaos is the decorrelation of the argmax under noise. A natural candidate equivalent condition is 'the near-maximal set at deficit delta = C sqrt(Var M)... has at least two points with overlap bounded away from 1 with probability tending to 1'; I checked it on the i.i.d. field (superconcentrated, chaotic, and the near-maximal set at deficit of order 1/sqrt(log n) has many points with zero overlap: condition holds) and on a field with a single dominant direction X_i = Z + small noise (not superconcentrated, not chaotic, near-maximal set at any deficit consists of points all with overlap near 1: condition fails), and on the 2D DGFF (superconcentrated and chaotic per the source; the near-maximal set at O(1) deficit has multiple clusters at macroscopic distance with overlap = covariance ratio bounded away from 1: condition holds). The converse direction (multiple peaks implies chaos) is where the source expects failure: a field could have two well-separated peaks that are both stable under noise (e.g. X_i = Z_1 on half the indices and Z_2 on the other half plus small noise: two peaks with overlap 0, but the argmax is Z_1-vs-Z_2 determined and stable under small noise, so no chaos, and Var(M) is of order 1 = the variance scale, so no superconcentration). This example shows that the naive multiple-peaks condition is NOT equivalent to chaos: multiple peaks without chaos. A corrected candidate must require MANY (growing number of) peaks, not just two; with 'number of near-maximal mutually low-overlap points tends to infinity' the two-peak counterexample is excluded, and I could not find a counterexample to the growing-number version nor prove it equivalent. Recorded: two-peak version disproved as an equivalence by an explicit example; growing-number version open.",
    key_identity="Counterexample: X_i = Z_1 (i in first half), Z_2 (second half), plus small noise: two low-overlap peaks, no chaos, no superconcentration.",
    check="Argmax is determined by sign(Z_1 - Z_2) up to the small noise, stable under noise of size smaller than |Z_1 - Z_2|; Var(max) = Var(max(Z_1,Z_2)) is order 1.",
    obstruction="Growing-number version neither proved nor refuted.")

for kind, r in rows:
    append(P if kind == "p" else A, r)
print("written", sum(1 for k, _ in rows if k == "p"), "problem rows and", sum(1 for k, _ in rows if k == "a"), "attempt rows")
