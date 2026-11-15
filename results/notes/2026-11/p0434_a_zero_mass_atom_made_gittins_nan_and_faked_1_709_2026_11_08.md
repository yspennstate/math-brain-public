---
name: p0434_a_zero_mass_atom_made_gittins_nan_and_faked_1_709_2026_11_08
description: "[VERIFIED] P0434 8 Nov 23:1x: a grid start with an atom of mass exactly 0 gave soap.py's Gittins line A/B with B = 0, nan ranks, and a fake (sup-1)/(S2-1) of 1.709 against T 1.0079; w 1e-14 gives 0.767"
metadata:
  node_type: memory
  type: project
  status: verified
  originSessionId: 637c11d8-331f-4f03-ac7c-c997f7076cfb
  modified: 2026-11-09T04:08:44.161Z
---

P0434 route item 118b (an agent, 8 Nov 2026 23:0x-23:1x), file w4tw22g_agent.py in codex_fleet/runs/own_p0434.

The grid over the twin mass w included w = 0.0. In soap.py's gittins_pieces the line for piece j against atom k divides by B = p[j:k+1].sum(), which is 0 when the atom at piece j has mass 0. The line becomes (inf, inf), the rank inf - inf*a is nan, np.min returns nan, and every comparison after that is meaningless. The first row printed 1.7090764 against T's 1.0079243, a 70 percent excess where every earlier scan sat below 1.008.

Measured at that point (K 2.2, t 1.01, q 1e-3, p 0.15429, eps 0.4508): w = 0 gives 1.70909; w = 1e-14, 1e-10, 1e-6 give 0.76718, 0.76718, 0.76719; the same law with the zero atom dropped gives 0.76718. The bad output is kept as w4tw22g_w0bug_agent.out; the rerun floors w at 1e-12.

**Why:** a number 70x further past the bound than anything in 117 rows was taken as a bug before it was taken as a counterexample, and it was one.
**How to apply:** never pass a zero-mass atom to soap.ratio. Floor masses (1e-12) or drop the atom. Read a RuntimeWarning "invalid value encountered" from soap.py as a wrong answer, not noise, and do not run these scans with -W ignore unless the masses are floored.

Links: [[p0434_small_d_branch_tends_to_the_twin_ratio_from_below_2026_11_08]] [[p0434_absolute_membership_tolerance_faked_a_corner_excess_2026_11_08]] [[report_surprising_number_before_break_it_2026_07_12]]
