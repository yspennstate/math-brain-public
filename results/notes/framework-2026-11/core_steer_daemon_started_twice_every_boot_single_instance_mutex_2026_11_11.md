---
name: core_steer_daemon_started_twice_every_boot_single_instance_mutex_2026_11_11
description: "core_steer.py running twice (dead parents, double sweeps)? It started twice at each of three boots (two logon launchers); since 11 Nov 01:15 a named mutex makes the second copy exit at once (10/10 controls). Running old copies stay until reboot; core_steer_selftest.py fails 2 checks, unread"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T01:17:16+02:00
  status: verified
  evidence: "brain_improvement/agent_run/core_steer_single/landed_20261111 (test.txt, test_live.txt, selftest.txt); compute/core_steer.log start lines"
---

Since 11 Nov 2026 01:15 (workstation clock) `core_steer.py` (sha256 e84a3adb808d9cc3) refuses to run
as a second daemon: `single_instance()` takes a named mutex at the top of `main()`, and a copy that finds it held
writes one log line and returns before it loads masks or sweeps anything.

**The failure it closes.** `compute/core_steer.log` shows the daemon starting twice at each of the last three boots:
18 Oct 00:56 and 00:58, 2 Nov 08:56 and 08:57, 10 Nov 16:36 and 16:38. Two launchers fire at logon a minute or two
apart and nothing noticed the first copy. Both copies then swept every process every five seconds and wrote the
same pins and the same state file (83 and 339 cpu-seconds by the evening of 10 Nov, both with dead parents). A peer
(an agent) saw them during a ui_freeze on 10 Nov 22:5x.

**Why a mutex.** The kernel releases a named mutex when its holder dies, however it dies, so there is no lock file
to go stale. `--restore` is not guarded (a one-shot run while the daemon is up). If the mutex cannot be created the
daemon runs, so a failed check never leaves the box without one. `CORE_STEER_MUTEX` names another mutex for tests.

**Controls** (`brain_improvement/agent_run/core_steer_single/test_single.py`, 10 of 10, on the copy and again on
the live file): the old file has no guard; a second process is refused while the first lives; after the holder
exits, and after it is killed hard, the next start is the daemon; another mutex name is independent; `main()` of a
second copy returns at once with one log line and no sweep; removing the guard gives back the old file byte for byte.

**What it does not change.** The two copies started on 10 Nov carry the old code and keep running until the next
boot (not stopped: the standing no-shedding rule). The guard acts from the next start. Which two launchers start it at logon
is not identified; with the guard the second one is harmless, but one of them is redundant.

**Found beside it, not fixed.** `core_steer_selftest.py` fails 2 of its checks on the live file, before and after
this change with identical output: "the user's apps are NOT dragged into a render pool" and "post-bridge pools renders
ONLY (agents and apps left alone)" (classified []). Either the test is stale against the daemon's current pools or
the classification regressed; nobody had run it.

Rollback: copy `core_steer.py.bak_single_20261111` over `core_steer.py`.

