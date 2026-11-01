# Semantic channel scope in the math hook (4 October 2026)

The math store's semantic channel ranks cards by the cosine between the question's embedding and each card's. It takes
its top K over every card vector in the store first and applies the caller's list of eligible ids afterwards. In the
hook the eligible ids are the prefilter's BM25 pool of 300 candidates, so with the channel switched on (it was off in
the hook at the time) only the part of the global top 50 that also sits in the pool could score. This probe asks what
that costs, before any arm is run: for each question, how much of the global semantic top 50 falls inside the pool,
and whether the answer is in the pool, in the global top 50, in the pool's own top 50 by the same score, and in the
global top 50 but outside the pool, which only a hybrid pool could hand the ranker. No hook was run and nothing was
written to the store.

## The fresh bank, 218 base questions

178 questions have an answer in the store and 40 do not. The prefilter returned a full pool of 300 for
199 of them. On average 28.3 of the global semantic top 50 fell inside the pool (median 29.5,
range 0 to 50).

Here an answer card is a card whose title carries one of the question's stems. 126 of the
answerable questions have one.

| | count |
|---|---|
| answer card in the BM25 pool | 125 of 126 |
| answer card in the global semantic top 50 | 119 |
| answer card in the pool's own semantic top 50 | 121 |
| answer card in the global top 50 but not the pool | 0 |
| best answer card at semantic rank 10 or better | 113 (median rank 1) |

The title match is loose, so 14 of the 40 questions without an answer also have a
matching title; 11 of those sit in the pool and 8 in the global
top 50.

## Reworded open-problem descriptions, 40 descriptions in three framings

The 40 open-problem descriptions of a locate bank, asked in the three framings the nightly instrument runs. The answer
is the node the problem was harvested from.

| framing | in BM25 pool | in global top 50 | in pool's top 50 | global top 50, not pool | median semantic rank |
|---|---|---|---|---|---|
| "Where is the open problem about ... posed, and on which page?" | 40 | 39 | 40 | 0 | 1 |
| "What is known about ...?" | 38 | 37 | 35 | 2 | 3 |
| the 50-word template | 40 | 24 | 28 | 0 | 23.5 |

## Reading

On these banks the BM25 pool already holds nearly every answer, so applying the eligible ids after the top K costs
almost no reach: no base question had its answer in the semantic top 50 and outside the pool, and two of the 120
reworded questions did, both in the "What is known about" framing. The weak spot is the 50-word template, where the
pool still held all 40 answers but the semantic order put only 24 of them in its top 50. A hybrid pool would buy little
on these banks; ranking inside the pool is where the template loses.

Counts only. The questions, descriptions, answers, card ids and item ids are not published. `SUMMARY.json` holds every
count in this page.
