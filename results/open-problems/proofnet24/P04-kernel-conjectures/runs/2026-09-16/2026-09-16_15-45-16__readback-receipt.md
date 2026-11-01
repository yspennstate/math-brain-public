# P04 immutable readback receipt — 2026-09-16 15:45:16 +03:00

Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; the scheduler exposes no model selector or reasoning-effort selector.

Report path:
`proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_15-45-16__run-report.md`

Creation commit:
`1b3bb0b666634055677588abfb0023d1dc24857b`

Verified report blob:
`42078016418f4397ef84f730df0a4a6ebcccd8e9`

Readback verification:
- fetched the report at the exact creation commit, not moving `master`;
- checked the opening model/metric line;
- checked the frozen P26/P03 audit ledger and exact remaining obligation;
- checked the final ledger;
- observed the terminal marker `**End of complete run report.**`.

Tracked quantity: required claim-scoped OTHER-audit obligations unresolved = `1 -> 1` (**no movement**).

Audit evidence retained:
- `P04-T1-OUTSIDE-AUDIT-P26`: SATISFIED by `P26-AUDIT-P04-T1-ENDTOEND-17 = PASS`.
- `P04-T1-OUTSIDE-AUDIT-P03`: OPEN; no completed P03 Target-1 / squared-ridge end-to-end audit was found on current `master` in this run.

Status: `COMPLETE_READBACK_VERIFIED`.
