# FOREST B20 source-bound handoff

Run: `20260922T012259Z-B20-e3d71907`  
Outcome: `ESSENTIAL_STEP_APPLIED`; parent FOREST conjecture remains `OPEN`.

Authoritative report: `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet01/B20/20260922T012259Z-B20-e3d71907/report.md`, blob `1a94f31efde4c0422d81cd81c1fb16b82bc57860`.

## New exact interface

For `K=G-{e,f}` and the standard addability cells `A00,A10,A01,A11` with overlap set `Q`, for `R in A00` let `P_e(R),P_f(R)` be the unique marked endpoint paths. Define `alpha=|P_e\P_f|`, `beta=|P_f\P_e|`, `gamma=|P_e cap P_f|`. For `H in A10,A01,Q`, let `c_e(H),c_f(H),c_q(H)` count `K`-edges between the corresponding two terminal components.

Then the exact path-cut flux laws are

`sum_A00 alpha = sum_A10 c_e`,

`sum_A00 beta  = sum_A01 c_f`,

`sum_A00 gamma = sum_Q c_q`.

They follow by inverse edge-deletion/edge-addition bijections and are genuine graph-global compatibility constraints absent from the local three-edge cone.

For simple graphs this implies

`2 n00 <= sum_A10 c_e + sum_Q c_q`,
`2 n00 <= sum_A01 c_f + sum_Q c_q`,
`3 n00 <= sum_A10 c_e + sum_A01 c_f + sum_Q c_q`.

## 3-connected overlap completion

If `G` is 3-connected, `K` is connected. For every `H in Q`, contract the components of `H`; the quotient of unused `K`-edges is connected, so the common terminal components have a quotient path. Adding its edges successively gives a forest in `A00`.

A direct one-edge reverse switch is false: in `K4` with `e=01`, `f=02`, `H={12}` lies in `Q`, but its common terminal components `{0}` and `{1,2}` have no direct remaining `K`-edge. A two-edge quotient path through vertex `3` completes it. The exact regression found 1452 zero-direct-capacity `Q` states in labelled 3-connected graphs on at most five vertices.

## Next exact target

Construct a multiplicity-controlled multi-step quotient-path flow, or equivalent Hall/fractional matching inequality, from `A00 x A11` into `A10 x A01` plus `H_all x Q`, using the three flux identities together with marked-1-separation cancellation and the lead's simultaneous Simpson/sign constraints. It must control fibres without a factor depending on graph size, quotient-path length, or number of quotient paths. The `K4` overlap state above is a mandatory regression.

Consumed source versions: lead `fleet01/B01/20260922T000824Z-fleet01-B01-forest-11/report.md` blob `367d85a8c6ac4ef3f00e1686a28eac60642274e0`; assigned partner `fleet04/B03/20260922T001033Z-B03-r43/REPORT.md` blob `9b0e6f246b82be1647a85af62269035b538fd655`; fleet01/B02 switching report blob `bb237f4918b79bf6122b574ee46dc1addc29fca2`.
