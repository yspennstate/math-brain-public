# R01–R20 hourly research: GitHub-only continuation protocol

Effective user instruction: 15 September 2026. Continue the existing twenty open-problem assignments, use the strongest available reasoning, and archive substantive results in `yspennstate/math-open-problems` on `master`. Do not send research emails. This document replaces the earlier Gmail/Drive delivery instructions for these twenty workers; it does not replace historical mathematical evidence.

This is a research and archival protocol, not evidence that a mathematical conjecture is solved or that a future scheduled run has completed. Scheduler activation is recorded separately after actual update confirmations.

## Execution

1. On each invocation, use the connected GitHub tool to read the repository README, this protocol, the exact target's latest complete report/ledger, and relevant source files. Recover actual proofs, not merely a search snippet or a PROVED label. Browse current primary literature when checking status or novelty. Do not assume cross-task chat memory, persistent local files, or access to past attachments.
2. Continue from the latest unresolved proof obligation. Spend most of the available execution budget on creative mathematical work: attempt an explicit new lemma, complete derivation, rigorous conditional reduction, or exact counterexample. A literature-only or status-only recap is not the intended deliverable. Never stop solely because the problem is old or difficult. Preserve useful restricted theorems without calling them the full conjecture.
3. Use the deepest reasoning and strongest model actually available in the execution environment. The user's preference is GPT-6 with maximum thinking and sustained work throughout the available hour. A prompt cannot itself select an unavailable model, extend a runtime limit, or guarantee sixty minutes of computation. Do not invent model settings, agents, experiments, elapsed work, or independent reviews. No purchases, external paid compute, endless sleeps, or resource-limit evasion.
4. Cross-read up to two useful completed peer reports when available; check concrete transferable lemmas rather than trusting labels. Do not wait for another task, create circular proof dependencies, or let missing peers block original work. Concentrate on solving, using targeted adversarial tests as part of the proof process rather than replacing research with administrative auditing.
5. Do not disable, pause, delete, create, or otherwise alter schedules. A lack of progress, missing service, failed GitHub write, or candidate solution must not be used by the worker as a reason to terminate the research program. After genuine full closure, preserve its complete proof and independent checks, then help the nearest unresolved repository target while retaining the original closure record. Follow any actual later user stop instruction and all platform limits/approval requirements; never circumvent a pause or approval requirement.

## Mathematical record

Every completed research run must preserve the full substantive work: exact target and normalization; prior state and source paths/commit identifiers; new derivations with equations and all intermediate obligations; stable claim IDs with quantifiers, hypotheses, dependencies and PROVED / CONDITIONAL / DISPROVED / OPEN labels; failed approaches and exact obstructions; reproducible code, parameters, seeds, exact or interval certificates when applicable; distinction between known and new results; remaining gaps and the precise next attack.

PROVED means the written argument has actually been checked under the stated hypotheses. A conditional bridge is not a proof of its missing premise. Separate finite from asymptotic/universal results, expectation from almost-sure statements, quenched from annealed laws, empirical evidence from theorem, and a model from its surrogate. Never fabricate a vote or call a target closed on the basis of a label alone.

## GitHub storage and collision safety

Repository: `yspennstate/math-open-problems`. Existing branch: `master`. Preserve repository privacy and all historical files.

If the exact target already has an established research folder, resume there and retain its naming. Otherwise use the fallback folder in the assignment table. Worker IDs R01–R20 are not the same numbering system as historical P01–P25 or lemma IDs R16/R32; match the mathematical target, not the number alone.

Create a NEW immutable UTF-8 report each run:

`<track>/runs/YYYY-MM-DD/YYYY-MM-DD_HH-MM-SS_UTC__Rxx__<unique-run-id>__report.md`

Save actual scripts, TeX, certificates and supporting text under the same track's `artifacts/`, with a run identifier. Use GitHub `create_file` for new text files, or another available authorized content/commit action. GitHub Contents writes are real commits to the named branch; local files alone are not a push. Avoid rewriting the large shared `STATE.md` or a global manifest on every worker run. Put any continuation ledger snapshot in the immutable report; update a per-track stable ledger only after reading its latest blob SHA and preserving concurrent changes.

