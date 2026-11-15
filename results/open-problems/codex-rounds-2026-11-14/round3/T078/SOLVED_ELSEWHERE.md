# Existing solution claim and verification status

OpenAI, *Spontaneous magnetization in the quantum Heisenberg ferromagnet*, September 24, 2026, Theorem 1.1.

- [Manuscript actually opened](https://mathcommunity.github.io/oai-math-revised/papers/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf), 54 pages.
- [Publisher's manuscript location](https://github.com/openai/math/blob/main/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf).
- arXiv identifier: not established in the inspected sources.

The theorem claims a translation-invariant zero-field beta-KMS state with one-site z-magnetization at least S/4 for each d>=3, each positive half-integer S, and every sufficiently large finite beta. Its Hamiltonian uses the ferromagnetic sign, coupling one, and unordered nearest-neighbor edges counted once. This matches the brief's spontaneous-magnetization statement. It does not itself assert the separate finite-volume two-point criterion.

Beyond the earlier report, the actual [October 26 comparator log](https://github.com/mathcommunity/oai-math-revised/blob/main/checks/comparator-2026-10-26/logs/Heisenberg.log) was opened and read through its final lines. It reports that the Lean default kernel accepted the solution against the comparator. This was not reproduced locally. Source inspection confirms the same dimension, spin, equilibrium and magnetization parameters in the [implementation](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/Main.lean) and the [comparator](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/Heisenberg.lean).

The full analytical argument and formal dependency chain remain unaudited here. This file records a matching solution claim with additional reported formal-check evidence, not an independently certified resolution. Because the earlier report explicitly requested a proof audit, the session checked and sharpened one finite-volume selection step; see PROOF.md and REPORT.md.
