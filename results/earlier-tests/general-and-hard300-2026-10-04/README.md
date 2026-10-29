# General problems and the hard 300, five and six arms (4 October 2026)

Two banks run on the same evening as the 80 problems in `three-arm-w7-2026-10-04`, with the same solver (Claude
Sonnet), the same budget of ten minutes a problem and the same instructions for every arm. Keys were out of the
solvers' reach, and nothing was tuned on these problems before the run.

| arm | what the solver had |
|---|---|
| nothing | the model alone: no tools, no files, no note |
| documents | the memory folder and a snapshot of the store, searchable with read, grep and glob |
| brain | documents, the recall command, and the note the brain hook served for the problem |
| served note only | the served note and nothing else |
| documents and recall | documents and the recall command, without the served note |
| math brain (hard 300 only) | documents plus the math brain as deployed: its notes, its audit and Lean prompts, one audit turn before the answer stands, its recall and a Lean check |

## 854 general problems

The frozen held-out half of the September bank: computations, proof audits with one planted fault, theorem
applications and assumption checks, graded exactly (sympy for values; the verdict and the faulty line for proofs).

| problems | n | nothing | documents | brain | served note only | documents and recall |
|---|---|---|---|---|---|---|
| all | 854 | 86.5% | 86.8% | 86.9% | 86.2% | 86.4% |
| assumption check | 40 | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| compute | 464 | 84.1% | 84.5% | 84.3% | 84.3% | 83.8% |
| proof audit | 188 | 79.8% | 79.8% | 80.3% | 78.2% | 79.3% |
| theorem application | 162 | 98.1% | 98.1% | 98.8% | 97.5% | 98.8% |

Every paired difference is under half a point (brain against nothing 6 to 3, p = 0.51; brain on top of documents 5 to
4, p = 1). These problems are complete as stated, the solver opened a file on at most one of the 854 in any arm, and
nothing stored could help. The brain did no harm either. Cost per answer ran from 0.0049 dollars (nothing) to 0.0072
(brain).

The hook fired too often. It served a note on 394 of the 854 problems (46 percent), on 174 of the 188 proof audits,
because their text shares words with stored proofs rather than because a stored result bears on them. On the problems
where it fired, the note alone turned 2 wrong answers right and 6 right answers wrong: not significant, but in
the wrong direction, and paid for in tokens on every problem where it fired.

A note served to many unrelated problems carries no information about any of them. The next day the hook was
probed for such notes on 100 problems of the hard computation bank (25 families, seed 5). It fired on 92 and
filled 257 note slots. The ten notes served most often filled 81 of them, and nine of the ten matched the
bank's own families: bipartite matching, Hall's theorem, the Andrasfai-Erdos-Sos theorem, multiplicative order,
divisibility, Euler's and Fermat's theorems, Wilson's theorem and Euclid's lemma. The tenth, a research attempt on a
scaling limit in the discrete Gaussian free field, was served on 7 problems that have nothing to do with it, and the
Beurling-Deny decomposition of a Dirichlet form, just below the ten, on 6.

## The hard 300

Built so that an arm can fail and so that what the store holds matters:

- A, 70 exact counts recorded in the store (self-avoiding walks in strips with excluded sites), worded differently from
  the record, among hundreds of near-duplicate records;
- B, 40 that need two records and a subtraction;
- C, 90 on our own results, each drafted from one record and kept only when a second model given that record alone gave
  the same answer;
- E, 100 hard computations nobody can look up (Stirling numbers, tilings, spanning trees, hitting times and more), every
  key computed twice by independent routes.

| problems | n | nothing | documents | brain | served note only | documents and recall | math brain |
|---|---|---|---|---|---|---|---|
| all | 300 | 62.3% | 88.0% | 93.7% | 73.7% | 96.0% | 79.3% |
| store-dependent (A+B+C) | 200 | 43.5% | 82.5% | 91.0% | 60.5% | 95.0% | 69.0% |
| A, store counts | 70 | 2.9% | 78.6% | 94.3% | 42.9% | 98.6% | 31.4% |
| B, two records | 40 | 25.0% | 65.0% | 70.0% | 27.5% | 87.5% | 70.0% |
| C, our own results | 90 | 83.3% | 93.3% | 97.8% | 88.9% | 95.6% | 97.8% |
| E, no lookup | 100 | 100.0% | 99.0% | 99.0% | 100.0% | 98.0% | 100.0% |

