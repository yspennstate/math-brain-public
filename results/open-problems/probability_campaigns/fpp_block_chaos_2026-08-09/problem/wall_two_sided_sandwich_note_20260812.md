# [2026-08-12 SELF-REFEREE, RETRACTION] The Addendum's "THE ESCAPE" claim below - that tracking
# the window ratio R(j) BREAKS the circularity - is RETRACTED. The upper leg's contraction rate
# rho_U is not R-independent: its premise beta = U(j+1)/L(j) = O(1) is itself a tight-window
# (R = O(1)) condition that fails at the loose-window start (beta >~ n^{2chi}/log n >> 1 with the
# only unconditional lower bound L >= c log n), so the two-sided carry RELOCATES the circularity
# into rho_U rather than removing it. What survives: the sandwich framing and the Thread-B
# identification. See wall_two_sided_sandwich_SELF_REFEREE_20260812.md for the full argument.
# chi = 1/3 unmoved. Read the note below with this retraction in force.
#
# Structural note: the wall is TWO-SIDED, and 3b's missing lower bound is the D-attempt
# note's restricted-min anticoncentration. 2026-08-12.
# STATUS: structural OBSERVATION connecting two existing campaign threads, honestly
# labelled. NOT a proof, NOT a claim of progress on chi. It reframes where the difficulty
# sits; it does not remove it. Referee before any use.

## The two threads it connects

THREAD A (upper side, section 3b + 9.8, refereed). (L1') is the variance ratio: the engine
needs the per-block second moment E[Delta_L^2 | U_L] <= beta Var(X_n), and 3b pins the
matching envelope exponent to alpha = chi (rho = Q^2/Var = O(1) at the scales iterated).
This CAPS the block-increment fluctuation from ABOVE relative to the global variance.

[REF-CORE item 3, 2026-08-12, (independent referee of the surviving
core): "section 3b + 9.8, refereed" overstates 3b. The REF-W1/W2 tags all sit in the 9.x
wall-reduction sections; 3b carries none, and 3b's own header says its C1 dependency's
referee is PENDING (the iter-68 resolution of the iter-66 challenge is internal, not an
external referee). Read Thread A as: 9.8's (L1')-identity REFEREED; 3b FLAGGED-STANDING and
conditional (per its iter-68 scope correction: admissible set (0, chi], equality only within
the hypothesis set, disjointness conditional on chi <= 0.4142). The framing's substance is
unaffected — it nowhere uses more of 3b than the corrected conditional statement.]

THREAD B (lower side, problem/D_lowerbound_blocktime_attempt_20260812.md). Any improvement
of the variance LOWER bound D through an environment-revelation channel reduces, across
three faces, to ANTICONCENTRATION OF RESTRICTED MINIMA at fluctuation scale: the
competitive block/corridor passage time must not CONCENTRATE too fast. This bounds the same
block-increment fluctuation from BELOW.

## The connection (the note's actual content)

LOG iter (line 409) already isolated the gap from the upper side, verbatim: "rho has Var in
the DENOMINATOR, so rho = O(1) requires a LOWER bound on the variance, and an induction that
carries an UPPER bound forward cannot supply a lower bound about itself. What is
unconditionally known is only Var >= c log n." That missing lower bound is not a side
condition - it is Thread B. The D-attempt note is a map of EXACTLY what rho = O(1)'s
denominator needs and why every naive route to it fails (self-similar restricted-min
anticoncentration; anchored methods e.g. Elboim penetrate one layer only).

