---
name: mlx_roll_step_holds_20_arrays_metal_stencil_kernel_5x_faster_2026_11_15
description: "[VERIFIED] MLX grid job on a Mac needs ~25x the array size in memory? A roll-and-add step keeps every temporary alive (2.45-3.15 GB at 5402^2 float32); one mx.fast.metal_kernel stencil step: same numbers, 5x faster, 1.3 GB"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T15:54:42+02:00
  status: provisional
  evidence: ""
---

15 Nov 2026, an agent, an M-series worker-machine (MLX 0.29.3). The I0001 Manhattan walk step written as rolls and adds (h=0.5p, h*E, h-h*E, four mx.roll, three adds, under mx.compile) measured a peak footprint of 3.15 GB on a 5402^2 float32 grid evaluated every second step, 2.45 GB evaluated every step: 21 to 27 full arrays, because the lazy graph keeps each temporary until eval. mx.set_cache_limit did not change it. The same step as one mx.fast.metal_kernel (each thread reads four neighbours and writes one cell; inputs p, E, F; output_shapes=[p.shape]) gave MSD equal to 2e-7 and identical return probabilities on the same seeds, 38 s instead of 198 s for 3000 steps, and peak 1.28 GB. At 8002^2, T=16000 it runs 349 s per environment at 2.56 GB. Also: the job queue admits a job only when mem_mb is under half of free+inactive+speculative+purgeable, so an over-stated header waits for hours behind another agent's resident job. How to apply: a stencil on a big grid on a Mac goes in one metal kernel, not a chain of array ops; measure the peak with /usr/bin/time -l (unified memory does not show in RSS) on a short run at full width before writing mem_mb. Script: manhattan_exact_w2.py. Related: [[i0001_manhattan_annealed_msd_slope_4_3_exact_gpu_evidence_2026_11_13]].
