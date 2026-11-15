# Round 3 vetting (an agent, 14 Nov 2026, after the first eight finished)

Round 3 re-ran every round 1-2 problem that ended PARTIAL, asking the worker to re-check the earlier result first and then
extend it. The three PROVED verdicts in the first pull are all on "AV" briefs, which ask whether a row was settled by the
OpenAI math release. None of them is a new solution of a list problem; each proves one step inside a check.

| Row | Verdict | What it is | Standing |
|---|---|---|---|
| T054 | PROVED | For each fixed bounded vertex test, delocalization of all eigenvectors (sup norm <= L/sqrt N) plus invariance of the random regular graph law under relabelling gives diagonal QUE in probability, error L^4 sqrt(32(D+2) log N / N), uniform over each eigenspace. Combined with He-Huang-Wang's bulk delocalization it covers T054 under that precise reading of QUE. | Elementary, as the worker says; the argument (condition on the unlabelled graph, the labelling is a uniform permutation, concentrate a permutation statistic) is the standard one and reads correctly. Row status: covered for fixed deterministic tests; open for graph-dependent tests or stronger observables. Not a paper. |
| T030 | PROVED | The finite resolvent lemma of the preprint under check, by Schur complements, with a quadrature limit. | A step of someone else's proof; the epsilon-to-zero passage is still unchecked. Row stays PARTIAL-CLAIMED. |
| T050 | PROVED | The finite-cell local-potential lemma of the OpenAI strict-convexity paper, with an explicit constant. | Verifies an upstream construction only. Row stays PARTIAL-CLAIMED (the release claims strict convexity for iid exponential weights, not the full row). |

Five PARTIAL (T010, T032, T083, T095, T132): each re-check found the earlier work holds; none changes a row's status.

## Second pull (15 Nov, 21 of 70 finished)

| Row | Verdict | What it is | Standing |
|---|---|---|---|
| T063 | PROVED | For a=b=1, every c>0: every local subsequential limit of the near-balanced cylinder states (n_L/L -> 1/2) minimises specific free energy among translation-invariant allowed arrow laws. Two weight-preserving surgeries (reflected rectangles give a balanced torus; inserted straight rows embed it in the near-balanced sector) give p_L(n) >= (H/L) p_c - 3 log 2 / L, then block-entropy subadditivity. Exact-arithmetic check_surgery.py passes. | The argument is the standard pressure-to-entropy passage and reads correctly. It supplies hypothesis O2 of Pei's November preprint (hexagon:2611.00291v1), whose uniqueness Corollary 1.3 (1<c<=2) is unaudited. Not GFF convergence; the T063 row stays open. A lemma, not a paper; novelty not claimed. |
| T068 | PROVED | The Gamarnik-Kizildag-Warnke online clique barrier (arXiv:2504.11450, Thm 2.2) survives up to floor(min(eps^2,1) log2 n / 128) deletions of accepted vertices, each vertex admissible only at its own inspection round; cost sum_{j<=r} C(n,j) from guessing the deleted set. Exhaustive check on all graphs up to 5 vertices. | A union-bound reduction to the published theorem; correct as stated, and its restriction (no later admission) is essential, as the worker notes. Mild extension, not a paper. |
| AV_T136, AV_T304 | PROVED | Steps inside the checks against the OpenAI release (SK exponential augmentation lemma; noisy-center error recurrence). | Verify upstream constructions only; rows unchanged. |
| AV_T137 | PARTIAL | Confirms the earlier full-row claim; explicit Viana-Bray normalisation bound. | Row stays as before. |
| AV_T176, T049, T050, T053, T056, T058, T060, T075 | PARTIAL | Each re-check found the earlier work holds; each adds a bounded piece (T049 stronger connectivity bound from five-edge detours; T050 all positive Gamma laws; T053 fixed-density flight bounds; T058 joint second moments on interior phase bands; T060 uniform-density restriction, conditional on a published uniqueness theorem; T075 finite-prefix concentration criterion). | No row changes status. |

No EARLIER RESULT WRONG verdict so far.

## Third pull (15 Nov, 26 of 70 finished)

