---
name: t415_reward_model_size_moves_peak_earlier_unless_eps_shrinks_2026_11_01
description: [PROVISIONAL] T415 target 3: estimation noise c/m alone moves best-of-n peak earlier (n* 120 to 63) and saturates; only eps(m) shrinking moves it later, n* eps sqrt(log n*) ~ 1
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T01:46:02+04:00
  status: provisional
  evidence: ""
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T415 target 3, move b0f41a32, files 02c89bb4 (rmsize.py, rmsize.txt). Model: G ~ N(0,1), P = G + N, N ~ (1-eps) N(0, c/m) + eps N(0, tau^2 + c/m), with c 25 and tau 5. At fixed eps 0.01, peak gold rises 1.16 to 1.95 with m, but n* falls 120 to 63 and saturates by m ~ 300: a noisier light part hides outliers longer. Gaussian estimation noise alone never turns. With eps = eps0 (m0/m)^a: n* ~ m^0.935 (a 1) and m^0.46 (a 1/2); n* eps sqrt(log n*) = 0.97-1.07 for eps <= 3.3e-4; KL at peak ~ a log m. eps(m) is assumed, not derived. Open: derive eps(m) from a fitted misspecified model.
Related: [[t415_best_of_n_peaks_at_one_expected_noise_outlier_per_batch_2026_10_31]] - target 1 model and n* eps ~ 1 that this refines
Related: [[t415_tilt_never_turns_but_loses_3x_to_best_of_n_heavy_noise_2026_11_01]] - target 2 of the same row

Update 2026-11-01 01:50: move debd4222 (files 793edfdc). Rare-feature mechanism: heavy error variance ch/m at fixed eps gives log n* = (m + ch)/(ch - c) log(1/eps), measured n* 52 to 14454 over m 1-100 (slope 0.055 vs 0.047 per unit m), so KL* grows linearly in m. But the dip shrinks and from m ~ 30 gold recovers above the peak by n = 1e9: transient overoptimization. At m 300 there is no local max below 1e9. The turn detector is now the first local max; the earlier sweep is unchanged (22/22 n*).

Update 2026-11-01 01:55: move c22ccedb (files d1c9210a). Any dip needs tau > tau_c, tau_c^2 = C/(2 ln(1/eps)), C about 4.6 (tau_c 0.70-0.72 at eps 0.01, 0.56-0.58 at 0.001). The dip shrinks continuously to 0 at tau_c. The rare-feature model loses overoptimization at m_c = ch/tau_c^2, about 200 (dip at m 180, none at 220).

Update 2026-11-01 01:59: move 96fe8821. With precise tails (log1p of survival, grid to 1e24), tau_c is (0.71,0.72), (0.57,0.58), (0.52,0.53) at eps 1e-2, 1e-3, 1e-4, so C = 2 tau_c^2 ln(1/eps) = 4.64-4.77, 4.49-4.65, 4.98-5.17. The ln(1/eps) law is approximate (C 4.5-5.2), not exact. Watch: past n ~ 1e13 log(cdf) loses its digits in double precision; use log1p(-sf).
