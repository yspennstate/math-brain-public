# Open-problem completion and audit run

This run develops complete proofs for specific questions in the research archive and attempts the broader Lyons determinantal entropy-concavity conjecture. The full Lyons conjecture remains unresolved here. The agent execution ledger records actual launches and completions; 100 distinct tasks have completed using requested model `gpt-6-astra` with `reasoning_effort=max`, run in batches under the concurrency limit.

The [original QSO project index](https://github.com/yspennstate/math-open-problems/tree/master/probability_campaign_2026_09/paper_qso_fixed_points_2026_09_14) now links the complete four-type proof from the question it resolves. The original manuscript is preserved, with a separate timestamped completion report.

Read the [final research report](FINAL_RESEARCH_REPORT.md) for the completed statements, audit coverage and remaining gaps. The [computation index](COMPUTATIONS_INDEX.md) identifies exact certificates and numerical diagnostics.

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

Historical novelty is a separate, unfinished question. The archived five-type example and its original two fixed points are explicitly due to Jamilov2017: [the full primary-source audit091](agents/091.md) identifies the exact tensor and theorem. The positive-mixture classification is a separate result. In particular, the complete hypotheses of Jamilov's closest 2016 four-type QSO paper have not been retrieved. The QSO uniqueness proof settles the exact four-type question left open in the project's manuscript; it is not presented as a verified worldwide first. The two tree counterexamples match the subcritical and critical infinite-variance clauses of Thévenin's closing conjecture, but this run does not establish that no earlier counterexamples exist. The [primary-source audit067](agents/067.md) checks their exact scope against later restricted results, including2023 and2026 papers.

The earlier [perturbative 0.502 range](QSO_AVERAGING_RANGE.md) is retained as a separate method, together with its independent audit. The global 0.51 result is a sufficient convergence range; the larger spectral range in the table concerns local stability only.

## Reading the research record

The theorem notes above give the principal proofs in a form suitable for review. The numbered [agent reports](agents/) retain full derivations, source checks, failures, limitations and per-claim ledgers. Earlier reports are immutable and can contain obligations later solved by subsequent reports. A report's `PROVED` label is not a substitute for its argument or audit.

The initial inventory is in reports [001](agents/001.md)–[006](agents/006.md). It covers the probability campaigns, probability-1000 intake, ProofNet tracks, older classical projects and QSO/free-Brownian companion repositories. It is a structured portfolio review, not a claim that every historical page was reverified. Existing completed candidate proofs were distinguished from current gaps.

Important corrections include an exact counterexample to an archived Aldous–Fill flow-cut reduction, invalid strengthened Janson condensation claims, the distinction between fresh chronological and cyclic interchange paths, and a dimension obstruction to a universal MASA lifting constant. Their corrected statements and exact witnesses are retained in the reports; none is relabeled a disproof of a broader conjecture it does not address.

## Reproducibility and limits

The [computations](computations/) include exact rational and polynomial certificates, finite algebra checks and explicitly labeled floating-point searches. The solver's final certificate is produced by exact rational arithmetic. [Usage instructions and a verified example](SOLVER_USAGE.md) explain the input format and independent verifier. Agent026 found a false-zero certificate in the original public API; the current solver rejects the problematic floating-point inputs and the exact regression passes. The historical implementation and failure remain available for reproducibility.

No universal theorem is claimed to have been checked by Lean, formally verified by another proof assistant, or externally refereed. Full conjectures remain open wherever the claim ledger says so. Numerical nonfailure and agreement among agents do not prove a universal statement.

Canonical repository: `yspennstate/math-open-problems`, branch `master`, private. Initial source snapshot: [`8861ffde776a1dbf842e918590cc1003492ff296`](https://github.com/yspennstate/math-open-problems/tree/8861ffde776a1dbf842e918590cc1003492ff296). New work is appended under `proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/`. Timestamped checkpoints preserve intermediate states and later reports preserve corrections; unrelated source correspondence is excluded.

Final execution: **107 launched; 100 completed; 7 interrupted; 0 active.** All 100 requested distinct tasks completed. The archive contains 96 full original completed reports and four clearly labeled recovery records for unavailable originals. Read the [execution ledger](execution_ledger.json), [agent index](AGENT_INDEX.md), and [recovery provenance](recovery/INTERRUPTIONS.md). The GitHub proof collection is the deliverable; the local draft PDF was unavailable after disconnection.



## Reports completed after recovery

| Report | Complete result and limits |
|---|---|
| [079](agents/079.md) | Full independent rank-two proof audit, exact arithmetic and a boundary entropy corollary for compression rank or corank at most one. |
| [080](agents/080.md) | Primary DC1 inheritance theorem matched; repaired open-dense proof, strict one-step horseshoe obstruction and a conditional iterate-horseshoe result. |
| [081](agents/081.md) | Complete conditional Fisher and fourth-power block-quartic proof; full strict-concavity neighborhood for connected 2+2 blocks. Independent audit 096 passes. |
| [082](agents/082.md) | Complete positive attracting raw two-cycle and exact averaging-rate obstructions. Global cycle uniqueness and optimal thresholds are not claimed. |
| [083](agents/083.md) | Strict two-coordinate entropy chords, sharp off-diagonal quartic modulus and the exact conditional flatness criterion, including boundary endpoints. |
| [084](agents/084.md) | Exact primitive C_p^2 Chern lattice Smith form and trace refinement. The whole cyclic-induction lattice is different; no Baum–Connes conclusion. |
| [085](agents/085.md) | Reconstructed spectral/subset entropy bounds, sharp forest/matching corrections and block-number equality. Full audit 101 passes with a wording erratum; the Lyons bridge is unproved. |
| [086](agents/086.md) | Exact four-type support and interiority, finite support propagation, and a five-type basin family with unchanged coefficient zero pattern. |
| [087](agents/087.md) | Full independent averaged leave-one-out gate audit passes, including covariance cancellation and the empirical-width counterexample. The neural pipeline remains conditional. |
| [088](agents/088.md) | Boundary diagonal entropy lines and co-monotone coordinate-resampling entropy with equality; mixed-sign counterexample to the broader noise claim. |
| [089](agents/089.md) | Exact neutral-bubble subdivision inventory, reserve estimate and encoding/norm obstructions. The general Benjamini–Schramm problem remains open. |
| [090](agents/090.md) | Cubic four-type uniqueness, interiority and averaged 9/10 contraction after five steps. Full audit 106 passes with two editorial clarifications. The full degree-at-least-four tensor class is empty. |
| [091](agents/091.md) | Full 2017 source audit identifies the archived five-type tensor, fixed points and spectra as Jamilov's prior result. The 2016 scope remains unverified. |
| [092](agents/092.md) | Structured disjoint-block rank-two six-site positivity and boundary entropy corollary with an exact certificate. The general case remains open. |
| [093](agents/093.md) | Bounded integrated proof audit passes after the rational-input premise and two LaTeX repairs. |
| [094](agents/094.md) | Certified whole-path rational continuation with adaptive Bernstein/Lipschitz/Hessian tubes; exact activation, invariant-face and piecewise certificates. |
| [095](agents/095.md) | Universal iid-column projector anchor bound and sharpness, with precise ANOVA/reveal/influence rate equivalences. The arbitrary-law influence estimate remains open. |
| [096](agents/096.md) | Full independent 081 audit passes without mathematical repairs; 950 exact assertions and the full 16-dimensional neighborhood argument checked. |
| [097](agents/097.md) | Reconstructed strict three-site entropy region, explicit rational center and radius, Fisher-null strictness and exact conditional-feature criterion. Full three-site conjecture remains open. |
| [098](agents/098.md) | Full independent 057 audit passes: exact algebraic certificates, universal and generic degree proofs, and boundary embedding checked. |
| [099](agents/099.md) | Bounded dependency/source audit found no blocking defect; independently rederived 030-to-092 and replayed exact 092. Scope and missing-witness limitations retained. |
| [100](agents/100.md) | Full bounded claim/source/provenance audit; four wording and attribution repairs plus interrupted-063 timestamp clarification. |
| [101](agents/101.md) | Full independent 085 audit passes; nonzero off-diagonal wording erratum; explicit failure of the matching estimate to establish the unproved Lyons bridge. |
| [102](agents/102.md) | Full independent 060 leakage audit passes, including both 1/2 endpoints and 7/50 uniqueness; exact cap, transport and symbolic counterexample certificates. |
| [103](agents/103.md) | Full 012 ODE audit passes; bounded forced-069 estimate reconstructed with stronger duration kernels, viability and perturbation counterexamples. Only scalar entrance is claimed sharp. |
| [104](agents/104.md) | Dimension-independent sufficient class for every diagonal direction: normalized L condition number at most 3 gives curvature at most −//a//²/2. Exact identities and mixed-entry/rectangle obstructions; 211 exact checks. |
| [105](agents/105.md) | Exact radial-source inverse-direction criterion with no effective-rank requirement, uniform small-ball and fourth-trace bounds, and a deterministic mean-direction obstruction. Actual harmonic-design gate remains open. |
| [106](agents/106.md) | Full independent cubic theorem and algorithm audit passes; 307 assertions and 45,056 exact assignments. Two editorial clarifications, no mathematical correction. |
| [107](agents/107.md) | Complete unlabeled diamond-cone equivalence, endpoint ranks, global extension of three-level dual certificates and real-frame rotation lemma. Complex equalization obstruction; general six-site positivity and the lost 074 witness remain unresolved. |

These are 29 full original reports created after recovery. Together with the 67 surviving completed reports among 001–068, there are 96 available full original completed reports. Four unavailable earlier originals remain labeled in the recovery record; interrupted 063 has a separate root-authored record. [Actual execution index](AGENT_INDEX.md).
