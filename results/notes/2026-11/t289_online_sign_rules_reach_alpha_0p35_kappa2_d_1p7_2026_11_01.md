---
name: t289_online_sign_rules_reach_alpha_0p35_kappa2_d_1p7_2026_11_01
description: [PROVISIONAL] T289 symmetric binary perceptron: cosh-potential online rule ends at |Ax|_inf = 1.7 sqrt(n) (n 100-400, m = 20 n), alpha_alg >= ~0.35 kappa^2; l2 greedy grows; flatness prediction failed +20pct from n 50
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T17:36:33+04:00
  status: provisional
  evidence: ""
---



1 Nov, an agent, brain-checked first ([[start_a_top400_row_only_after_brain_recall_t255_was_solved_17_oct_2026_11_01]]). Order kappa = Theta(sqrt(n/m)) is Bansal-Spencer, optimal under lattice hardness (2501.16517); m-OGP (2203.15667) matches up to logs. Files ~/math_loop/T289/; pushed 4b287ed, card claim_1663383958c04196b1c7a2cfa8b93640 (ff27cbf). Related row on a perceptron: [[t299_binary_perceptron_alpha_it_1p2447_and_overlap_barrier_2026_10_31]].

Ratio follow-up 1 Nov: cosh rule final D at m/n 5/20/80 is 1.67/1.69/1.70 (n 200) and 1.71/1.77/1.74 (n 400); pooled 1.71, alpha ~0.34 kappa^2; 10 pct agreement fails only at n 100. Pushed 531937d.

Barrier comparison 1 Nov: 2203.15667 m-OGP at alpha >= 10 kappa^2 log(1/kappa) (base unstated in that theorem); Bansal-Spencer K unnamed, measured K ~1.71. Window ratio 68/135/203 at kappa 0.1/0.01/0.001 (natural log). Pushed 647fd64.

kappa = 1 run 1 Nov (t289_k1.py, 10 runs/cell): cosh rule 50 pct point at alpha ~0.45 (m 200), 0.37 (400), 0.33 (800); prediction 0.25-0.6 held. Online barrier 1.77 (2203.15667), so the kappa = 1 open interval is ~0.33 to 1.77. Pushed 9d9ca2c (research_pushes/2026-11-01-loop-T289-k1), frontier move 47b496e3.

## Added 1 Nov (late): the ratio check and the barrier window, with every folder named

The work went up in four folders on research-repo, each a later version of the same note:
- research_pushes/2026-11-01-loop-T289-online: the first run above, at m/n = 20.
- research_pushes/2026-11-01-loop-T289-ratio: the ratio check. Potential rule at beta 2, m/n = 5, 20 and 80, 8 runs a cell. At n = 400 the final D is 1.71, 1.77 and 1.74; at n = 200 it is 1.67, 1.69 and 1.70. The prediction (the three ratios within 10% at each n) held at n = 200 (2%) and 400 (3.5%) and failed at n = 100 (20%, within the run-to-run noise there). Pooled over n 200-400 and all ratios D = 1.71, so alpha_alg >= 0.34 kappa^2, independent of the ratio from 5 to 80. l2 greedy: final D flat in the ratio, maximum over the run grows with run length (2.60, 2.94, 3.14).
- research_pushes/2026-11-01-loop-T289-ogp: the barrier side, read from the LaTeX source of 2203.15667 (Gamarnik, Kizildag, Perkins, Xu). Bansal-Spencer is restated there as success for alpha < (kappa/K)^2 with K unnamed; the m-OGP theorem gives failure of stable algorithms for alpha >= 10 kappa^2 log(1/kappa) at small kappa; the online-failure theorem is stated only at kappa = 1, for 1.77 <= alpha <= 1.8159. So the known small-kappa window is 0.34 kappa^2 (measured) to 10 kappa^2 log(1/kappa) (proved), a ratio of 68, 135 and 203 at kappa = 0.1, 0.01 and 0.001 (natural log; base 2 would make the upper end 1.44x). The paper attributes the log to the first moment of the cardinality term, so closing it needs a different count.
- research_pushes/2026-11-01-loop-T289-k1: the kappa = 1 run (half-success up to alpha about 0.33 at m = 800, against 1.77 for the proved online barrier).
The row's frontier moves of 1 Nov 17:44 and 18:27 carry the window and the kappa = 1 result.
