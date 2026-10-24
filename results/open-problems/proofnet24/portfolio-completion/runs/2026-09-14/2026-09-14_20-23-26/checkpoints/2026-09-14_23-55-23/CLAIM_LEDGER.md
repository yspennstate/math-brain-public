# Consolidated mathematical claims and limits

This ledger distinguishes the scope of a mathematical argument from its historical novelty, external acceptance, and formal verification. It is a cumulative review index; immutable numbered reports preserve earlier formulations and subsequent corrections. The [actual execution index](AGENT_INDEX.md) and [coordinator synthesis](agents/011.md) record the broader run.

**The full Lyons determinantal entropy-concavity conjecture remains unresolved in this run.** The two tree constructions disprove precisely the unrestricted fluctuation clauses stated below. The four-type uniqueness theorem completes the exact question left open in the project's QSO manuscript. None is presented as a cleared worldwide first.

## Principal completed proofs

| Statement | Exact scope | Proof and review |
|---|---|---|
| Four-type fixed-point uniqueness | Every symmetric quadratic stochastic operator with four types whose offspring can equal neither parent; allowed coefficients may be zero. Exactly one simplex fixed point, including possible boundary points. | [Main proof](FOUR_TYPE_UNIQUENESS.md);006, full independent007, constructive008, integrated031. |
| Certified convergent algorithm | Averaging weight2/5 enters the coordinate cap2/5 in three steps and then contracts by23/25. A rational residual gives a rigorous distance bound. | Main proof;008,013, corrected [solver and independent verifier](SOLVER_USAGE.md);026 adversarial audit and root regression. |
| Global averaging through0.51 | Every fixed positive weight at most51/100 converges from every simplex point. For weights from1/2 through51/100 the uniform factor is2499/2500 after three steps. | [Larger-range proof](QSO_GLOBAL_051.md), [below-half proof](QSO_AVERAGING_RANGE.md); full independent046. |
| Stronger half-step rate | At weight1/2, factor7967/8192 after three steps. The earlier0.502 perturbation method remains a valid separate estimate. | [Half-step proof](QSO_HALF_STEP_EXPLICIT.md);024 and046. |
| Quantitative coefficient dependence | Full-row-l1 Lipschitz constant2sqrt(5)-1; uniform analytic extension across the coefficient boundary; exact derivatives and quadratic remainder bounds. | Main note;013; [044](agents/044.md), independently read and checked by the parent. Sharper constants in later reports must retain their own proof obligations. |
| Attainable fixed-point geometry | Exact singleton and pair inequalities characterize attainable fixed points in every dimension at least three. In four types, an exact pair-product minimum improves the coefficient bound to(204+95sqrt(5))/121. | [Geometry proof](QSO_FIXED_POINT_GEOMETRY.md); full parent review of049. The global coefficient constant is not claimed sharp. |
| Tangent spectral bounds | Every tangent eigenvalue of the raw four-type Jacobian has modulus strictly belowsqrt(2); det(I-J) is greater than4/3. A larger sufficient averaging range is local stability only. | [Spectral proof](QSO_SPECTRAL_BOUNDS.md);029 and parent independent review. |
| Small parental leakage | Four-type uniqueness and global averaged convergence when total probability of reproducing a parent is below1-sqrt(3)/2. | Main note, Theorem6; coordinator011 and independent014. |
| Subcritical tree counterexample | One fixed aperiodic offspring law with mean below1 and finite third moment, no exponential moment, and a non-Gaussian two-normal degree-one count limit along a deterministic size subsequence. | [Complete proof](SUBCRITICAL_COUNTEREXAMPLE.md);015, full independent034, parent review. |
| Critical tree counterexample | One fixed computable aperiodic critical offspring law, with every moment above1 infinite, and a non-Gaussian mixture limit for centered degree-one counts on a size subsequence. | [Complete proof](CRITICAL_COUNTEREXAMPLE.md);028, full independent033 and its terminating selector, parent review, and full integration audit062. The evaluator is now fixed explicitly. No stage integer was numerically constructed. |
| Two-site determinantal entropy | Full complex Hermitian two-site concavity, including the closed contraction boundary. | [Entropy note](LYONS_PARTIAL_RESULTS.md);016 and independent018. |
| Coordinate restrictions in any dimension | Concavity with only a two-coordinate principal block varying; or with the principal block complementary to one coordinate fixed while its incident row and column vary. | Entropy note;010,016,017,018. |
| Scaled cross-matrix entropy | A two-coordinate block varies freely while the entire cross matrix is one fixed complex matrix times one complex scalar. Strict mutual-information chord gap if the scalar changes and the cross matrix is nonzero. | Entropy note, Section6;036, coordinator011, full independent045, parent review. |
| Indefinite rank-two entropy directions | At most one positive and at most one negative direction eigenvalue, through five sites, in arbitrary orientation. | Entropy note, Section4;019. The dimension-six compressed rank-two projection case remains open; independent068 is assigned. |
| Local lines through diagonal kernels | Every fixed nonzero Hermitian line through an interior diagonal kernel is strictly concave on some interval. For zero-diagonal directions the leading loss is an explicit positive quartic form. | Entropy note, Section5;023 and parent independent review. This is not full concavity on an entire neighborhood. |

