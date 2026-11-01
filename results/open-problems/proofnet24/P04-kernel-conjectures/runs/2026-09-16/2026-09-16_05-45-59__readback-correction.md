# ProofNet24 P04 — immutable readback correction and verification receipt

**Canonical report:** `proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_05-45-59__run-report.md`  
**Report creation commit:** `c1cb7939d1107b609100d32cd46e352738250015`  
**Verified report blob:** `65b73b0a99fc6ed01c5a3b4b73b320c643136afc`

The complete report was read back from the exact creation commit in contiguous ranges from beginning through end-of-file. The four-target ledger, Target-2 primary-source audit, Target-3 reduction/leverage separation, P20 peer audit, both new Target-4 proofs, tests, failure ledger, obligations, and next attacks are present.

Readback found three LaTeX transport corruptions caused by an escaped form-feed sequence in three local displays. The original immutable report is intentionally not overwritten. The exact corrections are:

1. In equation `(6.4)`, the displayed fragment rendered as `- rac{2s}{d}<a,J>` (with the transport character before `rac`). The intended and mathematically used term is

\[
-\frac{2s}{d}\langle a,J\rangle.
\]

2. In equation `(6.5)`, the displayed fragment rendered as `- rac4d<a,J>` (with the transport character before `rac`). The intended and mathematically used term is

\[
-\frac4d\langle a,J\rangle.
\]

3. In equation `(7.3)`, the displayed final term rendered as `- rac{delta_{ij}}d` (with the transport character before `rac`). The intended and mathematically used term is

\[
-\frac{\delta_{ij}}d.
\]

These are transcription/transport defects only. The immediately following equations `(6.6)`, `(6.8)`, `(7.5)`--`(7.10)`, all theorem statements, the one-delete recurrence `(8.21)`--`(8.25)`, claim statuses, constants, and dependency conclusions already contain the correct formulas and are unchanged.

No other truncation or mathematical readback discrepancy was observed in the complete contiguous readback.

**Verification status:** `COMPLETE_READBACK_VERIFIED_WITH_THREE_LOCAL_TEX_CORRECTIONS`.

No email or Gmail action was used. Target 4 remains OPEN; the continuing program is not disabled.