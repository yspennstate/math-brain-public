# Matching solution preprint located

OpenAI, *Spontaneous magnetization in the quantum Heisenberg ferromagnet*, September 24, 2026, Theorem 1.1, printed page 3.

- [Publisher's repository, manuscript](https://github.com/openai/math/blob/main/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf).
- [Readable copy of the manuscript actually opened](https://mathcommunity.github.io/oai-math-revised/papers/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf).
- arXiv identifier: none located. This is a repository preprint; no arXiv number is asserted.

Theorem 1.1 asserts that, for every integer d ≥ 3 and every positive half-integer spin S, some finite β₀(d,S) exists such that every finite β ≥ β₀ admits a translation-invariant zero-field β-KMS state ω with ω(S₀ᶻ) ≥ S/4. Equation (1.1), printed page 2, is precisely the brief's nearest-neighbor Hamiltonian, with coupling one and each unordered edge counted once.

This matches T078's spontaneous-magnetization statement. Section 1.2 distinguishes this conclusion from a finite-volume, volume-averaged two-point criterion; that stronger/different formulation is not inferred here. The result predates the brief's November 2026 status check.

## Checks and limits

The author's [formalization scope note](https://raw.githubusercontent.com/openai/math/main/lean/docs/271.md) independently identifies the same scope. The [implementation theorem](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/Main.lean), `spontaneous_magnetization`, uses ℓ = 2S and bound ℓ/8 = S/4. In particular, S = 1/2 gives 1/8 by either parametrization. The [comparator statement](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/Heisenberg.lean) defines the ferromagnetic Hamiltonian explicitly. Its `sorry` is a statement placeholder; the implementation is separate.

The manuscript and theorem statement were inspected, not the complete proof or imported Lean dependencies. No Lean build was run. This records a directly matching published preprint claim, not independent certification of its correctness or peer review. Under the task's literature-stop rule, no new proof or computation was attempted.
