---
name: diag29_codex_brain_beats_grep_joins_pooled_11p7_read_each_no_gain_2026_11_09
description: "[PROVISIONAL] Yes pooled (DIAG29): Codex brain 45.5 vs grep 27.0 of 66 on join items, pooled +11.7 over 3 runs; --read-each 1 adds nothing (-4.0)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T11:04:49+04:00
  status: provisional
  evidence: "the private brain repository 0c5772d11d 12_cognitive_architecture/brain_improvement/DIAG29_20261109"
---

Yes, with three runs pooled (DIAG29, 9 Nov 2026). On DIAG16's two-memory fault items (11 plants, 6 controls), Codex gpt-6.1-sol high with brain recall and the 48+ question advice (eachhi) scored 45.5 against grep's 27.0 (plant points of 66, six runs a cell scaled to 3 runs; bar 9): +18.5, items 10 higher / 0 lower. Pooled with DIAG16 and DIAG26 (15 and 13 runs): 40.8 vs 29.1, +11.7, items 9 / 2. DIAG26 alone was +5.5, so the pooled figure is the one to quote.

The new brain.py flag `recall ... --each ... --read-each 1` (prints the whole top memory of every question in the same call; K capped at 2, 8 reads a call; byte-identical output without it) did not add on top: eachre 41.5 vs eachhi 45.5, -4.0, items 3 / 7 / 1. eachre still beat grep +14.5 (H1 of the PREREG). eachre runs read about 40 memories each and had transcripts three times longer, and found fewer second causes on five items.

Validity: 17 of 18 runs valid. The void was a false void: grep run 1 opened a snapshot memory whose file name contains "graph_lane", which the grep arm's deny pattern for the brain's graph_lane code also matches. Counted in, gaps +13.5 and +17.5. Narrow that pattern to paths outside the snapshot in the next harness. Leak check 18 of 18 clean; all brain runs asked 72 to 80 questions. Run time about 5 minutes and 18 s per item in every arm. New in the harness: BRAIN_RECALL_EXCLUDE over DIAG result memories and the builder's compaction anchors for every Codex arm, so lists and reads cannot show a denied memory (0 of 64 gold slugs match). That may be part of why eachhi rose from 36.5 (DIAG26) to 45.5.

Graph brain-graph-full-2026-11-07, 11,982,982 directed + 4,828,684 co pairs = 16,811,666 edges, 243,689 sidecar link rows. PREREG f272cf6929, results 0c5772d11d at 12_cognitive_architecture/brain_improvement/DIAG29_20261109 on the private repository. brain.py backup before the flag: ~/brain/porting/brain.py.before_20261109_read_each.

Follows [[diag26_codex_brain_vs_grep_join_items_5p5_below_bar_2026_11_09]] (the +5.5 this pools with) and [[diag27_claude_brain_beats_grep_join_items_18_of_66_2026_11_09]] (Claude +18.0 on the same items). The read flag mirrors [[recall_read_k_one_call_finds_and_reads_sc3b_gold_4_to_23_of_67_2026_11_09]], which helped hunts but not this audit. Third Codex prompt or read change in a row that did not lift eachhi, after [[diag28_codex_reword_advice_minus_4p5_of_72_2026_11_09]].

**Why:** the author wants brain vs no-brain tests with Codex; until now Codex never cleared the bar against grep.
**How to apply:** quote Codex brain vs grep on joins as +11.7 pooled (bar met), on single-memory items as a tie. Keep Codex audit prompts at the plain 48+ question advice; do not add --read-each or wording advice to them.

