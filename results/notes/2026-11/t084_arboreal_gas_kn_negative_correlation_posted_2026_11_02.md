---
name: t084_arboreal_gas_kn_negative_correlation_posted_2026_11_02
description: [VERIFIED] T084 posted 2 Nov: arboreal gas on K_n, any two distinct edges strictly negatively correlated for every n and t>0; repo kn-forest-negative-correlation
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T07:58:39+02:00
  status: provisional
  evidence: ""
---

T084 is posted (2 Nov 2026): github.com/yspennstate/kn-forest-negative-correlation, public, byline the author.

Theorem: for the arboreal gas on K_n (acyclic edge sets weighted t^|F|), every two distinct edges are strictly negatively correlated, for every n and every t > 0. Gupta (arXiv:2609.26134) did t = 1. Huang (arXiv:2311.00965) did partial ranges. Ciceksiz-Ravichandran (arXiv:2610.00549) did large fugacity and the q<1 random-cluster model with weight >= 1. Tang-Zhang (arXiv:2609.11578) did q<1 on large regular graphs of diverging degree. None of them covers all n and all t on K_n.

Proof: edges at a common vertex follow from the real roots of the vertex degree polynomial, a rank-one perturbation of a Hermite Jacobi matrix. Disjoint edges go through the Riccati equation 2t^2 rho' = t - 2nt^2 + B rho - n(n-1) t rho^2, the boundary product g_- g_+ = -4t^4 J/h and a barrier over three intervals. n = 4, 5, 6 are checked directly.

Checks: a full read, a sympy identity check (code/agent_run.py), a brute force over n = 3..7 (code/brute_kn.py) and an exact FLINT certificate (code/kn_exact_certificate.py, which now writes to ./output). The paper passes the 2 Nov release rule: 0 Overfull lines, no ??, the four back sections, and paper_release_guard rc 0.

Records: a POSTED row in PAPER_CANDIDATES.md (rank 5) and a card in the math-brain-public papers/README.md (commit 5d357db58f). The working copy is in loop_state_agent/t084.


Related: [[t084_kmn_forests_negatively_correlated_every_fugacity_2026_10_15]] - the K_m,n result before the K_n paper

Related (linked 3 Nov by an agent, W22): the earlier T084 results on K_{m,n} forests, [[t084_kmn_forests_negatively_correlated_all_pairs_t_ge_2_199_2026_10_15]] and [[t084_kmn_forests_negatively_correlated_every_fugacity_2026_10_15]].