| Row | Verdict | What it is | Standing |
|---|---|---|---|
| T064 | PROVED | Random plane wave (covariance J_0): for a rectangle of area A and perimeter P and level delta <= 1, the left-right crossing probability of {f >= delta} differs from the level-0 one by at most delta/sqrt(2 pi) [A/(4 pi) + P/(2 pi)(1 + delta^2/3) + 4]. A Kac-Rice count of interior, edge and corner critical values in [0, delta]; levels o(R^-2) leave fixed-aspect crossings unchanged, so squares give 1/2. The interior density 0.091888 = 1/(2 sqrt 3 pi) matches Beliaev-Cammarota-Wigman Prop 1.1. | The step "the crossing changes only if a critical value lies between the levels" is the standard one and the bound reads correctly. Removes only o(R^-2) sprinkling; no RSW for non-squares, no Cardy limit. A lemma, not a paper; row stays open. |
| T078 | PROVED | Scalar field selection: if M lies in [-V/2, V/2] and P(M >= V/4) >= L, the tilted mean is at least V/8 exactly under the two stated conditions in z = bV/8; the sufficient form bV >= 8 log(1/L) sharpens the OpenAI Heisenberg manuscript's bV >= 16 log(11/L). Two-point extremisers. | Elementary and correct. The row's real input, the uniform low-temperature magnetisation tail (mesh_matrix_surface in the Lean source), is not checked. The row stays PARTIAL-CLAIMED. |
| T071, T073, T076 | PARTIAL | T071 an exact four-lineage criterion; T073 a strictly better high-noise uniqueness criterion for the fair-tie process on Z^2; T076 an exact return-kernel asymptotic for the 2D block profile. | No row changes status. |

Still no EARLIER RESULT WRONG verdict.

## Fourth pull (15 Nov 02:0x mini1 time, 44 of 70 complete)

The Codex account on mini1 hit its usage limit at 01:44 (mini1 clock, reset 03:26). The pool stopped starting briefs on its own.
Six briefs were cut mid-session and have no REPORT.md (T160, T179, T185, T200, T221, T222); 20 never started. Both groups
rerun after the reset, if mini1 has at least 25 pct memory free (it had 18 pct at 02:03).

| Row | Verdict | What it is | Standing |
|---|---|---|---|
| T092 | PROVED | U unitary, g with an orthonormal bilateral orbit, A = norm of h, P a finite orbit combination within eps < A of h: the support of P has at least (A^2 - eps^2)/(A norm(Uh - h)) points; for a map delta-close to a twist this is at least 3/(8 sqrt2 pi delta). | The invariant case (Uh = h, no approximation at all) re-derived here by averaging U^m P over m; the bound reads correctly. A constraint on the claimed finite construction, not a refutation; the construction's Lean dependency closure is unchecked. Lemma. |
| T105 | PROVED | The Aistleitner-Blomer-Radziwill long-gap constant 2.00636 is exactly optimal for the relaxation that uses only the first two Poisson factorial moments per interval, the mean spacing and the pair-correlation Lipschitz bound; an extremal non-exponential gap law attains it. | A limitation result: that route cannot improve the constant. Correct as an exact moment problem. Lemma; row unchanged. |
| T133 | PROVED | For the disordered Fredholm formulas in Bufetov's domain-wall six-vertex announcement (arXiv:2609.20576v1), norm of K_B is at most 1 - 2 gamma/pi < 1 for all -1 < Delta < 1, so the determinants stay positive on the announcement's omitted interval 1/2 < Delta < 1, and the critical equations continue analytically from B = 0. 19 numerical checks pass. | Shows one possible obstruction is absent; not a limit-shape proof. Lemma. |
| T084, T119, T142 | COMPUTED | T084 positive Rayleigh certificates for random-cluster measures on K_{5,5}; T119 an exact rational certificate of Harangi's four-atom cubic bound; T142 exact quadratic Walsh coefficients for fair binary LCS to n = 16. | Data, no row change. |
| T080, T081, T087, T089, T090, T097, T098, T101, T102, T116, T122, T127 | PARTIAL | Bounded extensions; T127 proves transience for Bernoulli(q) sleepers at q <= 419/1000 on the 3-ary tree and q <= 337/500 on the 4-ary tree. | No row changes status. |

Still no EARLIER RESULT WRONG verdict.

## Fifth pull (15 Nov 03:3x mini1 time, after the usage reset; 50 of 70 complete)

The pool was restarted at 03:29 mini1 time. The restart script stopped at once the first time: two finished briefs
(T133, T142) still carried the old usage-limit line in codex.log, and pool.sh reads every log. Those two logs were
set aside as codex.log.lim1 and the pool was started again. The six cut briefs reran first and all finished.

| Row | Verdict | What it is | Standing |
|---|---|---|---|
| T179 | PROVED | The bounded-start weak uniqueness in Han's arXiv:2611.07310v1 (Prop. 8.1, as the report cites it) extends to every deterministic L2 initial state: synchronous coupling of smooth approximations, solutions squeezed between those from min(v,w) and max(v,w), conserved expected mass of the gap, so an exact L1 contraction, then the L2 modulus with exponent 1/2. | The L1 step is the standard comparison argument for scalar SPDEs with a comparison principle and reads correctly. The row itself is settled by Han's paper (abstract: the full positive Hölder range), so T179 is retired as SOLVED (claimed, unrefereed). Our piece is an initial-data lemma; Han's proof is not audited. |
| T160 | PARTIAL | All subsequential limits under radius conditioning on the earlier degree-three tree are the mixtures of two explicit laws. | Example-level; no row change. |
| T185 | PARTIAL | No smooth homogeneous function of the workload is a Lyapunov function for the two-link network with loads (1/5, 1/2, 1/2). | An obstruction to one route; no row change. |
| T200 | PARTIAL | xi_3(1,1) <= 1 - 1/(495 log 3) < 0.99817 (earlier 0.99984). | A better bound; exact value open. |
| T221 | PARTIAL | A quantitative necessary condition on a hypothetical finite witness for RBS. | No row change. |
| T222 | PARTIAL | The Hoeffding energy constant for the planar TSP variance sharpened below 2/pi. | No row change. |

