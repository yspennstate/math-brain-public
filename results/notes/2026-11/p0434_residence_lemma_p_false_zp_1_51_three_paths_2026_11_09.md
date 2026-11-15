---
name: p0434_residence_lemma_p_false_zp_1_51_three_paths_2026_11_09
description: "P0434 9 Nov 06:3x: candidate (P) R_MS <= 2R_G + (2-c)Q_G FALSE, zP 1.507 on a 6-atom twin law (T ratio 1.50), three paths agree; giant 1e8 gives 1.945"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T06:39:08-05:00
  status: verified
  evidence: "~/codex_fleet/runs/own_p0434/zp_recheck_best.out; zp_hunt2.out"
---

P0434 (M-SERPT vs Gittins, Scully et al. Conj. 8.1, T_MS <= 2 T_G), 9 Nov 06:3x, an agent.

Candidate lemma (P) R_MS <= 2 R_G + (2-c) Q_G, c = 2/(1+sqrt(1-rho)) (with Lemma 5.6, Q_MS <= c Q_G, it would give 8.1)
is FALSE. zP = (R_MS - 2R_G)/((2-c)Q_G) must be <= 1; it reaches 1.50653 on the 6-atom law
  s = [1, 2.09026609, 3.36201514, 3.36242930, 3.36410309, 29182.2642]
  p = [7.84384408e-01, 1.84391796e-01, 3.01484547e-02, 9.99232441e-04, 7.61051421e-05, 3.33643341e-09]
  1-rho = 8.2095e-09
with T_MS/T_G 1.4969, so the conjecture itself is not touched. R_MS/R_G is 4.14 there.

Checked three ways (zp_recheck.py): soap.py/split.py float 1.506531, soap_mp at 50 digits 1.506531, and a grid SOAP
written from scratch (ranks from their definitions, no piece logic shared with soap.py) 1.506501 at 2000 and 8000 cells
per interval. With the giant pushed to 1e8 at the same load share, zP reaches 1.945 (float path only).

How it was found: zp_hunt2.py, Nelder-Mead started exactly at the near-2 laws with a small simplex. The first hunt
(zp_hunt.py), which jittered its starts by 0.3 in log masses, found nothing above 0.644. Near-tie laws are very
sensitive: 5-digit rounding of a zP 1.022 law gives 0.059. Start from the law itself, not near it.

What survives: on these laws Q_MS/(c Q_G) is about 0.75, so the waiting slack is large. A proof cannot spend Lemma 5.6 at
its worst case and bound R_MS term by term by Gittins quantities. It has to couple the residence excess with Q_MS's
distance below c Q_G.

Files: ~/codex_fleet/runs/own_p0434/zp_hunt2.py/.out, zp_recheck.py, zp_recheck_best.out, zp_best_law.py, NOTE.md 06:3x.
Replaces the "(P) alive" part of [[p0434_residence_twice_gittins_fails_borrowing_waiting_holds_2026_11_09]].
Related: [[p0434_joint_target_t_ms_le_2_q_g_plus_mean_fails_kappa_2_26_on_dfr_2026_11_09]],
[[p0434_srpt_plus_waiting_lower_bound_max_still_loses_2_07_on_dfr_2026_11_09]].

