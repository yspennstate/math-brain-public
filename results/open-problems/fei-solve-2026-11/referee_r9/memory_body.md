The FEIB31 monotone tower record holds: the word M,D,D,D,D,M,P,P,P,Q2,dual(PM(K4)),dual(T(4,3)),T(2,6),T(3,5)
(bottom to top; M = perfect matching on K3,3, D its dual, P = perfect matching on K4,4, Q2 = dual(T(2,2)),
T(w,s) = OR of s disjoint width-w terms) has min_i E_i/Inf_i = 4.506400645515568435507174..., where
E_i = H(1[i in U] | U minus i) for U from the squared spectrum. Measured 10 Nov 2026 by an agent with code written
without reading FEIB31's: 40-digit mpmath, agreeing with FEIB31's interval certificate to 22 digits.

How to recompute any composition tower in seconds (no truth table): for f = g(h,...,h) on disjoint blocks, the spectral
sample is T drawn from g's mu-biased squared spectrum (mu = E h) and, for each k in T, a block sample drawn from h's
spectrum conditioned nonempty. Carry one leaf as (mean, P(U empty), P(U = {i}), the part of E_i with U minus i nonempty,
Inf_i) and update per level. Checked against full Walsh transforms on 12-16 variables (4e-16 to 2.4e-13).
Code: 06_math_research/fei_solve_2026_11_09/referee_r9/tower_recompute.py and tower_recompute_mp.py.

Scar: the same recursion in double precision read 4.50640064333, 2.2e-9 below the certificate, after 14 levels with
16-variable biased gates. A ninth-digit disagreement is not a finding until a high-precision rerun.

Also confirmed: FEIB31's 590,490-variable witness M,D,D,D,D,dual(T(2,5)) = 4.50585006208; the old tower M,D,D,M,M,D,D =
4.50504996750 (monotone up to an output complement, as FEIB31 says); the pi/ln 2 read-once leaf bound (integral checked
by hand; 400 random read-once formulas, max leaf 4.132) and the width-w and (2.1) bounds (1,000 random functions, no
break). Plain M/D words get close: MDDDDDMM = 4.5063799 at depth 8. FEIB29's 4.505226 "PM(K33) tower" word was not
identified. A finite record is a lower bound for the monotone constant, not evidence that it is finite.
Referee note: 06_math_research/fei_solve_2026_11_09/referee_r9/REFEREE.md.

Related: [[fei_step_ratio_towers_4475_referee_2026_11_10]], [[fei_k33_invariant_search_complete_pmk33_max_2026_11_10]],
[[fei_equivalent_to_erasure_entropy_one_good_coordinate_2026_11_10]].
