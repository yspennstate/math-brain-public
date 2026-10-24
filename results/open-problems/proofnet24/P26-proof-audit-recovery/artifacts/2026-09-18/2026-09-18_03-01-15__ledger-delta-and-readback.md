# P26 ledger delta and immutable readback — 2026-09-18 03:01:15

Model actually running in the associated report: GPT-5.6 Sol. Reasoning level: UNVERIFIED. GPT-6/maximum was requested but not runtime-attested.

## Count delta

- Fixed metric: outside packages with two genuinely independent OTHER-track full-proof audits complete.
- Before: `27`.
- After: `28`.
- Supported unchanged count before: `1`.
- Supported unchanged count after: `0`.
- Newly reconciled package: P13 / I0051 / Aldous--Janson Open Problem 9 preserved clade-count package.
- Owner: P13.
- Activity: `RETIRED / PRESERVED`; active P13 successor is unchanged and this audit does not reactivate I0051.
- Mathematical status: frozen claim package PROVED; source-v3 match PASS at claim scope; campaign/publication closure NOT DECLARED.

## Distinct full-proof audits

1. `P26-AUDIT-P13-I0051-OP9-ENDTOEND-33 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_V3_SCOPE_PASS / RETIRED_PRESERVED_PACKAGE / FINITE_CORE_INDEPENDENT_PASS / PRIOR_ART_UNVERIFIED`.
2. `P12-AUDIT-P13-I0051-ENDTOEND-FULL-64 = PASS / COMPLETE OTHER-TRACK FULL-PACKAGE AUDIT`.

Reconciliation: `P26-RECONCILE-P13-I0051-2OF2-33 = PASS`.

These are two distinct audit authors/tracks, P26 and P12, both external to owner P13. Owner self-checks and repeated component audits are not counted as separate auditors.

## P26 report immutable readback

Path:
`proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_03-01-15__run-report.md`

Creation commit: `70b43b2bb9af718d193f01fc37ba9d483a148a57`.
Exact blob at that commit: `23dfa61579fb7815066f123842c7f586f269321c`.

Exact-commit first-line readback confirms:
`P26 fixed metric: 27 -> 28; supported unchanged count: 1 -> 0. NEW-METHODS used: #2, #11, #22.`

Exact-commit tail readback reaches the literal:
`End of complete P26 run report.`

## Independent finite core

Checker:
`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-18/2026-09-18_03-01-15__p13_i0051_independent_exact_audit.py`

Creation commit: `7e9b4a71b2b90384532d5ae682be94d37b77c939`.
Exact blob: `9a4bbe384c7b941ab52848cc8c1cf8a9c15b16c1`.

Archived output:
`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-18/2026-09-18_03-01-15__p13_i0051_independent_exact_audit.out`

Creation commit: `72859de08f89377fa9275fdbde61cf0680ba0974`.
Exact blob: `7a750f2d0cfa59929901f50638d9e36f69ba1d4c`.

Output begins `P26-P13-I0051-INDEPENDENT-EXACT-AUDIT: PASS` and ends `END P26-P13-I0051-INDEPENDENT-EXACT-AUDIT`.

## Second-audit immutable evidence

P12 full audit report:
`proofnet24/P12-smooth-iid/runs/2026-09-17/2026-09-17T02-18-44Z__run-report.md`

Creation commit: `72d2d7e9c8e33e0b7e0a02ee1718536a1f880dd0`.
Exact report blob: `21ed2256708297604cb85ea3e7e0129ceb156f7a`.

Its explicit verdict is `P12-AUDIT-P13-I0051-ENDTOEND-FULL-64 = PASS / COMPLETE OTHER-TRACK FULL-PACKAGE AUDIT`.

## Shared-root source blobs and safe merge delta

Fresh source blobs observed before the P26 report write:

- `RESULTS.md`: `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`.
- `POSTED.md`: `4cba5265702ede8ecf9c11938a4e70d55f52549c`.
- `QUEUE.md`: `2bb9fd1ac6ae45440cbddf25943e1afec6754693`.

Exact safe `RESULTS.md` merge input:

```text
P26 SUPPORT | target: outside narrow packages with two genuinely independent OTHER-track full-proof audits complete | fixed metric 27 -> 28 | supported unchanged 1 -> 0 | new counted package P13/I0051 Open Problem 9 preserved clade-count theorem | owner P13 | activity RETIRED/PRESERVED; active P13 successor unchanged | math PROVED at frozen claim scope; source-v3 match PASS; campaign/publication closure NOT DECLARED | P26 audit P26-AUDIT-P13-I0051-OP9-ENDTOEND-33 PASS | second distinct audit P12-AUDIT-P13-I0051-ENDTOEND-FULL-64 PASS | reconciliation P26-RECONCILE-P13-I0051-2OF2-33 PASS | report proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_03-01-15__run-report.md @ 70b43b2bb9af718d193f01fc37ba9d483a148a57 blob 23dfa61579fb7815066f123842c7f586f269321c | prior-art priority UNVERIFIED
```

`POSTED.md` delta: NONE. Audit completion is not public posting or novelty clearance.

`QUEUE.md` ownership delta: NONE. I0051 remains retired/preserved; active P13 successor remains unchanged.

The large shared roots were not replaced wholesale because the connector's write operation is complete-file replacement while bounded renders do not safely support reconstructing all unrelated concurrent history. This sidecar is the immutable conflict-safe merge input.

## Reserve and model-routing state

The queue still has 60 listed sourced candidates but does not certify 60 fully source/status/literature/history/ownership-checked genuinely unassigned READY candidates. Strong reserve requirement: `NOT CERTIFIED`.

Task controls exposed to this worker remain title, prompt, schedule/start timing, enabled state, and timing mode. There is no binding model-family selector, reasoning-effort selector, guaranteed duration, or authenticated applied-run telemetry. GPT-6/maximum therefore remains prompt-only. A task returning `You cannot modify this task` requires an owning/authorized context, ownership/admin repair, or platform support; no permission bypass or cloning is valid.

END SIDECAR
