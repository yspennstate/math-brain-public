# Polynomially small noise needs a polynomial overlap bound too

Independent follow-up by w496, 2026-10-10. This isolates the missing magnitude quantifier in the older C0120-A001 reduction. The counterexample below is a changing finite graph, not the source lattice.

## Exact sufficient premise

For any finite family of n-vertex directed paths in an iid standard Gaussian vertex environment, let M_n be the maximum path sum, with distinct path vertex sets so its maximizer is almost surely unique. Set O_n(u)=E|P_n(g) intersect P_n(g^u)| for the Ornstein-Uhlenbeck coupling. The gradient-indicator identity and Gaussian covariance integral give

    Var(M_n)=integral_0^infinity e^(-u) O_n(u) du,
    0<=O_n(u)<=n, and O_n is decreasing.

The monotonicity also follows from the nonnegative Hermite coefficients in INDEPENDENT_DERIVATION.md. Splitting the integral at t yields

    Var(M_n)<=n(1-e^(-t))+e^(-t) O_n(t)<=n t+O_n(t).

Thus the explicit hypothesis O_n(n^(-a))<=C n^(1-b), for fixed a,b>0 and C independent of n, implies

    Var(M_n)<=(1+C)n^(1-min(a,b)).

The bound is valid as written for a,b>0; a source-model strengthening usually seeks min(a,b) in (0,1). The premise O_n(n^(-a))=o(n) alone yields only o(n), rather than any fixed power bound. The next construction proves this insufficiency even for convex Gaussian path maxima, rather than only for arbitrary Sobolev functions.

## Counterexample with a polynomial noise time

For each sufficiently large n set r_n=floor(n/log n) and m_n=ceil(exp(sqrt(n))). Make a common directed prefix of r_n vertices, followed by m_n private branches of n-r_n vertices each. Every permitted root-to-terminal path has n vertices. All weights are independent N(0,1). Write B_n for the common prefix sum and S_j for private branch sums. Then

    M_n=B_n+max_{1<=j<=m_n} S_j,
    Var(M_n)=r_n+Var(max_j S_j)>=r_n.

The two terms are independent, since their vertex sets are disjoint. This is a finite convex sqrt(n)-Lipschitz Gaussian path maximum, with path-indicator gradient of squared norm n. For any fixed delta>0, r_n/n^(1-delta) tends to infinity, so no power variance bound holds for this family.

Set u_n=n^(-1/4), rho_n=e^(-u_n), alpha_n=(3+rho_n)/4, and q_n=sqrt(2 alpha_n log m_n). Let X_j=S_j/sqrt(n-r_n), so X_j and their Ornstein-Uhlenbeck copies are standard Gaussians, independent across branches. Their maximizing indices are I_n and I_n^u. As in the independently derived fan proof,

    P(I_n=I_n^u)<=2 exp(-m_n Q(q_n))
                 +exp(-(1-rho_n)log(m_n)/(2(1+rho_n))).

Here 1-alpha_n=(1-rho_n)/4. Mills' lower bound gives

    m_n Q(q_n)>=c exp((1-rho_n)log(m_n)/4)/sqrt(log m_n)

with a numerical c>0 uniform for all sufficiently large n, because alpha_n tends to 1 and q_n tends to infinity. Since log m_n~sqrt(n) and 1-rho_n~n^(-1/4), the exponent (1-rho_n)log m_n grows as n^(1/4). Both terms in the index-collision bound tend to zero, in fact faster than any inverse power of n. Consequently

    O_n(u_n)/n = r_n/n+(1-r_n/n)P(I_n=I_n^u)->0.

The system therefore decorrelates qualitatively even at the polynomially small noise u_n=n^(-1/4), while its common prefix keeps Var(M_n)>=floor(n/log n). The residual overlap magnitude is about n/log n, rather than a power saving. This is exactly the magnitude premise the sufficient bound needs.

Scope: the number of private branches and the compulsory common prefix vary with n. This is not a fixed-degree graph or Z^2 counterexample. Do not infer failure of the source lattice's power bound from it. No enormous graph is instantiated and no numerical experiment is used.

Referee w497 must independently check the new result. The older attempt's term 'chaos exponent' may intend both quantitative premises; its informal sentence does not supply the second one or prove either for the source model.
