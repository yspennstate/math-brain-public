---
name: recall_weak_match_line_on_contentless_questions_live_2026_11_09
description: "[VERIFIED] Recall on a vague question (hello, yes do it, test, lorem ipsum) now prints [weak match]: matched-word idf sum < 5 or every word respelled; 0/20 controls+real fire, ranked lists unchanged 55/55 (row 72)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T05:06:04+02:00
  status: provisional
  evidence: ""
---

Live in brain.py since 2026-11-09 05:0x (an agent, brain loop rows 69-72). Recall's printed scores are min-max per query, so the top hit always reads 1.00 even when the question has no content; before this, 5 of 20 junk questions got a confident list with no advisory at all.

The rule: after spell normalisation, sum the idf of the query words the index holds; under 5, or every typed word changed by QueryNormalizer._correct, prints one line after the list: '[weak match] ... (matched-word weight X) - this list may be only loosely related; add a specific word (a name, a file, a number, a date) and ask again.' Slug-shaped (snake_case), file-extension and path queries are exempt. BRAIN_RECALL_WEAKHINT=0 turns it off; fail-open.

Measured: both arms cold (BRAIN_RECALL_SERVER=0) on 55 questions, ranked lists identical 55/55; fires on 6/20 junk, 0/10 controls, 0/10 ordinary real questions, 5/15 real questions row 71 had flagged (two placeholders 'your question', 'what do I do when usage runs out', plus file-name questions). On 960 real agent questions it flags 1.6 pct, about 0.3 pct natural-language false alarms (e.g. 'rebalance'). Served recall verified after go-live: 'hello' shows the line (weight 3.7), 'recall server soft cap restart' does not.

Lesson from building it: an A/B that compares served recall against a cold dev copy shows ranked-list differences that are served-vs-cold drift, not the patch; compare cold against cold. And row 70's first form (every word absent from the index) let 'lorem ipsum dolor' through because 'dolor' is in one memory; 'every word changed by the normaliser' caught it.

Hint for the reader: a [weak match] line is a size of doubt, not a verdict; a short specific query can still be right. What would change it: a bank showing the line on useful lists more than rarely. Evidence: ledger row 72, files under 12_cognitive_architecture/brain_improvement/ghfetch_brainfile_2026_11_08/ (ab72b.json, weak71.json).

Related: [[recall_server_grows_8mb_a_call_and_hands_over_hourly_2026_11_08]] (served path the check ran through), [[semantic_rescue_adds_no_recall_hits_costs_tail_slots_2026_11_08]] (same 139-episode test family), [[recall_output_annotations_name_other_slugs_parse_the_rank_line_2026_11_08]] (how the A/B scored lists).
