---
name: p0186_coefficient_dimension_gap_eoN_vs_eCN2_open_2026_11_13
description: "P0186 (van Handel strong-convergence survey arXiv 2507.00346 Sec 6.6 p.68: optimal coefficient dimension D_N for strong convergence of GUE/Haar polynomials) is open on 13 Nov 2026. The gap is exact: strong convergence holds for D_N = e^{o(N)} (Chen-Garza-Vargas-Tropp-van Handel polynomial method; CGvH II arXiv 2412.00593 for GUE/GOE/GSE, Haar up to log factors) and can FAIL for D_N >= e^{C N^2} (Pisier 2014). Nothing in 2025-26 enters the gap: Parraud 2410.04481 reaches only e^{o(N^{2/3})}; Caspers-Chen 2607.15100 get dimension-uniform convergence for a different (graph-product) model. The survey names a basic obstacle past subexponential D_N (expected outlier counts carry the multiplicity D_N; our P0186-A001 example)"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T16:57:35.913Z
---

P0186, rank 44 on the 200 list. Source: van Handel, "The strong convergence phenomenon", arXiv 2507.00346, Section 6.6
"The optimal dimension of matrix coefficients" (p.68), with the history in Section 5.4.1 (p.58). For noncommutative
polynomials in N-dimensional GUE or Haar unitary matrices with matrix coefficients of dimension D_N, what is the largest
growth of D_N for which strong convergence still holds?

Status 13 Nov 2026: open. The gap, as the survey states it (read in the arXiv PDF on 13 Nov):
- Holds for D_N = e^{o(N)}, by the polynomial method of Chen, Garza-Vargas, Tropp and van Handel (survey ref. [33]).
  Chen, Garza-Vargas and van Handel, "A new approach to strong convergence II. The classical ensembles", arXiv
  2412.00593: GUE/GOE/GSE with coefficients of dimension exp(o(N)), and Haar U(N)/O(N)/Sp(N) up to log factors. Their
  abstract calls this a sharp form of Pisier's subexponential-operator-space result.
- Can fail for D_N >= e^{C N^2}. Pisier, "Random matrices and subexponential operator spaces", Israel J. Math. 203
  (2014); the example is in [33, Appendix A].
- History (p.58): Haagerup-Thorbjornsen's quantitative bounds give D_N = o(N^{1/4}). D_N = N is what the Peterson-Thom
  application needs.
- The survey says there is a basic obstacle to going beyond subexponential dimension ([33, Sec 1.3.1]). Known methods
  control extreme eigenvalues through expected spectral statistics, and those statistics count outliers with
  multiplicity up to D_N. Our 6 Sep pass P0186-A001 (codex_20h) gives a toy example of exactly this: X_N = 1_{E_N} I_{D_N} with P(E_N) = e^{-N/2} and D_N = e^N has norm tending to 0 in probability while the
  expected outlier count diverges. That explains the obstacle; it does not settle the question.
- My arXiv check on 13 Nov: strong convergence with matrix coefficients, tensor, coefficient; matrix-valued
  polynomials; author searches for Parraud and Pisier. Nothing proves strong convergence beyond e^{o(N)} or failure
  below e^{CN^2} for GUE/Haar. Nearby work:
  - Parraud, arXiv 2410.04481: tensor GUE with coefficient dimension M = exp(o(N^{2/3})), weaker than e^{o(N)}; another
    proof of Peterson-Thom.
  - Caspers and Chen, arXiv 2607.15100 (Jul 2026): q-Gaussian matrix models for |q| < sqrt 2 - 1, with convergence
    uniform over all coefficient dimensions at fixed polynomial degree. This is a different (graph-product) model, and
    a possible lead for what "uniform in D" can look like.
  - Xiang and Zhang, arXiv 2608.04824 (Aug 2026): strong convergence of iid-entry matrices with finite fourth moment.
    Fixed coefficients only.
- Earlier work: OP16 brain-vs-no-brain test (06_math_research/op16_strong_2026_10_12/OP16_PARTIAL_RESULT.md, 12 Oct).
  Both arms were graded PARTIAL on P0186, and both referees put the brain arm ahead, 2 against 1. There is no Codex
  report for P0186 in referee_reports/2026-11-13.

Related: [[p0184_psl2z_projective_line_strong_convergence_open_random_c2c3_done_2026_11_13]] (same survey, previous
item).
