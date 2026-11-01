## Catalog: Claude intake C, probability_1000_intake_claude_20260907, rows C0001-C0160

Shard summary: 160 rows (`C0001`..`C0160`) in the Claude intake C ledger (2026-09-07, directory `probability_1000_intake_claude_20260907`), of which 129 are admitted and 31 are excluded as literature resolutions (`admitted = false`, with a `resolved_by` field). Result-status counts across all 160 rows: attempted_unsolved 125, not_attempted_resolved 31, partial_result 4. Every row's `verification` field reads unreviewed, and per the ledger's own STATUS.json zero rows are author-checked or independently reviewed original solutions; four admitted rows (C0033, C0034, C0036, C0062) are `partial_result` and each carries a numerical or rigorous-partial-bound memo file under `raw/` in the intake directory. Eleven admitted rows had an initial attempt (A001) corrected by a Codex review into a second attempt (A002); each such entry below reports the corrected (A002) attempt as "Our work" and quotes the correction inline, per the ledger's own `correction_note` / `superseded_by` fields, rather than as a separate note. Two rows (C0023, C0094) share `dedup_key` theta_pc_zero_intermediate_dimensions and count once toward the ledger's admitted_distinct_problems figure of 128; both rows are written up below since every row gets an entry. Long `result` fields in attempts.jsonl (median about 200 words, up to 546) are condensed below to their first two or three sentences at a sentence boundary (never truncated mid-sentence) to keep entries near the target length; the full attempt text is in `attempts.jsonl` by `attempt_id` at the path above for anyone who wants the complete derivation.

### C0001. Joint scaling limit of all intermediate level sets of the 2D DGFF

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.1, p. 220.

Statement: Extract a joint distributional limit of the level sets {x in D_N : h_x >= 2 sqrt(g) lambda log N} (or the point measures (2.29)) simultaneously for all lambda in (0,1); couple the limit measures Z^D_lambda and show they all arise via the LQG construction from one underlying continuum GFF.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0001-A001). Method: Reduce to tightness plus a characterisation of subsequential limits through the Gibbs-Markov property, uniformly in lambda; try to replace the moment method of Theorem 2.7 by a single martingale approximation of the exponential of a Gaussian field. Result: Partial reduction only. For any finite set of lambdas the vector of point measures is tight (each coordinate is), and any subsequential limit satisfies the Gibbs-Markov property coordinatewise; the coupling question is therefore whether the joint limit is the image of one CGFF under the map lambda -> e^{alpha lambda h} dx with the Seneta-Heyde normalisation. Obstruction: Second moments of Z^D_lambda blow up as lambda -> 1/sqrt2 in the moment method; the uniform-in-lambda control needed for a joint limit up to lambda -> 1 is not available from moment calculations. Verification level: unreviewed.

### C0002. Fluctuations and large deviations of intermediate level sets of the 2D DGFF

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.2, p. 220.

Statement: Describe the rate of convergence in Corollary 2.9 (size of the intermediate level set), identify the limit law of the fluctuations of the level set around its limit, and study deviations whose probability tends to zero as N -> infinity.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0002-A002, correcting C0002-A001). Correction: Codex review 10:53: the Gaussian tail carries a 1/sqrt(log N) factor. Result: CORRECTION of C0002-A001. With Var h_x = g log N + O(1) and threshold 2 sqrt(g) lambda log N, P(h_x >= threshold) = exp(-2 lambda^2 log N)/(sqrt(2 pi) 2 lambda sqrt(log N)) (1 + o(1)), so the mean size of the intermediate level set is of order N^{2 - 2 lambda^2}/sqrt(log N), not a constant times N^{2(1 - lambda^2)} as A001 wrote; the (log N)^{-1/2} is the leading normalisation, not a correction term. Obstruction: No local limit theorem for pairs at every mesoscopic distance uniformly; the fluctuation law is a functional of the whole scale ladder, not of one scale. (carried over from C0002-A001, unchanged by the correction) Independent check: Correction checked line by line against the source and the holder's message by the Fable agent; the holder's claim was taken as a lead, not as authority. Verification level: unreviewed.

### C0003. Bypassing the Laplace-transform tail condition for the DGFF extremal measure

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Conjecture 16.3, p. 220.

Statement: Prove that any family of non-trivial random measures {Z^D : D in the class of admissible domains} obeying properties (1)-(4) of Theorem 10.15 (Gibbs-Markov, conformal covariance, positivity, non-atomicity) automatically satisfies property (5), the Laplace-transform tail asymptotics, for some c hat > 0.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0003-A001). Method: Try to derive the tail exponent from the Gibbs-Markov fixed-point equation as for smoothing transforms (Durrett-Liggett classification). Result: The Gibbs-Markov property along dyadic square partitions gives a fixed-point equation of smoothing type Z^D =_d sum_i e^{alpha Phi_i} Z^{D_i} with Gaussian binding field Phi and 4 pieces; Durrett-Liggett gives, for such equations, that non-trivial solutions have tails whose exponent is the root of a structure equation, here forcing E[Z^D(A)^s] finite iff s < 1. This yields the correct tail EXPONENT (P(Z^D(A) > t) decays like t^{-1} up to slowly varying factors) but not the precise Laplace asymptotic E e^{-lambda Z} = 1 - c lambda log(1/lambda)(1+o(1)) demanded by property (5); the slowly varying factor is exactly the content of the conjecture and the Durrett-Liggett theory does not fix it. Obstruction: Smoothing-transform theory fixes the power in the tail but not the logarithmic correction; the log factor is what (5) asserts. Verification level: unreviewed.

### C0004. Explicit density of the position of the DGFF maximum

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.4, p. 221.

Statement: Determine explicitly, or characterise by a PDE with a unique solution, the density rho^D of the limit law of the scaled position of the absolute maximum of the DGFF in D_N.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0004-A002, correcting C0004-A001). Correction: Codex review 10:53: ratio-of-expectations equality does not need a constant total mass. Result: CORRECTION of C0004-A001. The sentence 'the naive guess rho^D proportional to r_D(x)^2 fails unless Z^D(D) is a.s. constant' is too strong: if Z^D = xi mu with xi a random scalar and mu deterministic, then Z^D(dx)/Z^D(D) = mu(dx)/mu(D) is deterministic and E[Z^D(dx)/Z^D(D)] = E Z^D(dx)/E Z^D(D) although Z^D(D) is random. Obstruction: rho^D is a ratio expectation; without the law of the total mass Z^D(D) no closed form or PDE is available. (carried over from C0004-A001, unchanged by the correction) Independent check: Correction checked line by line against the source and the holder's message by the Fable agent; the holder's claim was taken as a lead, not as authority. Verification level: unreviewed.

### C0005. Size of deep extremal level sets of the 2D DGFF converges to the extremal measure

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Conjecture 16.5, p. 221.

Statement: There is c in (0,infinity) such that for each open A in D with Leb(dA)=0, (1/t) e^{-alpha t} #{x in Gamma^D_N(t) : x/N in A} converges in law, as N -> infinity then t -> infinity, to c Z^D(A), jointly for finitely many disjoint open sets.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0005-A001). Method: Use the cluster-process structure (Theorem 9.2) to write the level-set count as a sum over local maxima of cluster sizes, then a law of large numbers over clusters. Result: Gamma_N(A,t) = sum over extremal local maxima in A below depth t of the cluster size at depth t - (gap). Given Z^D, the maxima form a Poisson process with intensity Z^D(dx) e^{-alpha h} dh and the clusters are i.i.d.; the expected total is Z^D(A) integral_0^t e^{alpha s} E[cluster size at depth s] ds. Obstruction: Uniform-in-N control of the deep-cluster size at depth t (order t e^{alpha t} by Seneta-Heyde) is not available from the concentric decomposition beyond bounded depth. Verification level: unreviewed.

### C0006. Existence of the limit of e^{-alpha h} E nu(f_h) for the DGFF cluster law

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Conjecture 16.6, p. 222.

Statement: For the cluster law nu and the functionals f_h counting points at depth h in the cluster, the limit lim_{h -> infinity} e^{-alpha h} E_nu(f_h) exists in (0,infinity).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0006-A001). Method: Renewal-type argument on the cluster process viewed from the local maximum: depth-h count as a branching-like functional of the concentric decomposition. Result: Writing the cluster as the field pinned at a local maximum, e^{-alpha h} E nu(f_h) is the expected number of points at depth h weighted by e^{-alpha h}; the concentric decomposition expresses the cluster as a random walk with a Bessel-like entropic repulsion plus independent fine fields, so f_h is a sum over scales k <= log(h) of contributions, each of order e^{alpha h} times the probability that the walk is at height h at scale k. Obstruction: Scale inhomogeneity of the concentric-decomposition walk defeats the standard renewal theorem. Verification level: unreviewed.

### C0007. Profile of near-extremal level sets of the 2D DGFF

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Conjecture 16.7, p. 222.

Statement: The measure eta^D_N = (1/log N) sum_x e^{alpha(h_x - m_N)} delta_{x/N} x delta_{(m_N - h_x)/sqrt(log N)} converges in law to c Z^D(dx) x 1_{[0,infty)}(h) h e^{-h^2/2g} dh.

Status: historical status source_says_open; current-literature status resolved_in_literature. Resolved by: Biskup, Gufler and Louidor, arXiv 2010.13939v3, Theorem 2.3 (journal version 2024): the near-extremal profile of Conjecture 16.7 is proved. Identified by the Codex holder on 2026-09-07 11:15 his clock; source PDF read and archived on its side.

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0008. Universality of level sets and extremal process for log-correlated Gaussian fields in d=2

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.8, p. 222.

Statement: For Gaussian fields on D_N whose covariance scales to the continuum Green function and has a shift-invariant local limit, prove the analogues of Theorem 2.7 (intermediate level sets) and Theorem 9.3 (full extremal process).

Status: historical status source_says_open; current-literature status unverified. Status search found: Documented bounded search 2026-09-07: Ding-Roy-Zeitouni (Ann. Probab.

Our work (attempt C0008-A001). Method: Check which steps of the DGFF proof use only the covariance asymptotics and which use the Gibbs-Markov property of the DGFF specifically. Result: The intermediate-level-set moment calculations (Theorem 2.7) use only the two-point Gaussian densities, which are determined by the covariance asymptotics, plus a coarse Gibbs-Markov decoupling at one scale used to identify the limit as unique; for a general field the decoupling can be replaced by the comparison of the field with the DGFF plus an independent bounded-variance field via Kahane-type interpolation, provided the covariance difference is bounded uniformly. Obstruction: Without uniform boundedness of C_N - G_N the interpolation fails; with it, the level-set statement follows but the cluster law remains model-dependent. Verification level: unreviewed.

### C0009. Intermediate level sets for gradient fields with uniformly strictly convex potentials

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.9, p. 223.

Statement: Prove the scaling limit of intermediate level sets for gradient models (16.14) with uniformly strictly convex potentials V.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0009-A001). Method: Transfer the DGFF moment method through the Helffer-Sjostrand representation and the Brascamp-Lieb inequality. Result: Brascamp-Lieb gives Gaussian domination of the one-point marginals, so the first moment of the level-set size is at most the DGFF value up to constants; the matching lower bound and the two-point estimates need the exponential moments E exp(sum_i t_i h_{x_i}) to have the Gaussian log-correlated form up to bounded errors, which is the content of the Naddaf-Spencer / Giacomin-Olla-Spohn scaling limit at the level of the covariance but not at the level of exponential moments at height 2 sqrt g lambda log N (a large deviation regime for the field). Obstruction: Exponential moments of the gradient field at the level-set height are a moderate-deviation quantity outside the range of the Helffer-Sjostrand CLT. Verification level: unreviewed.

### C0010. DGFF over an ergodic uniformly elliptic random conductance model: level sets and extremal process

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.10, p. 224.

Statement: For uniformly elliptic conductances with a shift-invariant ergodic law, prove for almost every realisation the analogues of Theorems 2.7 and 9.3 for the associated DGFF.

Status: historical status source_says_open; current-literature status unverified. Status search found: Bounded search 2026-09-07 recalls a 2021-2022 result of Schweiger and Zeitouni on the maximum of the DGFF in random environment (random conductances) in d=2; whether the full extremal process and the intermediate level sets were also treated was not confirmed.

Our work (attempt C0010-A001). Method: Homogenisation of the Green function at all scales plus the DGFF argument. Result: The quenched Green function of the random conductance model in d=2 is g_eff log|x-y| + O(1) up to the scale where homogenisation holds; the concentric decomposition needs the O(1) error to be controlled uniformly over all dyadic scales near a point, which is a quenched local limit theorem at every scale. This is available for uniformly elliptic ergodic conductances by Andres-Deuschel-Slowik type estimates for the heat kernel, so the intermediate level sets (which only need two-point covariances) follow the DGFF proof with g replaced by g_eff. Obstruction: The analogue of the cluster law is environment-dependent; the statement of Theorem 9.3 must be modified before it can be proved. Verification level: unreviewed.

### C0011. Scaling limit of local-time level sets of planar random walk in the full range of eta

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.11, p. 224.

Statement: Show that a suitably normalised level set (16.19) of the local time of simple random walk on D_N (run to a multiple theta of the cover time), or the associated point measure, admits a scaling limit for all 0 < eta < 1 + (1/2) sqrt theta.

Status: historical status source_says_open; current-literature status unverified. Status search found: The acquired revision of the notes says an update resolves a related range (Abe's work on trees; a recent posting on the lattice). The exact range covered was not verified in a bounded search; the problem is kept with that caveat.

Our work (attempt C0011-A001). Method: Second Ray-Knight isomorphism to transfer the DGFF level-set result to local times. Result: By the second Ray-Knight theorem the local time at level theta of the walk is, in law, (1/2)(h + sqrt(2 theta ...))^2 for an independent DGFF-type field h; level sets of the local time at height eta times the cover-time scale correspond to DGFF level sets at height lambda log N with lambda determined by eta and theta, giving eta < 1 + (1/2) sqrt(theta)... in the notation of the notes exactly the range where the corresponding DGFF lambda is below 1. Obstruction: Sign ambiguity in the isomorphism couples two DGFF level sets; no joint limit is available. Verification level: unreviewed.

### C0012. Subdiffusive upper bound for the Liouville random walk on the DGFF

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.12, p. 225.

Statement: For the random walk X on Z^2 driven by the DGFF with parameter beta > 0 (13.9), show that for each delta > 0, P^0_h(|X_T| <= T^{1/psi(beta)} e^{(log T)^{1/2+delta}}) -> 1 in P-probability.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0012-A001). Method: Exit-time lower bound from effective resistance: compare the exit time from B(N) with the commute time. Result: The commute-time identity gives E^0_h tau_{B(N)^c} >= c R_eff(0, B(N)^c) pi(B(N)) where pi is the reversible measure (volume of the Liouville measure of the box). The volume is N^{psi... } of order N^{2 + 2 beta^2 g ...} in the notation of the notes, i.e. Obstruction: Exit-time concentration fails at fixed environment because of trapping at deep wells; the polylog correction is a trapping statement, not a resistance statement. Verification level: unreviewed.

### C0013. Existence of the Liouville Langevin motion as a joint scaling limit

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.13, p. 226.

Statement: Under a suitable time change, prove that the pair (h_eps, X_eps) of the regularised field and the associated Langevin-type walk converges jointly in law as eps -> 0 to (h, X) with h a CGFF and X a process with continuous non-constant paths correlated with h.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0013-A001). Method: Tightness via a Dirichlet-form argument and identification through conformal covariance. Result: The discrete process is a reversible diffusion with respect to the Liouville measure of the regularised field, with Dirichlet form (1/2) integral |grad f|^2 dx (the Dirichlet form is field-independent, only the speed measure depends on the field). Mosco convergence of the speed measures (the Liouville measures converge) gives convergence of the time-changed Brownian motion, i.e. the marginal law of X converges to Liouville Brownian motion; the joint law with the field converges by the same construction because the time change is a measurable functional of the field. Obstruction: The Langevin drift beta grad h_eps diverges; the problem needs a renormalisation scheme which the notes do not specify. Verification level: unreviewed.

### C0014. Limit of the normalised log-effective resistance of the DGFF electric network

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.14, p. 227.

Statement: For admissible approximations D_N of a domain D and the network with resistances (13.13) built from the DGFF, characterise the limit distribution of x -> (log N)^{-1/2} log R_eff(floor(xN), D_N^c) as N -> infinity.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0014-A001). Method: Bound log R_eff by the field along an annulus decomposition; compare upper and lower bounds. Result: Rayleigh monotonicity gives R_eff(x, D_N^c) <= sum over dyadic annuli around x of the resistance across the annulus, each bounded by the maximum of e^{beta h} over the annulus times a constant, so log R_eff <= beta max_{annuli} (h max over annulus) summed... more precisely log R_eff <= log sum_k e^{beta M_k} where M_k is the field maximum over annulus k; by the concentric decomposition M_k is the walk value at scale k plus a bounded extremal term, so log R_eff is bounded above by beta times the maximum over k of the concentric walk, which after dividing by (log N)^{1/2} converges to beta sqrt g times the maximum of a Brownian motion on [0,1]. Obstruction: Upper (flow) and lower (cutset) bounds converge to different functionals of the concentric walk. Verification level: unreviewed.

### C0015. Scaling limit of the current-minimising path in the DGFF network

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.15, p. 228.

Statement: Prove that the joint law of the DGFF and the random path P minimising the effective-resistance energy between two boundary points admits a non-degenerate scaling limit.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0015-A001). Method: Tightness of the path via the exponential metric (Liouville first passage percolation) comparison. Result: The energy-minimising path between two points concentrates on paths of small total resistance, i.e. on near-geodesics of the discrete metric with edge weights e^{beta h}; this is the Liouville first passage percolation metric, whose scaling limit (the LQG metric) exists for beta below the critical value by Ding-Dubedat-Dunlap-Falconet and Gwynne-Miller. Tightness of P is then plausible via geodesic tightness in that metric, but P is not a geodesic: the current spreads over many paths and the minimiser of the quadratic energy is a flow, not a path; the notes' 'path' is the sampled path of the current. Obstruction: No continuum electrical current on LQG has been constructed; the path is a functional of it. Verification level: unreviewed.

### C0016. Hausdorff dimension of the continuum DGFF current path and of the energy support

Source: Biskup: Extrema of the two-dimensional discrete Gaussian free field, PIMS-CRM lecture notes (`biskup_dgff_extrema_2020`), Problem 16.16, p. 228.

Statement: What is the Hausdorff dimension of the continuum random path of Problem 16.15, and, for the electric current between opposite sides of a square, what is the dimension of the support of the energy?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0016-A001). Method: Compare with known dimensions of LQG geodesics and of the LQG metric ball boundary. Result: If the continuum path were an LQG geodesic its Euclidean Hausdorff dimension would be that of LQG geodesics, which is strictly greater than 1 and below 2 and only known within bounds for general gamma; the energy support, if concentrated on a fractal set, would have dimension between the geodesic dimension and 2. I could not do better than these bounds because the object (C0015) is not constructed. Obstruction: Continuum object not defined; only the discrete energy scaling is accessible. Verification level: unreviewed.

### C0017. Conformal invariance of critical bond percolation on the square lattice

Source: Garban and Steif: Noise sensitivity of Boolean functions and percolation, lecture notes with open problems (`garban_steif_noise_2012`), Chapter II Section 4, p. 26.

Statement: Prove that critical bond percolation on Z^2 at p = 1/2 is conformally invariant in the scaling limit (Cardy's formula and convergence of interfaces to SLE(6)), as is known on the triangular lattice by Smirnov.

Status: historical status source_says_open; current-literature status no_resolution_found_in_documented_search. Status search found: Bounded search 2026-09-07: no proof of conformal invariance on Z^2 found; the problem is listed as open in Duminil-Copin's ICM 2018 survey as well (dedup with that source).

Our work (attempt C0017-A001). Method: Look for a discrete holomorphic observable on the square lattice analogous to Smirnov's on the triangular lattice. Result: Smirnov's argument needs the three-arm colour-switching symmetry, which on the triangular lattice comes from site self-duality; on Z^2 bond percolation the dual is the shifted square lattice and the exploration interface lives on the medial lattice, where the parafermionic observable F(z) = E[e^{i sigma W(z)} 1_{z on interface}] with spin sigma = ... satisfies only half of the discrete Cauchy-Riemann relations (the contour-integral relations, as for FK models with q not 2). Obstruction: Only the weak (contour) half of discrete holomorphicity holds for the q=1 parafermion on the square lattice. Verification level: unreviewed.

### C0018. Existence and value of the four-arm critical exponent for critical bond percolation on Z^2

Source: Garban and Steif: Noise sensitivity of Boolean functions and percolation, lecture notes with open problems (`garban_steif_noise_2012`), Chapter VI Section 2, p. 63.

Statement: Prove that alpha_4(R) = R^{-xi_4 + o(1)} for some xi_4 for critical percolation on Z^2, and show xi_4 = 5/4 as on the triangular lattice.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0018-A002). Method: Self-audit of C0018-A001 while preparing the math-brain bundle. Result: CORRECTION. C0018-A001 claimed that quasi-multiplicativity alone gives approximate subadditivity of f(R) = -log alpha_4(1,R) in log R and hence existence of the four-arm exponent on Z^2. Obstruction: Scale invariance up to constants is unavailable on Z^2. Independent check: The triangular-lattice value 5/4 uses conformal invariance in the one-scale factors; no Z^2 substitute. A prior attempt (C0018-A001) was corrected: The existence-of-exponent claim assumed alpha_4(rho,R) depends on R/rho only up to constants (scale invariance up to constants), which is unproved on Z^2; see C0018-A002. Verification level: unreviewed.

### C0019. Absence of logarithmic corrections in arm exponents on the triangular lattice

Source: Garban and Steif: Noise sensitivity of Boolean functions and percolation, lecture notes with open problems (`garban_steif_noise_2012`), Remark II.1, p. 28.

Statement: Show alpha_1(R) asymp R^{-5/48} (ratio bounded above and below), and similarly for the other arm events on the triangular lattice, i.e. no logarithmic corrections.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Du, Gao, Li, Zhuang (arXiv 2205.15901, 2022), 'Sharp asymptotics for arm probabilities in critical planar percolation', establish the sharp asymptotics of arm probabilities on the triangular lattice, removing the o(1) in the exponents; this source is already acquired in the campaign as sharp_arms_2022. Resolved by: sharp_arms_2022 (j>=2 only; planar one-arm remainder open, carried as P0130) Correction to this row's status: CORRECTION 2026-09-07 (codex-probability-01a07a40, msg-2a4dacb4ba): Du-Gao-Li-Zhuang arXiv 2205.15901 Thm 1.2 is j>=2 and footnote 3 excepts the planar ONE-arm exponent, so the one-arm case is NOT resolved. Kept excluded here only because the open remainder is the Codex ledger's P0130 (dedup: this row merges into P0130), not because it is resolved.

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0020. Optimal exponent for the computational complexity of randomised algorithms for percolation crossings

