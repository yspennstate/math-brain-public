# C0020 literature and source audit — 2026-10-12

Status: NO EXACT LITERATURE SOLUTION IDENTIFIED. This is a bounded search, not a proof of absence. OpenAlex citation retrieval and Semantic Scholar keyword search were rate-limited, so the coverage is explicitly incomplete. The source and the closely relevant 2024 paper were read in full at the relevant passages.

## Source and exact statement

Christophe Garban and Jeffrey E. Steif, *Noise sensitivity of Boolean functions and percolation*, arXiv:1102.5761v3, 29 May 2012. Later book: Cambridge University Press, 2014, DOI 10.1017/CBO9781139924160.
Downloaded PDF: source_pdf.pdf; extracted text: source.txt. Page numbers below distinguish the PDF page from the printed page.

Definition VIII.2 (printed 89, PDF 91):
> Given a randomized algorithm A for a Boolean function f, let C(A) (the cost of A) be the expected number of queries that the algorithm A makes. Let C(f) (the cost of f) be the infimum of C(A) over all randomized algorithms A for f.

Theorem VIII.3 (printed 87, PDF 89):
> Let f = f_n be the indicator function for the event that critical site percolation on the triangular grid contains a left to right crossing of our n × n box. Then δ_{f_n} ≤ n^{-1/4+o(1)} as n → ∞.

Open question (printed 90, PDF 92; Unicode math transcribed from the PDF):
> Open Question: Find the smallest σ such that there are algorithms A_n for f_n with C(A_n) ≤ n^σ. (We know σ ∈ [6/4, 7/4].)

The intake locator incorrectly treats p.92 as the printed page; it is the PDF page in this version. The exact exponent range refers to triangular-site critical p=1/2 percolation, not a proved exact-exponent assertion for square-bond percolation. Algorithms stop only when all completions agree (printed 83, PDF 85). This is average input-and-seed query complexity, zero error.

## Relevant papers and what they do not establish

1. Laurin Köhler-Schindler and Jeffrey E. Steif, *A study of distributional complexity measures for Boolean functions*, arXiv:2408.12995v1, 23 August 2024 (PDF manuscript dated 26 August 2024). Section 4.2, pp.24–27, discusses percolation functions. Proposition 4.6 on p.26 gives non-sharp square-bond critical bounds; Conjecture 4.7 on p.27 lists exponents including a ≤ m^(7/4+o(1)). It explicitly says, on p.27:
> Non-rigorous arguments suggest that w(f_m, π_{1/2}) behaves like m^{1.130···} and a(f_m, π_{1/2}) behaves like m^α with α ∈ [1.5, 1.6] (see [PSSW07]). Finding the exact exponents in these two cases are well-known open problems.
This is a later status lead, not a solution. The model in this example is square-bond; the accompanying discussion distinguishes triangular-site known arm exponents. The apparent 1.5–1.6 range is expressly non-rigorous and is NOT an upper bound used here. PDF stored as 2408.12995.response; text 2408.12995.txt.

2. Yuval Peres, Oded Schramm, Scott Sheffield and David B. Wilson, *Random-turn hex and other selection games*, American Mathematical Monthly 114(5) (2007), 373–387; arXiv:math/0508580v2. This predates the source and is a lead to algorithms and simulations. No theorem determining the optimal crossing-query exponent is identified. Stored as random_turn_hex.response/.txt.

3. Oded Schramm and Jeffrey E. Steif, *Quantitative noise sensitivity and exceptional times for percolation*, Annals of Mathematics (2) 171(2) (2010), 619–672; arXiv:math/0504586. This is source reference SS10b and supplies the low-revealment interface algorithm. This is the known upper-bound source, not a later solution.

4. Ryan O'Donnell and Rocco A. Servedio, *Learning monotone decision trees in polynomial time*, SIAM Journal on Computing 37(3) (2007), 827–844. The notes' reference OS07 supplies the total-influence-square lower bound reproduced as Theorem VIII.6 (printed pp.89–90). No claim of a new optimal exponent is made.

5. Michael Damron, Jack Hanson and Philippe Sosoe, *Strict inequality for the chemical distance exponent in two-dimensional critical percolation*, Communications on Pure and Applied Mathematics 74(11) (2021), 2431–2455; arXiv:1708.03643, PDF dated 5 July 2021. Theorem 1, p.1, bounds the conditional expected shortest crossing length relative to the lowest crossing. Its triangular-site discussion yields an exponent strictly below 4/3 for shortest crossing length. That is certificate geometry; it does NOT give a query algorithm finding a certificate at that cost. Stored as 1708.03643.response/.txt.

6. Nikita Gladkov, *Percolation Inequalities and Decision Trees*, arXiv:2408.08457v2, 22 August 2024. Theorem 1.1/Theorem 6.2 bounds three-point connectivity probabilities on general graphs. Its decision-tree inequalities are related techniques, not a matching crossing query-complexity theorem. Stored as 2408.08457.response/.txt.

7. Fan Chang, Hong Liu and Miao Liu, *The sharp diagonal spectral correlation inequality on the discrete cube*, arXiv:2606.32024v1, 30 June 2026. The main theorem bounds covariance of increasing Boolean functions by degree-weighted collision of Fourier spectra. No crossing algorithm or query-cost exponent theorem is stated. Six mentions of percolation, mostly contextual/bibliographic, do not change this. Stored as 2606.32024.response/.txt. This paper is a lead only; its proof is not an assumption in ATTEMPT.md.

8. Yitzchak Shmalo, *Entropy and singularity of spectral and pivotal sets in planar percolation*, arXiv:2609.15388v1, 14 September 2026. Theorem 1.1 concerns crossing entropy; the paper also treats discrete spectral/pivotal law separation. These are different open questions. It does not state/prove the optimal query exponent posed here. Stored as 2609.15388.response/.txt. Its assertions and the brain's provisional entropy claims are not used as lemmas.

