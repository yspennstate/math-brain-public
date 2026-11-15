# Round 5 vetting (an agent)

Round 5 runs on Mac mini 1 from 15 Nov 2026: 67 briefs, one per round-4 brief, each asked to recheck its round-4 result
and take the next named step; acc2, normal speed, made by `../make_r5.sh`. Each brief dir here holds the worker's
REPORT.md, PROOF.md, LOG.md and scripts; the raw codex.log stays on the Mac. Only briefs whose `run.exit` exists are
pulled, because a worker writes REPORT.md before it finishes.

How each report was read: the VERDICT line, the scope sentence under it, whether the report says the round-4 result it
builds on still holds, and every line that mentions a false statement, a counterexample or an error. A PROVED verdict
below is a lemma or special case unless the row says otherwise; no brief in this pull closes its top-200 row.

## First pull (15 Nov 2026, 08:05 mini time; 20 of 67 complete, all exit 0)

| brief | verdict as written by the worker |
|---|---|
| AV_T010 | PARTIAL parent-alternative cap reduced to branch transmission lower bound, with a mark-independent exp(O(L^2)) envelope |
| AV_T030 | PROVED the boundary reciprocal-inertia lemma from the earlier interior result, including radial limits, cutoff removal and boundary-kernel finiteness |
| AV_T032 | PARTIAL verified Lemma 7.2's exact conditional reference law from the displayed thermal slab density |
| AV_T050 | PROVED the comparison-network estimate for prescribed additional road anchors under the stated admissible-road and calibration hypotheses |
| AV_T054 | PROVED relative QUE for prescribed k-sets when k/[L^2(M+log N)] tends to infinity, under all-eigenvector delocalization and label symmetry |
| AV_T083 | PROVED the smooth-row estimate under its stated Bessel hypotheses with catalog loss 140(log_2(2d))^(3/2) |
| AV_T095 | PARTIAL deterministic chunk-to-disjoint-witness reduction checked under the stated corner, scale and endpoint inputs |
| AV_T132 | PARTIAL deterministic interior localization of actual sewing-path approximants |
| AV_T136 | PROVED scalar source-moment expansions E8-E9 under explicit regularity hypotheses, including the earlier-split factor and formal size cancellation |
| AV_T137 | PARTIAL lower-bound centering, truncation and finite-depth selection reduction checked; bounded-model comparison remains unaudited |
| AV_T176 | PARTIAL dyadic Lean model and eight-block completion checked at source level |
| AV_T304 | PROVED one-factor R improvement in Lemma 6.2's harmonic and angle error bounds, conditional on the stated spatial and probability-circuit inputs |
| T049 | PARTIAL a stronger local connectivity bound from enlarged square regions |
| T050 | PARTIAL an explicit simultaneous-envelope theorem for fixed road windows |
| T053 | PROVED stationary collision Palm law, finite positive collision intensity, and reciprocal-rate mean flight time at fixed density |
| T056 | PARTIAL proof audit of expanding asymptotically free finite models (Proposition models:sequence of the OpenAI preprint "A group without fixed price", 5 Oct 2026) |
| T058 | PARTIAL maximum disjoint independent-set packings inherit the Gaussian count fluctuations below phase 2/3 |
| T060 | PARTIAL a competing ground state's norm distance survives removal of every finite interval, conditional on the published local gap inequality |
| T063 | PROVED finite binary-bridge swap invariance and conditional fair cluster signs for inhomogeneous weights c_v >= 1 |
| T064 | PROVED explicit determinant-weighted saddle law and exact residual-field level comparison |

Reading notes. Nine PROVED (AV_T030, AV_T050, AV_T054, AV_T083, AV_T136, AV_T304, T053, T063, T064) and eleven PARTIAL; AV_T304
is conditional on its stated inputs. Every report that states it says the round-4 result was re-derived or its script
rerun and holds. The lines that mention failure mark limits, not errors: AV_T054 a block-Walsh example at k = L^2, T060
an example showing that round 3's density condition does not give the stronger inference the worker tried, T058 the
conflict bound above phase 2/3 (the report says this does not make the packing approximation false there), T050 a
remark that its estimate is not a counterexample to the canonical gauges. T060 rests on Tasaki, arXiv:2610.34330v2,
Theorem 2.1, whose finite numerical inputs the worker did not verify; T056 audits an intermediate proposition of an
outside preprint, not its main theorem. No report says an earlier result of ours or a published source is wrong.

