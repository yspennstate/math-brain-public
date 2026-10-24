# P0282 idea before archival checker — turn the uncovered region into a thin depth seam

Date: 2026-09-18 UTC
Worker: NM13-07
Source: P0282 / Chen fixed-size LIS log-concavity

The frozen metric remains `N_exact=83` on entry. The predecessor already gives two exact certificate families: all source inequalities in rows `n<=83`, and all source inequalities in the depth variable `s=2j-n` through `s<=40` for the relevant defects. Its coverage lemma says that row frontier `N` and depth frontier `S` completely cover every defect `j<=floor((N+S+1)/2)`.

This run will not spend its validation budget recomputing a whole rectangle. It will first attack the negation on the exact complement of the existing certificates. To raise the complete-defect frontier from 62 to 66 while holding `N=83` fixed, it is enough to extend the effective depth frontier from 40 to 48. The only genuinely new source-valid points are those with

`41 <= s <= 48`, `j <= 66`, `n=2j-s > 83`.

There are exactly 20 such seam points. The tail-correction formula proved in the predecessor family has finite support at every fixed `s`, so each of these can be evaluated with exact integer arithmetic from the fixed-defect recurrence and the finite Plancherel tail. If all 20 margins are positive, then the coverage lemma gives a genuine source theorem for every source-valid `n` at every defect `1<=j<=66`.

Section-B labels for this run are all recycled because all 30 were already used on P0282, but the mathematical attack is new relative to the previous triple: #2 ATTACK THE NEGATION FIRST (search the 20-point uncovered seam for a counterexample before promoting a theorem), #5 ADD A PARAMETER AND DIFFERENTIATE IN IT (use depth `s=2j-n` as the controlling deformation parameter and inspect where certificate support grows), and #30 DO ONE SCALE, ONE DIRECTION AT A TIME (advance only the depth layers 41..48 rather than another full row/rectangle). None is represented as previously unused.

Only after this route is stated do we archive and run a checker. The checker must report the exact number of seam points, exact positive margins, finite tail-atlas size, and a terminal `ALL_EXACT_CHECKS_PASS`. This is theorem progress even if the frozen row metric does not move; the report must still say `N_exact: 83 -> 83` and `no movement` for that frozen metric.
