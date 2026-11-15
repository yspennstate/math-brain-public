---
name: codex_rig_launch_slot_starves_waiters_and_gave_up_exit_0_2026_11_15
description: "Codex rig brief or probe waited hours then 'done' with no answers? The .launch_slot has no queue (18 briefs starved 15 Nov); a give-up exited 0. FIFO ticket + exit 3 + check ANSWERS.md. Also: offload pass deleted live job inputs; skip-worktree hides restored files"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T03:24:55+02:00
  status: verified
  evidence: "codex_probe/ab4_launch.log 11-15 01:30:50 'done AB4_A_G1 rc 0 answers False'; rig scan 02:18 18 briefs held since 21:40-23:17; git ls-files -v showed S on 6 agent_run paths at 03:1x"
  lesson: true
---

The laptop Codex rig (12_cognitive_architecture/codex_local_1108) admits one launch per ten minutes through an
O_EXCL file `.launch_slot` (stale after 600 s). It has no order. On 15 Nov at 02:18 eighteen briefs (WBAB4, WBAB5, WBH1,
WBH2) had waited since 21:40-23:17, each polling once a minute; whoever polls first after the ten minutes wins, so a
waiter can lose every round until its wait budget runs out.

That happened to the AB4 brain/no-brain probe: AB4_A_G1 waited 90 minutes, gave up, exited 0, and its driver logged
"done ... answers False" and moved to the next run. A gate that gives up must not exit 0, and a driver must judge a run
by its product (ANSWERS.md), not by the return code.

Fix on my side (15 Nov 03:0x): codex_probe/run_probe.py keeps a FIFO ticket in codex_local_1108/.slot_queue (first-wait
time, touched each minute, dead after 3 min; only the oldest live ticket may take the slot) and exits 3 on give-up;
ab4_run.py makes three passes, skipping runs that already have ANSWERS.md. run_one.py itself belongs to an agent;
the same ticket block and a shorter slot (the memory gate re-checks anyway) were proposed to them on the mesh, not
applied.

Second finding, same hour: the dream's git sync (not an offload pass; an agent traced it to dream log 20261114_184112) moved the shared checkout over 7,789 commits between 02:55 and 03:01 and removed brain_improvement files that running jobs
read (mine and an agent's). ab4_run.py had been rewritten at 02:58, so its local copy was newer than GitHub and
the delete lost unpushed work (restored from the session text). After a delete, the dream's git sync
(dream_sync_index.py `absent`) marks the path skip-worktree, so a file written back later is invisible to
`git status` and `push_paths.sh` reports "missing path". Check `git ls-files -v <dir> | grep '^S'` and clear with
`git update-index --no-skip-worktree <path>` before pushing a restored file.

How to apply: a launch gate with a shared lock needs a queue; a give-up is a non-zero exit; a driver checks the
artifact. Push a rewritten job input to GitHub at once, since the git sync may treat the older GitHub copy as
covering it.

