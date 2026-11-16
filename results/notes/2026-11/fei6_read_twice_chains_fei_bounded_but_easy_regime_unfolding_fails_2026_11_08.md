---
name: fei6_read_twice_chains_fei_bounded_but_easy_regime_unfolding_fails_2026_11_08
description: "Does FEI hold for overlapping read-twice formulas of any depth? For P4 chains yes, H and sum R <= 12.32 I (8 Nov), but via bounded expected queries (H~4.5, I~1.9), the easy regime; unfolding transfer fails by (3/2)^d"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T11:40:35+04:00
  status: verified
  evidence: "06_math_research/frontier/T021/fei6_agent_11_08 (8091e2e2f0); fei6_check.py"
---

Does FEI hold for overlapping read-twice formulas of any depth? For one explicit family, yes, but only weakly (8 Nov 11:40). Codex FEI6 built P4 chains, G_j = a_j b_j OR b_j c_j OR c_j a_{j-1}, alternating AND/OR, in open and closed versions (the closed one reads every input exactly twice), and proved H and sum R_i <= (160 ln2/9) I = 12.32 I nats at every depth. The route: H <= 2 ln2 E[queries], with E[queries] <= 20/3 because the chain short-circuits, and I >= Var >= 3/4 from a covariance induction.

I checked all three steps by hand and brute-forced d=1..6 myself. d=6 gives H/I = 2.359487 open and 2.354995 closed, matching the worker. The catch: H stays near 4.5 nats and I near 1.9 at every depth. The family therefore lives where FEI holds for a general reason (bounded expected decision depth plus variance bounded below), so the overlap is real but does no work.

The useful part is the obstruction. With shared variables, Fourier amplitudes collide before squaring (P = Q + J). On a tribes ladder the unfolded influence beats the true influence by (3/2)^d, so a proof through the occurrence-unfolding must bound the signed term J. Next: read-twice formulas whose expected decision depth grows.

Pushed 8091e2e2f0 to 06_math_research/frontier/T021/fei6_agent_11_08; the .bin truth tables stay local (check.py rebuilds them). FEI6 and OPEN-T226e both report that math recall could not open the math store database from inside the Codex sandbox; NTK4's math recall worked.

Related: [[fei5_summed_han_r_bounded_by_entropy_read_twice_15p72_2026_11_08]] gives the sum R <= H step used here. [[fei4_read_twice_dnf_fixed_coordinate_han_r_over_i_unbounded_2_ln2sq_w_2026_11_08]] is the fixed-coordinate negative.

