# Audit of agent B's next-order term (T354, NOTE.md "The next-order term", push 9ee337c3)

Auditor agent A, 20 Oct 2026 02:5x. Verdict: CONFIRMED, under the hypothesis E b = 0 that the derivation uses
(E g = x). The statement checked:

    x*/x0 = 1 + d [ K + (3/4) ( S/B2^2 - (K2/K) E[b Z^2]/(B2 B3) ) ] + O(d^2),
    K = (1-b1)/(1-b1 b2),  K2 = (1-b1)/(1-b1 b2^2),  Z = b^2 - B2,  S = Var(b^2).

## The three moments, re-derived by hand

Write c_j = d b2^j (sum 1), h_j = g_j^2 - V (mean 0, independent across j), y - 1 = sum_j c_j h_j / V, m = (1-b1) sum_i b1^i g_i.

E[m (y-1)]. Only j = i survives: (1-b1) sum_i b1^i c_i E[g h]/V = d K E[g h]/V, and E[g h] = E(x+b)^3 - V x = 2 x B2 + B3.
Exact, as stated.

E[m (y-1)^2]. E[g_i h_j h_k] vanishes unless j = k. For j = k = i it is E[g h^2]; for j = k != i it is x Var(g^2). So, exactly,

    E[m (y-1)^2] V^2 = x Var(g^2) d/(1+b2) + d^2 K2 ( E[g h^2] - x Var(g^2) ),

using sum_j c_j^2 = d/(1+b2) and (1-b1) sum_i b1^i c_i^2 = d^2 K2. With x = O(d), Var(g^2) = S + O(x), E[g h^2] = E[b Z^2] + O(x),
d/(1+b2) = d/2 + O(d^2) and V = B2 + O(x^2) this is d x S/(2 B2^2) + d^2 K2 E[b Z^2]/B2^2 + O(d^3), as stated.

E[m (y-1)^3]. The O(d^2) part is one h at lag i paired with g_i (factor c_i E[g h] = c_i B3 + O(d)) and the other two paired with
each other at a lag j != i (factor c_j^2 S), three ways: 3 dK (d/2) B3 S / B2^3 = (3/2) d^2 K B3 S/B2^3. The triple at one lag j != i
carries E g = x and sum c_j^3 = O(d^2), so it is O(d^3); all-four-at-lag-i is c_i^3 = O(d^3). As stated.

Quartic and higher: E[m (y-1)^4] is x times two pairs (d^2) or c_i E[g h] times a triple (d^2), both O(d^3); every higher power
is smaller. As stated.

## The solve

From E[m y^(-1/2)] = 0 and y^(-1/2) = 1 - (y-1)/2 + (3/8)(y-1)^2 - (5/16)(y-1)^3 + ...: x = E1/2 - (3/8) E2 + (5/16) E3.
Put x = x0 (1 + d delta), x0 = d K B3/(2 B2), and divide by x0:

    delta = K - (3/16) S/B2^2 + (15/16) S/B2^2 - (3/4)(K2/K) E[b Z^2]/(B2 B3) = K + (3/4)(S/B2^2 - (K2/K) E[b Z^2]/(B2 B3)).

Same bracket. The 1/V -> 1/B2 and d/(1+b2) -> d/2 replacements move delta by O(d), inside the stated O(d^2) in x*/x0.

## Special cases and the numbers

Two-valued b with mean zero: b^2 = (b_1+b_2) b - b_1 b_2, so Z = (b_1+b_2) b and both ratios equal (b_1+b_2)^2/B2; the bracket is
K + (3/4)((b_1+b_2)^2/B2)(1 - K2/K), equal to 1 at b1 = 0. Test model (9, -1 x 9): both ratios 7.11111 = 64/9. With r = d/(1-b1)
fixed, K -> 1/(1+r), K2/K -> (1+r)/(1+2r), giving 1/(1+r) + (16/3) r/(1+2r): 1.35354 at r = 0.1 and 2.27778 at r = 1. Confirmed.

Three-valued (6, 2, -1 x 8), recomputed here: B2 4.8, B3 21.6, S/B2^2 4.72917, E[b Z^2]/(B2 B3) 5.52315, bracket at b1 = 0 0.404514,
the same as the peer's prediction file. Their exact runs (laplace_exact_bvec.py, a copy of my laplace solver with b as a
parameter) give (x*/x0 - 1)/d = 0.35565, 0.38087, 0.39525, 0.39991 at d = 0.01, 0.005, 0.002, 0.001; the gap to 0.404514 is
4.89 d, 4.73 d, 4.63 d, 4.60 d, linear in d as an O(d^2) remainder in x*/x0 should be. The r = 1 gap on the test model is 13.2 d,
13.0 d, 12.9 d (d = 0.01, 0.004, 0.002). Both families converge to the predicted bracket.

## What this does not cover

- E b = 0 is used throughout (E g = x). A gradient-noise law with nonzero mean shifts the stationary point and adds terms; the
  formula is for the centred case only.
- The expansion of y^(-1/2) is formal here. The rigorous remainder bound is the separate iid lemma (audited in
  AUDIT_REMAINDER_agent_A.md); this audit confirms the coefficient of d, not a bound on the O(d^2) remainder.
- The numerical check reuses one exact route (the Laplace-transform solver). The independent second route is the hand derivation
  above; no Monte Carlo can see an O(d^2) term at these d.
