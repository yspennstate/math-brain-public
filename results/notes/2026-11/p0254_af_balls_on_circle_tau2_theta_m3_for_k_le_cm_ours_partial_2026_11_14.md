---
name: p0254_af_balls_on_circle_tau2_theta_m3_for_k_le_cm_ours_partial_2026_11_14
description: "[PROVISIONAL] P0254 (Aldous-Fill Example 14.32, m balls in K boxes on a circle, pick a box, if vacant the first ball met in a random direction moves in; conjecture tau2 = Theta(m^3), tau1 = O(m^3 log m)): ours, unrefereed - SSEP comparison gives tau2 <= K/(1-cos(2pi/K)), so Theta(m^3) whenever K <= Cm; exact tau2 for m=2..10 is nonincreasing in K with max (m+1)/(1-cos(2pi/(m+1))) at K=m+1, which if true for all m settles the tau2 half; K >> m open"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-14T03:48:42.865Z
---

P0254, our 200-list. Source: Aldous-Fill book Ch. 14 Sec. 7, Example 14.32 (html read 14 Nov 2026). Known: tau1 = O(m^10)
(Cuellar-Montoya, SPA 67 (1997) 69-99); tau2 >= m^3/(8 pi^2). Conjecture: tau2 = Theta(m^3), tau1 = O(m^3 log m).
Literature 14 Nov: OpenAlex lists two citers of Cuellar-Montoya (the AF book; Istrate-Bonchis 2015, heapable sequences),
neither on this question; two web searches found nothing newer. Open in the literature.

Our partial result (an agent, 14 Nov, unrefereed):
- Every SSEP move (a ball to an adjacent vacant box) is a move of this chain with probability >= 1/(2K), and both chains
  have the uniform law, so the Dirichlet forms compare: E_chain >= E_SSEP / (2K). SSEP gap on the K-cycle equals the
  random-walk gap 2(1 - cos(2 pi/K)) (Caputo-Liggett-Richthammer 2010). Hence tau2 <= K / (1 - cos(2 pi/K)) ~ K^3/(2 pi^2),
  exact at K = m+1 (one hole = lazy walk on Z_K). With the lower bound, tau2 = Theta(m^3) whenever K <= C m.
- tau1 for K <= Cm: a log-Sobolev constant c/K^2 for SSEP on the cycle uniform in particle number (Yau, PTRF 109 (1997)
  507-538) would give tau1 = O(m^3 log m) there. The Yau citation is NOT yet checked - do not quote this half until it is.
- Structure that may matter for K >> m: the lifted height function evolves by Hammersley's rule, so the same-box,
  same-direction coupling is monotone; the enclosed area is a martingale; the gap drift is the Laplacian of g^2 (no
  linear eigenfunctions, unlike the Caputo-Labbe-Lacoin adjacent walk).

Numerics (exact dense eigenvalues, scratch area p0254/gap_exact.py, cap C(K,m) <= 6000):
  m=2, K=3..39: tau2 = 2.0000 for every K.
  m=3, K=4..34: 4.0000 at K=4, decreasing to 3.7154.
So tau2 looks NONINCREASING in K. Conjecture (ours): sup_K tau2(m,K) = (m+1)/(1-cos(2 pi/(m+1))) ~ (m+1)^3/(2 pi^2),
  m=4, K=5..18: 7.2361 at K=5 (= 5/(1-cos(2pi/5)) exactly), decreasing to 6.4639.
  m=4, K=5..21: 7.2361 at K=5 (= 5/(1-cos(2pi/5)) exactly), decreasing to 6.4233.
  m=5..10 (K from m+1 up to C(K,m) <= 6000): first value equals (m+1)/(1-cos(2pi/(m+1))) to 4 decimals every time
  (12.0000, 18.5918, 27.3137, 38.4688, 52.3607, 69.2929) and the sequence never rises (m=10: 69.29 at K=11 -> 61.85 at K=15).
So tau2 is NONINCREASING in K on every case computed (m=2..10, 82 rows). Conjecture (ours): sup_K tau2(m,K) = (m+1)/(1-cos(2 pi/(m+1))) ~ (m+1)^3/(2 pi^2),
attained at one hole. Proving that monotonicity (adding a vacant box never slows the chain) would close the tau2 half for
every K. The smell test passes: the K -> infinity limit is the continuum gap chain, which should be Theta(m^3) too.

Large K (14 Nov, sparse Lanczos, scipy eigsh k=4 'LA' tol 1e-11 on the exact chain, C(K,m) <= 60000, scratch area p0254/gap_big.py,
log gap_big.log; lambda2 has multiplicity 2 from rotation; the K=34, m=3 row matches the dense solve, 3.7154): 78 more rows, zero rises.
m=3 to K=72 (24m): 3.7154 -> 3.6965; m=4 to K=36 (9m): 6.4233 -> 6.3249; m=5 to K=25: 10.48 -> 10.18; m=6 to K=21: 16.11 -> 15.56;
m=7 to K=19: 23.87 -> 22.81. The m=3 sequence flattens (3.7133 at K=36, 3.7020 at K=54, 3.6980 at K=66), consistent with a finite
continuum limit near 3.69. Monotonicity now holds on 160 rows, m=2..10.

What would change this: a counterexample to monotonicity at larger m (m >= 5 needs sparse solves), a paper on the
continuum limit, or a failed check of the Yau constant. Next if reopened: try to prove monotonicity in K by a
collapsing map (merge two adjacent vacant boxes) and a Dirichlet-form comparison; or do K >> m directly via the
Hammersley coupling. Related: [[p0247_af_last_vertex_uniform_yes_under_dc_via_bht_open_torus_like_2026_11_14]],
[[p0251_af_crossover_chain_mixes_log_k_plus_log_l_via_czumaj_switching_networks_2026_11_14]].
