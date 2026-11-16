---
name: hung_producer_check_missed_cpu_bound_subtrees_2026_11_14
description: "[VERIFIED] slow-sense 'N orphaned producers wrote nothing' counted a CPU-busy subtree as hung: run_fv_tf.py's 4 children burned 28.7 CPU-s/20 s with zero I/O. Since 14 Nov the probe carries subtree CPU; still grows only when bytes AND CPU stand still"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T02:15:06+02:00
  status: provisional
  evidence: ""
---

slow_probe.hung_producers judged an orphaned producer only by the bytes its subtree read and wrote. A numerical sweep writes nothing until it finishes, so run_fv_tf.py (pid 15048, session agent, ipm-lowerbound function-value shards) was named hung for five cycles while its four python children used about 1.4 cores. Fix (14 Nov 2026, an agent, live md5 0067d849): the watch row carries subtree CPU seconds; the silent-cycle count grows only when the byte total is unchanged AND CPU moved under 5 s between probes (_CPU_IDLE_S). Old 3-field rows fall back to bytes. Live two-pass test: 15048 went 6 -> 0; the six idle orphans stayed counted. Selftest passes.

Of the six still counted that night, pid 38004 (run_bneg_shards.py) is a real dead waiter: it polls ipm-lowerbound/runlogs/fv_all.done every 30 s, its owner wrote fv_1415.done instead, and the 8 bneg v3 shards it would run were produced by another runner. Harmless if it ever wakes (each shard exists, it would skip). Not killed: no agent stops others' work (18 Sep law); reported.

How to apply: before calling an orphan hung, measure subtree CPU over 20 s (scratch hung_cpu_check.py pattern), not just bytes. Ledger row an agent-20261114-hung-producer-cpu-aware. Related: [[slow_probe_named_a_never_started_process_a_hung_producer_2026_11_12]], [[compaction_sweep_reparsed_index_per_node_starved_holding_lock_2026_11_14]].
