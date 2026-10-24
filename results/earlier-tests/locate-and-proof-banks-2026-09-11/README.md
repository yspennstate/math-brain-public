# Locate banks and proof-bank reruns, 11-12 September 2026

Two kinds of test run in the same two days, after a repair of the hook that serves the store's cards.

On the morning of 11 September a check through the real hook path found that the math lane served the asked-about
theorem on 35% of unnamed and 38% of named questions of a fixed 89-question bank, against 84% and 97% on 3 September.
Three changes of the previous week had stacked: an on-topic floor fixed in raw BM25 units (a short question could
never reach it), a block budget that fit one card, and a document-frequency cap that removed every word of the
largest family in the store (2,018 self-avoiding-walk nodes, 28% of it). The floor now scales with the question's
own self-score, the block holds three whole cards, the cap is 0.5 and digit runs are tokens. After the repair the
same bank read 74% and 91%, and 79% and 93% after the changes listed below.

## The locate banks: questions only the store can answer

Each question asks for a value recorded in the store and nowhere else, so a solver without the store can only
answer UNKNOWN. A wrong value is scored apart from an UNKNOWN; that is the measure of invented answers. The solver
was Sonnet, run blind in shards of ten items; the keys were read only by the grading script, after serving.

- **L1, 60 items:** 40 exact counts of self-avoiding walks in a strip with forbidden sites, from the store's own
  enumerations, and 20 constants recorded by two research campaigns (first-passage percolation and Rademacher sums).
- **L2, 40 items:** the PDF page on which an open problem of the store's problem ledger is posed.
- **L3, 30 items:** two walk counts and their difference (same length and strip, different forbidden sites).

Each round of a bank followed one change to the hook, named by the round before it:

| bank | round | change before the round | right with the store |
|---|---|---|---|
| L1 | 1 | the repaired hook | 38 / 60 |
| L1 | 2 | signed numbers kept signed in both tokenizers ("(-2,2)" had read as "(2,2)"); card statement 480 characters, block 3,000 | 50 / 60 |
| L1 | 3 | a ranking led by one campaign may fill all three slots from it; the on-topic ratio is measured against the chosen cards | 54 / 60 |
| L1 | 4 | the abbreviation "FPP" counts as a mathematical anchor | 55 / 60 |
| L1 | 5 | a number in the question weighs three times a word in the excerpt window; the lexical favourite may take a free slot | 57 / 60 |
| L2 | 1 | "open problem" counts as an anchor (before it, 13 of 40 questions received any card) | 37 / 40 |
| L2 | 2, 2b | none; two reruns | 27 / 40, 29 / 40 (see below) |
| L2 | 3 | the question asks for the first page of a range | 40 / 40 |
| L3 | 1 | the hook of L1 round 4 | 4 / 30 |
| L3 | 2 | a short prompt whose parameter sets sit in separate clauses is asked clause by clause | 11 / 30 |
| L3 | 3 | in that path the candidates are restricted to rows whose tuple set equals the question's | 30 / 30 |

The row files keep the working names of the rounds (`L2_r3` is L2 round 1 above, `L2_r4` and `L2_r4b` round 2,
`L2_r5` round 3). Without the store: L1 3 of 60 (the three are computable from their own wording), L2 0 of 40, L3
0 of 30. Across
every round and every bank no solver given the store's cards gave a wrong value: when the served rows did not match
the question's parameters it said UNKNOWN. On L3 the four, then eleven, correct answers in rounds 1 and 2 are exactly
the questions on which both rows reached the block, and the solver computed the difference correctly on each.

The L2 dip in round 2 is the question's wording, not the block. On every item that flipped, the served card was
byte-identical to round 1's and cited a page range ("PDF 24-25"); round 1's solvers gave the first page, round 2's
abstained. Round 3 asked for the first page of a range and read 40 of 40. The L2 numbers measure whether the hook
reaches the node and whether the window it shows carries the fact; they say nothing about mathematical knowledge.

## Proof-bank reruns: does the served block help a blind auditor?

The same 100 and 35 screened proof-audit items as an earlier GPT-model test, which read 99 of 100 and 34 of 35 with
or without notes (a ceiling). Here the solver is Sonnet, which has room to fail; the frozen rule scores a verdict and
the first faulty step, and an uncertain answer scores zero. The block was captured fresh from the hooks.

| bank | date | without | with the block | helped / harmed | exact McNemar p |
|---|---|---|---|---|---|
| 100 items (48 flawed) | 11 Sep | 87 | 90 | 5 / 2 | 0.45 |
| 35 items | 11 Sep | 32 | 31 | 0 / 1 | 1.0 |
| 100 items | 12 Sep | 91 | 94 | 4 / 1 | 0.38 |
| 35 items | 12 Sep | 29 | 33 | 5 / 1 | 0.22 |

None of the four separates from zero. On 11 September all five items the block helped carried both the retrieved
cards and the proof-checking prompt, and the 41 items with cards only moved 37 to 36; between the two days the gate
of that prompt was widened to plain-ASCII mathematics (50 to 89 of the 100 items). Blind judges rated the 167 cards
served on the 100-item bank on 11 September: 86 bear on a step of the argument, 66 are the right field only, 15 are
unrelated. Of the three they flagged as false, one was a real error in a stored statement (the Moon-Moser triangle
bound written in two forms that differ by a factor of n; the store now carries the corrected form), one was the
judge's error, and one was an excerpt that dropped the card's opening hypothesis, after which excerpts keep it. In
each 12 September run the one harm is a clean argument that same-area cards led the auditor to doubt.

Read together: retrieving a stated result helps when the answer has to be found (L1-L3); it does not by itself turn
a wrong verdict on an argument into a right one.

## Files

`rows/` holds one file per run with each item's id and verdict per arm (`L*`: correct / unknown / wrong, and whether
the source node or both rows were served; proof banks: right or not per arm, and whether cards were served).
`python recompute.py` derives every number in the two tables from them and checks it; all sixteen runs match. The
questions, keys, served blocks and answers are not included, so that the banks stay usable.
