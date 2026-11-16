---
name: t007_wolff_fixed_cluster_count_xi_matches_alles_2026_11_02
description: T007 2D O(3): Wolff measured after 'V spins flipped' (state-dependent stop) biased xi 5-9% high; fixed cluster count gives xi within ~1% of Alles 1808.08129 (34.75 at beta 1.7), slope 6.50 near 2 pi
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T07:32:19+04:00
  status: verified
  evidence: "rows/T007/moves.jsonl c8b9c471"
---

T007 (Polyakov: 2D O(N), N >= 3, has a finite correlation length at every beta), correction move m007b, 2 Nov 2026, an agent. rows/T007/moves.jsonl c8b9c471. It supersedes the numbers in [[t007_o3_xi_slope_levels_near_2pi_beta_1p5_1p7_2026_11_02]].

- SCAR: a Wolff run must measure after a FIXED number of clusters. Measuring after "enough clusters to flip V spins" uses a state-dependent stopping time. The crossing cluster is size-biased, and big clusters come from ordered states, so chi and xi came out 5-9% high, growing with beta.
  - The cluster kernel was correct: it passed the exact 1D ring test.
  - That test missed the bug because it measured every 10 clusters.
  - Lesson: a correctness test must use the same measurement schedule as production.
  - What caught it: checking the absolute values against a published table, Alles et al. 1808.08129 Table 1, which the first move had only recalled.
- Corrected xi at beta 1.2-1.7: 3.230, 4.628, 6.619, 11.038, 19.278, 34.754.
  - Within +-1.1% of Alles log-interpolated, except 1.4 at -3.4%, 2 se. Log-linear interpolation of a convex ln xi overestimates, which is the same sign.
- The local slope of ln(beta xi) is 5.80, 6.22, 6.50 over 1.4-1.7, against 2 pi = 6.28. The prefactor levels at 0.0083-0.0085.
- PREREG88: (a) MISSED by the 1.4 point; b and c passed.
- The PDF of hep-lat/9411009 would not text-extract here: no pdftotext or PyMuPDF, and its fonts defeated a stream dump. ar5iv HTML pages worked.

