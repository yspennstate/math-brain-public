# Literature check: relevant advances, no settlement found

Search performed on 14 November 2026, approximately 21:28–21:35 Asia/Tbilisi.
The full T285 problem was not found to be settled. The following papers were
opened; this is a bounded literature check, not a claim of exhaustive coverage.

- Benjamin Aubin, Antoine Maillard, Jean Barbier, Florent Krzakala, Nicolas
  Macris, Lenka Zdeborová, *The committee machine: Computational to statistical
  gaps in learning a two-layers neural network*,
  [arXiv:1806.05451v3](https://arxiv.org/html/1806.05451v3), revised 29 February
  2024. Appendix D assumes committee symmetry for its large-K calculation.
  Appendix D.3 leaves the next-order channel term needed for instability at
  the K^2 scale for future work. The fixed-K replica result does not supply
  the requested general computational lower bound.

- Leonardo Defilippis, Florent Krzakala, Bruno Loureiro, Antoine Maillard,
  *A Noise Sensitivity Exponent Controls Large Statistical-to-Computational
  Gaps in Single- and Multi-Index Models*,
  [arXiv:2603.17896v1](https://arxiv.org/html/2603.17896v1), submitted 18 March
  2026. Theorem 4.2 treats the large-width AMP specialization scale for even
  activations in a separable sum with positive additive Gaussian noise.
  The non-even case is Result 4.3: Remark 4.4 and the limitations explicitly
  identify its symmetry assumption and non-rigorous expansion. Equation (5)
  observes the noisy sum, whereas T285 observes the sign of a sum of signs.
  Section 4 discusses that distinction. This is a relevant advance, but
  neither that theorem nor Result 4.3 settles the hard-sign question here.

- Alex Damian, Jason D. Lee, Joan Bruna, *The Generative Leap: Sharp Sample
  Complexity for Efficiently Learning Gaussian Multi-Index Models*,
  [arXiv:2506.05500](https://arxiv.org/html/2506.05500v1), submitted 5 June 2025.
  It gives low-degree lower bounds and matching estimation procedures in
  terms of the generative leap exponent for a fixed index dimension.
  The introduction explicitly assumes r=O_d(1). Its stated dimension
  exponents do not by themselves determine the K-dependent prefactor in T285.

- Emanuele Troiani, Yatin Dandi, Leonardo Defilippis, Lenka Zdeborová, Bruno
  Loureiro, Florent Krzakala, *Fundamental computational limits of weak
  learnability in high-dimensional multi-index models*,
  [arXiv:2405.15480](https://arxiv.org/abs/2405.15480), revised 2 April 2025.
  The abstract describes weak-learning limits for first-order iterative
  algorithms and hierarchical learning of directions. This is relevant to
  algorithm classes, but the abstract does not establish the growing-K
  hard-committee lower bound in T285.

Search terms included “committee machine low-degree”, “committee machine
specialization rigorous large K”, “committee machine rigorous specialization
2024 2025 2026”, and the titles of the multi-index papers above.

Work continues on the special case stated in PROOF.md.
