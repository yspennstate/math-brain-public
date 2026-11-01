# ProofNet24 P04 — immutable readback correction / receipt

**Corrected report path:** `proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_07-46-09__run-report.md`  
**Report creation commit:** `55c3c8e4e245aec6d6f0420ca27dff48e71a95ea`  
**Verified report blob:** `53141d29bc03899d6c7d6fb832d92c69bf0e3c46`

The historical report was read back completely at its exact creation commit in contiguous ranges through end-of-file. Two local LaTeX transport defects were found. The historical file is left immutable; this file is the canonical correction.

1. In Target 1, equation (2.1), the second regularization term was transported with a broken `frac` command. The intended exact objective is

   `L(w) = (1/(2N)) ||y-Xw||^2 + (lambda/2)||w||^2`

   equivalently

   `L(w) = (1/(4n)) sum_{i=1}^n sum_{j=1}^2 (y_i-x_ij^T w)^2 + (lambda/2)||w||^2`, with `N=2n`.

2. In equation (8.11), the left side was transported with a broken `frac` command. The intended inequality is

   `| E delta_R - (E N_R)/nu_d | <= (16/nu_d) E s^2 <= 1296 k^2/c_d^4`.

No other truncation or transport defect was observed in the complete readback. These are rendering-only corrections. They do not alter any theorem, bound, status, proof dependency, audit verdict, or next obligation in the report.

**Readback status:** `COMPLETE_REPORT_READBACK_WITH_TWO_RENDERING_CORRECTIONS`.
