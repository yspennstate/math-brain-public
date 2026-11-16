---
name: prompt_store_correction_flag_misses_half_2026_11_14
description: "Does the prompt store's correction flag find the author's corrections? Under half (14 Nov): 14 of 20 unflagged candidates were corrections; four phrase families would add about 480 at five in six; the fold is right 20 of 20; the writing cards hold the author's writing corrections"
metadata:
  node_type: memory
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T00:16:41+02:00
  status: provisional
  evidence: ""
  modified: 2026-11-14T00:38:46.643Z
---

Does the author-prompt store's correction flag find the author's corrections? Under half of them (14 Nov 2026, an agent, read-only audit of an agent's owner_prompt_subconscious).

- The fold is right: 20 seeded records recounted in PROMPTS.jsonl by the store's own rule, count and first and last time agree 20 of 20.
- The correction flag (a phrase list in build.py, 238 of 15,087 records) misses more than it finds: of 20 unflagged records with a correction-like word, 14 were corrections when read. Four phrase families would add about 480 records at about five in six on a read of six each: "is/was/looks/still wrong" (113), a prompt that opens with "no" (343), "that is what i asked/wanted/meant" (6), "stop with/using/making/asking" (25). "i don't want", "be careful", "what went wrong" and "over and over" are too loose (three in six or worse).
- The writing cards ([[writing_brain_card_patterns_audit_fitted_test_vs_shelf_false_alarms_2026_11_13]]) hold the author's explicit writing corrections: two phrase nets over the store found 76 uncarded candidates, 57 read, six about writing, and five of those are second sayings of a rule that has a card. One rule had no card: report in the quantity the author thinks in, not the code's parameter (the author's 29 Jul 01:25 prompt).
- So a simple writing mistake that reaches the author is more likely a card not served or a page check not run than a missing rule. Not yet measured.

UPDATE 14 Nov 02:00, counted again on the builder's 01:22 build (an agent widened the phrase list after the first audit): flagged 723 of 15,060 (was 238 of 15,087). 358 unflagged prompts with a correction-like word remain; of 20 drawn (seed 91) 8 were clear corrections, 4 were standing rules that open "i don't want", 8 were neither. So the miss rate among the leftover candidates fell from 14 in 20 to 8 in 20, on a pool about a third the size. Writing prompts flagged: 51 of 1,727. A build takes 958 s (312 s reading the 262 MB ledger, 494 s building nodes). The builder has agreed to add the missed shapes, a separate rule flag for "i don't want X", and a tail-read build; new counts are theirs to send. Re-count: AUDIT_section9_prompt_store_recount_1114.md in the same folder. The "under half" in this memory's name describes the first build, not the current one.

Report with the table, the author's exact words for the four second sayings and the proposed card: 12_cognitive_architecture/loops/agent_fork_1113/AUDIT_prompt_store_and_card_coverage_1114.md. Tools there: ps_audit.py (modes shape, fold, missed, phrases, nocard), ps_pick.py.

**Why:** the author's 13 Nov 23:33 word: the Fable agents audit what the other agents built from the author's prompts.

**How to apply:** a flag built from a phrase list is audited from the unflagged side: draw records the flag passed over that carry a weaker cue, read them, and count. Its precision on the flagged side (10 of 10 here) says nothing about what it misses. Before proposing a wider phrase, read samples of what it would add and give the count read beside the rate.

