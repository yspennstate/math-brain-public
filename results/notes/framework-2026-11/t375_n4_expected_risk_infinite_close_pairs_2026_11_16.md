---
name: t375_n4_expected_risk_infinite_close_pairs_2026_11_16
description: "[PROVISIONAL: proved, checked numerically, not independently audited] T375 min-cost (OWSS R-norm) interpolant in d=2 at n=4: a.s. unique, one ReLU plus affine by duality; close pairs with different labels give P(risk>M)>=c/M so E[risk]=infinite. Tent (3 sites within r) cannot: tail M^-2. n>=5 open."
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T18:44:39+02:00
  status: provisional
  evidence: ""
---

At n=4 in R^2 the interpolation constraints mod affine reduce to one functional D (c_i = signed areas), so min cost = |D(y)|/max_L |D sigma_L| and minimizers sit on maximizing lines. 18 candidate maximizer values, pairwise distinct at a random rational point (exact Fractions) -> ties null -> unique minimizer l + a sigma. Event: pair within delta in the central square, other two well conditioned, labels differ by 1: prob ~delta^2, |a| >~ 1/delta, risk >= kappa a^2/4 (compactness over lines meeting the centre). File 06_math_research/frontier/rows/T375/N4_INFINITE_EXPECTATION.md, scripts n4_checks/. Scar caught by the advisor: my first plan was a quantitative tent modulus; the tent's event is order r^4, an integrable tail, so it could never decide the expectation - check the probability-vs-risk scaling of a mechanism before trying to make it quantitative. Open: n>=5, where a narrow two-kink ramp (bounded risk) competes with the steep kink. Related: [[t375_fixed_n_large_risk_events_by_consistent_extra_samples_2026_11_16]]
