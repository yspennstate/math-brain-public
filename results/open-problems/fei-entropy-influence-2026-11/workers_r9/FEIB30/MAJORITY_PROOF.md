# Majority limit

PROVED. For every fixed 0<lambda<1 and each of the three predictors, Ov_lambda(Maj_n), along odd n, converges to the finite limit below. L=0 identically, because the Fourier spectrum is supported on odd cardinalities.

Put a=1-lambda, let X have the arcsine density

    dP(X=x)=dx/(pi sqrt(x(1-x))),  0<x<1,

and define

    r(x)=min(x/[a(1-x)],1/lambda),
    p_thin(x)=min(x,a),
    p_ratio(x)=min(1,x/[a(1-x)]),
    p_lrat(x)=min(1,lambda*x/[a(1-x)]).

Then, for any one of these p,

    K_infinity = E[p(X)/X],
    cost_infinity = E[-log2 p(X)],
    Ov_infinity = log2 K_infinity + cost_infinity.

These are convergent one-dimensional integrals, which identify the limit without an uncomputed limit in n. majority.py evaluates them, and evaluates K and cost again by independent quadrature as a check.

## Exact coefficients and the size-biased law

Write n=2h+1. The mass of an individual k-set is zero for even k, and for odd k it is

    mu_k = [2^(-2h) C(2h,h)]^2
           [C(h,(k-1)/2)/C(2h,k-1)]^2.

This follows, for example, by differentiating majority in one coordinate: its derivative is the indicator that the remaining 2h inputs have h ones; the signed binomial transform of that middle layer gives the formula. The total influence is exactly

    I_n=n*2^(-2h) C(2h,h).

The distribution relevant for Q is q_n(k)=k C(n,k) mu_k/I_n. For k=2r+1 it simplifies to the particularly useful exact formula

    q_n(2r+1)=4^(-h) C(2r,r) C(2(h-r),h-r).

It sums to one by the generating identity (1-z)^(-1/2)(1-z)^(-1/2)=(1-z)^(-1). This is a beta-binomial distribution on r, with parameters h,1/2,1/2. Equivalently choose Z~Beta(1/2,1/2), then r~Binomial(h,Z). It follows directly by conditional variance, or by Stirling's formula, that k/n converges weakly to X. In particular this is not the density proportional merely to x^(-1/2): the other endpoint contributes (1-x)^(-1/2) as well. For uniform tail estimates,

    q_n(k) <= C/[sqrt(k)*sqrt(n-k+1)]

with an absolute C, from the standard upper/lower central-binomial estimates.

## Noisy ratios

Let u_n(k)=sum_{j>=k, j odd} C(n-k,j-k) mu_j lambda^(j-k). By symmetry and the posterior-mean identity,

    (n-k) lambda u_n(k+1)/u_n(k)
       = E[j-k | a fixed k-set is contained in U, weight lambda^(j-k)].

For consecutive nonzero summands A_j in this sum, the coefficient formula gives exactly

    mu_(j+2)/mu_j = [j/(n-j-1)]^2,
    A_(j+2)/A_j = lambda^2 j^2 (n-j)
                  /[(n-j-1)(j-k+1)(j-k+2)].

For k/n->x in (0,1), this ratio is asymptotically [lambda*y/(y-x)]^2 for j/n->y. If x<a, it is above one before y=x/a and below one after; comparisons of products of ratios away from that point give exponentially vanishing mass outside every fixed neighborhood. If x>=a, the ratios favor the endpoint and j/n->1. This argument works for either parity of k. The posterior-mean formula therefore gives

    u_n(k+1)/u_n(k) -> r(x).

The equality case x=a has the same limit from both sides. At fixed positive x this convergence is uniform on closed subintervals not containing a; a neighborhood of a has vanishing arcsine mass, and the limit is continuous there.

## Passing from pointwise limits to expectations

Here are tail bounds that justify the integrals, rather than treating a saddle approximation as a proof. For each fixed lambda there are positive constants c_lambda,C_lambda,delta_lambda and n0 such that

    r_n(k) >= c_lambda min((k+1)/(n-k),1),  0<=k<n,
    r_n(k) <= C_lambda (k+1)/(n-k),      k<=delta_lambda n, n>=n0.

These follow from the displayed exact summand ratio. Details of the comparisons: put l=j-k. Below l=lambda*k/4 the forward ratio is at least four once k exceeds a fixed lambda-dependent constant. Compare mass below half of min(lambda*k/4,(n-k)/2) with the following interval. This bounds the posterior mean below by a fixed lambda-dependent multiple of min(k+1,n-k). If this interval contains fewer than two parity-compatible positions, the first nonzero term (even k), or the ratio A_(k+2)/A_k>=lambda^2*k^2/2 (odd k), supplies the needed bound. For bounded k these same first-term comparisons give a positive lambda-dependent constant. The posterior-mean formula proves the first inequality. The minimum is essential near the upper endpoint, since r_n(k)<=1/lambda always.

For the upper inequality choose a constant C so large that lambda^2(1+1/C)^2<1, then choose M so that multiplying this by M/(M-1) still gives rho<1. Whenever l>=C(k+1) and n-j>=M, the forward ratio is at most rho. Thus the mass after that point has a geometric tail. At the final M possible positions, the extra factor (n-j)/(n-j-1) is bounded and occurs only a fixed number of times. Taking delta_lambda small ensures that these endpoint terms lie a linear distance after C(k+1); their exponentially small mass contributes a bounded amount to the posterior mean. Hence E l<=C_lambda(k+1). Enlarging constants covers the finite set of small n. All constants here may depend on fixed lambda, which is sufficient for convergence.

It follows for each of the three predictors that

    -log2 p_n(k) <= C_lambda + log2(n/(k+1)),
    p_n(k) <= C_lambda (k+1)/n when k<=delta_lambda n.

The first bound uses min((k+1)/(n-k),1)>=(k+1)/n, r_n(k)<=1/lambda, and the explicit positive formulas for p. Together with the central-binomial tail bound, these imply uniform integrability at zero: the cost tail is bounded by C sqrt(delta)(1+|log delta|)+o(1), and the K tail by C sqrt(delta)+o(1). At one, p is bounded away from zero by the first inequality, and the arcsine tail mass is O(sqrt(delta)); K has no singularity there.

Finally the exact symmetric formulas can be written

    cost_n = sum_{k odd} q_n(k) [-log2 p_n(k-1)],
    K_n = sum_{k odd} q_n(k)
             [p_n(k-1) + ((n-k)/k) p_n(k)],

with the last p_n(n) term omitted. The pointwise limit and the tail bounds give the claimed expectations.

## Explicit limit formulas

Let theta=arcsin sqrt(a). For thin,

    K = (2/pi)(theta+sqrt(a*lambda)),
    cost = -(2/pi) [integral_0^theta log2(sin^2 t) dt
                          +(pi/2-theta) log2 a].

For ratio set b=a/(1+a), theta=arcsin sqrt(b), s=1/a. For lrat set b=a, theta=arcsin sqrt(b), s=lambda/a. In both cases,

    K=(2/pi)[s tan(theta)+cot(theta)],
    cost=(2/(pi ln 2))[-theta ln s+2 integral_0^theta ln(cot t) dt].

Thus K_ratio=4/(pi sqrt(a)), and K_lrat=(4/pi)sqrt(lambda/a). The thin limit tends to exactly two bits as lambda decreases to zero. The latter statement is a limit in lambda after the limit in n, not a uniform finite-n estimate. The brief's heuristic cost of two nats uses the wrong macroscopic level density; it is replaced by the formulas above.
