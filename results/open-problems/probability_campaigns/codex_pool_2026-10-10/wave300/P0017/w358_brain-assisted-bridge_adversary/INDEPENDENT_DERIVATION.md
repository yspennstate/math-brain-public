P0017 independent adversary derivation, 2026-10-10. Saved before reading w357's proof.

Exact target: a universal bound on CP(mu) for every isotropic log-concave probability law in every dimension. CP is defined by Var_mu(f) <= CP E_mu |grad f|^2. Recent primary preprints claim the full target; no novelty claim is made here.

Let Y have density exp(-y) for y>=0, and let X=Y-1. Its law mu is log-concave, centered, and Var(X)=1.

For s<1, define mu_s(dx)=exp(sx)mu(dx)/E_mu exp(sX). The normalizing factor is exp(-s)/(1-s). Under mu_s, Y has exponential rate 1-s, so

    E_mu_s X = s/(1-s),   Var_mu_s X = 1/(1-s)^2.

The linear test f(x)=x gives CP(mu_s)>=1/(1-s)^2. All tilted laws remain log-concave, but their covariance is not bounded by the ORIGINAL isotropic covariance. This does not challenge KLS with the covariance of each current law.

For t>0 and theta=1-t, let mu_(t,theta)(dx) be proportional to exp(theta*x-t*x^2/2)mu(dx). Setting y=x+1 gives a density proportional to exp(-t*y^2/2) on y>=0. Thus

    Var_mu_(t,1-t) X = (1-2/pi)/t.

Every integral is finite, and every such law is log-concave. This refutes an unqualified covariance bound uniform over all Gaussian-damped tilts as t decreases to zero. It is a deterministic family counterexample; it does not refute an expectation or stopping-time estimate for a particular stochastic localization process.

Minimal missing premise: control the covariance of the CURRENT law, or prove a probabilistic/integrated covariance bound for the actual process, including its filtration, time interval, and constants.

There is also an exact factorial/degree boundary check. The log moment-generating function Lambda(s)=-s-log(1-s) has cumulants kappa_m=(m-1)! for m>=2. No fixed K bounds these by K^m for all m. The cumulant estimate in arXiv:2610.05474v1 includes its factorial, so this is a calibration rather than an alleged error in that source.

For f in L2(mu), write its normalized tilt average as F_f(s)=(1-s)E[f(Y-1)exp(sY)]. For |s|<1/2, Cauchy-Schwarz and exponential integrability justify differentiation as a bounded L2 functional. For d>=1,

    T_d f = F_f^(d)(0)/d! = E[f(Y-1)q_d(Y)],
    q_d(y) = y^d/d! - y^(d-1)/(d-1)!.

Using E Y^k=k!, E q_d=0 and

    ||q_d||_2^2 = binomial(2d,d)-2*binomial(2d-1,d)
                  +binomial(2d-2,d-1)
                = binomial(2d-2,d-1).

Hence ||T_d||_(L2->R)=sqrt(binomial(2d-2,d-1)), attained by f=q_d/||q_d||_2. Stirling's formula yields lim ||T_d||^(1/d)=2. Any all-degree bound ||T_d f||<=R^d||f||_2 for this law needs R>=2, and R=2 suffices since binomial(2d-2,d-1)<=4^(d-1).

The source criterion needs all f, all degrees, factorial normalization, and Hilbert-Schmidt tensor norms in higher dimensions. A finite-degree or scalar moment check does not establish it. This example is not a regular smooth strongly log-concave law; using it within the source's regular class needs an approximation uniform in the constants.

Independent referee: w359, pending. Status: derived special cases awaiting independent review. No formal-check receipt or full-target proof.

Additional bridge calibration against the retrieved Gaussian attempt:

For centered X=Exp(1)-1, q1=X and q2=(X^2-1)/2 are centered Appell coefficients. Their Gram entries are E q1^2=1, E q2^2=2, and E q1*q2=1, because E X^3=2. Thus f=q1+q2 has variance 5, while a diagonal Parseval extrapolation predicts 3. Its derivative is 1+X, with Dirichlet energy 2, giving a Rayleigh quotient 5/2. Gaussian CP=1 cannot be transferred by replacing Hermite polynomials with these Appell polynomials. This is a counterexample to that stronger route, not to a universal bound with an unspecified constant.

The arbitrary-tilt obstruction also has a compact-support version. Let Y_L have density exp(-y)/(1-exp(-L)) on [0,L], let m_L=1-L/(exp(L)-1), and let v_L=1-L^2*exp(-L)/(1-exp(-L))^2. The standardized X_L=(Y_L-m_L)/sqrt(v_L) is isotropic and log-concave. Tilting X_L with s=sqrt(v_L) makes Y_L uniform on [0,L]. The tilted variance of X_L is L^2/(12*v_L), which diverges with L. This covers bounded support and finite moment-generating functions for every real tilt parameter.

NEXT: Compare w357's saved hardest bridge with these exact quantifiers and boundary cases.
