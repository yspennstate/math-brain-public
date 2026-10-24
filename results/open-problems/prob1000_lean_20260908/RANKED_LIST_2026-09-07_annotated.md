# The campaign's open problems ranked from easy to hard (2026-09-07, 12:5x his clock)

558 distinct open problems (430 from the Codex campaign ledger after removing its 26 copies of Claude-intake problems, 128 from the Claude intake, three of them added at 12:5x from the Haggstrom-Jonasson uniqueness survey; literature exclusions are not listed, among them two found this hour: the near-extremal DGFF profile is a 2024 theorem of Biskup, Gufler and Louidor, and the two-site ballisticity criterion is refuted by Fribergh and Kious). Ranked by the Fable agent's own reading of each problem's title, statement, recorded attempt and obstruction, against the rubric below. The rank is a judgment, author-checked only: it says how far the recorded attempts got and how the problem sits in its field, not how long a solution would take. Within a tier the order is by id, not by difficulty.

Rubric:

- Tier 1, tractable now: a candidate proof, counterexample or partial result is already on file, or the problem reduces to known theorems or a finite computation
- Tier 2, specific technical question: the tools exist, a moderate new idea or a careful verification is needed
- Tier 3, hard research problem: a genuinely new idea or a large technical machine is needed, but the problem is not a landmark
- Tier 4, major open problem of its area: decades old, many attempts, known walls
- Tier 5, famous field-defining conjecture

Counts: tier 1: 24, tier 2: 52, tier 3: 346, tier 4: 117, tier 5: 19

## Tier 1

Tier 1, tractable now: a candidate proof, counterexample or partial result is already on file, or the problem reduces to known theorems or a finite computation

| id | problem | attempt status | why this tier |
|---|---|---|---|
| P0032 | Embedding an equivalent Brownian law by adding a finite prefix | candidate_fu | candidate full construction recorded |
| P0033 | Ergodicity of stationary Galton-Watson flows | candidate_fu | candidate counterexample recorded |
| P0174 | Sharp support-diameter threshold for free Brownian unimodality | candidate_fu | candidate sharp constant C=1 recorded |
| P0189 | Brown-measure convergence from general strong convergence | candidate_fu | candidate counterexample recorded |
| P0193 | Eventual log-unimodality from arbitrary compact positive initial laws | candidate_fu | candidate negative answer recorded |
| P0205 | Metropolis relaxation for geometric-time Cayley targets | partial_coun | partial counterexample recorded |
| P0208 | Extremal arc-transitive walk parameters away from cycles | candidate_fu | candidate answer recorded, prior disposition to check |
| P0209 | Uniform stationary normal approximation from gap and bounded observable | candidate_fu | candidate proof recorded |
| P0266 | Critical variational SPDE maximal second-moment bound | candidate_fu | candidate counterexample recorded |
| P0267 | Endpoint energy-space continuity for critical variational SPDEs | candidate_fu | candidate counterexample recorded |
| P0276 | Product condition and cutoff for unweighted Abelian Cayley graphs | candidate_fu | candidate proof recorded |
| P0288 | Rank one polynomial asymptotics for lambda transient Markov chains | candidate_fu | candidate proof recorded |
| P0289 | Ross modulation monotonicity and a criterion for Cox workload ordering | candidate_pa | partial refutation recorded |
| P0340 | Growth of the minimal drawn length of critical beta-splitting trees | candidate_fu | candidate proof recorded |
| P0341 | Uniform occupation estimates and the polynomial-test ansatz | candidate_pa | partial result recorded |
| P0342 | Transferring a stationary fringe-process CLT to finite beta-splitting trees | candidate_pa | partial result recorded |
| P0347 | Distributions of balance indices for critical beta-splitting trees | candidate_pa | partial result recorded |
| P0355 | Endogeny of nonminimal discounted-tree fixed points | candidate_pa | degenerate partial result recorded |
| P0389 | Onset of mesoscopic hyperuniformity in the ARW free chain | candidate_pa | partial result recorded |
| P0390 | Hyperuniformity transition in stationary ARW wake states | candidate_pa | partial result recorded |
| P0411 | Boundary-hole monotonicity and coefficient positivity for ideal cells | candidate_pa | partial result recorded |
| P0429 | Largest growing fork-join batch compatible with asymptotic independence | candidate_pa | partial result recorded |
| P0458 | The standardized degree law in growing bilateral preference graphs | candidate_pa | partial result recorded |
| P0459 | Simultaneous concentration of bilateral preference degrees | candidate_pa | partial result recorded |

## Tier 2

Tier 2, specific technical question: the tools exist, a moderate new idea or a careful verification is needed

| id | problem | attempt status | why this tier |
|---|---|---|---|
| C0021 | Revealment exponent of the iterated 3-majority function | attempted_un | iterated 3-majority revealment; interval [0.166,0.369] proved |
| C0031 | Almost-sure convergence in the heavy-tailed circular law | attempted_un | a.s. heavy-tailed circular law; summable small-ball bound needed |
| C0033 | Concavity of the entropy of determinantal measures in the kernel | partial_resu | entropy concavity; 2x2 case first target, numerics clean |
| C0034 | Coupling of determinantal projection measures with union marginal | partial_resu | union-marginal coupling; LP evidence everywhere |
| C0035 | Determinantal processes with trigonometric-polynomial symbol as block factors | attempted_un | block factors for degree-m symbols; sublattice case done |
| C0036 | Fuglede-Kadison product-measure bounds for equivariant determinantal processes | partial_resu | FK domination; harmonic-mean bound proved, GM sharp numerically |
| C0039 | d-bar distance bound for commuting versus general equivariant kernels | attempted_un | d-bar linear bound for noncommuting kernels; S_3 test specified |
| C0057 | Filled-in peeling discovers the whole map for every critical weight sequence | attempted_un | peeling exhausts the map for all critical sequences; reduction done |
| C0062 | Uniqueness and description of the maximal-dimension Young diagram for finite n | partial_resu | max-dimension Young shape, verified n<=40 |
| C0075 | ISE scaling limit of critical high-dimensional percolation clusters of fixed siz | attempted_un | ISE limit, spread-out case conditional on Hara-Slade |
| C0089 | Quenched invariance principle for random walk on the vacant set of random interl | attempted_un | vacant-set QIP for all u<u*: PRS + sharpness |
| C0100 | Convergence of height-fraction statistics in the sandpile scaling limit | attempted_un | height-fraction convergence; conditional on transition layers |
| C0113 | Is the minimal spanning forest of a Poisson process in R^d a single tree for d > | attempted_un | Poisson MSF a tree in high d: conditional resolution, opposite sign |
| C0127 | Chaos versus superconcentration: an equivalent multiple-peaks condition | attempted_un | equivalent multiple-peaks condition; two-peak version refuted |
| C0129 | Recurrence-transience criterion for excited random walks under stationary ergodi | attempted_un | ERW criterion under SE; periodic case checks |
| C0130 | Escape probability of a transient one-dimensional excited random walk | attempted_un | escape probability of transient ERW; finite-state reduction |
| C0133 | Zero velocity on the non-transient event for excited random walks | attempted_un | zero velocity on recurrent event; done under BD given LD bound |
| C0134 | Ballisticity criterion under the positivity assumption instead of bounded stacks | attempted_un | ballisticity under POS1; expected via finite-mean migration |
| C0135 | Running-maximum limit theorem at the critical parameter delta = 1 under weaker a | attempted_un | delta=1 limit under (6.2); backtracking negligible |
| C0151 | Independent-set densities of random regular graphs as factors of i.i.d. on the t | attempted_un | Szegedy independent-set conjecture: refuted at the maximum by Rahman-Virag + Ding-Sly-Sun |
| P0001 | Negative correlation in uniform forests | partial_resu | cactus case done; matroid-circuit inequality is the gap |
| P0013 | Expected Lovasz theta of a dense independent-edge graph | attempted_un | expected Lovasz theta, dense random graph; sqrt n scale |
| P0023 | Efficient reflected-Brownian coupling in acute triangles | attempted_un | efficient coupling in acute triangles; spectral rate bound known |
| P0024 | Failure of synchronous contraction in a bounded planar domain | attempted_un | synchronous contraction failure; construct a domain |
| P0028 | Bounded independent Brownian pieces and two-sided Brownian motion | attempted_un | bounded independent pieces vs two-sided BM |
| P0029 | Separation of two peaks in random square-grid labelings | attempted_un | two-peak separation on grids; combinatorial counting |
| P0030 | Compatibility of forward and backward Brownian decompositions | attempted_un | forward/backward decomposition compatibility |
| P0031 | Sparse first-passage pieces in a forward Brownian concatenation | attempted_un | sparse first-passage pieces |
| P0039 | Positive-speed equivalence for Cayley percolation clusters | attempted_un | positive-speed equivalence; subexponential case done |
| P0050 | Singularity of distinct free and wired forest measures | attempted_un | singularity of distinct forest measures |
| P0087 | Forced network urn convergence and diffusion scaling | attempted_un | fixed-step convergence done; diffusion scaling open |
| P0088 | Matching local limits of Bernoulli and Poisson-outdegree attachment | attempted_un | local limits Bernoulli vs Poisson outdegree |
| P0090 | Multistate pivot-tree criterion for interpretation | attempted_un | multistate pivot-tree criterion |
| P0092 | Randomized tree automata and endogeny | attempted_un | randomized automata and endogeny; formulation issue |
| P0109 | Existence of finite FPP geodesics without distributional assumptions | attempted_un | geodesic existence without distributional assumptions |
| P0127 | Efficient approximately uniform sampling of lattice trees | attempted_un | efficient uniform sampling of lattice trees |
| P0133 | Torus spanning-tree dual homotopy distribution | attempted_un | torus spanning-tree dual homotopy distribution; computable |
| P0150 | Minimal assumptions for heavy-tailed critical metric convergence | attempted_un | minimal assumptions for heavy-tailed metric convergence |
| P0177 | Location of Brownian modes at large time | attempted_un | Brownian mode location at large time; partial asymptotics |
| P0218 | Growth exponents in the spatial city-formation model | attempted_un | city-formation exponents; one-sided bound done |
| P0220 | Explicit stationary law of the leftmost Hammersley drift-jump particles | attempted_un | explicit stationary law, Hammersley drift-jump |
| P0229 | Integrable supremum of routes to a bounded region | attempted_un | integrable supremum of routes |
| P0234 | A safe margin around extended initial color seeds | attempted_un | safe margin around color seeds |
| P0242 | Optimal stationary stopping under Markov-chain lumping | attempted_un | optimal stopping under lumping |
| P0245 | Exact minimum stationary cover time for reversible chains | attempted_un | minimum stationary cover time, reversible |
| P0255 | Variation of nearest-unvisited walk length under a random start | attempted_un | NUV length variation under random start |
| P0294 | Compute a first order bias correction for continuous workload mean field models | unsolved | first-order bias correction; solvable model done |
| P0336 | Selected limit of empirical Euclidean transport between separated rectangles | unsolved | selected limit between separated rectangles; partial computation |
| P0427 | Optimal allocation between two exponential parallelism classes | unsolved | two-class allocation; small cases solvable |
| P0439 | Server provisioning for a finite response-time SLO | unsolved | provisioning for a response-time SLO |
| P0441 | Deterministic DelayedOff waiting-power tradeoff | unsolved | DelayedOff tradeoff; idle-gap calculation done |
| P0456 | The fine connectivity window for bilateral preference graphs | unsolved | bilateral preference connectivity window; expansion known |

