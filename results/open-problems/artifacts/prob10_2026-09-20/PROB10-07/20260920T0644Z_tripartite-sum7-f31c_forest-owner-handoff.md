# PROB10-07 non-mutating handoff to the forest-owner history

This file records a new complementary structural-family theorem without editing or seizing any P14/HARD10-01 claim.

Consumed owner/history pointers before the work:

- `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md` — complete arbitrary-graph order metric `9`, minimal-counterexample reduction to 3-connected graphs, surviving three-terminal/mixed-term obstruction, and mandatory P14 handoff.
- `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md` — complete order-nine dense-sector history and equivalent three-separator/two-point-mixture obstruction before HARD10-01 rotated away.
- `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md` — preserved pre-refocus Komlós state.
- newest PROB10-07 predecessor: `runs/prob10_2026-09-20/PROB10-07/20260920T0540Z_tripartite-sum6-d2a7.md`.

New theorem in this run: for every integer `n>=1`, every distinct edge pair is strictly negatively correlated under the uniform measure on **all forests** of each of

`K_{1,6,n}`, `K_{2,5,n}`, and `K_{3,4,n}`.

Together with the earlier PROB10-07 transfer results, this proves the source inequality for every complete tripartite graph whose two smallest part sizes sum to at most seven.

Nonoverlap: this is not a graph-order census, does not alter the arbitrary-graph metric `9`, does not resolve the 3-connected ten-vertex obstruction, and does not claim the P14/HARD10-01 separator reductions. It uses a complete-tripartite repeated-part transfer. The new mechanism is an exact forced-spoke operator factorization for marked repeated vertices, avoiding joint enumeration of the fixed core with one or two marked stars.

Exact artifacts:

- idea note: `artifacts/prob10_2026-09-20/PROB10-07/20260920T0644Z_tripartite-sum7-f31c_idea.md`;
- checker: `artifacts/prob10_2026-09-20/PROB10-07/20260920T0644Z_tripartite-sum7-f31c_checker.py`;
- executed output: `artifacts/prob10_2026-09-20/PROB10-07/20260920T0644Z_tripartite-sum7-f31c.out`, ending `PROB10_07_TRIPARTITE_SUM7_EXACT_PASS`.

Status remains `OPEN / PARTIAL` for the universal Grimmett–Winkler conjecture. No novelty/priority claim is made from the bounded literature search.
