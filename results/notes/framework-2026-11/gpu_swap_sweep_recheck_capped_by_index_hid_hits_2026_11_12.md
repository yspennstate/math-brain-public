---
name: gpu_swap_sweep_recheck_capped_by_index_hid_hits_2026_11_12
description: "FEI GPU swap sweep found no hits on a beam row? Its float64 re-check took the first 50 partners by index, not the best 50, so a real hit could be skipped; sort by the float32 score before the cap. Shown 12 Nov with the undo of (590,1102)"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T14:57:10+02:00
  status: verified
  evidence: "06_math_research/frontier/fei_gpu_swap_agent/README.md"
  lesson: true
---

A float32 GPU screen followed by a float64 re-check must re-check the BEST candidates, not the first ones. The FEI
swap sweep (06_math_research/frontier/fei_gpu_swap_agent/swap_sweep.py, MLX) took
np.nonzero(R[i] > base - margin)[0][:50]: the first 50 partners by index. On the record table nothing came within the
margin, so the one-swap verdict was unaffected, but on a first-swap table every x has many near-record partners (the undo
and its copies under the gate's symmetries), and a true hit past the 50th index was never scored or written.

Control that caught it (12 Nov 14:47-14:50): table = record with (590,1102) swapped, ref unset. The undo (1102,590) must
be a hit. Index cap: best32 shows the undo, 0 hits. Partners sorted by float32 score: the hit 6.521845710923047 appears.

How to apply: any screen-then-verify search (GPU float32 then CPU float64, cheap score then exact score) needs a control
where a known winner sits among many near-ties, and the re-check sorts by the screen score before any cap. A "best32"
line that beats base while hits stays 0 is the smell. Fixed in both copies: agent's sha 21ea1c99,
fei_gpu_swap_agent/swap_torch.py (commit f10637ab8a25).