## Other completed deductions and their boundaries

The numbered reports contain the full arguments. An individual worker's `PROVED` label is not a substitute for the displayed proof, nor for a separately listed audit.

| Report | Result | Boundary of the claim |
|---|---|---|
| [012](agents/012.md) | Global four-type continuous-flow convergence, exact rate and cap-entry estimates. | Finite entry into the limiting cap itself is false in general. |
| [025](agents/025.md) | Fractional fixed-generation moment bounds under matching local probability estimates and a doubling-scale condition. | Does not settle unrestricted Janson Problem20.1. |
| [037](agents/037.md) | Fixed-law P12 three-tier small-ball theorem with corrected recursion and eventual exponential failure bound. | Independent[054](agents/054.md) passes, supplying a complete rectangular-net replacement for a dimensional ambiguity in a cited source proof. The triangular-array extension is not included. |
| [038](agents/038.md) | Arbitrarily switched averaged QSO tracking, convergence criteria, finite-variation equivalences, and periodic response. | Common forcing is required when comparing two trajectories; slowly varying coefficients alone need not give a constant state limit. |
| [041](agents/041.md) | Explicit higher-dimensional contraction neighborhoods around the equiprobable tensor and sharp thresholds for the specified contraction guarantees. | The general tensor contraction theorem and equiprobable convergence have prior literature; stronger uniqueness thresholds are not claimed. |
| [042](agents/042.md) | Complete zero-curvature classification and strict chords between distinct rank-one projection kernels, with the exceptional quartic coefficient. | Restricted endpoint class; no unrestricted entropy conclusion. |
| [043](agents/043.md) | Dimension-dependent bounds for nonlinear bounded lifts and exact optimal linear selection constants. | The distinction between a nonlinear choice of a preimage and one linear right inverse is essential. |
| [044](agents/044.md) | Uniform analytic extension, derivative formulas, and exact first-order activation of a missing QSO type. | The invariant-face dichotomy is for feasible affine rays; curved paths can activate at higher order. |
| [047](agents/047.md) | Sharper averaged leave-one-out gate from leave-two-out covariance cancellation. | An empirical-width substitute has an exact failure-probability counterexample; independent087 audit is assigned. |
| [048](agents/048.md) | Exact centered-inverse L-ensemble Hessian and a semidefinite rank-r Fisher bound controlled by atom-probability oscillation. | All semidefinite directions are not settled; the bound can lose force for rare atoms. |
| [050](agents/050.md) | Interior star-direction equality classification, quartic loss in flat directions, and strict star-slice chords. | Point-coordinate graph components matter; the broader entropy conjecture remains open. |
| [051](agents/051.md) | Gaussian realized-risk lower quantiles and failure of convergence to zero from conditional-mean lower bounds; exact effective-rank criterion for relative concentration. | A fixed positive threshold with probability tending to1 is a different conclusion from relative concentration. |
| [052](agents/052.md) | The archived five-type example mixed with the equiprobable tensor has exactly one interior fixed point for every positive mixing weight. | Full exact audit passes; this one path does not classify all strictly positive five-type operators. |
| [053](agents/053.md) | Strict three-site entropy curvature in every nonzero gauge-commutator direction, including affine-feasible boundary directions. | The sufficient higher-dimensional cone is restricted; arbitrary directions remain unresolved. |
| [055](agents/055.md) | Exact complete-bipartite product-demand flow and cut formulas, with sharp limiting gaps in the specified families. | This extends the archived reduction counterexample and does not settle the original Aldous–Fill diameter conjecture. |
| [056](agents/056.md) | Modular-oscillation and correlation-determinant improvements of the semidefinite Fisher bound; exact resolvent representation and a noncommuting strict chord. | Full independent066 audit is in progress. The pointwise sign of the resolvent integrand can change. |
| [057](agents/057.md) | Sharp rational four-type fixed-point field degree8, sharp boundary degree4, generic incidence degree, and dense rational fixed-point specializations. | Universal bounds and exact examples are fully displayed; independent symbolic reconstruction is assigned to098. No radical-solvability claim. |
| [058](agents/058.md) | Positive finite Rényi-order two-site concavity holds exactly at Shannon order1; exact order2 chord failure and sharp fixed-reference chi-square contraction. | Other Rényi orders are counterexamples to the altered functional, not to Lyons's Shannon conjecture. |
| [059](agents/059.md) | Exact anisotropic chronological contact-time transforms and a rigorous nonexponential example. | Fresh chronological interchange only; cyclic reuse is excluded. |
| [060](agents/060.md) | Uniform four-type uniqueness through parental leakage7/50; boundary-specific uniqueness through1/2 and an exact family disproving that guarantee above1/2. | Parent read the full proof; independent078 audit remains assigned. The larger uniqueness interval is not a convergence theorem. |
| [064](agents/064.md) | August2026 primary Matrix Spencer text states the unrestricted square result; realification and bounded-aspect reductions are proved. | The full analytical small-ball core has not been independently verified here; optimal unbounded-aspect dependence is not established by the inspected theorem. |

