---
name: word_page_check_blind_test_no_effect_12_13_2026_11_15
description: "Word-walk page check handed to a reviser: does it help? No: blind 40 pairs R 13, P 12, ties 15, sense +0.03; it moved ~8 words in 40 pages. Use as an editor's flag, never show its offers as replacements"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T18:50:05+02:00
  status: provisional
  evidence: ""
---

Handing a writer the `word_walk.py page` list (habitual and repeated words, each with near words) while revising a draft made no detectable difference in a blind test, 15 Nov 2026 (lane H, an agent).

Design: the 40 no-palette drafts of the palette test, each revised once by Codex gpt-6.1-sol (high, normal speed) in two arms, R (plain revise) and P (revise with the check's list, "use any of it only where it makes the sentence better"). Sixteen fresh Opus 5.5 judge sessions read each pair in both orders; a pick that flips with the order is a tie. Rule fixed before the run: helps at P >= 28 of 40 with sense not below -0.25; hurts at R >= 28 or sense < -0.25 at p < 0.05.

Result: R 13, P 12, ties 15; sense P minus R +0.03 (sign-flip p 0.91). No detectable effect. By genre story 5-2 for R, documentary 5-1 for P, poem 4-2 R, paper 3-3: noise at this size. Judges picked Text 1 in 51 of 80 (position bias, absorbed by the two-order design).

Why it is inert: the check flagged 100 word occurrences in 40 drafts; R left 93 in place, P 85; P took an offered word 4 times, R 2 by chance. Both arms changed about 9 pct of words. The list moved about eight words in forty pages.

How to apply: use `page` as an editor's flag (it names words like somewhere, nobody, inside, someone that may be cut), never show its near-word offers as replacements; they are often off sense (rope -> roach, animal -> female). Together with the palette test (plain beat palette 16 to 10, [[word_palette_blind_test_plain_beats_palette_16_10_2026_11_15]]) the word walk has not yet helped a page in a blind read.

Second judge family (Codex gpt-6.1-sol, same 16 prompts, 15 Nov 19:0x): R 16, P 10, ties 14, sense P-R -0.08 (p 0.32); same verdict as Opus on 25 of 40 pairs (about 13 by chance, kappa 0.44). No effect under both families; Codex also wrote the revisions, so it is not independent of the writer. Record blind_page/judging/codex/. What would change it: a story-only test at a larger n, or a third family that did not write the pages. Record: writing_brain/dictionary/blind_page/ (PLAN.md Result section, judging/RESULT.json), pushed commit 17793d113ca5; order key kept local at writing_brain_data/dictionary/blind_page_key.json.

