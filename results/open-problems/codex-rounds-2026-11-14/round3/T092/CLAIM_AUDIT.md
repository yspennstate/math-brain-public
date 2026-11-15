# External claim and the dependency reached

OpenAI, *A smooth three-torus diffeomorphism with simple Lebesgue
spectrum*, September 23, 2026. No arXiv identifier located.
The [citation README](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/README.md)
and [introductory theorem](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/01-introduction.tex)
were opened. Its claimed conclusion matches T092; validity remains
unverified here.

Primary sources inspected through the web tool on November 15, 2026
(the URLs use the mutable `main` branch):

| Source | Relevant location |
| --- | --- |
| [Comparator configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/ThreeTorus.json) | solution module and allowed axioms |
| [Comparator statement](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/ThreeTorus.lean) | `MainConclusion`, source lines 62–75 |
| [Main](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/Main.lean) | `simple_lebesgue_spectrum`, lines 16–45 |
| [SpectralTransport](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/SpectralTransport.lean) | `spectral_model_of_basis`, lines 225–257 |
| [PhysicalBasis](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/PhysicalBasis.lean) | `exists_physical_limit`, lines 144–177; `exists_physical_basis`, lines 280–305 |
| [DynamicsLimit](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/DynamicsLimit.lean) | `exists_stage_diagonal`, lines 284–314 |
| [SmoothLimits](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/SmoothLimits.lean) | smooth jet limit infrastructure |
| [Stages](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/Stages.lean) | `exists_one_stage`, lines 364–426; `exists_step`, lines 576–615 |
| [ControlledBlocks](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/ControlledBlocks.lean) | controlled signals and block iteration |
| [Manuscript completion](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/05-completion.tex) | final diagonal, lines 314–412 |

Line numbers above are one-based. No full transitive dependency audit,
axiom extraction, comparator run or compilation was performed. A proof
body is not a replay certificate.

The quantitative result in PROOF.md applies to the finite-stage output:
its orthonormal generator and approximation of an old invariant target
force polynomial support to grow as physical perturbations shrink.
Neither a contradiction nor a validation of finite-stage existence follows.
