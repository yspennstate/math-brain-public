---
name: p0323_circular_riesz_dlr_settled_in_print_for_s_below_1_2026_11_17
description: "[VERIFIED] P0323 circular Riesz DLR: settled for 0<s<1 by Boursier v5 (Oct 2026) + Dereudre-Vasseur AoP 2023; s>1 not stated, classical route (Georgii 1995) unchecked"
metadata:
  type: project
  created: 2026-11-17
  created_at: 2026-11-17T01:45:08+02:00
  status: provisional
  evidence: ""
---

Is P0323 (DLR equations for the thermodynamic limit of the circular Riesz gas, Boursier arXiv 2209.00396) still open? For 0<s<1, no: it is settled in print by the source's own v5 (27 Oct 2026), Sec 1.6.5. Dereudre and Vasseur (Ann. Probab. 2023, arXiv 2104.09408, Thms 1.8, 1.11, 1.14) built a subsequential limit of circular Riesz gases for 0<s<1 that satisfies the canonical and grand-canonical DLR equations and is not number-rigid; v5 Theorem 3 proves the whole sequence converges (s in (0,1) u (1,inf)), so the limit is that DLR solution. v4 (19 Jul 2023) Sec 1.3, which our list quoted, still posed DLR as the next step; v5 no longer does.

Left: s>1 (hypersingular, tail summable). v5 says nothing about DLR there. Expected by the classical route (positive, superstable, regular pair potential with periodic boundary; Georgii 1995 J. Stat. Phys. 80, equivalence of ensembles, says limits of canonical Gibbs measures are grand-canonical Gibbs) but I have not checked that Georgii's hypotheses cover the singular kernel |x|^{-s} at the origin. That check is the next step, not a result.

Recorded in open_problems_200_2026_10_10/LITERATURE_UPDATES.tsv (row P0323, 17 Nov). Lesson, again: our list was drawn from an older arXiv version; read the newest version before attacking a list item. Related: [[open_problem_check_must_search_the_web_not_only_arxiv_titles_2026_11_16]], [[intake_ledger_blind_to_posted_papers_filter_by_repo_readmes_2026_11_13]].


Update 17 Nov 02:0x, s>1. The hypotheses of the classical route are verified: phi=|x|^-s in d=1 with s>1 satisfies Georgii's (A1) regular and (A2) non-integrably divergent at 0 (J. Stat. Phys. 80, 1995, Sec 2.1; preprint mp_arc 94-314), and Boursier's kernel (1.1)-(1.2), rescaled to a circle of length N, is Georgii's periodic Hamiltonian (2.5). But no theorem in print covers Boursier's ensemble (fixed N, fixed beta, positions only): Georgii 1995 proves limits for microcanonical (N,E) with momenta, and Georgii PTRF 99 (1994) Thm 4 needs N in a non-degenerate density interval; the canonical case is a remark there ("left to the reader"). So s>1 stays open in print, likely routine. The reduction sketch and its one load-bearing step (exact-N canonical free-energy limit under periodic boundary conditions) are in the ledger row of LITERATURE_UPDATES.tsv. Checked: Boursier's C_N (Sec 1.4) is the rescaled configuration in a window around a fixed point (the origin of the circle), not around a particle, so its law is rotation-invariant and matches Georgii's periodised stationary measure; no Palm transfer is needed. Boursier cites no fixed-N DLR result for s>1.
