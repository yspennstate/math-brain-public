---
name: cuda_job_relaunched_under_cpu_only_venv_torch_2026_11_15
description: "[VERIFIED] Laptop CUDA torch job at ~2 cpu-s, GPU 0 pct, no rows? Wrong python: venvs/picaudit and venvs/kokoro have torch 2.14.1+cpu. The CUDA build (2.10.0+cu128) is C:/Python314 from its USER site-packages, so launch it WITHOUT -s."
metadata:
  node_type: memory
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T15:57:35+02:00
  status: verified
  evidence: "P0108 c12 run, 15 Nov 2026 15:09-16:05; pid 41060 (venv, CPU torch), pid 38000 (Python314 -s, ModuleNotFoundError), pid 55812 (Python314, no -s, cuda True)"
  modified: 2026-11-15T14:31:08.495Z
---

At 15:09 on 15 Nov 2026 the P0108 c12 run was relaunched under ~/venvs/picaudit/Scripts/python.exe. The first launch had used C:/Python314. The venv's torch is 2.14.1+cpu. The process loaded torch_cpu.dll and c10.dll but never torch_cuda.dll. It used 1.86 cpu-s in 50 minutes, wrote no rows and left stderr empty. It never failed outright because the script waits for an idle GPU before it first touches CUDA. I first blamed EcoQoS and moved the throttle opt-out above the import. That did not help.

The second relaunch used C:/Python314/python.exe -s. It died at once with "No module named 'torch'". Python314's torch (2.10.0+cu128) lives in the user site, ~/AppData/Roaming/Python/Python314/site-packages, and -s hides that folder. The earlier n4096 run worked because it ran pythonw.exe without -s.

Check before you trust a laptop CUDA launch:
- run `& 'C:\Python314\python.exe' -c "import torch;print(torch.version.cuda, torch.cuda.is_available())"`; or
- confirm that torch_cuda.dll appears in (Get-Process -Id N).Modules.

The script's idle-GPU wait hides a CPU-only torch for as long as the wait lasts.

Fixed as pid 55812, launched as C:/Python314/python.exe fpp_cyl_cuda.py with no -s.

A second cause stalled pid 55812 too. It had torch_cuda.dll loaded and the GPU read 0 pct, yet it used 1.9 cpu-s in 19 minutes. Its one thread sat in the Ready state. It was launched BelowNormal on a box where every core is busy, so it was never scheduled. Raised to Normal at 16:2x: at 16:30 the GPU read 95 pct and rows were landing. A GPU feeder needs little CPU but must get the CPU it asks for. Launch it at Normal priority, never BelowNormal under a full run queue (see [[gpu_feeder_process_must_not_sit_below_cpu_lanes_in_priority_2026_11_10]]).

The rule "use -s so user site-packages cannot shadow" is wrong for this interpreter: on Python314 the user site is the only place torch is installed.
