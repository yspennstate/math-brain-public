---
name: word_slot_sense_check_margin_does_not_separate_keep_it_2026_11_15
description: "[PROVISIONAL] word_slot ends 'every candidate failed the sense check'? Not a bug: the margin (word_walk show, <=4 passages a word) ranks good swaps below bad ones; keep the check"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T03:57:35+02:00
  status: provisional
  evidence: ""
---

On 15 Nov, six of twenty third-set sentences (refusing, controlled, team, alive, nearby, dipped) ended with every candidate failing word_walk's show() margin check. bench/show_margin_probe.py (creative/, json _1115) recorded the nine words it set aside: three keep the meaning by my reading (decline, contain, plunge) and six do not (check, squad, live, nigh, close, souse). The good three had margins -0.09 to -0.19, the bad six mostly -0.01 to -0.06, so a looser margin lets bad words in first. Cause of the noise: usage.json keeps at most four passages per word, so each word is judged on 3-8 shelf sentences, and the margin is against the best of up to 15 rival senses. **Why:** loosening the check looks like the fix and is not. **How to apply:** leave MARGIN at 0 and the refusal in place; a real fix needs more passages per word in usage.json (dictionary lane, read only for creative/), then re-run the probe. Labels are mine (in-sample), not a referee's. Related: [[same_synset_offers_keep_meaning_word_slot_draws_from_them_2026_11_15]], [[zipf_floor_fails_held_out_swaps_wrong_sense_is_the_fault_2026_11_15]].