Source: Garban and Steif: Noise sensitivity of Boolean functions and percolation, lecture notes with open problems (`garban_steif_noise_2012`), Chapter VIII Section 4, p. 92.

Statement: Find the smallest sigma such that there are randomised algorithms A_n deciding the left-right crossing f_n of an n x n box in critical percolation with computational complexity C(A_n) <= n^sigma; known sigma in [6/4, 7/4].

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0020-A001). Method: Lower-bound the complexity by the OSSS inequality with the sharp four-arm exponent and compare with the exploration-path algorithm. Result: The exploration algorithm reveals the pivotal-rich interface, of expected size n^{7/4+o(1)}, giving sigma <= 7/4. The lower bound 6/4 in the notes comes from Theorem VIII.6 (revealment times complexity). Obstruction: Both OSSS-type bounds saturate at 6/4; closing the gap to 7/4 needs a genuinely new lower-bound technique. Verification level: unreviewed.

### C0021. Revealment exponent of the iterated 3-majority function

Source: Garban and Steif: Noise sensitivity of Boolean functions and percolation, lecture notes with open problems (`garban_steif_noise_2012`), Exercise VIII.5 note, p. 97.

Statement: The revealments of the iterated 3-majority function on 3^k bits decay like n^{-sigma}; determine sigma.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0021-A001). Method: Compute the revealment of the natural recursive algorithm exactly and bound the optimal one from below via Theorem VIII.7. Result: The recursive algorithm (evaluate two random children, evaluate the third only if they disagree) reveals a given leaf with probability (2/3 + (1/3) p_disagree)^k where at each level the probability the third child is needed is 1/2 (two independent uniform bits disagree with probability 1/2), so delta = (5/6)^k = n^{-log(6/5)/log 3} = n^{-0.166}. Lower bound: Theorem VIII.7 gives delta >= Var(f)/(n max_i I_i) with I_i = (3/2)^k / 3^k ... the influence of a leaf in iterated 3-majority is (3/2)^k/3^k... wait each level multiplies influence by 3/2 relative to 1/3 branching: I_i = (1/2)^k ... corrected: I_i = (3/4)^k? Obstruction: No matching algorithm or lower bound; the true sigma lies in [0.166, 0.369]. Independent check: k=1: greedy reveals a given leaf with probability 2/3 + 1/3 * 1/2 = 5/6, matches; influence of a leaf in majority of 3 = 1/2, matches. Verification level: unreviewed.

### C0022. Singularity of the scaling limits of the spectral sample and of the pivotal set

Source: Garban and Steif: Noise sensitivity of Boolean functions and percolation, lecture notes with open problems (`garban_steif_noise_2012`), Chapter X Section 2, p. 111.

Statement: Prove that the scaling limits of (1/n) S_{f_n} (spectral sample) and (1/n) P_{f_n} (pivotal set) of the crossing event are singular random compact sets, and in particular that the spectral sample has a scaling limit.

Status: historical status source_says_open; current-literature status unverified. Status search found: Garban-Pete-Schramm (2013) constructed the scaling limit of the pivotal MEASURE; the notes' statement is about the sets and about the spectral sample. Not verified further. Correction to this row's status: CORRECTION 2026-09-07 (Codex review): existence of the scaling limits of the spectral and pivotal measures is known (Garban-Steif book, Chapter XIII.3); the open content is only their mutual singularity.

Our work (attempt C0022-A001). Method: Compare the two-point functions of the two random sets. Result: The pivotal set and the spectral sample have the same one-point intensity (alpha_4 at each point) and the same two-point function up to constants (both are asymp alpha_4(|x-y|) alpha_4(|x-y|, n) ...), so any singularity must come from higher-order structure. The known difference is in the third moment: E|S|^3 and E|P|^3 differ, and more precisely the conditional law of S given a point x in S has a strictly different clustering structure (spectral sample is 'more clustered'). Obstruction: One needs an almost-sure local statistic separating the two sets; only distributional differences are known. Verification level: unreviewed.

### C0023. No percolation at criticality on Z^d for 3 <= d <= 10

Source: Garban and Steif: Noise sensitivity of Boolean functions and percolation, lecture notes with open problems (`garban_steif_noise_2012`), Chapter XI Section 1, p. 136; also duminil_copin_icm_2018 Conjecture 1 p. 3 and duminil_copin_ising_potts_2017 Conjecture 1 p. 37.

Statement: Prove theta(p_c) = 0 for Bernoulli percolation on Z^d for every d >= 3; open for 3 <= d <= 10 (known for d >= 11 by Fitzner and van der Hofstad, and for d = 2).

Status: historical status source_says_open; current-literature status no_resolution_found_in_documented_search. Status search found: Bounded search 2026-09-07: no resolution for 3 <= d <= 10 found; the d >= 11 result (Fitzner-van der Hofstad 2017) and the half-space result of Barsky-Grimmett-Newman remain the state of the art. This row shares dedup_key `theta_pc_zero_intermediate_dimensions` with C0094; counted once toward admitted_distinct_problems.

Our work (attempt C0023-A001). Method: Try to bootstrap the half-space result of Barsky-Grimmett-Newman to the full space via a finite-energy and uniqueness argument. Result: In the half-space N x Z^{d-1} at p_c(Z^d) there is no infinite cluster (BGN). If the full space had an infinite cluster C at p_c, it would be unique (Burton-Keane), and by ergodicity and finite energy it would intersect every half-space; the half-space restriction of C is not the half-space percolation cluster (edges crossing the boundary are removed), and the half-space result only says the half-space's OWN clusters are finite, so C restricted to a half-space is a union of infinitely many finite half-space clusters connected through the other side. Obstruction: Infinite half-space susceptibility at p_c and a gluing lemma through the hyperplane are both unproved for 3 <= d <= 10. Verification level: unreviewed.

### C0024. Exceptional times for dynamical critical percolation on Z^2

Source: Garban and Steif: Noise sensitivity of Boolean functions and percolation, lecture notes with open problems (`garban_steif_noise_2012`), Chapter XI Section 3, p. 137.

Statement: Do exceptional times at which the origin percolates exist for dynamical critical bond percolation on Z^2?

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Garban, Pete and Schramm, 'The Fourier spectrum of critical percolation' (Acta Math. 2010) proved the existence of exceptional times on Z^2; the notes themselves cite this as [GPS10]. Resolved by: GPS10, cited in the acquired source

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0025. Hausdorff dimension of the set of exceptional times equals 31/36 on the triangular lattice

Source: Garban and Steif: Noise sensitivity of Boolean functions and percolation, lecture notes with open problems (`garban_steif_noise_2012`), Chapter XI Section 5, p. 142.

Statement: Prove that the set of exceptional times of dynamical critical site percolation on the triangular lattice has Hausdorff dimension 31/36 almost surely.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Proved in Garban-Pete-Schramm (Acta Math. 2010), cited as [GPS10] in the acquired notes; the notes present the earlier bounds [1/6, 31/36] of Schramm-Steif historically. Resolved by: GPS10, cited in the acquired source

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0026. Universality of local spectral statistics for non-Hermitian i.i.d. matrices

Source: Bordenave and Chafai: Around the circular law, survey with open problems (`bordenave_chafai_circular_2012`), Section 7, p. 51.

Statement: Show that the local eigenvalue statistics of n^{-1/2} X, X with i.i.d. entries of unit variance, converge to those of the complex (or real) Ginibre ensemble.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Tao-Vu (Ann. Probab. Resolved by: Tao-Vu 2015; Cipolloni-Erdos-Schroder 2019-2021

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0027. Universality of the elliptic law

Source: Bordenave and Chafai: Around the circular law, survey with open problems (`bordenave_chafai_circular_2012`), Section 7, p. 52.

Statement: For i.i.d. pairs (X_ij, X_ji) with unit variances and correlation t, prove that the empirical spectral distribution of n^{-1/2} X converges to Girko's elliptic law for general entry distributions.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Nguyen and O'Rourke, 'The elliptic law' (IMRN 2015), proved the elliptic law under the stated second-moment assumptions. Resolved by: Nguyen-O'Rourke 2015

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0028. Limiting spectral distribution of random oriented r-regular graphs

Source: Bordenave and Chafai: Around the circular law, survey with open problems (`bordenave_chafai_circular_2012`), Section 7, p. 52.

Statement: Prove that the empirical spectral distribution of the adjacency matrix of a uniform random oriented r-regular graph converges a.s. to the oriented Kesten-McKay law (1/pi) r^2(r-1)/(r^2-|z|^2)^2 on |z| < sqrt r.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Basak, Cook and Zeitouni, 'Circular law for the sum of random permutation matrices' (EJP 2018), proved the limit for the sum of r i.i.d. uniform permutation matrices, which is the uniform oriented r-regular multigraph; Basak-Dembo (2013) treated sums of Haar unitaries. Resolved by: Basak-Cook-Zeitouni 2018 Correction to this row's status: SCOPE NOTE 2026-09-07 (Codex review): any resolution claim for the fixed-r uniform regular graph case must match the exact model and degree growth; a sum-of-permutations citation alone does not settle it.

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0029. Spielman-Teng conjecture on the least singular value of Bernoulli matrices

Source: Bordenave and Chafai: Around the circular law, survey with open problems (`bordenave_chafai_circular_2012`), Section 7, p. 53.

Statement: For X with i.i.d. symmetric Bernoulli entries, show P(sqrt n s_n(X) <= t) <= t + c^n for some 0 < c < 1, all large n and all small t >= 0.

Status: historical status source_says_open; current-literature status unverified. Status search found: Bounded recall 2026-09-07: the t = 0 case, P(s_n = 0) = (1/2 + o(1))^n, was proved by Tikhomirov (Ann. Math. Correction to this row's status: SCOPE NOTE 2026-09-07 (Codex review): Sah-Sahasrabudhe-Sawhney arXiv 2405.20308 (GAFA 2025) prove the coefficient 1+o(1), not the exact constant; the exact-coefficient target stays open.

Our work (attempt C0029-A001). Method: Test whether the constant 1 in front of t is forced by the Gaussian comparison and whether the Bernoulli case can beat it. Result: For the Gaussian matrix Edelman's exact law gives P(sqrt n s_n <= t) = 1 - e^{-t^2/2 - t} ~ t as t -> 0, so the constant 1 is exactly the Gaussian density at zero of sqrt n s_n; the conjecture says Bernoulli matrices are no worse than Gaussian up to the exponentially small singular mass. A sufficient condition would be a local limit theorem for sqrt n s_n at zero uniform in n, which is a universality statement at the hard edge (the smallest singular value) and is known (Tao-Vu 2010 hard-edge universality) only in the form P(sqrt n s_n <= t) = (1 - e^{-t^2/2-t}) + O(n^{-c}) for t in a fixed range, which gives the conjecture for t >= n^{-c'} but not for t between c^n and n^{-c'}. Obstruction: Hard-edge universality covers t >= n^{-c}; the conjecture needs the constant 1 down to exponentially small t. Verification level: unreviewed.

### C0030. Circular law and real-root count for Gaussian Weyl polynomials

Source: Bordenave and Chafai: Around the circular law, survey with open problems (`bordenave_chafai_circular_2012`), Section 7, p. 54.

Statement: For Weyl polynomials sum_k b_k z^k / sqrt(k!) with i.i.d. standard Gaussian b_k, prove that the empirical distribution of roots tends to the uniform law on a disc and that in the real Gaussian case there are about (2/pi) sqrt n real roots.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Kabluchko and Zaporozhets ('Asymptotic distribution of complex zeros of random analytic functions', Ann. Probab. Resolved by: Kabluchko-Zaporozhets 2014; Edelman-Kostlan; Tao-Vu 2015

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0031. Almost-sure convergence in the heavy-tailed circular law

Source: Bordenave and Chafai: Around the circular law, survey with open problems (`bordenave_chafai_circular_2012`), Section 6.6 remark, p. 39.

Statement: Upgrade the convergence in probability of the empirical spectral distribution of n^{-1/alpha} X (i.i.d. entries in the domain of attraction of an alpha-stable law, alpha in (0,2)) to almost-sure weak convergence to mu_alpha.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0031-A001). Method: Borel-Cantelli over the Hermitisation: identify which estimate is only in probability. Result: The proof of Theorem 6.2 has three inputs: (i) convergence of the singular-value distributions of n^{-1/alpha}X - z for each z, which is almost sure by the objective method (the local weak convergence to the PWIT holds a.s.); (ii) uniform integrability of log at infinity, a.s. from moment bounds; (iii) uniform integrability of log near zero, i.e. a lower bound on the small singular values, which is where only an in-probability bound s_n(n^{-1/alpha}X - z) >= n^{-c} with probability 1 - o(1) is available. Obstruction: Need P(s_n(n^{-1/alpha}X - z) <= n^{-c}) summable in n for heavy-tailed entries. Verification level: unreviewed.

### C0032. Explicit form of the heavy-tailed circular law density

Source: Bordenave and Chafai: Around the circular law, survey with open problems (`bordenave_chafai_circular_2012`), Section 6.6, p. 39.

Statement: Identify explicitly the isotropic density g_alpha(|z|) of the limiting spectral law mu_alpha of n^{-1/alpha}X for alpha-stable-type entries; only g_alpha(0) and the tail (r^{2(alpha-1)} e^{-alpha r^alpha/2} up to constants) are known.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0032-A001). Method: Attempt to derive g_alpha from the PWIT recursive distributional equation for the resolvent at z, then differentiate in z. Result: The density is g_alpha(r) = (1/2pi) Delta_z of the log-potential U(z) = -integral log|z-w| dmu_alpha(w), and U is expressed through the limit of the singular-value law of the shifted operator on the PWIT, whose Stieltjes transform satisfies a fixed-point equation in a 2x2 matrix-valued function with alpha-stable-type nonlinearity (as in Bordenave-Caputo-Chafai). The z-dependence enters only through the off-diagonal entries; at z = 0 the equation closes on a single positive stable random variable, which is why g_alpha(0) is explicit. Obstruction: The matrix-valued PWIT fixed point does not reduce to a scalar equation away from z = 0. Verification level: unreviewed.

### C0033. Concavity of the entropy of determinantal measures in the kernel

Source: Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (`lyons_determinantal_2014`), Conjecture 2.6, p. 5 and Conjecture 5.3, p. 22.

Statement: For positive contractions Q_1, Q_2 on l^2(E), E finite, Ent(P_{(Q_1+Q_2)/2}) >= (Ent(P_{Q_1}) + Ent(P_{Q_2}))/2; which implies (Conjecture 5.3, by finite restrictions) concavity of the entropy rate H(P_f) of stationary determinantal processes in the symbol f; the converse is not claimed.

Status: historical status source_says_open; current-literature status unverified. Status search found: Not verified against later literature in this session.

Our work (attempt C0033-A002, correcting C0033-A001). Correction: Codex review 11:15: finite-kernel concavity implies stationary entropy concavity; it is not an equivalence. Result: CORRECTION of C0033-A001 and of the problem statement's 'equivalently': Lyons's Conjecture 2.6 (finite positive contractions) implies Conjecture 5.3 (stationary processes on Z, concavity of the entropy rate in the symbol) by taking limits of finite restrictions, but the converse is not claimed and is not known; the two are recorded as implication, not equivalence. The numerical evidence (1440 random pairs, no violation) is for Conjecture 2.6 only. Obstruction: No analytic argument beyond diagonal kernels; the 2x2 case is the natural next target. (carried over from C0033-A001, unchanged by the correction) Independent check: Correction checked line by line against the source and the holder's message by the Fable agent; the holder's claim was taken as a lead, not as authority. Verification level: unreviewed. Proof/memo evidence file: `raw/C_lyons_conj26_entropy_check.json` (under the intake directory).

### C0034. Coupling of determinantal projection measures with union marginal

Source: Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (`lyons_determinantal_2014`), Question 2.8, p. 6.

Statement: Given H = H_1 (+) H_2 orthogonal in l^2(E), is there a coupling of P_{H_1} and P_{H_2} whose union has law P_H?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0034-A002, correcting C0034-A001). Correction: Codex review 11:15: floating-point LP feasibility is not an exact certificate. Result: CORRECTION of C0034-A001's wording. HiGHS reported minimum total violation 0.0 on every instance in double precision; that is numerical evidence, not an exact feasibility certificate. Obstruction: No general construction; the naive conditional splitting fails. (carried over from C0034-A001, unchanged by the correction) Independent check: Correction checked line by line against the source and the holder's message by the Fable agent; the holder's claim was taken as a lead, not as authority. Verification level: unreviewed. Proof/memo evidence file: `raw/C_lyons_q28_lp_check.json (plus C_lyons_q28_lp_check_structured.json)` (under the intake directory).

### C0035. Determinantal processes with trigonometric-polynomial symbol as block factors

Source: Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (`lyons_determinantal_2014`), Question 5.4, p. 22.

Statement: Let f : T -> [0,1] be a trigonometric polynomial of degree m; the stationary determinantal process P_f on Z is m-dependent. Is P_f an (m+1)-block factor of an i.i.d. process? Known for m = 1.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0035-A002, correcting C0035-A001). Correction: Codex review 11:15: the sublattice reduction needs the reduced-degree case, so it settles only degrees that reduce to a proved case. Result: CORRECTION of C0035-A001's last claim. The sublattice lemma (symbol g(k theta) = interleaving of k independent copies of P_g) reduces degree m to degree m/k; it settles the question only when the reduced degree is a proved case, i.e. m/k = 1 (degree-1 symbols are 2-block factors by the known result). Obstruction: General degree-m symbols without a sublattice structure are not covered; no (m+1)-block realisability criterion. (carried over from C0035-A001, unchanged by the correction) Independent check: Correction checked line by line against the source and the holder's message by the Fable agent; the holder's claim was taken as a lead, not as authority. Verification level: unreviewed.

### C0036. Fuglede-Kadison product-measure bounds for equivariant determinantal processes

Source: Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (`lyons_determinantal_2014`), Conjecture 5.7, p. 23.

Statement: For every Gamma-equivariant positive contraction Q on l^2(Gamma), P_Q stochastically dominates the product measure with density FK(Q) = exp tr log|Q| and is dominated by the product measure with density 1 - FK(I-Q), and these bounds are optimal; open even for finite groups.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0036-A002, correcting C0036-A001). Correction: Codex review 10:53: the key identity conflated the Schur complement s with the probability s/(1+s). Result: CORRECTION of C0036-A001's key_identity line only. Correct chain: s_B = det J_{B+e}/det J_B is nonincreasing in B; s_min = 1/(J^{-1})_ee = 1/((Q^{-1})_ee - 1) = HM/(1 - HM); the minimal conditional probability of presence is s_min/(1 + s_min) = 1/(Q^{-1})_ee = HM(Q). Obstruction: Closing the gap between harmonic and geometric mean requires using conditional probabilities given partial information, not the worst-case conditioning. (carried over from C0036-A001, unchanged by the correction) Independent check: Correction checked line by line against the source and the holder's message by the Fable agent; the holder's claim was taken as a lead, not as authority. Verification level: unreviewed. Proof/memo evidence file: `raw/C_lyons_conj57_fk_domination_check.json` (under the intake directory).

### C0037. Tail triviality of determinantal processes with positive-contraction kernels

Source: Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (`lyons_determinantal_2014`), Conjecture 3.2, p. 12.

Statement: If K is a locally trace-class positive contraction, then P_K has trivial tail sigma-field.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Lyons, 'A note on tail triviality for determinantal point processes' (Electron. Commun. Resolved by: Lyons 2018 ECP; Osada-Osada 2018

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0038. Lyons-Peres completeness conjecture for projection determinantal processes

Source: Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (`lyons_determinantal_2014`), Conjecture 4.6, p. 20.

Statement: If K is a locally trace-class orthogonal projection onto H, then for P_K-a.e. configuration X the functions {K(., x) : x in X} span H, i.e. h in H vanishing on X is zero.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Bufetov, Qiu and Shamov, 'Kernels of conditional determinantal measures and the Lyons-Peres completeness conjecture', J. Eur. Resolved by: Bufetov-Qiu-Shamov, JEMS 2021

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0039. d-bar distance bound for commuting versus general equivariant kernels

Source: Lyons: Determinantal probability, basic properties and conjectures, ICM 2014 (`lyons_determinantal_2014`), Section 5.2, p. 23.

Statement: For Gamma-equivariant positive contractions Q, Q' the bound d-bar(P_Q, P_{Q'}) <= 6 3^{2/3} ||Q - Q'||_1^{1/3} holds, and d-bar(P_Q, P_{Q'}) <= ||Q - Q'||_1 when Q and Q' commute. Does the linear bound d-bar <= ||Q - Q'||_1 hold for all pairs?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0039-A001). Method: Test the linear bound on finite cyclic groups with non-commuting equivariant... note that on an abelian group all equivariant operators commute, so non-commuting examples need a non-abelian group; try S_3. Result: Observation that sharpens the question: on any abelian Gamma, equivariant operators are convolution operators and commute, so the linear bound is already known there; the first non-trivial case is a non-abelian finite group, e.g. S_3 acting on itself, where an equivariant Q is right-convolution by an element of the group algebra and two such operators commute iff their group-algebra elements do. d-bar on a finite group is the optimal coupling cost for the normalised Hamming distance under invariant couplings, which is an LP of size 2^6 x 2^6 = 4096 variables for S_3, feasible to compute exactly. Obstruction: Experiment specified, not executed in this batch. Verification level: unreviewed.

### C0040. Absolutely continuous invariant measure for the environment seen from the particle versus ballisticity

Source: Drewitz and Ramirez: Selected topics in random walks in random environment (`drewitz_ramirez_rwre_2014`), Open question 2.19, p. 24.

Statement: For a RWRE satisfying (ERG) and (E) and transient in a direction, is the existence of an invariant probability measure for the environmental process absolutely continuous with respect to P equivalent to ballisticity in that direction?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0040-A002, correcting C0040-A001). Correction: Codex review 12:02: the forward implication is Drewitz-Ramirez Corollary 2.15. Result: CORRECTION of C0040-A001. The direction 'invariant absolutely continuous probability measure for the environment process + transience in direction l implies ballisticity in direction l' is not open: it is Corollary 2.15 of the source (Drewitz-Ramirez, PDF pages 20-21), so A001's reduction of that direction to strict positivity of the velocity was solving a solved half. Obstruction: Without i.i.d. renewal structure neither the construction of the invariant measure nor strict positivity of the velocity is available. (carried over from C0040-A001, unchanged by the correction) Independent check: Correction checked line by line against the source and the holder's message by the Fable agent; the holder's claim was taken as a lead, not as authority. Verification level: unreviewed.

### C0041. Transience in a direction implies ballisticity for uniformly elliptic i.i.d. RWRE in d >= 2

Source: Drewitz and Ramirez: Selected topics in random walks in random environment (`drewitz_ramirez_rwre_2014`), Open question 2.20, p. 24.

Statement: Let d >= 2 and the RWRE satisfy (UE) and (IID) and be transient in direction l. Is the walk necessarily ballistic in direction l?

