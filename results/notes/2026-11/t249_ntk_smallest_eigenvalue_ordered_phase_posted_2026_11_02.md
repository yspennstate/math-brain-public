---
name: t249_ntk_smallest_eigenvalue_ordered_phase_posted_2026_11_02
description: T249 posted 2 Nov: smallest NTK eigenvalue of a deep tanh net, ordered phase (exact constant, strict positivity, unequal norms; order L chi_1^L credited to Xiao-Pennington-Schoenholz 2020) - repo ntk-smallest-eigenvalue-ordered-phase 8277f3d
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T01:43:30+02:00
  status: verified
  evidence: "git ls-remote github.com/yspennstate/ntk-smallest-eigenvalue-ordered-phase main = 8277f3d536a3 (2 Nov 01:3x); scripts rerun 2 Nov match paper numerics; ar5iv 1912.13053 Table 1/Sec 6.2/App B read 2 Nov"
---

T249 is posted as public repo github.com/yspennstate/ntk-smallest-eigenvalue-ordered-phase (commit 8277f3d, 2 Nov 2026 01:3x, author yspennstate). It holds the README, paper/t249.tex and t249.pdf, and code/t249_kappa_check.py, t249_ninput.py and t249_series.py. This is paper 4 of 10 for the top-ten papers loop (T-20261029-025).

Result: deep tanh net, infinite width, sigma_b^2>0, ordered phase chi_1<1, n distinct inputs on the fixed-point sphere:
lambda_min(Theta_L) = kappa * lambda_perp_min(-A) * L chi_1^L * (1+O(1/L)), with kappa = q* + B T*/chi_1, T* = q*/(1-chi_1), B = chi'(1).
Strict positivity: every Taylor coefficient p_k (k>=1) of the limiting gap profile Phi is > 0. Then Schoenberg and Chen-Menegatto-Sun make -A positive definite on 1-perp.
Unequal norms: chi_q < chi_1 gives the same asymptotics whenever lambda_perp(-A) > 0. Only >= 0 is proved there.

Prior art: Xiao, Pennington and Schoenholz, ICML 2020, arXiv:1912.13053. Table 1, Sec 6.2 and App. B Lemma 2 give the order O(l chi_1^l) of the bulk eigenvalues and the existence of the rescaled limit, for normalized inputs only. They give no constant and no strict positivity. The paper cites them in the abstract and the introduction, and claims only the constant, positivity and unequal norms as new.

Checks before posting: the three scripts were rerun on 2 Nov. The outputs match the numerics section: eight-input ratios 0.9443 (sw2 1.5, L 200) and 1.0604/1.0311/1.0208 (sw2 1.2); min p_k 1.54e-07 (1.2, 0.3) and 5.74e-06 (1.5, 0.05); A 0.42715. The banned-phrase grep and voice.py are clean. The pushed tree and the PDF streams carry no paths or emails.

How to apply: do not post T249 again. A follow-up would be strict positivity off the sphere, which is open. Records: PAPER_CANDIDATES.md row 4.

