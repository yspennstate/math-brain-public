---
name: word_slot_three_offers_writer_judges_70_of_80_vs_keep_41_2026_11_15
description: "word_slot offers: does a writer pick well among the three? Blind Codex judge 70/80 right vs 41 always-keep (p<0.001), swaps 32/35 right; keep printing the list"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T14:25:35+02:00
  status: provisional
  evidence: ""
---

A writing agent choosing among word_slot's three offers (or keeping its own word) beats always-keep by a wide margin. On 15 Nov a Codex gpt-6.1-sol judge, given only bench/judge_set_1115.jsonl (83 sentences, each with the text word_slot prints: three draws, glosses, shelf lines), was right in 70 of 80 labelled decisions, against 41 for always keep, 27 for a random offer and 26 for the first offer. Paired against keep: 32 rows right only for the judge, 3 only for keep, sign test p < 0.001. Its swaps were right 32 of 35 times; it kept its word on 7 of the 39 rows where an offer was right.

**Why it matters:** earlier probes showed the right word is on the three-word list about half the time, and that no automatic sense check separates right from wrong (AUC about 0.52). This says the reader's judgement does that job, so word_slot keeps printing a list for the writer to choose from instead of picking one word itself.

**How to apply:** when using word_slot, read each offer's gloss against the sentence and take one only if the sense fits; keeping the word is right more often than not. Limits: the labels are one model's (Claude's), so this is model-to-model agreement, not a human verdict; two judges on one set of 83 sentences. A second Codex judge on the 1116 set (same offers, plus the closest shelf line under each flagged offer) was right in 67 of 80, took the same word as the first on 80 of 83, and used the flag the same way, so the extra line was left out (pushed b659f5d27437).

Evidence: writing_brain/creative/bench/sense_check_1115.md (section "A writing agent judging the three offers"), picks bench/judge_picks_agent.jsonl, pushed ef25d749cc93. Related: [[word_slot_sense_check_margin_does_not_separate_keep_it_2026_11_15]], [[word_slot_common_rule_wins_list_loses_after_sense_check_2026_11_15]].

