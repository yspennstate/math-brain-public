## Catalog chapter 3: Codex campaign (Probability_1000_20h_20260906), P0301-P0450

This chapter covers rows P0301 through P0450 of the Codex 20-hour probability campaign ledger (problems.jsonl, attempts.jsonl, sources.jsonl in ~/Downloads/Probability_1000_20h_20260906). All 150 ids in the range are present in problems.jsonl; 140 of 150 are marked admitted and 10 are not admitted (each carries a resolution record in the ledger explaining why: a literature counterexample already exists, the source's own later paper already resolves it, or it is a known result not original here). Result_status counts across the 150 rows: unsolved: 131, candidate_partial_counterexample: 8, known_result_not_original: 5, literature_resolution_claimed_not_independently_certified: 3, literature_counterexample: 1, literature_counterexample_claim_not_full_proof_reviewed: 1, candidate_full_solution: 1. 140 of 150 rows have at least one recorded attempt in attempts.jsonl (the 10 not-admitted rows have none); 8 rows carry a proof_file or proof_path reference. Two admitted rows (P0411, P0429) carry two attempt records under the same attempt_id, the second an addendum with an extra exact check or a counterexample found after the first pass; the later, fuller record is reported for each. No CORRECTIONS.md file exists in the source directory; no record in this directory revises a status for a row in this range beyond what is already recorded on the row itself (the resolution_source_id / resolution_evidence / resolution_locator fields already carry the correcting record for the 10 not-admitted rows and for the small number of admitted rows whose current_status is resolved_in_literature or resolution_claimed_in_literature). As stated in the campaign's own README.md and STATUS.json, zero results in this ledger are independently reviewed; every verification level reported below is author_checked or weaker unless stated otherwise, and nothing in this chapter is a claim of publishable novelty.

### P0301. Full probabilistic noncompact imaginary Liouville theory

**Source.** Rhodes-Vargas: Two decades of probabilistic approach to Liouville conformal field theory,2025 (lcft_rhodes_vargas_2025), Section9,PDF18;Usciati et al2505.09390,PDF3-4.

**Statement.** Complete the probabilistic construction and identification of noncompact imaginary Liouville theory in the general non-neutral regime described by the survey. Ledger caveat: Usciati-Guillarmou-Rhodes-Santachiara give a proposed construction and exact circle results; their sphere construction depends on conjectured imaginary-chaos Laplace asymptotics. Chatterjee2504.02348 proves timelike results under charge neutrality. These partial results must not be erased or counted as new.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit calculation or obstruction with source-specific scope. Result: The circle contour calculation shows why simply integrating the constant mode over a real period imposes neutrality. For an integer screening expansion, the integral of exp(i*k*beta*c) over a full period vanishes unless k=0. A noncompact complex Hankel-type contour can avoid that selection rule, but requires a large-argument estimate for the complex GMC Laplace transform along its two infinite legs. Finite exponential moments only ensure finiteness for each fixed argument, not decay along those legs. Obstruction: The missing sphere Laplace estimate and identification with the imaginary DOZZ expression remain unresolved in the read source. Current status requires later papers beyond the read2025 proposal and April2026 charge-neutral result; it is not certified open solely from the survey. Verification: author_checked_partial. No proof file recorded.

### P0302. One critically loaded queue under general k-limited polling inputs

**Source.** Boon and Winands: Open problems for critically loaded k-limited polling systems (2022) (queues_klimited_uva_2022), Conjecture1 and Problem1,journal282,PDF3.

**Statement.** Prove the general finite-variance renewal-input heavy-traffic joint limit in Boon-Winands Conjecture1: one critically loaded queue has the stated scaled exponential limit, the other converges to the stated vacation queue, and the components become independent. Ledger caveat: The exponential and phase-type special cases are already established. The source regime lambda1/k1<lambda2/k2 and scaling with fixed interarrival coefficient of variation are essential.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit calculation or obstruction with source-specific scope. Result: The source switch-over variance absorption has a useful exact batch check. When the critical queue serves exactly k2 jobs per cycle, its batch time is sum of k2 iid B2 variables plus the total switch-over S. The batch variance divided by k2 is Var(B2)+Var(S)/k2. Assigning the same S/k2 to every effective job instead would give marginal variance Var(B2)+Var(S)/k2^2 but introduce correlations between those jobs. Ignoring those correlations would produce the wrong diffusion coefficient. Obstruction: This verifies the proposed effective mean and variance but not the joint stationary limit. General renewal residual lives, the stable-queue vacation environment, asymptotic independence and stationary interchange still need a proof. The source simulation correlation near zero is not a proof of independence. Verification: author_checked_partial. No proof file recorded.

### P0303. Simultaneous criticality in k-limited polling

**Source.** Boon and Winands: Open problems for critically loaded k-limited polling systems (2022) (queues_klimited_uva_2022), Problem2,journal283,PDF4.

**Statement.** Determine the heavy-traffic joint queue-length distribution when both queues in a k-limited polling system become critically loaded simultaneously. Ledger caveat: The two-queue source problem is one entry; extensions to more queues and parameter choices are grouped. The one-critical-queue theorem does not apply at equality of the load ratios.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit calculation or obstruction with source-specific scope. Result: The no-switch-over comparison has an exact simplification: if all jobs require deterministic time2 and arrivals are the superposition of independent Poisson streams, total workload is the workload of a work-conserving M/D/1 queue, independently of the polling order. Introducing deterministic switch-over times destroys work conservation even when the sum of a service time and a switch time remains2. Empty visits then consume capacity, and their boundary frequencies enter the two-dimensional reflected limit. Obstruction: The missing boundary occupation and reflection structure prevent identifying the limiting joint law from a scalar workload formula. The source suggests a two-dimensional transform boundary-value problem. No solution of that problem or valid interchange of its heavy-traffic limit is supplied. Verification: author_checked_partial. No proof file recorded.

### P0304. Telek two-matrix RAP to MAP conjecture

**Source.** Peralta: Rational arrival processes with strictly positive densities need not be Markovian (2026) (peralta_rap_2026), Conjecture1,PDF2;Theorem9,PDF9.

**Statement.** Must a rational arrival process with strictly positive joint densities and a unique dominant real eigenvalue of its no-arrival matrix admit a finite Markovian arrival-process representation? Ledger caveat: The2026 primary counterexample paper restates Telek2022 and refutes it. Excluded from the open target.

**Status.** Historical status: source_says_open_in_2022. Current-literature status: resolved_in_literature (no status-search record recorded in the ledger). Resolution record: https://arxiv.org/abs/2603.28047. Complete10-page primary preprint read; positive-density bound by summation by parts, normalization and irrational peripheral-pole obstruction checked. Not a new result here; independent human review not claimed. Admission: not admitted; result_status: literature_counterexample.

**Our work.** Not admitted (result_status: literature_counterexample); see the resolution record above. No attempt is recorded for this row in attempts.jsonl.

### P0305. Hausdorff dimensions of bulk LQG geodesic star sets

**Source.** Bhatia Gwynne Harper: Dimension lower bounds in random geometry via Lipschitz functions (2026) (lqg_lipschitz_2026), Introduction PDF2;discussionPDF6;Theorem1.2 baseline.

**Statement.** Determine the Hausdorff dimensions of bulk k-star sets for general gamma-LQG; in particular prove or refute the conjectured metric dimension2 of the three-star set. Ledger caveat: The different k values are grouped into a single source family. Brownian-map dimensions5-k for k<=5 and the2026 lower bound2 for three-stars are known results, not new solutions.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit calculation or obstruction with source-specific scope. Result: A difference-of-distance map f(x)=(D(x,a)-D(x,b),D(x,a)-D(x,c)) is2-Lipschitz in each coordinate. The source uses non-constancy of such maps to get dimension lower bounds. This mechanism supplies no upper bound: the coordinate projection from a square to a line is Lipschitz and has a one-dimensional image, while its non-constancy set is the entire two-dimensional square. Obstruction: An upper bound needs quantitative control of fibers or a covering estimate for points supporting multiple noncoalesced geodesics. Lipschitz mapping and topological confluence alone do not provide it. No matching upper bound for general gamma is proved. Verification: author_checked_partial. No proof file recorded.

### P0306. One-dimensional boundary two-star set in LQG

**Source.** Bhatia Gwynne Harper: Dimension lower bounds in random geometry via Lipschitz functions (2026) (lqg_lipschitz_2026), Conjecture1.4,PDF7;Theorem1.3 lower boundPDF6.

**Statement.** For the gamma-LQG metric associated with a Neumann GFF on the upper half plane, is the metric Hausdorff dimension of the boundary two-star set exactly1? Ledger caveat: The boundary intersection uses the ambient LQG metric restricted to the boundary, not an intrinsic boundary path metric. The established lower bound1 is not the requested equality.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit calculation or obstruction with source-specific scope. Result: Topological one-dimensionality of the boundary cannot prove this metric upper bound. On [0,1], the snowflake metric D_alpha(x,y)=|x-y|^alpha for0<alpha<1 induces the usual topology but has Hausdorff dimension1/alpha. A cover with Euclidean diameters r_j has D_alpha diameters r_j^alpha, making the s-dimensional metric Hausdorff sum the alpha*s-dimensional Euclidean sum. Obstruction: One needs a covering argument specifically for the random boundary two-star subset in the restricted LQG metric. The source lower bound and the fact that the boundary is a topological line do not establish the conjectured upper bound. Verification: author_checked_partial. No proof file recorded.

### P0307. Exact dimension of the LQG metric net

**Source.** Bhatia Gwynne Harper: Dimension lower bounds in random geometry via Lipschitz functions (2026) (lqg_lipschitz_2026), IntroductionPDF3;discussionPDF6 afterTheorem1.3.

**Statement.** Determine the Hausdorff dimension of the LQG metric net; in particular establish the expected metric dimension3 in the Brownian-map case. Ledger caveat: One metric-net dimension family is counted. Dimensions of geodesic stars and of intersections of two nets are different targets. The2026 source lower bounds are not claimed as new.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit calculation or obstruction with source-specific scope. Result: A fixed metric sphere and the union of spheres over all radii have different dimension behavior. In the Euclidean plane, each circle about the origin has Hausdorff dimension1 while their union over radii in[1,2] is an annulus of dimension2. Thus even a sharp dimension theorem for each outer boundary cannot be passed to the metric net by countable stability: the union is uncountable. Obstruction: For LQG one needs joint control of the outer boundaries as radius varies, including the jumps created by swallowed components. The source non-constancy representation supplies a lower bound, but not the required upper covering or exact law. The dimension3 statement remains unproved here. Verification: author_checked_partial. No proof file recorded.

### P0308. Canonical and grand-canonical equivalence for long-range Riesz gases

**Source.** Lewin: Coulomb and Riesz gases, the known and the unknown,2022 (lewin_riesz_review_2022), SectionIII,PDF27-28.

**Statement.** Prove the conjectured equivalence of canonical and grand-canonical thermodynamic free energies for neutral Riesz gases throughout the remaining positive long-range exponents0<s<d, beyond the known s>=d-2 regime. Ledger caveat: All remaining exponents are grouped. Nonpositive exponents can make the grand-canonical energy unbounded below and are outside this formulation. The source discusses a possible route when s>=d-4.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: The grand partition function contains its exactly neutral canonical summand, giving one free-energy inequality immediately. Concentration of the particle number around neutrality does not give the opposite inequality. For example, a law supported equally at N-floor(sqrt(N)) and N+floor(sqrt(N)) has particle number divided by N tending to1 but assigns probability zero to exactly N. Obstruction: A proof needs uniform energy and entropy control when inserting or removing the subextensive excess charge, or a local partition-function comparison. Long-range background energy makes that repair nonlocal. No reverse free-energy inequality is proved here. Verification: author_checked_partial. No proof file recorded.

### P0309. Positive-temperature crystalline Gibbs phases for three-dimensional Riesz gases

**Source.** Lewin: Coulomb and Riesz gases, the known and the unknown,2022 (lewin_riesz_review_2022), SectionVI,PDF59-61,66-67.

**Statement.** Prove existence of a crystalline Gibbs phase at sufficiently low positive temperature for the three-dimensional Coulomb or Riesz gas in the regimes predicted in the review. Ledger caveat: This is the positive-temperature phase-existence question; the lattice-energy minimization problem at zero temperature and individual numerical transition constants are not separate entries.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: The harmonic phonon calculation around an assumed crystal has infrared displacement variance proportional to integral over |k|<1 of |k|^-2 dk. In dimension d this is a constant times integral from0 to1 of r^(d-3)dr, finite in d=3 and logarithmically divergent in d=2. Therefore the elementary infrared objection to positional order is absent in three dimensions. Obstruction: One must control defects, anharmonic fluctuations and alternative configurations uniformly in volume and show nontrivial positional order. Finite variance within an assumed crystal cannot prove that the full Gibbs law is crystalline. Numerical BCC/FCC phase diagrams are not a proof. Verification: author_checked_partial. No proof file recorded.

### P0310. Uniqueness for the one-dimensional short-range Riesz Gibbs gas

**Source.** Lewin: Coulomb and Riesz gases, the known and the unknown,2022 (lewin_riesz_review_2022), SectionVI,PDF61;Boursier Section1.3,PDF5.

**Statement.** Establish the expected uniqueness of the one-dimensional short-range Riesz Gibbs state in the unresolved exponent range1<s<=2. Ledger caveat: The s>2 uniqueness regime is already known. Boursier proves a unique thermodynamic limit of the circular finite-volume laws for s>1, which is not by itself uniqueness among all DLR Gibbs states.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: A lattice interface calculation separates summability of a pair potential from summability of its boundary influence. For potential r^-s, its sum over r is finite when s>1, whereas the total weight of pairs crossing one cut is sum over r of r*r^-s, which diverges when s<=2. Hence the usual finite-boundary-energy argument cannot simply use integrability of the potential. Obstruction: A uniqueness proof must exploit convex repulsion or finer cancellation beyond finite interface cost, and control all boundary conditions. Uniqueness of a particular periodic approximation does not exclude other infinite-volume specifications. Verification: author_checked_partial. No proof file recorded.

### P0311. Optimal truncated pair-correlation decay in the Riesz fluid phase

**Source.** Lewin: Coulomb and Riesz gases, the known and the unknown,2022 (lewin_riesz_review_2022), SectionVI,PDF63,67,69.

**Statement.** Prove the predicted fluid-phase truncated pair-correlation tail of order |x|^(-(2d-s)) for long-range Riesz gases, with the exceptional Coulomb-type exponents and phase restrictions treated as in the source. Ledger caveat: One tail family is counted. Correlation of ordered gaps in the one-dimensional circular gas is a different observable and does not automatically prove this point-density asymptotic. Current openness is not certified for every parameter.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: The formal random-phase closure gives structure factor S(k)=1/(1+beta*rho*Vhat(k)). Since the Riesz Fourier transform scales as |k|^(s-d), this predicts S(k) of order |k|^(d-s) near0. Fourier homogeneity then predicts a real-space correction with degree -(2d-s). Obstruction: The closure replaces higher correlations by a Gaussian response and has no error estimate here. Establishing its leading nonanalytic coefficient, excluding crystalline oscillations and passing to a pointwise tail remain unresolved. The scaling calculation is a heuristic conditional implication. Verification: author_checked_partial. No proof file recorded.

### P0312. Infinite-volume BBGKY equation for the general sine-beta process

**Source.** Lewin: Coulomb and Riesz gases, the known and the unknown,2022 (lewin_riesz_review_2022), Equation147 and discussion,PDF63.

**Statement.** Justify the renormalized infinite-volume BBGKY equation described in the review for the sine-beta process at general beta. Ledger caveat: The source specifically distinguishes known DLR equations from the still-unjustified BBGKY passage. Later stochastic-dynamics work may overlap; current status remains unverified until its hypotheses are compared.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: Finite-volume integration by parts produces the force sum over other particles of1/(x-y). At unit density, the absolute far-field integral is integral from1 toR of dy/y=log R. Thus a bound obtained by taking absolute values before the infinite-volume limit cannot be uniform. A symmetric principal value may cancel the mean term, but then fluctuations and truncated correlations must be controlled. Obstruction: The missing step is uniform integrability of the renormalized force and justification of differentiation under the infinite conditional law. Existence of a DLR density does not alone justify that interchange. No general BBGKY identity is established here. Verification: author_checked_partial. No proof file recorded.

### P0313. Translation invariance in low-dimensional long-range Riesz gases

**Source.** Lewin: Coulomb and Riesz gases, the known and the unknown,2022 (lewin_riesz_review_2022), SectionVI,PDF63.

**Statement.** Prove the expected absence of translation-symmetry breaking for one-dimensional Riesz gases0<=s<1 and two-dimensional Riesz gases1<=s<2 in the regimes discussed in the review. Ledger caveat: The dimensions and exponent ranges are grouped as the source translation-invariance question. Leble2024 proves translation invariance for local bulk limits of the two-dimensional Coulomb gas s=0, a separate established case.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: A naive Mermin-Wagner deformation estimate based on absolute Hessians is divergent. For V(r)=r^-s, the Hessian has size of order r^-s-2. Multiplication by a displacement difference bounded crudely by a constant times r gives the second-order energy integral of order integral r^(d-1)*r^2*r^-s-2 dr = integral r^(d-s-1)dr. Obstruction: One needs a deformation adapted to neutrality or screening, with cancellation of long-range contributions and control of rare configurations. Absolute Hessian integrability cannot establish the stated symmetry theorem. Existing periodic-limit uniqueness is not automatically a theorem for every Gibbs state. Verification: author_checked_partial. No proof file recorded.

### P0314. Uniqueness of the general sine-beta DLR Gibbs measure

**Source.** Dumaz and Malvy: Long-Range Correlation of Sine beta Point Process (2026) (dumaz_malvy_sine_correlations_2026), Introduction,PDF2.

**Statement.** Prove or refute uniqueness of the sine-beta Gibbs measure under its Dobrushin-Lanford-Ruelle characterization for general positive beta. Ledger caveat: The March2026 primary source explicitly calls uniqueness for the DLR characterization open. A stationary free-energy characterization and special determinantal cases do not by themselves settle all DLR measures.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: A tempting variational route is to prove that the specific relative entropy of two candidate states vanishes. Vanishing entropy per volume alone cannot imply equality of states. On n binary sites take P_n=delta_(0,...,0) and Q_n=(delta_(0,...,0)+delta_(1,...,1))/2. Then D(P_n||Q_n)=log2 for every n, hence D/n tends to0, while the limiting cylinder event X_1=1 has probabilities0 and1/2. Obstruction: A successful variational argument needs a uniqueness mechanism beyond zero specific entropy, plus a theorem placing every DLR state in the admissible stationary finite-energy class. The diagnostic does not construct a second sine-beta Gibbs measure. Verification: author_checked_partial. No proof file recorded.

### P0315. Forrester-Haldane pointwise pair-correlation asymptotics for sine beta

**Source.** Dumaz and Malvy: Long-Range Correlation of Sine beta Point Process (2026) (dumaz_malvy_sine_correlations_2026), Introduction,PDF2-3;Lewin equations149-150,PDF64.

**Statement.** Prove the predicted oscillatory large-distance expansion of the sine-beta truncated two-point correlation function for general beta, beyond the established special values and weaker averaged decay estimates. Ledger caveat: All harmonics and beta regimes are one asymptotic family. Lewin uses unit density; Dumaz-Malvy use density1/(2*pi), so distances must be rescaled before comparing coefficients.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: At beta=2 and unit density the exact formula is rho_T(r)=-sin^2(pi*r)/(pi^2*r^2)=-1/(2*pi^2*r^2)+cos(2*pi*r)/(2*pi^2*r^2). This verifies the collision of the nonoscillatory r^-2 and oscillatory r^-4/beta powers at beta=2. It also shows why a naive nonzero pointwise ratio to a single power cannot hold: the expression vanishes at every nonzero integer. Obstruction: For general beta the March2026 theorem bounds a locally averaged correlation by a nonsharp power; it does not give the exact oscillatory coefficients or pointwise remainder. The desired expansion needs additive error control that remains meaningful at zeros. No generic asymptotic is proved. Verification: author_checked_partial. No proof file recorded.

### P0316. Two phase transitions in negative-exponent one-dimensional Riesz gases

**Source.** Dereudre and Digneaux: Rigidity of one dimensional point processes via optimal transport (dereudre_digneaux_rigidity_2025), Introduction and Figure1,PDF2-3;Lewin PDF68.

**Statement.** Prove or refute the predicted temperature-dependent phase diagram, including the suggested two transitions, for one-dimensional Riesz gases with -1<s<0. Ledger caveat: The2025 source explicitly leaves this interval open. Its rigidity and hyperuniformity result for -2<s<=-1 is established prior work and outside this unresolved interval.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: For V(r)=-r^p with p=-s in(0,1), the positive second derivative is p*(1-p)*r^(p-2). The harmonic lattice stiffness therefore has small-frequency order |k|^(1-p)=|k|^(1+s), obtained from the sum of (1-cos(k*r))*r^(-2-s). Its Gaussian displacement variance involves integral_0^1 k^(-1-s)dk, finite for every s<0 at any fixed temperature. Obstruction: Defects and changes of ordering must be controlled beyond the Gaussian expansion. The finite harmonic variance is neither a proof of a crystal nor a refutation of the proposed fluid and intermediate phases. No transition temperatures are established. Verification: author_checked_partial. No proof file recorded.

### P0317. Hyperuniformity of general long-range Riesz Gibbs gases

**Source.** Lewin: Coulomb and Riesz gases, the known and the unknown,2022 (lewin_riesz_review_2022), SectionVI.C,PDF69.

**Statement.** Prove the expected hyperuniformity of the long-range Riesz gas in the general regimes where the review predicts it, beyond presently established special cases. Ledger caveat: The question concerns subvolume number variance in growing windows. Fixed total particle number in a finite canonical ensemble is not itself hyperuniformity of an infinite-volume limit; newer one-dimensional and Coulomb results are partial established cases.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: Consider N independent uniform points in a box of volume N. The canonical truncated pair density is -1/N within the box, whose integral over the full box is -1. In any fixed bounded window A, the count has variance |A|*(1-|A|/N), tending to |A|; the local point-process limit is a unit-intensity Poisson process and is not hyperuniform. Obstruction: The canonical neutrality sum rule must be supplemented by uniform correlation-tail or screening estimates before passage to an infinite-volume variance law. Those estimates are not provided here for the full Riesz family. Verification: author_checked_partial. No proof file recorded.

### P0318. Sharp number-variance growth exponents for long-range Riesz gases

**Source.** Lewin: Coulomb and Riesz gases, the known and the unknown,2022 (lewin_riesz_review_2022), SectionVI.C,PDF69.

**Statement.** Establish the predicted three regimes for the variance of the number of particles in a ball of radius R: order R^s for s>d-1, order R^(d-1)*log R at s=d-1, and order R^(d-1) for s<d-1. Ledger caveat: The three regimes are one source family. The question asks for sharp growth beyond hyperuniformity alone. Existing one-dimensional gap fluctuation and selected Coulomb results must be treated as known subcases.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: Conditional on a stationary unit-density process with an integrable truncated pair density h satisfying integral h=-1, Var N(B_R)=-integral h(z)*(|B_R|-|B_R intersect(B_R-z)|)dz. For a ball, the intersection deficit is of order R^(d-1)*min(|z|,R). If h has a noncanceling negative tail of order |z|^(-(2d-s)), the contribution from1<|z|<R is of order R^(d-1)*integral_1^R r^(s-d)dr, yielding exactly the three predicted powers. Obstruction: This is a conditional calculation, not a proof that a Gibbs state satisfies the required sum rule, signed tail, uniform bounds or positive surface coefficient. Oscillatory tails may require cancellation rather than absolute comparisons. These unresolved hypotheses carry the probabilistic content. Verification: author_checked_partial. No proof file recorded.

### P0319. Old Riesz number-rigidity threshold at s=d-1

**Source.** Lewin: Coulomb and Riesz gases, the known and the unknown,2022 (lewin_riesz_review_2022), SectionVI.C,PDF70;Thoma2023 Introduction PDF2.

**Statement.** The historical conjecture predicts number rigidity for Riesz gases at and below the threshold s=d-1. Ledger caveat: Thoma explicitly reports disproving this conjecture by non-rigid Coulomb gas limits in d>=3. Excluded from the open target; the full15-page proof has not yet been read in this campaign.

**Status.** Historical status: source_says_open_in_2022. Current-literature status: claimed_resolved_in_literature (no status-search record recorded in the ledger). Resolution record: https://arxiv.org/abs/2303.11486. Primary introduction and Theorem1 read, plus2026 journal abstract; full proof not yet checked. New remaining interval recorded as P0320. Admission: not admitted; result_status: literature_counterexample_claim_not_full_proof_reviewed.

**Our work.** Not admitted (result_status: literature_counterexample_claim_not_full_proof_reviewed); see the resolution record above. No attempt is recorded for this row in attempts.jsonl.

### P0320. Number rigidity in the remaining Riesz exponent band

**Source.** Thoma: Non-rigidity Properties of the Coulomb Gas (thoma_coulomb_nonrigidity_2023), Introduction,PDF2.

**Statement.** Determine number rigidity or non-rigidity for Riesz gases in the remaining admissible band s in(d-2,d-1], which Thoma identifies as open after disproving the older general threshold conjecture. Ledger caveat: The earlier threshold claim is retained separately as an excluded historical conjecture P0319. The interval is one question, restricted to the Riesz models for which an infinite-volume gas is defined. Later status remains unverified.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: A symmetric displacement comparison cancels the first-order force: V(x+h)+V(x-h)-2V(x) is controlled by |h|^2 times a local Hessian bound. For V(x)=|x|^-s, the far-field Hessian integral has radial order integral_1^infinity r^(d-s-3)dr, finite exactly when s>d-2. This explains why a second-order transport argument might reach the stated band despite a nonintegrable first derivative. Obstruction: Integrability of the deterministic tail is only one ingredient. Constructing a number-changing comparison also requires entropy, label matching, local singularity control and uniform conditional probability bounds. No non-rigidity theorem for the open band is proved here. Verification: author_checked_partial. No proof file recorded.

### P0321. Existence of a hexatic phase for two-dimensional Riesz gases

**Source.** Lewin: Coulomb and Riesz gases, the known and the unknown,2022 (lewin_riesz_review_2022), SectionVI.B,PDF66-67.

**Statement.** Prove or refute the intermediate hexatic phase predicted in two-dimensional Riesz-gas phase diagrams, distinguished by orientational order and absence of crystalline positional order. Ledger caveat: This is a finite-temperature order-type question distinct from existence of a three-dimensional crystal. Numerical phase boundaries are motivation, not rigorous evidence of existence.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: A rotationally invariant Gibbs mixture can have zero mean orientational order while retaining long-range two-point order. As a diagnostic let theta_x=Theta+eta_x, where Theta is uniform modulo2*pi and the eta_x are iid. Then E exp(6*i*theta_x)=0, but for x distinct from y, E exp(6*i*(theta_x-theta_y))=|E exp(6*i*eta_x)|^2, which can be strictly positive. Obstruction: Consequently a vanishing rotation-averaged one-point order parameter cannot rule out the proposed phase. A proof must establish the proper bond-orientational correlations together with positional decorrelation for the actual Gibbs law, with defects and thermodynamic limits controlled. Verification: author_checked_partial. No proof file recorded.

### P0322. Critical gap-correlation decay in the one-dimensional s=1 Riesz gas

**Source.** Boursier: Decay of correlations and thermodynamic limit for circular Riesz gas (boursier_riesz_decay_2022), Section1.2,PDF4.

**Statement.** Determine the sharp decay of ordered-gap correlations in the critical one-dimensional Riesz gas at s=1, where the source conjectures a distance^-1 times logarithmic correction. Ledger caveat: The source treats s=1 as a distinct marginal regime omitted from its theorems for s<1 and s>1. This entry does not count separate values of an unknown logarithmic exponent.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: The harmonic heuristic at the marginal exponent leads to a logarithmically divergent Fourier symbol. The identity sum_(n>=1) cos(n*theta)/n=-log(2*sin(theta/2)) for0<theta<2*pi behaves as log(1/theta) near0. Inverting such a symbol suggests a slowly varying factor1/log(1/theta), rather than an ordinary power-law inverse. Obstruction: The actual random Hessian must first be compared with this translation-invariant harmonic operator, and a precise inverse-Fourier estimate with correct gap observable is required. The calculation does not identify the logarithmic exponent or prove a critical decay bound. Verification: author_checked_partial. No proof file recorded.

### P0323. DLR characterization of the circular Riesz thermodynamic limit

**Source.** Boursier: Decay of correlations and thermodynamic limit for circular Riesz gas (boursier_riesz_decay_2022), Section1.3,PDF5.

**Statement.** Prove that the thermodynamic limit of the circular one-dimensional Riesz gas constructed in Boursier satisfies the anticipated infinite-volume DLR equations. Ledger caveat: The paper proves convergence of the finite circular laws for0<s<1 and s>1 and explicitly says the DLR characterization remains open. This is existence of the specification identity for that limit, distinct from uniqueness among all Gibbs states.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: Weak convergence of joint laws does not automatically preserve a conditional specification that depends increasingly sensitively on the conditioning variable. Let Y be uniform on[0,1] and X_n=1 if the fractional part of n*Y is below1/2. Every X_n is a measurable deterministic function of Y, yet (Y,X_n) converges weakly to a uniform Y independent of a fair Bernoulli variable. Obstruction: The Riesz problem therefore needs continuity or uniform integrability of the renormalized exterior potential and conditional partition functions, beyond local weak convergence. The example diagnoses that missing interchange; it is not a Riesz counterexample. Verification: author_checked_partial. No proof file recorded.

### P0324. Analyticity of the one-dimensional Riesz free energy

**Source.** Boursier: Decay of correlations and thermodynamic limit for circular Riesz gas (boursier_riesz_decay_2022), Section1.3,PDF5.

**Statement.** Prove the expected real analyticity in inverse temperature beta of the thermodynamic free energy of the one-dimensional long-range Riesz gas0<s<1 defined in the source. Ledger caveat: The source discusses deriving twice differentiability from its correlation and convergence results and expects full analyticity. Neither a possible C2 consequence nor convergence of periodic laws is counted as analyticity.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Source-specific calculation, conditional implication or exact obstruction. Result: Finite-volume derivatives of log Z are energy cumulants: the second is a variance and the kth derivative is the kth centered cumulant up to sign. Analyticity in a beta neighborhood requires control at all orders, typically |cumulant_k|/volume bounded by C^k*k!, not merely a two-point decay estimate. Even real-analytic finite-volume functions can converge to a nonanalytic limit: f_n(beta)=sqrt((beta-beta0)^2+1/n) tends to |beta-beta0| for any fixed positive beta0. Obstruction: Uniform higher-order cumulant estimates or a convergent expansion are needed throughout the desired temperature range. The existing two-point control does not by itself provide them. No full analyticity theorem is established here. Verification: author_checked_partial. No proof file recorded.

### P0325. Uniqueness of the microscopic bulk limit of the two-dimensional Coulomb gas

**Source.** Leble: Les log-gas et leurs amis, HDR June2026 (leble_hdr_2026), Section2.3,PDF25.

**Statement.** For beta different from2, does the law of the bulk point configuration of the two-dimensional one-component plasma converge as particle number tends to infinity, rather than only along subsequences? Ledger caveat: The source finite-volume laws and bulk observation points are those in Section2.3. The Ginibre beta=2 case is known. This concerns convergence of the designated finite-volume approximations, not uniqueness of every DLR state.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: The new theorem gives translation invariance, number rigidity and DLR identities for every subsequential limit. These properties need not identify a measure: two distinct measures can satisfy the same invariance and integrability constraints. Even at the elementary sequence level, alternating between two different stationary point-process laws gives a tight sequence with those shared properties but no limit. Obstruction: The missing step is a characterization that uniquely selects the Coulomb bulk law, or a quantitative comparison of all finite-volume boundary approximations. The shared qualitative properties do not prove uniqueness of the subsequential limits. Verification: author_checked_partial. No proof file recorded.

### P0326. High-temperature uniqueness and variational characterization of the two-dimensional plasma

**Source.** Leble: Les log-gas et leurs amis, HDR June2026 (leble_hdr_2026), Section2.4,PDF25.

**Statement.** For sufficiently small positive beta, prove that the two-dimensional one-component plasma has a unique DLR solution and that this is also the unique free-energy minimizer. Ledger caveat: The two descriptions form the source liquid-phase uniqueness objective. Exponential decay of correlations is a separate observable recorded in P0327. Uniqueness of a bulk approximation alone would not establish this stronger assertion.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: The usual absolute-integrability high-temperature cluster estimate does not apply directly to the logarithmic pair interaction. In two dimensions its force has magnitude1/r, whose integral over1<|x|<R is2*pi*(R-1). Multiplication by an arbitrarily small fixed beta still diverges as R tends to infinity. Obstruction: An argument must incorporate the neutralizing background and screening before estimating influences. A direct short-range Dobrushin estimate fails to exploit those cancellations. No uniqueness theorem or equivalence of all DLR states with variational minimizers is proved. Verification: author_checked_partial. No proof file recorded.

### P0327. Exponential clustering in the high-temperature two-dimensional plasma

**Source.** Leble: Les log-gas et leurs amis, HDR June2026 (leble_hdr_2026), Section2.4,PDF25.

**Statement.** Prove exponential decay of the truncated two-point correlation function of the two-dimensional one-component plasma for all sufficiently small positive beta. Ledger caveat: The beta=2 Gaussian decay is established. The generic non-Coulomb power-law prediction in P0311 excludes this Coulomb mechanism; this is not another exponent copy of that question.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: Linear Debye screening gives the formal structure factor S(k)=|k|^2/(|k|^2+m^2), with m^2 proportional to beta times the background density. Its truncated-correlation Fourier transform is proportional to -m^2/(|k|^2+m^2). In two dimensions the inverse transform is a multiple of the modified Bessel function K0(m*r), whose large-distance behavior is proportional to exp(-m*r)/sqrt(m*r). Obstruction: The linear-response closure is not proved for the interacting Gibbs law. A rigorous result needs a uniform control of nonlinear correlations and error terms at distances beyond the screening length. The calculation identifies a mechanism, not a clustering theorem. Verification: author_checked_partial. No proof file recorded.

### P0328. Gravitational allocation for the two-dimensional one-component plasma

**Source.** Leble: Les log-gas et leurs amis, HDR June2026 (leble_hdr_2026), Section3.3 perspective,PDF30.

**Statement.** Construct and control the gravitational allocation from Lebesgue measure to the infinite two-dimensional Coulomb gas, in the sense of the proposed extension of the Nazarov-Sodin-Volberg construction; the source says this remains open even at beta=2. Ledger caveat: Existence of some finite-cost stationary transport coupling is already known. The target is the specified gradient-flow allocation, including meaningful cells and sufficient cell-size control.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: Gauss-law heuristics relate unit source strength to unit cell area, provided the flow is defined, flux through the cell boundary vanishes and trajectories are captured. Those hypotheses do not give a second-moment bound on allocation distance. A random cell-radius bound R that is finite almost surely can still have infinite second moment: choose P(R>r)=1/r for r>=1, giving E R^2=2*integral r*P(R>r)dr=infinity. Obstruction: The missing work includes renormalizing the infinite force field, ruling out escaping trajectories and quantifying cell tails. The already established abstract transport coupling is not necessarily generated by the gravitational field. Verification: author_checked_partial. No proof file recorded.

### P0329. Jancovici-Lebowitz-Manificat discrepancy deviations for general beta

**Source.** Leble: Les log-gas et leurs amis, HDR June2026 (leble_hdr_2026), Section2.2,PDF21;Serfaty Section10.3,PDF224.

**Statement.** Prove the predicted charge-discrepancy deviation exponents for the two-dimensional Coulomb gas at general beta, especially the unresolved small-deviation regime alpha>1/2 close to1/2. Ledger caveat: For a microscopic-radius R disk, the predicted powers are phi(alpha)=2*alpha-1 for1/2<alpha<=1,3*alpha-2 for1<=alpha<=2,and2*alpha foralpha>=2. All regimes are one family. Beta=2 and some larger-deviation regimes are known; no unit leading constant is asserted.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: If the discrepancy were Gaussian with variance c*R, a threshold R^alpha would cost logarithmic probability of order -R^(2*alpha-1)/(2*c). This exactly reproduces the first predicted power. It cannot produce the second and third powers: using the same Gaussian ansatz at alpha=3 would predict exponent5, whereas the large-excess prediction is6. Obstruction: A proof must control moderate deviations far beyond an ordinary CLT and account for nonlinear electrostatic cost of large charge rearrangements. The Gaussian calculation explains only one branch conditionally; it proves no rare-event asymptotic for the plasma. Verification: author_checked_partial. No proof file recorded.

### P0330. Higher-order free-energy expansion of the two-dimensional Coulomb gas

**Source.** Serfaty: Lectures on Coulomb and Riesz gases,2024 (serfaty_coulomb_lectures_2024), Section1.3,PDF21;Section9.3,PDF199-201.

**Statement.** Establish the predicted free-energy expansion beyond the thermodynamic order-N term for general beta in the two-dimensional logarithmic gas, including the proposed boundary, logarithmic and order-one contributions. Ledger caveat: The family of coefficients is one question. Determinantal special cases and the order-N theorem are already established. The preliminary book has visible normalization inconsistencies in the schematic formula on PDF200; exact coefficients must be matched to its proved formula9.3.5 before use.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: An exact beta=2 baseline is the planar density proportional to product_(i<j)|z_i-z_j|^2 * exp(-N*sum|z_i|^2), with labelled-particle Lebesgue normalization. Orthogonality of complex monomials gives Z_N=N!*pi^N*product_(k=0)^(N-1)k!*N^(-N*(N+1)/2). Stirling and the Barnes-G expansion yield a term (N/2)*log N and a logarithmic term(5/12)*log N. They therefore check normalization and show why an unqualified(1/4)*N*log N in a schematic beta-dependent formula cannot be copied literally. Obstruction: These exact identities are known determinantal calculations, not a solution at general beta. Beyond beta=2, one needs uniform boundary free-energy corrections and an order-one determinant/field-theory identification with controlled remainder. No generic higher-order expansion is proved. Verification: author_checked_partial. No proof file recorded.

### P0331. Sharpness of the Debye scale in Coulomb local laws

**Source.** Serfaty: Lectures on Coulomb and Riesz gases,2024 (serfaty_coulomb_lectures_2024), Equations8.0.1-8.0.2,PDF163;conjecturePDF164.

**Statement.** Prove the conjectured sharpness of the temperature-dependent minimal Debye scale in the Coulomb local-energy laws, including the proposed Poissonian behavior below that scale. Ledger caveat: The source scale is rho_beta=C*max(1,sqrt(chi(beta)/beta)) in microscopic coordinates; chi(beta) is the source dimension-dependent correction. In d>=3 it is1. All temperature and dimension cases are one scale-sharpness question.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: The linear screened structure factor S(k)=k^2/(k^2+m^2), m of order sqrt(beta), is close to1 for frequencies k much larger than m and small for k much smaller than m. Thus it predicts Poisson-sized fluctuations for wavelengths much shorter than beta^-1/2 and suppressed fluctuations above that length. This is consistent with the d>=3 scale in the theorem. Obstruction: This is only a linear-response diagnostic. Sharp failure of the nonlinear energy estimate8.0.1 below rho_beta is stronger than a structure-factor heuristic and needs a lower bound or a Poisson limit in a specified joint temperature-volume regime. The two-dimensional correction is not justified by this calculation. Verification: author_checked_partial. No proof file recorded.

### P0332. Regularity threshold for bounded Coulomb-gas linear-statistic fluctuations

**Source.** Serfaty: Lectures on Coulomb and Riesz gases,2024 (serfaty_coulomb_lectures_2024), Section10.3,PDF223.

**Statement.** Determine the sharp regularity threshold on test functions for bounded fluctuations of linear statistics of Coulomb gases, beyond the established smooth-function CLTs and selected indicator results. Ledger caveat: The source poses a general regularity question. Different dimensions and smoothness scales are grouped. A Sobolev prediction from the limiting Gaussian field is not automatically a uniform finite-particle variance theorem.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: In the two-dimensional bulk Gaussian-field approximation, the limiting variance is proportional to the Dirichlet energy integral|grad f|^2. Mollify an indicator of a smooth bounded region over a boundary layer of thickness epsilon. Its gradient has magnitude of order epsilon^-1 over area of order perimeter*epsilon, giving energy of order perimeter/epsilon. This demonstrates why merely approximating an indicator by smooth functions does not preserve a uniform variance bound. Obstruction: One needs uniform estimates in the mollification scale, identification of the maximal admissible function space and treatment of boundary terms. The smooth CLT cannot be applied with an increasingly rough test function without such uniformity. Verification: author_checked_partial. No proof file recorded.

### P0333. Multivariate fluctuation limits for empirical transport with Euclidean cost

**Source.** del Barrio et al: Distributional Limit Theory for Optimal Transport,July2026revision (ot_limit_survey_2026), Problem1,PDF29;Theorem3.1 baselinePDF10.

**Statement.** Find broad conditions in dimension d>1 under which sqrt(n)*(T1(P_n,Q)-E T1(P_n,Q)) converges weakly, and identify when its limit is Gaussian. Ledger caveat: T1 uses Euclidean distance, not its square. Known discrete-support and one-dimensional limits are excluded from new-solution claims. Trivial point-mass targets do not answer the intended general criterion.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: If Q is a point mass at y, T1(P_n,Q) is exactly the sample mean of ||X_i-y||, so the classical CLT applies under a finite second moment. This verifies one known degenerate baseline. For general Q the Efron-Stein linearization would reduce the question to convergence in L2 of empirical optimal dual potentials to a single population potential; Euclidean cost can have nonunique transport structures. Obstruction: The known special cases show both behaviors but provide no general multivariate condition controlling uniqueness and convergence of the relevant dual potential. Nonuniqueness and nondifferentiability cannot be dismissed solely from finite moments. Verification: author_checked_partial. No proof file recorded.

### P0334. Necessary and sufficient conditions for an Lp quantile-process limit

**Source.** del Barrio et al: Distributional Limit Theory for Optimal Transport,July2026revision (ot_limit_survey_2026), Problem2,PDF29;Sections2.2-2.4,PDF7-9.

**Statement.** Find necessary and sufficient conditions for sqrt(n)*(F_n^(-1)-F^(-1)) to converge weakly as an Lp(0,1)-valued random element, removing unnecessary endpoint monotonicity assumptions. Ledger caveat: The p=1 criterion is established in Beare-Kaji2502.01254. The remaining p>1 family is one question. The paper gives sufficient conditions involving J_p(P) and endpoint monotonicity.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: For a positive density f the only possible local Gaussian limit is B(t)/f(F^(-1)(t)), where B is a Brownian bridge. Its expected Lp norm to the pth power equals E|Z|^p times J_p(P), with J_p(P)=integral_0^1 [t*(1-t)]^(p/2)/f(F^(-1)(t))^p dt and Z standard normal. This makes the necessary tail-integrability quantity explicit. Obstruction: Local finite-dimensional convergence and finiteness of the candidate limit norm do not establish tightness of the empirical quantile tails. The missing uniform endpoint control without monotonicity is precisely the unresolved sufficiency direction. No complete criterion is proved. Verification: author_checked_partial. No proof file recorded.

### P0335. Nondegenerate centered fluctuations of null quadratic empirical transport

**Source.** del Barrio et al: Distributional Limit Theory for Optimal Transport,July2026revision (ot_limit_survey_2026), Problem3 and equation42,PDF29.

**Statement.** Determine whether n*(T2(P_n,P)-E T2(P_n,P)) has a nondegenerate limit for the uniform measure on the unit square, identify that limit, and determine the correct analogous behavior in other dimensions. Ledger caveat: T2 is squared Euclidean transport cost. All dimension extensions are grouped. The usual sqrt(n) theorem gives zero in this null case; known one-dimensional limits are starting points.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: The linearized matching-energy model gives n times the centered cost as a quadratic Fourier sum of terms (|Z_k|^2-1)/|k|^2. For independent normalized Gaussian modes, the variance is proportional to sum_(0<|k|<=K)|k|^-4, which converges in d<4, grows as log K in d=4, and as K^(d-4) in d>4. This makes a dimension-independent n normalization doubtful. Obstruction: One must control the nonlinear optimal matching remainder at fluctuation scale and identify dependence among empirical Fourier modes as the cutoff grows. The Gaussian surrogate neither proves the square conjecture nor refutes a proposed empirical limit in higher dimension. Verification: author_checked_partial. No proof file recorded.

### P0336. Selected limit of empirical Euclidean transport between separated rectangles

**Source.** del Barrio et al: Distributional Limit Theory for Optimal Transport,July2026revision (ot_limit_survey_2026), Problem4,PDF29-30.

**Statement.** For independent uniform samples from [0,1]^2 and [2,3]x[0,1], find the limiting empirical optimal transport plan for Euclidean distance as sample size tends to infinity. Ledger caveat: The empirical plan is almost surely a map, but the population problem has many optimal couplings. The task is to identify the plan selected by empirical optimization, not merely its limiting cost2.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: Write a horizontal displacement d=y1-x1 in[1,3] and vertical displacement h=y2-x2. The excess Euclidean cost over horizontal displacement is sqrt(d^2+h^2)-d=h^2/(sqrt(d^2+h^2)+d). Since |h|<=1, this lies between h^2/(sqrt(10)+3) and h^2/2. Therefore any sequence of couplings with cost tending to2 must have mean squared vertical displacement tending to0. Obstruction: Any subsequential limit is thus supported on equal vertical coordinates, as expected, but the horizontal coupling remains undetermined. Every such population coupling costs2. Resolving the lower-order empirical selection mechanism remains open here. Verification: author_checked_partial. No proof file recorded.

### P0337. Consistent estimation of the Sinkhorn null-limit spectrum

**Source.** del Barrio et al: Distributional Limit Theory for Optimal Transport,July2026revision (ot_limit_survey_2026), Theorem4.5 and following paragraph,PDF20-21.

**Statement.** Construct consistent estimators of the nonnegative spectral sequence determining the weighted chi-square null limit of the empirical Sinkhorn divergence. Ledger caveat: The source writes the limit as epsilon/2 times sum lambda_i^2*N_i^2, with sum lambda_i^2 finite. The target includes enough spectral control to approximate the full limiting law, not merely a fixed finite list.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: If a finite-rank approximation of the relevant positive operator were consistently estimated in operator norm, Weyl bounds would give convergence of every fixed ordered eigenvalue. This does not control the weighted chi-square tail. As a diagnostic, diagonal matrices with n eigenvalues all equal to1/n have operator norm tending to0 and every fixed eigenvalue tending to0, while their trace stays1. Obstruction: The required estimator must control the trace-class weights lambda_i^2, or an equivalent uniform tail, while estimating the population-dependent linearized Schrodinger operator. The fixed-rank perturbation argument supplies no such uniform tail bound. Verification: author_checked_partial. No proof file recorded.

### P0338. Minimax rates for conditional optimal-transport maps

**Source.** del Barrio et al: Distributional Limit Theory for Optimal Transport,July2026revision (ot_limit_survey_2026), Section6.2 concluding paragraph,PDF29.

**Statement.** Determine sharp minimax rates for estimating conditional optimal-transport maps in the regression setting referenced by the source. Ledger caveat: The source notes available nonsharp mixing-based rates. A meaningful minimax statement must specify covariate smoothness, response regularity, loss and reference measure; the entry records that unresolved model-class dependence rather than inventing a universal exponent.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: In a location-family submodel Y=m(X)+Z with known noise law and a reference matching Z, the conditional transport map is T_x(u)=m(x)+u. Thus estimating the map under integrated squared error is at least as hard as estimating the regression function m: the map difference is exactly the shift-estimation error for every reference point u. Obstruction: This reduction supplies a lower-bound route but no sharp rate for the general conditional map. One must combine covariate localization with the response-dimensional transport difficulty and prove a matching estimator under precisely specified regularity assumptions. Verification: author_checked_partial. No proof file recorded.

### P0339. Sample complexity of Gromov-Wasserstein plans and dual potentials

**Source.** del Barrio et al: Distributional Limit Theory for Optimal Transport,July2026revision (ot_limit_survey_2026), Section5.2 concluding paragraph,PDF27.

**Statement.** Determine sample-complexity bounds for Gromov-Wasserstein optimal plans and associated dual potentials, beyond known bounds for the optimal cost. Ledger caveat: The source explicitly says this complexity is unknown. Plans and potentials are grouped as the source optimizer-estimation question. Nonuniqueness and metric-space isometries require an identified loss or a set-valued target.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Explicit model calculation or source-specific limiting obstruction. Result: Cost convergence cannot determine a selected optimizer when symmetries create multiple optima. For a uniform two-point metric space with distance1, both the identity coupling and the swap coupling have zero Gromov-Wasserstein distortion between the space and itself. Their supports are disjoint. Alternating those two plans preserves exactly zero cost and has no limit as a labelled coupling. Obstruction: A rate theorem needs either a quotient by symmetries, distance to the full optimizer set, or an explicit unique selection with stability assumptions. The known cost rate alone cannot give a plan or potential rate in a fixed labelled norm. Verification: author_checked_partial. No proof file recorded.

### P0340. Growth of the minimal drawn length of critical beta-splitting trees

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem14,PDF54-55.

**Statement.** Determine the expected total vertical length in the minimal integer-height drawing of DTCS(n); the source specifically proposes growth on the scale n*(log n)^4. Ledger caveat: The source drawing recursion is authoritative. This is expected drawn length, not ordinary total edge count or the continuous-time total length.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: candidate_full_solution. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: For every full binary tree, drawn length equals the sum of all internal subtree heights plus the root height, and is at most the sum of all leaf depths. Hence its expectation is O(n*log^2 n), already refuting the proposed rate. A stronger proof gives E drawn length/n -> sum_(m>=2) a(m)*E height(T_m)/m, a finite constant at least2. A geometric halving bound proves E height(T_m)=O(log^2 m), and a uniform dyadic occupation bound controls the series tail. Obstruction: The source scale is contradicted and a linear expectation limit is derived, but there is no independent review or originality certificate. No LLN, variance, CLT or closed form for the series constant is claimed. Verification: author_checked_candidate. Proof file: proofs/P0340_beta_tree_drawn_length_counterexample_candidate.md.

### P0341. Uniform occupation estimates and the polynomial-test ansatz

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem8 and Ansatz20,PDF39-40.

**Statement.** Find quantitative bounds on the tagged harmonic-descent occupation probabilities and determine the validity of the displayed weighted-convergence ansatz for all nonnegative polynomially bounded test sequences. Ledger caveat: Brandenberger-Chin-Mossel2505.24821 supplies fixed-state and growing-state error bounds and a decaying-test special case. Those established advances are credited; the full source ansatz permits bounded sparse functions.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: candidate_partial_counterexample. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: The bounded test f(j)=1 when j is a power of2 and0 otherwise has finite limiting sum S because a(2^r)=O(r*2^-r). Along n=2^K, the certain root visit contributes1 in addition to every fixed initial set of terms tending to S. Thus the liminf is at least S+1, contradicting the proposed limit S. The test g(j)=j*f(j) separately refutes the divergent-series clause: the actual sum is at least2^K whereas the proposed truncated sum is of order K^2. Obstruction: The unrestricted ansatz is false. A comprehensive sharp two-parameter error theory and the best admissible class of tests remain unresolved here; therefore the broader numbered problem is only partly answered. Verification: author_checked_partial. Proof file: proofs/P0341_beta_tree_sparse_occupation_counterexample_candidate.md.

### P0342. Transferring a stationary fringe-process CLT to finite beta-splitting trees

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem12,PDF44-45.

**Statement.** Determine whether a CLT for a functional along the stationary infinite fringe process necessarily gives the same CLT for its sum over the leaves of DTCS(n). Ledger caveat: The source gives no quantitative locality condition in the numbered question. The explicit example below has a degenerate Gaussian limit; a strictly positive variance or fixed-neighborhood interpretation is retained as an unresolved scope restriction.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: candidate_partial_counterexample. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: Define a bounded continuous functional to be0 on infinite trees and n^-1/4*(B_n-p_n) on finite n-leaf trees, where B_n indicates that the smaller root child has at most floor(sqrt n) leaves and p_n is its exact probability. The original degree-two root and n are unchanged by leaf rerooting. Thus every infinite fringe sum is0, while the finite sum divided by sqrt n is n^1/4*(B_n-p_n). The split law gives p_n ->1/2, so these finite normalized sums are not tight. Obstruction: This disproves transfer if zero-variance Gaussian limits are admitted. For a class containing a nondegenerate fringe CLT functional and closed under this perturbation, a universal transfer rule also fails by a tight-difference argument. A concrete positive-variance or quantitatively local transfer theorem remains unsolved. Verification: author_checked_partial. Proof file: proofs/P0342_beta_tree_fringe_transfer_scope_counterexample.md.

### P0343. Correlations of critical-tree leaves at mesoscopic separation

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem1,PDF22.

**Statement.** For two leaves separated by r_n positions in the cyclic interval representation, prove that their continuous-height correlation tends to1-alpha when log(r_n)/log(n) tends to alpha in[0,1]. Ledger caveat: The macroscopic alpha=1 case is already established in the corrected published Aldous-Pittel result. All separation exponents form one question, not separate variants.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: The proposed common-ancestry approximation shares a Brownian path up to time s=1-alpha and then uses two independent continuations. For X=B_s+B1_(1-s) and Y=B_s+B2_(1-s), the variances are1 and covariance is s, so the predicted correlation is exactly1-alpha. This isolates the common time that a two-tagged-clade limit must identify. Obstruction: One needs a two-leaf process approximation valid for moving separations and sufficient uniform second-moment control to pass from weak limits to covariances. A one-leaf CLT alone proves neither requirement. Verification: author_checked_partial. No proof file recorded.

### P0344. Heights of prescribed interval-labelled leaves in the critical tree

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem2,PDF22-23.

**Statement.** Analyze the height distribution of a prescribed leaf i(n) in the original interval-splitting DTCS(n) and CTCS(n) models. Ledger caveat: Uniformly randomized leaf labels change the question. Boundary leaves and moving interior labels are one prescribed-location family.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: For the leftmost leaf the next size has the un-biased split law q(m,i), whereas a uniformly selected leaf uses size bias. Conditional on choosing the smaller left child, the leading weights are proportional to1/i. Therefore for0<u<1, the probability of I<=m^u, conditional on I<=m/2, tends to u, because the ratio of the relevant harmonic sums tends to u. This yields the proposed logarithmic contraction log I/log m ->Uniform(0,1). Taking another logarithm suggests a renewal drift of1/2 per split and height around2 log log n. Obstruction: The state-dependent renewal approximation must be controlled through the terminal small-size regime, and moving interior locations require an additional position coordinate. No full law, CLT or continuous-time analogue is proved here. Verification: author_checked_partial. No proof file recorded.

### P0345. The leading constant for maximum discrete critical-tree height

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem4,PDF28.

**Statement.** Prove that the maximum graph height of DTCS(n), divided by(log n)^2, converges in probability and identify its constant. Ledger caveat: The continuous-time maximum question was answered in the August2026 preprint; it is a different observable and is excluded separately. All conjectured constants for the discrete law are one problem.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: A tagged chain halves its size with conditional probability at least1/(2H_(n-1)); coupling to a negative-binomial waiting time and taking a union bound over leaves gives E maximum height=O(log^2 n). The uniform random-leaf CLT gives the lower bound maximum height/(log n)^2 >=3/pi^2-o(1) in probability. Thus the order can be obtained without identifying the extremal constant. Obstruction: The upper estimate is too loose to determine a common limit. Dependence among candidate deep branches and the tail behavior beyond a typical-leaf CLT remain the obstruction. Verification: author_checked_partial. No proof file recorded.

### P0346. Distinct and repeated clade shapes in critical beta-splitting trees

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem7,PDF39.

**Statement.** Determine the distributions and growth of the number of distinct clade shapes, the largest repeated clade and the smallest missing clade shape in DTCS(n). Ledger caveat: The three linked occupancy observables are grouped as one source question. The size-one clade and fixed-shape CLTs are known baselines.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: For any fixed clade shape chi of size m with positive model probability, its expected count is asymptotically n*p(chi)/m. The later fixed-clade variance bound is O(n), so Chebyshev gives probability O(1/n) that its count is zero. For any fixed finite list of distinct positive-probability shapes, all are therefore present with probability tending to1. It follows that the number of distinct shapes tends to infinity in probability, while it is always at most n-1 for internal clades. Obstruction: This supplies no growth rate: the constants and count estimates are not uniform over growing shapes. Largest repetitions and smallest missing shapes need joint tail information across an exponentially growing family. Verification: author_checked_partial. No proof file recorded.

### P0347. Distributions of balance indices for critical beta-splitting trees

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem10,PDF41-43.

**Statement.** Analyze the distributions of the source balance indices under DTCS(n), beyond the preliminary expectation heuristics. Ledger caveat: Indices and parameter variants are grouped. Some source one-split constants are incorrect; correcting them is partial progress, not a solution of the distributional problem.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: candidate_partial_counterexample.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: For a split I distributed by q(m,i), the exact quadratic toll is E(m-2I)^2=m^2-2m*(m-1)/H_(m-1), hence asymptotic to m^2 rather than the source m^2/4. Also E min(I,m-I)<=m/H_(m-1), so E|m-2I|=m-O(m/log m), rather than m/2. If S is the external path length and C the Colless index, S-C is the sum of2*min(child sizes). Therefore E(S-C)<=2n*sum_m a(n,m)/H_(m-1)=2n*E continuous leaf depth=O(n log n). Since E S~(3/pi^2)n log^2 n, E C has that same leading constant, twice the source heuristic coefficient. Obstruction: The mean Colless correction and one-split quadratic correction do not identify variances, normalized laws or joint distributions of the balance indices. Those remain unsolved here. Verification: author_checked_partial. No proof file recorded.

### P0348. The drawn width profile of a critical beta-splitting cladogram

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem15,PDF55.

**Statement.** Analyze the process counting vertical drawing segments crossing each integer height interval in the minimal cladogram representation of DTCS(n). Ledger caveat: The process is measured upward from leaves in the source minimal drawing. Ordinary breadth by distance from the original root is a different quantity.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: For every finite tree, W(h)=number of internal clades whose own graph height exceeds h, plus1 if the whole-tree height exceeds h. Thus E W_n(h)/n converges, for each fixed nonnegative integer h, to w(h)=sum_(m>=2) a(m)*P(height(T_m)>h)/m. The dyadic occupation bound in P0340 controls the tails uniformly, justifying the passage from fixed sizes to the full sum. Summing the limiting mean profile over h gives the linear expected-length constant from P0340. Obstruction: Only the limiting mean profile and its summability are obtained. Concentration, covariance, a random profile scaling limit and height regimes growing with n remain unproved. Verification: author_checked_partial. No proof file recorded.

### P0349. Complex powers of clade sizes in the critical tree

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem16,PDF56.

**Statement.** Give a detailed asymptotic analysis of the sum of complex powers of all internal clade sizes in DTCS(n). Ledger caveat: All powers form one family. The p=1 expectation and polynomially decaying weighted-sum cases are established baselines; they are not new open solutions.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: For real p<1, the normalized expectation is sum_m a(n,m)*m^(p-1). A dyadic block contains at most O(log m) expected tagged visits, uniformly in n, so its contribution is O(log m*m^(p-1)); this is summable over dyadic scales. Hence the limit equals sum_m a(m)*m^(p-1), consistent with the later decaying-test theorem. At p=1 the known expectation grows as n*log^2 n. For p>1, the same block estimate yields an upper bound O(n^p log n), while the root alone supplies n^p. Obstruction: The intermediate logarithmic factor, exact constants, variances and normalized laws in the nondecaying and complex regimes remain unresolved. The known p<1 limit is only a baseline check. Verification: author_checked_partial. No proof file recorded.

### P0350. A branchpoint point-process scaling limit of the critical fringe tree

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem17,PDF57.

**Statement.** Study the rescaled branchpoint-position process suggested by the infinite discrete fringe tree of the critical beta-splitting model. Ledger caveat: The source proposes a scaling-limit program without specifying a proved normalization. The task is recorded at that scope, rather than inventing an established limit law.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: The first upward jump from a distinguished leaf to an ancestor of size j has exact probability6/[pi^2*(j-1)^2]. Consequently the first-ancestor size has tail asymptotic6/(pi^2*m) and infinite mean. This immediately rules out using a finite-mean renewal heuristic for the raw ancestor sizes. Obstruction: Later upward transitions depend on the current clade size, so they are not independent copies of the first jump. A point-process limit requires a scale and joint control of these dependent jumps and their spatial positions. Verification: author_checked_partial. No proof file recorded.

### P0351. Connections between the critical fragmentation and beta(2,1) coalescent

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem19,PDF58.

**Statement.** Identify precise probabilistic connections between CTCS(infinity) and the beta(2,1) coalescent beyond their already known common tagged-subordinator and leading-CLT relations. Ledger caveat: The equality in law of selected frequency processes is already stated in the source. The open objective concerns stronger structural connections, not reproving that marginal identity.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record recorded in the ledger). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact tree identity, source-specific recurrence or explicit limiting obstruction. Result: A literal time reversal of the finite binary fragmentation cannot equal the usual beta(2,1) coalescent: on three labelled blocks the latter has a positive rate for merging all three at once. Its Lambda-coalescent triple-merger rate is integral x*2x dx=2/3. The finite fragmentation has only binary splits, so reversing any of its jump paths produces only binary mergers. Obstruction: This counterexample to naive reversal does not rule out a size-biased duality, a transformation of time or labels, or another coupling. The shared subordinator alone does not specify such a full-process relation. Verification: author_checked_partial. No proof file recorded.

