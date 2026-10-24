# Verification report — 2026-10-12

Final research verdict: PARTIAL. The shared Lean compiler outcome is unrecovered: the log records only a slot wait, the result marker remained RUNNING past its nominal hour, and no matching live runner/checker process was found. No Lean-checked claim is made. Ordinary proofs survived the author rereading.

The old tool session 82004 was unavailable on continuation. A read-only
process query found no matching live old check. Its outcome remains
unrecovered; it is not credited as a successful or failed compilation.

The fresh run used run_lean_check.py and the ordinary serialized lake shim:

    lake env lean ~/brain_workers/TRIO_1011/op/E0062/Prefix.lean

Working directory: ~/lean_verify. Timeout: 3600 seconds.
Recorded runner state: UNRECOVERED; exit code: None.
Source SHA256: 1501c43d279e8613945cfb46a43a9ead5a7772610efd33c1b4ac96a9cc58e954.
Exact run timestamps and command: lean_check_result.json.
Preserved compiler/queue output: lean_check.log.
For UNRECOVERED, the original stale RUNNING marker is preserved verbatim
in lean_check_result.before_assessment.json. UNRECOVERED is an author
assessment of the unavailable result, not a compiler success, compiler
error, or confirmed timeout. The exact compiler exit code is unknown.

Formalization scope: prefix and pair cancellation algebra, cross-term
nonnegativity, product expansions and the kappa bound, balanced product
identities, the symmetric finite-rate independent-support implication,
and weighted payoff/rate identities. Standard ring, positivity, norm_num,
linarith and order reasoning only; no sorry or native_decide. Selective
Mathlib imports only. The probability-measure and convergence arguments
are written ordinary proofs, not Lean certificates.

Completed exact rational checks: 2,187 prefix/cut checks, 23,166 strict
product-bound checks and 858 equality-case checks. These existing runs
are preserved in experiments_output.txt, exact_checks.json and
equality_checks.json. No unrelated tests were repeated.

The author's continuation rereading is REFEREE.md. The final mathematical
results and remaining gap are summarized in RESULTS.md. All claims are
recorded in CLAIMS.jsonl. The general magnitude-dependent criterion for
arbitrary matrices with zeros remains unproved.
