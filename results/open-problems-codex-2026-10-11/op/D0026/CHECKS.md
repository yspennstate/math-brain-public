# Verification record

Date: 2026-10-11.

* finite_experiments.py: exit code 0. Exhaustive nonempty-state connectivity
  for intervals of sizes 2 through 9; exact rational detailed balance for
  sizes 2 through 7 at q=1/10,1/3,1/2,9/10. See finite_results.json.
* dual_checks.py: exit code 0, reported computation time 0.369 seconds.
  For cycles of sizes 3,4,5 and q=1/4,1/3,1/2,3/4, every one of the
  64,256,1024 respective configuration pairs satisfies the generator
  duality identity, checked with fractions.Fraction. See dual_results.json.
* FiniteChecks.lean: submitted singly using
  `lake env lean ~/brain_workers/TRIO_1011/op/D0026/FiniteChecks.lean`
  from ~/lean_verify. The shared Lean wrapper reported a
  229-second slot wait, then started compilation. Compilation completed
  successfully with exit code 0 and no diagnostics.
  The file imports only Mathlib.Data.Finset.Basic, uses decide +kernel,
  and contains no sorry or native_decide. The two finite/combinatorial
  theorems are Lean-checked; none of the infinite-volume convergence
  claims is claimed to have been formalized.

The finite Python jobs use tiny state spaces; their data are well below
the 1 GB per-job limit. No stochastic simulation was used as proof.

## Additional attempt

* fresh_checks.py: exit code 0; elapsed computation 129.796 seconds on
  the shared machine. Twenty-five cases (cycle sizes 3 through 7;
  q=0.03,0.1,0.3,0.5,0.8) checked reversible symmetrization, the finite
  FA/dual spectral-gap comparison, the three Dirichlet form inequalities,
  and the heat-kernel bound WITH its finite-volume constant-mode correction.
  Floating-point PSD/gap tests used tolerance 1e-10; these are numerical
  checks only. See fresh_results.json.
* The same script checked 2580 binomial generating-function bounds in
  exact fractions.Fraction arithmetic, for lengths through 40 and three
  positive rational weights. The complete inequality proof is in
  FRESH_ATTEMPT.md, Fresh Lemma 3.
* HeatKernelChecks.lean: one compilation submitted through lake env lean
  from ~/lean_verify. It certifies only the three-component
  energy comparison algebra and the exponential-rate algebra. It imports
  Mathlib.Tactic.Linarith and Mathlib.Tactic.Ring, not all of Mathlib;
  no sorry or native_decide. The submission waited in the shared queue.
  On resumption its tool session was unavailable; a read-only process
  check found no process matching the target, and the shared wrapper log
  contained no start/end entry for this target. No successful compilation
  was observed. This additional file is NOT called Lean-checked.
  The previously completed FiniteChecks.lean certificate remains checked.
  The written algebra proof does not depend on this optional certificate:
  the two comparison differences are c and a+b, respectively, both
  nonnegative; the exponent identity follows by distributivity in R.
* similarity_checks.py: exit code 0; reported computation 0.542 seconds.
  Exact rational Schur-complement rank and intertwining checks passed for
  cycles of sizes 3,4,5 at q=1/3 and 2/3. See similarity_results.json.
  The all-size argument is proved separately in Fresh Lemma 4.
