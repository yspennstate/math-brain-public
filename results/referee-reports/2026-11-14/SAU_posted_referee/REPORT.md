# Referee report: uniqueness of stable allocations in dimensions one and two

Paper: yspennstate/stable-allocation-uniqueness at c349c7b (paper/main.tex, 332 lines). Referee: an agent, 14 Nov 2026.
Claims: for every locally finite set of centres in R or R^2 and every appetite in (0, inf) the stable allocation of
Hoffman-Holroyd-Peres is unique up to null sets (Theorem 1.1), answering HHP Section 7 problem (i) for d <= 2; in every
dimension it is unique when sum_k 4^k/(1 + N(2^k)) = inf (Theorem 1.2; N(r) = O(r^2 log r log log r) suffices).

## Verdict

SOUND. One sentence was imprecise and is fixed in the repository (commit 5a2b87f, PDF rebuilt, no undefined citations).

## Proofs checked

- Extremal allocations s (site-optimal) and c (centre-optimal) from HHP Lemma 15, stable by Lemma 14; the disagreement
  quantities Q(u,v) = C_u cap S_v with capacities q. Correct.
- Balance lemma: inflow <= L(A_u) <= L(B_u) = outflow. Correct.
- Radii lemma: T_v <= |x - v| < |x - u| <= T_u, v sated under c, the directed graph is acyclic, and the shell bound
  q(u,v) <= omega_d (T_u^d - T_v^d). Correct.
- The reachable subgraph H from the edge (rho, v_0), R = T_{v_0}, edge lengths <= l = max(2R, |rho - v_0|), and the packing
  bound #(V_0 cap closed B(z,r)) <= omega_d (r+R)^d / alpha. Correct.
- Transience of H from HHP Proposition 13 against recurrence from Nash-Williams with cutsets at r_j = (l+1)j
  (disjoint because edges are shorter than l < r_{j+1} - r_j) and Cauchy-Schwarz. Correct, including the index shift
  sum_{k>=1} 4^k/(1+N(2^{k+1})) = (1/4) sum_{k>=2} ... and C_0 = 1 + omega_d (2+R)^d / alpha for d <= 2.
- Remark 4.2 (d >= 3 and finite configurations). Correct.

## Remark 4.1 (a set where HHP Theorem 2 does not apply)

Xi_0 = union of C_n = {n + j/(10n) : 0 <= j < n}. The unit flow 1/(n(n+1)) on the n(n+1) edges C_n -> C_{n+1} conserves
mass (each inner point gets 1/n and sends 1/n) and has energy sum 1/(n(n+1)) = 1, so G_2 is transient (T. Lyons 1983);
extra edges of G_2 only lower resistance. Checked numerically (remark41.py, remark41.out): effective resistance from
C_1 to the shorted shell C_N is 0.724, 0.742, 0.751, 0.755, 0.757 for N = 10, 20, 40, 80, 120, bounded below the flow
bound 1, and N(r)/r^2 -> 1/2. The edge count inside the C_n is of order r^3, as stated.

## Citations checked

- HHP (arXiv math/0505668v4, Ann. Probab. 34 (2006) 1241-1272): Theorems 1-3, Lemmas 14 and 15, Proposition 13 (the
  transient undirected version, hypotheses (i)-(iii)), Remark (vi) with Woess Corollary 3.52 and the O(r^2 log r) pair
  count, Section 7 problem (i) worded as quoted. All as the paper states.
- The other entries (GS 1962, HP05, HHP09, FPV 2007, HMK 2016, CPPR 2010, T. Lyons 1983, Lyons-Peres 2016 Section 2.5,
  Nash-Williams 1959, Woess 2000) have the right authors, journals, volumes, years and pages.
- Prior-work search (two wordings, 14 Nov): nothing after HHP answers problem (i); HHP09 and later work treat Poisson or
  stationary centres. The extremal-allocation packing argument is not in HHP, whose Theorem 2 graph uses arbitrary pairs
  of stable allocations.

## The fix

The introduction said, after HHP's own sentence, that by HHP Theorems 2 and 3 a counterexample "must grow faster than
quadratically". Read as growth of N(r), this is contradicted by the paper's Remark 4.1 (N(r) ~ r^2/2 and HHP's
criterion fails); HHP mean the count of close pairs in Remark (vi). The sentence now reads: by Theorems 2 and 3 of HHP
and Remark (vi) there, such a set cannot come from a translation-invariant point process, and for some b the number of
pairs of its centres in B(0,r) at distance less than b is not O(r^2 log r).

Not changed (style hints only): the abstract runs 154 words; the notation table omits w.
