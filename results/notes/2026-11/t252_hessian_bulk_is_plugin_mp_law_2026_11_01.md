---
name: t252_hessian_bulk_is_plugin_mp_law_2026_11_01
description: [PROVISIONAL] T252: ridge MLR Hessian bulk at the minimizer = matrix-MP plug-in law of fitted softmax covariances; p-z dependence invisible (quantiles 0.7 pct, d=200)
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T00:14:02+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T252 target 1 (1 Nov, an agent), pushed 874a17d to research-repo (research_pushes/2026-11-01-loop-T252-bulk-plugin-law), card claim_752bb987aade460ba5b2c0f5b6c674c5, move eec3b032.

The plug-in law is R = ((1/n) sum A_i^(1/2)(I + (d/n) A_i^(1/2) R A_i^(1/2))^(-1) A_i^(1/2) + lam - zeta)^(-1), with A_i the fitted softmax covariances on 1-perp. The 10/50/90 percent quantiles of the trained Hessian bulk, of the reference Hessian with z and fitted p, of a Hessian with fresh independent z, and of the plug-in law agree within 0.7 percent at d=200, C=4, s=3, alpha 2-16. The data dependence of p_i (the dossier's FAILURE POINT) does not show in the bulk.

Why: A_i sees z_i only through span(W, mu), which is a finite-rank perturbation. The rest is rotation-invariant given P, by strict convexity. What remains open is one Gram-matrix statement, plus the training marginal of the Loureiro et al. fixed point.

Lesson: test "does the dependence matter" by swapping in fresh independent noise (Hind) before trying to prove that it doesn't. It cost one run.

Related: [[t287_high_noise_mi_prior_free_to_s5_2026_11_01]].
