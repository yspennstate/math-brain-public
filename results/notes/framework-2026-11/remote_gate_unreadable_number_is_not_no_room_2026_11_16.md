---
name: remote_gate_unreadable_number_is_not_no_room_2026_11_16
description: "A launch gate that waits for free memory on another machine sat idle for hours with that machine nearly empty. The number read over ssh came back on repeated lines, the shell's integer test failed on every pass, and the gate read the failure as no room. Validate the value; an unreadable number is its own outcome."
metadata:
  type: project
  created: 2026-11-16
  status: provisional
---

A gate on one machine read another machine's free memory and free disk over ssh and compared each with a floor
before starting a batch of 28 blind-reading jobs. The ssh call was wrapped in a retry, and more than one attempt
printed, so each number came back as two or three repeated lines. The test `[ "$free" -ge 18 ]` then failed with
"integer expression expected" on every pass. The gate did not stop. It treated the failed test as "not enough room
yet" and would have waited its full three hours without starting anything, while the remote machine sat idle with
23 percent of its memory free.

It was found only because the gate's log printed the number split across two lines.

The fix: take the first line only (`head -n 1`), strip everything that is not a digit, and treat an empty or
non-numeric value as a separate outcome ("could not read the machine"), logged and retried, never as "the machine
is full". The corrected gate started the jobs on its first pass.

How to apply:
- A gate that reads a number from another machine checks that it is a number before comparing it. A value it
  cannot read and a value below the floor are different outcomes and get different log lines.
- Read a gated job's first log line within a minute of starting it. A gate that prints a shell error once prints it
  on every pass.
- Do not edit a running script in place. Stop your own job by its exact process id and start a corrected copy that
  refuses to run twice (a marker file written at start).

Related: [[gist_belownormal_starvation_on_a_saturated_box_2026_11_13]] (another way a gate or job waits forever
without saying why).
