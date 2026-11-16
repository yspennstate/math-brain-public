---
name: bvnb139_brain_recall_ties_grep_on_the_memory_a_session_needed_2026_11_08
description: "Does brain recall beat grep at naming the memory a session later needed? No (BVNB139, 8 Nov): 35 vs 34 of 139 hits, grep ranks higher, 90 defeat both; grep arm saw a wake digest"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T17:06:32+02:00
  status: provisional
  evidence: ""
---

Does brain recall find the memory a session later needed better than plain search? Not on BVNB139 (8 Nov 2026).

The bank: 139 real session prompts from recall history; the key for each is the memories that session went on to read.
Two Codex workers named up to 8 memory slugs per prompt. Arm A used `brain.py recall` as often as it liked; arm B used
rg/grep and file reads only (plus a filename-derived helper it wrote itself).

- Hit in the first 8: A 35/139 (MRR 0.124), B 34/139 (MRR 0.176).
- Paired: 20 both, 15 A only, 14 B only, 90 neither. When both hit, B ranked the key memory higher 11 times, A twice.
- A's own review pass after answering kept the hits and lowered MRR (0.134 -> 0.124).
- Time: A median 57 s a question, B 6 s, but B's clock excludes its preparation, so the times do not compare.

Caveats, both serious: B was not a clean no-brain arm (a mandatory wake step showed it a brain digest), and this is one
bank of one task shape. What it does say: two thirds of these prompts defeat both methods - the memory a session ends up
needing is mostly not predictable from its opening prompt - and where it is predictable, a careful filename search is as
good as recall. Recall's value has to be shown on tasks where the words of the question are not the words of the slug.

Files: brainloop_c462/score_bvnb139.py (key beside it), bvnb139_scores.json, bvnb139_pair.json; ledger row 45.
Related: [[an_ab_whose_harness_hardcodes_the_tool_path_compares_nothing_2026_11_08]], [[hunt150_batch_b_rerun_brain_13_of_13_notes_11_2026_11_08]].

