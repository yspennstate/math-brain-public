---
name: p0434_ra_merge_into_k_fails_but_laws_stay_under_s2_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 15:2x: RA <= max_eps Q2(K,p+w) is false (+5.6e-4 at K=2.168, t=0.91, fine 2000-pt eps grid agrees); the six climbed laws sit at q=0.05-0.996 of S2"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:20:14-05:00
  status: provisional
  evidence: ""
---

Route item 87 (an agent). The item 86 candidate (merge the middle atom into K, eps free) fails on RA laws with t=(m-1)/(K-1) > 0.9 and p+w well below p*: ratio - M(p+w) up to +5.62e-4 at K=2.16848, t=0.9108, w=6.06e-2, p=7.19e-3, eps=0.1519. A 2000-point eps grid with a refine at every local max gave the same gaps to four digits, so it was not a coarse M. Against S2(K) the six laws have q=(ratio-1)/(S2-1) = 0.665, 0.321, 0.996, 0.212, 0.051, 0.326; the 0.996 one is the two-atom limit. Scar: S2 evaluated AT p* gives float ratio 1 (the tie edge); use a = p*(1-1e-10), which matches Nelder-Mead to 10 digits. Next: direct climb against S2 for 3-5 atoms, w3s2climb_agent.py. Links [[p0434_near_s2s_maximiser_only_ra_holds_and_it_stays_below_2026_11_08]] [[p0434_ra_edge_excess_negative_for_all_k_and_m_2026_11_08]].
