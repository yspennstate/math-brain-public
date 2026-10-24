# D0064: investigation, 11 October 2026

Additional complete reductions and finite-moment obstructions are in [REDUCTIONS.md](REDUCTIONS.md). Numerical and formal-check records are in numerical_results.json and lean_check.txt respectively; Lean coverage is algebra only.

At the user's request a second serious attempt is recorded in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md). It proves the full zero-gamma classification under uniform mixing without any moment assumptions, in every dimension and for all alpha in (0,1], and gives an L^2 tail-count obstruction to a proposed directing-measure recovery route. The positive-gamma classification remains unresolved.

## Exact scope of the source

Rhodes and Vargas, arXiv:1305.6221, Section 6.3, printed/PDF page 52, proposes classification of nonzero ergodic lognormal star-scale invariant random Radon measures, up to deterministic multiplication. It explicitly says that a stronger dependence decay than ergodicity must be imposed, but supplies no quantitative condition in this section. Thus the intended conjecture is not a fully specified theorem statement. Section 1.2, page 6, says that gamma is nonnegative, so its written parameter range includes zero.

Definition 2.17, page 17: for every 0<epsilon<=1,

    M =law exp(omega_epsilon(x)) M^epsilon(dx),
    M^epsilon(A) =law M(A/epsilon),

as random measures, with M^epsilon independent of the stationary, probability-continuous Gaussian process omega_epsilon. Section 6.3 assumes E exp(alpha omega_epsilon(x))=epsilon^d, 0<alpha<=1, and writes its centered part as (gamma/alpha) X_t for epsilon=exp(-t), where Cov(X_t(0),X_t(x))=integral_1^{exp(t)} k(ux)du/u and k(0)=1. It gives gamma^2<=2d.

Theorem 2.19 requires good covariance regularity and a finite 1+delta moment. Its classification cannot simply be extended to all alpha=1 measures without proving those additional hypotheses. The prior ledger's appeal to Shamov does not supply them either.

## A boundary construction to referee

Consider d=1, alpha=1/2, gamma=0. Let N be a Poisson random measure on R x (0,infinity) with intensity dx dz z^(-3/2). Define

    M = sum_(x,z) in N z (delta_x + delta_(x+sqrt(z))).

This construction is being checked. Its intended properties are: local finiteness, stationarity, mixing of bounded windows, exact deterministic star scaling, and dependent masses in disjoint intervals. At gamma=0 the proposed dual chaos is stable white noise (Lebesgue control), which has independent masses in disjoint sets. The cluster construction would therefore obstruct the classification under the explicitly stated ergodicity and zero-intermittency hypotheses. It must NOT be called a counterexample to a conjecture with an unspecified extra decay hypothesis, or to the positive-gamma classification.

### Local finiteness (complete proof)

Let K be a bounded Borel set. For z<=1, Tonelli and translation invariance give

    E sum_(x,z): z<=1 z [1_K(x)+1_K(x+sqrt(z))]
    =2 |K| integral_0^1 z^(-1/2) dz =4 |K| < infinity.

A nonnegative random variable with finite expectation is finite almost surely. For z>1, the intensity of points with at least one endpoint in K is bounded by

    2 |K| integral_1^infinity z^(-3/2) dz =4 |K|.

Consequently only finitely many such points occur almost surely; each has finite mass z. Apply this to the intervals [-n,n], n positive integers, simultaneously. The countable weighted sum of Dirac measures is locally finite on R and hence is a Radon measure. It is purely atomic. The Poisson configuration is countable by exhaustion with finite-intensity strips. Distinct endpoints coincide with probability zero, although that fact is not needed for local finiteness.

### Stationarity (complete proof)

For any a in R, (x,z)->(x+a,z) preserves dx dz z^(-3/2), and the cluster endpoints both translate by a. The mapping theorem for Poisson random measures therefore proves stationarity of the entire measure law.

### Exact star equation (complete proof)

For every epsilon>0, the map (x,z)->(epsilon x,epsilon^2 z) preserves the intensity: its inverse Jacobian is epsilon^(-3) and (z/epsilon^2)^(-3/2)=epsilon^3 z^(-3/2). It maps a cluster's two endpoint locations to epsilon x and epsilon x+sqrt(epsilon^2 z), and its two weights to epsilon^2 z. Thus

    [epsilon^2 M(A/epsilon)]_A =law [M(A)]_A.

For an independent copy M_tilde set M^epsilon(A)=M_tilde(A/epsilon), and omega_epsilon(x)=2 log epsilon. The latter is a deterministic, hence degenerate Gaussian, stationary continuous process; independence is automatic. This is exactly Definition 2.17, and E exp(alpha omega_epsilon)=epsilon for alpha=1/2. Its centered covariance is zero, so gamma=0. Any continuous normalized positive-definite k, for example exp(-x^2), may serve in (6.10) because the X_t term is multiplied by gamma=0. The zero covariance of omega satisfies all the covariance conditions of Definition 2.18.

