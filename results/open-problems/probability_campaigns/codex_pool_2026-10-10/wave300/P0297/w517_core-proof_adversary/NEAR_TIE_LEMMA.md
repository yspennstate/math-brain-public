# Conditional two-route near-tie remainder

w517, 2026-10-10. Derived after reading w516 ATTEMPT.md, L1-L5. Independent review by w518 is pending. This conditional finite-model result does not evaluate the LFPP exponent or the limiting measure in w516's input H.

Let X be centered Gaussian with positive semidefinite covariance C, let V=max_i C_ii, and take two positive path lengths l_p=sum_i a_pi exp(xi X_i), p=1,2, with fixed xi>0, a_pi>=0 and each coefficient vector nonzero. Set f_p=log l_p, w_pi=a_pi exp(xi X_i)/l_p, Delta=f_1-f_2, R=(w_1-w_2)^T C(w_1-w_2). For beta>0 let pi_p=exp(-beta f_p)/(exp(-beta f_1)+exp(-beta f_2)) and B_beta=pi_1 pi_2 R.

Define the finite nonnegative weighted gap measure nu(A)=E[R 1{Delta in A}]. Assume there are eta>0, L>=0 and a representative b on (-eta,eta) such that nu restricted to this interval has density b and |b(t)-b(0)|<=L|t| there. These are explicit additional hypotheses, not consequences asserted for the GFF crossing problem.

Then, with b0=b(0)>=0,

    |beta E B_beta - b0|
      <= (2 log 2)L/beta + (4 beta V + 2 b0) exp(-beta eta).    (NT)

In particular lim_{beta->infinity} beta E B_beta=b0 for this fixed finite model. No density assumption is needed away from the displayed interval.

Proof. For probability vectors w,w', positive semidefiniteness gives w^T C w<=V by |C_ij|<=sqrt(C_ii C_jj)<=V and the triangle inequality in the seminorm induced by C gives R<=4V. Thus nu(R)=E R<=4V. Algebra for two alternatives gives

    beta pi_1 pi_2 = K_beta(Delta),
    K_beta(t)=beta exp(-beta |t|)/(1+exp(-beta |t|))^2.

This is a probability density. Its tails have integral 2/(1+exp(beta eta)) and its first absolute moment is (2 log 2)/beta. The latter follows by integrating the logistic survival function: 2 integral_0^infinity (1+exp(beta t))^(-1) dt=(2 log 2)/beta. Hence beta E B_beta=integral K_beta(t) nu(dt).

On |t|<eta, integrate |b(t)-b0| against K_beta and use its first moment. On |t|>=eta, K_beta(t)<=beta exp(-beta eta), so the contribution of nu is at most 4 beta V exp(-beta eta), including any atoms on the two boundary points. The corresponding missing constant-density mass is at most 2 b0 exp(-beta eta). Adding these three errors proves NT. Density nonnegativity almost everywhere and continuity at zero imply b0>=0. All expectations are finite because R<=4V.

For a family indexed by n with scale T_n>0, the normalized bound is

    |beta_n E B_{n,beta_n}/T_n - b_n(0)/T_n|
      <= 2 log 2 L_n/(beta_n T_n)
         + [4 beta_n V_n/T_n + 2 b_n(0)/T_n] exp(-beta_n eta_n).

This licenses a joint n,beta limit only if the right side tends to zero and b_n(0)/T_n has a determined limit. Fixed-n uniqueness of the minimizer, or a fixed-n zero-temperature limit, supplies neither condition.

For independent N(0,1) single-edge fields, Delta is N(0,2xi^2), R=2 and b(t)=(xi sqrt(pi))^(-1) exp(-t^2/(4xi^2)). Thus b0=1/(xi sqrt(pi)); the switching limit is nonzero although B_beta tends to zero almost surely. This agrees with the independently saved O1 and provides a finite control, not a uniform LFPP estimate.

For more than two paths, pair probabilities pi_p pi_q are not the two-route logistic kernel: all other path lengths enter the denominator. A pairwise near-tie density alone is insufficient; one must also control whether those alternatives are competitive with every other path. No sum of NT over pairs is asserted to identify w516's full switching measure.

## Exact three-route obstruction to an unqualified pairwise extension

Let Z,U,V0 be independent N(0,1), xi>0 and M>=0. Take three parallel edges with log lengths f1=xi(Z+U), f2=xi(Z-U), f3=-M+xi V0. The field covariance is diag(2,2,1), hence positive definite; all base lengths are positive. The covariance distance for the first pair is R12=4 and its two-route weighted gap density at zero is b12(0)=2/(xi sqrt(2 pi)).

In the full three-route soft minimum, however,

    lim_beta beta E[pi1 pi2 R12]
      = [2/(xi sqrt(2 pi))] Phi(-M/(xi sqrt(2))).             (3R)

Thus at M=0 the first pair's contribution is half its two-route value; as M grows it can be arbitrarily smaller. The missing premise is competitiveness against the third route at the pair's tie, not merely a regular density of the pair's gap.

Proof. Factoring exp(-beta xi Z) out of the full denominator gives

    pi1 pi2 = [2 cosh(beta xi U)
               + exp(beta[M+xi(Z-V0)])]^(-2).

In the expectation of 4 beta pi1 pi2, substitute t=2 beta xi U. The resulting integral has prefactor 2/xi and Gaussian density phi(t/(2 beta xi)). It is bounded by (2/xi)phi(0)/(4 cosh(t/2)^2), which is integrable with integral (2/xi)phi(0). For almost every Z,V0 the limit of the denominator is 4 cosh(t/2)^2 if V0-Z>M/xi and infinity otherwise. Dominated convergence applies to this transformed integral, not to beta pi1 pi2 pointwise in U. Since V0-Z is N(0,2) independent of U, integrating the surviving event yields 3R. At the equality threshold the Gaussian probability is zero. This proves the finite positive-definite example without using independent path costs as a stand-in for the GFF.

The displayed formula is a counterexample to replacing a full-model pair contribution by its isolated two-route density. It is not a counterexample to w516 L1-L5, which retain the full path probabilities.

Remaining hardest input: derive and evaluate the relevant competitive weighted gap laws, with quantitative regularity uniform in cutoff and path family, and the within-path occupation term at scale log(1/epsilon). This is still unproved for the actual GFF optimization.
