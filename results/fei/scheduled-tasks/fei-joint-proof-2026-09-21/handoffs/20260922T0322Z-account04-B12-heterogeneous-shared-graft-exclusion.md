# account04/B12 source-bound FEI handoff — heterogeneous shared-graft exclusion

Source scientific report: `proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T031946Z-heterogeneous-shared-graft-exclusion/REPORT.md` in `yspennstate/math-open-problems`, report blob `e6854578d1cf8be7058847a80a558fc512f6f435`.

Status: `ESSENTIAL_STEP_APPLIED`; full FEI remains OPEN / NOT PROVED. Execution: `WITHOUT_VERIFIED_BRAIN`.

Named newest peer consumed: account02/B16 `20260922T031545Z-limit-prime-shared-core-threat-corridor`, blob `7b8836311af20ce7c0342e3deaeb4869651d2cfe`. Its exact implication is that any heterogeneous fixed-core counterexample to the stable candidate `C*=6.5218512` must start from a balanced input gadget with absolute defect `Delta_*(h)<3.846028304990334e-7`, and must use a source-valid singleton inside `0.002274773147<b<0.003151817853`.

New inference: every member `F_t` of the certified infinite shared-graft hard family has `Delta_*(F_t)>7.2298419700750362e-7`, with the finite-stage minimum at `F_2`; for all `t>=5`, `Delta_*(F_t)>4.9839460419424746e-5`. Hence the whole recursive family lies strictly outside the heterogeneous threat corridor by a uniform factor greater than `1.87982027`. Balanced self-composition only increases absolute defect, so the same exclusion holds for every `F_t^{circ d}`, `d>=1`.

Consequence: no member of the known record family, nor any of its balanced self-compositions, can be turned into a violating output of the exact shared-core transform merely by choosing a different actual singleton coefficient near the scalar maximizer. Any surviving heterogeneous attack on `LIMIT-PRIME-GATE-LIFT-v1` must use a genuinely different balanced Boolean gadget satisfying both the sub-`3.84603e-7` absolute-defect condition and the narrow singleton window.

Checker source blob `ffc5d9f7350232847edca10cde5fd49b967204d1`; recorded PASS output blob `4d797c14e8eef6552454ad18d27a9fcd4bfaf944`. The account04/B18 mixed-curvature theorem is preserved; this result makes no claim that `sum_k d_k=O(J)`.
