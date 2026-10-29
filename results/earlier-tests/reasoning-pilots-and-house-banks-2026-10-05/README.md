# Reasoning pilots, house banks and hook versions v5 to v8 (5 and 6 October 2026)

A series of small preregistered banks run over two days to find where documents, recall or the math brain can
help a solver that already reasons well. Every bank was frozen with its own snapshot of the store and the
documents before any arm ran, every prediction was written before the answers were read, and every solver
stream was scanned afterwards for markers of the bank, its keys or its authors. No stream in any arm touched
one. The items and keys are not published.

## Arms

| arm | what the solver had |
|---|---|
| tools only | Python and a Lean check, ten minutes a problem |
| documents and recall | the same tools, the memory folder and a store export, and the recall command |
| math brain v5 | the same, plus the math brain's prompt and Stop hooks (served notes, one closing audit) |
| v6 | v5, and when a problem names a result by surname and number the hook serves that stored statement word for word, leaving out superseded claims; silent otherwise (it served nothing on the 3,463 items of the other banks) |
| v7 | v6, and it also matches a result named by paper label and arXiv number, and drops internal reference labels from what it serves |
| v8 | v7, with three changes for Lean problems: 540 s before new checks stop instead of 360 s, a failed compile never triggers the advice to stop using Lean, and the closing audit asks for the final file to be compiled once more as submitted |

One rule governed every bank: further arms run only when tools only scores between 30 and 80 per cent, since
outside that range no arm has room to gain or lose.

## Self-contained reasoning: the ceiling

With Python and Lean, Claude Sonnet scored 31 of 31 on hand-written proof audits and true-or-false pairs, 20 of
20 on known Lean statements and 15 of 17 on new ones, and 20 of 20 on a bank written by a scheduled task. A
weaker solver, Claude Haiku, scored 26 of 31 on the first bank (above the ceiling, no further arms) and 14 of
20 on the scheduled-task bank, where documents with recall and math brain v5 did not change the score.

## Lean proofs on Haiku

The first Lean pilot could not be compared: the tools-only arm ran while the machine's compute gate held Lean
compiles, and of its 109 checks 89 were held, 17 timed out and 1 compiled. The other arms compiled freely. The
same 20 statements were rerun with a preflight compile before each arm and no check held: tools only 12,
documents and recall 12, v5 9. The v5 loss came from its closing audit, whose reply on 7 items described the
proof without repeating the code; read on the last Lean block written anywhere in the stream, v5 proves 11
(2 only in tools only, 1 only in v5, p = 1).

v7 against v8 on the same statements, read on the stream as fixed before the run: 12 against 14 proved, three
items only in v8 and one only in v7, exact McNemar p = 0.63. On the final message alone, 10 against 14
(p = 0.22): v7 lost six answers to its closing audit, v8 lost one. v8 roughly doubled the Lean checks (325
against 173) and more than tripled the compiles (71 against 20), and its stop still refused 5 checks, so the
preregistered prediction (a gain of two, at most one loss, no refused check) was not met as a whole.

## House banks: results newer than any model

The banks reason1k_house to house5 hold proof audits and true-or-false pairs built on five results that the
store settled and no model's training can contain. Each audit invokes one of them by name without restating it,
and turns on whether the result as established gives what the step asserts. Sonnet was the solver, so that a
miss reads as missing knowledge rather than weak reasoning. Every item was keyed blind before the author's key
was read.

| bank | items | tools only | documents and recall | v5 | v6 | v8 |
|---|---|---|---|---|---|---|
| house | 10 | 7 | 8 | 9 | | |
| house2 | 20 | 13 | 15 | 17 | 18 | |
| house3 | 18 | 13 | 15 | 13 | 16 | |
| house4 | 16 | 13 | 14 | | 14 | 15 |
| house5 | 20 | 19 | | | | |

Scores exclude seven audits (five in house3, two in house4) found after the house4 results were read to have a
second defensible key: a bare invoke followed by the result's own conclusion outside its scope. They stay in
the banks and the raw tables, and conclusions are drawn without them. The bank builder now refuses an audit
whose key sits at or just after a bare invoke unless the review records why only one key is defensible.
house5 scored 19 of 20 under tools only, so its other arms did not run.

Pooled, exact McNemar:

| comparison | items | gained | lost | p |
|---|---|---|---|---|
| v5 against tools only | 48 | 7 | 1 | 0.070 |
| documents and recall against tools only | 64 | 10 | 4 | 0.18 |
| v6 against tools only | 54 | 12 | 3 | 0.035 |
| v6 against v5 | 38 | 7 | 3 | 0.34 |
| v6 against v5, named items | 17 | 7 | 0 | 0.016 |
| v6 against documents and recall | 54 | 8 | 4 | 0.39 |
| v6 against documents and recall, named items | 21 | 5 | 0 | 0.063 |
| v8 against v6 | 16 | 1 | 0 | 1 |

An item is named when v6's own transcript shows it was served the item's stored statement. In the first house
bank Sonnet looked a result up on only 4 of 10 items and never on the ones it got wrong, while retrieval put the
right result first on three of those lookups; serving the named statement unasked is what v6 adds, and the
named items carry its whole lead. The comparison of v6 with documents and recall on named items was given one
last look on house5 before the run, and since house5 added no pair it stays at 5 to 0 (p = 0.063): suggestive,
and not retested by adding banks.

## A recall change measured in the same window

Recall's symbol channel stopped counting punctuation and the subscript sign as matching terms. On a question
written in notation they had decided rankings alone: a Lindeberg-condition question ranked the constructible
universe first, with about 48 of its 53 points from braces, commas and subscripts. On 328 labelled recall
questions, first place rose from 237 to 250 (18 gained, 5 lost to second place), the top three from 290 to 297,
and the top ten was unchanged at 317.

Variants of the change were measured on the same 328 questions. Counting numbers as symbol terms again cost 26
first places (224), numbers and operators together 33 (217). Keeping operators moved first place by at most two
(251 and 248 for two operator sets), and two gates on the symbol channel left it at 250 with the top three at 296.
The change went in as measured, without any of the variants.
