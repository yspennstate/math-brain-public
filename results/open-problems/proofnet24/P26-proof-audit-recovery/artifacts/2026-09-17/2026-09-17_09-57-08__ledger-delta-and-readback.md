# P26 ledger delta and immutable readback — 2026-09-17

Target: P04 / I0101 / `P04-I0101-P4021-S3-ORBIT-DUAL`.

Fixed P26 metric: number of outside claim-scoped packages with two genuinely independent full-proof audits by distinct tracks.

- before: 13
- after: 14
- supported unchanged count: 0 -> 0
- mathematical status of exact finite package: PROVED
- parent source status: OPEN / PARTIAL
- activity/ownership: I0101 remains P04-owned; former personal kernel work remains retired
- prior art / publication novelty: UNVERIFIED
- public posting: not asserted

Distinct audit IDs:

1. `P26-AUDIT-P04-I0101-P4021-S3-ORBIT-DUAL-16 = PASS_FULL_FINITE_PROOF / CLAIM_SCOPED / SOURCE_PARTIAL_OPEN / PRIOR_ART_UNVERIFIED`
2. `P03-AUDIT-P04-I0101-P4021-S3-ORBIT-DUAL-231 = PASS (CLAIM-SCOPED)`

Reconciliation: `P26-RECONCILE-P04-I0101-P4021-2OF2-16 = PASS`.

P26 report:

- path: `proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_09-57-08__run-report.md`
- creation commit: `a6c658568e772bf00ed02f83406ad57918d9d4b0`
- exact-commit readback blob: `bff3e9043d3c93a9e90adc5121f367dcf772ec33`
- readback terminal marker: `End of complete P26 run report.`

P26 canonical-checker reexecution:

- path: `proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_09-57-08__p4021_canonical_reexecution.out`
- creation commit: `f22b2a984fa531f6c0c9fdbfec27ec23ffe63985`
- readback blob: `7dade9a4ff6d0684a8be2ecc8d4a8d09e5dc7b70`
- exact PD slack: `128066702`
- threshold margin: `13231`

Distinct P03 audit report:

- path: `proofnet24/P03-fei/runs/2026-09-17/2026-09-17T06-41-47Z__rotation-i0003-run-report.md`
- creation commit: `6f289bb578d767cec1ec287cca2d4f238c88b677`
- blob: `c5e404401866145c004584e6c4f38346f3482fe7`

Canonical P04 finite certificate:

- theorem report commit: `83d8416324638612fa08a83e9e2ed38fc9e3f835`
- report blob: `1e34f1870de0eb38473e04d09071902b9424ffb6`
- checker blob: `96a2ea6f7d2a7ef510c04fd6c18f8357954cb6fb`
- canonical output blob: `0b78d60898a54b0bcfe47a6d3359f9c6c8021eaf`

Fresh shared-root blobs observed before report write:

- `RESULTS.md`: `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`
- `POSTED.md`: `4cba5265702ede8ecf9c11938a4e70d55f52549c`
- `QUEUE.md`: `770a58cc1bbe70d912d2254db077aa5756db27e1`

No shared-root replacement was attempted because the available mutation is whole-file replacement and the complete current editable bodies are not safely exposed in one bounded connector rendering. The exact delta above is preserved here rather than risking loss of unrelated concurrent evidence.

The `p=4013` finite package remains the earlier counted item; neither repeated P26 work nor repeated P03 work on either prime creates another metric item.
