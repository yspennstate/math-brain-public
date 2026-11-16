---
name: diag14_second_fresh_draw_brain_beats_bare_lines_no_agent_lift_2026_11_08
description: "Yes on both runtimes (DIAG14): Codex bare 4/48, each 10/16 (1 valid run), grep 24/32; Claude bare 3/48, each 31/48, grep 9/48; symptom lines lift recall rank within a memory (+0.094) but not agents (lined 35/72 vs held 39/72)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T19:24:09+04:00
  status: verified
  evidence: "brain_improvement/DIAG14_20261108 c8d388068e; keys_private/diag14 score_all.txt, compareA.txt, compareC.txt"
---

Does the brain still beat no brain on a second fresh draw, and do SYMSWEEP1's symptom lines help agents? Yes to the first, on both runtimes; no sign of the second in agents' scores, though the lines lift recall rank within the memory again (DIAG14, 8 Nov 2026).

Draw: 24 scars that got a SYMSWEEP1 line and 24 held back. Codex wrote items from copies with the line removed, blind to the pool. 37 were faults, the clue reader cleared 29, and 16 plants (8 per pool), 4 decoys and DIAG4's 6 controls made 26 items. Arms bare, each and grep, on Codex gpt-6.1-sol high and Claude opus-5-5 high, 3 runs each. Store brain-graph-full-2026-11-07 (16,811,666 edges).

Plants right (valid runs):
- Codex: bare 4 of 48, each 10 of 16 (one valid run; 31 of 48 with two false-positive voids restored), grep 24 of 32.
- Claude: bare 3 of 48, each 31 of 48, grep 9 of 48.
- Every brain arm clears the +6 bar. Claude grep clears it by the minimum. No decoy was taken, and every control was right.
- The plants were harder than DIAG13's: the recall arm got 62 to 65 percent, against 85 to 89.

Lines:
- Recall rank between memories: context MRR 0.107 lined against 0.050 held (+0.057, p 0.22). 24 of 37 contexts miss the top 40 in both pools.
- Agents: lined 35 of 72 against held 39 of 72 (-4; -9 with the restored runs). That is no lift.
- Within memory (Part C): 8 of 18 held memories got a line. Context MRR +0.094 (4 up, 0 down; three rescues from outside the 40), untouched +0.000. This replicates [[symlead1_symptom_lines_lift_recall_replicated_2026_11_08]].

Scar found: the recall rule in run_audit.py voids any brain.py command whose text contains "subprocess", even inside a quoted question. It voided 2 of 3 Codex each runs here. Mask quoted text before that check in DIAG15.

What it means: lines are a small within-memory rank gain, too small to show between memories or in agents' scores. The lever for agents is the contexts recall misses outright. Related: [[diag13_fresh_items_brain_beats_bare_codex_24_26_of_27_claude_23_14_2026_11_08]].

Rows: 12_cognitive_architecture/brain_improvement/DIAG14_20261108 (c8d388068e).

