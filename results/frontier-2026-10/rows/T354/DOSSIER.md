# T354 Convergence of Adam with the hyperparameters used in practice

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (abstracts read 16 Oct
08:3x, the 16 Oct 06:40 audit (status PARTLY, Adam two-cycle diagnostic) and worker L's pointer to 2208.09632 Prop E.1).

## STATUS (20 Oct 11:2x, agent B)
TARGET 1 is answered for the scalar model and for its coordinatewise vector form; the record, scripts and runs are in
agent_B/NOTE.md. Under a vanishing step Adam (PyTorch form, bias correction on) settles at the zero x* of the
frozen-x drift, and the residual is f'(x*). To first order
    x* = (1 - beta2) K r B3 / (2 abar B2) (1 + O(1 - beta2)),   r = sqrt(B2)/(sqrt(B2) + eps),
with B2, B3 the second and third moments of the per-example gradients at the optimum. K = (1 - beta1)/(1 - beta1 beta2) under
with-replacement sampling; under reshuffling K_rr has a closed form (kclosed.py): at beta1 = 0 it is 1/2 when n(1 - beta2) is
small and tends to 1 as n(1 - beta2) grows. So the residual is linear in 1 - beta2, does not vanish with the step at fixed
beta2, and is zero for symmetric noise; this gives the "matching lower bound" half of the STATEMENT in the scalar class.
VERIFIED (two audits each, audit_A/ and audit_C/): the first-order law for iid and RR, with momentum, with unequal
curvatures (eps = 0 and eps > 0), the vector case with per-sample Hessians, the next-order term at eps = 0 and eps > 0, the remainder
O((1 - beta2) x*) uniformly in n at eps = 0 and at eps > 0, and uniformly in beta1 (a comonotone transposition identity; on the exact root the
coefficient is 0.993 from beta1 .9999 to .999999 while K_rr falls a hundredfold). End-to-end Adam runs (2e6 steps) land on x* to within 0.3%.
The eps > 0 next-order term in closed form is verified too (second audit, AUDIT_CEPS, twelve Monte Carlo rows on two noise laws).
Nothing in the scalar law is left at one audit. Not attempted: the general
smooth nonconvex theorem of the STATEMENT; the scalar result fixes the order of the residual such a theorem must allow.

## STATUS (21 Oct 04:1x, agent A): the general smooth nonconvex case, vanishing step
general_A/THEOREM.md. Proposition 1 (proved, one audit owed): at frozen x the reshuffled Adam drift is
h_j = d_j f phi_j + phi'_j Cov(m_j, v_j) + R_j, with |Cov| <= (1 - b2)|C_j|(K + 1), C_j the per-coordinate covariance of
g and g^2 over the n examples, and R_j = O(1 - b2) times the variance of g^2 plus an exp(-c/(1 - b2)) tail (negative
association of permutations and Shao's comparison bound the variance and the Hoeffding tail at their iid values). Theorem 2:
under the ODE method's compactness assumption, a.s. liminf ||grad f(x_k)||_phi <= sup (sum rho_j^2/phi_j)^(1/2) =
O(1 - b2), any b1 < 1 and any n; the scalar class shows the order is attained. The tracking step (averaging hypothesis for
state-dependent Markov noise) is a sketch, so Theorem 2 is not yet a proof; it is an a.s. liminf, not a rate.
Theorem 3 (21 Oct 05:1x, written; author's second pass 05:4x fixed the early-epoch coupling, bound unchanged; independent audit owed) is the STATEMENT's form: with eta_k = eta/sqrt(k), eta below an explicit
eta_0, per-example gradients bounded by G, B2_j >= beta > 0 and eps > 0,
    min_{k <= T} E||grad f(x_k)||_phi <= rho_* + O(T^(-1/4) (n + log T/(1 - max(b1, b2)))^(1/2) log^(1/2) T),
rho_* = O(1 - b2) the residual of Proposition 1. The proof couples each epoch to the frozen chain at the iterate l epochs
earlier, whose later permutations are independent of it, so no averaging hypothesis is needed; the lookback l ~
log(1/eta_T)/(n(1 - b)) costs the log T/(1 - b). No condition ties b2 to n and b1 < 1 is free. Constants are crude.
Checks (drift_bound_check.py, d = 2 nonconvex sum, eps 1e-8, b1 0.9, eta 0.05/sqrt(k); dbc_*_run1.txt):
  b2 0.99,  n 16,  2e6 steps:  |h - first order| 2e-5..8e-5 against |h - zeroth| 1.5e-4..6.8e-4; grad f at the Adam endpoint
                               over grad f at the first-order zero 0.88 / 1.09.
  b2 0.999, n 16,  4e6 steps:  |h - first order| under 1.1e-6 (the first-order term removes 98-99 pct of h - zeroth); endpoint
                               ratio 1.85 / 1.40: grad f there is 1e-5..2e-5 and the endpoint still lags the zero by 6e-6,
                               the filter's O(eta_k/(1 - b2)) tracking error, which the theorem does not yet quantify.
  b2 0.99,  n 200, 2e6 steps:  first order removes 75-85 pct of h - zeroth (n(1 - b2) = 2, G^4/B2^2 large); endpoint ratio
                               1.07 / 1.06.
Every measured |Cov| and Var v sits under its bound and every |h - first order| under the remainder bound, but the remainder
bound is loose: 1e-1 against 1e-4 measured at n 16, and vacuous (up to 18) at n 200, where the tail term
exp(-(9/8)(1 + b2)B2^2/((1 - b2)G^4)) is not small. The order in 1 - b2 is right; the constant is a crude one.
Rate test (rate_check.py, 21 Oct 07:0x; 64 reshuffle streams, T 2^22, same problem; rc_b*_n16_run1.txt): the plateau of
E||grad f||_phi over 1 - b2 is 0.0685 (b2 .99) and 0.0680 (.995); at .999 the run is still falling at 2^22 (reading 0.093,
an upper value). The gap to the plateau decays like k^-1.38 / -1.17 / -0.96, faster than T^(-1/4), so the runs do not
contradict Theorem 3. This test can only falsify; the independent audit is still owed.
Longer runs (T 2^24, rc_b0.999/0.998_n16_T24_run1.txt, finished 21 Oct 08:0x): the last two checkpoints (2^23, 2^24) are
flat at E||grad f||_phi/(1 - b2) = 0.069 (b2 .999) and 0.066-0.067 (.998); the last-eighth plateau prints 0.0734 and 0.0682
(the .999 window still holds unsettled checkpoints). Gap slopes -0.91 and -1.00. Across 1 - b2 from 0.01 to 0.001 the ratio
stays in 0.066..0.073: rho_* is linear in 1 - b2 on this problem, constant near 0.068. Rows in THEOREM.md.

## STATEMENT
Repaired statement (the audit: the row must fix the sampling model, bias correction, the place of epsilon, initialization,
the stationarity measure, the probability mode, the noise class and the step schedule; exact stationarity with a fixed step
can fail without noise; a fixed beta_2 for every problem differs from a fixed problem class; the transformer advantage is a
separate question): Adam with random reshuffling on a smooth nonconvex finite sum of n terms, bias correction on, epsilon
inside the square root's denominator as in the PyTorch default, beta_1 < sqrt(beta_2), beta_2 fixed independent of the
problem, step eta_k = eta/sqrt(k). Prove convergence of min_k E||grad f(x_k)|| to a residual neighbourhood with explicit
dependence on (1 - beta_2), n, the gradient noise and epsilon, or a matching lower bound on the residual.

## FRONTIER
- Reddi, Kale, Kumar arXiv:1904.09237: divergence for hyperparameters chosen before the problem.
- Zhang, Chen, Shi, Sun, Luo arXiv:2208.09632: with random reshuffling, Adam converges to a neighbourhood of stationary
  points once beta_2 is large depending on n, beta_1 < sqrt(beta_2); their Prop E.1 (per worker L) bounds the residual.
- Li, Rakhlin, Jadbabaie arXiv:2304.13972: convergence under generalized smoothness without bounded gradients.
- Defossez, Bottou, Bach, Usunier (2020, cited from memory): simple convergence proof with explicit (1 - beta_2) terms.
- Zhang et al. arXiv:2402.16788 and Kunstner et al. arXiv:2402.19449: transformer advantage via block heterogeneity and
  heavy-tailed class imbalance (a separate row).
- Open: the residual's sharp dependence on 1 - beta_2 and n for fixed beta_2.

## ARCHITECTURE
With beta_2 fixed and n large, the second-moment estimate v_k averages over ~1/(1 - beta_2) recent gradients; when that
window is shorter than an epoch, v_k tracks the current example's squared gradient and the effective preconditioner is
correlated with the current direction, which biases the update; the bias is the residual.

## FAILURE POINT
The bias does not vanish with eta for fixed beta_2 and n >> 1/(1 - beta_2); a lower bound must show it does not average
out over an epoch.

## SHAPE
Days: a scalar finite-sum model (f_i(x) = a_i x^2/2 + b_i x with sum b_i = 0) where the residual can be computed (the
audit's suggested diagnostic of the invariant mean drift).

## OBSTRUCTION
Correlated preconditioner. Moves: compute the drift of the scalar model averaged over a random permutation, as a function
of n(1 - beta_2).

## TARGETS
1. Scalar model: the stationary point of the epoch-averaged Adam drift and its distance to argmin f, as a function of
   n(1 - beta_2) and epsilon.
