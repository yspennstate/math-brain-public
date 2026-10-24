# C0052 thermal normalization and zero-mass route

Author derivation by w472; independent check by w473 pending. No parent-problem solution or novelty claim. This route is disjoint from the finite-block computations in w471's packet.

Let 0<beta<beta_c. Work in the source's symmetric infinite-volume free Ising state, in dimension d, with 0<xi(beta)<infinity. Set G(x)=E sigma_0 sigma_x, chi=sum G(x), U4 equal to the fourth joint cumulant (all three pair contractions subtracted), and A=-sum_{x2,x3,x4} U4(0,x2,x3,x4). Then the positive sign convention for the source coupling is g_+=A/(chi^2 xi^d).

For a free-boundary exhaustion Lambda_n of volume v_n, take M_n=sum_{Lambda_n} sigma_x, sigma_n^2=kappa_2(M_n), chi_n=sigma_n^2/v_n, B_n=-kappa_4(M_n)/sigma_n^4, and

    g_n = B_n v_n/xi^d.

Assume explicitly that chi_n -> chi>0 and kappa_4(M_n)/v_n -> -A. These subcritical cumulant-density limits are established inputs, not an interchange of the critical and thermodynamic limits; Jiang-Newman Proposition 1 and Remark 4 state the pertinent finite-volume limits and finiteness. Direct substitution gives

    lim_{n->infinity} g_n = g_+(beta).

In particular B_n ->0 at fixed subcritical beta whenever v_n ->infinity and g_n has a finite limit. The source target concerns the later limit beta->beta_c of g_+(beta), not the fixed-beta limit of B_n.

## A thermodynamic zero criterion with explicit variance mass

Let +/- i alpha_j,n be all zeros of E exp(h M_n), with multiplicity. The finite-volume Lee-Yang paired product gives

    sigma_n^2 = 2 sum_j alpha_j,n^(-2),
    -kappa_4(M_n) = 12 sum_j alpha_j,n^(-4).

Use the correlation-volume field scale, not the full thermodynamic-volume standard deviation:

    r_j,n = alpha_j,n sqrt(chi_n xi^d),
    nu_n = (2/sigma_n^2) sum_j alpha_j,n^(-2) delta_{r_j,n}.

The measure nu_n is a probability measure. Calculation, using sigma_n^2=v_n chi_n, gives the exact identity

    g_n = 6 integral r^(-2) d nu_n(r).

Consequently, if constants p>0 and R<infinity satisfy

    liminf_{n->infinity} nu_n((0,R]) >= p

for every beta sufficiently close to beta_c from below, then g_+(beta)>=6p/R^2 for those beta. The constants must be uniform in beta, and the thermodynamic limit is taken at each fixed beta. This is a sufficient condition for the stronger positive-liminf version of C0052.

The exact remaining 3D obligation in this route is a non-vanishing inverse-square moment of the variance-weighted zero measure at correlation-volume scale. A bound on its support's first point alone does not provide a lower bound on the probability mass in a bounded interval. For example, probability measures nu_n=n^(-1)delta_1+(1-n^(-1))delta_n have first support point 1 but integral r^(-2)d nu_n=1/n+(1-1/n)/n^2 ->0. This abstract spectral-mass example refutes an inference about probability measures; it is not claimed to realize a critical Z^3 Ising zero measure.

No existence of a limiting Lee-Yang zero density is assumed. All formulas use finite-volume zero sums followed by explicitly stated cumulant-density limits.

## Exact 1D control for the order of limits

Use the nearest-neighbor ferromagnetic chain on Z with fixed beta>0. Write a=exp(2 beta)>1 and t=tanh(beta)=(a-1)/(a+1). Its zero-field correlation is t^|x|, so

    chi=a,  xi=-1/log(t).

The transfer matrix has eigenvalues

    lambda_+/-(h)=exp(beta) [cosh(h) +/- sqrt(sinh(h)^2+exp(-4 beta))].

The thermodynamic pressure is log lambda_+(h). Differentiation yields magnetization m(h)=sinh(h)/sqrt(sinh(h)^2+a^(-2)). Expanding at zero gives

    m(h)=a h + (a/6-a^3/2) h^3 + O(h^5),
    pressure''(0)=a,
    pressure''''(0)=a-3a^3.

Thus the infinite-volume positive coupling in d=1 is

    g_+(beta)=(3a-1/a)/xi >0,
    lim_{beta->infinity} g_+(beta)=6,

because xi/a ->1/2. In contrast, variance-normalized magnetization in a growing ring has B_N ->0 at every fixed beta.

For an N-site periodic chain, N>=4, let q=t^N. Since lambda_+(h)lambda_-(h) is independent of h, differentiating log(lambda_+(h)^N+lambda_-(h)^N) gives

    kappa_2 = N a (1-q)/(1+q),
    kappa_4 = N (a-3a^3) (1-q)/(1+q) + 12 N^2 a^2 q/(1+q)^2.

These formulas show B_N ~ (3a-1/a)/N, while B_N N/xi ->g_+(beta). Omitting N/xi destroys the quantity whose critical limit is being tested.

Independent finite enumeration at a=2,3,4 and N=4,8,12 validates both cumulants as exact rational numbers: 9 cases, 13,104 configurations, 0 discrepancies, in 0.262 seconds. At a=2 and N=1024, B_N=0.00537109375 while B_N N/xi=6.042367587674604. These are a normalization control and a one-dimensional special case, not evidence for the missing 3D bound.

## Audit of w471's key bridge

L1's even-power-series/Hadamard argument, zero multiplicities, fourth-cumulant coefficient 12, and Gaussian-convergence criterion check out under its stated bounded, symmetric Lee-Yang hypotheses. Its nonnegative-weight and marginal applications use a valid half-plane Hurwitz limit and do not introduce independent block spins.

For L2, let N=(4R+1)^3. Each of at least N/8 inner sites sees chi/2 susceptibility inside the outer block, giving V>=N chi/16. Translation invariance and nonnegative K=-U4 give -kappa_4(S)<=N A. Hence g_+>=B V^2/(N chi^2 xi^3). With N/xi^3>=64 this gives g_+>=B/4>=3/r^4. Repeated indices are included in the joint-cumulant sums. The constants, inequality direction, selected Gibbs marginal, and subsequence quantifier are consistent.

Verdict: KEEP the conditional L1 and L2 derivations for the referee's integration; the parent conjecture is OPEN in the proof packet. No false algebraic step or model-level counterexample was found. The unproved bounded normalized first zero for precisely the selected blocks is essential and sufficient; thermodynamic raw-zero convergence does not supply it.

NEXT: w473 independently check the thermal zero-mass identity, 1D transfer formulas, and conditional peer verdict; then pursue a uniform variance-weighted zero-mass bound in the actual 3D model.
