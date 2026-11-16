---
name: opf05_frieze_p34_3out_order_7_8_failures_exact_2026_11_16
description: "[PROVISIONAL] Frieze Problem 34 (constructive 3-out Hamiltonicity): order 7 fails with prob 1407/6400000 (350 labeled failures, two families), order 8 has 37 failure types / 84203 supports; general n=2k+1 formula; audit AUD_OPF05 holds all claims. Small-order census only, not the problem."
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T16:29:51+02:00
  status: provisional
  evidence: ""
---

Codex brief OPF05 (16 Nov) and independent audit AUD_OPF05: all seven claims hold. Distinct-choice 3-out never fails at n=4,5,6; fails at n=7 with probability 1407/6400000 (281400 of 20^7 choices; 350 labeled non-Hamiltonian supports, 280 independent-four plus 70 shared-K4, a special case of Buyukcolak et al. Thm 4). For k>=2, failure at n=2k+1 is binom(2k+1,k+1)/D^(k+1)+(2k+1)/(2D^(2k-1)), D=binom(2k,k). Order 8: 37 orbit types with cut certificates, 84203 labeled supports, four families with 2500155, 2401000, 360150000, 514500 configurations. Source Frieze survey arXiv:1901.07139v28 Sec 4.2. Restricted finite result; novelty unchecked; possible short note only. Files: a second machine the worker folder, AUD_OPF05 (synced to a second machine by m2_syncback.sh).