## Prior results and formal-proof provenance

| Topic | What this run establishes | Attribution or remaining gate |
|---|---|---|
| Lyons scalar-ray entropy | [039](agents/039.md) gives a complete quantitative scalar-ray derivation and equality condition. | Gu's thinning-relative-entropy theorem is prior work; scalar-ray concavity is not claimed as a new solution. |
| Erdős548 / Erdős–Sós | [040](agents/040.md) audits the elementary rooted-word proof, external statement-comparison logs, archive compatibility differences, and prepares a pinned replay directory. | A public proof and external Lean/NanoDa acceptance already existed at the pinned public commit. The local replay and new wrapper were not compiled; no Lean executable was available. |
| Matrix Spencer / matrix Komlós | [005](agents/005.md) distinguishes prior claims, dimension obstructions, and exact finite checks. | An existing published or public proof is not a new result of this session. |
| QSO literature | [009](agents/009.md), [035](agents/035.md), and041 record primary-source findings. | The full hypotheses of the closest Jamilov2016 four-type paper were not retrieved. Priority remains unverified. |

## Corrections and failed stronger statements

| Statement or route | Finding | What it does not disprove |
|---|---|---|
| Archived Aldous–Fill flow-cut reduction | [001](agents/001.md) gives an exact K2,3 counterexample, ratio39/35. | The original Aldous–Fill conjecture. |
| Strengthened condensation conclusions | [002](agents/002.md) refutes the archived gap-necessity and universal one-box claims. | The original broader open-ended Janson questions. |
| Chronological versus cyclic interchange | [004](agents/004.md) separates fresh chronological paths from cyclic reuse and its finite-cycle trapping atom. | A correctly conditioned or differently formulated limit theorem. |
| Original public solver accepted floats | [026](agents/026.md) found a false-zero certificate. The canonical API now requires exact rational inputs; exact regression and an independent verifier pass. | The mathematical residual theorem. The historical flawed implementation is retained. |
| One-point Fisher projection dominates entropy curvature | [048](agents/048.md) gives an exact noncommuting rank-two counterexample and an unbounded-ratio family. | Entropy concavity: the full Fisher term is strongly sufficient at the witness. |
| Endpoint-only Fisher optimization | [022](agents/022.md) gives a precise obstruction and the remaining quartic comparison. | The full Lyons conjecture. |
| Sectorwise beam-splitter entropy increase | [027](agents/027.md) gives an exact four-site counterexample. | The stronger global beam-splitter inequality or Lyons's conjecture. |
| Full exterior-square positivity | [030](agents/030.md) gives a strict interior counterexample on a nondecomposable bivector. | Positivity on decomposable directions used in019. |
| Polished Lyons formula transcription | A missing plus sign between the two expectations in equation(10) was corrected. The original019 proof had the correct sum. | The underlying mixed-derivative argument. |
| Literal least passing power is automatically computable | [033](agents/033.md) identifies the strict-comparison issue and supplies a terminating certificate enumeration. The polished critical construction adopts that selector. | Existence of the original mathematical least-power sequence; the two definitions need not choose the same law. |

## Original tree conjectures and excluded hypotheses

The source claims are the unrestricted subcritical/no-exponential-moment and critical/infinite-variance fluctuation clauses in Thévenin's closing conjecture, read alongside Janson's Problem20.2. The constructed subsequence limits are mixtures of two distinct normal laws, so they are not Gaussian. The counterexamples do not claim a complete classification of conditioned-tree degree counts. The critical construction is explicitly outside the finite-index stable-domain hypotheses of the established limit theorems. A separate source-status audit is assigned to067, moved forward from089.

Primary sources: [Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*](https://arxiv.org/abs/1112.0510); [Thévenin, *Vertices with fixed outdegrees in large Galton–Watson trees*](https://arxiv.org/abs/1812.07365); [Lyons, *Determinantal Probability: Basic Properties and Conjectures*](https://arxiv.org/abs/1406.2707); [Ganikhodzhaev–Rozikov, *Quadratic Stochastic Operators: Results and Open Problems*](https://arxiv.org/abs/0902.4207).

No new universal theorem in this run is claimed to have been formally verified, externally refereed, or cleared for historical priority. Exact arithmetic verifies the specific identities and certificates recorded in each script; finite numerical nonfailure does not establish a universal theorem.
