# Source and literature register

Date of targeted checks: 18 September 2026. Original research-source snapshot of the private repository: `492bc9007c7754e402aee4926ab15c1ec7ef7f55`. Later reads use the listed immutable file blobs. The delivery commit is separate and does not claim the repository was static during this continuation.

## Existing private repository evidence

Repository: `yspennstate/math-open-problems`.

1. `proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T17-58-00Z__report.md`, blob `b94c3d3e41eedcb647d9a69edaf7a404f3002648`. Existing full rank-two regular-kernel argument, leaf-free polynomial, sharp skewness envelope, and 1+5 lambda^4 bound. Read its proof and certificate description. The exact prescribed-eigenvalue minimization and sharper remainder in this package are not silently attributed to this earlier report.
2. `proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T17-14-40Z__report.md`, blob `f5e3fc4f504dd83fe0846df50a88155505e720d2`. Existing regular-kernel / triple-moment / transfer-operator reduction. Its positivity obstruction remains relevant; no generic fifth-trace theorem is proved in this package.
3. `proofnet24/P03-fei/solo-2026-09-17/ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`. Correct universal implication, conditional-entropy/Jensen--Shannon identity, and global-constant comparison.
4. `proofnet24/P03-fei/solo-2026-09-17/FINAL_HANDOFF_2026-09-18.md`, blob `ab77075ab4a76d4584aa5012e9a92ba7f1bd0f8a`. Its initial pointwise version of the reduction is false. The correction is supplied in `FEI.md`; the source file is preserved.
5. `proofnet24/P03-fei/solo-2026-09-17/INTERFERENCE_PATCHING_THEOREM_2026-09-18.md`, blob `79ab93e1cd3dbb16278f17bca337553e5520da6c`. Existing theorem with conditional bounded-coherence, boundary-separation, and local-leaf assumptions. No universal satisfaction of these hypotheses is inferred.
6. `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, blob `38c2595db2f075aba6fa4ac241efdd14542f9f85`. Used as context for proof-first research, honest scope, exact checks, preservation, and GitHub-only delivery. This was not a scheduler-maintenance run and makes no claim to have read every historical repository file or changed native tasks.

## Ising repository evidence

Repository: [yspennstate/ising-perceptron-capacity](https://github.com/yspennstate/ising-perceptron-capacity).

- `README.md`, blob `b57bb900d73dc0f3d28d2bf49b901f6805e594c6`: existing claimed theorem, exact replay scope, and independent-reproduction qualification.
- `THEORY.md`, blob `a302f3322dbc95da45a56d04c3164119e0fccec2`: source conditions, moment body, parameter assumptions, and certificate dependency map.
- `paper/main.tex`, blob `86a46bf89f5e84d203d3e2756da890c0e2d2467c`: moment-coordinate formulas, denominator, fixed-point normalization, and distinctions between analytic arguments and numerical enclosures. Read the relevant sections; no entire manuscript peer-review claim is made.
- `verification/verify_all.py`: inspected dispatch, failure handling, and requirement for full Region-I replay. Inspection is not execution.
- `reverification_20260713/independent_checks/star_interior_portable_check.py`, blob `749e04b373f01a174a832dbb572741b9c807857d`: existing portable geometric check, explicitly conditional on stored integral packets.
- `verification/results/huang_star_interior.json`, blob `889549cf88ef270333efa77ad0d5083f6f1d9d39`: source of the four stored packets copied in our checker. Payload identifier `e03fa07e2ea959ceb035313d28f222e193fd4d78427b389796746f3c69ae790a`. The geometric consequences were recomputed; the defining integrations were not.

The public package is MIT-licensed; this continuation uses mathematical definitions and the small explicitly identified packet inputs. It does not redistribute third-party source papers or private runtime credentials.

## Primary literature

### Sidorenko

- Joonkyung Lee and Bjarne Schuelke, *Convex graphon parameters and graph norms*, [arXiv:1910.08454](https://arxiv.org/abs/1910.08454). Establishes non-weak-norming for the graph in question and explicitly identifies its difficulty. A failure of the norm property does not refute Sidorenko.
- Balazs Szegedy, *On Sidorenko's conjecture for determinants and Gaussian Markov random fields*, [arXiv:1701.03632](https://arxiv.org/abs/1701.03632). Determinant/Gaussian-Markov-field inequalities discussed in the prior route; not imported as a proof of the required homomorphism inequality.
- David Conlon and Joonkyung Lee, *Sidorenko's conjecture for blow-ups*, Discrete Analysis (2021), [journal article](https://discreteanalysisjournal.com/article/21472-sidorenko-s-conjecture-for-blow-ups). A related structural result, not a certificate for the original H in this package.

### FEI

- Ryan O'Donnell and Li-Yang Tan, *A composition theorem for the Fourier entropy-influence conjecture*, [arXiv:1304.1347](https://arxiv.org/abs/1304.1347). Composition and read-once classes are prior work, not new consequences discovered here.
- Maria Jose Gonzalez, Paul MacManus and Maria Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, [arXiv:2606.00246v2](https://arxiv.org/abs/2606.00246v2). Primary 2026 restriction/stopping-tree framework; used to place the repository's restriction route in context. This note makes no assertion that the systematic-code obstruction is absent from every argument in that work.
- The random systematic-code existence proof in `FEI.md` is written in full. It is a basic coding-theoretic union-bound construction, not a claimed new code construction. The contribution assessed here is the constant-preserving application to the proposed FEI mechanism.

### Ising perceptron

- Brice Huang, *Capacity threshold for the Ising perceptron*, [arXiv:2404.18902v2](https://arxiv.org/abs/2404.18902v2), revised 22 April 2025. Directly inspected the objective, fixed-point definitions, Lemmas 7.2 and 7.10, and Sections 7.3--7.4. **Lemma 7.17 already proves the qualitative excluded half-space**; Proposition 7.16 already excludes boundary maximizers. The new explicit fixed-tilt collar is distinguished from those facts.
- Jian Ding and Nike Sun, *Capacity lower bound for the Ising perceptron*, [arXiv:1809.07742](https://arxiv.org/abs/1809.07742); Probability Theory and Related Fields 193 (2025), 627--715, [DOI](https://doi.org/10.1007/s00440-025-01364-x). Its numerical Condition 1.2 is a separate required input. This continuation does not rerun that condition's full certificate chain.
- Shuta Nakajima and Nike Sun, *Sharp threshold sequence and universality for Ising perceptron models*, [arXiv:2204.03469](https://arxiv.org/abs/2204.03469). The existing capacity claim uses this input to pass from the positive-probability lower bound and Gaussian disorder to the corresponding threshold statements. No broader universality assertion is newly proved here.

## Search conclusion

Targeted checks used the exact graph, rank-two kernel and skewness terms, FEI spectral coding/erasure and restriction terms, and Huang's exact condition and moment-body terminology. They distinguish existing results from what this continuation adds. They do **not** certify worldwide first priority or comprehensive absence of an equivalent theorem. The most important recovered antecedent during the work was Huang Lemma 7.17, and the package expressly credits it rather than counting a rederivation as a new theorem.
