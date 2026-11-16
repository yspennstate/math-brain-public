---
name: g0013_r10_cap_10_11_interval_proof_closes_all_711168_orbits_2026_11_10
description: "[PROVISIONAL] G0013 r10 full interval run (40 shards, 10 Nov): partition 22222 closes all 711,168 ten-value block orbits at mass cap 10/11, 0 failed, smallest lower bound +2.51e-6 at tau 5967438210; release g0013-r10-2026-11-09 asset g0013_r10_iv_full.tar.gz sha256 08b8807a"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T05:32:02+02:00
  status: provisional
  evidence: ""
---

Finished 10 Nov 07:10 Mac clock on a second machine (run_shards.sh, five workers x eight shards, nice 15). r10_iv_combine.py over shard_*_of_40.jsonl: 40 files, 711,168 rows, 711,168 distinct tau, all closed, rows_with_failed 0, bad_json_lines 0, global_min_lower 2.511523890227165e-06 at tau 5967438210, target 711,168. This turns the 9 Nov sample-only interval result of [[g0013_r10_ten_blocks_22222_clean_at_cap_10_11_on_grid_2026_11_09]] (200 orbits) into the whole orbit set: at mass cap 10/11 partition 22222 is positive on every ten-value block orbit by interval arithmetic.

How far to trust: the margin is thin (2.5e-6 against the grid's +0.419 smallest margin; the interval lower bound is a box bound, so far below the point value is expected, but it is the number to recheck first). Not re-derived a second way yet; an independent re-run of the argmin orbit at a finer box split is the check. The orbit count is the r10 audit's (an independent recurrence agreed). The full square (cap 1) still has 1,022 failing orbits; this result says nothing there.

Files: GitHub release g0013-r10-2026-11-09 in the private brain repository, asset g0013_r10_iv_full.tar.gz (31,666,941 bytes, sha256 08b8807afec921f36f7ae39f6d2addd4f416d2a8b9670918243bdafe5e5d1c9b, GitHub digest checked; holds iv_full shards, iv_full_combined.json, the runner, combiner and worker logs). Local shards deleted after the check; the second machine keeps iv_full_combined.json and OFFLOADED.txt.
Recheck 10 Nov 19:03 (an agent): the argmin orbit 5967438210 reproduces at iv.dps 60 (same 2.5e-6); demanding lower bound > 1e-3 needs two more C boxes and lifts the floor to 0.140 (float F 3.8-4.3 there), so the thin margin is box width, not a near-zero F. Same formula code, not an independent F. Note on GitHub: G0013/audit_agent/R10_ARGMIN_RECHECK_2026_11_10.md (commit 62c180ac).

Independent check 10 Nov 21:0x (an agent): max over equal-area partitions of F, from the paper's Lemma 4.1 alone (semi-discrete assignment on a pixel grid, not the run's code), for tau 5967438210: 8.2 at the argmin box centre (run's partition 4.32), smallest 5.99 over 96 bands of area 0.15..10/11 and 1.53 over 96 bands of area 0.01..0.15, at the corner, scaling like 15 sqrt(area); controls identity ~0 (grid error 0.02), reversal 5.35. F stays positive; the thin 2.5e-6 is box width. Float falsification test, one orbit. GitHub commit 45a783ce, folder G0013/audit_agent/AUDIT.md.
