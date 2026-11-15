---
name: fei_negated_inputs_table_settles_record_6_5218_stands_2026_11_11
description: "FEI tower table with negated gate inputs? W had a false cusp at 1/2; with negations W(1/2+e) >= c + 5.5e^2, the table settles (round 8 moved <= 0.00115), record 6.521845711 stands; all 2^32 five-input entry gates lose (best -0.0697), biased coins lose (-0.0052)"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T03:34:03+02:00
  status: provisional
  evidence: ""
---

FEI lower bound, tower (Bellman) frame, 11 Nov 2026, agent an agent. The record 6.521845710923 = G/(J-1) of
the 18-input gate (matching function of K33 on 9 edge inputs plus 9 coins) still stands. Four things learned:

1. A tower may feed a gate the state g or its negation (same G and J, bias p or 1-p). The gate libraries above four
   inputs never held such variants, so the table W_run6 was too low around 1/2: it had a downward cusp there
   (W - c about -1.6|e|), an artefact. With main inputs 0, 2, 3, 6 and all nine coins of the record gate negated,
   U = G_p - cJ_p + c = +10.8 e^2 at input bias 1/2 + e (0.0997 at e = 0.1), drift 0.19 e. Checked two ways: coin
   decomposition with per-input bias (code/rec_hess.py) and the explicit 2^18 truth table (code/neg_check.py).
   So W(1/2 + e) >= c + 5.5 e^2 and 1/2 is the minimum of the table. With all negations screened in (neg_screen.py,
   neg_loop.sh) the table settles in two rounds: W_run8 - W_run7 <= 0.00115; W(1/2) and the rollout stay 6.521845711.
   W(.25) 6.9923, W(11/32) 6.6884, W(.4824) 6.52344, W(.498) 6.521868.

2. Every function of five inputs as an entry gate on uniform bits (all 2^32 tables, code/fei_entry5.c) against that
   table: no positive slack. Best -0.069734 at output bias 11/32 (table 0000aafe, G 2.7284 J 1.4545), -0.0764 at
   10/32, -0.0807 at 12/32, -0.1187 for AND2-like tables at 8/32, -0.2609 balanced.

3. The record gate with uniform main inputs and coins replaced by small functions of bias q (code/coin_bias.py):
   U is +0.000012 at q = .45 and negative beyond; the coins' own cost is first order. Best total -0.0052. Dead.

4. Why the table says it all: for f = F(h,..,h), Phi(f) + D(p_f) = [U_F - J_F D(q) + D(p_f)] + J_F (Phi(h) + D(q)),
   Phi = G - c(J-1), D = W - c. The bracket is <= 0 by the table; the rest is the entry shortfall of h. Entries near
   the record pay about 3.8|q - 1/2| against D about 5.5 (q - 1/2)^2. And the frame loses nothing: C* equals the sup
   of H(g)/(I(g)-1) over balanced g, because g = y f with a fresh bit y is balanced with the same ratio as H(f)/I(f).

What would change this: a gate that raises W at a bias in .30-.40 by about 0.07, or an entry function with shortfall
near 0; the open lever is coin searches on bases with 12 to 16 inputs. The table is one implementation
(tower_vi2.py); the U values in item 1 and the gate values are checked from explicit truth tables.
Corrects the frame of [[fei_towers_drifting_and_unequal_bias_do_not_beat_6_5218_2026_11_11]] (its table had no
negated inputs; its conclusion stands). Files: brain-repo/06_math_research/
fei_solve_agent_2026_11_10 (STATE.md, code/, results/tower/W_run8.txt). Record card: math store
claim_dc791b32e0484ff9a7c3ca145381fcff.

