# Open problems

Attempts on open problems, most of them in probability and combinatorics: proofs,
partial results, counterexamples, verification code and papers in progress. Each
result carries its own status in its folder. Nothing here is refereed unless that
folder says so, and a claimed proof is a claim until a reader checks it.

## Where things are

| folder | what it holds |
|---|---|
| `proofnet24/` | one folder per problem, named by a short code (`P03-fei`, `C31-kemeny-constant`, `HARD10-02`, `NM13-05`, ...): statements, attempts, proofs, counterexamples and the code that checks them |
| `OPEN_PROBLEMS_200/` | a list of two hundred open problems in probability, each with its source, a summary and what is known around it |
| `Big Open problem in probability theory/` | work on one larger problem, kept apart from the list |
| `probability_1000*/` | a bank of a thousand probability problems, the intake that built it, and the attempts on it (`prob1000_lean_20260908/` holds the Lean checks) |
| `probability_campaign_2026_09/`, `probability_campaigns/` | campaigns that worked through a problem list one problem at a time |
| `erdos_problems_bench_2026_09_07/`, `hard8_2026-09-16/` | fixed problem sets used to compare methods |
| `paper*/`, `papers/`, `publications/` | papers written from the attempts above, with their sources |
| `qform/`, `least_sv_coordinate_optimized_2026_07_06/`, `open_problem_dl_2026_07_07/` | single studies: a quadratic-form density problem, the least singular value of a coordinate-optimized Gaussian submatrix, and an attempt on an open problem in the theory of deep networks |
| `research*/`, `runs/`, `artifacts/` | working runs and the files they produced |

Folder names inside a problem often carry a date and a run label (for example
`account02/B16/20260924T183053Z-...`). The label only says which of several
parallel runs produced the attempt; the mathematics is in the files.

## How to read a result

Start from the problem's own folder. A finished attempt has a statement, a proof
or a counterexample, and, where a computer was used, the code with the input that
reproduces the number. Where a Lean file exists, it is the strongest form of the
claim. Where a status line says partial, conditional or retracted, take it at its
word.
