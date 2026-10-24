# P0321 independent route: elastic correlations and the shear-zero trap

Date: 2026-10-10. Author: w543. Route was recorded in ROUTE_SELECTION.md before reading peer proof proposals. This is an auxiliary-model proof attempt, not a solution of P0321. The full source statement and its unresolved formalization are in STATEMENT.md. Current openness is UNKNOWN.

## Exact auxiliary model

Let T>0 and ultraviolet cutoff Lambda>0. Set P_L(k)=k k^t/|k|^2 and P_T(k)=I-P_L(k), for nonzero k in R^2. Fix 0<=s<2, a>0, b>=0, shear mu>0 and bending kappa>=0. Consider the real centered Gaussian displacement field with spectral covariance

S_mu(k)=T*1_{0<|k|<=Lambda}*[P_T(k)/(|k|^2*(mu+kappa*|k|^2))+P_L(k)/(a*|k|^s+b*|k|^2)].

Fourier integration is dk/(2*pi)^2. At s=0, |k|^s means 1. For mu>0, u is defined modulo a common displacement; its increments exist because the factor |exp(i*k.x)-1|^2 removes the infrared singularity. Define theta=curl(u)/2, C_6^mu(x)=E exp(6i*(theta(x)-theta(0))) and C_G^mu(x)=E exp(i*G.(u(x)-u(0))) for fixed G!=0. No particle process or microscopic Riesz Hessian is being claimed by this definition.

Every correlation below is obtained from the joint Gaussian covariance: for a centered real Gaussian Z, E exp(iZ)=exp(-Var(Z)/2). This uses the full covariance of the difference, not a product of conditional characteristic functions.

## Lemma H1: strictly positive shear gives orientational long-range order

For every mu>0 and kappa>=0,

log C_6^mu(x)=-9*T*integral_{|k|<=Lambda}(1-cos(k.x))/(mu+kappa*|k|^2) dk/(2*pi)^2.

In particular, as |x| tends to infinity,

C_6^mu(x) -> P(mu)=exp(-9*T*Lambda^2/(4*pi*mu)) if kappa=0,

and P(mu)=(1+kappa*Lambda^2/mu)^(-9*T/(4*pi*kappa)) if kappa>0.

Both limits are strictly positive. Hence this model cannot have algebraic sixfold correlation tending to zero, regardless of its longitudinal exponent s.

Proof. Curl annihilates P_L, and its multiplier has squared norm |k|^2/4 on P_T. Thus the spectral covariance of theta is T/[4*(mu+kappa*|k|^2)]. The increment variance is T/2 times the integral in the displayed formula. Multiplication by 6 and the Gaussian characteristic function yield the factor 9*T. For mu>0, the spectral density is integrable, so its cosine transform tends to zero by the Riemann-Lebesgue lemma. Its integral is Lambda^2/(4*pi*mu) for kappa=0 and log(1+kappa*Lambda^2/mu)/(4*pi*kappa) otherwise. This also proves the kappa->0 continuity. A common independent uniform orientational shift can make E exp(6i theta)=0 without changing C_6; the plateau is a two-point statement, not an artifact of using a nonzero one-point mean.

## Lemma H2: translational correlation is algebraic for positive shear

For fixed unit direction n and G!=0, as r tends to infinity,

log C_G^mu(r*n)=-(T*|G|^2/(4*pi*mu))*log r+O(1),

for all parameters of the model above. In particular there are positive constants c,C,r0 such that c*r^(-eta_G)<=C_G^mu(r*n)<=C*r^(-eta_G) for r>=r0, with eta_G=T*|G|^2/(4*pi*mu).

Proof. Directly from the increment covariance,

-log C_G^mu(x)=integral (1-cos(k.x))*G^t*S_mu(k)*G dk/(2*pi)^2.

The longitudinal density is integrable at zero because its radial majorant is a constant times k^(1-s); its contribution is bounded. For the transverse term use

1/[k^2*(mu+kappa*k^2)]=1/(mu*k^2)-kappa/[mu*(mu+kappa*k^2)].

The second term is integrable on the cutoff disk and contributes O(1). Write phi for the angle between G and n. Angular integration of the first term gives

(T*|G|^2/(4*pi*mu))*integral_0^Lambda [1-J_0(k*r)-cos(2*phi)*J_2(k*r)] dk/k.

The angular identity follows by expanding sin^2(theta-phi) and integrating cos(k*r*cos theta); it can be checked independently by circle quadrature. At zero, 1-J_0(t)=O(t^2) and J_2(t)=O(t^2). At infinity, both J_0 and J_2 are O(t^(-1/2)). Thus integral_0^R(1-J_0(t))dt/t=log R+O(1) and integral_0^R J_2(t)dt/t=O(1). This proves the stated exponent. These Bessel bounds are standard analytic facts, not statistical assumptions. No microscopic density-wave identification is supplied.

