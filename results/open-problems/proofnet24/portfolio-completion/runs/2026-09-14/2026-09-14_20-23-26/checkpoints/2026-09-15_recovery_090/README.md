# Open-problem completion and audit run

This run develops complete proofs for specific questions in the research archive and attempts the broader Lyons determinantal entropy-concavity conjecture. The full Lyons conjecture remains unresolved here. The agent execution ledger records actual launches and completions; the requested total is 100 distinct `gpt-6-astra` agents with `reasoning_effort=max`, run in batches under the concurrency limit.

The [original QSO project index](https://github.com/yspennstate/math-open-problems/tree/master/probability_campaign_2026_09/paper_qso_fixed_points_2026_09_14) now links the complete four-type proof from the question it resolves. The original manuscript is preserved, with a separate timestamped completion report.

## Main mathematical deliverables

| Result | Scope and proof | Independent review |
|---|---|---|
| Four-type fixed-point uniqueness | [Complete theorem note](FOUR_TYPE_UNIQUENESS.md): every four-type strictly non-Volterra QSO, including zero coefficients and boundary fixed points | [007](agents/007.md), [008](agents/008.md), and the independent constructive proof in [024](agents/024.md) |
| Quantitative stability and algorithms | Coefficient Lipschitz bounds, exact residual certificates, and a guaranteed rational solver with polynomial bit complexity | [013](agents/013.md), [exact grid proof065](agents/065.md), [solver usage](SOLVER_USAGE.md) |
| Half-step global convergence | [Explicit proof](QSO_HALF_STEP_EXPLICIT.md), factor `7967/8192` after three steps | [Full audit 024](agents/024.md) |
| Every averaging weight through 0.51 | [Global theorem](QSO_GLOBAL_051.md), including all smaller positive weights via [the entrance argument](QSO_AVERAGING_RANGE.md); factor `2499/2500` after three steps for weights from 0.5 through 0.51 | [Full independent audit046](agents/046.md) |
| Analytic coefficient dependence | [Uniform analytic extension across the coefficient boundary](agents/044.md), exact derivatives, quadratic remainder bounds, and precise activation of a missing type | Complete derivation [044](agents/044.md), parent independent review |
| Exact attainable fixed-point geometry | [Necessary and sufficient singleton/pair inequalities in every dimension](QSO_FIXED_POINT_GEOMETRY.md); improved four-type coefficient constant `(204+95sqrt(5))/121` | Complete derivation [049](agents/049.md), parent independent review |
| Tangent spectrum and determinant | [Spectral note](QSO_SPECTRAL_BOUNDS.md): strict eigenvalue modulus below `sqrt(2)`, determinant above `4/3`, and a sufficient local averaging range through `(18-sqrt(2))/23` | Full derivation [029](agents/029.md), parent independent review |
| Small parental-offspring leakage | Uniqueness and global averaged convergence if total parental probability is below `1-sqrt(3)/2` | Main note, Theorem 6; [014](agents/014.md) |
| Five-type perturbation path | [Exactly one interior fixed point](QSO_FIVE_TYPE_PERTURBATION.md) for every positive mixture of the archived multiple-fixed-point example with the equiprobable operator | [Full independent audit052](agents/052.md), parent review |
| Restricted Lyons cases | [Two sites, two-coordinate blocks, one-row/column slices, and indefinite rank-two directions through dimension five](LYONS_PARTIAL_RESULTS.md) | [016](agents/016.md), [017](agents/017.md), [018](agents/018.md), [019](agents/019.md) |
| Every kernel line through a diagonal | [Full feasible-interval entropy concavity in every dimension](DIAGONAL_ENDPOINT_ENTROPY.md), strict except constant lines; sharp marginal curvature and convex total correlation | [Full independent audit068](agents/068.md), exact symbolic certificate |
| Scaled cross-block entropy concavity | Any dimension: arbitrary two-coordinate block and a fixed cross matrix multiplied by one complex scalar; strict mutual-information chord bound | [Full independent audit045](agents/045.md), parent review |
| Subcritical tree counterexample | [One fixed law with finite third moment and a non-Gaussian degree-count subsequence limit](SUBCRITICAL_COUNTEREXAMPLE.md) | Construction [015](agents/015.md), full independent audit [034](agents/034.md), parent review |
| Critical infinite-variance tree counterexample | [One fixed computable critical law with a non-Gaussian degree-count subsequence limit](CRITICAL_COUNTEREXAMPLE.md) | Construction [028](agents/028.md), full independent audit and computable selector [033](agents/033.md), full integration audit [062](agents/062.md), parent review |
| Growing-signal Gaussian-kernel benignity | Uniform almost-sure interpolation consistency on the entire growing low-harmonic ball, with conditionally centered covariance-bounded noise | Derivation [003](agents/003.md), independent proof audit [021](agents/021.md) |
| Fixed-law P12 repair | [Three-tier recursion and complete exponential probability theorem](agents/037.md), including arbitrary-coupling almost-sure convergence | [Full independent audit054](agents/054.md), with a direct rectangular-net replacement for an ambiguity in the cited source proof |

Historical novelty is a separate, unfinished question. In particular, the complete hypotheses of Jamilov's closest 2016 four-type QSO paper have not been retrieved. The QSO uniqueness proof settles the exact four-type question left open in the project's manuscript; it is not presented as a verified worldwide first. The two tree counterexamples match the subcritical and critical infinite-variance clauses of Thévenin's closing conjecture, but this run does not establish that no earlier counterexamples exist. The [primary-source audit067](agents/067.md) checks their exact scope against later restricted results, including2023 and2026 papers.

The earlier [perturbative 0.502 range](QSO_AVERAGING_RANGE.md) is retained as a separate method, together with its independent audit. The global 0.51 result is a sufficient convergence range; the larger spectral range in the table concerns local stability only.

## Reading the research record

The theorem notes above give the principal proofs in a form suitable for review. The numbered [agent reports](agents/) retain full derivations, source checks, failures, limitations and per-claim ledgers. Earlier reports are immutable and can contain obligations later solved by subsequent reports. A report's `PROVED` label is not a substitute for its argument or audit.

The initial inventory is in reports [001](agents/001.md)–[006](agents/006.md). It covers the probability campaigns, probability-1000 intake, ProofNet tracks, older classical projects and QSO/free-Brownian companion repositories. It is a structured portfolio review, not a claim that every historical page was reverified. Existing completed candidate proofs were distinguished from current gaps.

Important corrections include an exact counterexample to an archived Aldous–Fill flow-cut reduction, invalid strengthened Janson condensation claims, the distinction between fresh chronological and cyclic interchange paths, and a dimension obstruction to a universal MASA lifting constant. Their corrected statements and exact witnesses are retained in the reports; none is relabeled a disproof of a broader conjecture it does not address.

## Reproducibility and limits

The [computations](computations/) include exact rational and polynomial certificates, finite algebra checks and explicitly labeled floating-point searches. The solver's final certificate is produced by exact rational arithmetic. [Usage instructions and a verified example](SOLVER_USAGE.md) explain the input format and independent verifier. Agent026 found a false-zero certificate in the original public API; the current solver rejects the problematic floating-point inputs and the exact regression passes. The historical implementation and failure remain available for reproducibility.

No universal theorem is claimed to have been checked by Lean, formally verified by another proof assistant, or externally refereed. Full conjectures remain open wherever the claim ledger says so. Numerical nonfailure and agreement among agents do not prove a universal statement.

Canonical repository: `yspennstate/math-open-problems`, branch `master`, private. Initial source snapshot: [`8861ffde776a1dbf842e918590cc1003492ff296`](https://github.com/yspennstate/math-open-problems/tree/8861ffde776a1dbf842e918590cc1003492ff296). New work is appended under `proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/`. Timestamped checkpoints preserve intermediate states and later reports preserve corrections; unrelated source correspondence is excluded.

Current recovery checkpoint: **90 launched;77 completed;7 interrupted;6 active.** The target is100 completed distinct agents, requiring107 launches after the recorded losses. Read the [execution ledger](execution_ledger.json), [agent index](AGENT_INDEX.md), and [recovery provenance](recovery/INTERRUPTIONS.md). Four completed original reports were not pushed before the workspace disconnected; their retained summaries are labeled, and important claims are being reconstructed. The GitHub proof collection is the durable deliverable; the local draft PDF was not recovered.


## Reports completed after recovery

| Report | Complete result and scope |
|---|---|
| [079](agents/079.md) | Independent rank-two entropy audit; arbitrary-dimensional rank/corank-one compression boundary corollary |
| [080](agents/080.md) | Repaired DC1 genericity proof and Lipschitz horseshoe obstruction |
| [081](agents/081.md) | Conditional Fisher identity and block quartic; full connected2+2 entropy neighborhood, independent096 audit pending |
| [082](agents/082.md) | Exact rate obstructions and positive attracting raw two-cycle for epsilon<=1/50 |
| [083](agents/083.md) | Strict two-coordinate entropy chords and sharp8/3 off-diagonal quartic modulus |
| [084](agents/084.md) | Exact C_p×C_p Chern lattice Smith form and conditional trace refinement; no Baum–Connes conclusion |

These are complete new reports. Earlier unavailable originals remain explicitly labeled in the recovery record. [All actual tasks](AGENT_INDEX.md).
