---
name: math_recall_build_reads_the_store_in_table_order_2026_11_10
description: "Math-recall prepared-state build slow (10-27 min)? Since 10 Nov 22:5x fastrecall reads the nodes in table order and sorts in Python: build 614 s -> 151 s on the same snapshot, output byte-identical; the rest of the wall is disk contention, CPU is ~96 s"
metadata:
  node_type: memory
  type: project
  created: 2026-11-10
  status: verified
  evidence: "scratch area build_equal.py: live 613.7 s, table order 150.7 s, state sha 7339f7cf.. and heavy sha c70c5452.. equal; profile_build.py with the signals sidecar: 509 s wall, 96 s CPU, read_store 327 s wall / 15 s CPU"
  modified: 2026-11-10T20:56:27.898Z
---

Measured 10 Nov 2026 22:20-22:51 workstation, an agent, on a backup-API snapshot of brain.sqlite3 (92,872 cards) with a copy of its brain.sqlite3.signals.sqlite sidecar.

Where the build's time goes: 509 s wall, 96 s CPU. read_store took 327 s wall and 15 s CPU, prefetch_signals 52 s wall and 13 s CPU, and _card_terms 30 s wall and 18 s CPU. Everything else is small. The build waits on the disk; it does not compute. This happened on a contended box: run queue 194, disk 154% busy, about 7,000 hard page-ins a second.

The change, landed 22:5x: fastrecall._read_store now calls _nodes_in_table_order(con), written by an agent on 5 Nov. It reads the nodes table in storage order and sorts by (created_at, id) in Python, instead of iter_nodes' ORDER BY over idx_nodes_created_at. The whole build came out byte-identical (state and heavy pickled sha256 equal): 613.7 s live against 150.7 s with the change. The second run was partly warm. A cold A/B of the node read alone gave 13.8-16.2 s against 23.1-27.4 s, with the same nodes sha. Backup: fastrecall.py.bak_tableorder_20261110 beside the live file.

Profiling scar from the same night: a snapshot without its .signals.sqlite sidecar recomputes every card's signals, so its profile does not show what the live build does. Copy the sidecar beside any snapshot you profile. At BelowNormal on this box a profile got 0.01 CPU-seconds per second and EcoQoS was not the cause. A build-time number taken at BelowNormal measures the box's load, not the code.

What would change this: a later build on the live store that is not faster, or a recall served from the new state that differs from one served from the old.

Related: [[recall_10x_2026_10_29]], [[brain_recall_walk_eight_steps_same_answers_2026_11_10]].

First live build on the new code: 10 Nov 22:54:44-23:01:47 (fastrecall.py replaced 22:53:24), built in 422.7 s at Normal priority (prebuild.log). Earlier live full builds on the old code: 591.6 s (9 Nov), 833.7 s (8 Nov), 213.6 s (2 Nov, a quieter box), 899-1,619 s (29 Oct). One run on a loaded box, so this is under the 10-minute target but does not show a speedup on its own: live build times swing 4x with the box load. The same-snapshot A/B above is the measurement.
