# NM13-11 P0257 run-report erratum (non-load-bearing wording correction)

This artifact corrects one sentence in the immutable run report

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T21-05-00Z__p0257-third-d2-topology-movement.md`

without editing or replacing that report.

In Section 7, after the exact bounds

`d13^2 >= 109/80 > 1`

and

`d14^2 <= 13617/10000`

with

`109/80 - 13617/10000 = 1/1250 > 0`,

the report says `d13>d14>1 uniformly`. The final `d14>1` clause is not implied and is unnecessary. The correct conclusion is

`d13^2 > max{1,d14^2}`,

or equivalently `d13>1` and `d13>d14`.

The topology proof uses only those two separate inequalities, together with `d24<1`, `d23>d13`, `d14>d24`, and `d14>d34`, all of which are exactly certified by the archived checker. Therefore this wording correction changes **no topology conclusion, no guard bound, no correction term, and no metric endpoint**.

No second run report is created; the immutable report remains the sole report for this invocation.