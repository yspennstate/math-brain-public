---
name: word_walk_context_dial_inert_and_planner_temper_undone_2026_11_14
description: "[VERIFIED] Writing brain math: word walk's context term (kappa) nearly inert - MH min(1,.) clipping in 1-5 steps lets ~0.17 of it reach the offers; bridge_plan per-row temper does nothing on even rows; fixes in writing_brain/stats"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T22:05:29+02:00
  status: provisional
  evidence: ""
---

Checked 14 Nov 2026 by an agent (lane S, writing_brain/stats/).

1. dictionary/word_walk.py offers: 1..steps Metropolis steps from the seed. Exact law of the first offer (stats/offer_law.py, no sampling), same start sense, context off->on: mass on words that fit the page moves +0.00..+0.10 over queue/quiet/walk/old at 3 and 5 steps; the share of log ctx^beta that reaches the offers is 0.01..0.77, median about 0.17. Cause: the acceptance min(1, pi(y)deg(x)/(pi(x)deg(y))) clips at 1, so a better-fitting neighbour is taken with probability 1 however much better; the context term can reject, never promote. It does NOT mean the offers fit worse: absolute fit mass ties 4-4 with the sampler, because the walk stays near the seed's sense. Drop-in local_offers() draws exactly from pi(x)*PPR_seed(x) on the same ball (restart a 0.35), so kappa and a both act. A spectral-gap step count aims at the stationary law, which forgets the seed: wrong target for offers near a seed.

2. maths/bridge_plan.py tempers each row and renormalises; the row normalisers undo beta wherever a beat's choices are even. Toy (one-way vs four-way branch): obvious plot 50.0% at beta 1, 0.5, 0.1, checked with bridge_plan.py. stats/bridge_global.py tempers whole plots (P^beta, no renormalising; Gibbs measure on arriving plots): 50.0/33.3/22.3%; example_plan at 0.6 top plot 30.9->22.7%, entropy 2.84->3.11 bits.

3. A/B tests: judges agreeing at Spearman ~0.2 means one judge's reliability ~0.2; Spearman-Brown 0.33 (2 judges), 0.56 (5), 0.71 (10). Use maths/BLIND_TEST.md's same-writer pairs, 5+ judges of two families, Bradley-Terry with a per-judge discrimination parameter. A word-walk arm in WBAB2 tested the walk's graph, not its context term.

Not measured: whether either fix makes better prose; that is the blind test's job. Holders told on the mesh 22:04 (agent lane H, agent lane M, agent A/B). Nothing in dictionary/ or maths/ edited. Related: [[writing_brain_dictionary_and_word_walk_2026_11_14]], [[word_walk_links_senses_not_words_drift_fixed_2026_11_14]], [[writing_brain_ab2_brain_pages_ranked_below_controls_judges_disagree_2026_11_14]], [[word_senses_from_contexts_lose_to_one_vector_old_shelf_2026_11_14]].
