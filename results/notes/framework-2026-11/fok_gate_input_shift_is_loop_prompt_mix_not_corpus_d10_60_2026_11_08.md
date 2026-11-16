---
name: fok_gate_input_shift_is_loop_prompt_mix_not_corpus_d10_60_2026_11_08
description: "Not from the corpus (8 Nov): fok's concentration-pass share fell 26-32% to 0% and median s1 235 to ~50 while the corpus grew up to 18k files, but 7 Nov was 172 of 250 rows on one compaction node from loop prompts; gates are ratios; no guard built"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:36:13+04:00
  status: provisional
  evidence: "fok_strength.tsv 3,882 rows by day; 7 Nov 6 sessions 6 slugs; 0 of 3,882 s1 under 30; no policy.json/learn_state.json in brain_graph/live"
---

Question: has fok_probe's gate drifted as the memory corpus grew, and does it need a snapshot-drift guard (D10 #60)?

Not from the corpus, as far as the log shows (8 Nov, provisional). The gate was tuned around 1 Nov (S1_MIN 30, CONC_MIN 1.9, RARE_MIN 0.6). Since then up to 18,110 of the 47,113 memory files are new (a birth-time count, so an upper bound; the BM25 index holds 47,101). fok_strength.tsv does move a lot by day. Median s1 fell from 235 on 3 Nov to about 50. The share of rows passing the concentration gate (s1/s10 >= 1.9) went from 26-32% to 0% on 7 Nov, and the median rare share rose from 0.50 to 0.88. Read alone, that looks like cue overload from a bigger corpus.

It is the prompt mix. On 7 Nov the 250 rows came from 6 sessions naming 6 memories, and 172 of them named one memory: 9f257a7a's compaction node, matched again and again by 5-minute loop prompts that the node quotes. The gates that decide are ratios, which a larger N barely moves, and S1_MIN 30 sits below all 3,882 logged s1 values. No auto-tuner runs on this Mac either: the recall weights in brain_graph_dial.json are hand-set with dated reasons, and graph_learn writes no policy.json or learn_state.json here. So no guard was built.

Not done: a replay of fixed probe prompts against the corpus as it stood before 1 Nov, which is the test that would settle corpus drift on its own.

How to apply: before reading a day-by-day shift in a hook's own log as drift, count distinct sessions and distinct targets for that day. A loop session repeats one prompt and can fill a day by itself. Also a lead for D1 #65's follow-up ([[fok_fires_under_competition_s1_s10_below_1p61_right_51pct_vs_91_d1_65_2026_11_01]]): loop sessions make fok fire through the weaker rare-word gate, on another session's compaction node. Related: [[fok_note_command_failed_on_mac_now_node_slug_1_of_139_d10_69_2026_11_08]].

