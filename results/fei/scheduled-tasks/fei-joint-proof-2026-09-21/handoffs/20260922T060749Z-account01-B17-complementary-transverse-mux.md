# account01/B17 FEI handoff — complementary transverse MUX tube

Classification: `ESSENTIAL_STEP_APPLIED`; full FEI remains OPEN / NOT PROVED. Execution: `WITHOUT_VERIFIED_BRAIN`.

Source-bound scientific report: private `yspennstate/math-open-problems`, commit `5627fc77f83837dd329a9ef7e81973b5182961eb`, path `proofnet24/P03-fei/fleet-2026-09-21/account01/B17/20260922T060749Z-complementary-transverse-mux-tube/REPORT.md`, readback blob `7a65f8fbc36f8628eb17f7d31a74d86d8e842168`.

For the live candidate `C^dagger=6.521851214`, take the balanced-address MUX in the exact B15 coordinates and start from account02/B12's proved complementary line `q0=q, q1=1-q`. Move transversely at fixed `v=1-2q` by `q0=q-u/2`, `q1=1-q-u/2`. Combining B15's exact signed-posterior reserve with B18's source-valid transformed-slope bound gives

`D_Gamma(u,1-2q) > F(q) - 56 |u|`,

where `F(q)=D_Gamma(0,1-2q)` is the exact complementary-line slack. Hence:

- if `0<q<=2^-11` and `|u|<=q/32`, then `D_Gamma > (23/20) q`;
- if `2^-11<=q<1/2` and `|u|<=min(2^-13,1-2q)`, then `D_Gamma > 9/1024`.

This is orthogonal to account04/B12's newest address-bias tube over the same complementary line. The balanced-MUX interior outside the equal-data/complementary tubes and simultaneous two-direction thickening remain open. The required half-band positive-current correction was read; no positive-current estimate is used here.