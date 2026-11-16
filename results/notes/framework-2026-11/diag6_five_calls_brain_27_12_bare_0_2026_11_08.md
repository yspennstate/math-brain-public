---
name: diag6_five_calls_brain_27_12_bare_0_2026_11_08
description: "Does the brain still lead at 5 tool calls of any kind? Yes (8 Nov, DIAG6): brain Codex 27, Claude 12 of 36, bare 0, no decoy taken; Codex won by grep, never calling recall"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:07:07+04:00
  status: verified
  evidence: "the private repository, 12_cognitive_architecture/brain_improvement/DIAG6_20261108 (prereg 2ebe81f8bd, results 335d29a831)"
---

Does the brain still lead when an arm gets only 5 tool calls of any kind (search capped as well as recall)? Yes (8 Nov, DIAG6).

DIAG5's 12 plants, 6 decoys and 6 controls, byte for byte, with DIAG5's faults fixed: the budget worded as it is counted, the recall loop check outside quoted text only, the deny list naming compaction nodes instead of the bare word, the memory folder path in the brain rules. Codex gpt-6.1-sol high and Claude opus-5-5 high, brain and bare, 3 runs each, store brain-graph-full-2026-11-07 (16,811,666 edges), sidecar 242,841 link rows. Prereg 2ebe81f8bd before the arms; judged blind under DIAG5's JUDGING.md.

- Bare: 0 of 36 plants on both runtimes; decoys 18 of 18, controls 17 and 18 of 18.
- Brain Codex: 11, 7, 9 = 27 of 36 (reading B). Under the primary, Dr2 and Dr3 are void on a leak marker that matched file names and MEMORY.md index lines, not anchor bodies (the anchor sentence occurs 0 times); Dr1 alone is 11 of 12.
- Brain Claude: 5, 3, 4 = 12 of 36, all valid.
- No brain run took a decoy (36 of 36). Audits 12 of 12 pass; recount agrees.

Against DIAG5: Codex 20 to 27, Claude 17 to 12. Claude spent 3 of its 5 calls on brain.py recall; its DIAG5 run had 14 to 19 file calls. Codex never called brain.py: all 5 calls were grep and reads of the memory folder, and it gained DREAM_PREFIX, CTIME_REPLACE and COPIED_SIDECAR. Whether the gain is the memory path in its rules or the memories the old deny word blocked is not separated.

Lesson: at a 5-call budget, grep over the memory folder found more planted causes than three recall calls did. That is a recall result at small budgets, worth a test of its own (recall-only arm against grep-only arm, same budget). Next leak marker: the anchor's FIRE WHEN sentence, not the compaction node name.

Rows and scripts: the private repository, 12_cognitive_architecture/brain_improvement/DIAG6_20261108 (results in 4 commits, the last 335d29a831). Follows [[diag5_capped_recall_brain_20_17_bare_0_2026_11_08]].

