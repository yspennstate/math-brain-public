# Bounded literature check

Search conducted on 14 November 2026, approximately 22:12–22:16 +04. Queries combined diffusion scores, GD/SGD, minimax rates, polynomial width and feature learning. No verified unconditional resolution after the prompt's November checkpoint was found. This is a bounded search, not a completeness claim.

The main nearby reference is Yinbin Han, Meisam Razaviyayn and Renyuan Xu, [*Neural Network-Based Score Estimation in Diffusion Models: Optimization and Generalization*, arXiv:2401.15604v4](https://arxiv.org/abs/2401.15604v4), 18 April 2026. Its Theorem 3.13 states a weighted score-risk bound of order `N^(-2/(d+3))`, up to logarithms, for an early-stopped finite network, conditional on its assumptions. These include Assumption 3.8 on the sample Gram eigenvalue. This predates the supplied checkpoint and uses NTK coupling. The [full text](https://arxiv.org/html/2401.15604v4) and [PDF](https://arxiv.org/pdf/2401.15604v4) were opened. Equation (2.7) is the bias-free network considered here; Section 3 specifies Euclidean-ball clipping. PROOF.md audits that parameterization, rather than accepting a universal approximation assertion for it.

Other primary pages opened:

- Stanislas Strasman, Sobihan Surendran and Sylvain Le Corff, [*Non-asymptotic Convergence of Stochastic Gradient Descent in Score-based Generative Models*, arXiv:2607.04775v2](https://arxiv.org/abs/2607.04775v2), 7 October 2026. Its abstract describes nonconvex SGD analysis and an overparameterized ReLU NTK regime. The abstract was inspected; the HTML full-text endpoint failed.
- Yu-Han Wu, Pierre Marion, Gérard Biau and Claire Boyer, [*Taking a Big Step: Large Learning Rates in Denoising Score Matching Prevent Memorization*](https://proceedings.mlr.press/v291/wu25a.html), COLT 2025, PMLR 291:5718–5756. The result concerns a stability obstruction to memorization for one-dimensional two-layer networks; it does not supply the requested estimation rate.
- Sinho Chewi, Alkis Kalavasis, Anay Mehrotra and Omar Montasser, [*DDPM Score Matching and Distribution Learning (Extended Abstract)*](https://proceedings.mlr.press/v336/chewi26a.html), COLT 2026, PMLR 336:1434–1435. The abstract describes score-to-density reductions, without a general GD-trained-network guarantee.
- Arthur Stéphanovitch, Eddie Aamari and Clément Levrard, [*Generalization bounds for score-based generative models: a synthetic proof*, arXiv:2507.04794](https://arxiv.org/abs/2507.04794). Only the abstract page was opened successfully; no optimization theorem from this paper is used.

Search snippets were not treated as primary references. In particular, a snippet associated arXiv:2611.01658 with conditional diffusion, but the opened arXiv page had a different title. That candidate was discarded.
