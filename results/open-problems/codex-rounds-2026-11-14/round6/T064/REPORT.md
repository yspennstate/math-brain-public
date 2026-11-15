VERDICT: PROVED quantitative annular arm stability at the height of a determinant-weighted saddle

Round 5's saddle law and exact residual-field comparison hold. Its
script passed again, and the determinant tilt and total variation
formula were independently re-derived. No solution of the Cardy/SLE(6)
conjecture was found in the five-minute literature check.

New beyond round 5: the remaining radial threshold is controlled at
finite scale. If p_*(t;R,S) is the probability of four alternating
strict-sign arms across the annulus R<=|x|<=S under the saddle Palm
field F_t, measured at its own height t, then for each fixed lambda>1,
S=lambda R, sufficiently large R, and |t|<=1,

    |p_*(t;R,lambda R)-p_*(0;R,lambda R)|
      <= delta(t^2)
         + pi(lambda^2-1) R^2 integral_0^|t| alpha(v) dv
         + 2 pi(lambda+1) R integral_0^|t| beta(v) dv
         + C_lambda |t| R,

where delta(a)<=(a/e) is the preceding report's exact residual TV,

    alpha(v) = phi(v)(v^2-1+2 exp(-v^2))/(4 pi),
    beta(v)  = phi(v)exp(-v^2)/(2 pi)
                + v phi(v)erf(v)/(2 sqrt(pi)),

and phi is the standard normal density. This implies own-height arm
stability for t=o(R^(-2)). It supplies no decay of the zero-height arm
probability and does not enlarge that sufficient level window.

PROOF.md gives the stronger exact bound with computable nonstationary
interior and circular-boundary densities k2,k1. The construction is
Y=h/(1-J0), where h is the Gaussian field conditioned on its zero
first jet. Its saddle law has Radon–Nikodym weight U=(a2^2+b2^2)/2.
A weighted stratified critical-value count controls the change of the
arm event. Both circles, including their curvature terms, are counted.
The event need not be monotone in the level.

The sharper local expansions are

    k2(r,v) = alpha(v)+(v^2-1)alpha(v)J0(r)+O(1/r),
    k1(r,v) = beta(v)-[beta(v)+v beta'(v)]J0(r)+O(1/r),

uniformly |v|<=1. The identity (r J1)'=r J0 makes the leading interior
error an endpoint term. This improves the crude O(|t| R^(3/2)) error
to O(|t| R) on fixed-aspect annuli. The constants and sufficiently
large starting radius are proved to exist; their numerical values
are not certified. No literature priority is claimed.

Commands:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r5/briefs/T064/check_saddle_palm.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_annular_stability.py
```

Both passed. The new audit took 0.273 s and 13.94 MiB peak RSS, with
actual niceness 20. Independent covariance constructions agreed to
3.463e-16; Gaussian fourth moments to 1.110e-16; folded-normal moments
to 5.528e-12. It also checked 32 signed-level quadratures, the exact
trace cancellation, circular Fourier derivatives and oscillatory
area integrals. LOG.md records the command and output. Numerical
quadrature audits the formulas; the proof does not depend on it.

What failed or remains uncertain: the first audit run stopped on a
Python import-scoping error, then passed after correction. There were
no failed mathematical checks. Full uncentered Palm laws remain
singular across heights. The theorem concerns annuli away from the
distinguished saddle; no bound uniform down to radius zero is proved.
No macroscopic arm bound, RSW, Cardy formula or SLE limit follows.
The bounded literature search cannot certify exhaustive novelty or
absence of a later solution.

Sources opened: Dmitry Beliaev, *Gaussian fields and percolation*,
[arXiv:2207.13448](https://arxiv.org/abs/2207.13448); Stephen Muirhead,
Alejandro Rivera and Hugo Vanneuville, with an appendix by Laurin
Köhler-Schindler, *The phase transition for planar Gaussian percolation
models without FKG*, [arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3);
and DLMF Sections [10.6](https://dlmf.nist.gov/10.6) and
[10.17](https://dlmf.nist.gov/10.17). Their roles are stated in PROOF.md.

Next worker: obtain a quantitative four-arm bound under the zero-height
determinant-weighted law. Formula (2) of PROOF.md transfers such an
estimate to own-height arms with an explicit finite-scale cost.
To enlarge the level window, the critical-value count itself must
retain global pivotality; the present count still includes all
critical points. Boundary pivotal estimates remain separate.

Only this folder was written. No git, subagents, shared-store writes,
or external mutations were used.

Task: “take the NEXT checkable step on this problem, building on that
work” — 15 November 2026, 10:20:02 Asia/Tbilisi (session launch; the
message-receipt time was not separately recorded).