Before writing, read the current branch/target path. Use create-only operations for reports; never replace a historical report or force-push. If a transient conflict occurs, refetch and make at most two bounded retries with a collision-safe name; do not overwrite another worker. Commit message: `ProofNet Rxx: research <UTC timestamp>`. After a successful write, record the returned commit SHA and read the created path back to confirm the full content. A commit identifier plus verified file content, not an intended path, is the success evidence. Save an intermediate substantive checkpoint before execution resources are nearly exhausted when feasible.

No Gmail sends, forwards, drafts, or email delivery attempts. No Drive uploads or mandatory mailbox/Drive scans. GitHub is the shared research destination. Do not post unrelated correspondence, credentials, account data, or private non-research material. Do not change repository visibility, permissions, workflows, branches, or unrelated files.

If GitHub is unavailable or requires approval, honor that requirement. Continue the mathematics and preserve the complete unpushed report in the task conversation/local attachment where available, marked `GITHUB_SAVE_FAILED` or `APPROVAL_REQUIRED`, with the exact intended path. A saving failure does not invalidate a proved lemma. Do not claim archival success without confirmation; a later invocation should recover and commit such output only when its actual contents are accessible. Never silently replace missing research with a summary. Return a brief task receipt containing status, confirmed repository path/commit, strongest result and next obligation after successful archival; return the full report in the conversation if archival fails. No email notification is requested.

## Preserved assignments and evenly staggered hourly slots

Slots below are minute-of-hour starts in Asia/Jerusalem, with no programmed end date. Completion and commit times can be later than the start slot. These are twenty separate research tasks, not twenty simulated agents inside a single task.

| Worker | Minute | Preserved target | Fallback research folder |
|---|---:|---|---|
| R01 | 00 | Full Fourier Entropy–Influence conjecture | `proofnet24/P03-fei` (existing FEI archive) |
| R02 | 03 | Dimension-free KLS conjecture | `proofnet24/R02-kls` |
| R03 | 06 | Sharp iid Rademacher singularity | `proofnet24/R03-sharp-bernoulli-singularity` |
| R04 | 09 | Critical one-dimensional random band matrices | `proofnet24/R04-critical-band-matrices` |
| R05 | 12 | Three-dimensional Anderson extended states | `proofnet24/R05-anderson-extended-states` |
| R06 | 15 | Two-dimensional Anderson localization | `proofnet24/R06-anderson-localization-2d` |
| R07 | 18 | KPZ fluctuations for undirected FPP | `proofnet24/R07-kpz-fpp` |
| R08 | 21 | Strict convexity of the exponential FPP shape | `proofnet24/R08-fpp-limit-shape` |
| R09 | 24 | Critical site percolation on Z^3 | `proofnet24/R09-critical-percolation-z3` |
| R10 | 27 | Square-lattice bond-percolation Cardy formula | `proofnet24/R10-square-lattice-cardy` |
| R11 | 30 | Planar self-avoiding-walk exponents | `proofnet24/R11-planar-saw` |
| R12 | 33 | Full deterministic-field de Almeida–Thouless line | `proofnet24/R12-de-almeida-thouless` |
| R13 | 36 | Komlós vector balancing | `proofnet24/R13-komlos` |
| R14 | 39 | Negative-margin spherical perceptron | `proofnet24/R14-negative-margin-perceptron` |
| R15 | 42 | Cugliandolo–Kurchan aging | `proofnet24/R15-cugliandolo-kurchan` |
| R16 | 45 | Full Beck–Fiala conjecture | `proofnet24/R16-beck-fiala` |
| R17 | 48 | Exact Chvátal–Sankoff binary constant | `proofnet24/R17-chvatal-sankoff` |
| R18 | 51 | Salem's Bernoulli-convolution classification | `proofnet24/R18-salem-bernoulli-convolutions` |
| R19 | 54 | Separable free-group-factor isomorphism problem | `proofnet24/R19-free-group-factors` |
| R20 | 57 | Kalikow directional zero–one problem | `proofnet24/R20-kalikow-zero-one` |

