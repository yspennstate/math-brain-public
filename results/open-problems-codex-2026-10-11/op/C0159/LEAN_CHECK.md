# Lean check — 2026-10-11

Command, run from ~/lean_verify:

    lake env lean ~/brain_workers/TRIO_1011/op/C0159/WeightedContact.lean

Result: exit code 0, no Lean diagnostics. The shared checker reported waiting for a slot, acquired slot 0 after 510 seconds, and completed the check. Only one Lean command was running for this attempt. It was polled without terminating or modifying any other process.

Checked declarations:

* contact_cardinality_bound: if each weight on a finite set is at least epsilon and its sum is at most M, then card times epsilon is at most M.
* separator_probability_positive: if p<1 then (1-p)^k>0.

There are two specific Mathlib imports, no `sorry`, no `native_decide`, and no full `import Mathlib`. These are ordinary kernel-checked proofs by library lemmas; no decision-procedure axiom is used. This check does not formalize the infinite sprinkling argument, the reliability recursion, or the grandparent-graph theorem, whose complete written proofs are in ATTEMPT.md.

## Second attempt — completed 2026-10-12 Jerusalem / 2026-10-11 21:18 UTC

Command, run from ~/lean_verify:

    lake env lean ~/brain_workers/TRIO_1011/op/C0159/NeumannFinite.lean

Result: exit code 0, no Lean diagnostics. The shared checker acquired slot 0 after 2467 seconds of waiting; the check then completed within the requested hour-long allowance. One Lean invocation ran at a time, and no other process was terminated or modified.

Checked declarations:

* finite_neumann_remainder: the finite identity (1-z) sum_{i<n} z^i = 1-z^n in an arbitrary ring, including a noncommutative one.
* finite_neumann_bound: for real 0<=z<1, sum_{i<n} z^i <= 1/(1-z).

Both use two narrow Mathlib imports and ordinary kernel-checked library proofs, with no `sorry`, `native_decide`, or full Mathlib import. These declarations support the finite algebra of SECOND_ATTEMPT.md Theorem A.1. They do not formalize BK, weighted Schur, the infinite operator limit, the contact-count bound, or the bubble-diagram criterion. Those remain complete written proofs with independent finite checks, not Lean-verified probability theorems.
