# Substantial partial advance; the full problem remains open

Literature check: 14 November 2026, approximately 20:54–20:57 UTC+4. No full solution was found in the bounded search. The filename records a partial advance, not a claim that T085 is solved.

Ewan Cassidy, *Random permutations acting on k–tuples have near–optimal spectral gap for k=poly(n)*, [arXiv:2412.13941v3](https://arxiv.org/abs/2412.13941v3), revised 24 October 2025. Opened the arXiv page and the [v3 full text](https://arxiv.org/html/2412.13941v3). Theorem 1.3 proves near-optimal spectral bounds for the action of a fixed number r>1 of independent uniform permutations on ordered distinct k_n-tuples, whenever k_n <= n^alpha for fixed alpha<1/20. For r=2 the nontrivial adjacency bound is 2 sqrt(3)+o(1), hence normalized upper gap at least 1-sqrt(3)/2-o(1). This is a substantial improvement over fixed-length tuple actions. It does not reach the full regular representation. The abstract page explicitly flags a corrected exponent; use v3, not an older exponent.

Ramon van Handel, *The strong convergence phenomenon*, [arXiv:2507.00346v2](https://arxiv.org/abs/2507.00346v2), revised 11 February 2026. Opened the arXiv page and [full PDF](https://web.math.princeton.edu/~rvan/cdm260211.pdf). Theorem 5.7 gives the growing-tuple bound; section 6.2 describes the remaining Cayley problem and the sign representation obstruction.

Ramon van Handel, *Strong Convergence: A Short Survey*, Proceedings of the International Congress of Mathematicians 2026, pp. 145–165, [DOI:10.1137/25M1807113](https://epubs.siam.org/doi/full/10.1137/25M1807113). Opened full text. Theorem 2.5 states a consequence of Cassidy's work for any sequence of irreducible S_N representations with 1<D_N<=exp(N^(1/21)). Section 4.3 explicitly describes the full Cayley gap as open. Do not infer simultaneous control over every representation from a statement about each chosen sequence without checking the probability estimates.

Baseline checked directly: Harald A. Helfgott, Ákos Seress, Andrzej Zuk, *Random generators of the symmetric group: diameter, mixing time and spectral gap*, [arXiv:1311.6742](https://arxiv.org/abs/1311.6742). The abstract states the diameter and mixing estimates in the prompt and a nonconstant gap bound.

The parity caveat remains necessary: use the generated group; use an upper spectral gap, or lazify the walk, if bipartite pairs are allowed. None of the statements above supplies the missing uniform upper gap on the full generated group.
