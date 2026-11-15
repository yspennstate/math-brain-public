---
name: zipf_floor_fails_held_out_swaps_wrong_sense_is_the_fault_2026_11_15
description: "[PROVISIONAL] Frequency (zipf) floor on word_slot swaps? No: AUC 0.72 on its own 46 labels, 0.49 on 63 held-out pairs (seed-23 bench); bad offers are common words in the wrong sense; slot pick good 1/10, walk first offer 4/16"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T01:05:42+02:00
  status: provisional
  evidence: ""
---

Writing brain, creative/ (an agent, 15 Nov 01:0x). bench/zipf_probe.py read the word's zipf from word_walk.Walk.zipf for every hand-labelled (slot, offered word) pair. First set (ws_labels.json, 46 pairs): AUC 0.72, floor 4.0 kept 10/12 good and 21/34 bad - but tuned on those labels. Held-out set (ws_bench.py collect 23 ws_bench_1115_heldout.jsonl, 18 usable sentences from other film scripts, ws_labels_heldout.json, 63 pairs, one reader): AUC 0.49, floor 4.0 drops 3/7 good with 19/56 bad. Not adopted; README says so (commit efe6a169eb48). What the held-out bad offers are: common words in the wrong sense (rubbish for attackers, train for tools, nose for survived), so the fault is sense choice, not register. word_slot's TYPICAL pick was good 1/10 there, word_walk's first offer 4/16: the pick drifts to an off sense (control->mortify, tool->muller, report->denote). Bench bug seen: the prefix match (w[:len-2]) takes moustache for mouse and through for throne - those rows were left out. Status provisional: one reader, small sets. Would change it: a third labelled set, or a second reader disagreeing. Next: why choose()/near_sense() pick the off sense. Links [[writing_brain_dictionary_and_word_walk_2026_11_14]] [[word_walk_links_senses_not_words_drift_fixed_2026_11_14]]
