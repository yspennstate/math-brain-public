---
name: word_palette_blind_test_plain_beats_palette_2026_11_15
description: "Does handing a writer a palette of less common dictionary words that fit the brief make better pages? Blind A/B on 40 briefs: plain 16, palette 10, ties 14 under Opus judges; 15-15-10 under Codex judges; both put the palette pages slightly lower on sense. A sham that swapped three words for rare synonyms lost 10 of 10."
metadata:
  type: project
  created: 2026-11-15
  status: provisional
---

The writing brain has a dictionary and a word walk meant to push writers toward words they would not have reached
for. This was the first blind measure of that push.

Design. A Codex writer wrote 40 briefs (documentary narration, story, poem, paper paragraph) twice: arm A plain,
arm B with a palette of less common dictionary words that fit the brief. Twenty fresh Opus 5.5 judge sessions, with
no tools and no hooks, read every pair in both orders; a pick that flips with the order is a tie. A sham arm swapped
three content words of a plain page for rare synonyms. The order key was held outside the repository, with its
sha256 published beside the judging files.

Result (Opus judges): A 16, B 10, ties 14 (B won 10 of 26 decided pairs, binomial p 0.33); sense score B minus A
-0.30 (p 0.07). By form: documentary A 5 B 0, story A 6 B 7, poem A 4 B 1, paper A 1 B 2. The sham lost 10 of 10,
sense -1.3 (p 0.002): judges notice rare words and mark them down. Text 2 was picked 58 of 100 times, so a few ties
are position picks.

Second judge family (Codex, same prompts): A 15, B 15, ties 10; sense B minus A -0.16 (p 0.02); the sham again lost
10 of 10. The two families gave the same verdict on 25 of 40 pairs (about 13 expected by chance, kappa 0.44). Codex
also wrote the pages, so that family is not independent of the writer.

How to apply: do not make a word palette a default for narration or for the writing hook; it leans worse, most of
all on documentary narration. A smaller, story-only palette is the one variant still worth testing.

Related: [[story_palette_blind_test_no_effect_lean_is_length_2026_11_15]],
[[word_page_check_blind_test_no_effect_2026_11_15]],
[[word_slot_three_offers_writer_judges_70_of_80_2026_11_15]].
