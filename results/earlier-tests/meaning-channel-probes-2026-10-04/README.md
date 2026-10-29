# The meaning channel inside the math hook: three probes (4 October 2026)

The math hook ranks cards by BM25 over a prefilter pool of 300 candidates. Beside it sits a meaning channel: the
question is embedded and compared by cosine with a vector for every claim in the store. Three probes asked what that
channel can and cannot do for the hook. None ran a solver; they read the store and the hook's own functions.

## Where the channel could help

For each base question of the fresh bank (178 answerable, 40 with no answer in the store) the probe compared the
global semantic top 50 with the BM25 pool. A median of 29.5 of the top 50 fall inside the pool, so a channel restricted
to the pool keeps a little over half of what it would rank. Of the 126 answerable questions whose answer card can be
identified by title, the answer is in the pool for 125, in the global semantic top 50 for 119, at a median global rank
of 1, and never in the semantic top 50 while missing from the pool. A hybrid pool would hand the ranker nothing new on
this bank.

The same question on 40 reworded open-problem descriptions in three framings:

| framing | answer in the pool | in the semantic top 50 | median semantic rank there | semantic top 50 only |
|---|---|---|---|---|
| 50-word paraphrase | 40 | 24 | 10 | 0 |
| "where is the open problem about X posed" | 40 | 39 | 1 | 0 |
| "what is known about X" | 38 | 37 | 2 | 2 |

## Can the channel open the entry gate?

The hook's entry gate refuses 32 of the 120 reworded questions, every one of them a "what is known about X". The probe
asked whether the channel's own confidence could admit them without admitting everyday prompts that have nothing to do
with mathematics. It recorded, for each prompt, the winner's cosine in standard deviations above the mean over all
claims (z1), its margin over the runner-up, and the winner's rank in the BM25 pool, on three populations: the 120
reworded questions, the 40 questions with no answer (anything admitted is a false fire), and 13,351 archived everyday
prompts that the gate refuses.

The existing vouch route, which admits a prompt holding two or more of the store's own words and serves it only when
the lexical and semantic winners agree, already routes 20 of the 32. The channel's winner is the right card on 8 of the
32. Over a grid of 112 threshold sets (z1 from 4 to 8, margin from 0 to 1, BM25 rank from 1 to 50), a confidence-based
first stage adds a right card beyond the vouch route at only two of them, z1 at least 4 with no margin floor and BM25 rank
within 10 or 50. Each adds one right card together with three or four wrong winners, two fires on questions with no
answer, and roughly 300 to 660 everyday prompts the vouch route does not admit. The channel's confidence separates a
right winner from a wrong one no better than its raw cosine does. Nothing was built.

## Superseded revisions

A wrong card is never deleted; a corrected revision supersedes it. The vector file still held a vector for each of the
361 claims a newer revision supersedes, and their text is close to the current revision's. retrieve() ranks current
revisions only, so when the channel's argmax named the old revision the lexical and semantic winners could not agree,
and the agreement checks silenced exactly the revised cards. Asked "What is <title>?" for 327 revised claims, the
channel's winner was the old revision 181 times and the current one 79 times.

The hook now masks superseded revisions before taking the winner. The same candidate was run with the mask off and on:

| questions | fired | hit | first card right |
|---|---|---|---|
| 327 on revised claims, mask off | 246 | 193 | 184 |
| 327 on revised claims, mask on | 256 | 202 | 192 |

Nine silences became the right card, one became a related card, and no answer was lost. On 588 general jobs (the fresh
bank's 218 questions, the 120 reworded questions and 250 admitted everyday prompts) no outcome changed. The rule that
followed applies to every winner or top K over claim vectors: drop the targets of supersedes edges first.
