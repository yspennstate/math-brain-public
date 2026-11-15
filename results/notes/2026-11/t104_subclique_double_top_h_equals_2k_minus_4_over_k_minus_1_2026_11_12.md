---
name: t104_subclique_double_top_h_equals_2k_minus_4_over_k_minus_1_2026_11_12
description: "T104 (Alon) stratum claim sum g(P-Q) >= 0: PROVED for every D >= 4, every weighted circulant, every n >= 8 graph with constant diag of the top projector (push 128); open D = 2, 3 with nonconstant diagonal; worst measured C_5 0.877"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T18:35:19+02:00
  status: provisional
  evidence: "06_math_research/t104_alon_agent_2026_11_11/GAP_STATE_FORM.md (double-top and clique-union sections); t104_degen_family.out 4.9e-15; t104_2k2_bridge.out; pushes 114-116; t104_R_identity.out; one reader"
  revised: 2026-11-12T19:0x (extended from one clique to disjoint unions; off-stratum rate added)
  revised: 2026-11-12T19:2x (s_inf reduction, lambda <= 1 lemma, R >= lambda refuted)
  revised: 2026-11-12T20:3x (pushes 117-122: closed, trace and edge forms; refuted routes; C_5 worst case; stale tail removed)
---

T104 (Alon's question, the H >= 0 form in 06_math_research/t104_alon_agent_2026_11_11/GAP_STATE_FORM.md).

Where the top eigenvalue of L is repeated, the proof route H >= s_inf is unavailable, so the stratum needs its
own argument. Proved (push 114, extended in push 115): a disjoint union of uniform cliques K_{a_1}, ..., K_{a_r},
each edge of K_{a_i} weighted proportionally to 1/a_i so the tops agree, has H = 2 - 2/D exactly for every beta,
D = sum (a_i - 1) the multiplicity of the top, provided n - D >= 2. The single K_k (H = 2(k-2)/(k-1)) is r = 1.
Why: only (Top, Zero) pairs have a gap; Zero vectors are constant on each clique, so each transposition of K_{a_i}
acts on the Top factor alone; summed over K_{a_i} it is the scalar a_i on that clique's standard representation and
zero on the others, so M is the scalar 2/D on Top (x) Zero and commutes with the projection onto V_[n-2,2].
Checked on 23 unions, n = 5..8, to 4.9e-15 (t104_degen_family.out).

Minimum on this family: H = 1 at D = 2 (triangle, two disjoint edges). C_5, C_7, K_4 minus an edge measure above 1.
Mac mini 2 double-top search, n = 5 (dg_n5_s41): 4,036 rounds by 12 Nov 19:1x, no value below 1 on the stratum (least 0.999996, just off it). Hint for the next
reader: 1 is a minimum along the stratum only. Joining two disjoint edges by a bridge of weight t gives
H = 1 - gap12 + O(gap12^2) (t104_2k2_bridge.out, beta up to 1e10), so a stratum bound does not extend to a
neighbourhood. Also: the search grid stops at beta = 1e6, which reads H slightly low when gap12 < 1e-5.

Push 116 (GAP_STATE_FORM.md, "The beta -> infinity value on the stratum"): on the stratum H >= s_inf, the limit
keeping only (Top, below) pairs weighted by their gaps, and s_inf - 1 = (n-2)(R - lambda) + (1 - lambda) with R the
gap-weighted Rayleigh average of M. Proved: lambda <= 1 on the stratum (2 lambda <= tr L = 2), equality only at the
balanced triangle and two equal disjoint edges; and an explicit edge formula for R - lambda (checked to 1e-14,
t104_R_identity.py). Hint for the next reader: R >= lambda is FALSE even on the stratum (n = 5, seed 11, point 13:
lambda 0.8508, R - lambda -0.0091, H = 1.12), and fails on 1,220 of 3,000 graphs off it; do not try to prove it.
The statement to prove is (n-2)(R - lambda) + (1 - lambda) >= 0; over 125 stratum points the ratio
(n-2)(lambda - R)/(1 - lambda) never exceeds 0.183 (limit 1). H = s_inf to 1.1e-5 at n = 5, up to 0.09 below H at n = 6.

Pushes 117-122 (12 Nov, GAP_STATE_FORM.md): with p = u*v, c = 2n/(n-2), g_l = lambda - mu_l, the stratum target is
sum_l g_l (P_l - Q_l) >= 0, P = trace over Top of mu + c(lambda|p|^2 - p'Lp) + (1-lambda)(1 - c|p|^2)/(n-2),
Q = 2 sum_e w_e (b_e.u)^2 (b_e.v)^2; basis-free it is a trace inequality T = X1 + X2 + X3 - Y >= 0, and with
gamma_e = b_e' G b_e it reads sum_e w_e gamma_e (2 tau_e - D) <= X2 + X3, tau_e = |Pi b_e|^2. Proved: gamma_e <= lambda(2 - tau_e),
too weak alone (C_5: 0.358 against 0.322). Hint for the next reader - these routes are FALSE, do not retry: per pair
(1.370, n = 5), per l with the trace over Top (Q/P 1.020, seed-11 point), any two of X1, X2, X3 alone, Chebyshev ordering
of g against F (fails 10/15 at n = 5). The plain sum over l is positive at all 27 points tried; the gap weights carry it.
Margin ratio sum g Q / sum g P: C_5 0.8769 (exact closed form, lambda = (2/5)(1 + cos pi/5)); C_7 0.654, C_9 0.507; C_n is NOT always the worst
circulant (n = 11: 0.4133 against 0.4110 for C_11); eight-start search on the n = 5 stratum 0.873; 75 stratum points near C_5 all below it (push 122,
2e7df888). So C_5 looks like the n = 5 maximum. Next: second variation at C_5 in closed form, then a proof of ratio <= 1.

Pushes 123-128 (12 Nov evening, all verified on GitHub): double-top searches n = 6 (301,525 stratum points, least H 1.000009
at the balanced triangle) and n = 7 (179,303, least 1.000014 at two equal edges), no value below 1. PROVED (push 128, 5165d31f;
Codex run STRAT on Mac mini 1, audited by an independent script t104_strat_audit.py): D >= 4 gives 2 S5 <= (4/D) X1, so T >= 0;
constant diag Pi = D/n with n >= 8 gives tau_e <= 4D/n and T >= 0 (all vertex-transitive graphs); circulants n = 5, 6, 7 by
nonnegative midpoint certificates (sector a hull of v_i, T = sum alpha_i alpha_j q_ij). That two-line argument supersedes the
long Fourier proof for odd n >= 21 (push 126) and the face search n = 5..19 (pushes 127-128). Hint for the next reader: before
a long special-case computation, try the crude bound tau_e <= max over the edge of the projector - it closed every symmetric case.
Open: D = 2, 3 with nonconstant diag Pi (Codex STRAT2 on Mac mini 1 since 21:43 local, counterexample hunt at n = 8..12 plus
proof routes). Status: provisional for the open part; the push-128 theorems have two readers (the Codex run and the audit).
Row T104: not solved.

Open: H >= 1 on the whole double-top stratum (measured only). Status: provisional, one reader.
own argument. The uniform K_k on k of the n vertices, 3 <= k < n, has H = 2(k-2)/(k-1) exactly, for every beta.
Why: the only pairs with a gap are (Top, Zero), and on Top (x) Zero every clique transposition acts only on the
Top factor (Zero vectors are constant on the clique). So M is the scalar 2/(k-1) = 1 - (k-3)/(k-1) of the
standard representation of S_k, and M commutes with the projection onto V_[n-2,2] because that subspace is
S_n-invariant. The eigenvector step is checked to 1e-15 for n = 5..8 (t104_subclique_eig.out).
Hint: the same "one factor sees only a subgroup" trick may give H on other symmetric configurations (a clique
plus a pendant, two disjoint cliques). The open part: is the triangle (H = 1) the minimum over the whole
double-top stratum? Only measured (a short n = 5 search found nothing below 1.0; mini 2 runs dg_n5/6/7).
Status: provisional, one reader. Row T104: not solved.
