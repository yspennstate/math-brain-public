# ProofNet24 P04 — immutable readback receipt

**Canonical report:** `proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_06-43-52__run-report.md`  
**Report creation commit:** `85ee6d25427d4b54c5e276e32c64b7fe25f967b6`  
**Verified report blob:** `f63db6fcc9f22eb07a1bc59ed19081d20bb82a07`  
**Branch written:** `master`

The canonical report was read back from the exact creation commit, not merely moving `master`, in complete contiguous ranges `1-300`, `301-600`, `601-900`, and `901-1200`; the final range reached end-of-file.

Readback verified:

- all four original targets and their hypotheses/quantifiers;
- `P04-T4-SECOND-TOP-ONEDELETE-52 = PROVED`;
- `P04-T4-ONEDELETE-IMMEDIATE-GAUSSIANIZATION-NOGO-52 = PROVED`;
- `P04-AUDIT-P20-ONEDELETE-ENDPOINT-52 = PASS`;
- Target 1 remains `PROVED / candidate complete; audit-count closure OPEN`;
- Target 2 remains `PROVED / AUDIT-CLOSED`;
- Target 3 remains `PROVED / AUDIT-CLOSED` with retained explicit constant `5/36`;
- Target 4 remains `OPEN`, with immediate angular obligation `e_2=O(d^-1)` equivalently the signed cumulative one-delete mark bound.

No truncation, historical overwrite, or readback corruption was detected. Status: **COMPLETE_READBACK_VERIFIED**.