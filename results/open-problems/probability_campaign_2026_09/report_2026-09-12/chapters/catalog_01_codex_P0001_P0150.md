## Catalog chapter 1: Codex campaign (Probability_1000_20h_20260906), P0001-P0150

This chapter covers rows P0001 through P0150 of the Codex 20-hour probability campaign ledger (problems.jsonl, attempts.jsonl, sources.jsonl in ~/Downloads/Probability_1000_20h_20260906). All 150 ids in the range are present in problems.jsonl; 148 of 150 are marked admitted. 66 rows (P0002 through P0066, and P0096) were revised in place in the ledger (a later line overwrote an earlier one for the same id); the corrected, later occurrence is reported for each such row and the count of revisions is noted in its entry. Result_status counts across the 150 rows: attempted_unsolved: 144, candidate_full_solution: 2, literature_counterexample_rederived: 1, literature_result_rederived_with_scope_correction: 1, partial_result: 2. Verification-level counts: author_checked_limited_argument: 62, author_checked_special_case_only: 2, candidate_under_author_and_literature_checks: 2, primary_statement_and_later_random_drift_checked: 1, primary_statement_checked: 73, primary_statement_checked_with_scope_caveat: 10. 150 of 150 rows have at least one recorded attempt in attempts.jsonl, and 4 rows carry a proof_file path. No CORRECTIONS.md file exists in the source directory; RESUME.md's correction notes concern higher-numbered rows (P0284, P0288, P0411, P0429 and the C00xx intake batch) and do not touch this range. As stated in the campaign's own README.md and STATUS.json, zero results in this ledger are independently reviewed; every verification level below is author_checked or weaker unless stated otherwise, and nothing here is a claim of publishable novelty.

### P0001. Negative correlation in uniform forests

**Source.** Selected problems in probability theory (grimmett_2022_selected), Conjecture 4.2, PDF page 8.

**Statement.** For every finite simple graph, does its uniform acyclic edge subset have pairwise nonpositive edge covariance?

