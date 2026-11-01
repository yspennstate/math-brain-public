# Lean verification — 2026-10-12

Command, run from ~/lean_verify:

    lake env lean ~/brain_workers/TRIO_1011/op/F0033/LeastAction.lean

Final run exited 0 with no diagnostics. Shared Lean slot wait: approximately 60 seconds; verification then completed. Toolchain: leanprover/lean4:v4.33.1. Imports: Lean.Elab.Tactic.Omega and Mathlib.Tactic.Ring. Proofs use omega and ring, which construct terms checked by the Lean kernel; no sorry, axiom declarations, or native_decide.

Checked statements:

- first_excess_impossible: the integer contradiction used by the least-action argument.
- wave_continues_iff: a completed wave continues exactly when four neighbours participated.
- quadratic_laplacian: the full-lattice strip quadratic has Laplacian two.

An earlier run failed because Mathlib.Tactic.Omega does not exist as an available compiled module here; using Lean.Elab.Tactic.Omega fixed the import. That failed run is not counted as a checked proof.

These are local algebraic components. The global sandpile reduction and probability arguments have written proofs in ATTEMPT.md and are not claimed fully formalized.

## Second attempt

Command, again from ~/lean_verify:

    lake env lean ~/brain_workers/TRIO_1011/op/F0033/BootstrapStep.lean

Final result: exit code 0, no Lean diagnostics. The shared-slot wait reported approximately 111 seconds before execution. Only Lean.Elab.Tactic.Omega is imported. Checked:

- activation_forces_toppling: the local terminal-height implication underlying bootstrap closure containment in every stabilizing toppling support.
- ladder_column_transfer: the two distinct incoming grains that propagate a ladder column.
- star_barrier_equations and star_outside_bound: the integer-scaled fractional-barrier inequalities.
- ceiling_fails: the exact rounded-barrier overflow.

Closed arithmetic goals use `decide +kernel`; the symbolic inequalities use `omega`. No sorry, native_decide or axiom declarations. This does not formalize the entire infinite ladder, probability law, Dirichlet energy proof, or uniform-radius gap.