Status: historical status source_says_open; current-literature status no_resolution_found_in_documented_search. Status search found: Bounded search 2026-09-07: Guerra and Ramirez (arXiv 1809.02011, 'A proof of Sznitman's conjecture about ballistic RWRE') proved the equivalence of conditions (T) and (T'), which is Open question 3.28 of the source, NOT this question; no proof that transience implies ballisticity in d >= 2 was found.

Our work (attempt C0041-A001). Method: Try the d = 2 special structure: directional 0-1 law (Zerner-Merkl) plus the renewal structure. Result: Under (IID)+(UE), transience in direction l gives the regeneration structure of Sznitman-Zerner with regeneration times tau_1; ballisticity is equivalent to E[tau_1 | D = infinity] < infinity. Transience only gives tau_1 < infinity a.s. Obstruction: Integrability of the regeneration time is not implied by transience without a quantitative condition. Verification level: unreviewed.

### C0042. Ballisticity under the ellipticity moment condition

Source: Drewitz and Ramirez: Selected topics in random walks in random environment (`drewitz_ramirez_rwre_2014`), Open question 2.22, p. 25.

Statement: For d >= 2, is every RWRE satisfying (E), (IID) and max_e E[1/(1 - omega(0,e) omega(0,-e))] < infinity which is transient in direction l ballistic in direction l? (Known for Dirichlet environments in d >= 3 by Sabot.)

Status: historical status source_says_open; current-literature status resolved_in_literature. Resolved by: Refuted as a criterion: Fribergh and Kious, arXiv 1404.2060v2, Proposition 4.4 (directionally transient, zero-speed RWRE in d >= 3 with uniformly positive edge escape); the source's displayed condition also carries a site-index typo. Identified by the Codex holder 12:02 his clock.

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0043. Transience of i.i.d. elliptic RWRE in dimensions d >= 3

Source: Drewitz and Ramirez: Selected topics in random walks in random environment (`drewitz_ramirez_rwre_2014`), Open question 2.23, p. 25.

Statement: Is every RWRE satisfying (E) and (IID) transient in dimension d >= 3? (Known for Dirichlet environments by Sabot and essentially for balanced environments by Lawler.)

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0043-A001). Method: Try to derive transience from the quenched invariance principle route used for balanced walks, in the general case. Result: For balanced environments Lawler's argument uses the invariant measure of the environment process (from the maximum principle) to get a quenched CLT and then transience via the Green function decay; for general elliptic i.i.d. environments no invariant measure absolutely continuous with respect to P is known to exist (its existence is Open question 2.19's territory), so the route fails at the first step. An alternative is the Lyapunov-exponent route: transience follows if the quenched Green function G_omega(0,0) is finite a.s., which for a random walk with bounded-range transitions in d >= 3 follows from a lower bound on the spectral gap of the walk killed outside large boxes; in a random environment the killed walk's Perron eigenvalue could be arbitrarily close to 1 if the environment contains near-recurrent regions, and under (E) alone such regions exist at all scales with small probability. Obstruction: No invariant measure for the environment process; trap density under mere ellipticity uncontrolled. Verification level: unreviewed.

### C0044. Zero-one law for directional transience in dimensions d >= 3

Source: Drewitz and Ramirez: Selected topics in random walks in random environment (`drewitz_ramirez_rwre_2014`), Open question 3.2, p. 42.

Statement: For a RWRE satisfying (E) and (IID) and any direction l, is P_0[A_l] in {0,1}, where A_l is the event of transience in direction l? Known for d = 1 and d = 2 (Zerner-Merkl).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0044-A002, correcting C0044-A001). Correction: Codex review 12:02: A_l and A_{-l} are disjoint by definition; the content of Zerner-Merkl is the 0-1 law for A_l. Result: CORRECTION of C0044-A001's first sentence. The events {X_n . l -> +infinity} and {X_n . l -> -infinity} are disjoint by definition, so 'Zerner-Merkl show P(A_l intersect A_{-l}) = 0' is empty; what Zerner-Merkl prove in d = 2 is P_0(A_l) in {0,1}, using planarity to show two walks in the same environment intersect, which is what A001 then describes. Obstruction: Planarity is essential to the d = 2 proof; no substitute in d >= 3. (carried over from C0044-A001, unchanged by the correction) Independent check: Correction checked line by line against the source and the holder's message by the Fable agent; the holder's claim was taken as a lead, not as authority. Verification level: unreviewed.

### C0045. Does positive velocity imply the polynomial ballisticity condition (P)_M?

Source: Drewitz and Ramirez: Selected topics in random walks in random environment (`drewitz_ramirez_rwre_2014`), Open question 3.20, p. 52.

Statement: Under (UE) and (IID), does ballisticity (positive limiting velocity in direction l, condition (3.26)) imply the polynomial condition (P)_M for M > 15d + 5?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0045-A002, correcting C0045-A001). Correction: Codex review 12:02: the claimed equivalence of (P)_M with arbitrary regeneration-moment bounds is unsupported. Result: CORRECTION of C0045-A001. A001 asserted '(P)_M for large M <=> E[tau_1^{M'}] < infinity for some M' growing with M'. Obstruction: No self-improvement mechanism for regeneration-time moments is known. (carried over from C0045-A001, unchanged by the correction) Independent check: Correction checked line by line against the source and the holder's message by the Fable agent; the holder's claim was taken as a lead, not as authority. Verification level: unreviewed.

### C0046. Equivalence of the ballisticity conditions (T) and (T')

Source: Drewitz and Ramirez: Selected topics in random walks in random environment (`drewitz_ramirez_rwre_2014`), Open question 3.28, p. 55.

Statement: Is Sznitman's condition (T') equivalent to condition (T) for RWRE in uniformly elliptic i.i.d. environments?

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Guerra and Ramirez, 'A proof of Sznitman's conjecture about ballistic RWRE' (arXiv 1809.02011; Comm. Pure Appl. Resolved by: Guerra-Ramirez 2018/2020

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0047. Benjamini-Schramm conjecture: p_c < p_u if and only if the group is non-amenable

Source: Duminil-Copin: Sixty years of percolation, ICM 2018 (`duminil_copin_icm_2018`), Conjecture 2, p. 4.

Statement: For a Cayley graph G of a finitely generated infinite group, p_c(G) < p_u(G) if and only if the group is non-amenable.

Status: historical status source_says_open; current-literature status unverified. Status search found: Amenable direction is known (Burton-Keane uniqueness gives p_c = p_u). The non-amenable direction is known for many classes (Pak-Smirnova for some generating sets, Hutchcroft for several classes including nonunimodular and hyperbolic settings); not verified in a bounded search whether the full conjecture has been settled by 2026.

Our work (attempt C0047-A001). Method: Attempt the non-amenable direction through the spectral radius criterion of Benjamini-Schramm and Hutchcroft's p_c <= 1/spectral radius... type bounds. Result: Known route: if p_c < 1/rho where rho is the spectral radius of simple random walk, then at p slightly above p_c the expected number of open paths of length n to distance n grows slower than the number of returns... this gives p_c < p_u for graphs where p_c(G) < 1/(rho ... ) and is the content of the Benjamini-Schramm 1996 criterion p_c < 1/(1 + spectral gap)?; the general conjecture needs p_c < p_u even when p_c is close to 1/rho... Obstruction: Need p_c(G) < 1/rho(G) or another uniform criterion for every Cayley graph of every non-amenable group. Verification level: unreviewed.

### C0048. Discontinuity of the Potts phase transition on Z^d for q >= 3, d >= 3

Source: Duminil-Copin: Lectures on the Ising and Potts models on the hypercubic lattice, PIMS 2017 (`duminil_copin_ising_potts_2017`), Conjecture 2, p. 93; also duminil_copin_icm_2018 p. 18 (q_c(d) = 2).

Statement: Prove that the phase transition of the nearest-neighbour q-state Potts model on Z^d with d >= 3 is discontinuous for every q >= 3 (equivalently q_c(d) = 2 for all d >= 3).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0048-A001). Method: Examine whether the reflection-positivity chessboard argument can be pushed down from q >= q_c(d) large to q = 3 in d = 3 using improved contour entropy bounds. Result: The Kotecky-Shlosman argument proves a first-order transition when the entropy of contours (bounded by e^{c |contour|}) is beaten by the energy gain, which requires q large enough that log q exceeds a lattice-dependent constant; in d = 3 the best constants give q >= some number in the tens. Improving to q = 3 needs the exact contour entropy, which is not available; numerically the d = 3, q = 3 transition is weakly first order with a tiny latent heat, so any argument must be sharp to within a few percent, beyond what chessboard estimates give. Obstruction: Contour-entropy constants are far from sharp and the two-dimensional transfer-matrix route has no three-dimensional analogue. Verification level: unreviewed.

### C0049. Convergence of random-cluster interfaces to SLE(kappa) for q in (0,4], q not 2

Source: Duminil-Copin: Lectures on the Ising and Potts models on the hypercubic lattice, PIMS 2017 (`duminil_copin_ising_potts_2017`), Conjecture 3 (Schramm), p. 93.

Statement: For the critical random-cluster model with cluster weight q <= 4 on Dobrushin domains, the exploration path converges to SLE(kappa) with kappa = 4 pi / (pi - arccos(sqrt q / 2)); known for q = 2 (Smirnov, Chelkak et al.) and, for q = 1 site percolation, on the triangular lattice only.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0049-A001). Method: Check which ingredients of the q = 2 proof are available for other q. Result: The q = 2 proof uses (i) the parafermionic observable being discretely holomorphic (full Cauchy-Riemann), (ii) RSW-type crossing estimates for tightness, (iii) identification of the limit via the martingale observable. For q in (1,4) not 2: (ii) is available (Duminil-Copin-Sidoravicius-Tassion 2017 for q in [1,4]); (iii) would follow from (i); (i) fails: for general q the observable satisfies only the contour relations (half of the Cauchy-Riemann equations), the same obstruction as in C0017. Obstruction: Discrete holomorphicity is only half-satisfied for q not 2. Verification level: unreviewed.

### C0050. Convergence of the parafermionic observable to (phi')^sigma for q <= 4

Source: Duminil-Copin: Lectures on the Ising and Potts models on the hypercubic lattice, PIMS 2017 (`duminil_copin_ising_potts_2017`), Conjecture 4 (Smirnov), p. 94.

Statement: For the critical random-cluster model with q <= 4, the vertex parafermionic observable f_delta satisfies (2 delta)^{-sigma} f_delta -> (phi')^sigma where phi maps the domain to the strip R x (0,1) with a, b sent to -infinity, +infinity.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0050-A001). Method: Test the conjecture's consistency by the boundary values and the contour relations alone. Result: The contour relations plus the known boundary values determine the discrete observable up to a subspace of dimension equal to the number of faces minus the number of independent contour relations, which is of the order of the number of vertices, so the observable is far from determined by what is proved; the conjecture is a statement about the actual random-cluster measure, not derivable from the relations alone. Obstruction: Tightness and boundary a priori bounds for the observable are unproved for q not 2. Verification level: unreviewed.

### C0051. Improved two-point function bounds for the critical three-dimensional Ising model

Source: Duminil-Copin: Lectures on the Ising and Potts models on the hypercubic lattice, PIMS 2017 (`duminil_copin_ising_potts_2017`), Conjecture 5, p. 94.

Statement: For the 3D nearest-neighbour Ising model at beta_c, there exist eps > 0 and constants with c_0 |x-y|^{-(2-eps)} <= <sigma_x sigma_y> <= c_1 |x-y|^{-(1+eps)}.

Status: historical status source_says_open; current-literature status unverified. Status search found: Bounded search 2026-09-07 surfaced Duminil-Copin and Panis, 'New lower bounds for the (near) critical Ising and phi^4 models' two-point functions' (arXiv 2404.05700); whether it achieves the lower bound with exponent 2 - eps in d = 3 was not confirmed in this session.

Our work (attempt C0051-A001). Method: Check what the random-current and infrared bounds give and where each half of the conjecture sits. Result: Upper bound: the infrared bound gives <sigma_0 sigma_x> <= C |x|^{-(d-2)} = C|x|^{-1} in d = 3, and improving to |x|^{-(1+eps)} is the statement eta > 0 (anomalous dimension), known numerically eta = 0.036; an argument would need to show the two-point function is strictly smaller than the Gaussian one in a scale-invariant way, e.g. via the random-current intersection probabilities (the same quantity that gives non-triviality, C0052): if two independent currents from 0 to x and from y to z intersect with probability bounded below uniformly, one gets a strict improvement of Simon-Lieb at every scale which iterates to a power gain. Obstruction: Both halves need scale-invariant intersection estimates for random currents in d = 3, which are not available. Verification level: unreviewed.

### C0052. Non-triviality of the scaling limit of the three-dimensional Ising model

Source: Duminil-Copin: Lectures on the Ising and Potts models on the hypercubic lattice, PIMS 2017 (`duminil_copin_ising_potts_2017`), Conjecture 6, p. 94.

Statement: Prove that the three-dimensional Ising model is non-trivial: its scaling limit is not a Gaussian field (the renormalised coupling constant does not vanish).

Status: historical status source_says_open; current-literature status unverified. Status search found: The second half of the source's Conjecture 6 (triviality in d = 4) was proved by Aizenman and Duminil-Copin, 'Marginal triviality of the scaling limits of critical 4D Ising and phi^4 models', Ann. of Math. 194 (2021) 163-235 (arXiv 1912.07973); the d = 3 non-triviality half remains open per the bounded search of 2026-09-07.

Our work (attempt C0052-A001). Method: Use the random-current representation: non-triviality is equivalent to non-vanishing of the intersection probability of two random currents at large scales. Result: By Aizenman's identity the four-point Ursell function U_4(x_1,...,x_4) is expressed through the probability that the currents from x_1 to x_2 and from x_3 to x_4 share a cluster; non-triviality means the renormalised coupling g = -U_4 summed appropriately does not vanish in the scaling limit, i.e. two independent random-current clusters at scale L intersect with probability bounded below. In d = 3 the clusters have a fractal dimension d_c and two independent such sets in a box of side L intersect with probability of order L^{2 d_c - 3} if they were independent random fractals, which is bounded below iff d_c >= 3/2. Obstruction: Variance of the intersection count needs six-point correlations beyond Lebowitz. Verification level: unreviewed.

### C0053. Localisation-delocalisation transition of one-dimensional random band matrices at W = N^{1/2}

Source: Bourgade: Random band matrices, ICM 2018 survey (`bourgade_band_icm_2018`), Conjecture (0.2), p. 2.

Statement: For d = 1, bulk eigenvectors of N x N random band matrices with band width W are localised for W << N^{1/2} and delocalised with GOE/GUE local statistics for W >> N^{1/2}.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Yau and Yin, 'Delocalization of one-dimensional random band matrices' (arXiv 2501.01718, 2025) proved delocalisation, QUE and GUE statistics for W > N^{1/2+eps}; arXiv 2508.05802 'Localization of one-dimensional random band matrices' (2025) treats the localised side; together the d = 1 transition is established per the bounded search of 2026-09-07. Resolved by: Yau-Yin 2025 (arXiv 2501.01718); arXiv 2508.05802

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0054. Localisation of all bulk states for two-dimensional random band matrices at fixed band width

Source: Bourgade: Random band matrices, ICM 2018 survey (`bourgade_band_icm_2018`), Conjecture (0.2), p. 2 and Section 2.2, p. 7.

Statement: For d = 2 and fixed band width W, all bulk eigenvectors of the random band matrix on a box of side N are localised with localisation length of order exp(W^2), and the local eigenvalue statistics are Poisson as N -> infinity.

Status: historical status source_says_open; current-literature status unverified. Status search found: The delocalised side W >> (log N)^{1/2} in d = 2 was addressed in arXiv 2503.07606 (2025) per the bounded search; the localisation side at fixed W is not known to be proved.

Our work (attempt C0054-A001). Method: Try a fractional-moment (Aizenman-Molchanov) argument adapted to band matrices at fixed W in d = 2. Result: The fractional-moment method proves localisation when the expected s-th moment of the Green function E|G_{xy}(E + i eta)|^s decays exponentially in |x - y|; for band matrices at fixed W in d = 2 the required a priori bound is a decoupling of the moment across a band-width-sized block, which for the Anderson model comes from the rank-one structure of the diagonal disorder. Band matrices have no rank-one structure: the randomness at a site is a W^2-dimensional block, and the decoupling lemma degrades by a factor that grows with W^2, so the method proves localisation only for W <= W_0 small (large disorder regime), not for every fixed W. Obstruction: Fractional-moment decoupling loses a factor growing with W^2; no method reaches exp(W^2) localisation lengths. Verification level: unreviewed.

### C0055. Finite critical band width in dimension three

Source: Bourgade: Random band matrices, ICM 2018 survey (`bourgade_band_icm_2018`), Conjecture (0.2), p. 2.

Statement: For d = 3 there is a finite critical band width W_c such that bulk eigenvectors of random band matrices are localised for W < W_c and delocalised for W > W_c.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0055-A001). Method: Locate the obstruction between the known polynomial regimes and a finite threshold. Result: Delocalisation is known in d = 3 for W >= N^{c} with explicit c (Yang-Yau-Yin quantum-diffusion results for W >> N^{1-eps} and later improvements), and the mean-field reduction of the source suggests W >> N^{1-eps}; a finite W_c requires an argument uniform in N at fixed W, i.e. a renormalisation-group or supersymmetric proof of diffusion for the Green function, which exists only for the density of states (Disertori-Pinson-Spencer in d = 3) and not for eigenvector delocalisation. Obstruction: All rigorous delocalisation results need W to grow with N; a fixed-W argument is non-perturbative. Verification level: unreviewed.

### C0056. Extended states for the three-dimensional Anderson model at weak disorder

Source: Bourgade: Random band matrices, ICM 2018 survey (`bourgade_band_icm_2018`), Section 2.1, p. 7.

Statement: Prove existence of absolutely continuous spectrum (delocalised states) for the random Schrodinger operator -Delta + lambda V on Z^3 at small disorder lambda, and GOE local statistics for its finite-volume restriction.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0056-A001). Method: Review the failure of perturbation theory and test a restricted version on a tree-like subgraph. Result: On the Bethe lattice a.c. spectrum is known (Klein; Aizenman-Warzel) because the self-consistent equation for the Green function has a stable solution; on Z^3 the corresponding equation is not closed. A known partial statement is that the disorder-averaged Green function has diffusive behaviour up to times lambda^{-2-delta} (Erdos-Salmhofer-Yau), which is the kinetic regime and does not reach the infinite-time statement. Obstruction: Absence of a closed self-consistency equation on Z^3; kinetic-regime results stop at finite times. Verification level: unreviewed.

### C0057. Filled-in peeling discovers the whole map for every critical weight sequence

Source: Curien: Peeling random planar maps, Saint-Flour XLIX 2019 lecture notes, author preliminary version (`curien_peeling_2019`), Open question after Corollary 27, p. 61.

Statement: Corollary 27 shows that for a critical weight sequence of type a in [3/2, 5/2] a filled-in peeling exploration of the infinite Boltzmann map almost surely exhausts the map; is this true for every critical weight sequence?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0057-A001). Method: Isolate what the proof uses about the type a and try to replace it by a general criterion. Result: The proof reduces the statement to the divergence of the series sum_n (1/S_n)^{a-1}... in general, to sum_n P(peeling step n swallows the marked boundary vertex | past) = infinity, i.e. a conditional Borel-Cantelli; the source uses the scaling limit of the perimeter process to show the summands are of order 1/n. For a general critical weight sequence the perimeter process S is a random walk (h-transform) whose step distribution nu has the property sum_k k nu(k) ... criticality gives a specific tail, and the swallowing probability at perimeter l is q_l := sum_{k >= l/2} b^{(l)}(*,k) which is of order l^{1-a} for type a. Obstruction: Non-regularly varying critical weight sequences: no growth control on the h-transformed perimeter walk. Verification level: unreviewed.

### C0058. A peeling algorithm exploring site percolation on Boltzmann maps

Source: Curien: Peeling random planar maps, Saint-Flour XLIX 2019 lecture notes, author preliminary version (`curien_peeling_2019`), Open question, p. 79.

Statement: Can one find a peeling algorithm exploring site percolation on Boltzmann planar maps in the same spirit as the algorithm for bond percolation, so as to compute the site percolation threshold?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0058-A001). Method: Design the algorithm and check whether the exploration frontier remains Markov. Result: For bond percolation the peeling frontier is a two-colour boundary (free/blocked edges) and the algorithm peels the edge at the colour change, keeping the unexplored region a Boltzmann map with a boundary of the same type. For site percolation the colour lives on vertices and after peeling a face the newly exposed boundary vertices are uncoloured; the natural algorithm peels the edge whose left endpoint is black and right endpoint is uncoloured, colouring the new vertices as they appear. Obstruction: Unbounded face degrees expose many uncoloured boundary vertices at once; the frontier state is a word, not an integer. Verification level: unreviewed.

### C0059. Transience of the dual infinite Boltzmann map for a in [2, 5/2)

Source: Curien: Peeling random planar maps, Saint-Flour XLIX 2019 lecture notes, author preliminary version (`curien_peeling_2019`), Open question, p. 93.

Statement: Let q be a critical weight sequence of type a in [2, 5/2); is the dual map m-dagger of the infinite Boltzmann map of the plane transient for simple random walk under P^{(1)}_infinity?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0059-A001). Method: Compare with the a in (3/2, 2) proof via first-passage percolation and with the recurrence criterion via degree growth. Result: For a < 2 the source proves transience through a finite-energy flow built from the fpp-distance structure, using that face degrees along the peeling are heavy-tailed enough (the dual has vertices of huge degree, giving 'highways'). For a >= 2 the degree of the dual's root is lighter tailed and the map is 'dilute'; the known results are: the primal map is recurrent for all a (bounded degrees, Gurel-Gurevich-Nachmias), and the dual is transient for a < 2. Obstruction: The tail index of the dual root degree crosses the Gurel-Gurevich-Nachmias regime inside the interval; the threshold is not located. Verification level: unreviewed.

### C0060. Positivity of the vacant-set threshold u* for random interlacements on the Sierpinski gasket times Z

Source: Drewitz, Rath, Sapozhnikov: An introduction to random interlacements, preliminary version of the SpringerBriefs book (`drs_interlacements_book_2014`), Chapter 10 notes, p. 81.

Statement: For random interlacements on G x Z with G the discrete Sierpinski gasket graph, is the vacant-set percolation threshold u* strictly positive?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0060-A001). Method: Try the renormalisation argument for u* > 0 with the gasket's polynomial growth and heat-kernel bounds. Result: The Z^d proof of u* > 0 (Sznitman) uses a renormalisation over boxes at scales L_n with the decoupling of the interlacement in distant boxes controlled by the capacity of boxes (order L^{d-2}) against the volume of the sprinkling; on G x Z the walk has spectral dimension d_s = 2 log 3 / log 5 + 1 = 2.365 and walk dimension d_w = log 5 / log 2 = 2.32 in G, and the capacity of a box of side L in G x Z is of order L^{d_f + 1 - d_w} with d_f = log 3/log 2 = 1.585, i.e. Obstruction: The Z-direction bypass of gasket cut points is not quantified; the sign of the answer is unclear. Verification level: unreviewed.

