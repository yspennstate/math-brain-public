---
name: fleet_status_done_means_report_exists_check_pid_2026_11_08
description: "Is a Codex fleet worker finished when status.txt says done? Not always: done means REPORT.md exists; check the pid (tools/watch_done.sh)"
metadata:
  type: feedback
  created: 2026-11-08
  created_at: 2026-11-08T16:34:53+04:00
  status: verified
  evidence: "MULTI2-BUILD 8 Nov 16:34, pid 42931 alive"
---

Is a Codex fleet worker finished when status.txt says "done"? Not always. The launcher writes
"done" as soon as the worker's REPORT.md exists, and some workers write an interim REPORT.md while still running:
MULTI2-BUILD showed "done" at 16:34 on 8 Nov with pid 42931 alive and its STATUS.md still saying "finish ... audit". Also,
status.txt is only rewritten when launcher.py runs, so a watcher that greps it without running the launcher reads a stale file.

Use `watch_done.sh HH:MM W1 W2 ...` (run in the background): it runs the launcher every 2
minutes (so queued briefs start when a slot frees) and exits only when a named worker has REPORT.md AND its pid from
state.json has exited. The launcher's cap of 8 counts every codex exec on the machine, including other agents' test arms,
so a brief can sit queued while my own fleet is at 6.
Related: [[stage_push_py_pushes_whole_stage_scan_skips_placeholder_secrets_2026_11_08]] (the other fleet tool of that afternoon).

