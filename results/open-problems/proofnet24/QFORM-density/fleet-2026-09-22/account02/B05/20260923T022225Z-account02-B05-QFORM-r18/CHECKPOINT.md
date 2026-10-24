SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T02:22:49Z.
attacking: rough-input interval theorem for the ruled one-sheet coarea geometry, then the convex/two-sheet side without fiber suprema

# Early mathematical checkpoint — rough one-sheet transfer and two-sheet bank exit

Run `20260923T022225Z-account02-B05-QFORM-r18`. Full QFORM remains open.

## Rough-input one-sheet interval theorem

Let independent real X_i have probability densities f_i<=1. Let r_1,r_2,r_3 be orthonormal and Q=lambda_1<r_1,X>^2+lambda_2<r_2,X>^2-mu<r_3,X>^2 with lambda_1,lambda_2,mu>0 and s=min(lambda_1,lambda_2,mu).

The completed ruled estimate in `interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md` gives, for smooth cap-one product laws, the one-sheet density bound
C_+(lambda)=(lambda_1 lambda_2 mu)^(-1/2) int_0^{2pi}[sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2)dtheta <= pi sqrt(2)/s.

This transfers to arbitrary measurable cap-one product densities at the interval level without choosing rough fiber traces. Mollify each f_i by a smooth probability kernel: f_i^eps=f_i*eta_eps, still 0<=f_i^eps<=1. With independent X^eps, Q(X^eps)->Q(X) in probability. For every majority-side interval [a,b] and every small delta>0, Portmanteau applied to an open enlargement inside the majority half-line gives
P(Q(X) in [a,b]) <= C_+(lambda)(b-a+2delta).
Letting delta down to zero yields
P(Q in [a,b]) <= C_+(lambda)(b-a) <= (pi sqrt(2)/s)(b-a).
At the critical endpoint use P(Q=0)=0, since a nonzero polynomial has a Lebesgue-null zero set under an absolutely continuous product law. Thus the ruled theorem is a genuine rough-law interval inequality; no pointwise representative of a projected density and no unrestricted fiber supremum is used.

## First two-sheet application of the designated partner

Account01/B15's exact rough two-sheet change of variables identifies, for q(z)=z_1^2+z_2^2-z_3^2 and alpha>0,
H_rho(alpha)=1/2 sum_{sigma=+-1} int_0^{2pi} int_{sqrt(alpha)}^infinity rho(sqrt(w^2-alpha)cos theta,sqrt(w^2-alpha)sin theta,sigma w) dw dtheta,
with P(-beta<Q<-alpha)=int_alpha^beta H_rho(u)du.

The completed designated partner account03/B05 theorem `QFORM-ONE-RANK2-TWO-RANK1-BANK-COAREA-v1` (run `20260922T223741Z-account03-B05-QFORM-r19`) gives, in its exact three-bank hypotheses with invertible indefinite scalar-bank compression B, aggregate determinant mass m and kappa=sigma_min(B),
||p_Q||_infinity <= 8*2^(3/4)*sqrt(5)*(kappa*m)^(-1/4).
Therefore the exact hyperbolic trace itself obeys
||H_rho||_infinity <= 8*2^(3/4)*sqrt(5)*(kappa*m)^(-1/4)
in that product-provenance class, and every two-sheet interval has the corresponding linear small-ball bound. This pays a genuine curved trace, rather than invoking the refuted X-ray-only mechanism.

Next step in this run: add the definite scalar-pair branch directly by a two-dimensional annulus-area interval estimate, then isolate the singular/near-isotropic embedded-curvature endpoint.
