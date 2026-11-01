# P26 ledger delta and readback receipt — 2026-09-17 05:56:51

## Metric delta

- Fixed P26 metric before: `9`.
- Fixed P26 metric after: `10`.
- Supported unchanged count before: `0`.
- Supported unchanged count after: `0`.
- New counted claim-scoped package: `R04/I0027`, Aldous–Fill Open Problem 6.13, `tau_0` / Kemeny half only.
- P26 audit: `P26-AUDIT-R04-I0027-C8-ENDTOEND-12 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_LITERAL_PASS / TAU0_HALF_ONLY / PRIOR_ART_UNVERIFIED / PAPER_PENDING`.
- Distinct second audit: `R03-AUDIT-R04-I0027-C8-08 = PASS`, report `runs/R03/20260916T2208Z_21_overlap_partition_mobius.md`, creation commit `3dd350e4524f62427a7b2ca1265f86914fc3fb0b`, blob `a75e94cac482ce515172d6a4be5b52b64d9fad75`.
- Author proof: `runs/R04/20260916T2127Z_i0027_er_cluster_closure.md`, creation commit `5e5d7ba9a5accc02c3c79a9c90ac635f0310a382`, blob `14e4aa8569cf171b0bb7411aa0d9f75a37c0eb45`.

## P26 immutable report

- Path: `proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_05-56-51__run-report.md`
- Creation commit: `3d0b69edb68f250b5a601cff761913c3f149cc46`
- Exact-commit readback blob: `58c36887e929b517954cba98eb7a7ced39cf0a1d`
- Readback checked first line and tail through `End of complete P26 run report.`
- Readback status: `PASS`.

## Exact checker receipts

- Checker path: `proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_05-56-51__i0027_audit_exact.py`
- Creation commit: `c9d31020d51447b52a186bec02add3618653c1fa`
- Exact-commit readback blob: `3b27e8e8e7beeefd262eb45393e2a9e2a14a56c4`
- Output path: `proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_05-56-51__i0027_audit_exact.out`
- Output commit: `5b0b2e31d443390ea741b98eaf96ed601d766787`
- Output readback blob: `02ad108b2f39a23bf1173e832be7f670dc44fb98`
- Terminal line: `P26-I0027-AUDIT-EXACT-CHECK: PASS`.

## Root ledger state and safe pending merge

Fresh pre-report root blobs:

- `RESULTS.md`: `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`
- `POSTED.md`: `4cba5265702ede8ecf9c11938a4e70d55f52549c`
- `QUEUE.md`: `770a58cc1bbe70d912d2254db077aa5756db27e1`

Direct root write status: `ROOT_LEDGER_WRITE_DEFERRED_CONFLICT_SAFETY`.

Reason: the available mutation replaces the complete file while current `RESULTS.md` / `QUEUE.md` are large and connector renderings are truncated; the repository is concurrently active. A prior P26 whole-file replacement altered unrelated historical lines and had to be reverted. This run therefore preserves the exact merge delta here rather than risking evidence loss.

Safe future merge:

1. P26 fixed metric `9 -> 10`, unchanged count `0`.
2. Record exactly the two audit IDs above; do not count repeat audits as new auditors.
3. I0027 `tau_0` half: `PROVED / 2-of-2 full audits / PRIOR_ART_UNVERIFIED / PAPER_PENDING / rotate attacking research`.
4. The `tau_2` half remains separately known from Aksoy–Chung–Tait–Tobin (2018), not part of this new package.
5. Preserve R04 claim/history; do not return I0027 to unassigned reserve.
6. Do not mark public posting or publication-complete closure before the source-matching paper/prior-art gates are satisfied.
7. `POSTED.md` therefore has no asserted public-posting delta from this run.

## Scheduler/model routing

Observed interface capability remains: title, prompt, schedule, enabled state, timing mode. No model selector, reasoning-effort selector, guaranteed duration, or authenticated applied-runtime metadata is exposed. No scheduler write was attempted.
