---
name: mossel_odonnell_open_problem_1_one_bit_optimal_n_le_9_certified_2026_11_15
description: "[VERIFIED] Mossel-O'Donnell 2005 Open Problem 1 (MAJ1 best antisymmetric protocol, 2<=k<=9): YES for n<=9; NEW only for 6<=k<=9 (k<=5 is Yu PTRF 2023 Cor 2); public repo cosmic-coin-flipping-nine-bits v1.0.1, two referees"
metadata:
  node_type: memory
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T07:45:17+02:00
  status: verified
  evidence: github.com/cosmic-coin-flipping-nine-bits v1.0.1 (40cef969); referees CCFR and CCF2 both sound with minor fixes, all applied
  modified: 2026-11-15T08:48:20.376Z
---

Mossel-O'Donnell, Coin flipping from a cosmic source (RSA 26 (2005) 418-436), Open Problem 1: for 2<=k<=9 is everyone outputting x_1 the best antisymmetric protocol? Answer YES for n<=9, certified 15 Nov 2026. Maximizers are exactly x_i xor b (needs the input complementation of Thm 1.4's signed permutation; i = pi^{-1}(1), b = b_i).

PRIOR WORK, found by the first referee and checked: L. Yu, On the Phi-stability and related conjectures, PTRF 186 (2023) 1045-1080, doi 10.1007/s00440-023-01209-5, Corollary 2: dictator maximizes symmetric alpha-stability over ALL balanced functions for alpha in [2,5], every dimension, every rho. That is k=4,5 for every n. k=2 Witsenhausen, k=3 MO05 Thm 1.3. So the new content is 6<=k<=9 for n<=9. Before claiming a noise-stability or NICD case is open, search Yu's Phi-stability papers.

How: their Theorem 1.4 reduces to one shared left-monotone f. Put t=2e/(1-2e); then P_k(f) = 2^{1-n} R_{f,k}(t)/(2(1+t))^{nk} with R = sum_x q_x^k, q_x nonnegative integer polys. Coefficients t^0, t^{nk-1}, t^{nk} of R are the same for all balanced f, so positivity of coefficients 1..nk-2 of R_MAJ1 - R_f proves the inequality on all of (0,1/2). Double precision is rigorous because everything is nonnegative (Higham Lemma 3.1, m=(k-1)(n+2)+2^n+1 roundings; q coefficients are integers <= 4^n so exact under any order/FMA; code test c > 2*gamma*(A+B), gamma=4mu/(1-mu), rounded test still implies c > gamma_m (A+B)).

Numbers (measured, results/ in the repo): 1,1,2,3,7,21,135,2470,319124 functions for n=1..9 (OEIS A109456). n=9: all certified for k=2..9 (~20 min), min relative margin 4.9e-5 (k=2). Margins 7.9e-3..4.9e-5 for n=3..9, ~2.5x smaller per bit. Exact sympy check n=3..8, k=4..9. Float grid n=7,8 minima 1.6e-2, 8.2e-3. n=5 k=10: rejects MAJ3 (beats MAJ1) and MAJ5 (below MAJ1 but a negative coefficient); k=11 MAJ3, MAJ5 both beat MAJ1. n=10 has 1.2e9 functions: out of reach.

Where: public repo cosmic-coin-flipping-nine-bits tag v1.0 (paper/, code/, results/). Two independent referee passes (CCFR, then CCF2). CCF2 re-derived Lemma 3.1 and the m count (even (k-1)(n+2)+2^n-1 suffices), reran n=5,6,7 float and n=5,6 exact (identical JSON), and asked only for wording: Cor 2.2 needs f antisymmetric and nk>=3 (vacuous at n=1,k=2), the float model needs "no underflow", the README had f/g vs n json reversed. Fixed in v1.0.1, plus the reference Li-Medard IEEE TIT 67 (2021) 778-789. Zenodo post handed to an agent 15 Nov. What would still change it: an error in the rounding bound or in the reduction. Related: [[p0165_monotone_gap_closed_by_mossel_odonnell_2005_n7_not_new_2026_11_15]]


ZENODO: 10.5281/zenodo.24242991, published 15 Nov 2026, title 'One bit is optimal for cosmic coin flipping on at most nine bits', linked to the GitHub tree 40cef969 (checked against the Zenodo API 15 Nov).

Plain words (how a non-specialist might ask): many people see a noisy copy of the same coin flips and each must output one bit; best way to agree; is majority vote the best rule; checked by computer for up to nine people.
