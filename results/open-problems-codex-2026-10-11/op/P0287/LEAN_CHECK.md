# Lean verification — 2026-10-12

Command: `lake env lean ~/brain_workers/TRIO_1011/op/P0287/ProductChecks.lean`

Working directory: `~/lean_verify`.

Result: exit code 0; no diagnostic output. One Lean job was run. The execution API has no command-timeout argument; the job was polled and completed within the requested one-hour ceiling. No extra job was started while it ran.

Checked: covariance polynomial identity, density equation, strict positivity constraint on kappa, telescoping boundary sum, and Boolean no-10 implication. Imports are specific Mathlib modules; no `import Mathlib`, no `sorry`, no `native_decide`. The finite Boolean step uses `decide +kernel`.

This checks algebraic components, not the infinite-process proof.

## Second attempt

Command: `lake env lean ~/brain_workers/TRIO_1011/op/P0287/CouplingChecks.lean`, from the same verification directory.

The shared wrapper waited 105 seconds for a Lean slot, then ran the check. Result: exit code 0; no Lean diagnostics. One job was run and completed within the one-hour ceiling.

Checked: ordered common-clock update, local total-discrepancy conservation, signed left-cut balance, lower and upper transmitted-current inequalities, and the occupied-run current inequality. All finite Boolean steps use `decide +kernel`; all other steps use ordinary kernel-checked tactics. No `sorry`, `native_decide`, or umbrella Mathlib import. The stochastic-order limit and infinite discrepancy process remain ordinary mathematical proofs, not Lean formalizations.
