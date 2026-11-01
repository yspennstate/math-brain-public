# ProofNet24 P02 — immutable readback correction

Canonical report:
`proofnet24/P02-closure-occupation/runs/2026-09-16/2026-09-16_15-04-01__run-report.md`

Creation commit: `24b01e1277c5f0f821bdeed189f4ff265fedcecd`  
Verified report blob: `6b2500a66b4069505048648e504b5ea68835e12c`

The full exact-commit readback found one harmless LaTeX notation typo in the proof of `P02-OCC-C1-PORTMANTEAU-BORDERED-GREEN`. Preserve the immutable report and read these occurrences authoritatively as follows:

- the displayed text `\nu=Z^T\xi` means `u=Z^T\xi`;
- the subsequent displayed occurrences `\nu_b` mean `u_b`.

All following prose already uses `u`, and equations (4.8) onward make the intended symbol unambiguous. No mathematical statement, sign, matrix entry, determinant, proof step, metric, or ledger status changes.

Readback coverage: report lines 1–250, 251–500, and 501–end were fetched at the creation commit, each returning blob `6b2500a66b4069505048648e504b5ea68835e12c`, including the terminal status marker.
