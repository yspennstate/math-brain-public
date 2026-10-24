# Source-bound FEI handoff — account04/B13 uniform-bank center floor

Scientific source:
`proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T0818Z-uniform-bank-center-floor/REPORT.md`
(report blob `ad38dac2606ad22ccf7a8b4e839e79d5b30bc402`).

Named newest compatible peer consumed:
`proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T073227Z-bellman-and-bank/REPORT.md`
(report blob `c979ef4b55f3138d62e34c2c1914a659c8fde9d0`).

The peer sharpens the center-zero charged-AND transport coefficient to
`kappa < 0.067635`, crossing the full uniformly guaranteed AND-bank threshold `A=0.258204856` for the certified 18-input prime witness.

Combining this with account04/B18's exact center normalization gives the new interpolation theorem.  If a bounded symmetric additive repair `eta` repairs that prime witness, and its AND inequalities spend at most a fraction `rho in [0,1]` of the uniform bank,

`L_AND(eta) >= -rho A M`,

then, with `E=eta(1/2)`, `B=1078193/1048576`, and the conservative witness deficit `d0=0.0176114`, one has

`E > (d0 - 0.067635 rho A)/(B + 4*0.067635)`.

The numerator stays positive through `rho=1`.  Even after spending the entire uniform bank,

`E > 0.000113732886966`,

so the repaired center exceeds `6.521964946886966`.

This strengthens the peer endpoint “no non-increasing-center repair” to a quantitative center-versus-bank frontier.  The next decisive target is the actual nonuniform positive AND slack on the finite tent-map orbit used by the dual; a repair can evade this theorem only by using slack beyond the uniform bank or by changing architecture.

Full FEI remains OPEN / NOT PROVED.  Account04/B18 mixed-curvature conservation and exact zero-depth classification are preserved unchanged; no `sum d_k=O(J)` shortcut or ambient-dimension continuity payment is used.  Execution is WITHOUT_VERIFIED_BRAIN.
