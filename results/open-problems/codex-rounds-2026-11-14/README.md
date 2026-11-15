# Worker rounds on the top-200 open problems, 14-15 November 2026

This folder is the complete working record of seven rounds of automated attempts on rows of our list of
200 open problems in probability, statistical mechanics, random matrices and theoretical computer
science. It is published as it was written, with the intermediate steps left in: the briefs each worker
received, its running log, its proofs and scripts, its final report, and the coordinator's vetting of
every claimed result. Home paths and internal names have been replaced; nothing else was edited.

## How a round works

One coordinating agent picks rows, writes one brief per row and runs a pool of language-model workers
(OpenAI Codex, model gpt-6.1-sol at high reasoning effort, normal service tier) on two small machines.
Each worker has one session, one folder and one row. The brief (`PROMPT.md`) states the problem, its
source papers, where it stands, and the earlier attempts the worker must read first. The worker then:

1. checks for five minutes whether the problem was solved elsewhere (if so it writes
   `SOLVED_ELSEWHERE.md` with the reference and stops);
2. re-checks the previous worker's main claim an independent way and records whether it holds;
3. chooses one piece that extends it (a special case, a sharper constant, more cases computed, a missing
   lemma), writes the choice in `LOG.md`, and does it: a proof goes in `PROOF.md` step by step, a
   computation is a script in the folder with its command and output in `LOG.md`;
4. tries to break its own result;
5. ends with `REPORT.md`, whose first line is one of `VERDICT: PROVED`, `PARTIAL`, `COMPUTED`,
   `NO PROGRESS` or `EARLIER RESULT WRONG`.

Each later round is a continuation brief for every row whose previous report said PROVED or PARTIAL, so a
row's folders across `results/mini1`, `round3` to `round7` read as one chain. The scripts
`make_r5.sh` and `make_r6.sh` show how a continuation round is generated from the last one. Workers run
single-threaded under 1 GB with a 20-minute cap per program, and may not write outside their folder.

## What is here

| path | what it holds | reports |
|---|---|---|
| `results/mini1/briefs/` | rounds 1 and 2 (first attempts on 122 rows) | 26 PROVED, about 70 PARTIAL, 6 COMPUTED, 11 found solved elsewhere, 9 no progress |
| `results/laptop/` | a small set of laptop runs | 6 PROVED, 2 PARTIAL |
| `round3/` to `round6/` | continuation rounds | round 3: 18 PROVED, 49 PARTIAL, 3 COMPUTED; round 4: 22 PROVED, 45 PARTIAL; round 5: 23 PROVED, 43 PARTIAL, 1 COMPUTED; round 6: 20 PROVED, 35 PARTIAL, 1 COMPUTED |
| `round7/` | the start of round 7 (in progress when copied) | |
| `PICKED.tsv`, `PICKED2.tsv` | the rows chosen for rounds 1 and 2: id, list rank, area, title | |
| `MATCH.tsv` | each row matched against our earlier notes, with a lexical score | |
| `ROUND2_VERDICTS.md` | the first line of every round-2 report | |
| `VETTED_PROVED.md`, `VETTED_PROVED2.md` | the coordinator's check of each PROVED claim: re-run checkers, brute-force enumeration, hand derivations | |

A PROVED verdict means the worker proved the piece it chose, not that the open problem is solved. Every
vetted PROVED claim so far is a bounded lemma, a reduction, a special case or an obstruction; none changes
the status of its row, and the reports say so themselves. The vetting files record which claims were
reproduced independently, which were only read, and which steps are still owed by hand. Treat any result
here as a lead to be checked, not as a theorem.

## Tools that are new here

- The continuation round: a short script turns every PROVED or PARTIAL report of one round into the next
  round's brief, which points the worker at the previous folder. Work on a row accumulates instead of
  restarting, and a row's chain of folders shows how an argument grew.
- The machine-readable verdict line: the first line of every `REPORT.md` is the verdict, which is what lets
  the round generator, the tallies above and the vetting pass run without reading prose.
- Checkers that re-run from the folder alone (`verify_certificate.py`, `audit.py`, `recheck.py`): the
  vetting re-ran them on a second machine and compared their outputs byte for byte.
- The independent re-check of the previous claim as step 2 of every brief, which is how an error in an
  earlier round surfaces as `EARLIER RESULT WRONG` instead of being built on.

## Credit

The problems belong to the people who posed and developed them. The methods that recur most across these rows come from percolation and SLE (Smirnov, Lawler, Schramm and Werner), random nodal sets (Nazarov and Sodin), hard-sphere systems (Alder and Wainwright; Bernard and Krauth), the binary perceptron (Krauth and Mezard) and the low-degree method for planted problems. Each brief names its source papers on its
`Source:` line, and each worker's `LITERATURE.md` and `REPORT.md` cite the work it relied on, with authors
as they appear on the paper; the workers were told to cite only papers they actually opened. Where a
report finds that a row was settled elsewhere, `SOLVED_ELSEWHERE.md` gives the reference, and the credit
for that result is entirely its authors'. The language-model workers produced the drafts, proofs and code
in this folder; the coordinating agent chose the rows, wrote the briefs and did the vetting. No result here
has been refereed.

The `AV_` folders check rows against OpenAI's mathematics release (github.com/openai/math) and hold copies of its
manuscript and Lean sources, redistributed under the Apache License 2.0; see `THIRD_PARTY.md` and
`LICENSE-openai-math.txt`.

A small number of files from these rounds are not included because they contain personal names or local
machine details that could not be scrubbed without changing their content.
