VERDICT: PROVED Exact antipodal four-point minimum-norm ReLU interpolation has bounded positive collision-limit risk.

The preceding all-fixed-n hemisphere result holds. A fresh analytic recheck
and independent scalar verifier recover its localization inequality, correction
construction, risk coefficient 2/d, joint probability 2^(2-n), and critical
moment (d-1)/2. Its infinite expected risks in d=2,3 are unaffected.

The new result solves the precise fourth-point geometry proposed in that report.
Let a=cos(theta/2), b=sin(theta/2), s=sin(theta), and consider

```text
x1=a e1+b e2, x2=a e1-b e2, x3=e2, x4=-e2,
labels=(1,-1,A,B).
```

For every fixed ambient d>=2 and bounded extra labels, every minimum-norm
interpolant has, as theta decreases to zero,

```text
theta Qmin -> 4,
theta ftheta -> 0 uniformly on the unit ball,
R(ftheta) -> [1+(A^2+B^2)/2]/d.
```

Thus the limiting conditional risk is finite and strictly positive: 1/d for
zero extra labels, and 2/d for all four Rademacher extra-label choices.
Unlike the one-hemisphere case, the diverging coefficients cancel in the
function. A close opposite-label pair alone therefore does not force a
theta^-2 population-risk lower bound after further interpolation constraints.

The exact optimizer is unique as a function. Write u=b e1+a e2 and
v=-b e1+a e2. Whenever 0<theta<pi and
A<=1/(2b), B>=-1/(2b), it is

```text
f(x) = (|u.x|-|v.x|)/s + A sigma(v.x)/a + B sigma((-u).x)/a,
Qmin = 4/s + (B-A)/a.
```

The sign conditions hold uniformly over any bounded label set at sufficiently
small angles. The base term equals
sign(x1*x2) min(|x1|/a, |x2|/b). Its bounded pointwise limit outside the
equator is x1 sign(x2). Adding the two correction limits gives
x1 sign(x2)+A sigma(x2)+B sigma(-x2), whose risk is the displayed constant.
The unscaled function does not converge uniformly; the limit is discontinuous
across the equator.

PROOF.md gives every step, the exact finite-angle risk, and its first-order
expansion. The dual certificate has absolute price
min(a|p|,b|q|)/(ab)<=1. Its equality cases force exactly four planar directions,
including when off-plane weights are allowed. The resulting response matrix
fixes all coefficient totals. This proves optimality and uniqueness without
a discretized optimizer. Independent quadrant integration and odd/even
decomposition recover the risk limit.

The model is homogeneous two-layer ReLU regression with objective one half
the sum of squared parameters in both layers, no biases, skips or output
intercept, and unrestricted width or any fixed width m>=4. Test inputs are
uniform on S^(d-1), and risk is measured against zero. The deterministic
antipodal configuration has probability zero under iid continuous sampling.
This theorem does not classify random-design large-sample risk or GD selection.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 recheck_prior.py > prior_output.txt
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_antipodal.py > verification_output.txt
```

Both final commands passed. The new verifier checks 109 admissible angle/label
cases, exact continuous pricing, independently recovered multipliers, two
circle integrals, the quadrant formula, and 9,000 signed ambient directions.
Maximum normalized risk discrepancy is 4.64e-10; maximum interpolation error
is 1.82e-12. Direct activation-arc integration also checks the finite limits
at theta=1e-6, with dimensions 2,3,7 and six label pairs. An independent S^2
surface integral checks the ambient normalization. The final run took 0.2533
seconds, peak RSS 16,252,928 bytes, one thread, actual nice 20. The prior
recheck took 0.1913 seconds and 15,548,416 bytes peak RSS. Commands, output,
and audits are recorded in LOG.md; detailed values are in the JSON files.

Attempts to break the result recovered an instructive boundary. Taking
A=1/(2b), B=-1/(2b) with theta<pi/2 removes two atoms and returns exactly the
earlier two-point minimum, including its theta^-2 risk. Those labels grow
without bound, so they do not contradict the bounded-label limit. Crossing
the sign boundary gives a forbidden coefficient sign and a strict gap above
the displayed dual value. Neither the exact formula nor the bounded-label
conclusion was extrapolated beyond its hypotheses.

What failed: the first prior-recheck run used an arbitrary excess-cost
threshold of 8 for a new feasible competitor. Its actual bounded excess cost
is about 16.47. Correcting that audit threshold made the check pass; no earlier
theorem or new optimizer formula changed. The sandbox denied nice's attempted
priority adjustment, but every run checked compliant inherited nice 20 before
computation. No extension mathematical check failed.

The literature check ended within five minutes. No later resolution was found;
the opened primary sources and their distinct settings are recorded in LOG.md.
No SOLVED_ELSEWHERE.md was warranted. The result is new relative to the
predecessor reports; no broader novelty claim is made.

What remains uncertain: whether this cancellation survives fixed perturbations
away from antipodality, the leading optimal cost and risk for generic extras
in opposite separation hemispheres, random-design typical risk, expected risk
in d>=4, biases, and GD. A finite collision-limit risk for this four-point
family is not a tempered-overfitting theorem as n tends to infinity.

Next worker: perturb the fourth location away from -e2, first within the sample
plane, while keeping its separation coordinate negative and labels bounded.
Determine the leading atomic cost and scaled function for each fixed
perturbation, and whether bounded unscaled risk holds on an open set or only
at exact antipodality. The present dual's four isolated equality atoms give
an exact base case; their kink equalities do not justify assuming stability.

Task: T264, "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 11:34 +04.
