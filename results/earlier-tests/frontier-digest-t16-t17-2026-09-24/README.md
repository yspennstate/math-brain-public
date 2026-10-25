# The frontier digest, tests T16 and T17, 24-25 September 2026

The math hook fires on the questions a person types, so a research session working one program for many hours saw
the store's cards only a handful of times. The frontier digest is the other route: at the first prompt of a session
on a program it hands over what the store holds on that program, newest first, with the failed routes. The two tests
ask whether that changes the work, measured on research plans written by Opus 5.5.

## Design

Two programs, the Fourier entropy-influence conjecture (FEI) and the bounded-density conjecture for quadratic forms
(QFORM), four cut-off times each. At each cut-off two planning agents got the program's goal and the conjecture's
statement; the DIGEST arm also got the digest the store would have produced at that moment, the NONE arm nothing more.
Each wrote a research plan of at most 700 words (what to try first, what to build on, what to avoid, the first step)
with no store, file or web access. One blind judge per program then saw, for each situation, the frontier at the
cut-off, what the store gained in the next twelve hours, and the two plans shuffled as P and Q, and scored each plan:

- built_on: established results it correctly builds on (count);
- redundant: steps that set out to prove something the frontier already holds (count);
- dead_end: steps along a route the frontier records as failed (count);
- on_target: whether its main line aims at what was established or found open next (0, 1 or 2);
- which plan serves the goal better.

built_on, redundant and dead_end are scored against the frontier the DIGEST arm was given, so they show whether the
digest was used rather than whether it helped. The bar was fixed before any judge ran and rests on the two measures
that can go against the digest: the judge prefers DIGEST in at least 5 of the 8 situations (P1), and DIGEST's
on_target total is at least NONE's (P2). Fewer redundant plus dead-end steps (P3) is reported.

T16 used the first version of the digest and cut-offs from 22 Sep 22:00 to 23 Sep 18:00. Between the tests the digest
was rewritten: every item is tagged as literature with its year or as an unrefereed house result, corrections are read
from the store's supersedes edges as of the cut-off, and a closing section lists what was withdrawn or refuted. T17
used that version on four new cut-offs, 23 Sep 22:00 to 24 Sep 10:00, all before the rewrite was finished, and nothing
in the code names a claim, a date or a program.

## Results

| test | DIGEST preferred | on_target DIGEST / NONE | redundant + dead_end DIGEST / NONE | built_on DIGEST / NONE | bar |
|---|---|---|---|---|---|
| T16 | 5 of 8 | 11 / 12 | 3 / 6 | 50 / 14 | P1 passes, P2 fails |
| T17 | 7 of 8 | 10 / 6 | 8 / 17 | 78 / 23 | passes |

T16 by program: FEI preferred DIGEST 4 of 4 with on_target 6 against 5; QFORM preferred NONE at the three earliest
cut-offs. In those situations the frontier carried a rank-three claim later found false, shown with the same
"[theorem]" tag as a published result, and the DIGEST plans built on it; the judge credited the NONE plans with
anticipating the corrections of the next hours. That case is what the rewrite addressed.

T17 by program: FEI 3 of 4 with on_target 6 against 5 (redundant steps 5 against 2, so P3 fails there); QFORM 4 of 4
with on_target 4 against 1, though every QFORM DIGEST plan scored 1, none 2. Three QFORM situations had an empty store
section in their reference, because the day's quadratic-form results reached the store late; their references were
completed with the program folder's commit subjects for the same twelve hours, a change made before the judges ran and
applied to all eight situations. Without those three, DIGEST was preferred 4 of 5 with on_target 7 against 6.

Checks on T17: the judges chose P four times and Q four times, and DIGEST won all three situations where it was Q.
DIGEST plans averaged 734 words against 681; the widest gap (FEI, 24 Sep 02:00) is the one situation DIGEST lost. The
QFORM results the judges credited were already in the program's repository before the first cut-off, so the digest
added nothing the repository did not hold; it put it in front of the agent. The sixteen T17 planning runs cost
USD 58.76 at API prices.

Limits: neighbouring cut-offs share eight of their twelve hours, there are two programs and one judge per program,
and the comparison is the digest against no frontier at all, not against what the math hook already serves.

## Files

`rows.json` has one row per situation: the de-shuffled scores of both plans, the judge's preference and one-sentence
reason, plan length, and for T17 the turns, seconds, cost and peak context of each planning run. `digests/` holds the
digest each DIGEST arm received; `plans/` holds all 32 plans. The goal texts given to the arms and the judges'
reference files are not included. `python recompute.py` rebuilds every count above from `rows.json`.