## Exact targets and inherited safeguards

### R01 — Fourier Entropy–Influence
Prove or disprove existence of universal C with sum_S fhat(S)^2 log(1/fhat(S)^2) <= C sum_S |S| fhat(S)^2 for every Boolean f:{-1,1}^n->{-1,1}, uniform-cube Fourier normalization and one fixed log base. Special classes and finite tests do not close FEI. Recover the repository's full signed-compiler, coset-pairing and entropy/coding work. Historical half-band endpoint bounds do not automatically control positive intermediate turnover or signed small-resolvent/parity frustration. Check these obligations and also try independent routes. Starting references to verify: arXiv:1312.3003 and arXiv:1711.00762.

### R02 — KLS
An absolute C must satisfy Var_mu(g) <= C integral ||grad g||^2 dmu for every isotropic log-concave probability measure on R^n and every locally Lipschitz g in the relevant Sobolev domain, uniformly in n. Polylogarithmic dimension dependence and quadratic-form-only bounds are not full closure. Try stopped stochastic localization/covariance resolvents and entropy/conditional Poincaré decompositions. Check product laws, simplexes and anisotropic conditional laws. Verify current primary literature, including arXiv:2607.24164, rather than importing a claimed bound uncritically.

### R03 — Sharp Rademacher singularity
For iid uniform +/-1 entries, target P(det B_n=0)=(1+o(1))*2*n*(n-1)*2^(-n). Equal/opposite row pairs and column pairs give leading mechanisms, with overlap corrections. The exponential rate (1/2+o(1))^n is not enough. Recover repository descendants of `rademacher_singularity_continuation_2026-08-15.md`. Connector-compatible linear entropy-defect rigidity and required-order centered-moment transfer were unresolved inherited obligations, not axioms; finite corank certificates do not close them. Test dense fibres, bounded-congestion decompositions and sharp collision-conditioned inverse Littlewood–Offord methods. Starting references: arXiv:2010.06554 and arXiv:2512.15077.

### R04 — Critical band matrices
Use real symmetric N-by-N Gaussian matrices on the discrete circle, independent centered upper-triangular entries, variance 1/(2W+1) for circular distance <=W, zero otherwise, W=floor(c*sqrt(N)), fixed c>0. At fixed bulk E in (-2,2), establish and identify the limiting microscopic point process N*rho_sc(E)*(lambda_j-E) and its c-crossover. Keep existence, identification, variance-profile normalization and universality distinct. Work on block Schur complements, transfer operators and microscopic tightness. Established regimes outside the critical window do not solve this target. Check arXiv:2508.05802, 2501.01718 and 2506.06441 and newer primary work.

### R05 — Anderson extended states
On ell^2(Z^3), H_lambda psi(x)=sum_{|y-x|_1=1}psi(y)+lambda V_x psi(x), V_x iid uniform[-1,1]. For all sufficiently small positive lambda, prove almost-sure nonzero absolutely continuous spectrum in a nonempty bulk energy interval. Pure ac and transport are separate stronger targets. Bethe lattices, sigma models, annealed Green functions and kinetic-time diffusion are not substitutes. Seek quenched small-imaginary-part resolvent control or a genuine multiscale spectral criterion; preserve the actual disorder law and order of limits.

### R06 — Anderson localization in two dimensions
For the same uniform-disorder nearest-neighbor Hamiltonian on ell^2(Z^2), prove for every lambda>0 almost-sure pure point spectrum with exponentially decaying eigenfunctions. Dynamical localization is a distinct stronger conclusion. Strong-disorder, spectral-edge, one-dimensional and finite-box statements do not settle weak-disorder two-dimensional localization. Attempt a disorder-dependent initial-scale estimate sufficient for multiscale/fractional-moment localization, with loops and logarithmic losses controlled.

