---
name: t405_halving_step_needs_no_beta_warm_start_2026_11_01
description: [VERIFIED] T405 unknown beta: halving step, epochs K/(eta^2 g2), 0.41-1.08x tuned at d=32; too-large steps hold m^2=1/(d(1-2eta*/eta)), a warm start
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T11:32:49+04:00
  status: provisional
  evidence: ""
---



Pushed cb5c845 (note), card claim_1dce8ad94c5f448fb7234b12eac09464 export fdc2fcf, move 8171e78d. Follows [[t405_tuned_escape_scales_as_inv_kappa4_sq_2026_11_01]].

- I predicted 1.5-7x the tuned cost, with too-large steps leaving |m| at the fresh-start level. Both were wrong, in the favourable direction.
- The mean ODE for m drops the Ito term. On the sphere the noise is neutral at m ~ 1/sqrt d, so a too-large step is a warm start, not a pull toward 0.
- The same omission makes the ODE overstate the tuned stochastic time by 1.1-2x.

**Why:** this closes the T405 unknown-beta item.

**How to apply:** before predicting that a large step hurts in a mean-ODE model on the sphere, add the Ito term. The equilibrium m^2 = 1/(d(1-2eta*/eta)) matched the epoch-end medians to 10-25 percent.

Update 1 Nov 12:32, d = 64 (pushed 4ab513d, move a59f04df): schedule/tuned 1.46/0.91/0.74/0.92 at beta 0.75/1/1.5/2, all 16 rows escape. The d = 32 factor-2 wins do not repeat; the schedule costs about the tuned step (0.7-1.5x). At beta 0.75 the first epoch under 2 eta* sits at 1.91 eta* (rate 0.17 of best). Equilibrium median 0.674/sqrt(d(1-2eta*/eta)) fits 6 of 7 epochs within 16-row noise (~30%).

Update 1 Nov 13:43: the doubling schedule never doubles (epoch 0 growth K(1/x - 1/2) > L), so it is the fixed small step and costs n_opt/(2x - x^2); measured at d = 32, beta 1 and 2, x = 1/4 and 1/8: 2.01-4.14 n_opt, all rows escape in epoch 0 (f2d74e9, research_pushes/2026-11-01-loop-T405-doubling). Unbounded in beta, so start high and halve.

Folders on research-repo: research_pushes/2026-11-01-loop-T405-unknown (the halving schedule, d = 32 and d = 64: T405_unknown.md, t405_unknown.py) and research_pushes/2026-11-01-loop-T405-doubling (the doubling follow-up).
