# Hostile referee review of the direct upper rate

2026-10-11. Verdict: the conventional proof in DIRECT_UPPER.md establishes
a NONOPTIMAL upper rate under the stated fixed iid (2+eps)-moment law.
It does not resolve the exact optimal dependence.

Critical failure modes examined:

1. **Entry derivative normalization.** Hermitian dilation has size 2n,
   rank-two entry perturbation, norm |u|/sqrt(n). The factor 1/(2n) in
   log absolute determinant gives derivative bound C_k/n, not C_k.
   Replacing n^2 entries therefore gives n^(1-p/2)=n^(-e/2), not a
   spurious n^(-p/2). Six trace derivative identities were checked at
   45-digit precision in direct_checks.json.
2. **Fractional moment replacement.** Cancellation is of the full real
   two-coordinate covariance, not merely E|X|^2. The Taylor remainder is
   bounded BOTH quadratically and cubically globally; their minimum
   gives the p-th power for 2<p<=3. No third moment is assumed when e<1.
3. **Gaussian real versus complex issue.** Projecting a real Gaussian
   onto a complex subspace is not a real chi-square of complex dimension
   times two. The argument explicitly uses eigenvalues of Re P in [0,1]
   and trace d, giving the safe real inverse-moment bound n/[v(d-2)].
   It requires k>=2 rows deleted. Anisotropic covariance is handled by
   conditioning the smaller independent Gaussian component; v>=1/2.
4. **Negative-second-moment identity.** It is applied to the rectangular
   row-deleted matrix, which is full row rank almost surely. The proof
   via Gram inverse and Schur complements is supplied. It is not a
   claim that the square inverse moment is finite.
5. **Moving deterministic shifts.** The Gaussian count bound is uniform
   in arbitrary shifts, by noncentral Gaussian integration. Tao–Vu's
   inverse bound is only used on a fixed compact z disk, whose shifts
   have norm O(sqrt(n)); its constants can therefore be chosen uniformly.
6. **Heavy-tailed concentration.** Entrywise Lipschitz concentration would
   require a tail condition. Instead entire independent rows are exposed,
   and singular-value rank interlacing bounds changes of the clipped
   statistics by C log n/n. This is valid even for unbounded rows.
7. **Clipping order.** The expectation comparison uses the smooth,
   UNCLIPPED regularized potential. Clipping is introduced solely for
   concentration, and its expectation error is bounded by energy/L^2.
   The chosen upper clipping threshold is polynomial and may depend on Q;
   the actual random potential in the final theorem does not depend on it.
8. **Regularization cost.** The crude error eta^2/s_min^2 would fail.
   The proof bounds log(1+x) by C log n x/(1+x), allowing the same V_eta
   count bound to control all singular values. The failure set in z is
   bounded in AREA by Fubini and Markov, never by a union over a continuum.
9. **Small-singular-value exceptional integrability.** The L2 negative
   eigenvalue logarithms have norm sqrt(pi/2) independently of energy.
   Positive logs grow as log(1+energy), whose square has finite expectation
   under a second moment. For high probability, energy <=n^(Q+2) by
   Markov gives deterministic L2 norm O_Q(log n). No fourth moment enters.
10. **Uniform rectangles.** Every smoothed rectangle is bounded by the
    SAME L1-potential event. Constants for Delta f and Lip(f) are uniform
    in both thresholds. The fixed cutoff chi_0 controls exterior mass;
    tightness is not assumed or obtained by moving to a growing disk.
11. **Gaussian comparison input.** The matching covariance may not have
    independent real/imaginary parts initially. A common phase rotation
    diagonalizes its covariance, and W_1 plus the circular target are
    invariant under that rotation. Only a fixed Gaussian law is used in
    Jalowy's expected W_1 corollary.
12. **Modes and quantifiers.** For every Q the constants may depend on Q.
    Summability with Q=2 proves almost-sure eventual rate for any coupling
    of sizes. A log factor remains; only delta<beta is asserted as a pure
    power upper bound. The optimal exponent is not identified.
13. **Local improvement.** Section G derives an area-scaled version of
    the potential bound; it is not inferred from the global L1 inequality.
    The bad-set threshold is a^2 n^-2, so Cauchy–Schwarz preserves a.
    The extra failure power absorbs a^-1<=n^rho. A deterministic family
    of O(h^-1) full-width strips suffices for every derivative transition,
    and its union bound absorbs only a prescribed polynomial probability.
    This gives beta=gamma/2, improving the earlier gamma/3 estimate. The
    strips' areas are 36h and their count is O(h^-1), including arbitrarily
    large or small rectangle thresholds (transitions outside the cutoff
    support simply have zero derivative there).

Auxiliary numerical tests cover: six rational exponent balances; 18 row
replacement cases; three translated complex-projection inverse-distance
experiments (12000 samples each, shared noise array); first-through-third
derivatives of both regularized functions; 1201 scalar log inequalities.
The largest sample array is 12000x16 and stays far below 1 GB.
The localized improvement additionally passed 3671 exact rational strip-
covering checks and six exact bad-area/union probability exponent checks
in local_checks.json. These checks were run after introducing Section G.

These tests are independent sanity checks of formulas, not proofs of an
asymptotic stochastic theorem. The theorem's proof is the full written
argument with the two external inputs identified by number and page.
The Lean certificate, if completed, checks only elementary inequalities.

Open gap: replace this weak-moment lower/upper interval by matching
sharp bounds. The direct upper exponent is deliberately conservative:
gamma from replacement/regularization, and beta=gamma/2 from rectangle
smoothing. Neither loss is proved necessary.
