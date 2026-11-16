---
name: a_rank_grid_merged_twin_atoms_and_read_ratio_one_2026_11_09
description: "P0434 9 Nov 07:4x: the grid recheck path read T_MS/T_G 1.000 on a near-2 law whose twins sit 1.4e-11 apart (soap and soap_mp 1.9937); compare atom gap to grid spacing first"
metadata:
  type: feedback
  created: 2026-11-09
  created_at: 2026-11-09T07:49:02-05:00
  status: verified
  evidence: "pprime_heavy_recheck.out"
---

P0434, 9 Nov 07:4x, an agent (measured on the box).

zp_recheck.py's path C (a SOAP rank grid written from scratch, N points per interval) is a good independent check on
ordinary laws (it matched soap to 5 figures on the q 0.894 law), but on the heavy-traffic near-2 law with twin atoms
3.129714801194438 and 3.129714801208326 (1.4e-11 apart) it printed T_MS/T_G 1.000000 against 1.993726 from soap float
and soap_mp at 50 digits. The grid cannot resolve the twins, merges them, and on the merged law M-SERPT and Gittins
coincide. So a disagreement of path C on a near-tie law is a resolution limit, not a bug in soap.

Rule: before trusting or dismissing the grid path, compare the smallest atom gap with its spacing. On near-2 laws the
twin tie IS the mechanism ([[p0434_near_two_laws_are_twins_each_carrying_one_t_g_2026_11_08]]), so a check that cannot see
the tie cannot check the ratio. Use soap_mp at high precision on the exact input there.

Evidence: pprime_heavy_recheck.out, pprime_heavy_best_law.py.