### C0061. Local uniqueness of the infinite vacant cluster throughout the supercritical phase

Source: Drewitz, Rath, Sapozhnikov: An introduction to random interlacements, preliminary version of the SpringerBriefs book (`drs_interlacements_book_2014`), Chapter 10 notes, p. 81.

Statement: Does the local uniqueness estimate P[0 connected in V^u to B(L)^c but not to infinity] <= kappa exp(-L^{1/kappa}) hold for every u < u*, and not only for u small?

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Duminil-Copin, Goswami, Rodriguez, Severo and Teixeira, 'Phase transition for the vacant set of random walk and random interlacements' (2023), proved the equality of the thresholds bar u = u* = u**, which gives local uniqueness with stretched-exponential bounds in the whole supercritical phase; bounded recall, not re-fetched. Resolved by: Duminil-Copin-Goswami-Rodriguez-Severo-Teixeira 2023

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0062. Uniqueness and description of the maximal-dimension Young diagram for finite n

Source: Romik: The surprising mathematics of longest increasing subsequences, author PDF (`romik_lis_2015`), Section 1.18 discussion, p. 74.

Statement: For finite n, describe the shape of maximal dimension (the partition of n maximising the number of standard Young tableaux) explicitly or by an efficient algorithm, prove it is unique, and improve the asymptotic bounds on the maximal dimension.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0062-A001). Method: Exact computation of maximal-dimension shapes for small n by the hook-length formula, checking uniqueness. Result: By the hook-length formula the dimension is n!/prod hooks. Exact enumeration of all partitions of n for every n <= 40 (raw/C_romik_maxdim_n_le_40.json): for every n <= 40 the maximiser is unique up to conjugation, i.e. either a single self-conjugate shape (n = 1, 3, 5, 6, 8, 10, 12, 15, 17, 21, 23, 27, 30, 34, 36, 38) or exactly one conjugate pair (all other n <= 40); no tie between non-conjugate shapes occurred. Obstruction: No structure theorem for the discrete maximiser; enumeration is exponential in sqrt n. Independent check: Conjugation preserves the multiset of hook lengths; the enumeration used exact integer arithmetic over all p(n) partitions (p(40) = 37338). Verification level: unreviewed. Proof/memo evidence file: `raw/C_romik_maxdim_n_le_40.json` (under the intake directory).

### C0063. Critical exponent beta = 1 in the asymptotic sense for high-dimensional percolation

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 9.1, p. 126.

Statement: Prove that theta(p) ~ c (p - p_c) as p decreases to p_c for percolation on Z^d in high dimensions (beta = 1 in the asymptotic, not only bounded-ratio, sense), possibly by a lace-expansion argument.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0063-A001). Method: Differentiate the magnetisation lace expansion at the critical point. Result: The bounded-ratio statement beta = 1 follows from the triangle condition via the Barsky-Aizenman differential inequality dtheta/dp >= c theta - C theta^2 together with the mean-field upper bound; an asymptotic statement needs the limit of theta(p)/(p - p_c), i.e. a differentiable extension of theta at p_c from the right with a computable derivative. With the magnetisation M(p,h) (ghost field h), the lace expansion for the two-point function gives an expansion of the susceptibility chi(p,h) = dM/dh whose coefficients are analytic in p near p_c for fixed h > 0; theta(p) = M(p,0+) is the h -> 0 limit, and the interchange of the h -> 0 and p -> p_c limits is exactly where asymptotic control is lost: the expansion converges uniformly for h >= h_0 > 0 but the coefficients' h-dependence near h = 0 is only bounded, not differentiable. Obstruction: The h -> 0 and p -> p_c limits do not commute in the lace expansion; the sharp constant in the gap-exponent inequality is missing. Verification level: unreviewed.

### C0064. Infrared bound for nearest-neighbour percolation in every dimension d > 6

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 10.1, p. 145.

Statement: Extend the infrared bound (the Fourier two-point function bounded by C/|k|^2 at criticality) from d >= 11 to every dimension d > 6 for nearest-neighbour percolation on Z^d.

Status: historical status source_says_open; current-literature status unverified. Status search found: Best known: d >= 11 by Fitzner and van der Hofstad (NoBLE, 2017); d > 6 for sufficiently spread-out models. Not verified further in this session.

Our work (attempt C0064-A001). Method: Examine the small parameter of the lace expansion and whether a different expansion parameter exists for d in {7,...,10}. Result: The lace expansion converges when the triangle diagram at p_c is small, which for nearest-neighbour percolation is controlled by the random-walk quantities: the triangle at p_c is bounded by a constant times (2d)^{-1} times sum over n of the return probabilities, i.e. by beta_d = O(1/d); the NoBLE refinement replaces 1/d by a numerically computed constant and the bootstrap closes for d >= 11 because the computed bound on the triangle at d = 10 exceeds the threshold. Obstruction: No small parameter for nearest-neighbour Z^d with 7 <= d <= 10. Verification level: unreviewed.

### C0065. Existence and equality of the supercritical exponents gamma', nu', nu_2' in high dimensions

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 11.1, p. 149.

Statement: Prove that the supercritical critical exponents gamma', nu', nu_2' (defined through the approach p decreasing to p_c) exist for high-dimensional percolation and coincide with gamma, nu, nu_2.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0065-A001). Method: Try to control the finite-cluster susceptibility above p_c via the lace expansion with a cluster-size cutoff. Result: Above p_c the finite-cluster two-point function tau^f(x) = P(0 <-> x, |C(0)| < infinity) is not directly lace-expandable because the finite-cluster condition is not local; the standard route is through the h -> 0 limit of the magnetisation, whose derivatives in h at fixed p > p_c give the finite-cluster moments. The scaling relation gamma' = gamma follows if the magnetisation M(p,h) has a scaling form M ~ (p - p_c) f(h / (p - p_c)^Delta) with the same Delta on both sides, which is the mean-field prediction; the mean-field magnetisation satisfies M ~ (p-p_c) + sqrt(h) crossover, and the finite-cluster susceptibility above p_c would then be chi^f ~ (p - p_c)^{-1}, i.e. gamma' = 1. Obstruction: No expansion for finite-cluster quantities above p_c; only the lower bounds are rigorous. Verification level: unreviewed.

### C0066. Sharp intrinsic and extrinsic one-arm exponents in high dimensions

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 11.2, p. 152.

Statement: Prove that the limits a_in = lim n P_{p_c}(exists x with intrinsic distance d_{C(0)}(0,x) >= n) and a_ex = lim n^2 P_{p_c}(0 <-> boundary of the box of side n) exist for percolation on Z^d, d > 6.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0066-A001). Method: Reduce the intrinsic limit to a renewal-type statement for the branching-process comparison. Result: The intrinsic one-arm probability is bounded above and below by constants over n (Kozma-Nachmias), and the comparison object is the survival probability of a critical branching process with finite variance, for which n P(survive n generations) -> 2/sigma^2 (Kolmogorov). For the intrinsic arm event the analogous statement would be n P(intrinsic radius >= n) -> a_in where a_in should be 2/V with V the variance of the offspring distribution of the effective branching structure (the cluster explored by intrinsic distance is a branching process with dependent offspring). Obstruction: Exact constants for the intrinsic branching structure require second-order lace expansion information. Verification level: unreviewed.

### C0067. Notions of criticality for percolation on high-dimensional tori

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 13.1, p. 179.

Statement: For percolation on the torus of side n in dimension d > 6, show that the maximiser p_c^{(1)} of the derivative of log of the torus susceptibility satisfies |p_c^{(1)} - p_c(T_{n,d})| = O(V^{-1/3}), and similarly for the other two candidate definitions p_c^{(2)}, p_c^{(3)}.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0067-A001). Method: Compute the maximiser of d/dp log chi_T(p) in the mean-field random-graph analogue and compare with the window width. Result: For the Erdos-Renyi graph G(n, p) the susceptibility chi(p) = E|C(uniform vertex)| satisfies chi ~ 1/(1 - np) below the window and the derivative of log chi is maximised inside the critical window np = 1 + O(n^{-1/3}), at distance O(n^{-1/3}) from any other reasonable critical point; the same holds for the torus IF the torus susceptibility has the mean-field form chi_T(p) = chi_{Z^d}(p) + V (theta-like term) with the crossover at |p - p_c| ~ V^{-1/3}, which is the content of the torus plateau results (Theorem 13.9 of the source and the 2021 Hutchcroft-Michta-Slade torus plateau). Obstruction: Two-sided derivative control of the torus susceptibility inside the scaling window is not available. Verification level: unreviewed.

### C0068. Concentration and uniqueness of the giant component above the scaling window on high-dimensional tori

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 13.2, p. 180.

Statement: For the torus T_{n,d}, d > 6, and p = p_c(1 + eps) with eps -> 0 but eps >> V^{-1/3}, prove that |C_max|/(eps V) -> c in probability and |C_(2)|/(eps V) -> 0, with c the right-derivative of theta at p_c(Z^d).

Status: historical status source_says_open; current-literature status unverified. Status search found: Hulshof and Nachmias (2020) proved uniqueness and concentration of the giant for the hypercube in a slightly supercritical regime; the torus case d > 6 was not verified as resolved in this session.

Our work (attempt C0068-A001). Method: Sprinkling plus the Z^d theta-asymptotics. Result: The natural argument: at p = p_c(1+eps) the density of vertices in clusters of size at least K (K large but fixed relative to eps) on the torus is close to theta_{Z^d}(p) ~ c eps by local comparison with Z^d (finite clusters of bounded size are local), and sprinkling a further eps' << eps of open edges merges the large clusters into one giant of size about theta(p) V, provided large clusters are spread out enough that sprinkled edges connect them (the standard ADS/ Borgs et al. argument). Obstruction: Uniform cluster-size tail bounds on the torus in the slightly supercritical regime are missing. Verification level: unreviewed.

### C0069. Scaling limit of critical percolation cluster sizes on the hypercube

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 13.3, p. 189.

Statement: For percolation on the hypercube {0,1}^d at p = p_c(1 + theta 2^{-d/3}), prove that V^{-2/3} (|C_(i)|)_{i>=1} converges in distribution to a limit (gamma_i(theta))_{i>=1}, expected to be related to the Erdos-Renyi multiplicative coalescent limit.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0069-A001). Method: Compare the exploration process of the hypercube with the Aldous exploration of the Erdos-Renyi graph. Result: Aldous's proof for G(n,p) uses that the exploration process is a random walk with drift theta - t and unit variance, up to depletion; on the hypercube the exploration of a cluster is a random walk whose step distribution depends on the local geometry (the number of unexplored neighbours of the current vertex is d minus the number of explored ones, and explored vertices are geometrically correlated). Obstruction: Local versus global depletion in the exploration walk; needs spread-out geometry of critical hypercube clusters. Verification level: unreviewed.

### C0070. Discrete duality principle for hypercube percolation

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 13.4, p. 190.

Statement: Show that for the hypercube the second largest cluster at p = p_c(1 + eps) (eps >> 2^{-d/3}) has, to leading order, the size of the largest cluster at p_c(1 - eps).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0070-A001). Method: Identify the subcritical largest cluster size, which the source flags as unknown, via the cluster tail. Result: In G(n,p) the duality principle comes from the exact exchangeability of the graph after removing the giant; on the hypercube there is no such exact symmetry, and the principle must be proved from the cluster-size tail: at p_c(1 - eps) the largest cluster has size Theta(eps^{-2} log(eps^3 2^d)) (the source's Theorem 13.8 gives the upper bound and the matching lower bound is the missing half), and at p_c(1+eps) the second largest is expected to be of the same form. Obstruction: Sharp exponential rate of the subcritical cluster tail on the hypercube and the post-giant tail are both unproved. Verification level: unreviewed.

### C0071. Multiplicative-coalescent scaling limit of critical percolation on high-dimensional tori

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 13.5, p. 196.

Statement: For T_{n,d}, d > 6, at p = p_c(Z^d)(1 + theta V^{-1/3}), prove that V^{-2/3}(|C_(i)|)_{i>=1} converges to (a time-shifted, rescaled) multiplicative coalescent, the Erdos-Renyi scaling limit.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0071-A001). Method: Same reduction as C0069 for the torus, with the additional plateau input. Result: The torus plateau (Hutchcroft-Michta-Slade) shows the two-point function inside the window is the Z^d two-point function plus a constant V^{-2/3}-scale plateau, which is the mean-field signature; the multiplicative coalescent limit would follow from convergence of the exploration process to Aldous's Brownian motion with parabolic drift, which needs (a) the exploration steps to have asymptotically the variance of a critical branching process, given by the Z^d local structure (available from the lace expansion), and (b) the depletion term to be asymptotically global (the same obstruction as on the hypercube; on the torus the geometric depletion is even more pronounced since clusters are localised in Euclidean space at scale V^{1/6}... the critical cluster of size V^{2/3} has Euclidean diameter of order (V^{2/3})^{1/4} = V^{1/6} in d > 6 (four-dimensional geometry), while the torus has side V^{1/d}; V^{1/6} vs V^{1/d}: for d > 6 V^{1/6} > V^{1/d}, so the critical clusters WRAP around the torus many times, which supports global (mean-field) depletion: a wrapped cluster sees the torus uniformly. Obstruction: Exploration-level (higher-point) plateau statement not available. Verification level: unreviewed.

### C0072. Scaling of the largest critical cluster in a high-dimensional box under free, zero and wired boundary conditions

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 13.6, p. 199.

Statement: For critical percolation on the box [0,n-1]^d, d > 6, identify the exact scaling of the largest cluster under bulk, zero and wired boundary conditions; conjecturally |C_max^{(b)}| / (n^4 log n) and |C_max^{(z)}|/(n^4 log n) converge in probability to constants and |C_max^{(w)}| / n^{d-1} converges to a constant.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0072-A001). Method: Heuristic derivation of the three scalings and identification of the rigorous gaps. Result: Free/zero boundary: the largest cluster among about n^d / n^4 ... the box contains clusters whose sizes have tail P(|C| >= k) ~ k^{-1/2} in mean field, cut off at the box scale where the cluster diameter ~ k^{1/4} reaches n, i.e. k ~ n^4; the number of clusters of size about n^4 in the box is n^d P(|C(0)| ~ n^4)/n^4 ~ n^{d-6} which is large for d > 6, and the maximum of n^{d-6} clusters with tail k^{-1/2} cut off at n^4 gives the log n factor through the extreme-value count, hence n^4 log n. Obstruction: Boundary-sensitive cluster-size tails for bulk/zero conditions; sharp one-arm constant for the wired constant. Verification level: unreviewed.

### C0073. Critical exponent of the diffusion constant of random walk on the supercritical percolation cluster

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 14.1, p. 206.

Statement: For random walk on the infinite percolation cluster in sufficiently high dimension, show that the diffusion constant satisfies sigma(p)^2 ~ (p - p_c)^2 as p decreases to p_c; even monotonicity of p -> sigma^2(p) is not known.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0073-A001). Method: Attempt monotonicity via a coupling of the percolation clusters and the variational formula for the diffusion constant. Result: The diffusion constant of the random conductance model has a variational (homogenisation) formula sigma^2 = inf over correctors of the expected Dirichlet energy per unit volume; adding edges (increasing p in the standard coupling) increases every Dirichlet energy but ALSO changes the normalisation (the density of the infinite cluster theta(p) and the invariant measure), so monotonicity of sigma^2 in p does not follow from the coupling: the variational formula gives monotonicity of the effective conductance per unit volume, sigma^2 theta(p)... more precisely the quantity theta(p) sigma^2(p) times the degree normalisation is monotone (it is the effective conductivity of the medium, monotone by Rayleigh), so sigma^2(p) >= sigma^2(p') theta(p')/theta(p) for p > p': a one-sided monotonicity statement. Obstruction: No lower bound on the backbone conductivity near p_c. Independent check: Rayleigh's monotonicity applies since the standard coupling only adds conductors; the homogenised conductivity equals theta times the diffusion constant times a fixed normalisation. Verification level: unreviewed.

### C0074. Scaling limit of random walk on the high-dimensional incipient infinite cluster

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 14.2, p. 212.

Statement: Prove that random walk on the incipient infinite cluster of high-dimensional (d > 6) percolation has a non-degenerate scaling limit.

Status: historical status source_says_open; current-literature status unverified. Status search found: Ben Arous, Cabezas and Fribergh ('Scaling limit for the ant in high-dimensional labyrinths', CPAM 2019) proved a scaling limit for random walk on high-dimensional critical clusters in the oriented and branching-random-walk settings; whether the unoriented IIC case d > 6 is covered was not confirmed in this session.

Our work (attempt C0074-A001). Method: Reduce to the scaling limit of the IIC itself (C0077) plus a homogenisation of the walk on the limit tree. Result: If the IIC converges (as a measure-valued process indexed by intrinsic distance) to incipient infinite super-Brownian motion, then the walk on the IIC should converge to the Brownian motion on the associated continuum random tree embedded in R^d, time-changed by the IIC volume measure, i.e. to the 'Brownian motion on the ISE-type tree' with spatial displacement given by the embedding (the Ben Arous-Cabezas-Fribergh limit). The walk on the discrete tree structure of the IIC is a random walk on a graph that is tree-like at all scales in d > 6 (the number of cycles at scale r is bounded), so the spatial position is a Brownian motion time-changed by the intrinsic clock; the intrinsic clock converges by the tree scaling limit; the embedding of the tree in R^d is a branching random walk-type embedding whose limit is the ISE embedding. Obstruction: Resistance-metric convergence of the IIC in d > 6 is not established. Verification level: unreviewed.

### C0075. ISE scaling limit of critical high-dimensional percolation clusters of fixed size

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 15.1, p. 218.

Statement: For critical percolation on Z^d, d > 6, show that the empirical measure of the cluster of the origin, rescaled by n^{-1/4} in space, conditioned on |C(0)| = n, converges in distribution to integrated super-Brownian excursion (ISE).

Status: historical status source_says_open; current-literature status unverified. Status search found: Hara and Slade proved convergence of the r-point functions of the critical cluster to those of ISE for spread-out models in d > 6 (2000); convergence of the conditional measure itself and the nearest-neighbour case were not verified as resolved.

Our work (attempt C0075-A001). Method: Check whether r-point function convergence implies convergence in distribution of the random measure. Result: Convergence of all moment measures (r-point functions) of a random probability measure on R^d determines its law when the moment measures satisfy a uniqueness condition, which holds for ISE since its moment measures are given by a Feynman-diagram-type formula with Gaussian factors and the total masses grow at most factorially, satisfying Carleman's condition. Hara-Slade's result gives, for spread-out models in d > 6, the convergence of the r-point functions conditioned on cluster size n (their Theorem gives q^{(r)}_n asymptotics) to those of ISE, for each fixed r. Obstruction: Nearest-neighbour r-point functions in d in [11, infinity) not expanded; verification of uniformity in Hara-Slade not redone here. Independent check: Carleman: the r-th moment measure of ISE has total mass of order r! times a constant^r, so sum of (total mass)^{-1/(2r)} diverges; determinacy holds. Verification level: unreviewed.

### C0076. Super-Brownian motion limit of critical percolation clusters in high dimensions

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 15.2, p. 219.

Statement: Show that for d > 6 there are gamma, v such that the measure-valued process X^{(n)}_{nt} = n^{-gamma} sum over vertices at intrinsic distance nt of delta at x/sqrt(vn), under n^gamma P_{p_c}, converges to the canonical measure of super-Brownian motion.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0076-A001). Method: Identify gamma and v from known exponents and locate the missing joint convergence. Result: gamma = 1: the intrinsic one-arm probability is of order 1/n (Kozma-Nachmias), so n P_{p_c}(intrinsic radius >= n) is bounded, matching the canonical measure normalisation; v is the variance per intrinsic step of the spatial displacement, given by the lace expansion two-point function through the intrinsic-distance two-point function (C0079). The finite-dimensional distributions of the process in t are the intrinsic r-point functions with fixed intrinsic distances, which are the objects of C0079 (Open Problem 15.5) at the level of r = 2; the source's Theorem 15.4 handles the number-of-pivotals two-point function, and the intrinsic distance version is the missing step. Obstruction: Intrinsic-distance r-point functions not lace-expanded for unoriented percolation. Verification level: unreviewed.

### C0077. Incipient-infinite super-Brownian-motion limit of the high-dimensional IIC

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 15.3, p. 221.

Statement: Show that for d > 6 the rescaled measure-valued process built from the incipient infinite cluster (vertices at intrinsic distance nt, rescaled) converges to incipient infinite super-Brownian motion (SBM with an immortal particle).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0077-A001). Method: Derive the IIC statement from the critical-cluster statement via the h-transform structure. Result: The IIC is the limit of the critical cluster conditioned on reaching intrinsic distance n (or on |C| large), which at the level of the branching-process comparison is the Doob h-transform of the critical branching process with h = survival, giving the Kesten tree (a spine plus critical trees); at the continuum level the canonical measure of SBM conditioned on survival to time t and then t -> infinity gives SBM with an immortal particle. Obstruction: Same as C0076 plus the sharp one-arm constant. Verification level: unreviewed.

### C0078. Mean-field behaviour of nearest-neighbour oriented percolation for all d > 4

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 15.4, p. 225.

Statement: Show that nearest-neighbour oriented percolation on Z^d x Z_+ exhibits mean-field critical behaviour for every d > 4 (known for sufficiently large d and for spread-out models with d > 4).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0078-A001). Method: Same structural obstruction as C0064, with the oriented triangle diagram. Result: For oriented percolation the lace expansion converges when the oriented triangle (bubble) diagram is small, controlled by the random-walk return probabilities of the d-dimensional walk, of order 1/d; the nearest-neighbour model in d = 5, 6, 7 has no small parameter, exactly as for unoriented percolation below d = 11. The NoBLE-type numerical bootstrap has not been carried out for oriented percolation in the source's account; the threshold would need to be beaten at d = 5, where the bubble diagram is of order 1. Obstruction: No small parameter for nearest-neighbour oriented percolation in d = 5, 6, 7. Verification level: unreviewed.

### C0079. Intrinsic-distance two-point function asymptotics in high dimensions

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 15.5, p. 228.

Statement: Extend the fixed-number-of-pivotals two-point function result (Theorem 15.4) to the intrinsic-distance two-point function tau_n^{(in)}(x) = P_{p_c}(d_{C(0)}(0,x) = n), d > 6.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0079-A001). Method: Relate the intrinsic distance to the number of pivotals along the backbone plus the sizes of the intermediate sausages. Result: The intrinsic distance from 0 to x equals the sum over the backbone decomposition of the intrinsic distances through each 'sausage' between consecutive pivotal bonds; the number of pivotals is the object of Theorem 15.4, and the sausage lengths are i.i.d.-like with a fixed law in the mean-field picture (each sausage is a doubly connected piece of bounded expected size in d > 6 with exponential tails?). Obstruction: Joint expansion in space and intrinsic length not available. Verification level: unreviewed.

