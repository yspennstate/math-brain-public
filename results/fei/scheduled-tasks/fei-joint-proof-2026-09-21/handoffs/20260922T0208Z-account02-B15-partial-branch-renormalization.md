# account02/B15 FEI handoff — partial-branch renormalization fixed point

Status: `WITHOUT_VERIFIED_BRAIN`. Full unrestricted FEI remains **OPEN / NOT PROVED**.

Scientific source: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T015258Z-partial-branch-renormalization/REPORT.md`, report blob `a8fd8e0a00b60ec8a4348d992f8df8d0365449b5`; checker-output blob `19aa4375289359d7eb37416826089921a421e40f`.

Consumed peer result: account01/B17 `20260922T014112Z-partial-branch-shared-core/REPORT.md`, blob `317694313bd078634b62d252fe9efa0085afcb14`, plus account03/B18's completed shared-graft-tail theorem.

New proved mechanism: for any balanced monotone marked gate with state `D=I-1`, `R=H/D`, marked singleton `c`, nest four copies only along the marked branch and then apply the exact nine-host shared-core operator. The state update is

`c' = 57/256 + c^4/256`,

`D' = 133/128 + (9/256)(1+c+c^2+c^3) D`,

`R' = q R + (1-q) T(c)`,

where `q=((9/256)(1+c+c^2+c^3)D)/D'` and `T(c)=(128/133)K(c^4)` for the exact source-core forcing `K`.

Starting from the certified 162-input gate, the reusable singleton decreases to the unique fixed point

`0.22266585228 < c_* < 0.22266585229`, 

and the ratios increase strictly to the forcing fixed point

`6.5218511673478 < R_* = T(c_*) < 6.5218511673480`.

Hence `C_FEI > 6.5218511673478`. This is a lower-bound/candidate-elimination theorem, not a universal FEI upper bound. It improves the account01/B17 partial-branch lower bound by more than `4.82666e-8` and completely exhausts repeated use of this same depth-four renormalization operator.

Next exact adversarial target: heterogeneous partial substitution, allowing branch depth and/or the branch gate to vary while tracking the state `(R,D,c)` against the exact convex update. Do not resume the already exhausted full-fourfold recurrence or repeat this fixed depth-four operator unchanged.
