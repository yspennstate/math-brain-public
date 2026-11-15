# FEIB30 results

Task: solve the Fourier Entropy-Influence conjecture, owner ask 9 Nov 2026 22:20; assigned thinning predictor referee and adversary.

Work started 10 Nov 2026 12:43 +04. Claims below will be marked PROVED, CHECKED NUMERICALLY, or HEURISTIC. Numerical results are recorded with their generating command and saved output.

The fleet rules restrict all writes to this folder and prohibit posting to the mesh. Consequently coordination, checklist, and memory writes outside this folder are omitted. Brain recall is read only with refresh disabled. No math store lookup was attempted, as directed by the brief.

## First numerical checks

CHECKED NUMERICALLY: `env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 10 python3 referee.py verify > verification.json` checked twelve random Boolean functions on eight variables at lambda 0.1, 0.25, 0.5. The maximum error in the posterior-mean identity and the predictor-gap/KL identity was 4.996003610813204e-16. A composed AND2-of-MAJ3 checked the displayed balanced composition law for every subset. Three independent direct truth-table transforms checked the tower recursion, including biased compositions; maximum metric error was 1.7763568394002505e-15 bits.

The shell already inherits nice 10 (`os.getpriority(os.PRIO_PROCESS,0)` printed 10). `nice -n 10` tried to increase this further and printed a sandbox warning but executed; subsequent runs inherit nice 10 directly. All numerical launches set the three thread variables to one. `uptime` at 12:46 +04 reported one-minute load 10.69.

CHECKED NUMERICALLY: exhaustive upward-closed size-eight subsets of the four-cube, quotiented by coordinate permutations, give four balanced monotone gate representatives: truth-set masks aaaa, e8e8, eaa8, eca8 (negative output on set bits). These include a dictator and MAJ3 with an unused input. The other two use all four inputs.

PROVED: the balanced composition law cannot be applied as written to biased gates. The needed correction uses Taylor coefficients of the outer multilinear polynomial at the inner mean; the implementation includes that correction. This is a scope condition, not a refutation of the displayed law.

## Search and larger families

CHECKED NUMERICALLY: `env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 adversary.py 160 > search_progress.jsonl` completed 525 runs, each with 160 proposed improving flips, on all n from eight through twelve. Starts were random, sparse, monotone DNF, positive weighted threshold, and quadratic bent type. At each lambda in {0.1,0.25,0.5}, separate objectives were each predictor's overhead and full bound, and the posterior-mean ratio. Total proposals: 84,000. Runtime in search_summary.json: 54.48968195915222 seconds. These are finite-budget local searches, not exhaustive Boolean-function optimization.

The best search-only overheads at lambda 0.1/0.25/0.5 were respectively 0.6538331610484089 / 0.8398184584801353 / 1.1976260894842388 bits. The best full bound was 1.742660791006726 bits per erased spectral element, and the largest posterior-mean ratio was 0.48580913462537895 deleted elements per unit influence. search_best.json identifies every objective's witness and its truth table. `python3 audit.py witnesses > witness_audit.json` independently recomputed all twenty-one saved witnesses through the original predictor.py; maximum metric difference was 8.881784197001252e-16.

CHECKED NUMERICALLY: `python3 structured.py verify > structured_verification.json` (with the same thread environment) compares thirty-nine closed-form evaluations against direct transforms. Maximum absolute error over entropy, influence, L, posterior mean ratio, logK and cost was 1.7763568394002505e-15. `python3 structured.py run > structured.jsonl` evaluates weighted thresholds through 256 variables, unequal tribes through 640 variables, quadratic-bent switches through 201 variables, and lexicographic functions through 256 variables. `python3 structured.py ands > threshold_ands.jsonl` adds 159 threshold-of-ANDs evaluations through 384 variables. Every family records all three predictors and all requested lambdas.

CHECKED NUMERICALLY: `python3 audit.py record > record.jsonl` reads the author's existing balanced eighteen-variable PM(K33) lift, without modifying its source. Mean zero and spectral normalization one were exact in float64. Its H/(I-1) is 6.5218457109230465 bits per unit excess influence. Its predictor overhead remains small: at lambda 0.1 the three overheads are 0.04963459878949572, 0.03153731753098987, and 0.04568629001804103 bits. This is a direct check of the saved record gate, separate from the unbalanced nine-variable perfect-matching tower.

## Proved conclusions

PROVED: the predictor gap is exactly a KL divergence; the posterior deleted-count, derivative/integral, thinning, and balanced composition identities hold. See PROOFS.md, including the biased extension and the finite tower recurrence.

PROVED: for each fixed balanced base gate, every one of these predictor overheads converges along its self-tower. The proof is by summable boundary terms, with geometric factor W1(base)/I(base), and does not bound constants uniformly over base gates. Moving-bias towers are tested numerically, not covered by that theorem.

PROVED: the majority limit is an arcsine expectation, as detailed in MAJORITY_PROOF.md. The thin limits at lambda 0.1, 0.25, 0.5 are respectively 2.000713713857661, 2.0074326716011104, 2.051986127389584 bits, from majority.jsonl. The ratio limits are 2.032311900475004, 2.040522884349612, 2.0856553143130676 bits; lrat limits are 2.5384922206251357, 2.1662830870931957, 2.0310377519771436 bits. The old heuristic of two nats is replaced by the exact arcsine calculation. The two-bits statement is the thin limit as lambda then tends to zero.

CHECKED NUMERICALLY: `python3 majority.py > majority.jsonl` uses the exact finite spectrum through n=12801; the largest normalization error there is about 1.2e-11. Each limiting integral was checked by a second quadrature expression, with maximum discrepancy 3.552713678800501e-15. Decimal values of proved limits are numerical evaluations, not interval-certified constants.

Literature has been checked before any priority claim; see LITERATURE.md. No novelty claim is made. General P and FEI are still open in this work.
