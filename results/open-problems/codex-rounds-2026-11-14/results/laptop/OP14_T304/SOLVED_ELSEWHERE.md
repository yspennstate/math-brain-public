# Substantial updates; T304 is not wholly settled

The literature check did not locate a matching answer for all dimensions, condition numbers, and accuracies. Continue with the reduction in PROOF.md.

- **Wei Guo, Bo Yuan, Ye He, Jiaming Liang, Molei Tao, Yongxin Chen**, *Subpolynomial-Query Proximal Sampling Beyond Log-Concavity*, [arXiv:2611.03442v1](https://arxiv.org/abs/2611.03442), submitted 2 November 2026. Theorem 3 in the opened HTML states a gradient-query bound `C_nu*kappa*(d+kappa+epsilon^(-1)+G0)^nu` for every fixed `nu>0`, under C^2 smoothness and a log-Sobolev inequality. This includes strongly convex targets. This updates the polynomial dimension benchmarks in the brief, but does not determine a sharp rate.
- **Huanjian Zhou, Taiji Suzuki**, *Towards the Query Complexity of Sampling under Strong Log-Concavity and Log-Sobolev Inequalities*, [arXiv:2611.05813v1](https://arxiv.org/abs/2611.05813), submitted 4 November 2026. Opened abstract and full HTML, including Theorems 4 and 8: a superpolylogarithmic lower bound at condition number 2 and constant TV accuracy, including a warm-start version. This is consistent with subpolynomial upper bounds.
- **Evan Dogariu**, *Sharp Lower Bounds for Parallel Log-Concave Sampling*, [arXiv:2611.15849](https://arxiv.org/abs/2611.15849), submitted 11 November 2026. The opened arXiv page concerns parallel rounds with polynomial batch width, rather than the unresolved sequential query count. Its abstract states a sharp logarithmic depth at fixed conditioning. This does not settle T304.

An additional lead was OpenAI, *Subpolynomial query complexity for well-conditioned log-concave sampling*, September 26, 2026, with no arXiv id found. Its [primary README](https://github.com/openai/math/blob/main/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/README.md) was opened. The PDF fetch failed; no independent proof audit of that work is claimed. The corollary in PROOF.md uses the explicitly opened theorem of Guo et al.

These are preprint statements. No claim of peer review or independent verification of their complete proofs is made.
