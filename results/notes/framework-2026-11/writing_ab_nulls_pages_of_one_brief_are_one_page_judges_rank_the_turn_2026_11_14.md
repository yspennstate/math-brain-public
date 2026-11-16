---
name: writing_ab_nulls_pages_of_one_brief_are_one_page_judges_rank_the_turn_2026_11_14
description: "Writing A/B null three times - why? Pages of one brief are one page in every arm (12 of 12 same opening, overlap 0.18-0.26), judges rank on what changes between the people (18 of 18 reasons), tools acted on words; built turn.py plan + draw"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T22:09:42+02:00
  status: provisional
  evidence: "writing_brain/turn/evidence/commons_bank.json, judge_reasons.json; commits 120c4a19, cf96838c"
---

Why the three writing-brain A/B tests of 14 Nov (WBAB, WBAB2, WBAB3) were null or against the brain, from a reading of the judged pages by an agent, 14 Nov 21:0x-21:3x.

What was measured
- Pages of one brief are nearly one page in every arm. For each of the six briefs of WBAB2 and WBAB3, 55 to 86 content-word stems that the brief did not give are held by half or more of the writers. Truck brief (WBAB3 task 2): 12 of 12 pages open on the father's instruction at the pedals, 10 use the dashboard, 7 a pale shape on a wall where something hung, 7 a loose socket or spanner, 7 the son saying how long the author has been driving. Mean pairwise Jaccard within an arm is 0.18 to 0.26 in every arm: writers with the brain are no less alike.
- The judges' stated reasons (6 judges x 3 tasks, 18 first places, 18 last places): all 18 firsts are about the people - 16 a change between them that comes out of what they do and say, or a person made particular by one choice or habit; 2 what passes unspoken. None gives word choice, imagery or rhythm. Lasts: 9 routine or activity that shows nothing of the person, 7 something arranged or staged, 6 a point repeated or pressed at the close, 3 unclear, 2 a feeling told (some name two).
- The judges are a noisy stick: WBAB3 inter-judge Spearman 0.32 to 0.67 by task, WBAB2 0.05 to 0.48. My own blind ranking of WBAB3 task 2 (fixed before unblinding) correlates 0.01 with the four judges' mean; on it the no-brain pages placed 2, 3, 4, 6 of 12. One task, one reader, and I had already read that the judges found brain pages busy.

Reading
The cards, page checks, practice and word walk act on words, sentences and detail. The ranking was decided one level up, in what happens between the people, and at that level every writer of a brief produced the same scene. A random walk on words varies the words of the same page.

What was built from it (writing_brain/turn/, commits 120c4a19 and cf96838c on the private repository)
- turn.py plan: five lines before a page (the page everyone writes, who they are, the turn, where it falls, what is left out) and a cutting pass.
- turn.py draw: a random leaf of a tree of scene shapes (648 for two people) plus a five-step +-1 walk uniform over the paths that end one step from the start; the brief's fixed terms are never drawn. The author's 21:3x ask to use the probability work at writing.
- turn.py commons: what several drafts of one brief share; evidence/commons_bank.json and evidence/judge_reasons.json.

Not known: whether either mechanism moves a blind ranking. WBAB4 (plan vs no brain) and WBAB5 (plan+draw vs no brain) are pre-registered in brain_improvement/wbab4_agent/ and running; this memory is to be linked from the result's memory.

**How to apply:** before testing another writing aid, run `turn.py commons` on the control pages: if the pages are one page, a word-level aid cannot show. Read the judges' why_first lines before believing a rank gap means what the aid's builder thinks it means. What would change this: a judge family whose reasons cite words or rhythm, or briefs on which control pages already differ.


Related: [[writing_brain_ab_first_test_no_difference_writer_spread_dominates_2026_11_14]], [[writing_brain_ab2_brain_pages_ranked_below_controls_judges_disagree_2026_11_14]], [[writing_recurring_business_tracks_worse_judge_rank_2026_11_14]], [[writing_brain_dictionary_and_word_walk_2026_11_14]], [[a_prediction_that_cannot_fail_is_not_evidence_2026_08_04]].