### P0352. Maximum continuous height of the critical tree

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem3,PDF24.

**Statement.** Maximum continuous height of the critical tree Ledger caveat: The August18,2026 preprint proves a law of large numbers with constant2 and a mixed Gumbel law, contradicting the older suggested constant1.878. The complete maximum-height proof was read; its martingale integrability result uses an external theorem not independently rechecked here.

**Status.** Historical status: source_says_open. Current-literature status: resolution_claimed_in_literature (no status-search record recorded in the ledger). Resolution record: beta_fragmentation_2026, Theorem2.12 and Remark2.13,PDF10-11;complete maximum-height argumentPDF20-25. Admission: not admitted; result_status: literature_resolution_claimed_not_independently_certified.

**Our work.** Not admitted (result_status: literature_resolution_claimed_not_independently_certified); see the resolution record above. No attempt is recorded for this row in attempts.jsonl.

### P0353. Fixed-clade count CLTs for critical beta-splitting trees

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem5,PDF37.

**Statement.** Fixed-clade count CLTs for critical beta-splitting trees Ledger caveat: The July2025 preprint explicitly answers the fixed-clade count question, with linear variance and a CLT for nontrivial clades. The proof text was read; several initial-index statements need care, including the literal variance-zero range for a size3 clade. This is a source-claimed resolution exclusion, not an independently certified proof.