### C0080. Borel summability of the 1/d expansion of the percolation threshold

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 15.7, p. 232.

Statement: Prove that the asymptotic expansion p_c(Z^d) = sum_i a_i (2d)^{-i} is Borel summable.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0080-A001). Method: Bound the coefficients' growth from the lace expansion's structure and compare with the Borel condition. Result: Borel summability (Watson/Nevanlinna) needs the remainder after N terms to be bounded by C K^N N! (2d)^{-N} uniformly in a sector, and the coefficients to grow at most like K^N N!. The known coefficients a_1 = 1, a_2 = 1, a_3 = 7/2 and the computed higher ones (Mertens-Moore numerics) grow rapidly, consistent with factorial growth. Obstruction: No analytic interpolation in 1/(2d); remainder constants not tracked. Verification level: unreviewed.

### C0081. Lace-expansion-free derivation and higher coefficients of the 1/d expansion of p_c(Z^d)

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 15.8, p. 232.

Statement: Find an argument for the existence of the asymptotic expansion of p_c(Z^d) in powers of 1/(2d) that avoids the lace expansion, and use it to compute the coefficients a_4, a_5, ....

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0081-A001). Method: Try a direct cluster-expansion (Mayer-type) argument for the susceptibility at fixed p (2d) in the d -> infinity limit. Result: At p = lambda/(2d) the expected cluster size chi(p) has, for fixed lambda < 1, a convergent expansion as d -> infinity in powers of 1/d obtained by comparing the cluster to a branching process with Poisson(lambda) offspring and counting cycles: the first correction comes from the 4-cycles of Z^d (each pair of neighbours of a vertex shares a common neighbour with frequency ~ 1/(2d)), which gives the known a_2 = 1 through the shift of the effective branching ratio. Obstruction: Uniformity of the subcritical cluster expansion up to the critical point; a_4 requires third-order cycle corrections. Verification level: unreviewed.

### C0082. First coefficient where the 1/d expansions of p_c on Z^d and on the hypercube differ

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 15.9, p. 232.

Statement: Extend the expansion of the critical value to the hypercube {0,1}^d and find the first index i for which the coefficients a_i for Z^d and for the hypercube are distinct (they agree for i = 1, 2, 3).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0082-A001). Method: Compare the short cycle structure of Z^d and the hypercube to predict the first differing coefficient. Result: The coefficients a_i are determined by the counts of closed non-backtracking walks of length up to 2i in the graph (the lace-expansion diagrams at order i involve random-walk loops of length up to 2i, up to the normalisation by (2d)^i). Z^d and the hypercube both have degree 2d (resp. d, with the appropriate rescaling) and both have girth 4; the number of 4-cycles through a vertex is d(d-1)/2 ... for Z^d: choose two distinct directions, 4 sign patterns give (2d)(2d-2)/2 cycles; for the hypercube choose two coordinates: d(d-1)/2 cycles; after the normalisation by degree these agree to leading order, which is why a_2 agrees. Obstruction: Not proved; requires the fourth-order lace diagrams on both graphs. Verification level: unreviewed.

### C0083. Asymptotic expansion of the critical value of the Hamming graph

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 15.10, p. 233.

Statement: Show that the critical value of percolation on the Hamming graph K_n^d satisfies p_c(K_n^d; lambda) = sum_{i=1}^{d/3} a_i(d) n^{-i} + O(n^{-1-d/3}), with a_1(d) = 1/d; the second-order term was identified by Federico, van der Hofstad, den Hollander and Hulshof.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0083-A001). Method: Compute a_2(d) by the cycle-correction method as a check, and identify why the expansion truncates at d/3. Result: On K_n^d every vertex has degree d(n-1); at p = lambda/(d(n-1)) the exploration is close to a branching process; the first correction to the branching ratio comes from triangles: each vertex lies in d (n-1)(n-2)/2 triangles (all in one coordinate line), so the effective number of NEW vertices reached in two steps is reduced by a relative amount of order 1/d... normalising, the triangle correction is of relative order (n-2)/(d(n-1)) ~ 1/d, not 1/n, so it shifts p_c at relative order 1/d which is absorbed into a_1(d)?? Obstruction: Third-order cycle corrections on K_n^d not computed. Verification level: unreviewed.

### C0084. No infinite cluster at criticality on quasi-transitive graphs with p_c < 1

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 15.11, p. 235.

Statement: For any quasi-transitive graph G with p_c(G) < 1, prove theta(p_c) = 0 (Benjamini-Schramm Conjecture 4).

Status: historical status source_says_open; current-literature status unverified. Status search found: Known for quasi-transitive graphs of exponential growth (Hutchcroft 2016) and for nonamenable graphs (Benjamini-Lyons-Peres-Schramm); the polynomial-growth case reduces essentially to the Z^d question (C0023).

Our work (attempt C0084-A001). Method: Split by growth type and identify the remaining cases precisely. Result: By Trofimov's theorem a quasi-transitive graph of polynomial growth is quasi-isometric to a Cayley graph of a virtually nilpotent group, and the critical behaviour of percolation is not a quasi-isometry invariant in general, so this does not reduce directly to Z^d; however the known proof for Z^2 (Harris-Kesten) and the high-dimensional proof (lace expansion, d >= 11) do not transfer either. Exponential growth is Hutchcroft's theorem. Obstruction: Polynomial growth is the Z^d problem; intermediate growth defeats the exponential-growth comparison. Verification level: unreviewed.

### C0085. Two-point function of high-dimensional invasion percolation

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 16.1, p. 240.

Statement: Show that for d > 6 there is a constant A such that P(x in the invasion percolation cluster) = A |x|^{-(d-4)}(1 + o(1)) as |x| -> infinity.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0085-A001). Method: Compare the invasion cluster two-point function with the IIC two-point function and locate the difference. Result: The IIC two-point function P_IIC(x in cluster) is asymptotic to A' |x|^{-(d-4)} in high dimensions (from the lace expansion of the IIC, Hofstad-Jarai), and the invasion percolation cluster is expected to have the same decay exponent because the invasion cluster near infinity looks like a critical cluster with a slightly supercritical 'ponds' structure at scales below the current pond size. The source notes that the IIC and IPC have different scaling limits on the tree (Angel-Goodman-den Hollander-Slade), so the constants A and A' differ and the exponent may agree. Obstruction: Requires slightly supercritical two-point asymptotics with constants (C0065-type input). Verification level: unreviewed.

### C0086. Scaling limit of high-dimensional invasion percolation

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 16.2, p. 241.

Statement: Identify the scaling limit, as a measure-valued process indexed by intrinsic distance, of the invasion percolation cluster for d > 6, and show it differs from the IIC limit.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0086-A001). Method: Propose the candidate limit from the tree case and the ponds heuristic. Result: On the regular tree the invasion cluster's scaling limit (AGdHS) is a Poisson-type collection of critical trees hanging off a backbone with a slowly varying supercritical parameter, mutually singular to the IIC's Kesten tree. In d > 6 the natural candidate is the analogous 'SBM with an immortal particle and a time-varying branching rate' where the extra rate at intrinsic distance n comes from the level eps(n) of the current pond; the difference from C0077 is the drift term. Obstruction: Quantitative pond structure in high dimensions is missing. Verification level: unreviewed.

### C0087. Diameter of the minimal spanning tree on high-dimensional tori and the hypercube

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 16.3, p. 245.

Statement: Show that the diameter of the minimal spanning tree (with i.i.d. uniform edge weights) on the torus T_{n,d}, d > 6, and on the hypercube is of order V^{1/3}.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0087-A001). Method: Relate the MST diameter to the critical percolation window via the invasion/Kruskal coupling. Result: The MST is the union of invasion clusters; its diameter is governed by the largest clusters at the critical window level p = p_c(1 + O(V^{-1/3})), whose intrinsic diameter is of order (V^{2/3})^{1/2} = V^{1/3} in the mean-field regime (intrinsic diameter of a critical cluster of size m is m^{1/2}), plus the path lengths connecting the window clusters through slightly supercritical levels, each adding at most a comparable amount because above the window the largest cluster's intrinsic diameter is V^{1/3}/eps ... the source's conjecture V^{1/3} matches the complete-graph result of Addario-Berry-Broutin-Goldschmidt-Miermont where diam(MST) ~ n^{1/3}. Obstruction: Supercritical uniqueness on the torus (C0068) and intrinsic geometry of torus window clusters. Verification level: unreviewed.

### C0088. Scaling limit of the minimal spanning tree on high-dimensional tori

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 16.4, p. 245.

Statement: Show that the MST on T_{n,d}, d > 6, and on the hypercube, with distances rescaled by V^{-1/3}, converges in distribution to a multiple of the scaling limit of the MST on the complete graph.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0088-A001). Method: Reduce to the multiplicative-coalescent limit of the critical window plus the MST construction from the coalescent. Result: On the complete graph the MST limit is built from the scaling limit of the critical Erdos-Renyi components (as metric spaces) glued along the multiplicative coalescent; the same construction on the torus would follow from (i) C0071 upgraded to metric-space (Gromov-Hausdorff-Prokhorov) convergence of the window clusters, and (ii) the coalescent dynamics of the clusters as p increases through the window, i.e. that clusters merge at rate proportional to the product of their sizes, which is the mean-field merging rule and requires the merged clusters to be 'spread out' (same mechanism as in C0071: clusters wrap around the torus in d > 6 so their mutual boundary is proportional to the product of sizes). Obstruction: Metric-space convergence of window clusters and the product merging rule are unproved on the torus. Verification level: unreviewed.

### C0089. Quenched invariance principle for random walk on the vacant set of random interlacements in the whole supercritical phase

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 16.7, p. 248.

Statement: Prove a quenched invariance principle for simple random walk on the random interlacement set and on an infinite component of the vacant set of random interlacements.

Status: historical status source_says_open; current-literature status unverified. Status search found: Procaccia, Rosenthal and Sapozhnikov (PTRF 2016) proved a quenched invariance principle for random walk on the interlacement set for every u > 0 and on the vacant set for u small; combined with the 2023 sharpness result of Duminil-Copin, Goswami, Rodriguez, Severo and Teixeira (which gives the required decoupling and local uniqueness for all u < u*), the vacant-set case throughout the supercritical phase appears to follow, but this combination was not verified in a fetched source.

Our work (attempt C0089-A001). Method: Check the hypotheses of the Procaccia-Rosenthal-Sapozhnikov framework against the 2023 sharpness result. Result: PRS prove the QIP for correlated percolation models satisfying a decoupling condition with polynomial error, a local uniqueness condition and a density condition; for the vacant set these were verified for u < u** (strongly supercritical) at the time. The 2023 sharpness theorem establishes u* = u** = bar u, so the local uniqueness and decoupling inputs hold for every u < u*, and the PRS conclusion should extend verbatim. Obstruction: Exact matching of the hypotheses not verified against fetched texts. Verification level: unreviewed.

### C0090. Critical behaviour of scale-free percolation

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 16.8, p. 251.

Statement: For scale-free percolation with parameters alpha (long-range exponent) and tau (weight tail), determine when lambda -> theta(lambda) is continuous, identify the critical exponents, and determine the upper critical dimension as a function of alpha and tau.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0090-A001). Method: Locate the mean-field boundary by the two-point function variance criterion. Result: In scale-free percolation the connection probability between x and y with weights W_x, W_y is 1 - exp(-lambda W_x W_y |x-y|^{-alpha d}); with tau the weight tail exponent, the effective long-range exponent for the annealed two-point function is gamma = alpha(tau - 1); the annealed model behaves like long-range percolation with exponent gamma when gamma < ... and the upper critical dimension of long-range percolation with connection decay |x|^{-d-s} (s = gamma d - d... ) is d_c = 3 s for s < 2 (Heydenreich-van der Hofstad-Sakai), giving d_c = 3 (gamma - 1) d?? in terms of the source's parameters, i.e. mean-field behaviour when d > 3(alpha(tau - 1) - 1)... this needs care: long-range with P(x <-> y) ~ |x-y|^{-d-s}: mean-field for d > 3 min(s, 2). Obstruction: Quenched weight correlations are not captured by the long-range comparison. Verification level: unreviewed.

### C0091. Negative association for the random-cluster model with q < 1

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 16.9, p. 252.

Statement: Prove any form of negative association (e.g. negative correlation of edge occupations, or the stronger negative association of increasing functions on disjoint edge sets) for the FK random-cluster model with cluster weight q < 1.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0091-A001). Method: Test the weakest form, pairwise negative edge correlation, on small graphs exactly, and examine the q -> 0 limits. Result: At q -> 0 with p -> 0 appropriately the model becomes the uniform spanning tree, which is negatively associated (Feder-Mihail / Lyons determinantal), and at q = 1 the model is a product measure; the conjecture is that negative association holds for all 0 < q < 1, and even the pairwise statement Cov(omega_e, omega_f) <= 0 is open. On a single cycle of length n one can compute exactly: the random-cluster measure on the cycle with edge weight w = p/(1-p) gives the configurations 'all n edges' weight w^n q, 'n-1 edges' weight w^{n-1} q (n choices), and generally k edges missing (k >= 1) weight w^{n-k} q^k; two edges e, f are both open iff neither is among the missing ones; the covariance can be written in closed form and is <= 0 for q <= 1 by a direct check of the sign of a polynomial in w and q (the missing edges form a 'positive' k-dependent weight with q^k which is log-concave in k for q <= 1... ). Obstruction: Even pairwise negative correlation lacks a general argument; the Feder-Mihail route needs a matroid-like structure absent for q in (0,1). Verification level: unreviewed.

### C0092. Sharp phase transition for the random-cluster model with q < 1

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 16.10, p. 254.

Statement: For the FK model on Z^d with cluster weight q > 0, show that the threshold for finite susceptibility equals the threshold for percolation (sharpness), defining a single p_c(q).

Status: historical status source_says_open; current-literature status unverified. Status search found: For q >= 1 sharpness was proved by Duminil-Copin, Raoufi and Tassion ('Sharp phase transition for the random-cluster and Potts models via decision trees', Ann. of Math. 2019) using the OSSS inequality; the residual open case is q < 1, admitted here.

Our work (attempt C0092-A001). Method: Check what the OSSS route needs and whether it survives for q < 1. Result: The DRT proof uses (i) the FKG property of the random-cluster measure for q >= 1 (to make the model monotone so that the OSSS inequality applies to increasing events with the correct sign) and (ii) a differential inequality obtained from OSSS. For q < 1 the measure is expected to be negatively associated (C0091), the opposite of FKG, and the OSSS inequality's use of monotonicity fails: the covariance terms Cov(f, omega_e) can be of either sign. Obstruction: No monotonicity, hence no OSSS-type inequality, for q < 1. Verification level: unreviewed.

### C0093. Lace expansion for the random-cluster model with q not in {1,2}

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 16.11, p. 254.

Statement: Derive a lace expansion for FK percolation with cluster weight q not in {1, 2} and use it to prove an infrared bound for the Fourier transform of the critical Potts covariance.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0093-A001). Method: Identify what makes q = 1 and q = 2 expandable and whether a q-analogue of the random-current switching lemma exists. Result: q = 1 is Bernoulli percolation (independence gives the pivotal decomposition); q = 2 is expandable through the random-current representation and the switching lemma (Sakai's lace expansion for the Ising model). For integer q >= 3 the Potts model has a random-current-like representation (the 'random-current representation for Potts' via the Edwards-Sokal coupling with q colours) but the switching lemma fails because currents are Z_q-valued and the pairing structure that gives the switching identity is specific to Z_2. Obstruction: No switching lemma for Z_q currents; the natural expansion variable is a Tutte-polynomial quantity. Verification level: unreviewed.

### C0094. No infinite cluster at criticality on Z^d for all d >= 2 (duplicate record)

Source: Heydenreich and van der Hofstad: Progress in high-dimensional percolation and random graphs, author version with open problems (`heydenreich_hofstad_highd_2017`), Open Problem 1.1, p. 16.

Statement: Show theta(p_c) = 0 for percolation on Z^d, d >= 2.

Status: historical status source_says_open; current-literature status unverified. Status search found: Same mathematical content as C0023 (open for 3 <= d <= 10); recorded as an additional locator only, and NOT counted as a distinct problem because it shares the dedup key. This row shares dedup_key `theta_pc_zero_intermediate_dimensions` with C0023; counted once toward admitted_distinct_problems.

Our work (attempt C0094-A001). Method: See C0023. Result: Duplicate of C0023; the attempt is recorded there. Obstruction: see C0023 Verification level: unreviewed.

### C0095. Convergence of the holomorphic observable of the honeycomb self-avoiding walk to a conformal covariant

Source: Bauerschmidt, Duminil-Copin, Goodman, Slade: Lectures on self-avoiding walks, Clay 2012 (`bdgs_saw_lectures_2012`), Conjecture 3.6, p. 23.

Statement: For the critical honeycomb self-avoiding walk in a simply connected domain with marked boundary points a, b, the ratio F_delta(a_delta, z_delta)/F_delta(a_delta, b_delta) of the discrete holomorphic observable converges as delta -> 0 to (Phi'(z)/Phi'(b))^{5/8}, with Phi the conformal map to the upper half-plane sending a to infinity.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0095-A001). Method: Same structure as C0050: contour relations plus Morera give holomorphy of subsequential limits; identify the missing a priori bounds. Result: Smirnov's parafermionic observable for the honeycomb SAW at the critical weight satisfies the discrete contour relation (sum around each hexagon vanishes) but is not discretely holomorphic (only half the Cauchy-Riemann relations), the same deficit as for FK with q not 2. Any subsequential limit of the normalised observable that is tight and locally bounded is holomorphic by Morera (the contour relations pass to the limit) with boundary modulus determined by the spin 5/8 and the boundary conditions; the function (Phi')^{5/8} is the unique such function with the prescribed singularity at a and normalisation at b. Obstruction: No RSW-type crossing estimates for critical SAW; tightness of the observable ratio is not available. Verification level: unreviewed.

### C0096. Interfaces of the honeycomb O(n) loop model converge to SLE(kappa)

Source: Bauerschmidt, Duminil-Copin, Goodman, Slade: Lectures on self-avoiding walks, Clay 2012 (`bdgs_saw_lectures_2012`), Conjecture 3.7, p. 25.

Statement: For n in [0, 2] and x = 1/sqrt(2 + sqrt(2 - n)) the honeycomb O(n) loop-model interface converges to SLE(kappa) with kappa = 4 pi/(2 pi - arccos(-n/2)); for x above that value it converges to SLE(kappa) with kappa = 4 pi/arccos(-n/2). Known only for n = 1 at the critical point (site percolation, Smirnov) and for the n = 0 boundary in the trivial sense.

Status: historical status source_says_open; current-literature status unverified. Status search found: The n = 0 critical case is the SLE(8/3) conjecture for SAW (the source's Conjecture 1.5), which the Codex campaign already records as P0003 (hexagonal SAW scaling limit); this record covers n in (0,2] and the dense phase, and the n = 0 dense case (x above critical, kappa = 8).

Our work (attempt C0096-A001). Method: Check which n have any discrete holomorphic observable and which have crossing estimates. Result: Duminil-Copin-Smirnov's parafermionic observable exists for all n in [0,2] at the critical x with spin sigma = 1 - 3 arccos(-n/2)/(4 pi)... (the spin depends on n) and satisfies the contour relations; full holomorphicity holds for none except the Ising-related n = 1 dilute? (n = 1 corresponds to the Ising model's low-temperature expansion on the honeycomb, for which the observable is the Ising fermion and IS holomorphic - that is how Smirnov's Ising result and Chelkak-Smirnov work; on the honeycomb the n = 1 loop model at x_c is the critical Ising model, so the n = 1 case at the critical point IS known via Ising, contrary to the naive reading; the source's remark 'n = 1 site percolation' refers to the dense phase x = 1, kappa = 6). Obstruction: Holomorphicity fails for n not 1; crossing estimates unavailable for n < 1. Verification level: unreviewed.

### C0097. Divergence of the 1/d expansion of the connective constant

Source: Bauerschmidt, Duminil-Copin, Goodman, Slade: Lectures on self-avoiding walks, Clay 2012 (`bdgs_saw_lectures_2012`), Section 1.5, p. 4-5.

Statement: Prove that the asymptotic expansion of the connective constant mu(d) of Z^d in powers of 1/(2d) has radius of convergence zero (expected but unproved; coefficients known to order 11 grow rapidly).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0097-A001). Method: Combine the known factorial-type lower bound heuristics with Graham's Borel-type bounds. Result: The source cites Graham's Borel-type bounds on the remainder; if the coefficients a_i satisfy |a_i| >= c K^i i! for infinitely many i then the radius is zero, and the computed a_i (Clisby-Liang-Slade) grow consistently with factorial growth. A rigorous proof of divergence would follow from a lower bound on the number of lace diagrams contributing with the same sign at order i, i.e. a non-cancellation statement; the lace expansion for SAW has alternating-sign contributions (pi^{(N)} with sign (-1)^N) so cancellation cannot be excluded without an explicit asymptotic analysis of the diagram sums. Obstruction: Alternating-sign lace contributions may cancel; no asymptotic diagram count with sign control. Verification level: unreviewed.

### C0098. Decidability of infinite toppling for i.i.d. sandpiles on Z^2

Source: Levine and Peres: Laplacian growth, sandpiles and scaling limits, BAMS 2017, with open problems (`levine_peres_sandpiles_2017`), Open problems (1), p. 26.

Statement: For i.i.d. initial heights s(x) in {0,1,2,3,4} on Z^2 (with a given law), the event that every site topples infinitely often has probability 0 or 1; give an algorithm deciding which, as a function of the law.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0098-A001). Method: Reduce to the stabilisability threshold and examine the known bounds. Result: By Fey-Meester-Redig, an i.i.d. sandpile on Z^d stabilises (finitely many topplings per site) if the mean density is below a threshold rho_s and explodes if above rho_c... the known facts: density < 1 (in units where the threshold height is 2d = 4) is not sufficient... on Z^2 the results are: if E s < 2d - 1 = 3?? I recall: on Z^d, i.i.d. sandpiles with density rho < d stabilise? and with rho > 2d - 1 explode; the exact threshold for i.i.d. Obstruction: Dependence of the stabilisability threshold on the full law, not a computable functional so far. Verification level: unreviewed.

### C0099. Recurrence of the rotor-router walk on Z^2 with uniformly random initial rotors

Source: Levine and Peres: Laplacian growth, sandpiles and scaling limits, BAMS 2017, with open problems (`levine_peres_sandpiles_2017`), Open problems (2), p. 26.

