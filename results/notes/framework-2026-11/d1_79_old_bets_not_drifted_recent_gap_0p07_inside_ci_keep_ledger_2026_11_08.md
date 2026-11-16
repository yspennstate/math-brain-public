---
name: d1_79_old_bets_not_drifted_recent_gap_0p07_inside_ci_keep_ledger_2026_11_08
description: "[PROVISIONAL] No: old resolved bets (n=165, gap -0.03) and recent ones (n=70, gap +0.07, hit 0.69 [0.57,0.78] around mean p 0.61) show no drift; archiving would cut the scored sample 235 to 70"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:10:30+04:00
  status: provisional
  evidence: "d179.py, predict.py parse/score, 8 Nov 03:10"
---

Should the brain move old resolved predictions to a cold ledger so calibration reflects the current regime (backlog D1.79)? Not now. Measured by an agent on 8 Nov at 03:10, read-only, with predict.py's own parse, score and _beta_interval (d179.py).

- memory/PREDICTIONS.md holds 339 bets; 235 are resolved hit or miss with a p.
- Split at a due date of 8 Sep: old n=165, mean p 0.58, hit rate 0.55 [0.47, 0.62], Brier 0.240, gap -0.03. Recent n=70, mean p 0.61, hit rate 0.69 [0.57, 0.78], Brier 0.200, gap +0.07.
- Split at 8 Oct: old n=202, gap -0.01; recent n=33, hit rate 0.67 [0.49, 0.80], gap +0.07.
- The recent bets lean underconfident, but their mean p sits inside their own interval at both cuts, so no drift is shown. Room to fail is small: with 70 recent bets the interval half-width is about 0.1, so a drift under about 0.1 could not show here. Dropping the old bets would cut the scored sample from 235 to 70 and widen every interval about 1.8 times.

How to apply: leave the ledger whole. Rerun d179.py when the recent half passes about 150 resolved bets; a recent gap whose interval excludes the mean p would be the signal to window the calibration (a recent-window read beside the full one, not a deletion). Related: [[prediction_ledger_is_calibrated_but_barely_sharp_auroc2_0p63_2026_10_30]], [[predictions_calibrated_0p59_but_unsharp_joy_framed_gap_0p15_d6_86_2026_11_03]].