**Status.** Historical status: source_says_open. Current-literature status: no_resolution_found_in_documented_search (searched 2026-09-06; evidence at https://arxiv.org/html/2603.10738v1, Conjecture 1.3; March 2026 primary paper still states general conjecture; later complete-graph results do not settle arbitrary graphs). Admission: admitted; result_status: partial_result.

**Our work.** Method: Condition independent weighted Bernoulli edges on acyclicity; factor disjoint cycle constraints in cactus graphs. Result: Complete author-checked proof of negative association for all finite cactus graphs and finite positive edge weights; target on arbitrary graphs remains unsolved here. Obstruction: Overlapping cycle constraints do not factor; generic conditioning on a decreasing event fails. Need an inequality using graphic-matroid circuit elimination.. Verification: author_checked. Artifact: proofs/P0001_cactus_forests.md. Proof file: proofs/P0001_cactus_forests.md.

### P0002. Self-avoiding-walk counting exponents

**Source.** Selected problems in probability theory (grimmett_2022_selected), Conjecture 2.1, PDF page 3 and footnote.

**Statement.** Determine the asymptotic correction to c_n=mu^n for lattice self-avoiding walks in dimensions two, three, and four.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Submultiplicativity and its limits. Result: On Z^d, splitting a walk gives c_(m+n)<=c_m c_n. Positive-coordinate walks give d^n<=c_n, and the nonbacktracking bound gives c_n<=2d(2d-1)^(n-1). Fekete determines the exponential growth rate. However a_n=mu^n exp(sqrt(n)) is submultiplicative and has no fixed polynomial prefactor.. Obstruction: Submultiplicativity cannot determine the critical exponent or the dimension-four logarithmic correction.. Verification: author_checked_limited_argument. No proof file recorded.

### P0003. Hexagonal self-avoiding-walk scaling limit

**Source.** Selected problems in probability theory (grimmett_2022_selected), Question 2.2, PDF page 3.

**Statement.** Does the rescaled uniform n-step hexagonal-lattice self-avoiding walk converge to SLE_(8/3)?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exact finite-domain conditional law. Result: For a finite-graph a-to-b self-avoiding path with weight z^length, condition on an initial simple prefix. The remaining path has the same fugacity law on the graph with earlier prefix vertices removed. The factor z^prefix_length cancels between numerator and partition function.. Obstruction: This domain Markov property supplies neither tightness nor conformal invariance and does not identify an SLE scaling limit.. Verification: author_checked_limited_argument. No proof file recorded.

### P0004. Existence of the quenched connective limit

**Source.** Selected problems in probability theory (grimmett_2022_selected), Question 2.3, PDF pages 3-4.

**Statement.** On the infinite supercritical bond-percolation cluster of Z^2, does c_n(v)^(1/n) converge almost surely, independently of v?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: partial_result. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Adjacent-root walk decomposition and a Markov/Borel-Cantelli bound. Result: Root-independent limsup on every infinite connected bounded-degree graph; annealed upper bound p mu. Obstruction: The cut-walk inequality has an environment-dependent endpoint maximum. No stationary scalar subadditive process or liminf lower bound was obtained.. Verification: author_checked. Artifact: proofs/P0004_quenched_limsup.md. Proof file: proofs/P0004_quenched_limsup.md.

### P0005. Ehrenfest mirror escape

**Source.** Selected problems in probability theory (grimmett_2022_selected), Question 3.1, PDF pages 4-5.

**Statement.** Which mirror densities p give positive escape probability in the square-lattice model with equally likely NE/NW mirrors?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Invertible routing and finite-volume diagnostics. Result: The local mirror pairings define an invertible map on oriented light states. Its orbits are cycles or bi-infinite trajectories. On a finite periodic torus every orbit is a cycle. A mirror-free initial straight run of N sites has probability (1-p)^N.. Obstruction: Finite periodic loop counts cannot decide infinite-volume escape; the N-to-infinity and p-to-zero limits cannot be interchanged from this bound.. Verification: author_checked_limited_argument. No proof file recorded.

### P0006. Poisson mirror escape threshold

**Source.** Selected problems in probability theory (grimmett_2022_selected), Question 3.2(a-c), PDF pages 5-6.

**Statement.** For nondegenerate Poisson-mirror orientation laws, characterize escape below the vacant-set threshold, including uniform orientations.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exact first-collision distribution for Poisson mirrors. Result: For a straight test ray segment of length L in direction alpha and mirrors of total length epsilon with orientation law mu, the centers whose mirror crosses the segment form a parallelogram of area epsilon L |sin(alpha-beta)| for angle beta. Unit-intensity marked Poisson counting gives no-collision probability exp(-epsilon L integral |sin(alpha-beta)| mu(dbeta)). Thus the first free flight is exponential whenever this rate is positive.. Obstruction: After reflection, previously examined empty regions and previously hit mirrors make the flight history dependent. The first-flight computation gives no independent-flight construction or escape threshold.. Verification: author_checked_limited_argument. No proof file recorded.

### P0007. Unbounded mirror component trapping every ray

**Source.** Selected problems in probability theory (grimmett_2022_selected), Question 3.3, PDF page 6.

**Statement.** Can an unbounded component of a mirror complement contain an origin from which every reflected ray stays bounded?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Attempted reduction to straight visibility. Result: An unbounded unobstructed straight ray from the origin immediately rules out the proposed all-directions trapped configuration. However an unbounded connected planar open set need not contain any unbounded straight ray: a sufficiently narrow unbounded spiral corridor is a topological counterexample to that inference.. Obstruction: Unboundedness of the vacant component gives a continuous route, not a realizable billiard route. No mirror configuration trapping all angles, or theorem preventing one, was constructed.. Verification: author_checked_limited_argument. No proof file recorded.

### P0008. Diffusive Poisson mirror trajectories

**Source.** Selected problems in probability theory (grimmett_2022_selected), Question 3.4, PDF page 7.

**Statement.** For rationally supported nondegenerate mirror orientations, do escaping trajectories have finite positive diffusivity and a Gaussian limit?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Green-Kubo variance and a failed CLT shortcut. Result: For a stationary mean-zero scalar velocity with integrable covariance C(s), Var(integral_0^t V_s ds)/t = 2 integral_0^t (1-s/t) C(s) ds tends to 2 integral_0^infinity C(s) ds. Covariance control alone does not imply a Gaussian limit: let Y_i=A epsilon_i with independent fair signs and independent A equal to 1 or 2 with probability 1/2. Distinct increments are uncorrelated, but n^(-1/2) sum Y_i converges to the equally weighted mixture of N(0,1) and N(0,4).. Obstruction: Need mixing or a martingale approximation for the billiard environment, including the effect of conditioning on an unbounded trajectory.. Verification: author_checked_limited_argument. No proof file recorded.

### P0009. Manhattan pinball localization

**Source.** Selected problems in probability theory (grimmett_2022_selected), Question 3.5, PDF page 7; model Figure 3.2.

**Statement.** Does every positive mirror density localize the Manhattan-oriented pinball trajectory?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Small-density straight paths and lack of an order argument. Result: At q=0 a ray moves indefinitely along its Manhattan street. The event that its first N potential collisions contain no mirror has probability (1-q)^N. This only controls a finite initial flight and gives no positive lower bound as N increases at fixed q.. Obstruction: The known localization interval near and above one-half cannot be extended to every q>0 using this finite-run bound or an unproved monotonicity assumption.. Verification: author_checked_limited_argument. No proof file recorded.

### P0010. Biased random square-lattice orientations

**Source.** Selected problems in probability theory (grimmett_2022_selected), Question 5.1, PDF page 9.

**Statement.** Does every nonzero orientation bias give positive probability of an infinite directed path from the origin?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Directed-percolation subgraph comparison. Result: Reflecting both coordinate axes maps p to 1-p, so the infinite-path probability is symmetric about one-half. North-east paths use independent edges pointing north/east with probability p; survival of the usual north-east directed percolation therefore implies survival in the full oriented graph. The p=0 and p=1 endpoints have deterministic infinite paths.. Obstruction: It does not settle the interval between one-half and that threshold. The critical p=1/2 result does not extend by continuity alone.. Verification: author_checked_limited_argument. No proof file recorded.

### P0011. Brownian SIR survival in dimensions at least two

**Source.** Selected problems in probability theory (grimmett_2022_selected), Question 6.1(ii), PDF pages 9-10.

**Statement.** Does the fully diffusing Poisson Brownian SIR model survive for sufficiently small positive removal rate when d>=2?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Counterexample to the usual pathwise lifetime monotonicity coupling. Result: Consider a deterministic contact schedule with A initially infected: A-C at time .1, A-B at 1, C-B at 9, B-D at 10, and no other contacts. Baseline infectious lifetimes are L_A=.5, L_C=12, L_B=2. Then B is infected at 9 and infects D at 10. Multiply every lifetime by 3: A now infects B at 1; B is removed at 7, cannot be reinfected at 9, and D is never infected.. Obstruction: This is not a counterexample to survival monotonicity or to the Brownian epidemic conjecture. It blocks a direct attractiveness proof; a Brownian contact-support realization was not proved.. Verification: author_checked_limited_argument. No proof file recorded.

### P0012. Gaussian tensor type-2 bound

**Source.** Randomstrasse101: Open Problems of 2025 (randomstrasse_2025_v1), Conjecture 16, Entry 8.

**Statement.** For symmetric order-r tensors T_i on R^d, p>=2 and independent standard Gaussians g_i, is E||sum_i g_i T_i||_(I_p) bounded by polylog(d,n) times O_(r,p)(d^(1/2-1/p) sqrt(sum_i ||T_i||_(I_p)^2))?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Diagonal-tensor Gaussian estimate. Result: For a diagonal homogeneous form T(x)=sum_j a_j x_j^r and 2<=p<=r, its supremum over the l_p unit ball is max_j |a_j|. Indeed sum |x_j|^r<=1 and a coordinate vector attains the maximum. For independent standard g_i, each diagonal coefficient of sum_i g_i T_i has variance at most sum_i ||T_i||^2, so the Gaussian maximum bound gives E||sum_i g_i T_i|| <= sqrt(2 log(2d)) (sum_i ||T_i||^2)^(1/2).. Obstruction: This verifies a restricted diagonal family. Off-diagonal terms and the full p range require the tensor geometry absent here.. Verification: author_checked_limited_argument. No proof file recorded.

### P0013. Expected Lovasz theta of a dense independent-edge graph

**Source.** Randomstrasse101: Open Problems of 2025 (randomstrasse_2025_v1), Conjecture 17, Entry 9.

**Statement.** For G distributed as G(n,1/2), is E theta(G)=(1+o(1)) sqrt(n)?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Complement symmetry and uniform-integrability obstruction. Result: The theta product inequality theta(G) theta(complement G)>=n and complement symmetry of G(n,1/2) give E theta>=sqrt(n) by arithmetic-geometric mean. A proof of concentration on a logarithmic scale would still need tail control: set Z_n to plus or minus (log n)/2, each with probability 1/(2 sqrt(n)), and zero otherwise. Then Z_n tends to zero in probability and variance, but E exp(Z_n) tends to 3/2.. Obstruction: Need a sharp upper bound and uniform integrability at the sqrt(n) scale; complement symmetry only yields the lower bound.. Verification: author_checked_limited_argument. No proof file recorded.

### P0014. Expected Lovasz theta of a random circulant graph

**Source.** Randomstrasse101: Open Problems of 2025 (randomstrasse_2025_v1), Conjecture 18, Entry 9.

**Statement.** For the graph on Z/nZ formed by independently including each unordered nonzero generator pair {k,-k} with probability 1/2, is E theta(G)=(1+o(1)) sqrt(n)?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Vertex-transitive complement identity. Result: A circulant graph is vertex transitive, so theta(G) theta(complement G)=n. Its random model is complement invariant. For Z=log(theta(G)/sqrt(n)), Z has the law of -Z and E theta/sqrt(n)=E cosh Z. The conjecture is therefore equivalent to E(cosh Z-1) tending to zero.. Obstruction: Must estimate the exponential tails of the logarithmic theta fluctuation for the dependent circulant adjacency structure.. Verification: author_checked_limited_argument. No proof file recorded.

### P0015. Random complex phase-retrieval injectivity at 4M-5 measurements

**Source.** Randomstrasse101: Open Problems of 2025 (randomstrasse_2025_v1), Conjecture 19(a,b), Entry 10.

**Statement.** Let p_M be the probability that a complex Gaussian (4M-5)-by-M matrix gives an injective phaseless measurement map modulo global phase. Is p_M<1 for each meaningful M, and does p_M tend to zero?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Complete M=2 obstruction via Hermitian lifting. Result: For M=2 the matrix has three complex Gaussian rows. Almost surely these span C^2. The real-linear measurement map from the four-dimensional Hermitian 2-by-2 space to R^3 has a nonzero kernel element H. H cannot be positive or negative semidefinite: a_i^* H a_i=0 for a spanning set would force H=0. Thus H has one positive and one negative eigenvalue and can be written xx^*-yy^* with noncollinear x,y. Their three intensity measurements agree. Hence p_2=0.. Obstruction: For M>2 a nonzero kernel matrix need not have rank at most two with one eigenvalue of each sign. The requisite low-rank intersection probability remains unresolved.. Verification: author_checked_limited_argument. No proof file recorded.

### P0016. Worst square-submatrix conditioning in a Gaussian frame

**Source.** Randomstrasse101: Open Problems of 2025 (randomstrasse_2025_v1), Open Problem 21 and Definition 10.1, Entry 10.

**Statement.** For a (2M-1)-by-M matrix of independent standard real Gaussians, determine the asymptotic size of omega(A), the minimum smallest singular value over row subsets whose complement has rank below M. In particular determine whether its decay is exponential and identify the exponential rate.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Union small-ball lower bound and one-normal upper bound. Result: For a standard M-by-M real Gaussian matrix A, sigma_min(A)<=t implies that some column has distance at most sqrt(M)t from the span of the other columns: project a minimizing unit vector equation using a coordinate of magnitude at least 1/sqrt(M). Each such distance has the law |N(0,1)|, so P(sigma_min<=t)<=sqrt(2/pi) M^(3/2)t. There are at most 4^M M-row submatrices of a (2M-1)-by-M frame. Therefore its minimum omega exceeds exp(-(log 4+epsilon)M) with probability tending to one. Conversely fix M-1 rows and a unit normal u. The M remaining row projections are independent N(0,1), and omega is at most their minimum absolute value, giving omega<=C log(M)/M with probability tending to one for sufficiently large C.. Obstruction: The exponential lower bound and polynomial upper bound are far apart. Sharp extremes of the strongly dependent minors remain uncontrolled.. Verification: author_checked_limited_argument. No proof file recorded.

### P0017. Dimension-free log-concave Poincare or Cheeger constant

**Source.** Randomstrasse101: Open Problems of 2025 (randomstrasse_2025_v1), Conjecture 30, Entry 13.

**Statement.** Is there a universal positive lower bound for the Euclidean Cheeger constant of every isotropic log-concave probability measure, in every dimension?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Gaussian special case by orthogonal expansion. Result: For standard Gaussian measure, expand a polynomial f in orthonormal multivariate Hermite polynomials with coefficients a_alpha. Then Var(f)=sum_(|alpha|>=1) a_alpha^2 <= sum |alpha| a_alpha^2 = E||gradient f||^2. Closure in Gaussian Sobolev norm extends the inequality to its natural domain.. Obstruction: A general isotropic log-concave measure lacks this diagonal Hermite generator. This special case does not prove its uniform Poincare or Cheeger bound.. Verification: author_checked_limited_argument. No proof file recorded.

### P0018. Sharp polynomial-logarithmic expected norm of graph matrices

**Source.** Randomstrasse101: Open Problems of 2025 (randomstrasse_2025_v1), Conjecture 31 and Definition 14.2, Entry 14.

**Statement.** For each fixed graph shape alpha with specified left and right index sets, form M_alpha by summing injective labelings with products of independent Rademacher edge variables. Must E||M_alpha|| be Theta(n^f(alpha) (log n)^g(alpha)) for some shape-dependent exponents?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Moment expansion with a crude operator-norm bound. Result: For every finite random graph matrix, E||M|| <= (E||M||_F^2)^(1/2). Expanding each entry as a sum of Rademacher edge monomials, cross terms vanish unless the two monomials use every edge with even combined multiplicity. For a fixed shape the remaining label identifications can be counted to obtain a polynomial upper bound in n.. Obstruction: The Frobenius bound can lose powers of n and cannot decide the sharp operator norm or the existence of one power-log asymptotic form.. Verification: author_checked_limited_argument. No proof file recorded.

### P0019. Brownian exit approach directions in higher dimensions

**Source.** Krzysztof Burdzy: My favorite open problems (burdzy_open_20260906), Problem 1.

**Statement.** For Brownian motion exiting a domain in dimension d>2, is the set of limiting approach directions at the exit point almost surely a sphere or a hemisphere?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Smooth-boundary directional containment. Result: At an exit point z where the domain boundary is C^1 with outward unit normal n, local differentiability gives n dot (z-x)>=-o(|z-x|) for x in the domain approaching z. Thus every limit of (z-B_s)/|z-B_s| as s increases to the exit time lies in the closed hemisphere {u:n dot u>=0}.. Obstruction: Containment does not prove that all hemisphere directions occur, and there is no supporting tangent half-space at the arbitrary boundaries in the full question.. Verification: author_checked_limited_argument. No proof file recorded.

### P0020. Finite-crossing arcs through a planar Brownian trace

**Source.** Krzysztof Burdzy: My favorite open problems (burdzy_open_20260906), Problem 2(i).

**Statement.** Almost surely, can every two points outside the trace of planar Brownian motion on [0,1] be connected by a Jordan arc meeting the trace at only finitely many points?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Reduction to component adjacency and access. Result: If both endpoints lie in the same component of the complement of the Brownian trace, an open connected planar set is polygonally connected; removing loops gives a simple arc avoiding the trace entirely. If an arc crosses the trace finitely many times, its complementary intervals give a finite sequence of complement components with touching closures at successive crossing points.. Obstruction: Need finite accessible chains for every pair of components, simultaneously for the Brownian trace.. Verification: author_checked_limited_argument. No proof file recorded.

### P0021. Interior remainder of planar Brownian trace

**Source.** Krzysztof Burdzy: My favorite open problems (burdzy_open_20260906), Problem 2(ii).

**Statement.** Delete from a planar Brownian trace on [0,1] all boundaries of connected components of its complement. Is the remaining set totally disconnected almost surely?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Failure of transferring total disconnectedness through the path map. Result: A possible approach is to identify a totally disconnected set of Brownian times surviving boundary removal. That would not suffice: the Cantor function restricted to the middle-third Cantor set maps this totally disconnected compact set continuously onto [0,1]. Continuous images can be connected.. Obstruction: The spatial remainder needs direct Brownian geometry. Showing it contains no simple arc would also be weaker than showing every connected component is a singleton.. Verification: author_checked_limited_argument. No proof file recorded.

### P0022. Percolation dimension of a planar Brownian trace

**Source.** Krzysztof Burdzy: My favorite open problems (burdzy_open_20260906), Problem 3.

**Statement.** Is the infimum of Hausdorff dimensions of nontrivial Jordan arcs contained in a planar Brownian trace on [0,1] equal to one almost surely?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Universal dimension lower bound for connecting sets. Result: Any connected set containing distinct x and y has Hausdorff dimension at least one. Orthogonal projection onto their joining line is Lipschitz and has connected image containing the interval between the projections, so its dimension is at least one.. Obstruction: Polygonal approximations of a Brownian path are not subsets of its trace. The missing step is constructing sufficiently thin connecting subsets inside the trace itself.. Verification: author_checked_limited_argument. No proof file recorded.

### P0023. Efficient reflected-Brownian coupling in acute triangles

**Source.** Krzysztof Burdzy: My favorite open problems (burdzy_open_20260906), Problem 4.

**Statement.** In any acute triangle, can reflected Brownian motions from distinct starting points be coupled so their meeting-time tail decays at every exponential rate strictly below the first positive Neumann spectral rate?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Spectral lower bound on coupling tails. Result: Let phi be a bounded nonconstant Neumann eigenfunction with semigroup P_t phi=e^(-lambda t) phi. For any coalescent coupling with meeting time T, |P_t phi(x)-P_t phi(y)|<=2||phi||_infinity P(T>t). Choosing phi(x)!=phi(y) yields P(T>t)>=c e^(-lambda t).. Obstruction: This proves that the spectral rate is an upper limit on coupling efficiency, but gives no coupling attaining arbitrarily close to that rate in an acute triangle.. Verification: author_checked_limited_argument. No proof file recorded.

### P0024. Failure of synchronous contraction in a bounded planar domain

**Source.** Krzysztof Burdzy: My favorite open problems (burdzy_open_20260906), Problem 5(i).

**Statement.** Does some bounded connected smooth planar domain admit synchronously coupled reflected Brownian motions whose distance has positive limsup with positive probability?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Synchronous contraction on convex domains. Result: For two reflected motions driven by the same Brownian path, the noise cancels in their difference. With inward normals, d|X-Y|^2=2<X-Y,n(X)>dL_X-2<X-Y,n(Y)>dL_Y. Convexity makes both contributions nonpositive, so the distance is nonincreasing.. Obstruction: Nonincrease alone does not prove convergence to zero. Nonconvex domains can have both signs and require control of the long-run reflection geometry.. Verification: author_checked_limited_argument. No proof file recorded.

### P0025. Synchronous reflection outside a disk

**Source.** Krzysztof Burdzy: My favorite open problems (burdzy_open_20260906), Problem 5(ii).

**Statement.** For synchronously coupled reflected Brownian motions in the exterior of a nondegenerate closed disk, can their distance have positive limsup with positive probability?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exterior-disk reflection has both distance signs. Result: At x=(R,0) on the inner circular boundary of the exterior domain, its inward-to-domain normal is (1,0). For y=(r,0), r>R, <x-y,n>=R-r<0; for y=(-r,0) it is R+r>0. Hence a reflection at X can either shrink or enlarge the synchronous separation.. Obstruction: A global monotone-distance proof is unavailable. The question turns on boundary occupation and angular correlations over indefinitely long times.. Verification: author_checked_limited_argument. No proof file recorded.

### P0026. Non-explosion of Fleming-Viot Brownian particles in arbitrary domains

**Source.** Krzysztof Burdzy: My favorite open problems (burdzy_open_20260906), Problem 6 with 2024 update.

**Statement.** For N>=3 Brownian particles in any bounded open connected domain, killed at the boundary and immediately cloned from a uniformly selected survivor, are the successive death times almost surely non-accumulating?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Attempted boundary-distance Lyapunov proof. Result: The candidate Lyapunov function -sum_i log dist(X_i,boundary D) becomes singular when particles approach the boundary, but an Ito argument needs derivative bounds. Even for a smooth domain, the distance is nonsmooth on its medial set; for arbitrary domains there may be no uniformly controlled smooth substitute. At a cloning event another particle may be still closer to the boundary, so the jump is not uniformly favorable.. Obstruction: No Lyapunov drift bound uniform over arbitrary boundary geometry and all cloning configurations was obtained.. Verification: author_checked_limited_argument. No proof file recorded.

### P0027. Rigidity of shy reflected-Brownian couplings

**Source.** Krzysztof Burdzy: My favorite open problems (burdzy_open_20260906), Problem 7.

**Statement.** If reflected Brownian motions in a bounded connected domain can remain a positive distance apart forever with positive probability, must there be such a coupling with one path a fixed deterministic function of the other at each time?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Explicit deterministic shy coupling on an annulus. Result: If an isometry F preserves a reflected-Brownian domain and has inf_x |x-F(x)|>0, take Y_t=F(X_t). Orthogonal transformation of Brownian noise and equivariance of inward reflection show Y has the correct reflected law, while separation stays positive. On R<|x|<R_out, F(x)=-x yields |X_t-Y_t|>=2R.. Obstruction: This verifies a nonempty deterministic class. It does not turn an arbitrary shy coupling into a single state map with the required path consistency.. Verification: author_checked_limited_argument. No proof file recorded.

### P0028. Bounded independent Brownian pieces and two-sided Brownian motion

**Source.** Krzysztof Burdzy: My favorite open problems (burdzy_open_20260906), Problem 8; compare Burdzy-Scheutzow (2014) Problem 7.7.

**Statement.** Concatenate independent Brownian path segments cut at stopping times indexed by all integers, with lengths uniformly bounded by a deterministic constant and divergent sums in both directions. Is the resulting path two-sided Brownian after some random time shift?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** [attempt 1 of 2] Method: Stationary Palm construction in the identically distributed finite-mean case. Result: For iid stopped Brownian segments with 0<E T<infinity, the cycle sequence is ergodic under shifting its index. A stationary occupation law is Q(F)=E[integral_0^T F(theta_s X) ds]/E T. Shifting by t changes the numerator by E[integral_T^(T+t) F(theta_s X) ds-integral_0^t F(theta_s X) ds]=0 because the concatenation rooted at the next cycle has the same Palm law. Tilting the iid cycle sequence by T_0/E T and choosing a uniform time in that cycle realizes this law; the forward filling lemma supplies that tilt by a finite randomized index shift.. Obstruction: The actual question allows independent non-identically distributed segments. There is then no invariant iid index law or common Palm mean to which this argument applies.. Verification: author_checked_limited_argument. [attempt 2 of 2] Method: Primary-source check of the iid finite-mean reduction. Result: Burdzy-Scheutzow (2014), Theorem 5.1 explicitly proves that strongly decomposable processes with finite mean segment length are two-sided Brownian motions. P0028-A001 rederives this known special case and is not a novel solution.. Obstruction: The independent non-identically distributed bounded-length question remains unresolved here.. Verification: source_theorem_checked. No proof file recorded.

### P0029. Separation of two peaks in random square-grid labelings

**Source.** Krzysztof Burdzy: My favorite open problems (burdzy_open_20260906), Problem 9.

**Statement.** Uniformly label an n-by-n square grid and condition on exactly two local maxima. Does their graph distance divided by n converge in distribution to zero?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exact small-grid count and an orientation reformulation. Result: On the 2-by-2 grid (a four-cycle), exactly two peaks must be opposite and carry labels 3 and 4. There are two choices of diagonal, two orders of the top labels, and two orders of the bottom labels: eight of the 24 labelings. Their graph distance is always two. More generally orient each edge toward its larger label. Two peaks means precisely two sinks of the induced acyclic orientation; the number of labelings yielding a fixed orientation is its number of linear extensions.. Obstruction: The small-grid calculation gives no large-n scale. The orientation sum requires sharp weighted counts of acyclic orientations with two prescribed sinks. The source title says repel while its displayed question asks distance/n -> 0; that wording discrepancy is retained, not silently corrected.. Verification: author_checked_limited_argument. No proof file recorded.

### P0030. Compatibility of forward and backward Brownian decompositions

**Source.** Forward Brownian motion (burdzy_scheutzow_2014), Problems 7.1-7.3, PDF pages 25-26.

**Statement.** Does a decomposable forward Brownian motion which is also backward Brownian necessarily become two-sided Brownian after a random shift? The source also asks weaker related formulations using independence of past and future at a random time.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Common-splice compatibility obstruction. Result: Two independent standard Brownian half-paths attached at the same deterministic time give a two-sided Brownian motion. For a general process certified separately as forward and backward Brownian, the certifying random times can differ. Moving either certificate to another random time can bias its marginal law, as the selection-density calculation in P0032 demonstrates.. Obstruction: No construction aligns both certificates at one time while preserving both marginal laws and their independence.. Verification: author_checked_limited_argument. No proof file recorded.

### P0031. Sparse first-passage pieces in a forward Brownian concatenation

**Source.** Forward Brownian motion (burdzy_scheutzow_2014), Problem 7.4, PDF page 26.

**Statement.** In a two-sided independent concatenation, use unit-length Brownian segments except at increasingly rare negative-time indices where segments stop on first hitting -1. Characterize frequencies giving backward or two-sided Brownian motion.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Sparse exceptional hitting-time clock estimate. Result: For a standard Brownian first hitting time tau of -1, reflection gives P(tau>t)=2 Phi(1/sqrt(t))-1 ~ sqrt(2/pi)t^(-1/2), hence E tau=infinity. If exceptional segment indices are 2^k, then sum_k P(tau_k>epsilon 2^k)<infinity. Borel-Cantelli yields tau_k/2^k ->0 almost surely. Splitting the sum into finitely many early terms and a geometrically weighted tail gives sum_(k<=K) tau_k/2^K ->0.. Obstruction: A negligible exceptional time fraction is an asymptotic statement; it does not construct an exact backward Brownian law after a finite random shift. The full frequency classification remains open here.. Verification: author_checked_limited_argument. No proof file recorded.

### P0032. Embedding an equivalent Brownian law by adding a finite prefix

**Source.** Forward Brownian motion (burdzy_scheutzow_2014), Problem 7.5, PDF page 26.

**Statement.** Given a process whose law on nonnegative time is equivalent to Wiener measure, can a random finite prefix be added, on an enlarged probability space if necessary, to produce a process with Wiener law?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: candidate_full_solution. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Forward density matching on the ergodic two-sided Wiener shift. Result: Complete candidate construction of a finite nonnegative integer prefix time for any suffix law absolutely continuous with respect to Wiener measure. Obstruction: No mathematical gap currently identified under the stated interpretation; source interpretation, measurability details, and earlier filling/embedding literature still under review. Verification: candidate_under_author_and_literature_checks. Artifact: proofs/P0032_brownian_prefix_candidate.md. Proof file: proofs/P0032_brownian_prefix_candidate.md.

### P0033. Ergodicity of stationary Galton-Watson flows

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 17.18, printed p.575, PDF p.592.

**Statement.** If a consistent equivariant Borel flow rule has a stationary probability measure equivalent to Galton-Watson law, must the associated subtree Markov chain be ergodic?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: candidate_full_solution. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Endogenous AND/OR tree coloring and conditional subtree selection. Result: Candidate counterexample: GW itself stationary, with two invariant color classes of mass one half. Obstruction: No mathematical gap currently identified; full author recheck and prior tree-automaton literature pending. Verification: candidate_under_author_and_literature_checks. Artifact: proofs/P0033_stationary_flow_counterexample_candidate.md. Proof file: proofs/P0033_stationary_flow_counterexample_candidate.md.

### P0034. Recurrence of the planar horizontal-new vertical-old walk

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 2.27, printed p.56.

**Statement.** Start at the origin in Z^2; after first visiting a site step horizontally with either sign equally likely, and after a repeat visit step vertically with either sign equally likely. Does any site receive infinitely many visits with positive probability?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Martingale estimates for the axis-switching walk. Result: The axis of the next step is predictable from the past, while its sign is fair. Both coordinates are martingales, their cross quadratic covariation is zero, and E|X_n|^2=n. Bounded increments and Azuma give summable bounds for P(|X_n|>epsilon n), so X_n/n tends to zero almost surely.. Obstruction: Zero speed and a diffusive second moment do not imply recurrence. The occupation-dependent balance of the two coordinate clocks remains uncontrolled.. Verification: author_checked_limited_argument. No proof file recorded.

### P0035. Positive speed of inward-biased walks below the Cayley growth rate

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 3.11, printed p.91.

**Statement.** For a Cayley graph of exponential growth rate b and 1<lambda<b, does the distance from the identity divided by time for RW_lambda converge almost surely to a strictly positive speed?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exact radial speed on a regular tree. Result: On the (b+1)-regular rooted tree, away from the root the radial walk steps out with probability b/(b+lambda) and in with probability lambda/(b+lambda). For lambda<b its speed is (b-lambda)/(b+lambda)>0: the root is visited finitely often and the bounded-difference martingale law of large numbers applies to the radial drift.. Obstruction: General Cayley graphs have dead ends and nonuniform distance-level neighborhoods. Transience alone does not control time spent in traps.. Verification: author_checked_limited_argument. No proof file recorded.

### P0036. Percolation threshold on arbitrary geodesic Cayley spanning trees

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 3.12, printed p.91.

**Statement.** If T is any geodesic spanning tree rooted at the identity of a Cayley graph of growth rate b, must br(T)=b, equivalently must its Bernoulli bond percolation threshold be 1/b?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Equal level growth does not determine branching number. Result: A geodesic spanning tree has exactly the Cayley graph sphere sizes at each level. But growth can exceed branching number for a bounded-degree tree: take a single infinite spine and at its nth vertex attach a finite b-ary tree of height n. Its level sizes have exponential rate sqrt(b)>1, while its only infinite ray is the spine and arbitrarily deep singleton cutsets give branching number one.. Obstruction: This is not a geodesic Cayley spanning-tree counterexample. It proves that matching sphere counts alone cannot establish the conjectured branching number.. Verification: author_checked_limited_argument. No proof file recorded.

### P0037. BK disjoint occurrence for weighted uniform spanning trees

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjecture 4.10, printed p.125.

**Statement.** For increasing events A,B on edge subsets, is the probability of their disjoint occurrence under any weighted uniform spanning-tree law at most P(A)P(B)?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: BK for fixed conjunctions and a nonincreasing-event obstruction. Result: For disjoint fixed edge sets F and H, the spanning-tree determinantal formula and Hadamard-Fischer inequality give P(F union H subset T)<=P(F subset T)P(H subset T). Thus fixed increasing conjunctions obey the desired inequality. The increasing condition matters: on a triangle, A={e in T} and B={f not in T}, e!=f, have disjoint coordinate witnesses but P(A intersection B)=1/3>2/9=P(A)P(B).. Obstruction: General increasing disjoint occurrence is a union over adaptive witnesses. A fixed-coordinate negative-association inequality cannot simply be applied after that union.. Verification: author_checked_limited_argument. No proof file recorded.

### P0038. Transience preserved in Cayley percolation clusters

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjecture 6.44, printed p.216.

**Statement.** Is every infinite Bernoulli percolation cluster on a transient Cayley graph almost surely transient?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Percolation on regular trees. Result: For bond percolation on the (b+1)-regular tree, descendants of a nonroot vertex form a Galton-Watson process with Binomial(b,p) offspring. Conditional on survival when bp>1, its branching number is bp almost surely, so the electrical-network branching-number criterion gives transience.. Obstruction: The reduction uses independent descendant trees and does not extend to clusters with overlapping paths in a general transient Cayley graph.. Verification: author_checked_limited_argument. No proof file recorded.

### P0039. Positive-speed equivalence for Cayley percolation clusters

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjecture 6.45, printed p.216.

**Statement.** Does simple random walk on a Cayley graph have positive speed if and only if simple random walk on its infinite Bernoulli percolation clusters has positive speed almost surely?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Zero speed on every bounded-degree subexponential-growth subgraph. Result: Let H be a connected subgraph of a bounded-degree graph G with |B_G(x,n)|=exp(o(n)). The Carne-Varopoulos bound gives P_x(X_n=y)<=2 sqrt(deg_H(y)/deg_H(x)) exp(-d_H(x,y)^2/(2n)). Summing over reachable vertices yields P(d_H(x,X_n)>=epsilon n)<=C exp(o(n)-epsilon^2 n/2), which is summable. Thus the intrinsic speed on H is zero almost surely.. Obstruction: It settles the zero-speed equivalence for subexponential-growth Cayley graphs and their clusters only. Exponential-growth cases need different information.. Verification: author_checked_limited_argument. No proof file recorded.

### P0040. Uniqueness threshold below one in one-ended transitive graphs

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjecture 7.27, printed p.258.

**Statement.** Does every locally finite quasi-transitive graph with exactly one end have Bernoulli percolation uniqueness threshold p_u<1?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Amenable Cayley special case and a cutset bottleneck. Result: For an amenable Cayley graph with one end, uniqueness gives p_u=p_c. The known strict p_c<1 theorem for transitive graphs not roughly isometric to Z therefore gives p_u<1 in this special case. One-endedness excludes the two-ended roughly-Z case.. Obstruction: The remaining nonamenable quasi-transitive setting needs bounds on separating cutsets or cycle structure. A bounded cycle-basis argument is unavailable without its hypotheses.. Verification: author_checked_limited_argument. No proof file recorded.

### P0041. Nonuniqueness phase for nonamenable quasi-transitive graphs

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjectures 7.31 and 7.41, printed pp.260 and 265.

**Statement.** Must p_c(G)<p_u(G) for every nonamenable quasi-transitive graph? The source's related formulation asks whether the property p_c<p_u is preserved by rough isometries among quasi-transitive graphs.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Strict gap on regular trees. Result: On a (b+1)-regular tree with b>=2, branching-process survival gives p_c=1/b. For every p in (1/b,1), infinitely many separated descendant subtrees contain infinite open clusters while their attachment edge is closed, using independent positive-probability events. Thus there are infinitely many clusters and p_u=1.. Obstruction: This proves the strict gap in a fundamental nonamenable family. Nonamenability by itself does not provide the same independent cone decomposition.. Verification: author_checked_limited_argument. No proof file recorded.

### P0042. Bootstrap thresholds as a characterization of amenable groups

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 7.42, printed p.266.

**Statement.** Is a finitely generated group amenable exactly when every Cayley graph from every finite generating set has bootstrap complete-occupation critical probability p(G,k) in {0,1} for every threshold k?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Bootstrap thresholds on the line and the three-regular tree. Result: On Z the one-neighbor bootstrap threshold is zero, whereas the two-neighbor threshold is one because any initially vacant adjacent pair stays vacant. On the three-regular tree with threshold two, the final vacant set is the two-core of the initial vacant percolation. If its density q<=1/2, all vacant clusters are finite almost surely and leaf pruning empties them. If q>1/2, with positive probability a vertex has two surviving vacant branches, giving a bi-infinite vacant path that remains vacant. Hence the complete-occupation threshold is p=1/2.. Obstruction: This illustrates both the amenable endpoint behavior and a nonamenable interior threshold. It does not classify every generating set or every group.. Verification: author_checked_limited_argument. No proof file recorded.

### P0043. Absence of infinite clusters at critical percolation

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjecture 8.15, printed p.285.

**Statement.** If G is quasi-transitive and p_c(G)<1, is there almost surely no infinite Bernoulli cluster at p_c(G)?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Critical branching-process extinction. Result: For the regular tree at p=1/b, an infinite descendant cluster would have survival probability x satisfying x=1-(1-px)^b. For b>=2 strict concavity gives 1-(1-x/b)^b<x for every x>0, so only x=0 is possible.. Obstruction: Critical clusters in a general quasi-transitive graph are not independent branching trees. Their loop dependence is not captured by this fixed-point proof.. Verification: author_checked_limited_argument. No proof file recorded.

### P0044. Invariant monotone coupling of free and wired uniform spanning forests

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 10.6, printed pp.348-349.

**Statement.** For an infinite network, is there a coupling (W,F) of its wired and free uniform spanning forests with W subset F almost surely whose joint law is invariant under all network automorphisms?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Invariant monotone coupling under an amenable action. Result: Start with a monotone coupling of the two invariant forest laws under a countable amenable action. Average its translates over a Folner sequence. The product space of two edge configurations is compact, the prescribed marginals are unchanged, and the order relation is closed. A subsequential weak limit is therefore still a monotone coupling and is invariant because translation changes each average by at most its Folner boundary ratio.. Obstruction: For a nonamenable acting group there is no Folner averaging sequence. Existence of an arbitrary monotone coupling does not by itself produce an invariant one.. Verification: author_checked_limited_argument. No proof file recorded.

### P0045. Rational expected free-forest degree for finitely presented groups

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 10.11, printed p.351.

**Statement.** For a Cayley graph of a finitely presented group, is the expected degree at the identity in its free uniform spanning forest rational?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Rational finite-volume values do not force a rational limit. Result: For the standard free-group Cayley tree the free spanning forest is the entire tree, so its expected degree is the integer 2r. Finite exhaustion spanning-tree expectations are rational under unit conductances, but rational approximants can converge to an irrational number, as floor(n sqrt(2))/n demonstrates.. Obstruction: The general finitely presented-group question needs the algebraic structure behind the first l2 Betti number; rationality of finite combinatorial counts is insufficient.. Verification: author_checked_limited_argument. No proof file recorded.

### P0046. Connecting a free uniform spanning forest by arbitrarily sparse invariant additions

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 10.12, printed p.351.

**Statement.** For any Cayley graph, its free uniform spanning forest F, and epsilon>0, is there an invariant connected random spanning subgraph omega containing F with P(e in omega minus F)<epsilon for every edge e?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Connection to the cost equality obstruction. Result: If the free forest is already connected, taking its own configuration gives the requested extension with no added edges. Otherwise, an invariant connected extension with each edge added with probability at most epsilon would have expected root degree at most E deg_F(o)+deg_G(o) epsilon. The standard invariant-graphing bound would then imply cost(Gamma)<=E deg_F(o)/2=1+beta_1(Gamma) after epsilon tends to zero.. Obstruction: No dependent sprinkling construction was found. This reduction explains why independent sprinkling or a generic connectivity argument does not settle the question.. Verification: author_checked_limited_argument. No proof file recorded.

### P0047. Deterministic component count of the free uniform spanning forest

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 10.28, printed p.359.

**Statement.** On every infinite connected locally finite network, is the number of free uniform spanning-forest components almost surely a constant?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Why tail triviality alone does not fix the component count. Result: An ergodic action under which the forest law is invariant makes its component count deterministic. On an arbitrary network there need not be such an action. Trying to substitute tail triviality fails at the logical step: adding one edge between two components can change the component count, so this statistic has not been shown to be measurable with respect to the edge tail sigma-field.. Obstruction: A forest-law-specific argument making the count constant is still needed in the absence of a useful invariant ergodic action.. Verification: author_checked_limited_argument. No proof file recorded.

### P0048. One or infinitely many free-forest components without unimodularity

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 10.29, printed p.360.

**Statement.** On every transitive network, is the free uniform spanning forest almost surely connected or composed of infinitely many components?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Invariant ergodicity permits a finite component count larger than one. Result: On the Cayley graph of Z with generators +/-1 and +/-2, retain exactly the edges of length two. The resulting deterministic spanning forest has two bi-infinite components, is translation invariant, and its point-mass law is ergodic. Thus those two properties alone cannot exclude a finite count of two.. Obstruction: This forest is not asserted to have a uniform-spanning-forest law. The target requires extra free-forest structure in the nonunimodular case.. Verification: author_checked_limited_argument. No proof file recorded.

### P0049. Infinitely many ends in all free-forest components without unimodularity

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 10.52, printed p.377.

**Statement.** On a transitive network with distinct free and wired uniform spanning-forest laws, must every free-forest component have infinitely many ends almost surely?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Missing mass-transport step in the nonunimodular case. Result: In the unimodular setting, an expected-degree argument can establish the presence of infinitely ended components, and indistinguishability can promote a component property to all components. On a nonunimodular graph the unweighted root mass balance used in that argument is invalid; modular weights enter and light components need not receive the same balance.. Obstruction: No replacement weighted transport and no counterexample with the required FUSF/WUSF inequality were obtained. This is a failed proof route, not a new theorem.. Verification: author_checked_limited_argument. No proof file recorded.

### P0050. Singularity of distinct free and wired forest measures

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 10.58, printed p.385.

**Statement.** If the wired and free uniform spanning-forest measures differ on an infinite network, must they be mutually singular?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Distinct invariant ergodic laws are mutually singular. Result: For a fixed countable group action, two distinct invariant ergodic probability measures are mutually singular. In the Lebesgue decomposition of one relative to the other, the absolutely continuous part is invariant. Its density is invariant and hence constant under the second ergodic law; ergodicity of the first forces its absolutely continuous mass to be either zero or one. Nonzero overlap therefore forces equality.. Obstruction: This handles forest laws admitting such an ergodic common action. Arbitrary networks may lack it; two distinct probability laws need not be singular in general.. Verification: author_checked_limited_argument. No proof file recorded.

### P0051. Zero-one law for all forest components having one end

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 10.59, printed p.386.

**Statement.** For both free and wired uniform spanning forests of an arbitrary infinite network, is the event that every component has one end of probability zero or one?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: The all-one-ended event is not automatically a tail event. Result: Take two disjoint one-ended infinite trees and add one edge joining them. Before the addition every component has one end; afterwards the connected tree has two ends, since deleting the joining edge separates two infinite pieces.. Obstruction: Uniform-forest tail triviality cannot be invoked until a separate tail representation of the event is proved. The example is a logical obstruction, not a uniform-forest counterexample.. Verification: author_checked_limited_argument. No proof file recorded.

### P0052. Limiting bushes along a wired uniform-forest ray

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjecture 10.60, printed p.386.

**Statement.** Along the unique ray from the identity in its wired uniform spanning-forest component, do the finite bushes at successive ray vertices, translated back to the identity, converge in distribution?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Stationarity along a chosen spine is an additional requirement. Result: The WUSF viewed from an ordinary invariant root and the WUSF viewed from the nth vertex on its distinguished spine are different rooted laws. Moving along the spine is a configuration-dependent selection and need not preserve the original root law. Compactness or tightness, even if proved for the bush sequence, would only give subsequential limits.. Obstruction: Need regeneration or asymptotic stationarity along the loop-erased spine. Known high-growth and standard-lattice cases in the source must be removed before claiming a new remaining case.. Verification: author_checked_limited_argument. No proof file recorded.

### P0053. One-ended wired minimal forests without unimodularity

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 11.13, printed p.401.

**Statement.** Does each wired minimal spanning-forest component of a nonunimodular transitive graph have one end almost surely?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: A failed largest-edge argument on an infinite path. Result: A finite-cycle minimum-spanning-tree proof deletes the largest edge of a cycle. A proposed extension to a bi-infinite path fails because its supremum need not be attained: labels 1-1/(|k|+2) along k in Z approach one and have no maximum.. Obstruction: One-endedness needs an invasion-percolation or mass-transport argument that treats unattained suprema and the nonunimodular setting.. Verification: author_checked_limited_argument. No proof file recorded.

### P0054. Infinitely many ends in free minimal forests distinct from wired

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjecture 11.16, printed p.402.

**Statement.** If a quasi-transitive graph has distinct wired and free minimal spanning-forest laws, does every free minimal-forest component have infinitely many ends almost surely?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Regular-tree special case and resampling obstruction. Result: On a regular tree every edge is a bridge and there are no finite cycles, so the free minimal spanning forest is the whole tree. It has infinitely many ends, providing a direct special case where free and wired forests differ. On a graph with cycles, inserting an edge can force deletion of another edge by the cycle-maximum rule.. Obstruction: A minimal forest is not a Bernoulli insertion-tolerant process. Arguments proving end properties for percolation do not transfer without controlling the forced deletions.. Verification: author_checked_limited_argument. No proof file recorded.

### P0055. Minimal-forest connectivity and uniqueness at p_u

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjecture 11.18, printed p.403.

**Statement.** On a nonamenable quasi-transitive graph with p_u<1, is the free minimal spanning forest connected almost surely exactly when Bernoulli percolation has a unique infinite cluster at p_u?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: The easy direction of the uniqueness connection. Result: Under the p_u>p_c hypothesis in the source proposition, each FMSF component meets exactly one infinite p_u cluster. Consequently a connected FMSF can meet only one such cluster, so connectivity implies uniqueness at p_u in that setting.. Obstruction: The reverse direction needs to exclude several free-forest components meeting the same infinite p_u cluster. The stronger component-bijection formulation remains unproved here.. Verification: author_checked_limited_argument. No proof file recorded.

### P0056. One or infinitely many minimal-forest components

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 11.19, printed p.403.

**Statement.** Must both free and wired minimal spanning forests on a quasi-transitive graph have either one or infinitely many components almost surely?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Ergodic factor laws give constancy but not the value of the count. Result: Minimal spanning forests are equivariant functions of iid continuous edge labels, so an ergodic label action makes their component count constant. That alone permits a finite constant larger than one: the invariant deterministic two-component forest on Z with generators +/-1,+/-2 from P0048 is a counterexample to the purely ergodic inference.. Obstruction: The usual insertion-tolerance route must account for cycle-breaking deletions. No argument excluding a finite count between two and infinity was obtained in the full quasi-transitive scope.. Verification: author_checked_limited_argument. No proof file recorded.

### P0057. Uniqueness-critical percolation versus invariant spanning trees

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 11.31, printed p.408.

**Statement.** For a Cayley graph with p_u<1, is there an implication in either direction between multiple infinite clusters at p_u and the nonexistence of an invariant random spanning tree?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Conditional implication through the component-bijection conjecture. Result: If there is no invariant random spanning tree, the invariant FMSF cannot be connected, because a connected spanning forest would itself be such a tree. If the stronger conjecture in P0055 gave a bijection between free-forest components and infinite p_u clusters, that disconnection would imply multiple clusters at p_u.. Obstruction: Two properties sharing FMSF disconnection as a consequence do not thereby imply one another. Neither unconditional implication in the source question is established here.. Verification: author_checked_limited_argument. No proof file recorded.

### P0058. Indistinguishability of minimal spanning-forest components

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjecture 11.33, printed p.409.

**Statement.** Are the components of both free and wired minimal spanning forests on a unimodular transitive graph indistinguishable by every invariant Borel component property?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Invariant ergodicity does not imply component indistinguishability. Result: Construct a periodic forest on Z^2 using blocks of four horizontal rows. The first row is a bi-infinite horizontal path. The next three rows form a comb: the middle row is a horizontal spine, with each vertex in the two outer rows attached vertically to that spine. Repeat and choose a uniformly random vertical phase. The law is translation invariant and ergodic on its finite phase orbit, yet its components are distinguishable as lines and combs by the existence of degree-four vertices.. Obstruction: This is not a minimal-spanning-forest construction. It disproves only the shortcut from invariance and ergodicity to indistinguishability.. Verification: author_checked_limited_argument. No proof file recorded.

### P0059. Limiting bushes along a wired minimal-forest ray

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjecture 11.34, printed p.409.

**Statement.** For a Cayley graph not roughly isometric to Z, does the sequence of translated bushes along a ray in the identity's wired minimal spanning-forest component converge in distribution?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Unique-ray and limiting-law issues must be separated. Result: A bush decomposition first needs an almost surely unique infinite ray in the relevant component. Assuming that ray before proving the applicable one-endedness result would import another open assertion. Even when uniqueness is available, rooting successively along the ray is a configuration-dependent operation and does not automatically preserve the original rooted law.. Obstruction: No regeneration theorem or coupling proving convergence along the wired minimal-forest ray was obtained. The preliminary one-endedness assumptions must be checked for each claimed case.. Verification: author_checked_limited_argument. No proof file recorded.

### P0060. Dimensions with a connected Euclidean minimal spanning forest

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 11.35, printed p.409.

**Statement.** For which dimensions d is the minimal spanning forest on Z^d connected almost surely?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exact one-dimensional connectivity. Result: On Z every edge is a bridge, so the free minimal spanning forest retains all edges. For an edge with label u<1 to be excluded by a wired connection at infinity, both infinite half-lines would have to supply paths of edges with labels below u. Each such event has probability zero for iid uniform labels, since the probability for its first N edges is u^N. Thus the wired forest also retains every edge almost surely.. Obstruction: The higher-dimensional connectivity classification depends on intersections of invasion structures and is not determined by the one-dimensional calculation.. Verification: author_checked_limited_argument. No proof file recorded.

### P0061. Full scaling limit of the square-lattice minimal spanning tree

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 11.36, printed p.410.

**Statement.** Does the minimal spanning tree on epsilon Z^2 have a full distributional scaling limit as epsilon tends to zero, in the embedded-tree topology used for its known subsequential limits?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exact universality under a monotone change of edge labels. Result: On every finite graph with distinct edge weights, a strictly increasing transform preserves their order and hence preserves Kruskal selection and the minimum spanning tree. Independently, the cycle characterization retains exactly the same nonmaximal edges under that transform. For iid continuous distributions this identifies the law through ranks, or through the probability integral transform almost surely.. Obstruction: This is label-distribution universality on a fixed graph. It does not compare triangular and square lattice geometries or prove tightness and uniqueness of a continuum scaling limit.. Verification: author_checked_limited_argument. No proof file recorded.

### P0062. Connectivity of minimal forests on graphs roughly isometric to trees

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 11.37, printed p.410.

**Statement.** If a connected locally finite graph is roughly isometric to a tree, must its free minimal spanning forest be connected almost surely?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Connected FMSF on trees of finite cycle blocks. Result: Suppose an infinite cactus graph is built from bridges and edge-disjoint finite cycles. Its free minimal spanning forest retains every bridge and removes exactly the unique largest-weight edge of each cycle. Each resulting cycle block remains connected. A finite block path between any two vertices remains connected after these deletions, so the forest is globally connected and acyclic.. Obstruction: Uniformly bounded block diameters give a class roughly isometric to trees. General roughly-tree graphs can have overlapping cycles and need not admit this block decomposition.. Verification: author_checked_limited_argument. No proof file recorded.

### P0063. Singularity of binary and ternary harmonic codings of the Cantor set

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 16.7, printed p.542.

**Statement.** For the middle-thirds Cantor set E, let nu_b be harmonic measure on the source's base-b coding tree T[b](E), pushed to E. Is nu_2 mutually singular with the Cantor-Lebesgue measure nu_3?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Likelihood-ratio strategy and its exact missing input. Result: For product Bernoulli measures with different parameters, the strong law gives disjoint full-measure sets of limiting digit frequencies and hence mutual singularity. A possible analogous strategy for the two Cantor measures is a likelihood-ratio martingale along a common binary coding, with cumulative conditional relative entropy forcing its limit to vanish.. Obstruction: No divergent conditional-entropy estimate or martingale tail control was established for the actual harmonic measure versus base-three Cantor measure.. Verification: author_checked_limited_argument. No proof file recorded.

### P0064. Dimension drop for every nonuniform Galton-Watson flow

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Conjecture 17.23, printed p.580.

**Statement.** For a nondegenerate supercritical Galton-Watson law of mean m under the chapter's moment assumptions, must every consistent equivariant flow rule different almost surely from UNIF have boundary-measure Hausdorff dimension below log m almost surely?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Exact dimension drop for the nonergodic same-color flow candidate. Result: For the AND/OR color construction of P0033, let K be the number of children of the parent color and choose uniformly among them. Conditional on root color zero, P(K=1,2,3)=(3/5,3/10,1/10); conditional on color one it is (3/10,3/5,1/10). The full conditional-child selection lemma implies these K variables are iid along the selected ray within each color class. Hence the local dimension is h_0=(3/10)log 2+(1/10)log 3 or h_1=(3/5)log 2+(1/10)log 3 by the strong law. Both are strictly less than log(12/5), the Galton-Watson dimension.. Obstruction: This author-checked special construction supports dimension drop and is not a counterexample to the full question. It inherits the P0033 coloring proof and remains without independent review.. Verification: author_checked_limited_argument. No proof file recorded.

### P0065. Monotonicity of harmonic dimension under inward bias

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 17.29, printed p.582.

**Statement.** For a nondegenerate supercritical Galton-Watson tree without leaves and 0<=lambda<m, does harmonic-measure dimension of RW_lambda increase with lambda, and is the increase strict?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: Regular-tree equality and a local-entropy countercheck. Result: On a deterministic b-ary tree, symmetry makes harmonic measure uniform on children for every transient bias lambda<b, so its dimension is log b, independent of lambda. Thus strict monotonicity must exclude deterministic offspring. A local root-entropy proof also fails: attach regular trees of branching 2 and 4 as two root subtrees. Their escape probabilities are 1-lambda/2 and 1-lambda/4 for lambda<2; last-exit child probabilities are proportional to these values and become more unequal as lambda increases toward 2, so their entropy decreases.. Obstruction: Global dimension averages local entropy under a bias-dependent law of the environment seen along the ray. Controlling that changing law remains necessary.. Verification: author_checked_limited_argument. No proof file recorded.

### P0066. Monotonicity of biased-walk speed on Galton-Watson trees

**Source.** Probability on Trees and Networks, paperback electronic version 19 August 2026 (lyons_peres_20260819), Question 17.33, printed p.592.

**Statement.** For Galton-Watson trees with p_0=0, is the speed of RW_lambda nonincreasing as the bias parameter lambda increases?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** Method: The changing stationary environment blocks a pointwise drift proof. Result: For fixed offspring D, the radial drift (D-lambda)/(D+lambda) decreases with lambda, and on a regular tree it gives the exact speed. In a nondegenerate Galton-Watson tree the stationary distribution of the environment seen by the walker also changes with lambda, so differentiating the speed has an additional measure-change term.. Obstruction: The example is not a Galton-Watson speed counterexample. No sign bound for the measure-change term, or alternative monotone coupling of speeds, was proved.. Verification: author_checked_limited_argument. No proof file recorded.

### P0067. Global Kuramoto synchronization of random cubic graphs

**Source.** Randomstrasse101: Open Problems of 2024 (randomstrasse_2024_v1), Conjecture3, PDF p.3.

**Statement.** Is a uniformly random simple 3-regular graph globally synchronizing with probability tending to one? Global synchronization means that every local minimum of sum_(ij in E)(1-cos(theta_i-theta_j)) is a consensus configuration.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Global Kuramoto synchronization of random cubic graphs special-case or structural calculation. Result: On the cubic prism C_m times K_2, m>=5, put theta_(j,a)=2 pi j/m for both layers. The sine forces along the two cycle neighbors cancel and rung forces vanish. The Hessian is a weighted Laplacian with cycle weights cos(2 pi/m)>0 and rung weights1, so it is positive definite modulo the global rotation. This is a nonconsensus strict local minimum modulo rotation.. Obstruction: Must show that uniformly random cubic graphs avoid all such stable phase arrangements with probability tending to one; the prism family itself has vanishing probability.. Verification: author_checked_limited_argument. No proof file recorded.

### P0068. Subspectral detection from a growing number of synchronization frequencies

**Source.** Randomstrasse101: Open Problems of 2024 (randomstrasse_2024_v1), OpenProblem7, PDF p.7.

**Statement.** For uniform U(1) signal x in C^n with |x_i|=1 and independent Wigner noises, observe Y_k=(lambda/n)x^(k)(x^(k))*+W_k/sqrt(n), k=1,...,L_n. Find a scaling of distinct frequencies L_n for which a polynomial-time algorithm reliably detects signal at some fixed lambda<1.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Subspectral detection from a growing number of synchronization frequencies special-case or structural calculation. Result: If L independent observations repeated the same rank-one signal, averaging would divide noise standard deviation by sqrt(L) and reduce the effective spectral threshold. In the actual model the vectors x^(k) differ with k, so averaging Y_k yields a sum of different rank-one projectors. It is not a repeated observation of xx*.. Obstruction: Need an algorithm exploiting algebraic relations between distinct powers. Repetition-based variance reduction solves a different experiment.. Verification: author_checked_limited_argument. No proof file recorded.

### P0069. Subexponential detection at fixed synchronization frequencies

**Source.** Randomstrasse101: Open Problems of 2024 (randomstrasse_2024_v1), OpenProblem8, PDF p.7.

**Statement.** In the same multifrequency U(1) or specified finite-group Gaussian synchronization model, fix L independently of n. For signal strength between its statistical threshold and1, is reliable detection possible in time exp(n^delta) for some delta<1?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Subexponential detection at fixed synchronization frequencies special-case or structural calculation. Result: Try enumerating an oracle seed of m=o(n) signal coordinates and use their edges to estimate a new coordinate in one channel. After multiplying by known seed phases, the sum has signal amplitude lambda m/n and noise standard deviation sqrt(m/n), so signal-to-noise ratio is lambda sqrt(m/n), which tends to zero.. Obstruction: This only defeats a one-step seed-and-average method. Iterative amplification or a different subexponential algorithm is not ruled out.. Verification: author_checked_limited_argument. No proof file recorded.

### P0070. Kikuchi spectral thresholds as the polynomial degree increases

**Source.** Randomstrasse101: Open Problems of 2024 (randomstrasse_2024_v1), Conjecture9, PDF p.8.

**Statement.** For even tensor order r and fixed l>=r/2, index M by l-subsets of [n] and set M_IJ=lambda+Z_(I symmetric_difference J) when that difference has size r, and zero otherwise, with independent standard Gaussian Z_S. Does the normalized spectral-outlier threshold n^(r/4) lambda_critical(r,l) tend to zero as l tends to infinity after n tends to infinity?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Kikuchi spectral thresholds as the polynomial degree increases special-case or structural calculation. Result: Each row has k=binomial(l,r/2)binomial(n-l,r/2) nonzero entries. For the normalized all-ones vector v, v*M(lambda)*v=lambda k+(k/binomial(n,r))sum_(|S|=r)Z_S. Thus its noise variance is k^2/binomial(n,r). Write M(0)=sum_S Z_S A_S; A_S^2 is the diagonal indicator of |I intersection S|=r/2, hence sum_S A_S^2=k I.. Obstruction: A Gaussian matrix-series bound introduces sqrt(log binomial(n,l)) into the norm estimate. Removing that loss and controlling the actual outlier transition remain necessary; the r=2 scope caveat needs resolution.. Verification: author_checked_limited_argument. No proof file recorded.

### P0071. Polynomial Glauber mixing throughout the SK high-temperature regime

**Source.** Randomstrasse101: Open Problems of 2024 (randomstrasse_2024_v1), OpenProblem15, PDF p.12.

**Statement.** For the Sherrington-Kirkpatrick Ising model with arbitrary external field, does single-site heat-bath Glauber dynamics mix in polynomial total-variation time for every fixed beta<1, with high probability over the Gaussian disorder?

**Status.** Historical status: source_says_open. Current-literature status: unverified (Large-field result, not arbitrary-field full regime (https://arxiv.org/abs/2607.06813); Preprint claims beta<1/2 uniform fields; full beta<1 remainder not resolved by its statement (https://arxiv.org/abs/2608.22159)). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Polynomial Glauber mixing throughout the SK high-temperature regime special-case or structural calculation. Result: At beta=0, spins are independent under the target product law. Couple two random-scan heat-bath chains using the same update coordinate and uniform draw. Once a coordinate has been updated it agrees forever. The probability some coordinate remains unupdated by t is at most n(1-1/n)^t<=n exp(-t/n), giving mixing time at most n log(n/epsilon) for every external field.. Obstruction: For beta>0 a later update can destroy agreement through neighboring disagreements. The beta=0 coupon-collector argument does not control the whole replica-symmetric interval.. Verification: author_checked_limited_argument. No proof file recorded.

### P0072. Geodesic selection by reinforced ants

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), Section2, main conjecture, PDF pp.1-2.

**Statement.** On a finite graph with nest N and food F, ants take edge-weighted random walks until hitting F. Reinforce either a uniformly chosen shortest N-F path in the visited trace, or the loop erasure of the reversed walk. Are all edges whose weights grow linearly contained in shortest N-F paths of the original graph?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Geodesic selection by reinforced ants structural argument. Result: On a finite tree with one food vertex, every N-F walk has the same simple path after loop erasure, and the shortest path in its trace is that path too. Each edge of that path therefore receives exactly one increment per ant; every other edge receives zero. The normalized weights converge to its indicator without a probabilistic limit theorem.. Obstruction: Cycles permit different simple paths and histories affect their weights. The deterministic tree reduction gives no control of their competition.. Verification: author_checked_limited_argument. No proof file recorded.

### P0073. Deterministic limits for trace-reinforced ants

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblems1-2, PDF p.2; underlying Kious-Mailler-Schapira Conjecture1.1.

**Statement.** When each ant reinforces every edge it visited at least once, do all edge weights divided by the number of ants converge almost surely to deterministic constants on general finite graphs, and does an appropriate edgewise statement hold on Z^2?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Deterministic limits for trace-reinforced ants structural argument. Result: If two parallel edges connect N directly to F, an ant crosses exactly one and reinforces it. Starting at weights a,b gives the classical Polya urn: the first normalized weight has Beta(a,b) limit with variance ab/((a+b)^2(a+b+1))>0. Thus the unrestricted multigraph formulation is false, and the underlying no-parallel-food assumption is necessary.. Obstruction: For simple finite graphs the nonlinear trace-hitting probabilities still require a uniqueness/attraction argument. On Z^2, changing conductances additionally complicate the guarantee that every ant reaches food.. Verification: author_checked_limited_argument. No proof file recorded.

### P0074. Maximal degree and its location in the infinite-path fitness regime

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem6, PDF p.5.

**Statement.** For superlinear preferential attachment with iid positive fitness and attachment f(k,w)=w k^p or k^p+w, determine the growth of the maximum degree and the label attaining it in the regime where the limiting tree is locally finite and has one infinite ray.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Maximal degree and its location in the infinite-path fitness regime structural argument. Result: Let Delta_n be the maximum degree and I_n a maximizing label. If Delta_n tends to infinity and each fixed vertex has finite limiting degree, then I_n tends to infinity: for every fixed K, the maximum of the K finite limiting degrees is finite, and eventually Delta_n exceeds it.. Obstruction: Neither the rate of Delta_n nor even its divergence follows from local finiteness alone. A deterministic infinite path has maximum degree2.. Verification: author_checked_limited_argument. No proof file recorded.

### P0075. Empirical degree scaling for superlinear attachment with fitness

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem7, PDF p.5.

**Statement.** Determine the scaling and limiting empirical degree distribution of the superlinear preferential-attachment tree with fitness described in Section3, including the infinite-path regime.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Empirical degree scaling for superlinear attachment with fitness structural argument. Result: For every n-vertex tree, the empirical degree law pi_n satisfies sum_k k pi_n(k)=2-2/n, hence pi_n([K,infinity))<=2/K. Thus the unscaled empirical laws are tight on the positive integers. Any weak subsequential limit is a probability law with mean at most2; its mean can be smaller because degrees are not uniformly integrable.. Obstruction: Tightness supplies no unique limit or model-specific tail scaling. Escape of the first moment must be tracked separately.. Verification: author_checked_limited_argument. No proof file recorded.

### P0076. Multiple-attachment phase transition with superlinear fitness

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem8, PDF p.5.

**Statement.** In the Section3 fitness model, replace one attachment per new vertex by m>=2 choices and determine how the transition between degree condensation and an infinite-path structure changes.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Multiple-attachment phase transition with superlinear fitness structural argument. Result: After n arrivals with exactly m outgoing attachments each, total degree is 2m(n-1) up to the finite seed. Consequently no collection of vertices can each have degree fraction greater than a if it contains more than 2m/a vertices. This bounds the number of macroscopic hubs but permits several of them, unlike a single-star conclusion.. Obstruction: A tree embedding into independent genealogical birth processes is lost when a vertex has several parents. The degree budget does not identify the phase boundary.. Verification: author_checked_limited_argument. No proof file recorded.

### P0077. Fluctuations of fitness-reinforced sequence sums

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem9, PDF p.7.

**Statement.** Let a new positive value be sampled from mu with probability beta, and otherwise copy a previous value with probability proportional to value times multiplicity. With ess sup mu=1 and mu({1})=0, find the fluctuation limit of sum_(i<=n)(X_i-lambda_star), where lambda_star is the Section4 law-of-large-numbers constant.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Fluctuations of fitness-reinforced sequence sums structural argument. Result: Writing S_n=sum X_i and Q_n=sum X_i^2 gives E[X_(n+1)|F_n]=beta m_1+(1-beta)Q_n/S_n. Subtracting this predictable mean yields bounded martingale differences, but the centered sum also contains sum[beta m_1+(1-beta)Q_i/S_i-lambda_star].. Obstruction: A martingale CLT alone cannot settle the question: fluctuations of Q_n/S_n and the slowly relaxing drift may contribute at the same or larger scale.. Verification: author_checked_limited_argument. No proof file recorded.

### P0078. Boundary profile of the reinforced-sequence condensate

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem10 and displayed conjecture, PDF pp.7-8.

**Statement.** When beta integral (1-x)^(-1) dmu<1 and mu(1-x,1) is regularly varying at zero with index alpha>1, determine a_n tending to infinity and c>0 for which n^(-1) sum f(a_n(1-X_i)) converges in probability to c integral_0^infinity f(x)e^(-x)x^alpha dx for compactly supported continuous f.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Boundary profile of the reinforced-sequence condensate structural argument. Result: Let rho=1-beta integral (1-x)^(-1)dmu be the mass missing from the bulk limit. If the claimed rescaled measure is tight on (0,infinity) and carries all that missing mass, integrating its density forces c=rho/Gamma(alpha+1). Without those two additional controls this identification is invalid.. Obstruction: The source provides only vague convergence away from the boundary. Finding a_n and proving boundary tightness are the load-bearing missing steps.. Verification: author_checked_limited_argument. No proof file recorded.

### P0079. Growth of sums with unbounded reinforcement fitness

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem11, PDF p.8.

**Statement.** For the same innovation/copying scheme with unbounded positive innovation law mu, determine the superlinear growth rate of S_n=sum_(i<=n) X_i as a function of the tail of mu.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Growth of sums with unbounded reinforcement fitness structural argument. Result: Let K_n count innovation draws and let Y_j be their iid values. Every innovation appears at least once, so S_n>=sum_(j<=K_n)Y_j and S_n>=max_(j<=K_n)Y_j, while K_n/n tends to beta almost surely. If E_mu Y=infinity, the truncated strong law and then monotone convergence give S_n/n tending to infinity from this lower bound alone.. Obstruction: Finite-mean unbounded mu requires amplification by reinforcement; innovation lower bounds alone remain linear and cannot give the requested rate.. Verification: author_checked_limited_argument. No proof file recorded.

### P0080. Weak reinforcement on infinite WARM networks

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), Conjecture1, PDF p.10.

**Statement.** For a bounded-degree infinite graph, bounded positive vertex firing rates, and WARM exponent 0<alpha<1, establish convergence of every normalized edge count to the intended unique positive equilibrium.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Weak reinforcement on infinite WARM networks structural argument. Result: On Z with all firing rates1, set edge values alternately2 and0. At each vertex the only positive incident edge is selected with probability1; its two endpoints supply total rate2, while zero edges get rate0. This is an equilibrium for every alpha>0. Shifting gives a second one, and the uniform edge value1 is a third. Thus uniqueness among all nonnegative equilibria is false.. Obstruction: The positive-equilibrium uniqueness and stochastic attraction problem on general infinite graphs remains; no finite total Lyapunov function is available.. Verification: author_checked_limited_argument. No proof file recorded.

### P0081. Critical WARM on the integer line

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), Conjecture2, PDF p.10.

