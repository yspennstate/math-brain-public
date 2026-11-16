---
name: p0343_beta_splitting_leaf_correlation_ours_posted_no_overlap_lit_check_2026_11_13
description: "P0343 (Aldous-Janson II Open Problem 1, leaf-height correlation at separation n^alpha in the critical beta-splitting tree -> 1-alpha) is answered by our own paper (github yspennstate/beta-splitting-leaf-correlation, e337fd8, 15 Oct 2026); 13 Nov arXiv check of every beta-splitting paper through 2611.00347 finds no overlap. Same source's Open Problems 3 and 4 were solved by others (Chorbadzhiyska-Minchev-Savov 2608.18320 Thm 2.12, constant 2 and mixed Gumbel; Heng Ma 2609.14329, discrete height (log n)^2 C_ht ~0.976). Candidate citations for a revision: Brandenberger-Chin-Mossel 2505.24821, Aldous-Janson III 2412.09655"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T15:52:46.119Z
---

P0343, rank 38 on the 200 list. Source: Aldous and Janson, "The critical beta-splitting random tree II: overview and
open problems", arXiv 2303.02529, Open Problem 1 (PDF p.22). For two leaves r_n apart in the cyclic order, the
correlation of their continuous heights should tend to 1 - alpha when log r_n / log n -> alpha.

Status 13 Nov 2026: answered by us, posted, no outside overlap found.
- Our result: rho(n, r) = 1 - log r / log n + O((log n)^(-1/2)) uniformly in 1 <= r <= n/2, from
  Cov = sigma^2 log(n/r) + O(sqrt(log n)) and Var = sigma^2 log n + O(sqrt(log n)), sigma^2 = 2 zeta(3)/zeta(2)^3.
  Paper: github.com/yspennstate/beta-splitting-leaf-correlation, commit e337fd8 (15 Oct 2026). Second audit
  op15_paired_2026_10_11/second_audits/P0343 says CORRECT. problem_recall shows four runs, the first on 7 Sep
  (P0343-A001, partial).
- 13 Nov literature check: an arXiv abstract search for "beta-splitting" returned 18 papers through 2611.00347. On
  2608.18320, 2611.00347 and 2510.17343 I also ran a full-text grep for "correlat", "two leaves" and "pair of leaves".
  None of the 18 treats the joint law of two leaf heights.
- The same source's other problems, solved by others (neither is on our 200 list):
  - Open Problem 3 (maximum continuous height): Chorbadzhiyska, Minchev and Savov, arXiv 2608.18320, Theorem 2.12 and
    Remark 2.13. D*_n / log n -> 2, with mixed Gumbel fluctuations. They show the conjectured constant of about 1.878
    in AJ II eq. (41) is wrong.
  - Open Problem 4 (discrete height): Heng Ma, arXiv 2609.14329. L*_n / (log n)^2 -> C_ht = min_{theta>1}
    theta / (2(psi(theta) + gamma)), about 0.976.
  - Open Problem 7 (clade shapes): Brandenberger, Chin and Mossel, arXiv 2609.24973.
- Our bibliography cites Ald96, AJ II, AJ IV, Aldous-Pittel, Iksanov-Nikitin-Yakymiv and Kolesnik. It does not cite
  two related papers:
  - Brandenberger, Chin and Mossel, arXiv 2505.24821 (CLTs for tree statistics via the harmonic descent chain);
  - Aldous and Janson III, arXiv 2412.09655.
  Neither proves our theorem. Add both if the paper is revised (citation hooks C04/C12). The posted paper was not
  edited for this.

Related: [[e0057_mra_mle_consistency_marginal_known_quasi_mle_open_2026_11_13]] (previous item checked in this loop).

14 Nov 04:36: independent post-posting referee pass by an agent (Opus 5.5) on main.tex 23b0099, every lemma and the proof of Theorem 1.1 redone by hand, table and constants recomputed in mpmath, code/checks.py rerun byte-identical to the posted output: ACCEPT, two optional remarks (the two uncited papers above; make the filtering step for Q explicit). Report: 06_math_research/referee_reports/2026-11-14/P0343_posted_referee/REPORT.md.
