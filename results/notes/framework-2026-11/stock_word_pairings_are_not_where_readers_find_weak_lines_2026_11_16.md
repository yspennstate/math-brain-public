---
name: stock_word_pairings_are_not_where_readers_find_weak_lines_2026_11_16
description: "[PROVISIONAL] Warn a writer off shelf-common word pairings (cliche check)? No: on six blind-reader sets of chapter one such sentences were LESS often weak (OR 0.46)"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T02:13:24+02:00
  status: provisional
  evidence: ""
---

Rule fixed first (bench/phrase_df_vs_readers.py, commit 1f28931b4fd4): a sentence scores the shelf df of its commonest consecutive content-word pair (phrase_df.py); flag at the text's 90th percentile; strata set x length bin. 329 flags, 11 on a reader-weak sentence against 21.25 expected, MH OR 0.46, one-sided p (fewer) 0.006; precision 3.3 pct against a 6.4 pct base. The six sets are near-copies of one chapter, so the p is a guide. Unplanned lead: among 8-11 word sentences 86 pct of the weak ones have no pairing the shelf has seen three times, against 50 pct of the rest; the gap reverses at 19-25 words. So do not build a 'too familiar' warning on phrase_df; test 'short sentence with unseen pairings is weak' on a second book's reader notes with the rule fixed first. Related [[summing_up_flag_is_not_a_length_proxy_2026_11_16]], [[reader_checks_vs_blind_readers_only_maxim_finds_2026_11_15]].

Held out (16 Nov 02:2x, unseen_pairs_heldout.py, commit f11e60ef89bf): on the two CH1C2 reader sets only 2 weak sentences were 8-11 words; 1 unseen vs 1.06 expected, OR 0.88, p 0.78. The unseen-pairing lead does not hold by the fixed rule, and the run is near-powerless: treat the lead as unproven.
