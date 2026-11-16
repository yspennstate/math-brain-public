---
name: section9_function_value_radius_is_gamma_cells_and_width_2026_11_12
description: "Ising perceptron kappa=0.05 lower bound: a Section 9 function-value cell not strict? entropy radius set by gamma_cells (600 to 2400), constraint radius by tau width (split in 4); curvature 89 cells, 4 and 7 strict"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T16:29:33+02:00
  status: provisional
  evidence: "ipm-lowerbound f57a2c3 and 6186e7c; runlogs/fv_pg80_p1/p2/p4.log"
---

The kappa = 0.05 lower-bound bridge (a private repository, branch lb/k0p05-finish, local clone ~/ipm-lowerbound) needs strictly negative Ding-Sun function-value enclosures on every Section 9 tau cell. Two things set whether a cell is strict, and they act on different parts of the radius.

1. The constraint and lambda parts of the radius are linear in the tau width. PG source cell 80 (tau 0.433..0.441): whole cell, upper +4.1e-4 (radius 7.7e-3, not strict); halved, -3.6e-3; quartered, -5.6e-3. So every source cell is split into four exact pieces (924 cells, schema v2, commit 6186e7c).
2. The entropy part does not shrink with the width; it is set by the entropy quadrature. At the default gamma_cells 600 the entropy enclosure on QG source cell 2 had radius 0.013 at every tau width, enough to stop the cell going strict however finely it was split. At 2400 it is 0.0016 (schema v3, commit f57a2c3, pushed).

So when a function-value cell will not go strict: read ent_rad against con_rad + lam_rad first. If ent_rad dominates, splitting tau does nothing and gamma_cells is the dial; if con/lam dominate, split the cell. probe_fv.py in the session scratch area prints the split.

Curvature cover, same branch: the schedule went from 56 to 89 cells (48 of width 1/800 over [0, 12/200], 41 of width 1/200). Cells 4 and 7, the weak-sign ones, are strict at the new widths (cell 4 upper about -0.096). The other 87 are running on this workstation, three at a time, each run twice in fresh processes and checked for byte identity (about 35 minutes a cell).

Still open on the bridge: function-value v3 production (16 shards), then the paired negative b_neg cover (0 of 51 after the v2 shards were rejected for a 120 to 80 bit precision reset), then the four-patch Arb concavity cover of Section 8, which needs Linux (fcntl) and about 61 CPU-hours. See [[perceptron_margin_extension_measured_compute_is_not_the_blocker_2026_09_20]].

What would change this: a v3 shard with a non-strict cell whose ent_rad is still the larger part would mean 2400 is not enough for that cell.

