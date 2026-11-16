---
name: t001_theta_pc_bounds_d3_0p10_d7_0p004_conditional_2026_11_02
description: T001 percolation continuity: conditional 99.9% bounds theta(p_c) <= P_{p_c+3sigma}(|C|>=65536): d3 0.1025, d4 0.0249, d5 0.0091, d6 0.0052, d7 0.0042; not a proof, the T014 power-law tail is the evidence; PREREG98 4/4
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T08:32:01+04:00
  status: provisional
  evidence: "rows/T001/moves.jsonl 64b1c104"
---

T001 (continuity theta(p_c) = 0 for bond percolation on Z^d, d 3-10 open), first frontier move, 2 Nov 2026, an agent. m001a is in rows/T001/moves.jsonl (64b1c104); the simulator is rows/T014/t014_perc.c.

- Bounds: theta(p_c) <= theta(p+) <= P_{p+}(|C| >= 65536), at p+ = p_c + 3 sigma. The 99.9% bounds are 0.1025 (d3), 0.0249, 0.0091, 0.0052 and 0.0042 (d7).
- They are conditional on p_c <= p+, and the sigmas were recalled from memory, not re-checked.
- The 3-sigma shift moves the tail by only 0.3-1.1% at this s.
- These bounds do not prove continuity. The real evidence is T014's unbroken power-law decay of the tail. PREREG98 4/4.
- A rigorous version needs a certified p_c upper bound: open.
- Related: [[t014_d7_percolation_tail_exponent_0p496_mean_field_2026_11_02]].

