---
name: process_ready_at_belownormal_is_starved_not_hung_brain_midx_hourly_2026_11_11
description: "Process shows no CPU for hours, looks hung? Read its thread state: Ready at BelowNormal is starved, raise it by PID. Brain clone repack sat 10 h; hourly index task BrainMidxHourly; fetch 62 s -> 11 s."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T08:04:11+02:00
  status: verified
  evidence: "scratchpad after_repack.txt 11 Nov 07:57-07:58 (midx write 11 s, fetch 11 s, rev-list rc 0); brain_repack_small.log rc=0 in 608.1 min; flash_check 833 samples at 36 ms, 0 windows"
  lesson: true
---

A process that shows no CPU for hours on the laptop is not always hung. Read its thread state before anything else:

    (Get-Process -Id N).Threads | Select-Object ThreadState, WaitReason ; (Get-Process -Id N).PriorityClass

`Wait` with a reason means it is blocked on something (a lock, a pipe, a prompt). `Ready` means it wants the CPU and is not getting it. `Ready` at BelowNormal on a loaded box is starvation, and the fix is to raise the priority by PID, not to kill it and not to delete its lock.

What happened (10-11 Nov, brain clone brain-repo, git 2.53.0.windows.2). My small-pack rollup (brain_repack_small.ps1: pin every pack of 1 MB or more with a .keep, then `git -c pack.threads=2 repack --geometric=2 -d --write-midx`) started 10 Nov 21:42. The script set itself BelowNormal and every git child inherited it. At 07:37 the next morning the repack's index writer had used 24 s of CPU in 3.7 hours; its one thread was Ready; laptop CPU load was 76 pct. A peer had read it as waiting on a y/n prompt (Git for Windows only asks when stdin and stderr are both terminals; GIT_ASK_YESNO=false makes it fail instead). At 07:38 I set the three git processes to Normal by PID. The index writer finished in under 25 s and the rest of the repack in 18 minutes (rc 0 after 608 minutes in all).

Result. Packs 8,216 -> 3,958 (613 under 1 MB left, all fetched during the run). `git --no-lazy-fetch rev-list --objects --exclude-promisor-objects --max-count=20 --all` clean. A plain `git multi-pack-index write` over all 3,963 packs took 11 s. `git fetch origin main` took 11 s; the peer had measured 62 s at 07:35 with about 600 packs outside the index.

Why the index goes stale. Every fetch leaves one new promisor pack, 90 to 130 an hour on these days, and a pack outside the multi-pack-index is searched one by one on every object lookup ([[brain_checkout_4761_promisor_packs_multi_pack_index_cuts_lookup_5x_2026_11_05]]). The dream refreshes the index (run_dream.ps1, when 20 or more packs are newer), but only when it runs: its 01:31 refresh found 791 newer packs (16 s), and six hours later 600 were outside again.

The fix, live since 08:00 on 11 Nov: scheduled task BrainMidxHourly (hourly at :23, `wscript //B ~/.claude/dreaming/brain_midx_hourly.vbs` -> brain_midx_hourly.ps1, task priority 4). It writes the index only (no object moves, no pack deleted) through run_bounded.py with a 600 s cap at Normal priority, skips when fewer than 20 packs are newer or when multi-pack-index.lock exists, and logs STALE-LOCK when the lock is two hours old. Log ~/.claude/dreaming/brain_midx_hourly.log; stop file ~/.claude/dreaming/brain_midx_hourly.STOP. Two hand runs: no console window in 833 samples at 36 ms.

How to apply.
- A job that holds a lock other jobs need (multi-pack-index.lock, index.lock, dream.lock) does not run at BelowNormal on this laptop. Set the lock-holding step to Normal, or it can sit on the lock for hours ([[run_bounded_restores_io_priority_for_owner_present_scheduled_jobs_2026_11_11]] is the same family: the cap and the priority belong to the job that holds the lock).
- Before calling a process hung: thread state, priority class, CPU seconds twice a few seconds apart.
- Not done: about 3,350 packs of 1 MB or more remain (31 GB); rolling those up rewrites the whole store and was not attempted. 23 tmp_pack files from killed fetches are still in the pack folder ([[board_publish_fetch_timeouts_and_tmp_packs_2026_11_08]]).

