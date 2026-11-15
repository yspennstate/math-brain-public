---
name: p0434_third_atom_local_result_written_as_one_note_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 19:1x: items 101-107 as one note (c78b52ef): a small third atom lowers S2 at first order for every K in (2,9/4]; which steps are exact, which numeric"
metadata:
  node_type: memory
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T19:21:13-05:00
  status: provisional
  evidence: ""
  originSessionId: 637c11d8-331f-4f03-ac7c-c997f7076cfb
  modified: 2026-11-09T00:45:46.087Z
---

P0434 route item 108 (c78b52ef, 8 Nov 19:1x, an agent): items 101-107 are written up as one note,
06_math_research/frontier/P0434/route_agent_2026_11_08/third_atom_local_agent.md.

Proposition: for 2 < K <= 9/4, a third atom of mass m at 1 + d(K-1), d in [0,1), with the K mass and the load free,
gives sup R = S2(K) - c(K,d) m + o(m) with c > 0. Exact pieces: S2' > 0 (item 101), the two-atom tie is a one-sided
peak with the ratio identically 1 past it (106), c(K,d) in closed form with F linear in d and both ends negative at
eps* (104). Exact at first order and local in pk: the sup over the K mass is on the three-atom tie (106, checked
numerically at 32 grid points in 105). Numeric only: far branches (107, one d), the soapsym branch over all K, and
the o(m) constant (error linear in m, unbounded). Nothing global is claimed.

Correction (item 109, d7ee0949): the slope carries the factor S2 - 1, sup R = S2 - c(K,d)(S2 - 1) m + o(m); c is the
slope of the relative excess. Measured, and the note is fixed; see [[p0434_third_atom_scan_at_five_d_and_c_is_a_relative_slope_2026_11_08]].

Read the note before re-deriving any of items 101-107. Builds on [[p0434_two_atom_tie_is_a_one_sided_peak_exactly_2026_11_08]],
[[p0434_third_atom_slope_positive_for_every_k_and_d_exactly_2026_11_08]], [[p0434_s2_increasing_on_2_to_9_4_proved_exactly_2026_11_08]].


Correction (8 Nov 21:1x): the note's statement is local only. S2 is not the sup over all three-atom laws: for K* = 2.17583 < K <= 9/4 the near-twin family of item 47 reaches T(K) > S2. The note now cites that, and step 6 (item 110) adds the past-first-order scan. See [[p0434_third_atom_branch_past_m_c_stays_under_the_twin_family_2026_11_08]].
