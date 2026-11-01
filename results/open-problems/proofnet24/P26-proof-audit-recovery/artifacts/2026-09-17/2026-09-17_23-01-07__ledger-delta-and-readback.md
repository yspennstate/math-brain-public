# P26 ledger delta and readback — 2026-09-17 23:01:07

## Fixed metric

- role: outside-proof-audit support
- fixed metric: number of outside packages with two genuinely independent OTHER-track full-proof audits complete
- before: `25`
- after: `25`
- movement: `0`
- supported unchanged count: `0 -> 1`

## Package audited

- owner: `R07`
- source: Burdzy--Scheutzow, *Forward Brownian Motion*, Problem 7.8 / intake `I0077`
- claim: `I0077-R07-T28`
- package description: geometric sampled spatial-comb gate obstruction, its source-driven positive central-tooth regime, and the positive-width log-time thickening implication
- mathematical status: `PROVED_CLAIM_SCOPED`
- parent source status: `PARTIAL`
- publication priority: `UNVERIFIED`

## Audit IDs

- P26: `P26-AUDIT-R07-I0077-T28-SAMPLED-COMB-29 = PASS_FULL_MATHEMATICAL_PROOF / CLAIM_SCOPED / SOURCE_PARTIAL / PRIOR_ART_UNVERIFIED`
- second genuinely distinct audit: `MISSING`
- reconciliation: `P26-RECONCILE-R07-I0077-T28-2OF2-29 = PENDING_SECOND_DISTINCT_AUDIT`

The earlier pair `P26 + R06` for `I0077-R07-T22` does not audit T28 and is not reused.

## Directed second-audit request

Concise request only; no job/schedule was created and no peer file was edited:

> **R06 if available:** independently audit `I0077-R07-T28` end to end. Do not inherit the T22 PASS. In particular rederive (i) the periodic-comb total transition-mass bound, (ii) why `Q<e^{-P}` rather than merely `Q<1` is needed, (iii) the arbitrary-real-terminal Brownian/Borel--Cantelli step, (iv) the dependence-safe transfer to a fixed-index FBM Brownian witness, and (v) the canonical exact finite core. Leave P26 reconciliation pending unless the full proof survives.

## Independent finite core

Checker:
`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_23-01-07__i0077_t28_exact_audit.py`

- creation commit: `6b496d77f4cf8851f280f671cadcd11c9e27efe0`
- exact-readback blob: `7a3d5c76a4f99548239d044c0260087481d6ea33`

Output:
`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_23-01-07__i0077_t28_exact_audit.out`

- creation commit: `f648ab6168950e866bd034814fc6fbc72fb07180`
- exact-readback blob: `e7de17fc5f9f0be21fc9a9346c4c9d9d4fba4609`
- first line: `P26-I0077-T28-INDEPENDENT-EXACT-AUDIT: PASS`
- last line: `ALL_EXACT_CHECKS_PASS`

## Immutable P26 report

`proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_23-01-07__run-report.md`

- creation commit: `30c1e7f5db2071a9e993f38bf2f183e89ecd5722`
- exact-readback blob: `eca1e06653778357cf3ed627afad665888c2556b`
- first-line readback: model `GPT-5.6 Sol`, reasoning `UNVERIFIED`, no movement `25 -> 25`, unchanged `0 -> 1`, methods `#2,#11,#22`
- tail readback reached literal `End of complete P26 run report.`

## Fresh shared-root blobs observed after report write

- `RESULTS.md`: `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`
- `POSTED.md`: `4cba5265702ede8ecf9c11938a4e70d55f52549c`
- `QUEUE.md`: `2bb9fd1ac6ae45440cbddf25943e1afec6754693`

No `POSTED.md` promotion, queue ownership change, or source closure is warranted. The root `RESULTS.md` view remains stale for the current P26 metric and is a whole-file replacement surface; this sidecar pins the exact safe merge delta rather than risking loss of unrelated concurrent history.

## Safe merge delta

```yaml
track: P26
fixed_metric: outside packages with two genuinely independent OTHER-track full-proof audits complete
before: 25
after: 25
movement: 0
unchanged_count_before: 0
unchanged_count_after: 1
package: R07/I0077/I0077-R07-T28
owner: R07
mathematical_status: PROVED_CLAIM_SCOPED
source_status: PARTIAL
activity: R07_ACTIVE
p26_audit: P26-AUDIT-R07-I0077-T28-SAMPLED-COMB-29=PASS_FULL_MATHEMATICAL_PROOF
second_distinct_audit: MISSING
reconciliation: PENDING_SECOND_DISTINCT_AUDIT
report_path: proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_23-01-07__run-report.md
report_commit: 30c1e7f5db2071a9e993f38bf2f183e89ecd5722
report_blob: eca1e06653778357cf3ed627afad665888c2556b
finite_core: P26-I0077-T28-INDEPENDENT-EXACT-AUDIT=PASS
prior_art: BOUNDED_DATED_SEARCH_DONE_NOVELTY_UNVERIFIED
posted_change: none
queue_change: none
```

END SIDECAR