**Statement.** For WARM on Z with alpha=1 and all vertex firing rates1, prove that each edge count divided by time converges almost surely to1.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Critical WARM on the integer line structural argument. Result: For any a,b>0 with a+b=2, the alternating edge configuration a,b,a,b,... solves the equilibrium equation: an a-edge receives a/(a+b) from each endpoint, totaling a, and similarly for b. Thus the ODE has a continuum of positive equilibria on the same graph.. Obstruction: Convergence to1 cannot follow merely from uniqueness of ODE equilibria, which is false. One must exploit stochastic dynamics or spatial structure to select the uniform equilibrium.. Verification: author_checked_limited_argument. No proof file recorded.

### P0082. Sharp reinforcement threshold for WARM forests

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem12, PDF pp.10-11.

**Statement.** Improve the known sufficient threshold alpha>2 ensuring that every connected component of a stable finite-graph WARM equilibrium is a tree, allowing arbitrary positive firing rates.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Sharp reinforcement threshold for WARM forests structural argument. Result: At a positive equilibrium x, put s_v=sum_(e~v)x_e^alpha. The Hessian of the correctly rate-weighted Lyapunov function satisfies H[delta,delta]=(alpha-1)sum_e delta_e^2/x_e-alpha sum_v p_v/s_v^2 (sum_(e~v)x_e^(alpha-1)delta_e)^2. Along an even cycle choose alternating delta_e=+/-x_e^(1-alpha), zero elsewhere. Every vertex sum vanishes, giving a positive direction for alpha>1 and hence linear instability.. Obstruction: This eliminates even cycles, not odd cycles or all odd unicyclic supports. It does not improve the universal forest threshold by itself.. Verification: author_checked_limited_argument. No proof file recorded.