Other arXiv and citation results on Voronoi/Poisson/Gaussian/Ising models, critical speeding-up, sharp thresholds and random-cluster decision trees use different hypotheses or objectives. They were screened as leads, not accepted as a printed solution.

## Read-only local evidence searches

- math_recall.py: "percolation randomized algorithm computational complexity revealment"; intake attempt card returned, treated as unverified.
- brain.py recall: "percolation algorithms mistakes" and "percolation crossing query complexity"; no checked solution returned.
- rg for C0020 in intake ledgers and codex_pool_2026_10_10. The first wildcard directory invocation failed on Windows; it was rerun with enumerated directory paths. The relevant intake is C0020-A001 in probability_1000_intake_claude_20260907/attempts.jsonl; it claims no solution and includes unsupported Fourier-level speculation.
- Read codex_pool_2026_10_10/team_O/w336/proofs/C0020.md: fixed-order OR and prepended-site-query counterexamples refute uniform revealment from total cost. Also read the corresponding file directly with git show origin/master:probability_campaigns/codex_pool_2026-10-10/team_O/w336/proofs/C0020.md in math-open-problems, after read-only git ls-tree filtering. No repository changes.

## Every external request, including unsuccessful searches

All requests used Python urllib from the shell, with bounded timeouts. No built-in web search was used. Exact requests and responses are retained; the following ledger is generated verbatim from search_log.jsonl.

- 2026-10-12 — source_pdf — https://arxiv.org/pdf/1102.5761 — HTTP 200, 1522266 bytes
- 2026-10-12 — arxiv — https://export.arxiv.org/api/query?search_query=all%3Apercolation+AND+%28all%3Aalgorithm+OR+all%3A%22query+complexity%22+OR+all%3Arevealment%29&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending — HTTP 200, 143532 bytes
- 2026-10-12 — openalex_source — https://api.openalex.org/works?search=Noise+Sensitivity+of+Boolean+Functions+and+Percolation&per-page=8 — HTTP Error 429: Too Many Requests
- 2026-10-12 — openalex_search — https://api.openalex.org/works?search=percolation+crossing+randomized+algorithm+complexity&per-page=40 — HTTP Error 429: Too Many Requests
- 2026-10-12 — crossref — https://api.crossref.org/works?query=percolation+crossing+randomized+algorithm+complexity&rows=40 — HTTP 200, 653715 bytes
- 2026-10-12 — semantic — https://api.semanticscholar.org/graph/v1/paper/search?query=percolation+randomized+algorithm+complexity&limit=40&fields=title%2Cauthors%2Cyear%2Cabstract%2Curl%2CexternalIds — HTTP Error 429: 
- 2026-10-12 — github — https://api.github.com/search/repositories?q=percolation+crossing+algorithm&per_page=30 — HTTP 200, 5919 bytes
- 2026-10-12 — arxiv_target — https://export.arxiv.org/api/query?search_query=abs%3Apercolation+AND+%28abs%3Arevealment+OR+abs%3A%22decision+tree%22+OR+abs%3A%22randomized+algorithm%22+OR+abs%3A%22randomised+algorithm%22+OR+abs%3A%22query+complexity%22%29&max_results=100&sortBy=relevance — HTTP 200, 217717 bytes
- 2026-10-12 — arxiv_chemical — https://export.arxiv.org/api/query?search_query=abs%3Apercolation+AND+%28abs%3A%22shortest+crossing%22+OR+abs%3A%22chemical+distance%22%29&max_results=35&sortBy=relevance — HTTP 200, 58833 bytes
- 2026-10-12 — crossref_target — https://api.crossref.org/works?query.bibliographic=randomized+algorithms+percolation+decision+trees+revealment&rows=25 — HTTP 200, 83213 bytes
- 2026-10-12 — crossref_source — https://api.crossref.org/works?query.title=Noise+Sensitivity+of+Boolean+Functions+and+Percolation&rows=4 — HTTP 200, 29715 bytes
- 2026-10-12 — openalex_retry — https://api.openalex.org/works?search=percolation+revealment&per-page=25 — HTTP Error 429: Too Many Requests
- 2026-10-12 — openalex_arxiv — https://api.openalex.org/works/https://arxiv.org/abs/1102.5761 — HTTP Error 429: Too Many Requests
- 2026-10-12 — semantic_source — https://api.semanticscholar.org/graph/v1/paper/ARXIV:1102.5761?fields=title,year,citationCount,citations.title,citations.year,citations.externalIds — HTTP 200, 28753 bytes
- 2026-10-12 — semantic_retry — https://api.semanticscholar.org/graph/v1/paper/search?query=percolation+revealment&limit=20&fields=title%2Cauthors%2Cyear%2Curl%2CexternalIds — HTTP Error 429: 
- 2026-10-12 — 2606.32024 — https://arxiv.org/pdf/2606.32024 — HTTP 200, 473098 bytes
- 2026-10-12 — 2408.12995 — https://arxiv.org/pdf/2408.12995 — HTTP 200, 632616 bytes
- 2026-10-12 — 2408.08457 — https://arxiv.org/pdf/2408.08457 — HTTP 200, 265498 bytes
- 2026-10-12 — 2609.15388 — https://arxiv.org/pdf/2609.15388 — HTTP 200, 549084 bytes
- 2026-10-12 — 1708.03643 — https://arxiv.org/pdf/1708.03643 — HTTP 200, 722401 bytes
- 2026-10-12 — openalex_doi — https://api.openalex.org/works/doi:10.1017/cbo9781139924160 — HTTP 200, 20163 bytes
- 2026-10-12 — openalex_citing — https://api.openalex.org/works?filter=cites%3AW1590619386&per-page=200 — HTTP Error 429: Too Many Requests
- 2026-10-12 — openalex_citing_retry — https://api.openalex.org/works?filter=cites:W1590619386&per-page=25 — HTTP Error 429: Too Many Requests
- 2026-10-12 — arxiv_hex — https://export.arxiv.org/api/query?search_query=ti%3A%22Random-turn+hex%22&max_results=4 — HTTP 200, 2509 bytes
- 2026-10-12 — arxiv_cost_exact — https://export.arxiv.org/api/query?search_query=abs%3Apercolation+AND+%28abs%3A%22algorithmic+complexity%22+OR+abs%3A%22computational+complexity%22%29&max_results=40 — HTTP 200, 37478 bytes
- 2026-10-12 — random_turn_hex — https://arxiv.org/pdf/math/0508580 — HTTP 200, 443079 bytes

