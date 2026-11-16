---
name: same_seed_different_chunk_size_different_paths_2026_11_13
description: "Two bootstrap runs with the same seed but different chunk sizes do not share paths: each chunk of B paths draws rng.random((B, m)) then rng.integers((B, m)), so the stream is consumed in a chunk-dependent order and the runs diverge after the first chunk. A gap between two such runs is sampling noise first, not floating-point rounding. Before calling two runs 'the same draws', compare one path across them."
metadata:
  type: project
  created: 2026-11-13
  status: verified
---

What happened. Two machines ran the same bootstrap simulation with the same seed, one with chunks of 2,500 paths and
one with 5,000. The gap between their means was read as float rounding between devices. A reproduction script showed
the runs shared no paths after the first chunk.

Why. Per chunk, the engine draws a (B, m) array of uniforms and then a (B, m) array of integers from one generator.
With B = 2,500 the stream goes uniforms(2,500), integers(2,500), uniforms(2,500), ...; with B = 5,000 it goes
uniforms(5,000), integers(5,000), ... The second run's first integer block is made of numbers the first run used as
uniforms. Same seed, different samples.

How large the gap was, and why. With the few paths whose value collapsed near zero removed (|arithmetic return|
above 10), the two samples agreed to 0.5 points a year at three horizons (40.2 against 40.1, 60.4 against 59.9, 55.6
against 55.1). The full means differed by up to 22 points because those few paths dominate a mean. A heavy-tailed
statistic is a poor engine check even on identical code.

How to apply.
- An engine check on "equal seeds" proves nothing unless chunk size, device and draw order also match. Compare one
  path (file, row) across the runs before claiming they are the same draws.
- For a true engine check, fix the chunk size, or replay a fixed input in order, or derive each path's draws from
  (seed, path index) with a counter-based generator (for example numpy's Philox, or a hash of seed and index as in
  the fused-kernel note), which makes the stream independent of chunking.
- Read a gap between two seeded runs as sampling noise first, and compare a robust statistic before the mean.

Related: [[fused_gpu_kernel_for_memory_bound_daily_path_simulation_2026_11_14]],
[[near_neutral_dial_is_not_a_noop_control_2026_11_16]].