### P0083. Sharp reinforcement threshold for WARM whiskers

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem13, PDF pp.10-11.

**Statement.** For finite WARM graphs with uniform vertex firing rates, improve the sufficient threshold alpha>25 for every surviving stable component to have diameter at most3.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Sharp reinforcement threshold for WARM whiskers structural argument. Result: Consider a support path of four edges with reflection-symmetric values a,b,b,a and unit vertex rates. The endpoint equation is a=1+a^alpha/(a^alpha+b^alpha), so 1<a<2. The neighboring inner-edge equation is b=b^alpha/(a^alpha+b^alpha)+1/2. Summing gives a+b=5/2. Thus any such equilibrium reduces to a scalar equation with b=5/2-a.. Obstruction: Existence and stability of this scalar branch must still be analyzed, and excluding this symmetric path alone would not exclude all larger asymmetric trees.. Verification: author_checked_limited_argument. No proof file recorded.

### P0084. Finite surviving components in infinite superlinear WARM

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), Conjecture3, PDF p.11.

**Statement.** With bounded-degree graph, firing rates bounded above and bounded away from zero, and alpha>1, prove edgewise convergence of normalized WARM counts and finiteness of every component of surviving edges.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Finite surviving components in infinite superlinear WARM structural argument. Result: If every edge had survival probability at most q, this would not imply domination by iid Bernoulli percolation. For example, activate all edges simultaneously with probability q and none otherwise. Every marginal is q, yet there is an infinite component with probability q for every q>0 on an infinite connected graph.. Obstruction: A valid comparison needs conditional probability bounds or explicit dependence control, together with convergence of the edge weights; small one-edge probabilities are insufficient.. Verification: author_checked_limited_argument. No proof file recorded.

