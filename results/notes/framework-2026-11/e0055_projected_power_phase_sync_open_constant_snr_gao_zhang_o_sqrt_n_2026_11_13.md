---
name: e0055_projected_power_phase_sync_open_constant_snr_gao_zhang_o_sqrt_n_2026_11_13
description: "E0055 (Bandeira Open Problem 10.1: for which sigma does the projected power method for Y = zz* + sigma W converge) is partly in print on 13 Nov 2026: spectral start, iterates reach and keep the optimal error (1+o(1)) sigma^2/2 for every sigma = o(sqrt n) (Gao-Zhang IEEE TIT 2021, arXiv 2010.04345 Thm 1.1/3.1); convergence to the MLE itself only for sigma <= c sqrt(n/log n) (Zhong-Boumal 2018). Open: constant SNR sigma = c sqrt(n), MLE convergence between the two scales, random starts"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T15:27:45.545Z
---

E0055, rank 36 on the 200 list. Source: Bandeira, "Ten lectures and forty-two open problems", Open Problem 10.1
(ETH copy p.133). Y = zz* + sigma W, z in the complex unit-modulus vectors, Algorithm 10.1 = z <- normalize entrywise(Y z).
The question: for which sigma does it converge w.h.p. to the MLE, or at least to an estimate well correlated with z.
No numerical threshold is conjectured there.

In print, theorems read 13 Nov 2026 in the arXiv PDFs:
- Zhong and Boumal, SIAM J. Optim. 28(2) (2018), arXiv 1703.06605: spectral start, linear convergence to the global
  maximizer (the MLE) for sigma <= c0 sqrt(n/log n).
- Gao and Zhang, "Exact minimax estimation for phase synchronization", IEEE TIT 67(12) (2021), arXiv 2010.04345,
  Theorem 1.1 (p.3) and Theorem 3.1 (p.7). They assume sigma^2 = o(np) and np/log n -> infinity, with entries observed
  with probability p. The power method starts from the normalized leading eigenvector (eq. 16). After a few iterations
  the error is at most (1+o(1)) sigma^2/(2p), which matches the minimax lower bound. At p = 1 this covers every
  sigma = o(sqrt n), the whole regime where nontrivial recovery is of smaller order than n. Their algorithm zeroes the
  diagonal, and the result bounds the error of the iterates. It does not show that the iterates converge to one point
  or to the MLE. The Codex E0055A report notes the same caveat.
- Zhang, arXiv 2209.04962 (2024): the plain spectral estimator already reaches the same exact minimax constant, so in
  the o(sqrt n) regime the iteration adds nothing to the error constant.
- Related, other group: Huroyan and Lerman, arXiv 2609.09502 (Sep 2026). For the projected power method in permutation
  synchronization they prove one-step contraction from any start in a majority basin. This is the kind of
  basin-of-attraction statement a random-start answer for U(1) would need.

Still open:
1. Constant SNR, sigma = c sqrt(n). The spectral start correlates with z exactly above the BBP point. Whether the
   projected power method then converges, and to what overlap, is open. AMP has a state-evolution theorem. For the
   plain iteration no theorem turned up in arXiv searches (power method / generalized power method / projected power
   method with phase or group synchronization), in a web search, or in the Codex run's search through 2026.
2. Convergence to the MLE itself for sqrt(n/log n) << sigma << sqrt(n).
3. Random starts, at any noise level that grows polynomially in n.

Our earlier work: the 8 Sep intake attempt E0055-A001 and the Codex run E0055A on 13 Nov
(06_math_research/referee_reports/2026-11-13/E0055A/REPORT.md). That run cites Gao-Zhang correctly. Before this memory,
the ledger line named only Zhong-Boumal.
Related: [[e0053_maxbis_minbis_open_equals_zdeborova_boettcher_via_aronow_lopatto_2026_11_13]] (the previous Bandeira
item on the list).
