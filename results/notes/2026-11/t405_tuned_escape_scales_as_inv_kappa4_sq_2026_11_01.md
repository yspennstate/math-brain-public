---
name: t405_tuned_escape_scales_as_inv_kappa4_sq_2026_11_01
description: [VERIFIED] T405: step scaled by |kappa4(beta)| makes smoothed SGD escape an exact time change, T(1)(1+beta^2)^4/(16 beta^8); gain same at every beta
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T09:50:04+04:00
  status: provisional
  evidence: ""
---



Pushed 7f626fe, move 3377ead9. Follows [[t405_switch_smoothing_off_at_escape_2026_11_01]].

- The drift scales with |kappa4|. The noise pull comes from null samples and does not.
- With eta = |kappa4| eta prime, the mean ODE (and its diffusion limit) is kappa4^2 times a beta-free ODE.
- Check: best steps x kappa4^2 stays at 29.8-29.9 (d=32) and 33.6-33.9 (d=64) for beta 0.5-4.
- Halving beta from 1 costs 39x more steps.
- A step tuned for one beta fails once |kappa4| drops below half its tuned value.

**Why:** this closes the T405 beta item. It is an identity, not a fit.

**How to apply:** when a parameter only scales the signal, look for the time change before running a sweep. A fixed-step Euler ODE scan of slow cases took far too long, while quadrature over m is instant.

Folder: research-repo research_pushes/2026-11-01-loop-T405-beta
