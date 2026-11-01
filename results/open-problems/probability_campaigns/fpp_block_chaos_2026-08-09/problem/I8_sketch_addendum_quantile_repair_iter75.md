# Addendum to the diving-chain sketch: the quantile repair, written before the referee returns
# (iter 75, author's hand. SEPARATE FILE because the sketch is under an active referee and
# edits under an active reader race the review. To be merged after the verdict. The slip this
# repairs was self-caught at iter 74 and recorded in LOG.md ahead of the verdict; the sketch
# referee's attack front D prices the same point independently.)

## The slip, restated exactly

Sketch display (2.1) prices each bulk segment's touching event as
    b (b/a) (l/K + 2d) P(deviation >= d)
and then takes d AT the wandering quantile. At the median quantile P(deviation >= d) is a constant
of order one, the term is Theta(l/K) per segment, Theta(l) in total, and the bound dies. The phrase
"the second term is o(1)" in (2.1) is false as written.

## The repair

Choose the dive depth at a POLYNOMIALLY SMALL quantile rather than the median:
    d := the level-(l^{-1}) quantile of the wall-ward deviation of the free geodesic
         between depth-d endpoints at horizontal... vertical separation l/K.
Under the sketch's conditional input (ii) - wandering at scale W(r) = r^xi with a stretched-
exponential tail of exponent theta > 0, uniformly over the arc and the class - that quantile is
    d <= c_theta W(l/K) (log l)^{1/theta}.                                          (A.1)
Then, summed over the K-2 bulk segments,
    total touching cost <= (K-2) b (b/a) (l/K + 2d) l^{-1} = O(1) = o(sqrt(l)).      (A.2)

## What the repair costs downstream, checked term by term

GEOM: d enters squared, so GEOM <= 2C d^2 K / l picks up (log l)^{2/theta}:
    GEOM <= C' (l/K)^{2 xi - 1} K (log l)^{2/theta} <= C'' sqrt(l) (log l)^{2/theta}   (xi <= 3/4).
Still square-root scale up to polylog. The master recursion's forcing becomes
    C sqrt(l) (log l)^{max(1, 2/theta)},
and the unroll is unchanged (geometric in 2/sqrt(K)), so
    f(l) = O( sqrt(l) (log l)^{max(1, 2/theta)} ).                                   (A.3)
The salvaged note's I8 needs only l^{1/2 + o(1)}; any fixed power of log is absorbed. No exponent
moves.

EARLY STOPPING (sketch 6.1): unaffected - the stopped term's arithmetic contains no d.

TILT COMPOUNDING (sketch 6.2): increments gain the same (log l)^{1/theta} factor; the total was
killed by l^{-c(1-xi)}, and polylog times a negative fixed power still vanishes. Unaffected in
substance.

BASE BOUND f(r0) <= C r0: contains no d. Unaffected.

## What this addendum does NOT do

It does not touch attack front B (first-order tilt term in GEOM for tilted parents), which remains
the most likely fatal point and is the referee's to decide. It does not claim the sketch is sound.
If the referee's verdict kills the sketch on another front, this file records only that THIS
particular defect had a standard repair, priced at a polylog.

--------------------------------------------------------------------------------------------------
# PART 2 (iter 77): the one-step class stability of G1, ATTEMPTED and NOT CLOSED. DERIVED,
# unrefereed. [Header corrected same fire: an earlier version of this line said "the step closes" -
# it was written before the derivation below fought back, and the body's ending is the truth:
# G1 is NOT mere bookkeeping, the depth budget cannot both admit the parent's endpoints and shrink
# with scale, and the construction needs a genuine new stage (the CLIMB, repair R1 below) that is
# not written. My iter-73 "bookkeeping with no new idea" is WITHDRAWN in the body.]
# [SUPERSEDED BY PART 3 (iter 78), IN PLACE: the climb R1 turned out to be unnecessary. The correct
# fix is architectural - only the wall-hugging child recurses (branching factor ONE), deep-far-end
# segments are priced full-plane, and the budget fight below dissolves. Part 2 stands as the
# demonstration of WHY the tree architecture cannot work; do not quote its conclusion ("G1 open,
# needs a climb") without Part 3, where G1 closes at sketch level.]

