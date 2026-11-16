---
name: d1_last_15_closed_session_effort_predicts_no_reuse_12p0_vs_13p1_d1_48_2026_11_08
description: "[VERIFIED] No (8 Nov): D1 #48 session effort does not predict reuse; memories after the heaviest 2 h of work are read later 12.0% vs 13.1% (p 0.58). D1's other 14 open items were already answered; #51/#70 decay lives in coactivation_end.py, #93 index compaction is built"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:54:41+04:00
  status: verified
  evidence: "w08_checks/d1_48_session_effort_vs_reuse_2026_11_08.py, 19 Mac sessions 2,012 memories 28 Oct-5 Nov; coactivation_end.py; brain.py _maybe_compact_index"
---

At 07:47 on 8 Nov, the open-items check listed 15 Domain 1 items as unrecorded: 2 5 9 15 42 48 51 52 55 64 70 72 77 86 93. By 07:54 all were closed. One needed a new measurement (#48). The rest already had an answer on a card or in code.

**#48 effort-based encoding: no premise, not built.** The idea is that a memory written after a long, hard session encodes stronger. It pays only if those memories get reused more, and they do not. I took 19 Mac sessions that have a transcript here, with 2,012 memories written from 28 Oct to 5 Nov. 12.9% were read by another session within 3 days.
- Whole-session tool calls: the top quartile was read 11.6% of the time against 16.0% for the rest (permutation p 0.18).
- Wall hours: 13.3% against 12.6% (p 0.83).
- Sessions here run for days, so the sharper test is the effort right before each memory: tool calls in the 2 hours before it, ranked within its own session. The top quartile was read 12.0% of the time (61 of 507) against 13.1% (196 of 1,498), p 0.58 with within-session shuffles.
- Over 28 Oct to 1 Nov with a 7-day window: 13.2% against 14.7%, p 0.55.

The sign is slightly negative every time and never significant. This is the same answer as [[read_burst_sessions_yield_no_more_reused_memories_d3_12_2026_11_01]] and [[salience_capture_boost_predicts_nothing_2026_10_30]]: features of the moment of writing do not predict reuse. Script: d1_48_session_effort_vs_reuse_2026_11_08.py. Its control gives p 0.98 and 0.50 for random splits.

**#51 nightly SHY downscale and #70 one-shot prune: built, in coactivation_end.py.** The 30 Oct first-list line in 1000_ways_mac_status.md credits reactivation.py, but that file only reads coactivation.tsv. The decay lives in coactivation_end.py: a global decay by elapsed time with a 0.5 floor, in place since 26 Sep. A link seen once lasts one half-life and is then pruned, which is #70's one-shot prune. [[coactivation_support_not_stored_12_multi_session_edges_no_input_d9_78_2026_11_01]] measured it: with no input, 11 edges remain after 14 days and none after 28.

**#93 load-triggered pruning: built for the index, ruled out for the corpus.** After a remember, once MEMORY.md passes 22,000 bytes, brain.py _maybe_compact_index runs compact_index.py. That brings the file down to its 16,000-byte cap by moving old rows to INDEX_ARCHIVE.md, so nothing is lost. At 07:50 the file was 18,931 bytes, inside the band. Pruning the memories themselves goes against the author's order that brain data is never deleted.

**Answered under other cards:**
- #2 by [[rereads_already_space_out_x1p4_but_79pct_are_read_once_d3_21_2026_11_01]].
- #5, #9, #15 and #86 all need a language-model dream pass, which the Mac does not have: [[mac_dream_has_no_llm_pass_so_dream_prompt_items_have_no_host_d1_16_2026_11_01]], which names #15. #9 is also covered by [[gisting_does_not_crowd_out_old_members_reads_0p30_vs_0p43_p0p74_d2_92_2026_11_01]] and [[rem_replay_already_52pct_full_charge_vs_sws_43_corpus_28_d3_32_2026_11_01]].
- #42 by [[surprise_gain_reaches_0p5pct_of_memories_replay_flat_in_bits_d3_3_2026_11_01]] and [[surprise_day_memories_reread_6p4_vs_8p5_no_month_sign_d4_12_2026_11_02]].
- #52 by [[retrieval_induced_forgetting_has_no_choice_signal_1pct_decided_d3_89_2026_11_01]] and [[recall_already_folds_losers_onto_winners_16_stale_of_211k_slots_d3_42_2026_11_01]].
- #55 and #77 by [[near_duplicate_memories_are_5pct_and_cost_recall_0_of_317_slots_d1_20_2026_11_01]]; #77 also by [[covered_scar_discount_frees_slots_for_other_memories_not_scars_d3_09_2026_11_01]].
- #64 by [[vivid_count_ratchets_on_rule_memories_but_nothing_reads_it_d3_70_2026_11_01]].
- #72 by [[oldest_reflexes_fire_most_and_are_least_precise_23_vs_35pct_d7_43_2026_10_31]] and the parked W112 (g) fire-mute.

Sibling batch: [[d8_last_13_answered_in_text_or_moot_rewrites_stopped_after_aug_2026_11_08]].

