# Round 4 vetting (an agent)

Round 4 runs on Mac mini 1 from 15 Nov 04:14 mini time: 67 briefs (T-rows continued from round 3, plus AV_ briefs that
re-audit an earlier claim of ours), acc2, at most 8 workers, memory floor 30 pct, normal speed. Each brief dir here holds
the worker's REPORT.md, PROOF.md, LOG.md and scripts; the raw codex.log stays on the Mac.

How each report was read: the VERDICT line, the scope sentence under it (what exactly is proved, under which
hypotheses), whether the report says the round-3 result it builds on still holds, and every line that mentions a false
statement, a counterexample or an external error. A PROVED verdict below is a lemma or special case unless the row says
otherwise; no brief in this pull closes its top-200 row.

## First pull (15 Nov 04:5x mini time; 35 of 67 complete)

| brief | verdict as written by the worker |
|---|---|
| AV_T010 | PARTIAL signed start-of-pass adjustment is measurable under every complementary-pass hidden-root closure; T010 remains only partially claimed |
| AV_T030 | PROVED the epsilon-to-zero passage in prop:interior-reciprocal under the preprint's bounded-density and strict-contraction hypotheses, including the infinite diagonal |
| AV_T032 | PARTIAL verified the deterministic single-replacement collision estimate underlying the earlier conditional insertion argument |
| AV_T050 | PROVED the common incoming-road gauge estimate under the stated product-world and local-comparison hypotheses, with an explicit uniform error bound |
| AV_T054 | PROVED relative QUE on each prescribed deterministic vertex set of size k with k/(L^8 log N) tending to infinity, uniformly over all eigenvectors under complete delocalization and label symmetry |
| AV_T083 | PROVED the depth-varying catalog-row lemma under its stated support, refinement, catalog and Bessel hypotheses |
| AV_T095 | PARTIAL rare-fast crossing input checked from the fixed-Gamma uniform shape theorem |
| AV_T132 | PARTIAL maximizing-zoom endpoint moments survive uniformly over varying laws and fixed dyadic enlargements |
| AV_T136 | PROVED exponential augmentation for finite zero-field Gaussian SK hierarchies and their fixed-site weak limits, with the physical-path coefficient and stopped density-norm bound. |
| AV_T137 | PARTIAL Source-level semantic match checked for the diluted Lean theorem; full proof remains unaudited |
| AV_T176 | PARTIAL reciprocal-degree lemma and final Fourier/sign completion checked for dyadic Thorp mixing |
| AV_T304 | PROVED deterministic coefficient and scale bounds feeding the previously checked compiler recurrence |
| T049 | PARTIAL a stronger local connectivity bound from every seven-edge detour |
| T050 | PARTIAL proved and sharpened the finite-cell local-potential lemma in every dimension d >= 2 |
| T053 | PROVED invariance of the conditioned environment-and-velocity law at fixed density |
| T056 | PARTIAL proof audit of the Bernoulli-to-finite-model transfer inequality |
| T058 | PARTIAL proved a joint Gaussian limit for adjacent independent-set counts on fixed interior phase bands |
| T060 | PARTIAL exclusion of normal competing ground states, conditional on the published local gap inequality |
| T063 | PROVED free-energy minimality for simultaneous near-balanced torus limits with one or both fluxes fixed |
| T064 | PROVED sharper crossing-stability bound with saddle-only interior counts and optimal corner coefficient |
| T068 | PROVED online clique barrier with bounded final late admissions and arbitrary intermediate revisions |
| T071 | PARTIAL descendant-family criterion and a uniform short-window N-BBM bound |
| T073 | PARTIAL improved high-noise uniqueness by bounding the two-disagreement slack |
| T075 | PARTIAL improved the conditional prefix-concentration L^p criterion from theta<1/18 to theta<1/4; T075 remains open |
| T076 | PARTIAL quadratic drift bound without an extra logarithm under a commuting low-mode envelope |
| T078 | PROVED smaller boundary-coloring cost for finite transposition meshes |
| T080 | PARTIAL uniform exponential bounds for connected underoccupied regions |
| T081 | PARTIAL geometric hypotheses verified for conditional contour replacement on connected-complement domains |
| T087 | PARTIAL reverse exponent-existence transfer under crossing-count control in probability |
| T089 | PARTIAL GOE target remainder below 10^-6 at order 58 instead of 390 |
| T090 | PROVED asymptotic sharpness of the Gaussian second-moment renewal lower endpoint at weak coupling |
| T092 | PROVED a centered-block analytic transfer estimate with square-root loss at most 3 delta squared |
| T097 | PARTIAL a non-shell capacity bound and a larger relative crossover coefficient |
| T116 | PARTIAL rechecked the reported resolution and located its actual Lean verification entry point |
| T127 | PARTIAL retrieved the outside full-solution paper and checked that its statements match T127 |

Reading notes. Twelve AV_ briefs re-audited earlier claims of ours: six came back PROVED (AV_T030, AV_T050, AV_T054,
AV_T083, AV_T136, AV_T304) and six PARTIAL, where the worker checked the step it was given and named the next step still
unaudited (AV_T137 and T116 are Lean source-matching checks, not proof audits). The seven reports that mention a
counterexample use it to show a hypothesis cannot be dropped (AV_T054 singleton and adaptive sets, T050 dimension one,
T081 the connected-complement condition, T071 a linear term); none says an earlier result of ours is wrong and none
reports an error in a published source. Each T-row report that builds on round 3 states that the round-3 result holds
and was re-derived or rerun before the new step. T078 and T127 record outside solution claims (T078 the 24 Sep 2026
OpenAI claim, T127 a full-solution paper whose statements match the row); neither proof was audited here, so neither row
is retired on this pull.

