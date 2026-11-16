---
name: diag21_brain_48q_beats_grep_claude_13_codex_ties_1_of_72_2026_11_09
description: "[PROVISIONAL] Claude yes, Codex no (DIAG21): fresh items, eachhi 48q vs grep over same memories: Claude 36 vs 23 (+13, meets bar 9), Codex 45 vs 44 (+1); Claude grep never listed file names, Codex grep did"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T06:43:02+04:00
  status: provisional
  evidence: "the private brain repository 08b2413a0f 12_cognitive_architecture/brain_improvement/DIAG21_20261109; prereg 2928210097"
---

On fresh items, the brain arm with the 48-question advice beats grep over the same memory copy for Claude, and only ties it for Codex.

DIAG21 (9 Nov 2026, runs ended 06:34): 12 new two-cause plants plus DIAG4's 6 controls. Budget 10 tool calls and 1200 s. Store brain-graph-full-2026-11-07 (11,982,982 directed + 4,828,684 co pairs = 16,811,666 edges), live sidecar walk. Three runs per arm per runtime. Plant points over valid runs are scaled to 3 runs, of 72; the bar is 9.

- Claude (opus 5.5 high): bare 4, eachhi 36, grep 23. eachhi - grep = +13 (8 items higher / 2 lower / 2 tied): MEETS BAR. Strict line (the one name-only leak hit voids its run): +10, still meets.
- Codex (gpt-6.1-sol high): bare 2, eachhi 45, grep 44. eachhi - grep = +1 (4/3/5), inside the bar.
- Controls 18/18 in every arm. All six eachhi runs complied with the advice (62-78 questions). Planted notes surfaced: Claude 12/16/10 of 24, Codex 16/16/20.
- The prereg predicted Claude about +4 and Codex about +2. Codex matched; Claude was off by 9.

Why Claude's margin exists (an observation, not tested): Claude's grep arm is weak (23 against Codex grep's 44), while the brain arms are closer (36 and 45). Every Codex grep run began with `rg --files` over the whole memory copy, putting 1.4-2.4 MB of transcript into the full list of descriptive file names, which works as an index. No Claude grep run printed the full name list; it grepped bodies with keyword patterns. The next test: tell Claude's grep arm to list names first. If its score jumps to Codex's level, the brain's Claude win is over a habit, not over the memory copy.

Judging: one judge, blind to arm. Item rulings were fixed before the runmaps were opened. Marks hashed 06:38: codex_judged 0d05b1022b7d33e8, claude_judged c1f9d89bb3dddb9d, JUDGING 7399cfe7a7f0bffc. Results recomputed three ways: score21.py, the key-free score21_rows.py over rows21.tsv, and raw mark sums (Codex 91 = 2+45+44, Claude 63 = 4+36+23).

Side lesson: zsh does not word-split `$F`, so `scan_secrets.py $F` with a multi-line list passes one argument. It fails as FileNotFound (relative paths) or errno 63 (name too long). List the files or use `${=F}`.


Follows [[diag17_fresh_draw_recall_beats_bare_loses_to_clean_grep_50_40_37_28_2026_11_09]] (grep won then) and [[diag20_asking_48_plus_beats_default_claude_5_codex_3p5_of_54_below_bar_2026_11_09]] (where the 48-question advice came from); the question-count effect is [[diag19_question_cap_16_costs_claude_12_codex_10_of_54_2026_11_09]].
