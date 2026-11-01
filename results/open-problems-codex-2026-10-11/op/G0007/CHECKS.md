# Verification record — G0007, 2026-10-11

- checks.py completed successfully: 1,442 finite labeled trees, 24 Bernoulli branching-excess cases, 76 Poisson-count density cases. Exact counts/float discrepancies in checks.json.
- surrogate_checks.py completed successfully: near-critical independent site-percolation slopes for d=3,5,7,20 converge to 2d/(d-2); detailed results in surrogate_checks.json. This is a different-model sanity check, not numerical evidence about nu_lambda derivatives.
- The analytic proofs were reviewed for sample-dependent mark insertion, strict time ordering, preservation of outside final states, exclusion of all-constant configurations, continuity of reciprocal cluster size, all possibilities for the number of infinite clusters, and fixed-ball merging. The precise arguments appear in ATTEMPT.md Sections 2--7. No branch independence or uniform finite-energy bound is assumed.

## Lean status

File: ~/brain_workers/TRIO_1011/op/G0007/MarkovObstruction.lean.
Command launched from ~/lean_verify:

    lake env lean ~/brain_workers/TRIO_1011/op/G0007/MarkovObstruction.lean

Only one Lean command was launched. It imports Mathlib.Tactic.FieldSimp and Mathlib.Tactic.Linarith, contains no sorry and no native_decide, and isolates the three-variable algebraic contradiction in ATTEMPT.md Section 8. The shared Lean wrapper reported that it was waiting for a slot. As of this record, no kernel result has returned. This file is NOT described as Lean-checked. The main continuity proof is a written analytic proof and has not been formally verified in Lean. The pending check does not replace any human proof step.

## Path error

The initial Lean setup command used Set-Content with a relative path while its working directory was ~/lean_verify. Consequently it also created ~/lean_verify/MarkovObstruction.lean outside the authorized G0007 folder. This was an execution mistake, acknowledged to the user. All subsequent artifact writes used G0007; no outside file was deleted or moved, in accordance with the user's prohibition. The accidental copy is not an output artifact of this folder and was not altered after the mistake.


## Second-attempt checks, 2026-10-11

- second_symbolic.py: completed; conditional moment and covariance identities simplify exactly.
- second_countermodel_checks.py: completed; 30 rational comparison cases and exact transition, survival, enhancement and susceptibility constants.
- second_fkg_checks.py: completed; finite four-vertex star normalized and all 256 lattice pair comparisons passed. The general downward-FKG claim relies on the posterior-tree proof, not on this finite test.
- second_threshold_bounds.py: completed; exact degree-4 and degree-5 constants, delta<1/100 and positive branching-excess margins verified.
- The original MarkovObstruction.lean process handle is no longer available. No exit-zero result was captured, so it remains NOT kernel-checked.
- One new Lean command was launched from ~/lean_verify: lake env lean ~/brain_workers/TRIO_1011/op/G0007/NoiseComparison.lean. This file only formalizes the two scalar independent-noise inequalities. Minimal Mathlib.Tactic.Linarith import, no sorry or native_decide. Its captured outcome will be appended separately. The analytic infinite-volume proofs are not formalized.
- All second-attempt artifact writes were inside G0007. No brain, repository or external record was modified.

Captured Lean status at 2026-10-11 18:22 UTC: the shared wrapper reported `[leancheck] slot 0 taken after 1516 s; running the check`. No completion or compiler result has yet been captured for NoiseComparison.lean. This file is NOT kernel-checked in the present record. The two elementary real inequalities also have complete written proofs in SECOND_PROOFS.md Section 2.3; their pending formal check does not supply any missing infinite-volume derivative argument.
