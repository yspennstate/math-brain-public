---
name: t012_interchange_3d_long_cycles_poisson_dirichlet_2026_11_02
description: T012 3D interchange: long-cycle phase sets in near beta 0.40-0.44 (L^2 cut), cycle shares at beta 2 move to PD(1) (0.641 vs 0.624); scar: exp(-mu) Poisson sampler underflow caps at ~745
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T06:49:47+04:00
  status: provisional
  evidence: "rows/T012/moves.jsonl 93a36eb5"
---

T012 (infinite cycles of the interchange process in d = 3, 4; proved d >= 5, Elboim-Sly 2211.17023), first frontier move, 2 Nov 2026, an agent. Move m012a, rows/T012/moves.jsonl 93a36eb5; t012_interchange.c, t012_cross.py and runs in 06_math_research/frontier/rows/T012.

- Setup: d = 3 tori, L 8-32. f_long is the fraction of vertices in cycles longer than L^2.
- f_long falls with L below beta 0.35 and rises with L at 0.45. The curves cross at beta 0.40-0.44, a location that depends on the cut.
- Deep in the phase (beta 2) the largest and second-largest cycle shares are 0.6411 and 0.2178 at L 32, moving with L toward PD(1)'s 0.6243 and 0.2095.
- PREREG84: (a) crossing in 0.25-0.40 MISSED; b and c passed.
- SCAR, caught before any result was kept: a Poisson sampler using exp(-mu) underflows for mu in the hundreds or more, and the multiply-uniforms loop then stops near 745. It looked like 'no long cycles at L 12, beta 1.2' while L 16 at beta 1.0 had 89%.
  - It was spotted because two sizes disagreed in a way no physics allows.
  - Use the normal approximation, or split mu, above about 50.
- d = 4 not run. Same pattern as [[t006_fpp_chi_0p31_xi_0p67_kpz_relation_holds_2026_11_02]].


ADDENDUM (2 Nov 06:53, move m012b): d = 4, L 6-16.
- The long-cycle phase sets in near beta 0.26, against 0.40-0.44 in d 3.
- At beta 2, L 16, share1 = 0.6251 and share2 = 0.2134, against PD(1) 0.6243 and 0.2095.
- PREREG85: 3 of 3 passed.
