---
name: core_steer_selftest_runs_in_hook_liveness_and_the_second_start_2026_11_11
description: "core_steer_selftest.py run by anything? Yes since 11 Nov: hook_liveness SELFTESTS runs it with and without -s and a failure reaches the wake. The second start at boot is the same launcher run twice (runner unreadable: scheduler log off); harmless since the mutex"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T02:25:56+02:00
  status: verified
  evidence: "brain_improvement/agent_run/selftest_schedule/; ledger_rows_20261111_c.jsonl"
---

Two loose ends of [[core_steer_daemon_started_twice_every_boot_single_instance_mutex_2026_11_11]] and
[[core_steer_selftest_two_failures_stale_check_and_silent_no_psutil_2026_11_11]], closed 11 Nov 2026 about 02:20.

**The selftest is now run by something.** `hook_liveness.py` (sha 0d2e4a3513a13cea) has a list `SELFTESTS` and a
runner `_run_selftests()`. Each listed script runs as a windowless child under each listed interpreter flag set;
`core_steer_selftest.py` is listed with and without `-s`, because its second failure showed only without the user
site. A failure is added to `_artifact_bad`, so it lands in `.liveness_status.json` and in the wake line every
session reads. A run that does not finish in 120 s is printed as a note and not raised: a starved box is not a
failed test. `HOOK_LIVENESS_SELFTESTS=0` skips the section.

Controls: 17 of 17 on the copy and on the live file, the old file fails the first; with the daemon as it was
before the fix beside today's selftest, the runner raises "without psutil a named encoder is still a render" under
both runs and the post-bridge check under `-s`; a full live run prints two ok rows and adds nothing to the status
file. Rollback: `hook_liveness.py.bak_selftests_20261111`.

**To add another selftest:** append `("name_selftest.py", [[]])` to `SELFTESTS`, but only if it touches no live
state and finishes in seconds. Still run by nothing: slow_sense_selftest.py (passes by hand, 4 s),
bm25_lane_selftest.py, graph_lane_ties_selftest.py, math_answer_closure_selftest.py,
graph_fire/owner_convention_selftest.py. Time each on a quiet box before listing it.

**The second start at every boot is the same launcher, run twice.** Both live copies have the launcher's exact
command line (`pythonw.exe -X utf8 ...core_steer.py`, cwd the home folder), both in session 1, started 115 s apart
on 10 Nov (143 s on 18 Oct, 58 s on 2 Nov), and neither at the logon instant (shell 16:33:12, starts 16:36:08 and
16:38:03). Ruled out by reading: no scheduled task names core_steer or the Startup folder (535 rows, and no logon
task's script mentions it); HKCU and HKLM Run, RunOnce, the WOW6432 Run key, the Policies Run keys and the
`Windows` load/run values hold nothing; the user Startup folder has one copy and the all-users folder none; the
shell started once; core_steer.py never spawns itself. What runs the launcher the second time cannot be read after
the fact, because the Task Scheduler operational log is disabled on this workstation. It no longer matters for the
daemon: the mutex is `Local\`, both copies are in one session, so the second exits at once. If someone wants the
answer, the cheap instrument is a line in the launcher that logs `WScript.ScriptFullName` at the next boot; I did
not edit a logon launcher for a question whose answer changes nothing.

**How to apply.** A selftest that no schedule runs is a file, not a test: when you write one, list it where the
wake will see its failure. And a "second launcher" may be one launcher run twice; compare command lines before
hunting for a second file.

