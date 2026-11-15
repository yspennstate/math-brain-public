---
name: p0434_third_atom_scan_at_five_d_and_c_is_a_relative_slope_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 19:3x: route item 109 (d7ee0949): 12 three-atom global scans (d 0.05-0.95, K 2.02-2.25) all below S2; measured slope is c(K,d)(S2-1), so sup R = S2 - c(S2-1)m; the note had dropped S2-1"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T19:45:03-05:00
  status: provisional
  evidence: ""
---

P0434 (M-SERPT against Gittins on [1, K], 2 < K <= 9/4), route item 109, 8 Nov 19:3x, commit d7ee0949 in
06_math_research/frontier/P0434/route_agent_2026_11_08 (w3cfard_agent.py/.out).

The three-atom global scan of item 107 (third atom of mass m 1e-4 at 1 + d(K-1); grid over the K mass and the load,
then Nelder-Mead) repeated at d 0.05, 0.25, 0.75, 0.95 and K 2.02, 2.1, 2.25. All twelve global bests are below S2.
At K 2.1 and 2.25 the best point is on the first-order tie to 1e-5 in pk/p*.

Normalisation fix, measured: item 104's c(K, d) = -num/(S2 - 1) is the slope of the RELATIVE excess. The measured
(S2 - best)/m equals c(S2 - 1): 0.0180 against 0.3287 x 0.05475 at (2.25, 0.95), 0.1196 against 3.1124 x 0.03841 at
(2.1, 0.95). So the proposition reads sup R = S2 - c (S2 - 1) m + o(m). The note third_atom_local_agent.md and
the memory [[p0434_third_atom_local_result_written_as_one_note_2026_11_08]] had written S2 - c m; the note is fixed
in d7ee0949, and the sign result (c > 0) is unaffected.

At K 2.02, p* = 0.0196, so m (1-d)/p*^2 = 0.25 at d 0: m 1e-4 is outside the first-order regime. The best lands below
the predicted tie (pk/p* 0.57 against 0.75 at d 0.05) and the drop is larger than first order (4.9e-3), still below S2.

Status: numeric, grid-limited. Still open: a bound on the O(m^2) term, anything global, the n = 5 climb.
How to apply: quote c with its (S2 - 1) factor; near K = 2 a "small" m must be small against p*^2.

