# Second serious attempt, 2026-10-11

The precise gap is the source-type tail C(N^a epsilon^b+exp(-cN)) at p(0) for arbitrary nonconstant free p, especially repeated-generator sums not covered by isolated Gaussian channels. The prior representative XYX+YXY remains outside the proved classes.

## Two approaches not previously tried

1. **Noncommutative rank and operator scaling.** Linearize p at its constant term to a pencil with singular deterministic coefficient. Ask whether full noncommutative rank/capacity, rather than invertibility of that coefficient, gives polynomial least-singular-value tails for Gaussian blow-ups. Search the brain for operator scaling, Gurvits and full-rank Gaussian pencils. The difficulty is quantitative: algebraic full rank alone supplies no uniform small-ball exponent, and Han's identity-coefficient theorem cannot be applied by an invertible deterministic change of coordinates when that coefficient is singular.

2. **Diagonalizable-generator conditioning plus pseudospectral area.** For a polynomial linear in Y, of the form sum a_l(X) Y b_l(X)+Q(other generators), the coefficient map on vectorized Y has eigenvalues h(lambda_i,lambda_j), h(u,v)=sum a_l(u)b_l(v). Use exact one- and two-point Ginibre eigenvalue densities to bound small h values. Control the random change-of-basis condition number using the expected area of the epsilon-pseudospectrum and the already proved deterministic-mean Gaussian bound, rather than assuming Ginibre eigenvectors are well conditioned. Decompose the conditional Gaussian covariance into an independent isotropic component and a remainder.

Approach 2 is more promising because all three required inputs have explicit finite-dimensional formulas. Start with X^2Y+YX^2: h(u,v)=u^2+v^2, and h(z,z)=2z^2 is not identically zero. An initial obstacle is the intrinsic kernel for h(z,z) identically zero (commutator channels); this is subsequently overcome by the separate off-diagonal baseline described below. The approach does not handle arbitrary nonlinear occurrences of Y.

## Initial calculations (now proved in RETRY_PROOF.md)

- Uniform Gaussian deformation bound suggests E sum_(|lambda_i|<=8) ||P_i||^2 <=81N^3 via Fatou and disk radius 9 pseudospectral area. If right eigenvectors have unit norm, kappa(V)^2<=N sum_i ||P_i||^2, giving P(kappa(V)>L, ||X||<=8)<=81N^4/L^2.
- Ginibre R_1<=N/pi and R_2<=N^2/pi^2 suggest P(min_(i,j)|lambda_i^2+lambda_j^2|<=s, ||X||<=8)<=129N^2 s.
- If kappa(V)<=t^(-1/5) and min coefficient>t^(2/5), the Frobenius least singular value of the coefficient map exceeds t^(4/5). Conditional independent-Gaussian decomposition then gives lower tail at most N^3 t^(2/5). The two exceptional events have the same t^(2/5) power. These exponents will be checked in a complete proof in ATTEMPT.md.

Referee hazards: control the *full diagonalizer* rather than individual eigenvalue condition numbers; include i=j in eigenvalue-pair avoidance; account for kappa(V)^2 in the matrix-space similarity; never claim entry independence after nonunitary conjugation; keep the source's bound uniform over epsilon, not only at epsilon=N^(-B).

Further progress: a separate baseline for independent off-diagonal Gaussian entries bypasses the exact diagonal covariance kernel. Its localized-normal case is controlled through a single off-diagonal entry in the corresponding row, with an unconditional density bound and a matrix-norm cutoff. The complete proof in RETRY_PROOF.md, Lemma F/Theorem G, yields exponent 2/(2D+7) for any nonzero h of total degree D, including h(z,z) identically zero. Norm cutoffs, change-of-basis factors, and the residual correlated Gaussian are all retained in the exponent. The faster full-covariance bound remains valid when h(z,z) is nonzero.
