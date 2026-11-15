---
name: p0175_free_conv_symmetric_unimodal_cauchy_case_and_cancellation_2026_11_15
description: "P0175 free convolution of symmetric unimodal laws: which cases are settled (semicircle, free Jurek, Cauchy), what the counterexample search covered, and why the Im G proof route needs cancellation"
metadata:
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T20:47:01+02:00
  status: provisional
  evidence: ""
---

P0175 (Hasebe-Ueda Conjecture 3.5: mu, nu symmetric unimodal => mu boxplus nu unimodal) stands open, with three
findings from 14-15 Nov that a next attempt should start from.

1. Settled cases: nu semicircle; both freely ID in the free Jurek class (Hasebe-Sakuma Thm 4.1, body read, semicircular
   part allowed); nu Cauchy C_g, where omega(z) = z + i g, G_{mu boxplus C_g}(z) = G_mu(z + i g) = Cauchy transform of the
   classical mu * C_g (Bercovici-Voiculescu 1993), unimodal by Wintner. The Cauchy case is the only heavy-tailed partner
   that is immediate.

2. Numerics find no counterexample: ~5,900 random 3-uniform pairs (search.py), 48 symmetric analogues of the one-sided
   strong-unimodality counterexample (fam2.py, rise exactly 0), hill-climb on elasticity (finds flatness, never a bump),
   and search3.py (atom + up to 8 uniforms, widths over six decades). The solver is not blind: the one-sided control
   nu = delta_0/100 + 0.99 U[0, L] shows its dip down to 1e-9 (ctl1.py).

3. The proof route "f = u(omega) with u = -Im G_mu / pi decreasing in |Re z| on every horizontal line" needs the
   coupling. f' = u_x a' + u_y b'; Re omega is NOT monotone on x > 0 in 4 of 5 test cases (a' down to -46), and u_y b' is
   positive on 65-97 pct of the grid at up to 0.18 of max |u_x a'|. f' <= 0 only through cancellation (route_im.py).
   Do not try to bound the two terms separately.

Files: 12_cognitive_architecture/math/trio_1011/op/P0175/ (NOTE.md is the running record; commits 77e7162, 9f7d8ff).
What would change this: a RISE line in search3_s*.txt that survives a finer grid and a tighter solver tolerance.

