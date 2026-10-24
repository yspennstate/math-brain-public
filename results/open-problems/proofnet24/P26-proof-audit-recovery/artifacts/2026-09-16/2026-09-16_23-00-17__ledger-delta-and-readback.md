# P26 ledger delta and exact readback — 2026-09-16 23:00:17

This immutable artifact records the safe shared-ledger delta, the exact GitHub readbacks, and one readback-detected rendering erratum. It does not overwrite any historical report.

## Canonical report receipt

- report: `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_23-00-17__run-report.md`
- creation commit: `810823c47ecf0aeb694cce3e9e48df63e438b3d6`
- readback blob: `340293c650d2f7b3f52e5b446b90844d7d4a5894`
- terminal readback verified: `End of complete P26 run report.`

## Readback erratum

The immutable report readback revealed one escaped-character rendering defect in equation (4.12): the first fraction command rendered as the literal text `rac{(297/16)^2}{(15/8)^3}` (preceded by a line break/control escape) instead of `\frac{(297/16)^2}{(15/8)^3}`.

The intended and mathematically used identity is exactly

\[
K^2=\frac{(297/16)^2}{(15/8)^3}=\frac{6534}{125}.
\]

The next equality in the immutable report, the exact checker, and the archived checker output all carry the correct value `6534/125`. No mathematical claim changes. The original report is preserved immutably rather than overwritten.

## Exact checker receipts

- checker source: `proofnet24/P26-proof-audit-recovery/artifacts/2026-09-16/2026-09-16_23-00-17__r19-c002-parameter-audit.py`
- source creation commit: `2002147a71272e80eae64afa2ff829517f0a31eb`
- source blob: `54c98610658ca96be45e2e2317b0851557db1239`
- computed source bytes: `1866`
- computed source SHA-256: `d82f88d9a7a6868e9d7d47ef0f9564000c12c4dd0da19c5b8bcf81d9e7522a68`
- output: `proofnet24/P26-proof-audit-recovery/artifacts/2026-09-16/2026-09-16_23-00-17__r19-c002-parameter-audit.out`
- output creation commit: `fbaedc707e1ab91d2f8322c1bb2df24ea20a1980`
- output blob: `a1ab90e82f9bd2f0d625877591aa16b47bc2e31c`
- computed output bytes: `311`
- computed output SHA-256: `eec33ab0c88422230aad4ec591d88978b2925b6c50fc71b063a577104b16385c`
- execution terminal status: `ALL_EXACT_CHECKS_PASS`

## Shared-root fresh blobs observed after report write

- `RESULTS.md`: blob `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`
- `POSTED.md`: blob `f9ab12835d6f043fbbe22da9cae98c80e9f6240a`
- `QUEUE.md`: blob `770a58cc1bbe70d912d2254db077aa5756db27e1`

No whole-file root replacement was attempted because the available `RESULTS.md` rendering was truncated while the write action requires complete replacement content. This is a conflict-safety deferral, not a claim that the root ledger is current.

## Exact merge delta

```yaml
ledger_delta:
  track: P26
  fixed_metric: "outside claim-scoped packages with two genuinely independent outside full-proof audits complete"
  before: 2
  after: 3
  unchanged_count_before: 0
  unchanged_count_after: 0
  movement: "+1"
  package:
    source: "Takahiro Hasebe and Yuki Ueda, ALEA 15 (2018), Conjecture 5.5, published free-stable branch"
    claim: "R19-I0084-C002"
    owner_report: "runs/R19/2026-09-16_15-35-00_UTC__i0084-free-halfstable-gap.md"
    owner_creation_commit: "da07675fba25ead7d124320f267bf51d8205d630"
    owner_blob: "99da40c57194cf11c4e301a3c69aee2d99d6e20f"
    audit_1: "R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF"
    audit_1_report_commit: "66e33808f21ad00ca88b4d81d3b9216c4e929cd4"
    audit_1_report_blob: "0a4504d58b140770fe19f89a1142f4a93c17074a"
    audit_2: "P26-AUDIT-R19-I0084-C002-ENDTOEND-06=PASS_FULL_MATHEMATICAL_PROOF/PUBLISHED_ALEA_SCOPE"
    audit_2_report_commit: "810823c47ecf0aeb694cce3e9e48df63e438b3d6"
    audit_2_report_blob: "340293c650d2f7b3f52e5b446b90844d7d4a5894"
    mathematical_status: "REFUTED_AS_STATED for published ALEA universal Conjecture 5.5"
    later_arxiv_frozen_scope: "NOT_MERGED / NOT_AUDITED_BY_THIS_PACKAGE"
    prior_art: "BOUNDED_CURRENT_SEARCH; GLOBAL_NOVELTY_UNVERIFIED"
    posted: false
  results_action: "PENDING_SAFE_MERGE"
  posted_action: "NO_CHANGE"
  queue_action: "NO_CHANGE"
```

End of immutable P26 ledger/readback artifact.
