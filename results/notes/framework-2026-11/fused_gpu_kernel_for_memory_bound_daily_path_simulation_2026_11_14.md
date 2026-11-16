---
name: fused_gpu_kernel_for_memory_bound_daily_path_simulation_2026_11_14
description: "A Monte Carlo simulation that steps many paths one day at a time ran slowly on an Apple-silicon GPU even under torch MPS, because each day's elementwise ops read and wrote the whole state from memory. One fused Metal kernel (torch.mps.compile_shader), one thread per path and setting, state in registers across all days: 48-71x faster than torch MPS and 620-890x faster than the numpy engine, outputs identical. Random draws inside the kernel and a streamed summary took it to 100 million paths."
metadata:
  type: project
  created: 2026-11-14
  status: provisional
---

The simulation: 96 parameter settings, each run over a few thousand daily steps, with a handful of state
variables per path (positions, a running value, its running peak, a few counters) updated each day from a shared
daily table and a resampled day index.

Why the torch version was slow. Each simulated day launched dozens of elementwise ops, and each op read and wrote
the full (paths x settings x state) tensor in GPU memory, once per day for every day. Making the chunks of paths
larger did not help (7,500 paths per chunk ran at 0.93x the speed of 2,500), which says launch overhead was not the
cost; memory traffic was.

The kernel. One Metal kernel, compiled at run time with `torch.mps.compile_shader`, one thread per path and
setting. Each thread keeps its state in registers for all days and reads only its day index and the small per-day
tables.

Measured cost per path, setting and day: the numpy engine on one CPU core 2.77e-7 s; torch MPS 2.4e-8 s; the fused
kernel 4.45e-10 s at 7,500 paths and 3.10e-10 s at 100,000 paths. At 7,500 paths, 0.7 s against 33.6 s, with all
96 printed cells identical.

Three follow-ups, each checked against the previous version:
1. Random draws inside the kernel. The day index moved from a numpy draw on the CPU (by then most of the run time)
   into the kernel, as a PCG hash of (seed, path, day). A numpy copy of the same hash fed to the earlier kernel gives
   bit-identical outputs, which is the right way to test it. One million paths across 24 settings: 5.7 s, about
   1.1e-10 s per path, setting and day, roughly 2,500x the numpy engine. Medians moved by 0.1 point or less against
   numpy-drawn runs.
2. A streamed summary. At ten million paths the limit became host memory for the per-path outputs, not the GPU.
   Per chunk, counts and sums are now reduced on the GPU; yearly log growth goes into a histogram with 1e-4 bins
   for the median and low percentiles; the lowest 0.2 percent of paths per setting are kept exactly for the
   extreme tail. A one-million-path control reproduced the full-array table cell for cell. One hundred million
   paths across 24 settings ran in 922 s with a peak footprint of 1.75 GB.
3. Two traps. MPS has no float64: convert reduced float32 results with `.cpu().numpy().astype(np.float64)` before
   accumulating across chunks, or the run stops with "Cannot convert a MPS Tensor to float64". And float32 changes
   the extreme value only on paths that end in failure, on the day they fail (16 of 19,200 cells, 5e-3 relative);
   surviving paths agree to 1.4e-6.

Limit of the streamed summary: the histogram is clipped at its lower edge, so a low percentile is wrong once more
than that percentage of a setting's paths fall below the edge.

How to apply: any daily-step path simulation with a few state variables per path is memory-bound under elementwise
GPU ops, and a fused kernel with register state is the fix. Compare the kernel against the old engine on the same
draws before trusting it.

Related: [[mlx_roll_step_holds_20_arrays_metal_stencil_kernel_5x_faster_2026_11_15]],
[[metal_wilson_ust_sampler_one_tree_per_gpu_thread_2026_11_14]].
