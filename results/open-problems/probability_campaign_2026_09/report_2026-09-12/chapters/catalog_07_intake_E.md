## Catalog chapter 7: Claude intake E (probability_1000_intake_E_20260908), E0001-E0113

This chapter covers the whole of the fourth disjoint Claude intake ledger in the probability-1000 campaign (problems.jsonl, attempts.jsonl, sources.jsonl, README.md, CORRECTIONS.md, STATUS.json in ~/<private-repo>/06_math_research/probability_1000_intake_E_20260908), mined from 48 validated sources on 2026-09-08 with corrections added the same evening and on 2026-09-09 and 2026-09-11. problems.jsonl carries 115 physical rows over 113 distinct ids, E0001 through E0113; two ids (E0077 and E0078) were each recorded twice, the ledger's own CORRECTIONS.md and later status_note fields supplying a corrected second row, and the later row is what is reported below in each case, per the ledger's own convention that current state is the latest row per problem_id. Of the 113 problems, 109 are admitted and 4 are literature exclusions (E0028, E0043, E0049 excluded at intake time on the source's or a cited paper's own words; E0077 excluded by a same-evening correction once Qi-Ming He's 2021 theorem was found). Result_status over all 113 latest rows: answered_yes_by_known_example: 1, attempted_unsolved: 95, candidate_partial_counterexample: 1, not_attempted_resolved: 3, partial_result: 6, proved: 2, refuted: 1, resolved_in_literature: 1, resolved_in_literature_2026: 1, settled_homogeneous_case: 1, settled_inertial_balls: 1. Verification levels: exact_rational_counterexample_root_checked_2026_09_08: 1, primary_published_theorem_scope_checked_2026_09_08: 1, unreviewed: 111; the two non-default labels sit on the corrected E0077 (resolved against a published theorem) and E0078 (an exact rational counterexample, root-checked) rows. Two problems (E0064, E0078) carry a written proof file or memo path recorded in an attempt row; a further four (E0046, E0061, E0077, E0052-as-corrected) have memo write-ups referenced in status_note or CORRECTIONS.md text without a structured proof-file field. Six additional rows in the STATUS.json snapshot are flagged candidate_partial_result (E0008, E0024, E0026, E0027, E0058, E0066), all author-checked extensions of a cited survey's own proposition rather than solutions of the source's stated open problem. Per the ledger's own STATUS.json and README.md, zero of the 110 substantive attempts are author-checked or independently-reviewed original solutions to a problem that was open in the literature and remains open after this work; the entries proved or refuted here (E0046 complex half, E0061, E0077 rederivation, E0078) were each subsequently found to postdate or duplicate a published result, and this is stated in each entry below rather than left as a claim of novelty. Every verification word below is copied verbatim from the record. CORRECTIONS.md content that changes a row's status beyond what problems.jsonl itself records is reported in the affected entries (E0052, E0064) with the correcting record named.

### E0001. Exact critical probabilities for a wide class of graphs

Source: Kesten: Some highlights of percolation (ICM 2002) (kesten_percolation_highlights_2002), Open problem 1, PDF p. 5.

Statement: Find p_c(G) for a wide class of graphs G. Kesten notes at once that a solution 'would not have any explanatory value': the critical probabilities determined so far depend heavily on special symmetry properties of the underlying graph, and their values vary from graph to graph.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 for exact critical probabilities for classes of transitive graphs, plus the arXiv listings of Duminil-Copin and collaborators mined for this intake. Nothing found that computes p_c for a class wider than the self-dual planar lattices and the tree/nonamenable examples already known in 2002; recent activity (Duminil-Copin and Panis 2024-2025, and the high-dimensional survey...

Our work: Method: Ask what a nonvacuous version of the question could say, by cataloguing the only two mechanisms that have ever produced an exact p_c: (i) a self-duality that forces the critical point to... Result: Mechanism (i) is not a property of the graph alone but of a pair (graph, dual): it delivers p_c only when the duality map has a unique fixed point in (0,1) AND the crossing probabilities at that point are bounded away from 0 and 1. That is why... Obstruction: No invariant of a transitive graph is known that predicts whether p_c is algebraic. Verification: unreviewed.

### E0002. Existence of the surface-order limit for the supercritical cluster-size distribution

Source: Kesten: Some highlights of percolation (ICM 2002) (kesten_percolation_highlights_2002), Open problem 2, PDF p. 6.

Statement: For site percolation on Z^d with p > p_c it is known that there are constants 0 < C_4(p), C_5(p) < infinity with C_4(p) <= -n^{-(d-1)/d} log P_p{|C(v)| = n} <= C_5(p) for all large n. Does lim_{n to infinity} n^{-(d-1)/d} log P_p{|C(v)| = n} exist?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the surface-order large deviations for supercritical percolation cluster size. Returned the Wulff-construction literature: Alexander-Chayes-Chayes (d = 2), Cerf, 'Large deviations for three dimensional supercritical percolation' (Asterisque 267, 2000), Cerf-Pisztora (2000, 2001), Bodineau (1999).

Our work: Method: Split the question into the half the Wulff theory delivers and the half it does not. Result: The upper half is immediate: {|C(v)| = n} is contained in {|C(v)| >= n}, so limsup n^{-(d-1)/d} log P_p{|C(v)| = n} <= -W_p, given only the monotone LDP. The matching lower bound is a volume-adjustment statement: it would suffice to modify a near-Wulff cluster of volume in [n... Obstruction: Trimming a supercritical cluster is not local: closing boundary sites to shed volume can disconnect the droplet, or merge the finite cluster with the infinite one and destroy... Verification: unreviewed.

### E0003. Left continuity of the percolation function between p_c and p_u

Source: Kesten: Some highlights of percolation (ICM 2002) (kesten_percolation_highlights_2002), Open problem 3, PDF p. 8.

Statement: For a transitive graph G, is p -> theta_v(p) = P_p(|C(v)| = infinity) left continuous on [p_c, p_u]? Kesten notes that on Z^d, where p_c = p_u, this is equivalent to theta(p_c) = 0, known in 2002 for d = 2 and for d >= 19.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on continuity of theta at criticality for transitive graphs and on the non-uniqueness interval. Fitzner-van der Hofstad (2017) lowered the high-dimensional threshold from d >= 19 to d >= 11, and Hutchcroft has proved theta(p_c) = 0 for large classes of nonamenable transitive graphs and of transitive graphs of exponential growth.

Our work: Method: Separate the two statements the question conflates: continuity in the interior of the interval, and the boundary value at p_c. Result: Right continuity is free everywhere and needs no hypothesis: theta(p) = inf_n P_p(v <-> boundary of B_n) is a decreasing limit of polynomials in p, hence upper semicontinuous, and theta is nondecreasing, so theta is right continuous on [0,1]. Left continuity on any interval where the infinite cluster... Obstruction: A jump of theta at some p in (p_c, p_u) would mean a positive density of vertices joins the infinite clusters at a single parameter. Verification: unreviewed.

### E0004. Power laws, universality and scaling relations for percolation

Source: Kesten: Some highlights of percolation (ICM 2002) (kesten_percolation_highlights_2002), Open problem 4, PDF p. 11.

Statement: Prove that the percolation critical exponents (beta, gamma, nu, delta, eta, defined through theta(p), chi(p), the correlation length and P_{p_c}{|C| >= n}) exist as genuine power laws; prove universality, that they depend only on the dimension and not on the lattice; and prove the scaling relations among them. Known in 2002 for site percolation on the triangular lattice and for d >= 19 by the lace expansion, with no progress in d = 3, 4, 5.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 for percolation critical exponents in intermediate dimensions 2024-2025. The recent results are on two-point functions: Duminil-Copin and Panis 2024/2025 for the Ising and phi^4 models (sharp for d >= 5, almost sharp with a logarithmic correction at d = 4), and a 2025 revisit of one-arm exponents in high dimensions, plus a spread-out...

Our work: Method: Ask which of the three demands is logically weakest, since the source poses them as one problem; order them existence, scaling relations, universality, and test whether that order is right. Result: The order is wrong in one place, and that is the useful observation: scaling relations are NOT downstream of existence. Several are proved as two-sided inequalities between limsup and liminf exponents by differential-inequality arguments (Aizenman-Barsky, Aizenman-Newman) that never assume a limit exists. Obstruction: Existence of an exponent asserts that a log-log slope has a genuine limit, and percolation offers no subadditivity in p to force one. Verification: unreviewed.

### E0005. Any power bound at all for percolation quantities in dimensions three, four and five

Source: Kesten: Some highlights of percolation (ICM 2002) (kesten_percolation_highlights_2002), Open problem 5, PDF p. 11.

Statement: For Bernoulli percolation on Z^d with 3 <= d <= 5, find upper and lower power bounds for theta(p), chi(p), xi(p) and P_{p_c}{|C| >= n}. Kesten notes that bounds on one side are known for most of these but that no bound of the form theta(p) <= C |p - p_c|^{C'} has been proved for 3 <= d <= 5, not even for p < p_c, and calls this 'probably the most fundamental bound to prove'.

Status: historical status source_says_open. Status search: Same search as E0004. The 2024-2025 Duminil-Copin and Panis lower bounds on two-point functions concern the Ising and phi^4 models and are sharp only for d >= 5 (almost sharp at d = 4); their percolation results are for spread-out models above six dimensions.

Our work: Method: Test how much of the missing bound is already forced by the inequalities the source itself quotes, in particular Kesten's chi(p) >= C |log(p_c - p)|^{-(d-1)/d} (p_c - p)^{-1/d} for p <... Result: That chain gives a power lower bound on chi with a poor exponent and gives nothing at all on theta, because the passage from chi to theta needs the other direction. The point that must be stated carefully: Aizenman-Barsky's inequality theta(p) >= c(p - p_c) is a LOWER... Obstruction: Every known proof of an upper bound on theta near criticality goes through the one-arm probability at p_c, via theta(p) <= P_{p_c}(0 <-> partial B_{L(p)}) with L(p) the... Verification: unreviewed.

### E0006. The closed-path functional N(v) in critical percolation in three and more dimensions

Source: Kesten: Some highlights of percolation (ICM 2002) (kesten_percolation_highlights_2002), Open problem 6, PDF p. 12.

Statement: Let N(v) := inf{number of closed vertices in any path from 0 to v} in critical percolation. On Z^2 it is known that [sigma_{p_c}(N(v))]^{-1}[N(v) - E_{p_c} N(v)] satisfies a central limit theorem, with E_{p_c} N(v) of order log|v| and standard deviation of order (log|v|)^{1/2}. On Z^d with d >= 3 it is only known that N(v) = O(|v|^{eps}) a.s. for every eps > 0. Improve the bound for N(v) and find a limit theorem for N(v) in dimension >= 3.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 for the minimal number of closed edges on a path in critical percolation in higher dimensions. The two-dimensional central limit theorem (Kesten-Zhang) remains the standing reference; no d >= 3 result of either kind surfaced.

Our work: Method: Ask what the two-dimensional proof actually uses and which ingredient survives in d >= 3. Result: Both the mean of order log|v| and the standard deviation of order (log|v|)^{1/2} come from the same structure - one asymptotically independent O(1) contribution per scale. Consequently the shape of the answer in d >= 3 is decided by a single question: is the per-scale cost still tight?... Obstruction: Cross-scale decoupling in d = 2 is RSW. Verification: unreviewed.

### E0007. Competitive exclusion in the two-type contact process with unequal death rates

Source: Durrett: Coexistence in stochastic spatial models (Wald lectures) (durrett_coexistence_2009), Problem 1, PDF p. 3.

Statement: In the two-species competition model (a multitype contact process with birth rates beta_i and death rates delta_i), show that species 1 outcompetes species 2 when the two dispersal distributions are the same and beta_1/delta_1 > beta_2/delta_2. Durrett notes that this is what the Competitive Exclusion Principle predicts and that simulation supports it.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on competitive exclusion for the multitype contact process. Neuhauser's 1992 ergodic theorems for the multitype contact process remain the standing result and cover equal death rates; Cox-Durrett-Perkins (Asterisque 340, 2011) and Durrett's 'Spatial evolutionary games with small selection coefficients' (EJP 2014) cover perturbations of the VOTER model, i.e. a small-selection regime, which is...

Our work: Method: Locate the exact place where the equal-death-rate proof breaks. Result: With delta_1 different from delta_2 that duality is destroyed, and not for a technical reason: a type-i particle dies at rate delta_i, so the ancestral lineage of a site would have to know its own type in order to run its death clock. The dual is therefore a... Obstruction: The two-type system with unequal death rates is not attractive in the coordinatewise order that makes type 1 grow at the expense of type 2 (increasing type 1... Verification: unreviewed.

### E0008. A general coexistence theorem for long-range interactions to replace fast stirring

Source: Durrett: Coexistence in stochastic spatial models (Wald lectures) (durrett_coexistence_2009), Problem 2, PDF p. 7.

Statement: Durrett's Theorem 5 gives coexistence in a stochastic spatial model with fast stirring at rate eps^{-2} whenever there is a function phi that (i) decreases along solutions of the mean-field ODE, (ii) is convex, and (iii) tends to infinity as min_i u_i tends to 0. Formulate and prove a similar general result for systems with LONG-RANGE interactions, where at present the coexistence proofs are done case by case.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 for a general long-range analogue of the fast-stirring coexistence theorem. Found the case-by-case long-range results the source cites (Durrett-Neuhauser 1997, Durrett-Lanchier 2008) and the later voter-perturbation programme of Cox-Durrett-Perkins, which is a different limit (weak selection around the voter model, not long range with a fixed nonlinearity).

Our work: Method: Carry the proof of Theorem 5 through with the diffusive limit replaced by the nonlocal limit. Result: The Lyapunov step survives, and the hypothesis that survives it is exactly the one the source already assumes. Set h = phi(u) with phi convex. Obstruction: The spreading step is where long range and fast stirring genuinely differ. Verification: unreviewed.

### E0009. Absence of coexistence in the host-pathogen model when the pathogen is a mutualist

Source: Durrett: Coexistence in stochastic spatial models (Wald lectures) (durrett_coexistence_2009), Problem 3, PDF p. 9.

Statement: In the three-state host-pathogen model of Durrett and Lanchier, show that coexistence is not possible when lambda_2 < lambda_3 < lambda_1. Durrett explains that in this regime the pathogen is a mutualist (it decreases the rate at which the species is replaced), that starting from 1s and 2s in equilibrium with a small density of 3s the fraction of 2s shrinks and the 3s gain an even bigger advantage, and that in this case there is no interior fixed point.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 for host-pathogen multitype contact process coexistence results after 2009, including the Lanchier-Neuhauser line of work. Found later host-pathogen and multitype papers but none proving the stated non-coexistence for lambda_2 < lambda_3 < lambda_1.

Our work: Method: Ask what kind of statement 'no coexistence' is, and which of the two standard machines can produce it. Result: The absence of an interior fixed point in the mean-field ODE, which the source records, is not by itself an obstruction to spatial coexistence, and it is important not to read it as one: spatial models routinely coexist where the ODE does not (the catalyst example in the... Obstruction: The comparison requires a monotone coupling of a three-type system, and three-type contact processes are not attractive in any order that keeps both comparisons simultaneously: making the 3s... Verification: unreviewed.

### E0010. Uniqueness of the nontrivial stationary distribution for the sexual reproduction model with fast stirring

Source: Durrett: Coexistence in stochastic spatial models (Wald lectures) (durrett_coexistence_2009), Problem 4, PDF p. 11.

Statement: Consider the sexual reproduction model with lambda > 4.5. Show that when the stirring rate eps^{-2} is large there is a unique nontrivial stationary distribution. Durrett notes that existence results for stationary distributions are common but convergence results such as the grass-bushes-trees theorem are rare, and that one should start with a concrete case.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on complete convergence theorems for non-attractive spatial models with fast stirring, and on the sexual reproduction (Durrett-Neuhauser) model. Found the existence results and the fast-stirring critical value lambda_c -> 4.5 (Durrett-Neuhauser 1994) but no uniqueness or complete convergence theorem for lambda > 4.5.

Our work: Method: Ask what a uniqueness proof would have to supply beyond what the block construction already gives, by pushing the block construction as far as it goes. Result: The block construction gives a two-sided density bound: any stationary distribution nu that is not the all-empty state dominates the upper invariant measure of a supercritical oriented percolation, so nu-a.s. the density is at least some rho_- > 0, and by the same comparison run downwards the density... Obstruction: Uniqueness for interacting particle systems is proved either by attractiveness plus a complete convergence theorem, or by duality. Verification: unreviewed.

### E0011. An explicit coexistence window for the catalyst model without stirring

Source: Durrett: Coexistence in stochastic spatial models (Wald lectures) (durrett_coexistence_2009), Problem 5, PDF p. 12.

Statement: In the catalyst model (states 0 = vacant, 1 = CO, 2 = O; 0 -> 1 at rate p, a pair of neighbouring 0s -> 22 at rate q/4, adjacent 12 -> 00 at rate r/4), find 0 < p_1 < p_2 < 1 so that coexistence occurs for p in (p_1, p_2). Durrett notes that Bramson and Neuhauser proved coexistence when the O_2s are replaced by an N x N polymer with N large, and that Durrett and Swindle proved coexistence in the original model by introducing fast stirring; simulations suggest the O density drops to 0 discontinuously at the upper critical value.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the catalyst / CO oxidation (ZGB-type) lattice model and rigorous coexistence without stirring. The Durrett-Swindle fast-stirring result and the Bramson-Neuhauser large-polymer result remain the rigorous statements; nothing found that removes the small parameter.

Our work: Method: Ask what the small parameter is doing in each of the two existing proofs and whether either can be made quantitative at a fixed lattice. Result: Both existing proofs buy the same thing: they make the local dynamics close to a deterministic system whose interior fixed point is attracting, so that a single block can be shown to seed its neighbours. Fast stirring does it by a hydrodynamic limit, the N x N polymer... Obstruction: The block construction needs 'one occupied block makes two', which for a three-state non-attractive system means controlling a two-dimensional density vector, so the finite-box estimate is over a... Verification: unreviewed.

### E0012. Absence of coexistence in the two-type colicin model with equal death rates

Source: Durrett: Coexistence in stochastic spatial models (Wald lectures) (durrett_coexistence_2009), Problem 6, PDF p. 14.

Statement: In the colicin model of Durrett and Levin (type 1 produces colicin, which raises the death rate of type 2 by an amount proportional to the local density of 1s), show that coexistence is not possible when lambda_1 < lambda_2 and delta_1 = delta_2 = 1. Durrett notes that in the parameter range where the mean-field ODE has an interior fixed point that fixed point is unstable, and that simulations show segregation with the interface moving in favour of the 1s.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the colicin / allelopathy spatial competition model and rigorous non-coexistence results. Found the Durrett-Levin (1997) analysis and the later interface literature but no proof of non-coexistence under the stated hypotheses.

Our work: Method: Take the source's own simulation observation seriously and ask what statement it is evidence for: the two types segregate into large single-type regions and the interface moves. Result: Under segregation the long-time behaviour is decided by the sign of the interface velocity, which in the mean-field PDE is the sign of the integral of the reaction term across the connecting orbit - the same computation the source performs for the sexual reproduction model, where c has... Obstruction: The reduction to an interface velocity is rigorous only under fast stirring, where the particle system converges to the PDE. Verification: unreviewed.

### E0013. Coexistence in the cyclic case of Silvertown's five-species competition model

Source: Durrett: Coexistence in stochastic spatial models (Wald lectures) (durrett_coexistence_2009), Problem 7, PDF p. 15.

Statement: Show that coexistence always occurs in the cyclic case of Silvertown's model - the multitype biased voter model on five species with the empirically measured invasion matrix alpha_ij given in the survey, in which i replaces j at rate alpha_ij. Durrett adds: 'For partial credit show that coexistence can occur for some parameters', and remarks that a proof by simulation is given in his Figure 9.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on cyclic multitype biased voter models and rigorous coexistence for more than three species. The three-species rock-paper-scissors and cyclic particle system results (Durrett-Griffeath and successors) are the standing rigorous statements; no five-species result with a general invasion matrix was found.

Our work: Method: Ask what the word 'cyclic' has to mean here for the known three-species proofs to have any chance of transferring, since Silvertown's matrix is a general nonnegative matrix rather than a cyclic... Result: The three-species proofs use an exact structure that the five-species matrix does not have: for the strictly cyclic system the mean-field replicator dynamics has the conserved quantity prod_i u_i^{c_i} for suitable positive c_i, which is what keeps the interior orbits from spiralling out, and the spatial proof then... Obstruction: Multitype systems with q > 3 types have no monotone structure and no duality (the biased voter model with unequal rates is not the voter model, so the... Verification: unreviewed.

### E0014. Coexistence in the three-species colicin model

Source: Durrett: Coexistence in stochastic spatial models (Wald lectures) (durrett_coexistence_2009), Problem 8, PDF p. 17.

Statement: Show that coexistence can occur in the three-species colicin model, whose mean-field ODE and simulation are given in the survey's Figures 10 and 11.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on three-strain colicin / rock-paper-scissors bacterial competition and rigorous coexistence. The rigorous literature covers the three-species cyclic particle systems and the Kerr-Riley-Feldman-Bohannan style models at the simulation level; no proof for the survey's three-species colicin model was found.

Our work: Method: Identify which of the two available coexistence machines applies: the fast-stirring Lyapunov theorem (Theorem 5 of the survey) or the cyclic-structure argument. Result: The three-species colicin system is a genuine rock-paper-scissors: the colicin producer beats the sensitive strain, the sensitive strain outgrows the resistant one, and the resistant strain outgrows the producer, because producing colicin is costly. That is the structure under which the cyclic machinery could apply, and it is... Obstruction: Whether the required inequality holds for the actual colicin rates is not settled by the survey, and 'coexistence with fast stirring' is weaker than the question, which is... Verification: unreviewed.

### E0015. Coexistence in the spatial Prisoner's Dilemma

Source: Durrett: Coexistence in stochastic spatial models (Wald lectures) (durrett_coexistence_2009), Problem 9, PDF p. 19.

Statement: Show that coexistence can occur in the spatial Prisoner's Dilemma, i.e. in the Hawks-Doves spatial birth-and-death system with game matrix a = -0.6, b = 0.9, c = -0.9, d = 0.7, whose homogeneously-mixing ODE has the Hawk-to-Dove ratio increasing until the population crashes to 0. Durrett reports that simulations suggest Hawks and Doves coexist in the spatial model, because the ODE dynamics happen locally and Doves left behind recolonise space after a local Hawk crash.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on rigorous coexistence in spatial evolutionary games. Cox-Durrett-Perkins, 'Voter model perturbations and reaction diffusion equations' (Asterisque 340, 2011) and Durrett, 'Spatial evolutionary games with small selection coefficients' (EJP 2014, arXiv:1406.5876) determine phase diagrams for spatial games INCLUDING Prisoner's Dilemma cases, but under the hypothesis that the selection coefficient is small (the dynamics is...

Our work: Method: Ask what the spatial model has that the ODE does not, in a form that could be turned into a proof, and check the mechanism the source proposes: local crashes followed by... Result: The proposed mechanism is a rescue effect and it has a precise signature: the survival of Doves is a statement about the SURVIVAL OF A SUPERCRITICAL GROWTH PROCESS IN THE DEBRIS OF A CRASH, not about a stationary density. That distinguishes this problem from all the others in... Obstruction: The selection here is not small: the payoff entries are order one, so the process is not a voter-model perturbation and the Cox-Durrett-Perkins rescaling does not apply. Verification: unreviewed.

### E0016. A spectral proof of ergodicity for the non-reversible TCP window-size process

Source: Some simple but challenging Markov processes (simple_challenging_markov_2014), Open question 1 (Spectral proof of ergodicity), PDF p. 5.

Statement: For the piecewise-deterministic Markov process X modelling the TCP window size (linear growth at unit rate, multiplicative jumps by a factor 1/2 at a state-dependent rate), the generator L has an explicit polynomial eigenbasis and the invariant law's moments satisfy m_n(t)' = n m_{n-1}(t) + (2^{-n} - 1) m_n(t); the polynomials are dense in L^2(mu) but the eigenvectors of L are not orthogonal there (for instance the integral of P_1 P_2 against mu is -64/27). Despite the lack of reversibility, is it possible to use the spectral properties of L to get estimates on the long-time behaviour of X?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 for spectral methods and convergence rates for the TCP window-size PDMP and for non-reversible PDMPs generally. The hypocoercivity line (Villani; Dolbeault-Mouhot-Schmeiser) and the Wasserstein/coupling results for this process are what the literature offers; no spectral proof of the ergodicity rate for this specific non-self-adjoint generator was found.

Our work: Method: Ask what 'spectral estimate' can mean for a generator whose eigenvectors are complete but not orthogonal, and test the natural substitute: a Riesz-basis or a similarity-transform bound. Result: The obstruction is quantitative and can be located exactly. If the polynomial eigenfunctions {P_n} formed a Riesz basis of L^2(mu), the semigroup would satisfy ||P_t f - mu(f)|| <= kappa exp(-lambda_1 t) ||f - mu(f)|| with kappa the Riesz constant, which is the condition number of the change... Obstruction: The eigenvalues are lambda_n = 1 - 2^{-n}, which accumulate at 1; the spectral gap is therefore fine, but the eigenvalue spacing shrinks geometrically, which is exactly the... Verification: unreviewed.

### E0017. Shape of the instability domain for a two-matrix switched linear system

Source: Some simple but challenging Markov processes (simple_challenging_markov_2014), Open question 2 (Shape of the instability domain) and Conjecture 4.3, PDF p. 10.

Statement: For the switched linear system dX/dt = A_{I_t} X with I_t a two-state Markov jump process of rate r and A_0, A_1 two fixed 2x2 matrices, let G(r) be the associated top Lyapunov-type functional. Prove Conjecture 4.3: there exists r_c approximately 4.6 such that G'(r) > 0 for r < r_c and G'(r) < 0 for r > r_c, with G(r_c) approximately 0.2, and G(r) -> 0 both as r -> 0 and as r -> infinity. This would imply that the instability set U_alpha = {r > 0 : G(r) > alpha} is empty for alpha > G(r_c) and a nonempty interval for alpha < G(r_c).

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on Lyapunov exponents of two-dimensional Markov-switched linear systems and the shape of the instability domain in the jump rate. Found the general theory (Bene-Chevallier and successors on PDMP Lyapunov exponents) but no proof of unimodality in r for this example. 2026-09-08: Conjecture 4.3 constants corrected (peak r_c=0.230, G=0.1986; G(4.6)=0.027); unimodality unproved. Attempt E0017-A002.

Our work: Method: Computed G(r) for the survey's pair (9) from Theorem 4.1's generator by finite volume (N up to 6000), checked against the closed form and against Monte Carlo. Result: The constants in Conjecture 4.3 are off in r: G is unimodal on the grid tested, with its maximum at r_c = 0.230 and G(r_c) = 0.1986, and G(4.6) = 0.0269; G is strictly decreasing on [0.5, 60]. The peak VALUE 0.2 in the conjecture is right; the... Obstruction: Proof of unimodality: the stationary density is explicit (Theorem 4.1) but G'(r) involves the r-derivative of an exp(cot)-type integral; a sign argument is not in sight. (2 recorded attempts, E0017-A001-E0017-A002; latest reported.) Verification: unreviewed.

### E0018. Can the instability set in the jump rate be a union of several intervals?

Source: Some simple but challenging Markov processes (simple_challenging_markov_2014), Open question 3 (Oscillations of the Lyapunov exponent), PDF p. 10.

Statement: Is it possible to choose the two 2x2 matrices A_0 and A_1 in such a way that the set of jump rates r for which the associated switched linear process is unstable is the union of several intervals?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on non-monotone dependence of the top Lyapunov exponent on the switching rate. Found examples of non-monotonicity (a single interior maximum) but no example producing two or more disjoint instability intervals. 2026-09-08: extensive planar search finds no two-hump exponent; only endpoint dips. Attempt E0018-A002.

Our work: Method: Reduction plus computation. Result: NOT FOUND, with evidence that planar symmetric switching is unimodal: 1,500 random traceless pairs (dense, one-directional cyclic, skewed, two-scale; rates over six decades), about 40 hand-designed one- and two-parameter families around the survey pair (near-nilpotent elliptic/hyperbolic deformations, opposite rotation senses, unequal strengths, widely separated scales, two elliptic matrices... Obstruction: A negative search is not a theorem. (2 recorded attempts, E0018-A001-E0018-A002; latest reported.) Verification: unreviewed.

### E0019. Smoothness of the invariant density of piecewise deterministic Markov processes

Source: Some simple but challenging Markov processes (simple_challenging_markov_2014), Open question 4, PDF p. 13.

Statement: What can be said on the smoothness of the density of the invariant measure of such processes (the switched-flow piecewise deterministic Markov processes considered in the paper, including the switched linear systems of Section 4)?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on regularity of invariant densities of PDMPs and of switched linear systems (Bakhtin-Hurth, Bene-Chevallier-Nyquist and successors). Regularity results exist under Hormander-type bracket conditions on the vector fields; the source's examples include ones where the vector fields are collinear on a nontrivial set (the source computes exactly the set where A_0 x and A_1...

Our work: Method: Read the source's own computation as the answer's shape. Result: That determinant is the bracket condition made explicit, and it says where regularity can and cannot come for free: off the two lines {Q = 0} the pair (A_0 x, A_1 x) spans the plane, the switched flow satisfies a Hormander-type condition and the invariant density can be... Obstruction: On the degeneracy lines the invariant measure of a switched flow typically develops a power-law singularity whose exponent is a ratio of the jump rate to the local... Verification: unreviewed.

### E0020. Convergence to equilibrium for time-reversed PDMPs with unstable fields and unbounded jump rates

Source: Some simple but challenging Markov processes (simple_challenging_markov_2014), Open question 5, PDF p. 14.

Statement: Theorem 4.10 of the paper applies to the processes of Examples 4.6 and 4.7. The associated time-reversal processes are associated to unstable vector fields and unbounded jump rates. What can be said about their convergence to equilibrium?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on convergence to equilibrium for PDMPs with unbounded jump rates and expanding flows. The Meyn-Tweedie Lyapunov route and the Wasserstein contraction route both assume either a confining drift or bounded rates; results covering an expanding field with rate growing without bound were not found.

Our work: Method: Test the two standard machines against the two hypotheses that the question deliberately combines: an expanding vector field, and a jump rate that grows without bound. Result: They do not fail for the same reason, and separating them is the useful output. A Wasserstein contraction argument fails on the expanding field alone: the flow separates two coupled copies at rate given by the field's positive exponent, and jumps must beat that, which they can only... Obstruction: A Lyapunov drift condition gives exponential ergodicity only with a small-set/minorisation condition, and for a time-reversed PDMP the natural small set is a compact region that the reversed... Verification: unreviewed.

### E0021. Quantitative convergence for realistic three-dimensional models of bacterial movement

Source: Some simple but challenging Markov processes (simple_challenging_markov_2014), Open question 6 (More realistic models), PDF p. 16.

Statement: Is it possible to establish quantitative estimates for the convergence to equilibrium for more realistic run-and-tumble dynamics, especially in R^3, as considered in the kinetic and biological literature the paper cites?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on quantitative hypocoercivity for run-and-tumble / velocity-jump processes in three dimensions. There is a substantial post-2014 literature (Dolbeault-Mouhot-Schmeiser style hypocoercivity applied to kinetic transport with a tumbling operator, and Wasserstein/coupling results for the telegraph process) that gives quantitative rates in some three-dimensional settings; I did not verify which of the source's cited models...

Our work: Method: Ask what is genuinely three-dimensional about the difficulty, since the one-dimensional telegraph process has sharp rates by coupling. Result: The difficulty is not dimension per se but the geometry of the velocity space. In one dimension the velocity takes two values and a coupling can be built by making the two copies' velocities agree after a single common tumble; in R^3 the velocity lives on the sphere... Obstruction: Realistic chemotaxis models make the tumbling rate depend on the time derivative of the chemoattractant concentration along the trajectory, which adds an internal memory variable. Verification: unreviewed.

### E0022. Does Hunt's hypothesis for every proper-subspace projection imply it for the process?

Source: Hunt's hypothesis (H) for Markov processes: survey and beyond (hunts_hypothesis_survey_2019), Question 1, PDF p. 15.

Statement: Let X be an R^n-valued Levy process. If for every nonempty proper subspace A of R^n the projection process X_A of X on A satisfies Hunt's hypothesis (H) (every semipolar set is polar), does X itself satisfy (H)?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on Hunt's hypothesis and Getoor's conjecture after 2019, including the Hu-Sun line of work. Getoor's conjecture (essentially all Levy processes satisfy (H)) is described in this 2019 survey as a major unsolved problem and I found no announcement of its resolution; the projection questions of Section 3.2 do not appear to have been...

Our work: Method: Fix the direction that is free. Result: It cannot, at the level of the underlying capacity theory, and that is the relevant warning. Polarity for a Levy process is an energy condition against the kernel Re[(alpha + psi(z))^{-1}] (the source's own alpha-energy), and the projected process has exponent psi restricted to the subspace, so the... Obstruction: The dichotomy is controlled by how Im(psi) is dominated by 1 + Re(psi) (Kanda-Forst, Rao, and the survey's own C_log conditions). Verification: unreviewed.

### E0023. Does Hunt's hypothesis for every one-dimensional projection imply it for the process?

Source: Hunt's hypothesis (H) for Markov processes: survey and beyond (hunts_hypothesis_survey_2019), Question 2, PDF p. 15.

Statement: Let X be an R^n-valued Levy process. If for every one-dimensional subspace A of R^n the projection process X_A satisfies Hunt's hypothesis (H), does X satisfy (H)?

Status: historical status source_says_open. Status search: Same search as E0022. The survey's own Section 3.2.1 answers the WEAKER Question 3 (coordinate axes only) in the negative by an explicit counterexample; Question 2, which quantifies over ALL one-dimensional subspaces, is left open there and I found no later resolution.

Our work: Method: Take the source's counterexample to Question 3 and ask how far it can be pushed, since Question 2 differs from Question 3 only by enlarging the family of directions tested. Result: The counterexample is X_t = a t + sqrt(Q) B_t with Q = [[2,2],[2,2]] and a = (1,-1): each coordinate-axis projection has a nondegenerate Gaussian part and so satisfies (H), but the projection onto the line {y = -x} is a uniform motion, which fails (H), and hence... Obstruction: For a pure-jump process there is no matrix Q whose rank identifies the bad directions; the analogue is the set of directions in which the Levy measure's projection... Verification: unreviewed.

### E0024. Hunt's hypothesis for a product of two independent Levy processes

Source: Hunt's hypothesis (H) for Markov processes: survey and beyond (hunts_hypothesis_survey_2019), Question 4 (equivalently Question 4'), PDF pp. 15 and 18.

Statement: Let X_1 and X_2 be independent Levy processes on R^n and R^m respectively, both satisfying Hunt's hypothesis (H). Does the R^{n+m}-valued Levy process X = (X_1, X_2) satisfy (H)? Equivalently (Question 4): if S is a nonempty proper subspace of R^n and the projections X_S and X_{S-perp} are independent and both satisfy (H), does X satisfy (H)?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 as for E0022; no resolution found. The survey itself proves the special case Proposition 3.10 (if both X_1 and X_2 satisfy its solution condition (S) then the product satisfies (H)), via the additivity of the exponents and the Kanda-Forst condition.

Our work: Method: Push the survey's own Proposition 3.10 mechanism as far as it goes. Result: Kanda-Forst is stable, which is what Proposition 3.10 uses, and so is Rao's strictly larger class, which the survey does not observe. Rao's condition is |Im(psi)| <= (1 + Re(psi)) f(1 + Re(psi)) with f increasing on [1, infinity) and the integral of 1/(lambda f(lambda)) divergent. Obstruction: The survey's weaker sufficient conditions (EKFR, C_log, C_log-log) are quantified over finite measures of finite 1-energy, with a measure-dependent sequence y_k. Verification: unreviewed.

### E0025. Hunt's hypothesis for pure jump subordinators with infinite Levy measure

Source: Hunt's hypothesis (H) for Markov processes: survey and beyond (hunts_hypothesis_survey_2019), Question 5, PDF p. 25.

Statement: Does any pure jump subordinator with infinite Levy measure satisfy Hunt's hypothesis (H)? More generally, does any pure jump n-dimensional Levy process satisfy (H)? The survey records in Section 2 that it is still unknown whether any pure jump subordinator of type-(alpha, beta) satisfies (H), where a pure jump subordinator is of type-(alpha, beta) with 0 < alpha < beta < 1 if its Levy measure has a density nu with c^{-1} x^{-(1+alpha)} <= nu(x) <= c x^{-(1+beta)} for x in (0,1].

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on Hunt's hypothesis for subordinators after 2019. The survey's own Theorem 2.29 gives (H) for a subclass of type-(alpha,beta) subordinators under an extra condition; no later paper covering all pure jump subordinators with infinite Levy measure was found.

Our work: Method: Compute the shape of the exponent for a subordinator and see what the Kanda-Forst ratio looks like, since that ratio is the only quantity all the known sufficient conditions control. Result: For a driftless subordinator the exponent is psi(z) = integral over (0, infinity) of (1 - e^{i z x}) nu(dx), so Re psi(z) = integral (1 - cos(zx)) nu(dx) and Im psi(z) = -integral sin(zx) nu(dx). Both integrands are supported on the same scales, and for a stable-like... Obstruction: To exploit the oscillation one has to control Re psi from below along the sparse sequence where Im psi is large, and the two-sided bound c^{-1} x^{-(1+alpha)} <=... Verification: unreviewed.

### E0026. Hunt's hypothesis for one-dimensional Levy processes of infinite variation of jumps

Source: Hunt's hypothesis (H) for Markov processes: survey and beyond (hunts_hypothesis_survey_2019), Question 6, PDF p. 25.

Statement: Does any one-dimensional Levy process X with integral of (1 and |x|) against nu(dx) equal to infinity satisfy Hunt's hypothesis (H)? The survey notes (Remark 5.1(i), citing Kesten) that a positive answer to Question 7 would imply a positive answer to Question 6.

Status: historical status source_says_open. Status search: Same search as E0025. Kept open.

Our work: Method: Use the survey's own reduction (Question 7 implies Question 6, via Kesten's Theorem 1(f)) together with a stability observation for Rao's class. Result: Combining the two gives a concrete class in which Question 6 has a positive answer. By the argument recorded in E0024, Rao's sufficient condition |Im psi| <= (1 + Re psi) f(1 + Re psi) with f increasing and the integral of 1/(lambda f(lambda)) divergent is stable under... Obstruction: The reduction is only as good as Rao's condition, and the survey's own point is that (H) can hold outside it; conversely the infinite-variation hypothesis in Question 6... Verification: unreviewed.

### E0027. Is Hunt's hypothesis stable under independent sums of Levy processes?

Source: Hunt's hypothesis (H) for Markov processes: survey and beyond (hunts_hypothesis_survey_2019), Question 7, PDF p. 25.

Statement: Suppose X and Y are two independent n-dimensional Levy processes both satisfying Hunt's hypothesis (H). Does X + Y satisfy (H)?

Status: historical status source_says_open. Status search: Same search as E0025. The survey states this as an open question it has raised before, and records that a positive answer would imply a positive answer to Question 6 by Kesten's Theorem 1(f).

Our work: Method: Test each of the known sufficient conditions for (H) for stability under addition of the Levy-Khintchine exponents, since psi_{X+Y} = psi_X + psi_Y for independent summands. Result: Kanda-Forst is stable: if |Im psi_X| <= M(1 + Re psi_X) and |Im psi_Y| <= M(1 + Re psi_Y) then |Im psi| <= M(2 + Re psi_X + Re psi_Y) <= 2M(1 + Re psi). Rao's condition is also stable, with the same argument as in E0024: monotonicity... Obstruction: The survey's own weaker conditions (EKFR, C_log, C_log-log) are not of the pointwise form |Im psi| <= g(Re psi): they involve, for each finite measure of finite 1-energy... Verification: unreviewed.

### E0028. Hunt's hypothesis from coordinate-axis projections

Source: Hunt's hypothesis (H) for Markov processes: survey and beyond (hunts_hypothesis_survey_2019), Question 3, PDF p. 15.

Statement: If the one-dimensional projection process of an R^n-valued Levy process X on each coordinate axis satisfies Hunt's hypothesis (H), does X satisfy (H)?

Status: historical status source_says_open; current status resolved_in_literature; result_status not_attempted_resolved. Not admitted (literature exclusion).

Excluded: Answered NEGATIVELY inside the source itself. The survey's Section 3.2.1 is headed 'Counterexample for Question 3' and opens: 'We use a counterexample to show that the answer to Question 3 is negative.' The counterexample (PDF p. 16) takes Q = [[2,2],[2,2]], so that sqrt(Q) = [[1,1],[1,1]] and sqrt(Q) R^2 = {(x,y) : x = y}, and a = (1,-1)^T, and sets X_t = a t + sqrt(Q) B_t. Each coordinate-axis projection has a nondegenerate Gaussian part and so satisfies (H) by the survey's Theorem 2.5; the projection on {(x,y) : y = -x} is a uniform motion, which does not satisfy (H); hence X does not satisfy (H) by the survey's Lemma 3.1. Recorded here as an exclusion so that the check is on the record: the objects match by name (the question and the counterexample both concern the coordinate-axis...

### E0029. Lower bounds on fluctuations beyond the distribution classes P(d) and P+(d)

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (1), PDF p. 27.

Statement: Extend the results of the paper beyond the distribution classes P(d) and P+(d); in particular, prove the fluctuation lower bounds under minimal assumptions on the distribution of the underlying randomness.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on lower bounds for fluctuations of Euclidean combinatorial optimisation and first-passage percolation after 2017. Found the later Bates-Chatterjee and Damron-Hanson-Houdre-Xu work on two-dimensional first-passage percolation and moderate-deviation papers, but nothing that removes the distributional hypotheses of the source's method in general.

Our work: Method: Read off what the distribution classes are doing in the method. Result: The role of P(d) and P+(d) is to make a TILT of the underlying product measure both admissible and computable: for i.i.d. coordinates tilted by a parameter delta, the total variation cost of n coordinates is of order delta sqrt(n) and the induced shift of a Lipschitz functional... Obstruction: For discrete weights the only available perturbations are resamplings, which change the total variation by an amount bounded below by the atom sizes, so one cannot make the... Verification: unreviewed.

### E0030. Convergence of the variance of the stochastic travelling salesman tour length

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (2), PDF p. 27.

Statement: In the travelling salesman problem for n uniformly distributed points in [0,1]^2, prove that the variance of the length of the optimal tour converges to a constant as n tends to infinity, and identify this constant if possible. Chatterjee attributes the conjecture to Mike Steele.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the variance of the Euclidean TSP tour length and its convergence. The standing results are the Beardwood-Halton-Hammersley law of large numbers, the Rhee-Talagrand concentration bounds, and the source's own lower bound of order 1; no proof of convergence of the variance was found.

Our work: Method: Ask what structure would make a variance converge, and check whether the TSP functional has it. Result: The natural route is stabilisation: if the tour length admits a representation as a sum over points of a local add-one cost that depends only on a neighbourhood of radius O_P(1) after rescaling to intensity one, then the Penrose-Yukich central limit theorem gives both a CLT and convergence... Obstruction: The TSP is not known to stabilise. Verification: unreviewed.

### E0031. Tight fluctuation lower bound for Euclidean minimal matching

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (3), PDF p. 27.

Statement: Prove a tight lower bound for the fluctuations of the length of the minimal matching when the points are uniformly distributed in [0,1]^d.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on fluctuations of the Euclidean minimal matching. The optimal-transport literature (Ambrosio-Stra-Trevisan and successors) gives sharp asymptotics for the MEAN of the matching cost in d = 2 and its logarithmic correction; fluctuation lower bounds of matching order were not found.

Our work: Method: Use the dimension dependence to decide what 'tight' should mean, since the answer is not the same in all d. Result: In d >= 3 the matching cost is a sum of n contributions each of order n^{-1/d}, and the local structure is genuinely local (the optimal matching is stabilising in the sense that a point is matched within distance O(n^{-1/d}) with a stretched-exponential tail), which is why a... Obstruction: In d = 2 the field-level heuristic predicts fluctuations of order (log n)^{1/2} for the total cost, which is smaller than the mean by a factor n^{1/2}, so... Verification: unreviewed.

### E0032. Fluctuation lower bound for the longest common subsequence of random words with uniform letters

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (4), PDF p. 27.

Statement: Prove a tight lower bound for fluctuations in the longest common subsequence problem for random words. Chatterjee notes that considerable progress has been made but that the most important case of UNIFORMLY distributed letters is open, and that a solution would complete the proof of the central limit theorem for longest common subsequences, as shown by Houdre and Islak.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on variance lower bounds for the longest common subsequence of random words. The Houdre-Islak central limit theorem (conditional on a variance lower bound) and the Houdre-Ma results on central moments are the standing references, together with the non-uniform-letter results the source cites.

Our work: Method: Ask why uniformity is the hard case rather than the easy one, since it is the most symmetric. Result: Because the method needs an asymmetry to tilt. For non-uniform letter distributions one perturbs the letter frequencies: raising the probability of the most common letter increases the expected LCS at a computable rate, and the total variation cost of the tilt is controlled - exactly the calibration of... Obstruction: To recover a first-order effect at the symmetric point one must tilt in a direction that is not a frequency change - for instance, a correlation between the... Verification: unreviewed.

### E0033. Improving the fluctuation lower bound for two-dimensional first-passage percolation

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (5), PDF p. 27.

Statement: Improve the lower bound for the fluctuations of the first-passage time in two-dimensional first-passage percolation.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on first-passage percolation variance lower bounds. Newman-Piza and Zhang give a variance lower bound of order log n; the search returned that 'Bates-Chatterjee and Damron-Hanson-Houdre-Xu give a lower bound of sqrt(log N) for the fluctuations of the passage time in two dimensions', which is the fluctuation-order statement of the source's own method.

Our work: Method: Compare the achieved order with the calibration of Lemma 1.2 to see what an improvement would require. Result: The sqrt(log n) bound is exactly what a tilt supported on the whole box gives: the passage time to distance n depends on order n^2 edges, a uniform tilt of size delta costs delta n in total variation, so delta = 1/n, and the shift produced by such... Obstruction: Any geodesic-adapted perturbation is a function of the very randomness being perturbed, so the two laws in Lemma 1.2 are not related by a fixed change of measure. Verification: unreviewed.

### E0034. Fluctuation lower bounds in first-passage percolation with discrete edge weights

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (6), PDF p. 27.

Statement: Extend the lower bound result for first-passage percolation to the case of discrete edge weights.

Status: historical status source_says_open. Status search: Same search as E0033. The Newman-Piza log n variance lower bound covers {0,1}-valued weights; a fluctuation-order (concentration-function) lower bound for discrete weights by the source's method was not found.

Our work: Method: Identify the exact failure of the coupling for atoms, and look for a substitute perturbation that is available in the discrete case. Result: With continuous weights the perturbation is a small shift of each weight, whose total variation cost is proportional to the shift; with weights on a lattice the smallest available move is a resampling, whose cost is bounded below by a constant times the number of resampled edges divided... Obstruction: Recovering the sign needs a positive-probability event on which the resampling raises the passage time by a definite amount, which in turn needs a lower bound on the... Verification: unreviewed.

### E0035. Any nontrivial fluctuation lower bound for first-passage percolation in dimension at least three

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (7), PDF p. 27.

Statement: Prove any nontrivial lower bound for the fluctuations of the first-passage time in higher dimensions. Chatterjee notes that a lower bound of order 1 is easy using the method of the paper.

Status: historical status source_says_open. Status search: Same search as E0033. Recent work on 'properties of first-passage percolation above the hypothetical critical dimension' surfaced but was not read; it concerns the conjectured d >= d_c regime rather than a fluctuation lower bound in d = 3.

Our work: Method: Ask why the two-dimensional dyadic-scale argument does not simply repeat in d = 3. Result: The two-dimensional sqrt(log n) comes from summing an O(1) contribution over the log n dyadic scales, and each scale contributes because a box of side 2^k contains a bottleneck that the geodesic must cross and whose weight can be tilted. In d >= 3 the geodesic can go... Obstruction: To beat the dilution one needs to perturb a whole cutset rather than a path, and a cutset in d dimensions has L^{d-1} edges, so the total variation... Verification: unreviewed.

### E0036. Improving the lower bound on the Newman-Piza exponent in two dimensions

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (8), PDF p. 27.

Statement: Improve the lower bound for the Newman-Piza exponent chi' for two-dimensional first-passage percolation.

Status: historical status source_says_open. Status search: Same search as E0033. Newman-Piza show that the log n variance lower bound can be improved to a power of n in directions where the limit shape is not flat, and that under a finite radius of curvature assumption power-law lower bounds and an inequality between chi and xi follow.

Our work: Method: Separate the conditional from the unconditional statement, since Newman-Piza's power bound is conditional on curvature of the limit shape. Result: The whole difficulty is that the two available routes need opposite inputs. The curvature route gives chi' > 0 but assumes a strictly convex limit shape - a statement about the shape that nobody can prove for any nondegenerate weight distribution in d = 2. Obstruction: Even the weaker disjointness statement is unproven: the only unconditional information about the limit shape in d = 2 is that it is convex, compact, and has the... Verification: unreviewed.

### E0037. Positivity of the Newman-Piza exponent in higher dimensions

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (9), PDF p. 27.

Statement: Show that the Newman-Piza exponent chi' is strictly positive in higher dimensions.

Status: historical status source_says_open. Status search: Same search as E0033 and E0036. Kept open.

Our work: Method: Combine the dilution computation of E0035 with the curvature route of E0036 and see which one degrades faster in d. Result: They degrade in opposite ways, which is the point worth recording. The curvature route needs less as d grows in one respect - the limit shape in high d is expected to be closer to a ball, hence more plausibly strictly convex - but the geodesic-disjointness input needs... Obstruction: There is no dimension in which both the shape input and the disjointness input are available. Verification: unreviewed.

### E0038. Optimality of the fluctuation lower bound for the Sherrington-Kirkpatrick free energy and ground state

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (10), PDF p. 27.

Statement: Improve the lower bound on the order of fluctuations of the free energy of the Sherrington-Kirkpatrick model, or show that it is optimal. The same for the ground state energy.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 covered by the fetch of the 2025 survey 'Free energy fluctuations in SK and related spin glass models: a literature survey' (source sk_free_energy_survey_2025 in this intake), which records the state of the art: Gaussian fluctuations of order 1/N in the high-temperature phase (Aizenman-Lebowitz-Ruelle), Chen-Lam at the critical temperature, and the low-temperature regime open....

Our work: Method: Ask what the conjectured order is in each phase, since 'optimal' means different things above and below the critical temperature, and check which phase the coupling method can see. Result: Above criticality the free energy has Gaussian fluctuations of order 1/N (in the normalisation where the free energy is O(1) per spin), and the coupling method's tilt - perturbing the disorder matrix by an independent Gaussian of size delta - costs delta N in total variation and shifts... Obstruction: In the low-temperature phase the response of the free energy to a disorder perturbation is a Gibbs average over a non-concentrated overlap distribution, so the shift in Lemma... Verification: unreviewed.

### E0039. Optimality of the fluctuation lower bound in the random assignment problem

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (11), PDF p. 27.

Statement: Prove the optimality of the lower bound in the random assignment problem for cost distributions in P+(1) or any other general class of cost distributions.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on fluctuations of the random assignment problem after Aldous's zeta(2) limit and Wastlund's exact formulas. The mean is known exactly (Wastlund, Linusson-Wastlund, Nair-Prabhakar-Sharma), but the order of fluctuations is not; no optimality proof was found.

Our work: Method: Use the exactly solvable structure, which this problem has and the others on the list do not. Result: The exact formula fixes the mean but not the variance, and the reason is structural: Wastlund's recursion computes an EXPECTATION by an exchangeability argument that does not lift to second moments, because the increments it telescopes are not independent. The conjectured fluctuation order is n^{-1} (so that the... Obstruction: The telescoping increments are strongly negatively correlated (adding a row makes the next row's marginal gain smaller), so the variance of the sum is much smaller than the... Verification: unreviewed.

### E0040. Fluctuation lower bounds for linear eigenvalue statistics and extreme eigenvalues of patterned random matrices

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (12), PDF p. 28.

Statement: Prove tight lower bounds for fluctuations of functionals of random matrices other than the determinant, such as linear statistics of eigenvalues and the maximum and minimum eigenvalues, in ensembles where such results are not known. This includes patterned random matrix ensembles such as random Toeplitz and Hankel matrices and random band matrices.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on fluctuations of linear eigenvalue statistics for Toeplitz, Hankel and band matrices. Central limit theorems for linear statistics exist for Toeplitz and Hankel ensembles (Chatterjee, Liu-Sun-Wang and successors), which give fluctuation lower bounds where they apply; the extreme eigenvalues of these ensembles remain far less understood.

Our work: Method: Split the request into its two halves, because they have opposite difficulty profiles: linear statistics are smooth functionals of the whole spectrum, extreme eigenvalues are non-smooth functionals of its edge. Result: For linear statistics the coupling method is well calibrated: a Gaussian tilt of the n independent entries of a Toeplitz matrix (there are only order n of them, not n^2) costs delta sqrt(n) and shifts a linear statistic by order delta n times the derivative of the test... Obstruction: Patterned ensembles have order n independent entries but n^2 matrix entries, so the entries are heavily dependent and the total variation cost of a tilt is computed on... Verification: unreviewed.

### E0041. A distributional limit theorem in any of the examples of the paper

Source: Chatterjee: A general method for lower bounds on fluctuations of random variables (chatterjee_lower_bounds_2017), Open problems, item (13), PDF p. 28.

Statement: Prove a distributional limit theorem in any of the examples discussed in the paper: the stochastic travelling salesman problem, the stochastic minimal matching problem, the random assignment problem, the Sherrington-Kirkpatrick model, first-passage percolation, or random matrices.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 covering the same examples. Distributional limits exist in the high-temperature SK phase (Aizenman-Lebowitz-Ruelle) and for some patterned-matrix linear statistics, so this item is partly addressed for two of the six examples; for the Euclidean optimisation problems, the random assignment problem and first-passage percolation no distributional limit is known.

Our work: Method: Ask what a distributional limit needs beyond a matching pair of bounds, and identify which example is closest. Result: A limit law needs an approximate decomposition of the functional into asymptotically independent pieces. Of the six examples, the one with such a decomposition in sight is minimal matching in d >= 3, where the optimal matching is expected to stabilise and the Penrose-Yukich machinery would give a... Obstruction: For the stabilising candidates the missing ingredient is stabilisation itself (see E0030 and E0031). Verification: unreviewed.

### E0042. The Komlos conjecture on vector balancing

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 0.1 (Komlos Conjecture), PDF p. 6.

Statement: Given n, let K(n) be the infimum over all reals such that for every set of n vectors u_1,...,u_n in R^n with ||u_i||_2 <= 1 there exist signs eps_i in {-1,+1} with ||eps_1 u_1 + ... + eps_n u_n||_infinity <= K(n). Prove that there is a universal constant K with K(n) <= K for all n.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the Komlos conjecture and on matrix discrepancy. Banaszczyk's O(sqrt(log n)) bound remains the best unconditional result, with algorithmic versions (Bansal-Dadush-Garg-Lovett) matching it; a constant bound is not known.

Our work: Method: Test what the probabilistic (random signs) benchmark gives and how far it is from the conjecture, so that the gap being attacked is explicit. Result: Random signs give, for each coordinate j, a sum of independent terms with variance sum_i u_i(j)^2, and the constraint ||u_i||_2 <= 1 bounds the sum over j of that variance by n, not each coordinate individually. So the worst case for random signs is all the mass in... Obstruction: Banaszczyk's theorem produces a signing into any convex body of Gaussian measure at least 1/2 after scaling by 5; the cube of side sqrt(log n) is the smallest... Verification: unreviewed.

### E0043. The Recht-Re noncommutative arithmetic-geometric mean inequality

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 0.2(a), PDF p. 7.

Statement: For any collection of d x d positive semidefinite matrices A_1,...,A_n, is it true that the spectral norm of (1/n!) sum over permutations sigma of the product A_{sigma(1)} ... A_{sigma(n)} is at most the spectral norm of (1/n^n) sum over all n-tuples (k_1,...,k_n) of the product A_{k_1} ... A_{k_n}? The source attributes conjecture (a) to Recht and Re, and records that it had been proved for n = 3 by Zhang.

Status: historical status source_says_open; current status resolved_in_literature; result_status not_attempted_resolved. Not admitted (literature exclusion).

Excluded: Zehua Lai and Lek-Heng Lim, 'Recht-Re Noncommutative Arithmetic-Geometric Mean Conjecture is False', arXiv:2006.01510, ICML 2020. Comparing the objects BY NAME: the source calls conjecture (a) the Recht-Re inequality, citing [RR12] = Recht and Re, 'Toward a noncommutative arithmetic-geometric mean inequality', and states it for d x d positive semidefinite matrices with the spectral norm; Lai and Lim's abstract says 'A groundbreaking result of Recht and Re reduces the problem to a noncommutative analogue of the arithmetic-geometric mean inequality where n positive numbers are replaced by n positive definite matrices... The conjectured Recht-Re inequality has so far only been established for n = 2 and a special case of n = 3. We will show that the Recht-Re conjecture is false for general n... which we show are false as soon as n = 5.' Same named conjecture, same objects (n...

### E0044. The reverse noncommutative arithmetic-geometric mean inequality

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 0.2(b), PDF p. 7.

Statement: For any collection of d x d positive semidefinite matrices A_1,...,A_n, is the spectral norm of (1/n!) sum over permutations sigma of A_{sigma(1)} ... A_{sigma(n)} at least the spectral norm of (1/n^n) sum over all n-tuples of A_{k_1} ... A_{k_n}? The source attributes conjecture (b) to Duchi and records that it had been proved for n = 3.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 as for E0043. Lai and Lim's paper is titled and stated for the RECHT-RE conjecture, which the source identifies as direction (a) with citation [RR12]; direction (b) is attributed by the source to a different reference, [Duc12].

Our work: Method: Check whether the two directions can both be false, or whether one direction is forced, by testing the commuting case and a rank-one case. Result: When the A_i commute both sides are the same product of scalars in different orders and the two conjectures both hold with equality on the spectrum, so no commuting example distinguishes them - which is why the problem is genuinely noncommutative. For rank-one A_i = v_i v_i^T the... Obstruction: The rank-one reduction makes both sides computable but the normalisations differ, and the tiny-vector construction may violate the implicit assumption that the A_i are comparable. Verification: unreviewed.

### E0045. The optimal basis for the largest d-dimensional projection of a Gaussian vector

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 1.1 (A. Mallat and Zeitouni), PDF p. 14.

Statement: Let g be N(0, Sigma) in R^p with Sigma known, and let d < p. For an orthonormal basis V = [v_1,...,v_p] let Gamma_V be the squared l_2 norm of the largest projection of g onto a subspace spanned by d elements of V, i.e. the max over subsets S of size d of the sum over i in S of (v_i^T g)^2. Which basis V maximises E[Gamma_V]? Mallat and Zeitouni conjecture the optimal basis is the eigenbasis of Sigma; this is known for d = 1 and open for d > 1.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the Mallat-Zeitouni conjecture on the best basis for the largest projection of a Gaussian vector. Found the original 2011 preprint and citations describing the conjecture as open; no resolution found.

Our work: Method: Isolate why d = 1 is easy and what breaks at d = 2, by writing the objective as an expected maximum over subsets. Result: For d = 1 the objective is E max_i (v_i^T g)^2, a maximum of p correlated squared Gaussians with variances v_i^T Sigma v_i summing to trace(Sigma). Since a maximum of Gaussians is maximised by making the variances as UNEQUAL as possible under a fixed sum, and the eigenbasis... Obstruction: The eigenbasis makes the coordinates independent, which maximises the spread of the subset sums but minimises their positive correlation; for d >= 2 the expected maximum over subsets... Verification: unreviewed.

### E0046. Monotonicity in n of the expected average singular value of a Gaussian matrix

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 1.2 (Monotonicity of singular values), PDF p. 17.

Statement: Let X be an n x n matrix with i.i.d. N(0,1) entries and let sigma_R(n) be the expected value of the average singular value of n^{-1/2} X, with sigma_C(n) the complex-Gaussian analogue. It is conjectured that sigma_C(n+1) <= sigma_C(n) for all n >= 1 (and the corresponding monotonicity in the real case).

Status: historical status source_says_open. Current-literature status: resolved_2026. Status search: WebSearch 2026-09-08 on monotonicity in the dimension of the expected average singular value of Ginibre matrices. Found the Bandeira-Kennedy-Singer source of the conjecture and later work on moments of the Marchenko-Pastur law; no proof of the monotonicity for all n was found. 2026-09-08: BOTH halves settled in 2026 by O. Hutnik (real: arXiv:2608.12151, Aug 2026; complex: companion preprint 2026, on Abreu recurrence CAOT 20 (2026) 159); the intake search missed them. Independent rederivation of the complex half tonight (E0046-A002) via a partial-sum recurrence and ratio induction; Lean E0046.lean.

Our work: Method: Exact finite-n formula: alpha_C(n) = n^{-3/2} sum_{k<n} a_k with a_k = int sqrt(x) e^{-x} L_k(x)^2 dx (LUE Christoffel-Darboux density). Result: PROVED (complex half): alpha_C(n+1) < alpha_C(n) for every n >= 1. The real half (alpha_R increasing) is untouched; numerically it holds for n <= 40. Obstruction: Real case: the LOE one-point function has an extra boundary term and the half-integer moment does not reduce to a two-term recurrence the same way. (2 recorded attempts, E0046-A001-E0046-A002; latest reported.) Verification: unreviewed.

### E0047. Threshold for rank-constrained semidefinite relaxations of the spiked Wigner model

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 1.3 (Spike model for rank constrained SDP), PDF p. 23.

Statement: Let W be a Wigner matrix with i.i.d. N(0,1) entries, and for symmetric B define Q_r(B) = max{trace(BX) : X psd, X_ii = 1, rank(X) <= r}, and q_r(lambda) = lim_{n to infinity} (1/n) E Q_r((lambda/n) 11^T + n^{-1/2} W). What is the value of lambda_r^* = inf{lambda >= 0 : ...}, the threshold above which the rank-r constrained relaxation detects the spike?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on rank-constrained SDP thresholds for the spiked Wigner model and on the Z2 synchronisation SDP. The r = 1 (integer) and r = infinity (full SDP) cases are understood via the Sherrington-Kirkpatrick free energy and the Montanari-Sen analysis; the intermediate finite-r thresholds are governed by the vector spin glass free energy and I...

Our work: Method: Identify q_r(lambda) with a known free energy, since the maximisation over rank-r psd matrices with unit diagonal is a spin system on the sphere. Result: Writing X = sigma sigma^T with sigma_i in S^{r-1} (unit vectors in R^r), the constraint set is exactly the configuration space of the r-component vector spin model, and (1/n) Q_r is the ground-state energy of the r-vector Sherrington-Kirkpatrick model with an added ferromagnetic term of strength lambda. So... Obstruction: The vector-SK Parisi formula is a variational problem over monotone matrix paths rather than scalar paths, and its zero-temperature limit is not known in closed form for any... Verification: unreviewed.

### E0048. Improving the noncommutative Khintchine inequality to a square-root logarithm

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 4.1 and Conjecture 4.21, PDF p. 69.

Statement: Let A_1,...,A_n be symmetric d x d matrices and g_1,...,g_n i.i.d. N(0,1). Prove or disprove that E||sum_k g_k A_k|| <= sigma + C (log d)^{1/2} sigma_*, where sigma is the strong variance ||sum A_k^2||^{1/2} and sigma_* the weak variance. The source notes that the conjecture may be false but that no counterexample is known.

Status: historical status source_says_open. Status search: Checked the arXiv abstract of Bandeira, Boedihardjo and van Handel, 'Matrix Concentration Inequalities and Free Probability', arXiv:2108.06312 (Inventiones 2023), which develops nonasymptotic bounds capturing noncommutativity and 'intrinsic freeness'. Comparing objects by name: the conjecture asks for the prefactor (log d)^{1/2} on the weak variance sigma_*; the abstract claims bounds that are sharp where the noncommutative...

Our work: Method: Check the conjecture against the two extreme cases that any candidate bound must reproduce, to see whether the exponent 1/2 is even the right guess. Result: When the A_k commute and are diagonal, the norm is a maximum of d independent Gaussians with variances given by the rows, so E||X|| is of order sigma_* sqrt(log d) exactly, and sigma can be as small as sigma_*; the conjecture is TIGHT there, which is the source's... Obstruction: The two extremes are separated by the free-probability quantity that BBvH call intrinsic freeness, and the known interpolation loses a factor because the noncommutative moment method must control... Verification: unreviewed.

### E0049. The Latala-Riemer-Schutt comparison for Gaussian random matrices

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 4.2 (Latala-Riemer-Schutt), PDF p. 69.

Statement: Given X a symmetric random matrix with independent Gaussian entries, is E||X|| comparable to E max_k ||X e_k||_2? The source notes that Bandeira-van Handel answer this positively for a large range of variance profiles but not in full generality, and that van Handel had proved it in a special case.

Status: historical status source_says_open; current status resolved_in_literature; result_status not_attempted_resolved. Not admitted (literature exclusion).

Excluded: Rafal Latala, Ramon van Handel and Pierre Youssef, 'The dimension-free structure of nonhomogeneous random matrices', Inventiones mathematicae 214 (2018); arXiv:1711.00807. Comparing the objects BY NAME: the source's question names 'X a symmetric random matrix with independent gaussian entries' and asks whether E||X|| is comparable to E max_k ||X e_k||_2. The paper's abstract, read in full via the arXiv API, opens 'Let X be a symmetric random matrix with independent but non-identically distributed centered Gaussian entries. We show that E||X||_{S_p} is comparable (with universal constants) to E[(sum_i (sum_j X_ij^2)^{p/2})^{1/p}] for any 2 <= p <= infinity', and adds 'This settles, in the case p = infinity, a conjecture of the first author'. At p = infinity the left side is E||X|| (the spectral norm is the S_infinity norm) and the right side is E[max_i (sum_j X_ij^2)^{1/2}] = E max_i ||X e_i||_2...

### E0050. The matrix Spencer conjecture

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 4.3 and Conjecture 4.23 (Matrix Six-Deviations Suffice), PDF p. 70.

Statement: Is there a universal constant C such that for any n symmetric matrices H_1,...,H_n in R^{n x n} with ||H_k|| <= 1 there exist signs eps_1,...,eps_n in {-1,+1} with ||sum_k eps_k H_k|| <= C sqrt(n)? When the H_k are diagonal this is Spencer's six standard deviations theorem.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 'matrix Spencer conjecture six deviations status resolved 2024'. Bansal, Jiang and Meka, 'Resolving matrix Spencer conjecture up to poly-logarithmic rank' (STOC 2023, arXiv:2208.11286) prove it for matrices of rank at most n/log^3 n.

Our work: Method: Calibrate against the random signing and against the diagonal case, to see where the sqrt(n) must come from. Result: Random signs give, by the matrix Chernoff/Khintchine bound, ||sum eps_k H_k|| of order sigma sqrt(log n) with sigma = ||sum H_k^2||^{1/2} <= sqrt(n), i.e. sqrt(n log n) - so exactly as in the scalar Spencer theorem, the random signing is off by sqrt(log n) and the conjecture asks... Obstruction: Spencer's partial colouring lemma works in the cube with a body defined by n linear constraints; the matrix version needs a body defined by a spectral constraint, whose... Verification: unreviewed.

### E0051. Concentration of the spectral norm of random k-lifts of graphs

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 4.5 (Random k-lifts of graphs), PDF p. 78.

Statement: Give a tight upper bound for E||A_{pi^k} - E A_{pi^k}||, where A_{pi^k} is the adjacency matrix of a random k-lift of a graph on n vertices. The source records Oliveira's bound of essentially sqrt(log(nk)) and notes that results of Amit-Bhatia-Grimmett-type suggest more concentration for large k, and that k = 2 reduces to a matrix Bernstein estimate.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 'Bordenave Collins eigenvalues of random lifts strong asymptotic freeness'. Charles Bordenave and Benoit Collins, 'Eigenvalues of random lifts and polynomials of random permutation matrices', Annals of Mathematics 190 (2019) 811-875 (arXiv:1801.00876) show that the nontrivial eigenvalues of random n-lifts of a FIXED base graph approximately achieve the Alon-Boppana bound with high probability as...

Our work: Method: Write down what each of the two known regimes gives and where they must meet. Result: Oliveira's matrix-Bernstein bound gives sqrt(log(nk)) because the ambient dimension of the lift is nk; Bordenave-Collins give the dimension-free constant 2 sqrt(d-1) for fixed n and k tending to infinity. These two are compatible only if the logarithm in Oliveira's bound is an artefact of the dimension counting, and... Obstruction: The trace method that gives Bordenave-Collins their result counts non-backtracking walks in the lift and is asymptotic in k with the base graph fixed; making it uniform in... Verification: unreviewed.

### E0052. A sharp lower bound on the probability that a sum of nonnegative unit-mean variables exceeds its mean plus one

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 4.6 and Conjecture 4.33, PDF p. 78.

Statement: Let X_1,...,X_n be independent random variables with X_i >= 0 and E X_i = 1 for every i. Prove or disprove that P(sum_i X_i <= n + 1) >= 1 - 1/e. The source notes that the bound is attained in the limit by the i.i.d. example X_i = n+1 with probability 1/(n+1) and 0 otherwise, for which the probability is 1 - (n/(n+1))^n, decreasing to 1 - 1/e.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on Feige's inequality and the 1 - 1/e conjecture for nonnegative independent variables with unit mean. Feige's original result gives a constant of 1/13, improved to 0.1798 (He, Zhang and Zhang) and further by later work; the sharp constant 1 - 1/e remains conjectural as far as the search showed.

Our work: Method: Check the conjecture against the extremal example and against the trivial bound, since the campaign's own audit found a case where a 'result' turned out to be Markov's inequality in disguise. Result: Markov gives P(sum > n+1) <= n/(n+1), i.e. P(sum <= n+1) >= 1/(n+1), which tends to 0 and is vastly weaker than 1 - 1/e - so the conjecture is genuinely more than the trivial bound, unlike the case the D-ledger audit caught. The extremal example is the... Obstruction: The difficulty is that the X_i need share no scale: some may be bounded and others heavy-tailed with the same mean, so no single truncation works, and the... Verification: unreviewed.

Correction (CORRECTIONS.md, added after this row was recorded): the row's statement inverts Feige's conjecture. Bandeira's Conjecture 4.33 (due to Feige) asks P(sum X_i >= n+1) <= 1-1/e, an upper bound on the upper tail; this row instead asks P(sum X_i <= n+1) >= 1-1/e, a lower bound on the lower tail. The two events overlap only at the atom sum=n+1, so they are not complementary, and the extremal two-point law attains 2/e (about 0.7358) for the row's event, not 1-1/e, so the 'attained in the limit' and 'cannot be improved' claims below do not hold as written. The row's central point, that the conjecture is strictly stronger than Markov's bound, survives once aimed at the correct event.

### E0053. Sum of maximum and minimum bisection of a random regular graph

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 8.5 and Conjecture 8.5, PDF p. 117.

Statement: Let G be a uniformly random d-regular graph on n vertices. Prove or disprove that for every d, as n grows, (1/n)(MaxBis(G) + MinBis(G)) = d/2 + o(1), where MaxBis and MinBis are the maximum and minimum bisection sizes. The source notes that the conjecture is known to hold up to o(sqrt(d)) terms by Dembo-Montanari-Sen.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on maximum and minimum bisection of random regular graphs and the Zdeborova-Boettcher conjecture. Dembo, Montanari and Sen (arXiv:1503.03923) establish the extremal cut values up to o(sqrt(d)) via the Parisi formula, and later work (Sen; Jagannath-Sen) refines the constants; I found no proof for fixed small d.

Our work: Method: Test the conjecture against the two regimes it must reconcile: large d, where the Parisi machinery applies, and small d, where it does not. Result: For large d the interpolation gives MaxBis/n = d/4 + P_* sqrt(d)/2 + o(sqrt(d)) and MinBis/n = d/4 - P_* sqrt(d)/2 + o(sqrt(d)) with P_* the Parisi constant, so the SUM is d/2 + o(sqrt(d)) automatically - the conjecture at large d is the statement that the two... Obstruction: The exact cancellation would follow from a sign symmetry exchanging the max-cut and min-cut problems, and no such symmetry exists on a fixed graph - it holds only... Verification: unreviewed.

### E0054. Partial recovery threshold for the balanced stochastic block model with more than three communities

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 9.1, PDF p. 121.

Statement: For the balanced stochastic block model with k > 3 constant communities, inner connection probability a/n and outer probability b/n, what is the threshold at which it becomes possible to produce an estimate correlating with the true partition (the partial recovery, or detection, threshold)?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the detection threshold for the stochastic block model with more than three communities. Abbe and Sandon showed that for k >= 4 the Kesten-Stigum bound is NOT the detection threshold in the disassortative case, and gave algorithms below it; Banks-Moore-Neeman-Netrapalli give information-theoretic bounds showing a gap for large k.

Our work: Method: State the two bounds that bracket the answer, and check whether the gap is an artefact or intrinsic. Result: The Kesten-Stigum bound (a-b)^2 = k(a + (k-1)b) is the reconstruction threshold for the broadcast process on the Galton-Watson tree that describes the local limit, and it is exactly the point where the second eigenvalue of the broadcast kernel crosses the branching-number threshold. For k <= 3 tree... Obstruction: The tree reconstruction threshold for the symmetric k-state channel is known only through bounds (Mossel-Peres for the non-reconstruction side, Sly for k = 3, and asymptotics in k)... Verification: unreviewed.

### E0055. Convergence threshold for the projected power method in the spiked Wigner model

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 10.1, PDF p. 133.

Statement: In the synchronisation model Y = z z^T + sigma W with z in {-1,+1}^n and W a Wigner matrix, for which values of sigma does the projected power method converge to the optimal solution of the maximum-likelihood problem, or at least to a solution correlating well with z, with high probability?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the projected power method for Z2 synchronisation and its convergence threshold. Later work (Chen-Candes on projected power methods, and the AMP literature of Deshpande-Abbe-Montanari) gives sharp thresholds for approximate message passing in this model; whether those thresholds transfer to the projected power method with a random or spectral initialisation was not established...

Our work: Method: Separate the question into the two things a power-method analysis needs: a basin of attraction and an initialisation inside it. Result: With spectral initialisation the analysis is essentially settled by the BBP transition: the top eigenvector of Y correlates with z as soon as sigma < sqrt(n), and one step of the projected power method improves the correlation monotonically, so the interesting regime is sigma of order sqrt(n) and... Obstruction: For random initialisation the first iterate is nearly orthogonal to z, so the signal appears only at second order and the analysis requires controlling the whole trajectory of... Verification: unreviewed.

### E0056. Tightness of the semidefinite relaxation for Z2 synchronisation up to the optimal noise level

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 10.2, PDF p. 134.

Statement: Prove or disprove: with high probability the semidefinite relaxation of the Z2 synchronisation maximum-likelihood problem is tight as long as sigma = O(n^{1/2}) up to logarithmic factors. The source notes this would follow from showing that ||W x^*||_infinity = O(n^{1/2}) up to logarithms, where x^* is the optimal solution.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on tightness of the SDP relaxation for Z2 synchronisation. Bandeira-Boumal-Voroninski and Abbe-Bandeira-Hall give tightness in the regime sigma = O(n^{1/4}) and its refinements; later work pushed the exponent, and I did not establish whether n^{1/2} up to logarithms has been reached.

Our work: Method: Examine the sufficient condition the source names and test whether it can hold, since it involves the optimal solution rather than a fixed vector. Result: For a FIXED vector x independent of W, ||W x||_infinity is of order sqrt(n log n) by a union bound over n coordinates, so the sufficient condition is exactly what one would get if x^* were independent of the noise. The whole difficulty, and the reason the condition... Obstruction: Controlling the residual dependence requires a leave-one-out argument in which one coordinate of the noise is resampled and the maximiser is shown to move little - which is... Verification: unreviewed.

### E0057. Consistency of the maximum likelihood estimator for multireference alignment

Source: Bandeira: Ten lectures and forty-two open problems in the mathematics of data science (bandeira_42_problems_2015), Open Problem 10.4, PDF p. 139.

Statement: (1) Is the quasi-maximum-likelihood (or the maximum-likelihood) estimator consistent for the multireference alignment problem, after fixing the power spectrum appropriately? (2) For a given signal length L and noise level sigma, how large must the number of observations n be to allow reasonably accurate recovery in the multireference alignment problem?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the sample complexity of multireference alignment. Part (2) is answered by Perry, Weed, Bandeira, Rigollet and Singer, 'The sample complexity of multireference alignment' (SIAM J. Math.

Our work: Method: Ask what the sample-complexity answer implies about the estimator question, since the two are related but not equivalent. Result: The sigma^6 rate comes from the third moment: the first two moments of the observations are invariant under the group action in a way that loses the phases, and the bispectrum (the third moment) is the first invariant that determines the signal, with estimation error of order sigma^3... Obstruction: With a degenerate Fisher information the standard consistency proof (uniform law of large numbers plus a well-separated maximum) fails at the rate that matters: the likelihood surface is... Verification: unreviewed.

### E0058. Another kind of Lyapunov function for Volterra quadratic stochastic operators

Source: Rozikov: Quadratic stochastic operators, results and open problems (qso_open_2009), Problem 1, PDF p. 3.

Statement: For the Volterra quadratic stochastic operator V(x)_k = x_k (1 + sum_i a_{ki} x_i) on the simplex S^{m-1}, with A = (a_{ki}) skew-symmetric and |a_{ki}| <= 1, does there exist another kind of Lyapunov function (beyond the known one) for V?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on Lyapunov functions for Volterra quadratic stochastic operators. The literature after 2009 (Ganikhodzhaev, Mukhamedov, Rozikov and successors) continues to use the same logarithmic family and its variants; no fundamentally different Lyapunov function was found.

Our work: Method: Derive the whole family of Lyapunov functions of logarithmic type directly, and see what the source's question is asking one to leave. Result: Take phi_c(x) = sum_i c_i log x_i with c_i >= 0. Along the Volterra map, phi_c(V(x)) - phi_c(x) = sum_i c_i log(1 + (Ax)_i), and since log(1+t) <= t this is at most <c, Ax> for every x in the simplex. Obstruction: Any Lyapunov function must be nonincreasing on all trajectories, and the Volterra dynamics preserves the faces of the simplex, so a candidate must degenerate on every face; the... Verification: unreviewed.

### E0059. Transversality for general quadratic stochastic operators

Source: Rozikov: Quadratic stochastic operators, results and open problems (qso_open_2009), Problem 2, PDF p. 3.

Statement: A skew-symmetric matrix A is transversal if all its even-order leading principal minors are nonzero, and a Volterra QSO is transversal if its A is. Define a concept of transversality for an arbitrary QSO and find necessary and sufficient conditions on the matrix P = (P_{ij,k}) under which the QSO is transversal. (For Volterra QSOs, transversality implies that the fixed point set is finite.)

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on transversality for quadratic stochastic operators. No general definition beyond the Volterra case was found in the post-2009 literature.

Our work: Method: Ask what transversality is FOR, since the definition should be chosen so that the theorem it supports survives. Result: Finiteness of the fixed point set is exactly transversality of the map x -> V(x) - x to zero, i.e. that 0 is a regular value of V - id on each face of the simplex. That is the definition that generalises, and it is intrinsic: it does... Obstruction: For a non-Volterra QSO the fixed-point equation is genuinely quadratic and its solution set is a variety rather than a linear subspace, so 'regular value' is a condition... Verification: unreviewed.

### E0060. Trajectories with periodic itinerary for Volterra quadratic stochastic operators

Source: Rozikov: Quadratic stochastic operators, results and open problems (qso_open_2009), Problem 3, PDF p. 4.

Statement: For a transversal Volterra QSO the fixed point set X is finite, and it is known that a trajectory spends asymptotically all of its time in a neighbourhood U = U_1 union ... union U_t of the fixed points, visiting them in a sequence n_1, n_2, ... called the itinerary. Since X is finite the itinerary repeats values. Is there a trajectory with a PERIODIC itinerary?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on itineraries and heteroclinic cycles for Volterra quadratic stochastic operators and Lotka-Volterra maps. The heteroclinic-cycle literature for continuous-time Lotka-Volterra systems is extensive but I found no result on periodic itineraries for the discrete-time QSO. 2026-09-08: YES via the m=3 cyclic operator (periodic itinerary 1,3,2); in m=4 itineraries mix routes, so eventual periodicity there is the live question. Attempt E0060-A002.

Our work: Method: Read the source's exact wording (Rozikov 2009, p. Result: ANSWERED YES by an example already in the literature: for the m=3 cyclic Volterra operator the itinerary of any non-fixed interior point is periodic, 1 -> 3 -> 2 -> 1 -> ... (sojourns 12, 51, 1073, ... Obstruction: None for the literal question. (2 recorded attempts, E0060-A001-E0060-A002; latest reported.) Verification: unreviewed.

### E0061. Sufficiency of the sign condition for Ulam's ergodic theorem for a three-dimensional Volterra operator

Source: Rozikov: Quadratic stochastic operators, results and open problems (qso_open_2009), Problem 4, PDF p. 4.

Statement: For the Volterra QSO on S^2 given by x' = x(1 + ay - bz), y' = y(1 - ax + cz), z' = z(1 + bx - cy) with a,b,c in [-1,1], Theorem 3 states that if a, b, c all have the same sign and none is zero then Ulam's ergodic theorem (existence of the Cesaro limit of V^k(x)) FAILS. Is the negation of that condition sufficient for the ergodic theorem to hold?

Status: historical status source_says_open. Current-literature status: settled_2026_09_08. Status search: WebSearch 2026-09-08 on Ulam's ergodic conjecture for quadratic stochastic operators and the Zakharevich counterexample. Later work (Ganikhodzhaev-Zanin and successors) extends the failure to further parameter ranges; I found no proof that the complementary region satisfies the ergodic theorem. 2026-09-08: sufficiency PROVED here (E0061-A003): non-cyclic trajectories converge; 2004 note gives necessity; the 2012 iff claim was unsupported by its citation.

Our work: Method: Read the 2004 note (Mathnet full text): it proves only the necessary condition. Result: PROVED: the ergodic theorem holds for (*) whenever a, b, c are not all nonzero of one sign; with the 2004 necessity theorem this is the iff that Ganikhodjaev-Zanin 2012 state (Theorem 1) but attribute to the 2004 note, which does not contain it. Every non-cyclic trajectory converges... Obstruction: None. (3 recorded attempts, E0061-A001-E0061-A003; latest reported.) Verification: unreviewed.

### E0062. Necessary and sufficient conditions for Ulam's ergodic theorem for general Volterra operators

Source: Rozikov: Quadratic stochastic operators, results and open problems (qso_open_2009), Problem 5, PDF p. 4.

Statement: Find necessary and sufficient conditions on the skew-symmetric matrix A of a Volterra QSO under which the ergodic theorem (existence of lim (1/n) sum_{k<n} V^k(x)) holds on S^{m-1} for every initial point, for m >= 2.

Status: historical status source_says_open. Status search: Same search as E0061. Kept open.

Our work: Method: Use the tournament reading of E0061 and ask what the right generalisation of 'all signs equal' is for m > 3. Result: The sign pattern of a skew-symmetric A is a tournament on m vertices, and the Volterra dynamics on the simplex is the discrete-time analogue of the replicator dynamics for that tournament. For replicator dynamics the classical dichotomy is between tournaments that admit an interior evolutionarily stable point (the... Obstruction: The replicator time-average theorem is a continuous-time statement whose proof integrates d(log x_i)/dt; the discrete map replaces that derivative by log(1 + (Ax)_i), which differs from (Ax)_i at... Verification: unreviewed.

### E0063. Do partition-type quadratic stochastic operators inherit the F-QSO fixed point theorem?

Source: Rozikov: Quadratic stochastic operators, results and open problems (qso_open_2009), Problem 10, PDF p. 6.

Statement: For an F-QSO (E_0 = {0,1,...,m}, a set F of 'females' and its complement of 'males', with P_{ij,k} = 1 for k = 0 whenever i and j lie in the same class, and P_{ij,0} = alpha_0 for i in F, j in M) Theorem 5 states that the operator has the unique fixed point (1,0,...,0) and that every trajectory converges to it exponentially fast. Consider now a partition pi = {E_1,...,E_q} of E with P_{ij,k} = 0 whenever i and j lie in the same block; call this a pi-QSO. Is an analogue of Theorem 5 true for any pi-QSO?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on F-quadratic stochastic operators and partition (pi-) QSOs. Later papers on F-QSOs exist (Rozikov and coauthors) but I found none proving or refuting the pi-QSO analogue for general q. 2026-09-09: YES, Theorem 5 extends to every xi-QSO with quadratic convergence (E0063-A002; Lean E0063.lean).

Our work: Method: Read Rozikov Problem 10 and (12) verbatim: a xi-QSO sends same-block pairs and pairs with the empty body to the empty body, cross-block pairs arbitrary. Result: PROVED (answer YES, with a sharper rate): for every xi-QSO with q blocks, 1 - V(x)_0 <= (1 - 1/q)(1 - x0)^2, so e_0 is the unique fixed point and 1 - x0 decays quadratically (and at least like (1-1/q)^n). Theorem 5 extends to every partition; cross-block coefficients... Obstruction: None for Problem 10 as posed. (2 recorded attempts, E0063-A001-E0063-A002; latest reported.) Verification: unreviewed.

### E0064. Fixed points and cycles of strictly non-Volterra operators in four or more types

Source: Rozikov: Quadratic stochastic operators, results and open problems (qso_open_2009), Problem 11, PDF p. 7.

Statement: A strictly non-Volterra QSO satisfies P_{ij,k} = 0 whenever k is in {i,j}. For m = 3 every such operator has the form x' = alpha y^2 + c z^2 + 2yz, y' = a x^2 + d z^2 + 2xz, z' = b x^2 + beta y^2 + 2xy with a+b = c+d = alpha+beta = 1, and Theorem 6 states that (1) for all parameter values the operator has a unique fixed point, which is not attractive, and (2) the operator has 2-cycles and 3-cycles depending on the parameters. Is Theorem 6 true for m >= 4?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on strictly non-Volterra quadratic stochastic operators in dimension four and above. Papers on strictly non-Volterra QSOs on S^3 exist (Rozikov and coauthors, post-2009) and give partial classifications; I did not establish whether uniqueness and non-attractiveness of the fixed point are proved for all m >= 4. 2026-09-09: non-attractiveness clause of Theorem 6 fails for m>=4 (globally attracting symmetric family; Jamilov-Ladra-Mukhitdinov 2016/17); uniqueness/cycles in general still open. Attempt E0064-A002.

Our work: Method: Uniqueness clause of Theorem 6 in m >= 4. Result: The uniqueness clause of Theorem 6 is FALSE for every m >= 5: the explicit 5-type operator above has two fixed points (both exact; tangent Jacobian eigenvalues (-2,-1,-1,2) at p, index -1, and (-4/3,-1/3,-1/3,0) at q, index +1; neither attractive), and for m >= 6 any operator with... Obstruction: m = 4 uniqueness: an index count would work if every fixed point had index +1, but the 5-type example shows a saddle of index -1 can occur... Proof/memo: ~/<private-repo>/06_math_research/prob1000_lean_20260908/REPORT_E0064_strictly_nonVolterra_fixed_point_uniqueness_fails_for_five_types_2026-09-11.md. (3 recorded attempts, E0064-A001-E0064-A003; latest reported.) Verification: unreviewed.

Correction (CORRECTIONS.md): this derivation was independently re-checked and confirmed to hold as stated.

### E0065. Exact regularity thresholds for quadratic stochastic operators

Source: Rozikov: Quadratic stochastic operators, results and open problems (qso_open_2009), Problem 12, PDF p. 7.

Statement: For a QSO V with matrix P = (P_{ij,k}) on S^{m-1}, let lambda_m be the smallest number such that P_{ij,k} > lambda_m for all i,j,k implies V is regular (every trajectory converges to a unique fixed point). Theorem 7 gives lambda_m <= 1/(2m) and lambda_2 = (3 - sqrt(7))/2. Find the exact value of lambda_m for every m >= 3.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on regularity thresholds for quadratic stochastic operators. No exact value beyond m = 2 was found.

Our work: Method: Check the two given data points against each other, since they are stated for the same quantity and should be consistent. Result: They are consistent but only just, and the comparison is informative. At m = 2 the general bound gives lambda_2 <= 1/4 = 0.25, while the exact value is (3 - sqrt(7))/2 = 0.17712..., so the general bound overshoots by about 41 per cent at the only point... Obstruction: The exact m = 2 value comes from solving a one-dimensional dynamical problem explicitly (the simplex is an interval), and for m >= 3 the extremal operator realising... Verification: unreviewed.

### E0066. Trajectories of quadratic bistochastic operators

Source: Rozikov: Quadratic stochastic operators, results and open problems (qso_open_2009), Problem 13, PDF p. 8.

Statement: A quadratic operator V on S^{m-1} is bistochastic if V(x) is majorised by x for every x, i.e. the partial sums of the decreasing rearrangement of V(x) are dominated by those of x. Investigate the behaviour of the trajectories of the bistochastic quadratic operators.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on quadratic bistochastic (doubly stochastic) operators and their trajectories. The classification results of Ganikhodzhaev and coauthors on extreme points of the set of quadratic bistochastic operators are the main literature; a general description of trajectory behaviour was not found.

Our work: Method: Use majorisation directly: bistochasticity says V(x) is majorised by x, so every Schur-concave function increases along trajectories. Result: That gives the dynamics a Lyapunov function for free, and a canonical one: the Shannon entropy H(x) = -sum_i x_i log x_i is Schur-concave, so H(V(x)) >= H(x) for every bistochastic V and every x. Hence H is nondecreasing along every trajectory and bounded above by log m... Obstruction: The entropy-preserving set can be large. Verification: unreviewed.

### E0067. Historic behaviour of quadratic stochastic operators on a set of positive measure

Source: Rozikov: Quadratic stochastic operators, results and open problems (qso_open_2009), Problem 19, PDF p. 10.

Statement: A trajectory has historic behaviour if the Cesaro averages of its iterates fail to converge. Find a class of QSOs for which the set of initial states giving rise to trajectories with historic behaviour has positive Lebesgue measure. The source notes that a similar problem was discussed by Ruelle.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on historic behaviour (Ruelle-Takens historic behaviour, Takens's last problem) for quadratic stochastic operators. The general dynamical-systems literature has positive-measure historic behaviour examples (Kiriki-Soma and successors) but I found none for QSOs.

Our work: Method: Use the m = 3 counterexample of Zakharevich as a seed and ask whether its historic set has positive measure. Result: In Zakharevich's example (a = b = c = 1, the fully cyclic Volterra operator on S^2) the interior fixed point is a repeller and every interior trajectory spirals out to the boundary heteroclinic cycle, so the Cesaro averages oscillate for EVERY interior initial condition - the historic... Obstruction: Producing coexistence requires an operator whose simplex splits into two basins, one of which is a stable heteroclinic cycle. Verification: unreviewed.

### E0068. Quadratic stochastic operators that are eventually idempotent

Source: Rozikov: Quadratic stochastic operators, results and open problems (qso_open_2009), Problem 21, PDF p. 11.

Statement: Bernstein's problem asks for a description of all QSOs with V^2 = V (Bernstein mappings, the stationarity principle or Hardy-Weinberg law); it was solved by Bernstein for m = 3 and by Lyubich for all m under a regularity assumption. Describe all QSOs which satisfy V^r(x) = V(x) for every x in S^{m-1} and some r >= 2.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the Bernstein problem for quadratic stochastic operators and on periodic Bernstein-type operators. The Lyubich theory of Bernstein algebras is the standing framework; I found no classification of the V^r = V case.

Our work: Method: Translate V^r = V into a statement about the image and the dynamics on it, before any algebra. Result: V^r = V says that V restricted to its own image W = V(S^{m-1}) satisfies V^{r-1} = id on W, so V|_W is a bijection of finite order r-1. Hence the classification splits into two independent parts: (i) the structure of the image W and the retraction of... Obstruction: A quadratic map cannot have finite order on a set with nonempty interior unless it is affine there, because the degree of V^{r-1} is 2^{r-1} and equals 1... Verification: unreviewed.

### E0069. Bi-harmonic functions on measured groups

Source: Five remarks about random walks on groups (five_remarks_rw_groups_2014), Problem 1, PDF p. 24.

Statement: Does every measured group (G, mu) admit a non-trivial bi-mu-harmonic function, i.e. a function that is both left and right mu-harmonic?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on bi-harmonic functions for random walks on groups and on the Poisson boundary of a measured group. Found the standard Furstenberg-Kaimanovich theory and later work on the Poisson boundary; no resolution of the bi-harmonic existence question was found.

Our work: Method: Compare the two one-sided problems, since a bi-harmonic function must be harmonic for both the left and the right walk. Result: A left mu-harmonic function is a limit of boundary data on the Poisson boundary (B, nu) of (G, mu) and a right mu-harmonic function corresponds to the boundary of the reflected measure mu-check. A bi-harmonic function is therefore a function measurable with respect to both boundaries at once... Obstruction: For non-symmetric mu the left and right Poisson boundaries are different measure spaces with no canonical map between them, so a common nonconstant function need not exist; constructing... Verification: unreviewed.

### E0070. A quotient space with no nonconstant quasi-harmonic functions

Source: Five remarks about random walks on groups (five_remarks_rw_groups_2014), Problem 2, PDF p. 24.

Statement: Construct a countable measured group (G, mu) and an infinite-index subgroup H < G such that the quotient space G/H does not admit any nonconstant left (quasi-)mu-harmonic functions whatsoever.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on harmonic functions on quotient spaces of measured groups and the Liouville property for coset spaces. The Kaimanovich-Vershik and Rosenblatt criteria for the Liouville property on groups are standard; the coset-space version with infinite index was not found resolved.

Our work: Method: Ask what the Liouville property means on a coset space and where the standard proofs of it use the group structure. Result: On a group, the Liouville property is equivalent to triviality of the Poisson boundary and is proved via the entropy criterion (the Avez entropy of mu vanishes) or via amenability plus a Folner argument. Both proofs use the transitive action of G on itself by translations. Obstruction: Quasi-harmonic functions are only asymptotically harmonic, so triviality of the Poisson boundary does not exclude them; the source's question deliberately asks for the stronger conclusion. Verification: unreviewed.

### E0071. Sublinear drift on quotient spaces under ergodicity on the Poisson boundary

Source: Five remarks about random walks on groups (five_remarks_rw_groups_2014), Problem 3, PDF p. 25.

Statement: Let (G, mu) be a measured group and H < G a subgroup which acts ergodically on the Poisson boundary of (G, mu). If d is a left G-invariant metric on the quotient space G/H, is it true that (1/n) sum_{k <= n} integral over G of d(gH, H) d mu^{*k}(g) tends to 0?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on drift of random walks on coset spaces and ergodic subgroup actions on the Poisson boundary. No resolution found.

Our work: Method: Interpret the conclusion as sublinear drift and ask what ergodicity of H on the boundary buys. Result: The quantity is the Cesaro average of the expected distance from the origin coset, so the assertion is that the walk projected to G/H has zero SPEED in the Cesaro sense. Ergodicity of H on the boundary says that the boundary carries no nonconstant H-invariant function, which is... Obstruction: The fundamental inequality is proved for random walks on groups, and its coset-space version requires an entropy for a non-transitive action; if the metric d has subexponential growth... Verification: unreviewed.

### E0072. Vanishing drift for conjugation-invariant metrics on symmetric measured groups

Source: Five remarks about random walks on groups (five_remarks_rw_groups_2014), Problem 4, PDF p. 25.

Statement: Let (G, mu) be a symmetric measured group and suppose there exists a bi-invariant (conjugation-invariant) and mu-integrable (semi-)metric d on G. Is the drift delta_d(mu) equal to 0? The source suggests as a first test case the commutator subgroup of the free group on two generators with the stable commutator length.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on drift of random walks with respect to conjugation-invariant metrics and stable commutator length. The stable commutator length literature (Calegari) and the bi-invariant metric literature (Burago-Ivanov-Polterovich) are the relevant background; no resolution of the drift question was found.

Our work: Method: Use symmetry of mu together with conjugation invariance of d, which are the only two hypotheses, and see what they force. Result: Conjugation invariance means d(g,h) depends only on the conjugacy class of g^{-1} h, so the function g -> d(e,g) is a class function; symmetry of mu means the walk is reversible. The drift is then the limit of (1/n) E[phi(X_n)] for a class function phi that is subadditive... Obstruction: The supremum in Bavard duality is over an infinite-dimensional set of quasi-morphisms with unbounded defect, and the drift of the supremum can exceed the supremum of the drifts... Verification: unreviewed.

### E0073. Isometric extensions of the Poisson boundary and non-ergodic self-products

Source: Five remarks about random walks on groups (five_remarks_rw_groups_2014), Problem 5, PDF p. 25.

Statement: Let (G, mu) be a symmetric measured group with Poisson boundary (B, m) and let (X, xi) be an ergodic (G, mu)-space admitting (B, m) as a factor. Assume that the product of (X, xi) with itself is not ergodic. Does this imply that there exists a factor (Y, eta) of (X, xi) which is a nontrivial isometric extension of (B, m)?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on relative Furstenberg-Zimmer structure theory for measured group actions over the Poisson boundary. The absolute Furstenberg-Zimmer theorem gives the isometric/weakly-mixing dichotomy for measure-preserving actions; the source's question is its relative form over a boundary, which is not measure preserving.

Our work: Method: Recognise the shape: non-ergodicity of the self-product is the classical signal of a nontrivial Kronecker factor, so the question asks for a relative Furstenberg-Zimmer dichotomy over the Poisson boundary. Result: In the measure-preserving setting the implication is a theorem: an ergodic system whose self-product is non-ergodic has a nontrivial Kronecker (isometric) factor, obtained from the eigenfunctions witnessing the non-ergodic invariant function. The obstruction to importing it is precisely that a (G, mu)-space over the Poisson boundary is NOT... Obstruction: Stationary actions have no unitary representation of G on L^2 preserving the measure, so the eigenfunction argument has no starting point; the substitutes (Nevo-Zimmer structure theory) apply to... Verification: unreviewed.

### E0074. Joint queue length generating function for a two-queue gated plus one-limited polling system

Source: On open problems in polling systems (polling_open_2014), Open problem 1, PDF pp. 2 and 4.

Statement: Determine the joint queue-length probability generating function at polling instants in the two-queue polling system in which one queue receives gated service and the other one-limited service (the G/1-L case). The source records the functional equation the pair (F_1, F_2) satisfies and notes that substituting z_1 = 0 yields a derivative, while substituting z_1 = h_1(z_1,z_2) leads to iterates F_1(h_1(h_1(z_1,z_2),z_2),z_2) with no apparent closure.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the two-queue gated plus one-limited polling model and exact analysis of polling systems with mixed disciplines. Boon-Boxma-Winands remains the reference for the open status; the boundary-value-problem literature for two-queue polling models (Cohen-Boxma, Fayolle-Iasnogorodski) covers other discipline pairs.

Our work: Method: Classify the functional equation, since the analytic method that applies is determined by whether the underlying branching structure is a multitype branching process with immigration. Result: Gated service is of branching type (each customer present at the polling instant is replaced during the visit by the customers arriving during its service), while one-limited service is not: exactly one customer is served regardless of the queue length, so the offspring generating function is degenerate. The... Obstruction: The boundary value method needs the kernel to define a Riemann surface of genus zero or one; with a gated component the kernel is not polynomial of degree... Verification: unreviewed.

### E0075. Large switch-over time asymptotics for polling systems with renewal arrivals

Source: On open problems in polling systems (polling_open_2014), Open problem 2 and Conjecture 4.2, PDF pp. 4, 5 and 7.

Statement: Prove Conjecture 4.2: a cyclic polling system with general (renewal) arrival processes converges to a deterministic cyclic system when the deterministic switch-over times tend to infinity. The corresponding result for Poisson arrivals is known and rests on the multitype branching interpretation and a relation between models with and without switch-over times; the source supports the general case by simulation.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on large switch-over time asymptotics in polling systems with general renewal arrivals. The Poisson case (Winands and coauthors) is the standing result; no proof for renewal arrivals was found.

Our work: Method: Ask what the limit statement is really saying, so as to identify the minimal probabilistic input. Result: As the deterministic switch-over time S grows, each cycle lasts at least the total switch-over time, so the number of arrivals per cycle at queue i is A_i(S(1+o(1))), and the assertion that the system becomes deterministic is exactly a law of large numbers for the renewal counting process... Obstruction: Tightness of the residual life uniformly in S fails for heavy-tailed interarrival distributions with infinite mean residual life, so the conjecture as stated needs a moment condition that... Verification: unreviewed.

### E0076. Classifying the polling disciplines that exhibit the deterministic large switch-over limit

Source: On open problems in polling systems (polling_open_2014), Open problem stated after Open problem 2 (dynamic visit orders), PDF p. 7.

Statement: The source records, from reference [14], that numerical testing shows the same large switch-over-time limit theorems carry over to systems with Poisson arrivals and DYNAMIC visit orders, in which there is no pre-determined order in which the queues are served. The problem is the classification of polling systems, in terms of service, visit and scheduling disciplines, which exhibit this behaviour.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on polling systems with dynamic visit orders and large switch-over asymptotics. Found the numerical study the source cites and later work on dynamic polling policies; no classification theorem was found.

Our work: Method: Ask what property of a discipline the limit theorem actually uses, given the reduction in E0075. Result: The reduction there shows the limit needs only (i) a law of large numbers for arrivals over a long cycle and (ii) asymptotic decoupling of successive cycles. Neither mentions the visit order, so a discipline should exhibit the behaviour whenever the SERVICE rule leaves a bounded amount of... Obstruction: For dynamic visit orders the sequence of visited queues is itself random and depends on the state, so 'cycle' is not well defined and the decoupling in (ii)... Verification: unreviewed.

### E0077. Is the squared coefficient of variation of a Markov modulated Poisson process at least one?

Source: Stationary Markovian Arrival Processes, results and open problems (map_processes_open_2019), Conjecture 4.1, PDF p. 8.

Statement: For an irreducible Markov modulated Poisson process (MMPP), is the squared coefficient of variation c^2 of the stationary inter-event time at least 1? The source records that this is folklore, that they initially believed it easy to verify, and that to date there is no known proof for an arbitrary irreducible MMPP.

Status: historical status source_says_open; current status resolved_in_literature; result_status resolved_in_literature. Not admitted (literature exclusion). Resolved by he_phase_type_scv_2021, Theorem 3.2 p.886; section 4.1 p.888.

Excluded: Excluded from currently open and newly solved counts. E0077-A002 is an independent rederivation, not a newly solved open problem. Its general Cox extension also requires an almost-sure nonempty-process hypothesis. Historical rows and proof attempts are preserved; E0077-A003 supplies the correction.

### E0078. Stochastic ordering of time-stationary and event-stationary MMPP waiting times

Source: Stationary Markovian Arrival Processes, results and open problems (map_processes_open_2019), Conjecture 4.2, PDF p. 8.

Statement: For every finite irreducible MMPP with nonzero nonnegative arrival-rate diagonal D, generator Q and stationary phase law pi, let lambda=pi D 1 and alpha=pi D/lambda. Is T^pi stochastically larger than T^alpha, where both are phase-type with subgenerator Q-D and initial laws pi and alpha respectively? This compares two stationary sampling conventions, not an exponential of the same mean.

Status: historical status source_says_open. Status search: Primary source statement and counterexample checked. He 2021 section 4.3 repeats this ordering question. The original title and statement mistakenly mentioned an exponential. E0078-A002 targets the correct pair and is preserved.

Our work: Method: Exact rational uniformization with independent row and column recurrences, bounded Poisson tail and an irreducible positive-rate 12-state cycle. Result: S_pi(19/2)-S_alpha(19/2) < -1/300000. Corrected problem statement compares time-stationary and event-stationary waits; no exponential comparison is refuted. Obstruction: No smallest-state or originality claim. Proof/memo: ~\<private-repo>\12_cognitive_architecture\audits\evidence\2026\09\08\overnight-mmpp-exact\sinusoidal12\PROOF.md. (3 recorded attempts, E0078-A001-E0078-A003; latest reported.) Verification: exact_rational_counterexample_root_checked_2026_09_08.

### E0079. Scanning Brownian motion for a prescribed set of paths

Source: Pitman and Tang: Patterns in random walks and Brownian motion (pitman_tang_patterns_2014), Question 1.5, PDF p. 4.

Statement: Given a Borel measurable subset S of C[0,1], can one find a random time T such that X_T := (B_{T+u} - B_T ; 0 <= u <= 1) lies in S with probability one? The source notes that this pattern-scanning problem in continuous time appears not to have been studied, and gives as examples the set E of excursion paths, the set of first-passage bridges, and the set RER of reflected excursion paths.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on scanning for path patterns in Brownian motion and on the Pitman-Tang programme. Later work on 'patterns in Brownian motion' and on the Vervaat transform continues the line; I found no general criterion for which Borel subsets of C[0,1] are scannable.

Our work: Method: Recognise the structure: the map t -> theta_t B, the shifted and recentred path, is a stationary Markov process on C[0,1] with the Wiener measure as its stationary law, so the question... Result: For a stationary process the hitting question is governed by a capacity, not a measure, which is exactly why S can have Wiener measure zero and still be scannable - the source's own examples (excursions, first-passage bridges) all have measure zero. Two immediate consequences that delimit the answer:... Obstruction: The shift process on Wiener space is not symmetric, so no Dirichlet form is available to compute the capacity, which is precisely the source's own Open problem 4.2. Verification: unreviewed.

### E0080. Capacity criterion for patterns in Brownian motion on the half line

Source: Pitman and Tang: Patterns in random walks and Brownian motion (pitman_tang_patterns_2014), Question 1.5-prime, PDF p. 27.

Statement: Given a Borel measurable set S' in C[0, infinity), decide whether CapMW(S') := integral over t >= 0 of e^{-t} P[there exists T in [0,t] with theta_T B in S'] dt is zero or strictly positive, where theta_t B := (B_{t+u} - B_t ; u >= 0). The source notes that CapMW is a Choquet capacity.

Status: historical status source_says_open. Status search: Same search as E0079. Kept open.

Our work: Method: Compare CapMW with the classical Wiener-space capacities to see which tools transfer. Result: CapMW is the hitting capacity of a stationary, non-symmetric Markov process, whereas the Malliavin-Fukushima capacity CapX on Wiener space is the capacity of a SYMMETRIC Dirichlet form (the Ornstein-Uhlenbeck form). The two are therefore capacities of different processes on the same space, and there is no a priori... Obstruction: Choquet capacitability gives measurability of the hitting probability but no computation. Verification: unreviewed.

### E0081. Order of the expected waiting time for a scale-indexed family of discrete patterns

Source: Pitman and Tang: Patterns in random walks and Brownian motion (pitman_tang_patterns_2014), Question 1.7, PDF p. 5.

Statement: Given for each n a collection A_n of patterns of length n, what is the order of the expected waiting time E T(A_n) until some element of A_n is observed in a simple random walk? The source notes it is aware of no previous study of pattern problems in which a natural definition of the collection of patterns is made for each n.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on expected waiting times for families of patterns in random walks (the Guibas-Odlyzko correlation-polynomial theory and the Conway leading-number method). Those give exact answers for a FIXED finite collection; the asymptotics for a natural family indexed by n is what the source asks for.

Our work: Method: Use the martingale (Conway leading number) identity for a collection, which is exact for any finite A_n, and read off what the asymptotics needs. Result: For a collection A of patterns in a fair coin sequence, the gambling-team martingale gives the exact relation sum over patterns w in A of P(the pattern seen is w) times the correlation polynomial of w with itself equals E T(A) - more precisely E T(A) = sum_w... Obstruction: The linear system has |A_n| unknowns, which grows exponentially, and its matrix of pairwise correlations has no product structure for the natural families (excursions, bridges, first passage), so... Verification: unreviewed.

### E0082. Exact waiting-time asymptotics for discrete bridges and first-passage patterns

Source: Pitman and Tang: Patterns in random walks and Brownian motion (pitman_tang_patterns_2014), Open problem 2.3, PDF p. 13.

Statement: Using the matching matrix method as in Theorem 2.1, (1) determine the exact asymptotics of E T(BR_{alpha,n}) for alpha in R as n tends to infinity, and (2) determine the exact asymptotics of E T(FP_{alpha,n}) for alpha < 0. The source proves the two-sided bounds c n <= E T <= C n in both cases and obtains E T(BR_{alpha,n}) of order n by a scaling limit argument.

Status: historical status source_says_open. Status search: Same search as E0081. Kept open.

Our work: Method: Ask what upgrading two-sided bounds to exact asymptotics needs in this framework. Result: By the correlation-system identity of E0081, an exact constant requires the limit of the normalised solution of the Conway system, i.e. the limit of the empirical distribution pi_w over the family together with the limiting correlation profile. For the excursion family the source obtains the exponent 3/2 from... Obstruction: The set of self-overlaps of a bridge pattern depends on the pattern, not just on n, so the correlation correction is an average over the family with respect... Verification: unreviewed.

### E0083. Relation between the Wiener-space capacity and the shift capacity

Source: Pitman and Tang: Patterns in random walks and Brownian motion (pitman_tang_patterns_2014), Open problem 4.2(1), PDF p. 27.

Statement: Is there any relation between the two capacities CapX and CapMW on Wiener space, where CapX is the capacity associated with the Ornstein-Uhlenbeck (Malliavin) Dirichlet form and CapMW is the hitting capacity of the spacetime shift process?

Status: historical status source_says_open. Status search: Same search as E0079. Kept open.

Our work: Method: Compare the null sets of the two capacities on the source's own examples, since a relation must at least be consistent with those. Result: The two capacities cannot be equivalent. The set of paths of finite quadratic variation different from t, for instance, is CapX-polar (it is a set of Malliavin capacity zero, being excluded by the OU quasi-sure quadratic variation theorem) but is hit by the shift with probability zero as... Obstruction: A relation in the other direction would need CapX to dominate CapMW, and there is no reason for it: CapX measures sensitivity to perturbations in Cameron-Martin directions, CapMW... Verification: unreviewed.

### E0084. A Dirichlet form for the spacetime shift process on Wiener space

Source: Pitman and Tang: Patterns in random walks and Brownian motion (pitman_tang_patterns_2014), Open problem 4.2(2), PDF p. 27.

Statement: Propose a non-symmetric Dirichlet form for the shifted process (theta_t B)_{t >= 0} which permits one to compute the capacities of the sets of paths E (excursions), M, BR_alpha and so on.

Status: historical status source_says_open. Status search: Same search as E0079. Kept open.

Our work: Method: Write down the generator of the shift and ask what a form for it would have to look like. Result: The shift semigroup on C[0, infinity) with Wiener stationary law is generated by the time derivative along the path, i.e. formally by the operator that shifts the path and re-centres it, and this generator is a pure translation - it has no symmetric part in L^2 of the... Obstruction: Without a sector condition the Ma-Rockner theory does not apply and there is no quasi-regular form, hence no capacity calculus. Verification: unreviewed.

### E0085. Favorite-site asymptotics for the two-dimensional random walk on a subgroup-shifted lattice

Source: Topics and problems on favorite sites of random walks (favorite_sites_2016), Open problem 1, PDF p. 5.

Statement: For d = 2, is it true that the results corresponding to Theorems 2.4 and 2.5 of the paper (the almost-sure asymptotics of the favorite-site quantities established there in higher dimensions) hold? The source explains the difficulty: the lower-bound argument would need estimates on P(T_H > exp(u_n n)), on P(T_0 - T_H > exp(u_n n)), and, for x in Z^2 with 0 < |x| < n^{u_n - 1}, on P(T_H - T_{x+H} > exp(u_n n)).

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on favorite sites of the two-dimensional simple random walk and on late points and thick points of planar walk. The Dembo-Peres-Rosen-Zeitouni thick-point and late-point results and the Abe-Biskup work on the local-time maximum are the relevant literature; the specific two-dimensional analogue of the source's theorems was not found.

Our work: Method: Identify what makes d = 2 different, given that the source's higher-dimensional proof is a first- and second-moment computation over hitting times. Result: In d >= 3 the walk is transient, so the hitting times T_H of a finite set H are integrable with exponential tails determined by the escape probability, and the three probabilities the source lists factor approximately. In d = 2 the walk is recurrent and every hitting... Obstruction: Proving that form needs the second-moment method for a log-correlated field with the truncated (barrier) argument, which for random-walk local times requires an isomorphism with the Gaussian free... Verification: unreviewed.

### E0086. Largest completely covered disc for a random walk in an annular region

Source: Topics and problems on favorite sites of random walks (favorite_sites_2016), Open problem 2, PDF p. 6.

Statement: Consider D_n intersect H with D_n contained in the complement of the disc D(0, a_n), where a_n tends to infinity. What is the almost sure asymptotic of M_{D_n}(n), the maximal local time over that region? The source is especially interested in the case D_n contained in D(0,2 a_n) minus D(0, a_n) with a_n = n^alpha for 0 < alpha < 1/2, noting that the largest disc completely covered by the planar walk before time tau_n has radius n^{1/2 + o(1)}, and conjectures that for a_n at least n^{1/2 + eps} a corresponding statement holds.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the largest completely covered disc for planar random walk and on late points in annuli. The Dembo-Peres-Rosen-Zeitouni cover-time and late-point results are the closest; the annular-region refinement was not found.

Our work: Method: Use the scaling that the source itself supplies: the walk run for n steps reaches distance about n^{1/2}, so an annulus at radius a_n = n^alpha with alpha < 1/2 is well... Result: That dichotomy fixes the shape of the answer without any computation. For alpha < 1/2 the annulus lies deep inside the walk's range and the local-time field there is, after time-change, a copy of the field near the origin at a reduced intensity: the number of visits to... Obstruction: Turning that into a theorem needs the multi-scale second-moment argument for the local-time field restricted to an annulus, where the field is log-correlated but NOT stationary: the variance... Verification: unreviewed.

### E0087. Coupling a variant Gaussian free field with the planar random walk local times

Source: Topics and problems on favorite sites of random walks (favorite_sites_2016), Open problem 3, PDF p. 7.

Statement: Consider the Gaussian free field on D(0,n) whose covariance is E_x[K(tau_n, y)] rather than the standard one, and the corresponding quantity V_n(lambda). Is there a sequence of couplings of that Gaussian free field on D(0,n) with the simple random walk on Z^2 such that for every eps > 0 and lambda in the relevant range, P(Lambda_n(lambda) contained in V_n(lambda - eps)) tends to 1, or P(V_n(lambda) contained in Lambda_n(lambda - eps)) tends to 1?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on couplings of random walk local times with the Gaussian free field (isomorphism theorems and the Jego / Lupu / Abe-Biskup line). The Dynkin and Eisenbaum isomorphisms and the Lupu coupling are the relevant tools; the specific one-sided inclusion for the source's modified field was not found.

Our work: Method: Ask which isomorphism could give a one-sided inclusion of level sets, since the classical ones are identities in law rather than couplings of level sets. Result: The Dynkin and Eisenbaum isomorphisms identify the local-time field plus an independent squared free field with a shifted squared free field, so they equate LAWS and do not by themselves couple level sets. The tool that does couple them is Lupu's isomorphism, which realises the walk's loop soup... Obstruction: Without an underlying Dirichlet form there is no loop soup, so there is no metric graph and no Lupu coupling; one would have to show directly that E_x[K(tau_n,y)]... Verification: unreviewed.

### E0088. Noise sensitivity of bootstrap percolation at the critical density

Source: Noise sensitivity in bootstrap percolation (bootstrap_noise_sensitivity_2015), Question 1.3, PDF p. 2.

Statement: Is it true that, for any sequence of finite graphs G_n, complete occupation by the k-neighbour bootstrap rule at the critical density p_c(G_n, k) is noise sensitive versus noise insensitive exactly according to whether p_c(G_n,k) tends to 0 or lim inf_n p_c(G_n,k) > 0?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on noise sensitivity of bootstrap percolation after 2015. Found later work on noise sensitivity in various models but no proof or counterexample for the general dichotomy stated here.

Our work: Method: Test the proposed dichotomy against the mechanism that makes bootstrap percolation sensitive, which is that the final configuration is determined by a sparse set of nucleation centres. Result: When p_c tends to 0, complete occupation is caused by a small number of critical droplets whose positions are spread over the graph, and each individual bit has tiny influence while the total influence is large - the standard Benjamini-Kalai-Schramm signature of sensitivity, so that half of the... Obstruction: The disjoint-union construction changes p_c of the whole sequence to the smaller of the two, so the naive falsification does not immediately work; a real counterexample must keep... Verification: unreviewed.

### E0089. Concentration of the critical density for bootstrap percolation on random regular graphs

Source: Noise sensitivity in bootstrap percolation (bootstrap_noise_sensitivity_2015), Question 1.4(a), PDF p. 3.

Statement: Consider the random d-regular graph sequence G_{n,d} with 2 <= k <= d-2. Is there a delta > 0 such that P_{G_{n,d}}(Corr_{p_c(n)}(f_n(omega), f_n(omega^eps)) > delta) tends to 1 as n tends to infinity? The source notes that establishing this would require showing that the critical density theta(G) concentrates around its mean, for instance that P(theta(G) > 1 - 2 eps) tends to 1, and suggests trying Azuma-Hoeffding for a Lipschitz martingale exploring G_{n,d} edge by edge or in the configuration model.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on bootstrap percolation on random regular graphs and concentration of the critical density (Balogh-Pittel and successors). The Balogh-Pittel analysis gives the critical density for random regular graphs; concentration of the quantity the source calls theta(G) across the graph randomness was not found.

Our work: Method: Check whether the suggested Azuma route can work, by computing the Lipschitz constant of the edge-exposure martingale. Result: Switching a single edge in the configuration model can change the final occupied set by an amount that is not bounded: in the supercritical regime a single edge can complete a nucleating droplet whose growth then occupies a constant fraction of the graph, so the vertex-exposure Lipschitz constant... Obstruction: Sharp-threshold theorems need a symmetric product measure, and the configuration model's edge set is not a product; transferring requires a switching argument whose error is of the same... Verification: unreviewed.

### E0090. Noise stability of complete occupation on random regular graphs

Source: Noise sensitivity in bootstrap percolation (bootstrap_noise_sensitivity_2015), Question 1.4(b), PDF p. 3.

Statement: For the random d-regular graph sequence with 2 <= k <= d-2, is the event C_n of complete occupation actually noise stable? That is, for any delta > 0, is there an eps > 0 such that with probability at least 1 - delta for all large n - or even with probability tending to 1 - the correlation between f_n(omega) and f_n(omega^eps) is at least 1 - delta?

Status: historical status source_says_open. Status search: Same search as E0089. Kept open.

Our work: Method: Ask what stability would mean given the nucleation picture, since stability and the sensitivity of E0088 are the two ends of the same spectrum. Result: On a random regular graph the critical density is bounded away from 0 (a positive fraction of vertices must be seeded), so by the dichotomy proposed in Question 1.3 the event should be insensitive; stability is the strictly stronger statement that the Fourier weight is concentrated on a... Obstruction: That reduction is only valid if complete occupation is asymptotically determined by the seed density, which is precisely the concentration statement of Question 1.4(a); the two questions are... Verification: unreviewed.

### E0091. Noise sensitivity of bootstrap percolation on tori and boxes

Source: Noise sensitivity in bootstrap percolation (bootstrap_noise_sensitivity_2015), Conjecture 1.6, PDF p. 3.

Statement: For any d >= k > 2, the event C_n of complete occupation under the k-neighbour bootstrap rule on the sequence of tori T_n^d and boxes [n]^d is noise sensitive.

Status: historical status source_says_open. Status search: Same search as E0088. Kept open.

Our work: Method: Check the conjecture against the proposed dichotomy of Question 1.3, since the two must be consistent. Result: They are consistent and the conjecture is the interesting instance: on [n]^d with k >= 2 the critical density is p_c of order (log^{(k-1)} n)^{-(d-k+1)} up to constants (the Cerf-Cirillo-Holroyd-Balogh-Bollobas-Morris asymptotics), which tends to 0, so Question 1.3 predicts sensitivity. The mechanism is explicit here in a way... Obstruction: BKS requires the sum of squared influences to tend to zero, and with influences of order 1/polylog and of order n^d p_c many relevant vertices the sum is... Verification: unreviewed.

### E0092. An explicit set of generators achieving Wilson's mixing bound

Source: Diaconis: Some things we have learned (about Markov chain Monte Carlo) (diaconis_mcmc_learned_2013), Question 1, PDF p. 9.

Statement: In item 2 of Wilson's theorem (Example 6 of the paper), the mixing result holds for almost all choices of the generating vectors V_1, V_2, ..., V_N. Can an explicit set be found, for example for N = 2n?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on Wilson's theorem for random walks generated by random vectors on the hypercube and explicit generating sets achieving the same mixing time. Found the derandomisation literature for expanders (Margulis, Lubotzky-Phillips-Sarnak, and the zig-zag product) but nothing specific to Wilson's example.

Our work: Method: Recognise the question as a derandomisation problem and ask what property of a random generating set the proof uses. Result: Wilson's argument uses that a random set of N vectors in F_2^n spans and has no small-weight linear dependencies, i.e. that the code generated by the V_i has large dual distance; the mixing bound is then a Fourier computation over the characters, and the rate depends only on... Obstruction: For binary codes no explicit construction meets the Gilbert-Varshamov bound; algebraic-geometry codes beat it only over alphabets of size at least 49. Verification: unreviewed.

### E0093. Typical mixing rate of a random random walk on a general finite group

Source: Diaconis: Some things we have learned (about Markov chain Monte Carlo) (diaconis_mcmc_learned_2013), Question 2, PDF p. 9.

Statement: For an arbitrary finite group G, if a generating set S is chosen at random, what is the typical rate of convergence of the random walk it generates? The source notes that this is the topic of random random walks, surveyed by Hildebrand, and that the best bounds on the diameter of random Cayley graphs are due to Babai, Beals and Seress, which can be turned into mixing bounds.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on random random walks on finite groups and mixing times of random Cayley graphs. The Hildebrand survey, the Babai-Beals-Seress diameter bounds and the later results on random Cayley graphs of abelian and of simple groups are the standing literature; a general answer for arbitrary G was not found.

Our work: Method: Separate the two regimes the question conflates: |S| growing with log|G| (where a cutoff is expected) and |S| fixed. Result: For |S| of order log|G| the random Cayley graph is an expander with high probability for many families and the mixing time is of order log|G|/log|S|, which is the diameter lower bound, so the answer is 'cutoff at the diameter' and the content is the constant. For |S|... Obstruction: The two regimes are separated by the group's representation theory, and for a general finite group the character degrees are not known well enough to run the upper... Verification: unreviewed.

### E0094. Which single generator best speeds up a given random walk on a group

Source: Diaconis: Some things we have learned (about Markov chain Monte Carlo) (diaconis_mcmc_learned_2013), Question 3, PDF p. 9.

Statement: Fix a generating set S of a finite group G. What element should be added to S to best speed up mixing? For example, for G = S_n with n odd and S = {(1,2), (1,2,...,n)} it is known that order n^3 log n steps are necessary and sufficient; is there a choice of sigma to be added that appreciably speeds this up?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on adding a generator to speed up mixing on the symmetric group and on the transposition-plus-n-cycle walk. The n^3 log n result (Diaconis-Saloff-Coste; Hildebrand) stands; I found no analysis of the optimal added generator.

Our work: Method: Compute what the best possible speed-up can be, so the question has a target. Result: Adding a single generator to a set of size 2 changes the walk on a graph of degree 3, and the diameter of any Cayley graph of S_n with 3 generators is at least log|S_n|/log 3 = c n log n, so no addition can bring the mixing... Obstruction: Proving a speed-up requires an upper bound for a walk whose generators have no common structure (a transposition, an n-cycle and one long permutation generate a group with... Verification: unreviewed.

### E0095. Best edge to add to a regular graph to speed up the random walk

Source: Diaconis: Some things we have learned (about Markov chain Monte Carlo) (diaconis_mcmc_learned_2013), Question 4, PDF p. 9.

Statement: One may ask the analogue of Question 3 for random walk on any graph: for a connected d-regular graph on an even number n of vertices, which edge (or perfect matching) should be added to best speed up the nearest-neighbour random walk?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on adding edges to minimise mixing time and on the Fiedler-value maximisation problem. The spectral-gap maximisation problem under edge addition is known to be NP-hard in general (Mosk-Aoyama and successors), and there is a substantial approximation literature; the probabilistic question of the typical gain was not found resolved.

Our work: Method: Compute the first-order effect of adding one edge on the spectral gap, since that is what governs the relaxation time. Result: Adding the edge {u,v} perturbs the Laplacian by the rank-one matrix (e_u - e_v)(e_u - e_v)^T, so first-order perturbation theory gives the change in the second eigenvalue as (phi(u) - phi(v))^2 divided by the appropriate normalisation, where phi is the Fiedler vector. So the optimal single edge, to... Obstruction: Choosing a matching rather than a single edge is a combinatorial optimisation with rank-n/2 perturbation, where first-order perturbation theory fails because the eigenvalue crossings cannot be ignored; the... Verification: unreviewed.

### E0096. Optimal delocalization bound for edge eigenvectors of Wigner matrices

Source: O'Rourke, Vu, Wang: Eigenvectors of random matrices, a survey (eigenvectors_survey_2016), Open question following Theorem 4.3, PDF p. 12.

Statement: For a Wigner matrix W with sub-gaussian atom variable, Theorem 4.1 gives ||v_i||_infinity = O(sqrt(log n / n)) in the bulk (delta n <= i <= (1-delta)n) but only O(log n / sqrt n) at the edge (i <= delta n or i >= (1-delta) n), while the matching lower bound of Theorem 4.3 is c sqrt(log n / n) for every i. Prove the optimal bound ||v_j||_infinity = O(sqrt(log n / n)) for ALL eigenvectors, including the edge case.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on optimal delocalization of edge eigenvectors of Wigner matrices. The bulk optimal bound (Vu-Wang and successors) is standard; edge delocalization has been improved in the Erdos-Schlein-Yau line and in later work on eigenvector moment flow, and I did not establish whether the sqrt(log n / n) edge bound has since been reached.

Our work: Method: Locate the source of the extra sqrt(log n) at the edge by tracking the resolvent identity that produces the bound. Result: The delocalization bound comes from the local law: |v_i(j)|^2 is controlled by eta times the imaginary part of the resolvent entry G_jj(E + i eta) at the spectral scale eta, and the optimal choice is eta of order 1/n in the bulk, where the density of states is... Obstruction: Level repulsion at the edge is known in distribution (Tracy-Widom) but not with the high-probability uniformity over all edge indices that a union bound requires; and the eigenvector... Verification: unreviewed.

### E0097. Universality of the limiting law of the largest eigenvector coordinate

Source: O'Rourke, Vu, Wang: Eigenvectors of random matrices, a survey (eigenvectors_survey_2016), Open question following the largest-coordinate results, PDF p. 12.

Statement: Is the limiting distribution of ||v_i||_infinity, the largest coordinate in absolute value of an eigenvector of a Wigner matrix, universal, or does it depend on the atom variables xi and zeta?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the distribution of the largest coordinate of Wigner eigenvectors and on eigenvector universality (the Bourgade-Yau eigenvector moment flow). The eigenvector moment flow gives universality of finitely many coordinates and of quadratic forms; the extreme order statistic over all n coordinates is a different object and I found no universality result for it.

Our work: Method: Compare with the Haar benchmark, since the conjectural answer is that the eigenvector behaves like a uniform point on the sphere. Result: For v uniform on the sphere, n ||v||_infinity^2 - log n converges to a Gumbel law, so the conjectured universal answer is Gumbel with the standard centring. The eigenvector moment flow proves universality of any FIXED number of coordinates, and a Gumbel limit for a maximum needs joint... Obstruction: The eigenvector moment flow's error in matching k coordinates grows with k, and the Poisson approximation for the maximum requires the errors to be uniform over all subsets... Verification: unreviewed.

### E0098. Universality of the limiting law of the smallest eigenvector coordinate

Source: O'Rourke, Vu, Wang: Eigenvectors of random matrices, a survey (eigenvectors_survey_2016), Open question following Corollary 4.8, PDF p. 13.

Statement: Is the limiting distribution of ||v_j(W)||_min, the smallest coordinate in absolute value of an eigenvector of a Wigner matrix, universal, or does it depend on the atom variables xi and zeta? Corollary 4.8 gives ||v_i(W)||_min of order 1/(n^{3/2} (log n)^{c}) with high probability, optimal up to logarithms.

Status: historical status source_says_open. Status search: Same search as E0097. Kept open.

Our work: Method: Compute the Haar benchmark for the minimum, which fixes the conjectural answer and the right normalisation. Result: For v uniform on S^{n-1} the coordinates are approximately independent N(0,1/n) variables, so the smallest absolute coordinate is of order 1/(n times sqrt(n)) = n^{-3/2} - matching Corollary 4.8 up to the logarithm - and n^{3/2} min_j |v_j| converges to an exponential law with rate sqrt(2/pi), since the... Obstruction: Universality at the origin is the hardest regime for the four-moment theorem, which matches moments and is therefore blind to the density at zero; a discrete atom variable... Verification: unreviewed.

### E0099. Concentration of extreme order statistics for eigenvectors with non-Gaussian entries

Source: O'Rourke, Vu, Wang: Eigenvectors of random matrices, a survey (eigenvectors_survey_2016), Open question following Corollary 5.4, PDF p. 15.

Statement: Theorem 2.10 gives, for v uniform on the sphere S^{n-1}, sub-Gaussian concentration at scale n^{-1/2} for both max and min over subsets S of size m of the partial norm ||v||_S. Extend Theorem 2.10 to eigenvectors of Wigner matrices with non-Gaussian entries.

Status: historical status source_says_open. Status search: Same search as E0097. Kept open.

Our work: Method: Ask what proof of Theorem 2.10 is being extended, since the technique determines what the extension needs. Result: Theorem 2.10 is a consequence of Gaussian concentration on the sphere: the map v -> max over |S| = m of ||v||_S is 1-Lipschitz, and Levy's isoperimetric inequality gives exp(-cnt^2). For an eigenvector of a Wigner matrix there is no ambient isoperimetry, but there is a substitute: the... Obstruction: Eigenvalue spacings in the bulk are of order 1/n with a positive probability of being much smaller, so the eigenvector is not uniformly Lipschitz in the entries and... Verification: unreviewed.

### E0100. The sigma-algebra generated by the limiting measure of a branching random walk

Source: On the boundary at infinity for branching random walk (brw_boundary_infinity_2022), Problem 4.1, PDF p. 9.

Statement: Characterise the sigma-algebra generated by the limiting measure W of a branching random walk on a nonamenable group. The source notes that the martingale limit W generates neither the tail sigma-algebra of the branching process nor that of the branching random walk, even in simple examples.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on the boundary of branching random walk on nonamenable groups and on the sigma-algebra generated by the limit measure. Candellero-Hutchcroft's paper is the source; I found no later characterisation.

Our work: Method: Bracket the sigma-algebra between two natural candidates and see what is lost at each inclusion. Result: W is measurable with respect to the tail of the branching random walk, and it dominates the tail of the underlying branching process only through the total mass. So sigma(W) sits between sigma(total mass) and the full tail. Obstruction: The equivalence relation described is generated by uncountably many rearrangements and need not be smooth, so the quotient may fail to be countably generated and the resulting sigma-algebra... Verification: unreviewed.

### E0101. When does the support of the limiting measure equal the accumulation set of the branching random walk?

Source: On the boundary at infinity for branching random walk (brw_boundary_infinity_2022), Problem 4.2, PDF p. 9.

Statement: Give conditions under which the support of the limiting measure W coincides almost surely with the set of accumulation points of the branching random walk B on the boundary. The source notes that most of the existing literature on the boundary behaviour of branching random walk studies the accumulation set rather than the measure.

Status: historical status source_says_open. Status search: Same search as E0100. Kept open.

Our work: Method: Compare the two objects directly: the accumulation set is a hitting-type limit and the support of W is a mass-type limit. Result: One inclusion is free: the support of W is contained in the accumulation set, because any boundary point carrying W-mass is approached by infinitely many particles. The reverse inclusion can fail exactly when a boundary direction is visited by infinitely many particles that nevertheless carry vanishing mass in... Obstruction: Biggins' criterion is available for branching random walk on the real line, where directions form a one-parameter family; on a hyperbolic group the directions form the boundary and... Verification: unreviewed.

### E0102. Fine properties of the limiting measure for branching random walk on a hyperbolic group

Source: On the boundary at infinity for branching random walk (brw_boundary_infinity_2022), Problem 4.3, PDF p. 9.

Statement: Study the fine properties of the limiting measure W for branching random walk on a hyperbolic group - for example, compute the Hausdorff dimension of the measure, or study its multifractal structure, mirroring what is known for the limit set.

Status: historical status source_says_open. Status search: Same search as E0100. Kept open.

Our work: Method: Predict the dimension from the two exponents that govern the model, since dimension of a limit measure is usually a ratio of a growth rate to a metric rate. Result: For branching random walk with mean offspring m and underlying walk of escape rate l (drift with respect to the word metric) on a hyperbolic group with boundary metric of parameter eps, the natural prediction, by the standard mass-distribution argument, is that W has Hausdorff dimension min{1, (log... Obstruction: The mass-distribution argument requires an upper bound on W of a ball of radius r that holds simultaneously for all balls, and W is not a Gibbs measure... Verification: unreviewed.

### E0103. Coverage asymptotics for the inertial Boolean model

Source: The mobile Boolean model: an overview and further results (mobile_boolean_2014), Open problem 1, PDF p. 18.

Statement: For the mobile Boolean model, study the coverage problem, i.e. the law of inf{t >= 0 : K contained in W(t)}, the first time a compact set K is entirely covered by the moving grains. For the Brownian Boolean model, and as the diameter of the region tends to infinity, the problem has been solved; what are the corresponding asymptotics for the INERTIAL cases, in which the grains move ballistically with random velocities?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on coverage times for mobile (dynamic) Boolean models with ballistic motion. The Brownian case (Kesidis-Konstantopoulos-Phoha and the detection literature) is standard; the inertial case was not found.

Our work: Method: Compare the two motions through the quantity that governs coverage - the expected measure of the uncovered set at time t - and see how the exponent changes. Result: For a Poisson field of intensity lambda with grains of radius r, a fixed point x is uncovered at time t with probability exp(-lambda E|swept region up to t|), so coverage times are governed by the expected swept volume. For Brownian grains in dimension d the swept volume... Obstruction: Coverage of a whole region, as opposed to a point, requires the uncovered set to be shown to break into asymptotically independent pieces; ballistic grains create long-range dependence... Verification: unreviewed.

### E0104. Comparison of detection times of two sets in the mobile Boolean model

Source: The mobile Boolean model: an overview and further results (mobile_boolean_2014), Open problem 2, PDF p. 18.

Statement: Let K_1 and K_2 be two sets (for example balls of radii r_1 and r_2) and let S_{K_1}, S_{K_2} be their detection times in the mobile Boolean model. Find the probability P(S_{K_1} < S_{K_2}).

Status: historical status source_says_open. Status search: Same search as E0103. Kept open. 2026-09-08: inertial case for balls settled by the capsule-union formula (E0104-A002); Brownian case open.

Our work: Method: Same capsule-union formula as E0105-A002 with two balls (radii r_1, r_2 at centres b_1, b_2): R_i = r_i + r, h = perpendicular offset of b_2 - b_1 from the track. Result: SETTLED for balls in the homogeneous inertial model: P(S_{K_1} < S_{K_2}) = P(S_{K_1} = 0 < S_{K_2}) + int_0^inf (d/dt Lambda)(u,u) exp(-Lambda(u,u)) du with Lambda the void exponent of the union of two parallel capsules. For the Brownian model the analogous statement needs the two-set Wiener sausage volume... Obstruction: Brownian case: joint Wiener sausage volume of two sets. (2 recorded attempts, E0104-A001-E0104-A002; latest reported.) Verification: unreviewed.

### E0105. Detection of a ball before a fixed point in the inertial Boolean model

Source: The mobile Boolean model: an overview and further results (mobile_boolean_2014), Open problem 3, PDF p. 18.

Statement: For the inertial Boolean model, find the distribution of the detection time of a ball before a fixed point is hit.

Status: historical status source_says_open. Status search: Same search as E0103. Kept open. 2026-09-08: exact law of tau via the joint law of (S_K,S_a) as a union-of-capsules void probability; validated by simulation. Attempt E0105-A002.

Our work: Method: Reduction: tau = inf{t: r0 B meets W(t), a not in W(t)} equals S_K on {S_K < S_a} and +infinity otherwise (W(t) is increasing), so the law of tau is a functional... Result: SETTLED for the homogeneous inertial model (the case the source itself solves for one ball): exact joint law of (S_K, S_a), hence the law of tau: an atom at 0 equal to exp(-lambda omega_d r^d) - exp(-Lambda(0,0)), a density (d/dt Lambda)(u,u) exp(-Lambda(u,u)) on (0,infinity), and an atom at... Obstruction: Non-homogeneous intensities give the source's 'laborious' integrals; the coverage problem (Open problem 1) and the stability problem (Open problem 5) are untouched. (2 recorded attempts, E0105-A001-E0105-A002; latest reported.) Verification: unreviewed.

### E0106. Stability of a spatial service system driven by the Brownian Boolean model

Source: The mobile Boolean model: an overview and further results (mobile_boolean_2014), Open problem 5, PDF p. 18.

Statement: Let Pi be an independent space-time Poisson process in R^d x R_+ of fixed intensity, whose points are interpreted as customers. The Brownian Boolean model is a space-time serving mechanism which clears points whenever it meets them. Find necessary and sufficient stability conditions. The source notes the connection to stability problems in queueing theory where the spatial dimension matters as much as the time dimension.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on stability of spatial queueing systems served by moving servers and on the greedy/Poisson matching literature (Foss, Baccelli, Sankararaman). Related stability results exist for spatial birth-and-death and for the 'Poisson matching' models; the specific Boolean-model server was not found.

Our work: Method: Do the rate balance, which for a spatial system is a comparison of two densities rather than two rates. Result: Customers arrive at space-time intensity nu per unit volume per unit time. A single Brownian grain of radius r clears, in time t, a region of expected volume equal to the Wiener sausage volume: of order 2 pi t / log t in d = 2 and c_d... Obstruction: The rate balance is only necessary; sufficiency needs a Lyapunov function for a measure-valued process, and the natural candidate (total number of unserved customers in a window) is... Verification: unreviewed.

### E0107. Existence and uniqueness of stationary measures for the local equation on sparse random graphs

Source: Interacting stochastic processes on sparse random graphs (sparse_graph_ips_2023), Section 5, Q1, PDF p. 22.

Statement: Can one establish general conditions for existence and uniqueness of stationary or invariant measures for the local equation - the autonomous reduced-dimension description of the marginal dynamics of an interacting particle system on a sparse random graph?

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on stationary measures of the local equation for interacting diffusions on sparse graphs (the Lacker-Ramanan-Wu programme). Existence and uniqueness results are known for specific models and for regular trees; a general theory was not found.

Our work: Method: Compare with the mean-field case, where existence and uniqueness for the nonlinear McKean-Vlasov equation is classical, and identify what the sparse case adds. Result: In the mean-field case the nonlinear equation's stationary measures are fixed points of a map on probability measures on the state space, and uniqueness follows from a contraction in Wasserstein distance under a smallness condition on the interaction. The local equation replaces that by a fixed-point problem on... Obstruction: The local equation is non-Markov in the root's state alone - it is a path-dependent equation involving conditional laws - so the fixed-point map acts on measures on... Verification: unreviewed.

### E0108. Large deviations for interacting particle systems on sparse random graphs

Source: Interacting stochastic processes on sparse random graphs (sparse_graph_ips_2023), Section 5, Q4, PDF p. 22.

Statement: Can one establish large deviation principles and concentration results for interacting particle systems on sparse random graphs? The source notes that such results are known for weakly interacting systems on complete and dense graphs.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on large deviations for interacting diffusions on sparse graphs. The dense/mean-field theory (Dawson-Gartner and successors) is classical; sparse-graph large deviations were not found beyond special cases.

Our work: Method: Ask what the rate function would be a functional of, since that determines whether a Dawson-Gartner argument can be adapted. Result: In the mean-field case the empirical measure is a sufficient statistic and the rate function is a relative entropy on path space. On a sparse graph the empirical measure loses the graph structure and the correct object is the empirical distribution of ROOTED NEIGHBOURHOOD-DECORATED paths, i.e. a measure... Obstruction: Bordenave-Caputo's rate function is for the STATIC neighbourhood distribution and is proved for specific graph ensembles; adding the dynamics multiplies the state space by path space, and the... Verification: unreviewed.

### E0109. Limit theorems for Nash equilibria of games on sparse interaction networks

Source: Interacting stochastic processes on sparse random graphs (sparse_graph_ips_2023), Section 5, Q6, PDF p. 23.

Statement: Can one establish limit theorems for Nash equilibria of games with a large number of agents in which the interaction network of agents is sparse rather than the complete graph? The source notes that recent work covers networks with diverging degrees, and that there are only a few works on graphs with uniformly bounded degree.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on graphon games and mean-field games on sparse graphs. The graphon-game literature covers dense networks; sparse (bounded-degree) mean-field games are treated in a few papers (Lacker-Soret and others) for specific structures.

Our work: Method: Ask what breaks when the degree stays bounded, by comparing with the graphon case. Result: In the dense case each agent's payoff depends on an average over a diverging number of neighbours, so a law of large numbers applies and the equilibrium condition becomes a fixed point against a deterministic aggregate - the mean-field game. With bounded degree the neighbour average does not... Obstruction: Fixed points on trees are computed by belief propagation, which converges only below the reconstruction threshold; above it, selecting the equilibrium that is the limit of the finite-graph... Verification: unreviewed.

### E0110. Dimension-linear relaxation time for generalized reflected Brownian motion

Source: Exponential ergodicity and convergence for generalized reflected Brownian motion (reflected_bm_ergodicity_2018), Conjecture 1.5, PDF p. 5.

Statement: Under the assumptions of Theorem 1.3, the generalized reflected Brownian motion GRBM(R, mu, Sigma, U) is uniformly exponentially ergodic with exponent of order 1/d: there exist W : R^d -> [1, infinity) and C > 0 such that ||P^t(x, .) - pi(.)||_{TV} <= W(x) exp(-C t / d). This would mean the relaxation time to global equilibrium is of order d for a class of GRBMs.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on dimension dependence of the relaxation time of reflected Brownian motion in a cone or orthant and on the O'Connell-Yor process. The source's own Theorem 1.3 gives exponential ergodicity without an explicit dimension dependence; I found no proof of the 1/d rate.

Our work: Method: Test the conjectured 1/d against the one case where the answer is computable, the free (unreflected) case with a confining drift, and against the geometry of the orthant. Result: For a d-dimensional Ornstein-Uhlenbeck process the relaxation time is the inverse of the smallest drift eigenvalue and is dimension-free, so a 1/d rate must come from the reflection, not the drift. The natural mechanism is that equilibration requires each of the d faces to be visited, and the... Obstruction: Resolving the discrepancy needs a lower bound on the relaxation time, and lower bounds for reflected diffusions in the orthant require a test function concentrated near one face... Verification: unreviewed.

### E0111. Free energy fluctuations of the Sherrington-Kirkpatrick model at the critical temperature

Source: Free energy fluctuations in SK and related spin glass models: a literature survey (sk_free_energy_survey_2025), Conjecture 2.4, PDF p. 11.

Statement: For the Sherrington-Kirkpatrick model at the critical value beta_c = 1, Var(F_N^{SK}(beta_c)) = (1/6) N^{-2} log N + O(N^{-2}) as N tends to infinity. The survey records as the best available progress the result of Chen and Lam giving Var(F_N(beta_c)) <= C(N^{-2}(log N)^2 + 1) and a companion statement.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 covered by the survey itself (fetched 2025-11 version), which states the conjecture and the state of the art. The bound available carries (log N)^2 where the conjecture has log N, and no matching lower bound of that order was reported.

Our work: Method: Locate the source of the log N by comparing with the two neighbouring regimes whose answers are known. Result: Above criticality the free energy fluctuation is of order N^{-1} with a Gaussian limit (Aizenman-Lebowitz-Ruelle), giving variance of order N^{-2} with no logarithm; the log N at beta_c must therefore come from the divergence of the high-temperature variance formula as beta approaches 1. In the ALR formula the... Obstruction: The truncation scale is set by the breakdown of the high-temperature expansion at beta = 1, which is exactly where the replica-symmetric solution becomes unstable; controlling it needs... Verification: unreviewed.

### E0112. Weak and strong disorder critical temperatures for directed Brownian polymers in a Poissonian environment

Source: Brownian polymers in Poissonian environment: a survey (brownian_polymers_poisson_2018), Conjecture 4.3.2, PDF p. 24.

Statement: For the directed Brownian polymer in a Poissonian environment, define the critical inverse temperatures beta_c^{+,dir} = sup{beta >= 0 : lim_t P[(W_t^{dir,beta})^{1/2}] > 0} and beta_c^{-,dir} = inf{beta >= 0 : lim_t P[(W_t^{dir,beta})^{1/2}] > 0}, the analogues of the weak/strong disorder transition. The survey formulates conjectures about these critical points for the directed model.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on weak and strong disorder for Brownian directed polymers in a Poissonian environment (Comets-Yoshida, Comets-Cosco). The existence of a single critical point and its coincidence with the L^1-L^2 threshold in high dimension is known in several lattice settings; the Poissonian Brownian version was not found resolved.

Our work: Method: Ask whether the two critical points can differ, since the conjecture is essentially that they coincide. Result: The normalised partition function W_t is a positive martingale, so its limit is either almost surely zero or has positive expectation, and the set of beta for which the limit is positive is an interval containing 0 by a standard monotonicity (Comets-Yoshida) argument. Hence beta_c^+ = beta_c^- automatically... Obstruction: The lattice proof couples environments at two temperatures through a monotone rearrangement of i.i.d. Verification: unreviewed.

### E0113. KPZ fluctuations for the free energy of the Brownian polymer in strong disorder

Source: Brownian polymers in Poissonian environment: a survey (brownian_polymers_poisson_2018), Conjecture 10.1.1, PDF p. 52.

Statement: For all nonzero beta, nu and r, there exists a constant sigma(beta, nu) such that (log Z_t - p(beta,nu) t) / (sigma(beta,nu) t^{1/3}) converges in law to the Tracy-Widom GOE distribution as t tends to infinity, in contrast with the weak disorder regime where the polymer is diffusive.

Status: historical status source_says_open. Status search: WebSearch 2026-09-08 on KPZ fluctuations for Brownian polymers in a Poissonian environment. The KPZ exponent and Tracy-Widom limits are proved for exactly solvable models (O'Connell-Yor, the semi-discrete polymer, the stochastic heat equation); the Poissonian Brownian polymer of the survey is not known to be integrable and no such result was found.

Our work: Method: Ask what integrability the known Tracy-Widom proofs use, and whether the Poissonian model has any of it. Result: Every proof of a Tracy-Widom limit for a positive-temperature polymer goes through an exact formula: a Whittaker measure (O'Connell-Yor), a Macdonald process (log-gamma), or the replica/Bethe-ansatz moment formula for the stochastic heat equation. The Poissonian Brownian polymer has a distinguishing feature that is worth stating: its environment is... Obstruction: For a Poisson environment the exponential moments of the environment are doubly exponential in beta, so E[Z_t^k] grows fast enough that the moment problem is indeterminate and no... Verification: unreviewed.

