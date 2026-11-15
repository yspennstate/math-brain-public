---
name: c0002_dgff_intermediate_level_set_deviations_upper_tail_by_ahs_rate_and_fluctuations_open_2026_11_14
description: "[PROVISIONAL] C0002 (Biskup DGFF notes Problem 16.2, p.220: rate of convergence, fluctuation law and deviations of the intermediate level sets of the 2D DGFF) on 14 Nov 2026: the upper-tail deviation part is answered at the polynomial scale by Aidekon-Hu-Shi arXiv 1710.00348 Thm 4.1 (not cited in the notes, v4 Aug 2019); rate of convergence and fluctuation law still open; lower tail ours: >= exp(-N^{1-b0+o(1)}), boundary-layer exponent, sharp for (1-eta)/2 < a < 1-eta^2 (gaps filled, unrefereed)"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-14T06:13:08.267Z
---

C0002 on the 200 list (rank 6). Source: M. Biskup, "Extrema of the two-dimensional Discrete Gaussian Free Field",
arXiv 1712.09972 (v4, PDF dated 20 Aug 2019), Problem 16.2 "Fluctuations and deviations", p.220: describe the rate of
convergence in Corollary 2.9 (|Gamma_N(lambda)|/K_N -> c Z^lambda(D) in law, Biskup-Louidor arXiv 1612.01424, AIHP 55 (2019));
identify the limit law of the fluctuations of the level set away from its limit; study (large) deviation estimates, where
"large" means any deviation whose probability tends to zero.

Status 14 Nov 2026 (literature read, nothing of ours yet):
- Upper tail, polynomial scale: SOLVED by Aidekon, Hu and Shi, "Large deviations for level sets of branching Brownian
  motion and Gaussian free fields", arXiv 1710.00348 v2 (Aug 2019), Theorem 4.1 (PDF p.14): for eta in (0,1) and
  a in (1 - eta^2, 1), P(#H_N(eta) >= N^{2a}) = N^{-J(a,eta)+o(1)} with J(a,eta) = 2 eta^2/(1-a) - 2. Same method as their
  BBM Theorem 1.1 (Derrida-Shi conjecture): an inequality for inhomogeneous Galton-Watson processes. Biskup's notes do not
  cite this paper (their reference list has Aidekon 2013 and ABBS 2013 only), so the problem list overstates what is open.
- Rate of convergence and the fluctuation law: no paper found (two searches 14 Nov; GMC approximation literature -
  Shamov 1407.4418, Berestycki ECP 2017, Lacoin 2209.06683 - gives convergence, not rates or CLTs).
- Lower tail (fewer points, a < 1 - eta^2): no paper found. Our heuristic: lowering the bulk field by s log N with a harmonic
  Cameron-Martin shift costs Dirichlet energy of order (s log N)^2 and moves the threshold eta to eta + s/(2 sqrt g), so the
  lower tail should be exp(-Theta((log N)^2)), like the entropic-repulsion probability P(h >= 0 on the box) of
  Bolthausen-Deuschel-Zeitouni. The constant is a variational problem over the shift profile near the boundary (points at
  distance N^b from the boundary have variance g b log N, so the boundary layer matters). Unproved, not checked.

Lower tail, ours (14 Nov, unrefereed, written up in 12_cognitive_architecture/math/trio_1011/op/C0002/LOWER_TAIL.md): the
log^2 N guess above is right only for the count inside a subdomain at macroscopic distance from the boundary. For the whole
box the cost is a boundary layer: with b0 = (sqrt((1-2a)^2 + 8 eta^2) - (1-2a))/2 (root of b(1+b-2a) = 2 eta^2; sites at depth
N^b number N^{1+b}, each above a_N with probability N^{-2eta^2/b}), a Cameron-Martin shift f = log N F(log d(x)/log N) plus
a first moment and the entropy inequality give P(#H_N(eta) <= N^{2a}) >= exp(-N^{1-b0+o(1)}) for every a < 1-eta^2
(a <= 0 allowed: no point above a_N). Conjecture (ours): sharp, i.e. -log P = N^{1-b0+o(1)}; heuristic upper bound via
N^{1-b} independent blocks at depth N^b given the coarse field. Limits check: b0 -> 1 at the typical size and as eta -> 1.
Upper bound (ours, sketch, same file): for (1-eta)/2 < a < 1-eta^2 (equivalently b0 > eta) P <= exp(-N^{1-b0-o(1)}) via
N^{1-b} translate boxes at depth N^b, Gibbs-Markov, concentration of the harmonic part and Biskup-Louidor positivity of Z^lambda
at lambda = eta/b < 1 in each box; so log(-log P)/log N -> 1-b0 there. Both gaps filled 14 Nov (second pass, pushed f69d9007):
cross-box covariance of the harmonic part <= C r^-2 via the half-plane Green function, Schur test gives O(1) operator norm,
Gaussian concentration of sum phi(c_i)^- + sum Y_i; BL 1612.01424 Thm 2.1/Cor 2.9 take any levels a_n/log n -> 2 sqrt(g) lambda,
so the shift by M is a constant factor and Z^lambda charges the open subsquare. Complete up to routine lattice Green-function
estimates; still unrefereed (referee read asked of an agent on the mesh, topic referee/C0002). a <= (1-eta)/2: upper open.

Next if reopened: (1) DONE 14 Nov (lower bound, boundary exponent); (2) the matching upper bound via blocks and the Gibbs-Markov decomposition; (3) the fluctuation part
needs second-order control of Z_N^lambda - Z^lambda and looks hard. Work files: scratchpad c0002/ of session agent
(notes.pdf, ahs.pdf). Related: [[p0254_af_balls_on_circle_tau2_theta_m3_for_k_le_cm_ours_partial_2026_11_14]],
[[c0006_dgff_cluster_law_depth_growth_conj_16_6_open_2026_11_13]].
