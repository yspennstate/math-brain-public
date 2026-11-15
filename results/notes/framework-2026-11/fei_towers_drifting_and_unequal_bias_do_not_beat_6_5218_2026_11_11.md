---
name: fei_towers_drifting_and_unequal_bias_do_not_beat_6_5218_2026_11_11
description: "FEI lower bound by drifting-bias towers, unequal-bias trees and gate searches (10-11 Nov)? None beats the published 6.5218 (PM(K33) + nine coins); record anatomy: affine in coins; traps: cusp at 1/2, dictator scores W(p)"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T01:44:38+02:00
  status: provisional
  evidence: "06_math_research/fei_solve_agent_2026_11_10/STATE.md; results/tower/vi_run4_summary.txt; results/zoo/zoo_run1.txt"
---

FEI lower bound by towers: what was tried on 10-11 Nov 2026 and what it gave. Status: provisional (every number is
a search or a value iteration; none of it is a proof that the published record cannot be beaten).

**The frame.** For g on uniform bits put p = Pr[g = -1], G = entropy of the normalised non-constant Fourier weights,
J = I/Var. Composing a gate F on independent copies of g gives G' = G_p(F) + J_p(F) G, J' = J_p(F) J, and H/I >= G/J.
The best tower from bias p has value W(p) with the Bellman equation W(p) = max_F [G_p(F) + W(p')]/J_p(F). With inputs
that are different functions g_j of biases p_j: G' = G_pvec(F) + sum_j J^(j) G(g_j), J' = sum_j J^(j) J(g_j), where
J^(j) is the normalised biased weight on sets containing j. Both rules agree with explicit truth tables to 4e-15
(code/bias_check.py --law, code/het_test.py). A function g beats the record c iff slack(g) = G - cJ + W(p_g) > 0; a
bit and the record gate have slack 0.

**The record.** 6.521845710923 = H/(I-1) of the perfect-matching function of K_{3,3} with nine coins (18 inputs,
balanced, monotone, H 6.776605309006, I 261/128). It is the published lower bound (math store card claim_dc791b32),
not ours. The matching function alone gives 6.4747 as a gate at 1/2; the coins are worth about +0.047.

**Anatomy of the record (11 Nov).** Nine inputs are the edges of K33 (influence 57/256 each), nine are coins
(influence 1/256 each). With every coin 0 it is the matching function (247 ones of 512, six minterms). Coin e adds
one minterm: the four edges sharing a vertex with e. Nothing else depends on a coin, and no two inputs form a module,
so the record is not a read-once tree. It is affine in the coins: g(x, y) = a(x) + sum_j b_j(x) Y_j with each x
labelled +1, -1, Y_j or -Y_j, and its spectrum is the union of the spectra of a and the b_j, so such functions cost
(k+1) 2^m to score at any number of coins. code/fei_coin.c searches that family (code/coin_check.py re-evaluates
from the explicit truth table; both give 6.521845710923 for the record). Results of that search: see STATE.md.

**What did not beat it (all with W(1/2) = 6.521845711, rollout = the record gate for ever).**
- value iteration over every monotone gate on at most 5 inputs and all 16181 monotone classes on 6 inputs;
- 211 structured functions of the main campaign (7-18 inputs) added as gates;
- 153 structured monotone gates (matchings of bipartite graphs, K4, K6, cube, octahedron, Petersen, prism, wheel;
  connectivity, triangles, Hamilton cycles, Hex, Y, bond crossing, projective and affine plane lines, thresholds),
  each at 101 biases: closest pm_K4 -0.0066 (p .58), match_K3,3 -0.018 (p .55);
- annealed gate searches on 8-14 inputs at biases 1/2, 11/32, golden: best values sit at near-dictators, below W(p);
- first run of the unequal-bias search (149 gates): every slack <= 0, largest away from the bit -0.0345 at p = .5013.

**Traps.**
- W has a cusp at 1/2: W(1/2 + e) = c - O(e log 1/e). A 601-point table interpolates across it and flatters any
  search at 1/2 that lands near but not at 1/2 (a "6.4846" with mean 0.0039 was this). Use the 9601-point table
  results/tower/W_run6.txt (W at log-odds +-0.005 is 6.520455).
- A dictator gate scores exactly W(p), so an annealer at a biased p drifts to near-dictators; only best - W(p) > 0
  against the SAME table the job used means anything (code/read_bell.py reads the table name from the job header).
- Coarse tables differ from the fine one by up to 7e-4 away from 1/2 (golden bias 6.576709 against 6.575957, the
  exact fixed-point value of the two-input gate); believe an explicit rollout, never a table entry.

**Where.** brain-repo/06_math_research/fei_solve_agent_2026_11_10 (STATE.md first; code/
tower_vi.py, fei_bias.c, zoo.py, het_search.py; results/tower, results/zoo). What would change this note: any gate or
tree with positive slack that survives expansion to a truth table and a second transform in high precision.