Statement: Does the rotor-router walk on Z^2 with i.i.d. uniform initial rotor directions return to the origin with probability 1? The range after n steps is predicted to be of order n^{2/3}; even an o(n) upper bound on the range would imply recurrence.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0099-A001). Method: Try to prove the o(n) range bound via the excess-visits argument of Florescu-Levine-Peres in reverse. Result: FLP prove the range is at least of order n^{2/3} using the fact that a rotor walk that visits a site k times exits it in each direction about k/4 times, so the walk's displacement is controlled by the 'rotor field' which is a bounded perturbation of a divergence-free field; the upper bound o(n) would follow if the walk cannot be transient with positive density of new sites per step, i.e. if the visited set has a hole-filling property. Obstruction: No upper bound on the range of rotor walk on Z^2 better than n. Verification level: unreviewed.

### C0100. Convergence of height-fraction statistics in the sandpile scaling limit

Source: Levine and Peres: Laplacian growth, sandpiles and scaling limits, BAMS 2017, with open problems (`levine_peres_sandpiles_2017`), Open problems (3), p. 27.

Statement: Refine the Pegden-Smart weak-* convergence of the rescaled sandpile s_n by showing that for any ball B and integer j the fraction of sites in B with exactly j particles converges as the lattice spacing tends to zero; also determine the scaling limit of the sandpile identity element.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0100-A001). Method: Use the Apollonian structure of the limit to predict the local statistics in each patch. Result: The Pegden-Smart limit is a piecewise-quadratic function whose Hessian takes values in the set Gamma of integer superharmonic matrices; inside a patch where the Hessian is a fixed matrix A in Gamma, the sandpile is (Levine-Pegden-Smart) a periodic pattern determined by A, so the height-j fraction in a patch converges to the frequency of height j in that periodic pattern, which is a computable rational number. Obstruction: Transition-layer width between patches not confirmed; identity element limit open. Verification level: unreviewed.

### C0101. Maximal integer superharmonic matrices in dimensions d >= 3

Source: Levine and Peres: Laplacian growth, sandpiles and scaling limits, BAMS 2017, with open problems (`levine_peres_sandpiles_2017`), Open problems (4), p. 27.

Statement: Describe the maximal elements of the set Gamma(Z^d) of integer superharmonic matrices for d >= 3: are they isolated, and do they have rational entries? (In d = 2 they correspond to the circles of the Apollonian band packing and are rational.)

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0101-A001). Method: Test the d = 3 analogue of the Apollonian structure on the simplest candidates (diagonal matrices). Result: Gamma(Z^d) is the set of symmetric matrices A for which there is an integer-valued function on Z^d whose discrete Laplacian is at most the constant ... with quadratic growth A: g(x) = (1/2) x^T A x + (lower order) integer-valued superharmonic. Diagonal A = diag(a_1,...,a_d): g(x) = sum_i (1/2) a_i x_i^2 rounded is integer-valued; the discrete Laplacian of x -> ceil(a x^2 / 2) in one dimension is at most a + 1 ... in one dimension the maximal a with an integer superharmonic quadratic of curvature a is determined by the 1D odometer; for diagonal matrices the problem separates into d one-dimensional problems and the maximal diagonal elements are rational (the 1D maximal curvatures are rational, e.g. the 1D sandpile has only finitely many patterns). Obstruction: No d = 3 analogue of the LPS correspondence between Gamma(Z^d) and packings. Verification level: unreviewed.

### C0102. Fyodorov-Hiary-Keating: subleading order of the maximum of the Riemann zeta function on short intervals

Source: Arguin: Extrema of log-correlated random variables, principles and examples (`arguin_logcorrelated_2016`), Conjecture 2, p. 24.

Statement: For tau uniform on [0,T], (max_{h in [0,1]} log|zeta(1/2 + i(tau + h))| - log log T)/log log log T converges in probability to -3/4.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Arguin, Belius, Bourgade, Radziwill and Soundararajan (CPAM 2019) proved the leading order; Arguin, Bourgade and Radziwill, 'The Fyodorov-Hiary-Keating conjecture. I' (2020) and 'II' (2023) proved the subleading -3/4 log log log T order with tightness. Resolved by: Arguin-Bourgade-Radziwill 2020/2023

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0103. Limiting distribution of the fluctuations of the maximum of zeta on short intervals

Source: Arguin: Extrema of log-correlated random variables, principles and examples (`arguin_logcorrelated_2016`), Conjecture 2 and following remark, p. 24.

Statement: Identify the limit law of max_{h in [0,1]} log|zeta(1/2 + i(tau + h))| - log log T + (3/4) log log log T as T -> infinity (Fyodorov-Hiary-Keating predict a specific distribution: a Gumbel convolved with the law of the log of a critical multiplicative chaos total mass, i.e. the same form as for log-correlated Gaussian fields).

Status: historical status source_says_open; current-literature status unverified. Status search found: Tightness of the centred maximum is proved (ABR II, 2023); the convergence in law and identification of the limit were not found resolved in a bounded search.

Our work (attempt C0103-A001). Method: Transfer the branching-random-walk identification of the limit to the random model of zeta, and locate the arithmetic obstruction. Result: For the random Euler-product model (45) of the source, the maximum over h in [0,1] is a maximum of a log-correlated non-Gaussian field with the multiscale structure (47)-(50), and the general theory (Arguin's Section 3, and the DRZ-type universality for the maximum) gives convergence of the centred maximum to a randomly shifted Gumbel whose shift is the log of the total mass of the critical multiplicative chaos of the field, provided (i) the increments have exponential moments with the right Gaussian-like rate (true for the random model), and (ii) a second-moment computation at the level of the critical chaos with the derivative-martingale normalisation. Obstruction: Fine-scale dependence of the prime sums prevents the local limit theorem needed to identify the cluster structure. Verification level: unreviewed.

### C0104. Fyodorov-Hiary-Keating for the characteristic polynomial of CUE: subleading order and limit law

Source: Arguin: Extrema of log-correlated random variables, principles and examples (`arguin_logcorrelated_2016`), Conjecture 1, Section 4 (p. 22-23).

Statement: For the characteristic polynomial P_N of an N x N Haar unitary matrix, max over the unit circle of log|P_N| equals log N - (3/4) log log N + O(1) with a specific limiting fluctuation law.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: The -3/4 log log N order was established through Arguin-Belius-Bourgade (2017, leading order), Paquette-Zeitouni (2018, subleading upper/lower bounds) and Chhaibi-Madaule-Najnudel (2018); convergence in law of the centred maximum was proved by Paquette and Zeitouni, 'The extremal landscape for the CbetaE ensemble' (2022/2024). Resolved by: Paquette-Zeitouni 2022 (extremal landscape for CbetaE), building on ABB 2017, PZ 2018, CMN 2018

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0105. Multiscale decomposition of the actual zeta function with self-similar increments

Source: Arguin: Extrema of log-correlated random variables, principles and examples (`arguin_logcorrelated_2016`), Section 4.1 discussion, p. 25-26.

Statement: Exhibit a rigorous multiscale (branching-random-walk-like) decomposition of log|zeta(1/2+i(tau+h))|, h in [0,1], whose increments are self-similar with the dichotomy (50) and asymptotically independent, sufficient to run the branching-random-walk machinery on zeta itself rather than on the random Euler-product model.

Status: historical status source_says_open; current-literature status unverified. Status search found: The ABR papers realised a version of this decomposition sufficient for the subleading order (C0102); whether a decomposition with the full self-similar independent structure exists as stated is not a theorem as far as this session could determine; admitted as the structural question the source poses.

Our work (attempt C0105-A001). Method: Analyse the covariance of the dyadic prime-block increments and the failure of independence. Result: The increments Y_h(l) = sum over primes with log p in (2^{l-1}, 2^l] of Re(p^{-i(tau+h)}) p^{-1/2} have, for tau uniform on [0,T], exact joint moments given by counting solutions of multiplicative equations among primes (Montgomery-Vaughan), so their joint law is asymptotically that of independent uniform phases as long as the number of primes involved is o(log T / log log T) in the moment order; this gives asymptotic independence of any FIXED number of increments at fixed moment order, but the branching-random-walk machinery needs exponential moments of sums of all n = log log T increments simultaneously, i.e. moments of order growing with n, where the multiplicative counting develops correlations from products of primes exceeding T. Obstruction: High-moment dependence of the last blocks. Verification level: unreviewed.

### C0106. Bolthausen-Sznitman genealogy of the Brunet-Derrida N-particle branching Brownian motion

Source: Berestycki: Recent progress in coalescent theory, Ensaios Matematicos 2009, with open problems (`berestycki_coalescents_2009`), Conjecture 6.1, p. 178.

Statement: The ancestral partition process of the N-particle branching Brownian motion with selection (Brunet-Derrida model), sped up by (log N)^3, converges to the Bolthausen-Sznitman coalescent.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Berestycki, Berestycki and Schweinsberg (Ann. Probab. Resolved by: Schweinsberg 2017 (EJP); Berestycki-Berestycki-Schweinsberg 2013

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0107. Bounded ratios in arm probabilities of critical percolation on the triangular lattice

Source: Werner: Lectures on two-dimensional critical percolation, PCMI 2007 (`werner_2d_percolation_2007`), Section 5 remark, p. 63.

Statement: Show that pi_j(j,n) n^{a_j} is bounded above and below as n -> infinity for the j-arm events of critical site percolation on the triangular lattice (SLE gives only the exponents).

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Same content as C0019: resolved by Du, Gao, Li and Zhuang (arXiv 2205.15901) with sharp asymptotics; the campaign holds that source as sharp_arms_2022. Resolved by: sharp_arms_2022

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0108. Optimal quadratic Littlewood-Offord bound

Source: Tao and Vu: From the Littlewood-Offord problem to the circular law, survey with open questions (`tao_vu_littlewood_offord_2009`), Section 6, p. 21.

Statement: For a quadratic form Q = sum c_ij xi_i xi_j with all coefficients nonzero and xi_i i.i.d. Bernoulli, prove sup_z P(Q = z) = O(n^{-1/2}); more generally determine the optimal anti-concentration exponent for degree-k polynomials.

Status: historical status source_says_open; current-literature status unverified. Status search found: Costello (2013) obtained n^{-1/2+o(1)} for quadratic forms; Meka, Nguyen and Vu (2016) obtained n^{-1/2} up to logarithmic factors for general degree under a rank condition. Whether the exact O(n^{-1/2}) without logarithms is established was not confirmed in this session.

Our work (attempt C0108-A001). Method: Decoupling plus the linear Littlewood-Offord bound, to see where the logarithm enters. Result: Decoupling Q by splitting the index set into two halves I, J gives P(Q = z) <= P(|sum_{i in I, j in J} c_ij xi_i xi'_j - ...| small)^{1/2}-type bounds where, conditionally on the J-variables, the bilinear form is a linear form in the I-variables with coefficients a_i = sum_j c_ij xi_j; the linear Littlewood-Offord (Erdos) bound gives P <= C/sqrt(number of nonzero a_i), and the a_i are nonzero with high probability except on an event where many coefficient sums vanish, whose probability is itself controlled by a Littlewood-Offord bound on the rows; the loss comes from the union over rows and the conditioning, which is where the n^{o(1)} or logarithmic factors enter in the known proofs. Obstruction: The known inverse Littlewood-Offord theorems carry logarithmic losses. Verification level: unreviewed.

### C0109. Rate of convergence in the circular law as a function of the moment assumption

Source: Tao and Vu: From the Littlewood-Offord problem to the circular law, survey with open questions (`tao_vu_littlewood_offord_2009`), Section 6, p. 22.

Statement: Determine the optimal rate n^{-delta} of convergence of the empirical spectral distribution of n^{-1/2} M_n to the circular law under a (2+eps)-th moment assumption, and the exact dependence of delta on eps.

Status: historical status source_says_open; current-literature status unverified. Status search found: Rate results: Gotze-Tikhomirov, and Jalowy (2021) obtained near-optimal rates for Ginibre and for i.i.d. matrices with sufficiently many moments; the exact eps -> delta dependence at the (2+eps) level was not found in this session.

Our work (attempt C0109-A001). Method: Locate the rate bottleneck in the Hermitisation argument. Result: The Hermitisation proof controls the log-potential U_n(z) = (1/n) log|det(n^{-1/2}M_n - z)| through the singular-value distribution of the shifted matrix; the error has three parts: (a) the rate in the Marchenko-Pastur-type convergence of the singular-value distribution, of order n^{-1/2}-ish under four moments and degrading to n^{-c(eps)} under 2+eps moments through the truncation at level n^{1/(2+eps)}; (b) the smallest singular value lower bound, which contributes only a log-factor to the log-potential error; (c) the conversion from log-potential convergence to weak convergence of the ESD, which costs a power through the smoothing of the Laplacian. Obstruction: Sharp conversion constant from log-potential to Kolmogorov distance. Verification level: unreviewed.

### C0110. Central limit theorem for the log-determinant of i.i.d. non-Gaussian matrices

Source: Tao and Vu: From the Littlewood-Offord problem to the circular law, survey with open questions (`tao_vu_littlewood_offord_2009`), Section 6, p. 22-23.

Statement: Prove that log|det M_n| satisfies a central limit theorem for i.i.d. entries beyond the Gaussian case (Girko's claim, unverified by the authors).

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Nguyen and Vu, 'Random matrices: law of the determinant', Ann. Probab. Resolved by: Nguyen-Vu 2014

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0111. Parisi's exact formula for the expected random assignment cost

Source: Aldous and Steele: The objective method, probabilistic combinatorial optimization and local weak convergence, 2004, with open problems (`aldous_steele_objective_2004`), Section 1, equation (1.2), p. 3-4.

Statement: For the n x n random assignment problem with i.i.d. exponential(1) costs, E[A_n] = sum_{k=1}^n k^{-2}.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Proved independently by Linusson and Wastlund (PTRF 2004) and by Nair, Prabhakar and Sharma (Random Structures Algorithms 2005); this also settles the monotonicity of E[A_n] mentioned on p. 3 of the source. Resolved by: Linusson-Wastlund 2004; Nair-Prabhakar-Sharma 2005

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0112. Variance asymptotics of the random assignment cost

Source: Aldous and Steele: The objective method, probabilistic combinatorial optimization and local weak convergence, 2004, with open problems (`aldous_steele_objective_2004`), Section 5, equation (5.30), p. 56.

Statement: There is sigma^2 > 0 with Var(A_n) ~ sigma^2/n for the random assignment problem with exponential costs.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Wastlund, 'The variance and higher moments in the random assignment problem' (2005), established Var(A_n) ~ (4 zeta(2) - 4 zeta(3))/n. Bounded recall. Resolved by: Wastlund 2005

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0113. Is the minimal spanning forest of a Poisson process in R^d a single tree for d >= 3?

Source: Aldous and Steele: The objective method, probabilistic combinatorial optimization and local weak convergence, 2004, with open problems (`aldous_steele_objective_2004`), Section 6, p. 63-64.

Statement: For the minimal spanning forest of a homogeneous Poisson point process in R^d, decide whether it is almost surely connected (a single tree); known true for d = 2 (Alexander), conjectured false for d large.

Status: historical status source_says_open; current-literature status unverified. Status search found: Lyons, Peres and Schramm ('Minimal spanning forests', Ann. Probab.

Our work (attempt C0113-A001). Method: Relate connectivity of the MSF to critical percolation of the Boolean/Gilbert model and to the number of infinite clusters at criticality. Result: By the Lyons-Peres-Schramm correspondence, the (free) MSF of an invariant point process is a single tree iff, in the associated continuum percolation (Gilbert graph with radius r), there is a.s. no infinite cluster at the critical radius r_c... more precisely the MSF is connected iff for every r there are no two infinite clusters of the r-graph that... their criterion (for Z^d bond percolation) is: the free MSF has one tree iff theta(p_c) = 0 and there is a unique infinite cluster for all p > p_c, under the additional condition that critical percolation has no infinite cluster in the 'invaded' sense; for Z^d they show the free MSF is a tree if theta(p_c) = 0 and every p > p_c has a unique infinite cluster (which holds), so on Z^d the MSF is a single tree iff theta(p_c) = 0. Obstruction: Transfer of the LPS criterion to Poisson processes and the exact statement of the high-d continuum result not verified from fetched sources. Verification level: unreviewed.

### C0114. Limit of the independence number of random regular graphs

Source: Aldous and Steele: The objective method, probabilistic combinatorial optimization and local weak convergence, 2004, with open problems (`aldous_steele_objective_2004`), Section 7, equation (7.1), p. 67.

Statement: For the uniform random k-regular graph G_{k,n}, prove that n^{-1} E[alpha(G_{k,n})] converges to a constant alpha_k, and identify alpha_k.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Existence of the limit: Bayati, Gamarnik and Tetali (Ann. Probab. Resolved by: Bayati-Gamarnik-Tetali 2013; Ding-Sly-Sun 2016

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0115. Convexity of the Parisi functional

Source: Panchenko: The Sherrington-Kirkpatrick model, an overview, J. Stat. Phys. 2012, with open problems (`panchenko_sk_overview_2012`), Section 7 remark, p. 22.

Statement: The Parisi functional P(zeta) is convex in the functional order parameter zeta, implying uniqueness of the minimiser in the Parisi formula.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Auffinger and Chen, 'The Parisi formula has a unique minimizer', Comm. Math. Resolved by: Auffinger-Chen 2015

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0116. Deterministic (1+epsilon)-approximation of the cover time

Source: Ding, Lee, Peres: Cover times, blanket times and majorizing measures, Ann. Math. 2012, with open questions (`ding_lee_peres_cover_2012`), Question 5.1, p. 51.

Statement: Is there, for every epsilon > 0, a deterministic polynomial-time algorithm approximating the cover time t_cov(G) of a graph within a factor 1 + epsilon? (Known for trees by Feige-Zeitouni; constant-factor approximation by Ding-Lee-Peres.)

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0116-A001). Method: Examine whether the Gaussian free field characterisation can be made asymptotically exact. Result: DLP show t_cov ~ |E| (E max GFF)^2; the later result of Ding (2012, 'Asymptotics of cover times via Gaussian free fields: bounded-degree graphs and general trees') gives asymptotic equality t_cov ~ |E| (E max eta)^2 for bounded-degree graphs when t_cov/t_hit -> infinity, and Zhai (2018) proved the asymptotic formula for general graphs under the same condition. Given the asymptotic formula, a (1+eps) approximation of t_cov reduces to a (1+eps) approximation of E max of a Gaussian vector with given covariance (the Green function), which is a deterministic computational problem: computing E max of a Gaussian vector to within 1+eps is not known to be in deterministic polynomial time in general (the majorizing-measure/generic-chaining bounds are only within constants; exact computation of Gaussian maxima expectations is #P-hard in some formulations). Obstruction: No deterministic (1+eps) algorithm for Gaussian expected maxima with general covariance. Verification level: unreviewed.

### C0117. Concentration of the cover time at the scale of the maximal hitting time

Source: Ding, Lee, Peres: Cover times, blanket times and majorizing measures, Ann. Math. 2012, with open questions (`ding_lee_peres_cover_2012`), Question 5.2, p. 51.

Statement: Is the standard deviation of the cover time tau_cov bounded by the maximal hitting time t_hit for every graph, and does (tau_cov - t_cov)/t_hit have an exponentially decaying tail with a universal rate?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0117-A001). Method: Test the claim on the extreme families and derive the one-sided bound from Matthews-type arguments. Result: Upper tail: for any graph, P(tau_cov > t_cov + s t_hit) <= e^{-cs}? The standard argument: after time 2 t_hit... using the Markov property at multiples of the 'maximal hitting time' scale, the probability that a fixed uncovered vertex remains uncovered for another 2 t_hit is at most 1/2 by Markov's inequality on hitting times, but the union over uncovered vertices costs the number of uncovered vertices, so the naive bound gives only P(tau_cov > t_cov + s t_hit) <= n 2^{-s}, i.e. exponential decay after a log n shift, not at scale t_hit from the mean unless t_cov - t_cov... Obstruction: Tightness of the GFF maximum on general graphs is not known. Verification level: unreviewed.

### C0118. Disorder chaos in the Sherrington-Kirkpatrick model

Source: Chatterjee: Chaos, concentration and multiple valleys, 2008, with open questions (`chatterjee_chaos_2008`), Section 12, problem (1), p. 59.

Statement: Prove chaos (in the sense of the source: decorrelation of the Gibbs measure under a small perturbation of the disorder) in the original SK model with xi(x) = x^2.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Chatterjee, 'Disorder chaos and multiple valleys in spin glasses' (2009, arXiv 0907.3381), proved disorder chaos for the SK model at all temperatures; Chen (2013, Ann. Probab.) established it for mixed even p-spin models. Resolved by: Chatterjee 2009; Chen 2013

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0119. Chaos in directed polymers in dimensions d >= 3

Source: Chatterjee: Chaos, concentration and multiple valleys, 2008, with open questions (`chatterjee_chaos_2008`), Section 12, problem (2), p. 59.

Statement: Prove chaos (sensitivity of the polymer measure to a small perturbation of the environment) for directed polymers in random environment in dimensions d >= 3, at low temperature.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0119-A001). Method: Check which steps of the d = 2 proof are dimension-dependent. Result: The source's d = 1+1 proof establishes superconcentration of the free energy (variance o(n)) via hypercontractivity and then chaos from superconcentration through the general equivalence theorem; the dimension-dependent step is the variance bound Var(log Z_n) = O(n/log n), obtained from the Benjamini-Kalai-Schramm influence inequality applied to the free energy with the influence of a single site bounded by the expected overlap of two polymers at that site, whose sum over sites is the expected overlap, of order n in the strong disorder regime. Obstruction: Quantitative (order n) path overlap in the strong disorder phase for d >= 3. Verification level: unreviewed.

### C0120. Fluctuation exponent of directed polymers beyond the logarithmic improvement

Source: Chatterjee: Chaos, concentration and multiple valleys, 2008, with open questions (`chatterjee_chaos_2008`), Section 12, problem (3), p. 59.

Statement: Improve the bound Var(log Z_n) = O(n/log n) for directed polymers in random environment in general dimension to a power improvement n^{1-eps}.

Status: historical status source_says_open; current-literature status unverified. Status search found: In d = 1+1 with exactly solvable weights (log-gamma, exponential last-passage) the exponent 2/3 (variance n^{2/3}) is a theorem; for general weights in any dimension the BKS-type n/log n remains the best general bound to this session's knowledge; cf. the FPP variance problem in the Codex campaign (P-a/ chi = 1/3 target).

Our work (attempt C0120-A001). Method: Same block as the first-passage percolation sublinear variance problem; record the exact reduction. Result: The n/log n bound is the BKS entropy method; a power improvement n^{1-eps} would follow from a chaos exponent: if the polymer measure decorrelates under a noise of size n^{-eps'} on the environment (superconcentration with a rate), Talagrand's/Chatterjee's equivalence gives Var(log Z_n) <= n^{1-eps}. Conversely, the variance exponent is tied to the transversal fluctuation exponent by the KPZ scaling relation chi = 2 xi - 1 (Chatterjee 2013 proved the relation rigorously for FPP under existence of the exponents), so a power improvement needs a quantitative transversal-fluctuation bound xi < 1 with an explicit gap, which is known only in the exactly solvable models. Obstruction: Quantitative chaos rate or transversal fluctuation bound unavailable outside integrable models. Verification level: unreviewed.

### C0121. Tightness of the maximum of the discrete Gaussian free field

Source: Chatterjee: Chaos, concentration and multiple valleys, 2008, with open questions (`chatterjee_chaos_2008`), Section 12, problem (4), p. 59.

Statement: Improve the variance bound O(log log n) for the maximum of the two-dimensional DGFF on the torus and on the box with zero boundary condition; is the variance O(1)?

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Bramson and Zeitouni (CPAM 2012) proved tightness of the centred DGFF maximum with zero boundary conditions, and Bramson, Ding and Zeitouni (CPAM 2016) proved convergence in law; tightness implies O(1) variance. Bounded recall. Resolved by: Bramson-Zeitouni 2012; Bramson-Ding-Zeitouni 2016

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0122. Chaos implies multiple peaks without nonnegative correlations

Source: Chatterjee: Chaos, concentration and multiple valleys, 2008, with open questions (`chatterjee_chaos_2008`), Section 12, problem (5), p. 59.

Statement: Show that chaos implies the multiple-peaks property for Gaussian fields whose correlations are not all nonnegative, which requires a second-moment bound on the overlap R(I_0, I_t) between the maximiser at time 0 and at time t.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0122-A001). Method: Attempt the second-moment bound on the overlap via Gaussian interpolation. Result: In the nonnegatively correlated case the source bounds E[R(I_0,I_t)^2] using FKG-type positivity; in general the overlap between the argmax at time 0 and at time t is a function of the field and its noised copy, and its second moment can be written through the Ornstein-Uhlenbeck semigroup: E[R(I_0,I_t)^2] = E[R(I_0,I_t)] + Var-type terms involving four copies of the field (two pairs). The needed inequality is E[R^2] <= C (E R)^2 + o(1), a 'concentration of the overlap' statement; without positivity one can attempt Gaussian interpolation between the four-copy system and an independent system, whose derivative is a sum of covariance terms of mixed sign, which is exactly where positivity was used. Obstruction: Second moment of the overlap without positive correlations. Verification level: unreviewed.

### C0123. Bridges between multiple peaks in the NK fitness landscape

Source: Chatterjee: Chaos, concentration and multiple valleys, 2008, with open questions (`chatterjee_chaos_2008`), Section 12, problem (8), p. 59.

Statement: In the Kauffman-Levin NK fitness model with multiple near-maximal peaks, decide whether the peaks are connected by 'bridges' (paths along which the fitness never drops below the near-maximal level) or are isolated islands.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0123-A001). Method: Estimate the number of near-maximal configurations and compare with the connectivity threshold of the level set on the hypercube. Result: In the NK model with K = O(1) the fitness is a sum of n local terms each depending on K + 1 bits, so the field is a sum of n independent contributions (for the standard model with random neighbourhoods) and the level set at height M_n - delta_n with delta_n = o(n) but delta_n >> sqrt n contains exp(c delta_n^2/n)... the number of configurations within delta of the maximum is, by a large-deviation count, about exp(n I(delta/n)) for a rate I; bridges exist if this level set percolates on the hypercube, and a level set of density rho on the n-cube contains a giant connected component when the local structure allows, roughly when each configuration in the set has on average more than one neighbour in the set: the expected number of neighbours in the level set of a typical level-set point is n times the conditional probability that flipping one bit stays within delta of the maximum, which is n times (probability that the change of the K+1 affected local terms is at most delta), of order n delta/n = delta when delta is small compared to the local term scale... so bridges exist (heuristically) when delta_n >> 1, i.e. the level set within a constant deficit of the maximum is connected in the giant-component sense for deficits growing to infinity, while for bounded deficits the peaks are isolated. Obstruction: Second moment for level-set paths on the hypercube not done. Verification level: unreviewed.

### C0124. Stability of the elliptic Harnack inequality under rough isometries

Source: Kumagai: Random walks on disordered media and their scaling limits, Saint-Flour XL 2010, author version (`kumagai_stflour_2014`), Section 1.1 remark, p. 9.

Statement: Is the elliptic Harnack inequality for weighted graphs stable under bounded perturbations of the weights and under rough isometries?

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Barlow and Murugan, 'Stability of the elliptic Harnack inequality', Ann. of Math. 187 (2018), proved stability under bounded perturbation and rough isometry. Resolved by: Barlow-Murugan 2018

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0125. Spectral dimension of random walk on the incipient infinite cluster below the critical dimension

Source: Kumagai: Random walks on disordered media and their scaling limits, Saint-Flour XL 2010, author version (`kumagai_stflour_2014`), Section 4.2 and 6.4, p. 42 and 58-59.

Statement: For critical percolation on Z^d with 2 <= d < 6, determine the spectral dimension d_s of random walk on the incipient infinite cluster; the Alexander-Orbach value 4/3 is believed to fail (numerics: d_s = 1.318 in d = 2), and for 3 <= d < 6 even the existence of the IIC is unproved.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0125-A001). Method: Derive d_s in d = 2 from known exponents via the Einstein relation and locate what is rigorous. Result: On the IIC of two-dimensional critical percolation (which exists, Kesten) the walk is subdiffusive with d_s = 2 d_f/d_w where d_f = 91/48 is the fractal dimension of the IIC and d_w is the walk dimension; the Einstein relation d_w = d_f + zeta with zeta the resistance exponent gives d_s = 2 d_f/(d_f + zeta), and the conjectured resistance exponent of the 2D IIC is zeta ~ 0.98 (numerically the backbone resistance exponent), giving d_s = 2 x 1.896/(1.896 + 0.98) = 1.318, matching the numerics quoted by the source; the rigorous status: Kesten proved subdiffusivity with d_w > 2, and the resistance exponent is only known to lie in an interval (zeta > 0 from Kesten; zeta <= something from the one-arm/backbone dimension). Obstruction: Resistance exponent of the 2D IIC unknown; IIC existence unproved for 3 <= d < 6. Verification level: unreviewed.

### C0126. Random walk on the incipient infinite cluster of oriented percolation in dimensions 5 and 6

Source: Kumagai: Random walks on disordered media and their scaling limits, Saint-Flour XL 2010, author version (`kumagai_stflour_2014`), Section 6.3 open problem, p. 58.

Statement: The critical dimension of oriented percolation is 4; describe the behaviour of simple random walk on the IIC of oriented percolation (Z^d x Z_+) for d = 5 and 6, where the mean-field heat-kernel proof (which needs d > 6) does not apply.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0126-A001). Method: Identify which estimate needs d > 6 and whether it is an artefact. Result: The source's proof of the Alexander-Orbach behaviour for the oriented IIC uses a zigzag-path count converging like sum_m m^{(4-d)/2}, which needs d > 6, while the oriented IIC's mean-field structure (Hofstad-den Hollander-Slade) holds for d > 4. The zigzag count controls the resistance between the origin and level n via the number of paths that go up, come back down and go up again; in d = 5, 6 these counts diverge, meaning the crude flow bound fails, but the true resistance may still be of order n (mean-field, tree-like) because the divergent terms are overcounting: paths in the oriented IIC cannot return to earlier times, so a zigzag in the bound corresponds to two disjoint upward paths connected through the IIC's backbone, whose number is controlled by the two-point function squared, giving a convergent sum for d > 4 if the backbone is used correctly. Obstruction: The improved flow construction is not carried out. Verification level: unreviewed.

### C0127. Chaos versus superconcentration: an equivalent multiple-peaks condition

Source: Chatterjee: Chaos, concentration and multiple valleys, 2008, with open questions (`chatterjee_chaos_2008`), Section 12, problem (6), p. 59.

Statement: Find a multiple-peaks condition on a Gaussian field that is equivalent to chaos and superconcentration, or show that no such condition exists.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0127-A001). Method: Test candidate conditions on the two extreme examples (i.i.d. field and the DGFF). Result: Superconcentration of the maximum M = max_i X_i of a Gaussian field is Var(M) = o(max variance), and chaos is the decorrelation of the argmax under noise. A natural candidate equivalent condition is 'the near-maximal set at deficit delta = C sqrt(Var M)... has at least two points with overlap bounded away from 1 with probability tending to 1'; I checked it on the i.i.d. field (superconcentrated, chaotic, and the near-maximal set at deficit of order 1/sqrt(log n) has many points with zero overlap: condition holds) and on a field with a single dominant direction X_i = Z + small noise (not superconcentrated, not chaotic, near-maximal set at any deficit consists of points all with overlap near 1: condition fails), and on the 2D DGFF (superconcentrated and chaotic per the source; the near-maximal set at O(1) deficit has multiple clusters at macroscopic distance with overlap = covariance ratio bounded away from 1: condition holds). Obstruction: Growing-number version neither proved nor refuted. Independent check: Argmax is determined by sign(Z_1 - Z_2) up to the small noise, stable under noise of size smaller than |Z_1 - Z_2|; Var(max) = Var(max(Z_1,Z_2)) is order 1. Verification level: unreviewed.

