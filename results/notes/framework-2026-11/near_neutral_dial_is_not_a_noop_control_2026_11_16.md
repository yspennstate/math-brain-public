---
name: near_neutral_dial_is_not_a_noop_control_2026_11_16
description: "An acceptance test of the form 'set the new dial a hair off neutral and the result must not move' is not a valid control when the dial triggers an event, such as rebalancing a position to a target: the trigger is a step, so a change of a thousandth can move the result a lot. Build the no-op control from structure instead (a run without the affected component, a window without the event), and keep the both-ways pair."
metadata:
  type: project
  created: 2026-11-16
  status: provisional
---

The setting. A switch was added to a GPU simulation kernel so that when a multiplier changed, only one component
was rebalanced to its new target instead of every component being re-sized. The acceptance test written with it
said: with the multiplier at 0.999 and the switch on, the output must equal the run with the multiplier at 1.0,
because a change of a thousandth is nothing.

Why the test is wrong. The multiplier does not enter the computation continuously. Any change in it, however small,
fires an event (a rebalance to target), and from that point the two runs follow different paths. The test compared a
path with the event against a path without it and failed for a reason unrelated to the fix.

The right control (proposed by a peer reviewing the kernel). Run the switch on a configuration that does not hold
the component being rebalanced. There the switch must be an exact no-op with the fix, and the old behaviour must show
without it: with the switch on, the output equalled the plain run row for row; with it off, the old re-size appeared.
That test fails without the fix and passes by construction with it.

Rules for the next kernel switch:
- A dial "near neutral" is a no-op only if the code path is continuous in the dial. An event-triggered action is
  not: the trigger is a step function of the dial.
- Build the no-op control from structure, not from a small number.
- Keep the both-ways pair: identical outputs with the switch off (all 32 output arrays matched the previous kernel),
  and a difference in the one place the fix should bite.
- When accepting a kernel, read every place that sets the event flag, not only the lines the change touched. The
  previous kernel had been accepted without reading what the flag did to the other components, and a peer found it.

Related: [[fused_gpu_kernel_for_memory_bound_daily_path_simulation_2026_11_14]],
[[same_seed_different_chunk_size_different_paths_2026_11_13]].
