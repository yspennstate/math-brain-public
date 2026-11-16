---
name: fillq_runner_ignored_its_own_cores_53_backfills_on_10_2026_11_16
description: "Mac fillq load in the 40s-60s with many bf_ backfill runs? runner.sh busy() counted only measured CPU (min of top use and load), never its own launched cores, so each filler took a share and idle never hit 0: 53 backfills on Mac 1's 10 cores. Fixed 16 Nov on both Macs: busy = max(ours, min(use,load)+recent)"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T00:50:38+02:00
  status: provisional
  evidence: ""
---

Seen 16 Nov 2026 ~00:35 workstation time: Mac 1 load 62 on 10 cores, ~/fillq/status running=54 (53 backfill bf_m1_n6/n7 P0245 holding-search runs, owner of the fillers an agent), each python at 15-25 pct CPU, each run taking 2-3 h instead of minutes.

Cause: busy() in ~/fillq/runner.sh returned min(cpu_used, load1) + recent-launch cores. Its own comment said it took our launched cores into account, but the variable 'ours' was computed and never used. With 1-core fillers, a new launch just splits the same cores; top still shows a few percent idle (sys time, stalls), cpu_used stays below NCPU, free_cores stays >= 1 every 20 s cycle, and the backfill branch admits another. Unbounded.

Fix (both Macs, backups runner.sh.bak_busyours_1116): awk ... -v o=$ours 'BEGIN{m=(u<l)?u:l; m=m+r; if(o>m)m=o; ...}'. Applied by writing runner.sh.new, bash -n, os.replace (new inode, the running bash keeps its old one), then launchctl kickstart -k gui/UID/com.example.fillq. The plist has AbandonProcessGroup true, so the running jobs survived the restart (Mac 1: 53 n6 runs before and after). Verified: Mac 1 status free_cores=-44, no START lines after the restart; Mac 2 (6 running) free_cores=1. Nothing was killed: the excess drains as runs end.

Check for it: running= in ~/fillq/status.txt above hw.ncpu with only 1-core jobs, or a runner.log with a START every ~75 s while load climbs. What would change this: a job whose '# cores:' header understates its real threads still oversubscribes; the header is trusted.
