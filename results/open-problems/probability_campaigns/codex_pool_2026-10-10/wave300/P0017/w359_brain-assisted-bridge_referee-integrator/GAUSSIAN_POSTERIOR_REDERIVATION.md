# Independent derivation before w357's proof is available

w359, 2026-10-10. Compare against w357/STATEMENT_FOR_ADVERSARY.md. This is a referee calculation, pending comparison with w357's complete proof; it is not an independently reviewed new result of w359.

Let X~mu have log-concave density exp(-V), and let Y=X+sqrt(t)G with t>0 and independent G~N(0,I). For smooth compactly supported f, the posterior rho_y has potential V(x)+|x-y|^2/(2t), whose Hessian is at least I/t when V is smooth convex. The nonsmooth log-concave case requires the standard convex-support/approximation version of the same inequality. The original mu need not be strongly log-concave.

Write T f(y)=E[f(X)|Y=y]. Differentiating the Gaussian likelihood and its normalizer gives grad_y T f = Cov_rho_y(f,X)/t. The scalar posterior Poincare and covariance bounds give Var_rho_y(f)<=t E_rho_y|grad f|^2 and Cov(rho_y)<=t I. Hence for every unit u,

    |Cov_rho_y(f,<u,X>)|^2 <= Var_rho_y(f) Var_rho_y(<u,X>)
                              <= t Var_rho_y(f).

Taking the supremum over unit u proves |grad T f|^2 <= Var_rho_y(f)/t <= E_rho_y|grad f|^2. Averaging gives D_nu(T f)<=D_mu(f). This establishes nonexpansion q=1. No step supplies a strict, uniform q<1.

Variance decomposition gives Var_mu(f) <= t D_mu(f)+Var_nu(T f). Product tensorization for independent (X,G), applied to g(X+sqrt(t)G), gives C_P(nu)<=C_P(mu)+t whenever C_P(mu) is finite. Combining these with q=1 yields only C_P(mu)<=C_P(mu)+2t, which does not close a bound.

If a uniform strict contraction D_nu(T f)<=q D_mu(f), q<1, held for some fixed numerical t>0 over the isotropic log-concave class, the same argument would give (1-q)C_P(mu)<=t(1+q), hence C_P(mu)<=t(1+q)/(1-q). Use finite-C_P regular approximations to justify this reduction without presupposing the general bound. Thus strict contraction is a substantial sufficient bridge, not a consequence of the recalled covariance theorem alone.

Calibration: for mu=N(0,I) and linear f(x)=<u,x>, T f(y)=<u,y>/(1+t), so the Dirichlet-energy ratio is (1+t)^(-2). This special Gaussian check cannot justify a uniform strict factor for the full log-concave class.

NEXT: Compare every identity and regularity condition against w357's saved proof, retaining q=1 and identifying q<1 as the unresolved step.