**Status.** Historical status: source_says_open. Current-literature status: resolution_claimed_in_literature (no status-search record recorded in the ledger). Resolution record: beta_harmonic_asymptotics_2025, Corollary1.4,PDF4;Sections3-4,PDF13-17. Admission: not admitted; result_status: literature_resolution_claimed_not_independently_certified.

**Our work.** Not admitted (result_status: literature_resolution_claimed_not_independently_certified); see the resolution record above. No attempt is recorded for this row in attempts.jsonl.

### P0354. Total continuous-time tree-length variance and CLT

**Source.** Aldous-Janson: Critical beta-splitting random tree II, overview and open problems (beta_splitting_overview), Open Problem6,PDF39.

**Statement.** Total continuous-time tree-length variance and CLT Ledger caveat: The July2025 preprint explicitly answers this question with linear variance and a CLT. The main argument and supporting displayed mean/variance estimates were read, but not every referenced contraction theorem or appendix independently verified. This is a source-claimed resolution exclusion, not a new campaign solution.

**Status.** Historical status: source_says_open. Current-literature status: resolution_claimed_in_literature (no status-search record recorded in the ledger). Resolution record: beta_harmonic_asymptotics_2025, Corollary1.5,PDF4;Section5,PDF17-18. Admission: not admitted; result_status: literature_resolution_claimed_not_independently_certified.

