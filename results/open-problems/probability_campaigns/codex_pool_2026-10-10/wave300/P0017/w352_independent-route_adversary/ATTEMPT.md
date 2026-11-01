# P0017 independent route, frozen before paired proof

Written 2026-10-10. w351's proposed proof has not been read. This is a disintegration/Sobolev route, rather than a stochastic-localization or Appell-coefficient route. It is an obstruction to a proof mechanism, not a counterexample to KLS.

Exact target: for all n >= 1 and all centered log-concave probability measures mu on R^n with Cov(mu)=I, find a universal C such that Var_mu(f) <= C integral |grad f|^2 dmu for every locally Lipschitz f in L^2(mu) with finite gradient energy. Lower-dimensional supports require intrinsic gradients and isotropy on the affine support. The dated ranking omits normalization; unnormalized dimension-free constants would be false by dilation.

Independent approach: split coordinates (U,V), use total variance, and attempt to control the marginal term via the Poincare inequality for V. The step requiring attention is whether conditional expectation T f(v)=E[f(U,V)|V=v] has uniformly bounded gradient energy as an operator from the full joint Dirichlet form to the marginal form. Even in dimension two, isotropy and log-concavity do not suffice.

Take p >= 2, with joint density proportional to exp(-x) 1{x >= |y|^p}. Its potential x + indicator of the convex epigraph is convex, so the law is log-concave. Integrating x gives Y density exp(-|y|^p)/Z_p, where Z_p=2 Gamma(1+1/p). Conditional on Y, X=|Y|^p+E, with E an independent mean-one exponential variable. Let a=1/p and sigma_p^2=Gamma(3/p)/Gamma(1/p). Then |Y|^p has Gamma(a,1) law, EX=1+a, Var X=1+a, EY=0, Var Y=sigma_p^2, and Cov(X,Y)=0 by symmetry.

Set U=(X-(1+a))/sqrt(1+a), V=Y/sigma_p. The joint law mu_p of (U,V) is centered, isotropic, and log-concave. For f(u,v)=u, the input Dirichlet energy is exactly 1. Its conditional expectation is

g_p(v)=(sigma_p^p |v|^p-a)/sqrt(1+a).

Therefore

integral |g_p'(v)|^2 d law(V)
 = D_p
 = p^2/(1+1/p) * Gamma(3/p) Gamma(2-1/p) / Gamma(1/p)^2.

As p tends to infinity, Gamma(c/p) is asymptotic to p/c and Gamma(2-1/p) tends to 1, giving D_p/p -> 1/3. Thus no finite universal C can make integral |(Tf)'|^2 <= C integral |grad f|^2 hold for all isotropic log-concave laws, even in dimension two. The more restrictive inequality using only partial_v f already fails at p=2, since partial_v f=0 but D_2=2/3.

There is no contradiction to KLS: Var(g_p(V))=1/(p+1), and E Var(f|V)=p/(p+1). Conditional averaging creates a narrow gradient layer while its variance shrinks. Applying marginal Poincare to g_p can therefore be very wasteful.

Hardest remaining piece for this route: replace a uniform Sobolev bound for conditional averaging by a direct bound on the variance of the conditional mean that couples both coordinates, or impose a proved quantitative condition on transport/score derivatives. Such a replacement is not established here. Isotropy alone is insufficient for the failed step.

Status: derivation/candidate obstruction awaiting independent referee w353. No claimed solution of P0017 and no novelty claim. Measurements and peer audit will be added as separate files without altering this pre-peer derivation.
