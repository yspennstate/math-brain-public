---
name: bt5_claude_brain_beats_reworded_grep_60_34_codex_ties_72_74_of_160_2026_11_09
description: "Split by runtime (BT5): Claude brain 60 vs reworded grep 34 of 160 stations (32 vs 6, hunt p 0.0067); Codex brain ties reworded grep 72 vs 74 (S1 77 vs 74)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T22:13:47+04:00
  status: provisional
  evidence: "brain-repo bt5_2026_11_09 commit 8338a5392a; plan 09e821efc6; S1 723fc5947e"
---

BT5 (9 Nov 2026, an agent): brain vs grep on 40 four-station scavenger hunts (160 stations), with matched rewording advice for both arms. Plan pushed 09e821efc6 before any arm ran. The budget was 12 counted commands and 600 s a hunt. Codex gpt-6.1-sol ran at reasoning high, Claude Opus 5.5 at effort high. The full brain store was brain-graph-full-2026-11-07: 376,111 nodes and 16,811,666 edges (11,982,982 directed plus 4,828,684 co pairs), with the link sidecar on.

Codex rep 1, frozen counter: brainrw 72, greprw 74, grep 59 of 160.
- brainrw vs greprw: 20 vs 22, sign p 0.88, cluster p 0.92.
- greprw vs grep: 23 vs 8, p 0.011, cluster p 0.053.
- The frozen counter charged each heredoc line as one command. That stopped the Codex brain arm early in 18 of 40 hunts.

Supplement S1 (plan 723fc5947e) reran the Codex brain arm with each heredoc counted as one command. brainrwS got 77 of 160 (2 real voids).
- brainrwS vs greprw: 19 vs 16, p 0.74, cluster p 0.83. That is no brain advantage under the S1 rule, which needs cluster p < 0.05.
- brainrwS vs grep: 32 vs 14, p 0.011, cluster p 0.12.

Claude rep 1, frozen counter (heredoc rule changes nothing for Claude): brainrw 60, greprw 34, grep 41 of 160.
- brainrw vs greprw: 32 vs 6, sign p <0.0001, cluster p 0.0067.
- brainrw vs grep: 25 vs 6, p 0.0009, cluster p 0.016.
- greprw vs grep: 10 vs 17, p 0.25. The advice did nothing for Claude grep; only 12% of its searches shared a word with the clue.

So the runtimes split. On Codex, recall with rewording advice ties grep given the same advice, which points to the advice as the main source of the BT4 lift (159 to 270 of 480). On Claude, recall beats both grep arms by hunt. One rep a runtime; a second Claude rep would firm it up.

Scars from running it:
- Answer-write text was voided as if it were a read. The fix is a mask candidate, answer_write_mask_test.py.
- The Claude grep arm's own spilled tool output was voided. See [[claude_arm_reading_its_own_tool_results_spill_is_not_a_projects_leak_2026_11_09]].
- A python walk that skips folders by exact name reaches the mirrors in ~/brain. See [[walk_skip_by_exact_name_reaches_codex_fleet_mirror_in_brain_2026_11_09]].

Earlier step: [[bt4_final_reword_lifts_codex_hunts_270_vs_159_of_480_grep_not_robust_2026_11_09]].

Rows, grades and README: brain-repo 12_cognitive_architecture/brain_improvement/bt5_2026_11_09/ (Claude lane pushed 8338a5392a).

