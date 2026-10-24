# PROB20-14 delivery/readback receipt

This receipt records the append-only delivery status for the 2026-09-16T09:08:40Z research iteration.

## Substantive report

Path:
`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/runs/2026-09-16/2026-09-16T09-08-40Z__report.md`

Creation commit: `4ab9b6c1dc21c5b4edc586ee5a99f806e2194b57`  
Readback blob at that exact commit: `4cc867bb91721021fa889558b9402b66f768d39c`

Status: **VERIFIED WITH APPEND-ONLY TRANSPORT ERRATUM**. Exact-commit readback exposed a typography/escaping defect in equations (5.3) and (5.4); no mathematical derivation changed. The correction is recorded below rather than overwriting the original report.

## Report addendum / transport correction

Path:
`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/runs/2026-09-16/2026-09-16T09-08-42Z__report_addendum.md`

Creation commit: `483c3aa62deb3099d96e841a2e4dab44287f1935`  
Readback blob at that exact commit: `488f00a7ac02bbf91731903cd9823776ddbbb0b3`

Status: **VERIFIED**.

## Reproducibility artifact

Path:
`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/kesten_entropy_budget_check_20260916.py`

Creation commit: `af6f83b69613c044172fa866d1b201232bf3229b`  
Readback blob at that exact commit: `55a2544932af9fdf08c0c45889f551df3721d39f`

Status: **VERIFIED**.

## Execution certificate

Path:
`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/runs/2026-09-16/2026-09-16T09-08-41Z__artifact_check.md`

Creation commit: `d0f7ac471458a9d8eb9c2d0b0b00b061aee0b671`  
Readback blob at that exact commit: `7497b4dafdc07e78161b1e9bbac07b99b2a34b0c`

Status: **VERIFIED**. The finite-support consistency checker actually executed and ended with `ALL_ASSERTIONS_PASSED`. It is explicitly not evidence for the infinite-variance target theorem.

## Access / policy status

No approval or security denial was exposed. No retry was needed. No existing or peer file was overwritten. No Gmail/email, Google Drive, workflow/settings, access-change, force-push, credential-inspection, public-posting, third-party-contact, or paid-compute action was taken.