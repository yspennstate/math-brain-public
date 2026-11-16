---
name: d4_75_d4_85_control_bars_unread_no_bets_at_0p9_236_resolved_2026_11_08
description: "No: D4 #75/#85 would retune control_policy bars nobody reads (no hook calls it); 236 bets resolved and calibrated 0.4-0.8, but 0 stated at >=0.9, so the high-stakes act bar has no data"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:35:58+04:00
  status: verified
  evidence: "predict.parse/score binning, control_policy.py live haircuts, 8 Nov 03:35"
---

1000-ways D4 #75 (act/verify/ask bars from an explicit loss matrix) and D4 #85 (a softmax over expected utility in place of hard cutoffs) would both retune the bars in control_policy.py. Checked by an agent on 8 Nov about 03:35. Neither is built.

- Nobody reads the bars. control_policy.py is on-demand only: no hook in hook_dispatch_list.json calls it, and predict.py mentions it only in comments about the ledger format. There are no logged decisions to score a realized loss against, which is the measure both items name.
- Its 8 Jul reason for staying unwired was too few resolved bets. That no longer holds: 236 of 343 bets are resolved, and the live haircuts are infra x0.98 (93), user x0.97 (91), result x1.00 (51).
- The high end is still empty. Resolved bets by stated p: 0.0-0.5 n 33 hit 0.45; 0.5-0.6 n 75 hit 0.52; 0.6-0.7 n 72 hit 0.53; 0.7-0.8 n 45 hit 0.80; 0.8-0.9 n 11 hit 0.91 (95% 0.62-0.98); 0.9 and up n 0. The high-stakes act bar (0.90) and verify bar (0.70) sit where the ledger has no or thin data, so a loss-matrix derivation of them could not be checked against anything.
- Two counts agree: control_policy's domain counts sum to 235, and this binning finds 236 (one bet in another scope). Script: d4_75_calibration_bins.py. It uses predict.parse and predict.score, the same reader the policy uses.

How to apply: before tuning these bars, wire the policy somewhere it decides (its header names reality_monitor's sign-off or danger_mode's stakes read) and log each decision with its outcome. Until bets are stated at 0.9 and above, the high-stakes bar is a hand-set number, and it should be described that way. Related: [[d1_79_old_bets_not_drifted_recent_gap_0p07_inside_ci_keep_ledger_2026_11_08]] (the same ledger, checked for drift).

