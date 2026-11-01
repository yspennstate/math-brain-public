Independent check of w357's statement-only Gaussian-posterior bridge, 2026-10-10. Derived before reading w357's ATTEMPT.md.

Let X have an isotropic log-concave law mu, G be independent N(0,I), t>0, Y=X+sqrt(t)G, nu_t=Law(Y), and T_t f(y)=E[f(X)|Y=y]. The proposed bridge is one fixed pair (t,q), with t>0 and q<1, such that D_nu_t(T_t f)<=q D_mu(f) for every dimension, law and Sobolev f. Here D_mu(f)=E_mu|grad f|^2.

1. The conditional argument gives non-strict contraction.

For the conditional law mu_y, the convex potential is V(x)+|x-y|^2/(2t), with curvature at least 1/t. Brascamp-Lieb/Bakry-Emery therefore give Cov_mu_y(X)<=t I and Var_mu_y(f)<=t E_mu_y|grad f|^2. Differentiating the normalized Gaussian likelihood yields grad_y T_t f=(1/t)Cov_mu_y(f,X). Cauchy-Schwarz in the direction of the covariance vector gives

    |grad T_t f|^2 <= Var_mu_y(f)/t <= E_mu_y|grad f|^2.

Averaging over Y gives D_nu_t(T_t f)<=D_mu(f). These hypotheses alone have supplied the numerical coefficient 1, and contain no quantitative strict margin. The remaining premise is a genuine averaged gap uniform over all isotropic laws and functions. Unbounded arbitrary-tilt covariance does not itself disprove such an averaged gap.

2. Separately derived variance reduction if the strict bridge is supplied.

For a fixed mu with finite CP(mu), total variance and the conditional Poincare bound give

    Var_mu(f) <= t D_mu(f) + CP(nu_t) D_nu_t(T_t f).

Product Poincare applied to g(X+sqrt(t)G) yields CP(nu_t)<=CP(mu)+t. If the strict bridge holds uniformly in f, take the Poincare supremum (or an approximating maximizing sequence) to obtain

    CP(mu) <= t+q(CP(mu)+t),
    CP(mu) <= t(1+q)/(1-q).

Finiteness for each fixed log-concave law, or a justified regular approximation, is required before rearranging; one must not manipulate infinity as a finite CP. The argument proves an implication from the bridge, not the bridge itself.

3. Rigorous exponential tail lower bound: q must be at least exp(-t/4).

For clarity use the translated law X~Exp(1) on [0,infinity); subtracting its mean makes it isotropic and leaves the energies and channel unchanged after translating Y. Take f_a(x)=exp(a*x) with 0<a<1/2, and center f_a if desired. Let Phi be the standard normal CDF and z=(y-t)/sqrt(t). Completing a square in the Gaussian convolution gives

    nu_t(y)=exp(-y+t/2) Phi(z),
    T_t f_a(y)=exp(a*y-a*t+a^2*t/2) Phi(z+a*sqrt(t))/Phi(z).

For fixed t, as y tends to infinity the CDF ratio tends to 1 and its derivative tends to 0, uniformly for a in [1/4,1/2]. Thus

    |(T_t f_a)'(y)|^2 nu_t(y)
       = exp(-(1-2a)y) [a^2 exp(t/2-2a*t+a^2*t)+o(1)]

uniformly in that parameter interval. A lower bound alone is sufficient: for any epsilon>0 choose R large enough that the coefficient in square brackets is at least a^2 exp(t/2-2a*t+a^2*t)-epsilon for all y>=R and a in [1/4,1/2]. Integrate this tail, use nonnegativity of the omitted integral, and divide by D_mu(f_a)=a^2/(1-2a). Let a increase to 1/2 and then epsilon decrease to zero. This gives

    liminf_(a up to 1/2) D_nu_t(T_t f_a)/D_mu(f_a)>=exp(-t/4),
    D_mu(f_a)=a^2/(1-2a).

Consequently any admissible universal q(t) must satisfy q(t)>=exp(-t/4). At t=1 it must be at least exp(-1/4), approximately 0.778801. The Gaussian linear-function value (1+t)^(-2) is 1/4 at t=1 and cannot be the general log-concave contraction coefficient. This calibrates possible constants; it does not refute existence of some q<1.

A concrete finite test also separates the Gaussian coefficient: t=1, a=49/100 and the tail y>=5. There z>=4. The Gaussian density phi(4)<1/1000 and the Mills inequality imply Phi(z)>999/1000. Set r=Phi(z+a)/Phi(z), so r>=1 and r'>-2/1000. Hence (a*r+r')^2>= (a-2/1000)^2. Direct tail integration gives

    D_nu_1(T_1 f_a)/D_mu(f_a)
      >= ((a-2/1000)/a)^2*(999/1000)*exp(1/2-2a+a^2-(1-2a)*5)
      > (99/100)*(999/1000)*(71/100) > 7/10.

The exponent is -3399/10000>-34/100. The alternating exponential series through the cubic term gives exp(-34/100)>71/100. This is an explicit smooth L2 test function showing the ratio exceeds 0.7, whereas the Gaussian linear coefficient at t=1 is 0.25. Centering the exponential law and the test function leaves this comparison unchanged.

Independent review requested from w359. Status: independently derived special-case arguments and a conditional reduction awaiting mathematical checking. The lower-bound proof needs only a positive tail integral, with no domination of the negative half-line. No numerical integral or formal proof is claimed.

NEXT: Audit whether w357's proof actually supplies the strict uniform averaged gap and respects the exponential lower bound on q.
