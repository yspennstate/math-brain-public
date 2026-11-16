---
name: t405_smoothing_gets_d2_slope_2p2_vs_3p2_2026_11_01
description: [PROVISIONAL] T405: smoothed online SGD (lam=d^1/4) finds spiked 4th cumulant in ~d^2 samples, slope 2.2 vs 3.2 plain to d 96; exact smoothed objective
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T04:47:54+04:00
  status: provisional
  evidence: ""
---



T405 smoothing (1 Nov, an agent). Pushed 1c7979e, research_pushes/2026-11-01-loop-T405-smoothing. Card claim_899ab6c92a224583a4ecd0f17a9b7df5. Frontier move 0d982440. links59 a258469 added 3 edges.

Result: the exact smoothed objective is F_lam(m) = 0.051 a^4 [m^4 + 6 lam^2 (m^2 - m^4)/(d-1) + 3 lam^4 (1-m^2)^2/(d-1)^2], checked by Monte Carlo. The step was eta = c lam^6/d^2. The mean ODE gives steps/d^2 flat in d. In the runs (16 per cell), every run escaped, and the log-log slope over d 16-96 was 2.17 / 2.20, against 3.19 for plain online SGD.

Reusable: smoothing a Hermite unit is a pure Mehler rescaling when the perpendicular norm is exactly sqrt d. All the gain comes from the |P x|^2/d fluctuation correlating with the signal.

Scar from this round: the d = 64 cell (250 d^2) looked like a log-factor trend. d = 96 fell back to 166. One median of 16 runs is scatter, so fit across all d before calling a trend.

Scar: a sed chain that renames links48 -> links59 first leaves the later message substitution with nothing to match. The links59 commit went out with the old "six edges for T330/T391" message. Put the message substitution first.

Related: [[t371_particle_error_uniform_in_time_2026_11_01]].