**Our work.** Not admitted (result_status: literature_resolution_claimed_not_independently_certified); see the resolution record above. No attempt is recorded for this row in attempts.jsonl.

### P0355. Endogeny of nonminimal discounted-tree fixed points

**Source.** Aldous and Bandyopadhyay: A survey of max-type recursive distributional equations (aldous_rde_2005), Conjecture34;PDF26-30.

**Statement.** Determine whether every positive-index invariant RTP from Corollary33 and condition39 is nonendogenous. Ledger caveat: The counterexample is restricted to literal zero-mark/unit-weight boundary assumptions. The intended strictly discounted nondegenerate regime remains unsolved.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: candidate_partial_counterexample.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: Set N=2, eta=0, xi1=xi2=1 and Y=1 deterministically. Every ray sum is0, the homogeneous equation fixes Y, condition39 holds, and every iterate from aY has law delta_a. The all-a tree process is invariant and endogenous because its root is constant. Thus the literal conjecture needs an additional assumption. Obstruction: This is a degenerate scope correction, not a solution of the substantive nondegenerate version or a novelty claim. Verification: author_checked_partial. Proof file: proofs/P0355_discounted_RTP_degenerate_scope_counterexample.md.

### P0356. A general boundedness criterion for discounted tree sums

**Source.** Aldous and Bandyopadhyay: A survey of max-type recursive distributional equations (aldous_rde_2005), Open Problem31;PDF26-28.

**Statement.** Characterize when the supremum over rays of the sum of positive marks multiplied by ancestral edge weights is almost surely finite. Ledger caveat: Includes random discounts and dependent mark/offspring vectors. Aidekon-Hu-Shi2025 and Zhang2026 solve substantial regimes, which are credited rather than counted as new results.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: On a deterministic m-ary tree with discount c=m^-H, take positive marks with tail x^-1/H*(log x)^-r for large x. Integration of the moment tail shows E eta^(1/H) is finite exactly when r>1. Zhang2026 Theorem1 then gives boundedness exactly for r>1 in this example. Both r<=1 and r>1 have the same tail exponent zeta=1/H=tstar, so a criterion using that exponent alone cannot resolve the critical boundary. Obstruction: This exact critical example is a consequence of a published preprint theorem. A necessary and sufficient criterion for general random discounts and mark/offspring dependence is not obtained. Verification: author_checked_partial. No proof file recorded.

### P0357. Rays with persistent extremal branching-random-walk local times

**Source.** Aidekon-Hu-Shi: Boundedness of discounted tree sums (discounted_trees_2024), Open question1(i),(ii);PDF2-5.

**Statement.** Determine whether the supremum over rays of the normalized liminf of level local times is positive and finite, with normalization log(n)/n under Theorem1.2 and1/n^2 under Theorem1.6(ii), and identify its value. Ledger caveat: The two regimes of this single numbered local-time question are grouped. The source already determines the corresponding levelwise maxima and certain limsups.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: In the boundary regime Theorem1.6(ii) immediately bounds the requested supremum of liminfs between0 and tstar/(2*theta). Interchanging the optimizing ray with liminf cannot justify positivity. On the compact space of binary sequences, f_n(x)=1{x_n=1 and x_(n+1)=0} has sup_x f_n=1 for every n, but every x has liminf_n f_n(x)=0 because the pattern10 cannot occur at every sufficiently large position. Obstruction: A single infinite ray must realize high occupation at all sufficiently large levels. Separate favorable rays for each level and existing limsup constructions do not provide that nested compatibility. Verification: author_checked_partial. No proof file recorded.

### P0358. The extremal ray-height constant in a heavy-tailed branching random walk

**Source.** Aidekon-Hu-Shi: Boundedness of discounted tree sums (discounted_trees_2024), Open question2;Theorem1.2;PDF2-5.

**Statement.** Identify the positive finite constant a1 in inf_ray limsup_n V(ray_n)/sqrt(n*log n)=a1 under Theorem1.2. Ledger caveat: This is the value of the source constant, not the already established existence theorem. Its full tilted-tail and logarithmic moment assumptions are retained by reference.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: Rescaling every displacement by c>0 preserves the theorem class with tstar replaced by tstar/c: the tilted moment measure transforms by x->cx, its positive mean is multiplied by c, and the tail lower bound retains the allowed polynomial form after changing constants or exponents. Pathwise the variational quantity is multiplied by c. Therefore any proposed distribution-free numerical value of a1 is impossible; a valid formula must transform homogeneously under spatial scaling. Obstruction: The upper and lower constructions depend on rare negative drops and reproduction. Their sharp matching coefficient is not extracted here; dimensional consistency only restricts possible formulas. Verification: author_checked_partial. No proof file recorded.

### P0359. The multifractal spectrum of extremal ray local times

**Source.** Aidekon-Hu-Shi: Boundedness of discounted tree sums (discounted_trees_2024), Open question3;PDF4-5.

**Statement.** Determine the Hausdorff dimension of rays with limsup, or liminf, N_ray^n/n^2=a under Theorem1.6(ii). Ledger caveat: All a and the related limsup/liminf spectra form one source question. Dimension uses the usual generation ultrametric on the tree boundary.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: Write A=tstar/(2*theta). The source levelwise maximum theorem implies that for every ray limsup N_ray^n/n^2<=A, on one common probability-one event. Hence the level sets in the question are empty for a>A. It is insufficient to count high-local-time vertices at isolated levels: Hausdorff covers use generation depths, whereas the local-time level n is a spatial coordinate and its visits may occur over widely separated generations. Obstruction: For0<a<=A, a sharp upper cover estimate and a lower-bound measure supported on compatible recurrent rays are both missing. No positive-dimensional spectrum is claimed. Verification: author_checked_partial. No proof file recorded.

### P0360. Does frozen-percolation endogeny imply unrestricted almost sure uniqueness?

**Source.** Rath-Swart-Szoke: A phase transition between endogeny and nonendogeny (frozen_transition_2021), Question1 and discussion;PDF7-9.

**Statement.** When the burning-time RTP is endogenous, must all solutions to the frozen-percolation equation driven by the same innovations agree, even without stationarity, adaptation or subtree independence? Ledger caveat: Includes the source conjecture for geometric freezing sets theta<1/2; these are not counted as separate parameter questions.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: Let A be the antitone map on proposed frozen sets defined by the percolation equation. If F is any fixed point then repeated antitonicity gives A^(2k)(empty)<=F<=A^(2k+1)(empty), after ordering the alternating iterates by inclusion. Thus equality of the even and odd limiting envelopes would prove uniqueness without distributional assumptions. The source observes that for theta>=1/2 the second iterate is empty, so these envelopes can remain the trivial two-cycle even in an endogenous regime. Obstruction: For theta<1/2 the required collapse of the envelopes is unproved here. For1/2<=theta<=theta_star the elementary envelope method is specifically too coarse, despite known endogeny. Verification: author_checked_partial. No proof file recorded.

### P0361. Uniqueness of the nondiagonal scale-invariant frozen-percolation coupling

**Source.** Rath-Swart-Szoke: A phase transition between endogeny and nonendogeny (frozen_transition_2021), Conjecture15;PDF10-11.

**Statement.** For theta_star<theta<=1, prove that the diagonal and minimal bivariate fixed points are the only solutions in the source space M_theta^(2). Ledger caveat: The theorem for theta=1 is established. Symmetry, the exact marginal rho_Xi, the union-tail bound and invariance under every geometric scaling are mandatory.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: A tempting proposed continuum of fixed points is the convex mixture nu_p=p*nu_diag+(1-p)*nu_min. It has the required marginals and scaling, but the branching update is nonlinear: with two independent child pairs, T2(nu_p)=p^2*T2(nu_diag)+(1-p)^2*T2(nu_min)+2p(1-p)*C, where C is the symmetrized cross-input output law. Since the endpoints are fixed, the mixture is fixed only if C=(nu_diag+nu_min)/2 for0<p<1. Obstruction: No identity forces the cross-input law to equal the endpoint average. Controlling the nonlinear recurrence and ruling out further scale-invariant solutions remain unresolved. Verification: author_checked_partial. No proof file recorded.

### P0362. Constructing frozen percolation on the PWIT as a finite-graph limit

**Source.** Frozen percolation on the binary tree is nonendogenous (frozen_nonendogeny_arxiv), Problem1;PDF12-14.

**Statement.** Construct frozen percolation on the Poisson weighted infinite tree and prove local weak convergence from the complete-graph lightning and deterministic-threshold models cited in Problem1. Ledger caveat: The finite-cluster size distributions and mean-field coagulation limits in the cited literature are established, not a full marked-process local limit.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: Before incorporating freezing, a vertex in K_n has Binomial(n-1,t/n) incident edges activated by rescaled time t, converging to Poisson(t). Joint exploration of any fixed bounded finite neighborhood has collision probability tending to0, giving the usual PWIT local structure. Freezing is not a local continuous function of this structure: a cluster can be frozen by a mark arbitrarily far outside the explored neighborhood. Obstruction: A tight marked-process construction and control of influence from arbitrarily large components are required. Convergence of component masses alone does not identify all local edge histories. Verification: author_checked_partial. No proof file recorded.

### P0363. A finite-graph approximation to frozen percolation on the three-regular tree

**Source.** Frozen percolation on the binary tree is nonendogenous (frozen_nonendogeny_arxiv), Problem2;PDF15.

**Statement.** Show that the canonical frozen-percolation process on the three-regular tree is the local weak limit of a suitable sequence of finite graphs. Ledger caveat: This asks for finite graphs, not the known growing-cluster-threshold approximation on an infinite binary tree.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: For a fixed finite ball B and bounded time t, the chance of any lightning in B is at most |B|*lambda_n*t, which vanishes under the source scaling lambda_n->0. Yet nontrivial freezing must survive in the limiting process. Therefore all limiting freezing in a fixed ball must be transmitted from components extending outside every fixed ball, so simply coupling local clocks and discarding distant vertices cannot prove the result. Obstruction: One needs quantitative control on mesoscopic component growth and transmitted freeze times. The local graph limit and vanishing local lightning do not determine the required boundary randomness. Verification: author_checked_partial. No proof file recorded.

### P0364. Uniqueness in law from the unoriented freezing rule and tree symmetry

**Source.** Frozen percolation on the binary tree is nonendogenous (frozen_nonendogeny_arxiv), Question3 and Theorem1;PDF3,15.

**Statement.** Do the freezing rule and invariance under automorphisms of the three-regular tree uniquely determine the joint law of activation times and frozen edges? Ledger caveat: The known characterization adds oriented subtree-independence. That additional hypothesis is exactly what this question seeks to remove.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: Nonendogeny gives an edge event Z with positive conditional variance given all activation times U. Starting from the canonical joint law, the density1+epsilon*(Z-E[Z|U]), with0<epsilon<1, preserves the full U law and all almost sure freezing rules, but changes E Z by epsilon*E Var(Z|U)>0. This constructs another law satisfying the rule alone. Obstruction: Selecting a distinguished edge breaks full automorphism invariance. No invariant tilt or valid invariant averaging construction is produced, so the actual rule-plus-symmetry question remains unsolved. Verification: author_checked_partial. No proof file recorded.

### P0365. Classifying endogenous laws among all frozen-percolation RDE solutions

**Source.** Frozen percolation on the binary tree is nonendogenous (frozen_nonendogeny_arxiv), Question4;PDF15 and Proposition37,PDF29-30.

**Statement.** Determine which of the complete family of marginal solutions to the marked-binary-tree frozen-percolation RDE have endogenous RTPs. Ledger caveat: The later geometric-freezing-set phase transition supplies a substantial subclass. General closed freezing sets and their RDE laws remain the classification target.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: The scalar marginal equation is integral_[0,t] s*mu(ds)=F(t)^2. It classifies one-dimensional laws but contains no conditional coupling information. Finite freezing sets produce endogenous processes by chronological induction. The geometric sets approaching0 include nonendogenous laws above theta_star, despite each finite truncation having a deterministic chronological construction. Thus finiteness or approximation by finite freezing sets cannot alone establish endogeny of the limit. Obstruction: A condition on the geometry of a general freezing set that controls its bivariate fixed points is missing. No classification beyond the credited finite and geometric cases is obtained. Verification: author_checked_partial. No proof file recorded.

### P0366. The extra randomness in nonendogenous frozen percolation

**Source.** Frozen percolation on the binary tree is nonendogenous (frozen_nonendogeny_arxiv), Question5;PDF15.

**Statement.** Give an explicit characterization of the randomness beyond all activation times needed to construct the binary-tree burning-time process. Ledger caveat: An abstract regular-conditional-distribution sampler is not the requested structural characterization; the source also records triviality of the burning-process tail sigma-field.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: Because the tree is countable and the state space is standard Borel, the whole process can formally be sampled from its conditional law using one independent Uniform(0,1), or countably many uniforms obtained from disjoint digit subsequences. This supplies an existence representation but simply encodes the unknown conditional kernel. Triviality of the process tail sigma-field rules out identifying the missing randomness with a nontrivial variable in that tail. Obstruction: The desired canonical noise space, coupling to the activation field, and geometric interpretation of its independent information are not identified. Verification: author_checked_partial. No proof file recorded.

### P0367. Support of the conditional burning-time law

**Source.** Frozen percolation on the binary tree is nonendogenous (frozen_nonendogeny_arxiv), Question6;PDF15.

**Statement.** Is the conditional law of the root burning time given all activation times supported on the entire interval allowed above the ordinary percolation time Xprime, including the never-burning state? Ledger caveat: Intervals are interpreted inside the source state space [0,1] union {infinity}; no false counterexample is based on literal real numbers between1 and infinity.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: For a Borel set A write q_A=P(X_root in A|U). A conditionally independent replica gives E q_A^2=P(X_root in A,Xprime_root in A), so the explicit bivariate fixed point determines the second moment of q_A. Cauchy-Schwarz yields P(q_A>0)>=P(X_root in A)^2/P(X_root in A,Xprime_root in A). This gives a quantitative positive-probability support statement whenever the marginal mass is positive. Obstruction: Full support requires ruling out random conditional gaps for every rational interval above the random lower endpoint. Second moments and nonendogeny alone do not exclude such gaps. Verification: author_checked_partial. No proof file recorded.

### P0368. All bivariate frozen-percolation fixed points and their attraction domains

**Source.** Frozen percolation on the binary tree is nonendogenous (frozen_nonendogeny_arxiv), Problem7;PDF16.

**Statement.** Classify every fixed point and domain of attraction of d(mu_h)/dh=T2(mu_h)-mu_h for frozen percolation on the oriented binary tree. Ledger caveat: The two scale-invariant fixed points are known; this question permits nonscale-invariant couplings and asks for their dynamics.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: Starting a law at a convex mixture of the two known fixed points does not make the evolution stationary. The two-child update has a cross-input term of weight2p(1-p), so along the mixture line the derivative is2p(1-p)*(C-(nu_diag+nu_min)/2). Thus an apparent line of equilibria in a linear interpolation plot can be spurious. The source suggests sharing lightning until a fixed time and separating it afterward as a possible source of other equilibria, which would require a consistent infinite-process construction. Obstruction: No invariant family containing the proposed time-split couplings has been constructed, and no global Lyapunov function or complete basin decomposition is obtained. Verification: author_checked_partial. No proof file recorded.

### P0369. Nonendogeny from instability of the diagonal coupling

**Source.** Frozen percolation on the binary tree is nonendogenous (frozen_nonendogeny_arxiv), Question8;PDF16.

**Statement.** Find general conditions under which instability of the trivial bivariate fixed point proves that an RTP is nonendogenous. Ledger caveat: The meaning of instability and the topology must be specified. The attempt below treats a closed scalar family of couplings only.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: Suppose a continuous invariant family of admissible self-couplings is parameterized by disagreement d in[0,D], with diagonal d=0 and T2 acting by a continuous f with f(0)=0. If f(d)>d for all sufficiently small positive d, then because f(D)<=D the intermediate value theorem yields a nonzero fixed point. Under the standard bivariate uniqueness criterion this proves nonendogeny. A derivative fprime(0)>1 is one sufficient way to obtain the strict inequality. Obstruction: For general state spaces, no scalar closure or compact trapping family is available, and linearized growth can leave the chosen family. This conditional criterion does not answer the fully general question. Verification: author_checked_partial. No proof file recorded.

### P0370. Endogeny of frozen percolation on higher-degree trees and the PWIT

**Source.** Frozen percolation on the binary tree is nonendogenous (frozen_nonendogeny_arxiv), Question9;PDF16;later frozen_transition_2021 PDF3.

**Statement.** Determine endogeny for the PWIT and for d-regular trees beyond the solved degree-three case. Ledger caveat: All degrees and the related infinite-degree limiting tree are grouped as the source asks. The degree-three theorem is excluded from the open target.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: The proposed transfer through a near-critical binary scaling limit cannot rely merely on convergence in distribution: deterministic measurable functions of richer input fields can converge jointly to a variable with extra randomness. A concrete example is U uniform[0,1] and X_n=1{fractional_part(nU)<1/2}. Each X_n is U-measurable, yet (U,X_n) converges weakly to an independent pair (U,Bernoulli(1/2)), as follows by averaging any continuous test function over the n equal subintervals. Obstruction: A transfer of nonendogeny from the binary scaling limit needs a quantitative bivariate discrepancy that survives the approximation, not just a marginal marked-tree limit. Verification: author_checked_partial. No proof file recorded.

### P0371. Existence of infinite-cluster frozen percolation on higher-dimensional lattices

**Source.** Frozen percolation on the binary tree is nonendogenous (frozen_nonendogeny_arxiv), Question10;PDF17.

**Statement.** For which dimensions d>=3 does nearest-neighbor Z^d admit a frozen-percolation process satisfying the source infinite-cluster freezing rule? Ledger caveat: This is freezing at infinite size, not constant-rate cluster freezing or finite-threshold models. All dimensions are one question.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Bounded primary-source and focused later-literature search on2026-09-07; later geometric endogeny and discounted boundedness advances credited. No full current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact recurrence, conditional-law calculation, or source-specific limiting obstruction. Result: A compactness limit of finite-threshold processes does not automatically preserve the rule, because percolation is not a continuous local event. On Z^d, configurations with only edges inside[-n,n]^d open converge locally to the all-open configuration. Every approximating root cluster is finite, while the limiting root cluster is infinite. Thus an assertion that no finite approximation froze cannot be passed through a local limit without extra control. Obstruction: One must rule out discontinuous creation of infinite clusters at limiting times while enforcing the freezing equation. The cited high-dimensional self-destructive-percolation results do not themselves construct the required dynamics. Verification: author_checked_partial. No proof file recorded.

### P0372. Spherical shape and uniform bulk density of ARW aggregates

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjectures 1-2; PDF3-4.

**Statement.** For fixed sleep rate lambda>0 on Z^d, d>=2, prove the point-source visited-set ball limit and constant-density weak scaling limit of the final sleepers, with one common density. Ledger caveat: The one-dimensional ball/density results are credited to arw_density_2024, Theorem1.1 and Corollary8.9. Visited sites and final occupied sites are different observables, grouped here.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: In a finite killed domain V, let J(x) count departures from x during stabilization of n particles at 0, and let h be the final sleeper indicator. Conservation and the fresh uniform jump choice give $\mathbb E h(x)=n1_{x=0}+\Delta\mathbb E J(x)$, where $\Delta f(x)=(2d)^{-1}\sum_{y\sim x}f(y)-f(x)$ with zero extension outside V. This follows by stopping after K departures, taking expectations of arrivals, and then passing to the finite-domain absorption limit. It identifies the candidate continuum Poisson equation, but not its unknown density or free boundary. Obstruction: A limit of the expected odometer is insufficient: concentration, a uniform bulk sleeper density, and inner/outer control of the visited region are all still required. Verification: author_checked_partial. No proof file recorded.

### P0373. Full microscopic limit of the ARW point-source aggregate

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjectures 3-5; PDF4-5.

**Statement.** Prove convergence of every finite-window law of the point-source stabilization, with translation-invariant limit having the aggregate density almost surely. Ledger caveat: The three tightly linked existence/symmetry/density claims are counted once. In d=1, one-site convergence and shift invariance of every subsequential limit are known from arw_local_density_2026, Theorem1.1 and Proposition1.2.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: Compactness gives subsequential limits, but the new one-site theorem does not identify them. At density 1/2, compare iid Bernoulli occupation with a checkerboard having a uniform random phase on Z. Both are shift-invariant, ergodic under the full translation action, and have deterministic density 1/2. Both have the same one-site laws. Their adjacent covariance is respectively 0 and -1/4. Thus even the one-site theorem plus ergodicity would leave a real joint-distribution gap. Obstruction: Need uniqueness of all cylinder probabilities, or a coupling that suppresses differences between all subsequences. One-site flattening cannot provide it alone. Verification: author_checked_partial. No proof file recorded.

### P0374. Quadrature-domain scaling limit from extended ARW sources

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 6; PDF6-7.

**Statement.** For bounded open A with null-volume boundary, prove that stabilizing one particle at each lattice point of A has the source quadrature-domain scaling limit at density zeta_a. Ledger caveat: The full geometric and integrability conventions of Conjecture6 apply. This is a multiple-source obstacle problem, not another point-source radius question.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: Let h be harmonic on a finite domain containing the evolution, and stop the process before exit and after at most K jumps. The sum of h over all particle locations is a martingale: sleeping and waking do not change locations, and each jump has zero conditional h-increment. For superharmonic h the corresponding sum is a supermartingale. Consequently, any tight scaling limit for which these stopped quantities are uniformly integrable must preserve harmonic moments and satisfy the superharmonic quadrature inequality. Testing h=1 and h=-1 forces |A|=zeta_a*|Astar|; linear harmonic tests force equality of centroids. Obstruction: No proof of tightness, uniform integrability, constant terminal density, or identification of the limiting support is obtained. Necessary moment constraints do not establish the conjectured limit. Verification: author_checked_partial. No proof file recorded.