### Mixing and ergodicity (complete proof)

For a bounded Borel window A write S_A={(x,z): x in A or x+sqrt(z) in A}. M restricted to A is a function of the Poisson restriction N|S_A. If A and B are disjoint and every point of B lies to the right of every point of A, then

    S_A intersection S_B = {(x,z):x in A, x+sqrt(z) in B}.

Changing variables y=x+sqrt(z), the intensity of this intersection is

    lambda(A,B)=integral_A integral_B 2/(y-x)^2 dy dx.

Indeed z=(y-x)^2 and dz=2(y-x)dy, so z^(-3/2)dz=2(y-x)^(-2)dy. If their distance is at least R>0, lambda<=2|A||B|/R^2. For windows in the opposite order the same estimate holds by exchanging their names.

The Poisson restrictions to S_A\S_B, S_B\S_A and S_A intersection S_B are independent. Keep the original shared restriction for M|A and replace it for M|B by an independent Poisson restriction with the same intensity. The resulting pair has product marginal law: it uses disjoint independent underlying Poisson randomness for its two coordinates. It agrees with the original pair if both shared restrictions are empty, an event of probability exp(-2 lambda). Consequently the total variation distance (supremum over events convention) between the joint law and its product marginal law is at most

    1-exp(-2 lambda) <= 2 lambda <= 4 |A||B|/R^2.

This is a quantitative mixing bound for the complete restrictions to bounded windows, not just their total masses. In particular it is summable over integer translations of fixed bounded windows. For arbitrary measurable events E,F of the random Radon measure, choose events E_n,F_n determined by its restriction to [-n,n] with P(E symmetric-difference E_n), P(F symmetric-difference F_n) tending to zero. Such approximations exist because bounded-window restrictions generate the measure's sigma field, by the martingale convergence theorem applied to conditional expectations of event indicators and thresholding at 1/2. Translation preserves these error probabilities by stationarity. For each fixed n the bound just proved implies P(E_n intersection T_R F_n)-P(E_n)P(F_n) tends to zero as |R| tends to infinity. The approximation errors then imply the same for E,F. Thus the translation action is mixing. If E is invariant under translations modulo null sets, P(E intersection T_R E)=P(E), while mixing makes its limit P(E)^2. Hence P(E) is zero or one, proving ergodicity.

The measure is nonzero almost surely. The intensity on {(x,z):x in [0,1], 0<z<1} is infinite; exhaustion by 1/n<z<1 gives finite intensities increasing to infinity, so the probability that there are no such points is zero. Each such point contributes positive mass to [0,1].

### Separation from the dual chaos at gamma=0 (complete proof)

For bounded nonnegative compactly supported f the Poisson Laplace formula gives

    E exp(-integral f dM)=exp(-H(f)),
    H(f)=integral_R integral_0^infinity
         [1-exp(-z(f(x)+f(x+sqrt(z))))] z^(-3/2) dz dx.

This integral is finite: for z<=1 use 1-exp(-u)<=u and integrate, obtaining at most 4 integral f dx; for z>1 bound by the indicator that an endpoint is in the compact support, giving at most 4 times its Lebesgue length. These bounds also justify the Laplace formula by truncation and monotone convergence.

Choose A=[0,1], B=[2,3], q,r>0. With a=1_A(x)+1_A(x+sqrt(z)) and b=1_B(x)+1_B(x+sqrt(z)), elementary algebra gives

    H(q1_A)+H(r1_B)-H(q1_A+r1_B)
    =integral (1-exp(-qza))(1-exp(-rzb)) z^(-3/2) dz dx
    =integral_0^1 integral_2^3
         2/(y-x)^2 [1-exp(-q(y-x)^2)] [1-exp(-r(y-x)^2)] dy dx
    >0.

All integrals are finite and the integrand in the last integral is strictly positive everywhere in its rectangle. Therefore

    E exp(-q M(A)-r M(B))
    > E exp(-q M(A)) E exp(-r M(B)).

Their masses are dependent. At gamma=0, standard GMC is Lebesgue measure, and its alpha-stable subordination, up to any deterministic multiplier, has Laplace functional exp(-c integral f^alpha dx). Its restrictions to disjoint sets are independent. The construction above thus has a different random measure law from every dual chaos listed at gamma=0.

### What this proves, and what it does not

This is a complete counterexample to the version of case (3) that assumes only Definition 2.17 (even good covariance regularity), nonzero stationarity, ergodicity, gamma>=0, and the displayed alpha normalization. It remains a counterexample if the additional hypothesis is bounded-window mixing with an integrable rate: here the rate is O(R^-2).

It is not a proved counterexample to a version requiring gamma>0, finite-range independence of measure restrictions, or a sufficiently stronger unspecified decorrelation condition. The source does not state the extra condition precisely, so it is impossible to check that condition line by line. The nondegenerate four-phase classification is not proved here. The correct overall verdict for the intended open problem is PARTIAL unless the intended hypotheses are expressly restricted to those printed and checked above.
