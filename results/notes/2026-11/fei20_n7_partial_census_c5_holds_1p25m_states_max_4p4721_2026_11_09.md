---
name: fei20_n7_partial_census_c5_holds_1p25m_states_max_4p4721_2026_11_09
description: "[PROVISIONAL] Does c=5 hold for n=7 FEI payment states? On every one reached: 1,254,610 states, max B/J 4.4721 (lower bound), 6 leaf layers open; general c=5 still open"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T04:36:43+04:00
  status: provisional
  evidence: "codex_fleet/20261108_pro/workers/FEI20 REPORT.md, coverage_summary.json; frontier T021 fei20_reserve_c5_n7_partial_2026_11_09 (4ea60bffa9)"
---

Not proved, but it holds everywhere FEI20 could reach (Codex gpt-6.1-sol high, read by an agent on 9 Nov).
The seven-input census of FEI18's signed AND/OR one-label interfaces stopped at its memory guard at about 2.8 GB
resident. By then it had certified 1,254,610 distinct payment states. All of them pass c = 5, and the largest B/J
lies in [4.4721299222675, 4.4721299222676] nats per unit influence, from 220-digit outward intervals with a
250-digit Decimal recheck. That is a lower bound on the full n = 7 maximum, not the maximum.

Coverage: the 7- and 8-leaf layers and the ordinary 9-leaf layer finished. Six pairs [literal leaves, selector
marked] are still open: [10,F] [11,F] [12,F] [9,T] [10,T] [11,T] (coverage_summary.json). The six-input bank
reproduced FEI18 exactly: 149,829 states, max 4.3327934. The witness is
((NOT x OR (NOT a OR a)) AND ((((x AND f) OR e) AND d) OR (b OR c))), with x the selector.

The sequence of maxima is n = 5: 4.1047, n = 6: 4.3328, n = 7 partial: 4.4721, and FEI18's n = 8 partial: 4.5832.
The gaps are shrinking (0.228, then 0.139 or more), but searching cannot settle c = 5. As
[[fei18_c5_passes_n6_full_149829_states_max_4p3328_need_4p583_2026_11_08]] says, the move is to bound how B/J grows
with n. The reserve floor of [[fei19_reserve_floor_pi2_over_2_2026_11_09]] (pi^2/2 = 4.935) sits above every value
found so far.

I read the report and its audit list; I did not recompute the witness myself. Pushed to frontier T021
fei20_reserve_c5_n7_partial_2026_11_09 (4ea60bffa9, 135 files). The checkpoints (census pkl, payments sqlite) are
still on the Mac.

