---
name: g0013_every_permutation_n_le_9_proved_exact_laguerre_certificate_2026_11_08
description: "G0013 (A_n) proved for every permutation n<=9: exact Laguerre-cell dual/primal certificate, 46,065 classes at n=9, min margin 2.824e-3; public c4a52932, ledger 7058371b"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T02:05:20+02:00
  status: verified
  evidence: "G0013/sd_exact_n3..9.out, sd_exact_ctrl.out"
---

G0013 (Catalano-Lavenant / Schrott Conj. 1.1, the statement (A_n): the identity is farthest from lambda x lambda among n-point grid permutation measures) is now PROVED for every permutation with n <= 9, in exact rational arithmetic, and public.

Method (papers_agent/G0013): semi-discrete W2 between the n grid points and the uniform law on the square, computed from Laguerre cells clipped to the square, Newton on the concave dual with the analytic Hessian -L_ij/(2|p_i-p_j|) (sd_fast.py, ~3 ms per permutation, max 6 Newton steps). Certificate (sd_exact.py): weights rounded to 2^-40; exact dual LOWER bound for W2^2(id); for one permutation per class under the square's 8 symmetries an exact primal UPPER bound W2 <= sqrt(C) + sqrt(2e) (cell-to-point coupling cost C plus excess mass e moved at most sqrt 2). Class counts 1,6,22,114,693,5281,46065 for n=3..9 (= OEIS A000903 less the id/rev class), all ok. Minimum certified margins in W2^2: n=6 7.79e-3, n=7 5.30e-3, n=8 3.79e-3, n=9 2.824e-3, always at the corner adjacent transposition (012345687 at n=9; float gap 2.827e-3, so rounding + excess cost < 3e-6). Negative control sd_exact_ctrl.py: id and rev do not separate. Units: A_n gap = (W2^2(id) - W2^2(sigma))/2; n^2 * gap at n=9 = 0.1145.

Published: paper Proposition 4.11 (prop:small), 12 pp, 0 Overfull; yspennstate/wasserstein-layered-permutation-copulas c4a5293221ff78e4647123789f8db6cf72ab0679 ("Every permutation for n at most nine"); ledger open-problems-repo master 7058371b62dfa24147813253aeec9c2bc825683d [skip ci] (status still partial: general n open; n >= 10 covered only for permutations made of blocks of length <= 9).

Why it matters for the next step: this route needs no partition or interval proof, only one Newton solve per class, so it is limited by the 9!/8 class count, not by block structure. n = 10 would be ~450k classes (~10x n=9's ~25 min exact run), feasible on the workstation if RAM allows; the margin shrinks like ~0.11/n^2 so 2^-40 rounding stays far below it.

