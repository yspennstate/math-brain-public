# How Codex math agents used the recall tools, 13 to 17 October 2026

A count, from the agents' own session records, of how Codex agents working on the frontier rows and the test banks
called the store's recall tools. The records were read in one streaming pass over 398 sessions dated 13 to 17
October. A session counts as a math session when its commands touch the frontier, a frontier row, a test bank or the
math store; 65 of the 398 do.

| | count |
|---|---|
| sessions | 398 |
| math sessions | 65 |
| math sessions with no recall call | 29 |
| `math_recall.py` searches in math sessions | 323 |
| `math_recall.py --id` walks | 61, of which 22 on ids an earlier search printed |
| frontier checks / briefs | 196 / 23 |
| recall over the notes (`brain.py recall`) | 13 |
| `math_recall.py` outputs read | 395 |
| ... returned while the command was still running | 81 (21 percent, an upper bound) |
| ... cut by the output cap | 16 |
| ... with a WEAK MATCH line | 16 |
| wait before reading the output (`yield_time_ms`) | 1,000 on 234 calls, unset on 140, 10,000 on 18, 30,000 on 3 |
| output cap (`max_output_tokens`) | mostly 500 to 2,500 (1,000 on 34, 500 on 32, 6,500 on 31, 2,500 on 21, 1,500 on 16) |

A search prints about 3,500 tokens and takes tens of seconds on a loaded machine, so a one-second wait reads a
command that has not finished and a cap under 3,500 cuts the cards off. With a 45-second wait and an 8,000-token cap
the cards arrive whole. Those two settings, with two or three wordings in one call and a walk on the printed ids, were
added to the instruction file these agents load on the evening of 17 October; none of the 123 campaign sessions of 15
to 17 October carried them, so the table shows use before them.

Limits. "Still running" is matched on the first 400 characters of an output and also catches a line that only reports
a session id, so it can overcount; a later poll that collected the cards is not followed; "math session" is a
heuristic on the command text. Counts only: the command excerpts and session records are not published.
