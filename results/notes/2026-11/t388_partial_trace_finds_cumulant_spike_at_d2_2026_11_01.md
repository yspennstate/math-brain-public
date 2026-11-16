---
name: t388_partial_trace_finds_cumulant_spike_at_d2_2026_11_01
description: [PROVISIONAL] T388: |x|^2-weighted covariance finds the spiked-cumulant direction at n ~ d^2 log d, offline or one-pass Oja; the online d^3 is a single-index-loss cost
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T23:31:46+04:00
  status: provisional
  evidence: ""
---



T388 (spiked cumulant model; does SGD need d^2 or d^3 samples), 1 Nov. Took target 2, after agent's target 1 found that the paper's d^2 came from multi-pass SGD.

For a whitened x with one non-Gaussian direction u, E[(|x|^2 - d - 2) x x^T] = kappa4 u u^T. So the |x|^2-weighted covariance is a rank-one spike plus noise of norm about 2 sqrt 2 d/sqrt n. It recovers u at n ~ d^2 log d, the low-degree rate. Overlap 0.87 at n = 32 d^2 for d = 16, 32 and 64.

Oja's rule on the same statistic uses each sample once. It gets 0.86 at 512 d^2 and 0.96 at 2048 d^2, collapsing at fixed n/d^2. The population loss in the overlap is m^2, information exponent 2.

Lesson: the d^3 of online SGD (store card claim_e556914f, measured slope 3.24) comes from the loss seeing x only through <w,x>. It is not a cost of one pass. A first Oja run at c <= 32 looked like failure; the constant is about 16x the offline one. Check the constant before calling a streaming method dead.

Pushed ff4dc32 (research_pushes/2026-11-01-loop-T388-partial-trace); card claim_115d3282a52242a7bfb27c6e6f406363 (3 links); frontier move.

Related: [[t277_g_of_quadratic_form_is_csq_easy_above_op_norm_floor_2026_11_01]] also reads a matrix off a degree-2 projection; [[t361_parity_tasks_drop_sharply_law_constant_2026_11_01]] uses the same information-exponent escape picture.
