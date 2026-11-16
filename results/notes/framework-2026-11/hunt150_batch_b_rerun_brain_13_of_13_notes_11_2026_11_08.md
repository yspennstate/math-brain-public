---
name: hunt150_batch_b_rerun_brain_13_of_13_notes_11_2026_11_08
description: "[PROVISIONAL] Does the brain beat plain notes on hunt150 batch B? Rerun 8 Nov: brain 13/13 complete (depth 37/37, median 1158 s, 841k tok), notes 11/13 (32/37, 1013 s, 629k tok); scored after the b-prefix checker fix"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:08:29+02:00
  status: provisional
  evidence: ""
---

Hunt150 batch B rerun (Br, items B003-B015, 26 rows in primary_directive/runs/bvnb_hunt_hunt150Br.jsonl, score in hunt150Br_score.txt), gpt-6.1-sol high, brain arm vs notes arm (grep over the same memory files, no brain.py). Brain: 13 of 13 complete, depth 37/37. Notes: 11 of 13, depth 32/37; B015 notes was a tool failure (0/3), one other run short. Medians over ok rows: brain 1158 s / 841k tokens, notes 1013 s / 629k tokens. Brute-force flags 2 per arm, after hunt_checker.py's 8 Nov fix (a b'...' string literal no longer matches a loop variable named b). Reading: on batch B the brain finishes every item; notes is cheaper per run but drops two. What would change it: a second rerun, or the tool failure retried. Logged on the board page AGENTIC-RECALL-HUNT-20261105.md. Related [[hunt_checker_slow_brute_b_prefix]].
