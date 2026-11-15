# A working list of major open problems in probability and in the probability side of deep-learning theory

This folder holds the list of open problems that our open-problem work has targeted since 14 October 2026, together
with the audits that checked it. Part one is about two hundred well-known conjectures in probability theory. Part two,
added on 16 October, is about two hundred open problems in deep-learning theory that are problems in probability
(random networks, high-dimensional learning, sampling and diffusion, training dynamics). Each row gives:

- the statement;
- a primary source and locator;
- why the problem matters;
- where it stands;
- any audit verdict.

`LIST.md` is the readable list and `list.jsonl` holds the same rows as data, one JSON object per row.

## How the list was made

The rows were first written from a language model's own knowledge and are ordered by fame within each domain. They
were then checked against the literature in several independent passes:

- **w672 and w673.** Two auditors (Codex, gpt-6.1-sol) compiled blind lists of their own. They then checked each row's
  statement and source against arXiv and the cited papers.
- **w684.** A status audit searched the primary literature posted since 1 August 2026 for claimed solutions.
  - `CLOSURE_CLAIMS.jsonl` holds the closure claims it found.
  - `RETIREMENTS.jsonl` holds the retirements it recommends, each with an exact statement match and page evidence.
  - `STATUS_UPDATES.jsonl` holds field corrections.
  - `VERIFY.jsonl` holds source-backed verdicts on rows marked for verification.
  - A negative verdict means only that no closure turned up within the recorded query, not that the problem is open.
- **w683.** A set of batches (`audits/w683_20261015/batch_*`) worked through individual rows in detail. Each claim
  against a row has its own versioned note under `audits/`. Each numerical check has its own script and JSON output
  under `checks/`. An `ARCHIVE_MANIFEST.json` records the hashes.
- **w687.** This pass read the sources of the deep-learning rows (T223 onward) and recorded a verdict for each.
  - Where it found a statement faulty, it wrote a repaired form, and that form is the one worked on.
  - `SOURCE_CORRECTIONS.jsonl` lists the citations it fixed.

A row found to be solved, misquoted or not central enough is retired under its own id and listed at the end of
`LIST.md`, together with the paper that settles it. Ids are never reused, so every audit stays keyed to its row. At
the last build, 393 rows were live and 86 were retired. `where_it_stands_checked` is false on rows whose status line
has not been checked against the current literature. Read those lines as a guide, not a survey.

`src/rows_*.py` are the row sources the list is built from. The build script is not included.

## Credit

The problems are the work of the people who posed them and of the many who advanced them, and the cited sources are
the record of that. The list leans especially on several surveys and problem collections:

- G. Grimmett, *Percolation*;
- I. Benjamini and O. Schramm, "Percolation beyond Z^d, many questions and a few answers";
- O. Häggström's account of Schramm's contributions;
- D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*;
- R. Lyons and Y. Peres, *Probability on Trees and Networks*;
- R. O'Donnell, *Analysis of Boolean Functions*;
- D. Levin, Y. Peres and E. Wilmer, *Markov Chains and Mixing Times*.

Each row names its own primary source, and every retirement points to the published argument that settles it. The
solutions belong to their authors. This list only records them.

## Reusing it

`list.jsonl` is meant to be read by programs. Its fields:

- `problem_id`, `title`, `domain`;
- `statement` and `statement_caveat`;
- `source`, `locator` and `url`;
- `why_important`;
- `where_it_stands` and `where_it_stands_checked`;
- `ledger_status`, plus `retired_reason` on retired rows;
- `audit`, the auditor's verdict where there is one.

The list is a working tool, not a ranking. Corrections are welcome.
