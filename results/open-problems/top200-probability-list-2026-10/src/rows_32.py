# Replacement rows from the T400 second replacement run (T400REP2), integrated 12 Nov 2026 by
# an agent: 13 probability rows and 2 deep-learning rows, filling both lists to 200.
ROWS = [{'id': 'T450',
  'd': 'SM',
  't': 'The essential-singularity scale of the slow-bond TASEP',
  's': 'In exponential directed last-passage percolation on the nonnegative square lattice, use independent rate-one '
       'exponential weights off the diagonal and rate-(1-epsilon) exponentials on the diagonal. Write '
       'Xi(epsilon)=lim_{n to infinity} n^{-1} E[T((0,0),(n,n))]-4. Prove or refute the predicted '
       'essential-singularity order Xi(epsilon)=exp(-Theta(1/epsilon)) as epsilon decreases to zero.',
  'c': 'The prediction means two exponential bounds with positive constant coefficients in 1/epsilon, not an already '
       'known exact constant.',
  'src': 'Sarkar, Sly and Zhang, Infinite order phase transition in the slow bond TASEP, arXiv:2109.04563, describing '
         "Lebowitz's prediction.",
  'loc': 'Introduction, p. 2, definition of Xi, Theorem 1 and paragraph immediately following it.',
  'url': 'https://arxiv.org/abs/2109.04563',
  'why': 'It asks how a single microscopic defect changes a macroscopic current.',
  'st': 'Xi(epsilon)>0 is known for every positive epsilon. 2109.04563 proves Xi(epsilon)=O(epsilon^C) for every fixed '
        'C and explicitly says establishing or refuting the exp(-c/epsilon) scale needs new ideas. 1704.07799 '
        'describes the stationary density profile but not this quantitative scale.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate D40), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T451',
  'd': 'BM',
  't': 'Markov uniqueness for the Phi^4_3 gradient Dirichlet form',
  's': 'Let mu be the finite-volume renormalized Phi^4_3 Gibbs measure on the three-dimensional torus in Zhu-Zhu. On '
       'smooth bounded cylinder functions put E_0(F,G)=(1/2) integral <DF,DG>_{L^2(T^3)} dmu. Is the closure of E_0 '
       'the only quasi-regular Dirichlet form on L^2(mu) whose restriction to this cylinder algebra is E_0? In '
       'particular, does it coincide with the Dirichlet form of the dynamical Phi^4_3 process?',
  'c': 'Conservativity of an already constructed process is not the missing assertion. No formal integration-by-parts '
       'drift is assumed to be an L^2(mu) cylinder generator.',
  'src': 'Rongchan Zhu and Xiangchan Zhu, Dirichlet form associated with the Phi^4_3 model, arXiv:1703.09987.',
  'loc': 'Theorems 1.1-1.3 and the discussion immediately after Theorem 1.3, pp. 4-5.',
  'url': 'https://arxiv.org/abs/1703.09987',
  'why': 'It would identify the analytic and SPDE constructions of the same equilibrium dynamics.',
  'st': '1703.09987 constructs the process form, identifies its cylinder restriction and obtains a closable gradient '
        'form. It explicitly leaves equality of the resulting closed forms and the associated uniqueness question '
        'unresolved. 1511.08030 proves restricted uniqueness in dimension two, not dimension three.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate F48), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T452',
  'd': 'RMT',
  't': 'The distribution of the permanent of a random sign matrix',
  's': 'Let M_n have independent entries taking +1 and -1 with equal probability. Determine whether there are '
       'deterministic centerings a_n and positive scales b_n for which (log|per M_n|-a_n)/b_n converges in '
       'distribution to a nondegenerate law, and, if so, identify that law. Interpret the variable conditionally on '
       'per M_n not being zero, whose probability tends to one.',
  'c': 'The entries are centered signs, not nonnegative Bernoulli(1/2) variables. A normal limit is a question, not an '
       "asserted conjectural answer. The logarithmic normalization is the chosen precise refinement of Vu's "
       "distribution question; it is not quoted as Vu's proposed law.",
  'src': 'Van Vu, question (2), Problems Section, Oberwolfach Report 1/2014, Combinatorics; Tao-Vu 0804.2362 and '
         '2608.26707 supply partial results.',
  'loc': 'Oberwolfach Report 1/2014, Combinatorics, Problems Section, Van Vu question (2), printed p. 84; 0804.2362, '
         'Theorem 1.1.',
  'url': 'https://arxiv.org/abs/0804.2362',
  'why': 'The permanent is the basic random-matrix statistic without determinant cancellation identities.',
  'st': 'Tao-Vu establish the leading n log n scale. 2608.26707 strengthens the lower bound to the sqrt(n!) exp(-Cn) '
        'scale for sign permanents; it does not give a fluctuation law. 1112.0752 proves a log-determinant CLT, which '
        'does not transfer to permanents.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate C52), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T453',
  'd': 'COMB',
  't': 'The binary Chvatal-Sankoff constant',
  's': 'Let X_1,X_2,... and Y_1,Y_2,... be independent iid fair binary sequences, and let L_n be the length of their '
       'longest common subsequence through time n. Determine the exact value of gamma_2=lim_{n to infinity} E[L_n]/n.',
  'c': 'T142 asks for variance growth. This asks for the mean limit constant; its appearance in T142 is background, '
       "not that row's target.",
  'src': 'Chvatal and Sankoff, Longest common subsequences of two random sequences, J. Appl. Probab. 12 (1975), '
         '306-315; Tiskin, The Chvatal-Sankoff problem, arXiv:2212.01582. Latest reported bound: Tomar, Certified '
         'upper bounds for the Chvatal-Sankoff constant, doi:10.5281/zenodo.23517988.',
  'loc': '2212.01582, Introduction, definition of gamma and table of bounds.',
  'url': 'https://arxiv.org/abs/2212.01582',
  'why': 'It is the basic limiting score in random sequence alignment.',
  'st': 'Rigorous bounds and improved lower-bound algorithms are available (2407.10925). 2212.01582v2 explicitly '
        'retracts incorrect earlier distributional claims while retaining a bound. No exact value is supplied by these '
        "results. Tomar's October 2026 author preprint (doi:10.5281/zenodo.23517988), Theorem 1.1, reports "
        'gamma_2<=0.821963. This is a bound, not an exact evaluation; the certificate and formal proof were not rerun '
        'here.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate K01), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T454',
  'd': 'GEOM',
  't': 'Critical allocation tails in the stable marriage of Poisson and Lebesgue',
  's': 'For a unit-intensity Poisson process in R^2, give every center appetite one and take its almost surely unique '
       'stable allocation of Lebesgue measure. Let X be the distance from the origin to its assigned center. Find a '
       'quantitative upper bound tending to zero for P(X>r) as r tends to infinity; more sharply, determine its tail '
       'order.',
  'c': 'This is allocation of continuum volume to centers, not pair matching between two Poisson point processes.',
  'src': 'Hoffman, Holroyd and Peres, Tail Bounds for the Stable Marriage of Poisson and Lebesgue, arXiv:math/0507324.',
  'loc': 'Open Problems (i), p. 29, critical behavior in dimensions two and higher.',
  'url': 'https://arxiv.org/abs/math/0507324',
  'why': 'It measures transport distances at a balanced spatial allocation transition.',
  'st': 'The paper proves a critical power-law upper bound in dimension one and exponential estimates away from '
        'criticality. Its explicit question asks for any quantitative upper bound in dimension two and higher; the '
        'successful current searches found no resolution of that planar critical question.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate K02), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T455',
  'd': 'TREE',
  't': 'The maximum-agreement-subtree exponent for random cladograms',
  's': 'Let T_n and T_n_prime be independent uniformly chosen unrooted binary trees with leaves labelled 1,...,n. Let '
       'M_n be the largest cardinality of A subset {1,...,n} for which the induced trees on A, after suppressing '
       'degree-two vertices, are isomorphic by a label-preserving map. Prove existence and determine the exponent beta '
       'in E[M_n]=n^{beta+o(1)}.',
  'c': '',
  'src': 'Aldous, Largest common substructures in probabilistic combinatorics, 2003 problem collection; Budzinski and '
         'Senizergues, Maximum Agreement Subtrees and Holder homeomorphisms between Brownian trees, arXiv:2304.00905.',
  'loc': '2304.00905, Introduction, Theorem 1 and discussion of the unknown optimal exponent; Aldous problem page.',
  'url': 'https://arxiv.org/abs/2304.00905',
  'why': 'It quantifies how much independently sampled evolutionary trees can agree by chance.',
  'st': 'Lower bounds have improved beyond the original recursive construction (2208.05148). 2304.00905 proves a '
        'polynomial improvement over the exponent-1/2 upper bound. 2601.00119 treats common unlabelled graph subtrees, '
        'a different matching notion, and does not determine this label-preserving exponent.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate K03), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T456',
  'd': 'RW',
  't': 'The relaxation time of branch rotations on cladograms',
  's': "Use Aldous's rooted cladograms with n labelled leaves. At each discrete step choose a non-root edge uniformly, "
       'detach its entire descendant subtree and suppress the resulting degree-two vertex. Reattach the subtree to '
       'each of the at most four edges adjacent to the merged edge with probability 1/4 each, using the remaining '
       'probability for a self-loop. Prove that the relaxation time 1/(1-lambda_2) is O(n^{3/2}).',
  'c': 'T167 concerns polygon triangulations. This row uses the separate labelled-tree chain in the same source.',
  'src': 'Aldous, Mixing Times for the Branch-Rotation Chain on Cladograms (or the Triangulation Walk), 2003 problem '
         'description.',
  'loc': 'clad-mix.pdf, pp. 1-2, chain definition and displayed PROBLEM.',
  'url': 'https://www.stat.berkeley.edu/~aldous/Research/OP/clad-mix.pdf',
  'why': 'It is a basic local sampler for phylogenetic trees.',
  'st': 'Aldous gives the matching order-n^{3/2} lower bound. 2609.16955 solves an order-n^2 mixing conjecture for a '
        'different chain: remove one leaf and reinsert it on any edge. 1809.05092 concerns flips on quadrangulations. '
        'Neither theorem is the stated branch-rotation bound.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate K05), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T457',
  'd': 'GF',
  't': 'The nodal-domain density of the random plane wave',
  's': 'Let F be the centered stationary Gaussian field on R^2 with covariance E[F(x)F(y)]=J_0(|x-y|). Let N(R) count '
       'its nodal domains contained in the disk B(0,R). Determine the exact Nazarov-Sodin density c_RPW=lim_{R to '
       'infinity} E[N(R)]/(pi R^2).',
  'c': 'The normalization is per Euclidean area for covariance J_0. T064 asks for a percolation scaling limit and '
       'explicitly excludes identifying its heuristic density with the true constant.',
  'src': 'Nazarov and Sodin, On the Number of Nodal Domains of Random Spherical Harmonics, arXiv:0706.2409; Ingremeau '
         'and Rivera, A lower bound for the Bogomolny-Schmit constant for random monochromatic plane waves, '
         'arXiv:1803.02228.',
  'loc': '1803.02228, Introduction and Theorem 1.1; normalization of the monochromatic field.',
  'url': 'https://arxiv.org/abs/1803.02228',
  'why': 'It is a canonical quantitative invariant of a Gaussian nodal set.',
  'st': 'Existence and positivity are known, and 1803.02228 supplies an explicit positive lower bound. 1707.00766 '
        'studies dependence on spectral measure and 2208.04208 universality of the constant. These do not evaluate the '
        'plane-wave constant.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate K07), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T458',
  'd': 'BM',
  't': 'The exact Pickands constant at alpha=1/2',
  's': 'Let B_{1/4} be standard fractional Brownian motion, with variance E[B_{1/4}(t)^2]=t^{1/2}. Determine the exact '
       'value H_{1/2}=lim_{T to infinity} T^{-1} E[exp(sup_{0<=t<=T}(sqrt(2) B_{1/4}(t)-t^{1/2}))].',
  'c': '',
  'src': "Pickands' Gaussian extreme-value constant; Harper, Pickands' constant H_alpha does not equal "
         '1/Gamma(1/alpha), for small alpha, arXiv:1404.5505; Bisewski and Jasnovidov, arXiv:2108.00756.',
  'loc': '1404.5505, Introduction, defining limit and known exact cases; 2108.00756, Theorems 2.1-2.3 on '
         'discretization.',
  'url': 'https://arxiv.org/abs/1404.5505',
  'why': 'The constant controls leading extreme-event probabilities for rough stationary Gaussian processes.',
  'st': 'Exact values are known at alpha=1 and 2. 1404.5505 refutes a once-proposed general gamma-function formula. '
        '2108.00756 gives convergence rates for discrete approximations, and 1609.07909 a perturbative expansion near '
        'Brownian motion, not the value at alpha=1/2.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate K08), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T459',
  'd': 'SM',
  't': 'The square-lattice self-avoiding-walk connective constant',
  's': 'Let c_n be the number of nearest-neighbor n-step self-avoiding walks on Z^2 starting at the origin. Determine '
       'exactly mu_square=lim_{n to infinity} c_n^{1/n}.',
  'c': 'Existing self-avoiding-walk rows ask for scaling limits, exponents or diffusive lower bounds, rather than this '
       'nonuniversal constant.',
  'src': 'Bauerschmidt, Duminil-Copin, Goodman and Slade, Lectures on Self-Avoiding Walks, arXiv:1206.2092; Couronne, '
         'New upper bound for the connective constant for square-lattice self-avoiding walks, arXiv:2211.16146.',
  'loc': '1206.2092, Section 1.4, connective constant; 2211.16146, main bound.',
  'url': 'https://arxiv.org/abs/1206.2092',
  'why': 'It is the basic entropy per step of the simplest lattice polymer.',
  'st': 'Submultiplicativity gives existence. The honeycomb value is known exactly, while the square-lattice value has '
        'only bounds and numerical estimates; 2211.16146 improves an upper bound without evaluating it.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate K13), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T460',
  'd': 'SM',
  't': 'The dimer entropy of the cubic lattice',
  's': 'Let M_n be the number of perfect matchings of the nearest-neighbor graph on {1,...,2n}^3. Determine the exact '
       'dimer entropy lambda_3=lim_{n to infinity}(2n)^{-3} log M_n.',
  'c': 'T131 concerns the Coulomb phase and correlations; entropy evaluation is a separate target.',
  'src': "Hammersley's monomer-dimer entropy problem; Friedland-Peled, Theory of computation of multidimensional "
         'entropy with an application to the monomer-dimer problem, arXiv:math/0402009; Qidong He, A new upper bound '
         'on the dimer constant of Z^3, arXiv:2607.28810.',
  'loc': '2607.28810, Introduction, definition of lambda_3 and Theorem 1.1; 0708.1641, entropy/permanent bounds.',
  'url': 'https://arxiv.org/abs/2607.28810',
  'why': 'It is the entropy of a uniform three-dimensional perfect-matching ensemble.',
  'st': 'The planar dimer constant has an exact solution. 2607.28810v2 explicitly states that the cubic constant has '
        'no exact expression and proves lambda_3<=0.452130, improving the previous 0.457547 upper bound.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate K16), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T461',
  'd': 'SM',
  't': 'Divergence of the high-dimensional self-avoiding-walk expansion',
  's': 'Write the all-orders asymptotic expansion mu(d)~sum_{j=-1}^{infinity} a_j(2d)^{-j} for the nearest-neighbor '
       'self-avoiding-walk connective constant of Z^d, with a_{-1}=1. Prove or refute that the power-series tail '
       'sum_{j>=0} a_j z^j has radius of convergence zero, equivalently limsup_{j to infinity}|a_j|^{1/j}=infinity.',
  'c': 'The recall card gave Section 1.5; the source body places this in Section 1.4, immediately before 1.5.',
  'src': 'Bauerschmidt, Duminil-Copin, Goodman and Slade, Lectures on Self-Avoiding Walks, arXiv:1206.2092; Graham, '
         'Borel type bounds for the self-avoiding walk connective constant, arXiv:0911.5163.',
  'loc': '1206.2092, Section 1.4, equation (1.19) and the paragraph crossing pp. 4-5; equation (1.20).',
  'url': 'https://arxiv.org/abs/1206.2092',
  'why': 'It tests whether a major high-dimensional expansion is only asymptotic or genuinely convergent.',
  'st': 'The all-orders asymptotic expansion and Borel-type remainder bounds are known. The lecture notes explicitly '
        'say zero radius is expected but unproved. Bounds of factorial type from above do not prove divergence.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate K21), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T462',
  'd': 'GF',
  't': 'The Brownian-map limit of uniform labelled planar graphs',
  's': 'Let G_n be uniform among connected simple planar graphs with vertex set {1,...,n}, with graph distance d_n and '
       'uniform probability measure mu_n on vertices; no planar embedding is chosen or weighted. Is there a constant '
       'c>0 such that (V(G_n),c n^{-1/4} d_n,mu_n) converges in distribution in the Gromov-Hausdorff-Prokhorov '
       'topology to the unit-area Brownian map?',
  'c': 'T023 concerns conformal embeddings of maps, and T132 FK-weighted embedded maps. Uniform labelled graphs give '
       'different weights to the underlying combinatorial objects.',
  'src': 'Chapuy, Fusy, Gimenez and Noy, On the diameter of random planar graphs, arXiv:1203.3079; Stufler, The '
         'scaling limit of random cubic planar graphs, arXiv:2203.07306.',
  'loc': '1203.3079, Introduction and main diameter theorem; 2203.07306, Introduction, discussion of critical graph '
         'classes before Theorem 1.1. The statement is the unrestricted graph extension, not the proved cubic theorem.',
  'url': 'https://arxiv.org/abs/2203.07306',
  'why': 'It asks whether the universal random-surface limit survives forgetting the embedding and sampling graphs '
         'uniformly.',
  'st': '1203.3079 proves the unrestricted diameter exponent 1/4 up to n^{o(1)} factors. 2203.07306 and 2203.17245 '
        'prove Brownian-map convergence for cubic planar graphs, not all connected planar graphs. 2608.21063 treats '
        'non-separable planar maps, whose sampling law differs from uniform labelled graphs. No unrestricted graph '
        'limit theorem was located.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate K23), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T463',
  'd': 'NNA',
  't': 'The optimal chain-of-thought length for binary multiplication',
  's': 'In the unique-hard-attention transformer model and CoT expressibility definition of Amiri et al. (Definition '
       '2.2), take two N-bit integers X,Y and let M_N be the Nth bit of XY in Definition 4.4. What is the optimal '
       'worst-case length of a scratchpad ending in M_N? In particular, can a family with uniformly bounded numbers of '
       'layers and heads compute this single bit using O(N) generated tokens?',
  'c': 'Width and positional encodings may depend on length as in Definition 2.2. No assertion of SGD learnability is '
       'added; the target is a single bit, so the lower bound is not merely the cost of printing the product.',
  'src': 'Amiri, Huang, Rofin and Hahn, Lower Bounds for Chain-of-Thought Reasoning in Hard-Attention Transformers, '
         'arXiv:2502.02393.',
  'loc': 'Definition 2.2; Section 4.2, Definition 4.4 and Theorems 4.5-4.6; Appendix C.2.3.',
  'url': 'https://arxiv.org/abs/2502.02393',
  'why': 'It turns inference-time reasoning cost into a concrete sharp complexity question.',
  'st': '2502.02393 proves an Omega(N) lower bound for the middle bit and constructs O(N log N) scratchpads for the '
        'full product. 2605.18079 studies low-precision softmax transformers and 2610.17283 a different '
        'autoregressive-neuron model; these are not a matching upper bound in UHAT.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate H40), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'},
 {'id': 'T464',
  'd': 'NNP',
  't': 'The sharp dimension for linearly accessible superposed features',
  's': 'Fix epsilon=1/4. Let d(m,k) be the smallest d for which real matrices A,B in R^{d by m} satisfy ||B^T A '
       'z-z||_infinity<epsilon for every k-sparse z in [-1,1]^m. Determine its sharp asymptotic order as k tends to '
       'infinity, uniformly for m>=k^3. In particular, close the logarithmic gap between the known upper and lower '
       'bounds.',
  'c': 'This is the quantitative gap in a specific formalization of the linear representation hypothesis, not a claim '
       'that every learned semantic concept is linear. T449 concerns pairwise-AND computation with bounded-bit '
       'parameters, a different task and model.',
  'src': 'Garg, Kleinberg and Peng, How Many Features Can a Language Model Store Under the Linear Representation '
         'Hypothesis?, arXiv:2602.11246.',
  'loc': 'Section 1.2, equation (12), Theorems 2-3; Section 5, extensions to feature classifiers.',
  'url': 'https://arxiv.org/abs/2602.11246',
  'why': 'It asks how much superposition a layer can support while individual features remain accessible to a linear '
         'next layer.',
  'st': 'The source proves d=O(k^2 log m) and d=Omega((k^2/log k) log(m/k)) at fixed error in this regime. Nonlinear '
        'compressed-sensing decoders have a different dimension requirement; the displayed linear-decoding bounds '
        'leave a factor of order log k.',
  'n': 'Added 12 Nov 2026 from the T400 second replacement run (candidate H47), checked by the integrator '
       '(codex_local_1108/briefs/T400REP2/AUDIT_claude-agent_2026_11_12.md).'}]
