---
name: diag18_query_advice_fresh_items_not_confirmed_2026_11_09
description: "[PROVISIONAL] Same direction, half size (DIAG18): Claude eachkw-each +8, Codex each-eachkw +7 of 54, bar 9, not confirmed; each-bare +40/+29 confirmed"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T04:08:24+04:00
  status: provisional
  evidence: "brain-repo 12_cognitive_architecture/brain_improvement/DIAG18_20261109 (08fff47eed)"
---

Does the query-advice paragraph (DIAG17 Addendum C) hold on items nobody had seen? Same direction, half the size, not confirmed (DIAG18, 9 Nov, pre-registered, N = 9 plants + 6 controls, bar 9 points).

Brain: brain-graph-full-2026-11-07, 11,982,982 directed + 4,828,684 co pairs = 16,811,666 edges, sidecar link walk 243,298 rows, BRAIN_RECALL_LOG=0, BRAIN_RECALL_REFRESH=0. Codex gpt-6.1-sol high and Claude claude-opus-5-5 high, 10 tool calls, 1200 s, three waves of 8 with every arm in every wave.

Plant points of 54 (valid runs scaled to 3):
- Codex: bare 0, each 40, eachkw 33 (2 valid runs, 22 of 36), grep 38.
- Claude: bare 4, each 33, eachkw 41, grep 31.5 (2 valid runs, 21 of 36).
- H1 Claude eachkw - each +8 (items 5 higher, 2 lower, 2 tied): not confirmed, same direction. H2 Codex each - eachkw +7 (5/1/3): not confirmed, same direction. H3 each - bare: Codex +40 (9/0/0), Claude +29 (8/0/1): confirmed.
- DIAG17 Addendum C had Claude +14 and Codex -11 on its own items, so the effect roughly halved on fresh items, as an effect tuned on the items it was written from should.
- Mechanism held: with the advice Claude asked ~45 questions a run against 32 and surfaced 43 planted-note cause-runs against 35; Codex's questions shrank from ~9 to ~6 words and it surfaced 24 of 36 against 44 of 54.
- Against clean grep: plain recall ties (Codex +2, Claude +1.5); only Claude with the advice clears it (+9.5).

Validity: 22 of 24 valid, leakcheck clean on all 24. Voids: Codex eachkw run 2 read a compaction node via brain.py node; Claude grep run 2 had a /tmp/ path in a command. Item rulings written from the key before any verdict was read; marks hashed before unblinding.

**Why:** the advice was written after seeing DIAG17's runs; this was the check before anyone puts it into recall's prompt or the hooks.

**How to apply:** do not add the paragraph to a shared prompt that both runtimes read. If it goes anywhere, it goes into Claude-only recall guidance, and a larger run (5+ runs per cell) should size the effect first. Brain recall beats no brain on every fresh draw so far; it does not beat a clean grep copy without the advice. Follows [[diag17c_query_advice_lifts_claude_recall_29_43_hurts_codex_40_29_2026_11_09]] and [[diag17_fresh_draw_recall_beats_bare_loses_to_clean_grep_50_40_37_28_2026_11_09]]; the index drift is [[recall_refresh_0_does_not_freeze_index_2026_11_09]]. Rows and scripts: brain-repo 12_cognitive_architecture/brain_improvement/DIAG18_20261109/ (prereg e2472268a5, 97ee64e6b3; results 08fff47eed).


Follow-up 9 Nov 04:5x: DIAG18B (runs 4-6) put the Claude difference at +0.0 and Codex at +1.5 of 54; pooled six runs +8.0 and +9.6 of 108, bar 18. Not confirmed: [[diag18b_query_advice_six_runs_not_confirmed_2026_11_09]].
