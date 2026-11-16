---
name: t240_l1_phi_o_e137_step_order_needs_loglog_n_69_2026_11_03
description: [PROVISIONAL] T240 (L1) with numbers: nondegenerate, but sd of Z^u ~ e^137 at eta 1/2 (T_2 = 4,417), so the plan's step order holds only for log log N > 68.6; theorem unaffected
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T03:26:45+04:00
  status: provisional
  evidence: "06_math_research/frontier/rows/T240/L1_agent/l1_phi.txt"
---

T240, 3 Nov 03:2x. (L1) is written out with numbers in 06_math_research/frontier/rows/T240/L1_agent on the private repository main (L1_WITH_NUMBERS.md, l1_phi.py, l1_phi.txt; floats, not bounds).

- (L1) holds as the plan states it: sqrt N u(T_2) -> l Phi_o(T_2) Z_0 + G^u with Z_0 ~ N(0, I_2), nondegenerate. Phi_o is the 2x2 odd variational flow on B = ((R11-R12), (R21-R22))/sqrt 2, and the noise limit is independent by the stable martingale CLT.
- At eta = 1/2 the symmetric ODE from Q = I, R = 0 reaches kappa U_c / 8 = 2.5e-9 of x* only at T_2 = 4,417 (within 1e-3 at t = 1,051, within 1e-6 at t = 2,851). log|l Phi_o(T_2)| = 137.2, against lambda T_2 = 139.6.
- So Z_N^u has s.d. about e^137. The plan's order (step 1 even convergence, then step 2 odd growth from N^{-1/2} to N^{-1/2} log^2 N) holds only once log log N > 68.6. The cone entry U_c/8 is passed before T_2 unless log N > 302.
- The theorem is unaffected (N-independent constants; tau_N shifts by O(1)). The explicit-N regime of the glued proof is set by this term, not by the noise constants (log N > 31.7 with the tight c_D, s2) or the cone margins.
- Repair idea, not done: run odd growth concurrently with even convergence; stop step 1 at plateau entry (|e| <= 1e-3) and recompute the hull constants on that box.

Numerics scar: integrating the symmetric slice in floats leaves the plateau at t ~ 1,160 because rounding seeds the odd mode at 1e-16. Symmetrize the drift exactly (average the swapped pairs) and renormalize the variational flow in chunks, or Phi overflows and the event never fires.

How to apply: when a proof hands off between phases at a fixed small radius, compute the growth of the unstable mode over the stable phase's duration before trusting the order of steps. Here it was e^137.

Related: [[t240_cd_17p6_s2_71p7_explicit_rigorous_2000x_loose_2026_11_03]], [[t240_e_rev2_review_t_eta_certified_2p1e9_rate_integral_fix_2026_11_03]].


Update 3 Nov 03:31: my repair idea checked (L1_agent/REPAIR_CHECK.md). Stopping step 1 at |e| <= 1e-3 cuts the threshold only to log log N > 15.4; the N^{-1/2} log^2 N window of step 2 forces it. The stable block still contracts on a 1e-3 box in floats (-1.73e-3); the interval code's +0.22 there is wrapping and certifies only to radius about 1e-5.
Update 3 Nov 03:39 (EXPLICIT_REGIME.md, move 8): the odd growth is 19.0 nats per decade of even convergence = lambda ln10 / 0.003826. The slowest stable mode -0.001918 is odd under the student swap, so y never sees it. Measured against (E) rev 2's start condition kappa U_c/128 rather than the plan's /8, the growth is 160, not 137, and the thresholds are log log N > 80 and log N > 347. A cone certified at U = 1e-3, kappa = 1 (float samples allow it) would give log N > 160 at best.
Correction 03:41 (move 9): the concurrent-phases repair idea above is wrong. While u is small, e follows y, so the cone-entry threshold log N > 2 (g(kappa U_c / c) + log(8 / U_c)) holds in any order of steps. Only the log log N condition is an artifact of the plan's window. The one lever is a wider certified window (kappa U_c).
