---
name: bt4_reword_paragraph_lifts_codex_hunts_53_vs_9_beats_grep_not_robust_2026_11_09
description: "[PROVISIONAL] Yes (BT4, 2 of 3 reps): a reword-the-query paragraph lifts Codex hunt stations 177 vs 104 of 320 (53 vs 9 per station without void hunts, clustered p 0.0005); vs grep 129 only before dropping voids; plain recall loses to grep"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T11:26:09+04:00
  status: provisional
  evidence: "bt4_results_BT4R1_BT4R2.txt; bt4_grade_sens_BT4R1_BT4R2.json"
superseded_by: bt4_final_reword_lifts_codex_hunts_270_vs_159_of_480_grep_not_robust_2026_11_09
---

Does telling a Codex hunter to reword its recall queries away from the clue's words find more scavenger-hunt stations? Yes, by a wide margin on two reps (BT4, 9 Nov, interim: rep 3 of the two brain arms runs from 11:24 and the final grade follows).

Setup. 40 scored hunts of 4 ordered stations each (160 stations), clues worded far from the memories on purpose, budget 12 counted commands, Codex gpt-6.1-sol high, two reps of three arms. brainread: brain.py recall with --read 3, node and file reads allowed. brainrw: the same rule plus one paragraph (bt2_controller/bt4_run.py REWORD) telling it to leave the clue's words out and write two or three guesses at how the memory would say it, as the question and its --or wordings. grep: rg over the memory folder copy, no brain. Recall ran on this Mac's graph lane (graph_lane_store, brain-graph-full-2026-11-07: 11,982,982 directed pairs plus co pairs, the full brain). Questions, scoring, the pairs and the sensitivity rule were pushed before grading (124b781e11, 3b8cc0de18, abe4db47b9).

Result, stations found of 320 (two reps): brainrw 177, grep 129, brainread 104. Per station, primary brainrw vs brainread: 61 better, 9 worse, 90 tied, sign p < 1e-4, hunt-clustered p 0.0001. brainrw vs grep 46 vs 17 (sign p 0.0003, clustered 0.021). brainread vs grep 21 vs 42 (sign p 0.011, clustered 0.18).

Sensitivity (pre-registered 10:1x: drop every hunt with a void in any arm: H014, H026, H040, R006, R007, so 35 hunts): brainrw vs brainread 53 vs 9 (clustered p 0.0005), holds. brainrw vs grep 33 vs 15, sign p 0.013 but clustered p 0.107, so the win over grep is not robust once the void hunts go. brainread vs grep 13 vs 39 (clustered 0.019): plain recall loses to grep.

Checked a second way: each share-difference sum equals half the gap in stations found (for example (151-87)/2 = 32 in the sensitivity run). Leak check (leak_shingles, 23 result memories, 8704 shingles) printed no hits on either rep.

Mechanism hints, not scored: brainrw's wordings still shared a clue word 78% of the time against brainread's 85%, so the paragraph changed the queries only a little. The bigger visible change is budget: brainread hit the 12-command budget in 45 of 80 hunt runs and printed 90 outputs over 40k chars; brainrw 25 and 43. Gold shown in some output and still missed: brainread 62, brainrw 68, grep 74, so many misses are reading misses, not surfacing misses. Time: medians 85 s (brainread), 84 s (brainrw), 91 s (grep) per hunt run.

Voids: grep 7 (reads of the live memory folder in H026, H040, R007 in both reps, and H014 where the answer text names python3); each brain arm 1 (R006: a home listing and a runpy call outside the allowed recall command).

Fits DIAG17C rather than contradicting it: there the advice was the opposite (copy distinctive words from the item) and it cut Codex from 40 to 29 of 66 ([[diag17c_query_advice_lifts_claude_recall_29_43_hurts_codex_40_29_2026_11_09]]); here, on clues worded far from the memories, telling Codex to keep the clue's words out lifted it. Which advice helps depends on how far the asking words sit from the memory's words.

Rows, grader output and scripts: brain-repo 12_cognitive_architecture/brain_improvement/bt4_2026_11_09/.

Related: [[bt3br_recall_read3_ties_grep_51_47_of_144_lifts_brain_18_of_96_2026_11_09]] [[diag17c_query_advice_lifts_claude_recall_29_43_hurts_codex_40_29_2026_11_09]] [[hunt_clue_recall_reach_3pct_alone_agent_rewording_65pct_2026_11_09]] [[brain_arm_misses_are_surfacing_misses_seen_426_of_479_unseen_23_of_331_2026_11_09]]

