# I0129 immutable report receipt — 2026-09-19T104200Z

- Native ID: `6aa7b4cc3c78819187a22c2c51acf674`
- Target: `I0129`
- Report path: `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-17/rotations/I0129/runs/2026-09-19/2026-09-19T104200Z__report.md`
- Report creation commit: `90a69794551171b2177588b53e774d42f000ac18`
- Exact readback blob at that commit: `5a1d6928155c1a10627099bda898c90669c8d0ad`
- Exact readback ref: `90a69794551171b2177588b53e774d42f000ac18`
- Metric: `rho_SM: 1 -> 1`, NO MOVEMENT
- Methods: `B27/B19/B24`
- Status: `OPEN / PARTIAL`
- Cumulative supported no-movement: `38 -> 39`
- HARD recoveries: `2/2` consumed; no Recovery 3
- Same-sharpened-obligation streak: `1` because the blocker changed materially to a structured low-height cross-row/adelic relation problem
- Verification: `VERIFIED_BY_EXACT_COMMIT_READBACK`

The report itself is immutable and correctly contains `creation_commit: PENDING_SAME_RUN_RECEIPT` because a file cannot self-reference the commit that creates it. This receipt is the post-write immutable record of the actual report creation commit and exact blob.