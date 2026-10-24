# account02/B20 r12 — final correction refresh addendum

Programme `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`. This addendum is part of run `20260922T145947Z-account02-B20-QFORM-r12` and preserves the main report immutably.

A final control/correction refresh at brain commit `d178e8c7b67bacc0328a928ed2807401e901b7a0` added the source-backed correction `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1` from account02/B01. Its family `A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)` has nonzero spectrum `{1,1,-1}` but any chosen singleton plus one coordinate from each bank has reciprocal rank-two aggregate determinant cost diverging like `sqrt(m)`. The family is not a QFORM counterexample because a completed diffuse-rank-two/dependence-safe-square theorem controls it uniformly.

This correction does **not** refute either theorem proved in the main r12 report. `QFORM-SCHUR-THIRD-DIRECTION-RETENTION-v1` is an exact singular-value statement for a scalar pivot already satisfying its hypotheses. `QFORM-HEAVY-DIAGONAL-SCHUR-DESCENT-v1` likewise assumes an actual heavy diagonal-dominated physical row and never extracts a fixed physical triple or pays a reciprocal three-coordinate minor.

It does sharpen the wording of the first unpaid implication. `QFORM-LOW-SR-THREE-WAY-PACKET-EXTRACTION-v1` must allow many-coordinate source-realizable aggregate banks and diffuse/dependence-safe endpoints; it may **not** be interpreted as forcing one uniformly conditioned physical triple. In particular, in the cross-dominated branch the first operation must be bank aggregation or a diffuse/separator descent before any reciprocal fixed-triple determinant payment. In the localized large-pivot branch the quantitative collar from r12 remains valid:

`|a|>=tau>=1/4`, `s_2(S)>=1/4`, `max_j (P_range(S))_jj>1/32`, `c_i>=1/64`, `||b||<=|a|`.

Full QFORM remains open. Continuity remains separate.
