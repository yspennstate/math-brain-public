---
name: swarm_keeper_quadratic_awk_stalled_mini1_codex_fleet_2026_11_16
description: "[VERIFIED] worker machine 1 Codex swarm keeper ran 0 agents for 73 min: awk s=s\"\\n\"$0 over a 66 MB codex.log is quadratic; fixed with grep -n last marker + tail -n +L"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T04:55:27+02:00
  status: provisional
  evidence: ""
---

16 Nov 2026, worker machine 1, ~/swarm1115/keeper.sh (keeper of a 30-agent Codex swarm). From 05:29 to 06:42 Mac time the keeper launched nothing, and 0 Codex agents ran. Its status.txt froze at 'running 14'. Cause: to read the log segment since the last launch marker, line 22 ran awk '/^=== launch /{s=""} {s=s"\n"$0} END{print s}'. Appending to one growing string is quadratic. AUD_HARV14's codex.log had grown to 66 MB with a single marker, so awk sat at 99% CPU for 69 minutes. The keeper.pid was alive, so a liveness check said healthy.

Fix (an agent): L=$(grep -n '^=== launch ' log | tail -1 | cut -d: -f1), then tail -n +L log piped to each grep. That took 2 s on the same file. The keeper also now skips a queue id that has neither PROMPT.md nor RESUME; keeper.out had filled with 'PROMPT.md: No such file'. The script was replaced by mv to a new inode, the stuck awk and the old keeper were killed, and the keeper was restarted with nohup. The detached workers were not touched. Backup: keeper.sh.bak_awk_3708.

Lessons:
- A keeper is alive when its status line moves, not when its pid exists.
- Any per-tick scan of a worker log must be linear and bounded: tail, not a whole-file string build.
- A Codex worker that prints tens of MB to codex.log will eventually hit any whole-file read.
