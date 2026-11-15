---
name: p0434_least_beta_is_at_least_0_0677_once_a_passes_one_half_2026_11_08
description: "P0434 8 Nov 13:1x: least beta in E T_MS <= 2Q_G+(1+beta)R_G is at least 0.0677 (tie family, a 0.90, rho 0.998, closed form matched to the solver); the old 0.035 came from capping a at 1/2; n 72 law gives 0.0373"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:13:07-05:00
  status: provisional
  evidence: "codex_fleet/runs/own_p0434/dinf_max.out, beta_direct.out, dinf_peakcheck.out"
---

P0434 (M-SERPT vs Gittins), 8 Nov 13:1x, an agent. The least beta in E[T_MS] <= 2 Q_G + (1+beta) R_G is NOT about
0.035. That value came from searching only a <= 1/2 on the tie family (small atoms 1 and 1+g, masses a and 1-a, many
far-apart large classes of equal load at the M-SERPT rank tie). The tie exists for every a in (0,1), and past 1/2 beta
keeps rising.

Closed form in the limit n -> inf (large-class waiting QL ~ c/n -> 0, large excess XL ~ 1e-4 QL):
  beta -> D_inf(a, rho) = [F(1-a)(W+1) + a(W+1) - F] / [1 + ln((1 - a rho)/(1 - rho))/(a rho)],
  F = 1/(1 - a rho), W = a rho/(2(1 - a rho)); at a = 1/2 the numerator is x^2/(4(1-x)^2), x = rho/2.
  max over (a, rho): 0.06769 at a 0.900, rho 0.9983 (a 1/2 alone gives 0.035218 at rho 0.9204).

Derivation, from the SOAP formulas: the 1+g class's worst future rank under M-SERPT sits just above the fresh rank,
so all fresh work (load a rho) counts as new work for its waiting and its whole residence: both are multiplied by F.
Under Gittins fresh work waits W and resides 1. Under the tie E[S] = 1/a, so the large classes carry load share 1 - a
and their Gittins residence gives the log term.

Measured: with the finite-n left sum for R_G the formula reproduces 25 solver points (n 8-72, ratio 1e2/1e4,
a 0.3-0.9, rho 0.5-0.998) to about 1e-4. A finite law already beats 0.035 directly: n 72, ratio 100, a 0.7, rho 0.95
gives beta +0.03725 (a 0.65, rho 0.93: +0.03516). So the plan "lemma A' (small D <= 0.036 R_G + 0.1 QL) plus lemma B"
is dead: A' fails for a >= 0.55 at large n.

Not a proof that 0.0677 is the sup over ALL laws, only a lower bound for the least beta from this family.
Files: ~/codex_fleet/runs/own_p0434/dinf_formula.py, dinf_ahigh.py, dinf_max.py, dinf_peakcheck.py, beta_direct.py (+ .out),
NOTE.md sections 12:5x and 13:1x. Supersedes [[p0434_least_beta_for_twice_waiting_plus_residence_is_about_0_035_2026_11_08]].
Related: [[p0434_worst_family_excess_sits_in_the_small_classes_2026_11_08]].


Update 13:2x: three small atoms with ties at ages 1 and 1+g (tri_scan.py) stay below the two-atom value - the second tie forces g ~ b/(a(1-a)) and D -> two-atom value from below as b -> 0. Not a sup over all laws yet; the large-class load profile is untested.

Update 13:3x: the large-class load profile was then tested (profile_scan.py, n 1/2/4/8, load ~ q^j, q 0.1-10, 180 points): whole beta negative everywhere (best -0.076) though the small part reaches 0.156; in the limit the Riemann sum tends to the same integral whatever the profile. charge_tie.py: on the tie family the large classes give back exactly their doubled Gittins waiting Q_GL (c_large -0.9999) and the small excess is 0.48-1.09 Q_GL while Q_GL/R_G ~ 1/n, so a proof of T_MS <= 2Q_G + (1+beta)R_G must charge the small excess to R_G. Citable write-up: ~/codex_fleet/runs/own_p0434/LOWER_BOUND_0677.md (pushed, commit 0be37d36).