### P0375. Independence of ARW bulk microstructure from the initial source shape

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 7; PDF7.

**Statement.** For an interior point of the limiting aggregate from any allowed extended source A, prove that its microscopic law is the same as the point-source law alpha. Ledger caveat: Interior-point condition and the existence of the relevant macroscopic support are retained. The source-shape universality claim is distinct from existence of alpha.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: A useful sufficient condition is a common local coding from instruction stacks. Suppose the output on a finite window W can be determined by stacks within a random radius R, with the same coding rule for both source geometries after their fronts pass, and P(R>r)<=C*r^(-beta). Coupling the stacks then bounds total variation of the two W-laws by 2*C*r^(-beta) whenever both available bulk neighborhoods have radius r. With r proportional to inverse mesh, this gives a quantitative microscopic universality rate. Obstruction: A common finite-radius coding rule is unproved at criticality and may itself be too strong. This is an explicit coupling reduction, not an assertion that ARW has a finite influence radius. Verification: author_checked_partial. No proof file recorded.

### P0376. Universal critical limit obtained by sprinkling subcritical ARW states

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 9; PDF7.

**Statement.** As Poisson sprinkling raises any stationary ergodic initial state to the critical density from below, prove a common limiting stabilized law with almost-sure critical density. Ledger caveat: The initial state, sprinkling, and local-limit order are exactly those of Conjecture9. Average density and almost-sure density are kept distinct.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: For a stabilizable stationary system, mass transport preserves the mean particle density: send one unit from every initial particle to its final sleeping site. Thus any local subsequential limit of the bounded occupation indicators has one-site mean zeta_c. This still does not imply almost-sure density. To see the precise gap, fill consecutive blocks of length m with iid Bernoulli(rho) values, constant within a block, and randomize the block origin uniformly. Each resulting process is stationary ergodic with density rho. As m tends to infinity its local law converges to the mixture rho*delta_all_ones+(1-rho)*delta_all_zeros, whose density is random. Obstruction: Need control of correlations or ergodic components that is uniform near criticality, together with uniqueness and independence from the initial law. Conservation of mean does not supply any of these. Verification: author_checked_partial. No proof file recorded.

### P0377. Universal stationary ARW density in higher-dimensional growing domains

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjectures 11-12; PDF8-9.

**Statement.** For d>=2 and vanishing boundary-to-volume exhaustions, prove concentration of the wired stationary density and equality with the fixed-energy and aggregate critical densities. Ledger caveat: Concentration, exhaustion independence, and equality of the related critical densities are one grouped density question. The interval/cycle result in d=1 is known.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: The exact stationary sampler starts one active particle at every site. Write D_V for the total number eventually killed at the boundary. Then S_V=|V|-D_V pathwise. If J(x) counts jumps at x, the departure identity gives E D_V=sum_{x in V} q_V(x)*E J(x), where q_V(x) is the one-jump exit probability. This shows why a vanishing number of boundary sites cannot by itself imply negligible dissipation: expected boundary odometers can grow enough to carry a volume-order flux. Obstruction: Need a concentration estimate for D_V and a limit for its volume-normalized expectation that is independent of the exhaustion. Surface-to-volume geometry alone does not control repeated boundary visits. Verification: author_checked_partial. No proof file recorded.

### P0378. Exhaustion-independent infinite-volume wired ARW measure

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 13; PDF9.

**Statement.** Prove local convergence of wired stationary measures along every exhaustion of Z^d, with the same limit. Ledger caveat: Compactness proves existence of subsequences only. The January2026 point-source paper still identifies this as a joint-law question.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: Finite-volume stationarity gives pi_V*K_v,V=pi_V for addition at v. To pass this identity through a local limit, truncate the avalanche at a radius r. If its influence on an observed window leaves that ball with probability at most epsilon_r, uniformly in outer V, then for each bounded local test f the discrepancy between the full and truncated expectations is at most 2*||f||_infinity*epsilon_r. The truncated operator is local and continuous, so subsequential limits inherit addition invariance if epsilon_r tends to zero. Obstruction: Uniform localization is missing and may fail for critical avalanches. Even inherited addition invariance would still need a uniqueness theorem to identify all subsequential limits. Verification: author_checked_partial. No proof file recorded.

### P0379. Equality of the three infinite-volume critical ARW laws

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Question 14; PDF9; Section9.

**Statement.** Determine whether the wired, subcritical-sprinkling, and point-source microscopic limits pi, mu, and alpha coincide. Ledger caveat: The question includes the required existence of its limits by reference to the preceding entries. Matching the mean densities or a finite covariance table is not equality of laws.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: Even agreement of every one- and two-site marginal need not identify a measure. On Z, partition into triples with a uniformly random phase and use iid uniform even-parity bit triples (000,011,101,110). Every pair of distinct bits is independent Bernoulli(1/2), including pairs across triples. The measure is translation invariant. For three consecutive sites, however, the all-ones probability is (1/3)*0+(2/3)*(1/8)=1/12, whereas iid Bernoulli(1/2) gives 1/8. Thus the pair-correlation experiments cannot distinguish all possible candidate laws. Obstruction: Need a coupling or a characterization using all cylinder events. This auxiliary counterexample refutes only the proposed inference from pair data, not equality of the actual ARW limits. Verification: author_checked_partial. No proof file recorded.

### P0380. Equality of bulk one-site density and wired global ARW density

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 15; PDF9.

**Statement.** Show that the one-site occupation probability under the infinite-volume wired measure equals the limiting finite-volume stationary density. Ledger caveat: This is the boundary-versus-bulk assertion for wired measures. The 2026 point-source one-site theorem does not directly prove it.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: Let rho_V(x) be the wired single-site mean. A sufficient estimate is sup_{dist(x,boundary V)>=r}|rho_V(x)-rho_infinity|<=epsilon_r, uniformly over V, with epsilon_r tending to zero. Splitting the mean over the depth-r boundary layer and its complement gives |E S_V/|V|-rho_infinity|<=epsilon_r+|boundary_layer_r(V)|/|V|. For each fixed r, the last ratio vanishes along lattice Folner exhaustions; then r can grow after V. Obstruction: Ordinary local convergence at a fixed origin does not give the required uniform interior estimate. A growing central defect can have zero volume fraction but determine every fixed-window limit. Verification: author_checked_partial. No proof file recorded.

### P0381. Higher-dimensional hockey-stick density evolution for wired ARW

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 17; PDF9-10.

**Statement.** On d-dimensional boxes with d>=2 and uniform driving from empty, prove that after floor(t*L^d) additions the density converges to min(t,zeta_c). Ledger caveat: The full interval theorem is proved in arw_hockey_2024, Theorem1. All times t are one question.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: Writing N=L^d, S_k for retained particles, and E_k for cumulative losses, the exact identity E_k=k-S_k converts the conjecture to E_floor(tN)/N -> (t-zeta_c)_+. At stationarity one addition has mean loss one, because 0=E(S_{k+1}-S_k)=1-E(loss_{k+1}). That balance does not say when stationarity is reached. The necessary transient estimate is a bound on the total excess loss before zeta_c*N and on the total retention after it. Obstruction: No bound makes the transient loss negligible below criticality and matches it to the linear excess above criticality in d>=2. Stationary mean balance alone cannot establish the hockey-stick curve. Verification: author_checked_partial. No proof file recorded.

### P0382. Critical-density total-variation cutoff for wired ARW in higher dimensions

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 19; PDF11.

**Statement.** Prove total-variation cutoff at zeta_s times the volume for uniformly driven wired ARW on lattice balls in d>=2. Ledger caveat: The interval theorem is established by arw_cutoff_2025, Theorem1.1. Separation cutoff at volume is a different metric and is not substituted.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: Assuming stationary-density concentration at rho, the lower bound at every t<(rho-epsilon)N follows immediately and sharply from the particle-count test. Starting empty, S_t<=t deterministically. For A={S>(rho-epsilon/2)N}, the time-t law gives probability zero whereas stationarity gives probability tending to one. Therefore the total-variation distance tends to one. This reduces the unresolved direction to forgetting the configuration just above rho*N. Obstruction: Need the matching upper bound after (rho+epsilon)N additions, including spatial activation coverage or a successful coupling. A small relaxation time and the density lower bound do not by themselves prove this upper bound. Verification: author_checked_partial. No proof file recorded.

### P0383. Exponential incompressibility of the infinite-volume wired ARW state

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 20; PDF11.

**Statement.** For every zeta>zeta_s, prove a volume-exponential upper tail for the number of sleepers in an L-sided cube under pi. Ledger caveat: Conditional on existence of pi and the intended mean density. Pairwise negative covariance is not assumed to imply negative association.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: A route through negative association would suffice: for N=L^d indicators with common mean rho and negative association, $\mathbb E e^{\theta S}\le(1-\rho+\rho e^\theta)^N$ for theta>0. Chernoff optimization at $e^\theta=\zeta(1-\rho)/(\rho(1-\zeta))$ yields $\mathbb P(S\ge\zeta N)\le e^{-N D(\zeta\Vert\rho)}$ for rho<zeta<1. Here D is Bernoulli relative entropy. At zeta=1 the bound is rho^N, obtained by a limit. Obstruction: Negative association, or a comparably strong exponential-moment estimate, is unproved here for pi. A covariance table cannot justify this step. Verification: author_checked_partial. No proof file recorded.

### P0384. Sharp first slow-stabilization threshold of the ARW free chain

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 21 and Question22; PDF12.

**Statement.** For the free addition chain on growing tori, prove concentration of the first superlinear stabilization time at critical density, and determine the proposed linear-to-exponential jump-count transition. Ledger caveat: The cycle fixed-energy polynomial/exponential threshold is known from arw_density_2024. It concerns a different initialization and does not automatically prove this first-passage statement for a chain of successive stable states.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: For a fixed threshold f(N), define tau_f=min{k:U_k>=f(N)}. An explicit sufficient pair of bounds is sup_{k<=(rho-epsilon)N} P(U_k>=f(N))=o(1/N), and P(U_floor((rho+epsilon)N)>=f(N))=1-o(1). The union bound gives the lower bound on tau_f, and the single late-time event gives the upper bound. Merely proving each early probability is o(1) cannot be enough: independent rare spikes with probability 1/N per step have a nonvanishing probability of a first crossing among N steps. Obstruction: Uniform early-time tails at the needed scale, the appropriate f, and a late-time slow-stabilization estimate for the free-chain input distribution are missing. Verification: author_checked_partial. No proof file recorded.

### P0385. Asymptotic equivalence of supercritical free and wake ARW states

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 23; PDF12.

**Statement.** At a fixed density zeta in (zeta_c,1), prove that the free-chain law and the stationary wake-chain law on growing tori converge in total variation. Ledger caveat: The same particle count is essential. This question concerns the law before an extra full wake, not just mixing of the wake kernel.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: Let K be the wake-and-stabilize kernel on k-particle configurations, and delta=sup_{x,y}TV(K(x,.),K(y,.)). If nu is stationary, convexity gives TV(mu*K,nu)<=delta for every input law mu. Consequently TV(mu,nu)<=TV(mu,mu*K)+delta. Even a proof that delta tends to zero only settles the target once the free-chain law mu is shown nearly invariant under the additional full wake. Obstruction: The approximate wake invariance of the free-chain law and a vanishing Dobrushin coefficient are both unproved here. The reduction identifies the extra distributional obligation. Verification: author_checked_partial. No proof file recorded.

### P0386. Uniform loss of initial-state information in dense ARW stabilization

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 24; PDF12-13.

**Statement.** For all active initial configurations on a torus with the same particle count between zeta*L^d and L^d, zeta>zeta_c, show their stabilized laws become uniformly close in total variation. Ledger caveat: The upper bound on particle count is necessary for stabilization and is made explicit. The survey credits a small-sleep-rate regime; it is excluded from any novelty claim.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: A particlewise coupling with k labelled particles would prove the result if every pair can be matched to share its future path and sleep instructions before it becomes permanently inactive, with individual failure probability o(1/k). Indeed, the union bound gives failure probability at most k*epsilon_k, and successful matching yields identical unlabelled terminal configurations. Pairwise success with probability merely 1-o(1) is too weak when k is of volume order. Obstruction: Long global stabilization time does not imply every labelled particle remains available for matching. Constructing a valid interacting coupling with uniform o(1/k) failure remains the missing step. Verification: author_checked_partial. No proof file recorded.

### P0387. Slow-to-one-step mixing transition of the ARW wake chain

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 25; PDF13.

**Statement.** Determine the proposed diffusive lower bound below critical density and one-step asymptotic mixing above it for the wake chain on tori. Ledger caveat: The empty configuration is a trivial exception to the literal lower bound. The substantive question concerns positive fixed density; mixing tolerance and worst-start versus individual-start quantifiers need specification.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: The exactly solvable one-particle sector provides a dilute check. On the cycle of length L, waking a particle runs rate-one simple random walk until an independent Exp(lambda) sleep time. For $\theta=2\pi/L$, its first Fourier multiplier is $r_L=\lambda/(\lambda+1-\cos\theta)$. After k wakes, a point start has cosine expectation $r_L^k$, whereas stationarity is uniform with expectation zero. Hence TV is at least $r_L^k/2$, and reaching TV<=1/4 requires $k\ge\log2/(-\log r_L)\sim\lambda\log2\,L^2/(2\pi^2)$. Obstruction: One particle has density tending to zero, so this does not prove the positive-fixed-density lower bound or the supercritical upper bound. Neither is claimed solved. Verification: author_checked_partial. No proof file recorded.

### P0388. Hyperuniformity of the infinite-volume wired ARW state

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 26; PDF13-14.

**Statement.** Prove a power saving below volume order for sleeper-number variance in large cubes under the wired infinite-volume measure. Ledger caveat: Existence and translation invariance of the measure remain prerequisites. The finite complete-graph result is a different model.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: For a stationary occupation field with covariance c(z), $\mathrm{Var}(S_B)=\sum_z c(z)|B\cap(B-z)|$. If $\sum_z c(z)=0$ and $\sum_z |z|_1|c(z)|<\infty$, a cube of side L satisfies $\mathrm{Var}(S_B)\le C_d L^{d-1}\sum_z|z|_1|c(z)|$. Subtract |B| times the zero sum, then bound the lost overlap by $C_d L^{d-1}\min(|z|_1,L)$. This would give the desired exponent d-1, including bounded variance when d=1. Obstruction: Neither the infinite-volume covariance cancellation nor the weighted absolute summability is proved for ARW. Finite-torus conservation gives a zero sum at each size but does not justify interchanging that sum with the infinite-volume limit. Verification: author_checked_partial. No proof file recorded.

### P0389. Onset of mesoscopic hyperuniformity in the ARW free chain

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Conjecture 27; PDF15.

**Statement.** Determine the subcritical linear-variance and critical/supercritical subvolume-variance regimes for particle counts in windows of the free-chain torus configuration. Ledger caveat: The literal source permits every box with size-uniform constants. That lower bound fails for boxes filling almost the whole torus. The intended mesoscopic or bounded-volume-fraction regime remains open.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: candidate_partial_counterexample.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: At step k the free chain has exactly k sleeping particles on N=L^d sites. Thus Var(S_B)=Var(S_Bc) and Var(S_B)<=min(|B|,N-|B|)^2/4. Taking the proper box B=[0,L-2] times the full other d-1 coordinate intervals leaves only L^(d-1) sites outside B. In d=1, B has L-1 sites and Var(S_B)<=1/4, contradicting a size-uniform lower bound c*(L-1) at any fixed positive subcritical density. The contradiction does not depend on a simulation or the full-torus endpoint. Obstruction: This is a scope counterexample to the unrestricted window quantifier. It does not settle variance growth for windows small compared with the torus, nor the critical exponent. Verification: author_checked_partial. Proof file: proofs/ARW_fixed_mass_window_obstructions.md.

### P0390. Hyperuniformity transition in stationary ARW wake states

**Source.** Levine and Silvestri: Universality conjectures for activated random walk (arw_universality_2024), Question28; PDF15-16.

**Statement.** Determine whether stationary wake-chain configurations have linear window variance below criticality and a power saving at and above criticality. Ledger caveat: As with the free chain, a fixed global particle count requires a restriction on observation windows for a positive uniform lower bound. The stationary and transient free ensembles are distinct source questions.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused searches on 2026-09-07 for ARW density, cutoff, local limits, hyperuniformity and incompressibility; four later primary papers read at stated theorem scope. No certificate of present openness.). Admission: admitted; result_status: candidate_partial_counterexample.

**Our work.** Method: Conservation, explicit coupling reduction, exact law comparison or spectral calculation. Result: Every wake-chain state has the same total k. On a cycle, the complement-of-one-site window therefore has variance rho_N*(1-rho_N)<=1/4 under the unique stationary law, where rho_N=k/N; the whole torus has variance zero. More generally, translation invariance forces sum_y Cov(I_x,I_y)=Cov(I_x,k)=0, but this finite-volume cancellation does not imply mesoscopic hyperuniformity. For comparison, uniform k-subsets have Var(S_B)=|B|*rho_N*(1-rho_N)*(N-|B|)/(N-1), which is volume order for |B|=o(N). Obstruction: The literal all-window lower bound is false; the meaningful small-window transition is unresolved. Exact global covariance cancellation alone cannot prove a subvolume variance bound. Verification: author_checked_partial. Proof file: proofs/ARW_fixed_mass_window_obstructions.md.

### P0391. Diffusion limit for an arbitrary symmetric M/G/1 discipline

**Source.** Zwart: Conjectures on Symmetric Queues in Heavy Traffic (queues_symmetric_2022), Problem 1; PDF1-2.

**Statement.** For every work-conserving symmetric discipline gamma, prove convergence of Q_gamma(r^2 t)/r to the common reflected Brownian limit when the service second moment is finite and r(1-rho_r) tends to beta. Ledger caveat: Use empty initial state, as in the source discussion of universal marginal laws. PS and LCFS are known special cases, not new solutions.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: Put m=E B, m2=E B^2 and h=m2/(2m). The workload diffusion has drift -beta and variance rate m2/m. If uniform-on-compacts state-space collapse Q/r-W/(rh) were established, its queue-length image would have drift -beta/h and variance rate m2/(m*h^2). For beta>0 the stationary exponential rate of this candidate is 2*(beta/h)/(m2/(m*h^2))=beta, exactly the rate obtained from P(Q>=k)=rho_r^k. This fixes the constants and reduces a proof to a precise collapse estimate. Obstruction: Uniform state-space collapse for arbitrary gamma remains unproved. Equality of fixed-time marginals does not establish process convergence or tightness. Verification: author_checked_partial. No proof file recorded.

### P0392. Infinite-variance scaling limits of symmetric queue lengths

**Source.** Zwart: Conjectures on Symmetric Queues in Heavy Traffic (queues_symmetric_2022), Problem 2; PDF2-3.

**Statement.** For a regularly varying service tail L(x)x^(-alpha), 1<alpha<2, and c_r*Fbar(c_r)=1/r, identify and prove the process limit of Q_gamma(c_r*t)/r for general symmetric gamma. Ledger caveat: The LCFS limit is known; the source identifies PS tightness and the general-discipline limit as unresolved. The following stationary calculation assumes beta>0.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: The Pollaczek-Khinchine transform is E exp(-sW)=(1-rho)*s/[s-lambda*(1-E exp(-sB))]. Regular variation gives E exp(-sB)=1-ms+a*s^alpha*L(1/s)+o(s^alpha L(1/s)), where a=-Gamma(1-alpha)>0. Substituting s=u/c_r and r(1-rho_r)->beta yields E exp(-uW/c_r)->beta/[beta+(a/m)*u^(alpha-1)]. In contrast Q/r has stationary exponential limit of rate beta. Consequently a positive linear state-space collapse W/c_r=c*Q/r cannot hold in this regime. Obstruction: This rules out only linear collapse and supplies a necessary stationary check. It neither identifies the temporal law nor proves tightness; even a nonlinear relation is not excluded by this marginal calculation. Verification: author_checked_partial. No proof file recorded.

### P0393. Uniform busy-cycle maximum bounds for symmetric queues

**Source.** Zwart: Conjectures on Symmetric Queues in Heavy Traffic (queues_symmetric_2022), Discussion, final paragraph before references; PDF3.

**Statement.** Obtain busy-cycle queue-maximum tail bounds for arbitrary symmetric disciplines strong enough to support the regenerative tightness route described in the source. Ledger caveat: This is the separately identified excursion-tail question. It is not counted again for each service distribution or traffic parameter.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: With exponential service of rate mu, the queue length under any symmetric gamma is a birth-death chain: the total departure hazard is mu times sum_i gamma(n,i)=mu. For a busy period starting at one, the probability that its maximum reaches K is (q-1)/(q^K-1), q=mu/lambda, with critical value 1/K. If r(1-rho_r)->beta>0 and K=floor(x*r), r times this probability tends to beta/(exp(beta*x)-1). Thus a usable general tail estimate must be compatible with this exact critical excursion scale. Obstruction: General service distributions destroy this one-dimensional Markov calculation. A uniform bound must control residual-service composition within an excursion; fixed-time insensitivity does not determine the maximum. Verification: author_checked_partial. No proof file recorded.

### P0394. Efficient input estimation from periodically observed queue workloads

