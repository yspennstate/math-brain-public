---
name: p0434_p12_crossing_rederived_from_r_tie_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 09:5x: item 47's P12 crossing reproduced from its stored R_tie; dR/dp at p0 changes sign at K*=2.175833294892"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T09:57:50-05:00
  status: provisional
  evidence: ""
---

an agent re-derived route item 47's crossing (637c11d8) from the stored closed form w3tiecf_agent_R.txt. At p0=(K-2)/(K-1), where w=0, the numerators of dR/dp and dR/deps share (K+eps-2)^2. Once that is removed, the resultant in eps is 4(K-2)^6(K-1)^8(K^2-K-1)P12(K), with the same P12. A bisection on the sign of dR/dp at the eps maximiser gives K*=2.175833294892, P12's root to 12 digits. dR/dp is +4.9e-4 at K=2.175 and -3.9e-4 at 2.1765, so a small w>0 pays above K*. This rests on item 47's R_tie, which came from soapsym. My own solver matched the family at four K. Files: P0434/audit_agent_2026_11_08/p12_check_e05f.py/.out, AUDIT_EDGE.md section 6, brain-repo main 8e7035a5. Lesson: a resultant of 0 meant a common factor; take the gcd out before reading it. Related [[p0434_tie_limit_closed_form_crossing_k_star_2_1758_2026_11_08]].
