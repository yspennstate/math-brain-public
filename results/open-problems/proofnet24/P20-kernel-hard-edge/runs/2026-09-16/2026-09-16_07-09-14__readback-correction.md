# ProofNet24 P20 — immutable readback correction

**Canonical report:** `proofnet24/P20-kernel-hard-edge/runs/2026-09-16/2026-09-16_07-09-14__run-report.md`  
**Report creation commit:** `03d335367902c90cfb141bb1d0bd4ae35b31c588`  
**Verified report blob:** `551c9c94ffdd2884ef5214f5a25208fca32ea20e`  
**Branch:** `master`

The canonical report was read back from the exact creation commit in complete contiguous ranges `1-300`, `301-600`, `601-900`, and `901-1500`; the last range reached end-of-file.

Readback verified the complete target statement, exact trace/traceless decomposition with shared radial dependence, P04 audit, new projection-stability theorem, submacroscopic one-delete persistence theorem, top-window cumulative theorem, primary-source correlated-entry no-go certificate, failed-route ledger, remaining obligations, and next attack.

One notation-only transport defect was found in equation (5.11): the intended expression

\[
E Q_k=\frac{k}{m-k+1}=\frac{k}{r+1}
\]

was serialized in the immutable report with the second `\frac` missing its leading `f` (`rac{k}{r+1}`). The equation immediately before and the subsequent equation (5.12) make the intended identity unambiguous. The correct equation is exactly the display above.

This correction changes no proof step, theorem statement, constant, asymptotic, audit verdict, dependency status, or next attack. The canonical report remains immutable and is not overwritten.

Verified new claim IDs in the canonical report:

- `P20-AUDIT-P04-SECOND-TOP-ONEDELETE-59 = PROVED / PASS`;
- `P20-QUADRATIC-ORBIT-PROJECTION-STABILITY-59 = PROVED`;
- `P20-SUBMACRO-ONEDELETE-PERSISTENCE-59 = PROVED`;
- `P20-TOP-WINDOW-CUMULATIVE-NEGLIGIBLE-59 = PROVED`;
- `P20-CHE-LOPATTO-MIXING-NOGO-59 = PROVED / route rejected`.

Target 4 remains **OPEN**. No different microscopic scale or limiting law is claimed. No email/Gmail action was used.

Status: **COMPLETE_READBACK_VERIFIED_WITH_NOTATION_CORRECTION**.
