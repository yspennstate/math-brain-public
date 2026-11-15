---
name: d0046_virag_q8_tridiagonal_dynamics_frozen_edge_refereed_2026_11_13
description: "[PROVISIONAL] Virag Question 8 (operator limits of Hermitian Brownian motion): two audits PARTIAL obstruction. Reversible Dumitriu-Edelman tridiagonal dynamics freeze the edge on DBM edge time; Q8 itself open."
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T09:44:19+02:00
  status: provisional
  evidence: ""
---

status: provisional
Two audits on 13 Nov: claim run D0046A (PARTIAL), referee D0046AR (MINOR). Ledger row in probability_1000_intake_D.
Proved: a stationary reversible Markov process on beta=2 Dumitriu-Edelman tridiagonal matrices (GUE eigenvalue law at each time; the process itself is prior work) has edge eigenvalues that do not move on the DBM edge time scale n^{-1/3}, uniformly on compacts in mean square, so it cannot converge to the Airy line ensemble. Extends to reversible tridiagonal diffusions with the same independent entry law and a uniformly bounded covariance OPERATOR (bounded entries alone are not enough; ordered DBM particles on a diagonal are a counter-picture outside the hypotheses). Lanczos tridiagonalisation of invariant Hermitian BM is Markov on the cyclic locus as an orbit quotient.
Referee fixes: physical time s n^{-1/3} is standard Airy time s, not 2s; say GUE eigenvalue law, not GUE matrix law; supply the Borel kernel for the quotient and do not claim cyclicity at all times at once.
Question 8 (Virag, arXiv 1804.06953, p. 25) is neither answered positively nor refuted; no printed answer found through 2026.
Related: [[d0040_nested_beta_laguerre_jacobi_matrix_refereed_2026_11_13]] [[d0043_virag_exotic_edge_operator_disproved_baslingker_2025]]

**Published 13 Nov 13:5x:** paper "Frozen edges of stationary tridiagonal dynamics with GUE spectra", https://github.com/yspennstate/tridiagonal-edge-freezing commit 50fed95, Zenodo 10.5281/zenodo.24194789; ResearchGate queued (Q/tridiagonal-edge-freezing). Do not write a second paper on D0046; a v2 goes through a Zenodo new version.
