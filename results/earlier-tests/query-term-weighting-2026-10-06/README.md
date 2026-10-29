# Query term counts in the math hook: linear or binary (6 October 2026)

The math hook scores a stored card against the problem by the query terms they share. The question was whether
a term repeated in the problem should count once (binary) or once per occurrence (linear, the production
setting).

## Design

Bank: 89 answerable probe items, each asked in two forms (content only, and with a hint naming the area), and
40 items the store cannot answer: 218 asks. Every item was asked once per arm in a single pass through the live
hook, with the arm order alternating item by item. An earlier sequential comparison had given three false wins
to whichever arm ran under lighter load. No ask timed out.

## Result

| | linear | binary |
|---|---|---|
| content form: theorem served | 71 of 89 | 67 of 89 |
| content form: at rank 1 | 55 | 52 |
| content form: silent | 9 | 12 |
| hinted form: theorem served | 87 of 89 | 87 of 89 |
| unanswerable: false fires | 19 of 40 | 18 of 40 |

The two arms served the same set on 193 of the 218 asks, and the outcome differed on 7. Each of the 7 was asked
twice more, interleaved, and every repeat matched the first pass, so the differences are deterministic and not
load. Linear won four answerable items. On three of them binary went silent (Gaussian concentration, Tychonoff,
Rademacher); on the fourth, Banach's fixed point theorem, binary served the complete-metric-space card and an
unrelated attempt where linear served the theorem first. Binary won two unanswerable items by staying silent
where linear fired falsely, and lost one the other way.

Binary costs four theorem answers (4.5 points on the content form, 3 at rank 1) to save one false fire, so the
hook stays linear. Using binary only on problems shaped like unanswerable ones would need a classifier the hook
does not have.
