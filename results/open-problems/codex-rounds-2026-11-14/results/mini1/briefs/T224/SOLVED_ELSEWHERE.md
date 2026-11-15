# Partial coverage in the source: the endpoint c=2

This does not settle the whole T224 question.

Margalit Glasgow and Joan Bruna, *Uniform-in-Time Weak Propagation-of-Chaos in Shallow Neural Networks*, [arXiv:2605.22010v3](https://arxiv.org/abs/2605.22010), revised 11 November 2026.

[Remark 6](https://arxiv.org/html/2605.22010v3#S4.SS1) treats the critical exponent c=2 under its stated normalized loss envelope and burn-in conditions. It gives a uniform-in-time, high-probability output/kernel-mean squared-error bound with width exponent 1/(3+5C_reg), up to logarithms and the displayed dimension/burn-in factors. Its proof truncates the square-root-loss integral on a deterministic interval.

This is endpoint coverage, not a sharp exponent theorem and not a result for 0<c<2. Section 6 still identifies slower decay as an open direction. The present session therefore continued on that remaining range; its contribution is in PROOF.md.

The comparison reference was also opened: Song Mei, Andrea Montanari, and Phan-Minh Nguyen, *A Mean Field View of the Landscape of Two-Layers Neural Networks*, [arXiv:1804.06561](https://arxiv.org/abs/1804.06561). No later theorem resolving the full question was found in the bounded literature search.
