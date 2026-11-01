# P0017 independent route, written before reading peer proofs

2026-10-10. Route reservation: Gaussian convolution, posterior conditional variance, and the Dirichlet contraction of conditional expectation. Do not use a polynomial/cumulant induction or a localization covariance-potential bootstrap. Prior-route disjointness will be checked against the exact local P0017 record before deriving claims.

Let X have an isotropic log-concave law mu, let Z be an independent standard Gaussian, and put Y = X + sqrt(t) Z for t > 0. Study the posterior law nu_y(dx) proportional to exp(-|x-y|^2/(2t)) mu(dx), and g(y) = E[f(X) | Y=y]. The intended argument is the exact total-variance identity, followed by a posterior Poincare bound and a bound on the Dirichlet energy of g. The hardest piece is a dimension-independent strict contraction of this last energy, or another independent upper bound on the smoothed Poincare constant. A coefficient of one would give only a circular inequality.

Source-status discovery already changes the purpose of the route: arXiv:2610.05474v1 Theorem 1.1 states the full dimension-free isotropic log-concave Poincare bound; arXiv:2610.01447v2 states the same result. These are current primary proof claims. This packet will not claim a new solution, certify their complete proofs, or infer current openness from the September ranking. The route is an independent reproduction and gap audit.

The targeted searches found no P0017 record in the named H/I attempt directories. The old store contains an open-problem card and an attempted-route card for this exact title; their complete targeted source extraction is recorded in STORE_P0017_REPORT.json. w351's route is a coordinate interaction criterion; w352's route is a coordinate conditional-averaging Sobolev obstruction; w356's route is a simplex fiber calculation. Gaussian-noise posteriors use a disjoint calculation. These boundaries were compared after this route was recorded, without adopting their formulas.

## Posterior decomposition and the exact gap

For a log-concave probability mu and t>0, the posterior potential is V(x)+|x-y|^2/(2t). Its curvature is at least 1/t (with convex support allowed), so the standard strongly log-concave Poincare inequality gives C_P(nu_y)<=t and Cov(nu_y)<=t I. Initially take f smooth with compact support so differentiation under the integrals is justified. Differentiating the normalized posterior integral gives

    grad_y g(y) = Cov_nu_y(f(X),X)/t.

For every unit v, scalar covariance Cauchy-Schwarz, followed by the posterior Poincare bound, gives

    |Cov_nu_y(f,v.X)|^2 <= Var_nu_y(f) Var_nu_y(v.X)
                         <= t^2 E_nu_y |grad f|^2.

Taking the supremum over unit v is the squared norm of the covariance vector. There is no sum over coordinates and hence no dimension factor. Integrating in y yields

    E |grad g(Y)|^2 <= E |grad f(X)|^2.

The exact total-variance identity then gives

    Var_mu f <= [t+C_P(mu*gamma_t)] E_mu |grad f|^2.

The usual Gaussian convolution bound C_P(mu*gamma_t)<=C_P(mu)+t follows from total variance conditional on X and Jensen's inequality for the gradient of E_Z h(X+sqrt(t)Z). Substituting it above yields only C_P(mu)<=C_P(mu)+2t when the constants are finite. This does not bound C_P(mu). Generalizing from compactly supported test functions requires the ordinary Sobolev approximation, not a hidden KLS assumption.

A dimension-independent strict averaged energy contraction, or a noncircular bound for the smoothed law, remains the hardest missing step of this route. The next result rules out one sufficient pointwise margin; it does not rule out the averaged contraction.

## Exact pointwise posterior covariance obstruction

Take n=1 and X=E-1, where E is Exp(1). Its density exp(-(x+1)) 1{x>=-1} is log-concave, EX=0 and Var X=1. This is a full-dimensional isotropic measure in dimension one. Let Y=X+sqrt(t)Z with Z standard normal independent of X.

Completing the square gives, for every real y, the conditional law X|Y=y as a N(m,t) variable truncated below at -1, where m=y-t. Set

    alpha=(-1-y+t)/sqrt(t),
    phi(alpha)=exp(-alpha^2/2)/sqrt(2pi),
    S(alpha)=integral_alpha^infinity phi(z) dz,
    lambda(alpha)=phi(alpha)/S(alpha).

Integrating z phi(z) and z^2 phi(z) by parts, using phi'(z)=-z phi(z), gives the normalized first and second moments lambda and 1+alpha lambda. Therefore

    Var(X|Y=y) = t[1+alpha lambda(alpha)-lambda(alpha)^2].

For every finite alpha, lambda(alpha)>alpha because it is the mean of a standard Gaussian conditioned to exceed alpha. Thus the bracket is less than one. As y tends to positive infinity, alpha tends to negative infinity, S(alpha) tends to one, lambda(alpha) tends to zero and alpha lambda(alpha) tends to zero. Consequently

    sup_y Var(X|Y=y)/t = ess sup_Y Var(X|Y)/t = 1.

The essential-supremum assertion is important: the density of Y is positive everywhere and the variance formula is continuous. For every theta<1, an open right half-line has Var(X|Y=y)>theta t and has positive Y-probability. This is not a null-fiber example.

Hence there is no universal theta<1 such that Cov(nu_y)<=theta t I for all isotropic log-concave mu and almost every observation y, even if t is fixed in advance and n=1. The stronger sufficient bound C_P(nu_y)<=theta t is also impossible, because a linear test function shows C_P(nu_y)>=Var_nu_y X. This is a proved special-case obstruction by w353, awaiting independent reviewer w356. It is neither a counterexample to KLS nor a claimed novel theorem.

For the Gaussian control X~N(0,1), posterior variance equals t/(1+t), the variance of the conditional mean for f(x)=x equals 1/(1+t), and the gradient-energy contraction equals 1/(1+t)^2. The total variance is exactly one. The Gaussian computation does not supply a uniform pointwise margin for the exponential example.

Reproduction: python -X utf8 ~/brain_workers/w353/verify_packet.py, receipts in COMPUTE_GATE.json and MEASUREMENTS.json. Floating-point convergence is evidence; the limit and essential supremum above are proved by the displayed identities.

NEXT: Audit a proposed averaged Dirichlet-contraction estimate with its gradient weights intact; the pointwise posterior margin is refuted and cannot be substituted for that estimate.
