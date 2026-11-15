---
name: word_slot_preposition_warning_fails_held_out_2026_11_15
description: "[PROVISIONAL] word_slot swap needs a preposition (compensate for)? The shelf habit rule (verb_preposition.py, share 0.25, 'of' left out) flagged 9 bad/1 good in-sample but 6 bad/1 good of 76 on a fifth held-out set = base rate; kept only as a printed fact. Bench runs must use a fresh agent (word_walk ledger)."
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T04:33:35+02:00
  status: provisional
  evidence: ""
---

Measured 15 Nov 04:2x-04:33 by an agent. In-sample (156 labelled pairs, four sets): 9 bad, 1 good flagged. Held-out fifth set (bench/fifth_score_1115.md): 6 bad, 1 good of 76 pairs with 11 good overall, so no separation; it missed dispose for sell (needs 'of'). word_slot keeps the meaning in about 1 of 4 picks across five sets (clean reruns: 2/7, 1/5, 2/7). word_walk gives an already-offered word a quarter weight per agent, so a bench run under a reused agent name is skewed; bench/rerun_set.py and ws_bench.py now use fresh agents. What would change this: a rule tested on a sixth set that beats the base rate. Commits b8c47bf58a9a, 945d43d9ff1c, c93b2a84e500 on brain-repo. Related [[word_slot_sense_check_margin_does_not_separate_keep_it_2026_11_15]] [[zipf_floor_fails_held_out_swaps_wrong_sense_is_the_fault_2026_11_15]]