## Saved result inventories


### arxiv

- http://arxiv.org/abs/2609.39980v1 — Logical information localisation in stabiliser codes via single-qubit measurements
- http://arxiv.org/abs/2609.36886v1 — Static versus dynamic universality in the site-diluted kagome Ising model
- http://arxiv.org/abs/2609.31860v1 — Mechanical Clustering of Cells via the ExtraCellular Matrix
- http://arxiv.org/abs/2609.26367v1 — An Operator-Theoretic Model of Entanglement Percolation in Series-Parallel Quantum Networks
- http://arxiv.org/abs/2609.19905v1 — Percolation Markov Decision Processes
- http://arxiv.org/abs/2609.19686v1 — Superconductivity at the metal-insulator phase boundary in a bulk nickelate at ambient pressure
- http://arxiv.org/abs/2609.22301v2 — Towards the spin-glass transition in finite dimensions via blue percolation
- http://arxiv.org/abs/2609.14510v1 — Unveiling healthcare-access inequality in Ghana using a multiscale approach
- http://arxiv.org/abs/2609.10887v1 — STV Audit Graphs: A Visual Tool to Measure Election Stability
- http://arxiv.org/abs/2609.07763v2 — Topographic Disorder, Wind Coupling, and Directional Fire Spread: Critical Behavior in a Terrain-Weighted Forest Fire Model
- http://arxiv.org/abs/2609.06176v1 — Long induced cycles in pseudorandom graphs
- http://arxiv.org/abs/2608.27613v1 — Criticality and universality in network dismantling
- http://arxiv.org/abs/2608.23340v1 — Anomalous stabilization of excitons by metallic proximity
- http://arxiv.org/abs/2608.23135v1 — Graph distance and effective resistance of the random walk trace in four and five dimensions
- http://arxiv.org/abs/2608.20750v1 — Two-dimensional percolation with algebraically decaying interactions II: Critical exponents in the long-range regime
- http://arxiv.org/abs/2608.20100v1 — Fluctuation-Controlled Asymmetric Kinetics in Metal-Insulator Transitions
- http://arxiv.org/abs/2608.19768v1 — Cluster finding with outskirt stellar masses and percolation
- http://arxiv.org/abs/2608.19489v1 — Fast Algorithms for Stoquastic Spin Systems
- http://arxiv.org/abs/2608.13992v1 — Testing the Reptation Picture: Topological Constraint from Monomer Dynamics
- http://arxiv.org/abs/2608.06895v1 — Local Structure Dictates Ionic Transport and Mechanical Properties in Glassy Solid Electrolytes for Lithium Batteries
- http://arxiv.org/abs/2608.03671v1 — Microscopic Origin of Random Singlet Behavior in B-site Disordered Spin-1/2 Perovskite BaCu_1/3Nb_2/3O_3 Revealed by EXAFS and Thermodynamics
- http://arxiv.org/abs/2607.28865v2 — First-Passage Percolation on Spread-out line graphs: Microscopic Regime
- http://arxiv.org/abs/2607.24975v1 — Strongly-connected percolation on directed lattices
- http://arxiv.org/abs/2607.23259v2 — Microphase Separation in Quorum-Sensing Active Particles with Competing Interactions
- http://arxiv.org/abs/2607.19221v1 — Statistical properties of quadrangular surfaces
- http://arxiv.org/abs/2607.18991v1 — Random site percolation with complex neighborhoods in five dimension
- http://arxiv.org/abs/2607.13364v1 — Direct Imaging of Temperature Evolution of Polar Nanoregions and Chemically Ordered Regions in PMN Relaxor: Evidence for Polar Phase Percolation
- http://arxiv.org/abs/2607.13231v1 — Conflict, mobility and fragmentation in the African interurban network
- http://arxiv.org/abs/2607.08048v1 — Active Particles Imprint Persistent Percolating Networks in Polymer Condensates
- http://arxiv.org/abs/2607.05695v1 — Structural Divergence of the Roman--Byzantine Trade Network, 0--1453\,CE: Persistent Homology, Topological Velocity, and Criticality Indicators of Imperial Collapse
- http://arxiv.org/abs/2607.04693v1 — Supercritical fluid of quantum electrons in three-dimensional superconducting fullerides
- http://arxiv.org/abs/2607.03698v1 — Graph-Based Kirchhoff Modeling of Non-Ohmic Electron Transport in Self-Assembled Nanonecklace Networks
- http://arxiv.org/abs/2606.30242v1 — Quantum percolation based dynamic propagation connectivity for critical-area identification in transport networks
- http://arxiv.org/abs/2606.22398v1 — Percolation of Zero-Weight Paths and the Shape of the Phase Boundary in the Two-Dimensional Random-Bond Ising Model
- http://arxiv.org/abs/2606.20347v1 — Critical Percolation as a Synthetic Data Model for Interpretability
- http://arxiv.org/abs/2606.19030v1 — Large-deviation tails of critical order-parameter distributions
- http://arxiv.org/abs/2606.17763v1 — Electronic access to glass transition in supercooled ionic liquids using ambipolar transistor
- http://arxiv.org/abs/2606.17191v1 — How twist angle inhomogeneity masks the BKT transition and the order parameter symmetry
- http://arxiv.org/abs/2606.14888v1 — Atomistic insights into the structural, thermal, and mechanical evolution of $Zr_{47.5}Cu_{47.5}Ag_{5}$ bulk metallic glass
- http://arxiv.org/abs/2606.14661v1 — Percolation of a rod-like particle in a static bed of spheres: trapping and passing
- http://arxiv.org/abs/2606.12399v1 — Revealing Peri-Urban Dislocation through Percolation Analysis
- http://arxiv.org/abs/2606.07671v2 — Stability and thermodynamic properties of bound magnetic polarons in ferromagnetic semiconductors: Beyond the Gaussian approximation
- http://arxiv.org/abs/2606.04748v1 — Percolation Criticality of Amorphous-Amorphous Transitions in Compressed Glasses
- http://arxiv.org/abs/2606.04070v1 — Quantum circuit partition as a maze: emerging percolation transition via path finding
- http://arxiv.org/abs/2606.02048v1 — Topological texture analysis of microscopy images of dynamic casein gelation and its relation to rheological properties
- http://arxiv.org/abs/2606.01627v1 — The geometry of the giant component of random geometric graphs
- http://arxiv.org/abs/2605.31107v1 — Clustering in atom probe tomography data: coordination number metric, percolation-based parameter scaling, and size effects
- http://arxiv.org/abs/2605.29745v1 — Geometry and localization: Probing Localization Landscape Theory on the Bethe Lattice
- http://arxiv.org/abs/2605.29552v1 — Emergence of Dynamical Anisotropy induced by Demixing in a Binary System with Differential Diffusivity under an External Potential
- http://arxiv.org/abs/2605.28386v1 — Order by inertia in spinning active matter: holey fluids and spin-textured crystals
- http://arxiv.org/abs/2605.28191v1 — Spatiotemporal Tracking in Cooperative ISAC Networks: A Stochastic Geometry Framework
- http://arxiv.org/abs/2605.18312v1 — Energy-Weighted Site Percolation in Two Dimensions
- http://arxiv.org/abs/2605.15066v2 — The critical activation density in graph bootstrap percolation
- http://arxiv.org/abs/2605.14910v1 — Sharp Phase Transition for the Formation of Infinite Tubes
- http://arxiv.org/abs/2605.11310v1 — Random-h Fractional-Dimensional Lattices Reveal Endpoint-Compressed Percolation Activation between Two and Three Dimensions
- http://arxiv.org/abs/2605.16368v2 — A Unified Critical Scaling Theory for Macroscopic Lightning and Quantum Avalanches: From Three-Dimensional Directed Percolation to Testable Predictions
- http://arxiv.org/abs/2605.07867v1 — Cluster Dynamics Stay Fast-Until Tricriticality
- http://arxiv.org/abs/2605.05894v2 — Intrinsic Floquet Generation and $1/I$ Quantum Oscillations in a Sliding Charge-Density Wave
- http://arxiv.org/abs/2605.04376v1 — GraphPI: Efficient Protein Inference with Graph Neural Networks
- http://arxiv.org/abs/2605.01151v1 — Threshold-Controlled Geometric Reorganization in 2D Bootstrap Percolation

