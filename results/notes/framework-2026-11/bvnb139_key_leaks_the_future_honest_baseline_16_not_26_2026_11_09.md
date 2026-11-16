---
name: bvnb139_key_leaks_the_future_honest_baseline_16_not_26_2026_11_09
description: "[PROVISIONAL] bvnb139 recall test flattered? Yes: its key is every memory the session read, long sessions read memories written after the question, and bm25's top 8 is 75% later nodes. At question time bm25 scores ~16/139, not 26 (rows 106-107); one-hop G2's +8 was +2"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T16:51:41+02:00
  status: provisional
  evidence: ""
---

Rows 106-107 of brain_improvement/IMPROVEMENT_LEDGER.jsonl (files under ghfetch_brainfile_2026_11_08/r106*, r107*). bvnb139 (8 Nov, build_bvnb139.py) takes each session's first user prompt as the question and every memory the session read as gold. 113 of 139 questions have a gold memory created after the question, 33 have only such golds. bm25 top 8 holds 838 of 1112 slots by nodes created after the question (mostly the session's own later compactions). Time-honest score (drop nodes created after the question; NTFS creation time when it falls on the slug date): 16/139; strict slug-date-23:59 10/139; lenient 00:00 35/139 - the dating matters. Row 104's G2 one-hop promotion won 8, 6 of them through the session's own later compactions; at question time +2 (one prompt asked twice). How to apply: score bvnb139 at question time before believing any arm, above all arms that favour fresh nodes; arm deltas in rows 46-106 carry the leak. What would change it: a timestamped retrieval trace per read (retrievals.tsv) to restrict gold to reads in the first turn.