### P0085. WARM percolation with vanishing rates on lattices

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem14, PDF p.11.

**Statement.** Do bounded positive firing rates on Z^d, d>=2, which are not bounded away from zero, and some alpha>1 yield a positive probability of an infinite component of surviving WARM edges? If so, determine uniqueness.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: WARM percolation with vanishing rates on lattices structural argument. Result: There is no bounded-length embedding of a b-ary tree, b>=2, into Z^d with distinct vertices: its depth-r ball contains order b^r vertices, whereas images lie in a lattice ball of radius Lr with only O(r^d) vertices. Therefore transferring the known regular-tree construction requires unbounded subdivisions or a different geometry.. Obstruction: Unbounded subdivisions change the local competition and rates along paths. The volume obstruction explains why a direct bounded-distortion transfer fails but does not exclude lattice WARM percolation.. Verification: author_checked_limited_argument. No proof file recorded.

### P0086. Recurrence of sublinear vertex-reinforced walk on Z

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem15, PDF p.12.

**Statement.** For nearest-neighbor vertex-reinforced random walk on Z, with transition weights w(1+local_time) and positive w satisfying w(x)=o(x^alpha) for some alpha<1, is the walk recurrent?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Recurrence of sublinear vertex-reinforced walk on Z structural argument. Result: For constant w the walk is simple symmetric random walk. Starting at1 and stopping at0 or m, the harmonic function h(k)=k/m gives probability1/m of hitting m before0. Letting m tend to infinity shows that the probability of avoiding0 forever is0; by the strong Markov property returns recur indefinitely.. Obstruction: For nonconstant reinforcement, position alone is not Markov and the gambler-ruin harmonic function no longer solves the conditional transition equation.. Verification: author_checked_limited_argument. No proof file recorded.

### P0087. Forced network urn convergence and diffusion scaling

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem16, PDF pp.14-16.

**Statement.** For Z_(n+1)=(1-r-f)Z_n+r X_(n+1)+f p with E[X_(n+1)|F_n]=Q Z_n, Q=A^T irreducible row-stochastic and X binary coordinatewise, determine nonconvergence and the continuous-time limit when r tends to0 and f is asymptotic to c r^2.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Forced network urn convergence and diffusion scaling structural argument. Result: A complete fixed-step classification follows. On any event Z_n->z, the update forces X_n to converge to a binary vector x and hence eventually equal it. The bounded martingale-difference strong law gives x=Qz. The update limit gives z=(r x+f p)/(r+f). A binary coordinate of Qz can equal0 or1 only when all its positive-weight predecessors have the same x-value and matching p-value. Irreducibility then forces x and p to be the all-zero or all-one vector. Conversely if p=0, the positive stationary vector pi gives E[pi.Z_n]=(1-f)^n E[pi.Z_0], and Markov plus Borel-Cantelli yields Z_n->0; p=1 follows by complementing.. Obstruction: This resolves the fixed-step convergence subquestion under the stated assumptions, but not the whole diffusion question. Fast synchronization, an initial layer, and the covariance specification must be treated before a full solution label.. Verification: author_checked_limited_argument. No proof file recorded.

### P0088. Matching local limits of Bernoulli and Poisson-outdegree attachment

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem23, PDF p.21.

**Statement.** Relate the local weak limit of the Dereich-Morters Bernoulli preferential-attachment model, whose older vertices are chosen independently with probability f(in_degree)/(n-1), to an appropriately matched model with iid Poisson outgoing degree and attachment based on in-degree.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Matching local limits of Bernoulli and Poisson-outdegree attachment structural argument. Result: Conditional on current degrees, the Bernoulli outgoing count has mean Lambda_n=sum_i p_ni. Its total variation distance to Poisson(Lambda_n) is at most sum_i p_ni^2 by the elementary independent Bernoulli-to-Poisson coupling. If max_i p_ni->0 and Lambda_n stays bounded, this error tends to0.. Obstruction: A matching outgoing count does not prove local graph convergence. Target choices, ancestor types, and dependencies across successive births must be coupled over an explored neighborhood.. Verification: author_checked_limited_argument. No proof file recorded.

### P0089. Local limits for nonaffine attachment with multiple edges

**Source.** Aletti et al.: Open problems in stochastic reinforcement models; March2023 workshop, published2025 (reinforcement_matrix_2023), OpenProblem24, PDF p.21.

**Statement.** Determine local weak limits of preferential-attachment graphs with fixed outgoing degree m>=2 and nonaffine attachment function f, extending the known tree and affine cases.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Local limits for nonaffine attachment with multiple edges structural argument. Result: With m=1 and equal attachment weights, the graph is a uniform recursive tree and its empirical degree law is tight by the tree degree identity. With m>=2 the degree budget still gives uniform-root degree tightness, since its mean is at most2m plus a vanishing seed term.. Obstruction: Tightness of the root degree alone does not ensure tightness of radius-two neighborhoods: a uniformly selected leaf can attach to a hub of diverging degree. Condensation and size bias must be controlled.. Verification: author_checked_limited_argument. No proof file recorded.

### P0090. Multistate pivot-tree criterion for interpretation

**Source.** Random tree recursions: which fixed points correspond to tangible sets of trees? (tree_automata_2019), Section6, PDF p.39, first paragraph.

**Statement.** Extend the two-state interpretation criterion of Theorem1.7 to finite color sets of size at least3, covering critical and supercritical pivot trees even without positive regularity.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Multistate pivot-tree criterion for interpretation structural argument. Result: For a finite-type pivot branching process with mean matrix M and spectral radius less than1, E[population at level n] tends to0, hence P(level n nonempty)<=E[size] tends to0. This proves extinction and explains the subcritical direction already covered by Theorem1.8.. Obstruction: At spectral radius1 the first moment need not decay, and reducible type classes can behave differently. The established subcritical argument does not settle critical/supercritical interpretation.. Verification: author_checked_limited_argument. No proof file recorded.

### P0091. Infinite-state tree-automaton interpretation criteria

**Source.** Random tree recursions: which fixed points correspond to tangible sets of trees? (tree_automata_2019), Section6, PDF pp.39-40, second paragraph.

**Statement.** Extend the random-tree interpretation and pivot-process theory to infinite state spaces, so it can handle recursive distributional models beyond finite colors.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Infinite-state tree-automaton interpretation criteria structural argument. Result: Consider a countable-type branching process in which each type k individual has deterministically one child of type k+1. It survives forever, although every finite truncation of its mean matrix is nilpotent and every fixed type eventually disappears.. Obstruction: Finite truncations falsely suggest extinction because population escapes through types. Any infinite-state criterion needs tightness or a suitable operator topology, not only finite truncation eigenvalues.. Verification: author_checked_limited_argument. No proof file recorded.

### P0092. Randomized tree automata and endogeny

**Source.** Random tree recursions: which fixed points correspond to tangible sets of trees? (tree_automata_2019), Section6, PDF pp.39-40, second paragraph.

**Statement.** Extend the interpretation/pivot theory when each vertex has iid auxiliary randomness and its state is a function of its child states and that local randomness.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Randomized tree automata and endogeny structural argument. Result: Let each vertex state be its own independent Bernoulli(p) innovation, ignoring its children. The pivot tree is empty and the state is measurable from the marked tree, but for 0<p<1 it is independent of the unmarked tree and cannot be a measurable function of that tree.. Obstruction: A literal extension retaining only the unmarked-tree sigma-field is false. A useful theorem must specify the innovation sigma-field and then handle nontrivial child dependence.. Verification: author_checked_limited_argument. No proof file recorded.

### P0093. Infinitely many fixed points of a finite-color automaton

**Source.** Random tree recursions: which fixed points correspond to tangible sets of trees? (tree_automata_2019), Section6, PDF p.40, third paragraph.

**Statement.** For a finite color set of size at least3 and a deterministic child-count automaton under the paper standing offspring assumptions, can the distributional map have infinitely many fixed points?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Infinitely many fixed points of a finite-color automaton structural argument. Result: If the offspring distribution has finite support bounded by D, each coordinate of the distributional map is a polynomial of degree at most D in the color probabilities. Fixed points are therefore a compact real algebraic subset of the probability simplex. In contrast with one variable, polynomial equations may have curves of zeros, so analyticity alone cannot prove finiteness.. Obstruction: The nonnegative multinomial coefficients and deterministic count assignments constrain which algebraic sets can occur. Neither an admissible positive-dimensional example nor a general exclusion is obtained.. Verification: author_checked_limited_argument. No proof file recorded.

### P0094. Prescribing rogue and interpretable automaton fixed points

**Source.** Random tree recursions: which fixed points correspond to tangible sets of trees? (tree_automata_2019), Section6, PDF p.40, third paragraph.

