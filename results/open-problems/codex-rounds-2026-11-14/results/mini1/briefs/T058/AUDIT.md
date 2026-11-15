# Checks and limitations

## Second derivation of the density constants

This derivation uses only the count at entry and exit from a band. It does not sum past cycles as in PROOF.md.

Let d=b-a, s=r^d and v=r^{1-d}. One band stretches x by factor s; the gap to the next band stretches it by v. Write L for the limiting proportion at entry, and U for that at exit. During the band every integer is counted, so U=(L+s-1)/s. During the gap none is counted, so the next entry proportion is U/v. Consequently the entry update is

    L_next=(L+s-1)/r.

This affine map has contraction factor 1/r<1 and unique fixed point (s-1)/(r-1). The limiting exit proportion is r(s-1)/(s(r-1)). The o(1) errors in the actual stretching factors do not change these limits: if e_m is the difference from the fixed point, then e_{m+1}=e_m/r+o(1), which tends to zero by splitting its iterated recurrence into finitely many recent terms and a geometrically small tail. Integer rounding also contributes o(1) after division by x. These are exactly the two expressions in (1).

For d=1/2, s=2^{1/4} and r=s^2. Entry density is (s-1)/(s^2-1)=1/(s+1); exit density is s/(s+1). They sum to one and straddle 1/2, as expected for equal-length alternating bands and gaps in the log coordinate. Both go to zero as d goes to zero and to one as d goes to one in the general formulas. For every 0<d<1 their difference is positive: its numerator is (r^d-1)(r^{1-d}-1). Thus the ordinary density genuinely fails to exist.

An independent coordinate check for logarithmic density puts y=log x. Equation (4) becomes d f(e^y)/dy=(2/log 2)(1-1/y). A complete phase cycle has y-length tending to (log 2)/2 and a phase band of length d has y-length tending to d(log 2)/2. A finite terminal cycle has bounded y-length. The ratio of their total lengths therefore tends to d. This also explains why ordinary counting cannot be replaced by an assertion that fractional parts are uniformly distributed in natural density.

## Check of the exponent and the probabilistic quantifiers

Solving max(t,1-t)/2<=beta gives both t<=2 beta and t>=1-2 beta. Their interval has length 4 beta-1. At beta=3/8 these endpoints are 1/4 and 3/4, and the interval length is 1/2. On that band both candidate exponents are at most 3/8. This independently checks the numerical specialization rather than substituting into a single density expression.

The approximation of theta is uniform, including near integer phase jumps: the proof uses 0<=t<1 throughout and never assumes t is separated from an endpoint. The Lipschitz bound for the maximum then allows an arbitrarily small enlargement or shrinkage of a band, rather than asserting exact equality between the theta band and the fractional-phase band.

For every density-one D, removing its complement changes counting proportions by o(1). Thus a set with lower density 1/(1+2^{1/4}) cannot avoid D eventually. This is stronger than merely exhibiting an infinite exceptional subsequence, which could have density zero.

The fixed-confidence W_q conclusion uses BOTH directions of Conjecture 10. The contradiction to the brief's density-one exponent uses its upper bound on a positive-density phase band. No inference from variance to high-probability interval width is used. Endpoints of integer intervals add at most two to length; their contribution to the exponent vanishes since lambda>=1/4.

There is no canonical single “shortest interval containing the variable with probability tending to one” for an isolated n: the probability rate must be specified. W_q makes the conditional distribution statement precise for each fixed q in (0,1). The conjectured global high-probability intervals also restrict to every subsequence, so they already supply shorter high-probability intervals on the phase band.

## Numerical cross-check

The exact invocation is `OMP_NUM_THREADS=1 nice -n 15 python3 verify_phase.py`. Full output is recorded in LOG.md and verification.json. The script checks direct integer enumeration against inverse-band counting through 200,000, computes the constants by the independent endpoint recurrence, evaluates real interval lengths through phase cycle 2560, and checks the algebraic identity used in deriving theta with independently expanded arithmetic. These are diagnostics; the asymptotic proof does not depend on floating-point certification.

The finite theta values approach their phase slowly. They must not be treated as evidence for a finite-n concentration prediction. Enumeration compares counts for exactly the same finite phase formula, not random chromatic numbers.

## Limits of the result

No unconditional new bound on chi has been proved. No novelty claim is made for the elementary deterministic density theorem. The work supplies a quantified formulation correction and a conditional consequence of the published conjecture. The literature check was bounded and may miss unindexed work. Papers about p tending to zero or one do not decide the fixed-p=1/2 question.
