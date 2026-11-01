# PROB10-07 -> forest-owner handoff: complete tripartite fixed width six

Parent source remains Grimmett–Winkler uniform-all-forests pairwise edge negative correlation. This is a restricted structural theorem, not a universal resolution and not graph-order enumeration.

New exact theorem in this run: for every integer `n>=1`, every distinct edge pair is strictly negatively correlated under the uniform measure on all forests of each of

- `K_{1,5,n}`;
- `K_{2,4,n}`;
- `K_{3,3,n}`.

Together with the immediately preceding PROB10-07 theorem for all complete tripartite graphs whose two smallest parts sum to at most five, this gives strict p-NC for every `K_{a,b,c}` whose two smallest part sizes sum to at most six.

Mechanism: full Bell-partition transfer on the six fixed terminals; `M_6=7I+N_6`, `N_6^6=0`; exhaustive marked-edge orbit reduction; every normalized Rayleigh polynomial has nonnegative exact rational coefficients and is positive on its physical integer domain. Exact checker/output:

- `artifacts/prob10_2026-09-20/PROB10-07/20260920T0540Z_tripartite-sum6-d2a7_checker.py`;
- `artifacts/prob10_2026-09-20/PROB10-07/20260920T0540Z_tripartite-sum6-d2a7.out`.

The executed output ends `PROB10_07_TRIPARTITE_SUM6_EXACT_PASS` and independently regresses every actual edge pair for `n=1,2` in all three families.

Nonoverlap: P14/HARD10-01 own the complete-order-nine / minimal-counterexample / separator history; this run does not repeat their census. NM13-04/NM13-08 own triangle-join / right-layer structural families; this result is a complete-tripartite fixed-core theorem and does not claim their classes.

Preserved history:

- `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`;
- `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`.

Parent source status remains OPEN/PARTIAL; complete-all-graphs order metric remains 9; novelty/priority of this exact fixed-width theorem remains UNVERIFIED pending independent literature/audit work.