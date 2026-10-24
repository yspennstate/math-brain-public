Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P04 immutable readback receipt — 2026-09-17T23-04-46Z

Status: **COMPLETE_READBACK_VERIFIED**

The following immutable writes were fetched back from their exact creation commits:

1. Exact checker
   - path: `proofnet24/P04-closure-local-paley/artifacts/2026-09-17T23-04-46Z__frontier_4073_4157_exact.py`
   - creation commit: `700395b14ccd91a3500f64a03c0bec159abe7349`
   - blob SHA: `b37dd1454ee498e8f944aeed756e476ffb12ee40`
   - readback verified the exact-checker header and certificate methodology.

2. Archived checker output
   - path: `proofnet24/P04-closure-local-paley/artifacts/2026-09-17T23-04-46Z__frontier_4073_4157_exact.out`
   - creation commit: `e78e4532f44d301a9dff2e1a7d6e53d870a0b956`
   - blob SHA: `3b059073dd80927403c68a11007e1ed5fb71ec1b`
   - readback verified the p=4157 PASS block and terminal frontier summary, including `FRONTIER_ALL_EXACT_CERTIFIED=PASS`, complete retained domain, `FROZEN_METRIC_AFTER=4157`, and `FINITE_EVIDENCE_ONLY=YES`.

3. Immutable run report
   - path: `proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T23-04-46Z__run-report.md`
   - creation commit: `6251e05cecffec17f155ddd3132b0ef09bef3037`
   - blob SHA: `149fc24279e1123fac155f63c50e312386d9e4b9`
   - readback covered the report in contiguous ranges and recovered the terminal marker `**End of complete run report.**`.

Verified run facts:

```text
frozen_metric: 4057 -> 4157
complete_exact_domain: {149,257,1009,4001,4013,4021,4049,4057,4073,4093,4129,4133,4153,4157}
post_4057_unchanged_streak: 5 -> 0
status: PARTIAL / source OPEN
source_asymptotic_statement_proved: NO
rotation: NO
```

No peer file and no shared RESULTS ledger was edited by P04.

**End of immutable readback receipt.**