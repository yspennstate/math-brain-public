---
name: diag19_question_cap_16_costs_claude_12_codex_10_of_54_2026_11_09
description: "[VERIFIED] Yes (DIAG19): at most 16 questions vs at least 48 costs Claude 12 of 54 (7/1/1 items), Codex 10 primary (+7 with a falsely voided run back); never cap brain questions low; my in-range correlation prediction failed"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T05:12:46+04:00
  status: provisional
  evidence: "the private repository 33ad52d1de 12_cognitive_architecture/brain_improvement/DIAG19_20261109"
---

Question: does the number of questions an agent asks the brain drive the brain arm's score?

Yes for Claude, probably for Codex (DIAG19, 9 Nov 04:55-05:07; prereg 2473ba4ca1, results 33ad52d1de, 12_cognitive_architecture/brain_improvement/DIAG19_20261109). DIAG18's frozen items, key and budget (10 calls, 1200 s), on the full brain brain-graph-full-2026-11-07 (16,811,666 edges) with the live sidecar link walk. Two arms built from DIAG18's each arm: eachlo is at most 16 questions with the remaining calls spent on node reads; eachhi is at least 48. 3 runs per arm on each runtime (Opus 5.5 high, gpt-6.1-sol high). Every run complied: eachlo asked exactly 16, eachhi 53-56.

- Claude: eachhi 38 vs eachlo 26 of 54, +12, items 7 higher / 1 lower / 1 tied (sign test one-sided p 0.035). Bar 9: met.
- Codex: primary 31 vs 21 (eachlo had 2 valid runs), +10, 7/1/1, so it meets the bar. With the voided run put back it is +7 (6/1/2), below the bar. That void was a harness false positive: recall_over flags "subprocess" outside quotes, and the run's one node call named a slug containing that word. Fix before the next test: exempt the slug argument of brain.py node.
- Planted notes surfaced (of 18): Claude eachhi 14/15/14 vs eachlo 9/9/7. Points follow surfaced notes. Leakcheck was 12/12 clean, and a positive control (marker appended to a copied transcript) was caught.

Reading: the cap is what costs points. Node reads did not replace the questions given up. As a descriptive comparison, the old each arm (27-38 questions for Claude) scored about 34.5 of 54, so eachhi is at most slightly above the default. Codex's default already asks 37-56.

My sealed prediction (PREDICTION.txt sha 1319059cee175891: both below the bar) was wrong. I extrapolated from a weak run-to-run correlation inside 27-56 questions to a cap at 16, outside that range. A correlation inside the observed range says nothing about a dose outside it. For brain-arm prompts: never cap questions low, and spend the calls on distinct wordings.

Related: [[scar_extrapolation_past_measured_range_2026_07_08]] (the same trap, repeated here), [[diag18b_query_advice_six_runs_not_confirmed_2026_11_09]], [[leak_voids_4_of_11_were_name_hits_not_content_2026_11_09]].

DIAG20 follow-up (9 Nov): 48+ vs the default each arm, Claude +5, Codex +3.5 (+1.0 sensitivity), below the +9 bar; see [[diag20_asking_48_plus_beats_default_claude_5_codex_3p5_of_54_below_bar_2026_11_09]]. Claude's eachhi scored 38 in both tests.
