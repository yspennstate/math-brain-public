---
name: word_slot_common_rule_wins_list_loses_after_sense_check_2026_11_15
description: "[PROVISIONAL] word_slot: pick the most common kept word instead of the typical draw? Wins on candidate lists (20/47 vs 6/29, sixth set blind 3/10 vs 0/6) but run whole with the sense check 2/9 vs draw 3/9: draw stays default, --rule common kept. Score the whole pipeline, not the list."
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T05:34:48+02:00
  status: provisional
  evidence: ""
---

Measured 15 Nov 05:1x-05:3x by an agent (bench/synset_freq_1115.md, ws_labels_sixth.json).

A rule scored on word_slot's printed candidate list skips the sense check (W.show) that every real pick passes. The most common kept word led on the list on five in-sample sets and on a sixth set labelled before any rule was read. Run end to end it did not: it takes the commoner sense of a many-sense word (gross for visible), and when the sense check refuses a word the fallback walks to the next most common, often a kind of the word (ranch for farm, bun for bread). The same draw, same sentence and seed, gave 3 of 9 at collection and 0 of 6 on rerun, because word_walk reads the agent ledger: a gap of one or two on twenty sentences is noise.

How to apply: score a word_slot change on its final printed word under a fresh agent name, never on the candidate list. The loss is in the sense check (it refused provide for supply, close for nearby, both right), which is the next thing to measure. Would change with: a sense-check change that keeps right words on a held-out labelled set. Links: [[word_slot_sense_check_margin_does_not_separate_keep_it_2026_11_15]] [[same_synset_offers_keep_meaning_word_slot_draws_from_them_2026_11_15]]
