# Codex open-problem rounds, 14-15 November 2026

This folder holds the working record of seven rounds of automated attempts on rows of our open-problem
lists (the top-200 probability and analysis list and the related T/AV rows). Each attempt is one folder
named after its row. It keeps what the worker was asked, what it did and what it claims, so that a reader
can check a claim against the work behind it.

## What a folder contains

| file | what it is |
|---|---|
| PROMPT.md | the brief: the row, where the literature stands, what the previous round left, what to try |
| LOG.md | the worker's own running log: commands, dead ends, checks, timings |
| REPORT.md | the result; its first line is the verdict (PROVED, PARTIAL, COMPUTED, SOLVED elsewhere, NOT settled) |
| PROOF.md | the argument, when there is one |
| VERIFY.md, AUDIT.md, *.py, *.json, *.txt | scripts that check the claim and their recorded output |
| *.lean | Lean 4 statements and proofs written for the row |
| LITERATURE.md, SOLVED_ELSEWHERE.md | prior work found during the attempt |

`results/` is the first wave (two machines), `round3` to `round7` are continuations: a round-n brief is
written for every row whose round-(n-1) report said PARTIAL or PROVED a subclass, and the worker reads the
previous folder before pushing the next piece.

## Verdicts by round

| round | PROVED | PARTIAL | COMPUTED | SOLVED elsewhere | not settled |
|---|---|---|---|---|---|
| first wave | 32 | 72 | 6 | 11 | 9 |
| 3 | 18 | 49 | 3 | | |
| 4 | 22 | 45 | | | |
| 5 | 23 | 43 | 1 | | |
| 6 | 20 | 35 | 1 | | |

A PROVED verdict almost always means a side statement: a restricted model, a one-sided bound, a finite
certificate or a reduction. None of these attempts settles the open question of its row, and each report
says what is and is not covered. `VETTED_PROVED.md`, `VETTED_PROVED2.md` and `ROUND2_VERDICTS.md` record
an independent reading of the PROVED claims, with the checks that were re-run and the verdict on each.

## How the rounds ran

The workers were Codex (gpt-6.1-sol, high reasoning effort, normal speed) running headless on a Mac mini
and a laptop, one problem per process, each confined to its own folder, with the math brain available for
recall of earlier attempts and of the literature. A Claude session wrote the briefs, read the reports and
vetted the PROVED claims. The briefs and logs are kept as written; only local paths were shortened.

## Credit

The questions belong to the people who posed them, and the PROMPT.md of each row names the papers it starts
from. The largest debts are to the authors of the problem collections the rows come from and to the
groups whose methods recur here: percolation and SLE (Smirnov, Lawler, Schramm and Werner), random
nodal sets (Nazarov and Sodin), hard-sphere melting (Alder and Wainwright; Bernard and Krauth), the binary
perceptron (Krauth and Mezard) and the low-degree method for planted problems. Several rows are paired with
the Lean comparator challenges of the openai/math repository (Apache 2.0); those files are referenced by
link and not copied here. arXiv sources the workers downloaded for reading are not included either.

## Tools that are new here

- The continuation-round generator (a short shell loop over the previous round's reports): turns a round's PARTIAL
  reports into the next round's briefs, so work on a row accumulates instead of restarting.
- Certificate scripts that re-run from the folder alone (`verify_certificate.py`, `audit.py`, `recheck.py`):
  the vetting re-ran them on a second machine and compared outputs byte for byte.
- The verdict line convention: the first line of every REPORT.md is machine-readable, which is what lets the
  round generator and the tallies above work without reading prose.
