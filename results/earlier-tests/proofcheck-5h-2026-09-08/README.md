# Proof checker readiness lane, 8 September 2026

This folder holds the Lean checker candidate from a five-hour readiness push on 8 September 2026. It sits beside the twenty-hour audit of 7 September, which found that the checker passed a file containing `sorry` and a false axiom. This lane took the next step: it separates "the file compiled" from "a named theorem was proved".

## What the old checker got wrong

Three cases in `BASELINE_lean_check.py` returned PASS when they should not have:

1. The source file was missing after compilation, and the checker read it as empty text.
2. The file contained only definitions and no theorem.
3. `--file` ignored `--target`, so the checker never looked for the proposition it was asked about.

## The candidate

`lean_check.py` and `proof_receipt.py` issue a certificate only when all of the following hold:

- The named target exists and is of theorem kind.
- A transitive axiom receipt matches it.
- An explicit source-review assertion is bound to the exact bytes that were compiled.

Missing, changed or ambiguous evidence fails closed. A failed tactic is never read as evidence that the statement is false.

Translation fidelity is a separate obligation, and this lane leaves it open. Fidelity means the Lean statement says what the informal one says.

`lean_process.py` owns the compiler process on Windows.

`admission_followup.py` validates the compute-governor state before a launch:

- It rejects NaN values, which the JSON parser accepts.
- It rejects unknown status and mode strings.
- It rejects stale or incomplete timestamps.

## What was measured

- All 34 mocked unit tests pass (`python -B -m unittest -v test_proof_receipt test_lean_check`), with no real compiler process started. `VALIDATION.json` records the run and the sha256 of every source file. In this copy the `guard` helper in `test_lean_check.py` checks only that fixtures stay inside `mock_controls`, so that file's hash differs from the recorded one; the 34 tests pass on it.
- Real Lean integration, process-ownership tests and translation fidelity were not measured in this lane and are marked UNVERIFIED.
- The candidate was staged, not deployed.

## Threat boundary

Lean source is executable metaprogram code, so compiler output cannot be authenticated against a malicious file. A source-review hash records a reviewer's assertion; it is neither a sandbox nor an automatic review. A compromised toolchain and dishonest review are outside what this checker guarantees.

## Left out

The lane's working notes, its proof-gate prompts and the mock control directories are not included. Local paths are replaced by `<HOME>`.
