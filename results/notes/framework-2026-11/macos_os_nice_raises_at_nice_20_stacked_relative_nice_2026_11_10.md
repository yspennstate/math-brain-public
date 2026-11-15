---
name: macos_os_nice_raises_at_nice_20_stacked_relative_nice_2026_11_10
description: "[VERIFIED] No: on macOS os.nice(0) at nice 20 raises PermissionError (rc 1); relative nice -n 10 from a nice-10 parent lands at 20; set absolute priority, read with os.getpriority"
metadata:
  type: reference
  created: 2026-11-10
  created_at: 2026-11-10T00:57:59+04:00
  status: verified
  evidence: "reproduced 10 Nov 00:50-00:56 by the shell: nested nice one-liners; 6/6 launch tests fail at nice 10 for 2 relative-nice launchers, 6/6 pass for an absolute setpriority launcher"
  originSessionId: e0cb16b5-5cfd-44a6-80d7-9dc7c80f5862
---

Does a Python child that calls `os.nice(0)` survive being started at nice 20 on the Mac? No. On macOS (Darwin 24.5,
Python 3.13) `os.nice(0)` at nice 20 raises `PermissionError: [Errno 1] Operation not permitted`, so a script that
reads its own priority that way dies with exit 1 on its first line. `os.getpriority(os.PRIO_PROCESS, 0)` at the same
nice returns 20 and does not raise.

How a process gets to 20 without anyone asking: relative nice stacks. A launcher that runs `nice -n 10 <cmd>` from a
parent already at nice 10 (a governor-niced job, a nice-10 grader or driver, a launchd job with Nice 10) puts the
child at 20. Reproduce with:
`nice -n 10 /usr/bin/nice -n 10 python3 -c 'import os; os.nice(0)'` (traceback, rc 1), against
`nice -n 10 /usr/bin/nice -n 10 python3 -c 'import os; print(os.getpriority(os.PRIO_PROCESS, 0))'` (prints 20).

Measured 10 Nov 00:50-00:56: a test suite run at nice 10 failed all six worker-launch tests for the two launchers that
used relative `nice -n 10` (their stand-in CLI called os.nice(0)), and passed all six for a launcher that set absolute
priority with setpriority(..., 10). The same code at nice 0 passed everywhere, which had earlier looked like a one-off
flake.

How to apply:
- to put a child at low priority, set an absolute level (`os.setpriority(os.PRIO_PROCESS, 0, max(10, current))` in a
  preexec_fn, or `renice`), not a relative `nice -n` on top of whatever the parent has;
- to read priority, use os.getpriority, never os.nice(0);
- when a test or tool fails only under a niced runner, try it at nice 0 before calling it a flake.

Related: [[a_long_background_job_launches_at_nice_10_2026_11_07]] (the habit that puts parents at 10);
[[one_pytest_pass_is_not_a_grade_7_launch_tests_failed_once_2026_11_10]] (the failure this explains).