**Statement.** Given a finite prescribed configuration of two-state fixed points with rogue/interpretable labels, determine whether a deterministic tree automaton and offspring distribution can realize it, including the monotone-automaton restriction.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Prescribing rogue and interpretable automaton fixed points structural argument. Result: For a differentiable increasing distributional map Psi, let g(p)=Psi(p)-p. At an isolated simple fixed point, crossing from g>0 to g<0 gives Psi prime<1, while the opposite crossing gives Psi prime>1. Consecutive simple interior crossings must alternate signs. Thus a prescribed list of simple attractive/repulsive crossings cannot have two consecutive crossings of the same orientation without an intervening zero.. Obstruction: The derivative restriction is necessary, not sufficient for an automaton realization or rogue classification in degenerate cases. Constructing compatible multinomial maps remains open here.. Verification: author_checked_limited_argument. No proof file recorded.

### P0095. Automaton-level conditions for a unique fixed point

**Source.** Random tree recursions: which fixed points correspond to tangible sets of trees? (tree_automata_2019), Section6, PDF p.40, fourth paragraph.

**Statement.** Find structural conditions on a tree automaton itself that force uniqueness of its distributional fixed point, complementing the source condition on a first-order interpretation.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Automaton-level conditions for a unique fixed point structural argument. Result: Suppose that for each offspring count D the rule depends on a fixed set of at most k(D) child positions, and E k(D)=c<1. Couple child colors optimally with disagreement probability dTV(mu,nu); the union bound over that fixed relevant set gives dTV(Psi(mu),Psi(nu))<=c dTV(mu,nu). Iteration is a contraction and yields a unique fixed point on the finite simplex.. Obstruction: For supercritical offspring the crude contraction constant exceeds1. A useful structural criterion must exploit much finer properties than the number of children.. Verification: author_checked_limited_argument. No proof file recorded.

### P0096. Four-edge-minimum lower bound for the FPP time constant

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question12, PDF pp.32-33 boundary; repeated p.146; manuscript26September2016.

**Statement.** For iid nonnegative edge times on Z^2 with F(0)=0, is the axial time constant at least the expected minimum of four independent edge times?

**Status.** Historical status: source_says_open. Current-literature status: resolved_in_literature (no status-search record.). Admission: not admitted; result_status: literature_counterexample_rederived. This row was revised 2 times in problems.jsonl; the latest occurrence is reported here.

**Our work.** [attempt 1 of 2] Method: Supercritical zero-weight limit and bounded finite-distance continuity. Result: Take tau=eta+epsilon U with P(eta=0)=3/4 and U uniform[0,1]. For epsilon>0 this is atomless and bounded with F(0)=0. The four-edge minimum has expectation at least1/256. The eta-model time constant is0. For each n, passage times converge to their eta-model values and are bounded by2n; dominated convergence and mu=inf_n E T(0,ne1)/n imply mu_epsilon tends to0. All sufficiently small epsilon reverse the proposed inequality.. Obstruction: No mathematical gap identified in the written candidate; later-literature and erratum search remain incomplete. No explicit numerical epsilon threshold or independent review is claimed.. Verification: author_checked_candidate. [attempt 2 of 2] Method: Primary theorem comparison and exact quantile evaluation. Result: Ahlberg2019/2020 already refuted the question. Applying his mu<=2t_(2/3) to the independently drafted tau=eta+epsilon U family gives t_(2/3)=8epsilon/9, hence mu<=16epsilon/9. With epsilon=1/1024, mu<=1/576<1/256<=E minfour. This supplies an explicit atomless bounded counterexample using an established theorem.. Obstruction: No current-open problem remains for this universal inequality. This is literature-established, not an original solution.. Verification: primary_two_page_proof_read_and_author_checked. No proof file recorded.

### P0097. An explicit nontrivial FPP time constant and limit shape

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Questions1 and37, PDF pp.11 and141.

**Statement.** Identify an explicit positive axial time constant for a nondegenerate iid nearest-neighbor passage-time law on Z^d, or explicitly determine a nontrivial compact limit shape.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: An explicit nontrivial FPP time constant and limit shape structural argument. Result: If every edge time is multiplied by c>0, every finite path cost and every passage time is multiplied by c, so the time constant is multiplied by c and the limit shape is dilated by1/c. Thus scaling a known degenerate example cannot produce the missing nontrivial shape.. Obstruction: Homogeneity supplies a transformation law, not a computable nondegenerate base model. Integrable directed last-passage formulas apply to a different optimization problem.. Verification: author_checked_limited_argument. No proof file recorded.

### P0098. Strict FPP comparison in higher dimensions at a large minimum atom

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question3, PDF p.13; Definition2.8 and Theorem2.12, pp.12-13.

**Statement.** Extend strict comparison of axial time constants for strictly ordered passage-time laws in increasing-concave order to d>2 when the minimum support value r>0 has mass at least the oriented-percolation threshold.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Strict FPP comparison in higher dimensions at a large minimum atom structural argument. Result: For the special coupling tau'_e=tau_e+delta with delta>0, every path from0 to ne1 has at least n edges. Its primed cost is at least its original cost plus delta n. Taking infima and limits gives mu'(e1)>=mu(e1)+delta.. Obstruction: General increasing-concave order, including mean-preserving spreads, has no pointwise additive coupling. The argument does not handle the remaining comparison class.. Verification: author_checked_limited_argument. No proof file recorded.

### P0099. Strict convexity of iid FPP limit shapes

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question4, PDF p.21; Section2.8.

**Statement.** For continuous iid passage-time distributions satisfying the shape-theorem assumptions, prove that the deterministic limit shape is strictly convex.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Strict convexity of iid FPP limit shapes structural argument. Result: Finite geodesic uniqueness does not imply strict convexity of an asymptotic norm. For example, the strictly convex norms ||x||_p converge uniformly on compact sets to ||x||_infinity as p tends to infinity, and the latter unit ball has flat faces. Even stronger finite approximations can lose strictness in the limit.. Obstruction: This is a counterexample to an inference about limits, not an iid FPP counterexample. A uniform quantitative gap in the triangle inequality is missing.. Verification: author_checked_limited_argument. No proof file recorded.

### P0100. Excluding axial facets and cubical FPP shapes

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Questions5,8,9, PDF pp.21 and24.

**Statement.** Rule out a cube as an iid FPP limit shape and, more strongly, rule out a boundary segment perpendicular to e1 at the axial boundary point; exhibit a nondegenerate law with no such axial segment.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Excluding axial facets and cubical FPP shapes structural argument. Result: The l_infinity unit ball satisfies every elementary symmetry and convexity condition of an FPP limit shape and has axial facets. The l1 unit ball also satisfies those conditions but has an axial corner. Thus the shape theorem's convexity and lattice symmetries permit both geometries.. Obstruction: One needs a property specific to iid optimization that excludes the cubical candidate; deterministic convex geometry alone supplies none.. Verification: author_checked_limited_argument. No proof file recorded.

### P0101. Classification of flat FPP boundary pieces

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Questions6-7, PDF p.24; definition of M_p, p.22.

**Statement.** For planar iid FPP, show that the only flat boundary portions are the oriented-percolation-cone portions associated, after rescaling, with a positive minimum edge weight carrying a sufficiently large atom.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Classification of flat FPP boundary pieces structural argument. Result: If tau_e>=1, then every path from0 to x costs at least ||x||_1, so the limit shape lies inside the l1 ball. An oriented path consisting entirely of unit-time edges attains this lower bound exactly. This explains the mechanism generating the known cone flats.. Obstruction: The mechanism proves why these flats occur, not why no alternative mechanism creates a flat segment away from that cone.. Verification: author_checked_limited_argument. No proof file recorded.

### P0102. Strong Busemann limits for subadditive arrays and FPP

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Questions10 and32, PDF pp.26 and113.

**Statement.** Find useful conditions ensuring almost-sure limits of X_(m,N)-X_(n,N), including FPP differences of passage times to receding hyperplanes.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Strong Busemann limits for subadditive arrays and FPP structural argument. Result: Let S be simple symmetric random walk and X_(m,n)=|S_n-S_m|. This is an integrable stationary ergodic subadditive array. For N with S_N>=2, X_(0,N)-X_(1,N)=S_1; for S_N<=-2 it equals -S_1. Both events occur infinitely often almost surely, so this Busemann difference does not converge.. Obstruction: Kingman's usual hypotheses are insufficient. FPP triangle bounds yield compact subsequences, but an additional uniqueness or directional structure is needed for a full limit.. Verification: author_checked_limited_argument. No proof file recorded.

### P0103. Uniform curvature of continuous-law FPP shapes

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question11, PDF p.31.

**Statement.** Prove that every continuous iid passage-time law with a compact limit shape has a uniform constant C>0 such that 1-mu(z)>=C min(mu(z-z1),mu(z-z2))^2 for boundary points z1,z2 and z=(1-lambda)z1+lambda z2.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Uniform curvature of continuous-law FPP shapes structural argument. Result: Strict convexity alone cannot imply this inequality. On the l_p unit ball for p>2, take z1=((1-t^p)^(1/p),t), z2=((1-t^p)^(1/p),-t), and their midpoint z. Then 1-||z||_p is asymptotic to t^p/p, whereas ||z-z_i||_p^2=t^2. Their ratio tends to0.. Obstruction: This is a norm counterexample to a proof strategy, not an FPP counterexample. Uniform lower curvature must be proved from the random model.. Verification: author_checked_limited_argument. No proof file recorded.

### P0104. Subdiffusive and KPZ passage-time fluctuation exponents

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Questions13 and15, PDF pp.34 and40; Section3.

**Statement.** Under suitable nondegenerate iid passage-time assumptions, prove a fluctuation exponent strictly below1/2, identify the planar exponent as1/3, and establish a positive exponent in a suitable dimension.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Subdiffusive and KPZ passage-time fluctuation exponents structural argument. Result: A variance upper bound of order n/log n does not establish an exponent below1/2. Indeed log(n/log n)/(2log n) tends to1/2. Sums of floor(n/log n) independent mean-zero variance-one variables realize that variance order in an elementary model.. Obstruction: Known sublinear-variance estimates leave a polynomial-exponent gap. An additional power saving, and a matching lower bound for identification, are required.. Verification: author_checked_limited_argument. No proof file recorded.

### P0105. High-dimensional limit of the FPP fluctuation exponent

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question14, PDF p.34.

**Statement.** Determine whether the dimension-dependent passage-time fluctuation exponent chi(d) tends to zero as d tends to infinity.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: High-dimensional limit of the FPP fluctuation exponent structural argument. Result: Embedding Z^d into Z^(d+1) with shared weights gives T_(d+1)<=T_d and hence mu_(d+1)<=mu_d. This ordering says nothing comparable about variance: a Bernoulli random variable is bounded above by the constant1 but has larger variance.. Obstruction: A distributional comparison controlling centered fluctuations across dimensions is missing. Monotonicity of means cannot supply it.. Verification: author_checked_limited_argument. No proof file recorded.

### P0106. Polynomial overlap of independent planar FPP geodesics

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question16, PDF p.42.

**Statement.** Show that two independent geodesics from0 to ne1, sampled in independent iid planar environments with the same law, have expected edge overlap at least n^a for some a>0.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Polynomial overlap of independent planar FPP geodesics structural argument. Result: Let E_r be the 8r+4 edges leaving the square[-r,r]^2, for r=0,...,n-1, and p_e=P(e belongs to the selected geodesic). Every path to ne1 crosses E_r, so sum_(e in E_r)p_e>=1. Independence and Cauchy-Schwarz give E|Gamma intersect Gamma'|=sum_e p_e^2 >= sum_(r=0)^(n-1)1/(8r+4) >=(1/8)log(2n+1).. Obstruction: This establishes only a logarithmic overlap lower bound. Improving shell-level spreading to a power requires model-specific concentration of geodesic locations.. Verification: author_checked_limited_argument. No proof file recorded.

### P0107. Critical Bernoulli FPP growth in three dimensions

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question19, PDF p.71.

**Statement.** For iid edge times0 with probability p_c(Z^3) and1 otherwise, determine whether E T(0,boundary B(n)) is comparable to log n.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Critical Bernoulli FPP growth in three dimensions structural argument. Result: Collapse every connected zero-edge cluster to a vertex and retain unit-cost edges between the resulting vertices. Passage time is precisely graph distance in this random quotient graph, counting the fewest positive edges needed to reach the target. In the original graph it is bounded above by the number of positive edges on a fixed n-step coordinate path.. Obstruction: The logarithmic estimate requires quantitative geometry of the cluster-adjacency quotient. The planar argument based on nested dual circuits has no direct three-dimensional counterpart.. Verification: author_checked_limited_argument. No proof file recorded.

### P0108. Sharp width threshold for the thin-cylinder FPP CLT

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question20, PDF p.72.

**Statement.** Determine the largest power alpha for which standardized passage times constrained to Z times[-n^alpha,n^alpha]^(d-1) converge to a standard normal law.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Sharp width threshold for the thin-cylinder FPP CLT structural argument. Result: At width0 the graph is a line, and the passage time to ne1 is exactly the sum of n iid edge weights. For a nondegenerate finite-variance law the classical iid CLT gives normalization sqrt(n Var(tau)) and mean n E(tau).. Obstruction: For growing width, competing paths introduce correlations and varying block sizes. The width0 reduction does not control how rapidly an approximately independent block decomposition deteriorates.. Verification: author_checked_limited_argument. No proof file recorded.

### P0109. Existence of finite FPP geodesics without distributional assumptions

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question21, PDF p.73.

**Statement.** For every iid finite nonnegative passage-time distribution in d>=3, prove that the infimum over finite paths between any two vertices is attained.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Existence of finite FPP geodesics without distributional assumptions structural argument. Result: If all edge times are at least a>0, a fixed connecting path of cost M bounds any competing path length by M/a; only finitely many simple paths of that length start at a fixed vertex, so a minimum exists. Without a positive lower bound, a deterministic ladder can fail: give each vertical edge from height j-1 to j on both rails weight2^(-j), and the rung at height k weight3*2^(-k). A route across at height k costs2+2^(-k), with infimum2 unattained.. Obstruction: The ladder environment is deterministic and spatially inhomogeneous, so it is only a counterexample to a general compactness inference. The iid critical case requires additional probabilistic structure.. Verification: author_checked_limited_argument. No proof file recorded.

### P0110. An iid FPP law with proved KPZ exponent relation

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question22, PDF p.89; equation4.19.

**Statement.** Exhibit a nondegenerate iid undirected FPP law with well-defined fluctuation and wandering exponents satisfying chi=2xi-1.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: An iid FPP law with proved KPZ exponent relation structural argument. Result: If a geodesic deviates transversely by n^xi and the norm has quadratic curvature, the deterministic excess norm over a displacement of length n has order n*(n^(xi-1))^2=n^(2xi-1). This yields the proposed balance only after assuming random fluctuations are of the same order.. Obstruction: Both the required exponent existence and error control when replacing random passage times by the norm remain unproved for a concrete iid law here. The balance calculation is conditional, not a proof.. Verification: author_checked_limited_argument. No proof file recorded.

### P0111. Infinitely many planar FPP geodesic rays for continuous laws

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Questions23-24, PDF p.91.

**Statement.** Prove that continuous iid planar passage-time distributions have infinitely many pairwise eventually disjoint geodesic rays; the source also asks for an example outside the percolation-cone class.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Infinitely many planar FPP geodesic rays for continuous laws structural argument. Result: Finite geodesic existence and finite lattice degree yield at least one ray: among geodesics to points tending to infinity, choose an infinite subsequence with a common first edge, then a common second edge, and continue. Every finite segment of the diagonal limit is minimizing.. Obstruction: This compactness proof gives one ray, not many eventually disjoint rays. Endpoint sequences in different directions could still share the same limiting tail without additional shape information.. Verification: author_checked_limited_argument. No proof file recorded.

### P0112. Full-sequence convergence of FPP geodesics to a ray

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question25, PDF p.92.

**Statement.** For iid passage-time laws with unique finite geodesics, determine whether the geodesics from0 to ne1 converge locally to a single infinite ray as n tends to infinity.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Full-sequence convergence of FPP geodesics to a ray structural argument. Result: The space of infinite rooted paths in a locally finite graph has a compact product topology after adjoining finite-path endpoints. Thus long finite geodesics admit subsequential limits. But the abstract sequence of paths alternating between two disjoint infinite branches has two subsequential limits and no full limit.. Obstruction: The example is not an iid lattice FPP counterexample. A uniqueness-of-limit or directional-coalescence argument is missing for the specified endpoint sequence.. Verification: author_checked_limited_argument. No proof file recorded.

### P0113. Almost-sure escape from a fixed midpoint in FPP

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question26, PDF p.92.

**Statement.** In uniquely geodesic planar iid FPP, prove that no fixed vertex belongs to geodesics from-ne1 to ne1 for infinitely many n.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Almost-sure escape from a fixed midpoint in FPP structural argument. Result: If a fixed vertex v belongs to infinitely many such geodesics, both endpoint distances from v tend to infinity. A diagonal subsequence of the two oriented halves produces a doubly infinite geodesic through v. Therefore absence of all bigeodesics would imply the target.. Obstruction: Neither a summable midpoint bound nor unconditional absence of bigeodesics is obtained. Later midpoint papers must be compared against this exact almost-sure quantifier.. Verification: author_checked_limited_argument. No proof file recorded.

