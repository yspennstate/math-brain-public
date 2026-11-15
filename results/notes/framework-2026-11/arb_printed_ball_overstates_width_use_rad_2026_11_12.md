---
name: arb_printed_ball_overstates_width_use_rad_2026_11_12
description: "[VERIFIED] Box or interval width quoted in a paper from a python-flint arb printout? The printed ball rounds outward; take widths from .rad() (margin paper: 1.9e-6/1.9e-4 printed, true 1.48e-6/9.24e-5)"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T12:17:06+02:00
  status: provisional
  evidence: ""
---

status: verified. In the Ising margin paper the kappa=0.05 hull of the end boxes was quoted as 1.9e-6 in q0 and 1.9e-4 in psi0, read from str() of arb balls. str() rounds the midpoint and adds that rounding to the printed radius, so it overstates. Measured with 2*x.rad(): 1.48e-6 and 9.24e-5 (fourth audit, 12 Nov). How to apply: any width, radius or slack that goes into text comes from .rad()/.mid() or from lo/hi of the stored ball, never from the printed string. Same pass found the paper's premise slack 0.311 was really 0.292 (min over 180 slabs of the certified lo values): recompute every quoted extreme from the result files, not from memory of an older run. Fixed in ising-perceptron-margin commit 3872d41.
