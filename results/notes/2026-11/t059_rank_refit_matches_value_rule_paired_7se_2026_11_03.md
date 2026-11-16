---
name: t059_rank_refit_matches_value_rule_paired_7se_2026_11_03
description: [VERIFIED] T059 Robbins n=5: best memoryless exactly 1.586131; m059a rank rule was local, refit 1.57359 (paired -0.00044, 7.5 se) = m059b value rule, so no running-min gain shown
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T04:34:57+04:00
  status: provisional
  evidence: "06_math_research/frontier/rows/T059/reviews_agent/REVIEW_T059_ADDENDUM.md"
---

T059 (Robbins' problem, n = 5), checked 3 Nov 04:34 by an agent.

The best memoryless threshold rule is exactly 1.586131, at t = 0.23851 0.30208 0.39181 0.53582, from a closed form that sums over stopping times. m059a's thresholds score exactly 1.586330.

m059a's 10-parameter rank-aware rule, 1.57403, was a local fit. A refit from its own start scores 1.57359. The paired difference on 2e7 common sequences is -0.000437 +- 0.000058, or 7.5 se. That equals m059b's 20-parameter running-minimum rule (1.57360), so the running minimum shows no gain yet.

Lesson: compare two rules PAIRED on common random numbers. An unpaired 1e7 score of the refit read 1.57302 +- 0.00028, 2 se lucky.

Files: 06_math_research/frontier/rows/T059/reviews_agent/ (REVIEW_T059_RULES.md, REVIEW_T059_ADDENDUM.md).


Related: [[t059_robbins_n5_rank_rule_1p5740_c002_not_refuted_2026_11_02]] - the 1.5740 rank rule there is the local fit this refit beats.
