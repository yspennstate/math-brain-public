# C0127: growing near-peaks with a common Gaussian factor

Label: proof refuting one explicitly quantified candidate condition, pending w347. An equivalence requiring overlaps tending to zero is not refuted here.

Fix 0<rho<1. For m>=2 let Z_0,Z_1,...,Z_m be independent standard normal variables, and X_i=sqrt(rho)*Z_0+sqrt(1-rho)*Z_i. Each X_i has variance one; distinct coordinates have covariance rho, bounded away from one. Put M_m=max_i X_i. Independence gives

    Var(M_m)=rho+(1-rho)*Var(max_i Z_i)>=rho.

Thus these maxima are not superconcentrated relative to the unit coordinate variance. Any two selected coordinates have covariance at least rho, including maximisers before and after Gaussian noise, so an overlap-to-zero chaos criterion also fails.

Nevertheless, for delta_m=(log m)^(-1/4), the number K_m of coordinates within delta_m of M_m tends to infinity in probability. To prove this, let b_m=sqrt(2 log m), d_m=delta_m/(2 sqrt(1-rho)), and x_m=b_m-d_m. A Gaussian Chernoff bound gives

    P(max_i Z_i > b_m+d_m) <= exp(-b_m*d_m-d_m^2/2) -> 0.

Let N_m count Z_i>=x_m. It is binomial with mean mu_m=m*barPhi(x_m). For x>=1, integrating the Gaussian density on [x,x+1/x] gives barPhi(x)>=exp(-3/2)*exp(-x^2/2)/(sqrt(2*pi)*x). Therefore

    log mu_m >= b_m*d_m-d_m^2/2-log(x_m)-3/2-log(2*pi)/2 -> infinity.

Here b_m*d_m is a positive constant times (log m)^(1/4), which dominates log(x_m)=O(log log m). Since Var(N_m)<=mu_m, Chebyshev gives N_m->infinity in probability. On the high-probability maximum event, each of these N_m coordinates is within 2*d_m of max Z, hence within delta_m of M_m. Thus K_m>=N_m with probability tending to one.

This refutes the rule that a growing number of peaks at a vanishing absolute deficit and pairwise overlaps merely bounded away from one suffices for superconcentration. The fixed common component matters. It does not refute a candidate requiring the absolute overlaps themselves to tend to zero.

The prior two-block example needs a quantifier correction. For two independent Z_1,Z_2 and fixed deficit d>0, the probability both are within d of their maximum is P(|Z_1-Z_2|<=d)=erf(d/2)<1; replication of each coordinate does not change this. Thus that example alone does not refute a condition requiring two low-overlap near-peaks with probability tending to one. The common-factor family above does satisfy a high-probability growing-peaks condition.

Checks: covariance positivity for every finite m; independence of the common factor and maximum; the Gaussian tail bound and binomial variance; exact near-peak deficit scaling; explicit preservation of the nonzero-overlap limitation. Numerical samples illustrate the fixed-deficit version only and are not a proof of the shrinking-deficit asymptotic.
