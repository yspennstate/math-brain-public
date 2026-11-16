---
name: check_no_console_test_leaves_scheduled_tasks_on_timeout_2026_11_13
description: "[VERIFIED] Running brain_graph/bin/test_check_no_console.py under a timeout? A killed run leaves its two BrainNoConsoleTest_<pid>_pos/neg scheduled tasks registered; five pairs found 13 Nov"
metadata:
  type: project
status: verified
---
test_check_no_console.py (brain-framework and math-brain-public, brain_graph/bin) registers two scheduled tasks named BrainNoConsoleTest_<pid>_pos and _neg, runs check_no_console.ps1 on each, and unregisters them in a finally block. A runner that kills it on a timeout skips the finally, so the tasks stay. They have no trigger and never fire, but they pile up: on 13 Nov there were five pairs, four from 7 Nov runs by other sessions and one from my own 300 s runner (PowerShell starts were taking 15-35 s, so the test needs far more than 300 s on a busy workstation).

**Why:** a test that touches Task Scheduler leaves system state behind whenever it is killed; nobody notices because the tasks are silent.

**How to apply:** give this test a long timeout (it starts PowerShell about seven times) or skip it on a loaded box; after any timeout, list `Get-ScheduledTask -TaskName 'BrainNoConsoleTest_*'`, remove the pair whose pid was yours (the temp folder %TEMP%\noconsole_* creation time tells which), and remove its temp folder. A fix worth making in the test: at start, unregister BrainNoConsoleTest_* tasks whose pid is no longer alive. Related: [[public_framework_trees_drifted_two_ways_56_ported_207_diverged_2026_11_13]].

Update 13 Nov 10:4x: fixed in brain-framework (uncommitted at writing, goes with the 150-file sync): the test now starts with one PowerShell call that unregisters BrainNoConsoleTest_<pid>_* tasks whose pid is no longer running. Dry run on this workstation picked exactly the four dead 7 Nov pairs. math-brain-public still has the old test.
