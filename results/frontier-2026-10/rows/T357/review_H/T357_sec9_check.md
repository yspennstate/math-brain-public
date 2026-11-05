# an independent reading check of T357's Section 9 (the causal AMP embedding)

Agent H, 4 Nov 2026 22:4x. Reading only. The source is `T357_GAUSSIAN_COMPLETE_PROOF.md` lines 663-745,
in this repository. This follows `T357_amp_check.md`, which checked Theorem 5. Section 9 was the
second remaining item from `REVIEW_agent_H.md`.

## What I re-derived, and it holds

1. **The index map between GD and AMP is consistent.** With w_0 = 0 we have sigma(0) = 1/2, so R_1 = M(Y - 1/2) is the
   GD residual r_0. That gives the correspondence Q_t <-> w_t and R_{t+1} <-> r_t.
   - Equation (9.5) is w_t = w_{t-1} + lambda[A_0^T r_{t-1} + s r rho_{t-1} v] with rho_{t-1} = z^T r_{t-1}/N, which is
     (9.3) one step back.
   - Equation (9.6) is r_t = M[Y - sigma(A_0 w_t + s q_t z)], which is (9.2).
   - The overlap rho_{t-1} = E[Z R_t] is known before the t-th column update, so there is no fixed point at a step. The
     causality paragraph is right.

2. **The Onsager terms cancel exactly.** Z_t + sum_{h<t} b_{th} Q_h = A_0^T R_t, and Y_t + sum_{h<=t} a_{th} R_h =
   A_0 Q_t. The AMP trajectory is therefore the frozen-overlap GD trajectory, algebraically and at every finite d.

3. **The two comparison inequalities are correct**, re-derived from scratch.
   - *(9.9).* |sigma'| <= 1/4 gives ||S - S_bar|| / sqrt(N) <= ||A_0|| ||w - w_bar|| / sqrt(N) + s Z_N |q_emp - q_t|.
     Here ||w - w_bar|| / sqrt(N) = e_t / sqrt(r), and |q_emp - q_t| <= V_m e_t + eps_q. Together these give (9.9).
   - *(9.10).* ||A_0^T (r - r_bar)|| / sqrt(m) <= C sqrt(r) h_t, and |rho_emp - rho_t| <= Z_N h_t + eps_rho. With the
     factor s r V_m on the v term, this gives (9.10).
   - With e_0 = 0, finitely many steps and (9.8), induction gives max_{t <= T}(e_t + h_t) -> 0 in probability.

4. **The regularity claims hold.** Map (9.5) is affine in the fields. Map (9.6) is Lipschitz with constant 1/4 times the
   field coefficient. Projecting M and Y onto [0, 1] changes no value that is actually observed. Every function has
   polynomial growth.

## What I did not re-derive

- **Nondegeneracy.** The regularization with fresh Gaussian side perturbations, needed when the source theorem requires
  a nondegenerate covariance, is deferred to the companion proof (B04/B01). I did not read that proof.
- **The step from H/sqrt(m) to D = A_0 + (s/m) z v^T.** This covers the operator-norm remainder E_d and the drift in
  (lambda_d, s_d, r_d). It is called "the same finite-time stability estimate". The estimate is routine: one more
  additive term ||E_d|| ||w_t|| / sqrt(N) in (9.9), with ||w_t|| / sqrt(m) bounded by induction. Still, it is stated
  rather than written out.
- **The step-size scale lambda = c / alpha.** I did not recheck it against the GD normalization of Section 1; B01 checked
  that normalization.

## Verdict

I found no gap in Section 9 as written: the indexing, the cancellation and both inequalities check. Together with
`T357_amp_check.md`, the residual risk on T357 is now three things:
- the nondegeneracy regularization, which lives in the companion proof;
- one stability estimate that is stated but not written out;
- a word-for-word comparison with the Wang-Zhong-Fan text.

None of these blocks internal acceptance.
