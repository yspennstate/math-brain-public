# P0140: Poisson marking explains the random critical drift

Status: author-checked derivation, no independent review, no novelty claim. Excluded from the current-open target and original-solution counts. The filename preserves the initial candidate workflow. The later primary paper already states an indirect identification with Joseph's independent-increment limit. What is supplied here is a direct calculation and an explicit obstruction to holding the critical drift deterministic.

Sources: van der Hofstad, *Stochastic processes on random graphs*, July12,2017, equations4.5.5 and4.5.20, Open Problem4.1, PDF pp.206,210; https://www.win.tue.nl/~rhofstad/SaintFlour_SPoRG_fin_Saint_Flour.pdf . Dhara,van der Hofstad,van Leeuwaarden,Sen, *Heavy-tailed configuration models at criticality*, December2019 version, equation2.22 and Remark11, PDF pp.9-10; https://arxiv.org/pdf/1612.00650 . Joseph's original independent-increment limit: https://arxiv.org/abs/1012.2352 . Exact comparison with every convention in Joseph's characteristic function remains a separate check; the independence statement below is direct.

## Setup and the distinction in the question

Fix 3<tau<4, c>0, and mu>0. Let Gamma_i be the arrival times of a rate-one Poisson process and set theta_i=(c/Gamma_i)^(1/(tau-1)). Thus the theta_i form a Poisson point process on(0,infinity) with intensity

rho(dx)=(tau-1)c x^(-tau) dx.

Conditionally on these points, give each theta_i an independent exponential clock T_i with rate theta_i/mu. The source's process with a deterministic real parameter lambda is

S_lambda(t)=sum_i theta_i[1{T_i<=t}-(theta_i/mu)t]+lambda*t.

The ordered series is well defined. For small theta_i, its conditional means are O(theta_i^3) and its conditional variances are O(theta_i^3); sum theta_i^3 is finite almost surely. There are finitely many points above1, each finite. A process-level construction also follows from the compensated Poisson representation below.

The important parameter for iid degrees is the RANDOM variable Lambda_0 in equation2.22 of the later paper, not a fixed lambda. Define

Z=lim_(epsilon down0)[sum_(theta_i>epsilon) theta_i^2 - integral_(epsilon,infinity) x^2 rho(dx)].

The small-point part of this compensated Poisson integral converges in L2 and almost surely because integral_(0,1) x^4 rho(dx)<infinity. The large-point part is finite almost surely and has finite first absolute moment because integral_(1,infinity) x^2 rho(dx)<infinity. Its second moment need not be finite. Set Lambda_0=Z/mu.

At the random cutoff epsilon=theta_n, including the nth point changes the sum only by theta_n^2, which tends to0. Since

integral_(theta_n,infinity) x^2 rho(dx)=c^(2/(tau-1))*Gamma_n^(1-2/(tau-1))/(1-2/(tau-1)),

the definition of Z/mu is exactly equation2.22 after telescoping the integrals over[Gamma_(i-1),Gamma_i]. This checks the random-drift convention against the primary source, not merely by analogy.

## Direct independent-increment representation

For every epsilon>0 the cancellation is an identity:

S_0,epsilon(t)+(t/mu)Z_epsilon
= sum_(theta_i>epsilon) theta_i 1{T_i<=t} -(t/mu) integral_(epsilon,infinity) x^2 rho(dx).

By independent Poisson marking, the pairs(theta_i,T_i) form a Poisson random measure with deterministic intensity

nu(dx,ds)=rho(dx)*(x/mu)*exp(-xs/mu) ds.

The jump sum in the last display has independent increments in t, since disjoint time intervals select disjoint sets of this Poisson measure. Its centering is deterministic. Passing to finite-dimensional limits preserves independence, so

L(t):=S_0(t)+(t/mu)Z=S_(Lambda_0)(t)

has independent increments. They are generally NONSTATIONARY: the jump intensity contains exp(-xs/mu).

For completeness, this passage is not based on a formally divergent cancellation. Write the truncated expression as M_epsilon(t)+D_epsilon(t), where

M_epsilon(t)=sum_(theta_i>epsilon) theta_i1{T_i<=t}
             -integral_(epsilon,infinity) x(1-exp(-xt/mu))rho(dx),

