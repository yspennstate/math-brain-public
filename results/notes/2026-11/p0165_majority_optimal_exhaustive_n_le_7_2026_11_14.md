---
name: p0165_majority_optimal_exhaustive_n_le_7_2026_11_14
description: "[PROVISIONAL] P0165 (O'Donnell: is majority on an odd subset optimal for r players agreeing on eps-noisy copies?): no counterexample on all odd f n=5 and all 1,422,564 self-dual monotone f n=7, eps 0.01-0.49, r 2-1000; gap 8.9e-13 = round-off. Still open"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T12:45:13+02:00
  status: provisional
  evidence: ""
---

P0165, O'Donnell's open problem on many-player correlation distillation. Model: x uniform on {-1,1}^n, r players each see an eps-noisy copy, all apply the same odd f; agreement = E_x[p^r + (1-p)^r], p = (1 + T f)/2. Known: dictator optimal for r = 2, 3 (Mossel-O'Donnell-Regev-Steif-Sudakov, Israel J. Math. 154 (2006)). arXiv 2510.20013 and 2604.06590 are the erasure model, a different question.

14 Nov 2026 (an agent): exhaustive checks against the best of Maj_1..Maj_n on eps in {0.01..0.49} (14 values), r = 2..40 plus 50..1000:
- n=5 all 65,536 odd f: max excess 4e-14.
- n=5, 6 self-dual monotone (81, 2646 - OEIS A001206): 1.9e-13, 1.7e-13.
- n=7 all 1,422,564 self-dual monotone f (sdm7.py, chunked, Mac mini 1 fillq, 2200 s, ~300 MB): 8.9e-13 at eps 0.08 r 1000. Round-off; no non-majority beats a majority by more than 1e-9 anywhere.
Which majority wins moves with r (eps 0.1, n 5: dictator to r=12, Maj_5 from r=16).
Caveat: n=6,7 cover monotone odd f only; that compression toward monotone does not lower agreement is unproved (n=5 full search agrees).
Files: 12_cognitive_architecture/math/trio_1011/op/P0165/ (NOTE.md, STATUS.md, ex5.py, sdm.py, sdm7.py, outputs). Store card claim_810d519a21a76e34.
Next if resumed: a proof that monotone compression helps (would make n=7 a complete check), or n=8 needs the 2^37-ish monotone count - infeasible exhaustively; random search or local search over odd f on n=9..11 instead.
