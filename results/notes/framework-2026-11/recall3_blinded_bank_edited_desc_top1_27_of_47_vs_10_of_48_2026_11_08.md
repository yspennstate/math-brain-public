---
name: recall3_blinded_bank_edited_desc_top1_27_of_47_vs_10_of_48_2026_11_08
description: "Yes (8 Nov): on 120 questions written blind to descriptions, the 47 RECALL1b-rewritten memories hit top-1 27/47 vs 10/48 controls (p 0.0003); same groups were 6/47 vs 9/60 before"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T10:05:25+04:00
  status: verified
  evidence: "~/codex_fleet/20261108_pro/workers/RECALL3s/GROUP_SCORES_BASELINE.json"
---

Do the RECALL1b description rewrites help recall on questions their writer never saw? Yes (8 Nov 2026). A second Codex worker, RECALL3 (gpt-6.1-sol high), wrote 120 questions from memory bodies with descriptions and file names stripped (40 typo'd). With the 47 rewritten descriptions live, one single-wording `brain.py recall` per question gave top-1 27/47 for the edited memories against 10/48 for untouched controls (top-5 36 vs 19, top-20 42 vs 29; Fisher two-sided p 0.0003, 0.0004, 0.002). The comparison is across memories, not paired, but before the edits the same 47 scored top-1 6/47 and the controls 9/60 on RECALL1's bank, so the edited group had no head start. 25 memories re-described by W114 the same morning sit between, 9/25.

So the question-lead descriptions are not only a same-writer artifact ([[recall1b_question_leads_top1_6_to_31_of_47_same_writer_2026_11_08]] was the upper bound). Worth doing for more memories: a description that states what a question about the memory would ask moves it from rank 4-ish to rank 1.

Caveat: RECALL3's own audit voided the bank under its path rule, because the AGENTS.md startup ritual read ~/.claude/compute/compute_state.json first ([[codex_agents_md_wake_ritual_breaks_blinded_briefs_2026_11_08]]). Its command log shows that file holds load numbers and process names only, and nothing else outside its folder was read, so the bank is used with that stated.

Where: ~/codex_fleet/20261108_pro/workers/RECALL3 (bank, private), RECALL3s (run), RECALL1b/score_groups.py; ranks and README in 12_cognitive_architecture/brain_improvement/recall3_2026_11_08/.

