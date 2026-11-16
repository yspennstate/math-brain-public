---
name: gpu_feeder_process_must_not_sit_below_cpu_lanes_in_priority_2026_11_10
description: "Apple-silicon GPU only 59-71 percent busy on a saturated machine? The process feeding the GPU (an MPS search, a model server) ran at a lower CPU priority (nice 10-15) than the CPU-only lanes (nice 5-10). Start GPU feeders at nice 0-5; on zsh, BG_NICE silently adds 5 to every background job."
metadata:
  type: project
  created: 2026-11-10
  status: provisional
---

Measured on two Apple-silicon machines running mixed queues, 10 Nov 2026.

- Machine 1: an MPS search for open problem P0245 ran at nice 15, the CPU-only lanes for the same problem at nice 10,
  load 10.8 on 10 cores. The GPU was 59-61 percent busy, and the search slowed from about 53 to 76-80 seconds per 100
  steps over five rounds.
- Machine 2: a model server ran at nice 10, six CPU-only lanes at nice 5, load 12 on 12 cores, GPU 71 percent. There
  swapping set the pace, so priority was not the main brake.

The rule: on a saturated machine, start the process that feeds the GPU at nice 0-5 and CPU-only lanes at 10 or
higher. One core keeps the whole GPU fed; starving that core idles the most efficient compute on the machine.

Two traps found on the way:
- zsh's BG_NICE option renices every background job by +5, so a server started from a launcher that is itself
  backgrounded lands at nice 10. Use `setopt NO_BG_NICE`, or `nice -n 0` from another shell.
- Wrappers that add their own `nice -n 10` on top of an inherited nice stack silently (5 + 10 gave 15). Check
  `ps -o ni` after launch.
- On macOS a non-root user cannot lower a running process's nice, so the fix is at launch, not a renice.

Status: inferred from priority, load and the slowdown, and the BG_NICE cause was confirmed on the second machine. Not
yet tested by relaunching the GPU lane at a lower nice and timing its step; that test would settle it.
