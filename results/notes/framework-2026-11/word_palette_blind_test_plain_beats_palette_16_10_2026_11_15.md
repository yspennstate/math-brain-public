---
name: word_palette_blind_test_plain_beats_palette_16_10_2026_11_15
description: "[PROVISIONAL] Rare-word palette for writers: does it help? Blind A/B 15 Nov: no palette 16, palette 10, ties 14; rare-swap sham lost 10/10; keep it off narration"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T16:31:35+02:00
  status: provisional
  evidence: ""
---

Word-palette blind test, 15 Nov 2026 (writing_brain/dictionary/blind_palette, result commit 2c0eb01c). Codex wrote 40 briefs twice: arm A plain, arm B handed a palette of less common dictionary words that fit the brief. 20 fresh Opus 5.5 judges (no tools, hooks off) read every pair in both orders.

Result: A 16, B 10, ties 14 (B 10 of 26 decided, binomial p 0.33); sense B-A -0.30 (p 0.07). Documentary A 5 B 0; story A 6 B 7; poem A 4 B 1; paper A 1 B 2. Sham (three content words swapped for rare synonyms) lost 10 of 10, sense -1.3 (p 0.002): the judges catch rare words and mark them down. Text 2 was picked 58 of 100, so a few ties are position picks.

**Why:** the author asked (14 Nov 07:34) for a dictionary and a random walk pushing agents toward words they would not have used. This is the first blind measure of the push.
**How to apply:** do not wire a word palette into narration or the writing hook as a default; it leans worse, most on documentary narration. Only a story-only, smaller palette is still worth testing. Key held outside the repo (writing_brain_data/dictionary/blind_palette_key.json, sha in judging/KEY_SHA256.txt). Related: [[word_slot_three_offers_writer_judges_70_of_80_vs_keep_41_2026_11_15]], [[zipf_floor_fails_held_out_swaps_wrong_sense_is_the_fault_2026_11_15]].


Second judge family, 15 Nov 19:2x: Codex gpt-6.1-sol read the same 20 prompts (no commands, hooks off): A 15, B 15, ties 10; sense B-A -0.16 (p 0.02); sham lost 10 of 10 (sense -0.75). Same verdict as Opus on 25 of 40 pairs (about 13 by chance, kappa 0.44). Still no detectable effect, and both families put the palette pages slightly lower on sense. Codex wrote the pages too, so it is not independent of the writer. Record: blind_palette/judging/codex/.
