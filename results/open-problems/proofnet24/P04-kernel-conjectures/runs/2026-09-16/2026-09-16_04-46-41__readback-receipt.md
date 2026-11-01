# ProofNet24 P04 — immutable readback receipt

**Canonical report path:** `proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_04-46-41__run-report.md`  
**Report creation commit:** `60ee7e1c42af6ded59bad4c1b06fe7b59345f7b9`  
**Verified report blob SHA:** `7218a2cfd4acb866b05d02965dc9df7c9c472d8b`  
**Readback ref:** exact creation commit above  
**Branch written:** `master`  
**Status:** `COMPLETE_READBACK_VERIFIED`

The report was read back from GitHub at the exact creation commit in contiguous ranges covering its beginning, four-target/T1--T3 state, complete Target-4 setup and new proofs, peer audit, dependency ledger, failed-route ledger, next attacks, final four-target ledger, and delivery checkpoint. No truncation, historical overwrite, or mathematical transport corruption was found in the committed UTF-8 report. No erratum is required.

The verified report preserves the four original targets and records the new claims:

- `P04-T4-SCORE-FISHER-JORDAN-BLINDNESS-50 = PROVED`;
- `P04-T4-WEIGHTED-JORDAN-WARD-50 = PROVED`;
- `P04-AUDIT-P20-LINEAR-EQUIVARIANT-WARD-UNIQUENESS-50 = PASS`.

Final target state in the verified report:

- T1: `PROVED / candidate complete; formal audit-count closure OPEN`;
- T2: `PROVED / AUDIT-CLOSED`;
- T3: `PROVED / AUDIT-CLOSED`, explicit `c(h)=5/36`;
- T4: `OPEN`, with immediate angular debt `e_2=O(1/d)` and downstream microscopic hard-edge dependencies retained.
