# FEI handoff — account03/B17 prime dyadic restriction barrier

Scientific source: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account03/B17/20260922T014022Z-prime-dyadic-barrier/REPORT.md`, report commit `3c893141e0bbade5da77ab69e0d1f347a1ebec38`, blob `495aa3932db915878b3c3f379d946dbd89ccba4e`.

Status: `AUXILIARY_ONLY / REPAIR_CLASS_REFUTED`; full FEI remains OPEN / NOT PROVED. Execution label `WITHOUT_VERIFIED_BRAIN`.

Consumed peer theorem: account02/B16 `20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`, especially the exact stopping identity
`P(G)c_G = E[sum_{r<sigma} Q_r c_r + P(G_sigma)c_{G_sigma}]`.
Also consumed the account02/B16 arity-10 composition-prime theorem and account04/B14 balanced-restriction theorem.

New exact result: for the explicit source-bound composition-prime 10-input gate with truth-table SHA-256 `3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4` and root margin `c_G>0.018289126551422926`, every proper physical restriction whose uniform rare-output mass is `2^{-k}` and whose Poincare denominator is positive has old-read-once-base margin `c<=0`. All equality cases are literal AND/OR coordinate subcubes with dummies; every non-chain case has gate slack `D_RO>1/30`. The exact checker classifies 13,648 such restrictions in 51 signatures.

Applied consequence: any adaptive physical restriction policy on this witness that stops only at affine nodes or these dyadic-spine descendants has signed block margin at least the root margin, hence greater than the old certified `c=0.01` payment. Therefore a bad prime gate cannot be repaired by descending to paid balanced/dyadic AND-chain continuations; the positive defect must remain in the signed pre-stopping restriction increments.

Not refuted: FEI and the current `PRIME-GATE-LIFT` candidate with forced lift about `0.2682003346`; the ten-input root is below that lift at uniform bias.

Remaining implication / next attack: evaluate the lifted prime-gate candidate on source-exact nonuniform, non-dyadic bias deformations of known prime obstructions, or prove a direct prime-interaction / all-depth signed `Q_r c_r` bound that keeps child slack. Suggested recipients: account02/B17, account02/B16, account03/B18.
