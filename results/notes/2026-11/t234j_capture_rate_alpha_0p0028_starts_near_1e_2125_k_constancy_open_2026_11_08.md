---
name: t234j_capture_rate_alpha_0p0028_starts_near_1e_2125_k_constancy_open_2026_11_08
description: "Where does small-alpha GD capture start on T234 (T234j)? Near alpha 1e-2125: the saddle approach decays as alpha^0.0027913, far below float64; K constancy still open"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T16:10:45+04:00
  status: verified
  evidence: "frontier T234 pushes f00132cf63 5868732280; card claim_97da5c49; t234j_check.out"
---

Why did small-alpha GD on the T234 instance (d=40, n=60, step 1/20) look so slow to settle on the captured endpoint, and where
does capture actually start? Because the approach to the saddle shrinks only like alpha^0.0028. Codex OPEN-T234j (8 Nov)
derived kappa_X = gamma 2a/(2b+a) = 0.0027913 (gamma = 0.0847680 from the origin rates, a and b the slow stable and
transverse rates at the saddle) and measured 0.0027914 with a scaled solver that reaches alpha = 1e-20000. The 1e-6 matching
allowance T234i used is first met between alpha 1e-2125 and 1e-2150. So no start a float64 computation can make (alpha >=
1e-308) is anywhere near the captured regime; T234i's 0.3408 bound describes no run we can do in ordinary floats.

My check (t234j_check.py): gamma recomputed from the 70-digit eigenvalues to 2e-15; closest-approach slopes from the worker's
own table 0.0027915, 0.0027913, 0.0027912 per power of ten; at alpha 1e-150 its endpoint (excess 0.440192, closest approach
0.166542) matches my separate T234i rebuild (0.440, 0.167).

Still open: whether the outgoing family K is constant (nine phases agree to 7.3e-31, at the double-double floor, which is
evidence not proof), and a cutoff valid for every smaller alpha. A finite-alpha rank-40 lemma for generic full-width
endpoints is author-audited only. 220 paired Gaussian runs at 11 alphas show no alpha-independent excess law.

Pushed f00132cf63 (row, review, check) and 5868732280 (worker folder). Card claim_97da5c49352f48a2a281429ed6276f78, depends on
the T234i card. Predecessor: [[t234i_full_width_capture_asymptotic_only_regime_below_float64_2026_11_08]].

