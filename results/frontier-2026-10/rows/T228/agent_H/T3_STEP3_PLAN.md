# T228 target 3, step 3 plan: c0 > 0

agent H, 22 Oct 2026 04:2x. Plan only; no claim.

Model to copy: ABB (arXiv 2102.02299, agent_AF/src/ABB.txt), Proposition 8.1 (txt l.1996: the tail constants are
strictly positive when the stationary law has unbounded support), proved from Lemma 8.2 (l.~2030) with 8.3, 8.4 (l.2515).
Lemma 8.2: pi with support unbounded to the right; if (87) P(T_t < oo) >= K1 t^(-alpha) for the first passage T_t of the
Lipschitz product above t, and (88) P(Y > t) <= K2 t^(-alpha) for the perpetuity Y = sum_n L_n B_(n+1), then
liminf t^alpha pi((t, oo)) > 0.

Our version (radial, iid pairs by Lemma R):
  |x_n| >= Pi_n |x_0| - Y_n,   Pi_n = xi_(n-1)...xi_0,   Y_n = sum_(j<n) (xi_(n-1)...xi_(j+1)) B_j,
from |Psi(x)| >= |Mx| - B and |M_k x_k| = xi_k |x_k|.
  (87') Cramer-Lundberg for S_n = sum log xi_j: E e^(alpha log xi) = 1, m_alpha in (0, oo), non-arithmetic, so
        P(sup_n S_n > log t) ~ C_CL t^(-alpha) with C_CL > 0 (Feller II, XII.5; or Iglehart). Lower bound K1 t^(-alpha).
  (88') Y_n is dominated by the backward perpetuity sum_j (xi_0...xi_(j-1)) B_j in law; its tail is O(t^(-alpha)) by
        Goldie's Theorem 2.3 / Kesten (positive perpetuity, E xi^alpha = 1, E B^alpha < oo). Check the condition on the page.
  Unbounded support: Theorem 1 (iii), pi has positive density on every ball.
Then follow Lemma 8.2's proof: start from |x_0| >= M (pi-mass > 0), stop at T_(t/ (M/2)), and show Y at that time is
below M Pi /2 with probability bounded below; the strong Markov property and stationarity give pi(|x| > t) >= K t^(-alpha).

Read Lemma 8.2's proof on the page before writing (the stopping-time and the dependence of B_j on xi_j need care: the pairs
(xi_j, B_j) are iid but xi_j and B_j are dependent within a pair).