### C0128. One-sided zero-one laws for one-dimensional excited random walks

Source: Kosygina and Zerner: Excited random walks, results, methods, open problems, 2012 (`kosygina_zerner_erw_2012`), Problem 3.5, p. 11.

Statement: For excited random walks on Z, find conditions on the cookie environment under which P_0(sup X_n = +infinity), P_0(inf X_n = -infinity) and the events {X_n -> +infinity}, {X_n -> -infinity} have probability 0 or 1 (beyond the two sufficient sets of conditions in Theorem 3.10).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0128-A001). Method: Check whether the ergodic-environment argument for the two-sided statement (Theorem 2.3/3.2) localises to one side. Result: The two-sided 0-1 law (range infinite or not) follows from stationarity of the environment plus a Borel-Cantelli over the sites visited; the one-sided event {sup X_n = infinity} is not invariant under the natural shifts because the walk started at 0 and the environment to the left matter. Under (SE) and (EL) the source notes (3.4) and (3.5) are equivalent, so the question is the 0-1 property itself. Obstruction: Left environment influences right excursions; no shift invariance of the one-sided event. Verification level: unreviewed.

### C0129. Recurrence-transience criterion for excited random walks under stationary ergodic environments

Source: Kosygina and Zerner: Excited random walks, results, methods, open problems, 2012 (`kosygina_zerner_erw_2012`), Problem 3.11, p. 13.

Statement: Can the assumption (IID) in the recurrence/transience criterion (3.10) of Theorem 3.10 (recurrent iff |delta| <= 1 for bounded cookie stacks) be replaced by stationarity and ergodicity (SE)?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0129-A001). Method: Examine the branching-process-with-migration proof and where i.i.d. is used. Result: The proof of Theorem 3.10 under (3.10) translates the walk into a branching process with migration whose offspring law at site k is determined by the cookie stack at k; under (IID) the branching process is homogeneous in space and the criterion delta > 1 is the criterion for the branching process to die out... under (SE) the process is a branching process in a stationary ergodic environment (BPRE with migration), whose survival criterion is governed by the Lyapunov exponent of the environment, i.e. by an ergodic average of log-means, not by the mean delta of the drift. Obstruction: Ergodic total-progeny theorem for branching processes with migration in stationary environments. Verification level: unreviewed.

### C0130. Escape probability of a transient one-dimensional excited random walk

Source: Kosygina and Zerner: Excited random walks, results, methods, open problems, 2012 (`kosygina_zerner_erw_2012`), Problem 3.12, p. 13.

Statement: Compute, for a transient excited random walk on Z, the probability P_0(X_n not 0 for all n >= 1) of never returning to the starting point.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0130-A001). Method: Express the escape probability through the branching-process representation for the one-cookie deterministic case. Result: In the deterministic environment with one cookie of strength p at each site (M = 1, delta = 2p - 1... transient iff delta > 1 which needs more than one cookie; take M = 2 cookies of strength p each, delta = 2(2p - 1) > 1 iff p > 3/4). The event of never returning to 0 after the first step: the walk must never come back, which in the branching-process picture (right excursions counted by the number of down-crossings of each edge) means the branching process with migration started from the edge (0,1) never produces a down-crossing of (0,1) into 0... the escape probability equals the probability that the total number of down-crossings of the edge (0,1) is zero, which is P(the branching process with migration started at 1 individual at level 1 has zero descendants at level 0) - not directly a standard extinction probability but a hitting probability of the time-reversed process. Obstruction: No closed form beyond special cases; the reduction gives a numerical procedure only. Verification level: unreviewed.

### C0131. Recurrence-transience dichotomy for excited random walks in dimension d >= 2

Source: Kosygina and Zerner: Excited random walks, results, methods, open problems, 2012 (`kosygina_zerner_erw_2012`), Problem 3.21, p. 16.

Statement: For excited random walks on Z^d, d >= 2, with i.i.d. uniformly elliptic cookie environments, is the walk either recurrent (visits every site infinitely often... in the source's Definition 3.1 sense) or transient?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0131-A001). Method: Compare with the RWRE 0-1 law in d >= 3 (C0044) and locate the extra difficulty from self-interaction. Result: For Markovian RWRE the dichotomy question is the directional 0-1 law (C0044, open in d >= 3). For excited random walks the process is not Markov, and even the statement 'either recurrent or transient' (return to the origin infinitely often a.s. or finitely often a.s.) is not implied by any Markov-chain dichotomy; the source's Definition 3.1 asks for a 0-1 law for the number of returns. Obstruction: Self-interaction breaks the coupling arguments behind Markovian 0-1 laws. Verification level: unreviewed.

### C0132. Transience and recurrence of the M(d1,d2) balanced excited random walks

Source: Kosygina and Zerner: Excited random walks, results, methods, open problems, 2012 (`kosygina_zerner_erw_2012`), Remark and Problem 3.22, p. 16-17.

Statement: For the M(d1,d2) walk on Z^{d1+d2} (simple random walk step in the first d1 coordinates on the first visit to a vertex, in the last d2 coordinates on later visits), prove that M(1,2) and M(2,1) are transient and that M(1,1) is recurrent (M(2,2) is known transient).

Status: historical status source_says_open; current-literature status unverified. Status search found: Peres, Popov and Sousi (2013) and Peres, Schapira and Sousi (2016) proved transience results for several balanced excited walks in three dimensions; whether M(1,2), M(2,1) and the recurrence of M(1,1) were fully settled was not confirmed in this session.

Our work (attempt C0132-A001). Method: Analyse M(1,1) on Z^2 through the range of the first-coordinate walk. Result: In M(1,1) the first coordinate moves only at first visits and the second at later visits; the set of visited vertices is the range, and the first-coordinate process is a simple random walk on Z run at the rate of new visits. Recurrence of M(1,1) would follow if the walk returns to the origin infinitely often; since the second coordinate performs a simple random walk on the column above the current first coordinate whenever the vertex was visited before, the walk behaves in each column like a 1D random walk (recurrent) until it hits an unvisited vertex, at which time the first coordinate steps. Obstruction: Growth rate of the visited interval in column 0 not controlled. Verification level: unreviewed.

### C0133. Zero velocity on the non-transient event for excited random walks

Source: Kosygina and Zerner: Excited random walks, results, methods, open problems, 2012 (`kosygina_zerner_erw_2012`), Problem 4.7, p. 19.

Statement: For excited random walks on Z^d with i.i.d. elliptic environments and a direction l, does X_n . l / n converge to 0 almost surely on the complement of the event {|X_n| -> infinity}?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0133-A001). Method: Try to derive it from the law of large numbers structure of Theorem 4.8. Result: Theorem 4.8 gives lim X_n/n in {v, -cv} a.s. under a 0-1 law assumption for the directional events; on the non-transient event the walk returns to a bounded region infinitely often, so liminf |X_n|/n = 0 trivially along the return times, and the question is whether limsup X_n . l / n can be positive: the walk would have to make excursions of linear size and return. Obstruction: Uniformity fails without bounded stacks. Verification level: unreviewed.

### C0134. Ballisticity criterion under the positivity assumption instead of bounded stacks

Source: Kosygina and Zerner: Excited random walks, results, methods, open problems, 2012 (`kosygina_zerner_erw_2012`), Problem 5.3, p. 20.

Statement: Can the assumption (BD) (bounded cookie stacks) in the one-dimensional ballisticity criterion of Theorem 5.2 (positive speed iff delta > 2) be replaced by (POS1) (all cookies push to the right) with unbounded stacks?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0134-A001). Method: Check the branching-process-with-migration proof for its dependence on bounded stacks. Result: Under (BD) the branching process with migration has bounded migration per generation, and the criterion delta > 2 comes from the tail of the total progeny of a critical branching process with migration delta: P(total progeny > n) ~ n^{-delta/2}... the speed is positive iff the expected total progeny (expected excursion time) is finite iff delta > 2. With unbounded stacks under (POS1) the migration is unbounded but positive; the total progeny tail is then governed by the same exponent if the migration has finite mean, and the natural conjecture is that the criterion persists as long as the expected total drift delta = E sum_i (2 omega(0,i) - 1) is finite, with additional conditions on the tail of the stack size (as in the source's assumption (6.2) with the exponential-moment-type condition on the number of cookies far from 1/2). Obstruction: Tail analysis of branching with unbounded finite-mean migration not verified. Verification level: unreviewed.

### C0135. Running-maximum limit theorem at the critical parameter delta = 1 under weaker assumptions

Source: Kosygina and Zerner: Excited random walks, results, methods, open problems, 2012 (`kosygina_zerner_erw_2012`), Problem 6.4, p. 26.

Statement: Does the convergence of the excited random walk with delta = 1, rescaled by b sqrt(n) log n, to the running maximum of Brownian motion (Theorem 6.3) remain true when (IID), (BD), (WEL) are replaced by the assumptions (6.2), and can (POS1) then be removed?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0135-A001). Method: Identify what the log n scaling comes from and whether it survives without (POS1). Result: The log n factor at delta = 1 comes from the total progeny of the critical branching process with migration delta = 1 having a tail n^{-1/2} with a logarithmic correction, so that the time to make n right excursions is of order n^2 log n, equivalently the maximum after time t is of order sqrt(t)/log t... the source's scaling sqrt n log n for X_{[nt]} reflects the backtracking being negligible at that scale. Obstruction: Two-sided branching-with-migration comparison not verified under (6.2) without (POS1). Verification level: unreviewed.

### C0136. Tracy-Widom fluctuations of the second eigenvalue of random regular graphs

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Conjecture 7.15, p. 83.

Statement: For uniformly random k-regular graphs on n vertices, the second eigenvalue satisfies (lambda_2 - 2 sqrt(k-1))/k, suitably centred and scaled by unknown functions f(n), g(n), converges to the GOE Tracy-Widom law.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Huang, McKenzie and Yau, 'Ramanujan property and edge universality of random regular graphs' (2024), prove Tracy-Widom fluctuations of the extreme eigenvalues of random d-regular graphs for fixed d >= 3. Bounded recall. Resolved by: Huang-McKenzie-Yau 2024

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0137. Positive speed of random walk on a group is independent of the generating set

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Question 9.6, p. 94.

Statement: Is positivity of the speed of simple random walk on a finitely generated group independent of the finite symmetric generating set? Known for the lamplighter groups Z_2 wr Z^d (Erschler).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0137-A001). Method: Use the Kaimanovich-Vershik equivalence: positive speed iff positive entropy iff non-trivial Poisson boundary, and ask which of these is generating-set invariant. Result: The non-triviality of the Poisson boundary of a group (existence of non-constant bounded harmonic functions for some/all symmetric finitely supported non-degenerate steps) is NOT known to be independent of the step distribution in general, and positive entropy of the walk is equivalent to non-triviality of the boundary for the same step distribution, so the question is equivalent to: is boundary non-triviality invariant under change of finitely supported symmetric generating measure. Obstruction: No structural characterisation of Liouville groups. Verification level: unreviewed.

### C0138. Kozma's conjecture: sublinear harmonic functions and diffusive walks

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Conjecture 9.14, p. 99.

Statement: Simple random walk on a finitely generated group has no non-constant harmonic functions of sublinear growth if and only if the walk is diffusive, E dist(X_0, X_n) asymp sqrt(n).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0138-A001). Method: Test both directions on the known examples and locate the mechanism. Result: Diffusive groups: polynomial growth (virtually nilpotent) groups are diffusive and have no sublinear harmonic functions beyond constants (Kleiner/Colding-Minicozzi-type results give that harmonic functions of growth below linear are constant). Non-diffusive examples: non-amenable groups (positive speed) have bounded non-constant harmonic functions, which are sublinear; lamplighters Z_2 wr Z^d for d >= 3 have positive speed and bounded harmonic functions; Z_2 wr Z has speed of order n^{3/4}... in the exponent sense l(n) asymp n^{3/4} and non-constant harmonic functions of sublinear growth are expected (built from the lamp configuration). Obstruction: Growth exponents between 1/2 and 1 are not reached by the second-moment martingale argument. Verification level: unreviewed.

### C0139. Non-trivial percolation phase transition on every graph with an isoperimetric inequality IP_{1+eps}

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Conjecture 12.7 (Benjamini-Schramm), p. 134.

Statement: If a bounded-degree graph satisfies an isoperimetric inequality IP_{1+eps} for some eps > 0, then p_c < 1.

Status: historical status source_says_open; current-literature status unverified. Status search found: Duminil-Copin, Goswami, Raoufi, Severo and Yadin (2020) proved p_c < 1 for bounded-degree graphs of isoperimetric dimension d > 4 and for every Cayley graph of superlinear growth; the conjecture for isoperimetric dimension in (1, 4] on non-Cayley graphs was not found resolved.

Our work (attempt C0139-A001). Method: Isolate the regime left open by the Gaussian-free-field proof. Result: The DGRSY argument uses the GFF on the graph, whose existence and level-set structure need the random walk to be transient with Green function decay controlled by the isoperimetric dimension d > 4; for isoperimetric dimension in (1,4] the GFF-based route fails (in dimension at most 2 the field is not even defined without renormalisation). For transitive graphs the missing cases are covered by structure theory (polynomial growth is virtually nilpotent, hence Z^d-like, hence p_c < 1 for d >= 2 by classical arguments), so the genuinely open case is NON-transitive bounded-degree graphs with isoperimetric dimension in (1, 4]. Obstruction: GFF route needs isoperimetric dimension > 4; Peierls needs cutset counts not implied by IP_{1+eps}. Verification level: unreviewed.

### C0140. Existence of a giant component in slightly supercritical percolation on finite transitive graphs

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Conjecture 12.24 (Benjamini), p. 155.

Statement: For connected finite transitive graphs G_n with |V_n| -> infinity and diameter o(|V_n|/log|V_n|), there are a, eps > 0 with P_{1-eps}[a component of size at least a|V_n|] > eps for large n.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Hutchcroft and Tointon, 'Non-triviality of the phase transition for percolation on finite transitive graphs' (2021, arXiv 2104.05607), prove the conjecture. Bounded recall. Resolved by: Hutchcroft-Tointon 2021

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0141. Uniqueness of the giant component on finite transitive graphs

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Conjecture 12.25 (Alon-Benjamini-Stacey), p. 155.

