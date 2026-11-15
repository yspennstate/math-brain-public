---
name: t315_rbm_alpha_poly_by_analytic_sublevel_2026_11_01
description: [PROVISIONAL] T315: random bounded-degree RBM visible-MRF min Fourier coeff alpha >= n^-c whp (analytic sublevel sets); numerics n^-1.0..-1.35
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T02:52:10+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T315 restated target (1 Nov, an agent). Pushed e6b74ba to research-repo (research_pushes/2026-11-01-loop-T315-rbm-alpha); card claim_2e5bafa95eab4da6907a66ee3d1e4c01.

Proof pattern worth reusing for any "random parameters give a nondegenerate coefficient" claim:
1. Show the coefficient is real-analytic in boundedly many parameters and not identically zero (find its lowest Taylor term).
2. Use compactness to get a fixed-order directional derivative bounded below on finitely many boxes.
3. Apply the van der Corput sublevel lemma to get P(|c| < eps) <= C eps^beta.
4. Take a union bound to get alpha >= n^-c.

Cone mechanism: logcosh -> |v.x| kills the coefficients on sets missing a dominant index, giving c = 0.13 e^(-2 gap). That is where small alphas come from at low temperature.

Numbers: alpha ~ n^-1.01..-1.35 over n = 1e2..1e5. Open: an explicit beta, Gaussian weights, and CD.

Related: [[t298_escape_rate_width_free_digamma_offset_2026_11_01]].
