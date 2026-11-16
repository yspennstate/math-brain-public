---
name: fei18_c5_passes_n6_full_149829_states_max_4p3328_need_4p583_2026_11_08
description: "Does c = 5 pay the FEI reserve inequality? (FEI18) Yes on all 149,829 six-input states (max 4.3328), still open in general; eight-input witness needs c >= 4.5832; read-once-cofactor route refuted"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T23:28:59+04:00
  status: verified
  evidence: "codex_fleet/20261108_pro/workers/FEI18 REPORT.md; frontier T021"
---

FEI18 (Codex gpt-6.1-sol high, reviewed by an agent 8 Nov). The general c = 5 reserve inequality is still open. The complete six-input search has 149,829 payment states, all passing c = 5, with max B/J = 4.3327934 nats per influence. Partial seven- and eight-input searches only give lower bounds; the eight-input witness pushes the necessary constant to at least 4.5831520, still under 5. The margin is shrinking (n = 5: 4.1047, n = 6: 4.3328, n = 8 partial: 4.5832), so the next move is to bound how B/J grows with n, not to search further. The FEI15 family pays I_x[2 ln(e/I_x) - 5] at every m (m = 1..31 by 230-digit intervals, a tail bound from m = 32). (x OR a) AND [(x OR b) AND c AND d] (I_x = 3/16, zero cofactor reserve) kills the read-once-cofactor route below exp(-3/2). My check: fei18_check.py gives n = 5 = 4.1046677, matching [[fei17_leaf_side_paid_4ln2_5_8_n5_max_4p1047_join_only_fails_2026_11_08]]. Frontier T021, folder fei18_reserve_c5_n6_full_2026_11_08 (pushed 137/137). Math card claim_2074c30a113c4db18bf39c2213c1fcb1 depends on the FEI17 card.

