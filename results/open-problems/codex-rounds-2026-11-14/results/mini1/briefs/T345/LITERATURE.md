# Literature check, 14 November 2026

The search began at about 21:31 and ended at 21:34 Asia/Tbilisi, under the
ten-minute limit. No source opened in this check settles the whole problem.
No verified result published after the prompt's November 2026 status date was
found. This is a bounded search, not a proof that none exists.

Papers actually opened:

1. Sébastien Bubeck, Eric Price, Ilya Razenshteyn,
   [Adversarial examples from computational constraints](https://arxiv.org/abs/1805.10204),
   arXiv:1805.10204 (2018). Source named in the question.
2. Sébastien Bubeck, Yin Tat Lee, Eric Price, Ilya Razenshteyn,
   [Adversarial Examples from Cryptographic Pseudo-Random Generators](https://arxiv.org/abs/1811.06418),
   arXiv:1811.06418 (2018). Source named in the question.
3. Chen Dan, Yuting Wei, Pradeep Ravikumar,
   [Sharp Statistical Guarantees for Adversarially Robust Gaussian Classification](https://arxiv.org/abs/2006.16384),
   arXiv:2006.16384 (2020);
   [opened proceedings PDF](https://proceedings.mlr.press/v119/dan20b/dan20b.pdf).
   Their model is balanced, with conditional laws N(y mu, Sigma), hence a shared
   covariance. They give a convex-program learner and matching statistical rates
   in their stated signal regime. Thus important shared-covariance Gaussian
   cases already have an efficient solution. The model does not allow two
   independently varying spherical variances.
4. Arjun Nitin Bhagoji, Daniel Cullina, Prateek Mittal,
   [Lower Bounds on Adversarial Robustness from Optimal Transport](https://arxiv.org/abs/1909.12272),
   arXiv:1909.12272 (2019). The abstract gives a transport characterization and
   matching Gaussian bounds. Dan–Wei–Ravikumar restate the shared-covariance
   Gaussian classifier as their Theorem 2.1.
5. Elvis Dohmatob,
   [Classifier-independent Lower-Bounds for Adversarial Robustness](https://arxiv.org/abs/2006.09989),
   arXiv:2006.09989 (2020);
   [opened full HTML](https://arxiv.org/html/2006.09989v6).
   Relates robust risk to transport and describes finite matching methods.
   The use of a bipartite graph in this session is therefore established
   methodology, not a claimed new graph reduction.
6. Muni Sreenivas Pydi, Varun Jog,
   [Adversarial Risk via Optimal Transport and Optimal Couplings](https://arxiv.org/abs/1912.02794),
   arXiv:1912.02794 (2019; revised 2020). The opened abstract states a transport
   characterization and explicit couplings/classifiers for univariate laws,
   including Gaussian laws. It does not by itself establish the high-dimensional
   unequal-spherical-variance learning theorem proved here.
7. Hancheng Min, Rene Vidal,
   [Gradient Flow Provably Learns Robust Classifiers for Orthonormal GMMs](https://proceedings.mlr.press/v267/min25c.html)
   (ICML 2025). Opened the proceedings page, not the full paper: its PDF link at
   the initially guessed PMLR path failed. The abstract concerns isotropic
   mixtures with orthonormal centers and a gradient-flow guarantee. No broader
   claim about unequal spherical variances is inferred from that abstract.

Searches included computational hardness with natural distributions, Gaussian
robust classification in 2025–2026, unequal Gaussian variances, spherical
Gaussians, rotational symmetry, quotient spaces, and optimal transport.

The session's mathematical piece is a self-contained reduction and approximation
theorem for unequal spherical Gaussians under Euclidean attacks. It is not a
claim that no comparable theorem has ever appeared elsewhere.