### R07 — KPZ first-passage fluctuations
Ordinary undirected nearest-neighbor FPP on Z^2 with iid Exp(1) edge weights: prove Var(T(0,n e1))=n^(2/3+o(1)). Transversal exponent 2/3 and limiting laws require separate arguments. Do not substitute directed last-passage percolation or silently assume curvature. Seek exact resampling covariance identities and scale-dependent geodesic overlap estimates. Cross-read R08 without circular curvature assumptions. Starting primary-author reference: arXiv:1511.03262.

### R08 — FPP shape
For the same undirected Exp(1) model, mu(x)=lim_n T(0,floor(nx))/n and B={x:mu(x)<=1}. Prove or disprove that boundary B has no nontrivial line segment. Quantitative curvature and differentiability are separate properties. Use positive-density surgery or jointly constructed Busemann increments without assuming rotational symmetry, curvature or differentiability. Atom-induced flat-edge examples are not exponential-law counterexamples. Start with arXiv:1511.03262 and verify the current frontier.

### R09 — Critical percolation
For independent nearest-neighbor SITE percolation on Z^3, prove theta(p_c)=P_pc(0 in an infinite open cluster)=0, with p_c=inf{p:theta(p)>0}. Dimension two, high-dimensional lace expansion, trees and nonamenable graphs are not substitutes. Seek finite-volume pivotal inequalities or rigorous downward renormalization from hypothetical critical percolation without assuming the needed robust crossings. A dichotomy such as that discussed in arXiv:2608.23661 is not automatically the full theorem.

### R10 — Square-lattice Cardy
For critical BOND percolation on the square lattice at p=1/2 and every Jordan quadrilateral, prove convergence of designated crossing probabilities to Cardy's conformal-cross-ratio formula as mesh tends to zero. State boundary and cross-ratio conventions. SLE6 convergence is a separate stronger conclusion. Triangular SITE percolation is not the target. RSW and tightness alone do not identify the limit. Try corrected local observables, exact finite-cell cancellation and a proved globally summable defect. Starting reference: doi:10.1007/s00220-025-05255-z.

### R11 — Planar self-avoiding walk
Uniform n-step nearest-neighbor self-avoiding walk on Z^2 from zero: primary target E||omega_n||^2=n^(3/2+o(1)). Separate target c_n=mu^n*n^(11/32+o(1)), mu=lim c_n^(1/n). The honeycomb connective constant, high-dimensional exponents and kinetic-growth walks are different problems. Try quantitative bridge renewal/polygon surgery or parafermionic control without assuming SLE8/3 convergence. Exact enumeration can falsify proposed inequalities but is not an asymptotic proof. Starting reference: arXiv:1205.0401; check every claimed proof's actual arguments.

### R12 — de Almeida–Thouless
SK Ising Gibbs weight exp[(beta/sqrt(N))*sum_{i<j}g_ij sigma_i sigma_j+h*sum_i sigma_i], iid standard Gaussian g_ij, deterministic h. With correctly selected RS overlap q=E tanh^2(beta*sqrt(q)*Z+h), establish equivalence of replica symmetry of the Parisi minimizer and beta^2 E sech^4(beta*sqrt(q)*Z+h)<=1. Handle branch selection, h=0 and equality explicitly. Local replicon stability is not global Parisi minimality; a Gaussian random-field theorem is not this target. Work on the full Parisi directional-derivative obstacle and global monotonicity. Starting reference: doi:10.1063/5.0073807.

### R13 — Komlós
For every real m-by-n matrix A with all column Euclidean norms <=1, find epsilon in {-1,1}^n with ||A epsilon||_infinity<=K for an absolute K independent of m,n. This is deterministic worst-case, not random Gaussian input or Matrix Spencer. Seek dimension-free partial coloring, entropy/spectral potentials or deterministic certificates. Coordinate with R02/R03/R16 without assuming their unresolved bridges. Check arXiv:2508.03961, 2512.15077 and 2608.28452 for exact scope.

### R14 — Negative-margin spherical perceptron
For each fixed kappa<0, g_a iid N(0,I_N), M=floor(alpha N), seek x with ||x||^2=N and <g_a,x>/sqrt(N)>=kappa for all a. Establish the sharp SAT/UNSAT threshold alpha_c(kappa), a correctly normalized full-RSB variational characterization and matching high-probability bounds. Recover the actual candidate functional from primary sources; do not invent it or assume the positive-margin RS expression remains valid. Ising and zero-margin models are different. Separate information-theoretic from algorithmic capacity. Starting references: arXiv:2010.15811, 1306.3980 and 2312.16531; assess claimed resolutions critically.

