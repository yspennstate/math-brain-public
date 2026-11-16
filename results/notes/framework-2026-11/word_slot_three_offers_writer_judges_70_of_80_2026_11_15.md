---
name: word_slot_three_offers_writer_judges_70_of_80_2026_11_15
description: "word_slot prints three replacement offers for a flagged word. Does a writing agent choose well among them, or keep its own word? A blind Codex judge was right on 70 of 80 labelled decisions against 41 for always keeping the word (sign test p < 0.001), and its swaps were right 32 of 35 times. So the tool prints a list for the writer to judge rather than picking a word itself."
metadata:
  type: project
  created: 2026-11-15
  status: provisional
---

Earlier probes showed that the right word is on word_slot's three-word list about half the time, and that no
automatic sense check separates the right offer from the wrong ones (AUC about 0.52). The question here was whether
the writer's own judgement does that job.

Design. A Codex judge was given only the text word_slot prints for 83 sentences: the sentence, three draws, a gloss
for each, and a line from the shelf using it. For each sentence it chose an offer or kept the original word. The
labels (which choice was right) had been written beforehand.

Result: right on 70 of 80 labelled decisions. Baselines on the same rows: always keep 41, a random offer 27, the
first offer 26. Paired against always-keep, 32 rows were right only for the judge and 3 only for keep (sign test p <
0.001). Its swaps were right 32 of 35 times; it kept its word on 7 of the 39 rows where an offer was right.

A second Codex judge on a second set (the same offers plus the closest shelf line under each flagged offer) was right
on 67 of 80, took the same word as the first judge on 80 of 83 rows, and used the flag the same way, so the extra line
was dropped.

How to apply: word_slot keeps printing a list. A writer using it reads each offer's gloss against the sentence and
takes one only when the sense fits; keeping the original word is right more often than not.

Limits: the labels are one model's, so this measures agreement between models, not a human verdict; two judges on one
set of 83 sentences.

Related: [[word_slot_sense_check_margin_does_not_separate_keep_it_2026_11_15]],
[[word_slot_common_rule_wins_list_loses_after_sense_check_2026_11_15]].
