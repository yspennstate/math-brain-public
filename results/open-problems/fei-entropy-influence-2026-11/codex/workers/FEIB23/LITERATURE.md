# Literature checked 10 November 2026

Only opened primary sources are used for the external literature statements below. Search non-results are not evidence of a priority claim.

- Read-k DNFs: Arunachalam, Chakraborty, Koucký, Saurabh and de Wolf prove the min-entropy version for fixed k, rather than a general Shannon FEI theorem for read-k DNFs ([journal manuscript, Theorem 1.9](https://iuuk.mff.cuni.cz/~koucky/EPAC/papers/FEI-journal-version.pdf)).
- Unambiguous DNFs: Paraashar and Saurabh's 4 November 2026 preprint bounds Shannon Fourier entropy by the smaller one-sided average unambiguous parity-certificate cost, which by itself supplies no comparison of that cost to influence ([Theorem 4.3 and introduction](https://arxiv.org/html/2611.06451)).
- Linear DNFs: no Shannon FEI theorem for pairwise-at-most-one-overlap monotone DNFs was found in the opened primary papers; their statements on linear threshold functions concern a different class ([González, MacManus and Pereyra, introduction](https://arxiv.org/html/2606.00246v2), [Paraashar and Saurabh, prior work](https://arxiv.org/html/2611.06451)).
- Bounded-width DNFs: the opened papers do not state FEI for all bounded-width DNFs; the monotone bounded-width conclusion proved in PROOFS.md section A is narrower and no novelty claim is made ([Arunachalam et al.](https://iuuk.mff.cuni.cz/~koucky/EPAC/papers/FEI-journal-version.pdf), [Paraashar and Saurabh](https://arxiv.org/html/2611.06451)).

For comparison, read-k decision trees do have Shannon FEI bounds: [Wan, Wright and Wu](https://arxiv.org/abs/1312.3003), improved in k by [Shalev](https://arxiv.org/html/1806.03646). A read-k DNF need not be a read-k decision tree. [Lecomte and Tan](https://arxiv.org/abs/2109.04525) prove Fourier concentration for read-k DNFs; concentration is not automatically a Shannon entropy-influence bound.

The recovered math-store cards describe older unrefereed manuscripts on read-k and bounded-width monotone DNFs. They helped locate ideas, but are not substitutes for the external source checks. The brief's (LIN) and this worker's (MIX) add explicit coordinate-erasure estimates in sparse linear incidence systems; uniformity over size is part of those statements. A theorem for all of L would add an absolute Shannon FEI constant for unbounded term width and unbounded read. This report has not proved that theorem.

Opened sources also include [O'Donnell and Tan's composition paper](https://arxiv.org/abs/1304.1347) and [Han's entropy bound](https://link.springer.com/article/10.1007/s00493-024-00133-z). None of these sources was used to turn an upper bound with a divergent parameter into a claimed absolute constant.
