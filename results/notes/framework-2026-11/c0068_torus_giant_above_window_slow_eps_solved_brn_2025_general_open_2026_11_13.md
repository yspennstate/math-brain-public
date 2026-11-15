---
name: c0068_torus_giant_above_window_slow_eps_solved_brn_2025_general_open_2026_11_13
description: "[PROVISIONAL] C0068 high-d torus giant above the window: solved for eps*V^{1/3} -> infinity slowly (Blanc-Renaudie-Nachmias arXiv 2512.19672 Cor 1.3); any eps=o(1) open, in their words"
metadata:
  type: project
status: provisional
---

C0068 on the 200 list (Heydenreich-van der Hofstad survey): torus Z_n^d, d>6, p = p_c(1+eps), V^{-1/3} << eps -> 0;
prove |C_max|/(eps V) -> c and |C_(2)|/(eps V) -> 0 in probability.

Read 13 Nov 2026 from the arXiv HTML of Blanc-Renaudie and Nachmias, "Critical percolation on the discrete torus in
high dimensions", arXiv 2512.19672 (Dec 2025). Setting: nearest-neighbour with d large, or spread-out with any d>6.
- Theorem 1.1/1.4: inside the window p = p_c(Z^d) + C lambda n^{-d/3}, the largest clusters over C' n^{2d/3} converge
  to Aldous's excursion lengths. This proves the conjecture of Heydenreich-van der Hofstad (their Open Problem 13.5).
- Corollary 1.3: for p = p_c(Z^d) + eps_n with eps_n V^{1/3} -> infinity SLOWLY ENOUGH, |C_1| * C_2 C_1/(2 eps_n V) -> 1
  and |C_j| ~ 2 C_1^2 C_2 log(eps_n^3 V)/eps_n^2 for j >= 2, in probability. C_1, C_2 are the susceptibility amplitudes.
  The proof is Theorem 1.1 plus Bollobas 1984 and Luczak 1990.
- Their own words after Cor 1.3: showing this for every eps(n)=o(1) with eps(n) >> V^{-1/3} "remains an open problem".
  The order of magnitude for V^{-1/3} << eps << (log V)^{-C} is announced in upcoming work by the first author.

Status: PARTIAL. Solved in the slowly-growing regime (eps measured additively, so p_c(1+eps) differs by a factor p_c).
The constant is 2/(C_1 C_2), not stated as theta'(p_c+); identifying it with the right derivative of theta is a
separate check. Open for general eps. The hypercube analogue is van der Hofstad-Nachmias (JEMS 2017).

Would change this: the announced Blanc-Renaudie paper, or Blanc-Renaudie-Hutchcroft (super-Brownian limits, in progress).