**Source.** Ravner: Queue input estimation from discrete workload observations (queues_input_estimation_2022), Problem statement and final discussion; PDF2-3.

**Statement.** Construct statistically efficient estimators of the finite-dimensional compound-Poisson input parameters from discrete M/G/1 workload observations, retaining their temporal dependence. Ledger caveat: Consistency and transform-based methods already exist. The target is attainable asymptotic efficiency, not simply another consistent moment estimator.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: For a stable M/M/1 benchmark let a=P(W>0)=lambda/mu and b=E W=a/(mu-lambda). Inversion gives mu=a/[b*(1-a)] and lambda=a^2/[b*(1-a)]. Empirical busy fraction and mean workload therefore yield a consistent estimator on a fixed sampling grid by ergodicity. Its asymptotic covariance, when the joint CLT holds, is J*Sigma*J^T, where J is the Jacobian of this inversion and Sigma=sum over integer lags of Cov((1{W_0>0},W_0),(1{W_l>0},W_l)). The off-zero lags are part of the information calculation. Obstruction: The estimator is a benchmark only. Neither an efficiency bound for general input families nor an estimator attaining it has been proved here. Verification: author_checked_partial. No proof file recorded.

### P0395. Network decomposition with several bottlenecks and internal flow covariance

**Source.** Whitt-You: New decomposition approximations for queueing networks (queues_decomposition_2022), Sections2.1.1-2.1.2; PDF2.

**Statement.** Extend the robust queueing network analyzer to several simultaneously critical nodes while estimating and propagating the internal cross-flow covariance needed in non-tree networks. Ledger caveat: The multiple-bottleneck and covariance-fitting subquestions are grouped because the proposed limit calculation needs both.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: Separate rate and IDC functions cannot determine the required joint input law. Let N1,N2 each have rate lambda Poisson marginals. If independent, Var(N1(t)+N2(t))=2*lambda*t; if N1=N2, the variance is 4*lambda*t. Both inputs have identical individual IDCs equal to one, but the total IDC is respectively one and two. Thus any multi-bottleneck diffusion approximation based solely on the marginal IDC data has a missing covariance parameter before reflection is even applied. Obstruction: Need a consistent joint covariance model and its propagation through multidimensional reflected Brownian flow limits. This information obstruction does not provide those estimates or an approximation error bound. Verification: author_checked_partial. No proof file recorded.

### P0396. IDC-based decomposition for networks of multiserver queues

**Source.** Whitt-You: New decomposition approximations for queueing networks (queues_decomposition_2022), Section2.2(i), Section3.2(i); PDF2-3.

**Statement.** Extend the single-server IDC-based robust queueing analysis to multiple servers at each network node, with a justified performance approximation. Ledger caveat: The source distinguishes this from the existing multiserver QNA and generic robust-queueing models.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: Even without future arrivals, aggregate workload cannot close a two-server state description. Residual workloads (2,0) and (1,1) both sum to two, but their immediate workload drain rates are one and two. Their times to empty are two and one. A scalar workload approximation therefore needs an additional busy-server or residual-work descriptor, or a proved collapse regime that removes this ambiguity. Obstruction: Need an augmented state and a tractable covariance propagation rule, together with an asymptotic justification. A scalar workload replacement alone cannot be universally exact. Verification: author_checked_partial. No proof file recorded.

### P0397. Multiclass and non-Markovian-routing robust queueing decomposition

**Source.** Whitt-You: New decomposition approximations for queueing networks (queues_decomposition_2022), Section2.2(ii), Section3.2(ii); PDF2-3.

**Statement.** Extend the IDC network approximation to class-dependent or more general routing without losing the dependencies that determine downstream congestion. Ledger caveat: The source describes aggregation into approximate Markovian routing as an existing method, not an exact solution.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: Consider iid job marks taking two values with equal probability. A job has first-node service requirement B=1 or B=3. In model A only the B=3 jobs are routed downstream; in model B only B=1 jobs are routed downstream. Both models have the same marginal service distribution and the same routing probability 1/2. But E[B*R] is 3/2 in A and 1/2 in B, and Cov(B,R) is respectively 1/2 and -1/2. Marginal service and routing data thus do not identify the marked flow dependence entering a downstream approximation. Obstruction: Need a marked or class-resolved closure and bounds for its error. The scalar marginal primitives alone cannot recover this cross moment. Verification: author_checked_partial. No proof file recorded.

### P0398. Robust network approximations under time-varying arrivals

**Source.** Whitt-You: New decomposition approximations for queueing networks (queues_decomposition_2022), Section2.2(iii), Section3.2(iii); PDF2-3.

**Statement.** Develop and justify a time-varying extension of the robust queueing network analyzer, accounting for propagation delays and changing congestion. Ledger caveat: Single-queue time-varying robust approximations are already cited in the source. Network behavior is the target.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: An exact infinite-server benchmark shows the necessary temporal response. With exponential service rate mu and arrival intensity lambda(t)=lambda0+epsilon*cos(omega*t), the periodic mean occupancy is lambda0/mu+epsilon*(mu*cos(omega*t)+omega*sin(omega*t))/(mu^2+omega^2). It solves mprime=lambda(t)-mu*m. The instantaneous stationary substitution lambda(t)/mu has neither the correct amplitude nor the phase delay when omega is comparable to mu. Obstruction: A finite-server interacting network requires an additional queueing and routing response, plus a controlled approximation regime. The linear benchmark constrains such a model but does not solve it. Verification: author_checked_partial. No proof file recorded.

### P0399. Identifiable and efficient probe inference in tandem queueing networks

**Source.** Antunes-Jacinto-Pacheco: Statistical inference in queueing networks with probing information (queues_probing_2022), Problem statement; PDF2.

**Statement.** Design a minimally perturbing probing strategy and inference method for the unknown arrival streams and packet-size distributions in the source tandem FIFO network. Ledger caveat: The full per-stream target needs identifiability assumptions. The source allows n queues without an explicit n>=2 restriction; the following obstruction concerns n=1.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: For n=1, streams 0 and 1 have the same route. If both are independent Poisson processes with the same positive packet-size law G, their superposition is a marked Poisson process of rate lambda0+lambda1 and mark law G. Every probe departure is a function of that unlabelled input and the chosen probes. Therefore all positive pairs (lambda0,lambda1) with a common sum give exactly the same probe-data distribution, including under adaptive strategies whose randomization is independent of the hidden stream labels. Obstruction: Separate per-stream rates cannot be recovered in this allowed one-node case. Identifiable multi-node models, optimal probe design, asymptotic normality and efficiency remain open targets. This is a scope obstruction, with no novelty claim. Verification: author_checked_partial. No proof file recorded.

### P0400. Response-time laws with correlated redundancy replicas

**Source.** Gardner: Correlation in redundancy systems (queues_redundancy_2022), Q1; PDF1,3.

**Statement.** Derive useful exact or justified approximate response-time laws for redundancy-d queues with correlated replica service requirements and specified scheduling rules. Ledger caveat: Known product-form results for independent exponential replicas and numerical FCFS methods are credited. Replica starting times need not coincide in a loaded system.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: For an isolated job in the S-and-X model, all d copies start together and completion time is X*min(S1,...,Sd), where X is independent of the iid slowdowns. Consequently E T=E X times integral_0^infinity P(S>t)^d dt. This gives a required zero-load boundary value for any response approximation. With unit-rate exponential S the value is E X/d; with deterministic S=1 it is E X for every d. Obstruction: The isolated-job result is exact but classical. Positive-load response depends on staggered starts, cancellations and inter-queue dependence; no formula or error bound for that regime is established. Verification: author_checked_partial. No proof file recorded.

### P0401. Optimizing replication degree under correlated service requirements

**Source.** Gardner: Correlation in redundancy systems (queues_redundancy_2022), Q2; PDF1,3.

**Statement.** Determine the replication degree d minimizing steady-state mean response time for correlated-replica redundancy queues. Ledger caveat: All degrees are one optimization question. Independent-replica monotonicity results do not resolve general correlation.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: For a simultaneously started isolated job, total server effort is d*X*min_i S_i. Unit-rate iid exponential slowdowns give mean effort E X for every d, while identical deterministic slowdowns give d*E X. The corresponding completion times are E X/d and E X. Thus the same replica count can buy latency without extra mean work in one model, or multiply mean work without reducing latency in another. A degree optimizer must account for both the joint slowdown law and load. Obstruction: This does not determine the optimum at positive load. Queue-state-dependent staggering can change both effort and latency, and an optimization theorem needs a controlled response function. Verification: author_checked_partial. No proof file recorded.

### P0402. Stability beyond processor sharing with correlated redundancy copies

**Source.** Gardner: Correlation in redundancy systems (queues_redundancy_2022), Q3; PDF1,3.

**Statement.** Characterize the stability region of correlated-replica redundancy-d systems under FCFS and other scheduling disciplines beyond the known PS results. Ledger caveat: The following fully replicated endpoint d=k is a solvable check outside the survey focus d much smaller than k; it does not resolve the general regime.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: When d=k and every queue is FCFS, all queues have the same job order and begin the next job simultaneously after a cancellation. The system is exactly an M/G/1 queue of rate k*lambda and service duration M=min(B1,...,Bk), where the vector B is iid across jobs but may be correlated within each job. Its strict stability condition is k*lambda*E M<1. In the S-and-X case M=X*min_i S_i. Identical copies yield lambda<1/(k*E B); independent unit exponentials yield lambda<1. Obstruction: For d<k, different compatibility sets break synchronization. The exact endpoint cannot justify a stability criterion based only on d times the isolated minimum service duration. Verification: author_checked_partial. No proof file recorded.

### P0403. Optimal scheduling for correlated redundancy systems

**Source.** Gardner: Correlation in redundancy systems (queues_redundancy_2022), Q4; PDF1,3.

**Statement.** Identify scheduling rules minimizing mean response time, including how the optimal rule changes with the replica correlation and service law. Ledger caveat: The source credits least-redundant-first optimality in special nested exponential models. The following deterministic comparison is only a finite-workload diagnostic.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: Take two servers and two simultaneously present jobs with identical replica durations a<=b across servers. Replicating the shorter job on both servers first gives completion times a and a+b, with mean a+b/2. Assigning one job to each server immediately gives completion times a and b, with mean (a+b)/2. The second policy improves the mean by a/2. Therefore a proof based on always assigning every free server to the currently shortest job cannot be valid across the correlated-copy model class. Obstruction: Need a dynamic rule and a stochastic comparison or control proof for the full arriving system. Finite-workload preference need not identify a steady-state optimizer. Verification: author_checked_partial. No proof file recorded.

### P0404. Tractable concurrent-replica policies with broad stability guarantees

**Source.** Gardner: Correlation in redundancy systems (queues_redundancy_2022), Q5; PDF2-3.

**Statement.** Design analytically tractable redundancy policies that retain useful simultaneous service and achieve a provably maximal stability region under a specified correlated-replica model. Ledger caveat: RIQ and delta-probe maximal-stability results with only one served replica are already known. Baseline stability is weaker than a maximal-region theorem.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: A conservative construction uses independent primary routing and serves extra replicas only on otherwise idle servers, with instantaneous preemption of an extra whenever a primary needs that server. Couple each primary to the same job and primary service requirement in the no-replication system. An extra completion can only remove work earlier, and an extra never consumes primary capacity, so each primary workload is no larger than its baseline counterpart. Under iid uniform primary routing, the ordinary M/G/1 load condition lambda*E B_primary<1 supplies a baseline stability benchmark. Obstruction: This comparison does not prove maximality or quantify response gains, and is not claimed as a new policy. For general service laws redundancy can alter achievable capacity; a universal baseline argument is insufficient. Verification: author_checked_partial. No proof file recorded.

### P0405. Characterizing optimality of MAX-H in multiclass queues

**Source.** Aalto and Scully: Minimizing the mean slowdown in the M/G/1 queue (queues_slowdown_resolution_2023), Section4 after Theorem3; PDF15.

**Statement.** Find a necessary and sufficient characterization, or a sharper usable sufficient condition, for MAX-H optimality in the multiclass M/G/1 generalized holding-cost problem. Ledger caveat: Theorem3 gives a sufficient monotonicity condition only. The concluding prose loosely says necessary and sufficient; the theorem and PDF15 explicitly explain that necessity is unresolved. Single-class FCFS is already resolved.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: For one class and attained service a, the index is the supremum over b>a of the Fbar-weighted average of h_c(y)=c(y)h(y) on [a,b]. Its value G(a) therefore satisfies H(a)<=G(a)<=U(a), where H is the weighted average over [a,infinity) and U(a)=sup_{y>=a}h_c(y). A sufficient statewise certificate for the MAX-H chosen job i is H_i(a_i)>=max_{j!=i} U_j(a_j). Then G_i>=H_i>=U_j>=G_j, so that choice is Gittins-optimal. This supplies an explicit conservative certificate computable from service and cost laws. Obstruction: The certificate is often too strong or vacuous when U is infinite, and checking it on every reachable state is itself hard. It does not give the missing necessity characterization or improve the paper uniformly. Verification: author_checked_partial. No proof file recorded.

### P0406. Finite-system performance of size-based scheduling with impatience and noisy sizes

**Source.** Ibrahim: Personalized scheduling in service systems (queues_personalized_2022), Problem statement and discussion; PDF2.

**Statement.** Quantify the performance of size-based scheduling in multiserver queues with abandonment and noisy service-time estimates beyond the established overloaded many-server throughput limit. Ledger caveat: Dong-Ibrahim later proves noisy-SJF asymptotic throughput results under its calibration assumptions. Those results are credited; finite-server performance and error control remain the retained part of the broad source question.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 search for symmetric limits, correlated redundancy, slowdown and noisy scheduling; matched later slowdown theorem and noisy-SJF limits. No current-openness certificate.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Transform asymptotics, exact special case, coupling reduction or identifiability check. Result: The relevant ranking variable need not be the raw prediction. Let two prediction classes be z1<z2, but their true service times be deterministically 10 and 1. With one free server, no further arrivals and infinite patience for this local check, raw-prediction order has completion times 10,11 and mean 10.5; ordering by the conditional mean service times gives 1,11 and mean 6. Thus calibration monotonicity E[B|Z=z] increasing in z is a substantive assumption, not a consequence of having a prediction. Posterior service and patience information must enter a general performance model. Obstruction: Need a finite-server state description and quantitative waiting/abandonment analysis under stated prediction and patience laws. This local misranking example provides neither an error bound nor a general optimizer. Verification: author_checked_partial. No proof file recorded.

### P0407. FCFS characterization for minimum mean slowdown

**Source.** Aalto: Minimizing the mean slowdown in a single-server queue (queues_slowdown_2022), Conjecture1; PDF4.

**Statement.** FCFS minimizes mean slowdown among non-anticipating policies if and only if Htilde(x)>=Htilde(0) for every x.

**Status.** Historical status: source_says_open. Current-literature status: resolved_in_literature (no status-search record recorded in the ledger). Resolution record: queues_slowdown_resolution_2023, Corollary3 equation18; PDF13. The later formula for H_sld is identical to the source Htilde. Corollary3 states the iff claim and explicitly identifies the earlier conjecture. No new solution claimed. Admission: not admitted; result_status: known_result_not_original.

**Our work.** Not admitted (result_status: known_result_not_original); see the resolution record above. No attempt is recorded for this row in attempts.jsonl.

### P0408. Recovering an ideal Voronoi tessellation from vertices or its dual

**Source.** D Achille Curien Enriquez Lyons Unel: Ideal Poisson Voronoi tessellations on hyperbolic spaces (ideal_voronoi_2023), Question7.2; PDF48.

**Statement.** Determine whether the maps from a hyperbolic IPVT to its vertex set and to its ideal Delaunay tessellation are almost surely injective. Ledger caveat: The two inverse-map questions are grouped. Theorem3.11 already reconstructs the ideal nuclei from richer tessellation information.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: A sufficient reconstruction route is quantitative local decoding. Suppose for every rational test ball and every accuracy epsilon there is a measurable decoder from the observed vertex set in radius R whose answer about the tessellation in that ball fails with probability epsilon_R tending to zero. Choose R_k with epsilon_Rk<=2^(-k). Borel-Cantelli then recovers all countably many test answers almost surely, yielding the complete random closed tessellation. This turns injectivity into a concrete conditional-uncertainty estimate. Obstruction: No such decoder or vanishing-error estimate is constructed. Vertex coordinates alone do not supply adjacency automatically, and the dual-map question needs its own decoding argument. Verification: author_checked_partial. No proof file recorded.

### P0409. Joint law of neighboring ideal Voronoi vertices

**Source.** D Achille Curien Enriquez Lyons Unel: Ideal Poisson Voronoi tessellations on hyperbolic spaces (ideal_voronoi_2023), Question7.3; PDF48; Proposition4.4.

**Statement.** Find the joint distribution of all neighboring vertices viewed from a typical vertex of the hyperbolic IPVT. Ledger caveat: Typical means the vertex Palm law, not the cell containing a fixed point. The source gives Gamma(d+1) separation at a typical vertex.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: The vertex graph has constant degree d+1. Under its stationary Palm law, rerooting at a uniformly selected neighbor preserves the marked-vertex marginal by mass transport: send f of the receiving marked vertex along every directed edge with weight 1/(d+1). Outgoing expectation is the neighbor average and incoming mass is f at the root. Thus the separation mark of a uniformly chosen neighbor also has the source Gamma(d+1) marginal. Any proposed joint neighbor formula must reproduce this law, not the Exp(1) law for a volume-typical point. Obstruction: Marginal preservation does not determine dependence between neighboring separation marks, lengths or angles. A joint Palm/Mecke calculation remains missing. Verification: author_checked_partial. No proof file recorded.

### P0410. Hole probabilities for lower-dimensional ideal Voronoi faces

**Source.** D Achille Curien Enriquez Lyons Unel: Ideal Poisson Voronoi tessellations on hyperbolic spaces (ideal_voronoi_2023), Question7.4, hole-probability portion; PDF48.

**Statement.** Compute the probabilities that observation balls miss k-faces of the hyperbolic IPVT for 0<=k<=d-2. Ledger caveat: The face-volume-density portion of the source question is resolved by ideal_face_volumes_2026, Corollary2.1. All dimensions of the remaining hole question are grouped.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: For vertices, let N_B count those in a ball B and let alpha^(2) be the second factorial moment measure. Bonferroni gives 1-E N_B <= P(N_B=0) <= 1-E N_B+(1/2)*E[N_B(N_B-1)], with the lower bound truncated at zero if needed. The known intensity determines E N_B=I_d,0*vol(B), while the next term is alpha^(2)(B times B). Hence the new mean-density formulas identify only the first term of a small-ball expansion; a second-order joint-vertex calculation is already required for a quantitative remainder. Obstruction: The factorial moment measures and a controlled inclusion-exclusion remainder are unavailable here. Treating the vertex process as Poisson merely because the nuclei are Poisson would be unjustified. Verification: author_checked_partial. No proof file recorded.

### P0411. Boundary-hole monotonicity and coefficient positivity for ideal cells

**Source.** D Achille Curien Enriquez Lyons Unel: Ideal Poisson Voronoi tessellations on hyperbolic spaces (ideal_voronoi_2023), Conjecture7.5; PDF48; Proposition5.1 PDF35.

**Statement.** Establish the proposed normalized-hole monotonicity, odd-dimensional positive rational polynomial form, and even-dimensional positive power-series form, with the related decreasing-density behavior. Ledger caveat: The source already gives d=3 explicitly and observes odd-dimensional rationality. The conjunction is counted once. A private partial packet proves monotonicity and odd-dimensional coefficients and gives a negative sixth Maclaurin coefficient in d=2 for the literal displayed distance variable. Remaining even-dimensional density/median claims are not proved; no novelty certification.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: candidate_partial_counterexample. This row was revised 3 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: Put n=d-1 and J=1/H, where H is the boundary-hole probability. The exact source integral, after x=e^(-u)z and q=e^(2u), gives e^(-nu)J=c_d^(-1) integral [sqrt((q+1)^2/4+|z|^2)-(q-1)/2]^(-2n) dz. The bracket strictly decreases with q for z nonzero, so e^(nu)H strictly decreases. When n=2m, a separate radial substitution gives J=e^(2mu)*p_m(e^(2u)), where p_m has degree m and strictly positive rational coefficients, written explicitly as integer-argument beta integrals in the proof packet. Subsequent exact calculation: in dimension two the required f(u)=exp(-u)/H_2(u) has coefficient [u^6]f=61/240-4/(5*pi)<0, since pi<22/7. This is a candidate counterexample to the positive Maclaurin-coefficient clause in the displayed distance variable. Obstruction: No independent review or novelty certification. The literal even-dimensional power-series clause has a candidate counterexample; a different intended variable would require source clarification. Even-dimensional decreasing-density/median claims beyond the source-known d=2 case are not proved here. The grouped entry remains partial. Verification: author_checked_partial. Proof file: proofs/IPVT_boundary_hole_partial.md. (This problem carries 2 attempt records under the same attempt_id; the later, fuller record is reported.)

### P0412. A general transfer theorem between horospherical and hyperbolic typical values

**Source.** D Achille Curien Enriquez Lyons Unel: Ideal Poisson Voronoi tessellations on hyperbolic spaces (ideal_voronoi_2023), Question7.6; PDF48; Section5.3.

