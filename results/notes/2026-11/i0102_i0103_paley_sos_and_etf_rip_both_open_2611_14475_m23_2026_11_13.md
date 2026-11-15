---
name: i0102_i0103_paley_sos_and_etf_rip_both_open_2611_14475_m23_2026_11_13
description: "[PROVISIONAL] I0102 Paley clique degree-4 SoS O(p^{1/2-eps}) and I0103 Paley ETF RIP beyond sqrt both open 13 Nov 2026; Kunisky-Yu Omega(p^{1/3}); arXiv 2611.14475 explicit RIP k=m^{2/3-o(1)} via strongly regular subset (not whole Paley ETF)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T18:09:27+02:00
  status: provisional
  evidence: ""
---

I0102 (Randomstrasse101 2025, Conjecture 28: degree-4 SoS gives O(p^{1/2-eps}) for the Paley clique number) and I0103 (Conjecture 29: the Paley ETF has RIP for m ~ p^{1/2+eps}) are both still open as of a web and arXiv check on 13 Nov 2026.

What is known, read 13 Nov 2026:
- Kunisky and Yu, "A degree 4 sum-of-squares lower bound for the clique number of the Paley graph", CCC 2023, arXiv:2211.02713: the degree-4 SoS value is Omega(p^{1/3}) for prime p, so degree 4 can at best move the exponent from 1/2 to 1/3. Their numerics suggest O(p^{1/2-eps}); nothing proves it. A block-diagonal SDP follow-up (arXiv:2304.08615) restates it as a numerical suggestion.
- Paley ETF RIP: still only conditional. Bandeira, Mixon and Moreira show that a conjectured discrepancy bound for the Paley graph implies RIP beyond the square root for the Paley ETF. arXiv:2011.02907 (on the RIP of the Paley matrix) is conditional on its Conjecture 7.
- New context, arXiv:2611.14475 (submitted 10 Nov 2026), "Explicit restricted isometries with k = m^{2/3-o(1)}": it builds an explicit RIP family by picking a large vertex set in a strongly regular graph where every small subset spans few edges (via an incidence result of Zahl), using only the entrywise absolute value of the Gram matrix. It shows the absolute-value barrier is m^{2/3}, not m^{1/2}. It uses a chosen subset, not the whole Paley ETF, so it does not settle Conjecture 29. It is the closest recent tool, and a Codex attempt on I0103 should start from it.

How to apply: do not spend a run re-searching these two. An attempt on I0103 starts from 2611.14475 and asks whether the whole Paley ETF (not a chosen subset) passes the m^{2/3} absolute-value argument. It cannot by that argument alone: Paley cliques of size ~log p give subsets with many edges. An attempt on I0102 needs an upper bound on the degree-4 SoS value, which is the open part.