Statement: For connected finite transitive graphs with |V_n| -> infinity, for every a, eps > 0 the probability under Bernoulli(p) percolation, uniformly over p < 1 - eps, of two components of size at least a|V_n| tends to zero.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Easo and Hutchcroft, 'Supercritical percolation on finite transitive graphs I: Uniqueness of the giant component' (2021, arXiv 2112.12778), prove uniqueness of the giant. Bounded recall. Resolved by: Easo-Hutchcroft 2021/2023

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0142. Polynomial mixing time of the giant component of the hypercube

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Conjecture 12.31 (folklore), p. 169.

Statement: The giant cluster of percolation at p = (1 + eps)/n on the hypercube {0,1}^n has polynomial mixing time, probably of order C_eps n^2.

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Anastos, Diskin, Lichev and Zhukovskii, 'Diameter and mixing time of the giant component of the hypercube' (arXiv 2510.13348, acquired by the Codex campaign as hypercube_giant_mixing_2026), establish the mixing time; bounded recall of that source's abstract. Resolved by: Anastos-Diskin-Lichev-Zhukovskii 2026

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0143. Exponential decay of large finite clusters touching the infinite cluster on transitive graphs

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Conjecture 12.32 (Pete), p. 169.

Statement: For a transitive (perhaps unimodular) graph G and all p > p_c(G), P_p(|C_o| < infinity but C_o has more than n edges to an infinite cluster) <= C_p exp(-c_p n); known for Z^d and for graphs with exponentially many minimal cutsets at p close to 1.

Status: historical status source_says_open; current-literature status unverified. Status search found: Contreras, Martineau and Tassion (2022) proved supercritical sharpness results on graphs of polynomial growth; whether that covers this statement for all transitive graphs of polynomial growth, and the exponential-growth case, was not verified.

Our work (attempt C0143-A001). Method: Reduce to a slab/renormalisation statement and identify what replaces the Z^d cluster-uniqueness input. Result: On Z^d the proof (Pete 2008) uses the Grimmett-Marstrand renormalisation and the uniqueness of the infinite cluster to show that a finite cluster with n boundary edges to C_infinity must be enclosed by a closed surface of size at least n in the renormalised picture, whose cost is exponential. On a general transitive graph the two inputs are (i) a renormalisation scheme giving supercritical behaviour on coarse-grained blocks, available for polynomial growth via the CMT 2022 results and for nonamenable graphs via the Benjamini-Lyons-Peres-Schramm / Hutchcroft methods, and (ii) an isoperimetric bound turning 'n edges to the infinite cluster' into a large closed cutset, which holds when minimal cutsets separating a finite set from infinity have size at least a function of the set's boundary, true on unimodular transitive graphs by mass transport (a finite set with boundary n has a minimal cutset of size at least n/deg). Obstruction: Amenable exponential-growth transitive graphs lack a renormalisation scheme; nonunimodular graphs lack the cutset bound. Verification level: unreviewed.

### C0144. Folner sequences along which the infinite cluster has a single giant piece

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Question 12.34 (Nekrashevych-Pete), p. 170.

Statement: For an amenable transitive graph and p > p_c, is there a connected Folner sequence F_n such that almost surely the second largest component of F_n intersect C_infinity is o(the largest) and the largest has density theta(p) in F_n?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0144-A001). Method: Try the natural Folner sequence of balls and see what fails; then a subsequence argument. Result: For balls in Z^d the statement is a theorem (uniqueness of the giant in boxes, Grimmett-Marstrand plus the finite-box uniqueness results of Pisztora); the difficulty on a general amenable transitive graph is that a Folner set can have a thin boundary but a disconnected interior structure in which C_infinity intersect F_n splits into several macroscopic pieces linked only outside F_n. A sufficient condition is a 'coarse connectivity' of F_n: every two macroscopic sub-blocks of F_n are joined inside F_n by a path of blocks each of which contains the giant with high probability; on Z^d this is the block renormalisation, and on a general amenable graph the existence of such a Folner sequence would follow from a renormalisation as in C0143, which is available for polynomial growth. Obstruction: Interior coarse connectivity of Folner sets on amenable exponential-growth graphs. Verification level: unreviewed.

### C0145. Bounded chemical-distance ratio in the uniqueness phase

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Question 12.35, p. 170.

Statement: For a transitive (unimodular?) graph and p > p_u(G), is there K(p) < infinity with E[dist_omega(x,y)/dist(x,y) | dist_omega(x,y) < infinity] < K(p) for all x, y, and is K(p) = O((p - p_u)^{-kappa+o(1)}) with kappa < 1?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0145-A001). Method: Compare with the Antal-Peres chemical distance theorem on Z^d and identify the input that p > p_u provides on nonamenable graphs. Result: On Z^d for p > p_c the chemical distance is linear with exponential tails (Antal-Peres), by renormalisation. On a nonamenable transitive graph above p_u the infinite cluster is unique and 'robust' in the sense that connections between far points exist with probability bounded below (the Lyons-Schramm characterisation inf P(x <-> y) > 0), which gives finiteness of the conditional expectation of the ratio only if one can build a chemical path of length comparable to the graph distance from these connection events, i.e. a chain of overlapping connections along a geodesic; each link is an event of probability bounded below but not close to one, and the conditional expectation of the ratio requires the links to be found within a bounded number of trials, which the uniform connection bound gives with geometric tails along the geodesic PROVIDED the connection events for different links are approximately independent, which they are not (they share the same cluster). Obstruction: Dependence of connection events along a geodesic; no renormalisation on nonamenable graphs. Verification level: unreviewed.

### C0146. Monotone coupling of random-cluster measures in p for cluster weight q < 1

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Question 13.2, p. 185.

Statement: Is there a monotone coupling (omega_p)_{p in [0,1]} of the FK(p,q) measures for q in [0,1)? (Related to negative association for q < 1, C0091.)

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0146-A001). Method: Check whether monotonicity in p of the FK(p,q) measures holds at all for q < 1, which the coupling needs. Result: For q >= 1 the measures are FKG and increasing in p (Holley), which is why a monotone coupling exists; for q < 1 FKG fails and monotonicity in p is not known in general. A necessary condition: FK(p,q) must stochastically dominate FK(p',q) for p > p', i.e. every increasing event must have nondecreasing probability in p. Obstruction: Monotonicity in p itself is unverified for q < 1; a small-graph symbolic test is the next step. Verification level: unreviewed.

### C0147. Majority-dynamics fixation threshold equals one half on Z^d and on high-degree trees

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Question 13.6, p. 188.

Statement: Is p_fix(Z^d) = 1/2 for all d >= 2, and p_fix(T_d) = 1/2 for d >= 4, where p_fix is the threshold initial density above which zero-temperature Glauber (majority) dynamics fixates at plus? Known: lim_d p_fix(Z^d) = 1/2 (Morris), p_fix(T_3) > 1/2 (Howard).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0147-A001). Method: Test the bootstrap-percolation comparison that gives the high-dimensional limit and see why it fails at fixed d. Result: Morris's proof of lim p_fix(Z^d) = 1/2 compares majority dynamics with an r-neighbour bootstrap process whose critical density tends to 1/2 as d grows; at fixed d the comparison loses a constant because the minus phase can stabilise in finite blocks (a 2x2 block of minus in Z^2 is stable under majority with ties broken against flipping, and a large minus region with flat boundary is stable), so at any density below 1/2 + eps there are stable minus regions at all scales with positive density unless the plus phase erodes them, which needs the plus phase to have a percolating 'majority backbone'. Obstruction: Stable finite minus configurations at any density under deterministic tie rules; no monotone comparison at fixed d. Verification level: unreviewed.

### C0148. Local weak approximability of Cayley graphs and soficity

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Question 14.3, p. 200.

Statement: (a) Does local weak approximability of one Cayley graph of a group imply it for all its Cayley graphs? (b) If all finitely generated Cayley graphs of a group are local-weak approximable by finite graphs, is the group sofic?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0148-A001). Method: Compare unlabelled local weak limits with the labelled (Cayley diagram) version where the answer is yes. Result: For labelled Cayley diagrams, approximability by finite labelled digraphs is soficity, and changing the generating set preserves it (relabel words). For unlabelled graphs, a finite graph sequence converging locally to the Cayley graph of one generating set need not carry labels; the question is whether one can recover a compatible labelling on most of the finite graphs. Obstruction: Recovering labels from unlabelled approximants when the Cayley graph has many automorphisms. Verification level: unreviewed.

### C0149. Bowen's conjecture: Benjamini-Schramm approximants of Kazhdan groups are essential expanders

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Conjecture 14.4 (Bowen), p. 201.

Statement: Any Cayley graph of a Kazhdan (property T) group can be Benjamini-Schramm approximated only by essential expanders: for some c > 0 and every eps > 0, from any approximating G_n one can remove eps|V(G_n)| vertices so that all remaining components are c-expanders.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0149-A001). Method: Relate to the spectral characterisation of property T and to the known fact that approximants of T groups have a spectral gap in the limit. Result: Property T gives a uniform spectral gap for every unitary representation without invariant vectors; for finite quotients this is the classical fact that quotients of T groups form expanders. Benjamini-Schramm approximants are not quotients: they only agree locally. Obstruction: Spectral-gap-in-the-limit does not localise to a removable vertex set for general graphs. Verification level: unreviewed.

### C0150. Atiyah's conjecture for torsion-free groups

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Conjecture 14.12 (Atiyah), p. 208.

Statement: For a torsion-free group, simple random walk has no atoms in its spectral measure; more generally every nonzero element of the group algebra has trivial kernel on l^2, and kernels of matrices over the group algebra have integer von Neumann dimension.

Status: historical status source_says_open; current-literature status unverified. Status search found: For groups WITH torsion the conjecture in its unrestricted form is false (Grigorchuk-Zuk lamplighter spectrum; Austin 2009; Grabowski 2010, irrational and transcendental l^2-Betti numbers); the torsion-free (strong Atiyah) conjecture remains open per bounded recall. Admitted as stated for torsion-free groups.

Our work (attempt C0150-A001). Method: Record the probabilistic content (no atoms in the return-probability spectral measure) and what the known positive cases use. Result: The random-walk form: the spectral measure of the Markov operator at the identity has no atoms iff the return probabilities p_{2n}(e,e) have no periodic component of positive mass... precisely, an atom at lambda contributes lambda^{n} to p_n(e,e) without decay, so no atoms is implied by p_n(e,e) -> 0, which holds for every infinite group (the walk is not positive recurrent). So the 'no atoms' statement for the Markov operator is immediate for infinite groups: atoms of the spectral measure sigma_{x,x} at the identity would give p_{2n}(e,e) not tending to 0. Obstruction: General group-algebra elements have no positivity; the problem is algebraic. Verification level: unreviewed.

### C0151. Independent-set densities of random regular graphs as factors of i.i.d. on the tree

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Conjecture 14.16 (Szegedy), p. 214.

Statement: The set of possible asymptotic densities of independent sets in random d-regular graphs coincides with the set of densities of independent sets that are factors of i.i.d. processes on the d-regular tree.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0151-A001). Method: Compare the two sets on what is known: the maximum independent set density versus the best factor-of-iid density. Result: One inclusion is a theorem: any factor-of-i.i.d. independent set on the tree can be transferred to random d-regular graphs (large girth) with the same density up to o(1), so factor densities are achievable. The conjecture is the converse: every achievable density is a factor density. Obstruction: none for the refutation; the residual question is trivial by dilution Independent check: Both results are widely cited; not re-fetched in this session. Verification level: unreviewed.

### C0152. Abert-Szegedy entropy conjecture for factor processes on Benjamini-Schramm convergent graphs

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Conjecture 14.17 (Abert-Szegedy), p. 214.

Statement: For a Benjamini-Schramm convergent sequence of finite graphs G_n, i.i.d. processes omega_n on them and a factor process F(G_n, omega_n) with finitely many configurations, the normalised entropy h(F, G_n)/|G_n| converges.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0152-A001). Method: Test on the two extremes: amenable limits (Ornstein-Weiss) and large-girth sequences with a tree limit. Result: For a sequence converging to an amenable transitive graph the normalised entropy of a factor converges to the Ornstein-Weiss entropy of the limiting factor process (entropy is a local-averaging quantity when Folner sets approximate). For large-girth d-regular graphs converging to the tree, two different sequences (random regular graphs versus explicit large-girth expanders) can carry the same factor F but the normalised entropy of F(G_n, omega_n) counts the number of typical configurations on G_n, which depends on global structure through the number of solutions of local constraints: this is exactly the phenomenon behind the independent-set density gap in C0151 (random regular graphs admit more independent sets than factor constructions produce). Obstruction: Entropy of a factor is not a local statistic; local-global convergence is the natural extra hypothesis. Verification level: unreviewed.

### C0153. Local limits of random-cluster models converging to nonamenable transitive graphs are wired

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Question 14.19, p. 215.

Statement: If finite graphs G_n converge locally weakly to a nonamenable transitive graph G, is the local limit of the FK(p,q) random-cluster measures on G_n (especially q > 1) the wired measure on G? Known for the WUSF (q = p = 0) and for Ising on regular trees (Montanari-Mossel-Sly: symmetric mixture of plus and minus).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0153-A001). Method: Separate the random-cluster question from its spin-model consequence. Result: For q = 2 the Montanari-Mossel-Sly result is about the ISING local limit on regular trees, which is the symmetric mixture of the plus and minus extremal measures; in random-cluster language this corresponds to the wired measure (the mixture of the two spin phases is the Edwards-Sokal image of the wired FK measure). So the q = 2, tree case is consistent with the question. Obstruction: Giant uniqueness for non-transitive local approximants. Verification level: unreviewed.

### C0154. Amenability of Thompson's group F

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Question 15.3, p. 222.

Statement: Determine whether Thompson's group F is amenable. (Random walks have positive speed for some generating set, Kaimanovich, so the speed criterion does not decide it.)

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0154-A001). Method: Record why the probabilistic criteria are inconclusive. Result: Positive speed of a symmetric finitely supported walk does not decide amenability (amenable groups such as lamplighters have positive speed), and the Kesten criterion (spectral radius < 1 iff nonamenable) would decide it but the spectral radius of F is not computable by current methods; numerical estimates of return probabilities on F (Haagerup-Haagerup-Ramirez-Solano) are consistent with both. Probabilistic content available: F has exponential growth and contains no free subgroup (Brin-Squier), so the Tits alternative route is closed; F is not elementary amenable; F's Folner sets, if they exist, must be exotic (Moore's lower bound on Folner function growth). Obstruction: No computable amenability criterion applies to F. Verification level: unreviewed.

### C0155. Quasi-isometry of two independent Poisson point processes on the line

Source: Pete: Probability and geometry on groups, lecture notes with open problems (`pete_pgg_notes`), Question 16.2 (Szegedy), p. 222.

Statement: Are two independent Poisson point processes on R almost surely quasi-isometric to each other (as metric spaces with the induced metric)?

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0155-A001). Method: Construct an explicit bijection with bounded distortion using the law of the iterated logarithm. Result: Order both processes as ...< x_{-1} < x_0 < x_1 < ... and ...< y_{-1} < y_0 < y_1 < ... and map x_i -> y_i. Distortion: |y_i - y_j| versus |x_i - x_j| for i < j are both sums of j - i i.i.d. exponentials, so their ratio is close to 1 for large j - i by the law of large numbers, but a quasi-isometry needs a UNIFORM bound C such that |x_i - x_j|/C - c <= |y_i - y_j| <= C|x_i - x_j| + c for ALL pairs; for nearby pairs (j - i small) the ratio of two independent Gamma(k) variables is unbounded over infinitely many pairs (there are a.s. pairs with x-gap tiny and y-gap of order 1), so the index map fails. Obstruction: Existence of a bounded-distortion non-monotone matching between two independent Poisson processes is unresolved. Verification level: unreviewed.

### C0156. Once-reinforced random walk phase transition in the reinforcement parameter

Source: Kozma: Reinforced random walk, survey with open problems (`kozma_reinforced_2012`), Section 2 (Beffara-Sidoravicius conjecture), p. 3.

Statement: For once-reinforced random walk on Z^d, d >= 3, with weight 1 + a on traversed edges, there is a phase transition in a: for small a the walk behaves like simple random walk and for large a it is confined and grows like an aggregation model.

Status: historical status source_says_open; current-literature status unverified. Status search found: Kious and Sidoravicius (2018) proved a phase transition for once-reinforced walk on trees; the Z^d statement was not found resolved in bounded recall.

Our work (attempt C0156-A001). Method: Recall what the tree result uses and why Z^d resists. Result: On trees the once-reinforced walk restricted to the range is a walk on a growing tree with an exact renewal structure at cut points (the walk exits a subtree forever with positive probability), and the phase transition is a comparison of the escape probability from the range boundary with the branching. On Z^d the range has no cut structure; for large a the walk at the boundary of its range prefers to return inside (reinforced edges), so the range grows like an aggregate whose growth rate per boundary visit is 1/(1+a)-ish, giving a ball-like range of radius growing like t^{1/(d+...)}; for small a the perturbation of simple random walk is small at every step but accumulates over the infinitely many returns to the range boundary, and transience of simple random walk in d >= 3 suggests the walk escapes the range often enough to stay diffusive: the expected number of visits to the range boundary before escaping to fresh territory is bounded in d >= 3, so the total effect of reinforcement on the walk's law up to time t is a bounded number of biased steps per new site, i.e. Obstruction: Reinforcement bias is applied at every new-site visit, giving O(t) biased steps; no perturbative comparison. Verification level: unreviewed.

### C0157. Recurrence of linearly reinforced random walk on Z^2

Source: Kozma: Reinforced random walk, survey with open problems (`kozma_reinforced_2012`), Section 5, p. 11.

Statement: Linearly reinforced random walk on Z^2 is recurrent, at least for small reinforcement (Diaconis's conjecture from the 1980s; Merkl-Rolles proved it on a modified two-dimensional graph).

Status: historical status source_says_open; current-literature status resolved_in_literature. Status search found: Sabot and Zeng, 'A random Schrodinger operator associated with the vertex reinforced jump process on infinite graphs' (J. Amer. Resolved by: Sabot-Zeng 2019

Not admitted: literature exclusion (`admitted = false`, `result_status = not_attempted_resolved`); the resolving citation is given in Status above.

### C0158. Number of infinite clusters at the uniqueness threshold p_u on nonamenable transitive graphs

Source: Haggstrom and Jonasson: Uniqueness and non-uniqueness in percolation theory, Probability Surveys 2006, with open problems (`haggstrom_jonasson_uniqueness_2006`), Section 3, p. 13 (PDF).

Statement: Determine, for nonamenable transitive graphs with p_c < p_u < 1, whether the number of infinite clusters at p = p_u is 1 or infinity. Known: infinity on T_d x Z (Schonmann) and on products G x H with a nonamenable factor (Peres); 1 on planar nonamenable one-ended graphs (Benjamini-Schramm).

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0158-A001). Method: Look for the invariant that separates the product case from the planar case. Result: In the planar one-ended case uniqueness at p_u comes from duality: non-uniqueness at p would put infinitely many infinite dual clusters at 1 - p, and the planar argument shows the two cannot coexist at the threshold, forcing N(p_u) = 1. In the product case Peres's argument uses that G x H contains many disjoint copies of a nonamenable graph along which connectivity decays, and the key quantity is the connection probability tau_p(x,y) as |x - y| -> infinity: at p_u uniqueness holds iff inf tau_{p_u}(x,y) > 0 (Lyons-Schramm characterisation), and for products the decay of tau at p_u is inherited from the factor. Obstruction: Positivity of the two-point infimum exactly at p_u has no general criterion; known only via duality (planar) or factor decay (products). Verification level: unreviewed.

### C0159. Cluster repulsion for nonunimodular transitive graphs

Source: Haggstrom and Jonasson: Uniqueness and non-uniqueness in percolation theory, Probability Surveys 2006, with open problems (`haggstrom_jonasson_uniqueness_2006`), Section 6, p. 20-21 (PDF).

Statement: Does every transitive graph exhibit cluster repulsion, i.e. two distinct infinite clusters at level p almost surely do not come within bounded distance of each other along an infinite set of sites (Haggstrom-Peres-Schonmann conjecture)? Timar proved it for unimodular transitive graphs by mass transport; the nonunimodular case is open.

Status: historical status source_says_open; current-literature status unverified.

Our work (attempt C0159-A001). Method: Check whether the mass-transport step can be replaced on nonunimodular graphs by a tilted transport. Result: Timar's argument transports mass from each site of cluster C_1 that is adjacent (in the graph) to a site of C_2 to the nearest such neighbour and uses the mass-transport principle to show the expected received mass is bounded, forcing finitely many 'touching' pairs per site on average, hence no strongly neighbouring pair of infinite clusters with positive density; unimodularity enters exactly in the equality of sent and received mass. Obstruction: Tilted mass transport does not bound received mass; the grandparent graph is the test case in both directions. Verification level: unreviewed.

### C0160. Continuity of the uniqueness threshold in the retention parameter: is N(p) monotone in p on transitive graphs?

Source: Haggstrom and Jonasson: Uniqueness and non-uniqueness in percolation theory, Probability Surveys 2006, with open problems (`haggstrom_jonasson_uniqueness_2006`), Section 3, p. 12 (PDF).

Statement: For i.i.d. bond percolation on a transitive graph, show that the number of infinite clusters N(p) cannot switch back and forth between infinity and 1 as p increases: the set of p with uniqueness is an interval [p_u, 1] (proved for transitive graphs by Haggstrom-Peres and Schonmann; the survey records the general question for quasi-transitive and for non-unimodular graphs as settled only in the transitive case).

Status: historical status source_says_open; current-literature status unverified. Status search found: The survey states uniqueness monotonicity for transitive graphs (Haggstrom-Peres 1999, Schonmann 1999); the admitted residual question is the quasi-transitive and general invariant-percolation setting. Bounded reading of the survey only.

Our work (attempt C0160-A001). Method: Trace the transitive proof and mark where transitivity is used. Result: Haggstrom-Peres prove uniqueness monotonicity for transitive graphs via the simultaneous uniqueness of the standard coupling: if the p_1-cluster is unique then each p_2-cluster, p_2 > p_1, contains a p_1... more precisely each infinite p_2-cluster contains an infinite p_1-cluster (the 'no new infinite clusters at higher p' statement), which uses transitivity through the two-point-infimum characterisation of uniqueness and its monotonicity in p. Quasi-transitivity (finitely many orbits) is enough for the two-point infimum argument with a finite set of base points, so the monotonicity transfers to quasi-transitive graphs with the same proof, which I believe is stated in Lyons-Peres. Obstruction: Nonunimodular dependent families: the Lyons-Schramm characterisation needs unimodularity. Verification level: unreviewed.

