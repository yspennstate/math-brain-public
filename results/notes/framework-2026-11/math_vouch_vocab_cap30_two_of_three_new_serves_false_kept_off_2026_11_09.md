---
name: math_vouch_vocab_cap30_two_of_three_new_serves_false_kept_off_2026_11_09
description: "No (9 Nov): cap-30 vouch vocab serves 3 of 2030 new archive prompts, 2 false fires; banks identical; kept off"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T00:31:18+04:00
  status: verified
  evidence: "vouch_stage2_cap30_all.out, vcap30.summary, pb_vcap30.summary"
---

Does a bigger vouch vocabulary (cap 30, 10,174 terms against the live 6,611) earn its place in the math hook? No (9 Nov 00:3x, an agent): it is kept off.

What it bought: two probe prompts now get the right card first (intermediate value theorem; tail event -> Kolmogorov zero-one law). What it cost: across all 2,030 archive prompts the bigger vocab newly vouches for, it served 3, and 2 of the 3 were false fires (an options-data subscription paste got a Clark-Ocone lookback-hedging card; a security-approval note got a stray "dossier fresh rerun verification" card). The third, a random-matrix singular value question, was right. An earlier 200-prompt sample served none, which hid the false fires; only the full pass found them.

Banks did not move at all: the 218-item hookpath bank kept the same ids on every item (q_content served 65/89, rank-1 50, false fire 20/40, as live), proof banks 27/32 and 51/57 as live, must-stay-silent probes 6/6. The birthday and coin-flip probes stay silent even with the bigger vocab, so their misses are upstream (math gate, coverage prefilter), not vocabulary.

Recipe if someone retries: vouch_vocab_caps.py with max_neg_df 30 on the live built_from settings; scored by vouch_stage2.py 30 5000 and the hookpath/proof-bank evals with MATHBRAIN_VOUCH_VOCAB pointing at the candidate. A retry would need a guard against the two false-fire shapes (product-page pastes, ops/security prose) before it could win. Per-item outputs sit in local_keyed (hookpath_vcap30.jsonl, pb_vcap30.json); the archive prompts stay private.

Related: [[math_semtie_margin_tiebreak_1_up_2_false_fires_2026_11_09]] (the same night's other kept-off change, same +gain/+false-fire shape), [[math_sense_heals_vector_gap_itself_2026_11_09]] (the first cap-30 run was spoiled by a vector gap and rerun).

