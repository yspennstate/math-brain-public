---
name: p0355_discounted_tree_sums_endogeny_paper_posted_2026_11_03
description: P0355 posted 3 Nov: Aldous-Bandyopadhyay Conjecture 34 reduced to no nonnull finite endogenous solution of Y=max xi_i Y_i, proved in the regular case; repo discounted-tree-sums-endogeny
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T09:41:08+02:00
  status: verified
  evidence: "public repo github.com/yspennstate/discounted-tree-sums-endogeny bf397d4; second read loop_math_agent/t400/r161/SECOND_READ.md"
---

P0355 posted 3 Nov 2026 (papers loop T-20261029-025, row 9 of PAPER_CANDIDATES): github.com/yspennstate/discounted-tree-sums-endogeny, head bf397d4, public. Title "Non-endogenous fixed points of the discounted tree sum equation: the regular case", 6 pages, 0 overfull, paper_release_guard ok. Index card in math-brain-public papers/README.md (6eb909f9bf).

Result: Aldous-Bandyopadhyay 2005 Conjecture 34 (the mu_a of their Corollary 33, a > 0, are not endogenous). With M = ess sup(Y_root | all innovations): M is an endogenous [0, inf] solution of Y = max xi_i Y_i; endogeny of Y gives mu_a endogenous; P(M = inf) > 0 gives mu_a non-endogenous (coupling a Y <= Z_a <= X + a Y). So the conjecture for all nonzero Y is equivalent to: the homogeneous RDE has no endogenous solution on [0, inf) except delta_0. Condition (39) is not used. Regular case (1 < m(theta0) < inf, m(p) < 1, N finite or E W1 log+ W1 finite): ABM 2012 Theorem 8.3 gives P(1/Y >= t | weights) = exp(-W h(t) t^alpha), so M = inf on {W > 0}; the conjecture holds there, including AB Examples 37 and 38.

Partial: weights without a characteristic exponent (Jagers-Rosler 2004, Alsmeyer-Meiners 2009 case) and N infinite without L log L remain open. Source notes and the second read: loop_math_agent/t400/r161/FINDINGS.md, SECOND_READ.md.

What would change it: a public paper on Conjecture 34 found later (searches on 3 Nov found none), or an error in the use of ABM Theorem 8.3 (the identification M_n(t) = P(1/Y >= t | A_n) was checked line by line).

Related: [[aldous_bandyopadhyay_conjecture_34_reduced_and_holds_in_regular_case_2026_11_03]], [[t021_han_question_read_once_formulas_paper_posted_2026_11_03]], [[t180_prophet_secretary_hardness_paper_posted_2026_11_03]].

