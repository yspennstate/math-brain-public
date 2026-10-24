from pathlib import Path
s=r'''

## A1. Smoothing closes the limit at each fixed scale (proved)

Assume X,Y,(X,Y) have resolvent densities, X satisfies (H), and Y is symmetric. Let nu be a finite positive compactly supported measure of finite product 1-energy. Write nu_1 for its first marginal. Survey Proposition 4.5 (PDF pp.21-23) gives E_X^1(nu_1)<infinity. The original Kanda paper has now been fetched: *Notes on energy for space-time processes over Levy processes*, Nagoya Math. J. 122 (1991), 63-74, DOI 10.1017/S0027763000003536. Its Corollary of Lemma 2.1, printed p.66/PDF p.4, proves BOTH monotonicity in lambda for positive finite-energy measures and monotonicity under positive-measure domination. Its hypotheses are resolvent densities, explicitly stated at printed p.65. This confirms the precise imported positive-measure result used here; it is not used for complex measures.

Let gamma_epsilon be the centered Gaussian measure on R^m with Fourier transform exp(-epsilon |y|^2/2), and let

nu_epsilon=nu*(delta_0 tensor gamma_epsilon).

For the complex partial Fourier measure sigma_y from ATTEMPT.md Section 7, write sigma_y=A_y-B_y+i(C_y-D_y), where all four measures are positive and <=nu_1. Specifically they integrate the positive/negative parts of cos(<y,v>) and sin(<y,v>) against nu(du,dv). Thus each has finite X 1-energy by positive domination. Fourier Cauchy-Schwarz gives, for rho>=lambda>=1,

E_X^rho(sigma_y)<=4(E_X^rho(A_y)+E_X^rho(B_y)+E_X^rho(C_y)+E_X^rho(D_y))
               <=16 E_X^lambda(nu_1).

The second inequality applies Kanda's positive domination and positive-measure monotonicity separately to the four positive measures. It is NOT a claim that E_X^rho(sigma_y) is itself monotone.

The exact sliced-energy identity and Gaussian multiplier yield

E_Z^lambda(nu_epsilon)
 = int exp(-epsilon |y|^2) E_X^{lambda+r_Y(y)}(sigma_y) dy
 <=16 (pi/epsilon)^{m/2} E_X^lambda(nu_1) -> 0

for every fixed epsilon>0, by (H) for X and survey Theorem 4.2. All integrals here are nonnegative Fourier integrals; Tonelli applies. Although nu_epsilon is no longer compactly supported, it is a finite positive measure and the energy criterion allows such measures.

Also

E_Z^1(nu-nu_epsilon)
 = int w_1(x,y)|nu_hat(x,y)|^2(1-exp(-epsilon|y|^2/2))^2 dxdy ->0

by dominated convergence, since the last squared multiplier is between 0 and 1 and original nu has finite 1-energy. This is energy-norm approximation, different from and not ruled out by the earlier diagonal domination obstruction.

## A2. Exact uniformity criterion for removing smoothing (proved)

For EACH such fixed nu, the following are equivalent:

(i) E_Z^lambda(nu)->0 as lambda->infinity;
(ii) D_epsilon(nu):=sup_{lambda>=1} E_Z^lambda(nu-nu_epsilon)->0 as epsilon decreases to zero.

Proof. The multiplier gives E_Z^lambda(nu-nu_epsilon)<=E_Z^lambda(nu) at every lambda. Also the elementary kernel comparison in ATTEMPT.md (7.2) gives E_Z^lambda(tau)<=lambda E_Z^1(tau) for any finite complex measure tau of finite 1-energy.

Suppose (i). Given eta>0, choose M with E_Z^lambda(nu)<eta for every lambda>=M. This bounds the residual energy by eta on that tail. For 1<=lambda<=M it is bounded by M E_Z^1(nu-nu_epsilon), which tends to zero by A1. Therefore limsup_epsilon D_epsilon(nu)<=eta. Since eta is arbitrary, (ii) follows.

Conversely, Fourier |a+b|^2<=2|a|^2+2|b|^2 gives

E_Z^lambda(nu)<=2 E_Z^lambda(nu-nu_epsilon)+2 E_Z^lambda(nu_epsilon).

At fixed epsilon the second term tends to zero by A1. Thus limsup_lambda E_Z^lambda(nu)<=2D_epsilon(nu); letting epsilon decrease to zero proves (i). QED.

This is an exact per-measure reformulation of the symmetric-partner gap. It identifies precisely the needed exchange of two limits. It does not prove uniformity from energy-norm approximation alone.

## A3. A fixed, already-(H) product defeats a uniform energy-norm shortcut (proved)

One might try to remove smoothing by a bound

E_Z^lambda(nu-nu_epsilon)<=C E_Z^1(nu-nu_epsilon)  for all lambda>=1,

with C depending only on Z and applying to all positive nu. This bound is false, even for a fixed product whose (H) is already known, and even at epsilon=1 with smooth positive probability measures.

Take X with exponent Phi(x)=|x|+i kappa x log|x|, kappa=2/pi, and independent Brownian Y with exponent Psi(y)=y^2. X is a skew 1-stable process satisfying (H); both factors have transition densities. They satisfy a common Rao bound f(A)=2+kappa log A (use f for Brownian as well), so their product Z satisfies (H) by the first attempt's Theorem 3.1. Its Fourier energy kernel is

w_lambda(x,y)=(lambda+|x|+y^2)/[(lambda+|x|+y^2)^2+(kappa x log|x|)^2].

For T>1 set delta=T^{-1/2}, b_T=kappa T log T, and let G_delta(u) be the centered real Gaussian density of variance delta^{-2}. Define the positive probability measure

nu_T(du,dv)=Z_T^{-1} G_delta(u)G_delta(v)[1+cos(Tu+v)] du dv,
Z_T=1+exp[-(T^2+1)/(2delta^2)].

Positivity follows from 1+cos>=0; Gaussian integration gives the displayed normalizer. All these densities are square integrable, so every E_Z^lambda is finite since w_lambda<=1/lambda. Their Fourier transforms are

nu_T_hat(x,y)=Z_T^{-1}[g_delta(x,y)+(1/2)g_delta(x-T,y-1)+(1/2)g_delta(x+T,y+1)],

g_delta(x,y)=exp[-(x^2+y^2)/(2delta^2)].

Let tau_T=nu_T-nu_T*(delta_0 tensor gamma_1). Its Fourier transform is the above multiplied by q(y)=1-exp(-y^2/2). Put q_1=1-exp(-1/2)>0. As T->infinity,

E_Z^1(tau_T) ~ pi q_1^2/[2 kappa^2 T^2(log T)^2],
E_Z^{b_T}(tau_T) ~ pi q_1^2/[4 kappa T^2 log T].       (A3.1)

Consequently E_Z^{b_T}(tau_T)/E_Z^1(tau_T) ~ (kappa/2)log T ->infinity, disproving the bound.

Complete verification of the asymptotics. Expanding the squared Fourier transform gives three squared Gaussian packets and their cross terms. For packet centers c_i,c_j, completion of squares gives exactly

g_delta(z-c_i)g_delta(z-c_j)
 =exp[-|c_i-c_j|^2/(4delta^2)] exp[-|z-(c_i+c_j)/2|^2/delta^2].

Distinct centers here have distance at least T. Each cross integral is at most pi delta^2 exp[-T^2/(4delta^2)], times its fixed coefficient, since 0<=q^2<=1 and w_1<=1; at b_T it is bounded even more strongly by 1/b_T times this quantity. These are negligible relative to either leading expression. Z_T tends to 1 with error exponentially small in T^3.

For the packet centered at zero, q(y)<=y^2/2, so its weighted integral at level 1 is O(delta^6)=O(T^{-3}), using the Gaussian fourth moment in y and zeroth moment in x. At level b_T it is O(T^{-3}/b_T), because w_{b_T}<=1/b_T. These too are negligible in (A3.1).

For either packet centered at (T,1) or (-T,-1), take a ball of radius delta R_T where R_T=sqrt(20 log T). On it, q(y)^2=q_1^2(1+o(1)) uniformly, since delta R_T->0. Also |x|=T+o(1), y^2=1+o(1), and |kappa x log|x||=b_T(1+o(1)) uniformly. Hence

w_1(x,y)=(kappa^2 T(log T)^2)^{-1}(1+o(1)),
w_{b_T}(x,y)=(2kappa T log T)^{-1}(1+o(1)),

uniformly on each ball. The integral of the squared Gaussian packet over that ball is pi delta^2(1+o(1)); the omitted Gaussian mass is pi delta^2 exp(-R_T^2)=pi T^{-21}. Bounding kernels by 1 at level 1 and by 1/b_T at the other level shows the omitted tails are negligible relative to (A3.1). Finally there are two such packets, each with coefficient (1/2)^2=1/4, so their combined leading factor is pi delta^2 q_1^2/2. Substitution of delta^2=1/T proves both formulas in (A3.1). QED.

All measures in this example are finite positive and smooth before taking the signed smoothing residual. The theorem disproves a bound uniform over positive input measures, not A2's possible per-measure uniformity for an arbitrary (H) product. The family nu_T changes with T and is not a single non-(H) witness. The example is noncompact, but the global energy criterion quantifies over all finite measures. No compact-support counterexample to this inequality is claimed here.

Numerical verification: second_numerical_checks.py uses 40-point Gauss-Hermite quadrature in each coordinate, exactly splits the nine Gaussian packet products using completion of squares, and uses expm1 to evaluate the small smoothing multiplier. At log T=8,12,16,20 the measured ratios were about 2.546,3.853,5.119,6.387; the asymptotic leading ratios were 2.546,3.820,5.093,6.366. These agree with convergence to the stated asymptotic, but the proof above is the certificate of unboundedness. The job used small arrays and finished in seconds.
'''
p=Path('SECOND_ATTEMPT.md');p.write_text(p.read_text(encoding='utf8')+s,encoding='utf8')
