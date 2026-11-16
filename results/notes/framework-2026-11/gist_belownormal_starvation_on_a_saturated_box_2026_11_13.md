---
name: gist_belownormal_starvation_on_a_saturated_box_2026_11_13
description: "Gist (SWS 13 Nov 2026): six memories, one mechanism - a BelowNormal child on this saturated workstation is the last job the box runs; watchdogs, timeouts and wall-clock reads on it measure the run queue, not the work. Raise the child by PID or opt out of EcoQoS; never a timeout that kills a writer."
metadata:
  type: project
status: verified
tags: [gist, compute, belownormal, ecoqos, task-scheduler, starvation]
---

Six memories from two windows (24-25 Sep, 12-13 Nov 2026) tell one story, and nobody had said it once.

**The mechanism.** Task Scheduler, a VBS launcher and pythonw start the job at BelowNormal, and every child inherits
the class. When the workstation's cores are full of Normal and AboveNormal work (the usual state now: about a thousand
processes, 82-87 pct CPU), a BelowNormal process gets a fraction of a percent of a core. It is not hung and not slow at
its work; it is simply never scheduled. Everything built on top of it then lies:

- a watchdog or `timeout` wrapper kills it before it has done anything ([[humanness_check_starved_at_below_normal_2026_11_13]]:
  three Mondays of "exceeded 8 min", 0-byte output, nobody watching; [[s500_music_render_starves_at_below_normal_2026_11_12]]:
  12.5 cpu-s in 20 minutes, killed mid-write, a partial flac that would have passed as finished);
- a wall-clock reading of it is a reading of the queue ([[belownormal_parent_starves_recall_cli_2026_11_13]]: 650-860 s per
  recall from the hidden parent, 5 s on the server's own row, 5.7 s from a Normal shell;
  [[the_slow_probe_was_measuring_its_own_throttle_2026_09_25]]: the slow probe's own throttle was most of its "slow");
- a lock it holds is held for as long as the box stays busy ([[transport_write_lock_held_at_below_normal_starved_two_hours_2026_11_12]]:
  1 h 55 at 0.3 pct of a core, 29 queued results refused meanwhile).

**What to do (the same move each time).** Check the priority class and CPU-seconds of the job before calling it hung or
slow. Raise the child to Normal by PID when the result is needed, or opt the process out of EcoQoS and keep the class
([[a_belownormal_render_stalls_on_ecoqos_opt_out_keeps_the_priority_2026_09_24]]: 1 picture to 17 in 15 s, same priority).
A watchdog on such a job must measure CPU-seconds consumed, not wall time, and must never kill a process that is
writing a file. The standing rule that background work runs BelowNormal so it yields to his browser is right; the error is
reading that work's timing, or its silence, as a fact about the work.

**Where it does not apply.** A box with idle cores: there BelowNormal runs at full speed and a slow job is slow for its
own reasons. And a job whose stall is EcoQoS alone speeds up with the opt-out while a job starved by the run queue needs
the class raised; the Sept measurement is the first case, the Nov ones the second.

Reflex compiled tonight: `a_belownormal_child_on_a_full_box_is_the_last_job_it_runs` (fire; controls 5 fire / 6 silent in
the same pass). Older schema it sits under: [[owner_law_no_shedding_load_we_power_through_2026_09_18]] (report, do not
kill) and [[never_starve_a_shared_computer_size_memory_before_you_queue_2026_09_06]] (the box's health is the launcher's).


Correction, same pass (04:0x): the reflex named above was NOT shipped. Its controls failed in the same pass - the two-hour-lock sentence did not fire (no verb from the list follows 'BelowNormal ... every core was busy') and a recall command quoting the words 'belownormal starvation' fired. Trigger handed forward: add held, busy and hours to the second group, and exclude lines that are a recall or grep command. The gist stands; the gut still carries only the guide.
