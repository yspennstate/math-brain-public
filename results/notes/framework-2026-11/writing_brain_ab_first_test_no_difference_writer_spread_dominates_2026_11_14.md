---
name: writing_brain_ab_first_test_no_difference_writer_spread_dominates_2026_11_14
description: "Does the writing brain make Codex prose better? First blind A/B (WBAB, 14 Nov): no - overall 8.83 vs 8.83, mean rank 2.5 vs 2.5, brain arm 1.77x the tokens; writer spread (W1 best, W2 worst) beats arm spread; scale near ceiling, so a weak null; next: more writers, pairwise judge, harder tasks"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T07:55:39+02:00
  status: provisional
  evidence: ""
---

First controlled test of the writing brain's practice method (WBAB, 14 Nov 2026, an agent). Four Codex writers (gpt-6.1-sol, high, normal speed) wrote the same three one-page tasks: a winter 1910 railway waiting room where one stranger wants the other's place by the stove; a village girl carried through three years at a city mill; an old ferryman telling a boy about the river in flood. W1 and W2 were told to use the writing brain (writing_recall.py, practice.py warmup, after_page.py); C1 and C2 had no brain. One blind Codex judge read all twelve pages with the letters reshuffled on every task (key kept in the scratchpad only, never on GitHub) and scored detail, dialogue, freshness, shape, fit and overall from 1 to 10, then ranked each task.

Result: no difference between the arms. Overall 8.83 against 8.83, mean rank 2.5 against 2.5. The dimension means differ by at most 0.33 (detail 9.00 vs 9.33 for the control, shape 9.17 vs 9.00 for the brain). The writers differ far more than the arms: W1 ranked 1, 2, 1 and was the best writer of the four; W2 ranked 3, 4, 4 and was the worst; C1 4, 1, 2; C2 2, 3, 3. The best page came from the brain arm on two of three tasks, both by W1, which is a writer effect, not a brain effect.

What the brain arm had: the practice method of 14 Nov morning (recall of hand cards and passages, the warm-up, the after-page check). It did NOT have the dictionary word walk (dictionary/word_walk.py, landed the same day) or the Lane M measures, so this is an ablation of the writing brain, not the strongest version.

Cost: the brain arm used 150,220 tokens (W1 80,302, W2 69,918), the control arm 84,919 (C1 28,040, C2 56,879): 1.77x the tokens for the same scores.

Room to fail was small, so this is a weak null, not evidence the brain does nothing. Fit scored 9 or 10 on every page and overall 8 to 10, so the scale had about two points of range; with six pages per arm and a page-to-page spread near 0.6, a true difference under about one point could not show. The next test should use more writers per arm (at least four), a pairwise judge (which of these two pages is better, both orders) instead of 1-10 scores, and harder tasks where the stock move is tempting (an explained feeling, a greeting opening, a tidy ending), since that is what the hand cards target.

Where things are: briefs under 12_cognitive_architecture/codex_local_1108/briefs/WBAB_W1, W2, C1, C2 and WBAB_J (JUDGEMENT.json, REPORT.md); the ledger row is an agent-20261114-wbab-writing-brain-ab in brain_improvement/IMPROVEMENT_LEDGER.jsonl. Related: [[writing_sessions_never_run_the_page_check_2026_11_14]], [[writing_brain_dictionary_and_word_walk_2026_11_14]], [[a_prediction_that_cannot_fail_is_not_evidence_2026_08_04]].

