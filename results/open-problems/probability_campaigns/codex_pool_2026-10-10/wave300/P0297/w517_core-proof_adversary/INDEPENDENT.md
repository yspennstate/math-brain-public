# P0297 independent obstruction (w517)

Saved 2026-10-10 before reading w516's proof or claims. Referee: w518, pending. These are elementary graph examples, not LQG metrics or a solution of P0297.

The primary metric definition is an infimum of exponential field integrals over paths. A calculation for an unselected path cannot supply the joint law at its minimizer. The missing input is a sharp, field-dependent all-path crossing estimate, not the existence of the area measure.

## O1: selection changes a centered Gaussian law

Let v>0, rho in [-1,1], and let (X,Y) be jointly centered Gaussian with Var X=Var Y=v and Cov(X,Y)=rho v. Put two edges in parallel between s and t, with lengths exp(xi X), exp(xi Y), where xi>0. The distance is D=exp(xi min(X,Y)). Then

    E log D = -xi sqrt(v(1-rho)/pi).

Proof: min(X,Y)=(X+Y-|X-Y|)/2. The difference has variance 2v(1-rho), and E|N(0,sigma^2)|=sigma sqrt(2/pi), obtained by integrating the Gaussian density. This also covers rho=1 by degeneracy. Each fixed edge has E log length=0; the selected edge has negative mean for rho<1. At xi=0 the expected log distance has right derivative -sqrt(v(1-rho)/pi), not zero. For arbitrary real xi the expectation equals -|xi|sqrt(v(1-rho)/pi). No conditioning or independence has been silently added.

For rho=0, the selected value has density 2(1-Phi(x/sqrt(v))) phi(x/sqrt(v))/sqrt(v); it is not centered Gaussian. For rho=1 the selected value is the common centered variable. Thus equal one-point laws and equal constant-shift scaling do not identify even this finite optimized quantity.

## O2: the same defect can survive at exponent scale

Fix kappa>0 and xi>0. Let eps_n=exp(-n) and m_n=ceil(exp(kappa n)). Use a graph with m_n parallel unit edges. Compare two field laws:

* Independent: X_{n,1},...,X_{n,m_n} are independent N(0,n).
* Common: all X_{n,i}=Z_n, where Z_n is N(0,n).

All edge marginals in the two models coincide. Both distances satisfy D(X+c)=exp(xi c)D(X). For D_n=min_i exp(xi X_{n,i}), however,

    log D_n/n -> -xi sqrt(2 kappa) in probability (independent),
    log D_n/n -> 0 in probability (common).

Proof, independent case: write r=sqrt(2 kappa). For a>r, a union bound gives

    P(min_i X_{n,i} < -a n) <= m_n exp(-a^2 n/2) -> 0.

For 0<a<r, let p_n=P(N(0,n)<=-a n). Independence gives

    P(min_i X_{n,i}>-a n)=(1-p_n)^{m_n} <= exp(-m_n p_n).

Integrating the standard Gaussian density from a sqrt(n) to a sqrt(n)+1/(a sqrt(n)) shows p_n >= c_a n^(-1/2) exp(-a^2 n/2) for all sufficiently large n, with c_a>0. Hence m_n p_n tends to infinity, proving the other tail. Taking a=r+delta and a=r-delta for 0<delta<r proves convergence; larger deltas follow from a smaller one. No independence between different n is needed. In the common case Var(Z_n/n)=1/n, so Chebyshev gives convergence to zero.

If a_n is any median of D_n, the same limits hold for log a_n/n: convergence in probability to a constant forces every median into each fixed neighborhood of that constant eventually. Therefore log a_n/log eps_n tends to xi sqrt(2 kappa) in the independent model and zero in the common model. This is an obstruction at the exact scale of a normalization exponent. The graphs have changing geometry and no GFF covariance or LQG locality axioms; this is a counterexample only to deductions using marginal Gaussian data and constant shifts alone.

## Narrow lemma boundary

I take the law of the field along a chosen minimizing crossing, and the replacement of joint path entropy/overlap by fixed-path or marginal estimates. I do not take Brownian-map identities, metric KPZ, volume-growth identification, or the other triads' geometric computations.

Primary reference used before the paired proof: Ding, Dubedat, Gwynne, Introduction to the Liouville quantum gravity metric, arXiv:2109.01252v2 (2023), equations (2.1)-(2.5), Remark 2.2. Public source: https://arxiv.org/html/2109.01252v2 . The reduction and exact openness check are recorded separately in ATTEMPT.md and SOURCE_STATUS.json.
