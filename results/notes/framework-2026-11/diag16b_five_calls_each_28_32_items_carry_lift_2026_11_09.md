---
name: diag16b_five_calls_each_28_32_items_carry_lift_2026_11_09
description: "[VERIFIED] Mostly the items (DIAG16B): at 5 calls Codex each 40->28, Claude each 35->32, Claude grep 23->14; each still beats bare by 23+; Codex grep all leak-void"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T02:13:49+04:00
  status: provisional
  evidence: "DIAG16B_20261109/score.txt 336e065234"
---

---
status: verified
---
Did DIAG16's lift come from the 10-call budget or from the unrewritten items? Mostly the items. DIAG16B reran the brain arms on DIAG16's 17 items at 5 tool calls, with the plan pushed before any run (3bb7fed938). Codex each fell 40 -> 28 of 66 (-12, just past the pre-registered 11-point bar, so the budget mattered there). Claude each fell 35 -> 32 (-3) and Claude grep 23 -> 14 (-9), both inside the bar. At 5 calls each still beats DIAG16's bare by 24 (Codex) and 23 (Claude), and Claude's each beats its grep by 18. Controls were 18/18 in every valid cell. Store: brain-graph-full-2026-11-07, 16,811,666 edges, sidecar 243,298 links.

Codex grep has no valid run: the leak check voided all three. One printed lines of my own compaction node, one printed a line of the DIAG16 result memory, and one hit only my session id (originSessionId in an unrelated memory's frontmatter, a false positive of the '472b1d4f-77c3' marker). Scored back in, the two leaky runs carried the cell (17 of 66 with all three, 1 of 22 for the clean-hit run alone). Second time in two tests (DIAG16's grep_codex_Dr2 too): a grep arm over the live memory folder reaches the author's notes on the test. The next bank should give the grep arm a memory snapshot without the author's compaction nodes and the DIAG result memories. Same root as [[test_built_before_own_compaction_leaks_items_via_anchor_v3e_void_2026_11_07]] and [[diag12_diag5_items_burned_grep_reads_result_memories_3_of_6_void_2026_11_08]].

Judge: me again (the DIAG16 judge, who knew the items), under DIAG16's rulings plus six new ones written before the runmaps were opened. The items are now burned for grep arms. Follows [[diag16_ten_calls_each_40_35_bare_4_9_of_66_2026_11_09]]. Files: the private repository, 12_cognitive_architecture/brain_improvement/DIAG16B_20261109/ (336e065234).

