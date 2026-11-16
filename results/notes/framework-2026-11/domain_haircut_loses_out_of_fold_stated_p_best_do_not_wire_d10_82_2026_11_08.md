---
name: domain_haircut_loses_out_of_fold_stated_p_best_do_not_wire_d10_82_2026_11_08
description: "No (8 Nov): D10 #82 per-domain haircuts lose out of fold (LOO Brier 0.2318 vs global 0.2292 vs stated p 0.2281, 236 bets); control_policy stays unwired though the domains now have the bets; plant caught"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:54:45+04:00
  status: verified
  evidence: "d10_82_domain_haircut_loo_2026_11_08.py; predictions.tsv 236 resolved; plant domain wins by 0.041; pushed 7a8d5ca1fa blobs equal"
---

Question: should control_policy's confidence haircut be split by domain (D10 #82), and should it now be wired in?

No to both, measured 8 Nov. control_policy.py already computes a haircut per domain: the shrunk hit rate over the mean stated p, clamped to 0.3-1.0. It has never been wired. Its July note said to wire it once the domains had enough resolved bets, and they now do (infra 94, user 91, result 51). The live factors are x0.97, x0.97 and x1.00.

d10_82_domain_haircut_loo_2026_11_08.py fits each factor without the bet it scores (leave one out, 236 bets, predict.py's shrink KAPPA 4). The Brier scores:
- stated p: 0.2281
- one global haircut: 0.2292, worse by 0.0011 (95% 0.0009 to 0.0012)
- per-domain haircuts: 0.2318, worse than global by 0.0026 (0.0015 to 0.0036)

So every correction makes the ledger slightly worse. This is the same answer as isotonic and Platt, which lost to stated p out of fold on 31 Oct ([[isotonic_recalibration_loses_out_of_fold_on_the_prediction_ledger_2026_10_31]]). The ledger is already calibrated ([[prediction_ledger_is_calibrated_but_barely_sharp_auroc2_0p63_2026_10_30]]). Its problem is sharpness, not bias, and no haircut fixes sharpness.

The test can fail. A planted overconfident domain (infra hits at p >= 0.6 turned to misses) makes the per-domain arm win by 0.041 (-0.061 to -0.022). A real domain bias of that size would show.

One practical edge: a x0.97 factor moves a stated 0.76 to 0.74, under the 0.75 act bar for medium stakes. Wiring it would turn some act decisions into verify ones for no gain in accuracy.

Done: one dated paragraph in control_policy.py's wiring note says not to wire it and names the script to re-run first. Backup: control_policy.py.pre_d10_82_20261108. No logic changed; it parses and prints the same haircuts.


Two more items fall with this one (8 Nov). D10 #45 (a new ern_learn reflex raises control_policy's haircut for its domain) and D10 #48 (a high-charge memory raises the stakes term) both act only through control_policy. It has no caller: grep finds no reference in the hooks, settings.json or any dreaming script except comments in predict.py. danger_mode, which is wired, has no stakes, charge or salience term to raise instead. Both wait until control_policy earns a wiring, and on this measure it should not get one.
