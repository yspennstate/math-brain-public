---
name: writing_recurring_business_tracks_worse_judge_rank_2026_11_14
description: "Brain pages ranked below controls - why? On the 24 WBAB2 pages, words back in 3+ paragraphs (per 100) track worse judge rank (rho +0.46, p 0.015, a hypothesis: picked from 3); brain 4.4 vs control 3.3; WBAB3 pre-registers it; creative_draw.py page lists them"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T12:52:09+02:00
  status: provisional
  evidence: ""
---

On the 24 pages of the second blind writing-brain test (WBAB2, 14 Nov 2026, two Codex judges ranking 8 pages per task), the share of content stems that appear in three or more paragraphs, per 100 content words, tracked a worse mean judge rank: Spearman +0.46 over all 24, positive in each task (+0.21, +0.40, +0.64), permutation p 0.015 (0.008 shuffling within task). Three measures were tried against a rule set before the run (rho >= 0.30 and positive in 2 of 3 tasks); the echo-ending measure (last fifth reusing earlier words, rho +0.27) and the plain repeat rate (+0.14) failed. It is not paragraph count: paragraphs run slightly the other way (rho -0.14 with rank). Brain pages carried more of it than controls, 4.4 against 3.3 per 100, which fits the judges' complaint about the brain pages: "physical business repeated without a new consequence".

What was done with it: `writing_brain/creative/creative_draw.py page` prints RECURRING BUSINESS (the words, how many paragraphs each is in, the rate, flagged above 4.0), so a writer sees which objects and gestures keep coming back. Selftest has three checks for it.

Size of the doubt: one test, 24 pages, two judges who agree at about 0.2, three measures tried (about 0.045 after a Bonferroni factor). What would change it: a third test where writers act on the list and the gap to controls closes, or a test where the rate does not track rank. Test script echo_test.py in an agent's scratchpad; pages under codex_local_1108/briefs/WBAB2_*. Related: [[writing_brain_ab2_brain_pages_ranked_below_controls_judges_disagree_2026_11_14]], [[a_prediction_that_cannot_fail_is_not_evidence_2026_08_04]].

