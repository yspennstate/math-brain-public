---
name: p0434_least_beta_for_twice_waiting_plus_residence_is_about_0_035_2026_11_08
description: "[PROVISIONAL] P0434 8 Nov: least beta for E T_MS <= 2 Q_G + (1+beta) R_G on the n-large tie family tends to about 0.035 (a->1/2, rho 0.9; fits to n 72 agree)"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T09:26:19-05:00
  evidence: "codex_fleet/runs/own_p0434/beta_n100_extrap.out"
  status: superseded
  superseded_by: p0434_least_beta_is_at_least_0_0677_once_a_passes_one_half_2026_11_08
---

P0434 (M-SERPT against Gittins), 8 Nov 2026 09:2x. The least beta with E[T_MS] <= 2 E[Q_G] + (1+beta) E[R_G] on the n-large family (1, 1+g, n far-apart large atoms of equal work, large mass at the M-SERPT tie) tends to about 0.035 as n grows, at a near 1/2 and load 0.9. This replaces [[p0434_least_beta_for_twice_waiting_plus_residence_is_about_0_02_2026_11_08]], which fixed a at (3 - sqrt 5)/2.

Measurements, full SOAP split (split_T):
- beta rises monotonically as a -> 1/2 at every load tried (beta_a.out, beta_a2.out); the golden a is best only at low load.
- At a = 0.499, sizes 1e4 * 100^j: beta at rho 0.85 / 0.9 / 0.95 is 1.41e-2 / 7.8e-3 / -1.5e-2 (n 32), 2.04e-2 / 1.69e-2 / 1.9e-3 (n 48), 2.35e-2 / 2.15e-2 / 1.02e-2 (n 64), 2.45e-2 / 2.30e-2 / 1.29e-2 (n 72).
- Limits in 1/n (two-, three- and four-point fits, all agree to 3 digits): 0.0328 (rho 0.85), 0.0348 (rho 0.9), 0.0343 (rho 0.95).
- Spacing 1000^j instead of 100^j raises beta by 2-6 percent at n 32 and 48, so the far-apart limit is about 0.035-0.037.
- Random laws (300) and tie laws with n <= 8 large atoms (95) all have beta < 0; generic laws have much room, more toward heavy traffic.

Reading: on this family a 2 Q_G + 1.04 R_G target probably holds for every n, far inside Conjecture 8.1's 2 Q_G + 2 R_G. Not a proof: extrapolation from n <= 72, one family, one model (soap lineage). E[T_MS]/E[T_G] stays at or below about 1.061 on all of it.

Evidence: ~/codex_fleet/runs/own_p0434/ beta_scan*, beta_extrap*, beta_random*, beta_tie*, beta_a*, beta_n100.py/.out, beta_n100_extrap.out, NOTE.md 08:4x-09:2x; research-repo codex-fleet.

Update 09:3x (beta_parts.out): the large classes are served identically by both policies (Q_MS = Q_G, R_MS = R_G to 3-4 digits), so their slack is only their Q_G, which vanishes like 1/n. The limit beta is the small classes' excess over 2 Q_G + R_G (0.0353 of total R_G at rho 0.9, nearly n-independent) divided by total R_G; on the small classes alone Q_MS/Q_G = R_MS/R_G = 1.41.

Update 10:4x-10:5x (beta_seeded.out, beta_rho32.out, beta_seeded48.out): a climb seeded at n 32 reached 0.0157, but the equal family itself gives 0.0156 at rho 0.80 (0.0078 at 0.9), so the gain was the load, not the size pattern. At finite n the worst rho sits near 0.8 (n 32: 0.0120/0.0152/0.0156/0.0141 at rho 0.65/0.75/0.8/0.85; n 48: 0.0204 at 0.8 vs 0.0170 at 0.9), and the tiled climbed pattern at n 48 (0.0193) is below the equal family there. The 0.035 limit stands as the best estimate.

Update 11:1x (beta_nfit.out): at each n's own worst rho the equal family gives 0.0048/0.0115/0.0156/0.0206/0.0235 at n 16/24/32/48/64, the worst rho drifting 0.70 -> 0.84. Extrapolated in 1/n: 0.0288 (first order), 0.0327 (with 1/n^2, residual 7e-5). Consistent with 0.035 as the sup along this family.

Update 11:2x (beta_limit.out): large D equals -Q_G(large) to 1% and Q_G(large) ~ 1/n, so beta_inf(rho) is the small classes' D, which peaks at rho about 0.93: 0.0359 (n 48), 0.0356 (n 72), drifting down with n, and falls to 0.026 at rho 0.999. The equal-family sup is 0.035-0.036, worst rho tending to about 0.93.

Update 11:3x (smallD_climb.out): off the equal family the small classes' D alone reaches 0.073 of R_G (rho 0.989, beta -11.8), so a bound on small D by R_G alone is false; the charge must include Q_G(large), with c1 about 0.036 from the equal-family limit.

SUPERSEDED 8 Nov 13:1x by [[p0434_least_beta_is_at_least_0_0677_once_a_passes_one_half_2026_11_08]]: the 0.035 came from searching a <= 1/2 only; past 1/2 the same family reaches 0.0677 in the limit and +0.0373 at n 72.