### arxiv_target

- http://arxiv.org/abs/2408.08457v2 — Percolation Inequalities and Decision Trees
- http://arxiv.org/abs/2404.08873v2 — Bond percolation does not simulate site percolation
- http://arxiv.org/abs/2101.07180v3 — Phase transitions and noise sensitivity on the Poisson space via stopping sets and decision trees
- http://arxiv.org/abs/1803.03307v3 — Criticality and covered area fraction in confetti and Voronoi percolation
- http://arxiv.org/abs/2402.08927v1 — Critical speeding-up in dynamical percolation
- http://arxiv.org/abs/math/0504586v2 — Quantitative noise sensitivity and exceptional times for percolation
- http://arxiv.org/abs/2209.00999v1 — Almost sharp sharpness for Poisson Boolean percolation
- http://arxiv.org/abs/1906.02666v3 — Bargmann-Fock percolation is noise sensitive
- http://arxiv.org/abs/2003.12018v2 — The asymptotic distribution of cluster sizes for supercritical percolation on random split trees
- http://arxiv.org/abs/2210.16100v3 — An OSSS-type inequality for uniformly drawn subsets of fixed size
- http://arxiv.org/abs/1708.03054v2 — Noise sensitivity and Voronoi percolation
- http://arxiv.org/abs/1210.6134v1 — In-Network Estimation of Frequency Moments
- http://arxiv.org/abs/1907.05107v1 — Percolation description of charge transport in amorphous oxide semiconductors
- http://arxiv.org/abs/2509.16162v2 — Sharpness of the phase transition for constrained-degree percolation
- http://arxiv.org/abs/1705.03104v2 — Sharp phase transition for the random-cluster and Potts models via decision trees
- http://arxiv.org/abs/2505.12643v1 — Thermodynamic analysis of diverse percolation transitions
- http://arxiv.org/abs/2206.04483v1 — Characterizing spatial point processes by percolation transitions
- http://arxiv.org/abs/2005.12705v3 — Molecular-shape- and size-independent power-law dependence of percolation thresholds on radius of gyration in ideal molecular systems
- http://arxiv.org/abs/1609.07275v1 — Critical behavior of $k$-core percolation: Numerical studies
- http://arxiv.org/abs/2401.11862v1 — Effects of Different Q-swaps Modes on Percolation Threshold in Small-world Quantum Networks
- http://arxiv.org/abs/2305.14021v3 — Iterative Site Percolation on Triangular Lattice
- http://arxiv.org/abs/2208.07462v4 — Speeding up random walk mixing by starting from a uniform vertex
- http://arxiv.org/abs/2409.16786v2 — Hierarchy of percolation patterns in a kinetic replication model
- http://arxiv.org/abs/cond-mat/0207202v1 — Slow regions percolate near glass transition
- http://arxiv.org/abs/cond-mat/0610688v1 — Phase Transition and Critical Dynamics in Diluted Josephson Junction Arrays
- http://arxiv.org/abs/cond-mat/0505440v1 — Target-searching on the percolation
- http://arxiv.org/abs/2306.11672v2 — Critical percolation in the ordering kinetics of twisted nematic phases
- http://arxiv.org/abs/1807.03698v1 — Thermal Percolation Threshold and Thermal Properties of Composites with Graphene and Boron Nitride Fillers
- http://arxiv.org/abs/2204.13067v3 — The dynamic nature of percolation on networks with triadic interactions
- http://arxiv.org/abs/1601.05996v1 — Discrete Scale Invariance in Supercritical Percolation
- http://arxiv.org/abs/1412.3678v2 — Predicting percolation thresholds in networks
- http://arxiv.org/abs/1809.06575v1 — How does bond percolation happen in coloured networks?
- http://arxiv.org/abs/hep-lat/0601011v1 — Where is the confining string in random percolation
- http://arxiv.org/abs/2006.06839v1 — Jamming and percolation of dimers in restricted-valence random sequential adsorption
- http://arxiv.org/abs/2306.11857v2 — Critical properties of the optical field localization in a three-dimensional percolating system: Theory and experiment
- http://arxiv.org/abs/1505.02276v2 — Phase ordering percolation and an infinite domain wall in segregating binary Bose-Einstein condensates
- http://arxiv.org/abs/1103.0922v1 — Impact of Single Links in Competitive Percolation -- How complex networks grow under competition
- http://arxiv.org/abs/1110.4288v2 — Ordinary Percolation with Discontinuous Transitions
- http://arxiv.org/abs/1810.00633v2 — Redefinition of site percolation in light of entropy and the second law of thermodynamics
- http://arxiv.org/abs/1701.04117v2 — Cluster Formation and Percolation in Ethanol-Water mixtures
- http://arxiv.org/abs/1906.03966v1 — Percolation of aligned rigid rods on two-dimensional triangular lattices
- http://arxiv.org/abs/1104.5376v2 — Gaussian model of explosive percolation in three and higher dimensions
- http://arxiv.org/abs/2104.05457v1 — Higher-order percolation processes on multiplex hypergraphs
- http://arxiv.org/abs/1101.0775v1 — Percolate or die: Multi-percolation decides the struggle between competing innovations
- http://arxiv.org/abs/cond-mat/0011140v1 — Etching of random solids: hardening dynamics and self-organized fractality
- http://arxiv.org/abs/2307.15346v2 — The nature of hypergraph $k$-core percolation problems
- http://arxiv.org/abs/2509.13500v1 — Sandpiles with finite-range interactions
- http://arxiv.org/abs/1805.00695v2 — Subcritical phase of $d$-dimensional Poisson-Boolean percolation and its vacant set
- http://arxiv.org/abs/2601.07115v1 — Percolation-Driven Magnetotransport due to Structural and Microstructural Evolution in Ultrathin Si/Fe Bilayers
- http://arxiv.org/abs/2510.22148v1 — Berezinskii-Kosterlitz-Thouless Transition and Multifractal Critical Phase in Two-Dimensional Quantum Percolation
- http://arxiv.org/abs/2411.04748v1 — Self-similar gap dynamics in percolation and rigidity percolation
- http://arxiv.org/abs/cond-mat/0404265v1 — Global Physics: From Percolation to Terrorism, Guerilla Warfare and Clandestine Activities
- http://arxiv.org/abs/2410.24068v1 — Universal Scaling of Gap Dynamics in Percolation
- http://arxiv.org/abs/1707.00348v3 — Rare events and discontinuous percolation transitions
- http://arxiv.org/abs/cond-mat/0602611v2 — k-core (bootstrap) percolation on complex networks: Critical phenomena and nonlocal effects
- http://arxiv.org/abs/2601.09747v2 — Topological Percolation in Urban Dengue Transmission: A Multi-Scale Analysis of Spatial Connectivity
- http://arxiv.org/abs/cond-mat/0301317v1 — On reducing Terrorism Power: A Hint from Physics
- http://arxiv.org/abs/2302.03032v1 — Particle migration in porous media: from the mesoscopic perspective
- http://arxiv.org/abs/1406.1674v3 — Opinion formation models on a gradient
- http://arxiv.org/abs/0704.0494v1 — Vortex Dynamics at the Initial Stage of Resistive Transition in Superconductors with Fractal Cluster Structure
- http://arxiv.org/abs/1112.0557v1 — Non-Local Product Rules for Percolation
- http://arxiv.org/abs/2112.04264v2 — Description of laminar-turbulent transition of an airfoil boundary layer measured by differential image thermography using directed percolation theory
- http://arxiv.org/abs/2603.21303v2 — The phase boundary of the random site Ising model
- http://arxiv.org/abs/2504.18861v1 — Percolation in the two-dimensional Ising model
- http://arxiv.org/abs/2606.14661v1 — Percolation of a rod-like particle in a static bed of spheres: trapping and passing
- http://arxiv.org/abs/2402.15462v5 — Unveiling the Importance of Nonshortest Paths in Quantum Networks
- http://arxiv.org/abs/1404.4470v4 — Two Types of Discontinuous Percolation Transitions in Cluster Merging Processes
- http://arxiv.org/abs/1805.00894v2 — Controlling the uncertain response of real multiplex networks to random damage
- http://arxiv.org/abs/2002.08079v1 — History-dependent percolation on multiplex networks
- http://arxiv.org/abs/2004.09644v1 — Site-bond percolation solution to preventing the propagation of \textit{Phytophthora} zoospores on plantations
- http://arxiv.org/abs/1703.10373v1 — Two-step percolation in aggregating systems
- http://arxiv.org/abs/0912.4471v1 — Origin of the Cosmic Network: Nature vs Nurture
- http://arxiv.org/abs/2602.11579v1 — Coupling Lattice Distortion and Cation Disorder to Control Li-ion Transport in Cation-Disordered Rocksalt Oxides
- http://arxiv.org/abs/1608.05469v2 — Topology and geometry of the dark matter web: a multistream view
- http://arxiv.org/abs/2210.00337v1 — Flow induced rigidity percolation in shear thickening suspensions
- http://arxiv.org/abs/2101.12142v2 — Properties of hydrogen bonded network in ethanol-water liquid mixtures as a function of temperature: diffraction experiments and computer simulations
- http://arxiv.org/abs/1907.09957v1 — Explosive Phenomena in Complex Networks
- http://arxiv.org/abs/2601.06291v1 — Confinement-controlled chase-escape dynamics
- http://arxiv.org/abs/2406.15185v3 — Percolation transition of k-frequent destinations network for urban mobility
- http://arxiv.org/abs/cond-mat/0008110v1 — Angular Structure of Lacunarity, and the Renormalisation Group
- http://arxiv.org/abs/2007.10691v1 — Nonequilibrium continuous phase transition in colloidal gelation with short-range attraction
- http://arxiv.org/abs/1801.01116v4 — The Shape and Size distribution of HII Regions near the percolation transition
- http://arxiv.org/abs/1907.12451v1 — Percolation phase transition by removal of $k^{2}$-mers from fully occupied lattices
- http://arxiv.org/abs/1902.03746v1 — Electrical percolation in metal wire network based strain sensors
- http://arxiv.org/abs/2502.08399v3 — Ferromagnetic Resonance in a Magnetically Dilute Percolating Ferromagnet: An Experimental and Theoretical Study
- http://arxiv.org/abs/2409.15123v2 — The geometric phase transition of the three-dimensional $\mathbb{Z}_2$ lattice gauge model
- http://arxiv.org/abs/2502.01121v3 — Universality of percolation at dynamic pseudocritical point
- http://arxiv.org/abs/1008.5072v1 — Semiflexible Filamentous Composites
- http://arxiv.org/abs/1206.1233v1 — Fracturing highly disordered materials
- http://arxiv.org/abs/2606.19030v1 — Large-deviation tails of critical order-parameter distributions
- http://arxiv.org/abs/cond-mat/0002298v1 — Surface Hardening and Self-Organized Fractality Through Etching of Random Solids
- http://arxiv.org/abs/1703.06740v1 — Heterogeneous micro-structure of percolation in sparse networks
- http://arxiv.org/abs/0805.1449v2 — A sequential algorithm for fast clique percolation
- http://arxiv.org/abs/1605.04936v1 — Percolation network dynamicity and sheet dynamics governed viscous behavior of poly-dispersed Graphene nano-sheet suspensions
- http://arxiv.org/abs/1506.03049v2 — Formation and growth of shear bands in glasses: existence of an underlying directed percolation transition
- http://arxiv.org/abs/2410.03681v1 — Gaussian Level-Set Percolation on Complex Networks
- http://arxiv.org/abs/cond-mat/0303003v1 — Temperature Dependence of Microwave Loss, Electronic Transport and Magnetic Parameters in Polycrystalline Perovskite Manganites - Evidence that the Magnetic and the Metal-Insulator Transitions are not Identical
- http://arxiv.org/abs/cond-mat/0110067v1 — Improved percolation thresholds for rods in three-dimensional boxes
- http://arxiv.org/abs/cond-mat/0211240v2 — Asynchronously parallelised percolation on distributed machines
- http://arxiv.org/abs/astro-ph/9605041v2 — Percolation Analysis of a Wiener Reconstruction of the IRAS 1.2 Jy Redshift Catalog

