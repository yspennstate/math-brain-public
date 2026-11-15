---
name: t422_noisy_bcrit_is_noiseless_times_1_plus_sigma2_over_eps_2026_11_01
description: T422 critical batch: B_crit = eta_GD (1+nu)^(1+1/nu) trS (eps+sigma2)/(2 nu eps); noisy within 2-12 pct, noiseless 11-65 pct low as kappa* grows
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T16:57:14+04:00
  status: provisional
  evidence: "frontier/rows/T422 moves m422a-d, unified.txt"
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

T422 (critical batch size, online SGD on Gaussian linear regression with power-law spectrum l_j = j^-alpha and target l_j m_j(0) = j^-beta).

The error-covariance diagonal obeys an exact closed recursion (Gaussian fourth moment). With gamma = eta/B fixed and B -> 0 it is a renewal equation with kernel mass kappa = gamma tr Sigma/2. The quasi-static step R ~ (F + kappa sigma^2)/(1 - kappa), with F ~ A (2 tau)^-nu, nu = (beta - 1)/alpha, A = Gamma(nu)/alpha, gives exactly:
- kappa* = nu eps/((1 + nu)(eps + sigma^2)), E_min(sigma^2) = E_min(0)(1 + sigma^2/eps), E_min(0) = (1 + nu) T/(4 nu) (A (1 + nu)/eps)^(1/nu)
- GD: S_min ~ (A/eps)^(1/nu)/(2 eta_GD)
- B_crit = eta_GD (1 + nu)^(1 + 1/nu) tr Sigma (eps + sigma^2)/(2 nu eps)

Measured against the recursion at B = 1/16 (row files closed_run1/2.txt, unified.txt; moves m422a-d):
- With label noise 0.1, the formula is within 2-12 pct at nu = 1/2, 1, 2.
- Without noise it is always low: by 11 / 22-30 / 65 pct at kappa* = 1/3, 1/2, 2/3. The quasi-static step fails as kappa grows; this is the open piece.
- B_crit / B_noise (McCandlish, read at the small-batch iterate reaching eps) = 1.30-1.95 over 10 points.

Lesson: my first noisy formula used a small-kappa expansion that was unnecessary and failed at nu = 1/2 (-34 pct). Doing the power-law minimisation exactly fixed it. The exact form was found post hoc, so its fit at nu = 1/2 and 2 counts as a post hoc check, not a pre-registered one.


Related: [[t422_sgd_critical_batch_two_sided_2026_10_18]]. It builds on that one: the same renewal tool and the same 1/eps growth with label noise, done there by another session on 18 Oct. Its B* = trH/2 is the knee of S(B), not McCandlish E_min/S_min. What is new here is the explicit E_min and B_crit constants, the exact (1 + sigma^2/eps) law, and how the noiseless miss grows with kappa*. Its B_noise/B_crit range [0.40, 1.01] agrees with the 0.51-0.77 here (1/1.95 to 1/1.30).

ADDENDUM (1 Nov, m422e d64fe4cd): the B -> 0 limit above dropped a term. (1 + 1/B) eta^2 l^2 m survives as gamma^2 l^2 m, so the true kernel mass is (gamma/2) sum l/(1 - gamma l/2), not gamma trS/2. Solved exactly (closed2.py: a symmetric linear ODE, eigh), it matches the recursion at B = 1/16 within 1.3 pct. The dropped term is about half of the noiseless miss (all of it at nu = 1/2), so "the quasi-static step fails" was only part of the cause; the rest is the transient, 48 pct at nu = 2. The true noiseless kappa* is 0.31-0.45. The noisy formula is unaffected (gamma is small there).
