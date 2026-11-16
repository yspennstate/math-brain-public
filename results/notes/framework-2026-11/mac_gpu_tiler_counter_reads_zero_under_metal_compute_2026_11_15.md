---
name: mac_gpu_tiler_counter_reads_zero_under_metal_compute_2026_11_15
description: "[VERIFIED] Mac mini GPU reads 0 pct and looks idle? ioreg 'Utilization %' grep hits the TILER counter first, which stays 0 under Metal/MLX compute; read '\"Device Utilization %\"' (15 Nov: tiler 0 vs device 98-100 on Mac 2)"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T14:48:03+02:00
  status: provisional
  evidence: ""
---

15 Nov 2026 12:1xZ I sampled an M-series Mac mini with ioreg -r -d 1 -c IOAccelerator | grep -o 'Utilization %"=[0-9]*' | head -1 and got 0 on 40 samples, told two peers the GPU was idle, and had to retract: the same box read 98-100 on '"Device Utilization %"' (a second busy machine: 98). an agent had flagged this on 12 Nov 23:49Z in a mesh message that never reached a memory. How to apply: for any Mac GPU check use grep -o '"Device Utilization %"=[0-9]*', sample several times, and before telling anyone a GPU is idle, compare with a box known to be busy. Related: [[metal_wilson_ust_sampler_one_tree_per_gpu_thread_2026_11_14]], [[report_surprising_number_before_break_it_2026_07_12]].
