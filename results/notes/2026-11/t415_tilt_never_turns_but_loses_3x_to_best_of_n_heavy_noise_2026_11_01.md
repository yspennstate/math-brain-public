---
name: t415_tilt_never_turns_but_loses_3x_to_best_of_n_heavy_noise_2026_11_01
description: [PROVISIONAL] T415 target 2: with independent noise the tilt pi_0 exp(lambda P) has gold = lambda exactly (no turning point) but is 3-5.5x below best-of-n at best-of-n's peak KL; it spends KL on the heavy-noise component
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T01:00:52+04:00
  status: provisional
  evidence: ""
---

Written 2026-11-01 01:00 +0400; T415 move 7b870a69, files d28aec78 (tilt.py/.txt). The tilt factorises, so G ~ N(lambda, 1) under pi_lambda. KL = lambda^2/2 + KL of the tilted noise mixture. eps 0.01 tau 5: tilt 0.588 vs best-of-n 1.770 at d 1.81, with the heavy weight under the tilt at 0.42. The curves cross during best-of-n's dip (d about 2.4) and the tilt stays ahead to n 1e7. The qualitative light-tail result is Kwa et al. 2407.14503; the gap at practical KL is ours. Related: [[t413_gaussian_ct_fixed_point_is_product_of_cosines_sqrt_d_over_eps_2026_11_01]] - same session's exactly solvable population calculations.

Related: [[t415_best_of_n_peaks_at_one_expected_noise_outlier_per_batch_2026_10_31]] - the best-of-n curve this tilt is compared against, same model.
