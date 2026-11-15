---
name: t104_uniform_kn_zero_is_empty_quotient_convention_not_equality_2026_11_12
description: "T104 (Alon): search returns H = 0 at equal weights on K_n - counterexample or third equality case? Neither: empty-quotient convention; M(K_n) = (4/n) I so H -> 4(n-2)/n nearby"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T18:22:29+02:00
  status: provisional
  evidence: "proof in 06_math_research/t104_alon_agent_2026_11_11/GAP_STATE_FORM.md; t104_kn_local.out n=5..8; push 113; one reader"
---

T104 (Alon's question, the H >= 0 form in 06_math_research/t104_alon_agent_2026_11_11/GAP_STATE_FORM.md).

The uniformly weighted K_n gives H = 0 in the search code. That value is the convention for an empty quotient
(every gap is zero, so the code returns -need, and need = 0 there). It is not an equality case. M(K_n) = (4/n) I on
V_[n-2,2], from the content sum of [n-2,2] (Schur), so H -> 4(n-2)/n along every approach. Measured at eps = 1e-3,
n = 5..8: 2.3976, 2.6640, 2.8543, 2.9970 against 2.4, 2.667, 2.857, 3.0.

Hint for the next reader: if a T104 search reports H about 0 at equal weights on every edge, it is this
convention, not a counterexample. The search's distance mask excludes only the star and the single edge, so add
K_n to the mask, or read gap12 (about 1e-16 there).

Side bound: H >= (n-2) lambda_min(M) - need anywhere, because s_beta is a positive average of Rayleigh quotients of
M. It settles only about 12 per cent of sampled graphs (the dense, near-uniform ones), so it is not the global
route.

Status: provisional, one reader, proof written in GAP_STATE_FORM.md and the measurement in t104_kn_local.out; it
would change if the empty-quotient convention were defined differently in the paper's statement. Row T104: not
solved.