### P0114. Uniqueness of planar directional geodesics in every fixed direction

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Questions27-28, PDF p.95.

**Statement.** Show that every deterministic direction belongs to the Licea-Newman full-measure set D: from a fixed lattice vertex there are almost surely not two distinct geodesic rays with that direction.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Uniqueness of planar directional geodesics in every fixed direction structural argument. Result: A full-measure deterministic set may omit the axis, for example[0,2pi) without0. Also, a random exceptional set can be nonempty almost surely while excluding each fixed angle almost surely: a singleton containing an independent uniform angle has this property.. Obstruction: Fubini-based almost-every-direction arguments do not settle even a prescribed exceptional angle. A geometric argument sensitive to that direction is needed.. Verification: author_checked_limited_argument. No proof file recorded.

### P0115. Coalescence of directional FPP rays in higher dimensions

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question29, PDF p.97; Theorem4.22, p.96.

**Statement.** Extend the planar coalescence conclusion to higher dimensions: for a fixed direction with almost-sure uniqueness of a directional ray from each vertex, must directional rays from different vertices coalesce?

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Coalescence of directional FPP rays in higher dimensions structural argument. Result: Translation invariance and one outgoing edge at every vertex do not force coalescence. Orient every edge line in the positive e1 direction in Z^d. There is exactly one forward ray from each vertex, but rays on different parallel lines never meet.. Obstruction: This is a forest counterexample to a proof strategy, not the iid FPP model. Planar shielding and ordering used in the source proof do not extend automatically.. Verification: author_checked_limited_argument. No proof file recorded.

### P0116. Growth of the infinite-descendant part of the FPP geodesic tree

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question30, PDF p.97.

**Statement.** Let f(r) count edges meeting the Euclidean circle of radius r that belong to infinitely many finite geodesics from0. Determine whether f(r) tends to infinity, and at what rate.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Growth of the infinite-descendant part of the FPP geodesic tree structural argument. Result: In a locally finite rooted tree, an edge has infinitely many descendants exactly when it lies on an infinite ray, by the finite-branching compactness lemma. If the tree has infinitely many ends, then for every k one can choose k rays with disjoint tails outside some fixed ball; each tail crosses every sufficiently large circle. Consequently f(r)>=k eventually.. Obstruction: This proves divergence conditional on infinitely many ends, without a rate. It supplies no unconditional ray multiplicity and no bound on where k rays separate.. Verification: author_checked_limited_argument. No proof file recorded.

### P0117. Absence of bi-infinite geodesics in planar iid FPP

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question31, PDF p.98.

**Statement.** For nondegenerate continuous iid planar passage-time laws in the usual positive-speed regime, determine whether a bi-infinite geodesic exists.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Absence of bi-infinite geodesics in planar iid FPP structural argument. Result: Taking geodesics between-ne1 and ne1 gives candidate long paths, but a compactness argument produces a bi-infinite limit through a bounded region only if their distance from that region is tight along a subsequence. Paths can escape every fixed ball while connecting endpoints on opposite sides.. Obstruction: Finite-geodesic existence does not give the required anchoring. Proving or ruling out such anchoring under iid passage weights remains unresolved here.. Verification: author_checked_limited_argument. No proof file recorded.

### P0118. Noncircular low-dimensional Eden limit shape

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question33, PDF p.130; model definition pp.128-129.

**Statement.** Prove that the Eden model's limit shape is not a Euclidean ball in the dimensions left open by existing high-dimensional results, in particular dimension2.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Noncircular low-dimensional Eden limit shape structural argument. Result: With independent rate-one clocks on currently available boundary vertices, the next added vertex is uniform and the holding time is exponential with rate equal to their number. In edge-clock growth, a vertex with k infected neighbors has k active edge clocks and hence total rate k. A boundary vertex with two infected neighbors is selected twice as often as one with a single neighbor in that version.. Obstruction: This identifies the correct finite-state generator and prevents a model substitution, but the angular growth rate does not close as a function of the current radius. No anisotropic limit-shape inequality is obtained.. Verification: author_checked_limited_argument. No proof file recorded.

### P0119. Noncoexistence of unequal-speed Richardson infections

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Questions34-35, PDF pp.134-135.

**Statement.** Show that two-type Richardson growth on Z^d, d>=2, from distinct finite seeds cannot coexist indefinitely at unequal infection speeds; establish the proposed monotonicity in relative speed if that route is valid.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Noncoexistence of unequal-speed Richardson infections structural argument. Result: A common-clock monotone comparison of one infection's absolute size does not imply monotonicity of coexistence, because the latter requires both species to remain infinite. On Z with seeds at0 and1, every site at most0 can only be reached first through the left seed and every site at least1 through the right seed; with positive finite passage times both species survive for every speed ratio.. Obstruction: The one-dimensional example shows the essential role of bypass geometry and is excluded from the intended d>=2 conclusion. A coupling controlling the joint survival event in higher dimensions remains missing.. Verification: author_checked_limited_argument. No proof file recorded.

### P0120. Strict interface speedup in half-plane inhomogeneous FPP

**Source.** Auffinger, Damron and Hanson: 50 years of first-passage percolation (fpp_survey_2015), Question38, PDF p.142.

**Statement.** Characterize the pairs of iid half-plane edge laws F_minus,F_plus for which vertical growth along their interface is strictly faster than in either homogeneous model.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Strict interface speedup in half-plane inhomogeneous FPP structural argument. Result: For constant times a on one half-plane and b on the other, let c=min(a,b)>0. Every path with vertical displacement n costs at least cn. A path taking a bounded horizontal detour into the cheaper half-plane, moving n steps vertically, then returning costs cn+O(1). Thus the interface time constant is exactly c, so there is no strict speedup beyond both homogeneous models.. Obstruction: Random switching between regions may exploit complementary favorable segments. The deterministic comparison cannot characterize when that advantage is strictly positive.. Verification: author_checked_limited_argument. No proof file recorded.

### P0121. Uniform Lipschitz height models and their interfaces

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problems2.2-2.3, PDF pp.15-16.

**Statement.** Establish Gaussian-free-field scaling and SLE4 interface limits for the source's uniform odd-integer triangular-lattice heights, and for its uniform real-valued Lipschitz heights with the appropriate boundary amplitude.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Uniform Lipschitz height models and their interfaces structural reduction or obstruction. Result: Conditioning an interior height on all other heights gives a uniform law on its feasible interval, intersected with the odd integers in the discrete model. The interval endpoints are the maximum of neighbor heights minus the slope bound and the minimum plus the bound. Its conditional mean is the midpoint of these extrema, not generally the arithmetic mean of neighboring heights.. Obstruction: The discrete Gaussian harmonic-observable proof therefore does not transfer by replacing a Gaussian field with a uniform Lipschitz field. One must first control the effective large-scale field and then the discontinuous operation of extracting its zero interface.. Verification: author_checked_limited_argument. No proof file recorded.

### P0122. SLE4 from spectral truncations of the Gaussian free field

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem2.4, PDF p.16.

**Statement.** Project a planar Dirichlet Gaussian free field onto Laplace eigenmodes with eigenvalue magnitude at most R, add the harmonic extension of suitably chosen two-arc boundary values, and prove that the connecting zero interface converges to SLE4 as R tends to infinity.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: SLE4 from spectral truncations of the Gaussian free field structural reduction or obstruction. Result: Even uniform convergence of smooth functions does not make zero sets continuous. On a fixed square, h_n(x,y)=1/n has no zero set, whereas its uniform limit0 vanishes everywhere. With changing signs, n^(-1)sin(nx) also converges uniformly to0 but has many macroscopic vertical zero components.. Obstruction: These examples do not satisfy the prescribed random-field law or boundary data; they invalidate only the proposed continuous-mapping argument. Uniform control of near-zero topology and a characterization of the selected interface are missing.. Verification: author_checked_limited_argument. No proof file recorded.

### P0123. High-temperature triangular Ising interfaces converge to SLE6

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem2.5, PDF p.17, high-temperature portion.

**Statement.** For every fixed inverse temperature strictly between0 and the triangular Ising critical inverse temperature, prove convergence of the two-boundary-arc spin interface to chordal SLE6.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: High-temperature triangular Ising interfaces converge to SLE6 structural reduction or obstruction. Result: The high-temperature Gibbs law is not a small total-variation perturbation of independent spins uniformly over a growing domain. For n independent two-spin blocks with coupling beta>0, the average within-block product concentrates at tanh(beta), whereas at beta=0 it concentrates at0. Choosing a threshold halfway between these means distinguishes the two product laws with probability tending to1.. Obstruction: Thus finite-range or exponentially decaying local dependence does not justify global total-variation replacement. A renormalization or observable argument controlling crossing geometry is still needed for the actual triangular model.. Verification: author_checked_limited_argument. No proof file recorded.

### P0124. Critical planar random-cluster interfaces for general cluster weight

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problems2.6 and2.11, PDF pp.17-18.

**Statement.** For the square-lattice FK model at p=sqrt(q)/(1+sqrt(q)), q in(0,4), establish the predicted chordal SLE limit with kappa=4*pi/arccos(-sqrt(q)/2).

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Critical planar random-cluster interfaces for general cluster weight structural reduction or obstruction. Result: Given all edges except e, the FK conditional probability that e is open is p if its endpoints are already connected, and p/[p+q(1-p)] otherwise. At the proposed self-dual p these become sqrt(q)/(1+sqrt(q)) and1/(1+sqrt(q)). They straddle1/2 for q>1.. Obstruction: Self-duality supplies symmetry but not an independent percolation exploration law. The dependence on long-range connectivity prevents a direct reuse of the q=1 or q=2 observable argument.. Verification: author_checked_limited_argument. No proof file recorded.

### P0125. Conformal limits of the critical and dense O(n) loop model

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem2.7, PDF p.17.

**Statement.** For the hexagonal O(n) loop model, establish the predicted SLE limits of a boundary-to-boundary strand at the critical edge weight and in the dense phase.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Conformal limits of the critical and dense O(n) loop model structural reduction or obstruction. Result: Deleting all closed loops from a configuration does not give a self-avoiding walk with weights depending only on its length. The marginal weight of a strand gamma is proportional to x^|gamma| times the partition function of loops compatible with gamma. Two equal-length strands may leave different complementary regions and therefore different loop partition functions.. Obstruction: The environmental partition-function factor is the missing ingredient in a reduction to self-avoiding walk. Its conformal asymptotics have not been derived here.. Verification: author_checked_limited_argument. No proof file recorded.

### P0126. Planar uniform lattice-tree diameter and scaling limit

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem2.8, PDF p.18.

**Statement.** Determine the expected Euclidean diameter growth and the rescaled random-set limit of the uniform n-vertex lattice tree containing the origin, in particular on the planar square lattice.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Planar uniform lattice-tree diameter and scaling limit structural reduction or obstruction. Result: Every such planar tree has Euclidean diameter at most n-1. If its diameter is D, all its vertices lie in an axis-aligned square of side at most2D around any chosen vertex, containing at most(2D+1)^2 lattice points. Hence D is at least(sqrt(n)-1)/2, deterministically.. Obstruction: The interval between square-root and linear growth is too wide to identify the exponent. Expected-diameter normalization also gives no tightness of the full tree geometry by itself.. Verification: author_checked_limited_argument. No proof file recorded.

### P0127. Efficient approximately uniform sampling of lattice trees

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem2.9, PDF p.18.

**Statement.** Give a provably efficient algorithm to sample approximately uniformly from the n-vertex lattice trees containing the origin, or prove an appropriate computational obstruction.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Efficient approximately uniform sampling of lattice trees structural reduction or obstruction. Result: All eligible trees lie in the radius n-1 lattice ball. Enumerating all subsets of its edges, retaining exactly the connected acyclic n-vertex subsets containing0, and choosing a uniformly random retained index gives an exact finite sampler. On Z^2 the ambient edge count is O(n^2), so the naive running time is at most exponential in n^2.. Obstruction: This supplies existence and exactness but fails efficiency. The later Fredes-Marckert survey constructs uniform-stationary chains; their existence alone does not provide a polynomial mixing bound.. Verification: author_checked_limited_argument. No proof file recorded.

### P0128. Cardy conformal invariance for Voronoi percolation

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem2.12, PDF p.19.

**Statement.** Prove the analogue of Smirnov's crossing-probability theorem for critical planar Voronoi percolation, with the corresponding conformally invariant interface limit.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Cardy conformal invariance for Voronoi percolation structural reduction or obstruction. Result: A planar conformal map f sends a homogeneous Poisson process of intensity lambda to an inhomogeneous process whose intensity at w is lambda/|f'(f^(-1)(w))|^2. Thus exact rotation and translation symmetry of the original process do not produce exact invariance under arbitrary conformal maps.. Obstruction: One would need to prove that a smoothly varying local intensity does not affect the limiting critical crossing law. The Jacobian computation exposes that missing universality step without proving it.. Verification: author_checked_limited_argument. No proof file recorded.

### P0129. Cardy conformal invariance for Boolean continuum percolation

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem2.13, PDF p.19.

**Statement.** Establish Smirnov-type conformally invariant critical crossing limits for the planar Poisson Boolean model of equal-radius disks.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Cardy conformal invariance for Boolean continuum percolation structural reduction or obstruction. Result: Scaling space by1/r maps intensity1 centers with disk radius r to radius-one disks whose centers have intensity r^2. Therefore all Euclidean-scale behavior depends on the dimensionless product lambda*r^2 for general intensity lambda. Under a nonaffine conformal map, however, each disk is deformed and its local size depends on position.. Obstruction: The scalar scaling relation does not control spatially inhomogeneous radii and noncircular images under conformal maps. Proving their irrelevance at criticality remains the obstruction.. Verification: author_checked_limited_argument. No proof file recorded.

### P0130. Sharp planar one-arm probability beyond its exponent

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem3.1, PDF p.20, one-arm remainder.

**Statement.** Improve the critical triangular-percolation one-arm probability R^(-5/48+o(1)) to sharp multiplicative asymptotics, at least bounds by constant multiples of R^(-5/48).

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Sharp planar one-arm probability beyond its exponent structural reduction or obstruction. Result: Quasi-multiplicative information and a logarithmic exponent need not imply a constant asymptotic amplitude. For alpha>0 and0<a<alpha, define f(R)=R^(-alpha)*exp(a*sin(log R)), R>=1. Then f is decreasing, has logarithmic exponent-alpha, and obeys exp(-3a)<=f(RS)/(f(R)f(S))<=exp(3a), but R^alpha f(R) has no limit.. Obstruction: This is a scalar obstruction to extracting an asymptotic constant from coarse multiplicativity. It is not a percolation counterexample, and even constant-factor bounds for the specified probability are not proved by it.. Verification: author_checked_limited_argument. No proof file recorded.

### P0131. Exact critical percolation chemical-distance exponent

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem3.3, PDF p.20.

**Statement.** Determine the exponent alpha for the expected length of the shortest left-right critical percolation crossing of a square of side R, conditional on a crossing existing.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Exact critical percolation chemical-distance exponent structural reduction or obstruction. Result: A shortest crossing may be chosen self-avoiding by deleting loops. Its length is at least a constant times R and at most the number of sites in the square, which is O(R^2). Thus any exponent defined by the stated expectation must lie in[1,2].. Obstruction: These geometric bounds do not quantify the critical detours around closed clusters. Interface dimensions are not automatically dimensions of shortest open crossings.. Verification: author_checked_limited_argument. No proof file recorded.

### P0132. Measurable loop erasure of planar Brownian motion

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem6.1, PDF p.24; Berestycki-Sauzedde2026, Section7 first question.

**Statement.** In the joint scaling limit of a planar random walk and its loop erasure, determine whether the SLE2 path is a measurable function of the Brownian path.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Measurable loop erasure of planar Brownian motion structural reduction or obstruction. Result: For random elements(G,W) in standard Borel spaces, G is measurable from W exactly when the regular conditional distribution Law(G|W) is a point mass almost surely. An arbitrary measurable choice of a point in each fiber is insufficient: if G is standard normal and W=|G|, choosing the positive preimage changes the joint law, whose conditional signs remain fair.. Obstruction: No degeneration of the conditional SLE law given the complete Brownian chronology has been shown. The new forward map does not provide this missing conditional-law argument.. Verification: author_checked_limited_argument. No proof file recorded.

### P0133. Torus spanning-tree dual homotopy distribution

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem6.2, PDF p.24.

**Statement.** Determine the limiting distribution of the homotopy classes of the three edge-simple noncontractible closed paths in the dual complement of a uniform spanning tree on a fine toroidal square grid.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Torus spanning-tree dual homotopy distribution structural reduction or obstruction. Result: On a toroidal N-vertex square grid, E=2N and there are N faces. Removing the N-1 primal tree edges leaves N+1 dual edges. The dual complement is connected, so its first Betti number is(N+1)-N+1=2. This explains two independent topological cycles but does not itself specify the triple of simple-loop homotopy classes.. Obstruction: Rank2 determines neither winding slopes nor their probabilities. A scalar Laplacian determinant counts all spanning trees without resolving this joint topological information.. Verification: author_checked_limited_argument. No proof file recorded.

