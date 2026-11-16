---
name: t240_cd_17p6_s2_71p7_explicit_rigorous_2000x_loose_2026_11_03
description: [VERIFIED] T240 c_D = 17.64, s2 <= 71.71 explicit (R drift exact at every N; Q correction eta^2(E[g'g'd^2|Px|^2]-4E[g'g'd^2])/N); MC control passes; ~2000x loose, explicit N log N > 284 vs 6.2
metadata:
  type: project
  created: 2026-11-03
  created_at: 2026-11-03T03:11:43+04:00
  status: provisional
  evidence: "brain-repo T240/cD_s2_agent/cd_s2_bounds.txt (1e6-sample MC at N=12,40)"
---

T240, 3 Nov 03:11. The constants c_D and s2, which L3 and E used only as finite numbers, now have explicit values: 06_math_research/frontier/rows/T240/cD_s2_agent on brain-repo main.

- The R drift has no finite-N correction. (lambda, nu) is exactly Gaussian at every N.
- Only the eta^2 |x|^2/N term in the Q equations moves: D_N^{Q_ik} = eta^2 (E[g'g' delta^2 |Px|^2] - 4 E[g'g' delta^2]) / N, with P the projection on span(w_1, w_2, v_1, v_2).
- From |g'| <= sqrt(2/pi), |delta| < 4, Q_ii <= 0.37 and eta <= 0.5000000001: c_D = 17.64 and s2 <= 71.71. In the frame, with |P^-1|_2 = 1.597, they are 28.2 and 183.0.
- Control: an exact finite-N Monte Carlo at the plateau. At N = 12 it resolves N D_N = 0.0075 at 5 s.e., it finds the R entries exact, and it measures E|N dX|^2 = 0.034. Every value sits under its bound, and the check could have failed.

The bounds are rigorous but about 2,000 times loose, because sup|delta| = 4 ignores that the error is small at the plateau. That matters as soon as N is made explicit. L3's bad-event bound needs log N > 284 with the bound, but only 6.2 with the plateau value. The next step is a certified enclosure of E[delta^2 ...] over the box N, using iv_scm.py.

How to apply: before calling a constant "finite is all we use", bound it once with the crudest sup argument and see what that does to the explicit-N figure. Here the crude bound is valid, and it still moves the explicit N from e^6 to e^284.

Related: [[t240_e_rev2_review_t_eta_certified_2p1e9_rate_integral_fix_2026_11_03]] (the review that listed these constants as open), [[t240_stochastic_cone_lemma_window_44_n_1e24_2026_11_01]] (the lemma whose bad-event bound uses s2).


Update 3 Nov 03:2x: the looseness is now removed rigorously. E[delta^2] is enclosed over N in [0.029274, 0.029306] (Monte Carlo 0.02930 inside), and Hoelder then gives s2 <= 0.893, c_D <= 0.174, frame noise 2.28/N, so L3's explicit N needs only log N > 31.7 (cd_s2_tight.py, same folder). The 71.71 / 17.64 figures above are the crude first pass.