## Why "anchored" fails as a class

Run the chain on an anchored parent p = (0,0), q = (D_q, s) with D_q > 0 (which the recursion
produces immediately: the top level's children have far-depth d(l/K) > 0). The chain's LAST segment
runs from (d', (K-1)s/K) to (D_q, s): BOTH endpoints off the wall. It is neither anchored nor an
equal-depth bulk pair. The class as first stated is not stable under one step. This is exactly the
kind of defect G1 predicted; here is the repair.

## The repaired class

    C(rho) := pairs (u, v) with depths D_u, D_v <= DEPTH(rho), vertical separation in [rho/2, rho],
              chord tilt <= t(rho),
    DEPTH(rho) := d(K rho)   (the dive depth of the PARENT scale - one scale up),
    d(m) := level-(m^{-1}) quantile dive depth from Part 1, d(m) = c_theta m^xi (log m)^{1/theta}.

Wall-anchored pairs are the D = 0 members; the top-level target (0,0) -> (0,l) is in C(l) trivially
(depths 0 <= DEPTH(l)).

## One step, checked member by member

Parent (u, v) in C(rho), WLOG u = (D_u, 0), v = (D_v, s), s in [rho/2, rho]. Chain: dive to
d' := d(rho/K); w_j = (d', j s/K) for j = 1..K-1; w_0 = u, w_K = v.

(i) First and last segments: (u, w_1) has depths D_u <= DEPTH(rho) = d(K rho) and d' = d(rho/K);
    both <= DEPTH(rho/K) = d(rho)? CHECK: d' = d(rho/K) <= d(rho) yes; D_u <= d(K rho) - NOT
    obviously <= d(rho). THE RESOLUTION: the parent's OWN depth budget enters the chain at its
    endpoints only, and the correct reading is that the first segment inherits the PARENT's depth
    at u. So the child class must be entered at the NEXT scale with DEPTH(rho/K) = d(rho), and the
    first segment's u-depth D_u <= d(K rho) exceeds it in general. Repair inside the step: prepend
    a CLIMB segment from u = (D_u, 0) to u' = (min(D_u, d(rho)), ~0)... unnecessary - simpler:
    note the recursion only ever produces parents whose OWN depths came from THEIR parent's dive,
    i.e. D_u, D_v <= d(rho) for the pairs the recursion actually generates from the second level
    on (the top level has depth 0). Formally: tighten DEPTH(rho) := d(rho) and check the step
    produces children with depths <= max(d', parent depths) <= max(d(rho/K), d(rho))... the child
    at scale rho/K needs depths <= DEPTH(rho/K) = d(rho/K), but it carries one endpoint at depth
    up to d(rho) > d(rho/K). SO THE BUDGET MUST LAG ONE SCALE: DEPTH(rho) = d(K rho) as first
    stated, AND the step must be checked to produce children with depths <= max(d(rho/K), DEPTH(rho))
    = max(d(rho/K), d(K rho)) = d(K rho)... child budget DEPTH(rho/K) = d(rho) >= d(rho/K) yes but
    is d(K rho) <= d(rho)? NO - d is increasing. THE ARITHMETIC FORCES THE LAG THE OTHER WAY.
    Honest resolution, third try, and this one is right: the chain should dive from the parent's
    endpoints INWARD, so the deep segments sit at depth d' >= parent depths. Set the dive depth of
    the step at scale rho to
        d* := max( d(rho/K), DEPTH(rho) ) = max( d(rho/K), d(K rho) ) = d(K rho)   (d increasing),
    i.e. THE STEP DIVES TO THE PARENT'S OWN BUDGET DEPTH (or deeper), not to the child scale's.
    Then: first/last segments have depths <= d* = d(K rho) and the CHILD pairs (u, w_1), (w_{K-1}, v)
    at scale rho/K have depths <= d(K rho) = DEPTH(K rho/K * K)... child budget is DEPTH(rho/K)
    = d(rho). Need d(K rho) <= d(rho): STILL FALSE.

## Stop. The clean fix, and what it costs

The tangle above is real and instructive: a depth budget that both (a) admits the parent's
endpoints and (b) shrinks with scale cannot exist, because the recursion hands depths DOWNWARD
unchanged. The clean fix decouples the two roles:

    C(rho) := pairs with depths <= d(rho) * (log l)^{q}  AND  vertical separation in [rho/2, rho],
    with ONE GLOBAL l (the top scale) fixed throughout the recursion,
and the chain at scale rho dives to d* = d(rho) (its own scale's quantile depth, per Part 1).
Children of a C(rho) parent: first/last segments have depths <= max(parent depths, d*)
<= max(d(rho) polylog, d(rho)) = d(rho) polylog. The child scale is rho/K and the child budget is
d(rho/K) polylog. The ratio d(rho)/d(rho/K) = K^xi is a CONSTANT (in K only). So children exceed
their own scale's budget by at most a FIXED K-power per level... which compounds over levels. Over
the J <= log_K(l) levels the compounding is K^{xi J} = l^{xi} - fatal if uncontrolled. BUT the
early stopping of the sketch's section 6 caps J at levels down to r0 = l^c, i.e. J <= (1 - c)
log_K l, and the compounding K^{xi J} multiplies the DEPTH, whose square-over-length enters GEOM:
depth at level j is at most d(rho_j) K^{xi j}?? - no. Enough: I am not able to close this cleanly
tonight, and the honest statement is:

    G1 IS NOT MERE BOOKKEEPING. The depth-budget bookkeeping fights back: the recursion hands the
    parent's dive depth to the child, whose own scale is smaller, so depths relative to scale GROW
    down the recursion unless the chain re-anchors toward the wall between levels - a step the
    current construction does not have. Candidate repairs, for the referee or a later fire:
    (R1) a CLIMB stage inside each step returning the far endpoint to depth d(rho/K) before
    recursing, priced like GEOM (the climb chord's g-difference under arc-curvature) - plausibly
    another d^2 K / rho term, same scale, and it would restore a genuinely shrinking budget;
    (R2) Alexander's own two-parameter mesh, which handles exactly this by approximating over a
    lattice of (position, scale) pairs rather than a single recursion tree.

My iter-73 claim that what remains of G1 is "bookkeeping with no new idea" is WITHDRAWN - it was
optimistic. The gap is a genuine construction step (the climb), with a plausible same-scale price,
but it is NOT written and the sketch's status line should read: G1 open, with R1 the named repair
path. Recorded here before any referee says it for me.
[SUPERSEDED IN PLACE, iter 78: neither R1 nor R2 was needed. Part 3 below closes G1 by changing
the ARCHITECTURE - only the wall-hugging child recurses; the deep-far-end child is full-plane
priced because its shallow endpoint clears its own scale's wandering by the factor K^xi. The
withdrawal of the "bookkeeping" claim stands; the OPEN status does not. Read Part 3.]

--------------------------------------------------------------------------------------------------
# PART 3 (iter 78): G1 CLOSED BY A CHANGE OF ARCHITECTURE - no climb needed, the recursion is a
# PATH. DERIVED, unrefereed; supersedes Part 2's pessimism the honest way: by construction, not by
# optimism. Part 2's failure analysis stands as the reason THIS architecture is the right one.

## The realization

Part 2's budget fight assumed every non-bulk child must recurse. False. A pair whose SHALLOW
endpoint sits at depth >= K^xi times its own scale's wandering does not feel the wall at all - it
is priced FULL-PLANE like the bulk segments, no recursion. Checking the chain's children against
that criterion: only the child that hugs the wall recurses. The recursion has BRANCHING FACTOR ONE.

## The stable class, exactly

    P(s) := anchored pairs (0,0) -> (D, s') with s' in [s/2, s], far-depth D = d(K s'), tilt <= t(s),
    d(m) := the level-(m^{-1}) quantile dive depth of Part 1  ( = c_theta m^xi (log l)^{1/theta} ).

STEP at scale s: chain dives to d(s); points w_0 = (0,0), w_j = (d(s), j s/K), w_K = (D, s).
  - Child 0 = (0,0) -> (d(s), s/K): anchored, far-depth d(s) = d(K x s/K) - IN CLASS P(s/K). The
    one recursing child.
  - Children 1..K-2: bulk at depth d(s); their scale is s/K and d(s)/d(s/K) = K^xi > 1, so the
    shallow depth clears their wandering by the factor K^xi (the polylogs cancel exactly - both
    carry (log l)^{1/theta} with the SAME global l). FULL-PLANE priced.
  - Child K-1 = (d(s), (K-1)s/K) -> (D, s): depths d(s) and d(K s); shallow = d(s), same K^xi
    clearance over its scale s/K. FULL-PLANE priced. Tilt of its chord: (d(Ks) - d(s)) K / s <=
    K^{1+xi} s^{xi-1} polylog = o(1) - inside the arc; full-plane Alexander is direction-uniform.
  - TOP LEVEL ONLY: (0,0) -> (0,l) has far-depth 0, not d(Kl); its chain has TWO anchored children
    (one per end, each with far-depth d(l) = d(K x l/K) - in class at scale l/K). Branching 2 at
    the root, 1 forever after. Total multiplicity 2. Harmless.

## GEOM for the class, with the deep far end

Chords: (d(s), s/K) once, (0, s/K) x (K-2), (D - d(s), s/K) once; total chord (D, s). Using the
norm's symmetry-plus-convexity (g((x,y)) nondecreasing in |x| for fixed y) and arc-curvature on
both tilted chords (both depths D, d(s) << s/K at large l):
    GEOM <= C [ d(s)^2 + D^2 ] K / s <= C K^{1+2xi} s^{2xi-1} (log l)^{2/theta},
square-root scale for xi <= 3/4, exactly as in the sketch, constants worse in K only.

## The recursion is now a sum, not a tree

    f(s) <= f(s/K) + (K-1) [full-plane Alexander at s/K] + GEOM(s) + touching(s),
    f(l) <= Sum_{j >= 0} [ C sqrt(l/K^j) log l + C (l/K^j)^{2xi-1} K' polylog ] + f(base)
         = O( sqrt(l) (log l)^{max(1, 2/theta)} ).
No 2^j factor exists anywhere - the branching-2 recursion of the original sketch (and its
early-stopping repair, and Part 2's entire budget fight) were artifacts of recursing on a child
that never needed recursing. Early stopping is retained only to bound the base and the tilt sum.
Touching costs: O(K) full-plane-priced segments per level, O(log_K l) levels, each priced
crude x l^{-1} by the quantile choice: total O(K log l / l) x linear = o(1). All terms accounted.

## Status after Part 3

G1: CLOSED AT SKETCH LEVEL by the path architecture (this part). G2: closed by early stopping
(sketch 6.2) - the arc still shrinks. G3: the quantile repair (Part 1). G4: absorbed into the
K^xi clearance check above. G5: single log, as in sketch 6.4, now with the simpler sum. STILL
OPEN AND STILL THE REFEREE'S: attack front B - whether arc-curvature really gives the quadratic
bound at TILTED chords (both GEOM terms consume it at tilt o(1), so the required form is
"quadratic transverse gain uniformly over a shrinking arc", which is exactly H2-arc); and every
line of this part, which no referee has seen. The sketch package is now: diving chain + quantile
repair + path architecture, one open attack front, conditional throughout on H2-arc + published
inputs.
