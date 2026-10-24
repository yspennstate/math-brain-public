# Tests

Each test runs agents on a fixed set of questions with and without the brain and counts correct answers. P values come from exact paired tests on the items where the arms disagree. The questions, the answer keys and the per-question records are kept private, so the tests can be run again on later versions without the answers having been seen. Anchors for some blinded experiments were committed in advance and are public: [brain-benefit-experiment-anchors](https://github.com/yspennstate/brain-benefit-experiment-anchors).

## Recall of results held in the store, 100 questions (11 October 2026)

Every question asks for a fact held in the store. Sixty were reworded so they share no words with their card; forty are plain. Codex agents (gpt-6.1-sol, high reasoning) took one question per session.

| Arm | Correct |
|---|---|
| no tools | 0 |
| the hook's served notes, no tools | 7 |
| text search over a copy of the store's files | 75 |
| recall tool (whole cards, ids, linked ids) | 83 |
| hook, recall tool and link walk | 82 |

The full stack against the recall tool alone went 2 to 3 (exact McNemar p = 1.0). The test had room to fail: 17 questions were wrong under the recall tool alone, so a net gain of about seven would have shown. Against text search the full stack went 10 to 3 (p = 0.09).

The hook was silent on 85 of the 100 questions, including all 60 reworded ones: its gate reads them as non-mathematical, and its search has no shared words to start from. On the 15 plain questions where it spoke, the full stack answered 11, the recall tool alone 9, text search 10 and the hook's notes alone 7.

The way results are printed decided much of the score. The same retrieval printing titles and 700-character snippets without ids scored 34; printing ids, whole cards and linked ids scored 83.

Cost, from the session logs:

| | Recall tool alone | Hook, recall and link walk |
|---|---|---|
| Input tokens, all questions | 186 million | 24.6 million |
| Uncached input tokens per question | 24 thousand | 13 thousand |
| Output tokens per question | 1.9 thousand | 0.4 thousand |
| Session-minutes | 666 | 78 |

About 98 percent of all input tokens were cached re-reads, so the saving in uncached input is 1.8 times, not 7.6. On the first 20 questions, with the same search tool in both arms, both scored 18 of 20; with the walk the sessions read 3.1 million tokens and made 40 searches, without it 16.9 million tokens and 55 searches. That comparison has two sessions an arm, so the size of the saving is uncertain, but it went the same way in every session. Agents walked 82 times alongside 273 searches, and no walk failed.

## Ranking on held-out questions (12 October 2026)

This test measures the retrieval engine and the recall tool without an agent: how often the answer card is among the first eight results, on questions that played no part in tuning.

| | Answer in the first eight |
|---|---|
| 584 questions, frozen copy from the morning | 298 |
| 584 questions, after the day's ranking changes | 317 (27 gained, 8 lost, p = 0.002) |
| six more question sets, 1,070 questions, morning copy | 891 |
| the same six sets, after | 1,018 (143 gained, 16 lost) |

The six sets moved unevenly: three gained 32, 44 and 66, two that were already near the ceiling with word search alone lost 9 and 7, and one gained 1. The ranking was tuned on questions written by Codex agents, and its largest held-out gain is on a set written by Claude agents. The gain comes from the ranking, BM25 with b = 0.4 and titles counted twice. The meaning channel adds about nothing here, and the cards added that day moved none of these counts.

## Files kept in GitHub repositories (12 October 2026)

The questions were drawn from little-known files in GitHub repositories, and Codex agents (gpt-6.1-sol, medium reasoning) answered them. A crash cut the run short. With git and the brain the agents answered 83 of 90 questions; with git alone, 76 of 90. On the 80 questions answered in both arms the scores were 73 and 68 (9 to 4, p = 0.27). The brain arm read 14 percent more tokens per question and 6 percent more per right answer, and both arms had the same share of cached input, about 98.8 percent.

## Solving and auditing, 61 items (5 and 6 October 2026)

Claude Sonnet agents worked each item with Python, Lean and file tools for up to 600 seconds; the 61 items come from four runs, pooled. The arms add one layer at a time: tools only; documents; ranked recall; the math-brain hook and math recall; held notes, a six-minute clock and a hint; and the statement of any named result the item refers to. The full package has every layer.

| Comparison | Items | Scores | Disagreements | p |
|---|---|---|---|---|
| full package against tools only | 61 | 52 and 41 | 15 to 4 | 0.019 |
| the same, without 7 items whose keys proved ambiguous | 54 | 48 and 39 | 12 to 3 | 0.035 |
| items that name a known result | 26 | 22 and 13 | 10 to 1 | 0.012 |
| items that name none | 35 | 30 and 28 | 5 to 3 | 0.73 |
| full package against documents and recall | 61 | 52 and 46 | 10 to 4 | 0.18 |

The gain over tools alone is real and sits in the items that name a known result. Against agents that already have the documents and a recall tool, the further gain is not significant.

## One thousand items whose answer must be recalled (13 September 2026)

Without the brain agents answered 538 of 1,000; with it, all 1,000. The brain helped on 462 items and harmed none (p = 1.7e-139). Every item needs a fact that has to be recalled from the store. On items a strong solver can work out for itself, the brain changes nothing.

## Twenty recall items, one agent with and without the brain (23 October 2026)

One Claude agent (Opus 5.5, high effort) took 20 items drawn at random from a 50-item recall bank. It first answered every item from its own knowledge with no tools and wrote the answers down; it then answered them again using `math_recall.py`, two or three wordings per call. A script graded both sets against keys the agent never read. Without the brain it answered 9 correctly, with it 19 (10 to 0 on the discordant items, exact sign test p = 0.002). The items it missed alone were the store's own results, such as constants found in the FEI campaign; the items it got alone were classical facts. The one item missed both ways may have a strict key.

## What did not help

- **Spreading activation** (11 October). Agents told why each card came up scored 79 with spreading and 80 without, while reading 46 percent more input tokens. Without agents, on the 584 questions, spreading moved first-eight hits from 298 to 307, but it found no card the word search had missed: it only re-ranks.
- **New open problems** (11 October). Fourteen Codex agents worked 13 open problems on which the store held only a first attempt from September. Graded blind, the brain arm scored 24 of 39 and the no-brain arm 26. A referee comparing each pair preferred the no-brain attempt 8 times and the brain's 3 times, with 2 even (p = 0.23).
- **An early version against plain documents** (a hard 300-item set, no tools). Version 1 of the math-brain stream (hook notes, math recall, Lean and an audit step) scored 238; agents given the documents directly scored 264 (14 to 40, p = 0.0005). Most of the loss was in one group of 70 items, 22 against 55. A later version, which routes to math recall first and adds a clock, scored 102 of 110 against 104 for documents with recall (6 to 8, p = 0.79).
