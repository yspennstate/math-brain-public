# The nightly math-brain gate, 11 September to 25 October 2026

A regression gate runs every night and after each change to the math hook. Among its instruments it sends one fixed bank
through the production entry point (`framework/dreaming/eval_math_hookpath.py`) and refuses a change that pushes a count
below its floor. The bank is the fresh probe of 3 September, the same 218 prompts as in `hook-path-ablations-2026-09-23`:
89 results asked in two forms (`q_content` describes the result without naming it, `q_hinted` names it the way a reader
would), and 40 results the store did not hold when the bank was written. An answerable prompt counts when a served title is
the asked result, and counts as first when that card heads the block. An unanswerable prompt that gets any card is a false
fire, unless the card is its target and the store has since gained it.

This folder keeps the hook's mark on every one of the 218 prompts for each of the 51 complete runs of the bank between
11 September and 25 October, and the gate's verdict for all 88 of its runs in those weeks (20 were quick runs that skip the
bank). Each cell gives served / first / silent, of 89; the last column counts unanswerable prompts that got a card, of 40,
with the number of those that were the target in brackets.

| run | unnamed | named | unanswerable served (target) |
|---|---|---|---|
| 11 Sep | 66 / 50 / 13 | 81 / 76 / 4 | 30 (0) |
| 14 Sep | 72 / 57 / 9 | 84 / 81 / 3 | 27 (7) |
| 24 Sep | 72 / 56 / 8 | 86 / 83 / 1 | 29 (7) |
| 6 Oct | 71 / 55 / 9 | 87 / 84 / 0 | 26 (8) |
| 7 Oct, nightly | 56 / 43 / 19 | 77 / 74 / 10 | 27 (8) |
| 7 Oct, after the revert | 66 / 50 / 11 | 85 / 82 / 2 | 26 (8) |
| 19 Oct | 60 / 47 / 14 | 85 / 81 / 2 | 26 (8) |
| 25 Oct | 72 / 60 / 7 | 87 / 83 / 1 | 26 (10) |

Over the six weeks the unnamed form went from 66 to 72 served and from 50 to 60 first, and the named form from 81 to 87
served and from 76 to 83 first; silences fell from 13 to 7 and from 4 to 1. The 40 unanswerable prompts drew 30 wrong cards
on 11 September and 16 on 25 October; ten more drew the target itself, which had entered the store in the meantime. The
steps of 14 September and 23 September line up with selector changes measured on their own: name coverage and the rule
that keeps a definition below the result it defines, then the named-family rule.

The gate passed 55 runs, breached on two, ended in an error on two and was inconclusive on 29. The breach of 7 October had
two causes. A filter landed on 6 October that dropped cards matched only through glued symbols; it silenced the unnamed form
on ten more prompts and the named form on ten, and failed the health check's unnamed Hoeffding and Turán probes. Separately, 35
correction cards lacked their schema version and failed the same check. The unnamed form read 56 of 89, under its floor of
0.65, and the locate instrument reached 0.825 of its bank against a floor of 0.90. The filter was reverted that morning and
the run after the revert read 66. The breach of 19 October was the health check alone: on an unnamed Turán question the hook spoke without
the Turán card. The bank's counts were within their floors that night. After the revert the unnamed form stayed between 60
and 66 until the run of 25 October brought it back to 72; most nights in between were inconclusive, so the series does not
show when the recovery happened.

From 8 October most nights are inconclusive because an instrument ran out of time on a heavily loaded machine. Where such a
night still finished the bank, its marks are in `rows.json`.

## Files

`rows.json` holds one row per prompt: an opaque item number shared with `hook-path-ablations-2026-09-23` (the two forms of
one result share it), the kind, the area, the form and a string of marks with one character per bank run. It also holds
each gate run's verdict, the reasons it gave and the fractions it recorded. The bank's keys name the results, so they and
the prompts are not included. `python recompute.py` derives every count above from the marks, checks them against the
fractions the gate recorded, and lists the items whose mark differs between the first and last run.
