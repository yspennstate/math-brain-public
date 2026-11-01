# Research completion report — 15 September 2026

## Outcome and exact scope

This run reviewed the GitHub research portfolio, developed complete proofs for specified statements, tested proposed routes, and recorded independent audits and corrections. The full Lyons determinantal entropy-concavity conjecture was the main famous target. **It remains unresolved in this run.**

The principal finished archive problem is four-type fixed-point uniqueness for strictly non-Volterra quadratic stochastic operators. Two full conditioned-tree counterexamples address the precise unrestricted fluctuation clauses identified below. These are mathematical proof claims with their arguments and audits available for review; historical priority, external acceptance and formal verification are separate questions.

[Current proof index](README.md) · [Claim ledger](CLAIM_LEDGER.md) · [Actual agent record](AGENT_INDEX.md) · [Exact execution metadata](execution_ledger.json)

## 1. A complete answer to the archive's four-type fixed-point question

Let
\[
V_k(x)=\sum_{i,j=1}^4 P_{ij,k}x_i x_j,\qquad
P_{ij,k}=P_{ji,k}\ge0,\quad \sum_kP_{ij,k}=1,
\quad P_{ij,k}=0\quad(k\in\{i,j\}).
\]
Then \(V\) has exactly one fixed point in the simplex. Zero coefficients and boundary fixed points are included.

The [complete theorem note](FOUR_TYPE_UNIQUENESS.md) contains the proof. Every fixed point has coordinates at most \((3-\sqrt5)/2<1/2\); the exact two-versus-two sign transfer bound then excludes two distinct fixed points. Independent derivations and full audits are retained in reports 007, 008, 024 and 031. The original project's entry page now links the completion from the question left open in its preserved manuscript.

The completed quantitative extensions include:

| Result | Exact scope and review |
|---|---|
| Guaranteed rational solver | Averaging with weight \(2/5\), a coordinate cap, factor \(23/25\), and exact residual certificates. Report 065 proves the single-point polynomial bit-complexity guarantee; the corrected [solver instructions](SOLVER_USAGE.md) identify the usable implementation. |
| Larger global averaging range | Every constant positive averaging weight at most \(0.51\); [full theorem](QSO_GLOBAL_051.md) and independent 046 audit. A larger spectral range is only a local stability result. |
| Sharp algebraic degree | Rational fixed-point field degree at most eight, boundary degree at most four, with sharp exact examples; full independent 098 audit of 057. |
| Whole coefficient paths | Report 094 gives finite rational tubes covering all parameters of a piecewise-affine coefficient path, including zero coefficients and boundary activation. Its output-sensitive cell bound is \(O(\varepsilon^{-1/2})\), not a polynomial bound in tolerance bit length for an explicit entire partition. |
| Parental leakage | Uniform four-type uniqueness through total leakage \(7/50\), and the boundary-specific threshold \(1/2\), with full independent 102 audit of 060. These larger uniqueness ranges do not extend the global convergence range. |
| Continuous and forced dynamics | Report 103 audits 012 and reconstructs the bounded forced estimate from lost 069. The scalar entrance bound is sharp; the exponential constants are sufficient. |
| Cubic analogue | Report 090 proves the four-type, three-parent, strict all-parent-exclusion theorem and a guaranteed averaged algorithm. Full independent 106 audit passes. The exact full tensor class is empty for degree at least four. |
| Raw dynamics obstruction | Report 082 proves an attracting positive-coefficient raw two-cycle for its explicit family. Fixed-point uniqueness therefore does not imply convergence of raw iteration. |

The five-type example at the endpoint of the perturbation study is **prior work by U. U. Jamilov (2017)**, including its two fixed points and spectra. Report 091 retrieved and checked the original paper. The positive-mixture classification in [the separate note](QSO_FIVE_TYPE_PERTURBATION.md), audited by 052, is distinct. The full hypotheses of the closest 2016 four-type paper remain unverified, so this run does not claim a cleared worldwide first.

## 2. Two precise conditioned-tree counterexamples

The [subcritical construction](SUBCRITICAL_COUNTEREXAMPLE.md) gives one fixed aperiodic offspring law with mean below one, finite third moment and no exponential moment. Along a deterministic conditioning subsequence, its centered degree-one count has a non-Gaussian mixture of two normal laws. Report 034 independently audits the complete construction.

The [critical construction](CRITICAL_COUNTEREXAMPLE.md) gives one fixed computable critical offspring law with a non-Gaussian degree-count subsequence limit. Its certificate-enumeration selector is integrated in the proof and independently audited in 033 and 062. The argument does not claim that the huge first selected stage integer was explicitly computed.

These address the unrestricted subcritical/no-exponential-moment and critical/infinite-variance clauses in the closing conjecture of Thévenin's *Vertices with fixed outdegrees in large Galton–Watson trees*, read alongside Janson's Problem 20.2. Report 067 checks the primary formulation and later restricted results; 099 and 100 review the source interface. They are not a disproof of all questions in Janson 20.2 or of finite-variance Gaussian limit theorems. Priority remains unverified.

