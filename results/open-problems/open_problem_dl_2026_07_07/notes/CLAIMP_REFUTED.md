# Claim P refuted; the projection width characterized; the constraint triangle complete
# Status: agent-derived with a complete proof of the refutation; numerics decisive.

## The refutation theorem (complete proof in the session record)
For d >= log^2 n, any 2 <= k <= sqrt(d/(C log n))/2, whp over x, SIMULTANEOUSLY for
every y and every m <= n/(2k):
   sup_R ||P_R y|| >= c sqrt(m k),     c = 0.35.
Construction: disjoint k-blocks of majority-sign points; aimed poles u_j = normalized
block sums; thresholds t_j = 1/(4 sqrt k). On the pairwise-incoherence event the caps
are CLEAN (support exactly the block => r_j mutually orthogonal) and each normalized
ramp captures 0.35 sqrt(k) of y. Consequences:
 - E_y sup_R ||P_R y|| >= c' sqrt(m) (d/log n)^{1/4} for m <= n sqrt(C log n/d):
   CLAIM P IS FALSE for every d >> log n (multiplicative excess — not the affordable
   additive kind).
 - Band saturation: m = n/T, d >= C T^2 log n: capture >= c sqrt(n/2) — the FULL
   majority-sign subspace. Numerics: 0.705 sqrt n, dead flat across T and d.
 - Matched upper bound via the Gram-Schmidt/residual-dictionary route: capture <=
   sqrt(m) W_m with W_m <= C (d/log n)^{1/4}: THE PROJECTION WIDTH IS
   Theta( sqrt(m) (d/log n)^{1/4} ) — a complete standalone characterization of the
   rank-m ReLU-span capture of a Rademacher vector. (Publishable by-product.)
 - Claim P IS true iff d <~ log n (below the program's regime).
 - The prior "flat 2 sqrt m" numerics were a matching-pursuit artifact (random inits
   never find aimed deep caps; explicit caps give 4.6 sqrt m on the same instance).

## Why (M) survives and the route dies
The attack's coefficients alpha_j ~ sqrt k violate rigidity by ~59x (numerics: median
|alpha| 5.86 vs budget ~0.1); normalization erases them, so ||P_R y|| cannot see the
violation. Lemma R's Cauchy-Schwarz is too lossy by exactly 1/(c_0 eps). The RIGID
version of the same attack captures ~ c_0 eps n/sqrt2 << eps n/4 — consistent with
BAND_CLAIMS (attacks sqrt T below threshold). Nothing refutes (M).

## THE CONSTRAINT TRIANGLE (the night's negative trilogy, all rigorous)
Any proof of (M) must use ALL THREE simultaneously:
 1. Drop the clip (quadratic-form/HW route): FATAL — op-norm of projected Gram ~ n dimV
    (visible-sector Theorem 3 refutation).
 2. Drop rigidity (projection route, Lemma R + Claim P): FATAL — aimed deep caps
    capture sqrt(n/2) (this file).
 3. Drop label-randomness (deterministic l1/serving counts): vacuous at n-scale
    (F14/BAND_CLAIMS arithmetic).
Also mapped: variance is the wrong invariant (VBL vacuous at d >= n — the energy is in
cross-covariances); per-cluster TV rigidity is false (G1 counterexample) but merged-TV
holds; the sqrt-m gain cannot come from linear-algebraic orthogonality.
WHAT REMAINS: the clip-aware joint chaining of RIGID bounded-TV merged ridges — with
per-point value budget + sign-correct counting + the profile anchoring (bulk values
<= C L* |s| — anchored slope-bounded profiles are TINY on the bulk, ~L*/sqrt d) as the
non-discardable structure. The serving/incidence arithmetic (my session-15 attempt)
closes the deep sector (too few deep points to serve eps n/2 for d <= eps n log/Op)
and stalls exactly at the per-ridge direction-dictionary cost m L* sqrt n — the clip
must make the m direction-sups non-additive. This is THE precise residual question.
