---
name: replay_child_timeout_must_be_sized_from_loaded_cell_time_2026_11_13
description: "[VERIFIED] QG monotonicity shards died at exactly 2 h: the double-replay parent's child timeout (7200 s) was set when a cell took minutes; under 12-way load a cell took about 1 h, so 1 of 17 cells finished. Fix 27f6bb4 (4 days)."
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T18:22:40+02:00
  status: provisional
  evidence: ""
---

Section 9 negative-QG monotonicity production (ipm-lowerbound, branch lb/k0p05-finish) lost 2 h on 8 shards on 13 Nov: run_section9_qg_monotonicity_production.py runs each shard twice in fresh children with subprocess timeout=7_200; with 8 shards, 4 curvature cells and other agents on 16 cores, the first cell took about 1 h and the parent raised TimeoutExpired at 7200 s (rc=1, empty .partial). Fix: timeout 345_600 s (commit 27f6bb4), tests 20/20. Rule: a child timeout in a long certified replay is set from the measured per-cell wall time under the load it will really run with, times the cell count, times two; check it before launching a fleet, not after it dies. The assembler hashes the producer source at assembly time, so a timeout change only requires rerunning the shards with the new source.

Second instance, same day (18:35): the left curvature producer (run_section9_curvature_tau_left_cell.py) had timeout=3600 and cells 000/001/003 died the same way; fixed in 646096e. When one replay producer is found with a short child timeout, grep every sibling producer for timeout= before relaunching anything.