## Second pull (15 Nov 2026, 08:56 mini time; 48 of 67 complete, these 28 new, all exit 0)

| brief | verdict as written by the worker |
|---|---|
| T068 | PROVED online clique barrier with polynomially many final deletion disagreements |
| T071 | PARTIAL sharp propagation bound for the terminal-weighted family moment |
| T073 | PARTIAL improved high-noise uniqueness using exactly three disagreements |
| T075 | PARTIAL arbitrarily long small-cap prefixes at singular parameters in (1/2,1); T075 remains open |
| T076 | PARTIAL sharp two-logarithm bound for noncommuting quadratic errors and a bounded-variation criterion |
| T078 | PROVED sparse injection energy bound on the full cubic lattice, with sharp displacement power and sparsity threshold |
| T080 | PARTIAL robust triangular interfaces evade the earlier underoccupation detector |
| T081 | PARTIAL uniform surface-pressure estimate verified for the safe-state restricted ensembles |
| T087 | PARTIAL scale-dependent rectangular crossing criterion for subpolynomial component counts |
| T089 | PARTIAL GOE target remainder below 10^-6 at order 10 instead of 58 |
| T090 | PROVED first relative correction to the Gaussian second-moment weak-coupling asymptotic |
| T092 | PROVED a quantitative weighted residue-transport bound with explicit coefficient discrepancy |
| T097 | PARTIAL the cube-capacity coefficient with a bounded error, cap(B_R) = kappa R + O(1), and a strict improvement of the previous trial constant |
| T098 | PARTIAL volume-uniform simultaneous first rotation for truncated good cells in diluted Ising chains |
| T101 | PARTIAL exact probability of vertex-simple periodic orbits with at most twelve mirrors |
| T102 | COMPUTED circuit mismatch costs in 120 finite conditioned triangular-percolation configurations |
| T105 | PROVED an improved almost-everywhere flat-torus gap limsup bound exceeding 2.008 |
| T116 | PARTIAL audit of the common-reference testing step in the reported outside resolution |
| T122 | PROVED finite-cascade kernel invariance, giving the regular hierarchical upper bound |
| T127 | PARTIAL retrieved and audited the formal model of the claimed outside solution |
| T133 | PROVED positive curvature on every open candidate arc at Delta = 1/sqrt(2), for all weight ratios |
| T160 | PARTIAL uniform BK localization estimate for the finite-box exterior response on Z^3 |
| T179 | PROVED nonanticipating H-valued linear-growth drift extension, conditional on the prior drift-free input |
| T185 | PARTIAL positive Harris recurrence for the two-link unit-file example under every weighted alpha-fair policy |
| T200 | PARTIAL radial exit estimates and xi_3(1,1) <= 1 - 2/(627 log 3) < 0.9971 |
| T221 | PARTIAL exact stationary extrema for the fair-AND collision table, with an explicit missing compatibility constraint |
| T222 | PARTIAL a boundary-exclusion theorem and upper bound for the first Hoeffding projection |
| T224 | PARTIAL loss-decay-only polynomial weak rates for one-dimensional output feature spans |

Reading notes. Eight PROVED (T068, T078, T090, T092, T105, T122, T133, T179), one COMPUTED (T102), nineteen PARTIAL. T179
is conditional on the round-3 drift-free input. T133 is an exact integer certificate about the candidate curvature formulas;
the worker says it does not prove T133 or identify a liquid region. Every folder holds LOG.md and PROOF.md, so no report
stands without its work. Each report that says so states the round-4 result was re-derived or its script rerun and holds
(T221: the completion lemma, information inequality and AND cap survived rederivation and the 515 earlier cost entries
match). The lines that mention failure mark limits, not errors: T101 two extrapolations from the earlier corner counts
(the twelve-corner term does not vanish at p = 1, the weight-three factor does not survive the full sum), T185 the naive
bound Q <= m with new local arrivals, T071 a uniform propagation factor (the separated-leader example saturates it), T098 a
resonant three-site example showing the bad-site quadratic term cannot be dropped, T080 a proposed implication about
orientations, T224 the earlier logarithmic bound on one example (the new theorem gives O(m^(-1/5)) there). T116 and T127
audit outside work (T116 the OpenAI preprint of 24 Sep 2026 on deletion channels; T127 a formal model pinned to a commit);
neither is our result. No report says an earlier result of ours or a published source is wrong. Numbers checked by hand:
T200's bound, 1 - 2/(627 ln 3) = 0.99710, is below 0.9971 as stated.

