---
name: bt4_corrected_grep_false_voids_brainrw_vs_grep_45_24_p0p059_2026_11_09
description: "No (BT4 corrected): all 7 grep voids were false ('python' matched file names and rg patterns); grep 146 not 129 of 320; brainrw vs grep 45 vs 24, clustered p 0.059; advice lift 64 vs 11 stands"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T13:50:48+04:00
  status: verified
  evidence: "bt4_regrade_fv.json; bt4_regrade_fv_sens.json; bt5_audit_test.py ALL OK"
  supersedes: bt4_final_reword_lifts_codex_hunts_270_vs_159_of_480_grep_not_robust_2026_11_09
  modified: 2026-11-09T09:51:12.239Z
---

Does BT4 show the brain with rewording advice beating grep on Codex scavenger hunts? Not at the 0.05 bar once the grep arm's false voids are cleared: brainrw 270 of 480 stations against grep 146 of 320, 45 stations better and 24 worse, sign p 0.015 but hunt-clustered p 0.059 (9 Nov 13:5x). The rewording advice's lift over plain recall stands unchanged, 64 vs 11, p < 1e-4.

What was wrong. All 7 grep voids in BT4 (H014, H026, H040, R007 across reps 1 and 2) were false. The grep arm's forbid list holds r"python", and it matched the file name of a memory the arm was allowed to read (one with python in its name), the word python inside rg search patterns, and answer text written with printf. No grep run executed python or read outside the memory folder; every one of the flagged commands was read by hand. Void hunts score 0, so grep lost 17 stations (129 -> 146 of 320). The earlier memory called these "reads of the live memory folder"; that was wrong.

Corrected result (BT4R1-3, Codex gpt-6.1-sol high, 12-command budget, full brain brain-graph-full-2026-11-07 on this Mac's graph_lane_store):
- stations: brainrw 270/480 (56%), brainread 159/480 (33%), grep 146/320 (46%)
- brainrw vs brainread: 64 vs 11, 85 tied, clustered p < 1e-4 (unchanged)
- brainrw vs grep: 45 vs 24, sign p 0.015, clustered p 0.059
- brainread vs grep: 23 vs 52, sign p 0.001, clustered p 0.011: plain recall loses to grep
- pre-registered sensitivity (drop every hunt with a void; now only R006, brain arms, real voids: a home listing and a runpy call): brainrw vs grep 43 vs 22, clustered p 0.054; brainread vs grep 23 vs 48, clustered p 0.018
Checked a second way: share-difference sums equal the share gaps, 270/3 - 146/2 = 17.0 and 159/3 - 146/2 = -20.0.

So BT4 says: the advice paragraph helps the brain arm a lot, plain recall loses to grep, and brain plus advice is ahead of grep by a margin that does not reach significance. BT5 (grep gets the matched advice) is the test that separates brain from advice.

Fix for BT5: bt2_controller/bt5_run.py audits the grep arms with memory-folder file paths and slash-free quoted strings masked, python void only when run as a command (shlex, command position), and any .. path void (the old audit let memory/../../ walk out unnamed). Tested: 13 true violations void, 6 known false ones clean, BT4's 1,287 grep commands give 0 new voids and clear exactly the 7.

Reflex: a void flag is a claim about a command, not a verdict. Read every void's command before scoring 0; a forbid word that can appear in a file name or a search pattern will fire on innocent runs.

Regrade script and output: bt4_regrade_falsevoids.py, bt4_regrade_fv.json, bt4_regrade_fv_sens.json, to be pushed to brain-repo 12_cognitive_architecture/brain_improvement/bt4_2026_11_09/final/regrade_false_voids/.

Related: [[bt4_final_reword_lifts_codex_hunts_270_vs_159_of_480_grep_not_robust_2026_11_09]] (superseded by this) [[bt4_reword_paragraph_lifts_codex_hunts_53_vs_9_beats_grep_not_robust_2026_11_09]] [[leak_voids_4_of_11_were_name_hits_not_content_2026_11_09]]


The same flaw in earlier rounds, found with the fixed audit and each command read by hand (09 Nov 14:23): BT2 (bt2_20261108a) 3 of 4 grep voids false (a memory file named brain_graph_..., matched by the brain_graph forbid word), BT3BR 1 of 1 false (BT3BR2 H109; regrade in [[bt3br_recall_read3_ties_grep_51_47_of_144_lifts_brain_18_of_96_2026_11_09]]). SC3B, RES1-3 and both calibrations had no grep voids.

The same flaw was found and filed on 30 Oct in recall A/B ([[bare_name_forbid_rules_void_honest_solvers_2026_10_30]]: bare-name rules matched names inside the allowed corpus); the BT audits were built without it surfacing. Before writing any forbid list, recall that card.
