# Short literature check, 14 November 2026

The web search lasted less than ten minutes. Only primary pages actually
opened are listed. This is a scoped search, not a proof of absence.

- Lénaïc Chizat, *Mean-Field Langevin Dynamics: Exponential Convergence and
  Annealing*, [arXiv:2202.01009v3](https://arxiv.org/html/2202.01009v3).
  Section 5.1, Proposition 5.1, requires bounded full features for its
  displayed LSI estimates. The following limitations discussion explains
  the exclusion of the vanilla unbounded neuron. The paper distinguishes
  temperature from its quadratic regularization coefficient.

- Alireza Mousavi-Hosseini, Denny Wu, Murat A. Erdogdu, *Learning Multi-Index
  Models with Neural Networks via Mean-Field Langevin Dynamics*,
  [arXiv:2408.07254v2](https://arxiv.org/html/2408.07254v2), ICLR 2025.
  Section 4 gives polynomial guarantees under compact-manifold curvature
  and temperature conditions. Its discussion after Proposition 8 explicitly
  excludes a fixed number of indices from the stated diversity condition.
  This does not settle the present fixed-neuron Gaussian-input question.

- Zong Shang, Tomoya Wakayama, Guillaume Lecué, Taiji Suzuki, *The Geometry
  of Statistical Feature Learning in Mean-Field Langevin Dynamics*,
  [arXiv:2606.31429v2](https://arxiv.org/html/2606.31429v2).
  This studies spherical stationary geometry and statistical recovery.
  Appendix E, Proposition 11, retains an exponential inverse-temperature
  factor in its convergence estimate. The discussion's phrase about an
  exponential time guarantee is not used here as a risk-time lower bound.

- Margalit Glasgow, Denny Wu, Joan Bruna, *Mean-field analysis of
  polynomial-width two-layer neural network beyond finite time horizon*,
  [COLT 2025 primary page](https://proceedings.mlr.press/v291/glasgow25a.html).
  Its polynomial-time single-index results concern projected gradient
  dynamics. They do not directly supply a low-temperature MFLD theorem.
  Only the primary abstract page was opened for this item.

- Guillaume Wang, Lénaïc Chizat, *Local convergence of mean-field Langevin
  dynamics: from gradient flows to linearly monotone games*,
  [arXiv:2602.11999](https://arxiv.org/abs/2602.11999).
  The opened abstract establishes local convergence under a stationary
  Poincare inequality, rather than the global risk-time guarantee asked here.

- Jing An, Lihan Wang, *Local Algebraic Stability of Wasserstein Gradient
  Descent-Ascent and Mean Field Langevin Dynamics without Spectral Gap*,
  [arXiv:2610.35528](https://arxiv.org/abs/2610.35528).
  The opened abstract concerns local stability without a spectral gap,
  including polynomial-tailed equilibria. It does not settle the Gaussian
  prior regression problem in this task.

No whole-problem resolution was found. No SOLVED_ELSEWHERE.md is asserted.
