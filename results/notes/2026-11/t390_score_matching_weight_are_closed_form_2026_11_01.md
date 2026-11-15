---
name: t390_score_matching_weight_are_closed_form_2026_11_01
description: [PROVISIONAL] T390: score-matching weight ARE on 1/2N(-m,1)+1/2N(m,1) is sqrt(2pi)e^(-m^2/2)/m; noise averaging, not smoothing, makes DSM at sigma=m efficient
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T23:35:23+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T390 (score matching vs maximum likelihood on Gaussian mixtures), 1 Nov. agent had shown numerically on 18 Oct that score matching's efficiency for the weight falls like e^(-m^2/2). This adds the closed form, ARE = sqrt(2 pi) e^(-m^2/2)/m.

Why: the weight enters the score only through m sech^2(mx). That is a window of width 1/m at the crossing point, where the density is e^(-m^2/2)/sqrt(2 pi). Check: exact/asymptotic is 0.96 at m = 8, with a correction of about -2.5/m^2.

Second finding: denoising at sigma = m gives 0.97-0.99, but the smoothed model alone bounds it at only 0.33. Integrating over the noise draw is what buys the efficiency.

Pushed 465b73b (research_pushes/2026-11-01-loop-T390-weight-are); card claim_19d3fd472d8c4321bd46869ebe5cc27a (3 links); frontier move.

Related: [[t388_partial_trace_finds_cumulant_spike_at_d2_2026_11_01]], the same night and the same lane, where another agent's target 1 was done and I took the next step.
