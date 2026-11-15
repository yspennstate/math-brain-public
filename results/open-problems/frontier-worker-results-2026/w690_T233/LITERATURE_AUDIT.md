# T233 literature and source audit

Read HXP arXiv:2001.05992, Theorem 5.1 and Section 5.1 plus Appendix B in full at the proof bottlenecks. Also checked its orthogonal Theorem 4.1 for contrast and Du-Hu arXiv:1901.08572 Theorem 4.1. Du-Hu states eta<=d_out/(3L||X^T X||); HXP orthogonal theorem uses d_y/(2L||X||^2). This convention difference does not affect C001, which assumes eta<=1 for sufficiently large L.

Bottleneck map: fixed-vector chi-square first moment; coordinate-net dimensions and sqrt(number of coordinate groups); L^2 block union; polynomial factor in the deterministic perturbation series; polynomial prefactors in output, gradient and escape time. Strengthening only the first item cannot justify the unchanged neighborhood (C002). C001 instead retains all polynomial factors explicitly and pays a large constant in q/log L.

Primary sources:
- Hu, Xiao, Pennington, Provable Benefit of Orthogonal Initialization in Optimizing Deep Linear Networks: https://arxiv.org/pdf/2001.05992 (Section 5.1, Lemmas 5.2-5.5, Appendix B; orthogonal contrast Theorem 4.1).
- Du, Hu, Width Provably Matters in Optimization for Deep Linear Neural Networks: https://arxiv.org/pdf/1901.08572 (Theorem 4.1).
- Bassetti, Ladelli, Rotondo (2024), Proportional infinite-width infinite-depth limit for deep linear neural networks: https://arxiv.org/html/2411.15267v1 . Its abstract and section structure concern distributional prior/posterior limits, not a theorem on GD escape time in the width interval here.

Search queries included the exact HXP title with 2025, its arXiv identifier with later years, deep linear/Gaussian/width/convergence 2024-2026, and deep linear L/m gradient descent on arXiv. Results included recent residual, regularized/fixed-depth, Bayesian, and finite-step balanced-chain work. Two OpenReview candidate pages returned browser-verification challenges. No directly settling GD-width theorem was verified in this pass. This is a scoped negative search, NOT proof of global novelty or an exhaustive citation audit. C001 must remain proposed until the reviewer checks overlap with later literature and proof details.
