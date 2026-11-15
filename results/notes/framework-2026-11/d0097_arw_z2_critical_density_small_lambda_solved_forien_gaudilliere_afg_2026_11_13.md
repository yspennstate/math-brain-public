---
name: d0097_arw_z2_critical_density_small_lambda_solved_forien_gaudilliere_afg_2026_11_13
description: "D0097 (Rolla ARW survey arXiv 1906.05037, first open problem after Thm 7.2: for unbiased walks on Z^2, prove zeta_c < 1 for every lambda and zeta_c -> 0 as lambda -> 0) is solved in print, both halves. Forien-Gaudilliere arXiv 2203.02476: zeta_c < 1 for small lambda and zeta_c -> 0 as lambda -> 0 in every dimension d >= 1, new for d = 2. Asselah-Forien-Gaudilliere arXiv 2210.04779: zeta_c < 1 for every lambda in every dimension, with small- and large-lambda upper bounds. Hu arXiv 2203.14406 gave Z^2 small lambda independently. The 13 Nov TSV row had cited only the second paper"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T18:22:59.478Z
---

D0097, rank 55 on the 200 list. Source: Leonardo T. Rolla, "Activated random walks on Z^d", Probability Surveys 2020,
arXiv 1906.05037, Section 7, first open problem after Theorem 7.2, PDF p.35. Theorem 7.2 gives, for transient walks
(d > 2), zeta_c < 1 for every lambda < infinity and zeta_c -> 0 as lambda -> 0. The problem: the same for unbiased walks
on Z^2.

Status 13 Nov 2026: solved in print, both statements (abstracts read from the arXiv API on 13 Nov).
- zeta_c -> 0 as lambda -> 0: Forien and Gaudilliere, "Active phase for activated random walks on the lattice in all
  dimensions", arXiv 2203.02476v2. Every d >= 1; the abstract says the result is new for d = 2. Method: fix the set of
  final sleeping sites, reduce to a density-one model, and dominate the torus stabilization time by the escape time of a
  negatively drifted one-dimensional walk (exponentially slow phase, then an active phase on the infinite lattice).
- zeta_c < 1 for every lambda: Asselah, Forien and Gaudilliere, "The critical density for activated random walks is
  always less than 1", arXiv 2210.04779v2 (Ann. Probab. 2024 per the earlier TSV row; journal not rechecked here). Every
  d >= 1, every lambda, with upper bounds in both regimes.
- Independent small-lambda proof on Z^2: Hu, arXiv 2203.14406 ("for small enough sleep rate, the critical density of the
  symmetric ARW on Z^2 is strictly less than one").
- In d = 1 the rate is known: Asselah, Rolla and Schapira, arXiv 1907.12694, c sqrt(lambda) <= zeta_c <= C sqrt(lambda).
  The sharp small-lambda rate on Z^2 is not part of D0097 and was not checked here.
- The TSV row written earlier on 13 Nov (from the six-already-solved sweep by an agent) cited only 2210.04779, which
  covers the first half. This memory adds the second half; the problem is closed either way.

Related: [[d0093_arw_cycle_linear_toppling_open_codex_no_progress_2026_11_13]] (previous item in this loop, same survey);
[[p0383_arw_wired_infinite_volume_incompressibility_open_pi_existence_open_2026_11_13]] (ARW).
