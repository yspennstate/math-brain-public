---
name: p0245_n3_proved_holding_only_raises_cover_time_2026_11_10
description: "[PROVISIONAL] P0245 (Aldous-Fill OP 6.30) at n=3: proved E_pi C >= 3 for every reversible 3-state chain with holding; E-3 = N/D, holding monomials all positive, holding-free part (a+b)(a+c)(b+c)[4 sum a^3 - sum_sym a^2b - 6abc] >= 0, equality only K_3 no holding. Slug overclaims: holding can LOWER E_pi C (41/3000 at n=3); only the bound is proved"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T06:42:55+02:00
  status: provisional
  evidence: ""
---

Proof and sympy script: brain-repo/12_cognitive_architecture/codex_local_1108/briefs/OPEN3/independent_check_agent/HOLDING_STEP_2026_11_10.md and n3_sym_proof.py (10 Nov 2026, an agent). Status provisional: machine algebra, checked a second way (ordered substitution, all coefficients nonnegative) and against 400 Nelder-Mead starts (min exactly 1). Next question: whether the holding part stays coefficient-positive at n=4. Related: [[p0245_four_state_stationary_cover_time_bound_certified_2026_11_10]].

**Correction (10 Nov 06:5x, same author):** the slug says "holding only raises" - that is wrong. The proof bounds E_pi C - 3 >= 0; it does not say adding holding raises E_pi C (the denominator D contains h). Random test: 41 of 3,000 three-state chains have lower E_pi C with holding than without (n4_check_ctrl.py in briefs/OPEN3/independent_check_agent). The bound itself stands.
- **Independent audit (an agent, 10 Nov 19:3x):** separate exact solver, 300 Nelder-Mead starts, min exactly 3.000000000000 at K_3, none below; holding lowered E_pi C on 195/3000 (N(0,2) log-weights). Bound confirmed numerically. briefs/OPEN3/audit_agent/AUDIT_N3_2026_11_10.md
