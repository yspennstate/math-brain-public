# Hadamard rounding independent audit

Classical FEI remains OPEN. Read [AUDIT.md](AUDIT.md) for the analytic proof review, precise hypotheses, scope, and historical export defects.

Run `python independent_check.py` from this directory. It performs 110 finite coefficient-vector cross-checks and verifies every interval in the final Hadamard output under both binary64 and exact-decimal interpretations. The finite checks supplement the analytic review; they are not a formal certificate or novelty claim.

- `source/`: immutable original checker and output from c4d07e6
- `final/`: immutable repaired checker and output from 67c4459
- `independent_results.json`: independently generated results and exact rational defect witnesses
- `source_manifest.json`: source revisions and SHA-256 hashes

All author files are preserved unchanged. The original output defect is recorded historically; the final repair has been independently verified.
