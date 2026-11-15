---
name: writing_brain_ab3_third_null_word_walk_raises_repetition_2026_11_14
description: "Does the writing brain improve Codex prose? Third blind A/B (WBAB3, 14 Nov): no. Brain without word walk 6.40 vs no-brain 5.73 of 12 (p=0.69); full brain 7.38, worse; 1.4-1.8x tokens"
metadata:
  type: project
  created: 2026-11-14
  status: provisional
  evidence: "12_cognitive_architecture/brain_improvement/agent_run/WBAB3_RESULT.md"
---

Third writing-brain A/B (WBAB3, 14 Nov 2026, an agent), rules fixed before any page (WBAB3_PREREG.md, bb74cf84).
Twelve Codex writers (gpt-6.1-sol high, normal speed), four per arm, three fiction tasks, four blind Codex judges each
ranking all twelve pages of a task (1 best), key kept in the session scratchpad only.

- B- (brain without word_walk, after_page prints a stem-repeat count and the writer revises once above 4.0) vs no brain:
  mean rank 6.40 vs 5.73, one-sided p=0.69. No win.
- B (the WBAB2 brain, word walk included) vs no brain: 7.38 vs 5.73, worse (two-sided about 0.10).
- Stem repetition (stems in 3+ paragraphs per 100 content words): C 3.59, B 4.76, B- 2.46. The word walk
  does push repetition up, and the stem check pulls it down, but across the 36 pages the measure did not track rank
  (Spearman -0.005). The WBAB2 after-the-fact correlation did not replicate.
- Room to fail: per-page mean ranks across the four judges have sd 2.74, so a one-sided p<0.10 with 12 pages per arm needed about a 1.4-place gap (of 12) in the arm's favour; B- came out 0.67 places the other way. Neither ceiling nor floor: the test could have shown a win.
- Four judges agree better than two did: median Spearman 0.32 / 0.67 / 0.39 by task.
- Tokens: C 300,260, B 423,618, B- 533,618, judges 206,241.

How to use this: three tests in a row show no gain from the writing brain as Codex uses it, and the word walk version
leans worse. Do not claim the writing brain improves prose. Changing the stem count is not the lever: the judges rank on
something it does not measure. A fourth test should change what the brain serves (one specific scar or exemplar
passage per page, read before drafting) rather than add more steps, and keep pre-registration and four judges.
Earlier: [[writing_brain_ab2_brain_pages_ranked_below_controls_judges_disagree_2026_11_14]],
[[writing_brain_ab_first_test_no_difference_writer_spread_dominates_2026_11_14]]; on nulls:
[[a_prediction_that_cannot_fail_is_not_evidence_2026_08_04]]. Ledger id an agent-20261114-wbab3-writing-brain-third.
