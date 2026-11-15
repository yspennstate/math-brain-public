---
name: p0434_worst_family_excess_sits_in_the_small_classes_2026_11_08
description: "P0434 8 Nov 12:2x: on the equal (worst) family the large classes carry under 1 pct of the excess (XL/QL 0.009); all difficulty is in the small-class lemma, whose slack is about -0.002 R_G and flat in n"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T12:28:36-05:00
  status: provisional
  evidence: "~/codex_fleet/runs/own_p0434/lemma_eq2.out"
---

On the equal family that sets P0434's sup (sizes 100^j, equal work per class, a 0.499), the large classes carry almost none of M-SERPT's excess over Gittins: XL/QL is 0.0086-0.0093 for n 16-72 at every rho tried (0.70-0.90), and QL falls from 0.018 to 0.007 R_G. So beta = (T_MS - 2Q_G - R_G)/R_G is the two small classes' charge D_small less QL, and lemma B (XL <= 0.9 QL) has huge room there.

Lemma A' (D_small <= 0.036 R_G + 0.1 QL) is where all the difficulty sits. Its slack grows with rho and is nearly flat in n: -0.0022 (n 56) and -0.0020 (n 72) at rho 0.90; at the small-D peak near rho 0.93 (small D 0.0356-0.0359 R_G from beta_limit) the slack is about -0.1 QL, i.e. -0.001 to -0.002 R_G. At QL = 0 lemma A is the target inequality itself.

Scar avoided: a 1/n fit of A' slack taken at beta's worst rho gave -0.0011 (first order) against +0.0004 (second order) and looked like a coin flip. It was the wrong rho; A's own worst rho is higher. Read a lemma at its own worst point, not at the target's.

Also: 100^j sizes overflow a square in soap.py past n ~74 (1e4 * 100^(n-1) squared > 1e308); a run at n 96/128 printed a RuntimeWarning and was stopped.

Evidence: ~/codex_fleet/runs/own_p0434/lemma_eq.out, lemma_eq2.out, NOTE.md section 12:2x. Related: [[p0434_small_class_charge_needs_only_0_024_of_large_waiting_2026_11_08]], [[p0434_large_excess_over_large_waiting_grows_with_n_past_one_half_2026_11_08]], [[p0434_least_beta_for_twice_waiting_plus_residence_is_about_0_035_2026_11_08]].

Update 12:4x (lemma_eq4.out, ratio 1e4): small D is nearly flat in n at fixed rho while n*QL is nearly constant (0.45 at rho 0.80), so beta_n(rho) ~ D_inf(rho) - K(rho)/n and sup beta = sup of the limit small-class charge D_inf over (a, rho).

Update 12:4x (dinf_grid.out): the limit charge D_inf(a, rho) increases in a (about 0.01 per 0.1) and peaks near rho 0.93; its max is at a -> 1/2, about 0.036. The sup of beta is then max over rho of D_inf(1/2, rho), a one-variable function.

Update 8 Nov 13:0x (dinf_pieces/dinf_formula/dinf_ncheck): closed form. Under M-SERPT the 1+g class has waiting and residence both times F = 1/(1 - a rho); Gittins fresh waiting W = a rho/(2(1 - a rho)); large classes share load 1 - a. D_inf(1/2, rho) = x^2/(4(1-x)^2(1 + ln((1-x)/(1-2x))/x)), x = rho/2; max 0.035218 at rho 0.9204 [a = 1/2 only; the sup is higher, see the 13:1x correction below]. With the finite-n left sum for R_G the formula reproduces all 10 n 36 grid values to 1e-5; at ratio 100 n 8-64 the solver tracks it (0.03561 vs 0.03568 at n 64) and beta rises to it from below. The n 36 value 0.0361 is a 1/n lag. F, W and the residence were read off the solver, not derived.

Correction 8 Nov 13:1x: the a <= 1/2 cap above was a choice, not a constraint. Past 1/2 the closed form keeps rising to 0.0677 (a 0.90, rho 0.998), and the solver agrees; see [[p0434_least_beta_is_at_least_0_0677_once_a_passes_one_half_2026_11_08]].
