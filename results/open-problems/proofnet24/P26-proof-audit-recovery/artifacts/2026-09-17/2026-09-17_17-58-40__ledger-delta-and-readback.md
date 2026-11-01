# P26 ledger delta and exact-readback receipt — 2026-09-17 17:58:40 run

Track: P26 independent outside-proof audit recovery.
Repository / branch: `yspennstate/math-open-problems` / `master`.

## Fixed metric delta

- metric: number of outside claim-scoped packages with two genuinely independent OTHER-track full-proof audits complete
- supported before: `20`
- supported after: `21`
- supported unchanged count: `0 -> 0`
- new counted package: `R20 / I0100 / p=41 exact one-localized Paley theta theorem`

## Claim and audits

Frozen theorem:

`vartheta(complement G_{41,1}) = 2*sqrt(5)`.

P26 audit:

`P26-AUDIT-R20-I0100-P41-FOURIER-DUAL-ENDTOEND-24 = PASS_FULL_FINITE_PROOF / CLAIM_SCOPED / SOURCE_PARTIAL_OPEN / PRIOR_ART_UNVERIFIED`

Distinct OTHER-track audit:

`R19-AUDIT-R20-I0100-P41-01 = PASS`

Reconciliation:

`P26-RECONCILE-R20-I0100-P41-2OF2-24 = PASS`

Count consequence: add exactly one package, `20 -> 21`. Repeated future P26/R19 reviews of the same finite theorem do not move the metric.

## Immutable P26 report

Path:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_17-58-40__run-report.md`

Creation commit:

`fe197529156e14b3944db5e3ce6aa4f6fba57336`

Exact-commit readback blob:

`0ff272b481ed60e675151b250fc52633c126e076`

Tail readback reached:

`End of complete P26 run report.`

## P26 exact finite audit artifact

Checker path:

`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_17-58-40__p41_independent_exact_audit.py`

Checker creation commit:

`73f0878b26895e78d641a7fce3b0c75177176a26`

Checker readback blob:

`628ac0575054b6ac008b010b39015f63d5751eda`

Archived output path:

`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_17-58-40__p41_independent_exact_audit.out`

Output creation commit:

`73f061af1070dc6d7b9e64a21d1695541d820bb1`

Output readback blob:

`942e7b650150bc38f076b41a47e53221f40b55c6`

Output verdict:

`P26-I0100-P41-INDEPENDENT-EXACT-AUDIT: PASS`

Exact reconstructed data include complement reduced classes `[1,2,3,6,8]`, primal support `[0,1,4,5,6,9]`, dual slack set `{-1/2+sqrt(5)/4,0,1,sqrt(5)/4}`, and exact objective `2*sqrt(5)`.

## Distinct R19 evidence

R19 report:

`runs/R19/2026-09-16_15-35-00_UTC__i0084-free-halfstable-gap.md`

Current readback blob:

`99da40c57194cf11c4e301a3c69aee2d99d6e20f`

The report explicitly records `R19-AUDIT-R20-I0100-P41-01 = PASS` and says it independently rebuilt the p=41 exact primal/dual certificate. Its exact checker/output separately record PASS for the same audit ID.

## Parent-source status

- Randomstrasse Conjecture 26 remains source-level `OPEN / PARTIAL` in this reconciliation.
- This finite p=41 theorem does not prove the asymptotic.
- R20 remains the active I0100 research owner.
- Publication novelty/priority remains `UNVERIFIED`; the circulant/Fourier LP mechanism is known prior art.
- No `POSTED.md` promotion is made.

## Shared-root freshness after report write

Fresh observed blobs:

- `RESULTS.md`: `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`
- `POSTED.md`: `4cba5265702ede8ecf9c11938a4e70d55f52549c`
- `QUEUE.md`: `2bb9fd1ac6ae45440cbddf25943e1afec6754693`

No destructive whole-file update was attempted. The connector exposes the large current `RESULTS.md` body through bounded/truncated rendering, so reconstructing it would risk unrelated concurrent ledger loss. This sidecar is the exact safe merge input for the P26 `20 -> 21` update.

The queue surface has 60 listed source candidates but does not certify 60 fully source/status/history/ownership-checked genuinely unassigned READY candidates. Stronger reserve requirement remains `NOT CERTIFIED`.

## Runtime/configuration note

Actual report line records GPT-5.6 Sol / reasoning `UNVERIFIED`. The task interface exposed to this worker provides title, prompt, schedule, enabled state and timing mode, but no enforceable model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated per-run routing attestation. No scheduler state was modified.

END SIDECAR
