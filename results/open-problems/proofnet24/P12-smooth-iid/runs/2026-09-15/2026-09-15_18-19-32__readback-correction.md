# ProofNet24 P12 — immutable readback correction

**Affected report:** `proofnet24/P12-smooth-iid/runs/2026-09-15/2026-09-15_18-19-32__run-report.md`  
**Affected report commit:** `d437b958c23c21933414b37411da4d240462846a`

GitHub readback exposed two presentation-only serialization/typing defects:

1. In equation (5.4), the intended difference-concentration formula is
   \[
   \mathcal Q_m^{\mathbb C}(\rho)
   \ge
   P\{|\xi_m-\xi_m'|\le\sqrt2\rho\}.
   \]
   The archived report contains one nonbreaking-space character immediately after the opening absolute-value bar.

2. In Section 12 under **Anti-concentration**, the intended notation is
   \[
   \mathcal Q_m^{\mathbb F}(\rho_{\rm source})
   \le
   1/\gamma+o(1).
   \]
   The archived report rendered the subscript token as `\rho_{\nm source}`.

No hypothesis, constant, theorem statement, proof step, peer-audit verdict, ledger status, dependency, or next-attack conclusion is changed. The original report is preserved immutably; this note records the exact intended notation under the readback protocol.