## Third pull (15 Nov 2026, 09:45 mini time; 67 of 67 complete, these 19 new, all exit 0)

| brief | verdict as written by the worker |
|---|---|
| T225 | PARTIAL exact initial nonlinear residual motion and a quantitative positivity window for the sine teacher |
| T226 | PARTIAL almost-sure strictly subcritical endpoints in the larger zero-target rectangle |
| T227 | PARTIAL a logarithmic-time escape lemma for unbiased independent middle-layer signs; convergence and eta_max remain open |
| T245 | PARTIAL first-order learning-rate correction to the endpoint flow and full NTK in the structured deep-linear model |
| T247 | PARTIAL unnormalized joint-limit empirical isometry for orthogonal tanh networks with small Gaussian biases at simultaneous forward/backward critical initialization |
| T248 | PROVED TW1 with deterministic finite-size centering for the projected spherical kernel with arbitrary quadratic Hermite coefficient |
| T264 | PROVED Infinite high-order risk moments at every fixed sample size for homogeneous minimum-norm ReLU interpolation on the sphere |
| T265 | PARTIAL no finite margin-stationary representation of the earlier Gaussian conical scores, almost surely; GD benign overfitting remains unresolved |
| T267 | PARTIAL proved the centered quadratic training-Gram approximation and the ReLU training-kernel reduction with its radial spike retained |
| T284 | PARTIAL the general amplification loss has optimal order sqrt(n log n) |
| T286 | PROVED likelihood-weighted cubic integration by parts for uniformly positive finite-output channels |
| T305 | PARTIAL finite-step energy bounds for compact coupled perturbations outside dimension-independent Frobenius regularity |
| T324 | PARTIAL stopped concentration for independently noisy groups and preservation of the deterministic merging prefactor in probability |
| T325 | PROVED almost-sure global population-gradient-flow convergence at every finite depth for scalar attention with both key/query factors trained and all other blocks fixed |
| T347 | PROVED a positive iid exclusion cap for local minima around a specified stored pattern at every positive load |
| T423 | PARTIAL uniform small-mass local-time and occupation bounds |
| T427 | PROVED the quantitative equal-mass square/torus semidiscrete-to-smoothing reduction by an independent Jacobian argument |
| T428 | PARTIAL Uniform time-resolved Brownian signed pair limit for N-dependent profiles with unchanged critical tuning |
| T430 | PARTIAL order-1/N conditional full-state transient product-mixture bound |

Reading notes. Six PROVED (T248, T264, T286, T325, T347, T427; T427 is a reduction step), thirteen
PARTIAL. Every report states that the round-4 result was re-derived or its script rerun and holds (T225: the earlier shear
obstruction is correct; T284: conditional on its published concentration input). The lines that mention failure mark
limits, not errors: T225 a counterexample whose tail sign does not match the full flow, T226 an exact example showing the
algebraic exception is needed, T227 a blanket deterministic escape statement (false; the result is in probability), T265
the unqualified exclusion at zero center (false by an exact KKT example), T267 dropping the radial correction (leaves an
operator error 1/(4 pi gamma)), T325 convergence from every initialization (false; the theorem is almost sure), T423 an
unjustified passage from almost-sure extinction. Process failures (a macOS RLIMIT_DATA refusal in T427, a refused nice in
T264, a too-coarse step in T324's own recheck) were fixed before the final runs and change no result. T286 extends a
bound to equations (158)-(161) of Appendix B.6 of a paper by Barbier, Camilli, Nguyen, Pastore and coauthors; T284 rests on
a published concentration result of Pittel whose full proof the worker could not open. No report says an earlier result of
ours or a published source is wrong. Numbers checked by hand: T347's cap, 1/88,202,000 = 1.13e-8, is above 1e-8 as stated.

Round 6 (one continuation brief per round-5 brief, 67, made by `../make_r6.sh` from clean prompt parts) started on Mac
mini 1 at 09:44 mini time, acc2, normal speed, at most six at a time.
