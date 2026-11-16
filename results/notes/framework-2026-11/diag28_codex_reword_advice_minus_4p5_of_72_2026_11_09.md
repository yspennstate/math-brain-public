---
name: diag28_codex_reword_advice_minus_4p5_of_72_2026_11_09
description: "[PROVISIONAL] No (DIAG28): Codex told to word recall questions like the memory scored 43.0 vs 47.5 of 72, -4.5, inside bar"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T10:18:52+04:00
  status: provisional
  evidence: "the private brain repository 51e7d8d4f5 12_cognitive_architecture/brain_improvement/DIAG28_20261109"
---

No (DIAG28, 9 Nov 2026). Telling Codex (gpt-6.1-sol high) to word its brain recall questions as guesses at the memory's own words (tool, file, error text, cause and fix; three guesses per item as separate --each questions) scored 43.0 against 47.5 for the plain 48+ question advice, plant points of 72 on DIAG21's single-memory items, six runs a cell, scaled to 3 runs. Gap -4.5, items 2 higher / 5 lower / 5 tied, inside the bar of 9. Strict line (one eachhi run voided for a session-id name hit in an unrelated memory's frontmatter) -5.0. Controls 36/36 in both arms; 12 of 12 runs valid, all 48+ questions.

The advice did change the search: fewer questions (56-70 vs 64-80), longer ones (12-15 words vs 11-13), more node reads (1-3 vs 0-1). It did not find more. Drops came on items whose second cause is already in plain operational words in the item (D05, D13, D14, D18).

Graph: brain-graph-full-2026-11-07, 11,982,982 directed + 4,828,684 co pairs = 16,811,666 edges, live sidecar link walk. Pre-registered 941a84da5c (prediction H1 fails near +3: verdict right, sign wrong). Results 51e7d8d4f5 at 12_cognitive_architecture/brain_improvement/DIAG28_20261109 on the private repository.

This is the second wording advice to fail for Codex, after [[diag17c_query_advice_lifts_claude_recall_29_43_hurts_codex_40_29_2026_11_09]]. The same eachhi arm scored 43.5 on these items in [[diag24_codex_brain_ties_grep_six_runs_0p5_pooled_2p7_of_72_2026_11_09]], so the arm is stable across grading passes.

**Why:** prompt advice on how to word queries keeps failing to lift Codex, while offline rewording passes helped bare recall.
**How to apply:** do not add query-wording paragraphs to Codex brain prompts. If wording matters, put the rewording in the tool (a separate step that rewrites the question before recall), not in advice to the searching agent.