### arxiv_chemical

- http://arxiv.org/abs/1506.03461v1 — On the chemical distance in critical percolation
- http://arxiv.org/abs/1602.00775v1 — Recent work on chemical distance in critical percolation
- http://arxiv.org/abs/1601.03464v1 — On the chemical distance in critical percolation II
- http://arxiv.org/abs/1803.03141v2 — Regularity of the time constant for a supercritical Bernoulli percolation
- http://arxiv.org/abs/2011.04955v2 — On the chemical distance exponent for the two-sided level-set of the 2D Gaussian free field
- http://arxiv.org/abs/1308.2282v2 — Large deviations for simple random walk on percolations with long-range correlations
- http://arxiv.org/abs/2604.14122v1 — The scaling limit of random walk and the intrinsic metric on planar critical percolation
- http://arxiv.org/abs/math/0304144v1 — Asymptotic shape for the chemical distance and first-passage percolation in random environment
- http://arxiv.org/abs/2602.01036v1 — Superconcentration and chaos in Bernoulli percolation
- http://arxiv.org/abs/0907.0697v1 — Déviations modérées de la distance chimique
- http://arxiv.org/abs/0907.0698v1 — Moderate deviations for the chemical distance in Bernoulli percolation
- http://arxiv.org/abs/1407.6926v1 — Variational problems with percolation: rigid spin systems
- http://arxiv.org/abs/1605.04449v4 — Chemical distances for percolation of planar Gaussian free fields and critical random walk loop soups
- http://arxiv.org/abs/2309.04667v1 — Nontrivial upper bound for chemical distance on the planar random cluster model
- http://arxiv.org/abs/2312.03550v2 — Lipschitz-continuity of time constant in generalized First-passage percolation
- http://arxiv.org/abs/2501.02881v1 — Chemical Distance for the Level Sets of the Gaussian Free Field
- http://arxiv.org/abs/1807.11117v2 — Percolation for level-sets of Gaussian free fields on metric graphs
- http://arxiv.org/abs/math/0409317v3 — Large deviations for the chemical distance in supercritical Bernoulli percolation
- http://arxiv.org/abs/2211.02605v2 — On the upper tail large deviation rate function for chemical distance in supercritical percolation
- http://arxiv.org/abs/2005.08934v3 — Chemical subdiffusivity of critical 2D percolation
- http://arxiv.org/abs/1411.6824v1 — From heavy-tailed Boolean models to scale-free Gilbert graphs
- http://arxiv.org/abs/1708.03643v1 — Strict inequality for the chemical distance exponent in two-dimensional critical percolation
- http://arxiv.org/abs/2503.22434v1 — Chemical distance for smooth Gaussian fields in higher dimension
- http://arxiv.org/abs/2508.10470v2 — Existence and uniqueness of the conformally covariant geodesic metric on non-simple conformal loop ensemble gaskets
- http://arxiv.org/abs/1212.2885v3 — On chemical distances and shape theorems in percolation models with long-range correlations
- http://arxiv.org/abs/1502.05379v1 — Bounded-hop percolation
- http://arxiv.org/abs/2605.31568v2 — Lipschitz continuity of the time constant for continuum percolation
- http://arxiv.org/abs/1112.3428v4 — Shortest-Path Fractal Dimension for Percolation in Two and Three Dimensions
- http://arxiv.org/abs/2103.09786v1 — Euclidean and chemical distances in ellipses percolation
- http://arxiv.org/abs/2112.09116v2 — Phase transition for level-set percolation of the membrane model in dimensions $d \geq 5$
- http://arxiv.org/abs/cond-mat/0203089v1 — Survival probability and order statistics of diffusion on disordered media
- http://arxiv.org/abs/2604.21341v1 — Fractals of Simple Random Walks in Two Dimensions: A Monte Carlo Study
- http://arxiv.org/abs/2505.10582v1 — The contact process on Scale-Free Percolation
- http://arxiv.org/abs/2009.04044v1 — On Chemical Distance and Local Uniqueness of a Sufficiently Supercritical Finitary Random Interlacement
- http://arxiv.org/abs/cond-mat/0206198v2 — Stochastic Renormalization Group in Percolation: I. Fluctuations and Crossover

