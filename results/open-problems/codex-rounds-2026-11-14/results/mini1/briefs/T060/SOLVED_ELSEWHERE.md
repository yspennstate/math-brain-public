# T060: substantial advances found

Checked November 14, 2026. The supplied status is outdated for the spin-1 periodic spectral gap. The full statement in the prompt has a remaining distinction: uniqueness among all infinite-volume algebraic ground states is stronger than the translation-invariant uniqueness established below. The stop condition applies because substantial advances were found.

## Papers opened

1. **OpenAI**, *The periodic spin-one Haldane gap*, September 24, 2026. [Original repository PDF](https://github.com/openai/math/blob/main/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/paper.pdf); [readable mirror actually opened](https://mathcommunity.github.io/oai-math-revised/papers/The-periodic-spin-one-Haldane-gap-September-24-2026/paper.pdf). No arXiv identifier was found for this manuscript.

   Theorem 1.1 treats precisely the pure bilinear spin-1 Hamiltonian with coupling one and periodic boundary conditions. It proves a unique ground state for every even length at least 60 and a positive uniform gap there; for every even length at least 2304 the lower bound is `(log 20)/784`. Corollary 6.1 addresses local excitations in subsequential periodic thermodynamic limits. This is a computer-assisted result, combining finite certificates with an analytic argument.

2. **Hal Tasaki**, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2](https://arxiv.org/abs/2610.34330v2), October 27, 2026. [Full text opened](https://arxiv.org/html/2610.34330v2).

   Theorem 2.1 proves exactly one translation-invariant algebraic ground state, which is pure and locally unique and gapped. Theorem 2.4 gives the same local limit for every selection of finite open-chain ground vectors, including both parities. The final discussion explicitly leaves uniqueness among arbitrary nontranslation-invariant ground states beyond the proof. The results use the earlier numerical inputs.

3. **Sirui Lu**, *Bridging Gaps with Tensor Networks: From the Haldane Gap and Beyond*, [arXiv:2611.11049v1](https://arxiv.org/abs/2611.11049v1), November 8, 2026. [Full PDF opened](https://arxiv.org/pdf/2611.11049).

   The paper reports exact-arithmetic verification of the finite inputs and strengthens the periodic bound to `Delta_L > 0.0729` for every even `L >= 36`; see Sec. SII.B. Sec. SIV/Table S6 distinguishes Lean proofs of the general criterion from the spin-1 finite trace premises that remain hypotheses. This is not a claim that the complete spin-1 computation has been checked unconditionally inside Lean.

An additional full text opened was **Hal Tasaki**, *OpenAI's proof of the Haldane gap in the S=1 antiferromagnetic Heisenberg chain: Continuous-time version*, October 18, revised October 19, 2026, [author-hosted PDF](https://haltasaki.github.io/writings/AI/OpenAI_Haldane_CT.pdf). No arXiv identifier was found for this exposition. It reconstructs the analytic argument and expressly does not independently check the numerical estimates.

## Limits of this finding

These statements document the papers' results; the finite certificates and Lean builds were not rerun here. No new proof is claimed. These papers suffice to trigger the requested stop rule without asserting the prompt's unrestricted uniqueness statement or the general assertion for every integer spin. No conclusion about all higher spins is drawn from these references.
