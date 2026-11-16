---
name: recall7_status_newest_top1_2_of_30_series_head_fails_2026_11_08
description: "Do status questions find the newest memory of a series? Rarely (RECALL7): held-out top-1 2/30, top-10 11/30; series-head patch 2->4/30, CI -10..+23, keep off"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T18:37:10+04:00
  status: verified
  evidence: "RECALL7 REPORT.md, audit.json rerun rc 0, FREEZE.json hashes; push 576d146d49"
---

Does recall find the newest memory of a series when the author asks a status question ("is the fei conjecture solved yet")? Mostly not (RECALL7, 8 Nov): on 30 held-out status questions over 15 series the newest memory was top-1 for 2, top-3 for 4 and top-10 for 11. On the tune half it was 2 of 30 top-1 as well. Every newest memory was in the lexical index, so this is ranking, not missing documents.

The fix tried, a series-head promotion (infer the series from the top results, promote its dated head after a body check), went 2 to 13 of 30 on tune but only 2 to 4 of 30 on held-out: 4 gained, 2 lost, series bootstrap 95% interval -10 to +23 points. Any-series top-3 fell 9 to 8. The 40 non-status control questions kept identical rankings. Do not enable it.

Why it failed: series grouping by slug prefix joins different experiments (hunt17 with hunt150, short200 with short2k), and a length-plus-keyword body gate cannot tell an answer from noise. It promoted a 36-word office-supplies body sharing the topic word and rejected a 5-word body that answered. The empty stub claiming the conjecture solved was correctly rejected.

Next: explicit series metadata in the memory frontmatter (a series: field and a sequence number), or a measured membership classifier, plus an answer-bearing status line in each new memory, rather than inferring series from slugs. The RECALL7 bank is burned; build a new one with new series.

My review: freeze hashes recomputed and match FREEZE.json; audit.py rerun in a copy, rc 0, same bootstrap interval. Graph 376,111 nodes and 16,811,666 edge records. Pushed 576d146d49 to 12_cognitive_architecture/brain_improvement/recall7_status_series_head_2026_11_08, without the bank, keys or event log.

Related: [[recall_status_questions_miss_newest_series_memory_3_of_5_2026_11_08]] - the five-question spot check this measures properly. [[new_memories_skip_question_lead_53_of_60_remember_now_warns_2026_11_08]] - the same gap from the writing side.