## Tier 3

Tier 3, hard research problem: a genuinely new idea or a large technical machine is needed, but the problem is not a landmark

| id | problem | attempt status | why this tier |
|---|---|---|---|
| C0002 | Fluctuations and large deviations of intermediate level sets of the 2D DGFF | attempted_un | fluctuations of intermediate level sets |
| C0003 | Bypassing the Laplace-transform tail condition for the DGFF extremal measure | attempted_un | bypassing the Laplace tail condition |
| C0004 | Explicit density of the position of the DGFF maximum | attempted_un | explicit density of the DGFF maximum position |
| C0005 | Size of deep extremal level sets of the 2D DGFF converges to the extremal measur | attempted_un | deep extremal level sets; equivalent to C0006 given UI |
| C0006 | Existence of the limit of e^{-alpha h} E nu(f_h) for the DGFF cluster law | attempted_un | cluster-size limit at depth h |
| C0008 | Universality of level sets and extremal process for log-correlated Gaussian fiel | attempted_un | universality for log-correlated fields (max known) |
| C0010 | DGFF over an ergodic uniformly elliptic random conductance model: level sets and | attempted_un | DGFF over random conductances (max known) |
| C0011 | Scaling limit of local-time level sets of planar random walk in the full range o | attempted_un | local-time level sets, full eta range |
| C0012 | Subdiffusive upper bound for the Liouville random walk on the DGFF | attempted_un | subdiffusive bound for the Liouville random walk |
| C0014 | Limit of the normalised log-effective resistance of the DGFF electric network | attempted_un | log effective resistance limit of DGFF network |
| C0020 | Optimal exponent for the computational complexity of randomised algorithms for p | attempted_un | optimal algorithmic complexity exponent for crossings |
| C0022 | Singularity of the scaling limits of the spectral sample and of the pivotal set | attempted_un | singularity of spectral and pivotal scaling limits |
| C0032 | Explicit form of the heavy-tailed circular law density | attempted_un | explicit heavy-tailed circular density |
| C0040 | Absolutely continuous invariant measure for the environment seen from the partic | attempted_un | invariant a.c. measure vs ballisticity under ERG |
| C0045 | Does positive velocity imply the polynomial ballisticity condition (P)_M? | attempted_un | positive velocity implies (P)_M |
| C0058 | A peeling algorithm exploring site percolation on Boltzmann maps | attempted_un | site-percolation peeling algorithm |
| C0059 | Transience of the dual infinite Boltzmann map for a in [2, 5/2) | attempted_un | dual Boltzmann map transience for a in [2,5/2); threshold expected |
| C0060 | Positivity of the vacant-set threshold u* for random interlacements on the Sierp | attempted_un | u* > 0 on gasket x Z |
| C0063 | Critical exponent beta = 1 in the asymptotic sense for high-dimensional percolat | attempted_un | beta = 1 asymptotically in high d |
| C0065 | Existence and equality of the supercritical exponents gamma', nu', nu_2' in high | attempted_un | supercritical exponents in high d |
| C0066 | Sharp intrinsic and extrinsic one-arm exponents in high dimensions | attempted_un | sharp one-arm constants in high d |
| C0067 | Notions of criticality for percolation on high-dimensional tori | attempted_un | torus criticality definitions |
| C0068 | Concentration and uniqueness of the giant component above the scaling window on  | attempted_un | giant uniqueness above the window on tori |
| C0070 | Discrete duality principle for hypercube percolation | attempted_un | hypercube duality principle |
| C0072 | Scaling of the largest critical cluster in a high-dimensional box under free, ze | attempted_un | box cluster scaling by boundary condition |
| C0073 | Critical exponent of the diffusion constant of random walk on the supercritical  | attempted_un | diffusion-constant exponent; product monotonicity proved |
| C0074 | Scaling limit of random walk on the high-dimensional incipient infinite cluster | attempted_un | walk on the high-d IIC scaling limit |
| C0076 | Super-Brownian motion limit of critical percolation clusters in high dimensions | attempted_un | SBM limit of critical clusters |
| C0077 | Incipient-infinite super-Brownian-motion limit of the high-dimensional IIC | attempted_un | IIC to incipient SBM |
| C0079 | Intrinsic-distance two-point function asymptotics in high dimensions | attempted_un | intrinsic two-point asymptotics |
| C0081 | Lace-expansion-free derivation and higher coefficients of the 1/d expansion of p | attempted_un | lace-free derivation and a_4 |
| C0082 | First coefficient where the 1/d expansions of p_c on Z^d and on the hypercube di | attempted_un | first differing coefficient Z^d vs hypercube; prediction a_4 |
| C0083 | Asymptotic expansion of the critical value of the Hamming graph | attempted_un | Hamming graph p_c expansion |
| C0085 | Two-point function of high-dimensional invasion percolation | attempted_un | invasion percolation two-point function |
| C0087 | Diameter of the minimal spanning tree on high-dimensional tori and the hypercube | attempted_un | MST diameter on tori |
| C0090 | Critical behaviour of scale-free percolation | attempted_un | scale-free percolation critical behaviour |
| C0097 | Divergence of the 1/d expansion of the connective constant | attempted_un | divergence of the connective-constant expansion |
| C0098 | Decidability of infinite toppling for i.i.d. sandpiles on Z^2 | attempted_un | decidability of infinite toppling |
| C0101 | Maximal integer superharmonic matrices in dimensions d >= 3 | attempted_un | maximal superharmonic matrices in d>=3 |
| C0105 | Multiscale decomposition of the actual zeta function with self-similar increment | attempted_un | multiscale decomposition of zeta |
| C0108 | Optimal quadratic Littlewood-Offord bound | attempted_un | optimal quadratic Littlewood-Offord |
| C0109 | Rate of convergence in the circular law as a function of the moment assumption | attempted_un | circular law rate as a function of moments |
| C0116 | Deterministic (1+epsilon)-approximation of the cover time | attempted_un | deterministic (1+eps) cover-time approximation |
| C0117 | Concentration of the cover time at the scale of the maximal hitting time | attempted_un | cover-time concentration at the hitting-time scale |
| C0119 | Chaos in directed polymers in dimensions d >= 3 | attempted_un | chaos for directed polymers d>=3 |
| C0122 | Chaos implies multiple peaks without nonnegative correlations | attempted_un | chaos implies multiple peaks without positivity |
| C0123 | Bridges between multiple peaks in the NK fitness landscape | attempted_un | bridges between NK peaks |
| C0126 | Random walk on the incipient infinite cluster of oriented percolation in dimensi | attempted_un | oriented IIC walk in d=5,6 |
| C0128 | One-sided zero-one laws for one-dimensional excited random walks | attempted_un | one-sided 0-1 laws for ERW |
| C0131 | Recurrence-transience dichotomy for excited random walks in dimension d >= 2 | attempted_un | ERW recurrence-transience dichotomy in d>=2 |
| C0139 | Non-trivial percolation phase transition on every graph with an isoperimetric in | attempted_un | p_c<1 under IP_{1+eps} for non-transitive graphs of isoperimetric dimension <=4 |
| C0143 | Exponential decay of large finite clusters touching the infinite cluster on tran | attempted_un | exponential decay of large finite clusters touching C_infinity; amenable exponential growth open |
| C0144 | Folner sequences along which the infinite cluster has a single giant piece | attempted_un | Folner giant piece; open for amenable exponential growth |
| C0146 | Monotone coupling of random-cluster measures in p for cluster weight q < 1 | attempted_un | monotone coupling of FK q<1; small-graph test next |
| C0148 | Local weak approximability of Cayley graphs and soficity | attempted_un | local weak approximability vs soficity |
| C0153 | Local limits of random-cluster models converging to nonamenable transitive graph | attempted_un | wired local limits of FK models; reduces to giant uniqueness |
| C0155 | Quasi-isometry of two independent Poisson point processes on the line | attempted_un | two Poisson processes quasi-isometric; matching question |
| P0004 | Existence of the quenched connective limit | partial_resu | quenched connective constant existence; subadditive-type |
| P0007 | Unbounded mirror component trapping every ray | attempted_un | trapping component question; geometric |
| P0009 | Manhattan pinball localization | attempted_un | Manhattan pinball localization for all q |
| P0010 | Biased random square-lattice orientations | attempted_un | biased orientations interval |
| P0011 | Brownian SIR survival in dimensions at least two | attempted_un | Brownian SIR survival, d>=2 |
| P0012 | Gaussian tensor type-2 bound | attempted_un | Gaussian tensor norm type-2 bound |
| P0014 | Expected Lovasz theta of a random circulant graph | attempted_un | random circulant theta; dependence |
| P0015 | Random complex phase-retrieval injectivity at 4M-5 measurements | attempted_un | phase retrieval injectivity at 4M-5 |
| P0016 | Worst square-submatrix conditioning in a Gaussian frame | attempted_un | worst submatrix conditioning, exponential-polynomial gap |
| P0018 | Sharp polynomial-logarithmic expected norm of graph matrices | attempted_un | sharp graph-matrix norm with logs |
| P0019 | Brownian exit approach directions in higher dimensions | attempted_un | Brownian exit approach directions |
| P0020 | Finite-crossing arcs through a planar Brownian trace | attempted_un | finite-crossing arcs through Brownian trace |
| P0021 | Interior remainder of planar Brownian trace | attempted_un | interior remainder of Brownian trace |
| P0022 | Percolation dimension of a planar Brownian trace | attempted_un | percolation dimension of Brownian trace |
| P0025 | Synchronous reflection outside a disk | attempted_un | synchronous reflection outside a disk |
| P0026 | Non-explosion of Fleming-Viot Brownian particles in arbitrary domains | attempted_un | Fleming-Viot non-explosion, arbitrary domains |
| P0027 | Rigidity of shy reflected-Brownian couplings | attempted_un | rigidity of shy couplings |
| P0034 | Recurrence of the planar horizontal-new vertical-old walk | attempted_un | horizontal-new vertical-old walk recurrence |
| P0035 | Positive speed of inward-biased walks below the Cayley growth rate | attempted_un | inward-biased walk speed on Cayley graphs |
| P0036 | Percolation threshold on arbitrary geodesic Cayley spanning trees | attempted_un | percolation threshold on geodesic spanning trees |
| P0037 | BK disjoint occurrence for weighted uniform spanning trees | attempted_un | BK inequality for weighted UST |
| P0038 | Transience preserved in Cayley percolation clusters | attempted_un | transience of Cayley percolation clusters |
| P0042 | Bootstrap thresholds as a characterization of amenable groups | attempted_un | bootstrap thresholds characterise amenability |
| P0044 | Invariant monotone coupling of free and wired uniform spanning forests | attempted_un | invariant monotone coupling FUSF/WUSF nonamenable |
| P0046 | Connecting a free uniform spanning forest by arbitrarily sparse invariant additi | attempted_un | sparse invariant additions connecting FUSF |
| P0047 | Deterministic component count of the free uniform spanning forest | attempted_un | deterministic FUSF component count |
| P0048 | One or infinitely many free-forest components without unimodularity | attempted_un | one or infinitely many FUSF components, nonunimodular |
| P0049 | Infinitely many ends in all free-forest components without unimodularity | attempted_un | infinitely many ends, FUSF, nonunimodular |
| P0051 | Zero-one law for all forest components having one end | attempted_un | zero-one law for one-ended components |
| P0052 | Limiting bushes along a wired uniform-forest ray | attempted_un | limiting bushes along WUSF ray |
| P0053 | One-ended wired minimal forests without unimodularity | attempted_un | one-ended wired minimal forests, nonunimodular |
| P0054 | Infinitely many ends in free minimal forests distinct from wired | attempted_un | FMSF ends when FMSF differs from WMSF |
| P0055 | Minimal-forest connectivity and uniqueness at p_u | attempted_un | FMSF connectivity at p_u |
| P0056 | One or infinitely many minimal-forest components | attempted_un | one or infinitely many FMSF components |
| P0057 | Uniqueness-critical percolation versus invariant spanning trees | attempted_un | p_u percolation vs invariant spanning trees |
| P0058 | Indistinguishability of minimal spanning-forest components | attempted_un | indistinguishability of MSF components |
| P0059 | Limiting bushes along a wired minimal-forest ray | attempted_un | limiting bushes along WMSF ray |
| P0062 | Connectivity of minimal forests on graphs roughly isometric to trees | attempted_un | MSF connectivity on rough trees |
| P0063 | Singularity of binary and ternary harmonic codings of the Cantor set | attempted_un | singularity of harmonic codings of Cantor set |
| P0064 | Dimension drop for every nonuniform Galton-Watson flow | attempted_un | dimension drop for nonuniform GW flows |
| P0065 | Monotonicity of harmonic dimension under inward bias | attempted_un | harmonic dimension monotone under bias |
| P0068 | Subspectral detection from a growing number of synchronization frequencies | attempted_un | subspectral detection, growing frequencies |
| P0069 | Subexponential detection at fixed synchronization frequencies | attempted_un | subexponential detection at fixed frequencies |
| P0070 | Kikuchi spectral thresholds as the polynomial degree increases | attempted_un | Kikuchi spectral thresholds |
| P0072 | Geodesic selection by reinforced ants | attempted_un | geodesic selection by reinforced ants |
| P0073 | Deterministic limits for trace-reinforced ants | attempted_un | deterministic limits for trace-reinforced ants |
| P0074 | Maximal degree and its location in the infinite-path fitness regime | attempted_un | max degree location, fitness regime |
| P0075 | Empirical degree scaling for superlinear attachment with fitness | attempted_un | degree scaling, superlinear attachment with fitness |
| P0076 | Multiple-attachment phase transition with superlinear fitness | attempted_un | multiple-attachment transition with fitness |
| P0077 | Fluctuations of fitness-reinforced sequence sums | attempted_un | fluctuations of reinforced sums |
| P0078 | Boundary profile of the reinforced-sequence condensate | attempted_un | boundary profile of the condensate |
| P0079 | Growth of sums with unbounded reinforcement fitness | attempted_un | unbounded reinforcement fitness growth |
| P0080 | Weak reinforcement on infinite WARM networks | attempted_un | weak reinforcement on infinite WARM |
| P0081 | Critical WARM on the integer line | attempted_un | critical WARM on Z |
| P0082 | Sharp reinforcement threshold for WARM forests | attempted_un | sharp WARM forest threshold |
| P0083 | Sharp reinforcement threshold for WARM whiskers | attempted_un | sharp WARM whisker threshold |
| P0084 | Finite surviving components in infinite superlinear WARM | attempted_un | finite surviving components, superlinear WARM |
| P0085 | WARM percolation with vanishing rates on lattices | attempted_un | WARM percolation on lattices |
| P0089 | Local limits for nonaffine attachment with multiple edges | attempted_un | local limits nonaffine attachment, multiple edges |
| P0091 | Infinite-state tree-automaton interpretation criteria | attempted_un | infinite-state tree-automaton criteria |
| P0093 | Infinitely many fixed points of a finite-color automaton | attempted_un | infinitely many fixed points of an automaton |
| P0094 | Prescribing rogue and interpretable automaton fixed points | attempted_un | prescribing rogue/interpretable fixed points |
| P0095 | Automaton-level conditions for a unique fixed point | attempted_un | unique fixed point conditions |
| P0098 | Strict FPP comparison in higher dimensions at a large minimum atom | attempted_un | strict FPP comparison at large minimum atom |
| P0102 | Strong Busemann limits for subadditive arrays and FPP | attempted_un | strong Busemann limits |
| P0106 | Polynomial overlap of independent planar FPP geodesics | attempted_un | polynomial overlap of planar geodesics |
| P0107 | Critical Bernoulli FPP growth in three dimensions | attempted_un | critical Bernoulli FPP growth in 3D |
| P0108 | Sharp width threshold for the thin-cylinder FPP CLT | attempted_un | sharp width threshold for cylinder CLT |
| P0113 | Almost-sure escape from a fixed midpoint in FPP | attempted_un | escape from a fixed midpoint |
| P0116 | Growth of the infinite-descendant part of the FPP geodesic tree | attempted_un | growth of infinite-descendant geodesic tree |
| P0120 | Strict interface speedup in half-plane inhomogeneous FPP | attempted_un | interface speedup in half-plane FPP |
| P0121 | Uniform Lipschitz height models and their interfaces | attempted_un | uniform Lipschitz height interfaces |
| P0122 | SLE4 from spectral truncations of the Gaussian free field | attempted_un | SLE4 from GFF spectral truncations |
| P0126 | Planar uniform lattice-tree diameter and scaling limit | attempted_un | planar lattice-tree diameter and limit |
| P0130 | Sharp planar one-arm probability beyond its exponent | attempted_un | sharp one-arm amplitude beyond exponent |
| P0132 | Measurable loop erasure of planar Brownian motion | attempted_un | measurable loop erasure of planar BM |
| P0134 | A nontrivial exact Hausdorff gauge for SLE | attempted_un | exact Hausdorff gauge for SLE |
| P0135 | Almost-sure fibers of chronological loop addition | attempted_un | a.s. fibers of chronological loop addition |
| P0136 | Chronological Brownian loop addition in three dimensions | attempted_un | chronological loop addition in 3D |
| P0137 | A loop-erased representation of a unit Brownian loop | attempted_un | loop-erased representation of Brownian loop |
| P0138 | Law of loop-decorated SLE beyond kappa2 | attempted_un | loop-decorated SLE beyond kappa 2 |
| P0139 | Rough-path continuity of chronological loop attachment | attempted_un | rough-path continuity of loop attachment |
| P0141 | First-order distance constants in finite-variance preferential attachment | attempted_un | first-order PA distance constants |
| P0142 | Fluctuations of preferential-attachment distances and diameter | attempted_un | PA distance fluctuations and diameter |
| P0143 | Second-order extremal hopcount in exponential complete-graph FPP | attempted_un | second-order extremal hopcount; first order recovered |
| P0144 | Conservative weighted-distance fluctuations in heavy-tailed configuration models | attempted_un | weighted-distance fluctuations, heavy-tailed CM |
| P0145 | Hopcount universality in infinite-variance weighted configuration models | attempted_un | hopcount universality, infinite variance |
| P0146 | Weak-to-strong disorder universality in complete-graph FPP | attempted_un | weak-to-strong disorder, complete graph |
| P0147 | Fluctuations of weighted flooding and diameter on configuration models | attempted_un | weighted flooding fluctuations |
| P0148 | General edge-weight laws for random-graph flooding and diameter | attempted_un | general weight laws, flooding/diameter |
| P0149 | Extreme hopcounts for general random-graph degree and weight laws | attempted_un | extreme hopcounts |
| P0151 | Critical window for fixed-outdegree preferential attachment | attempted_un | critical window, fixed-outdegree PA |
| P0152 | Kernel criteria for critical inhomogeneous random-graph universality | attempted_un | kernel criteria for inhomogeneous universality |
| P0153 | Vacant-set percolation threshold on general configuration models | attempted_un | vacant-set threshold on configuration models |
| P0154 | Metric scaling of critical random-walk vacant components | attempted_un | metric scaling of vacant components |
| P0156 | Configuration-model minimum spanning-tree metric limits | attempted_un | CM minimum spanning tree metric limits |
| P0157 | Two competing largest-component scales in barely subcritical configuration model | attempted_un | two competing scales, barely subcritical CM |
| P0158 | Ordered-phase susceptibility exponent on random trees and graphs | attempted_un | ordered-phase susceptibility exponent on trees |
| P0159 | Quenched non-Gaussian critical spin limits on heterogeneous random graphs | attempted_un | quenched non-Gaussian critical spin limits |
| P0160 | Fixed-temperature metastability for general configuration models | attempted_un | metastability for configuration models |
| P0161 | Potts free energy for general configuration-model degrees | attempted_un | Potts free energy, general degrees |
| P0164 | Gaussian lower bound for noise stability of unbiased thresholds | attempted_un | Gaussian lower bound for noise stability of thresholds |
| P0165 | Optimal odd functions for many-player correlation distillation | attempted_un | optimal odd functions, correlation distillation |
| P0166 | Influential coordinates of bounded low-degree polynomials | attempted_un | influential coordinates, low-degree polynomials |
| P0167 | Minimum correlation of symmetric Gaussian sets | attempted_un | minimum correlation of symmetric Gaussian sets |
| P0169 | Linear Fourier mass versus Boolean degree | attempted_un | linear Fourier mass vs degree |
| P0170 | Optimal limited independence for Gaussian polynomial thresholds | attempted_un | limited independence for Gaussian PTFs |
| P0171 | Polynomial small bias sufficient to fool DNF events | attempted_un | small bias fooling DNFs |
| P0172 | Sharp erasure-distillation bound from the Gaussian limit | attempted_un | sharp erasure-distillation bound |
| P0173 | Asymptotic influence bounds for polynomial thresholds | attempted_un | influence bounds for PTFs (Gotsman-Linial type) |
| P0175 | Symmetric unimodality under free addition | attempted_un | symmetric unimodality under free addition |
| P0176 | Existence of nontrivial freely strongly unimodal laws | attempted_un | freely strongly unimodal laws |
| P0178 | Critical moment condition for eventual stable-process unimodality | attempted_un | critical moment condition, stable eventual unimodality |
| P0179 | Uniform permutation representations of the Gieseking group | attempted_un | permutation representations of the Gieseking group |
| P0182 | Strong convergence of high-dimensional representations of a fixed compact group | attempted_un | strong convergence of representations of a compact group |
| P0183 | Deterministic strong convergence from LPS generators | attempted_un | deterministic strong convergence from LPS generators |
| P0184 | Strong convergence of modular-group actions on finite projective lines | attempted_un | strong convergence of modular-group actions |
| P0185 | Ramanujan inequalities for growing families of matrix polynomials | attempted_un | Ramanujan inequalities for matrix polynomial families |
| P0186 | Largest coefficient dimension compatible with strong convergence | attempted_un | largest coefficient dimension for strong convergence |
| P0187 | Optimal edge-fluctuation scales for arbitrary random-matrix polynomials | attempted_un | edge-fluctuation scales for matrix polynomials |
| P0188 | Joint strong convergence for permutation and deterministic matrices | attempted_un | joint strong convergence permutations + deterministic |
| P0190 | Intrinsic freeness for non-Hermitian eigenvalues | attempted_un | intrinsic freeness for non-Hermitian eigenvalues |
| P0191 | Least singular values at the polynomial constant term | attempted_un | least singular values at the constant term |
| P0192 | Brown-measure universality beyond complex entry densities | attempted_un | Brown-measure universality beyond densities |
| P0196 | Sharp comparison of systematic and random Ising updates | attempted_un | systematic vs random scan comparison |
| P0197 | Relation between Ising relaxation and mixing on transitive graphs | attempted_un | relaxation vs mixing on transitive graphs |
| P0199 | Cutoff for cyclic-to-random transpositions | attempted_un | cutoff for cyclic-to-random transpositions |
| P0200 | Cutoff for card-cyclic random insertion | attempted_un | cutoff for card-cyclic insertion |
| P0203 | Mixing exponent of uniform binary row additions | attempted_un | mixing exponent of binary row additions |
| P0204 | Mixing on large monotone subsets of the hypercube | attempted_un | mixing on monotone hypercube subsets |
| P0210 | Martingales detectable by computationally practical stopping rules | attempted_un | martingales vs practical stopping rules |
| P0211 | Relaxation of linear-polymer coagulation and fragmentation | attempted_un | coagulation-fragmentation relaxation |
| P0212 | Low-density genealogical limit of branching coalescing walks | attempted_un | low-density branching-coalescing genealogy |
| P0213 | Constant-factor online scheduling with subadditive batch durations | attempted_un | online scheduling with subadditive batches |
| P0215 | Growth exponent for common subcladograms of random trees | attempted_un | common subcladogram exponent |
| P0216 | Limit constant for common random two-dimensional partial orders | attempted_un | common two-dimensional partial orders constant |
| P0217 | Percolation of merging planar empires | attempted_un | percolation of merging empires |
| P0219 | High-density oriented percolation flow asymptotics | attempted_un | high-density oriented percolation flow |
| P0221 | Limit of the optimal online random spanning-tree cost | attempted_un | optimal online spanning-tree cost limit |
| P0222 | Near-unit stretch versus length in spatial networks | attempted_un | near-unit stretch versus length |
| P0224 | Feasible length and stretch statistics of scale-invariant networks | attempted_un | SIRSN feasible statistics |
| P0225 | Attainment of the optimal SIRSN length-stretch tradeoff | attempted_un | SIRSN optimal tradeoff attainment |
| P0226 | Local finiteness of scale-invariant network traffic measures | attempted_un | local finiteness of SIRSN traffic |
| P0227 | Implications among SIRSN finiteness and geodesic properties | attempted_un | SIRSN implications |
| P0228 | Uniqueness of the unbounded major-road component | attempted_un | uniqueness of unbounded major-road component |
| P0230 | Asymptotic total length of finite SIRSN samples | attempted_un | asymptotic total length of SIRSN samples |
| P0231 | A zero-one law for Poisson-coloring frontier dimension | attempted_un | zero-one law for coloring frontier dimension |
| P0232 | Continuous curves in the Poisson-coloring frontier | attempted_un | continuous curves in the coloring frontier |
| P0233 | Absence of double points on Poisson-coloring interface curves | attempted_un | double points on interface curves |
| P0235 | A Feller topology for limits of reversible Markov chains | attempted_un | Feller topology for chain limits |
| P0236 | Infinite mean route length at each large fixed Euclidean separation | attempted_un | infinite mean route length |
| P0243 | Sharp constant-one comparisons of reversible mixing and stopping parameters | attempted_un | constant-one comparisons of mixing/stopping parameters |
| P0244 | Sharp extremal walk parameters among regular graphs | attempted_un | extremal walk parameters among regular graphs |
| P0246 | Universal leading cover-time upper bound under transitivity | attempted_un | universal leading cover-time bound under transitivity |
| P0247 | Asymptotic uniformity of the final discovered vertex | attempted_un | uniformity of the last discovered vertex |
| P0250 | Kalai absorption bound from a directed cut parameter | attempted_un | Kalai absorption bound |
| P0251 | Mixing of the random-pair binary crossover chain | attempted_un | random-pair crossover chain mixing |
| P0252 | Sharp harmonic-mean characterization of meeting times | attempted_un | harmonic-mean characterisation of meeting times |
| P0253 | Maximal stationary antivoter variance | attempted_un | maximal antivoter variance |
| P0254 | Mixing of gap-jump exclusion on a discrete circle | attempted_un | gap-jump exclusion mixing |
| P0256 | Weak concentration of nearest-unvisited walks under exponential edge noise | attempted_un | NUV concentration under exponential noise |
| P0257 | Law of large numbers and constants for NUV lengths | attempted_un | NUV law of large numbers |
| P0258 | Variance scale and Gaussian fluctuations of NUV lengths | attempted_un | NUV variance scale |
| P0259 | Never-visited density for the planar Poisson greedy walk | attempted_un | never-visited density of greedy walk |
| P0268 | Abstract stochastic maximal regularity with non-small multiplicative noise | unsolved | abstract maximal regularity, non-small noise |
| P0269 | Necessary and sufficient operator criterion for stochastic maximal regularity | unsolved | operator criterion for stochastic maximal regularity |
| P0270 | Critical time regularization at Hilbert exponent two | unsolved | critical time regularisation |
| P0271 | Global stochastic reaction diffusion under a triangular reaction structure | unsolved | global reaction diffusion, triangular structure |
| P0272 | Global stochastic reaction diffusion with quadratic reactions and mass control | unsolved | global reaction diffusion, quadratic reactions |
| P0281 | Log concavity of finite particle TASEP transition probabilities | unsolved | log-concavity of TASEP transition probabilities |
| P0282 | Chen log concavity conjecture for fixed size random permutation LIS | unsolved | Chen log-concavity conjecture for LIS |
| P0285 | Finitary ordering permutation of a KPZ line ensemble vertical slice | unsolved | finitary ordering of KPZ line ensemble slice |
| P0286 | Stationary two color ASEP covariance decay on a large ring | unsolved | two-colour ASEP covariance decay |
| P0287 | Invariant measures for full line TASEP with killing at one site | unsolved | invariant measures, TASEP with killing |
| P0290 | Ross workload ordering for an image of a doubly monotone Markov chain | unsolved | Ross ordering for lumped chains |
| P0291 | A nonmonotone Markov intensity with supermodular time ordering | unsolved | nonmonotone intensity with supermodular ordering |
| P0292 | Characterize CTMC speed monotonicity in supermodular order | unsolved | characterise CTMC speed monotonicity |
| P0293 | Order one over N accuracy for least workload mean field queues | unsolved | 1/N accuracy for least-workload mean field |
| P0295 | Fluid limit with dependent service and patience marks | unsolved | fluid limit with dependent marks |
| P0296 | Interchange stationary and many server limits with dependent marks | unsolved | interchange of limits with dependent marks |
| P0302 | One critically loaded queue under general k-limited polling inputs | unsolved | one critically loaded k-limited polling queue |
| P0303 | Simultaneous criticality in k-limited polling | unsolved | simultaneous criticality in polling |
| P0305 | Hausdorff dimensions of bulk LQG geodesic star sets | unsolved | bulk LQG geodesic star sets |
| P0306 | One-dimensional boundary two-star set in LQG | unsolved | boundary two-star set in LQG |
| P0307 | Exact dimension of the LQG metric net | unsolved | exact dimension of LQG metric net |
| P0308 | Canonical and grand-canonical equivalence for long-range Riesz gases | unsolved | canonical vs grand-canonical Riesz gases |
| P0310 | Uniqueness for the one-dimensional short-range Riesz Gibbs gas | unsolved | uniqueness for 1D short-range Riesz gas |
| P0311 | Optimal truncated pair-correlation decay in the Riesz fluid phase | unsolved | optimal truncated correlation decay, Riesz fluid |
| P0312 | Infinite-volume BBGKY equation for the general sine-beta process | unsolved | infinite-volume BBGKY for sine-beta |
| P0315 | Forrester-Haldane pointwise pair-correlation asymptotics for sine beta | unsolved | Forrester-Haldane asymptotics for sine-beta |
| P0318 | Sharp number-variance growth exponents for long-range Riesz gases | unsolved | sharp number-variance exponents |
| P0320 | Number rigidity in the remaining Riesz exponent band | unsolved | number rigidity in remaining Riesz band |
| P0322 | Critical gap-correlation decay in the one-dimensional s=1 Riesz gas | unsolved | critical gap-correlation decay, s=1 |
| P0323 | DLR characterization of the circular Riesz thermodynamic limit | unsolved | DLR characterisation of circular Riesz limit |
| P0324 | Analyticity of the one-dimensional Riesz free energy | unsolved | analyticity of 1D Riesz free energy |
| P0329 | Jancovici-Lebowitz-Manificat discrepancy deviations for general beta | unsolved | JLM discrepancy deviations for general beta |
| P0331 | Sharpness of the Debye scale in Coulomb local laws | unsolved | sharpness of the Debye scale |
| P0332 | Regularity threshold for bounded Coulomb-gas linear-statistic fluctuations | unsolved | regularity threshold for bounded linear statistics |
| P0333 | Multivariate fluctuation limits for empirical transport with Euclidean cost | unsolved | multivariate fluctuations of empirical transport |
| P0334 | Necessary and sufficient conditions for an Lp quantile-process limit | unsolved | Lp quantile-process limit conditions |
| P0335 | Nondegenerate centered fluctuations of null quadratic empirical transport | unsolved | nondegenerate fluctuations of null quadratic transport |
| P0337 | Consistent estimation of the Sinkhorn null-limit spectrum | unsolved | Sinkhorn null-limit spectrum estimation |
| P0338 | Minimax rates for conditional optimal-transport maps | unsolved | minimax rates for conditional OT maps |
| P0339 | Sample complexity of Gromov-Wasserstein plans and dual potentials | unsolved | Gromov-Wasserstein sample complexity |
| P0343 | Correlations of critical-tree leaves at mesoscopic separation | unsolved | mesoscopic leaf correlations, critical tree |
| P0344 | Heights of prescribed interval-labelled leaves in the critical tree | unsolved | heights of interval-labelled leaves |
| P0345 | The leading constant for maximum discrete critical-tree height | unsolved | leading constant for maximal height |
| P0346 | Distinct and repeated clade shapes in critical beta-splitting trees | unsolved | clade shape counts |
| P0348 | The drawn width profile of a critical beta-splitting cladogram | unsolved | drawn width profile |
| P0349 | Complex powers of clade sizes in the critical tree | unsolved | complex powers of clade sizes |
| P0350 | A branchpoint point-process scaling limit of the critical fringe tree | unsolved | branchpoint point-process limit |
| P0351 | Connections between the critical fragmentation and beta(2,1) coalescent | unsolved | fragmentation vs beta(2,1) coalescent |
| P0356 | A general boundedness criterion for discounted tree sums | unsolved | boundedness criterion for discounted tree sums |
| P0357 | Rays with persistent extremal branching-random-walk local times | unsolved | persistent extremal BRW local times |
| P0358 | The extremal ray-height constant in a heavy-tailed branching random walk | unsolved | extremal ray-height constant |
| P0359 | The multifractal spectrum of extremal ray local times | unsolved | multifractal spectrum of ray local times |
| P0360 | Does frozen-percolation endogeny imply unrestricted almost sure uniqueness? | unsolved | frozen-percolation endogeny vs uniqueness |
| P0361 | Uniqueness of the nondiagonal scale-invariant frozen-percolation coupling | unsolved | uniqueness of nondiagonal frozen coupling |
| P0362 | Constructing frozen percolation on the PWIT as a finite-graph limit | unsolved | frozen percolation on PWIT as a limit |
| P0363 | A finite-graph approximation to frozen percolation on the three-regular tree | unsolved | finite-graph approximation on the 3-regular tree |
| P0364 | Uniqueness in law from the unoriented freezing rule and tree symmetry | unsolved | uniqueness in law from freezing rule |
| P0365 | Classifying endogenous laws among all frozen-percolation RDE solutions | unsolved | classify endogenous frozen RDE solutions |
| P0366 | The extra randomness in nonendogenous frozen percolation | unsolved | extra randomness in nonendogenous frozen percolation |
| P0367 | Support of the conditional burning-time law | unsolved | support of conditional burning-time law |
| P0368 | All bivariate frozen-percolation fixed points and their attraction domains | unsolved | bivariate frozen fixed points |
| P0369 | Nonendogeny from instability of the diagonal coupling | unsolved | nonendogeny from diagonal instability |
| P0375 | Independence of ARW bulk microstructure from the initial source shape | unsolved | source-shape independence of ARW microstructure |
| P0378 | Exhaustion-independent infinite-volume wired ARW measure | unsolved | exhaustion-independent wired ARW measure |
| P0380 | Equality of bulk one-site density and wired global ARW density | unsolved | bulk vs wired ARW density |
| P0383 | Exponential incompressibility of the infinite-volume wired ARW state | unsolved | exponential incompressibility of wired ARW |
| P0384 | Sharp first slow-stabilization threshold of the ARW free chain | unsolved | first slow-stabilisation threshold |
| P0385 | Asymptotic equivalence of supercritical free and wake ARW states | unsolved | supercritical free vs wake ARW states |
| P0386 | Uniform loss of initial-state information in dense ARW stabilization | unsolved | loss of initial information in dense ARW |
| P0387 | Slow-to-one-step mixing transition of the ARW wake chain | unsolved | slow-to-one-step mixing of the wake chain |
| P0391 | Diffusion limit for an arbitrary symmetric M/G/1 discipline | unsolved | diffusion limit, symmetric M/G/1 discipline |
| P0392 | Infinite-variance scaling limits of symmetric queue lengths | unsolved | infinite-variance symmetric queue limits |
| P0393 | Uniform busy-cycle maximum bounds for symmetric queues | unsolved | busy-cycle maximum bounds |
| P0394 | Efficient input estimation from periodically observed queue workloads | unsolved | input estimation from periodic workloads |
| P0395 | Network decomposition with several bottlenecks and internal flow covariance | unsolved | multi-bottleneck decomposition |
| P0396 | IDC-based decomposition for networks of multiserver queues | unsolved | IDC decomposition, multiserver |
| P0397 | Multiclass and non-Markovian-routing robust queueing decomposition | unsolved | multiclass robust decomposition |
| P0398 | Robust network approximations under time-varying arrivals | unsolved | robust approximations, time-varying arrivals |
| P0399 | Identifiable and efficient probe inference in tandem queueing networks | unsolved | probe inference in tandem networks |
| P0400 | Response-time laws with correlated redundancy replicas | unsolved | response laws with correlated replicas |
| P0401 | Optimizing replication degree under correlated service requirements | unsolved | optimal replication degree |
| P0402 | Stability beyond processor sharing with correlated redundancy copies | unsolved | stability beyond PS with replicas |
| P0403 | Optimal scheduling for correlated redundancy systems | unsolved | optimal scheduling with redundancy |
| P0404 | Tractable concurrent-replica policies with broad stability guarantees | unsolved | tractable replica policies |
| P0405 | Characterizing optimality of MAX-H in multiclass queues | unsolved | MAX-H optimality characterisation |
| P0406 | Finite-system performance of size-based scheduling with impatience and noisy siz | unsolved | size-based scheduling with impatience |
| P0408 | Recovering an ideal Voronoi tessellation from vertices or its dual | unsolved | recovering ideal Voronoi from vertices |
| P0409 | Joint law of neighboring ideal Voronoi vertices | unsolved | joint law of neighbouring ideal vertices |
| P0410 | Hole probabilities for lower-dimensional ideal Voronoi faces | unsolved | hole probabilities for lower-dimensional faces |
| P0412 | A general transfer theorem between horospherical and hyperbolic typical values | unsolved | horospherical vs hyperbolic transfer theorem |
| P0413 | Low-intensity variance of typical hyperbolic Voronoi cell volume | unsolved | low-intensity typical-cell variance |
| P0414 | Hausdorff dimension of exceptional rays in the planar ideal Voronoi tree | unsolved | exceptional rays in the planar ideal tree |
| P0415 | Canonical intensity and typical-cell laws for unbounded hyperbolic cells | unsolved | canonical intensity for unbounded cells |
| P0417 | Regular exponential volume growth without full graph IPVT convergence | unsolved | regular growth without full IPVT convergence |
| P0418 | Non-Poisson low-intensity ideal Voronoi diagrams | unsolved | non-Poisson low-intensity diagrams |
| P0419 | Equal-growth L1 products beyond the divergent tilted-volume condition | unsolved | equal-growth L1 products |
| P0420 | Low-intensity Voronoi limits for products with the L2 metric | unsolved | low-intensity limits with the L2 metric |
| P0421 | Convergence of edge-measured product-graph Voronoi diagrams | unsolved | edge-measured product-graph diagrams |
| P0422 | More than two distinguishable types of group IPVT cells | unsolved | more than two IPVT cell types |
| P0425 | Optimal parallel allocation with unknown nonexponential job sizes | unsolved | parallel allocation, unknown sizes |
| P0426 | Optimal known-size parallel allocation with Poisson arrivals | unsolved | known-size allocation with Poisson arrivals |
| P0428 | Mean-response optimization for stochastically arriving DAG jobs | unsolved | DAG job mean-response optimisation |
| P0430 | Response laws for limited fork-join shortest-queue dispatching | unsolved | limited fork-join shortest-queue response |
| P0431 | Straggler replication in queued limited fork-join systems | unsolved | straggler replication in fork-join |
| P0432 | Optimal known-size multiserver scheduling beyond SRPT | unsolved | multiserver scheduling beyond SRPT |
| P0433 | Optimal dispatching to SRPT queues outside heavy traffic | unsolved | dispatching to SRPT queues |
| P0434 | Sharp approximation ratio for simple alternatives to Gittins | unsolved | approximation ratio vs Gittins |
| P0435 | Optimal nonasymptotic scheduling with unknown sizes in M/G/k | unsolved | nonasymptotic unknown-size M/G/k scheduling |
| P0436 | Optimal finite-deadline success scheduling | unsolved | finite-deadline success scheduling |
| P0437 | Dropping probability and optimality gap of DTLH | unsolved | DTLH dropping probability |
| P0438 | Feasibility of class-specific response quantiles | unsolved | class-specific response quantiles |
| P0440 | Waiting-time tails with deterministic multiserver setup | unsolved | waiting tails with deterministic setup |
| P0442 | Optimal waiting-power Pareto frontier with deterministic setup | unsolved | waiting-power Pareto frontier |
| P0443 | Closed-form performance bounds for general setup distributions | unsolved | bounds for general setup distributions |
| P0444 | Computational complexity of the multiserver-job stability threshold | unsolved | complexity of the multiserver-job stability threshold |
| P0445 | Monotone workload recurrences beyond FCFS multiserver jobs | unsolved | monotone recurrences beyond FCFS |
| P0446 | Perfect multiserver-job samples with a stability-matching upper bound | unsolved | perfect multiserver-job samples |
| P0447 | Finite-size response characterization for classical fork-join queues | unsolved | finite-size fork-join response |
| P0450 | Conditional generation limits for the Erlang weighted tree | unsolved | conditional generation limits, Erlang weighted tree |
| P0451 | Unimodularity and reversibility of the Erlang branching spine | unsolved | unimodularity of the Erlang spine |
| P0452 | Giant-component density from Erlang weighted-tree survival | unsolved | giant density from EWT survival |
| P0453 | Weaker degree-tail hypotheses for Erlang weighted-tree growth | unsolved | weaker degree tails for EWT growth |
| P0457 | Diameter near the newly established bilateral connectivity threshold | unsolved | diameter near bilateral threshold |
| C0159 | Cluster repulsion for nonunimodular transitive graphs | attempted_un | Timar's mass transport fails nonunimodular; grandparent graph is the test case |
| C0160 | Uniqueness monotonicity beyond i.i.d. transitive percolation | attempted_un | quasi-transitive i.i.d. case follows; residual is nonunimodular dependent families |

