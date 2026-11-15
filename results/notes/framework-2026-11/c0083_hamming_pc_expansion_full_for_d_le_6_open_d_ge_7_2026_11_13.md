---
name: c0083_hamming_pc_expansion_full_for_d_le_6_open_d_ge_7_2026_11_13
description: "[PROVISIONAL] C0083 Hamming p_c expansion: full for d=4,5,6 (FHHH CPC 2020), open for d>=7 (terms to n^{-d/3} unproved)"
metadata:
  type: project
status: provisional
---

C0083 on the 200 list (Heydenreich-van der Hofstad survey): show p_c(K_n^d) = sum_{i<=d/3} a_i(d) n^{-i} + O(n^{-1-d/3}).

Literature checked 13 Nov 2026 (web search, two queries; not a full arXiv sweep):
- Federico, van der Hofstad, den Hollander, Hulshof, "Expansion of percolation critical points for Hamming graphs",
  arXiv 1701.02099, Combin. Probab. Comput. 29 (2020) 68-100. Second-order term identified, error O(m^{-1} V^{-1/3})
  = the critical-window width. Their own remark: for d = 4, 5, 6, m^{-3} = O(m^{-1}V^{-1/3}), so their formula is the
  full asymptotic expansion there. Upper bound by lace expansion, lower bound by comparison with branching random walk.
- Heydenreich-Matzke (CPC 2022) do three terms for site percolation on Z^d in 1/(2d); not the Hamming graph.
- No 2021-2026 paper found extending the Hamming expansion past second order.

Status: solved for d <= 6 (in print), OPEN for d >= 7, where terms n^{-3}..n^{-floor(d/3)} are needed. The obstacle
is the lower bound: the branching-random-walk comparison gives one order; each extra order needs the lace-expansion
coefficients to that order matched from below.

Would change this: an arXiv paper after 2020 on "Hamming graph" + "critical point" + "expansion". Low-priority as a
paper target (heavy lace-expansion bookkeeping).