So the wall is a SANDWICH on one object - the block-increment fluctuation scale s_block:
  - Thread A (upper): s_block^2 <= beta * Var  (don't be too big vs the global variance)
  - Thread B (lower): s_block does not concentrate below ~Var^{1/2} at block scale
                      (don't be too small; the restricted min doesn't collapse)
Both pin s_block to the SAME scale as the global standard deviation. That is why alpha = chi
(3b) and "restricted-min dispersion >= diameter-scale" (Thread B) are the SAME requirement
seen from opposite inequality directions.

## Why this is a fixed point, and why neither side closes it alone

Write the self-consistency the sandwich expresses: at the iterated scale, the block
fluctuation must equal the fraction of the global std dev the geometry assigns it. This is a
FIXED-POINT equation for the exponent; chi is its solution (chi = 1/3 under KPZ). The
campaign's own obstruction (LOG 409) is precisely that a one-directional induction cannot
reach a fixed point: an upper-bound induction supplies only the upper leg and "cannot supply
a lower bound about itself." Thread B supplies the lower leg but, per the D-attempt note,
only conditionally (needs a restricted-min anticoncentration input nobody has). So:

  THE UNIFIED STATEMENT. chi is pinned iff BOTH legs of the sandwich are proved at the same
  scale simultaneously; each leg alone is a one-sided inequality that the other's absence
  lets drift. The campaign has the upper leg conditionally (3b, refereed) and now a map of
  the lower leg (Thread B). The problem is not two separate walls; it is one fixed-point that
  needs a two-sided argument - which is exactly the structure a one-directional variance
  induction cannot have.

## Honest limits (strongest case against)

- HEURISTIC at the sandwich framing: "s_block pinned to the std-dev scale" is dimensional /
  self-consistency reasoning, not a theorem; the constants and the exact power in Thread B's
  lower leg are unproved (the D-attempt note closes NO route, it only maps them).
- The equivalence "alpha = chi (3b) == restricted-min dispersion (Thread B)" is stated at
  the level of what each requires of s_block, not proved as a formal iff; a referee should
  check whether 3b's rho = O(1) is genuinely the SAME lower bound Thread B produces or only
  a weaker consequence.
- Nothing here is unconditional; chi = 1/3 is exactly where it was. This note REORGANISES
  the difficulty (one fixed point, two legs) - it does not shrink it. Its only claim to
  usefulness: it says a future attempt should stop trying to prove either leg in isolation
  and instead look for a two-sided / self-consistent argument, and it names the lower leg's
  content precisely (restricted-min anticoncentration) so the search is concrete.

Related: problem/D_lowerbound_blocktime_attempt_20260812.md (Thread B, full),
CRUX_iteration_arithmetic.md section 3b + 9.8 (Thread A), LOG lines 408-409 (the missing-
lower-bound isolation this note attaches Thread B to).

## Addendum (same day): why a TWO-SIDED bootstrap escapes "the induction does not start",
## and the exact condition it then needs.

The campaign's own finding (memory fpp_wall_is_the_variance_ratio_three_routes; CRUX 9.8):
the natural move is induction on the variance ratio, and IT DOES NOT START - using (L1')
needs beta = O(Var(X_Mn)/Var(X_n)) = O(1), but bounding that ratio is what the halving
CONCLUDES (circular), and the only unconditional lower bound on the denominator is
Var >= c log n (LOG 409). This addendum isolates why the circularity is an artifact of
carrying ONE bound, and what a two-sided carry needs instead.

SETUP. Iterate over scales n_0 < n_1 < ... with n_{j+1}/n_j bounded (say = 2). Carry a
WINDOW at each scale: L(j) <= Var(X_{n_j}) <= U(j). Two engines act on the window:
  - UPPER leg (the refereed halving): given a lower bound L(j) at the small scale, the
    halving contracts the upper bound at the next scale - U(j+1) <= (1 - c) * (ratio) *
    U(j)-type step, valid because (L1')'s beta = U(j+1)/L(j) is what it consumes.
  - LOWER leg (Thread B, restricted-min anticoncentration, UNPROVEN): given an upper bound
    U(j), anticoncentration forbids the variance from collapsing - L(j+1) >= (1 + c') *
    (ratio) * L(j)-type step.

THE ESCAPE. A one-directional induction assumes the ratio U/L = O(1) (circular). A
two-sided carry does NOT assume it - it TRACKS the window ratio R(j) := U(j)/L(j) and asks
only that R stay bounded under the joint step. The upper leg divides R (contracts U toward
L); the lower leg divides R again (lifts L toward U). So R(j+1) <= R(j) / (contraction of
BOTH legs). R is now a CONTRACTED quantity, not an assumed one - the circularity is broken
because neither bound is proved "about itself"; each is proved from the OTHER at the
previous scale. This is exactly the two-legged structure a fixed-point needs and a
one-directional induction cannot have.

THE CONDITION IT REDUCES TO (the sharpening - more concrete than "does not start"). Let
rho_U be the upper leg's per-step contraction factor on R and rho_L the lower leg's. The
scale step inflates the raw variance by the growth factor g per step. The bootstrap
CONTRACTS the exponent window iff
    rho_U * rho_L  <  1   AFTER accounting for g,
i.e. the PRODUCT of the two legs' contraction rates must beat the per-scale variance
growth. [CORRECTION 2026-08-12, my own strongest-case-wrong check: an earlier draft here
claimed the huge base window R(0) ~ n/log^2 n is "killed in O(log log n) steps" and is a
red herring. THAT IS WRONG. The scales double, so reaching scale n from O(1) allows only
~log_2 n steps, not more; a per-step contraction factor q gives R(log n) ~ R(0) *
q^{log_2 n} = R(0) * n^{log_2 q}, which is O(1) only if |log_2 q| >= 1 given R(0) ~ n -
i.e. q <~ 1/2 per step. So the base window is NOT a red herring: its polynomial size sets
a HARD FLOOR on how strong the per-step contraction must be (q bounded well below 1),
because only logarithmically many steps are available to erase a polynomially large ratio.
The honest reduction is therefore: rho_U * rho_L must contract R by a factor <~ 1/2 EVERY
step, sustained over all ~log n scales - a quantitatively stronger demand than "product <
1". The upper leg (refereed halving) delivers a constant-factor contraction; whether its
constant is small enough, and whether Thread B's rho_L even exists let alone reaches that
strength, are both open.]

WHAT THIS DOES AND DOES NOT DELIVER.
  - Delivers: the obstruction "the induction does not start" is RECLASSIFIED as "one
    contraction rate is missing" - the upper leg's rho_U is the refereed halving
    (conditional, exists); the lower leg's rho_L is Thread B, UNPROVEN. A future attempt
    needs ONLY the lower leg AS A CONTRACTION RATE (not the full variance lower bound) -
    a strictly weaker-looking target: "restricted minima do not concentrate faster than
    the current upper bound permits, per scale."
  - Does NOT deliver: rho_L itself. Thread B closes no route to it. And the product
    condition rho_U * rho_L < 1 after growth g is unverified - it may fail even if both
    legs exist (the legs could be too weak jointly). Both are honest gaps.
  - chi = 1/3 UNMOVED. This is a structural reclassification of the difficulty into a
    single missing ingredient (rho_L as a per-scale contraction), with the base-case
    red herring (huge R(0)) explicitly cleared. Referee owed on the two leg-step
    inequalities and the product bookkeeping.
