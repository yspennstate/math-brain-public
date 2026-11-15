---
name: p0434_least_beta_for_twice_waiting_plus_residence_is_about_0_02_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov: least beta for E T_MS <= 2 Q_G + (1+beta) R_G on the n-large family extrapolates to about 0.02 (rho<=0.7); peak at middle load"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T08:59:52-05:00
  evidence: "codex_fleet/runs/own_p0434/beta_extrap.out"
  status: superseded
superseded_by: p0434_least_beta_for_twice_waiting_plus_residence_is_about_0_035_2026_11_08
---

P0434 (M-SERPT against Gittins), 8 Nov 2026 08:5x. Since E[T_MS] <= 2 E[Q_G] + E[R_G] fails from 12 large classes ([[p0434_twice_gittins_waiting_plus_residence_fails_at_low_load_2026_11_08]]), I measured the least beta with E[T_MS] <= 2 E[Q_G] + (1+beta) E[R_G] on the same family (1, 1+g, n far-apart large atoms of equal work, sizes 1e4 * 1000^j, a = (3 - sqrt 5)/2, large mass at the M-SERPT tie), with the full SOAP split at loads 0.001 to 0.99.

Peak beta by n: 2.0e-4 (n 12), 1.8e-3 (16), 5.5e-3 (24), 8.0e-3 (32), 1.18e-2 (48). The peak sits at middle load (0.2 at n 12, 0.7 at n 32 and 48) and beta is negative near rho 0.99, so heavy traffic is not where this family binds. beta fits A - B/n closely: two-point (n 32, 48) and three-point (n 24, 32, 48) limits agree to 3-4 digits for rho <= 0.7: limit beta 1.7e-5 (rho 0.001), 1.9e-3 (0.1), 6.7e-3 (0.3), 1.28e-2 (0.5), 1.94e-2 (0.7). At rho 0.9 and 0.99 the two fits disagree (2.3e-2 vs 2.3e-2 at 0.9 but 3.9e-2 vs 2.0e-2 at 0.99), so the limit there is not measured.

Reading: on this family a target of the form 2 Q_G + (1 + 0.03) R_G probably survives every n at loads up to 0.7, and E[T_MS]/E[T_G] stays at or below 1.061 everywhere. Not a proof; extrapolation in 1/n from n <= 48, and loads above 0.7 are open.

Evidence: ~/codex_fleet/runs/own_p0434/ beta_scan.py/.out, beta_scan2.out, beta_extrap.py/.out, NOTE.md 08:4x-08:5x; research-repo codex-fleet.

Update 09:1x: the 0.02 is for a = (3 - sqrt 5)/2 only. At n 32, rho 0.8, beta is +4.3e-3 at that a but +1.45e-2 at a = 0.48 (beta_a.out), so the sup over a is larger and still unmeasured. Tie laws with n <= 8 all had beta < 0 (beta_tie.out).

Update 09:2x: beta grows as a -> 1/2 (beta_a2.out). At a 0.499 the peak is 1.59e-2 (n 32, rho 0.8) and 2.06e-2 (n 48, rho 0.85); two-point 1/n limits are 0.033-0.036 at rho 0.85-0.95, rough because the peak load still moves with n. So the family's beta is probably about 0.04, still far below the 1 that Conjecture 8.1 allows.
