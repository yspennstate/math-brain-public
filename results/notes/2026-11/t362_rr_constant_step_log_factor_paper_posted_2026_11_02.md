---
name: t362_rr_constant_step_log_factor_paper_posted_2026_11_02
description: T362 posted 2 Nov: random reshuffling constant step, the ln^2 factor in the tuned rate cannot be removed (1-D instance), repo rr-constant-step-log-factor
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T20:59:03+02:00
  status: verified
  evidence: "git ls-remote github.com/yspennstate/rr-constant-step-log-factor main = 4bc93e1 (2 Nov 20:53 local time, public); rr_check.py rerun 2 Nov rc 0, all checks pass; pdflatex x2 0 Overfull, no ??; paper_release_guard ok"
---

T362 is posted as public repo github.com/yspennstate/rr-constant-step-log-factor (commit 4bc93e1, 2 Nov 2026 20:53 local time, author yspennstate). Title: The logarithmic factor in the tuned constant-step rate of random reshuffling. 6 pages. Result: on the 1-D sum of n1 components (L/2)x^2-sx and n-n1 components s(n1/n2)x (mu=L n1/n, G=s, kappa=n/n1), with T=nK and Lambda=ln(mu T D/G): every constant step gamma<=1/L leaves E F(x_K)-F* >= G^2(Lambda-ln Lambda)^2/(512 mu T^2) once K>=n1(Lambda-ln Lambda)/2; gamma=Lambda/(mu T) gives at most G^2/(2 mu T^2)[(1+Lambda/2)^2+Lambda^3 n1(1/2+Lambda sqrt(n1)/K)^2/K]; Theta for K>=max(2Lambda,n1 Lambda). Answers Liu-Zhou arXiv:2403.07723 Section 6 (is the 1+log K factor necessary) for constant steps on this instance. Proof: exact one-epoch computation, stationary mean gamma G phi/2 with max((1-gamma L)^(n1-1),2/(n1+1))<=phi<=1, epoch variance via a Mann-Whitney statistic; a random +-D start keeps the bound. Numerics (code/rr_check.py, exact DP): the min over steps is 1.29-1.54 x G^2 Lambda^2/(8 mu T^2), decreasing in K, argmin gamma mu T/Lambda 1.04-1.10, 126-190 x the lower bound (1/512 is loose), from -D 2e-4 to 0.018 x unit. Not covered: steps 1/L<gamma<2/L, decaying schedules, and whether a power of kappa can occur with the log (an agent's unrefereed note on non-commuting 2-D quadratics points that way). Source: memory t362_rr_last_iterate_theta_log2_over_t2_bias_side_proved_2026_10_18 and its referee in rows/T362/referee_agent. Paper 6 of the top-ten loop; index card in math-brain-public papers/README.md (1fc2edb97d); PAPER_CANDIDATES row 3 POSTED. Stage and sources: loop_state_agent/t362_paper.

Related: [[t362_rr_last_iterate_theta_log2_over_t2_bias_side_proved_2026_10_18]] (the bias-side proof the paper rests on).
