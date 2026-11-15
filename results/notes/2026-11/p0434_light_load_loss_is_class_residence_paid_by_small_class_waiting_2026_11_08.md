---
name: p0434_light_load_loss_is_class_residence_paid_by_small_class_waiting_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov 15:2x: at the m 6 light-load optimum (L+/Q_G 0.772) the M-SERPT loss is residence in one mid class, 1.47x its own Gittins waiting and 1.17x that of all equal-or-larger classes; no class-local charge"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T15:20:27-05:00
  status: provisional
  evidence: ""
---

adv_lowload_perclass.py in codex_fleet/runs/own_p0434 (NOTE.md 15:2x). First-order coefficients, rho 1e-4 and 1e-5 agree to 4 figures. Q_G/rho 0.739, L+/rho 0.570. Class s 2.146 (mass 0.555): dT/rho +0.529, all residence = 1.47x own Q_G, 1.17x Q_G of classes >= it. Class s 4914 (mass 7.6e-5): +0.042, residence, 1.05x own. Gains: the two small classes' waiting (0.103->0.036, 0.185->0.066). So a proof of L+ <= Q_G at light load must charge a class's residence loss to the Gittins waiting of smaller (higher-rank) classes. Extends [[p0434_light_load_loss_over_gittins_waiting_grows_with_atom_count_2026_11_08]] and [[p0434_no_cut_or_class_local_charge_one_class_can_be_111x_slower_2026_11_08]].
