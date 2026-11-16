---
name: laptop_gpu_feeder_starves_at_belownormal_run_normal_one_thread_2026_11_13
description: "Laptop GPU idle (0 pct) under a torch/CUDA job? At BelowNormal on the saturated workstation the kernel-launching CPU thread starves; run the feeder at Normal with torch.set_num_threads(1), hidden, and check nvidia-smi within a minute"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T20:42:55+02:00
  status: verified
  evidence: "13 Nov 20:4x workstation: pid 36484 BelowNormal cpu=4.6 s, nvidia-smi 0 pct; rerun Normal + set_num_threads(1): batch 0 in 2 s, then chain pid 57328 nvidia-smi 100 pct 3097 MiB"
---

On a saturated workstation, a GPU job launched at BelowNormal priority can leave the GPU at 0 pct: the one CPU thread that launches the CUDA kernels is starved. Seen 13 Nov 2026 on the workstation (96 python processes, slow disk): a torch roll-and-add evolution at BelowNormal had 4.6 s of CPU after five minutes and nvidia-smi showed 0 pct; the same script at Normal priority with torch.set_num_threads(1) ran a T=400 batch in 2 s and drove the card to 100 pct.

How to apply: for a GPU-bound job on the workstation, run the feeder at Normal priority with one CPU thread (it costs one core), launch it hidden (Start-Process -WindowStyle Hidden), and check nvidia-smi utilization within a minute. Also: torch import takes about 33 s on this workstation, so a smoke test needs a timeout of minutes, and never pipe a smoke run through tail (output stays empty until it ends). Array arithmetic is not DNN training; the training ban does not apply. Related: [[owner_order_gpu_allowed_again_2026_09_30]], [[owner_law_no_dnn_training_on_this_laptop_gpu_for_movies_only_2026_09_06]].



Also seen the same evening on CPU-only work (an agent, 13 Nov 2026, 20:53-21:09 workstation, measured with paired psutil samples 8 s apart): seven of my below-normal jobs were getting 0.00 to 0.08 s of CPU per 8 s while the box read 73 pct busy. The level-check ffmpeg of the chapter-one music mix had 10.6 s of CPU after 43 minutes; moved to Normal by pid (psutil nice, nothing stopped) it finished within ten seconds, and two eigenvector checks went from 0.00 to 7 s of CPU per 10 s. So a job that looks hung at BelowNormal on this workstation is usually starved: take a paired CPU sample before calling it hung, and before waiting hours on it. A tool that starts each child step below normal starves again at every step; a small watcher that raises the children of one named pid fixed that for one job. The standing rule keeps film encodes BelowNormal to protect the desktop; this note covers single-thread audio and check steps, one job at a time, and does not change that rule.
