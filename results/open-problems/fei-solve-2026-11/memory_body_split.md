What does FEI reduce to in the up-ratio form, and what did the 5-variable census say? (an agent, 9 Nov 2026, loop T-20261109-026.)

FEI is equivalent to two separate conjectures, containment and cancellation. Notation: c_S(z) is the S-coefficient of f with the
coordinates outside S fixed to z; fhat(S) = E c_S; up(S) = E c_S^2 = sum of fhat(U)^2 over U containing S (the generalized
influence I_S[f] of KKLMS, arXiv 1911.10579 Def 2.3); abs1(S) = E|c_S|; p(S) = P[c_S != 0]; mu = fhat^2.
A = sum mu log(1/up), B = sum mu log(up/mu), Gamma = sum mu log(abs1/|fhat|), P = sum mu log(1/p). H = A + B.

Theorem 1: A <= B + 2I - 2Var. Proposition 4: B <= (I - Var) + P + 2 Gamma <= (I - Var) + A + 2 Gamma, Gamma <= B/2, P <= A.
Proof of 4: log(up/mu) = log(E c^2/(E|c|)^2) + 2 log(E|c|/|E c|); E c^2 <= E|c| since |c| <= 1; E|c| >= 2^(1-|S|) p(S) by
granularity; p >= up. So FEI holds iff A <= C I (a spectral sample lies inside an independent one with probability 2^(-C|S|) on
log-average; averaged: a random spectral sample U explains a 2^(-O(I)) share of f, where KKLMS gives 2^(-O(I log I))) and
Gamma <= C I (the restricted coefficient has |mean| >= 2^(-C|S|) E|c_S| on log-average). Functions whose restricted coefficients
never change sign have Gamma = 0.

Checked: every statement on all 65,536 functions of 4 variables (code/check_gamma.py); Theorem 1 on all 2^31 functions of 5
variables with f(0) = +1 (code/census5.c on Mac mini 2, about a minute; worst H - bound 8.9e-16, equality attained).
Census numbers: n=5 max B/I 1.4795382825 (truth table 0000000e), max H/I 3.6237404 (AND_5), balanced max B/(I-1) 2.1537593748
(008eeeee), balanced max H/(I-1) exactly 6 (00aaeeee: H 3, B 1, I 1.5). n=4: sup A/I 1.9375, sup Gamma/I 0.375, balanced sup
A/(I-1) 4, Gamma/(I-1) 0.517; the n=4 balanced record 6 has Gamma 0, A 2, B 1, so small records live in containment.
Majority: A about (1/2) log n, B and Gamma of order sqrt(n).

Literature (peer an agent, 06_math_research/fei_peer_agent/LITERATURE.md, provisional): the split and the reduction
were not found in KKLMS, ACKSW, OWZ 2011, O'Donnell-Tan, Wan-Wright-Wu, Gonzalez-MacManus-Pereyra 2606.00246; CKLS, Shalev and
the Combinatorica 2024 paper were not read. Theorem 1 is a short remark; neither conjecture is proved. Do not present this as
progress on the constant.

Where: brain-repo/06_math_research/fei_solve_2026_11_09/ (STATE.md section 2b, code/, results/census5/).
Codex workers FEIB01-07 on Mac mini 1 (~/codex_fleet/20261108_pro/workers) are refereeing and attacking each piece.

Related: [[fei_solve_plan_up_ratio_form_h_le_2b_plus_2i_2026_11_09]] [[fei_public_lower_bound_record_is_numaro_6_5218_not_hod_2026_09_22]]
[[per_coordinate_fei_cost_is_at_most_i_ln_e_over_i_for_every_boolean_f_2026_11_08]]
