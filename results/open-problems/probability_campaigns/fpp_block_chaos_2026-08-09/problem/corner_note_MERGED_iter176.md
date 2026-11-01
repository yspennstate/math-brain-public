# The corner package, merged: one statement of what is proved, on what, with today's constants
# (iter 176, 2026-08-10; authorized by the second-night order "corner note final merged form once
# inputs settle" - the three referee rounds of this morning settled them)

STATUS AND READING ORDER. This is a CONSOLIDATION: every claim below exists in a refereed layered
document, and where this note and a layered document disagree, the LAYERED DOCUMENT IS RIGHT and
this note is the defect (the same rule as the localization statement page). Nothing here is new
mathematics. Provenance for each piece is the table in section 6. chi = 1/3 is NOT solved; this
package conditionally establishes the corner threshold, whose honest meaning is stated in section 5.

## 0. What the package establishes, in one paragraph

On Z^2 bond first-passage percolation with iid weights in [a, b], 0 < a < b, ASSUMING two one-sided
curvature conditions on the limit shape at the axis direction (both open on Z^2; section 2), the
half-plane mean gap A_+(l) = E T_+((0,0),(0,l)) - g(l e_2) is O(sqrt(l) polylog(l)) - the I8 input
at the strength the corner route needs - via an explicit two-spine dive construction, with every
auxiliary probabilistic input either published (Kesten-scale concentration; Alexander's mean bound)
or derived inside the package and independently refereed (the entropy walk for confined times; the
localization tail lemma). Consequently, per the corner note's refereed consequence chain, the
corner obligation closes for envelope exponents alpha > 1/3 package-relatively: the program
assembles exactly for chi in (1/3, 1/2), conditional on the stated inputs.

## 1. The claim chain, with each link's supplier

    corner threshold (alpha > 1/3)  <-  I8: A_+(l) = O(sqrt(l) polylog)     [C1 note, refereed]
    I8                              <-  the two-spine dive                  [v2, 3 referee rounds]
    dive consumes: (H-curv) upper   <-  HYPOTHESIS c_+ (open)               [section 2]
                   (H-wand) tail    <-  localization lemma                  [refereed iter 162]
                   (H-I3) confined  <-  entropy walk                        [refereed iter 154]
                   (P-Alex), (P-conc) published, unconditional
    localization lemma consumes: (P-conc), (P-Alex), and c_- (open)         [section 2]
    entropy walk consumes: BLM 6.15 (published) + deterministic counts      [nothing open]

The dependency graph is a DAG (verified iter 107; re-checked when (L3) reuse was added): no cycle,
and in particular the localization lemma never consumes any output of the dive.

## 2. The hypothesis ledger - exactly two unpublished inputs, doing different jobs

(c_+) POINTWISE UPPER curvature at e_2: u(s) - u(0) <= c_+ s^2 for |s| <= delta, u the profile of
      g at the axis. Consumed ONCE, by the dive's GEOM pricing through first differences at the
      axis. One-sided; nothing two-sided is used anywhere.
(c_-) ENCLOSING-BALL LOWER curvature at e_2 on an arc: dogleg excess >= c_- d^2/r for transversal
      displacement d <= delta r. Consumed ONCE, by the localization lemma (what nature pays to
      wander). Also one-sided - per the v2 referee, this is the side Newman-Piza actually print.
      Known constraints: genuinely restrictive (every l^p norm with p > 2 has c_- = 0 at its axis -
      store row, verified); for AXIS-ALIGNED spans the midpoint form suffices (midpoint minimality,
      refereed); for the dive's TILTED pairs, three priced options exist (v2 seam bracket), default
      being the restricted union at no constant cost.
Neither implies the other; a shape can fail either alone. Everything else consumed anywhere is
published or refereed-internal.

## 3. Constants, post-referee (U[1,2] instantiation in brackets)

    dive parameter        K in [5, 10]           (REF1: the upper bound was missing; 2^xi <= C_K)
    window constant       C_K = 1/(1 - K^{xi-1})  [K=5, xi=3/4: 3.0188]
    localization Form A   P(dev >= sigma W_r) <= 12 C1 (b/a) r exp(-c'' c_- sigma^2)   (REF3: 12, not 18)
    chase constant        c'' = c1/(6 sqrt(2 + b/a))              [c1/12]
    range                 sigma^2 <= (delta^2/4) sqrt(r)          (REF3: /4, ceiling escape)
    required wlogs        delta <= min(1, 3 C2/c_-);  c1 <= 3 sqrt(2 + b/a)/C3   (REF3, new)
    validity floor        r >= r_0, range EMPTY below              (REF3; measured 1e5.5-1e14)
    walk tail (improved)  P(T_+ - ET_+ >= t sqrt(r)) <= exp(-a t^2/(8 b^3)), t in (0, 4b^2 sqrt(r)/a)
                          (REF2: factor 2 better, variational parameter deleted)   [exp(-t^2/64)]
    seam wiring           c = (c''/2) c_-                          [c1 c_-/24]
    union count law       consumer's A >= max(2, C3 c'') - made vacuous by the c1 wlog (A = 2 works)

## 4. Scope, stated with the theorem as the campaign's threshold law requires

Asymptotic throughout, with THREE computed thresholds, none small:
    l_0 (dive's own o(1) tilts):      ~1e80-1e90 at the literal base case; ~1e18 under the
                                       stratified base-case reading (REF1's structure, derived
                                       7.3; REVIEWED 2026-08-12 - both named checks close, see
                                       the [REVIEWED] annotation at v2's 7.3 STATUS paragraph;
                                       two stale prints flagged for v3)
    r_0 (localization validity floor): 1e5.5-1e14 depending on constants (REF3)
    l_1 (localization -> dive seam):   ~1e91-1e127 (REF3; scales with the base exponent like l_0)
No numerical experiment at any reachable size probes the regime where the hypotheses hold; every
machine-check in this campaign tests bookkeeping, never the regime. This does not distinguish the
package from most multiscale asymptotics, but here it is PRINTED rather than implied.

## 5. What this does and does not mean

DOES: reduce the corner side of the chi = 1/3 program, package-relatively, to two unpublished
one-sided curvature statements about the Z^2 limit shape - both believed, neither proved, and the
c_- side now known to be genuinely restrictive rather than free. Every other input is published or
refereed inside the campaign with its check scripts on disk.
DOES NOT: touch the WALL (CRUX section 2). The variance engine still cannot iterate on today's
unconditional inputs; the wall reduces to the variance ratio at the typical blocks ((L1'), three
independent routes, needed only on O(M^{7/4}) axis blocks) and behind it sits a fluctuation-scale
variance lower bound - a well-known open problem, not a bespoke hypothesis. chi = 1/3 remains open,
and this package does not claim otherwise.

## 6. Provenance table (the layered records are the authority)

    dive + [REF1][V5-x] tags        problem/I8_from_curvature_v2_iter82.md (+ REFEREE1_*)
    localization + [REF3] section 6 problem/localization_tail_draft_iter106.md (+ REFEREE3_*)
    statement page                  problem/localization_lemma_STATEMENT_iter130.md
    entropy walk + [REF2] tags      problem/I3_entropy_route_walk_iter86.md (+ REFEREE2_*)
    corner consequence chain        problem/C1_corner_route_attempt_iter60.md (+ REFEREE_iter72)
    wall + reduction                problem/CRUX_iteration_arithmetic.md sections 2, 8, 9
    ledger entries                  VERIFIED_CLAIMS_LEDGER.md 25-33
