# Check receipts — 2026-10-11

Final local Lean outcome: the lighter ordered-field attempt also ended with the 900 MiB interpreter memory exception, exit 3221226505, after 102.16 seconds. Complete final receipt: lean_check.log. No local Lean declaration is counted as checked. No further Lean jobs were launched. Hand proofs and public external proof reports are separate from these failed local checks.

The explicit-real corrected run ended with a Lean interpreter memory exception at the 900 MiB limit (exit 3221226505); receipt retained as lean_check_memory_failure.log. A final sequential lighter attempt states the same inequalities over an arbitrary field with linear order and strict ordered-ring structure. This includes real numbers mathematically while avoiding the concrete Real implementation import. Again, only a complete exit-0 receipt without sorry-dependent axioms can count as checked.

Continuation correction: the recovered local rerun completed with exit 1 because the tactic-only imports did not define the real-number type. Lean implicitly treated the undeclared `ℝ` identifier as a type variable, causing arithmetic-instance errors. Its complete receipt is preserved as `lean_check_missing_real_import.log`; its printed no-axiom lines are not passing proofs. The source was corrected by importing `Mathlib.Data.Real.Basic`, and the covariance step now uses an explicit ring identity. One sequential corrected check was then launched; only its final exit-0 receipt, if obtained, can be counted as checked.

The exhaustive Python geometry check passed on 10,096 rooted connected sets (dimension 2, sizes 1–7; dimension 3, sizes 1–5), plus 21 explicit solid, hollow, punctured and thin shapes in dimensions 2–4. It checked exterior-boundary star connectivity, cut-edge square connectivity, the integer surface inequality, and the positive-axis anchor. Results: `geometry_checks.json`. These finite checks support, but do not replace, the written proofs.

Resource caveat: the job's recorded elapsed wall time was 1816.03 seconds on this shared machine, longer than the requested small-job duration. No further numerical jobs were launched. It used small finite sets and enumeration, not a large percolation simulation. Peak memory was not instrumented, so no measured memory receipt is claimed.

The first local Lean invocation failed before proof checking because the PowerShell-generated source had a UTF-8 byte-order mark. Its log is retained as `lean_check_initial.log`. The BOM was removed and a second invocation started, using the requested shared Lean workspace, a one-hour subprocess timeout, and only the tactic imports needed for the finite algebra. The second result must be read from `lean_check.log`; an absent log is not a passing check.

Public external-proof evidence: GitHub API metadata reports both CI and comparator success at commit `cd090736b8f5984d49926e80363910e7c6441a4f`, dated 2026-10-09:

- CI: https://github.com/nitromannitol/percolation-after-anthropic/actions/runs/37879691991
- Comparator: https://github.com/nitromannitol/percolation-after-anthropic/actions/runs/37879691984

The recursive source-tree response identifies the same revision. The final site theorem has only dimension and `3 ≤ d` as displayed mathematical hypotheses. Its comparator vocabulary matches independent site percolation on the nearest-neighbour lattice. The challenge's intentional `sorry` is distinct from its solution importing the final theorem. The authors report a strict rebuild and only standard axioms; API success and authors' statements are external evidence, not an independent local replay of that proof chain. This audit has not certified the approximately 100,800-line external development.

The exact G0001 tail theorem was not found as a numbered theorem in the downloaded 28-page companion manuscript. The critical-site theorem remains a resolution lead under the user's precise SOLVED_IN_LITERATURE criterion. Accepting it would resolve G0001 by the fully written reduction; this conditional consequence is not itself an independently verified critical-extinction theorem.

Continuation: the old Lean session could not be recovered and no completed log was saved; a read-only check found no Lean process for this folder. A single new check was started by run_lean_checked.py, with an incremental log, one-hour timeout and 900 MiB compiler memory limit. Its checked declarations and exit status must be taken from the completed lean_check.log, not inferred from the source or a launch message. The full external critical-site development is separate from this small algebra file.

The continuation also verified pinned Git blob hashes, reconstructed all 13 Git directory-tree hashes, and checked exact equality of the comparator's statement vocabulary. Public artifact access returned HTTP 401 without credentials. CERTIFICATE_AUDIT.md states the scope and remaining kernel-replay gap. The new deterministic boundary obstruction has a complete hand proof in BOUNDARY_OBSTRUCTION.md; it is not represented as a numerical percolation experiment.


Final continuation receipt (2026-10-11): The local algebra check did not produce a successful receipt; no Lean-checked claim is made. See lean_check.log. The written hand proofs stand separately. Source SHA256: ec187a2ef6ada4c049b7a495e5572b412226086220515afe65c28bc6aa4fddf2.
Final verdict: PARTIAL. The complete full-scope consequence remains conditional on the public critical-site theorem. Its pinned statement and public verification reports were audited, but its full dependency closure was not independently kernel replayed. A successful replay would supply the missing endpoint; no exact numbered finite-tail theorem satisfying the requested literature criterion was found.
