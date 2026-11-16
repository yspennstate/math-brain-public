---
name: method_feed_the_gpu_from_one_compiled_step_2026_11_13
description: "Method: a GPU idling on a loaded host is usually paying host CPU per step - measure user+sys per step, then collapse the step into one compiled/precomputed unit (MLX mx.compile with random state; torch MPS: hoist host-built tensors out of the loop). 1.71 s -> 0.80 s, identical output."
metadata:
  node_type: memory
  status: provisional
  tags:
    - method
    - gpu
    - mlx
    - torch-mps
    - mac-mini
    - profiling
  type: reference
  modified: 2026-11-13T09:08:42.159Z
---

**The move.** When a GPU reads underused and the host's load is above its core count, do not touch batch size, the
number of slots or the queue first - measure the HOST cost of one step (user+sys CPU per step), then collapse that
step's dozen small framework calls into a single compiled or precomputed unit so the device is fed from one dispatch
instead of twelve.

**Where it worked, with the number.** worker machine 1, 13 Nov 2026, MLX TASEP sweep: wrapping one full step in
`mx.compile` - `state = [mx.random.state]`, `@partial(mx.compile, inputs=state, outputs=state)`, and `mx.eval` every few
hundred steps rather than every step - cut user+sys from 1.71 s to 0.80 s per step with byte-identical output
(`agent_run/gpu_d0025/tasep_flux_c.py`). Same day, Mac 2, torch MPS vol-pair engine: one host-built mask copied to
the device inside the loop (`torch.as_tensor(((t+1) % hint) == 0, device=mps)`) was half the wall; hoisting it out
recovered that half. The diagnostic tell in both: raising the batch (chunk 1000 -> 5000) barely moved the wall. A
launch-bound job gets faster with bigger batches; a per-step host cost does not.

**Where it would not help.** A step that is already one large matmul has nothing to fuse; a bandwidth-bound kernel will
not care; and if the real cause is the *reading* (`ioreg ... | head -1` returns the Tiler counter, so compute shows 0)
or head-of-line starvation in the fillq runner, compiling the step changes nothing. Check those in the same pass -
[[gist_mac_gpu_idle_is_usually_the_reading_or_the_host_2026_11_13]].

**The one check that would break it.** Compile the step, then measure user+sys per step again on the same input. If
host CPU per step does not fall, the host was never the bottleneck and the idle belongs to the device, the queue or the
counter you are reading - stop optimizing the loop.

Related: [[mlx_compile_step_halves_host_cpu_on_starved_mac_2026_11_13]]
[[torch_mps_host_mask_per_step_halved_pair_sim_speed_2026_11_13]]
[[mac_mini_gpu_idle_is_cpu_starved_host_loop_not_slot_2026_11_13]]
