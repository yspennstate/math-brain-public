---
name: t298_escape_rate_width_free_digamma_offset_2026_11_01
description: [PROVISIONAL] T298: plateau escape T = log d/(2 lambda_eff), rate free of width p, p enters as 4(log(p/2)-psi(p/2)); SGD rate 1/8 - gamma c0/2
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T02:42:48+04:00
  status: provisional
  evidence: ""
---



T298 target 2 (1 Nov, an agent). Pushed 805f9df to research-repo (research_pushes/2026-11-01-loop-T298-escape-time); card claim_048e61e56c6c434585753490ddff2b9d.

Model: teacher exp(-(u.x)^2/2), a student committee of the same unit, spherical weights. Pair expectations ((1+a)(1+b)-c^2)^(-1/2) make the population flow exact at finite d, which is the trick worth reusing for any Gaussian-bump unit.

Results:
- The rate is 1/8 for every width, checked up to p = d/8.
- The width enters only through the initial chi2 draw, as the offset 4(log(p/2)-psi(p/2)) with sd 4 sqrt(psi_1(p/2)). Checked at 200 seeds.
- SGD rate: 1/8 - gamma c0/2, the sphere Ito correction. Verified at d = 6400.

Lesson: fitted T-vs-log d slopes under SGD read short. The along-u noise c_u (2.4 times c0) adds an a/d term that bends T(d) at moderate d. Measure the rate on a late window at large d instead. And a first 40-seed check against a noisy p = 256 reference looked 1.5 s.e. off; the theory baseline with 200 seeds fixed it.

Open: at gamma = 10 the escape is 1.6-2.3 longer than the moment law.

Related: [[t307_one_step_dsm_finds_hidden_line_2026_11_01]], [[t239_trained_readout_width_drops_out_2026_11_01]].
