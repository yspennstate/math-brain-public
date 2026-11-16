---
name: diag4_budget5_brain_36_33_bare_14_15_2026_11_08
description: "[VERIFIED] Yes (8 Nov, DIAG4): at a 5-command budget the brain still named 36 and 33 of 36 scar causes against bare 14 and 15; a recall call with --or wordings makes 5 commands about ten searches"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T14:18:49+04:00
  status: verified
  evidence: "12_cognitive_architecture/brain_improvement/DIAG4_20261108 (64729abede)"
---

Does the brain's lead at naming a past failure's cause survive a budget of 5 shell commands instead of 20? Yes. DIAG4, 8 Nov, an agent. Same 24 items and key as DIAG3 (12 plants, 6 decoys, 6 controls), same arms (Codex gpt-6.1-sol high, Claude opus-5-5 high, brain and bare, 3 runs each), same store (brain-graph-full-2026-11-07, 16,811,666 edges). Commitment c1ffe2997a before any run; results 64729abede in 12_cognitive_architecture/brain_improvement/DIAG4_20261108, read back over GraphQL (25 files plus 40 in runs/).

Plants named:
- Claude: brain 36 of 36, bare 14 of 36.
- Codex: brain 22 of 24 on its 2 valid runs (33 of 36 on all runs), bare 6 of 12 on its 1 valid run (15 of 36 on all runs).
- Against DIAG3's budget of 20: brain Codex 36 to 33, brain Claude 36 to 36, bare 16 to 15 and 15 to 14.
- Decoys and controls: all right on every run for every arm.
- The one plant where bare Codex beat brain Codex was NO_ONNX (2 of 3 against 1 of 3). Both brain misses said the fresh install lacked "learned recall state" instead of the query embedding model.

What I learned:
- A command budget is not a search budget. Brain Codex spent all 5 commands, but four were recall calls with two or three --or wordings each, so it still ran about ten searches. My prediction of a large Codex drop (18 to 32) was wrong; it fell by 3. To make search cost bite, cap recall calls or wordings, not shell commands.
- Three of twelve runs went void on the known false positive: the live audit matched "brain.py" and "h3models" inside the arms' own verdicts writes, because the items' logs name those. The audit should skip the verdicts text before the next round.
- The output leak check (leakcheck.py, reading each transcript for text only a denied file holds) found 12 of 12 clean, so the verify-gate and session-tree leak paths found while building were closed.
- The brain arms are at the ceiling: 69 of 72 plants here, 108 of 108 on Claude across DIAG1 to DIAG3. Next: plants held weakly (symptom without fix, or two memories to join) and the clue checker rereading the rewrites.

Status: verified. Scores recounted a second way from the marks, runmaps and key without grade.py; they match. Follows [[diag3_brain_36_bare_16_15_stripped_clues_at_ceiling_2026_11_08]]. The leak paths it closed are in [[blind_test_key_leaks_via_verify_gate_turns_and_session_trees_2026_11_08]].

