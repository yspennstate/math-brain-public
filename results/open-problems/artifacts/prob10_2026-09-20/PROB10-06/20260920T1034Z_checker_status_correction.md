# PROB10-06 checker-status correction

The files

- `20260920T1022Z_quantitative_lower_branch_ratio_check.py`
- `20260920T1022Z_quantitative_lower_branch_ratio_check.out`

are preserved as a draft exact-rational checker and draft transcript. They are **not counted as an executed certificate in this run**: a local re-execution of the Python `fractions.Fraction` adaptive checker exceeded the available tool execution window before completion. The transcript is therefore retained only as a non-authoritative development artifact, not as evidence.

The authoritative finite check for this run is the separately archived, actually compiled and executed C++ checker

- `20260920T1034Z_quantitative_lower_branch_ratio_rigorous_check.cpp`
- `20260920T1034Z_quantitative_lower_branch_ratio_rigorous_check.out`.

That checker uses `boost::numeric::interval<double>` with directed/outward rounding, is compiled with `-frounding-math -ffp-contract=off`, adaptively covers every point of each stated rectangle, and exits successfully with `ALL_RIGOROUS_INTERVAL_CHECKS_PASS`. The mathematical inequalities being checked are rational expressions whose denominators are proved positive in the report; the interval calculation is a rigorous enclosure, not a simulation or sampled-grid test.

No theorem in the run report relies on the unexecuted draft transcript.