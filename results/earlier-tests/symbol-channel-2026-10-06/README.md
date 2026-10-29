# The symbol channel in recall: which notation tokens count (6 October 2026)

Recall scores a stored card against a question through several channels. The symbol channel turns both into
normalised mathematical tokens and counts the tokens they share. Variable names were already dropped as slots.
Punctuation (braces, brackets, parentheses, commas, colons) and the subscript sign were kept, and on a question
written mostly in notation they could decide the ranking on their own. On one limit-law question an unrelated
set-theory card ranked first, with 48 of its 52.9 points from subscripts, braces and commas, and the card the
question was about was outside the top ten.

## Design

328 labelled questions from seven banks, each with a known card. Recall ranked the store's cards once per
question in each arm, on the same store and the same code apart from the set of symbol tokens it counts. The measure
is the rank of the known card. This is a ranking test: no model answered anything.

| arm | symbol tokens counted |
|---|---|
| keep | all, as before |
| drop | without the subscript sign and punctuation (the change tested) |
| ops | drop, and also without powers and equals signs |
| allops | drop, and without every operator token |
| nums | drop, and without single digits |
| numsops | drop, without digits and operators |
| gate 3, gate 6 | drop, with a card's symbol score counted in full only once its lexical score reaches 3 or 6, and in proportion below that |

## Result

| arm | first | top three | top ten |
|---|---|---|---|
| keep | 237 | 290 | 317 |
| drop | 250 | 297 | 317 |
| ops | 251 | 298 | 317 |
| allops | 248 | 292 | 316 |
| nums | 224 | 270 | 316 |
| numsops | 217 | 261 | 318 |
| gate 3 | 250 | 296 | 317 |
| gate 6 | 250 | 296 | 317 |

By bank, first / top three / top ten:

| bank | questions | keep | drop |
|---|---|---|---|
| limit laws, written mostly in notation | 10 | 5 / 7 / 9 | 7 / 9 / 10 |
| content questions | 89 | 61 / 81 / 85 | 59 / 81 / 85 |
| the same questions with the area named | 89 | 81 / 89 / 89 | 81 / 89 / 89 |
| where an open problem is posed | 40 | 40 / 40 / 40 | 40 / 40 / 40 |
| where a self-avoiding-walk result is proved | 40 | 27 / 40 / 40 | 36 / 40 / 40 |
| pairs of self-avoiding-walk results | 30 | 4 / 11 / 26 | 9 / 16 / 25 |
| questions in the user's own words | 30 | 19 / 22 / 28 | 18 / 22 / 28 |

Against keep, drop put the known card first on 18 more questions and 5 fewer, and each of the 5 fell only to
second place. The gains are in the banks written in notation; the losses are three content questions and one in
the user's words, where punctuation had been helping by accident.

Cutting further does not help. Dropping powers and equals signs as well gives 251 first places against 250, which
is noise, and dropping every operator gives 248 with the top three down from 297 to 292. Single digits are content:
without them first place fell to 224 (33 questions lost, 7 gained), nearly all on the self-avoiding-walk locates,
where the numbers are what the question is about. The lexical gate was neutral on these questions. On a separate
set of 20 questions about the store's own results it gave 15, 16 and 17 first places at gates 0, 3 and 6, with no
question lost, which is too few to act on.

Of the 78 questions whose card is not first under drop, two miss because the question uses a word that the card
writes only as notation. Where recall still misses on these banks, the gap is vocabulary rather than symbols.

## What happened to the change

Drop did not stay live. On the nightly math gate's own bank of 89 questions it lost four content questions and
gained one, and on its own it failed a must-pass control of the math health check, so it was reverted from the
live build on 7 October. The measurement above still holds. Ops, allops, nums and the gate remain named settings,
off by default.

## Files

`SUMMARY.json` holds, for every arm and bank, the number of questions and the counts at ranks 1, 3 and 10. Each
count was recomputed from the per-question ranks of its run and matches that run's own summary. The per-question
ranks are not published, because their keys name the items.
