---
name: metal_wilson_ust_sampler_one_tree_per_gpu_thread_2026_11_14
description: "[VERIFIED] Uniform spanning trees fast? ust_metal.swift on a Mac mini GPU: Wilson's algorithm, one tree per thread, flattened phase loop; 4,800 trees/s at 160x160, ~2,000x the numba CPU sampler, law matches it (40x40, 48k vs 24k, all < 2 se)"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T20:33:56+02:00
  status: provisional
  evidence: ""
---

P0133 (12_cognitive_architecture/math/trio_1011/op/P0133/ust_metal.swift), 14 Nov 2026, an agent, Mac mini 2 (Apple M6, 16 GB).

- Build and run with no Xcode and no torch: swiftc -O ust_metal.swift -o ust_metal; the Metal source is a string compiled at run time with device.makeLibrary(source:). ./ust_metal n1 n2 s samples seed out.tsv 4096. Output lines are those of ust_torus_shear.py (classes of all fundamental cycles on the sheared torus).
- Design: one tree per GPU thread, per-thread slabs (next direction uint8, in-tree uint8, lifted x/y int32 = 10 bytes a vertex), PCG32 per thread, 2 random bits per step. The walk, the sum pass and the lift pass of Wilson's algorithm run as ONE loop with a phase variable, so a lane that finishes its loop-erased walk does not idle while the other 31 lanes of its SIMD group finish theirs.
- Measured: 48,000 trees of 40x40 in 0.4 s; 10^6 trees of 160x160 in 206 s, of 200x160 in 274 s, of 64x128 in 71 s. GPU 99 pct busy during runs (it was at 0 pct before).
- Check: 40x40 s20, 48,000 GPU samples vs 24,000 numba samples, every superbase within 2 se (top 0.71708 vs 0.71710). Compare a new kernel against the CPU sampler on the same mesh before trusting it.
- Memory: T threads x N vertices x 10 bytes (4096 x 65,536 = 2.7 GB at 256x256); size it against free unified memory first.
- Carries over to any spanning-tree / loop-erased-walk statistic (LERW lengths, CRSF homology, sandpile via burning bijection). Related: [[fused_metal_kernel_600x_daily_path_sim_memory_bound_2026_11_14]] (torch.mps.compile_shader route), [[p0133_ust_torus_superbase_law_rotation_invariant_2026_11_14]].
