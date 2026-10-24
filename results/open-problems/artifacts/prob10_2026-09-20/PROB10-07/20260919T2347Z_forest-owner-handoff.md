# PROB10-07 handoff to the historical forest-owner chain

This file is a non-mutating handoff for readers of the earlier P14/HARD10-01 uniform-forest work. It does not edit or seize any P14/HARD10 claim.

Historical owner pointers read before the new work:

- `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md` — forest source handed off with complete-size metric 9 and minimal-counterexample reduction to 3-connected graphs.
- `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md` — separate hard-track handoff, same complete-size metric 9 and the three-terminal/degree-three-apex blocker.

The PROB10-07 complementary route does **not** run a graph-order census and does **not** attack the old degree-three-apex response inequality. It proves a separate infinite 3-connected family by an exact five-state terminal-partition transfer:

> For every integer `n>=1`, a forest chosen uniformly from all forests of `K_{3,n}` has pairwise negatively correlated edge indicators. For `n>=2` every distinct pair is strictly negatively correlated. Under the Cocks fixed-graph implication already used in the P14 chain, each `K_{3,n}` is consequently independence-correlated for all positive real edge weights.

The exact count formulas and proof are in the immutable PROB10-07 run report. The checker is

`artifacts/prob10_2026-09-20/PROB10-07/20260919T2347Z_k3n-transfer_checker.py`

with executed output

`artifacts/prob10_2026-09-20/PROB10-07/20260919T2347Z_k3n-transfer_checker.out`.

This does **not** change the universal source status (OPEN) or the complete finite-order metric (9). It adds an all-parameter infinite graph-family result and a low-rank transfer mechanism that may be useful for other 3-connected bipartite families.
