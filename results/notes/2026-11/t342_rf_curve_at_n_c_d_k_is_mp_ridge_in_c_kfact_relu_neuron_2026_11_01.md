---
name: t342_rf_curve_at_n_c_d_k_is_mp_ridge_in_c_kfact_relu_neuron_2026_11_01
description: [PROVISIONAL] T342: exact-kernel check of claim T342-C001 (20 Oct, already proved); RF (n=inf) risk for a ReLU neuron at N=c d^k is [kappa_k + c_k^2 e(c k!, kappa_k/c_k^2)]/Var (MP ridge); exact kernel check k=1 0.008 at d=800, k=2 off +0.055 at psi 0.25 (1/d degree-1 residual)
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T18:37:13+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



Pushed 52f724a (research_pushes/2026-11-01-loop-T342-rf). Exact population risk via arc-cosine kernel, no sampling. Prediction (within 0.03 everywhere) failed for k=2 at psi 0.25 and 0.5. Related: [[t293_random_weights_learnable_every_poly_width_smoothed_corollary_w0_2026_11_01]]

AUDIT 1 Nov (same day): the limit formula was already claim T342-C001 (an agent, 20 Oct, via 2403.08160 Thm 4, reviewer PASS), recorded only in the row frontier log 06_math_research/frontier/rows/T342/moves.jsonl. My curve is algebraically identical. What is new here is only the exact-kernel finite-d check. Note re-pushed d763776 as a check of C001; frontier move 9b9c231c.

**Update 1 Nov 21:2x (finite-d formula, verified on 30 rows).** The exact risk 1/2 - b^T K^-1 b is a noise-free GP
posterior variance on the sphere. Its deterministic equivalent N = sum_j N_j mu_j/(mu_j+nu), R = sum_j N_j mu_j nu/(mu_j+nu)/Var
with the exact Gegenbauer spectrum reduces to the limit curve at one level. Against exact risks averaged over 256
targets it is within 0.008 on all 30 rows, d = 16 included; the limit curve is off by up to 0.165. Exact exceeds it by
about 0.002 on 29 of 30 rows. Two lessons: build mu_j from the Hermite series (each r^l splits into degree fractions summing
to 1). Integrating the arc-cosine kernel against P_j directly breaks, because multiplicities up to 1e78 amplify the
rounding. And a one-target-per-draw exact column is noisy by up to 0.04 (0.423 vs 0.380 at d = 16, psi = 0.25); the
earlier "1/d excess" partly came from that noise. Files T342/t342_detequiv.py, t342_detequiv_avg.py.

## Added 1 Nov (late): the finite-d formula, and a correction to the k = 2 numbers above
research_pushes/2026-11-01-loop-T342-detequiv on research-repo: the exact risk is the posterior variance of a Gaussian process on the sphere, so the standard deterministic equivalent with the exact Gegenbauer spectrum, N = sum_j N_j mu_j/(mu_j + nu) and R = sum_j N_j mu_j nu/(mu_j + nu)/Var, reduces with a single level to u^2 + (psi + lam - 1) u - lam = 0, whose root is e(psi, lam). The limit curve is its d -> infinity case, with nothing fitted. The spectrum comes from k(r) = sum_l c_l^2 r^l by Gauss-Jacobi quadrature (fractions sum to 1 to 1e-10). A first version integrated the arc-cosine kernel directly; its rounding times multiplicities up to 1e78 broke the trace, and those numbers were discarded.
Correction: the 3-draw exact column used above is the noisy side (one target a draw; at d = 16, psi = 0.25 it reads 0.423 where 256 targets give 0.380). With 4 feature draws x 64 targets, largest |exact - finite-d formula| is 0.003-0.008 on every row (k = 1, d 50/200/800; k = 2, d 16/28/40), against |exact - limit| of 0.075/0.020/0.007 and 0.165/0.082/0.056. The k = 2 small-psi excess is therefore not a 1/d term: it is the degree-0 and degree-1 fit at its real size, which the finite-d fixed point carries. The exact risk sits about 0.002 above the formula on 29 of 30 rows, the size of a 1/N correction; open.
research_pushes/2026-11-01-loop-T342-card is the math-store card for this result (card/card.json and its link edges), not a separate result.
Open: a proof that the equivalent is exact to o(1) at N = c d^k with the full spectrum (Defilippis-Loureiro-Misiakiewicz should cover it); the finite-n version; the row's Yehudai-Shamir half.