**Statement.** Explain by a general theorem the matching typical geometric statistics of the stationary horospherical ideal-cell model and the hyperbolic IPVT. Ledger caveat: The source records several matching examples. Equality for those functionals does not by itself identify the two Palm constructions.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: A change of Palm sampling usually introduces a weight. If random measure tau is w times sigma, then the Campbell identity gives E_tau^0 f=E_sigma^0(w*f)/E_sigma^0 w, provided the intensities are finite and positive. As a diagnostic, equal-probability marks of weights one and two become probabilities 1/3 and 2/3 under weighted sampling. A transfer theorem must therefore identify why the actual geometric weight cancels for the invariant functionals under consideration. Obstruction: The actual horospherical-to-hyperbolic Palm weight, and the class of functionals for which it cancels, are not identified. Matching a few moments does not remove this obligation. Verification: author_checked_partial. No proof file recorded.

### P0413. Low-intensity variance of typical hyperbolic Voronoi cell volume

**Source.** D Achille Curien Enriquez Lyons Unel: Ideal Poisson Voronoi tessellations on hyperbolic spaces (ideal_voronoi_2023), Question7.7; PDF48.

**Statement.** Determine the finite limit, if any, of lambda times the typical-cell volume variance at actual nucleus intensity lambda, and its proposed coupling representation. Ledger caveat: Use lambda for the actual intensity in this entry. The source uses an auxiliary reparametrization in parts of its proofs; no reparametrized intensity is substituted in the Palm identity.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: Let V be typical-cell volume and V0 the zero-cell volume. Volume bias gives E V0=E V^2/E V, while mass conservation gives E V=1/lambda. Therefore E V0-E V=lambda*Var(V) exactly whenever these moments are finite. If a finite-intensity coupling produces a nonnegative excess D_lambda converging in law to the proposed ideal-cell excess D, then Fatou gives only E D<=liminf E D_lambda. A uniform bound on E D_lambda^(1+epsilon) would supply the missing uniform integrability and hence the desired equality of limits. Obstruction: Neither a suitable finite-intensity excess coupling nor uniform integrability is proved. The algebraic variance identity is known Palm calculus and is not claimed as a solution. Verification: author_checked_partial. No proof file recorded.

### P0414. Hausdorff dimension of exceptional rays in the planar ideal Voronoi tree

**Source.** D Achille Curien Enriquez Lyons Unel: Ideal Poisson Voronoi tessellations on hyperbolic spaces (ideal_voronoi_2023), Question7.9; PDF49.

**Statement.** Determine the almost-sure Hausdorff dimension of rays whose separation-mark averages fail the value three obtained along cell-boundary rays. Ledger caveat: The ray space is uncountable. Ergodicity along each ordinary boundary ray is not a simultaneous theorem about every ray.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: A first-moment route would use a uniform large-deviation bound for all rooted length-n paths. If each such path has probability at most exp(-n*I) of a prescribed average deviation, there are 3*2^(n-1) paths in the 3-regular tree, so the expected number of bad prefixes is at most (3/2)*exp(n*(log(2)-I)). In a visual metric where a depth-n cylinder has diameter theta^n, this implies the limsup bad-ray set has dimension at most max(0,(log(2)-I)/log(1/theta)); if I>log2 it is empty by Borel-Cantelli. Obstruction: No uniform deviation rate along arbitrary rays is proved, and a matching lower bound would require a correlated branching construction. One-vertex Gamma marginals are insufficient. Verification: author_checked_partial. No proof file recorded.

### P0415. Canonical intensity and typical-cell laws for unbounded hyperbolic cells

**Source.** Hyperbolic meets stochastic geometry, Oberwolfach57/2025 (hyperbolic_stochastic_2025), Random tessellations overview; PDF16.

**Statement.** Develop natural replacements for cell intensity and the typical-cell distribution when a stationary hyperbolic tessellation contains unbounded cells. Ledger caveat: The source explains that an equivariant finite center cannot be selected for infinite-volume cells by the usual mass-transport construction.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: The bounded-cell Palm relation already exposes the obstruction to simply retaining the old normalization. If finite cell intensity gamma and a probability-valued typical-cell law satisfied gamma*E[volume(C_typ)]=1, assigning positive typical probability to infinite-volume cells would make the left side infinite for every gamma>0. Thus a putative extension must change the sampling measure, allow a sigma-finite object, or restrict the observables. A boundary- or horosphere-based sampling scheme is a possible route, but needs its own invariance statement. Obstruction: No canonical replacement measure or uniqueness principle is constructed. The contradiction applies to preserving the usual finite-intensity volume Palm identity, not to every conceivable generalized notion. Verification: author_checked_partial. No proof file recorded.

### P0416. Amenability of ideal Bernoulli Voronoi relations on nonexact groups

**Source.** Jardon Sanchez Mellick Poulin Wrobel: Exactness and topology of invariant random equivalence relations (exactness_ire_2025), Question1; PDF18; Theorem4.5.

**Statement.** Determine whether ideal Bernoulli Voronoi equivalence relations are amenable for arbitrary countable groups, beyond the theorem for exact groups. Ledger caveat: Limits of arbitrary finite invariant equivalence relations can be nonamenable on nonexact groups. That theorem is not automatically a Voronoi counterexample.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: Uniform probability measures on finite approximating cells do not automatically pass to invariant probability kernels on the limiting classes. The elementary sequence uniform[-n,n] on Z has mass 1/(2n+1) at each included point; every coordinate tends to zero, so its pointwise limit is the zero measure, not a probability measure. For the Voronoi limit, a proof must retain an appropriate Reiter or hyperfinite approximation with a uniform error bound, rather than taking an unqualified limit of the finite-cell averages. Obstruction: No Voronoi-specific uniform amenability estimate is proved. Conversely, the known arbitrary finite-relation counterexamples need not arise from low-density Voronoi cells. Verification: author_checked_partial. No proof file recorded.

### P0417. Regular exponential volume growth without full graph IPVT convergence

**Source.** D Achille and Khezeli: Convergence towards Ideal Poisson Voronoi tessellations with a focus on Diestel Leader graphs (ideal_convergence_2026), Question7.1; PDF49; Theorem1.3.

**Statement.** Find or rule out a transitive graph with log-regularly-varying growth for which the boundary-measure convergence required in Theorem1.3 fails. Ledger caveat: The intensity phase condition in Theorem1.3 is retained. Ordinary full convergence across all intensity phases is a different issue.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: Write nu_n for the uniform ball measure in the horocompactification and sigma_n for the uniform sphere measure. If F(n-1)/F(n)->1/p, then nu_n is asymptotically (1-1/p)*sigma_n+(1/p)*nu_(n-1). Alternating sphere limits alpha,beta would therefore produce ball subsequential limits (p*alpha+beta)/(p+1) and (alpha+p*beta)/(p+1), which differ whenever alpha differs from beta. This isolates the required mechanism: stable volume ratios can coexist algebraically with oscillating directional mass. Obstruction: The missing step is realizing such directional oscillation in a transitive or Cayley graph with the prescribed volume growth. An abstract sequence of sphere measures is not such a graph. Verification: author_checked_partial. No proof file recorded.

### P0418. Non-Poisson low-intensity ideal Voronoi diagrams

**Source.** D Achille and Khezeli: Convergence towards Ideal Poisson Voronoi tessellations with a focus on Diestel Leader graphs (ideal_convergence_2026), Question7.2; PDF49.

**Statement.** Construct a nontrivial low-intensity ideal diagram with a law different from the IPVT using a non-Poisson nuclei process. Ledger caveat: The source suggests the alpha-hyperbolic ensemble. Merely making the finite-intensity point process non-Poisson need not alter the limiting diagram.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: A simple global Cox mixture cannot achieve the target when the underlying Poisson model has a unique intensity-independent limit. Let Z be any positive finite random variable and, conditionally on Z, take a Poisson nuclei process of intensity lambda*Z. For every bounded continuous diagram test f, conditional convergence at each fixed Z=z gives E[f(V_lambda)|Z=z]->E[f(V_IPVT)]. Dominated convergence then yields the same unconditional IPVT law. Randomizing the global intensity changes finite-scale counts but not this unique limit. Obstruction: Need spatial dependence that survives the boundary-and-delay limit. The Cox comparison does not analyze the determinantal candidate or construct a distinct nontrivial limit. Verification: author_checked_partial. No proof file recorded.

### P0419. Equal-growth L1 products beyond the divergent tilted-volume condition

**Source.** D Achille and Khezeli: Convergence towards Ideal Poisson Voronoi tessellations with a focus on Diestel Leader graphs (ideal_convergence_2026), Question7.3; PDF49; Proposition5.14(i).

**Statement.** Determine IPVT convergence for equal-growth product factors when the tilted-volume integrals required in Proposition5.14(i) need not diverge. Ledger caveat: The source condition is integral exp(-b*s)dF(s)=infinity for each factor, with their common growth exponent b. The following is a radial comparison model only.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: Consider two equal radial densities proportional at large r to exp(b*r)*(1+r)^(-a), a>1. On a large L1 sphere, the split at radius s has weight proportional to (1+s)^(-a)*(1+R-s)^(-a). The contribution from epsilon*R<=s<=(1-epsilon)*R is O(R^(1-2a)), whereas either fixed endpoint region contributes order R^(-a). Their ratio tends to zero because a>1. Thus equal exponential growth alone need not force both factor radii to diverge; endpoint concentration can replace the tensor product of two boundary laws. Obstruction: The model is not asserted to be a homogeneous geometric counterexample. A general theorem needs precise radial regularity, the endpoint mixture weights, and nondegeneracy of the resulting ideal diagram. Verification: author_checked_partial. No proof file recorded.

### P0420. Low-intensity Voronoi limits for products with the L2 metric

**Source.** D Achille and Khezeli: Convergence towards Ideal Poisson Voronoi tessellations with a focus on Diestel Leader graphs (ideal_convergence_2026), Question7.4; PDF49.

**Statement.** Give conditions and identify the limiting boundary measure for products with the L2 metric, including comparison with an appropriately weighted L1 model. Ledger caveat: The source conjectures a relation under mild conditions. A formal saddle-point calculation alone is not a convergence theorem.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: If radial shell densities have leading exponents b*r1 and bprime*r2 with both positive, their product on r1^2+r2^2=R^2 is governed by maximizing b*r1+bprime*r2. Cauchy-Schwarz gives the unique maximum B*R at (r1,r2)=R*(b,bprime)/B, B=sqrt(b^2+bprime^2). Taylor expansion of the product distance then suggests the limiting horofunction (b*h1+bprime*h2)/B. The second derivative in r1 at the maximizer is -B^3/(bprime^2*R), so the radial split fluctuates on the sqrt(R) scale under regular Laplace asymptotics. Obstruction: Need uniform asymptotics for shell measures and angular laws, control of the saddle-point tails, and convergence of the boundary measures. Exponential rates alone do not justify these steps. Verification: author_checked_partial. No proof file recorded.

### P0421. Convergence of edge-measured product-graph Voronoi diagrams

**Source.** D Achille and Khezeli: Convergence towards Ideal Poisson Voronoi tessellations with a focus on Diestel Leader graphs (ideal_convergence_2026), Question7.5; PDF49; Theorem4.12.

**Statement.** Characterize when weighted edge-measured product graphs satisfy the full low-intensity convergence criterion of Theorem4.12. Ledger caveat: The theorem involves boundary behavior of edge endpoints; a vertex measure alone can lose this information.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: For a finite weighted edge set, choosing an edge proportionally to its weight and then a uniform endpoint samples vertices with probability proportional to weighted degree. Thus a uniform-vertex limit need not equal the endpoint limit when degrees or weights vary. Even knowledge of both endpoint marginals does not identify their joint boundary law: an equal mixture of pairs (0,0),(1,1) and an equal mixture of (0,1),(1,0) have the same marginals but disjoint supports. Product-edge convergence must retain the endpoint-pair measure and horizontal/vertical edge weights. Obstruction: No convergence estimate for the actual product-graph endpoint measure is proved. The pair-law example is an information diagnostic, not a constructed graph counterexample. Verification: author_checked_partial. No proof file recorded.

### P0422. More than two distinguishable types of group IPVT cells

**Source.** D Achille and Khezeli: Convergence towards Ideal Poisson Voronoi tessellations with a focus on Diestel Leader graphs (ideal_convergence_2026), Question7.6; PDF49; Proposition6.7.

**Statement.** Construct or rule out group IPVTs with a finite number of distinguishability types greater than two, or infinitely many types. Ledger caveat: The directed Diestel-Leader/group-action example already has two types. The symmetry group is part of the statement: the undirected automorphism group can merge those types.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused 2026-09-07 primary literature check; 2026 convergence/face-density and 2024 indistinguishability results matched. Present openness and novelty not certified.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact integral manipulation, Palm calculus, mass transport, limiting obstruction or conditional construction. Result: A sufficient construction route is an equivariant recoverable nucleus mark. Suppose the limiting boundary decomposes into invariant measurable sets A1,...,Ak of positive intensity, nuclei in every Ai produce nonempty cells, and the associated boundary label can be reconstructed measurably from each cell and its diagram. Then selecting cells whose label is Ai is an equivariant rule, so these classes are distinguishable. Independent restrictions of the boundary Poisson process preserve all k label populations, but geometric visibility of those nuclei remains an additional requirement. Obstruction: No group with the required boundary decomposition and visibility properties is constructed. The criterion gives at least k distinguishable classes, not exactly k; within-class indistinguishability still requires proof. Verification: author_checked_partial. No proof file recorded.

### P0423. Ideal Voronoi face-volume intensities

**Source.** D Achille Curien Enriquez Lyons Unel: Ideal Poisson Voronoi tessellations on hyperbolic spaces (ideal_voronoi_2023), Question7.4, density portion; PDF48.

**Statement.** Compute all ideal k-face volume densities.

**Status.** Historical status: source_says_open. Current-literature status: resolved_in_literature (no status-search record recorded in the ledger). Resolution record: ideal_face_volumes_2026, Corollary2.1 and Remark2.2; PDF6. The theorem computes every density and Remark2.2 explicitly identifies D_d,k with the original tilde-I_d,k notation. The separate hole probabilities remain P0410. Admission: not admitted; result_status: known_result_not_original.

**Our work.** Not admitted (result_status: known_result_not_original); see the resolution record above. No attempt is recorded for this row in attempts.jsonl.

### P0424. Indistinguishability of hyperbolic ideal Voronoi cells

**Source.** D Achille Curien Enriquez Lyons Unel: Ideal Poisson Voronoi tessellations on hyperbolic spaces (ideal_voronoi_2023), Question7.8; PDF48-49.

**Statement.** Prove that ideal hyperbolic Voronoi cells admit no nontrivial equivariant selection.

**Status.** Historical status: source_says_open. Current-literature status: resolved_in_literature (no status-search record recorded in the ledger). Resolution record: ideal_indistinguishable_2024, Theorem1; PDF1. The source update explicitly credits Mellick. His Theorem1 includes real hyperbolic symmetric spaces and states indistinguishability. Admission: not admitted; result_status: known_result_not_original.

**Our work.** Not admitted (result_status: known_result_not_original); see the resolution record above. No attempt is recorded for this row in attempts.jsonl.

### P0425. Optimal parallel allocation with unknown nonexponential job sizes

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section3.2; PDF8.

**Statement.** For Poisson arrivals and a common concave speedup curve, characterize the mean-response-time optimal allocation when inherent sizes are unknown and nonexponential. Ledger caveat: The exponential EQUI theorem is already known; the scheduler observes attained service and the size law. Multiple servers and sublinear parallel speedup are essential to the remaining question.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: For an absolutely continuous size law with hazard h, a job at attained service a allocated b servers completes at instantaneous rate h(a)*s(b), while its age advances at rate s(b). A formal controlled generator therefore has both an age-drift term s(b)*partial_a V and a completion term h(a)*s(b)*(V_after_departure-V). Maximizing the departure rate alone drops the learning and continuation terms. The common exponential case removes age learning but does not justify that omission for a general size law. Obstruction: No solution of the infinite-state average-cost control equation or verification theorem is supplied. Verification: author_checked_partial. No proof file recorded.

### P0426. Optimal known-size parallel allocation with Poisson arrivals

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section3.3; PDF10.

**Statement.** Determine optimal mean-response-time allocation for known-size parallel jobs arriving over time under a common concave speedup curve. Ledger caveat: The all-jobs-at-zero case has later general concave algorithms; it is excluded separately. Those offline results do not solve the Poisson-arrival problem.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: With remaining-work vector x, arrival rate lambda, and relative value V, the formal average-cost equation is g=m+lambda*E[V(x appended with S)-V(x)]-max_{sum b_i<=n} sum_i s(b_i)*partial_i V(x). Interior allocations must satisfy s_prime(b_i)*partial_i V=nu. Thus the offline allocation can persist only if the stochastic value gradients preserve the required ratios; arrivals explicitly couple all coordinates through the appended-state term. Obstruction: The value gradients, boundary conditions at completion, recurrence assumptions and optimality verification remain unknown. Verification: author_checked_partial. No proof file recorded.

### P0427. Optimal allocation between two exponential parallelism classes

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section3.4; PDF10-11.

**Statement.** Characterize optimal allocation when two classes have different ordered concave speedup curves and unknown exponential inherent sizes. Ledger caveat: The source already shows that instantaneous maximum-throughput allocation need not minimize delay. This attempt supplies a small diagnostic, not a new counterexample claim.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: Even with two jobs and no arrivals, continuation values change the allocation. Take four divisible servers and independent Exp(1) inherent job sizes. Use normalized concave speedups s1(b)=min(b,sqrt(b)) and s2(b)=min(b,b^(3/4)), including linear fractional-server behavior below one server. Allocate b to class one and 4-b to class two until the first completion, then all four to the survivor. Expected sum of completion times is V(b)=[2+s1(b)/(2*sqrt(2))+s2(4-b)/2]/[s1(b)+s2(4-b)]. The throughput maximizer is b=1: total rate increases below one and decreases above it. Yet V(81/64)<V(1). The slower departure rate improves the continuation state. Obstruction: The no-arrival diagnostic does not determine a stationary optimal policy with Poisson arrivals, nor prove a universal allocation formula. Verification: author_checked_partial. No proof file recorded.

### P0428. Mean-response optimization for stochastically arriving DAG jobs

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section4; PDF13-14.

**Statement.** Find optimal scheduling or tractable mean job-response laws for DAG jobs with random arrivals and task durations, retaining task precedence. Ledger caveat: Different graph shapes and information models must be specified. This attempt uses known finite DAGs and independent exponential task times as a concrete submodel.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: Total work does not identify a job duration. Two independent Exp(mu) tasks in parallel have mean completion time 3/(2*mu), while the same two tasks in a serial chain have mean 2/mu; both have mean total work 2/mu. For general DAGs a Markov state must retain the completed downward-closed vertex set and currently served eligible tasks. Lower bounds are the expected critical-path duration and expected total work divided by server count, but neither retains inter-job interference. Obstruction: No optimal stochastic DAG allocation or stationary response formula is derived. Worst-case offline guarantees are not substituted for the stochastic objective. Verification: author_checked_partial. No proof file recorded.

### P0429. Largest growing fork-join batch compatible with asymptotic independence

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section5; PDF16.

**Statement.** Determine how quickly the number k(n) of tasks per uniformly routed job can grow while the corresponding k(n) stationary queues remain asymptotically independent. Ledger caveat: The source credits k=o(n^(1/4)); fixed-dimensional convergence alone does not answer the growing-dimensional question. Private author-only packet extends the credited coupling under exponential service. Later primary-source leads do not establish novelty.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: candidate_partial_counterexample. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: A finite-horizon input coupling suggests a cubic collision scale. Fix k tagged servers. Jobs arrive at rate Lambda=lambda*n/k and choose a uniform k-subset. If N is the number of tagged servers hit by an arrival, E[N(N-1)]=k*(k-1)*k*(k-1)/(n*(n-1)). Remove arrivals that hit at least two tagged queues and restore their lost marginal rates by independent Poisson streams. A union bound on removed events and added events is at most (3/2)*Lambda*T*E[N(N-1)], hence at most 3*lambda*T*k*(k-1)^2/(2*(n-1)). The resulting streams are independent with the correct marginal rates. With independent task marks and queues initially empty, this also bounds total variation of their workload paths on [0,T]. Extending the credited source coupling to stationary starts gives TV<=2*k*r(T)+3*lambda*T*k*(k-1)^2/(2*(n-1)), where r(T) is the stationary marginal emptying tail. With independent exponential service of rate mu>lambda, a stopped generator calculation gives r(T)<=(1+sqrt(lambda/mu))*exp(-(sqrt(mu)-sqrt(lambda))^2*T). Taking T=2*log(n)/(sqrt(mu)-sqrt(lambda))^2 gives sufficient k=o((n/log(n))^(1/3)). A conditional polynomial tail r(T)<=C*T^(-p) gives sufficient exponent p/(3*p+1). Obstruction: Partial exponential-service sufficient regime only. No optimal threshold, boundary k of order n^(1/3), general-service improvement, correlated-mark result, uniform heavy-traffic result or novelty certification. The basic source coupling is credited. Verification: author_checked_partial. Proof file: proofs/Limited_forkjoin_stationary_exponential_partial.md. (This problem carries 2 attempt records under the same attempt_id; the later, fuller record is reported.)

### P0430. Response laws for limited fork-join shortest-queue dispatching

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section5; PDF16.

**Statement.** Analyze job response time when k distinct tasks are sent to the k shortest queues or the k least-workload queues. Ledger caveat: Random-routing independence results do not transfer automatically to state-dependent routing; queue-length and workload policies use different information.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: For queue-length vector q and a simultaneous unit increment on selected set A of size k, the quadratic potential changes by 2*sum_{i in A}q_i+k. Selecting the k shortest queues minimizes this one-step drift over all distinct-server choices. Uniform selection instead gives mean increment 2*k*sum_i q_i/n+k. This establishes a local balancing property, but the response of the job is the maximum of its task sojourn times, which also depends on residual service and the joint selected-state law. Obstruction: No stationary maximum-sojourn law or optimality for mean job response follows from the quadratic drift inequality. Verification: author_checked_partial. No proof file recorded.