### P0134. A nontrivial exact Hausdorff gauge for SLE

**Source.** Schramm: Conformally invariant scaling limits, overview and collection of problems, 2006v2 (schramm_2006_v2), Problem7.1, PDF p.25.

**Statement.** Find a nontrivial Hausdorff gauge measure for SLE_kappa, kappa<8, which is sigma-finite and preferably finite on compact subarcs, as intended by the source's natural-parametrization question.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: A nontrivial exact Hausdorff gauge for SLE structural reduction or obstruction. Result: Hausdorff dimension alone cannot select the exact gauge. For any set of dimension d, a power exponent s>d gives zero Hausdorff measure, while s<d gives infinite measure; at s=d either zero, finite positive, or infinite behavior can occur. Multiplying r^d by a slowly varying factor can change the critical measure while leaving the dimension unchanged.. Obstruction: One needs fine local occupation estimates, not just dimension or existence of Minkowski content. The predicted logarithmic correction has not been proved here.. Verification: author_checked_limited_argument. No proof file recorded.

### P0135. Almost-sure fibers of chronological loop addition

**Source.** Berestycki and Sauzedde: Brownian paths as loop-decorated SLEs,2026 (brownian_loop_sle_2026), Section7, Almost sure(non-)injectivity.

**Statement.** Determine whether the chronological attachment map from a typical SLE2 path and the intersected Brownian loops to the resulting Brownian path has a unique preimage almost surely, or instead infinitely many.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Almost-sure fibers of chronological loop addition structural reduction or obstruction. Result: Global noninjectivity cannot settle almost-sure invertibility. The map f:R->R with f(0)=f(1)=0 and f(x)=x otherwise is noninjective, yet it is injective off the two-point set and therefore injective on a full-measure set for a continuous input law. Conversely, x->|x| has two typical preimages for a symmetric continuous law.. Obstruction: One must exhibit an ambiguity mechanism occurring on a positive-probability or full-probability family of loop configurations. A deterministic exceptional pair or a measurable selection theorem does not do this.. Verification: author_checked_limited_argument. No proof file recorded.

### P0136. Chronological Brownian loop addition in three dimensions

**Source.** Berestycki and Sauzedde: Brownian paths as loop-decorated SLEs,2026 (brownian_loop_sle_2026), Section7, Dimension3.

**Statement.** Extend the chronological loop-decoration representation to the three-dimensional scaling limit of loop-erased random walk, yielding the full parametrized Brownian path rather than only equality of random ranges.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Chronological Brownian loop addition in three dimensions structural reduction or obstruction. Result: A fixed planar circle intersecting a line in R^3 becomes disjoint from that line after an arbitrarily small translation in the perpendicular direction. For example, gamma is the x-axis segment[-2,2] and ell is the unit circle in the xy-plane; ell+(0,0,epsilon) avoids gamma for every epsilon nonzero while converging uniformly to ell.. Obstruction: Attaching or omitting a loop of fixed diameter changes the resulting path macroscopically. Typical random intersections need a stability argument beyond deterministic uniform closeness; the example does not refute such an almost-sure statement.. Verification: author_checked_limited_argument. No proof file recorded.

### P0137. A loop-erased representation of a unit Brownian loop

**Source.** Berestycki and Sauzedde: Brownian paths as loop-decorated SLEs,2026 (brownian_loop_sle_2026), Section7, SLE2 loop analogue.

**Statement.** Describe a unit Brownian loop as an SLE2-type loop decorated by an independent Brownian loop soup, with a precise law and chronology.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: A loop-erased representation of a unit Brownian loop structural reduction or obstruction. Result: Even in a finite closed walk, rooting before chronological loop erasure can discard all information: the standard loop erasure of a finite walk ending at its starting vertex is the single starting vertex. When the terminal return is processed, it erases the whole currently retained path.. Obstruction: A nontrivial loop analogue cannot simply apply the open-path loop-erasure algorithm to an arbitrarily rooted closed Brownian path. A cyclic or marked-edge construction and its resulting sampling bias remain to be established.. Verification: author_checked_limited_argument. No proof file recorded.

### P0138. Law of loop-decorated SLE beyond kappa2

**Source.** Berestycki and Sauzedde: Brownian paths as loop-decorated SLEs,2026 (brownian_loop_sle_2026), Section7, Other values of kappa.

**Statement.** Identify the chronological path law obtained by decorating chordal SLE_kappa with Brownian loops at restriction intensity lambda=(8-3*kappa)*(6-kappa)/(2*kappa), including its proposed interpretation as partially erased Brownian motion.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Law of loop-decorated SLE beyond kappa2 structural reduction or obstruction. Result: At kappa2 the displayed intensity is1; at kappa8/3 it is0. Agreement of the filled hull with a restriction law cannot identify the ordered path: a circle traversed clockwise or counterclockwise has the same trace and hull, and arbitrary monotone time changes also preserve the hull.. Obstruction: Restriction formulas control avoidance of sets, not chronological finite-dimensional distributions or quadratic variation. A path-level stochastic characterization is missing.. Verification: author_checked_limited_argument. No proof file recorded.

### P0139. Rough-path continuity of chronological loop attachment

**Source.** Berestycki and Sauzedde: Brownian paths as loop-decorated SLEs,2026 (brownian_loop_sle_2026), Section7, Continuity in rough path topologies.

**Statement.** Prove appropriate Holder, p-variation, or rough-path continuity estimates for the chronological loop-attachment map, possibly restricted to the cusp conditions proposed by the authors.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Rough-path continuity of chronological loop attachment structural reduction or obstruction. Result: Concatenate m positively oriented circles of radius m^(-1/2), each based at0, over a unit time interval. Their sup norm tends to0 and, for p>2, their first-level p-variation is at most C_p*m^(1/p-1/2), which also tends to0. But their total signed area is m*pi*m^(-1)=pi.. Obstruction: This proves that first-level convergence alone cannot control the second iterated integral. It does not rule out continuity with properly enhanced input loops or the source's additional cusp restrictions.. Verification: author_checked_limited_argument. No proof file recorded.

### P0140. Random critical drift in the annealed thinned Levy process

**Source.** Van der Hofstad: Stochastic processes on random graphs, Saint-Flour2017 (rhofstad_saintflour_2017), Open Problem4.1, PDF p.210; equations4.5.5 and4.5.20.

**Statement.** Explain directly how mixing the heavy-tailed degree weights yields the independent-increment iid-degree exploration limit.

**Status.** Historical status: source_says_open. Current-literature status: resolved_in_literature (no status-search record.). Admission: not admitted; result_status: literature_result_rederived_with_scope_correction.

**Our work.** Method: Marked Poisson process and exact random-slope cancellation; separate mixed-Laplace stress test. Result: For PPP weights with intensity(tau-1)c*x^(-tau)dx and exponential marks of rate x/mu, the random drift Z/mu cancels the empirical quadratic compensator and leaves independent increments from a deterministic marked-Poisson intensity. With a deterministic drift, a mixed log-Laplace difference is positive for small a, so increments are dependent.. Obstruction: No unproved theorem is claimed: the corrected law was already identified indirectly in2019. Exact source normalization and later availability of the direct proof are retained as scope/novelty limits.. Verification: author_checked_proof_text. No proof file recorded.

### P0141. First-order distance constants in finite-variance preferential attachment

**Source.** Van der Hofstad: Stochastic processes on random graphs, Saint-Flour2017 (rhofstad_saintflour_2017), Open Problem2.3, PDF p.74.

**Statement.** For affine preferential attachment with m>=2 and delta>0, prove convergence of typical graph distance/log n and diameter/log n to explicit positive constants a<b.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: First-order distance constants in finite-variance preferential attachment structural reduction. Result: For every connected graph, the distance D(U,V) between two uniform vertices is bounded by its diameter, so if the two normalized quantities converge in probability to constants a,b then necessarily a<=b. Strict inequality does not follow: a complete graph has typical distance and diameter both1 with probability tending to1.. Obstruction: This gives only the necessary weak ordering. The preferential-attachment age correlations and extreme peripheral vertices must be quantified to identify constants and show a strict gap.. Verification: author_checked_limited_argument. No proof file recorded.

### P0142. Fluctuations of preferential-attachment distances and diameter

**Source.** Van der Hofstad: Stochastic processes on random graphs, Saint-Flour2017 (rhofstad_saintflour_2017), Open Problem2.4, PDF p.76.

**Statement.** Determine the centered fluctuation scales and limiting laws for typical distances and diameter in affine preferential-attachment graphs with m>=2.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Fluctuations of preferential-attachment distances and diameter structural reduction. Result: If integer-valued X_n is centered by real c_n, every centered value lies in Z-c_n. Along a subsequence with fractional parts c_n tending to r, any weak limit is supported on Z-r. Two subsequences whose fractional parts have different limits can therefore have incompatible translated-lattice limits.. Obstruction: A claimed continuous full-sequence limit without additional scaling would require checking this lattice obstruction. No centered distance law for the actual attachment model is obtained.. Verification: author_checked_limited_argument. No proof file recorded.

### P0143. Second-order extremal hopcount in exponential complete-graph FPP

**Source.** Van der Hofstad: Stochastic processes on random graphs, Saint-Flour2017 (rhofstad_saintflour_2017), Open Problem3.1, PDF pp.99-100.

**Statement.** Determine fluctuations of the longest minimum-weight path, both from a fixed root and over all vertex pairs, beyond the first-order e log n and alpha_star log n scales.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Second-order extremal hopcount in exponential complete-graph FPP structural reduction. Result: For a random recursive tree, F_n(z)=E sum_v z^(depth(v)) equals product_(j=1)^(n-1)(1+z/j). For z>1, P(height>=k)<=z^(-k)F_n(z)<=exp(z H_(n-1)-k log z). Taking k=a log n,z=a gives an upper exponent a-a log a. A union bound over n roots adds1, explaining alpha_star log(alpha_star)-alpha_star=1.. Obstruction: This recovers a first-order upper bound only. It loses dependence between extreme paths and the logarithmic corrections needed for a fluctuation law.. Verification: author_checked_limited_argument. No proof file recorded.

### P0144. Conservative weighted-distance fluctuations in heavy-tailed configuration models

**Source.** Van der Hofstad: Stochastic processes on random graphs, Saint-Flour2017 (rhofstad_saintflour_2017), Open Problem3.2, PDF p.142.

**Statement.** Describe the fluctuations of the minimal total weight between two typical vertices of an infinite-variance configuration model when the associated weighted branching process is conservative.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Conservative weighted-distance fluctuations in heavy-tailed configuration models structural reduction. Result: For nonnegative weights, a path sum is at least its maximum edge, so the FPP distance dominates the minimax path value. The latter is exactly the smallest level t at which the two vertices are connected using edges of weight at most t. This follows by comparing the same path family under the two objectives.. Obstruction: The lower bound tracks the largest obstruction but discards accumulated small costs. In the conservative regime infinitely many layers can contribute, so the minimax comparison does not determine centered sum fluctuations.. Verification: author_checked_limited_argument. No proof file recorded.

### P0145. Hopcount universality in infinite-variance weighted configuration models

**Source.** Van der Hofstad: Stochastic processes on random graphs, Saint-Flour2017 (rhofstad_saintflour_2017), Open Problem3.3, PDF p.142.

**Statement.** Determine the scaling and possible central limit laws for the number of edges on a minimum-weight path between typical vertices of an infinite-variance configuration model.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Hopcount universality in infinite-variance weighted configuration models structural reduction. Result: If all weights lie in[a,b] with0<a<=b, the hopcount H of a minimizing path and graph distance d satisfy d<=H<=(b/a)d: a shortest unweighted path costs at most bd, whereas the chosen path costs at least aH. Monotone transformations do not preserve hopcount: paths with weights(1,4) and(1.8,1.8,1.8) reverse their cost ordering when weights are squared.. Obstruction: A bounded-factor comparison gives no fluctuation law, and it disappears for weights approaching0. The exploration process must jointly control accumulated cost and generation depth.. Verification: author_checked_limited_argument. No proof file recorded.

### P0146. Weak-to-strong disorder universality in complete-graph FPP

**Source.** Van der Hofstad: Stochastic processes on random graphs, Saint-Flour2017 (rhofstad_saintflour_2017), Open Problem3.4, PDF p.149 and discussion p.154.

**Statement.** Complete the classification of complete-graph first-passage percolation with varying edge-weight distributions, including the strong-disorder regime related to the minimum spanning tree.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Weak-to-strong disorder universality in complete-graph FPP structural reduction. Result: For any positive edge labels a_e and any simple path of at most n-1 edges, max a_e^s <= sum a_e^s <=(n-1)max a_e^s. Taking infima over paths and s-th roots shows that the FPP value lies between the minimax value M and(n-1)^(1/s)M. If s/log n tends to infinity, this ratio bound tends to1.. Obstruction: Nearly equal objective values may be attained by very different paths. This deterministic estimate does not identify the hopcount crossover or a metric-space scaling limit.. Verification: author_checked_limited_argument. No proof file recorded.

### P0147. Fluctuations of weighted flooding and diameter on configuration models

**Source.** Van der Hofstad: Stochastic processes on random graphs, Saint-Flour2017 (rhofstad_saintflour_2017), Open Problem3.5, PDF pp.150-151.

**Statement.** Identify centered fluctuation laws for exponential-weight flooding time and weighted diameter in the configuration-model regimes of Theorem3.37.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Fluctuations of weighted flooding and diameter on configuration models structural reduction. Result: On any fixed graph, the minimum incident exponential edge weight at a degree-d vertex is Exp(d). For a collection of m pairwise nonadjacent degree-d vertices these minima use disjoint edge sets and are independent. Hence P(d max X_v-log m<=x)=(1-exp(-x)/m)^m tends to exp(-exp(-x)).. Obstruction: This identifies one endpoint-delay component of the extremes. The bulk connecting distances and their dependence on the extreme endpoints are not controlled, so no full flooding or diameter limit is claimed.. Verification: author_checked_limited_argument. No proof file recorded.

### P0148. General edge-weight laws for random-graph flooding and diameter

**Source.** Van der Hofstad: Stochastic processes on random graphs, Saint-Flour2017 (rhofstad_saintflour_2017), Open Problem3.6, PDF p.152.

**Statement.** Extend weighted flooding-time and diameter asymptotics from exponential weights to general iid nonnegative edge-weight laws on the configuration model.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: General edge-weight laws for random-graph flooding and diameter structural reduction. Result: At a degree-d vertex the minimum incident weight X has tail P(X>t)=(1-F(t))^d. Over m nonadjacent such vertices, P(max X_v<=t)=[1-(1-F(t))^d]^m. For weights E^s this gives max X_v asymptotic to(log m/d)^s in probability.. Obstruction: Endpoint delays alone can change scale, but the fastest route through the bulk is a different optimization. Matching these two mechanisms for general F is still missing.. Verification: author_checked_limited_argument. No proof file recorded.

### P0149. Extreme hopcounts for general random-graph degree and weight laws

**Source.** Van der Hofstad: Stochastic processes on random graphs, Saint-Flour2017 (rhofstad_saintflour_2017), Open Problem3.7, PDF p.152.

**Statement.** Determine the first-order extreme hopcount from one root and over all pairs for general configuration-model degree laws, and extend beyond exponential edge weights.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Extreme hopcounts for general random-graph degree and weight laws structural reduction. Result: On a graph with maximum degree Delta, there are at most n*Delta*(Delta-1)^(k-1) oriented simple k-edge paths. With iid weights Y, the chance any such path has total weight at most t is at most this count times exp(a*t)*(E exp(-aY))^k for every a>0.. Obstruction: The bound is too crude when a few hubs make Delta large and does not automatically constrain minimizing paths with unknown total cost. Degree-biased branching and extreme endpoint selection require sharper control.. Verification: author_checked_limited_argument. No proof file recorded.

### P0150. Minimal assumptions for heavy-tailed critical metric convergence

**Source.** Van der Hofstad: Stochastic processes on random graphs, Saint-Flour2017 (rhofstad_saintflour_2017), Open Problem4.2, PDF p.218; Theorem4.39.

**Statement.** Remove the extra degree restrictions used to upgrade heavy-tailed critical configuration-model components from Gromov-weak convergence to Gromov-Hausdorff-Prokhorov convergence.

**Status.** Historical status: source_says_open. Current-literature status: unverified (no status-search record.). Admission: admitted; result_status: attempted_unsolved.

**Our work.** Method: Minimal assumptions for heavy-tailed critical metric convergence structural reduction. Result: Let X_n=[0,1] with the ordinary metric and probability measure(1-1/n)delta_0+(1/n)Lebesgue. Every fixed finite iid sample from this measure lies at0 with probability tending to1, so its distance matrices converge to those of a point. Yet the spaces all have diameter1 and cannot converge in Gromov-Hausdorff distance to a point.. Obstruction: This is a precise failure of weak measured convergence to control thin appendages. A uniform lower bound on masses of fixed-radius balls is the missing type of estimate.. Verification: author_checked_limited_argument. No proof file recorded.

