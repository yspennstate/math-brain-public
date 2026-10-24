# FEI handoff — account02/B18 fixed depth-four shared-core saturation

Source scientific report: `proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T0204Z-depth4-shared-graft-saturation/REPORT.md`, creation commit `fe63d5af4fcc82108499ecde3f437d55dd54db41`, blob `d5c769a021199e9c778cc2fe3d813060fd75b594`.

Consumed completed OTHER-account result: account03/B15 `20260922T012556Z-iterated-shared-graft`, which certifies `R(F6)>6.5218509495504481848401605388605` and supplies the exact account01/B18 depth-four recurrence.

New exact results:

1. For the same nine-host shared-core transform preceded by arbitrary integer self-composition depth `m>=1`, a balanced gadget `(R,I,c)` maps to

   `R'-R = [K(c^m) - (133/128)R] / [(9/256) I^m + 257/256]`.

   Thus the sign of improvement is independent of `I`; influence only suppresses step size.

2. For the source core, `0 <= K(b) <= 153/16` on `0<=b<=1`.

3. Continuing the exact depth-four recurrence from account03/B15's `F6`, the **total absolute movement over every future round is < 1e-26**. Hence every later ratio and the limiting ratio are `< 6.52185094955044818484016055`.

Interpretation: the fixed depth-four shared-graft lower-bound mechanism is now quantitatively saturated. Do not spend another run merely extending `F6 -> F7 -> ...` with the same depth four. A stronger same-core lower obstruction must use a different depth `m` with positive numerator `K(c^m)-(133/128)R`, or change the shared core/gate. This is not a universal FEI upper bound. Full FEI remains OPEN.

Suggested nonoverlapping next claims: one worker can rigorously classify integer depths `m` for the current `(R6,c6)` using the numerator above; another can seek a different shared core. Upper-bound workers should continue the universal all-gate potential problem rather than iterating this saturated lower-bound family.

Execution: `WITHOUT_VERIFIED_BRAIN`; no scheduler mutation; no credentials, scheduler identifiers, machine paths, benchmark data, or private transcripts included.
