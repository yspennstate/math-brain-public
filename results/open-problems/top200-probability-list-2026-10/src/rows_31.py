# Replacement rows from the T400 run, staged 12 Nov 2026 by an agent. Rename to rows_31.py in the
# same change that retires the rows they replace (see top200_review_2026_11_10/NEXT.md steps 1-3, 6).
ROWS = [{'id': 'T423',
  'd': 'BM',
  't': 'Pathwise uniqueness for the SPDE of super-Brownian motion in one dimension',
  's': 'On R, let W be space-time white noise and let u0 be a deterministic nonnegative smooth function of compact '
       'support. Are any two adapted, nonnegative, continuous, tempered mild solutions with finite total mass of '
       'du=(1/2)u_xx dt+sqrt(u)dW, driven by this same W and initial value, indistinguishable? There is no immigration '
       'term.',
  'c': '',
  'src': 'Burdzy-Mueller-Perkins, Non-uniqueness for non-negative solutions of parabolic stochastic partial '
         'differential equations (arXiv:1008.2126); Chen (arXiv:1308.5141).',
  'loc': '1008.2126, introduction: square-root case without immigration; 1308.5141, distinction from immigration.',
  'url': 'https://arxiv.org/abs/1008.2126',
  'why': 'This asks whether the canonical density equation admits a strong construction from its prescribed noise.',
  'st': 'Weak uniqueness does not give pathwise uniqueness. The nonuniqueness in 1308.5141 includes immigration; the '
        'strong-solution equation in 1203.4873 is a different, cumulative-distribution SPDE.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate C07), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T424',
  'd': 'COMB',
  't': 'The matrix Spencer conjecture',
  's': 'Is there a universal C such that, for every n and every collection of real symmetric n by n matrices A1,...,An '
       'with operator norm at most one, some signs s_i in {-1,1} satisfy ||sum_i s_i A_i||op <= C sqrt(n)?',
  'c': '',
  'src': 'Matrix Spencer conjecture; Bansal-Jiang-Meka, Resolving Matrix Spencer Conjecture Up to Poly-logarithmic '
         'Rank (arXiv:2208.11286).',
  'loc': '2208.11286, introduction and main rank-restricted theorem.',
  'url': 'https://arxiv.org/abs/2208.11286',
  'why': 'This is the matrix counterpart of Spencer discrepancy and removes a logarithm from general bounds.',
  'st': 'Inherited OPEN from the 10 Nov verification. Bansal-Jiang-Meka handle a polylogarithmic rank restriction, not '
        'arbitrary full-rank matrices. The cited primary paper was opened for the formulation; the completed status '
        'search was not repeated.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate C13), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T425',
  'x': "SOLVED (claimed, unrefereed), 14 Nov 2026: the OpenAI math release preprint 'The second Kahn-Kalai conjecture' (24 Sep 2026, github.com/openai/math, Thm 1.1) claims p_c(H) <= C p_E(H) (1 + log_2 e(H)) for every finite simple H with the unlabelled-copy expectation threshold, which is the stated bound up to the constant; Lean files are supplied. AI-written and unrefereed; this records the claim, not a check of the proof. Replacement row to be screened.",
  'd': 'COMB',
  't': 'The second Kahn-Kalai conjecture',
  's': 'Let H=H(n) be a simple graph with at most n vertices. Let p_c(H) be the least p for which G(n,p) contains H '
       'with probability at least 1/2. Let p_E(H) be the least p for which every nonempty edge-induced F subset H has '
       'expected number of unlabelled copies in G(n,p) at least 1/2. Is p_c(H) <= C p_E(H) log(2+e(H)) for a universal '
       'C?',
  'c': 'The source uses log e(H); log(2+e(H)) avoids the one-edge degeneracy and changes only a universal constant.',
  'src': 'Kahn-Kalai, Conjecture 2; formulation in Mossel et al., arXiv:2209.03326.',
  'loc': '2209.03326, Section 1, definition (1) and the displayed second Kahn-Kalai conjecture.',
  'url': 'https://arxiv.org/abs/2209.03326',
  'why': 'A proof would express graph containment thresholds through ordinary first moments.',
  'st': 'Inherited OPEN from the 10 Nov verification. 2209.03326 proves the bound for a larger modified threshold that '
        'counts the multiplicity of each subgraph inside H. That modification does not prove the original conjecture.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate C18), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T426',
  'd': 'RG',
  't': 'Maximum cut and minimum bisection of random regular graphs (Zdeborova-Boettcher)',
  's': 'For every fixed integer d>=3 and uniform simple d-regular G_{n,d} on an even number n of vertices, is '
       'MaxCut(G_{n,d})+MinBis(G_{n,d})=dn/2+o(n) with probability tending to one? MinBis minimizes the number of '
       'crossing edges over partitions with exactly n/2 vertices on each side.',
  'c': 'The additional unspecified Parisi-formula request has been removed.',
  'src': 'Zdeborova-Boettcher, Conjecture on the maximum cut and bisection width in random regular graphs '
         '(arXiv:0912.4861).',
  'loc': '0912.4861, abstract and central conjecture.',
  'url': 'https://arxiv.org/abs/0912.4861',
  'why': 'This relates two apparently different sparse random-graph optimization problems.',
  'st': 'The original source proposes precisely the complement relation. 2609.19057 proves equality of maximum-cut and '
        'maximum-bisection densities; its bisection is a maximum, not the minimum asked here. Large-degree asymptotics '
        'do not settle fixed d.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate C22), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T427',
  'd': 'GEOM',
  't': 'The second-order term in the two-dimensional random matching problem',
  's': 'Let X1,...,Xn be iid uniform points in the unit square, mu_n=(1/n)sum_i delta_Xi, and let lambda be uniform '
       'probability measure on the square. Does c_square=lim_{n to infinity}[n E W_2(mu_n,lambda)^2-(log n)/(4 pi)] '
       'exist as a finite number, and what is its value?',
  'c': 'The two-empirical-sample problem has a different leading coefficient. No unchecked predicted numerical value '
       'is asserted.',
  'src': 'Ambrosio-Stra-Trevisan, A PDE approach to a 2-dimensional matching problem (arXiv:1611.04960); '
         'Ambrosio-Glaudo, Finer estimates (arXiv:1810.07002); Caracciolo et al. (arXiv:1402.6993).',
  'loc': '1611.04960 and 1810.07002, semidiscrete uniform-square matching estimates; 1402.6993, scaling prediction.',
  'url': 'https://arxiv.org/abs/1810.07002',
  'why': 'It is the next geometric term beyond the universal logarithmic matching cost.',
  'st': 'The leading logarithmic term is proved. Finer error estimates and nonconstant-density leading asymptotics do '
        'not identify the finite semidiscrete next-order constant. The heuristic source does not constitute a proof of '
        'this limit.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate C47), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T428',
  'd': 'GF',
  't': 'The critical two-dimensional stochastic heat flow and the two-dimensional KPZ equation at criticality',
  's': 'Prove Conjecture 1.17 of arXiv:2609.15832: retain the other hypotheses and critical tuning of Theorems 1.9 and '
       '1.15, but replace nonnegativity and uniform compact support of the spatial kernels zeta_N by |zeta_N(x)|<=C '
       'exp(-a|x|), uniformly in N, for some C,a>0. Do the discrete and continuum measure-valued flows still converge '
       'in finite-dimensional distributions to the critical two-dimensional stochastic heat flow, with the same '
       'critical-tuning coefficients Lambda_N?',
  'c': 'This is a named remaining conjecture; no undefined logarithm of a singular flow is called a solution of '
       'critical KPZ.',
  'src': 'A universality result for the critical 2d stochastic heat flow (arXiv:2609.15832); Caravenna-Sun-Zygouras '
         '(arXiv:2109.03766).',
  'loc': '2609.15832, Conjecture 1.17, referring to Theorems 1.9/1.15 and Definitions 1.8/1.14.',
  'url': 'https://arxiv.org/abs/2609.15832',
  'why': 'This removes substantive restrictions on spatial regularization from a critical universality theorem.',
  'st': '2609.15832 proves universality for a substantial class of linear flows, including correlated polymers and '
        'mollified Gaussian SPDEs. It explicitly leaves the signed, exponentially decaying spatial-kernel extension as '
        'Conjecture 1.17.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate C54), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T429',
  'd': 'IPS',
  't': 'Poisson-Dirichlet law of the macroscopic cycles of spatial random permutations in three dimensions',
  's': 'Run nearest-neighbour random interchange on the d-dimensional discrete torus of side L, d>=3, from the '
       'identity, with rate-one Poisson transpositions on each edge. At a fixed time beta above the macroscopic-cycle '
       'transition, prove the Poisson-Dirichlet conjecture of Ioffe-Toth: there is a deterministic macroscopic mass '
       'm(beta)>0 and the decreasing cycle lengths divided by L^d converge to m(beta) times PD(1). The microscopic '
       'cycles account for the missing mass.',
  'c': 'The unqualified Bose-gas clause is removed; interaction, boundary conditions and ensemble cannot be silently '
       'interchanged.',
  'src': 'Ioffe-Toth, Split-and-Merge in Stationary Random Stirring on Lattice Torus (arXiv:1909.06188), finite-time '
         'conjectures.',
  'loc': '1909.06188, Section 1.6, Conjectures 1 and 2.',
  'url': 'https://arxiv.org/abs/1909.06188',
  'why': 'This would identify the distribution of the macroscopic loops behind three-dimensional long-range order.',
  'st': 'The theorem in 1909.06188 starts in the stationary uniform-permutation law; its Section 1.6 explicitly '
        'distinguishes the identity-start conjectures. 1007.2224 and 2607.04264 establish Poisson-Dirichlet laws in '
        'annealed or ideal-gas models, not the stated finite-time lattice interchange model.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate D02), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T430',
  'd': 'Q',
  't': 'Asymptotic independence in the supermarket model with general service times',
  's': 'Consider N FIFO unit-rate servers, Poisson arrivals of rate lambda N with 0<lambda<1, iid service requirements '
       'of a fixed law G of mean one, and routing to a shortest queue among d>=2 uniformly sampled servers. In the '
       'stationary law, does the joint state of every fixed k servers converge, as N tends to infinity, to '
       'pi_G^{tensor k} for a single-server law pi_G? The state includes the queue length and service age or residual '
       'requirement.',
  'c': 'The proposed statement fixes FIFO and the full queue state; it does not conflate queue lengths with Markov '
       'states.',
  'src': 'Bramson-Lu-Prabhakar, general-service supermarket ansatz; Decay of tails at equilibrium for FIFO join the '
         'shortest queue networks (arXiv:1106.4582).',
  'loc': '1106.4582, abstract and introduction explaining the asymptotic-independence ansatz.',
  'url': 'https://arxiv.org/abs/1106.4582',
  'why': 'This would justify equilibrium mean-field predictions for realistic service distributions.',
  'st': '1106.4582 states the ansatz and proves tail results conditional on it; it records decreasing-hazard-rate '
        'cases where the ansatz is known. General-service transient propagation of chaos does not by itself justify '
        'exchange with the stationary limit.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate D07), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T431',
  'd': 'BM',
  't': 'Invariance of the Phi^4_3 Gibbs measure under the three-dimensional cubic nonlinear Schrodinger equation',
  's': 'For the defocusing complex cubic NLS on T^3, construct a global measurable flow for almost every initial '
       'condition under the renormalized complex Phi^4_3 Gibbs measure, prove uniqueness in a specified probabilistic '
       'solution class, and prove invariance of that measure. The renormalized equation must be obtained consistently '
       'from its Gibbs-preserving ultraviolet-cutoff flows.',
  'c': 'The complex measure, counterterms, limiting topology and uniqueness class are part of the problem, not an '
       'unrenormalized deterministic cubic equation.',
  'src': 'The three-dimensional Schrodinger counterpart of Bringmann-Deng-Nahmod-Yue, Invariant Gibbs measures for the '
         'three dimensional cubic nonlinear wave equation (arXiv:2205.03893).',
  'loc': '2205.03893, discussion distinguishing the wave equation from the Schrodinger problem.',
  'url': 'https://arxiv.org/abs/2205.03893',
  'why': 'This is a central singular Hamiltonian PDE problem with genuinely rough equilibrium data.',
  'st': 'Inherited OPEN from the 10 Nov verification. The cited work constructs invariant dynamics for the cubic wave '
        'equation; it does not give the corresponding Schrodinger flow. No repeat status search was run.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate D10), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T432',
  'd': 'RMT',
  't': 'The mobility edge for Levy matrices and for sparse Erdos-Renyi graphs',
  's': 'For every 0<alpha<1, prove that the positive-energy equation lambda(E,alpha)=1 in Mobility Edge for Levy '
       'Matrices has exactly one solution E_mob(alpha)>0, with lambda>1 below it and lambda<1 above it. Here lambda is '
       'precisely the Perron-Frobenius/Lyapunov quantity defined in that paper for the alpha-stable '
       'Poisson-weighted-tree limit, not an arbitrary matrix eigenvalue.',
  'c': 'The separate sparse Erdos-Renyi problem is omitted rather than bundled into a different spectral model.',
  'src': 'Aggarwal-Bordenave-Lopatto, Mobility Edge for Levy Matrices (arXiv:2210.09458).',
  'loc': '2210.09458, results and the uniqueness discussion; the paper defines lambda(E,alpha).',
  'url': 'https://arxiv.org/abs/2210.09458',
  'why': 'A unique crossing would complete the single-mobility-edge picture throughout the heavy-tail regime.',
  'st': 'The paper proves localization and delocalization criteria in terms of lambda for general alpha, and proves a '
        'unique crossing when alpha is sufficiently near 0 or 1. The remaining uniqueness at intermediate alpha is '
        'what the proposed row asks.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate D22), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T433',
  'd': 'BM',
  't': 'Convergence of N-player games to mean-field games without monotonicity',
  's': 'Under the boundedness, continuity, compact-control and nondegenerate-idiosyncratic-noise hypotheses of '
       'Lacker-Le Flem, can every weak mean-field equilibrium be obtained as a weak limit of empirical state flows of '
       'closed-loop epsilon_n-Nash equilibria, epsilon_n tending to zero, when the finite-player strategies use only '
       'the game state histories and its prescribed common noise, with no auxiliary public signal?',
  'c': 'This is the proposed remaining converse, not a claim that all nonmonotone mean-field convergence is unsolved. '
       'The integrator should check later refinements of the strategy class.',
  'src': 'Lacker, On the convergence of closed-loop Nash equilibria to the mean field game limit (arXiv:1808.02745); '
         'Lacker-Le Flem, Closed-loop convergence for mean field games with common noise (arXiv:2107.03273).',
  'loc': '2107.03273, introduction and converse construction with an additional common signal.',
  'url': 'https://arxiv.org/abs/2107.03273',
  'why': 'It distinguishes endogenous equilibrium randomness from randomness added by the modeler.',
  'st': 'General weak-limit characterizations already allow nonunique mean-field equilibria. The converse in '
        '2107.03273 permits a broader strategy class with an additional common signal. This row isolates removing that '
        'information enlargement, rather than asking for an already available weak-limit framework.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate D23), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T434',
  'd': 'BM',
  't': 'Multidimensional backward stochastic differential equations with quadratic growth (Peng)',
  's': 'For an m-dimensional BSDE driven by d-dimensional Brownian motion, Y_t=xi+integral_t^T f(Z_s)ds-integral_t^T '
       'Z_s dB_s, consider deterministic homogeneous quadratic generators f_i(z)=sum_{j,k=1}^m a^i_{jk}(z_j dot z_k). '
       'Characterize the coefficient tensors a for which every finite T and every bounded terminal vector xi admit a '
       'unique bounded adapted Y with Z dot B a BMO martingale.',
  'c': 'This precise classification target is an integrator proposal motivated by the cited work, not a quoted '
       'conjecture attributed to Peng.',
  'src': 'Structural well-posedness problem for multidimensional quadratic BSDEs; A class of multidimensional '
         'quadratic BSDEs (arXiv:1703.04153) and Multidimensional quadratic BSDEs with weak interactions '
         '(arXiv:2606.27640).',
  'loc': '2606.27640, introduction and structural/smallness hypotheses; 1703.04153, structural existence results.',
  'url': 'https://arxiv.org/abs/2606.27640',
  'why': 'It asks which couplings permit globally meaningful nonlinear stochastic systems.',
  'st': '2606.27640 explicitly calls general multidimensional quadratic well-posedness open and proves a '
        'weak-interaction class under smallness assumptions. Universal existence without structure is false. This row '
        'asks for a classification in a fixed finite-parameter subclass.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate E20), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md). This formulation is ours, built from '
       'the cited work; it is not a conjecture stated by those authors.'},
 {'id': 'T435',
  'd': 'IPS',
  't': 'The Bak-Sneppen model',
  's': 'For a one-dimensional nearest-neighbour Bak-Sneppen p-avalanche on Z, start with fitness zero at the origin '
       'and one everywhere else: repeatedly resample the current minimum and its two neighbours with independent '
       'Uniform[0,1] values until no value below p remains. Let S_p be its duration and p_c the infimum of p for which '
       'P(S_p=infinity)>0. At p=p_c, does P(S_{p_c}>=t)=t^{-a+o(1)} for a deterministic a>0, and what is a?',
  'c': 'This is an infinite-volume avalanche statement, not an undefined critical threshold of a fixed finite cycle. '
       'The duration convention includes a possible infinite avalanche.',
  'src': 'Gillett-Meester-Nuyens, Bounds for avalanche critical values of the Bak-Sneppen model (arXiv:math/0508167).',
  'loc': 'math/0508167, avalanche critical values and nontriviality bounds.',
  'url': 'https://arxiv.org/abs/math/0508167',
  'why': 'It asks for a rigorous critical exponent in a canonical model of self-organized criticality.',
  'st': 'Nontrivial critical-value bounds already address the proposed p_c<1 clause. They do not establish the '
        'critical avalanche-duration power law of the original one-dimensional model.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate E23), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T436',
  'd': 'PERC',
  't': 'The graph-distance exponent of critical long-range percolation',
  's': 'On Z^d, force nearest-neighbour edges and independently add each other edge {x,y} with probability 1-exp(-beta '
       '|x-y|^{-2d}), beta>0. Determine the distance exponent theta(beta,d) characterized by D(0,n '
       'e1)=n^{theta(beta,d)+o_P(1)}. Give an explicit or otherwise effective analytic characterization beyond its '
       'present existence and qualitative properties.',
  'c': 'Nearest-neighbour edges fix connectivity. The tail coefficient and normalization of beta must be matched to '
       'the cited model before numerical constants are compared.',
  'src': 'Ding-Sly (arXiv:1303.3995); Baeumler, critical long-range distance exponent (arXiv:2208.04793).',
  'loc': '2208.04793, statements on the critical exponent and its dependence on beta.',
  'url': 'https://arxiv.org/abs/2208.04793',
  'why': 'This identifies the metric scaling of a scale-invariant random graph.',
  'st': 'Inherited OPEN from the 10 Nov verification. The exponent exists and has continuity, monotonicity and certain '
        'asymptotic bounds; those results do not identify its value as a function of beta.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate E28), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T437',
  'd': 'Q',
  't': 'The extremal GI/GI/1 queue (Kingman; Daley)',
  's': 'Normalize a stable FIFO GI/GI/1 queue by E A=1, E S=rho<1, Var A=c_a^2 and Var S=rho^2 c_s^2. Let F0 put mass '
       'c_a^2/(1+c_a^2) at 0 and the rest at 1+c_a^2. For b>=rho(1+c_s^2), let G_b be the two-point service law with '
       'these service moments and upper atom b. Is sup_{F,G with these moments} E W(F,G)=lim_{b to infinity} E '
       'W(F0,G_b), where W is stationary Lindley waiting time?',
  'c': 'Attainment by one fixed pair of two-point laws is not asserted. For G_b, its lower atom is rho-rho^2 '
       'c_s^2/(b-rho); degenerate zero-variance cases are interpreted by limits.',
  'src': 'Chen-Whitt, Extremal GI/GI/1 Queues Given Two Moments, author manuscript Extremal_Two_040421.pdf; '
         'comparison: arXiv:1907.13019.',
  'loc': 'Chen-Whitt, Conjecture 1(b), pages 2-3; the longer numerical manuscript gives the corresponding upper-bound '
         'conjecture.',
  'url': 'https://www.columbia.edu/~ww2040/Extremal_Two_040421.pdf',
  'why': 'It would identify the sharp performance bound available from only two moments.',
  'st': 'Chen-Whitt explicitly conjecture a limiting two-point supremum for unbounded support. Their bounded-support '
        'results and numerical evidence do not prove it. 1907.13019 uses mean absolute deviation, a different '
        'constraint from variance.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate F11), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T438',
  'd': 'Q',
  't': 'Optimal scheduling in the M/G/k queue',
  's': 'For every k>=2, Poisson rate lambda and known iid service law G with finite second moment and lambda E[G]<k, '
       'identify a causal preemptive-resume policy that minimizes stationary mean response time in an M/G/k queue. Job '
       'sizes are unknown until completion; the policy observes attained service and the queue history, and a job uses '
       'at most one unit-rate server at a time.',
  'c': 'Known-size scheduling is a different information model; it is not silently mixed with Gittins policies.',
  'src': 'Scully-Grosof-Harchol-Balter, Optimal Multiserver Scheduling with Unknown Job Sizes in Heavy Traffic '
         '(arXiv:2003.13232); Wang-Grosof (arXiv:2502.08804).',
  'loc': '2003.13232, abstract/introduction; 2502.08804, intermediate-load lower-bound framework.',
  'url': 'https://arxiv.org/abs/2003.13232',
  'why': 'An optimal rule would resolve the basic scheduling problem in a standard model of service systems.',
  'st': 'Gittins is optimal for one server. Heavy-traffic optimality and additive approximations for multiple servers '
        'do not identify an optimal policy at every load. The 2025 paper explicitly emphasizes the unresolved '
        'intermediate regime.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate F12), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T439',
  'd': 'STAT',
  't': 'Uniform equilibria in stochastic games with three or more players',
  's': 'Does every finite stochastic game with at least three players, finite state/action spaces, bounded stage '
       'rewards and perfect monitoring have a uniform equilibrium payoff v? Precisely, for every epsilon>0, are there '
       'one strategy profile sigma and n0 such that for all n>=n0 its expected n-stage average payoffs are within '
       'epsilon of v, and no unilateral deviation raises any player payoff above v_i+epsilon?',
  'c': 'Sunspot and correlated equilibria are weaker conclusions and do not answer this question.',
  'src': 'Solan-Vieille, Stochastic games, PNAS 112 (2015); Solan, The Modified Stochastic Games (arXiv:1703.04026).',
  'loc': 'Solan-Vieille survey, non-zero-sum section; 1703.04026, introduction.',
  'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4653174/',
  'why': 'This is the general equilibrium-existence problem for undiscounted dynamic games.',
  'st': 'Two-player finite games and several absorbing-game classes are known. 2512.04306 treats a restricted positive '
        'recursive absorbing class; it is not a theorem for arbitrary finite multiplayer games.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate F24), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T440',
  'd': 'TREE',
  't': "The rate of Muller's ratchet",
  's': 'In the Haigh diffusion formulation used in arXiv:2606.15842, X_k is the frequency with k deleterious '
       'mutations, mutation rate lambda>0 and additive selection alpha>0. Its drift is '
       '[alpha(mean(X)-k)X_k+lambda(X_{k-1}-X_k)]dt, and its Wright-Fisher covariance is nu^{-1}(X_k delta_{kl}-X_k '
       'X_l)dt. Start from the mutation-selection Poisson profile with mean lambda/alpha and let '
       'tau_nu=inf{t:X_0(t)=0}. Determine sharp asymptotics of E tau_nu as nu tends to infinity with alpha,lambda '
       'fixed, including the exponential rate and leading prefactor.',
  'c': 'This is the specified diffusion first-click problem. It does not silently identify that time with the '
       'long-time clicking rate of every finite-population genetic model.',
  'src': 'A small noise approximation for Muller’s Ratchet (arXiv:2606.15842); Fluctuations of fitness distributions '
         'and the rate of Muller’s ratchet (arXiv:1206.6782).',
  'loc': '2606.15842, model definition and fixed-parameter small-noise approximation.',
  'url': 'https://arxiv.org/abs/2606.15842',
  'why': 'It would turn an important population-genetic timescale into a quantitative theorem.',
  'st': '2606.15842 gives fixed-time approximations of mean mutation count and the least-loaded class up to order '
        'nu^{-2}; these are not sharp rare-click first-passage asymptotics. Diffusion and population limits must not '
        'be interchanged without justification.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate F36), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T441',
  'x': "DUPLICATE of T088, 14 Nov 2026: the same problem (the exponent of the shortest open crossing of an n by n box in critical site percolation on the triangular lattice), stated from the Damron-Hanson-Sosoe papers instead of Schramm's ICM 2006 list. The open question is kept under T088.",
  'd': 'PERC',
  't': 'The chemical distance exponent of critical planar percolation',
  's': 'For critical Bernoulli site percolation on the triangular lattice, let L_n be the length of the shortest open '
       'left-to-right crossing of an n by n box, conditioned on an open crossing existing. Prove that E[L_n | '
       'crossing]=n^{s+o(1)} for a deterministic exponent s and determine s.',
  'c': '',
  'src': 'Damron-Hanson-Sosoe, On the chemical distance in critical percolation (arXiv:1506.03461) and Strict '
         'inequality for the chemical distance exponent (arXiv:1708.03643).',
  'loc': '1506.03461 and 1708.03643, introductions and main comparisons with lowest crossings.',
  'url': 'https://arxiv.org/abs/1708.03643',
  'why': 'It measures the intrinsic geometry of a critical cluster, beyond conformal arm exponents.',
  'st': 'There are nontrivial lower bounds and strict improvements over the lowest crossing, whose exponent is 7/4. '
        'These comparisons neither prove existence nor identify the shortest-crossing exponent.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate F44), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T442',
  'd': 'RW',
  't': 'The spectral radius of simple random walk on surface groups',
  's': 'Determine the exact spectral radius of simple random walk on the Cayley graph of <a,b,c,d | [a,b][c,d]=1> for '
       'the symmetric generating set {a,a^{-1},b,b^{-1},c,c^{-1},d,d^{-1}}: each of the eight generators is chosen '
       'with probability 1/8. Equivalently, determine rho=lim_{n to infinity} P_e(X_{2n}=e)^{1/(2n)}.',
  'c': 'The generating set and probability normalization are essential; values for other walks are different.',
  'src': 'Gouezel, A numerical lower bound for the spectral radius of random walks on surface groups '
         '(arXiv:1310.4265).',
  'loc': '1310.4265, introduction and standard genus-two generating set.',
  'url': 'https://arxiv.org/abs/1310.4265',
  'why': 'It is a concrete return-probability constant for the simplest closed hyperbolic surface group.',
  'st': 'Rigorous numerical lower and upper bounds are available; computing arbitrarily accurate bounds does not '
        'supply the unknown exact value for this generating set.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate G01), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T443',
  'd': 'RW',
  't': 'Sampling satisfying assignments of bounded-degree k-CNF formulas',
  's': 'For Boolean k-CNF formulas whose clauses have k distinct variables and whose variables each occur in at most '
       'Delta clauses, determine the largest asymptotic Delta=Delta(k) for which every satisfiable instance has a '
       'randomized sampler within total-variation epsilon of its uniform satisfying-assignment law in time polynomial '
       'in formula size and 1/epsilon. Can one reach Delta=2^{k/2-o(k)}?',
  'c': 'The inherited 2026 algorithm comparison was not searched again; the integrator should replace rough exponents '
       'with the latest precise theorem before publishing.',
  'src': 'Bounded-occurrence SAT sampling; Guo-Jerrum-Liu, Uniform Sampling through the Lovasz Local Lemma '
         '(arXiv:1611.01647), and the hardness/algorithm references discussed there.',
  'loc': '1611.01647, introduction and Section 7.1 on k-CNF formulas.',
  'url': 'https://arxiv.org/abs/1611.01647',
  'why': 'It asks where constructive local-lemma methods can sample rather than merely find solutions.',
  'st': 'Inherited OPEN from the 10 Nov verification. The prior note reports a gap between samplers and hardness near '
        'the 2^{k/2} scale. 1611.01647 is an algorithm paper, not itself a Bezakova hardness theorem; the earlier '
        'shorthand attribution is corrected.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate G02), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T444',
  'd': 'RG',
  't': 'Detecting latent geometry in sparse random geometric graphs (Bubeck-Ding-Eldan-Racz)',
  's': 'Fix c>1. Draw n independent uniform points on S^{d-1} and join i,j when their inner product exceeds the '
       'threshold giving edge probability c/n. Is the total-variation distance between this geometric graph law and '
       'G(n,c/n) asymptotically zero whenever d/(log n)^3 tends to infinity? Together with detection below this scale, '
       'this would locate the sparse geometry-testing threshold up to constants.',
  'c': 'The statement asks for statistical indistinguishability, not merely failure of a particular spectral '
       'algorithm.',
  'src': 'Liu-Mohanty-Schramm-Yang, Testing thresholds for high-dimensional sparse random geometric graphs '
         '(arXiv:2111.11316).',
  'loc': '2111.11316, introduction and detection/indistinguishability dimension bounds.',
  'url': 'https://arxiv.org/abs/2111.11316',
  'why': 'This identifies when latent geometry is statistically visible in a graph with constant average degree.',
  'st': 'The cited testing paper leaves a polylogarithmic gap. 2507.06556 identifies a global spectral limit in some '
        'sparse high-dimensional regimes; equality of empirical spectral distributions is weaker than '
        'indistinguishability in total variation.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate G03), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T445',
  'd': 'GEOM',
  't': 'The constants in the higher-dimensional Ulam problem',
  's': 'For each fixed d>=3, let L_n be the largest coordinatewise increasing chain among n independent uniform points '
       'in [0,1]^d. Determine c_d=lim_{n to infinity} n^{-1/d} L_n, which exists almost surely. In particular, '
       'identify c_3 exactly.',
  'c': 'The original paper metadata and author-hosted abstract were opened, but its AMS PDF returned 403. The '
       'mathematical statement was checked against the full Calder-Esedoglu-Hero paper. The separate '
       'fluctuation-exponent question is omitted.',
  'src': 'Bollobas-Winkler, The longest chain among random points in Euclidean space, Proc. Amer. Math. Soc. 103 '
         '(1988), 347-353; Calder-Esedoglu-Hero, arXiv:1302.5828.',
  'loc': '1302.5828, introduction/background on the Bollobas-Winkler constants; original paper DOI '
         '10.1090/S0002-9939-1988-0943043-6.',
  'url': 'https://arxiv.org/abs/1302.5828',
  'why': 'It is the basic geometric constant in high-dimensional longest-chain and nondominated-sorting limits.',
  'st': 'The source recalls existence of c_d, monotone convergence c_d to e, and that only c_1=1 and c_2=2 are known '
        'explicitly. The additional API query finds continuum-limit rates and numerical schemes, not exact '
        'higher-dimensional constants.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate G06), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T446',
  'd': 'GF',
  't': 'Global well-posedness of the dynamical sine-Gordon model in the full subcritical regime',
  's': 'On the two-dimensional torus, the dynamical sine-Gordon model du = (1/2)Δu dt + c sin(βu) dt + dW, with W '
       'space-time white noise, is renormalised and solved locally for every β^2 < 8π (Hairer-Shen; '
       'Chandra-Hairer-Shen). Prove that the renormalised solutions exist for all time for every β^2 < 8π and that the '
       'sine-Gordon measure is invariant under the flow. Global existence is known for β^2 < 6π.',
  'c': '',
  'src': 'M. Hairer and H. Shen, The dynamical sine-Gordon model, Comm. Math. Phys. 341 (2016), arXiv:1409.5724; A. '
         'Chandra, M. Hairer and H. Shen, The dynamical sine-Gordon model in the full subcritical regime, '
         'arXiv:1808.02594; B. Bringmann and S. Cao, Global well-posedness of the dynamical sine-Gordon model up to '
         '6π, arXiv:2410.15493',
  'loc': 'Bringmann-Cao 2410.15493, introduction: global well-posedness for β^2 < 6π, the range from 6π to 8π left '
         'open.',
  'url': 'https://arxiv.org/abs/2410.15493',
  'why': 'The sine-Gordon model is the standard test case for regularity structures beyond the first thresholds; '
         'global solutions up to 8π would close the gap between the local and the global theory.',
  'st': 'Open for 6π ≤ β^2 < 8π. arXiv search on 12 Nov 2026 finds no global result past 6π after Bringmann-Cao; '
        'arXiv:2602.14996 concerns the hyperbolic sinh-Gordon model, a different equation.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate D30), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T447',
  'd': 'NNA',
  't': 'Minimum width for universal approximation in the uniform norm',
  's': 'For positive integers d_x,d_y, let w_min(d_x,d_y) be the least hidden-layer width w such that affine-output '
       'ReLU networks with biases, arbitrary finite depth and every hidden layer of width at most w are dense in '
       'C([0,1]^{d_x},R^{d_y}) in the uniform norm. Determine w_min for all pairs d_x,d_y.',
  'c': 'The domain is the full cube; arbitrary compact subsets can have different topology. Leaky-ReLU and L^p results '
       'are not substituted for uniform ReLU approximation.',
  'src': 'Park-Yun-Lee-Shin, Minimum Width for Universal Approximation (arXiv:2006.08859); Kim-Min-Park, Minimum width '
         'for universal approximation using ReLU networks on compact domain (arXiv:2309.10402).',
  'loc': '2006.08859, uniform versus L^p approximation; 2309.10402, compact-domain uniform lower bounds.',
  'url': 'https://arxiv.org/abs/2309.10402',
  'why': 'It identifies the exact bottleneck dimension for continuous neural approximation.',
  'st': 'Exact L^p widths do not settle uniform approximation. 2309.10402 proves a uniform lower bound d_y+1 in the '
        'range d_x<d_y<=2d_x and explicitly distinguishes compact-domain L^p results from whole-space results. No '
        'general uniform-width formula is supplied.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate H31), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md). Replaces T255.'},
 {'id': 'T448',
  'd': 'NNA',
  't': 'An explicit unconditional lower bound for bounded-depth log-precision transformers',
  's': 'Establish an unconditional superpolynomial width lower bound for computing Boolean Formula Value with a fixed '
       'number of transformer layers and O(log n)-bit precision: the input encodes an n-token Boolean formula and its '
       'variable assignment, and the output is its truth value. Use constant-depth polynomial-size feedforward blocks '
       'and a uniformly constructible family with polynomially many heads; prove that no polynomial width suffices for '
       'this explicit NC^1-complete task.',
  'c': 'This target is proposed here, not quoted as a conjecture of Merrill-Sabharwal. It is close to major '
       'circuit-complexity barriers; allowing arbitrary feedforward computation would change the model.',
  'src': 'Concrete lower-bound target motivated by Merrill-Sabharwal, The Parallelism Tradeoff: Limitations of '
         'Log-Precision Transformers (arXiv:2207.00729).',
  'loc': '2207.00729, log-precision constant-depth threshold-circuit simulation.',
  'url': 'https://arxiv.org/abs/2207.00729',
  'why': 'It asks for a genuinely explicit lower bound in a standard finite-precision architecture.',
  'st': 'Merrill-Sabharwal give a threshold-circuit upper bound and conditional limitations. One-layer, '
        'restricted-attention or different-precision lower bounds do not prove this assertion for arbitrary fixed '
        'depth and polynomial width.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate H35), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md). Replaces T314. This formulation is '
       'ours, built from the cited work; it is not a conjecture stated by those authors.'},
 {'id': 'T449',
  'd': 'NNA',
  't': 'Computation in superposition',
  's': 'In the parameter-driven computation model of Adler-Shavit, fix feature sparsity two, constant output error '
       'below 1/4 and constant bits per network parameter. For M Boolean input features, consider the worst ordered '
       'collection of M distinct pairwise AND outputs, with both input and output represented in superposition and '
       'with all encoding/decoding description charged as prescribed in the model. Determine the sharp neuron '
       'complexity N(M): close the gap between the lower order sqrt(M log M) and constructive upper order sqrt(M) log '
       'M.',
  'c': 'Input feature count, output operation count, sparsity, error and precision are all fixed explicitly; the '
       'original wording conflated these quantities.',
  'src': 'Adler-Shavit, On the Complexity of Neural Computation in Superposition (arXiv:2409.15318); Mathematical '
         'Models of Computation in Superposition (arXiv:2408.05451).',
  'loc': '2409.15318, Sections 2.1/2.2, upper constructions and parameter-description lower bounds.',
  'url': 'https://arxiv.org/abs/2409.15318',
  'why': 'It makes the capacity question quantitative while retaining the information model that supports its lower '
         'bound.',
  'st': '2409.15318 gives the stated description-length and neuron bounds in its fixed-bit model. The gap is '
        'logarithmic; arbitrary real precision or free function-dependent encodings would invalidate a neuron-only '
        'information bound.',
  'n': 'Added 12 Nov 2026 from the T400 replacement run (candidate H12), checked by the integrator '
       '(codex_local_1108/briefs/T400REP/AUDIT_claude-agent_2026_11_12.md). Replaces T363.'}]
