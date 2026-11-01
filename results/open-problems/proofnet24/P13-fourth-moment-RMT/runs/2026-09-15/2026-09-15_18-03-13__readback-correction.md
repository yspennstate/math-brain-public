# ProofNet24 P13 — immutable readback correction

**Affected report:** `proofnet24/P13-fourth-moment-RMT/runs/2026-09-15/2026-09-15_18-03-13__run-report.md`  
**Affected report commit:** `8cf8eba0220b38e4dc624bfb8d2263c3b39562fe`

The GitHub readback exposed one serialization defect in Section 2. The intended definition is

\[
H_j=\operatorname{span}\{C_\ell:\ell\neq j\}.
\]

The archived run report rendered the `\neq` token with an unintended line break between `\` and `e j`. No hypothesis, constant, theorem statement, proof step, audit verdict, ledger status, dependency, or next-attack conclusion is changed.

The original report is preserved immutably; this note is the correction record required by the readback protocol.