### arxiv_hex

- http://arxiv.org/abs/math/0508580v2 — Random-Turn Hex and other selection games

### arxiv_cost_exact

- http://arxiv.org/abs/1102.5014v1 — Randomized algorithms for statistical image analysis and site percolation on square lattices
- http://arxiv.org/abs/2408.12995v1 — A study of distributional complexity measures for Boolean functions
- http://arxiv.org/abs/1102.4803v1 — Detection of objects in noisy images and site percolation on square lattices
- http://arxiv.org/abs/1204.3844v1 — On how percolation threshold affects PSO performance
- http://arxiv.org/abs/1102.4811v1 — Robust nonparametric detection of objects in noisy images
- http://arxiv.org/abs/cond-mat/9906036v1 — Low-density series expansions for directed percolation I: A new efficient algorithm with applications to the square lattice
- http://arxiv.org/abs/2404.13942v1 — Dominic Welsh (1938-2023)
- http://arxiv.org/abs/1310.8574v1 — Spatial statistics, image analysis and percolation theory
- http://arxiv.org/abs/2211.02346v2 — Improving mean-field network percolation models with neighbourhood information
- http://arxiv.org/abs/1503.05270v4 — Efficiently Controllable Graphs
- http://arxiv.org/abs/cond-mat/9503170v1 — The Computational Complexity of Generating Random Fractals
- http://arxiv.org/abs/1605.00897v2 — Covering Problems and Core Percolations on Hypergraphs
- http://arxiv.org/abs/2209.01777v3 — Neural Network Approach to Scaling Analysis of Critical Phenomena
- http://arxiv.org/abs/2303.10423v4 — Random site percolation thresholds on square lattice for complex neighborhoods containing sites up to the sixth coordination zone
- http://arxiv.org/abs/1603.08273v1 — Collective Influence Algorithm to find influencers via optimal percolation in massively large social media
- http://arxiv.org/abs/1810.08484v1 — On the complexity of color-avoiding site and bond percolation
- http://arxiv.org/abs/2210.16100v3 — An OSSS-type inequality for uniformly drawn subsets of fixed size
- http://arxiv.org/abs/2005.11758v2 — On the impact of treewidth in the computational complexity of freezing dynamics

