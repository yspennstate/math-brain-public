---
name: fei24_two_path_small_influence_no_counterexample_sup_pi2_over_2_2026_11_09
description: "[VERIFIED] No (FEI24): blind two-path hunt max 4.9348021874 at I_x 5e-12, 1.31e-8 below pi^2/2; none above; fit to pi^2/2, not proved"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T05:08:26+04:00
  status: provisional
  evidence: "workers/FEI24/REPORT.md; verify.py rerun rc 0; frontier T021 bded7398c8"
---

Did a blind counterexample hunt break the two-path reserve bound at small influence? No (FEI24, 9 Nov). The largest certified ratio was 4.93480218742578232847 nats per unit influence at I_x about 5.144e-12, which is 1.3119e-8 below pi^2/2 = 4.934802200544679. Nothing went above pi^2/2, and nothing went near 5.

The witness is an alternating inside-out path of 32,768 gates with a gamma=5/2 power taper, ANDed with x OR a fresh block. Its opposite-polarity version is certified separately. Over the finite series the gap shrinks like length^-1.993, i.e. I_x^0.797, and the fitted limit is about 4.934802201. That is a fit to one family, not a bound over all formulas. With the geometric mesh held fixed, cutting the influence converges to a lower value that depends on the mesh, so small influence on its own does not remove mesh error. The equal-strength two-sided maximum is 4.93478856757888854418.

Checks: 22 certificates with 100-digit outward intervals, an independent 120-digit entropy recurrence, 60 integer Walsh truth-table controls, and a planted wrong sign that was caught. I reran verify.py: rc 0. I recomputed the gap as pi^2/2 minus the ratio and got 1.3119e-8, which matches.

Two lessons to reuse. Keep the signed selector difference as a product; do not subtract cofactor means that are nearly equal. Test sign plants on asymmetric mixed paths, because an all-OR fixture hides a wrong sign (phi is even).

This supports pi^2/2 as the two-path supremum ([[fei19_reserve_floor_pi2_over_2_2026_11_09]] gives the matching lower bound). It does not prove it; see [[fei23_two_path_reserve_reduced_to_log_moment_lemma_2026_11_09]] for the open analytic step. The n=7 census is in [[fei20_n7_partial_census_c5_holds_1p25m_states_max_4p4721_2026_11_09]].

Pushed to the private brain repository: 06_math_research/frontier/T021/fei24_two_path_small_influence_no_counterexample_sup_pi2_over_2_2026_11_09 (bded7398c8, 30 files).

