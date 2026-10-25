# A graph lane for recall: diffusion over the use-grown graph, 26 September 2026

The brain records every touch an agent makes: which files and notes it read or wrote, and the words it said in the
minutes before. That record forms a graph. This test asked whether a walk over it, blended into the lexical (BM25)
recall of the memory notes, finds the right note more often than BM25 alone.

## The method

- **The store.** 4,821,823 events from 642 agent sessions over 40 days, with every test session removed (the
  headless question runners and every session that touched a test bank or its keys), so that no question or answer
  of a bank can leak into the graph. After keeping the 300 strongest edges per row: 113,205 nodes and 2,917,443 edges.
  8,451 of the memory notes are a node of some kind.
- **The walk.** Personalised PageRank. A context-to-target edge and a co-use edge weigh max(0, ln(P(j|i)/P(j))) x
  ln(1+n), co-use at half weight; rows are normalised; the walk restarts at the seed with probability alpha (0.3 or
  0.6). The seeds are the query's words, rarer words heavier, optionally with BM25's top five notes added. A lift
  parameter gamma (0, 0.5, 1) raises the weight of the strongest edges.
- **The blend.** One dial, lambda: 0 is BM25 exactly as before, 1 is the graph's order alone. Two fusions were tried,
  a convex mix of min-max scores and reciprocal-rank fusion.
- **The questions.** 948 pilot questions, one per memory note, each a rewording of what the note says written by a
  Haiku model, asked of the whole collection. 46.4% of the answers are graph nodes at all.

## Result

| arm | hit@1 | hit@5 | hit@10 | MRR | answers moved up / down |
|---|---|---|---|---|---|
| BM25 alone (lambda 0) | 257 | 412 | 481 | 0.352 | |
| best blend (words, alpha 0.3, gamma 1, convex 0.1) | 258 | 414 | 480 | 0.352 | 16 / 73 |
| words, alpha 0.3, convex 0.3 | 252 | 413 | 478 | 0.348 | 12 / 238 |
| words, alpha 0.3, convex 0.5 | 108 | 363 | 442 | 0.244 | 11 / 631 |
| graph alone, words | 3 | 4 | 5 | 0.007 | |

Across both restarts, all three lifts, both seedings and both fusions, no blend beat lambda 0. The best ones tie it
by moving a few answers up and more of them down. A one-hop word graph scored the same morning on a second held-out
bank of 968 reworded questions gave the same outcome: BM25 hit@5 0.344, the graph alone 0.003, every lambda above 0
lower. The dial's default is therefore 0.

Why it fails. The graph reaches a note only if an agent read it in the window, and what it knows about that note is
the words an agent happened to say just before reading it. BM25 reads the note's own text. Seeding the walk from
BM25's top notes mostly brings back what BM25 already had. What the graph does know is where work goes next: on a
walk forward through the real record it led the simple baselines in predicting the next project (+8.2 points at
hit@10), repository (+4.8) and folder (+3.4). That points it at the hook that loads context at the start of a task,
not at deliberate recall.

## Controls

- On a planted corpus, both directions (7 of 7): a folder plus a word ranks the expected note first; a word reaches a
  note two hops away through an intermediate one; a word with no history ranks nothing; the cached walk ranks exactly
  as the freshly built one; both fusions give the lexical order at lambda 0 and the graph's order at 1.
- On live recall, five queries with the BM25 index frozen: with the lane installed and lambda 0 the ranked rows were
  byte-identical to recall without it; at lambda 0.3, 26 rows changed.

## Files

`eval_lambda.json` holds every arm's numbers for every lambda and both fusions (counts and MRR only; no questions,
notes or answers). `python best_arm.py` reads it, prints the best blend and checks that none beats lambda 0.
