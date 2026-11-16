---
name: commit_history_per_file_finds_files_questions_describe_2026_11_08
description: "[PROVISIONAL] Where-is file lookup (brain 10x file nodes): adding the subjects of each file's last 8 commits as a separate FTS (hist_fts, weight 2) took the strict commit bank (question names no word of the path) from 0 to 17.3% hits@8 and named from 26.9 to 31.6% (top-1 65 -> 86); leak check 2-7 of ~400 near-copies"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T10:57:50+02:00
  status: provisional
  evidence: ""
---

Task 12 (). add_file_history.py writes node_hist from local clones (git log, no API); bank commits and same-subject commits held out; bulk commits >50 files and repeated subjects skipped. file_node_lookup.py --hist-index builds hist_fts; FILE_NODE_HIST_WEIGHT default 2.0 (weight 1: strict 2.5%, named 28.3%, top-1 52 - too weak against name scores). Trap: joining an FTS5 table on its unindexed id column makes SQLite scan node and do a full FTS lookup per node (hung >17 min); run the MATCH in a subquery with LIMIT, then join. Caveat: neighbouring commits on the same work share words with the bank commit - that is the signal, but a stricter test would use only history older than each bank commit. Files: the private repository: 12_cognitive_architecture/brain_10x_file_nodes_2026_11_08 (push 694c806f), hist_eval.log, hist_leak_check.py.
