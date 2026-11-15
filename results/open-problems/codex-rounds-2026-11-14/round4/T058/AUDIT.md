# Audit of the joint-limit calculation

## Independent derivation of the previous covariance

Let each missing-edge indicator be Z_e, and put eta_e=2Z_e-1. For a
j-set A its independence indicator is

    I_A = q_j product_{e in binom(A,2)} (1+eta_e).

Products eta_F are orthonormal as F ranges over edge subsets. A nonempty
F with v non-isolated vertices occurs in exactly binom(n-v,j-v) j-sets.
If a_v counts edge subsets on v labelled vertices without isolated
vertices, orthogonality gives

    Cov(X_K,X_l) = q_K q_l sum_{v=2}^l
        binom(n,v) a_v binom(n-v,K-v) binom(n-v,l-v).

Using binom(n,v)binom(n-v,K-v)=binom(n,K)binom(K,v), this becomes

    Cov(X_K,X_l)/mu_K = q_l sum_{v=2}^l binom(K,v) a_v binom(n-v,l-v).

This is an independent way to compute the overlap numerator. Partitioning
all graphs by their non-isolated vertex set gives

    a_0=1;  a_v = 2^binom(v,2) - sum_{u=0}^{v-1} binom(v,u) a_u.

In particular a_1,a_2,a_3,a_4=0,1,4,41. The value 41 can also be checked
by inclusion-exclusion: 64-4*8+6*2-4+1=41. The script
recheck_moments.py compares these exact integer numerators with the
overlap formula and reproduces all three large-n ratios from round 3 at
its largest sample.

## Coupling normalization, checked a second way

The forced count has size-biased law. Its mean is E(X^2)/mu, so the mean
increment is Var(X)/mu, not that quantity plus 1. The additional 1 is
already included in the forced chosen set. On the event that A was
originally independent the increment is exactly zero, and on its
complement it is at least one. Thus

    E|D-1| = E[(D-1) 1_{D>=1}] + P(D=0) = ED-1+2q.

This checks the factor 2 in epsilon without differentiating a
characteristic function.

For j=2, X counts missing edges and is binomial with parameters
N=binom(n,2) and 1/2. Forcing one pair changes the count by a
Bernoulli(1/2) increment. Hence ED=1/2 and E|D-1|=1/2 directly. The
variance formula gives the same values. For n=6, j=3, direct pair counting
gives mean 5/2 and variance 5; therefore epsilon=2-1+1/4=5/4, matching
the exhaustive forcing distribution. For j=4 the variance-to-mean ratio
is 125/64, so epsilon=125/64-1+2/64=63/64, again matching enumeration.

## Constants and signs in the characteristic-function estimate

Size bias gives the coefficient
i sqrt(mu)(exp(iz/sqrt(mu))-1)=-z+O(z^2/sqrt(mu)). The negative sign is
necessary: the limiting equation is psi'=-z psi, whose solution is
exp(-z^2/2). The Taylor remainder bound is z^2/(2 sqrt(mu)). Integration
from 0 to |z| gives exactly |z|^3/(6 sqrt(mu)); integration of
|z|epsilon gives z^2 epsilon/2. The integrating-factor kernel is
exp(-(z^2-v^2)/2)<=1 for 0<=v<=z, so dropping it is an upper bound.
Negative arguments follow by complex conjugation.

The dependence bound uses a bilinear covariance, without a conjugate.
Its small-argument expansion begins with -st Cov(V,W), so the coefficient
1 in the absolute-value bound agrees with the second derivative at the
origin. The enumerated dependence-error/bound ratios approach 1 for
small arguments; the largest tested ratio is about 0.991. No factor from
a complex covariance norm is missing: the integral identity is applied
before taking its absolute value, and its kernel is nonnegative.

## Independent route from marginal normality to the joint conclusion

There is also a proof of joint independence that does not use the complex
covariance bound. Marginal convergence implies tightness of the pair.
Take any subsequential joint weak limit (V,W); its marginals are standard
normal. Their continuity makes every upper-right rectangle a continuity
set, so the normalized threshold kernels H_n converge pointwise to the
limit kernel H. Positive association gives H_n>=0. Their integrals are
exactly c_n, which tends to zero. Fatou's lemma gives

    0 <= integral H <= liminf integral H_n = 0.

The limit H is continuous: changing either coordinate changes a joint
tail by at most the corresponding marginal probability, and both
marginals are continuous. A continuous nonnegative function with zero
integral vanishes everywhere. Thus H=0, proving independence. Every
subsequential limit is the product normal law, verifying the joint
conclusion by a second argument.

## Cases and inference limits

Gaussian marginals and zero covariance alone would not suffice. For
example, if V is standard normal and B is an independent fair random
sign, then W=BV is standard normal and Cov(V,W)=0, but |V|=|W| almost
surely. The association/kernel argument is therefore an essential part
of the proof, rather than an inference from the earlier correlation.

The graph is represented using missing edges. Counts are increasing in
these variables; reversing just one coordinate would invalidate the
positive-kernel argument. The induction proving association conditions
on one Bernoulli variable, leaving a product measure on the others.
Zero or one shared vertex entails no shared edge constraint. Equal-set
variance terms and contained adjacent pairs must both be retained.

Both means diverge uniformly only because the phase stays in a fixed
interior band. The marginal-normal argument is not a claim about a
bounded-mean Poisson endpoint regime. The upper endpoint also matters:
the variance error for X_(k-1) is not controlled here if the phase
approaches 1 arbitrarily fast. Finite sample phases differ from targets
by integer-rounding errors; no exact membership in a particular closed
band is inferred merely from the target label.

The rate in PROOF.md is a characteristic-function rate at bounded
arguments. It is not a total-variation or Kolmogorov error rate. Joint
Gaussian convergence describes the normalized fluctuation scale; it
does not prove independence of the unnormalized counts in total
variation, or a limit conditional on a specified exact value of one
count. No conditional relation to chi has been proved, so no
concentration-width bound for chi follows from this work.
