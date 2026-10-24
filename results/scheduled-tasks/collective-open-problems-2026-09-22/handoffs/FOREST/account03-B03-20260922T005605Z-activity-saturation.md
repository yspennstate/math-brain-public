# FOREST handoff — account03/B03 activity residual boundary saturation

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T005605Z-b03-forest-r11b`  
Outcome: `AUXILIARY_ONLY / STRUCTURAL_CONSTRAINT_PROVED`  
Parent Grimmett–Winkler uniform-forest conjecture: `OPEN`.

## Exact peer consumed

Assigned other-account partner used directly:
`proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B01/b01-20260922T001208Z-forest-r11/report.md`, blob `d5faa9e572e9fa67b736693a7f1a9d5205764b3c`.
Its exact multi-bridge gluing theorem localizes the remaining source obstruction to the 3-connected case.

Also used account03/B01's exact activity/unrooting representation, scientific commit `f9f56b1817456c462e1b0c9708099eeb00b997d8`, including overlap `q` as an activity-weighted basis-exchange mass and the exact 2:1 weight ratio of the reverse exchange.

## New exact identity

Put the marked edges first in the activity order, `e<f<others`. Let `A,B,C,D` be activity-weighted spanning-tree masses for marked-edge membership `00,10,01,11`. Let `q` be the forward exchange mass from the `01` class and define

`B0 = B-2q >= 0`, `C0 = C-q >= 0`.

Then

`4 Delta_G(e,f) = (B0+2q)(C0+2q) - D(A-q)`.

Thus the source pair inequality is exactly equivalent to

`D(A-q) <= (B0+2q)(C0+2q)`.

This is a global activity compatibility coordinate; a source violation requires `A>q` and strict reversal.

## New structured constraint

For disjoint marked edges in `K_n`, symmetry reduces the exact ratio

`R_n = D(A-q)/((B0+2q)(C0+2q))`

to

`1-R_n = Delta/(Z_e-2 Z_ef)^2`.

Stark's complete-graph forest asymptotics imply

`1-R_n = n^-2 + O(n^-3)`, hence `R_n = 1-n^-2+O(n^-3)`.

Therefore **no graph-independent fixed multiplicative margin** `R<=1-epsilon` can close this exact activity formulation. Any proof must preserve sign information at the source boundary; constant-factor loss is fatal.

An exact labelled-tree checker verifies the identity, nonnegative activity residuals, and positive source gap for every `K_n`, `4<=n<=100`. The observed scaled gaps `n^2(1-R_n)` decrease toward 1 (`2.16186` at n=10, `1.48535` at 20, `1.17311` at 50, `1.08323` at 100).

## Scientific artifacts

Private scientific repository `yspennstate/math-open-problems`:

- report creation commit `245eb4f12482729fa2773f77d846e10e71314a71`, readback blob `0246ec8c670c47ed632dfc2de0b7a6fdb3f8443f`;
- checker creation commit `8313a80df9837084cbe5aa26d90fc67c3a0f4ad2`, readback blob `7e1ad633fd1d51ea2ed95e6dcf838f305a767cae`;
- output creation commit `6ec155016de63c93fcc6728e5884ae4a7fb84613`, readback blob `8a39269cb45a5308849ddf811f2076fc893b9d29`.

Executed source SHA-256: `cdc80c93275cb92d6617f630e3e84029e5658dcc4248573b192a7f9a764b69f7`.  
Captured output SHA-256: `f2b28a7db79b111d936bb02282baebabdea9b4c53fe78f3f4c7150d084eaf813`.

## Next recipient and exact obligation

Recipients: lead `account01/B01`, assigned partner `account04/B01`, and switching/activity workers.

Next exact obligation: prove the sign-exact activity residual inequality by a weight-preserving exchange/conservation mechanism coupling `D x (A minus the q-exchange reservoir)` into the two one-sided residual classes, or derive an equally sharp simultaneous-third-edge conservation law. Any proposal must regress against both this `K_n` `Theta(n^-2)` saturation and the earlier `K_{3,m}` overlap-leading-order obstruction.

No full proof, novelty claim, brain-ingestion claim, or production-state claim is made. Historical brain installation/state artifacts remain preserved but installation work is stopped by the later owner control.
