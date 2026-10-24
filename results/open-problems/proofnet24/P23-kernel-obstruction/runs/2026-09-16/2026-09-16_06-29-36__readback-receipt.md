# ProofNet24 P23 — immutable readback receipt

**Canonical report:** `proofnet24/P23-kernel-obstruction/runs/2026-09-16/2026-09-16_06-29-36__run-report.md`  
**Report creation commit:** `a2db9ccf3761cb8922e317a442f41a45db9264d4`  
**Verified report blob:** `91875c3aa4ed975385600fc44871ec2f5f527137`

The canonical report was read back from the exact creation commit, not merely from moving `master`, in contiguous ranges covering the complete file:

- lines 1--220;
- lines 221--499;
- lines 500--940;
- lines 941--1400; and
- lines 1401 through end-of-file.

The readback confirms the original Target-3 expectation theorem and explicit `c(h)=5/36`; the finite-window reduction/leverage separation; the exact Mercer ratio source check; `P23-T4-SIGNED-ONEDELETE-OD-WINDOW-40`; `P23-T4-AFFINE-LINEAR-MIXED-PARTITION-BLINDNESS-40`; peer audit `P23-AUDIT-P20-ONEDELETE-MARK-GAMMA-40 = PASS`; exact low-dimensional checks; failure ledger; cumulative status ledger; and next attack.

No truncation, missing section, or mathematical serialization discrepancy was observed. The report is immutable and was not overwritten.

**Verification status:** `COMPLETE_REPORT_READBACK_VERIFIED`.

No email or Gmail action was used. Target 4 remains OPEN; the continuing program is not disabled.