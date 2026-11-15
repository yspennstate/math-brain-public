---
name: slow_probe_named_a_never_started_process_a_hung_producer_2026_11_12
description: "Slow-sense says hung_producer for hours on one pid? Check its thread: one thread Wait/Suspended, 0 ms CPU, 0 handles, no modules means it was created and never started (launcher died before resuming it). It holds nothing; the job's later runs are fine. slow_probe skips such a process since 12 Nov (_never_started) and counts it apart. Zero handles is not proof of exit."
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T00:16:48+02:00
  status: verified
  evidence: "agent_run/slow_probe_fix (make_patch.py, test_never_started.py and .txt); ledger row a of 12 Nov"
---

**What happened.** From the afternoon of 11 Nov past midnight the slowness probe reported one hung producer, pid 27804
(`publish_board.py`, created 11 Nov 15:32:32, parent gone, "it and its children produced nothing"). Every session was
handed the advisory, the prompt hook repeated the line, and a peer broadcast it to the fleet asking the publisher's
owner to look. The board publisher itself was fine: PUBLISH.log shows it publishing every fifteen minutes all evening.

**What the process was.** Measured 12 Nov 00:14 with Get-Process: one thread, state Wait, wait reason Suspended; 0 ms
of CPU; no modules loaded; 0 handles; 1.2 MB working set. Windows creates every process with its first thread
suspended and the creating process resumes it. This one's launcher died in between, so the process never ran one
instruction. It stays in the table, its byte counters are zero for ever, and "no byte moved across two probe cycles"
is true of it for as long as the machine is up. A second one sat beside it, created in the same second: pid 57720
(`claude_pool/usage_week_alert.py`), watched for 22 cycles and kept off the hung line only because its folder had
fresh files.

**The fix (slow_probe.py, 12 Nov).** `_never_started(pr)`: no CPU time at all and no handles. A process that has run
anything of its own has both, so the two zeros together are not an idle worker. hung_producers skips such a process
before the byte test and the state file counts it on its own lines (`never_started_producers`, `never_started_note`).
Controls both ways in `agent_run/slow_probe_fix/test_never_started.py`: a live sleeping child is not matched, a
child created suspended on purpose is, and on the probe's own saved state the old code names 27804 while the new code
names nothing and watches the other 14 processes exactly as before.

**The wrong turn worth keeping.** My first reading was "0 handles, so it has exited and a handle pins it" (the scar
[[win32process_presence_is_not_proof_of_life_2026_08_12]] says as much about dead processes). I wrote that fix and its
test first, and the test refuted it: GetExitCodeProcess answered STILL_ACTIVE for 27804, and an exited child whose
handle my test still held did not appear in the Toolhelp snapshot at all. The thread state was the measurement that
settled it. Zero handles has two causes that look alike in a process list: gone, or never begun.

**How to tell next time.** `Get-Process -Id <pid>` then look at `.Threads`: one thread, ThreadState Wait, WaitReason
Suspended, TotalProcessorTime 0, `.Modules` empty. Such a process holds nothing and does nothing; it is not a sign
that the job it was meant to run is stuck. Check the job's own log for later runs before telling anyone to look.

Not done: the two leftovers were left in the table (not mine). Why two launchers died in the same second is unknown.

Related: [[the_hung_producer_check_named_his_publish_waiters_2026_09_25]],
[[win32process_presence_is_not_proof_of_life_2026_08_12]].