## Tier 4

Tier 4, major open problem of its area: decades old, many attempts, known walls

| id | problem | attempt status | why this tier |
|---|---|---|---|
| C0001 | Joint scaling limit of all intermediate level sets of the 2D DGFF | attempted_un | joint limit of all intermediate DGFF level sets |
| C0009 | Intermediate level sets for gradient fields with uniformly strictly convex poten | attempted_un | level sets for gradient fields |
| C0013 | Existence of the Liouville Langevin motion as a joint scaling limit | attempted_un | Liouville Langevin motion |
| C0015 | Scaling limit of the current-minimising path in the DGFF network | attempted_un | scaling limit of the DGFF current path |
| C0016 | Hausdorff dimension of the continuum DGFF current path and of the energy support | attempted_un | dimension of the continuum current path |
| C0018 | Existence and value of the four-arm critical exponent for critical bond percolat | attempted_un | four-arm exponent on Z^2 (existence and value) |
| C0029 | Spielman-Teng conjecture on the least singular value of Bernoulli matrices | attempted_un | Spielman-Teng constant one |
| C0043 | Transience of i.i.d. elliptic RWRE in dimensions d >= 3 | attempted_un | transience of i.i.d. elliptic RWRE in d>=3 |
| C0044 | Zero-one law for directional transience in dimensions d >= 3 | attempted_un | directional 0-1 law in d>=3 |
| C0047 | Benjamini-Schramm conjecture: p_c < p_u if and only if the group is non-amenable | attempted_un | Benjamini-Schramm p_c<p_u for every Cayley graph |
| C0049 | Convergence of random-cluster interfaces to SLE(kappa) for q in (0,4], q not 2 | attempted_un | FK interfaces to SLE for q not 2 |
| C0050 | Convergence of the parafermionic observable to (phi')^sigma for q <= 4 | attempted_un | parafermionic observable convergence for q<=4 |
| C0051 | Improved two-point function bounds for the critical three-dimensional Ising mode | attempted_un | 3D Ising two-point exponent improvement |
| C0054 | Localisation of all bulk states for two-dimensional random band matrices at fixe | attempted_un | 2D band matrices localised at fixed W |
| C0055 | Finite critical band width in dimension three | attempted_un | finite W_c in d=3 |
| C0064 | Infrared bound for nearest-neighbour percolation in every dimension d > 6 | attempted_un | infrared bound for nearest-neighbour d in 7..10 |
| C0069 | Scaling limit of critical percolation cluster sizes on the hypercube | attempted_un | hypercube scaling limit of cluster sizes |
| C0071 | Multiplicative-coalescent scaling limit of critical percolation on high-dimensio | attempted_un | multiplicative coalescent on high-d tori |
| C0078 | Mean-field behaviour of nearest-neighbour oriented percolation for all d > 4 | attempted_un | nearest-neighbour oriented percolation mean-field for all d>4 |
| C0080 | Borel summability of the 1/d expansion of the percolation threshold | attempted_un | Borel summability of the p_c expansion |
| C0084 | No infinite cluster at criticality on quasi-transitive graphs with p_c < 1 | attempted_un | theta(p_c)=0 on quasi-transitive graphs |
| C0086 | Scaling limit of high-dimensional invasion percolation | attempted_un | invasion percolation scaling limit |
| C0088 | Scaling limit of the minimal spanning tree on high-dimensional tori | attempted_un | MST scaling limit on tori |
| C0091 | Negative association for the random-cluster model with q < 1 | attempted_un | negative association for FK q<1 |
| C0092 | Sharp phase transition for the random-cluster model with q < 1 | attempted_un | sharpness for FK q<1 |
| C0093 | Lace expansion for the random-cluster model with q not in {1,2} | attempted_un | lace expansion for FK q not 1,2 |
| C0095 | Convergence of the holomorphic observable of the honeycomb self-avoiding walk to | attempted_un | SAW observable convergence |
| C0096 | Interfaces of the honeycomb O(n) loop model converge to SLE(kappa) | attempted_un | O(n) loop interfaces to SLE, n not 1 |
| C0099 | Recurrence of the rotor-router walk on Z^2 with uniformly random initial rotors | attempted_un | rotor-router recurrence on Z^2 |
| C0103 | Limiting distribution of the fluctuations of the maximum of zeta on short interv | attempted_un | limit law of zeta maximum fluctuations |
| C0125 | Spectral dimension of random walk on the incipient infinite cluster below the cr | attempted_un | IIC spectral dimension below d=6 |
| C0132 | Transience and recurrence of the M(d1,d2) balanced excited random walks | attempted_un | M(1,1) recurrence and M(1,2) transience |
| C0137 | Positive speed of random walk on a group is independent of the generating set | attempted_un | positive speed independent of generating set (Liouville characterisation) |
| C0138 | Kozma's conjecture: sublinear harmonic functions and diffusive walks | attempted_un | Kozma's sublinear-harmonic/diffusive conjecture; o(r^1/2) case follows |
| C0145 | Bounded chemical-distance ratio in the uniqueness phase | attempted_un | chemical-distance ratio above p_u |
| C0147 | Majority-dynamics fixation threshold equals one half on Z^d and on high-degree t | attempted_un | majority-dynamics fixation threshold one half |
| C0149 | Bowen's conjecture: Benjamini-Schramm approximants of Kazhdan groups are essenti | attempted_un | Bowen's essential-expander conjecture |
| C0152 | Abert-Szegedy entropy conjecture for factor processes on Benjamini-Schramm conve | attempted_un | Abert-Szegedy entropy conjecture |
| C0156 | Once-reinforced random walk phase transition in the reinforcement parameter | attempted_un | once-reinforced walk phase transition on Z^d |
| P0002 | Self-avoiding-walk counting exponents | attempted_un | SAW critical exponents on Z^d, d=2,3,4; d=4 log correction |
| P0005 | Ehrenfest mirror escape | attempted_un | Ehrenfest mirror escape: old, no tools |
| P0006 | Poisson mirror escape threshold | attempted_un | Poisson mirror threshold: same family |
| P0008 | Diffusive Poisson mirror trajectories | attempted_un | diffusivity of mirror billiards: dynamical, hard |
| P0040 | Uniqueness threshold below one in one-ended transitive graphs | attempted_un | p_u<1 for one-ended transitive graphs (Benjamini-Schramm) |
| P0041 | Nonuniqueness phase for nonamenable quasi-transitive graphs | attempted_un | nonuniqueness phase for nonamenable quasi-transitive graphs |
| P0045 | Rational expected free-forest degree for finitely presented groups | attempted_un | rational expected FUSF degree for finitely presented groups (Atiyah-type) |
| P0060 | Dimensions with a connected Euclidean minimal spanning forest | attempted_un | dimensions where Euclidean MSF is connected (d>=3 open) |
| P0061 | Full scaling limit of the square-lattice minimal spanning tree | attempted_un | full scaling limit of square-lattice MST |
| P0066 | Monotonicity of biased-walk speed on Galton-Watson trees | attempted_un | monotonicity of biased-walk speed on GW trees (Lyons-Pemantle-Peres) |
| P0067 | Global Kuramoto synchronization of random cubic graphs | attempted_un | Kuramoto synchronization of random cubic graphs |
| P0071 | Polynomial Glauber mixing throughout the SK high-temperature regime | attempted_un | polynomial Glauber mixing in whole SK high-temperature regime |
| P0086 | Recurrence of sublinear vertex-reinforced walk on Z | attempted_un | recurrence of sublinear vertex-reinforced walk on Z |
| P0097 | An explicit nontrivial FPP time constant and limit shape | attempted_un | explicit nontrivial FPP time constant |
| P0099 | Strict convexity of iid FPP limit shapes | attempted_un | strict convexity of FPP limit shapes |
| P0100 | Excluding axial facets and cubical FPP shapes | attempted_un | exclude axial facets / cubical shapes |
| P0101 | Classification of flat FPP boundary pieces | attempted_un | classify flat FPP boundary pieces |
| P0103 | Uniform curvature of continuous-law FPP shapes | attempted_un | uniform curvature of FPP shapes |
| P0105 | High-dimensional limit of the FPP fluctuation exponent | attempted_un | high-dimensional limit of FPP exponent |
| P0111 | Infinitely many planar FPP geodesic rays for continuous laws | attempted_un | infinitely many geodesic rays, continuous laws |
| P0112 | Full-sequence convergence of FPP geodesics to a ray | attempted_un | full-sequence convergence of geodesics |
| P0114 | Uniqueness of planar directional geodesics in every fixed direction | attempted_un | uniqueness of directional geodesics in every direction |
| P0115 | Coalescence of directional FPP rays in higher dimensions | attempted_un | coalescence of directional rays in higher dimensions |
| P0118 | Noncircular low-dimensional Eden limit shape | attempted_un | Eden limit shape noncircular in low dimensions |
| P0119 | Noncoexistence of unequal-speed Richardson infections | attempted_un | noncoexistence of unequal-speed Richardson |
| P0123 | High-temperature triangular Ising interfaces converge to SLE6 | attempted_un | high-temperature Ising interfaces to SLE6 |
| P0124 | Critical planar random-cluster interfaces for general cluster weight | attempted_un | critical FK interfaces for general q (Schramm conjecture) |
| P0125 | Conformal limits of the critical and dense O(n) loop model | attempted_un | conformal limits of O(n) loop models |
| P0128 | Cardy conformal invariance for Voronoi percolation | attempted_un | Cardy formula for Voronoi percolation |
| P0129 | Cardy conformal invariance for Boolean continuum percolation | attempted_un | Cardy formula for Boolean percolation |
| P0131 | Exact critical percolation chemical-distance exponent | attempted_un | exact chemical-distance exponent |
| P0155 | Erdos-Renyi component-size limits for high-dimensional tori | attempted_un | Erdos-Renyi limits on high-d tori (multiplicative coalescent) |
| P0163 | Polynomial Fourier concentration for DNF formulas | attempted_un | polynomial Fourier concentration for DNF (Mansour) |
| P0168 | Noise-optimal equal-volume Gaussian partitions | attempted_un | noise-optimal Gaussian partitions (standard simplex) |
| P0180 | Optimal spectra of random symmetric-group Cayley graphs | attempted_un | optimal spectra of random symmetric-group Cayley graphs |
| P0181 | Fixed-degree random Cayley graphs with optimal spectral gap | attempted_un | fixed-degree random Cayley graphs with optimal gap |
| P0194 | Polynomial mixing with plus Ising boundary conditions | attempted_un | polynomial mixing with plus boundary through the whole regime |
| P0195 | Monotonicity of the ferromagnetic Ising spectral gap | attempted_un | monotonicity of ferromagnetic Ising spectral gap |
| P0198 | Cutoff on bounded-degree transitive expanders | attempted_un | cutoff on transitive expanders |
| P0201 | Optimal Glauber mixing near the coloring degree threshold | attempted_un | optimal Glauber mixing near coloring threshold |
| P0202 | Diameter-squared upper bound for transitive mixing | attempted_un | diameter-squared mixing bound for transitive graphs |
| P0214 | Fluctuations of shortest routes in Poisson proximity networks | attempted_un | KPZ fluctuations of Poisson proximity routes |
| P0223 | Sharp relaxation exponent for local tree rotations and triangulation flips | attempted_un | sharp relaxation exponent for tree rotations / flips |
| P0273 | Local stochastic Navier Stokes theory with no slip and non-small transport noise | unsolved | local stochastic Navier-Stokes, no slip, non-small noise |
| P0274 | Optimal critical spatial smoothness for stochastic Navier Stokes transport noise | unsolved | critical smoothness for stochastic NS transport noise |
| P0275 | Supremum endpoint Serrin criterion for stochastic Navier Stokes | unsolved | endpoint Serrin criterion, stochastic NS |
| P0277 | Cutoff for conservative exclusion in dimension at least two | unsolved | cutoff for exclusion in d>=2 |
| P0278 | Cutoff for unit-rate zero range on higher dimensional lattices | unsolved | cutoff for zero range in higher dimensions |
| P0279 | Cutoff for bounded-degree Ising throughout the rapid-mixing phase | unsolved | cutoff for Ising throughout rapid mixing |
| P0280 | Cutoff for bounded-degree hardcore throughout the rapid-mixing phase | unsolved | cutoff for hardcore throughout rapid mixing |
| P0283 | Exact binary longest common subsequence time constant | unsolved | exact binary LCS constant (Chvatal-Sankoff) |
| P0284 | Gaussian fluctuations for uniform binary longest common subsequences | unsolved | Gaussian fluctuations for LCS |
| P0298 | General Toda three-point structure constants | unsolved | Toda three-point constants |
| P0299 | Probabilistic conformal bootstrap for Toda theory | unsolved | probabilistic bootstrap for Toda |
| P0300 | Conformal bootstrap for the noncompact H3 WZW model | unsolved | bootstrap for H3 WZW |
| P0301 | Full probabilistic noncompact imaginary Liouville theory | unsolved | noncompact imaginary Liouville |
| P0313 | Translation invariance in low-dimensional long-range Riesz gases | unsolved | translation invariance, low-d long-range Riesz |
| P0314 | Uniqueness of the general sine-beta DLR Gibbs measure | unsolved | uniqueness of sine-beta DLR measure |
| P0316 | Two phase transitions in negative-exponent one-dimensional Riesz gases | unsolved | two transitions in negative-exponent Riesz gases |
| P0317 | Hyperuniformity of general long-range Riesz Gibbs gases | unsolved | hyperuniformity of long-range Riesz gases |
| P0325 | Uniqueness of the microscopic bulk limit of the two-dimensional Coulomb gas | unsolved | uniqueness of 2D Coulomb bulk limit |
| P0326 | High-temperature uniqueness and variational characterization of the two-dimensio | unsolved | high-temperature uniqueness, 2D Coulomb |
| P0327 | Exponential clustering in the high-temperature two-dimensional plasma | unsolved | exponential clustering, high-temperature plasma |
| P0328 | Gravitational allocation for the two-dimensional one-component plasma | unsolved | gravitational allocation for the 2D OCP |
| P0330 | Higher-order free-energy expansion of the two-dimensional Coulomb gas | unsolved | higher-order free-energy expansion, 2D Coulomb |
| P0370 | Endogeny of frozen percolation on higher-degree trees and the PWIT | unsolved | endogeny on higher-degree trees and PWIT |
| P0371 | Existence of infinite-cluster frozen percolation on higher-dimensional lattices | unsolved | infinite-cluster frozen percolation, higher d |
| P0372 | Spherical shape and uniform bulk density of ARW aggregates | unsolved | spherical ARW aggregates |
| P0373 | Full microscopic limit of the ARW point-source aggregate | unsolved | full microscopic ARW limit |
| P0374 | Quadrature-domain scaling limit from extended ARW sources | unsolved | quadrature-domain ARW limit |
| P0376 | Universal critical limit obtained by sprinkling subcritical ARW states | unsolved | universal critical ARW limit by sprinkling |
| P0377 | Universal stationary ARW density in higher-dimensional growing domains | unsolved | universal stationary ARW density, higher d |
| P0379 | Equality of the three infinite-volume critical ARW laws | unsolved | equality of the three critical ARW laws |
| P0381 | Higher-dimensional hockey-stick density evolution for wired ARW | unsolved | higher-d hockey-stick evolution |
| P0382 | Critical-density total-variation cutoff for wired ARW in higher dimensions | unsolved | critical-density cutoff, higher d |
| P0388 | Hyperuniformity of the infinite-volume wired ARW state | unsolved | hyperuniformity of wired ARW |
| P0416 | Amenability of ideal Bernoulli Voronoi relations on nonexact groups | unsolved | amenability of ideal Bernoulli Voronoi relations on nonexact groups |
| C0158 | Number of infinite clusters at the uniqueness threshold p_u on nonamenable transitive graphs | attempted_un | classification at p_u; reduces (unimodular) to positivity of the two-point infimum at p_u |

## Tier 5

Tier 5, famous field-defining conjecture

| id | problem | attempt status | why this tier |
|---|---|---|---|
| C0017 | Conformal invariance of critical bond percolation on the square lattice | attempted_un | conformal invariance on Z^2 |
| C0023 | No percolation at criticality on Z^d for 3 <= d <= 10 | attempted_un | theta(p_c)=0 for 3<=d<=10 |
| C0041 | Transience in a direction implies ballisticity for uniformly elliptic i.i.d. RWR | attempted_un | transience implies ballisticity, UE i.i.d., d>=2 |
| C0048 | Discontinuity of the Potts phase transition on Z^d for q >= 3, d >= 3 | attempted_un | Potts discontinuity d>=3, q>=3 |
| C0052 | Non-triviality of the scaling limit of the three-dimensional Ising model | attempted_un | 3D Ising non-triviality |
| C0056 | Extended states for the three-dimensional Anderson model at weak disorder | attempted_un | 3D Anderson delocalisation |
| C0120 | Fluctuation exponent of directed polymers beyond the logarithmic improvement | attempted_un | power improvement of polymer variance (KPZ) |
| C0150 | Atiyah's conjecture for torsion-free groups | attempted_un | Atiyah conjecture for torsion-free groups |
| C0154 | Amenability of Thompson's group F | attempted_un | amenability of Thompson's group F |
| P0003 | Hexagonal self-avoiding-walk scaling limit | attempted_un | SAW to SLE(8/3): field-defining conjecture |
| P0017 | Dimension-free log-concave Poincare or Cheeger constant | attempted_un | KLS-type dimension-free Poincare/Cheeger for log-concave |
| P0043 | Absence of infinite clusters at critical percolation | attempted_un | theta(p_c)=0 on quasi-transitive graphs |
| P0104 | Subdiffusive and KPZ passage-time fluctuation exponents | attempted_un | FPP fluctuation exponents (chi=1/3) |
| P0110 | An iid FPP law with proved KPZ exponent relation | attempted_un | iid FPP law with proved KPZ relation |
| P0117 | Absence of bi-infinite geodesics in planar iid FPP | attempted_un | no bigeodesics in planar iid FPP |
| P0162 | Fourier entropy versus total influence | attempted_un | Fourier entropy versus influence conjecture |
| P0297 | Exact Hausdorff dimension of Liouville quantum gravity | unsolved | exact Hausdorff dimension of LQG |
| P0309 | Positive-temperature crystalline Gibbs phases for three-dimensional Riesz gases | unsolved | 3D crystalline phase for Riesz gases (crystallisation) |
| P0321 | Existence of a hexatic phase for two-dimensional Riesz gases | unsolved | hexatic phase for 2D Riesz gases |

## Duplicates removed

Cross-source restatements of one conjecture are kept as separate rows, because duplicates are removed by source and locator, not by title: for example C0023 (Garban-Steif) and P0043 (the Codex ledger) both state the absence of an infinite cluster at critical percolation in intermediate dimensions. A title-level merge is a follow-up, not done here.

P0461 to P0487 in the Codex ledger (except P0484, which it excluded) are Claude-intake problems merged by the Codex worker under new ids, and C0094 is a second locator for C0023; each is listed once under its C id.


---

## Status update, 2026-09-08: thirteen of these are settled, and the list has grown

This file is unchanged above; the update is appended so nothing in the ranking is silently rewritten.

**Thirteen problems on this list are now settled**, with a full write-up in
`Probability_open_problems_thirteen_settled_2026-09-08.md` and a brain memory each. By ledger id:

| id | source problem | verdict |
|---|---|---|
| P0208 | Aldous-Fill Open Problem 7.27 | refuted, the thickened cycle C_m[K2-bar] |
| P0340 | Aldous-Janson Open Problem 14 | proposed rate wrong; drawn length is Theta(n) |
| P0193 | Hasebe-Ueda-Wang Problem 4.7 | no, a two-atom measure |
| P0266 | Agresti-Veraar Problem 4 | no, a BES(4) construction |
| P0267 | Agresti-Veraar Problem 5 | no, the same construction |
| P0209 | Aldous-Fill Open Problem 4.30 | no, a rare-state four-state chain |
| D0035 | Bradley Question 7 (intake D, not ranked here) | false as literally stated |
| P0288 | Pollett Section 2 Conjecture (ii) | no, a two-ended killed walk |
| P0032 | Burdzy-Scheutzow Problem 7.5 | yes, a filling scheme |
| P0276 | Salez Problem 2.4 | literal statement falls, an unweighted reset |
| P0033 | Lyons-Peres Question 17.18 | no, an AND/OR tree colour |
| P0174 | Hasebe-Ueda Problem 3.3 | the optimal constant is C = 1 |
| P0341 | Aldous-Janson Ansatz 20 (inside Open Problem 8) | false in both parts |

Prior art is unchecked on most of them, which is the whole distance to a publishable claim. Two
(P0288, P0032) carry specific prior-art warnings and are probably known; one (D0035) needs no check,
being refuted from material printed in the same survey.

**The tier-1 reading in this file is vindicated.** Tier 1 was assembled from the campaign's own
recorded candidates and I flagged at the time that this made it circular. Every tier-1 row I
re-derived independently held up, and reading all 25 files in the Codex ledger's `proofs/` directory
turned up no wrong calculation anywhere. The ledger also labels its own spent results honestly.

**The list has grown by 92**: intake D, at
`06_math_research/probability_1000_intake_D_20260908/`, adds 92 distinct problems with attempts.
They are not ranked here.

**One problem should be added back.** Intake D excluded D0039 (Virag's ICM Question 1, on the
fractal spectrum of the beta-Hermite measure against Gaussian multiplicative chaos) as resolved by
Chhaibi and Najnudel. That citation is about the CIRCULAR beta ensemble; the question names the
beta-Hermite measure. It is still open. The other seven of intake D's exclusions were checked
against their sources and hold.
