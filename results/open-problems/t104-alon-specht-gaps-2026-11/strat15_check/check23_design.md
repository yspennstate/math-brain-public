# Checks 2-3 (design review), 13 Nov 11:09 - what STRAT15 certifies for q >= 1

exact_bernstein.chart_data() splits the STRAT10 numerator (divided by 8) by the power of q: cs[0], cs[1], cs[2], so C_N = c0 + c1 q + c2 q^2.
Three targets: c2, d1 = c1 + 2 c2 (= C'(1)), C1 = c0 + c1 + c2 (= C(1)).
Logic: on a box where c2 >= 0, C'(1) >= 0 and C(1) >= 0, C(q) = C(1) + C'(1)(q-1) + c2 (q-1)^2 >= 0 for all q >= 1. Sound (exact Taylor
expansion of a quadratic at q = 1). Since C_N = 10(N-2)^2 D^2 Delta T_N and q/(N-2) -> 1, T_inf = c2/(10 D^2 Delta): c2 >= 0 IS the N -> inf
statement, so the limit is included. (A box with c2 < 0 somewhere cannot be closed this way; it would need a different split - watch for it.)
All-N premises (checked by hand):
- ratio = 784 Delta - 75 tau^2 >= 0  <=>  Delta/tau^2 >= 75/784 = r/(1+r)^2 at r = 3/25, i.e. r >= 3/25 (complement of STRAT9/10's all-N r <= 3/25 region).
- scale14 = 62500 (tau^2 - 4 Delta) - X^2 with X = 129 D - 250 tau: the complement of a <= 129/250 (STRAT10 sextic all-N ceiling), valid only
  where scale_guard X >= 0 on the whole box - same guard pattern as STRAT14 (103/200). Check 1b must confirm the guard per box.
- connected = 25 t^2 - 5 t tau + Delta equals (5t - M00)(5t - M11) - M01^2 (expanded by hand). Rest equal STRAT10 necessary().
To do when final: confirm c0, c1, c2 by my own expansion of C_N(q) at q = 0 and q = -1 (T6 and 2 Cface identities) and at q = 1, 2.

## Coefficient checks, 13 Nov 11:20 (run on Mac mini 1, ~/agent_run/strat15_check_claude)
- my_cs_cross2.py: STRAT15 c0, c1, c2 (x8) equal STRAT10 zero_face numerator's q^0, q^1, q^2 coefficients exactly (1255/1255/1253 terms). PASS.
- my_cs_cross.py: c0 - c1 + c2 = (1/4) x STRAT8 face numerator, coefficientwise, one ratio over all 1254 terms (consistent: cs = num/8,
  num(q=-1) = 2 Cface). Targets c2, d1 = c1 + 2c2, C1 = c0 + c1 + c2 are as stated. PASS.
- Scar: the first run reported 'support differs 5017' = 1254 + (1255+1255+1253): `from zero_face import` had returned STRAT10's cached
  7-variable module, not STRAT8's. Load same-named modules from different strata by spec_from_file_location under distinct names.
