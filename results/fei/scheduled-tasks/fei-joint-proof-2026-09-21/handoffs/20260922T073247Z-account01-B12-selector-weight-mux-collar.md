# FEI handoff — account01/B12 selector-weight MUX collar

Source scientific artifact: `proofnet24/P03-fei/fleet-2026-09-21/account01/B12/20260922T071311Z-selector-weight-mux-collar/REPORT.md`, scientific commit `82f27e65d09d0290c27730424378d34d95060a89`, report blob `2f51e9ea8b6a832d3db33f5eb4db081a2e699ec0`.

Classification: `ESSENTIAL_STEP_APPLIED`; full FEI remains OPEN.

Live candidate: `C^dagger=6.521851214`, `Gamma^dagger=Gamma_0+0.268204856 p(1-p)`, common target `LIMIT-PRIME-GATE-LIFT-v1`.

Consumed and extended exact peer: `account03/B15/20260922T065548Z-adaptive-mux-142/REPORT.md`, blob `65012580ffd1844e2a316138f54e35948f55beb7`.

New theorem. For `MUX(A;D0,D1)` with selector bias `p<=1/2`, other-data bias `x`, near-deterministic data bias `y`, set
`Q=p(1-p)x(1-x)` and `L=log2(16/Q)`. Then

`0 <= y <= Q/(288 p L)  ==>  D_{Gamma^dagger}(MUX;p,x,y) >= 0`.

Together with the peer `Q/(142L)` collar, the certified width is at least
`(Q/L) max{1/142,1/(288p)}`, so the new bound is strictly wider for `p<71/144` and does not collapse linearly as `p->0`.

Key mechanism: retain the selector factor `p` in both physical potential movements, prove the two child-AND spectral laws have TV exactly `4p(1-p)|2x-1|` and hence entropy difference `<4pL`, and retain `p` in the six-mass MUX spectral TV. This yields

`R_1^dagger > -(75969/294912) Q = -0.257598876953125 Q`,

whereas any live-candidate counterexample would require
`R_1^dagger < -0.258204856 Q`. Exact gap:
`0.258204856 - 75969/294912 = 38782659/64000000000 > 0`.

Next missing implication: the genuinely interior unequal-MUX region outside deterministic-face collars and already-closed common/complementary/zero-credit tubes. Even full MUX remains weaker than the all-prime/all-bias target.

Execution label: `WITHOUT_VERIFIED_BRAIN`; this is repository handoff only, not a native brain-assistance claim.
