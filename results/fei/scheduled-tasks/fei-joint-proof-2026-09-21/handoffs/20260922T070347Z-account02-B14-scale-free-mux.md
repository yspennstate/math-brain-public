# FEI source-bound handoff — account02/B14 scale-free MUX selector

Run: `20260922T070347Z-fei-mux-offplane`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full FEI status: **OPEN / NOT PROVED**.

Scientific source is private `yspennstate/math-open-problems`, own path:

`proofnet24/P03-fei/fleet-2026-09-21/account02/B14/20260922T070347Z-scale-free-mux-selector/`

Read back scientific artifacts:
- `REPORT.md`, commit `5cc4461031c53d1f2a9827570b8e1fb74fba1d17`;
- `verify_bounds.py`, commit `6bf000633ec357007bfa2085c4445810609ba277`;
- `verification.txt`, commit `15ec1a71d60ba3bdc65d7736c79c802f3b6c712c`;
- `MARGIN_ADDENDUM.md`, commit `9347b63c3967250364e5b2a1db441c451cb9a4b9`, blob `a816ee26961498c5e882ef7f1fc71b80cf7ff37a`.

Named peer inputs actually consumed:
- account03/B13 `20260922T063425Z-mux-selector-tube-x8/REPORT.md`;
- account04/B18 `20260922T061350Z-mux-equal-data-offcenter-tube/REPORT.md`;
- account01/B18 `20260922T055608Z-balanced-mux-collar-sharpen/REPORT.md`;
- account01/B14 `20260922T0044Z-balanced-gate-margin-refutation/REPORT.md`, blob `776ade5c2e2017844785b09ab7af50c7eaf54c03`.

New theorem for the live lifted Campaign-A potential `Gamma^dagger=Gamma_0+0.268204856 z(1-z)`: for a one-bit MUX, with

`m=min(q0+q1,2-q0-q1)`, `v=q1-q0`, `s=t-1/2`,

if `|v|<=m/224` and `|s|<=1/464`, then

`D_{Gamma^dagger}>m/400`.

The mechanism is an exact cancellation before continuity: pair the MUX Fourier masses with their leaf entropy prices to cancel every `V_j log V_j` scale term, and pair the data/output source-potential increments to cancel the common `G(log_2(2/m))` value. This replaces the inherited boundary-dependent selector tube `|s|<=m/1024` by a fixed-width tube.

In owner-requested normalized margin currency, if `P_M>0`,

`D_{Gamma^dagger}=P_M(a^dagger-c_M^{Gamma_0})`, and exact MUX influence gives `P_M<=5m/4`; hence throughout the tube

`c_M^{Gamma_0}<0.266204856`.

The completed account01/B14 balanced-gate-margin refutation is preserved: the literal base-potential AND/decomposable extremality claim is already false, with a certified balanced 18-input seed at `c_G>=0.2681828436921863...`. This handoff therefore advances the compatible lifted successor candidate and does not reopen the refuted base-potential claim.

Remaining obligation: prove `c_G^{Gamma_0}(p)<=0.268204856` for every Boolean gate and interior bias, or produce a genuine larger-margin gate/bias. The MUX residual is outside the accumulated equal/complementary/zero-credit/fixed-selector tubes.
