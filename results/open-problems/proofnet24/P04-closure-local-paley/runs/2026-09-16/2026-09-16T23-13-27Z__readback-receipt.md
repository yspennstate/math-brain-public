# P04 / I0101 exact-commit readback receipt

Status: **COMPLETE_READBACK_VERIFIED**.

Canonical report:
`proofnet24/P04-closure-local-paley/runs/2026-09-16/2026-09-16T23-13-27Z__run-report.md`

Creation commit: `7740ff6439628a79a4626950d72f66113ec4c598`  
Verified report blob: `50dd769a010303338a8e110ba818c75109949b47`

The report was read back from that exact creation commit, not from moving `master`, in contiguous ranges 1--250, 251--500, and 501--end. The final range contains the terminal marker `**End of complete run report.**`; no truncation or theorem-changing transport defect was found.

Exact self-check artifact:
`proofnet24/P04-closure-local-paley/artifacts/2026-09-16T23-13-27Z__trace_kernel_selfcheck.py`

Creation commit: `d015e474c126903441864cadb985b82ac15b4636`  
Verified blob: `ebb737225251eb21a639003de3e91a2a0b112275`

Archived executed output:
`proofnet24/P04-closure-local-paley/artifacts/2026-09-16T23-13-27Z__trace_kernel_selfcheck.out`

Creation commit: `7d83635c0ed84c7693e21eb446d31bb730852567`  
Verified blob: `84da41262875edf3cb7b43323a6bd5fe3501591c`

Both artifacts were read back at their exact creation commits. The archived output records `P04-I0101-TRACE-KERNEL-SELFCHECK=PASS` and `SELF_CHECK_ONLY=true`.

No historical file was overwritten. No root shared ledger was edited by P04.
