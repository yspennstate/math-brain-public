# Ten recall-speed and ranking probes (12 October 2026)

Ten separate probes of the two recall paths, each on the development question sets of the recall benchmark (a tune half
used for choosing settings and a check half kept apart from it). Each probe changed one thing on a copy of the tools and
was compared with the live tools on the same questions. A speed change counted only if the printed output stayed byte
for byte the same; a ranking change only if it gained on the check half without losing on the tune half. The question
sets are not published.

## What was tried

| probe | question | outcome |
|---|---|---|
| general recall, cached state | can the recall command keep its query-independent work between calls without changing a byte? | landed: output identical on 617 of 617 tune and 120 of 120 check questions |
| math prompt hook | can the hook read only the three edge kinds it needs instead of the whole edge table? | landed: same notes chosen on 165 of 166 prompts, processor time 0.742 s to 0.188 s a prompt |
| walk-next line | does one extra line naming the next card to open help after a miss? | candidate: names the answer on 17 of 105 check misses, rest of the printout unchanged |
| how agents are told to recall | do the agent guidance files describe the math recall tool? | none did; the help text and a short guidance block were drafted |
| general recall ranking | does a meaning rerank of the top 60 lexical results help? | +0.03 MRR on the tune half; never scored on the check half |
| card rewordings | do stored rewordings of each card help questions phrased in other words? | gain only on covered cards, which were 9.6 per cent of the store |
| shorter printout | does a shorter printout cost less? | no: the answer text was hidden 3 times in 55 and agents walked 2.3 times more |
| hook cost | how much of the hook text repeats lines already in the agent's context? | 21.8 per cent |
| meaning channel | do query-side changes help reworded questions? | gains within noise |
| math recall cold start | where does a cold call spend its time? | about 80 per cent on work that does not depend on the question |

## General recall, cached state

The recall command parsed the same index, graph and vector files on every call. The change keeps those parsed forms in
cache files keyed on the identity of their sources (file id, birth time, size and modification time), so a source
replaced with its old modification time is a miss, never a stale hit.

With the merge of newly written memories turned off, as the benchmark runs it, the median call fell from 9.81 s to
6.12 s on the check half (120 of 120 identical) and from 9.89 s to 8.25 s when every call started from an empty cache
(30 of 30 identical). In normal use new memories are written every minute or two, so nearly every real call merges
them into the index first, and that merge does not use the cache. Measured that way the median warm call went from
9.94 s to 7.76 s and a cold call was about even. A full miss writes about 35 MB of cache files, three generations of
which are kept.

The same work turned up a fault in the benchmark: its cold-latency probe called the live command for every candidate
arm, so the cold timings it printed for a candidate were the live ones.

## Math prompt hook

The hook read the whole edge table on every prompt (380 to 416 ms) to find three edge kinds that an index serves in 8 to
10 ms. Over 166 prompts, run in alternating order, the candidate chose the same notes for the same reasons on 165. On the
remaining prompt the live hook failed its own consistency read under load (38.8 s) and the candidate answered normally.
The median processor time a prompt fell from 0.742 s to 0.188 s and the median wall time from 2.14 s to 0.41 s; the
machine was bound by disk at the time, so the processor time is the fairer figure. Over the three days before, the hook
ran about 1,150 times in sessions, 1,024 of its fires were evaluation runs, and it took over a second on 27 prompts.

## Walk-next line

On the check half the answer was outside the eight printed cards for 105 questions. For 24 of those it was one link from
a printed card, and 23 of the 24 were already named on a printed link line; 23 more were two links away and 58 further or
not linked. The candidate adds one line of about 107 characters naming up to three cards to open next (one link away,
nearest by meaning, two links away). It named the answer on 17 of the 105 check misses and 11 of 64 tune misses, cost
about 0.1 s a call, and left the rest of the printout identical on 430 of 430 questions. Whether agents act on the line
was not measured.

## How agents are told to recall

None of the three agent guidance files named the math recall tool or its `--or` option, and its help text printed one
line. In three agent campaigns of the same week, 103 sessions made 12 recall calls in all; in the second, 164 runs made
no call to the math recall tool; in the third, 58 runs made 10 searches and 18 card reads. The agent harness returned a command still running after 10 s as empty, and a cold search
took about 10 s, so 70 of 105 calls came back unfinished and cost extra turns (a median of four more calls before the
printout arrived). Agents also set output caps of 1,000 to 3,000 tokens where a search prints a median 3,488, so 8 of 23
card reads in one campaign were cut. The WEAK MATCH line held up as a signal to reword: with it the answer was printed
on 23 per cent of questions, without it on 51 per cent, and it appeared on 88 of 92 off-topic prompts.

## Negative results

- Ranking of the general recall: rescoring the top 60 lexical results by the query's meaning raised MRR from .531 to
  .561 on the tune half (25 questions gained first place, 7 lost) at a cost of 2.5 to 3 s on a cold call. It was not
  scored on the check half, and the tune questions were written from the memory text, which may favour it.
- Card rewordings: a field holding only words absent from a card's own title and body, at weight 0.5, gained on both
  halves with no loss, but only 1,024 of 10,710 cards carried rewordings, so the expected change on an arbitrary question
  is about zero. The same probe found that the rewordings file was looked up at a relative path when the store location
  was not set in the environment, which had no effect at the time because the field weight was zero.
- Shorter printouts: layouts 30 to 41 per cent shorter kept the same hits but showed the answer text in its block on 51
  or 39 of 55 questions against 54 for the full layout. In an earlier agent comparison a 400-character printout kept
  accuracy (86 against 85 right) but agents opened 2.3 times as many cards and each answer cost 6.5 per cent more.
  Folding near-duplicate cards won nothing: judged duplicates filled 7 of 656 printed slots.
- Meaning channel: the query prefix was already in use; a query ensemble, feedback on the vectors and dropping
  superseded rows changed nothing. Title-and-body vectors helped questions in other words and hurt paraphrases.
- Hook cost: hook text came to about 24 million cached tokens a day, 6.4 per cent of all input tokens; 21.8 per cent of
  it repeated a line already in the same context.
- Math recall cold start: of a 7.2 s cold call, about 2.2 s went to per-card term preparation, 1.9 s to parsing the store,
  1.0 s to prefetching signals and 0.9 s to starting the encoder. A pre-optimized encoder file loaded in 0.49 to 0.73 s
  against 0.64 to 1.15 s and gave bitwise identical vectors on 108 of 108 questions.

Counts only.
