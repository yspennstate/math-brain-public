# !! SUPERSEDED — THE LAW IS FALSE (verifier, session 19). The derivation evaluated the
# AMBIENT gradient at the subset-aligned point, where the pole-sum is purely RADIAL and
# the TANGENTIAL gradient (= what Lip_S measures) VANISHES: balanced-frame test shows
# ambient 108 Lambda vs tangential 0.46 Lambda (232x gap). Consequences #1-#4 all
# withdrawn: no m' <= O(d/log) law; the disjoint lower bound IS net-legal (Lip_S ~ 4
# Lambda, flat in d and m'); Phi_disj and c* = 1/32 stand; the S2 data-point pile-up
# stands (data-point-sharing poles genuinely SPREAD, so tangential ~ sqrt(J) bites
# there — the m'-independent throttle). Forced-depth confirmed vacuous at the anchor;
# shallow co-depth multiplicity genuinely unbounded — harmlessly. The residual reverts
# to (S1): general -> aimed carrying Lip_S <= L* (threshold concentration), or
# equivalently the shallow chaining bound. Kept for the record of the failure mode:
# on the sphere, subset-aligned points are tangential CRITICAL points — the single
# worst witness for Lipschitz violations.
# The subset-aligned Lipschitz constraint: a possible m' <= O(d/log) law
# Status: MY DERIVATION (session 18), UNVERIFIED â€” the next agent's task. If right,
# it re-geometrizes the whole (R') layer and re-audits the disjoint lower bound.

## The observation
For J' pairwise nu-incoherent poles with a COMMON rising window (all profiles have
slope ~ Lambda at depths [sigma, 2 sigma]), the subset-aligned sphere point
x_A = normalized sum of the J' poles sits at depth ~ 1/sqrt(J') in every cap. If
1/sqrt(J') lands in the common window (J' ~ 1/sigma^2), ALL J' caps are rising at x_A
and the aggregate gradient is ~ Lambda sqrt(J') = Lambda/sigma. The net constraint
Lip_S(f) <= L* forces Lambda/sigma <= 2L*, i.e. NO 1/sigma^2-sized incoherent co-rising
family may exist at scale sigma < C_L/2 â€” equivalently:
   #caps rising at scale sigma  <  1/(4 sigma^2)   for every sigma in [tau_0, t*].
Summing dyadically: m'_incoherent <= sum_j 1/(4 sigma_j^2) ~ 1/(3 tau_0^2) = d/(6 log(m'n)).

## Consequences IF VERIFIED
1. Any legal band net's mesoscopic structure, after merging at coherence scale nu, has
   at most O(d/log) incoherent super-clusters: the effective m' is DIMENSION-limited.
   For d << n log/T the raw m' = n/T exceeds it => coherent clustering is GENERIC, and
   the merged machinery is the main case, not the edge case.
2. THE DISJOINT LOWER BOUND (RPRIME_CORRECTED "rigorous") is class-legal but likely
   NET-illegal above the slice: its m' = n/T ramps share the window [tau_0, tau_0+delta*],
   and subsets of size 1/tau_0^2 <= m' give gradient Lambda/tau_0 >> L*. (M)'s truth
   only needs net-realizable attacks â€” so (M) may hold with MORE room than Phi_disj
   suggested, and the achievable-capture landscape must be recomputed under the
   staggering constraint.
3. The ledger must be redone with the per-scale budget K_sigma < 1/(4 sigma^2):
   capture = sum over scales of K_sigma k_sigma v-optimized â€” a new optimization.
4. Possible resolution shape: effective m' ~ d/log with per-cluster capture ~
   Lambda/(4 tau_0) rebuilds Phi_det ~ (d/log) Lambda/tau_0Â·... vs the old m'-based
   Phi_det â€” recompute everything.

## Cautions / possible flaws in my derivation (for the verifier)
- The subset point x_A needs the J' caps SIMULTANEOUSLY rising AT x_A: staggered
  windows or plateau-below-the-scale evade it; my dyadic count tried to handle this â€”
  check the bookkeeping.
- x_A must be a valid sphere point with the claimed depths: <u_g, x_A> =
  (1 + cross)/sqrt(J'(1 + (J'-1)nu)): corrections O(J' nu) â€” at J' = 1/sigma^2 and
  nu ~ tau_0/(2t*): J' nu ~ nu/sigma^2 â€” for sigma ~ tau_0: nu/tau_0^2 = 1/(2 t* tau_0)
  >> 1?!?! â€” THE CORRECTION EXPLODES at sigma ~ tau_0: ||sum u_g||^2 = J'(1 + (J'-1)nu)
  with (J'-1)nu >> 1 => depth = 1/sqrt(J'(1+J'nu)) ~ 1/(J' sqrt(nu)) << 1/sqrt(J') â€”
  the aligned point is SHALLOWER than 1/sqrt(J') when J' nu >> 1 â€” MY DERIVATION MAY
  FAIL exactly at the relevant scales (the pairwise coherences, though individually
  <= nu, ACCUMULATE in the norm!). Worst-case coherences ~ +nu everywhere:
  depth ~ 1/(J' sqrt(nu)); but TYPICAL incoherent poles have signed coherences
  ~ N(0,1/d): sum ~ J' sqrt(nu-fluct)Â·... E||sum||^2 = J' + J'(J'-1) E<u,u'> = J'
  for CENTERED coherences: depth ~ 1/sqrt(J') restored for typical/generic pole sets
  (coherences average ZERO). So the constraint bites for GENERIC pole families but can
  be evaded by NEGATIVELY-correlated pole designs (sum-norm suppressed)? Frames/
  equiangular-negative constructions: ||sum||^2 = J'(1 - J'nu...) -> the aligned point
  gets DEEPER â€” worse for legality. The verifier must sort out: for which pole
  configurations does the subset-Lipschitz argument bind, and is the m' <= O(d/log)
  law true for ALL nets or only generic-pole ones (an adversary CHOOSES poles!).

