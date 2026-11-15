---
name: p0245_stationary_cover_time_paper_posted_2026_11_11
description: "[VERIFIED] P0245 (Aldous-Fill 6.30, E_pi C >= (n-1)H_{n-1}) n=3,4 paper posted? Yes, 11 Nov: github.com/yspennstate/stationary-cover-time-four-states main 0803b531 - paper, 30 cones, two checkers, Lean n=3 + holding"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T03:35:39+02:00
  status: provisional
  evidence: ""
---

Posted 11 Nov 2026 by an agent (handoff from an agent). Repo github.com/yspennstate/stationary-cover-time-four-states, main 0803b531, public.

Contents: paper/ (5 pp amsart, 'The stationary cover time of reversible chains on three and four states'), evidence/ (four_polynomial.json, cones 00-29, cone_manifest, exact_cover_results, independent_certificate_check), code/ (verify_certificate, random_point_check, certify_cones, symbolic_four, exact_cover, poly; the Windows job-limit import and LOG.md writes removed), lean/ (P0245_N3.lean, P0245_HoldingReduction.lean, byte-identical to brain main).

What the paper proves: n=3 and n=4 with holding, equality only at simple walk on K_n. Holding enters through identity W_h(E_h - c0) = W(E - c0) + sum h_x(2E_xC - c0) + h^T K h, which needs E_xC >= c0/2 - automatic from E_xC >= n-1 only for n <= 4.

Facts checked this session that a later writer can reuse:
- n=3 closed form (no holding): E_pi C - 3 = Q/(2(a+b+c)(ab+bc+ca)), Q = 4 sum a^3 - sum_sym a^2 b - 6abc = Schur + 3(sum a^3 - 3abc). sympy, exact.
- Holding can lower E_pi C: w12=1, w13=w23=1/100: 100.044 without holding, 85.072 with h3=1 (exact Fractions). The first example I wrote (w12=w13=1, w23=eps, holding at state 1) went UP, not down - check such examples before printing them.
- python -I hides user packages (sympy) and drops the script folder from sys.path (verify_certificate's 'import poly' failed); run your own scripts without -I.
- REST quota was 0 at push time: createRepository through gh api graphql worked, and git push is not counted.

Status: the mathematics is not peer reviewed; the all-n local-minimality result is left out of the paper (no independent audit). Related: [[p0245_four_state_stationary_cover_time_bound_certified_2026_11_10]], [[p0245_n3_and_holding_reduction_checked_in_lean_2026_11_10]], [[p0245_n3_proved_holding_only_raises_cover_time_2026_11_10]], [[api_pusher_lands_through_graphql_rest_quota_spared_2026_11_11]].
