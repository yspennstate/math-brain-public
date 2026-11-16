---
name: i0001_manhattan_annealed_msd_slope_4_3_exact_gpu_evidence_2026_11_13
description: "[PROVISIONAL] Manhattan walk annealed MSD t^{4/3} (I0001)? Exact GPU evolution, 150 envs to T=2000 + 54 to T=4000: local slopes 1.30-1.34 (+-0.02-0.03) flat at 4/3; still open in print; evidence only"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T22:52:51+02:00
  status: provisional
  evidence: "agent_run/i0002n/runs/T2000.npz, local_slopes.py output 13 Nov 22:4x"
---

I0001 (Bou-Rabee and Peres, arXiv:2609.07621, Section 7 Problem 1): is the annealed mean-square displacement of the randomly oriented Manhattan walk on Z^2 of order t^{4/3}? Still open on 13 Nov 2026 (Ledger-Toth-Valko 2018 give superdiffusive bounds only; arXiv:2608.21701 is the three-dimensional lattice; t^{4/3} appears only in simulations of a crowded-lattice variant).

Numerical evidence, exact (no walker noise): manhattan_exact_torch.py evolves the full quenched distribution on a (2T+2)^2 grid on the workstation GPU (CUDA, array arithmetic, no training), one iid environment per sample; the average over environments of the exact quenched MSD IS the annealed MSD. T=2000, 96 environments, bootstrap over environments (local_slopes.py):
- MSD local slopes 1.318, 1.336, 1.317, 1.322 (+-0.02) on [125,250], [250,500], [500,1000], [1000,2000]: flat at 4/3 within one sigma, no drift; t log t would read about 1.15.
- annealed p_t(0,0) slopes -1.28, -1.30, -1.28, -1.24 (+-0.04): near -4/3 but lower and noisier; annealed return probability need not scale as 1/MSD, so this is not a contradiction.
A T=4000 run continues (about 2 environments per 7-9 minutes). Ledger row I0001 NUMERICAL_EVIDENCE, 13 Nov 22:50.

Update 13-14 Nov 23:5x (pooled_slopes.py; each dyadic window uses every environment whose run reaches it): T2000 (96 envs) + workstation T4000 (48) + worker machine 1 full-grid T4000 (6) = 150 envs: slopes 1.317, 1.317, 1.302, 1.315 (+-0.016-0.019) on [125,250]..[1000,2000], and 1.343 (+-0.029, 54 envs) on [2000,4000]. Still flat; the first four sit about one sigma below 4/3 (the windows share environments, so they are not independent). A log correction t^{4/3}(log t)^{-a} with a ~0.1 cannot be told apart from this.
Cropped windows: the walk's mass stays well inside the full grid, so manhattan_exact_torch_w.py (CUDA) and manhattan_exact_w.py (MLX) evolve a (2W+2)^2 window, with the environment drawn on the full grid and then cropped (otherwise the same seed gives a different environment), and they record the largest mass in a 64-wide edge band. At T=1000 a window of W=500 (about 4.7 rms) matches the full grid to 2e-7 and W=300 is off by 9e-4 with edge mass 9e-3, so the monitor separates good windows from bad ones. The worker machine MLX window run matches the workstation CUDA full-grid run on the same seed to 2e-7. Running: T=8000, W=3000 on the workstation GPU (runs/T8000w, 40 x 2 envs, ~5 GB VRAM) and T=4000, W=1800 on worker machine 1 (fillq 58_, 80 x 1 env).
Scar: the full-grid MLX job at T=4000 held about 10 GB of wired memory on worker machine 1 while its header said 3.5 GB (MLX unified memory does not show in RSS; read the peak footprint with /usr/bin/time -l) and it blocked a 6 GB voice queue; it was stopped and replaced by the window job. On this workstation, python -I hides the user site-packages where numpy and torch live, so the job dies at import.

Update 14 Nov 01:0x (interim, runs still going; pooled_slopes.py over T2000 96 + T4000 48 + T4000m 6 + mini1 window T4000w 40 + workstation window T8000w 24 = 214 envs): slopes 1.298, 1.304, 1.304, 1.322 (+-0.012-0.016) on [125,250]..[1000,2000], 1.352 (+-0.022, 118 envs) on [2000,4000], 1.369 (+-0.036, 24 envs) on [4000,8000]. The local slope RISES with t: early windows sit about 2 sigma below 4/3, late ones about 1 sigma above. Consistent with a slow approach to 4/3 from below (a correction to scaling) and not with t log t; an exponent above 4/3 cannot be excluded until the [4000,8000] window has ~80 envs. Code pushed: brain repo 06_math_research/probability_1000_intake_I_20260914/I0001_exact_gpu (commit 5c7a6aa8).

How to apply: this supports the conjectured exponent and says the renormalization route is aiming at the right number; it is not a result and does not go in a paper as one. More environments at T=4000 would tighten the slope to about +-0.01. Files: agent_run/i0002n/. Related: [[i0003_manhattan_paper_posted_2026_11_13]], [[i0003_manhattan_orientation_fields_recurrence_partial_two_audits_2026_11_13]], [[laptop_gpu_feeder_starves_at_belownormal_run_normal_one_thread_2026_11_13]].


Update 14 Nov 03:3x (both window runs finished; pooled_slopes.py over T2000 96 + T4000 48 + T4000m 6 + mini1 T4000w 80 + workstation T8000w 80 = 310 envs): slopes 1.304, 1.317, 1.320, 1.323 (+-0.010-0.013) on [125,250]..[1000,2000], 1.332 (+-0.015, 214 envs) on [2000,4000], 1.331 (+-0.023, 80 envs) on [4000,8000]. The 01:0x reading of 1.369 on [4000,8000] was 24 envs and came down to 1.331 at 80. The local slope rises monotonically and the last two windows sit on 4/3 = 1.3333 within 0.1 sigma: a slow approach to 4/3 from below, no sign of overshoot, and t log t (slope drifting toward 1 + 1/log t) is not what is seen. Running: workstation T8000w2 (seeds 81000+, 80 more envs, pid in runs/T8000w2.pid) to bring [4000,8000] to about +-0.016.
