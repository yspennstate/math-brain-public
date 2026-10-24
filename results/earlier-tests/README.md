# Archive of earlier brain tests

`TESTS.md` describes the tests the paper relies on. This folder keeps the rows of earlier tests that are not in it, so
that each number can still be recomputed. Each subfolder is self-contained and has its own README.

## ab30-2026-09-23: thirty math tests, brain on against brain off, with every agent's tokens counted

Thirty questions (twenty proof audits and ten questions about results held in the store), each answered by one Claude
agent with the brain and one without, graded blind against keys by three graders. Four later rounds reused the design:
round 2 compared two ways of delivering the brain to headless agents, round 3 re-ran the twenty proof audits with the
checks delivered, round 4 asked research questions, and round 5a tested a change to how the store reports what it does
not hold.

| round | items | points, brain on / off | cost, brain on / off |
|---|---|---|---|
| 1 | 30 | 27 / 26 | $61.26 / $40.48 in total; median $1.68 / $0.77 a run |
| 2 | 10 | not graded (two brain arms) | $17.05 as delivered / $17.37 with the lighter delivery |
| 3 | 20 | 18 / 17 (both graders) | $30.88 / $15.66; median $1.37 / $0.56 |
| 4 | 14 | 13 / 13 | median item cost 1.81 times the control |
| 5a | 8 | 7 / 6 (6 for the earlier version of the brain) | median item cost 1.56 times the control |

Almost every answer in every round received full credit, and every difference between arms in rounds 4 and 5a was a
90-minute timeout. What these rows support is the cost of the brain and what it delivered, not a gain in accuracy: on
questions a strong model already answers, the brain made a run cost between 1.5 and 2.2 times as much. The later tests in `TESTS.md`
moved to questions whose answer has to be recalled for that reason.

`python recompute.py` derives every number above from the rows and compares it with `CLAIMS.json`; all 21 claims
match. The claims name the tables of the campaign's report, which is not included because it also carries notes about
the machine the tests ran on; every number it published is in `CLAIMS.json`. The answer keys, the graders' notes and
the raw session streams are not included either (see the folder's own README); `TREATMENT_COMMITMENTS.jsonl` holds a
hash of each counted session stream.

## three-arm-house-2026-09-29: 281 recall questions, three arms

A Sonnet solver answered 281 questions about results held in the store, drawn from seven banks (proof-audit cards,
held-out statements, blind questions written from the store's own result notes, and three levels of "where is this
proved" questions). Each question was asked three times: with nothing (`nodata`), with read access to the store's
exported files (`data`), and with the files plus the recall tool and the block the math hook serves (`data_brain`).
Two graders marked each answer correct or not and a third decided the 41 disagreements.

| arm | correct of 281 | median input tokens | median turns | total cost |
|---|---|---|---|---|
| nothing | 42 | 2,985 | 1 | $2.32 |
| files | 230 | 36,017 | 7 | $13.85 |
| files + recall + served block | 252 | 7,320 | 1 | $4.45 |

Files against nothing: 190 against 2 discordant pairs (exact McNemar p = 5.9e-54). Recall on top of the files: 36
against 14 (p = 0.0026), +7.8 points on first attempts, at a fifth of the input tokens and a third of the cost of
reading the files. `REPORT_r2.txt` adds two arms run the same evening: `data_nav`, the files with one added sentence
telling the agent that computed results live in the store rather than the memory folder (29 against 22 over files
alone, p = 0.40; it gained on the bank that needs both sources and lost 10 items on another), and `data_recall`, the
files and the recall tool without the served block (32 against 21, p = 0.17). `REPORT_CONTRACT.txt` reports the
same run by cohort, with the check that the store did not change between the export and the run. The rows give
each item's id and verdict per arm; the questions and keys are not included.

## three-arm-w7-2026-10-04: 80 problems on our own mathematics, five arms

Eighty problems (50 about stored results, 10 open conjectures from the store, 20 controls that need no store) answered
by a Sonnet solver under five arms and graded blind on a 0 / 0.5 / 1 scale, with a separate flag for a false claim made
with confidence.

| arm | full credit of 80 | mean mark | confident false claims |
|---|---|---|---|
| nothing | 27 | 0.41 | 5 |
| files | 62 | 0.82 | 8 |
| files + served block + recall | 68 | 0.89 | 7 |
| served block only | 53 | 0.73 | 4 |
| files + recall | 71 | 0.92 | 9 |

Files against nothing: +43.8 points (p = 2.8e-9). The full brain against files alone: +7.5 points, not significant at
n = 80 (p = 0.29); recall on top of files +11.2 points (p = 0.064). The served block on its own, without any search,
lifted full credit from 27 to 53. It carried the right card unasked on 36 of the 60 store and conjecture problems.

## agents100-2026-09-07: 100 proof-audit items, an agent that queries the store against one that cannot

One hundred items drawn with a fixed seed from a bank of 12,193 arXiv probability results whose proofs were rewritten
as numbered steps, with one step altered in 67 of them. Ten agents per arm, same model; the only difference was whether
the agent could query the store. The design was registered in `PROTOCOL_100Q.md` before any answer was served.

| arm | full credit on the 67 flawed items | detected at all | false positives on the 33 clean |
|---|---|---|---|
| no store | 37 | 40 | 6 |
| with store | 36 | 38 | 5 |

Paired by item: -1.5 points, 95% interval -11.2 to +8.2, exact McNemar p = 1.0. The store was used (about 95 queries,
65 items marked as informed by it) and no item's unaltered step was in the store, so the null is not a delivery or
leakage failure. It is underpowered (a powered test needs 129 flawed pairs) but it had room to show a gain: the
control arm sat at 55 percent. Both arms missed the altered hypotheses almost entirely (1 of 9 with the store, 0 of 9
without). The report reads this with two earlier tests: retrieving notes about a result does not check whether a step
uses that result correctly. The per-item verdicts, the sample's item list and the per-item fault labels are not
included.

## bank10k-replication-2026-08-22: right notes against scrambled notes, 160 paired proof audits

A replication of an 80-item test from 17 Aug on a second, difficulty-screened bank. A Haiku solver audited flawed and
clean proofs under three arms: three notes served from the brain, the same notes reassigned to the wrong items (a
placebo matched in titles and length), and no notes. The protocol was frozen before the analysis (`PROTOCOL_FROZEN.md`).

| arm | full credit on the 160 primary items | false positives on clean controls |
|---|---|---|
| brain notes | 128 (80.0%) | 1 of 40 |
| scrambled notes | 117 (73.1%) | 2 of 41 |

Brain against placebo: +6.9 points, 95% interval +0.8 to +12.9, discordant items 18 to 7, exact McNemar p = 0.043, so
the pre-registered replication succeeds. Against no notes at all (77.4%) the brain arm gains only +2.6 points (p = 0.50):
about half of the gap is the placebo pulling the solver below the no-notes arm. What the run shows is that the right
notes beat wrong ones; it does not show that an agent with the brain beats one without it. `METRIC_CARD.md` is the
one-page statement; `audit_regrade.json` holds the primary and sensitivity contrasts.
