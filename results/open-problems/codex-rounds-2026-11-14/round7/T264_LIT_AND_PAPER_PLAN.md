# T264 after round 7: literature check and paper plan (an agent, 15 Nov 2026)

Web search, 15 Nov (two queries on multivariate minimum-norm ReLU interpolation, tempered or catastrophic, expected risk):
- arXiv:2307.15396 (N. Joshi, G. Vardi, N. Srebro, ICLR 2024): univariate two-layer min-norm ReLU; tempered for L_p,
  1 <= p < 2, catastrophic for p >= 2 and in expectation over the training set. Univariate only.
- arXiv:2305.15141 (G. Kornowski, G. Yehudai, O. Shamir): tempered to benign with input dimension; classification by
  max-margin, a different question.
- arXiv:2602.00825 (Karhadkar, Sietsema, Needell, Montufar): harmful overfitting for near-minimal W^{k,p} interpolants;
  Sobolev norm, not the ReLU parameter norm (already in round6/T264/LIT_CHECK.md).
No result found giving the fixed-n tail exponent of the risk for multivariate min-norm ReLU interpolation.

Paper (candidate, rounds 5, 6, 7):
Title idea: "The risk tail of minimum-norm ReLU interpolation on the sphere".
Main theorem: for iid uniform inputs on S^(d-1), Rademacher labels, every fixed n >= 3, every measurable selection of
minima, P(R_n > t) is bounded above and below by constant multiples of t^{-(d-1)/2}; hence E R_n^r < infinity iff
r < (d-1)/2, and the mean risk is infinite in d = 2, 3 and finite in d >= 4. Remark: antipodal extra points (round 6)
keep the collision-limit risk bounded, so the one-hemisphere event is what drives the tail.
Credit in the introduction and the AI declaration (owner order 14 Nov 23:34): Joshi, Vardi and Srebro found the
univariate catastrophic-in-expectation phenomenon and the close-pair spike mechanism; Ongie, Willett, Soudry and Srebro
(arXiv:1910.01635) and Savarese, Evron, Soudry, Srebro (univariate) for the function-space view of the norm; Mallinar
et al. for the tempered taxonomy. New here: the multivariate tail exponent, both directions, at fixed n.
Before posting: C01-C26, lintgate exit 0, referees from the allowed list, authors checked against each arXiv page.