### P0431. Straggler replication in queued limited fork-join systems

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section5; PDF16-17.

**Statement.** Analyze and optimize selective straggler replication when a fork-join job completes only after every task completes and replicas also encounter queues. Ledger caveat: This adds a job-level maximum and delayed replication to the simpler correlated single-task redundancy questions P0400-P0404.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: In the no-queue, independent exponential diagnostic, two simultaneous replicas each at rate mu complete after Exp(2*mu), while expected total server effort is 2/(2*mu)=1/mu, equal to one original. With a deterministic overhead c followed by Exp(mu), cancellation at first completion instead consumes mean effort 2*c+1/mu versus c+1/mu without replication. Thus a service-time shift can reverse the apparent free speedup before any waiting is considered. In a k-task job this replication helps only if the replicated task controls the maximum. Obstruction: The diagnostic does not quantify queue feedback, correlation, delayed starts or the stationary fork-join response distribution. Verification: author_checked_partial. No proof file recorded.

### P0432. Optimal known-size multiserver scheduling beyond SRPT

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section7.1.1; PDF21; later SEK-SMOD paper Theorem4.1.

**Statement.** Characterize nonasymptotic optimal mean-response scheduling and sharp performance bounds in the known-size M/G/k queue. Ledger caveat: The later SEK-SMOD result already outperforms SRPT-k in its stated scope. Existence of any improvement over SRPT-k is no longer admitted as open.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: A first-arrival decomposition explains why no-arrival optimality is insufficient. For two policies coupled until a selected state, assume their cost difference through recoupling is integrable and let D(t) be its conditional expectation given that the next arrival occurs at time t, including their specified continuation rules. Under a Poisson rate lambda, the expected difference is integral_0^infinity lambda*exp(-lambda*t)*D(t) dt. The sign of D on an intermediate interval can outweigh both early-arrival harm and a favorable no-arrival endpoint. A global comparison must also bound the cost until recoupling; comparing only the first completed job misses that term. Obstruction: No new policy comparison or sharp universal lower bound is proved. The later source resolves the improvement-existence subquestion, not full optimal control. Verification: author_checked_partial. No proof file recorded.

### P0433. Optimal dispatching to SRPT queues outside heavy traffic

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section7.1.1; PDF21-22.

**Statement.** Determine a mean-response-optimal dispatcher to separate SRPT servers at nonasymptotic loads. Ledger caveat: Guardrails heavy-traffic optimality is credited. This attempt distinguishes current workload from the incremental delay imposed on existing jobs.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: Consider two unit-speed SRPT queues with no future arrivals: queue one holds one job of residual size 100; queue two holds ten jobs of residual size 0.1 each. A new job of size 0.05 preempts either queue and finishes in 0.05. Sending it to queue one delays one existing completion by 0.05; sending it to queue two delays ten existing completions by 0.05 each. Thus the total incremental completion cost is 0.10 versus 0.55, although queue two has much less workload. Least workload is not the correct one-step objective for this size-aware setting. Obstruction: Future arrivals and the stationary distribution of dispatcher states are omitted. The example is a diagnostic against a proposed greedy criterion, not the optimal dispatcher. Verification: author_checked_partial. No proof file recorded.

### P0434. Sharp approximation ratio for simple alternatives to Gittins

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section7.1.2; PDF22-23.

**Statement.** Improve or identify the sharp worst-case mean-response approximation factor for M-SERPT or other simple age-based policies in M/G/1. Ledger caveat: The source credits a factor-five guarantee. Heavy-traffic factor-two results and the conjectured sharp factor two are distinct from a uniform all-load guarantee.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: A two-job calculation isolates the value of probing. Job A has size 0.01 with probability 0.9 and 100 with probability 0.1; job B has known size 2. SERPT initially selects B because E[A]=10.009. Completing B before A gives expected sum of completion times 14.009. Serving A for 0.01, then serving B if A survives, gives 0.9*(0.01+2.01)+0.1*(102+2.01)=12.219. The Gittins stopping ratio at probe duration 0.01 is 0.01/0.9, smaller than B rank 2. Any approximation proof based only on expected residual size loses this probing advantage. Obstruction: This finite instance does not establish a stationary approximation factor, nor distinguish the full worst-case ratios of SERPT and M-SERPT. Verification: author_checked_partial. No proof file recorded.

### P0435. Optimal nonasymptotic scheduling with unknown sizes in M/G/k

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section7.1.2; PDF23.

**Statement.** Characterize optimal nonanticipating mean-response policies with multiple servers when sizes are unknown but their law and attained service are observed. Ledger caveat: Gittins single-server optimality and multiserver heavy-traffic results are known. No universal finite-load optimality is assumed.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: For exponential sizes with a common rate mu, every nonidling policy has the same queue-count death rate mu*min(m,k), so scheduling is immaterial for that special law. With nonexponential sizes the departure intensity becomes sum_i h(a_i) over served jobs, and the age vector has policy-dependent drift. Thus queue count ceases to close: two states with equal m but different service ages can have different next-departure laws. A proposed extension of the exponential argument must retain this age information and its effect on future capacity. Obstruction: No optimal age-vector control is constructed. The reduction supplies a known special case and an obstruction to extending its proof. Verification: author_checked_partial. No proof file recorded.

### P0436. Optimal finite-deadline success scheduling

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section7.2; PDF24-25.

**Statement.** Minimize the fraction of known-size Poisson arrivals missing a common relative deadline D, with an explicit convention that dropped jobs count as failures. Ledger caveat: This is a finite-threshold objective; large-time tail asymptotics alone do not solve it. The source discusses preemptive and dropping policies.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: A deadline-success value must carry remaining slack as well as remaining work. For a job arriving at a with size x, slack at t is a+D-t-x_remaining. Two equal-work jobs can have opposite feasibility depending on arrival age. Moreover an admission rule using only current feasibility ignores the opportunity cost of accepted work: a size close to D may be feasible now but block many later short jobs. In a finite-horizon control equation the immediate reward is a unit success at completion before the deadline, rather than the running holding cost used for mean response. Obstruction: The stationary success-maximizing policy, admissible preemption/drop rules and its verification remain unresolved. Verification: author_checked_partial. No proof file recorded.

### P0437. Dropping probability and optimality gap of DTLH

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section7.2; PDF24.

**Statement.** Determine the stationary loss probability and performance gap of Drop-The-Larger-Hopeless in the source model. Ledger caveat: A precise implementation must specify which eligible larger waiting job is removed. Loss probabilities refer to all arrivals, including removed old jobs.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: Total workload alone does not determine the next admission outcome. Let the in-service residual be 0.1, the waiting workload be 0.8, D=1, and the new job have size 0.5. If the waiting line is one size-0.8 job, removing it makes the newcomer feasible. If the waiting line is two size-0.4 jobs, neither is larger than the newcomer, so the newcomer is dropped. Both states have total workload 0.9. A Markov analysis needs the ordered waiting-size/slack state, not just a reflected scalar workload. Obstruction: No stationary ordered-state law or approximation ratio is obtained; the example diagnoses insufficient state information. Verification: author_checked_partial. No proof file recorded.

### P0438. Feasibility of class-specific response quantiles

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section7.3; PDF25-26.

**Statement.** Characterize scheduling feasibility for several classes with different response deadlines and allowed miss fractions. Ledger caveat: The source gives distinct class SLOs. A class-blind aggregate quantile cannot substitute for all class-specific constraints.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: For class i with nonparallel intrinsic service S_i and deadline D_i, every policy obeys P(T_i>D_i)>=P(S_i>D_i). Also an aggregate miss rate is a weighted average sum_i p_i*m_i and does not bound each m_i: if a rare class has probability 0.005 and all its jobs miss while the rest succeed, aggregate misses are 0.005 but that class has miss rate one. Thus aggregate feasibility and even workload stability leave separate unavoidable class constraints. Obstruction: These necessary conditions are not sufficient; no policy is proved to attain the feasible vector of quantiles. Verification: author_checked_partial. No proof file recorded.

### P0439. Server provisioning for a finite response-time SLO

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section7.3; PDF26.

**Statement.** Find the minimum server count and a feasible scheduling policy that meet a prescribed response-time quantile under a specified stochastic workload. Ledger caveat: The exponential FCFS model is a known benchmark only. General service laws and policy choice are part of the source question.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: For the stable M/M/k FCFS benchmark with total arrival rate Lambda and service rate mu per server, let C be Erlang-C and a=k*mu-Lambda. Waiting time is zero with probability 1-C and otherwise Exp(a), independent of the tagged Exp(mu) service. For a!=mu this gives P(T>t)=(1-C)*exp(-mu*t)+C*[mu*exp(-a*t)-a*exp(-mu*t)]/(mu-a). At a=mu the bracket is exp(-mu*t)*(1+mu*t). This gives a reproducible benchmark for each k; simply using the waiting-time tail as the response-time tail would omit service. Obstruction: The benchmark neither proves the minimum k over all policies nor transfers to M/G/k. No new general staffing rule is established. Verification: author_checked_partial. No proof file recorded.

### P0440. Waiting-time tails with deterministic multiserver setup

**Source.** Williams Wang Harchol-Balter: An Upper Bound on the M M k Queue With Deterministic Setup Times (queues_deterministic_setup_2025), Section8; PDF39.

**Statement.** Obtain higher-moment or tail bounds for the M/M/k system with deterministic simultaneous setup times and the paper specified cancellation policy. Ledger caveat: The source already supplies multiplicatively matching mean bounds in its parameter regime; that mean result is not recounted as open.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: For a state with m jobs and z busy servers, the count part of the generator applied to exp(theta*m) is [Lambda*(exp(theta)-1)+mu*z*(exp(-theta)-1)]*exp(theta*m). It is negative when z is sufficiently large, but positive when every server is in setup. Thus a one-step exponential drift estimate cannot hold uniformly on large-m states using m alone. A useful Lyapunov function must include residual setup times, or the proof must use a time interval long enough for setup completion while controlling cancellations. Obstruction: No tail exponent or higher-moment bound with verified constants is obtained. Mean bounds alone do not certify the tail. Verification: author_checked_partial. No proof file recorded.

### P0441. Deterministic DelayedOff waiting-power tradeoff

**Source.** Williams Wang Harchol-Balter: An Upper Bound on the M M k Queue With Deterministic Setup Times (queues_deterministic_setup_2025), Section8; PDF39-40.

**Statement.** Analyze waiting and power for deterministic setup when idle servers remain on for a grace interval gamma before switching off. Ledger caveat: The source distinguishes these policies from its instantaneous-off model and credits earlier exponential-setup studies.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: A single idle-gap diagnostic is exact: for next-arrival gap G~Exp(Lambda), the chance the server becomes cold is exp(-Lambda*gamma), and expected on-idle duration is E[min(G,gamma)]=(1-exp(-Lambda*gamma))/Lambda. If a cold arrival triggers deterministic setup beta, that arrival incurs beta*exp(-Lambda*gamma) expected setup delay. The local marginal tradeoff follows by differentiation, but a full renewal cycle also includes later arrivals during setup, active service and possible setup cancellation. Obstruction: The idle-gap calculation is not a stationary many-server mean or a globally optimal grace period. Verification: author_checked_partial. No proof file recorded.

### P0442. Optimal waiting-power Pareto frontier with deterministic setup

**Source.** Williams Wang Harchol-Balter: An Upper Bound on the M M k Queue With Deterministic Setup Times (queues_deterministic_setup_2025), Section8; PDF40.

**Statement.** Characterize the attainable and optimal tradeoff between mean waiting time and average power over admissible multiserver on-off policies. Ledger caveat: This ranges over all policies, whereas P0441 analyzes one specified family. Always-on is the source-known minimum-wait endpoint.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: Let a stationary occupation measure record active, idle-on, setting-up and off servers. Average power is a linear functional of that measure, while mean waiting equals E[Q]/Lambda by Little law when finite. Minimizing E[Q]/Lambda+eta*E[power] for eta>=0 produces supported frontier points. If policies share a common regenerative empty/reset state and have finite cycle moments, randomizing between them at those epochs produces convex mixtures of cycle reward rates. The mixing weight is cycle-length biased; averaging policy labels without that correction gives the wrong frontier. Obstruction: No feasible occupation-measure characterization, optimal control solution, or proof that DelayedOff spans the frontier is supplied. Verification: author_checked_partial. No proof file recorded.

### P0443. Closed-form performance bounds for general setup distributions

**Source.** Williams Wang Harchol-Balter: An Upper Bound on the M M k Queue With Deterministic Setup Times (queues_deterministic_setup_2025), Section8; PDF40.

**Statement.** Extend closed-form multiserver setup bounds to exponential, phase-type or two-point setup times under explicitly stated restart/cancellation semantics. Ledger caveat: Exact numerical matrix formulas already exist in some models; a simple parameter-explicit bound and its error are the remaining target.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: The mean setup time alone loses a basic renewal quantity. If setup durations B are sampled independently with finite second moment and a time observer samples a stationary setup interval, the residual mean is E[B^2]/(2*E[B]). Deterministic B=beta gives beta/2, while Exp(mean beta) gives beta. But an arrival that initiates a setup samples the original B, not this length-biased residual. Therefore neither substituting the same mean nor blindly inserting the residual-life formula yields a correct multiserver approximation. Obstruction: The inspection-paradox calculation is a diagnostic only. Actual queue-coupled setup intervals and cancellation can violate its independent renewal assumptions. Verification: author_checked_partial. No proof file recorded.

### P0444. Computational complexity of the multiserver-job stability threshold

**Source.** The Multiserver Job Stochastic Recurrence Equation for Cloud Computing Performance Evaluation (queues_msj_recurrence_2026), Section5; PDF11.

**Statement.** Determine the complexity and certified approximation accuracy of the saturated pile growth rate gamma that defines the FCFS multiserver-job stability threshold. Ledger caveat: The source already establishes the threshold representation lambda_c=1/gamma. A stopped simulation with small successive change is not automatically a certified estimate.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: For the special case where every job needs b servers, put c=floor(s/b). The saturated system is a c-machine list schedule. Its maximum completion time after n jobs is at least total service/c and at most total service/c+(1-1/c)*max_{j<=n}S_j. For iid finite-mean service, total service/n->E[S] and max S_j/n->0 almost surely, so gamma=E[S]/c. Heterogeneous demands break this scalar packing reduction. In the general estimator, a small difference between consecutive sample means does not bound the distance from their limiting value. Obstruction: No general finite-sample certificate or computational complexity bound is derived; the equal-demand case is a credited classical scheduling reduction. Verification: author_checked_partial. No proof file recorded.

### P0445. Monotone workload recurrences beyond FCFS multiserver jobs

**Source.** The Multiserver Job Stochastic Recurrence Equation for Cloud Computing Performance Evaluation (queues_msj_recurrence_2026), Section10; PDF22.

**Statement.** Identify scheduling disciplines beyond FCFS whose multiserver-job workload maps preserve the monotonicity needed by the source framework. Ledger caveat: The paper proves monotonicity for its FCFS map. A different queue discipline needs its own state and order, not merely the same name for workload.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: Compositions of coordinatewise isotone primitive maps remain isotone: if x<=y, first F(x)<=F(y), then G(F(x))<=G(F(y)). Consequently, a policy using an exogenously fixed sequence of the same monotone primitives inherits the comparison. An adaptive scheduler instead selects F_{a(x)} at state x and F_{a(y)} at y; isotonicity of each separate F_a gives no comparison between those two values. In one dimension, F0(x)=x and F1(x)=x+10 are both increasing, but selecting F1 below threshold one and F0 above it makes the chosen map decrease at the threshold. Obstruction: No new non-FCFS discipline is proved monotone. A queue-specific comparison requires controlling policy switches and the admissible arrival order. Verification: author_checked_partial. No proof file recorded.

### P0446. Perfect multiserver-job samples with a stability-matching upper bound

**Source.** The Multiserver Job Stochastic Recurrence Equation for Cloud Computing Performance Evaluation (queues_msj_recurrence_2026), Section10; PDF22.

**Statement.** Construct computable stationary upper bounds with the same stability region as the FCFS multiserver-job queue, enabling perfect rather than sub-perfect samples. Ledger caveat: The source already obtains monotone lower samples that eventually couple; detecting that coupling is a separate problem.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: Serializing every job yields a simple potential dominating workload but may destroy the needed stability region. With two servers, single-server-demand iid service of mean one, and arrival rate 1.5, the actual M/G/2 has load 0.75, while an all-jobs-serialized M/G/1 has load 1.5 and no finite stationary workload. Thus this upper-bound construction cannot support perfect sampling throughout the true stable region. Nor does observing a lower sequence remain constant over a finite number of lookback extensions certify that it will never jump later. Obstruction: No stability-matching dominating chain or detectable coalescence criterion is constructed. Verification: author_checked_partial. No proof file recorded.

### P0447. Finite-size response characterization for classical fork-join queues

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section5; PDF15; later fork-join extreme-value theorem.

**Statement.** Obtain a tractable sharp finite-n response characterization for classical fork-join queues beyond the two-server special case. Ledger caveat: Later normal-limit results identify a logarithmic centering constant in their light-tailed regime. This entry retains only the finite-size joint-law question, not the older unresolved-constant claim.

**Status.** Historical status: source_says_open. Current-literature status: unverified (Focused later-primary-source checks on 2026-09-07; offline concave scheduling, general FCFS threshold representation, SEK-SMOD and fork-join asymptotics credited. No present-openness certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Controlled generators, exact finite-state diagnostic, coupling, renewal reward or capacity comparison. Result: In a stable exponential-service fork-join model with common Poisson arrivals, independent task services alone give E[T_job]>=H_n/mu, where H_n is the nth harmonic sum, because waiting times are nonnegative. An independence approximation applied to stationary task sojourns would give H_n/(mu-Lambda), but shared arrivals make those sojourns dependent. Computing each marginal M/M/1 law therefore does not identify the maximum. The gap between these two scales also warns against replacing a finite-n maximum by its asymptotic centering without a remainder bound. Obstruction: No finite-n joint transform or sharp error bound is obtained. The independent-sojourn expression is explicitly an approximation unless a separate association comparison is invoked. Verification: author_checked_partial. No proof file recorded.

### P0448. Offline common-concave speedup allocation

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section3.3 PDF10.

**Statement.** Offline common-concave speedup allocation

**Status.** Historical status: source_says_open. Current-literature status: resolved_in_literature (no status-search record recorded in the ledger). Resolution record: queues_concave_resolution_2025, Sections2 and5; PDF3-4,14-15. The later paper provides SmartFill for known jobs all present at zero with a common strictly concave differentiable increasing speedup and compatible weights. This resolves the main offline smooth common-curve subproblem; no Poisson-arrival extension is claimed. Admission: not admitted; result_status: known_result_not_original.

**Our work.** Not admitted (result_status: known_result_not_original); see the resolution record above. No attempt is recorded for this row in attempts.jsonl.

### P0449. General FCFS multiserver-job stability representation

**Source.** Harchol-Balter: Open problems in queueing theory inspired by datacenter computing (queues_computing_frontiers_2021), Section2 PDF5.

**Statement.** General FCFS multiserver-job stability representation

**Status.** Historical status: source_says_open. Current-literature status: resolved_in_literature (no status-search record recorded in the ledger). Resolution record: queues_msj_recurrence_2026, Theorem5.1; PDF11. The later theorem gives lambda_c=1/gamma using the saturated pile growth rate for the stated stationary input framework. This credits the representation; evaluation complexity remains P0444 and no blanket critical-boundary claim is added. Admission: not admitted; result_status: known_result_not_original.

**Our work.** Not admitted (result_status: known_result_not_original); see the resolution record above. No attempt is recorded for this row in attempts.jsonl.

### P0450. Conditional generation limits for the Erlang weighted tree

**Source.** Moharrami, Subramanian, Liu and Sundaresan: The Erlang Weighted Tree, A New Branching Process (v5, 27 May 2023) (erlang_weighted_tree_2023), Section4, question1; PDF15-16.

**Statement.** Determine survival-conditioned generation laws and their proper normalization for critical and subcritical Erlang weighted trees, including conditioning on later survival. Ledger caveat: The source groups these conditional-limit versions. Its displayed notation mixes a counting measure with its type space; the target must distinguish total population from the finite point-measure law. Critical unscaled tightness cannot be assumed.

**Status.** Historical status: source_says_open. Current-literature status: unverified (2026-09-07 bounded primary searches for EWT, La-Kabkab and bilateral preference degree results; 2025 connectivity theorem credited. No current-open or novelty certification.). Admission: admitted; result_status: unsolved.

**Our work.** Method: Exact conditioning, spectral integral estimate, deterministic graph comparison or order-statistic asymptotics. Result: An exact classical branching diagnostic shows why the critical normalization matters. For geometric offspring with pgf f(s)=1/(2-s), iteration gives f_l(s)=(l-(l-1)*s)/(l+1-l*s). Thus survival has probability 1/(l+1), and the conditional positive population is geometric with success 1/(l+1). Its mass on {1,...,M} tends to zero for each fixed M, while Z_l/l conditioned on survival converges to Exp(1). This is a single-type diagnostic, not the EWT. For EWT a possible route uses the positive right eigenfunction to form a size-biased spine, but convergence under survival conditioning requires a separate comparison to that bias. Obstruction: No EWT Yaglom or Q-process theorem is proved. A size-biased spine law is not automatically the law conditioned on nonextinction. Verification: author_checked_partial. No proof file recorded.