D_epsilon(t)=integral_(epsilon,infinity) x[1-exp(-xt/mu)-xt/mu]rho(dx).

On bounded time intervals, the centered contribution from points x<=1 is an L2 martingale in t. The variance contributed by0<x<=epsilon is bounded by

(T/mu) integral_(0,epsilon) x^3 rho(dx),

which tends to0 because tau<4. Doob's inequality gives uniform-in-time L2 convergence of this small-point martingale. The deterministic drift converges uniformly on bounded time intervals because its integrand near0 is O(x^3), uniformly for bounded t. The finitely many large points and their finite deterministic compensator cause no problem. Hence L has a cadlag version obtained by this construction, and S_0=L-(t/mu)Z does too.

The deterministic drift can also be evaluated:

D(t)= - (tau-1)c * Gamma(4-tau)/[(tau-2)(tau-3)] * (t/mu)^(tau-2).

To check the sign and constant, substitute u=xt/mu and integrate twice by parts in the positive integral of u^(1-tau)(exp(-u)-1+u). All boundary terms vanish for3<tau<4. The remaining integral is Gamma(4-tau)/[(tau-2)(tau-3)]. In particular D(t)<0, consistent with depletion of previously discovered vertices.

## A deterministic lambda does not have independent increments

This part checks the strongest way the preceding conclusion could be misreported. Consider increments A=S_0(mu) and B=S_0(2mu)-S_0(mu). A marked point of size x contributes

F1=x1{T<=mu}-x^2,
F2=x1{mu<T<=2mu}-x^2.

Let K(a,b)=log E exp(aA+bB), for a,b>=0. These Laplace transforms are finite. Indeed, large points have nonpositive F1,F2 once x>=1; for small points the linear terms have integrable expectation O(x^3) and the quadratic remainder has integrable expectation O(x^3). The compensated Poisson formula, or its finite-cutoff version followed by these bounds, gives

K(a,a)-K(a,0)-K(0,a)
=integral rho(dx) E_T[(exp(aF1)-1)(exp(aF2)-1)].

For x>=1 both F1 and F2 are nonpositive, so the integrand is nonnegative. If0<a<=1/4 and x lies in[a^(-1/2),2a^(-1/2)], then x>=2 and F1,F2<=-x^2/2. Consequently the integrand is at least(1-exp(-1/2))^2 on this interval. Its rho-mass is

c*(1-2^(1-tau))*a^((tau-1)/2).

The potentially negative part is confined to0<x<1. The two indicators in F1,F2 are disjoint, and

E|F1F2| <= x^3 P(T<=2mu)+x^4 <=3x^4.

Since |exp(au)-1|<=a|u|exp(a|u|) and |Fj|<=2 on this range, the absolute contribution of this whole region is at most

3a^2 exp(4a) integral_(0,1) x^4 rho(dx)=C*a^2 exp(4a).

Thus the mixed log-Laplace difference is bounded below by a positive constant times a^((tau-1)/2) minus C*a^2 exp(4a). Since (tau-1)/2 is strictly less than2, it is positive for all sufficiently small a>0. Independence would make this difference identically0. Therefore A and B are dependent. Adding any deterministic lambda changes only their deterministic means and cannot fix this dependence.

This is a direct counterexample to interpreting the 2017 question as a claim about deterministic lambda after mixing the weights. It does not refute the corrected iid-degree statement, whose random drift is explicitly supplied in the later paper.

## Checks and remaining status limits

The argument has two complementary checks: Poisson marking proves independence after the exact random-slope cancellation; the mixed Laplace estimate disproves independence without it. The latter avoids covariance calculations, which would be invalid because the random slope can have infinite variance. The PPP intensity follows independently from the tail count E number{theta_i>x}=c*x^(-(tau-1)). The source's Gamma-coordinate expression telescopes to exactly the same compensated slope.

No simulation is used as proof. No independent referee has checked this text. The 2019 paper already identifies the corrected law indirectly, so this derivation does not establish an unproved theorem for the corpus and is not counted as an original solution. Later literature may also contain this direct marking calculation; that novelty search remains incomplete.
