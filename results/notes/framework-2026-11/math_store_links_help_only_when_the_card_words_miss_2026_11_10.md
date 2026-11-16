---
name: math_store_links_help_only_when_the_card_words_miss_2026_11_10
description: "Do math-store links help recall? Not on the store as is (MRR .458 vs .457); when the answer card loses the question words, typed links (not semantic, not near-copies) recover 23.5% top-20 from 0, rewiring kills it; on REAL misses a neighbour side list rescues only 2-5 of 94, so not wired in (10 Nov, br300)"
metadata:
  node_type: memory
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T17:54:36+02:00
  status: provisional
  evidence: 06_math_research/graph_recall_51f2/results2.json
  modified: 2026-11-10T16:12:09.201Z
---

The math store's links carry real information about where an answer is, but on the store as it stands the card's own
words already find everything the links would. Links pay only when the answer card's words miss the question.

Measured 10 Nov 2026 on the live store (94,329 cards, 166,756 links), br300 card-id items (221; dev/test split by item
hash, test n=119). BM25 over title+body[:3000]; one hop s1 = s0 + alpha * mean of neighbours' s0; alpha chosen on dev.
Code and numbers: 06_math_research/graph_recall_51f2/ (harness.py + results.json, harness2.py + results2.json).

- Store as is: no gain (test MRR .458 -> .457). Same as the 15 Oct 79 vs 80 and the 8 Nov top-8 result.
- Gold card's 3 rarest shared words removed: top-8 .261 -> .303, top-20 .294 -> .345.
- Every question word removed from the gold card: text alone 0/119; with links top-8 .185, top-20 .235 (alpha 10).
- Same arms with links rewired (targets shuffled, degrees kept, 3 seeds): no gain at all. Paired vs rewired: 117 better,
  2 worse.
- Not near-copies: dropping the 17 gold-to-near-copy links (token Jaccard >= .6; 14/200 gold cards have one) changes
  nothing.
- Not the semantic links: without semantic_association links top-20 is .244 (same or better); semantic links alone .168.
  The typed links (depends_on, cites, analogous_to, fails_under ...) carry it.

How far to trust it: one bank, one store, test n=119. Dev picked alpha 10, the top of the grid, where the ranking is
effectively by the neighbours' text alone, so the masked-arm gain is "find the card whose neighbours match", not a
blend. The masking is synthetic: it has not been shown that real WEAK MATCH questions behave like masked cards.
What would change it: a run on real depth-0 misses (questions whose answer card ranks below 20 by text) that adds a
neighbour-score pass and finds nothing; or the same numbers failing on the public 1 Nov snapshot.

Run 3, same day (harness3.py + results3.json), the product test on REAL misses: 94 of 221 questions have the answer
card below rank 20 by text. A side list (cards outside the text top-(L-m), ranked by the mean of their neighbours' text
score) at equal list length rescues 3/94 (L 8, m 3), 2/94 (8, 2), 4/94 (20, 5), 5/94 (20, 10); rewired links rescue 0,
and a sum-of-neighbours side list rescues 0 (hubs win). Over all items the net is +1, +2, +1, 0 of 221: each side slot
pushes out a text hit. So the masked-card gain (0 to .235) does not carry over to real misses (about .04): on a real
miss the question's words are absent from the answer card's neighbours too.

Use: keep --depth 0 everywhere, including the WEAK MATCH path; rewording (15 Oct: 4 of 21 -> 49 of 79) does far more
than a neighbour side list. Not wired into math_recall.py. What would reopen it: a store whose links are denser around
the answer (learned or task-specific links), or a bank where most misses are vocabulary gaps on the answer card alone.
Research statement ('When do links help recall?'): this is the planted-topic prediction, seen on real data with the
vocabulary-removal and degree-preserving rewiring ablations.


Related: [[math_recall_what_works_agents_2026_10_15]] (depth 0 default), [[graph_structure_in_brain_recall_only_learned_links_move_the_top_8_2026_11_08]], [[brain_recall_two_mode_validated_2026_07_10]] (the memory-brain rewire).