### crossref

- ['Percolation'] — DOI 10.23943/princeton/9780691176840.003.0004
- ['PERCOLATION'] — DOI 10.2307/j.ctt1vwmgzt.7
- ['Percolation: Crossing the great divide of bulk heterogeneous matter'] — DOI 10.1016/b978-0-443-33540-2.00029-9
- ['Continuum Percolation'] — DOI 10.1007/978-3-642-27737-5_95-3
- ['4. PERCOLATION'] — DOI 10.1515/9781400885497-005
- None — DOI 10.1049/iet-tv.48.12148
- ['Continuum Percolation'] — DOI 10.1007/978-0-387-30440-3_95
- ['Crossing probabilities for Voronoi percolation'] — DOI 10.1214/15-aop1052
- ['FirnPerc: An intermediate-complexity water percolation model for firn'] — DOI 10.5194/egusphere-egu26-7173
- ['Percolation, Introduction to'] — DOI 10.1007/978-3-642-27737-5_385-4
- ['Percolation Phase Transition'] — DOI 10.1007/978-3-642-27737-5_387-3
- ['Crossing probability and number of crossing clusters in off-critical percolation'] — DOI 10.1088/1751-8113/45/3/032005
- ['Percolation, Introduction to'] — DOI 10.1007/978-0-387-30440-3_385
- ['Correlated Percolation'] — DOI 10.1007/978-3-642-27737-5_104-3
- ['Percolation Phase Transition'] — DOI 10.1007/978-3-642-27737-5_387-4
- ['Percolation Phase Transition'] — DOI 10.1007/978-0-387-30440-3_387
- ['Percolation, Introduction to'] — DOI 10.1007/978-3-642-27737-5_385-5
- ['Complexity and Algorithms'] — DOI 10.1201/9781315152394-4
- ['Elastic Percolation Networks'] — DOI 10.1007/978-3-642-27737-5_170-3
- ['Basics of Complexity'] — DOI 10.1201/9781315152394-14
- ['A new conceptual model for forest fires based on percolation theory'] — DOI 10.1002/cplx.20194
- ['Invasion Percolation'] — DOI 10.1007/978-0-387-30440-3_294
- ['Correlated Percolation'] — DOI 10.1007/978-3-642-27737-5_104-4
- ['Percolation Thresholds, Exact'] — DOI 10.1007/978-0-387-30440-3_390
- ['Correlated Percolation'] — DOI 10.1007/978-0-387-30440-3_104
- ['Social percolation in relations between activists and supporters'] — DOI 10.1002/cplx.20139
- ['Elastic Percolation Networks'] — DOI 10.1007/978-0-387-30440-3_170
- ['Addressing Complexity and Difference in Research Methodology'] — DOI 10.1057/9781137468741.0007
- ['Explosive Percolation Processes'] — DOI 10.1007/978-3-642-27737-5_628-1
- ['Crossing probabilities for planar percolation'] — DOI 10.1215/00127094-2022-0015
- ['An Optimal Bit Complexity Randomized Distributed MIS Algorithm (Extended Abstract)'] — DOI 10.1007/978-3-642-11476-2_25
- ['Percolation and Polymer Morphology and Rheology'] — DOI 10.1007/978-3-642-27737-5_388-3
- ['Percolation Theories for Multipartite Networked Systems under Random Failures'] — DOI 10.1155/2020/3974503
- ['The complexity excuse'] — DOI 10.1201/9780429020810-27
- ['The lowest crossing in two-dimensional critical percolation'] — DOI 10.1214/aop/1055425778
- ['Percolation in Complex Networks'] — DOI 10.1007/978-0-387-30440-3_383
- ['Percolation in Porous Media'] — DOI 10.1007/978-0-387-30440-3_389
- ['Percolation and Polymer Morphology and Rheology'] — DOI 10.1007/978-0-387-30440-3_388
- ['Percolation and Polymer Morphology and Rheology'] — DOI 10.1007/978-3-642-27737-5_388-4
- ['Percolation theory suggests some general features in range margins across environmental gradients'] — DOI 10.1016/j.ecocom.2020.100814