## 3. Substantial restricted Lyons results, with the remaining gap preserved

The [entropy proof collection](LYONS_PARTIAL_RESULTS.md) gives full arguments and links for:

- Complex two-site kernels and fixed two-coordinate blocks in every dimension.
- Every feasible kernel line through a diagonal kernel, with boundary diagonal endpoints covered by 088.
- Arbitrarily oriented indefinite rank-two directions through dimension five, with full independent 079 audit.
- A full strict-concavity neighborhood around two connected interior two-site blocks, proved by 081 and independently audited by 096.
- A structured six-site compression class, proved by 092 and independently rederived within 099's bounded audit.
- An explicit full nine-real-dimensional three-site ball, reconstructed by 097, with a rational center, radius \(1/200000\), and a negative definite Hessian bound.
- All signs of diagonal directions under the dimension-independent condition \(\operatorname{cond}_2(\Gamma)\le3\), where \(\Gamma\) is the normalized L matrix. Report 104 proves \(H''[\operatorname{diag}a,\operatorname{diag}a]\le-\|a\|_2^2/2\); the hypothesis must hold throughout a segment for its integrated bound.

Report 085, audited in full by 101, gives spectral/subset entropy bounds, sharp forest and matching corrections, and block equality results. These estimates do not establish the proposed bridge to full Lyons concavity. An explicit example in 101 shows why the matching estimate is too weak for that route.

Report 107 proves the finite-cone coupling criterion and the real-frame rotation lemma, including a global extension of three-level dual certificates. A separate complex example refutes universal basis equalization. Neither statement supplies the missing general six-site positivity proof.

The exact three-site seven-feature scalar inequality in 097 remains to be proved universally. General six-site mixed positivity remains open. Finite numerical checks, the success of restricted cases, and agreement among agents are not substituted for those missing arguments.

## 4. Other completed deductions and corrected routes

The numbered reports preserve complete work across the portfolio. Selected later deductions include the exact primitive Chern lattice Smith form (084), a repaired DC1 inheritance and genericity proof with its precise hypotheses (080), support and basin classifications (086), a full averaged leave-one-out gate audit (087), exact subdivision inventory and encoding obstructions (089), and a universal iid-column projector anchor bound with its remaining influence condition (095).

Report 105 proves a source comparison theorem for the actual independent radial source and an arbitrary deterministic inverse map. It removes an effective-rank requirement when the stated weighted contraction and mean-direction condition holds. Its omitted-mean counterexample is a deterministic inverse-map obstruction. Establishing the condition for the actual harmonic design, and the full P20 hard-edge law, remain open.

Earlier reports retain exact failures of strengthened flow-cut, condensation, empirical-width, boundary-solver and exterior-square claims. Each failure is attached to the statement it actually refutes; the broader famous problem is not relabeled solved.

## 5. Corrections and verification

The current proof notes incorporate 093's explicit rational-input hypothesis and two LaTeX repairs. The original QSO entry point incorporates the 091/100 attribution correction. The current claim ledger records 101's equality wording erratum and 106's two cubic editorial clarifications while preserving the immutable numbered reports.

Verification includes full independent proof audits, exact rational and polynomial arithmetic, and specifically labeled floating-point diagnostics. [The computation index](COMPUTATIONS_INDEX.md) identifies the execution environment and purpose of the newly attached scripts. A script's finite checks certify those calculations, not a universal theorem by themselves. No new universal theorem was compiled in a proof assistant or externally refereed in this run.

## 6. Execution and archive provenance

**100 distinct agent tasks completed from 107 actual successful launches; seven interrupted tasks are excluded. Every worker launch requested `gpt-6-astra` with `reasoning_effort=max`. No worker task remains active.** There are 96 available full original completed reports plus four explicitly labeled completion/recovery records for unavailable originals.

Seven interrupted sessions are excluded from the requested completion count. Four other agents (069, 070, 072, 074) completed before a disconnection, but their original unpushed reports were unavailable afterward. Their terminal completion is retained in the conversation record; their surviving findings are explicitly labeled root recovery summaries. New reports reconstruct specified claims without claiming to restore missing original bytes.

In particular, the specific matrix, dual terms and atom weights of the retained 074 witness were not recovered or verified. The general coupling argument is handled separately; no invented certificate fills that gap. [Recovery provenance](recovery/INTERRUPTIONS.md) and [the retained findings](recovery/UNPUSHED_COMPLETED_REPORTS.md) state what survived.

The deliverable is the complete available and reconstructed GitHub proof/code collection. The local draft PDF was unavailable after disconnection and was not delivered. Existing manuscripts, completed numbered reports, and earlier checkpoints remain preserved.
