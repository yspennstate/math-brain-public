# Lean source manifest

Fetched read-only from `https://raw.githubusercontent.com/openai/math/main/lean/` on 15 November 2026. These are source snapshots, not compiled objects. All local paths below are relative to this file.

The Main closure contains 51 OAI modules; the only external import reached is Mathlib. Four additional first-power reciprocal modules were opened. The graph has no cycle. Lexical scanning of these 55 solution modules found no `sorry`, `admit`, `axiom` or `unsafe`; Mathlib and compiler/tactic implementation bodies were not audited.

| Module | In Main closure | Direct imports |
| --- | --- | --- |
| [BlockEmbedding](lean/BlockEmbedding.lean) | yes | FourierPerturbation |
| [BlockFibers](lean/BlockFibers.lean) | yes | BlockEmbedding |
| [BlockLaws](lean/BlockLaws.lean) | yes | BlockFibers |
| [Classification](lean/Classification.lean) | yes | Irreducibility |
| [ConditionalFlow](lean/ConditionalFlow.lean) | yes | SpectralDecay |
| [ConditionalLaw](lean/ConditionalLaw.lean) | yes | MaskedResampling |
| [ConvolutionBounds](lean/ConvolutionBounds.lean) | yes | PermutationCharacters |
| [CosetBounds](lean/CosetBounds.lean) | yes | ProductProjectors |
| [Cyclic](lean/Cyclic.lean) | yes | Parity |
| [DegreeBounds](lean/DegreeBounds.lean) | yes | PartitionBounds |
| [EightBlocks](lean/EightBlocks.lean) | yes | BlockLaws |
| [EnergyDecay](lean/EnergyDecay.lean) | yes | NoiseEnergy |
| [ExceptionalShapes](lean/ExceptionalShapes.lean) | no | FirstMoment |
| [ExtensionBounds](lean/ExtensionBounds.lean) | yes | LinearExtensions |
| [FiniteExpectation](lean/FiniteExpectation.lean) | yes | ConditionalFlow |
| [FiniteLaw](lean/FiniteLaw.lean) | yes | Reachability |
| [FirstFourier](lean/FirstFourier.lean) | no | ExceptionalShapes, BlockEmbedding, Model |
| [FirstMain](lean/FirstMain.lean) | no | FirstFourier |
| [FirstMoment](lean/FirstMoment.lean) | no | ReciprocalDegrees |
| [FourierBounds](lean/FourierBounds.lean) | yes | CosetBounds |
| [FourierFamilies](lean/FourierFamilies.lean) | yes | Reynolds |
| [FourierPerturbation](lean/FourierPerturbation.lean) | yes | Trimming |
| [FreshCoins](lean/FreshCoins.lean) | yes | WalshFlow |
| [HalfHistories](lean/HalfHistories.lean) | yes | FreshCoins |
| [Irreducibility](lean/Irreducibility.lean) | yes | Polytabloids |
| [JointProjectors](lean/JointProjectors.lean) | yes | FourierFamilies |
| [LinearExtensions](lean/LinearExtensions.lean) | yes | Classification |
| [Main](lean/Main.lean) | yes | EightBlocks |
| [MarginalBounds](lean/MarginalBounds.lean) | yes | PrefixTests |
| [MarginalEnergy](lean/MarginalEnergy.lean) | yes | EnergyDecay |
| [MaskedResampling](lean/MaskedResampling.lean) | yes | MarginalEnergy |
| [MixingBounds](lean/MixingBounds.lean) | yes | FiniteLaw |
| [Model](lean/Model.lean) | yes | Mathlib |
| [NoiseEnergy](lean/NoiseEnergy.lean) | yes | HalfHistories |
| [PairAveraging](lean/PairAveraging.lean) | yes | Model |
| [Parity](lean/Parity.lean) | yes | MixingBounds |
| [PartitionBounds](lean/PartitionBounds.lean) | yes | ExtensionBounds |
| [PermutationCharacters](lean/PermutationCharacters.lean) | yes | VectorOrbits |
| [Polytabloids](lean/Polytabloids.lean) | yes | Specht |
| [PrefixTests](lean/PrefixTests.lean) | yes | TaggedCompletion |
| [ProductProjectors](lean/ProductProjectors.lean) | yes | JointProjectors |
| [Reachability](lean/Reachability.lean) | yes | MarginalBounds |
| [ReciprocalDegrees](lean/ReciprocalDegrees.lean) | yes | DegreeBounds |
| [Reynolds](lean/Reynolds.lean) | yes | ReciprocalDegrees |
| [Specht](lean/Specht.lean) | yes | Tableaux |
| [SpectralDecay](lean/SpectralDecay.lean) | yes | Support |
| [Support](lean/Support.lean) | yes | Walsh |
| [SymmetricFamilies](lean/SymmetricFamilies.lean) | yes | FourierBounds |
| [Tableaux](lean/Tableaux.lean) | yes | Cyclic |
| [TaggedCompletion](lean/TaggedCompletion.lean) | yes | TaggedDeviation |
| [TaggedDeviation](lean/TaggedDeviation.lean) | yes | ConditionalLaw |
| [Trimming](lean/Trimming.lean) | yes | ConvolutionBounds |
| [VectorOrbits](lean/VectorOrbits.lean) | yes | SymmetricFamilies |
| [Walsh](lean/Walsh.lean) | yes | PairAveraging |
| [WalshFlow](lean/WalshFlow.lean) | yes | FiniteExpectation |