Paired on the 200 store-dependent problems (exact McNemar): documents against nothing 81 to 3 (p = 1e-20); recall on
top of documents 30 to 5 (p = 2e-5); brain on top of documents 28 to 11 (p = 0.009); the served note alone against
nothing 39 to 5 (p = 1e-7); the served note on top of search 7 to 15 (p = 0.13). On the 100 problems nobody can look up,
every arm scored 98 to 100 percent.

So the help came from the recall command. The served note is worth a good deal on its own, but once the solver can
search it stops helping, and if anything it pulls the other way.

The math brain arm matched documents on everything except the store counts: 22 of 70 there against 55. Its counting
check asks for a recount by a second method, and the only tool for one was Lean. The solver tried Lean on 69 of the 70
lookups and 30 of them ran out of time, 24 while still waiting on a Lean check. Over the whole bank Lean compiled 4
times; 61 calls were refused by the harness because the Lean source had a line starting with `#`, and 29 were held by
the Lean check's own memory gate. The audit turn changed 4 final answers, all from wrong to right. This is the version
1 result listed under "What did not help" in `TESTS.md`; the later version routes to recall first.

Failures and cost by arm on the hard 300:

| arm | out of time | answered UNKNOWN | answered and wrong | median cost (dollars) | median seconds |
|---|---|---|---|---|---|
| nothing | 86 | 11 | 16 | 0.007 | 13 |
| documents | 16 | 8 | 12 | 0.016 | 17 |
| brain | 2 | 9 | 8 | 0.014 | 12 |
| served note only | 53 | 14 | 12 | 0.011 | 16 |
| documents and recall | 2 | 1 | 8 | 0.017 | 16 |
| math brain | 38 | 33 | 3 | 0.030 | 28 |

## Later versions of the math brain arm

Two follow-ups were written after the main results and are not part of the preregistered test. Version 3 looks the
answer up first and prices each check; it scored 248 of 300 (41 of 70 on the recorded counts), against 288 for
documents and recall (8 to 48, p = 5e-8), and ran about three hours after that arm rather than beside it. Version 4
finishes when Lean cannot run: Lean is optional, a failed Lean check sends the solver back to the record, and it searches
the memory notes as well as its own recall, lookup first. On the 110 store problems it scored 102 against 104 for
documents and recall (6 to 8, p = 0.79). Version 1 had scored 50 on these problems.

The versions were then run side by side on the store problems, at the same time on the same machine, with the old
prompts run again because by then the machine had the memory for Lean to start:

| comparison | problems | n | right (first / second) | only first / only second | p | out of time | Lean calls |
|---|---|---|---|---|---|---|---|
| v4 against v3 | recorded counts | 70 | 67 / 41 | 26 / 0 | 3e-8 | 3 / 20 | 12 / 42 |
| | two records | 40 | 35 / 21 | 14 / 0 | 0.0001 | 2 / 16 | 14 / 27 |
| v4 against v1 | recorded counts | 70 | 67 / 28 | 39 / 0 | 4e-12 | 3 / 18 | 12 / 69 |
| | two records | 40 | 35 / 31 | 9 / 5 | 0.42 | 2 / 2 | 14 / 36 |
| v3 against v1 | recorded counts | 70 | 41 / 28 | 19 / 6 | 0.01 | 20 / 18 | 42 / 69 |
| | two records | 40 | 21 / 31 | 3 / 13 | 0.02 | 16 / 2 | 27 / 36 |
| new checks only against v1 | recorded counts | 70 | 30 / 28 | 9 / 7 | 0.80 | 21 / 18 | 56 / 69 |
| | two records | 40 | 20 / 31 | 2 / 13 | 0.007 | 15 / 2 | 32 / 36 |

Looking up first helped on the recorded counts and cost on the two-record questions, where version 3 ran out of time
on 16 of 40; the change that closed the gap was letting the solver finish without Lean.

## Faults found during the run

- 22 calls never reached the model: a Claude process read the shared settings file while another was rewriting it and
  exited at once. The driver now retries that case, and every affected problem was asked again before grading.
- The recall command crashed on Windows whenever a result held a Greek letter or a German sharp s (60 titles and 1,149
  statements in the store). With the fix, and a fix to the passage search behind it, the right passage reached the
  reader on 99 per cent of 9,813 cases drawn from the store, against 70 per cent before.
- 12 calls on the hard 300 returned the account's usage-limit message instead of an answer. They were set aside and
  asked again, and the driver now waits and retries when the limit is hit.
