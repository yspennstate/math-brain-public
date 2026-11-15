# Finding and ranking open problems, September to November 2026

The open problems the agents work on did not come from one list. They were collected from surveys, monographs,
problem collections and recent arXiv papers, checked against the literature, ranked, and later reviewed. This
folder holds the ledgers and scripts of five of those passes, in the order they were made.

## The passes

- `probability_1000_intake_agent/` (7 September). The first intake ledger outside the main campaign: 35
  sources, problem records `C0001`.., one recorded attempt per admitted problem, and the cycles that loaded each
  batch into the math store (`brain_cycle_*`, `brain_bundle_*`, `brain_ingestion_*`) with before-and-after
  retrieval checks (`brain_retrieval_*_before.json`, `*_after.json`). `RANKING_2026-09-07.md` ranks 555 open
  problems from easy to hard against a written rubric; `SOLVER_MAP.md` says which method family each one calls for.
  `raw/` keeps the numerical checks behind the partial results (coupling linear programs, entropy and domination
  checks).
- `probability_1000_intake_E_20260908/` (8 September). Intake E: 47 sources not mined by any earlier ledger, 113
  records, 110 attempts, and a source identity check (`raw/source_identity_check_20260908.json`) confirming each
  PDF was the intended document before any row was written. `CORRECTIONS.md` lists rows withdrawn on rereading.
- `probability_1000_intake_I_20260914/` (14 September). Intake I: 117 records from 34 sources, among them every
  numbered open problem of Aldous and Fill, the end of Janson's 2012 survey, Schramm's problem collection, van der
  Hofstad's Saint-Flour notes, Lyons and Peres, and the first-passage percolation survey. `I0001_exact_gpu/` is an
  exact GPU computation for the first row.
- `open_problems_200_2026_10_10/` (10 October). The list of 200 publishable and doable probability problems drawn
  from all the intakes, each searched for papers since 2019 (`LITERATURE_UPDATES.tsv`), with the build scripts
  under `build/` and the tree-ladder computation for P0062.
- `top200_review_2026_11_10/` (10 November). A review of the two top-200 lists (probability and deep learning):
  a verdict per row (keep, restate, move, removed as solved by others or by us), replacement candidates screened
  against every listed and retired row (`candidates_*_screen.tsv`), and `CLOSEST.md`, the rows on which a verified
  partial result already stands, ranked by how much of the row it covers.

## What the ledgers record

Every problem row carries its statement as the source gives it, the source, and a line on what is known. A row
found settled in the literature stays in the ledger with `admitted = false` and the paper that settles it, so that
nobody attempts it again. The extracted source texts and raw search responses are not copied here; the source
lists give the bibliographic data needed to find each one.

## Credit

The problems belong to the mathematicians who posed them: among the largest sources are Aldous and Fill
(Reversible Markov Chains and Random Walks on Graphs), Lyons and Peres (Probability on Trees and Networks),
Schramm's problem collection, Janson, van der Hofstad, Heydenreich and van der Hofstad (Progress in High-Dimensional
Percolation and Random Graphs), and the authors of the surveys and papers listed in each `sources.jsonl`. Where a
row is marked settled, the credit for settling it is in its `resolved_by` field. The ledgers, rankings and
attempts were produced by AI agents (Claude and Codex) and have not been reviewed by a person.

## Reusing it

`intake_tools.py` in each intake reads and validates the ledger schema (`probability-source.v1`,
`probability-attempt.v1`). To start a new intake, copy one, give its ids a fresh prefix, and check each new source
against the union of the existing `sources.jsonl` files before fetching it.
