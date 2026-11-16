---
name: t377_w2s_lower_bound_needs_no_universality_2026_11_02
description: T377 target 1: the weak-to-strong lower bound L_ST >= (3/4) L_TE^2 of 2503.02877 is deterministic, no Gaussian universality; 2610.09044 is conditional on its Assumption 1
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T03:35:34+04:00
  status: provisional
  evidence: "rows/T377/moves.jsonl 1657ad86"
---

T377 (weak-to-strong generalization), Target 1, read 2 Nov 2026 from the main texts of 2503.02877 and 2610.09044v1 (appendix proofs not checked). Move m377a, rows/T377/moves.jsonl 1657ad86, file t377_target1_reading.md.

- Medvedev et al. 2503.02877: the limits of the gain are proved with no distributional assumption. L_ST >= (3/4) L_TE^2 holds for any shrinkage-optimal teacher and student (Thm 4.3, Cor 4.4), and gradient flow from zero is shrinkage optimal. L_ST >= L_TE^2/4 holds for a bounded student (Thm 4.5, Cor 4.6).
- The Gaussian Universality Ansatz there is only behind Thm 3.1's sharper exponent 1.49. The main ReLU bound holds with probability 1 - 3/M_TE.
- Oliveira and Paquette 2610.09044: all theorems are about deterministic equivalents. Assumption 1 (concentration plus universality) carries them to the random ReLU networks.
- So the open part of the row is a feature-learning student (Target 2; see the b9a49845 model move of 30 Oct) and removing Assumption 1 for the sharp constants.


ADDENDUM (2 Nov, an agent, move m377b, moves.jsonl 3034b3c9, t377_basin.*): Target 2, rho = 0 case of the 30 Oct model F = (m+m^2)/2 + c s^3.
- The flow is exactly a planar ODE. A Bernoulli-equation argument gives P(student reaches w*) = Phi(sqrt(d)/(4.562 c)), with 4.562 = 3 J and J = int_0^inf e^{-G} = 1.5207.
- The exact ODE from 4000 starts at d 100 and 1e4 agrees start by start on at least 97.5 percent (d 100) and 99.8 percent (d 1e4) of starts.
- The one heuristic step is m decoupling from s before escape.
(Restored 2 Nov 04:5x: this addendum was in the file at the 04:0x mirror 53236a0c and missing from it by 04:3x, writer unknown.)

ADDENDUM 2 (2 Nov, an agent, move m377c, moves.jsonl 66c2a1f3, t377_fold.* / t377_cusp.*): rho > 0.
- The max near w* folds away at c_bif = 1/(8 rho) (exact: 1.2849 at rho 0.1), at tilt phi = rho. That is half the pole of the 30 Oct small-tilt formula.
- Above the cusp rho_c = 0.2178 there is no fold: the maximum slides continuously toward v.
- Below c_bif every random start at d 1e4 reaches the near-w* max. So any overlap rho > 0 moves the failure from c ~ sqrt(d) to c ~ 1/(8 rho).

ADDENDUM 3 (2 Nov, an agent, move m377d, moves.jsonl 9cbeb9c4, t377_sgd.*): online SGD at d 100, c 2.
- The fraction reaching w* is 0.41, 0.60, 0.83 at eta d 0.03, 0.01, 0.003, against the flow formula 0.8635. The formula is the small-step limit.
- Step noise pushes runs toward the error direction, even below 1/2. Heuristic, not measured beyond d 100: the noise along v scales like c^2, so for c ~ sqrt(d) the flow basin needs eta << 1/d^2.
- Classifier lesson: under noise the near-w* state sits at m about 0.3-0.8, so classify by m vs |s|, not m > 0.9.
