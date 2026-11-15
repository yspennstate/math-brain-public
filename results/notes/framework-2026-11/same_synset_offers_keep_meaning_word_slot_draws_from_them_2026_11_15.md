---
name: same_synset_offers_keep_meaning_word_slot_draws_from_them_2026_11_15
description: "[PROVISIONAL] Word swap keeping the meaning? Offers from the slot word's own synset kept it 9/23, hyponyms 4/27, broader 2/12, other 4/47 (109 labelled pairs). word_slot now draws only same-synset words when present + no verb after a preposition: held-out picks good 3/9 (was 2/11), in-sample."
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T01:33:15+02:00
  status: provisional
  evidence: ""
---

Measured 15 Nov 01:0x-01:3x by an agent (writing brain, creative/ lane), pushed 5cb43c7387e2 on yspennstate/brain-repo.

- bench/relation_probe.py over ws_labels.json + ws_labels_heldout.json (109 pairs): same synset good 9 of 23, kind-of (hyponym) 4 of 27, broader (hypernym) 2 of 12, other neighbour 4 of 47.
- word_slot.py: after the walk, if any candidate shares the synset of the sentence's sense (tied by gloss == OEWN synset definition, wn_relations.py, cache writing_brain_data/creative/wn_syn_hypo_hyper_v2.json.gz), draw among those only. Hyponyms kept because spurn/rebuff (good for refused) are hyponyms.
- infer_pos: a non -ing word right after a preposition is not a verb (under [control] had walked to 'temper').
- Rerun on the 18 held-out sentences (bench/ws_repick_1115.tsv): good 3 of 9 picks (assailant, beast, quicker) vs 2 of 11; abstains where it had picked exist and mortify.

Doubt: the held-out labels were used to find the rule, so this is in-sample; one reader labelled everything. What would change it: a third labelled set from new scripts. Still open: ws_bench prefix-match bug (moustache for mouse), sense_pick tie on 'reports' (sense 5 over 1). Related: [[zipf_floor_fails_held_out_swaps_wrong_sense_is_the_fault_2026_11_15]], [[word_walk_links_senses_not_words_drift_fixed_2026_11_14]].

Out-of-sample check, 02:0x 15 Nov (third set, seed 37, drawn after the rules were fixed, pushed 01c9bf813ec5): word_slot picks good 3 of 10 vs word_walk first offer 1 of 19; same-synset good 3 of 11 vs every other relation 1 of 18. The rule holds out of sample, weaker than in-sample. Two more POS rules (noun after one/two/both/...; -s form after an -ing/-ed word is a noun) were fixed on that set, so they are in-sample. WordNet example sentences stay in sense_pick: 13 of 22 right with them, 9-10 without (bench/example_words_probe.py), even though one shared word ('day') misread 'reports'.
