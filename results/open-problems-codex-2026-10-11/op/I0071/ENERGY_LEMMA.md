# Weighted polynomial construction (2026-10-12)

Let m >= 2 be an integer, theta_i >= 1, and

P(u) = sum_{|alpha|=m} binom(m,alpha) c_alpha u^alpha,
c_alpha = product_i theta_i^(alpha_i^2).

All coefficients are positive, so S^m <= P <= C S^m, S=sum_i u_i.
For |beta|=m-1 the coefficient ratio in P_i versus P_j is
c_(beta+e_i)/c_(beta+e_j) = theta_i^(2 beta_i+1)/theta_j^(2 beta_j+1).
Choose theta_i successively backwards, with theta_i >= D theta_j^(2m-1)
for each j>i. This gives P_i >= D P_j pointwise on the positive orthant.

For |beta|=m-2 one has exactly
c_(beta+e_i+e_j)^2 = c_(beta+2e_i)c_(beta+2e_j)/(theta_i theta_j)^2.
Cauchy-Schwarz in the finite sum yields
0 <= P_ij <= (theta_i theta_j)^(-1) sqrt(P_ii P_jj).
Thus all mixed normalized Hessian entries can be arbitrarily small,
simultaneously with the ordered gradient inequalities.

If R is nonnegative invertible lower triangular, choose D large enough that
P_i >= sum_{j>i} (R_ji/R_jj) P_j. Back substitution in R^T lambda=grad P
shows 0 <= lambda_i <= P_i/R_ii. Hence, if Rf <= (1+S)r,
grad P dot f <= C(1+S)S^(m-1) <= C(1+P).

For stochastic transport, the integrated diffusion/transport quadratic form
has diagonal <= -(mu/2) P_ii |grad u_i|^2 under ordinary strict stochastic
parabolicity. Its mixed terms have magnitude bounded by
C sum_{i<j} P_ij |grad u_i||grad u_j|. Choose all theta_i large enough
to absorb these into the negative diagonal. This uses bounded b, not its
derivatives. Lipschitz noise with g_i=0 on u_i=0 gives ||g_i(u)|| <= L u_i;
the remaining Ito corrections can be absorbed at cost C P.

These algebraic claims have direct proofs above. Full SPDE globalization,
the variational Ito justification, the whole-space case, and superlinear
noise extensions are still being audited; this file alone is not a claimed
solution to Problem 7.
