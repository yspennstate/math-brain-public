---
name: a_driver_with_no_spread_across_sites_blew_up_a_linear_emulator_2026_11_08
description: "[VERIFIED] IEEE CarbonGlobe 8 Nov: test sites have no train twins; a climate ridge cut warm-holdout MSE 0.103->0.0745 but test drivers sat 30-49 sd out, test means 0.88 vs gbm 1.06"
metadata:
  type: project
  created: 2026-11-07
  created_at: 2026-11-07T21:36:37-05:00
  status: provisional
  evidence: ""
---

ie-twin v1: nearest train site to each test site at L2 0.81 (median 1.40) on the scaled 15-age year-0 curve, against a train-to-other-train median of 0.25; zero test sites under 1e-2. So no copy-the-twin shortcut. ie-clim v1: ridge per seed age on the age curve plus each of 136 drivers' 40-year mean and last10-minus-first10 trend (z-scored on train). Random-site holdout 0.0691 vs curve-only 0.1003; warm holdout (top 20% warming) 0.0745 vs 0.103. Climate inputs help about 28% under shift. But the trend features of drivers 11-23 sat at |z| 30-49 in the test files: features with almost no spread across training sites (likely global forcing shared by every site) get a tiny sd, so any test difference becomes a giant z and a linear model extrapolates into nonsense (test means h/agb 0.88/0.66 vs gbm 1.06/0.99). Lesson: before z-scoring drivers for a shifted test, drop the ones with no cross-site spread (their effect cannot be learned from cross-site variation at all) and clip test to the train range. A ridge is also far weaker in-distribution (0.069 vs the gbm's 0.024). v2 (kernels/ie-clim) drops and clips and judges ridge vs LightGBM on the same warm split. Related: [[a_present_climate_age_curve_ran_low_so_only_its_pattern_helped_2026_11_08]], [[scar_extrapolation_past_measured_range_2026_07_08]].