### R15 — Cugliandolo–Kurchan aging
Initially spherical p=3, small fixed positive T, covariance E H_N(x)H_N(y)=N*(<x,y>/N)^p/2 on sphere radius sqrt(N), Langevin generator T Delta_S-grad_S H_N dot grad_S, independent uniform start. Prove the predicted long-time two-time correlation/response aging and nonequilibrium fluctuation-dissipation relation after taking N to infinity FIRST. Derive response normalization and the aging clock; do not assume t/s scaling automatically. Fixed-N equilibrium, threshold energy or a formal ansatz is not closure. Try coercive Volterra-memory estimates and sector-matching lemmas. References: doi:10.1103/PhysRevLett.71.173, doi:10.1002/cpa.22197 and arXiv:2608.20623, with exact scope verified.

### R16 — Beck–Fiala
For every 0/1 matrix with at most t nonzeros per column, find signs epsilon with ||A epsilon||_infinity<=C sqrt(t), absolute C for all dimensions and t>=1. Random incidence, fractional coloring and only t>=log^2 n do not settle the full target. Exploit bounded column support using localized partial coloring, entropy or resampling rather than merely assuming R13. Starting reference: arXiv:2508.03961; verify exact remaining regimes.

### R17 — Chvátal–Sankoff
Determine exactly gamma_2=lim_n E LCS(X_1...X_n,Y_1...Y_n)/n for independent iid uniform binary strings. Existence, a simulation or a renamed unknown limit is not closure. Seek an evaluated exact characterization via genuine boundary processes/stationarity or matching computable primal/dual bounds with uniform errors. Match indicators have rectangular-cycle dependence: the independent Bernoulli matching model is not the actual LCS model. Preserve certified improved bounds as partial progress. Starting references: arXiv:2212.01582 and doi:10.1111/sjos.70086.

### R18 — Salem Bernoulli convolutions
Classify lambda in (1/2,1) for which Law(sum_{j>=0} epsilon_j lambda^j), independent uniform signs, is Lebesgue absolutely continuous. Prioritize genuinely unresolved reciprocal-Salem parameters and a reusable criterion. A single parameter, almost-everywhere result, full Hausdorff dimension or Fourier decay to zero is not full classification. Do not strengthen absolute continuity to L2 without proof. Seek exact Fourier-product/entropy collision or algebraic transfer-operator estimates with certified truncation errors. Starting references: arXiv:2604.18875 problem 1.1(4), arXiv:1602.00261. Do not rely on the withdrawn arXiv:1708.05544 as an established result.

### R19 — Free group factors
Decide isomorphism/nonisomorphism of the usual separable II_1 factors L(F_m),L(F_n) for distinct 2<=m,n<=infinity; start with L(F_2) versus L(F_3) and justify all-or-none reductions precisely. Reduced C*-algebras and a nonseparable analogue are different targets. A canonical-generator entropy calculation is not enough without the necessary W*-invariance. Seek a generator-independent invariant or constructive isomorphism and check invariance before rank computations. Starting comparison: doi:10.1007/s00039-024-00669-8; do not mistake its nonseparable scope for closure here.

### R20 — Kalikow directional zero–one
For each d>=3, iid nearest-neighbor elliptic environments on Z^d and deterministic unit ell, decide whether annealed P_0(lim_n X_n dot ell=+infinity) belongs to {0,1}. Start with uniformly elliptic d=3 as a milestone, not the full target. The union of opposite-direction transience events, planar cases, ballisticity and Dirichlet-only results are different conclusions. Stationary mixing counterexamples do not settle the iid problem. Seek same-environment two-walk couplings or measurable conditional-tail/regeneration arguments; spatial iid does not make the visited environments independent. Starting references: Kalikow (1981), arXiv:2108.11424 and arXiv:math/0501533.
