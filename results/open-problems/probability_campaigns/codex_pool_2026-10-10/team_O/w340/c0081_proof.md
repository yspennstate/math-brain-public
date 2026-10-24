# C0081: compact subcritical expansions cannot determine a critical pole

Label: proof of a refuted general inference, awaiting w346. This is an analytic model illustrating the obstruction, not a percolation counterexample.

For integer d>=2 put a_d=1-1/d and

F_d(z) = [(1-z)^(-1)+exp(-d)(1-z/a_d)^(-1)]/[1+exp(-d)].

It has nonnegative Taylor coefficients, F_d(0)=1, and its first positive pole and power-series radius are a_d. On every compact interval [0,1-eps], for d large enough that 1/d<=eps/2,

|F_d(z)-(1-z)^(-1)| <= (3/eps) exp(-d).

Indeed both inverse denominators are positive and at most 1/eps and 2/eps, respectively, since 1-z/a_d=(a_d-z)/a_d>=eps/2. Subtracting the baseline leaves exp(-d)/(1+exp(-d)) times their difference. Thus for every fixed eps>0 and every integer k the error is o(d^(-k)) uniformly on that interval. Nevertheless the first pole differs from the baseline pole by exactly 1/d.

Consequently even an all-orders 1/d asymptotic expansion with uniform remainders on every fixed subcritical compact interval cannot, by itself, locate the critical point to first order. The prior C0081 route must establish control in a shrinking critical neighborhood, or exclude small-residue poles by an additional structural theorem. This result neither denies a lace-free percolation expansion nor computes a_4.