## Second pull (15 Nov 05:5x mini time; 55 of 67 complete)

| brief | verdict as written by the worker |
|---|---|
| T098 | PARTIAL dimension-independent first rotation at good barriers in Bernoulli-diluted Ising chains |
| T101 | PARTIAL exact probability of vertex-simple periodic orbits with at most ten mirrors |
| T102 | PARTIAL sharp bounds for matching boundary currents on nested circuits |
| T105 | PROVED adjacent-interval incompatibility of the scalar extremizer and a positive separation G >= G* + 1/1944 in the strengthened moment relaxation |
| T122 | PARTIAL specialized the regular invariant-kernel variational principle and proved an explicit temperature error; hierarchical equality remains open |
| T133 | PROVED positive midpoint curvature and a local convex-side collar for the disordered candidate curve when gamma <= u < pi-gamma |
| T160 | PARTIAL exact finite-box ratio criterion for cylinder convergence on Z³ |
| T179 | PROVED measurable linear-growth drift extension for unbounded diffusion and arbitrary L2 initial states, conditional on the prior drift-free input |
| T185 | PARTIAL uniform negative sampled drift near the through-workload axis |
| T200 | PARTIAL optimal deterministic time weights and xi_3(1,1) < 0.9981 |
| T221 | PARTIAL a collision-table refinement of the finite-model defect bound, with a sharp cap for the three-input AND encoder |
| T222 | PARTIAL a strict geometric improvement of the earlier interaction-energy bound |
| T224 | PARTIAL improved curvature-dependent uniform weak rates by concentration on iid trajectories |
| T225 | PARTIAL prediction-relevant exponentially small symmetry-restricted proximal gaps arbitrarily near Gaussian initialization |
| T226 | PARTIAL almost-sure parameter convergence in the larger zero-target spectral rectangle |
| T227 | PARTIAL a high-probability catapult interval with independent mixed signs in the dense middle layer; eta_max remains open |
| T245 | PARTIAL finite-dimensional global gradient-flow closure and exact discrete-GD balance defect for the structured deep-linear model |
| T247 | PARTIAL unnormalized joint-limit empirical isometry for vanishing-variance backward-critical orthogonal tanh networks |
| T248 | PROVED TW1 with deterministic finite-size centering for spherical inputs and a strictly subcritical quadratic Hermite component |
| T264 | PROVED Uniform open-set three-point risk coefficient 2/d and divergent random-triple risk moments of orders at least (d-1)/2. |

Reading notes. Five PROVED (T105, T133, T179, T248, T264), fifteen PARTIAL; T179's result is conditional on the round-3
drift-free uniqueness input, as its scope sentence says. Every report that builds on round 3 says the round-3 result was
re-derived or rerun and holds. The counterexamples again mark limits, not errors: T226 an exact one-step landing that
blocks an endpoint conclusion (probability zero under the stated law), T227 the column condition in the entrance lemma,
T264 the fixed-delta restriction, and T225 shows round 3's polynomial frozen-gap bound does not extend uniformly to a
small KL neighbourhood of the Gaussian start, which bounds how far that result reaches without contradicting it. No
report says an earlier result of ours or a published source is wrong.

## Third pull (12 briefs, 15 Nov 2026)

| id | verdict and result |
|---|---|
| T265 | PARTIAL exact path norm over all bias-free ReLU representations of the target |
| T267 | PARTIAL all-time test-risk reduction for wide uncentered ReLU random features |
| T284 | PARTIAL inverse-polynomial success amplifies at O(sqrt(n log n)) vertex loss, using the concentration tool of Etesami-Mahloujifar-Mahmoody (arXiv:1907.05401); no novelty is claimed for that tool |
| T286 | PROVED quantitative cubic Gaussian replacement for the cavity replicas |
| T305 | PARTIAL nonquadratic block entropy bounds for HMC |
| T324 | PARTIAL deterministic concentration and merging asymptotics for two groups in circle attention |
| T325 | PROVED global population gradient-flow convergence at every finite depth L for untied scalar attention step sizes, the learned steps being the reciprocals of the roots of an explicit residual polynomial |
| T347 | PROVED a strictly decreasing limiting shell profile does not exclude strict local minima for correlated binary Hopfield patterns (explicit construction, K = 2^q) |
| T423 | PARTIAL exact limit T delta_T -> 2 E L_infinity for the extinction-disagreement probability of the same-noise pair, improving round 3's liminf criterion |
| T427 | PROVED equal-mass flat-grid subdivision bound O(n^(-1/60) log(en)^(11/10)) at t = n^(-5/6), sharper than the O(n^(-1/120) log n) of Lemma 4.1 in Y. Xu, Random matching between distinct distributions in two dimensions |
| T428 | PARTIAL time-resolved Brownian signed pair-renewal limit, locally uniform in positive time in operator norm, with the round-3 critical tuning unchanged |
| T430 | PARTIAL quantitative full-state finite-time product-mixture bound for power-of-d tagged paths that keeps the random initial empirical measure; replaces a false arrival-rate monotonicity step with a uniform routing estimate |

Reading notes. Four PROVED (T286, T325, T347, T427), eight PARTIAL. Every report says its round-3 result was re-derived
and holds. T430 replaces an arrival-rate monotonicity step of the earlier reports, which its report calls false, with a
uniform routing estimate; the reading did not check how much of the earlier argument that restores. T347's construction and T427's comparison with Xu's
lemma are the two results most worth an outside check before any write-up. Round 4 is complete: 67 of 67 briefs ran.
