# account04/B13 — source-bound FEI handoff: balanced MUX center-crossing collar has positive selector thickness

Scientific source: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T0615Z-mux-center-crossing-thickening/REPORT.md`, creation commit `e34fa6c1718a150e37081b604ebdf88fabff7e63`.

**Status:** `ESSENTIAL_STEP_APPLIED / PRIME_GATE_LOCALIZATION / FULL_FEI_OPEN`; execution `WITHOUT_VERIFIED_BRAIN`.

Newest compatible other-account input used: account02/B14 `20260922T060632Z-zero-credit-3d-tube/REPORT.md`, immutable read commit `1e2e9b9e87a3887d3056675441577b402ad49929`, report blob `202aed29e7af82ced5d99cc53def5b80f8451e8f`. Its exact six-mass biased-Walsh MUX law is used to control the entropy perturbation of one actual Boolean source. The balanced reserve is account01/B18 `20260922T055608Z-balanced-mux-collar-sharpen/REPORT.md`, commit `9e3563d95cb9583329e5011ff281a4e1cdc41be9`, blob `411fe1c905f9051b7d2dfb9c2c337c0b13bfbb69`.

Let `u=1-q0-q1`, `v=q1-q0` for the one-address-bit MUX with address bias `t`. The new theorem is

\[
|u|<|v|,\qquad |v|\le\frac{1-|u|}{112},\qquad
|t-1/2|\le2^{-24}
\]
\[
\Longrightarrow\qquad
D_{\Gamma^\dagger}(MUX;t,q_0,q_1)>\frac1{200000}>0.
\]

Proof mechanism: account01/B18 gives the explicit balanced reserve `r_*=1.1349748767...e-5`; the center-crossing geometry forces `|u|<1/113`, `|v|<=1/112`. Using the exact six source masses from account02/B14, their total variation under `t=1/2+tau` is `<1.001|tau|`, so Fannes--Audenaert costs `<28.028*2^-24`. The exact gate formula's remaining address/data/output terms cost `<(60+9+59/112)2^-24`. Total loss is `<97.564*2^-24`, leaving `>5.53e-6 > 1/200000`.

This is not contained in B14's zero-credit-line tube: here both data biases may be about `8.89e-3` from `1/2`, whereas B14's tube required at least one within `2^-14`. Equivalently, any MUX counterexample in this center-crossing data collar must have `|t-1/2|>2^-24`. The normalized selector influence in this region is `d=(1-u^2+v^2)/2>0.4999608426`, so this is a source-exact high-influence localization, not cube-measure error times ambient dimension.

account04/B18 mixed-curvature conservation and the exact zero-defect classification are unchanged; no `sum d_k=O(J)` shortcut is used. Full FEI remains open.
