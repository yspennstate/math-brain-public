---
name: mlx_compile_step_halves_host_cpu_on_starved_mac_2026_11_13
description: "[VERIFIED] worker-machine GPU idle because the host CPU is starved? Compile the MLX step: mx.compile with random state halved host CPU (1.71 s -> 0.80 s user+sys), identical output."
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T09:48:50+02:00
  status: provisional
  evidence: ""
---

status: verified (one benchmark, 13 Nov, worker machine 1 at load 16-18)
On a CPU-starved Mac (load above core count) an MLX simulation loop leaves the GPU waiting on Python: each step dispatches a dozen small ops. Wrapping one full step in mx.compile cut user+sys CPU from 1.71 s to 0.80 s for the D0025 TASEP loop (n=4096, 74 rings, 2000 sweeps); J values identical to 4 decimals. Wall time was slightly longer on the short test (compile cost), which amortises on long runs.
How: state = [mx.random.state]; @partial(mx.compile, inputs=state, outputs=state) def sweep(X): ... ; call mx.eval every few hundred steps, not every step. Random ops inside a compiled function need the state passed this way or every call repeats the same draws.
Code: agent_run/gpu_d0025/tasep_flux_c.py (copy on mini1 ~/gpu_work/d0025_tasep/).
Related: [[mac_mini_gpu_idle_is_cpu_starved_host_loop_not_slot_2026_11_13]] [[torch_mps_host_mask_per_step_halved_pair_sim_speed_2026_11_13]]
