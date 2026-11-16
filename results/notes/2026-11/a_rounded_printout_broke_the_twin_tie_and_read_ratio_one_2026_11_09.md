---
name: a_rounded_printout_broke_the_twin_tie_and_read_ratio_one_2026_11_09
description: "P0434 9 Nov 08:2x: a maximiser law printed to 10 digits lost its twin tie; float and soap_mp both read T_MS/T_G 1.0000069 against 1.9958 in-run. Print near-2 laws with repr and check the printout reproduces the run"
metadata:
  type: feedback
  created: 2026-11-09
  created_at: 2026-11-09T08:21:04-05:00
  status: verified
  evidence: "pprime_gap_scan.out; pprime_gap_mp.out"
---

P0434, 9 Nov 08:2x, an agent.

pprime_gap_scan.py printed its maximiser laws with s to 10 significant digits and p to 7. The best law reached q 0.9979806,
T_MS/T_G 1.9958498 inside the run. Rechecked from the printed numbers (pprime_gap_mp.py), soap float and soap_mp at 50
digits agree on the same input, and both read T_MS/T_G 1.0000069 and q 0.50003. Rounding broke the twin tie: the
twin atoms 3.167842443 / 3.167842451 are the near-2 mechanism, and the tie is a knife edge in both s and p (compare
[[p0434_fixed_parameter_atom_slope_is_a_tie_jump_2026_11_09]] and [[p0434_two_atom_tie_is_a_one_sided_peak_exactly_2026_11_08]]).
So a printed near-2 law is worthless unless it is printed with repr (17 digits). Even then, recheck it from the printed text
before citing it.

The two paths agreeing did not catch it. They agree on whatever input they get, and the input was wrong. The check that
caught it was comparing the recheck's ratio with the run's own ratio.

How to apply: any optimiser on twin/tie laws prints s, p and the raw parameter vector with repr. Before citing a law,
evaluate the printed text and require that it reproduces the in-run value. Related: [[a_rank_grid_merged_twin_atoms_and_read_ratio_one_2026_11_09]].