Still no EARLIER RESULT WRONG verdict.

## Sixth pull (15 Nov 04:0x mini1 time; all 70 briefs complete, pool idle)

Every report below rechecked the earlier result on its row first; all nineteen of ours hold.

| Brief | Verdict | What is new | Row consequence |
|---|---|---|---|
| T224 | PARTIAL | Curvature-dependent polynomial weak rate improved by an output cancellation. | None. |
| T225 | PARTIAL | Polynomial spectral gap for the sine proximal law on the symmetric sector; exact nonlinear symmetry reduction. | None. |
| T226 | PARTIAL | A convergent subcritical basin and an asymptotic edge-endpoint probability at initialisation variance of order 1/eta. | None. |
| T227 | PARTIAL | A probability-one catapult interval for a fully connected three-layer tanh network; eta_max open. | None. |
| T245 | PARTIAL | Closed depth-profile NTK dynamics for several training directions in the structured deep-linear model. | None. |
| T247 | PARTIAL | Exact dependent-gate trace identities; scalar-normalised empirical isometry for orthogonal tanh networks. | None. |
| T248 | PROVED (subclass) | TW1 with deterministic centring for spherical inputs and Lipschitz activations of Hermite rank >= 3, aspect ratio away from 1; uses Chen-Lyu arXiv:2610.41416 Cor. 1.4 as stated. | Subclass only; row stays open. |
| T264 | PROVED (one geometry) | Exact three-constraint minimum-norm ReLU interpolants, risk coefficient 2/d, for one third-point family. | Measure-zero family; row stays open. |
| T265 | PARTIAL | Explicit Bayes-consistent bias-free ReLU interpolation when n/d diverges; GD selection open. | None. |
| T267 | PARTIAL | All-time test-risk limit and one-minimum property for very wide sine random-feature networks. | None. |
| T284 | PARTIAL | Subpolynomial success amplifies to high probability with vanishing density loss. | None. |
| T286 | PROVED (one condition) | One deferred self-covariance condition of Barbier et al. arXiv:2510.24616 App. B.6, for phi = He_3. | Other assumptions remain; row stays open. |
| T305 | PARTIAL | Finite-step Gaussian remainder bounds and an unavoidable entropy drift. | None. |
| T324 | PARTIAL | Unequal-mass two-atom merging laws and a joint small-noise exponent. | None. |
| T325 | PROVED (d = 1) | Global convergence of population gradient flow for two untied scalar attention step sizes, other blocks fixed. | Special case; row stays open. |
| T347 | PARTIAL | Profile-well implication proved; the converse fails for explicit correlated binary Hopfield patterns. | None. |
| T423 | PARTIAL | Terminal extinction synchrony and a natural-scale disagreement criterion. | None. |
| T427 | PROVED (one constant) | h_Q of the square evaluated by an exponentially convergent positive series with a truncation bound; beta_sd and Xu's proof not checked. | None until beta_sd is evaluated. |
| T428 | PARTIAL | Brownian signed pair-renewal Laplace limit with unchanged critical tuning. | None. |
| T430 | PARTIAL, external error | Lemma 3.3 of Fittipaldi-Jonckheere-Lopez, arXiv:1809.05373 (v1, PDF dated 13 Nov 2021), is false as stated. | None; see below. |

T430, checked by an agent against the paper itself (PDF read 15 Nov 2026): the paper's own expansion (3.4) says
that when x(N+1) < k the red arrivals never reach server 1, so lambda_{N+1}(x,k) is the yellow term alone,
lambda(N+1-D) times the old routing weight over C(N,D), which is (N+1-D)/N times lambda_N(x,k). For a fixed infinite
configuration with infinitely many N at which x(N+1) < k = x(1) and lambda_N > 0 (the periodic 1,2,0 witness), the
sequence decreases infinitely often, so no N0 independent of x makes it non-decreasing. The lemma is used for the a.s.
convergence step after Lemma 3.3 (monotone and bounded); the convergence itself may still hold by another route (the
witness's rates converge). arXiv lists one version and Crossref shows no journal record under that title. No contact
with the authors has been made; that is the author's call.

Still no EARLIER RESULT WRONG verdict on our own work. Round 3 is complete: 70 of 70.
