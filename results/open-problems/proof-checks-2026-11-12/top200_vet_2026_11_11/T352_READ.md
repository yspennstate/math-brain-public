T352, privacy of hidden-state noisy SGD for nonconvex losses: what the cited papers prove (read 11 Nov 2026)

Row verdict in top200_review_2026_11_10/VERDICTS.tsv: REMOVE_SOLVED_BY_OTHERS, citing arXiv 2401.10371v7, Theorem 3.3.

Theorem 3.3 of 2401.10371v7 (read in the HTML version, lit_t352/p.txt). For projected noisy gradient descent
(full batch, the paper's PNGD) on a bounded closed convex set of radius R, with each loss L-smooth and
M-Lipschitz and no convexity, the learning process is (alpha, eps)-Renyi DP at iteration T with

    eps <= (2 alpha eta S^2 M^2 / (sigma^2 n^2)) sum_{t<T} prod_{t'=t}^{T-1} (1 + eta sigma^2 / C_{t',1})^{-1},

where the log-Sobolev constants C_{t,1} stay below Cbar = 6(4(R + eta M)^2 + eta sigma^2) exp(4(R + eta M)^2/(eta sigma^2)).
Since Cbar does not depend on t, the sum is bounded in T: the privacy loss plateaus at order
alpha eta S^2 M^2/(sigma^2 n^2 c) with c in (0,1) independent of T. This is a hidden-state bound without convexity.
It is for full-batch updates. For minibatches the paper says only that the analysis of its reference [18] "can be
combined" with the log-Sobolev tracking; no theorem is stated. The authors call the nonconvex constant not tight
because of its exponential dependence on the parameters.

Minibatch noisy SGD (abstracts read, arxiv_t352_followup.xml, t352_followup_abs.out).
- Chien and Li, arXiv 2410.01068v2: convergent Renyi DP bound for hidden-state Noisy-SGD over a bounded domain for
  non-convex non-smooth losses with Hoelder continuous gradient, answering the questions of Ye-Shokri and
  Altschuler-Talwar.
- Asoodeh and Diaz, arXiv 2305.09903v1: the privacy loss of projected DP-SGD (clipped gradients) converges
  exponentially fast without convexity or smoothness; also a regularized unprojected variant.

Verdict. The removal stands, but the citation should be 2410.01068 (and 2305.09903), not Theorem 3.3 of the
unlearning paper alone, which covers full-batch updates. What is not covered by any of the three, as far as the
abstracts and Theorem 3.3 show: an unbounded domain with no projection, clipping or regularization, and constants
that are not exponential in R^2/(eta sigma^2). If the list wants a successor row, that is it.
