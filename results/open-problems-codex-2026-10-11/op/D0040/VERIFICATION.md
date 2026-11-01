# Verification — 2026-10-12

## Exact mathematical checks

ATTEMPT.md contains full proofs of the Laguerre construction, the common-measure formulation, the canonical quartic obstruction and its tail asymptotic. A hostile-referee checklist states the scope and possible failure points.

The finite-size distribution input is Dumitriu–Edelman Theorem 3.4, downloaded and inspected on PDF p. 14. The source Question 2 and surrounding Theorem 4.1 were inspected on PDF pp. 5–6.

## Numerical checks

Command: `python -X utf8 check_laguerre.py` from this folder.
Finished successfully. Detailed results: numerical_checks.json. Four runs of 10,000 matrices of size 5; memory use consists of small chi arrays and a single small matrix per iteration, far below 1 GB. These verify transformation identities and basic moments, not the full joint eigenvalue density.

Maximum spectral transformation discrepancy: 2.85e−14.
Leading-block equalities: all assertions passed.
Trace z-scores: 1.952, −0.034, 0.981, 1.155.
The smallest interlacing gap rounded to −7.11e−15 in a boundary case; exact strict interlacing is proved independently.

## Lean

Command issued once from ~/lean_verify:

    lake env lean ~/brain_workers/TRIO_1011/op/D0040/LaguerreCheck.lean

The shared leancheck wrapper reported: `[leancheck] slot 0 taken after 1698 s; running the check`.
Imports: Mathlib.Data.Real.Basic and Mathlib.Tactic.Ring only.
The file contains two ring proofs, no sorry and no native_decide. The probability and operator arguments are not formalized.
Completion status will be appended when the command returns; nothing is called Lean-checked before successful completion.

At finalization the command has not returned a compiler result despite repeated polling after slot acquisition. Its active tool session is 52930. Accordingly both Lean declarations remain **unconfirmed**, and no claim in this record relies on successful Lean verification. No process was terminated. The algebraic identities also have direct expansions in ATTEMPT.md; the probability proofs remain ordinary mathematical proofs with the listed standard theorem inputs.

## Renewed attempt checks

The previous session 52930 is no longer available. Its outcome remains unknown. The two identities have been included in the new single check, alongside the unit-vector Cauchy–Schwarz step and complementary Gram diagonal used for the Jacobi construction.

Command run by verify_second_lean.py, from ~/lean_verify:

    lake env lean ~/brain_workers/TRIO_1011/op/D0040/JacobiCheck.lean

The runner applies a 3600-second timeout and captures the result in second_lean_result.json and second_lean.log. The wrapper reported slot acquisition after 213 seconds. Pending compiler success is not treated as verification. Only one new Lean job was launched after checking that no D0040 Lean process from the previous attempt was present.

The main new probability proof is ordinary mathematics in SECOND_ATTEMPT.md, using the verified finite Edelman–Sutton theorem, not Lean. The finite CS block orientation check completed at six sizes with 6000 samples and all assertions passing. The 60000 Jacobi stress samples and 10000+10000 independent model/Wishart comparison samples completed; their full outputs and statistical qualifications are in SECOND_ATTEMPT.md and the two new JSON reports. These checks do not prove the density or the classification.
