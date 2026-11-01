# P26 ledger delta and exact-readback receipt — 2026-09-17 14:56:56

Model actually running for the associated report: GPT-5.6 Sol. Reasoning level: UNVERIFIED. GPT-6 / maximum was requested but not authenticated by the exposed scheduler/runtime.

## Fixed metric delta

- metric: outside packages with two genuinely independent full-proof audits complete
- supported before: 17
- supported after: 18
- unchanged count before: 0
- unchanged count after: 0
- newly counted package: `P11-I0062-Q36-SOURCE-REFUTATION-02P`
- P26 audit: `P26-AUDIT-P11-I0062-Q36-SOURCE-REFUTATION-02P-21 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_LITERAL_QUESTION_PASS / CORRECTED_HEIGHT_PROVEN / ORIGINAL_1987_HEIGHT_PROVENANCE_UNVERIFIED / PRIOR_ART_UNVERIFIED / CLAIM_SCOPED`
- distinct OTHER-track audit: `P04-AUDIT-P11-I0062-Q36-SOURCE-REFUTATION-02P-10 = PASS (CLAIM-SCOPED)`
- reconciliation: `P26-RECONCILE-P11-I0062-Q36-02P-2OF2-21 = PASS`

The P04 audit is genuinely distinct from P26 and P11 self-proof. Repeated P26/P04 audits do not count again.

## P26 immutable report

Path:
`proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_14-56-56__run-report.md`

Creation commit:
`f00d576231bfcc2ac0a91746b0646a1a5eb6a5d7`

Readback blob:
`e0cfd0da6b9bc8dc9334a0d20aff9d30bcedcd90`

Exact-commit head readback reproduced the required first line and baseline. Exact-commit tail readback reached:
`End of complete P26 run report.`

## P26 exact-check reexecution

Path:
`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_14-56-56__p11_i0062_heavytail_checker_reexecution.out`

Creation commit:
`bca4de73691ce24a5d74d07c89dcf8a0ac622290`

Readback blob:
`57ea3526206b3b392a4f2c19418a496825dca8da`

Terminal verdict:
`P26-I0062-Q36-EXACT-RECHECK: PASS`

## Distinct P04 audit evidence

Path:
`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T09-42-30Z__run-report.md`

Creation commit:
`2898565e9814059a45cf36ca60c187b457663915`

Blob at that commit:
`05792586dc3e473449c4f8476b5fe484c7e945f3`

The P04 report independently reconstructs the heavy-tail law, corrected height geometry, independent high-column estimate, Borel-Cantelli step, primal flow and dual cut lower bound, and records `P04-AUDIT-P11-I0062-Q36-SOURCE-REFUTATION-02P-10 = PASS (CLAIM-SCOPED)`.

## Fresh shared-root blobs after report write

- `RESULTS.md`: `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`
- `POSTED.md`: `4cba5265702ede8ecf9c11938a4e70d55f52549c`
- `QUEUE.md`: `2bb9fd1ac6ae45440cbddf25943e1afec6754693`

No shared-root file was rewritten. `RESULTS.md` remains visibly stale for P26 and a whole-file reconstruction from bounded rendered content would risk unrelated concurrent history. `POSTED.md` receives no promotion from this audit alone. `QUEUE.md` receives no ownership change; live canonical ownership is P11 under `operations/claims/I0062.md`.

## Exact safe RESULTS merge input

```text
P26 SUPPORT | outside packages with two genuinely independent full-proof audits complete | 17 -> 18 | PROVED claim-scoped package / source complete-deletion reading REFUTED under corrected intended height | unchanged=0 | P11-I0062-Q36-SOURCE-REFUTATION-02P | P26-AUDIT-P11-I0062-Q36-SOURCE-REFUTATION-02P-21 + P04-AUDIT-P11-I0062-Q36-SOURCE-REFUTATION-02P-10 | report proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_14-56-56__run-report.md @ f00d576231bfcc2ac0a91746b0646a1a5eb6a5d7 | original-1987-height-provenance=UNVERIFIED | prior-art=UNVERIFIED | public-posting=not asserted
```

## Reserve status

`QUEUE.md` still records 60 listed source candidates but does not certify 60 genuinely unassigned fully source/status/history/ownership-checked READY candidates. Newly certified READY entries remain zero in that root snapshot. The stronger reserve requirement is therefore NOT CERTIFIED.

## Model/scheduler routing status

Exposed scheduled-task controls remain title, prompt, schedule, enabled state and timing mode. No enforceable model selector, reasoning-effort selector, guaranteed duration, or authenticated per-run model attestation is exposed. Enforcing GPT-6/maximum requires product/backend support for those fields plus trustworthy run telemetry. A `You cannot modify this task` denial requires the authorized owner/main-agent/UI/admin context for the same task or platform support to repair ownership; permission bypass or cloning is not a valid workaround.

End of P26 ledger/readback sidecar.
