---
name: t104_hooks_exterior_powers_conjecture_f_reduction_2026_11_11
description: "T104 Alon 2/3 conjecture, second round (11 Nov): hook representations are exterior powers of the graph Laplacian (all hook pairs settled); the pair ([2,1^(n-2)],[2,2,1^(n-4)]) has conjectured constant (n-2)/(n-1), reduced to one covariance condition and to one quadratic inequality in the weights (no counterexample n = 5, 6; false at n = 4); where 2/3 comes from at n = 6, 7, 8; what failed"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T02:54:00+02:00
  status: provisional
  evidence: "06_math_research/t104_alon_agent_2026_11_11/HOOKS_AND_TWO_ROWS.md; commits 48cc5153, f8c2f4f1; dom_n8.tsv"
---

T104 (G. Alon, arXiv 2610.22151, Conjecture 1.5: lambda_min(G, tau) >= (2/3) lambda_min(G, sigma) for [n] != sigma
dominating tau; it implies Oliveira's conjecture). Second round, 11 Nov 2026, one author, not audited. Files:
06_math_research/t104_alon_agent_2026_11_11/ (HOOKS_AND_TWO_ROWS.md is the note; commits 48cc5153, f8c2f4f1).

What is proved (short proofs in the note, checked numerically):
- Lemma H. L(G, [n-k, 1^k]) is the derivation of the graph Laplacian on the k-th exterior power of the sum-zero
  space, so its eigenvalues are the sums of k distinct Laplacian eigenvalues. Every pair of hooks satisfies the
  conjecture with ratio >= k/j. The paper does not use this.
- Conjugation. lambda_min(G, nu') = 2W - lambda_max(G, nu). So tau = [2, 1^(n-2)] turns the conjecture into an upper
  bound on the largest Laplacian eigenvalue by the top of the spectrum in another representation.
- Model. V_[n-2,2] = symmetric matrices with zero diagonal and zero row sums; on it
  <T, L T> = 2 tr(L_G T^2) - 4 sum w_ij T_ij^2.
- Lemma U. For a disjoint union, lambda_min(G1 + G2, nu) = min over Littlewood-Richardson pairs of
  lambda_min(G1, mu) + lambda_min(G2, lam). The value 2/3 that the search finds at n = 6, 7, 8 (pairs (2211,222),
  (3211,322), (4211,422), (22211,2222)) is the n = 4 pair (211, 22) on K_{1,3}, lifted through horizontal strips.

What is conjectured:
- Conjecture F. lambda_max(L_G) <= (2W + (n-2) lambda_max(G, [n-2,2]))/(n-1), i.e. the pair
  ([2,1^(n-2)], [2,2,1^(n-4)]) has constant (n-2)/(n-1), equality on the star. n = 4 is the earlier Theorem 3.
  The search gives 3/4, 4/5, 5/6 (n = 7 table), 6/7 at n = 5, 6, 7, 8.
- Reduction R. With T = P(x y^t + y x^t), y of covariance C on {1, x}^perp, F follows if for every unit x some C makes
  (n-1) slack_ij = (2 - d^2) + (2 n kappa/(n-2))((n-1) d^2 - 2) - 2 n g_ij - (n-2)(2 d^2 - 1) c_ij >= 0 for all pairs
  (kappa = E sum x_k^2 y_k^2, g_ij = E (x_i y_i - x_j y_j)^2, c_ij = E (y_i - y_j)^2, d = x_i - x_j). An optimiser
  finds such a C at every x tried for n = 4, 5, 6; for three-valued x = (a, b, c, ..., c) a one-parameter C always
  exists (n = 5, 6, 8, 12, 30).

What failed (do not retry as is):
- y uniform on {1, x}^perp: exact at the star and edge vectors, negative between them, also in weighted form.
- C = Q diag(omega(x_k)) Q with omega = exp(-b n x^2), (1 + b n x^2)^(-2): best leaves -0.0095 (n = 4), -0.0006 (n = 5).
- Test vectors from the graph in the weighted form (y = Fiedler vector, y = second-top eigenvector, uniform,
  C proportional to lambda_max - L): each is negative somewhere; the last one at n = 4 near two disjoint heavy edges.
  A bug to avoid: for a disconnected graph the eigensolver's first vector is not the constant vector; subtract a
  multiple of the all-ones matrix before taking the basis of {1, x}^perp.

Search minima of the ratio: n = 4: 2/3; 5: 3/4; 6: 2/3; 7: 2/3; 8: 2/3 (194 pairs). Nothing below 2/3.
Next: a closed-form C(x) (or a graph-dependent test vector) that proves Conjecture F; an independent audit of
N4_PROOF.md and of Lemma H / Lemma U before any of this is called a result.