## Lemma H3: finite-window imitation of algebraic orientational order

Now take kappa>0. Define the mu=0 orientational increment model by

log C_6^0(x)=-(9*T/kappa)*integral_{|k|<=Lambda}(1-cos(k.x))/|k|^2 dk/(2*pi)^2.

This is well-defined for each finite x, and

log C_6^0(r*n)=-(9*T/(2*pi*kappa))*log r+O(1).

For every R>0 and every mu>0,

0<=log[C_6^mu(x)/C_6^0(x)]<=[9*T*mu*R^2/(8*pi*kappa^2)]*log(1+kappa*Lambda^2/mu), for |x|<=R.

Consequently C_6^mu converges uniformly, in relative error on every bounded distance window, to the algebraically decaying mu=0 correlation as mu decreases to zero. Nevertheless every fixed positive mu has the positive infinite-distance plateau of H1. Taking mu->0 before r->infinity changes the observed regime.

Proof. The massless exponent follows from the scalar circle integral (2*pi)^(-1)*integral_0^Lambda(1-J_0(k*r))dk/k and the bounds used in H2. Subtract the two exact log formulas. The difference is

9*T*integral(1-cos(k.x))*mu/[kappa*|k|^2*(mu+kappa*|k|^2)] dk/(2*pi)^2.

It is nonnegative. Use 1-cos(k.x)<=|k|^2*R^2/2 and the disk integral from H1 to obtain the bound. Since mu*log(1+constant/mu) tends to zero, the upper bound tends to zero. Exponentiating gives an explicit relative-error bound exp(B_R)-1. This is a counterexample to inferring an infinite-distance algebraic limit from arbitrarily accurate bounded-window agreement alone; it is not a Riesz-gas counterexample.

## Lemma H4: zero-shear displacement does not acquire ordinary increments

For mu=0, kappa>0, introduce an infrared cutoff epsilon>0. Keep the same longitudinal part and replace the transverse covariance by T*P_T(k)/(kappa*|k|^4) on epsilon<|k|<=Lambda. For fixed x!=0 and G!=0,

-log C_{G,epsilon}^0(x)=[T/(32*pi*kappa)]*(|G|^2*|x|^2+2*(G_1*x_2-G_2*x_1)^2)*log(1/epsilon)+O(1).

The coefficient is strictly positive, so C_{G,epsilon}^0(x)->0 for every fixed nonzero separation. The Gaussian displacement increments have diverging variance and do not converge to an ordinary finite Gaussian increment field. In contrast, the orientational increment correlation has the finite limit in H3.

Proof. At small |k|, expand 1-cos(k.x)=(k.x)^2/2+O(|k|^4*|x|^4). The remainder, divided by |k|^4, is integrable. With e=k/|k| and e_perp its unit perpendicular, the divergent coefficient is

T/[2*kappa*(2*pi)^2] * integral_0^(2*pi)(e.x)^2*(G.e_perp)^2 dtheta.

The angular integral is (pi/4)*(|G|^2*|x|^2+2*(G_1*x_2-G_2*x_1)^2). The radial integral is integral_epsilon^delta dk/k. The longitudinal term is bounded as in H2. This proves both the coefficient and divergence. The limiting characteristic function, zero off zero and one at zero, is discontinuous and cannot be the characteristic function of a finite displacement increment. A field modulo affine functions is a different construction and does not supply the missing particle Gibbs measure.

## Substantive attempt and the single hardest remaining gap

The candidate mechanism is a phase with screened shear, positive orientational stiffness, and an effective massless angle field. H1-H2 rule out obtaining it merely by using a positive-shear harmonic crystal. H3 gives a precise finite-scale trap near mu=0. H4 shows that simply setting mu=0 in a Gaussian displacement model does not construct the particle process.

The single hardest remaining obligation is a controlled microscopic Riesz-jellium-to-compact-angle reduction on a nonempty coupling interval, including dislocations and disclinations, with scale-dependent errors strong enough to preserve the two distinct long-distance correlations. This must simultaneously prove positional disorder and algebraic orientational order. Neither the existence of a Gaussian angle model nor a small fixed approximation error closes it: the error must be small relative to correlations tending to zero, uniformly as the separation grows. No such reduction has been proved here, and the proposed relation of a,b,mu,kappa to the microscopic gas remains open.

Result status: H1-H4 are author-proved special cases for a defined Gaussian auxiliary model; independent review requested from w545. P0321 itself remains unresolved in this packet. No formal proof-check receipt is claimed; no axioms or admissions were hidden behind a numerical test.
