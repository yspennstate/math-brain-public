---
name: bt4_final_reword_lifts_codex_hunts_270_vs_159_of_480_grep_not_robust_2026_11_09
description: "Does a reword-your-queries paragraph lift Codex scavenger hunts? Yes (BT4 final, 3 reps): brainrw 270 vs brainread 159 of 480, 54 vs 11 stations after dropping void hunts; win over grep (129/320) not robust, clustered p 0.082"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T13:37:12+04:00
  status: provisional
  evidence: "bt4_results_final.txt; the private repository, 12_cognitive_architecture/brain_improvement/bt4_2026_11_09/final"
  supersedes: bt4_reword_paragraph_lifts_codex_hunts_53_vs_9_beats_grep_not_robust_2026_11_09
superseded_by: bt4_corrected_grep_false_voids_brainrw_vs_grep_45_24_p0p059_2026_11_09
---

Does telling a Codex hunter to reword its recall queries away from the clue's words find more scavenger-hunt stations? Yes, and it held across three reps (BT4 final, 9 Nov 13:24). Whether that puts the brain ahead of grep is not settled: the win over grep is not robust once void hunts are dropped, and only the brain arm got the advice.

Setup. 40 scored hunts of 4 ordered stations each (160 stations), clues worded far from the memories on purpose, budget 12 counted commands, Codex gpt-6.1-sol high. Arms: brainread (brain.py recall --read 3, node and file reads), brainrw (the same plus one paragraph, bt2_controller/bt4_run.py REWORD: leave the clue's words out, write two or three guesses at how the memory would say it as the question and its --or wordings), grep (rg over a memory folder copy, no brain). Reps: brain arms 3, grep 2 (rep 3 was the two brain arms only). Recall ran on this worker machine's graph lane (graph_lane_store, brain-graph-full-2026-11-07: 11,982,982 directed pairs plus co pairs, the full brain). Questions, scoring, pairs and the sensitivity rule were pushed before grading (124b781e11, 3b8cc0de18, abe4db47b9).

Result, stations found: brainrw 270 of 480 (56%), brainread 159 of 480 (33%), grep 129 of 320 (40%). Per station (share of reps found, 160 stations, hunt-clustered permutation p):
- brainrw vs brainread: 64 better, 11 worse, 85 tied, p < 1e-4.
- brainrw vs grep: 53 vs 21, sign p 0.0003, clustered p 0.012.
- brainread vs grep: 28 vs 48, sign p 0.029, clustered p 0.22.

Sensitivity (pre-registered: drop every hunt with a void in any arm of any rep, H014, H026, H040, R006, R007; 35 hunts): brainrw vs brainread 54 vs 11 (clustered p 0.0001), holds. brainrw vs grep 36 vs 19, sign p 0.03 but clustered p 0.082: not robust. brainread vs grep 16 vs 44 (clustered p 0.011): plain recall loses to grep.

Checked a second way: each share-difference sum equals the gap in station shares, (270-159)/3 = 37.0, 270/3 - 129/2 = 25.5, and in the sensitivity run (228-129)/3 = 33.0. Rep 3 alone repeats the direction: brainrw 93 vs brainread 55 of 160.

Leak check. The interim memory's "no hits" was a blind read: leak_shingles.py globbed only *_Dr[0-9].jsonl, and BT4 transcripts are keys_private/bt4_runs/<run>/<arm>_codex_<hunt>.jsonl, so it read 0 transcripts on every rep (fixed 13:3x: it now reads that layout and exits with an error on 0). Reread properly: 13, 13 and 6 transcripts (of 120, 120, 80) hold 8-word runs of the 23 older result memories, but those 23 name 0 of the 153 BT4 gold slugs, so none of them can give an answer away. BT4's own interim memory names 0 gold slugs as well. In rep 3, 1 of 80 transcripts shares 10 or more of its runs (max 28). Reps 1 and 2 ran before it existed and show 4 and 7 of 120 (max 30), from shared wording. No run was voided for a leak. A positive control (part of a result memory planted as a transcript) came back LEAK with 163 runs.

Mechanism hints, not scored. The paragraph changed the queries only a little: 77% of brainrw wordings still shared a clue word, against brainread's 86%. Budget changed more. brainread ran out of its 12 commands in 66 of 120 hunt runs and printed 141 outputs over 40k chars; brainrw 38 and 55. Gold was shown in some output and still missed: brainread 79, brainrw 100, grep 74 station-runs. Gold never shown and missed: brainread 238, brainrw 106, grep 89. So rewording mainly cut surfacing misses. Median time per hunt run: brainread 89 s, brainrw 83 s, grep 91 s.

Voids: grep 7 (reads of the live memory folder in H026, H040, R007 in both reps, and H014 where the answer text names python3). Each brain arm had 1 (R006 in one rep: a home listing and a runpy call outside the allowed recall command). The brain arms had none in rep 3.

Next: BT5 (draft at codex_fleet/20261108_pro/inputs/bt5/DESIGN_DRAFT.md) gives grep the matched reword paragraph, so brainrw vs greprw separates the brain from the advice. It runs on Codex and Claude, uses fresh hunts and scrubs tokens from the Codex child env.

Rows, grader output and scripts: the private repository, 12_cognitive_architecture/brain_improvement/bt4_2026_11_09/final/.

Related: [[bt4_reword_paragraph_lifts_codex_hunts_53_vs_9_beats_grep_not_robust_2026_11_09]] (the interim, two reps) [[bt3br_recall_read3_ties_grep_51_47_of_144_lifts_brain_18_of_96_2026_11_09]] [[diag17c_query_advice_lifts_claude_recall_29_43_hurts_codex_40_29_2026_11_09]] [[hunt_clue_recall_reach_3pct_alone_agent_rewording_65pct_2026_11_09]] [[brain_arm_misses_are_surfacing_misses_seen_426_of_479_unseen_23_of_331_2026_11_09]]

