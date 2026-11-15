---
name: gist_mac_gpu_idle_is_usually_the_reading_or_the_host_2026_11_13
description: "Gist (NAP 13 Nov 2026): six memories, one story - 'the Mac GPU is idle' was the queue only once; three times it was the host loop or the ioreg line being read. Read Device Utilization, host load against core count, and the queue head before answering his standing complaint."
metadata:
  node_type: memory
  status: provisional
  tags:
    - gist
    - mac-mini
    - gpu
    - mlx
    - torch-mps
    - fillq
    - measurement
  type: project
  originSessionId: agent-6426-4bcb-9a12-82aa4cdc6a69
  modified: 2026-11-13T09:04:55.840Z
---

Six memories written in the 36 hours to 13 Nov 2026 all answer the same question - why is the Mac mini GPU not busy -
and they answer it four different ways. Only one of the four is the queue. Nobody has said that in one place, and he
keeps asking: *"make sure to use all the gpu on the computers because right now they are not being used which is a
problem"* (12-13 Nov, four times across two days), with film directive D30 behind it ("idle Mac CPU or GPU is a bug in
our queue, not a rest").

**1. The reading itself was wrong, and this one is verified.** The check everyone pasted,
`ioreg -r -d 1 -w 0 -c IOAccelerator | grep -o 'Utilization %"=[0-9]*' | head -1`, takes the TILER counter, because
ioreg prints "Tiler Utilization %" first. MLX compute kernels do not touch the tiler. On mini2 at ~01:50 on 13 Nov that
line read 0 twenty times in ten seconds while "Device Utilization %"=100 with an MLX job running. It went unnoticed for
days because on mini1 the three counters happened to agree (96/96/98). So an unknown number of "mini2 GPU at 0%"
reports - including ones that reached him - were a grep artefact [[mac_gpu_check_head1_reads_tiler_not_device_2026_11_13]].

**2. The host loop was starved, not the slot.** On mini1 (10 cores) the card read 28-49% with a GPU job running and
150+ jobs queued. The first suspect was the fillq runner's one-`# gpu: 1`-job-at-a-time rule; the actual cause was host
load 12-16 on 10 cores, so the Python loop feeding Metal never got scheduled. Fix: GPU jobs at nice 0 and keep the host
loop fed [[mac_mini_gpu_idle_is_cpu_starved_host_loop_not_slot_2026_11_13]].

**3. Half the wall was host work per step, in BOTH frameworks.** MLX: wrapping one full step in `mx.compile` (with
`mx.random.state` passed as inputs/outputs, `mx.eval` every few hundred steps rather than every step) cut user+sys from
1.71 s to 0.80 s with identical output [[mlx_compile_step_halves_host_cpu_on_starved_mac_2026_11_13]]. Torch MPS: a
mask built on the host and copied to the device inside the loop
(`torch.as_tensor(((t+1) % hint) == 0, device=mps)`) cost half the wall, and bigger batches barely helped - which is
exactly how a per-step host cost gets misdiagnosed as "launch bound, raise the batch"
[[torch_mps_host_mask_per_step_halved_pair_sim_speed_2026_11_13]].

**4. The queue failed twice, in opposite directions.** A big job at the head of fillq never started while small ones ran
past it [[fillq_big_job_starves_behind_small_jobs_2026_11_13]] - real head-of-line starvation. And the obvious
"solution" is banned for a reason: a free-running GPU loop outside fillq blocked his audiobook
[[free_running_gpu_loops_outside_fillq_blocked_owner_audiobook_2026_11_13]]. The cure for an idle GPU is never a loop
started beside the queue.

**What to do before answering "the GPUs are not being used".** In this order: (a) read *Device* Utilization, never
`head -1`; (b) compare host load to core count - above it, the GPU is waiting on Python and the fix is `mx.compile` /
a precomputed tensor / nice 0, not more jobs; (c) look at the head of fillq, not just its length; (d) queue through
fillq. Report the numbers, as D30 asks.

**The check that would break this gist:** a window where Device Utilization is genuinely low, host load is *below* core
count, and fillq has GPU jobs queued. Then the slot rule or the runner really is the cause and items 1-3 are noise. That
window has not been measured yet; items 2-4 are provisional and only item 1 is verified.

Related: [[owner_order_veo_clips_only_on_request_l4_h3_stopped_2026_11_12]]
[[gist_belownormal_starvation_on_a_saturated_box_2026_11_13]]

**A scar this may explain.** On 11 Nov at 02:00 his own Mac 2 usage report read 25% GPU after he had
been told all of it was in use - a 75-point discrepancy that was never traced to a cause. Item 1 is
now the first candidate: if that report was built from the `head -1` line (or from a sampler that
copied it), the number was the tiler and the discrepancy is instrument, not idleness. The check is
cheap and nobody has run it - find the exact command behind that report and re-read it beside
"Device Utilization %". Until then this is a lead, not an answer; the honest statement to him stays
"measured X% on host H at time T, with this command".