### crossref_target

- ['APPROXIMATION ALGORITHMS FOR DECISION TREES'] — DOI 10.17771/pucrio.acad.56533
- ['Percolation on random recursive trees'] — DOI 10.1002/rsa.20603
- ['Randomized algorithms and noise sensitivity'] — DOI 10.1017/cbo9781139924160.009
- ['Decision Trees'] — DOI 10.1002/9781394345816.ch02
- ['Decision Trees'] — DOI 10.1201/9781315371658-11
- ['Popular Decision Trees Induction Algorithms'] — DOI 10.1142/9789814590082_0007
- ['Experimental Study of Algorithms for Transforming Decision Rule Systems into Decision Trees'] — DOI 10.5220/0013533300004000
- ['DECISION TREES AND DECISION RULES'] — DOI 10.1002/9781119516057.ch6
- ['Decision Trees and Decision Rules'] — DOI 10.1002/9781118029145.ch6
- ['Self‐destructive percolation as a limit of forest‐fire models on regular rooted trees'] — DOI 10.1002/rsa.20646
- ['Optimal Randomized Algorithms of Weakly-Balanced Multi-Branching And-Or Trees'] — DOI 10.2139/ssrn.4571377
- ['Optimal Randomized Algorithms of Weakly-Balanced Multi-Branching And-Or Trees'] — DOI 10.2139/ssrn.4571795
- ['The asymptotic distribution of cluster sizes for supercritical percolation on random split trees'] — DOI 10.1002/rsa.21046
- ['Decision trees'] — DOI 10.1002/9781118950951.ch3
- ['Decision Trees'] — DOI 10.1017/cbo9781107298019.019
- ['Decision Trees'] — DOI 10.1002/9781119575955.ch12
- ['Chapter 2 Decision Trees'] — DOI 10.1201/9781315371658-3
- ['Multirange percolation on oriented trees: Critical curve and limit behavior'] — DOI 10.1002/rsa.21104
- ['Monotonicity and phase diagram for multirange percolation on oriented trees'] — DOI 10.1002/rsa.20805
- ['Sizes of the largest clusters for supercritical percolation on random recursive trees'] — DOI 10.1002/rsa.20448
- ['Decision and Regression Trees'] — DOI 10.1201/b15288-6
- ['Survival Analysis Algorithms based on Decision Trees with Weighted Log-rank Criteria'] — DOI 10.5220/0010987100003122
- ['Zero-Touch Selection of Virtual Network Embedding Algorithms Using Multi-Objective Decision Trees'] — DOI 10.5220/0014726500004039
- ['Upper Bounds and Algorithms for Construction of Deterministic Decision Trees for Decision Tables. Second Approach'] — DOI 10.1007/978-3-030-41728-4_5
- ['Bounds on Complexity and Algorithms for Construction of Nondeterministic and Strongly Nondeterministic Decision Trees for Decision Tables'] — DOI 10.1007/978-3-030-41728-4_6

### crossref_source

- ['Noise Sensitivity of Boolean Functions and Percolation'] — DOI 10.1017/cbo9781139924160
- ['Book Review: Noise sensitivity of Boolean functions and percolation'] — DOI 10.1090/bull/1591
- ['Noise sensitivity of boolean functions and applications to percolation'] — DOI 10.1007/bf02698830
- ['Noise Sensitivity of Boolean Functions and Applications to Percolation'] — DOI 10.1007/978-1-4419-9675-6_12

## Additional attempt (2026-10-12)

Brain queries: conditional variance queried score O Donnell Servedio percolation influence; Peres Schramm Sheffield Wilson Random Turn Hex pivotal optimal strategy; card walk claim_0c1e55cfd7605d30089c4ffeca09b142d03be5573c9ce9401839396350a60738. No relevant residual variance theorem was returned. The Cerf card was not used because its displayed formula was corrupted.

Read the already saved Peres--Schramm--Sheffield--Wilson arXiv:math/0508580v2, Lemma 3.1 (PDF p.5): maximizing conditional pivotal probability characterizes optimal winning moves in monotone random-turn selection games. It does not assert minimum expected query cost. Theorem 4.1 gives the old 3/2 lower exponent, and the associated length discussion is numerical, not a rigorous new upper exponent. No new external network search was performed in this additional attempt.
