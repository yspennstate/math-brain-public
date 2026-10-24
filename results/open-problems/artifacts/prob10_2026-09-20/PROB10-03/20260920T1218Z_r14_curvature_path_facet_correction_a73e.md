# PROB10-03 / R14 — correction to preliminary idea note

This create-only note preserves, rather than edits, `20260920T1210Z_r14_curvature_path_facet_idea_a73e.md`.

The theorem in Attack A is unchanged, but one explanatory **pointwise** decomposition in the preliminary proof was written incorrectly. The correct algebra is

`(tau-a)^2/(1+tau)`

` = (tau-a) - (1+a)(tau-a)/(1+tau)`.

Taking expectation and using `E(tau-a)=0` gives

`E[(tau-a)^2/(1+tau)]`

` = (1+a)[(1+a)E(1/(1+tau))-1]`.

Therefore

`(1+a)E[1/(1+tau)]-1`

` = (1/(1+a))E[(tau-a)^2/(1+tau)]`,

which is exactly the `eta_tau` used in Theorem A1. No theorem statement, inequality direction, specialization, checker result, or numerical scout changes. The final immutable run report uses this corrected proof only.