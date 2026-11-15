---
name: t128_critical_band_matrices_complex_block_solved_ghosal_remy_real_open_2026_11_14
description: "T128 random band matrices at W~sqrt N: critical crossover law proved for complex Gaussian block band matrices (Ghosal-Remy arXiv 2611.15085, 11 Nov, Lean); real symmetric model open; T129 adds 2610.39424"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T10:55:22+02:00
  status: provisional
  evidence: ""
---

T128 on the top-200 list (random band matrices at the critical bandwidth W = c sqrt N; Fyodorov-Mirlin crossover) is solved for the complex Gaussian block model and still open for the real symmetric model the row states.

- Ghosal and Remy, arXiv:2611.15085 (posted 11 Nov 2026, 302 pages, autoformalized in Lean 4 by AxiomProver, abstract only read): for N x N complex Gaussian band matrices in the Yau-Yin periodic block form, QUE for bulk eigenvectors whenever W^2/N -> infinity, and at N/W^2 -> tau the bulk eigenvalues and block-mass eigenvector profiles converge jointly to a law fixed by the DMPK diffusion of the unitary class; sine as tau -> 0, Poisson as tau -> infinity.
- Fan-Zou arXiv:2609.23389 gives Poisson bulk statistics for real Gaussian band matrices when W^2 << N/log N (already on the row).
- Open: the orthogonal class (real symmetric), and the sharp band profile rather than the block form.
- Row text updated in rows_11.py (top200_probability_2026_10_14), pushed in push 212; status row in top200_vet_agent_2026_11_11/STATUS_1114.tsv.

Same tick: T129 (symmetric sign matrix singularity, base 1/2) still open; Liang-Yu-Yu arXiv:2610.39424 prove P(rank <= n-k) <= 2e^{-c nk} for all k and reprove the exponential bound.

Hint for the next reader: the 302-page claim is unrefereed and I read only the abstract. Before calling T128 "half solved" in anything public, read its main theorem statement for the exact model.

