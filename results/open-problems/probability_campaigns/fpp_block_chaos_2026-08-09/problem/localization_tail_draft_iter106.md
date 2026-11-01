# The localization tail from concentration plus curvature: a draft of the (H-wand) fallback lemma
# (iter 106, author's hand)

STATUS: REFEREED, iter 162 (2026-08-10) - report problem/REFEREE3_localization_report.md with three
check scripts and their outputs. MAIN RESULT: the mechanism and every exponent SURVIVE; G-a, G-b(i),
G-c's display, G-d, G-e and G-f's totals all CONFIRMED by independent re-derivation. The referee
returned FOUR corrected constants, TWO new conditions the draft must state, ONE genuine hole WITH a
free repair of its own construction, and ONE conditional narrowing that matters to the v2 consumer.
All applied in place below with [REF3] tags at the exact sites; the sharpest items, so no summary
hides them: (1) Form A's prefactor is 12 C1 (b/a_w) r, not 18 (union count was loose); (2)
C''' = delta^2/4, not delta^2 (the CEILING of D can escape the window); (3) a new wlog
c1 <= 3 sqrt(2 + b/a_w)/C3 is REQUIRED to close a middle band the draft left unproved (45/324 grid
points); (4) THE RANGE CAN BE EMPTY at small r - "r >= r_0" must be stated, with r_0 measured
between 1e5.5 and 1e14 depending on constants; (5) G-b(ii)'s "v arbitrary at its distance" is a
READING of (H-curv-LOWER), not a consequence - the referee PROVED it free for axis-aligned spans
(convexity + lattice reflection) but measured it FALSE by 4.5% for tilted spans, which the v2
consumer uses; (6) the union may be restricted to j in [-delta r/2, r + delta r/2] via the
referee's own convexity repair (excess >= g(e_2) * overshoot, no curvature needed), which kills the
far-longitudinal sites the tilted-span worry lived on. Previous status line kept below for the
record. This is the fallback named in the
v3 document's tail-form debt line: if no printed Z^2-FPP theorem supplies the deviation tail,
derive it inside the program. If this survives its referee, (H-wand)'s tail form stops being a
citation debt and becomes a lemma of the program, consuming only inputs already on the ledger.
Mesh task 480 is this item's landing; this draft starts the clock on its referee.

## 0. What is to be proved, exactly

LEMMA (conditional, draft). Z^2 bond FPP, iid weights in [a,b]. Assume:
  (P-conc)  Kesten-scale concentration for free passage times, direction-uniform (published):
            P(|T(x,y) - E T(x,y)| >= t sqrt(|x-y|)) <= C exp(-c t) for t <= C' sqrt(|x-y|).
  (P-Alex)  Full-plane Alexander (published): E T(x,y) <= g(y-x) + C sqrt(|y-x|) log |y-x|.
  (H-curv-LOWER) ENCLOSING-BALL curvature at e_2, in an o(1) arc: for directions u within the arc
            and transversal displacement d <= delta r,
            g(v) + g(x - v) - g(x) >= c_- d^2 / r
            whenever x = r u and v sits at transversal distance d from the segment [0, x].
            [This is the ONE-SIDED enclosing-ball condition - per the v2 referee's reading, the
            side Newman-Piza actually print. It is NOT the (H-curv) upper pinning the v3 document
            uses for GEOM. See section 3 for the two-sides clarification.]
THEN, for the free geodesic between endpoints at distance r in the arc, with W_r = sqrt(r Q_r)
and Q_r = sqrt(r) (Kesten scale):
    P( transversal deviation >= sigma W_r ) <= C poly(r) exp( - c'' c_- sigma^2 )
for sigma^2 <= C''' sqrt(r). In (H-wand)'s notation: stretched-exponential tail with theta = 2 -
GAUSSIAN in sigma, stronger than the theta > 0 the consumer needs, on exactly the quantile range
the consumer uses (sigma ~ polylog). [All constants now explicit per G-c, WITH the referee's
corrections of section 6 applied - read the display as: poly(r) = r, C = 12 C1 b/a_w (REF3-1),
c'' = c1/(6 sqrt(2 + b/a_w)) CONFIRMED, C''' = delta^2/4 (REF3-2); U[1,2]: c'' = c1/12 CONFIRMED.
Additionally required: the wlog c1 <= 3 sqrt(2+b/a_w)/C3 (REF3-3) and r >= r_0 (REF3-4, the range
is EMPTY below it). The union may be taken over j in [-delta r/2, r + delta r/2] only (REF3-6).]

## 1. The mechanism (Newman-Piza's dogleg, upgraded from median to tail)

Suppose the geodesic gamma from 0 to x = r e_2 passes within distance 1 of a point v at
transversal distance D >= sigma W_r. Then, up to an O(b) seam cost,
    T(0, x) >= T(0, v) + T(v, x) - O(b).
[As resolved in G-a and priced in G-c, the final form needs no seam at all: the through-vertex
v* at level exactly ceil(D) gives the inequality EXACTLY, and the union is linear, not r^2.
This section keeps the original narration; sections 4(G-a)/(G-c) carry the arithmetic.]
Take expectations of the RIGHT side via subadditivity's floor and curvature:
    E T(0, v) + E T(v, x) >= g(v) + g(x - v) >= g(x) + c_- D^2 / r        [(H-curv-LOWER)]
while the LEFT side's mean is capped by (P-Alex):
    E T(0, x) <= g(x) + C sqrt(r) log r.
So the through-v event forces at least one of three deviations:
    [T(0,x) - E T(0,x)]  or  [E T(0,v) - T(0,v)]  or  [E T(v,x) - T(v,x)]
to exceed (1/3)(c_- D^2/r - C sqrt(r) log r - O(b)). At D = sigma W_r = sigma r^{3/4}:
    c_- D^2 / r = c_- sigma^2 sqrt(r),
which dominates the Alexander error once sigma^2 >= C log r. Each deviation is a (P-conc) event
at t ~ c_- sigma^2 / 3 (both legs have length in [r/2, 2r], so their sqrt normalizations are
comparable up to constants):
    per-site probability <= 3 C exp( - c c_- sigma^2 / 3 ).

## 2. The union, and the range

Union over a unit grid of candidate points v in the strip {transversal distance in [sigma W_r,
r]} - at most C r^2 sites; dyadic refinement over deviation scales D = 2^k sigma W_r tightens the
constants but is not needed for the statement. Total:
    P( deviation >= sigma W_r ) <= C r^2 exp( - c' c_- sigma^2 ),
and the poly(r) is absorbed by sigma^2 >= (2/c' c_-)(2 log r + A log l) at the consumer's
quantile. The (P-conc) range t <= C' sqrt(r) translates to sigma^2 <= C''' sqrt(r) - far above
the polylog quantiles consumed. QED-SHAPE (gaps below).

## 3. The two curvature sides do different jobs - a ledger clarification this draft forces

The v3 document's (H-curv) is the UPPER pinning (u(s) - u(0) <= c_+ s^2): it prices GEOM - the
cost the CONSTRUCTION pays for diving, an upper bound on a norm difference. THIS lemma needs the
LOWER side (the enclosing ball, g-dogleg >= c_- d^2/r): it prices what NATURE pays for wandering,
a lower bound on a norm difference. Neither implies the other; a shape can be flat (kills c_-,
wandering uncontrolled, this lemma dies) or kinked (kills c_+ locally... though convexity plus
evenness limits how) independently. The honest hypothesis ledger for the FULL corner package
therefore carries BOTH one-sided conditions, each consumed exactly once: c_+ by GEOM, c_- by the
wandering tail. Neither is two-sided arc curvature; both are one-sided, per the referee's
favourable correction. This split was implicit in (H-wand)'s pedigree note; this draft makes it
explicit, which is worth having even if the lemma itself dies in review.

## 4. THE GAPS, named for the referee

(G-a) THE SEAM AND THE GRID. [RESOLVED iter 108, cleaner than drafted - referee to confirm:
      there is NO seam. A lattice path changes transversal coordinate by unit steps, so if the
      geodesic's transversal max reaches D it contains a vertex v* at level EXACTLY ceil(D)
      (take the first such). v* lies ON gamma, so subpath optimality gives
      T(0,x) = T(gamma) = T(gamma[0->v*]) + T(gamma[v*->x]) >= T(0,v*) + T(v*,x) EXACTLY -
      the through-v* lower bound with no O(b) correction and no within-1 coupling. The union runs
      over the sites v* can occupy: two levels (+-ceil(D)), longitudinal coordinate bounded by
      the length cap |y| <= (b/a_w) r - LINEARLY many sites, C r per level, not the drafted r^2.
      Section 2's poly(r) improves to C r; nothing else changes.]
(G-b) LEG DIRECTIONS AND LENGTHS. [RESOLVED iter 108 - referee to confirm, two parts:
      (i) THE FAR BAND DIES DETERMINISTICALLY. A path from 0 to r e_2 through transversal level D
      has at least r + 2D edges (l1: the transversal excursion costs 2D extra steps), each of
      weight >= a_w, so T(through-D) >= a_w(r + 2D); the direct path caps T <= b r. Through-D is
      therefore IMPOSSIBLE outright for D > r(b - a_w)/(2 a_w) - probability zero, no union term.
      Only the band sigma W_r <= D <= r(b - a_w)/(2 a_w) remains, and its leg lengths lie in
      [ceil(D), C_b r] with C_b = 1 + (b - a_w)/a_w + 1 - constants absorb the sqrt normalization
      spread in (P-conc).
      (ii) THE DIRECTION WORRY WAS MISPLACED. The legs' concentration input (P-conc) is
      DIRECTION-UNIFORM as published (Kesten/Talagrand - all directions, no arc), so steep legs
      cost nothing. The only arc-constrained input is (H-curv-LOWER), and its arc constrains the
      ENDPOINT direction of the segment [0, x] (here exactly e_2), not the dogleg legs - the
      displaced point v is arbitrary at its distance in the condition as stated. No wider-arc
      hypothesis is needed.
      MACHINE-CHECKED iter 109 (bug-catcher, not proof - scratchpad bandcap_check.py, seed
      20260810): the deterministic cap held on 600 random U[1,2] instances at r = 32/64/128
      (max observed deviations 2/4/6 vs caps 16/32/64); the tracker passed a planted-detour
      positive control; and the BOUNDARY PROBE behaved exactly as the arithmetic prices it - a
      cheap highway planted at cap-4 was taken to exactly its depth (28 of cap 32), one planted
      at cap+8 was refused outright (deviation 0). The check also caught a pre-run bug in MY OWN
      test harness: a planning slip had the U[1,2] cap at r/4 instead of r/2, and the patch
      width sized off the wrong number would have masked violations - caught by the
      disconfirmation discipline before the first run.]
(G-c) THE CONSTANT CHASE. [RESOLVED iter 114 by hand - referee to confirm. The task changes
      from "re-derive with explicit constants" to "check this arithmetic."
      SETUP. D = sigma W_r <= delta r; v* = the first vertex at transversal level Dbar := ceil(D)
      (G-a, exact - no seam, no O(b)); union over N <= 6 (b/a_w) r sites (two levels +-Dbar,
      longitudinal range |j| <= (b/a_w) r from the length cap).
      SPLIT, EXPLICIT. On the through-v* event, T(0,x) >= T(0,v*) + T(v*,x) exactly, so
          [T(0,x) - ET(0,x)] - [T(0,v*) - ET(0,v*)] - [T(v*,x) - ET(v*,x)]
            >= g(v*) + g(x - v*) - g(x) - C3 sqrt(r) log r    [legs floored by E T >= g (Fekete);
                                                               span capped by (P-Alex)]
            >= c_- Dbar^2 / r - C3 sqrt(r) log r  =:  Delta,
      hence at least one centered term exceeds Delta/3 - and only one-sidedly: the span UPWARD,
      or a leg DOWNWARD. (H-version accounting, CORRECTED iter 116 - my iter-114 print of this
      parenthesis claimed the walk supplies "exactly that", which is HALF-wrong: the walk covers
      the span's UPPER tail, yes, but its own not-covered section says the LOWER tail of T_+ is
      not walked - so the legs' downward deviations would need free lower tails (published I2)
      plus control of E T_+ - E T at child scales, which is A_+(r') again: the G-d revival
      clause's scale-by-scale architecture. One more reason all current consumers use the FREE
      version, where (P-conc) covers both directions.)
      NORMALIZATIONS. Every pair length lies in [Dbar, C_L' r] with C_L' = 2 + b/a_w: legs
      |v*| <= r(delta + b/a_w), |x - v*| <= r(delta + 1 + b/a_w), both <= C_L' r for delta <= 1,
      and both >= Dbar (transversal distance); the span is r. So each of the three deviations is
      a (P-conc) event at t >= Delta / (3 sqrt(C_L' r)):
          P(through-v*) <= 3 C1 exp( - c1 Delta / (3 sqrt(C_L' r)) ).
      THE CANCELLATION. At D = sigma r^{3/4}: Delta = sqrt(r) (c_- sigma^2 - C3 log r)
      >= sqrt(r) c_- sigma^2 / 2 once sigma^2 >= (2 C3 / c_-) log r, and the sqrt(r) cancels the
      normalization's sqrt(r) exactly - the chi' = 1/2 vs xi' = 3/4 scaling identity is what makes
      the exponent r-free:
          exponent >= [c1 / (6 sqrt(2 + b/a_w))] c_- sigma^2  =:  c'' c_- sigma^2,
          i.e.  c'' = c1 / (6 sqrt(2 + b/a_w)).
      UNION. P(dev >= sigma W_r) <= 18 C1 (b/a_w) r exp( - c'' c_- sigma^2 )        [Form A]
      and, absorbing the linear factor,
          P <= exp( - (c''/2) c_- sigma^2 )
          once sigma^2 >= (2/(c'' c_-)) log(18 C1 (b/a_w) r).                        [Form B]
      RANGE LEDGER, all pinned. Lower: sigma^2 >= max( (2 C3/c_-) log r,
      (2/(c'' c_-)) log(18 C1 (b/a_w) r) ) - polylog, inside the consumer's quantiles. Upper:
      sigma^2 <= C''' sqrt(r) with C''' = delta^2, EXPLICIT, under the wlog
      delta <= min(1, 3 C2/c_-). That single constraint keeps D <= delta r inside the curvature
      window AND implies both (P-conc) range checks t <= C2 sqrt(pair) where they bind: on the
      span, Delta <= c_- sigma^2 sqrt(r) <= c_- delta^2 r <= 3 C2 r needs delta^2 <= 3C2/c_-
      (true: delta^2 <= delta <= 3C2/c_-); on the SHORT leg (length Dbar), Delta <= 3 C2 Dbar
      follows from D <= delta r <= (3 C2/c_-) r. [First print of this ledger wrote
      C''' = min(delta^2, 3C2/c_-) - valid but mixing a squared and a linear constraint;
      corrected same iteration to the clean form.]
      MID-BAND. For delta r < D <= r(b - a_w)/(2 a_w) (above the curvature window, below the
      deterministic cap): the event is contained in through-level-ceil(delta r), so Form A at
      sigma^2 = delta^2 sqrt(r) applies - stretched-exponential in r, far below any consumed
      quantile. Beyond the cap: impossible (G-b), no term.
      U[1,2] INSTANTIATION. b/a_w = 2: c'' = c1/12 in Form A, c1/24 in Form B. Every constant
      in the lemma now has a formula in (C1, c1, C2, C3, c_-, delta, b/a_w).]
(G-d) THE H-VERSION. [SUPERSEDED IN PLACE, iter 107: this gap is a PHANTOM of my framing - the
dependency audit (dependency_graph_iter107.md) traced every consumption site and NOBODY in the
current package consumes half-plane-geodesic wandering tails: v3's touching events are
FREE-geodesic deviations (on the non-touching event T_+ = T, which is the whole point of the
deep pricing), the corner note's concentration inputs are free-lower and confined-upper (the
walk, no wandering), and Claim 4 is deterministic. The free version of THIS lemma is the only
version any consumer needs; the graph is a DAG and no circularity architecture is required. The
dissolution survived its own falsifier sweep with a positive control. REVIVAL CLAUSE: if the
referee finds any site that secretly needs a confined-geodesic tail, this supersession is wrong
and the circularity question below returns in full.] Original text: The v3 consumer needs this
tail for HALF-PLANE geodesics between the priced
      ENTROPY WALK SUPPLIES (I3_entropy_route_walk_iter86.md, repaired form: Gaussian upper tail
      at sqrt scale, constant window). The dogleg's mean floor needs g_+ = g (the corner
      referee's self-contained F3 proof) and the same c_-. So the H-version consumes: the walk +
      F3 + c_- + (P-Alex restricted to H via A_+ <= ... NO - the Alexander cap must be for E T_+,
      which is g r + A_+(r), and A_+ is the very quantity the v3 document bounds - CIRCULARITY
      CHECK REQUIRED: the v3 proof consumes (H-wand) at scales r/K while bounding A_+ at scale r;
      if the H-version of THIS lemma consumes A_+(r') at smaller scales r', the induction may
      close scale-by-scale, but that must be architected, not assumed. THIS IS THE HARDEST GAP.)
(G-e) ONE-SIDEDNESS. [RESOLVED iter 110 - referee to confirm: the one-sided version is the same
      proof with half the union. For the wall-ward tail only, take v* at level -ceil(D) only (the
      first vertex the path puts at that level on the wall side); the dogleg floor consumes
      (H-curv-LOWER) only for displacements toward the wall; the union halves. The v3 consumer's
      touching events are exactly this one-sided form (the free geodesic between deep pairs
      dipping toward x = 0), so the lemma as consumed is the cheaper half. Both-sided remains
      true and costs only the factor 2 the draft already paid.]

## 5. What this changes if it survives

(H-wand) sheds its citation debt: its tail form becomes this lemma (theta = 2), consumed at
polylog quantiles well inside the range, with the hypothesis ledger clarified to two one-sided
curvature conditions doing different jobs. [CONSUMER CONTRACT, checked by hand iter 115 against
v2's [V5-1]/[V5-2] - referee to confirm both sides of the seam: v2 consumes this lemma only at
scales r' >= ~l^c/K (its section-5 base case, c <= 0.12), where sigma^2 = Theta(log l) sits
inside the Gaussian window delta^2 sqrt(r') for ANY fixed delta - no window condition survives
at the consumer; and the consumer's union constant must satisfy A >= max(2, C3 c'') so its
quantile clears this lemma's lower threshold - constant-level, satisfiable by choice, recorded
on the v2 side. Wiring: theta = 2, C = 1, c = (c''/2) c_- = c1 c_-/(12 sqrt(2 + b/a_w)).] The corner package's unpublished inputs then reduce
to: c_+ (GEOM), c_- (this lemma), I8-via-v3 (the construction), I3-via-the-walk (repaired), and
the wall stays the wall. Referee first; nothing moves in any ledger until then.

(G-f) ENDPOINT UNIFORMITY - the caveat both consumers now need (raised at iter 123 for the
      blockwise fourth moment, again at iter 127 for the slab count; ATTEMPTED HERE, iter 128,
      PARTIALLY RESOLVED with the residual gap named exactly).
      THE PROBLEM. Every consumer applies this lemma to a geodesic whose endpoints are RANDOM -
      wherever a longer geodesic happens to meet a slab or block boundary - while the lemma is
      stated for a fixed pair. A conditioned law is not a fixed-endpoint law, so the lemma cannot
      be quoted pointwise at the crossing points.
      THE ROUTE, and it needs no conditioning at all. By subpath optimality the crossing piece IS
      a geodesic between its own endpoints, so for any deviation threshold D,
        {crossing piece deviates >= D} SUBSET Union over boundary pairs (u,v) {geod(u,v) dev >= D},
      and a union bound needs no independence and no conditioning. The only question is how many
      pairs must be carried.
      THE COUNT IS DETERMINISTIC, not circular. The candidate endpoints are confined by (G-b)'s
      band cap - a deterministic fact, machine-checked iter 109 - so each boundary carries at most
      C n sites at slab scale n, hence at most C^2 n^2 pairs. With Form A's own linear prefactor
      and the union over M slabs, the total failure probability is
        <= M * C^2 n^2 * 18 C1 (b/a_w) n * exp(-c'' c_- sigma^2) = C' M n^3 exp(-c'' c_- sigma^2),
      which is o(1) once sigma^2 >= (log M + 3 log n + O(1))/(c'' c_-) - POLYLOG, and far inside
      the range sigma^2 <= delta^2 sqrt(n). So the endpoint union costs a constant multiple of
      log n in the quantile and nothing else. The polylog already absorbed into the block height
      (CRUX 9.7) covers it; only the constant inside the logarithm changes.
      THE RESIDUAL GAP, stated exactly because it is real. (H-curv-LOWER) is assumed on an o(1) ARC
      around the axis, so the union above is legitimate only for pairs whose chord lies in that arc.
      A pair with transversal offset >= theta n has chord tilt >= theta and falls outside. Two cases:
        (i) WIDE-ARC / NARROW-WEIGHT REGIME - NO GAP. The band cap bounds every crossing's tilt by
            (b - a_w)/(2 a_w) deterministically (1/2 for U[1,2]). If the curvature arc's half-width
            in slope is at least that number, NO large-tilt pair exists at all and the union above
            is complete. This is a condition relating the weight spread to the arc, checkable in
            any instantiation, and it is satisfied whenever the curvature hypothesis is assumed on
            a fixed arc rather than a shrinking one.
        (ii) NARROW-ARC REGIME - GAP. If the arc is genuinely o(1), large-tilt crossings are not
            excluded deterministically, and bounding their probability is a COARSE wandering
            statement (deviation of order theta n, i.e. linear) that this lemma cannot supply: at
            deviation theta n the quantile is sigma = theta n^{1-xi}, whose square exceeds the
            lemma's own range delta^2 sqrt(n). So the narrow-arc case needs a separate,
            weaker-but-different input: geodesics do not cross a slab with linear-order tilt. The
            only free fact in that direction is the band cap's constant, which is not small.
      STATUS: resolved in regime (i), open in regime (ii), with the dividing line explicit. Referee:
      the arithmetic of the union, and whether regime (i)'s comparison is the right one to demand of
      an instantiation.
      [(G-f) REGIME (ii) CLOSED, iter 129 - the narrow-arc case needs NO new input after all; it is
      the same lemma applied at the TOP scale, where the arc hypothesis is satisfied by construction.
      THE INCLUSION. A crossing of slab k with transversal offset |h2 - h1| >= theta n forces
      max(|h1|,|h2|) >= theta n / 2, since |h2 - h1| <= |h1| + |h2|. So
          {some slab is crossed with tilt >= theta}  SUBSET  {global deviation >= theta n / 2},
      an event about the SCALE-R geodesic (R = Mn) whose endpoints lie on the axis - inside the arc
      by construction, since the engine's column is axis-aligned. No union over slabs is needed: the
      right-hand event is global.
      IN RANGE, and checked numerically before being claimed. With W_R = R^{3/4} the lemma's
      condition sigma^2 <= delta^2 sqrt(R) is exactly D <= delta R, so D = theta n/2 is admissible
      whenever theta/2 <= delta M - true for every theta below the band cap at any M >= 5. The
      quantile is sigma^2 = (theta^2/4) sqrt(n) / M^{3/2}, giving
          P(some slab crossed with tilt >= theta) <= C (Mn) exp( - c'' c_- (theta^2/4) sqrt(n) M^{-3/2} ),
      stretched-exponential in sqrt(n) - which beats the C^2 n^2 pairs and the M slabs of the main
      union by an enormous margin. (Grid check across M in {5,8}, n in {1e4,1e6,1e8}, theta in
      {0.05,0.2,0.5}: in range at every point, exponent theta^2 sqrt(n)/M^{3/2}.)
      THE ONE HONEST LIMIT: that exponent is only LARGE once n >~ M^3 / theta^4 - at n = 1e4,
      M = 5, theta = 0.05 it is 0.0056 and the bound says nothing. So regime (ii) closes
      ASYMPTOTICALLY, for n above an explicit threshold n_0(M, theta, delta, c_-), which is the
      regime the engine iterates in but must be stated rather than assumed.
      CONSEQUENCE: (G-f) is closed in BOTH regimes - deterministically when the arc is wide relative
      to the weight spread, asymptotically otherwise - so the endpoint-uniformity caveat that both
      consumers were carrying costs a logarithm in the quantile and a largeness condition on n, and
      no new hypothesis. Referee: the inclusion, the range identity D <= delta R, and the threshold.]

## 6. THE REFEREE'S CORRECTIONS, applied (iter 162) - each at the strength it was delivered

(REF3-1) FORM A PREFACTOR: 12 C1 (b/a_w) r, not 18 (one-sided form: 6). The union count is
N <= 2(rho r + 1) <= 4 rho r with rho = b/a_w; my 6 rho r was loose. Every display quoting 18
should read 12; Form B's absorption threshold shrinks accordingly. Exponents untouched.

(REF3-2) RANGE CONSTANT: C''' = delta^2 / 4, not delta^2. The through-vertex sits at level
ceil(D), and requiring ceil(D) <= delta r (the hypothesis window as literally written) costs the
factor: D <= delta r - 1 must hold at the QUANTILE, and the clean sufficient form is
sigma^2 <= (delta^2/4) sqrt(r). My draft let the ceiling escape the window by one lattice unit.

(REF3-3) NEW WLOG, REQUIRED not optional: c1 <= 3 sqrt(2 + b/a_w) / C3. Without it there is a
middle band of (sigma, r) - 45 of 324 grid points in the referee's sweep - where the draft's
display is UNPROVED: the Alexander error is not yet dominated and the concentration range not yet
entered. Since c1 is a constant of the published input, this is a wlog in the harmless direction
(shrinking c1 only weakens the conclusion), but it must be STATED.

(REF3-4) THE RANGE CAN BE EMPTY: the lower threshold (polylog) can EXCEED the upper (delta^2
sqrt(r)/4) at small r - 1488 of 2187 grid points at r <= 1e10 in the referee's sweep. The lemma
therefore holds FOR r >= r_0(constants), with r_0 measured between 1e5.5 and 1e14 across plausible
U[1,2] constants. Stated here; every consumer inherits it.

(REF3-5) G-b(ii) NARROWED, and this is the one that matters to v2: "the displaced point v is
arbitrary at its distance" is a READING of (H-curv-LOWER), and it is load-bearing - the union's
far-longitudinal sites need exactly it. The referee PROVED the reading free for AXIS-ALIGNED spans
(convexity plus lattice reflection: the midpoint case implies all longitudinal positions; zero
numerical violations), and measured it FALSE for TILTED spans - a 4.5% deficit on the worst case
swept - which are what the v2 consumer's tilted pairs present. CONSEQUENCE: as applied to v2,
either (H-curv-LOWER) must be READ as holding for displaced points off tilted spans (a genuinely
stronger hypothesis, to be declared in v2's ledger), or the union must avoid needing it - which the
next item supplies.

(REF3-6) THE REFEREE'S OWN REPAIR, free of curvature: for sites with longitudinal coordinate
outside [-delta r/2, r + delta r/2], the dogleg's EXCESS is at least g(e_2) times the longitudinal
overshoot, by CONVEXITY OF g ALONE. Those sites die at exp(-c1 g(e_2) delta sqrt(r)/(6 sqrt(2+rho)))
- stretched-exponential, no curvature consumed - and the union restricts to the window as literally
written. This simultaneously repairs G-f(i)'s justification defect (the band cap was quoted at slab
scale where it only holds at top scale; the restricted union no longer needs it) and removes the
tilted-span exposure of (REF3-5) for every site the restricted union retains. c'' and c_- unchanged.

(REF3-7) G-f CORRECTIONS: the tilt admissibility is theta <= 2 delta M (not "any theta below the
band cap"), and the honest threshold is n_0 = (16/(c'' c_-)^2) (M^3/theta^4) log^2(C M n) - four to
nine orders of magnitude above the printed M^3/theta^4. The G-f total survives both.

(REF3-8) SEAM [V5-2] DEFECT, exported to v2: the "upper range clean at all consumption scales" line
is ASYMPTOTIC with an unstated threshold l_1 defined by l^{c b/2}/log l >= 2 A sqrt(K)/(delta^2 c'' c_-),
which for plausible U[1,2] constants is l_1 ~ 1e91 to 1e127 - ABOVE v2's own 1e80 scope note. The
seam is real but it opens even later than the construction's own hypotheses do. Recorded in v2.
