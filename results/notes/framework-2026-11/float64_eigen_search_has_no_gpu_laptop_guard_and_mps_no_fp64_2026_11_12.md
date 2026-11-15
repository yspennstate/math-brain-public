---
name: float64_eigen_search_has_no_gpu_laptop_guard_and_mps_no_fp64_2026_11_12
description: "Float64 eigen search (batched eigh) on our GPUs? Not now: the laptop guard refuses local CUDA torch runs, Mac MPS has no float64 and no eigh. Measured 12 Nov 14:30: mini 1 GPU 70-93 pct busy, mini 2 GPU 0 pct, laptop 0 pct. Float32 work to the minis; float64 eigen work on CPU."
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T14:38:38+02:00
  status: verified
  evidence: "laptop run 12 Nov 14:33-14:36 (gputest6.out), guard refusal text from compute_sense.py at 14:3x, ioreg Device Utilization sampled 5 times over 20 s on both minis"
---

Can a float64 eigenvalue search (T104's H(G), batched 6x6 eigh) use a GPU we own? Not on 12 Nov 2026.

- Laptop RTX PRO 2000: torch 2.10 cu128 works, and the batched search ran once (4,096 graphs x 400 steps per
  round, about 82,000 evaluations a second, agreeing with a direct numpy evaluation to 5e-15). The next launch was
  refused by the PreToolUse guard in compute_sense.py ("BLOCKED (local GPU safety): local CUDA/diffusers execution
  can crash this laptop"), which matches any local CUDA torch run, not only training. That guard is a deliberate
  stop; do not route around it. Only the author can open it for math.
- Mac minis: Apple MPS has no float64 and torch.linalg.eigh is not implemented on MPS, so an eigen search that
  needs 1e-10 accuracy cannot run there. A float32 screen for failures of order 1e-3 or larger would need a
  hand-written batched Jacobi solver.
- Measured 12 Nov 14:30 laptop time (the Macs' clocks read 16:30) over 20 s: mini 1 GPU 70-93 percent busy (peer jobs), mini 2 GPU 0 percent
  (86 percent RAM free; its CPU full of peer fei_bias jobs; system python3 has numpy only).

How to apply: when told to "use all the GPU", match the work to the hardware. Float32 work that fits MPS
(MLX/torch-MPS models, matrix products, Monte Carlo) goes to the minis; float64 eigen work stays on CPU. Measure
utilisation over an interval before and after, and report the numbers.
Script: 06_math_research/t104_alon_agent_2026_11_11/t104_gpu_hsearch.py.

