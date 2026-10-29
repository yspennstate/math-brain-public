# Small tests, 7-29 October 2026: a four-arm pilot, two with/without pairs and three recall checks

None of these is in `TESTS.md`. The pilot found no brain advantage, the recall pair was lost to timeouts, and the three
recall checks found that a proposed change buys nothing; they are kept because the negative results bound what the
larger tests show. All counts below are in
`SUMMARY.json`. A timeout or an error with no answer counts as wrong.

## Four-arm pilot (7 October)

27 items, each asked of Codex (gpt-6.1-sol) four ways: two arms with the brain (A, B) and two without (C, D), one
session an item. The rows were graded on 29 October, 65 by rule and 43 by a model judge on the bank's rubric.

| arm | brain | score out of 27 | finished | timed out | crashed | median seconds |
|---|---|---|---|---|---|---|
| A | yes | 21.7 | 24 | 0 | 3 | 96 |
| B | yes | 15.0 | 15 | 9 | 3 | 264 |
| C | no | 23.0 | 25 | 0 | 2 | 79 |
| D | no | 11.0 | 13 | 7 | 7 | 216 |

The brain gave no advantage. Most of the spread between arms is sessions that never finished: B lost nine items to
the time limit (two of them had written an answer before it and were graded right) and its hook alone took 147
seconds; D lost fourteen to timeouts and crashes. On the rows that finished the four arms are close (0.90, 0.87, 0.92
and 0.85 of a point a row).

## Recall pair (22-23 October)

25 recall questions about the store's own records, Claude Sonnet, one arm with the brain and one without. Without the
brain no answer was right (13 answered, all wrong; 11 timeouts, 1 error). The brain arm's first run is excluded: the
recall tool was broken and all ten of its rows timed out. Run again with the tool fixed, it answered 3, all right, and
timed out on 21 at about 1,900 seconds, on a machine whose memory commit stood at 88-96 percent. The other 15 items
were never run. The result says more about the machine than about the brain; the three-arm test in `TESTS.md`, run
from the next day on questions of the same kind, is the measurement to read.

## The same agent with and without the brain (23 October)

One Claude Opus 5.5 session answered 20 items of a recall bank twice: first from the model alone, before any search,
then with the recall tool (two wordings in one call, then one walk to the cards it printed). Keys were applied by the
bank's own grader.

| | right of 20 |
|---|---|
| model alone | 9 |
| with the brain | 19 |

Ten items were right only with the brain and none only without it (two-sided sign test p = 0.002). Every miss
without the brain asked about the store's own results, which no model knows from training. The graded pass took 21
recall calls, 291,307 characters of tool output (about 73 thousand tokens) and 100 seconds of tool time.

## Recall depth after the 28 October links

On 28 October the store gained 76,434 links and 3,396 paper source cards (90,797 cards, 125,830 links). The question
was whether following links one step from the printed cards (`--depth 1`) now finds answers the words miss. 98 items
of the held-out recall bank were run at both depths; depth 1 reached its time limit after 43.

| paired, 43 items | depth 0 | depth 1 |
|---|---|---|
| right card first | 18 | 18 |
| right card in the top 3 | 20 | 19 |
| right card in the top 8 | 22 | 22 |
| MRR at 8 | 0.440 | 0.443 |
| tokens a call | 4,625 | 4,841 |
| median seconds a call | 2.9 | 13.2 |

Neither depth found any of the 16 hard items. Depth 1 reorders what the words already found, at four and a half times
the time. Depth 0 stays the default.

## A bank built to favour depth 1 (29 October)

63 held-out items were chosen so that the answer card shares few words with the question and has a linked card that
shares more. On the 30 items both depths finished (19 of them hard), the answer was printed for the same 11 items at
both depths and was in the top 8 for none. Tokens a call 4,946 against 5,014, median time 3.5 against 11.0 seconds.
A direct check printed each served card's linked cards beside the depth 0 hits: a linked card appeared for 11 of the
30 items, the answer for the same 11, and never a linked card without the answer. Wherever a link led to the answer,
the words had found it already.

## A cap on compactions per session (28 October)

13,115 of 36,915 memory files are the anchors of compaction summaries, and on one misspelt query four of the eight
recall rows were compactions of one session. 110 queries were scored on one recall list, with the cap applied to the
same scores:

| queries | n | hit at 8, no cap | cap 1 | cap 2 |
|---|---|---|---|---|
| memories, clean wording | 40 | 38 | 38 | 38 |
| memories, with typos | 40 | 37 | 37 | 37 |
| the exact compaction asked for | 30 | 12 | 5 | 6 |
| a compaction of the same session | 30 | 25 | 25 | 25 |

Compactions took 1 of 320 slots on clean queries and 3 with typos, so the cap had nothing to remove there, and it lost
the exact compaction asked for (12 to 5) because the one wanted is often not its session's best scoring. Nothing was
shipped. The queries come from each target's own words, which favours the target.

Counts only. The questions, keys, answers, card ids and item ids are not published.
