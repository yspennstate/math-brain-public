---
name: bt3_reserve_grep_35_of_48_fails_60pct_gate_word_rule_missed_bodies_2026_11_08
description: "Is the BT3 hunt bank hard enough for brain vs grep? No: Codex grep 35 of 48 reserve stations (73%) over the 60% gate; the word rule skipped memory bodies, so joins and corrections still grep in one hop; rebuild BT3B"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:51:37+04:00
  status: verified
  evidence: "~/.claude/compute/keys_private/bt3r_runs/RES2_grade.json"
---

Is the BT3 scavenger-hunt bank hard enough for a brain-versus-grep test? No (8 Nov 2026, reserve calibration, an agent).

A Codex grep arm (gpt-6.1-sol high, no brain, 12 commands enforced live) was credited with 35 of the 48 reserve stations (73 percent) and 4 of 12 full hunts.
The preregistered ceiling was 60 percent, so the bank goes back to be rebuilt. By the key's kind tags (raw right answers, counts only):
single 4/5, join 15/20, correction 6/8, recent 5/5, reason 3/5, sequence 3/5; station 1 was 12/12.

Why: the word rule (no 5+ letter word shared with the answering memory) covered only the description line and the file name.
Grep reads bodies. Two-memory joins and superseded-value corrections did not slow it down, because each hop was still a
word match. Same lesson as [[diag7_grep_32_recall_16_codex_17_15_agent_11_08]], where grep beat recall on Codex by reading slugs and bodies.

How to apply: a clue must share no 4+ letter word with ANY line of the memory that answers it (and, for a join, with memory A),
checked by grepping its rarest words. Calibrate on a reserve with a grep arm before any scored run. BT3B-BUILD (launched 15:3x)
does this; the next calibration is RES3. RES1 was void (controller KeyError 'station', no clues served).

Pushed baa26eaacf to 12_cognitive_architecture/brain_improvement/bt3_reserve_calibration_2026_11_08. Key and per-hunt rows stay in
~/.claude/compute/keys_private/bt3r_runs (counts only leave it). Before it: [[bt2_hunts_brain_beats_grep_on_claude_not_agent_11_08]].

