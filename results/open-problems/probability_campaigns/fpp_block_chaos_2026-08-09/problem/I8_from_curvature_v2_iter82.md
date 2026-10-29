# I8 from curvature, v2: the consolidated conditional theorem (iter 82)

REFEREE VERDICT ON THIS DOCUMENT (iter 88/89): MAJOR REVISION - every re-derived bound survives,
no exponent moves, all repairs statement-level. Full report: I8_v2_REFEREE_iter83.md. The two
MAJORs are fixed in place below with [V2REF] tags; the remaining items are listed here and owed to
a v3 pass:
- WORST DEFECT (consequence chain, MAJOR - and it is the exact error I asked the referee to hunt):
  the main threshold and assembly claim SILENTLY CONSUME I3, which appeared zero times in this
  document's "one hypothesis ledger". FIXED IN PLACE: (H-I3) added to section 1. (P-conc) covers
  free times only, never T_+.
- STATEMENT (MAJOR): (H-wand) was scoped to the anchored class, whose wandering the proof never
  consumes; the pairs actually priced (bulk and deep-far segments) fell outside the stated
  hypothesis. FIXED IN PLACE: (H-wand) re-scoped to the priced pairs.
- Construction: the exact-far-depth class with a separation window is not step-stable off s' = s,
  and it excludes its own root (the D = 0 branch). One-line repairs owed in v3: far-depth WINDOW
  (per the sketch referee's fixed-point form), and D = 0 admitted.
- Slope lemma: internally correct (constants, corner-robustness, slack re-derived and pass) BUT
  wired to the wrong architecture - v2's two-spine chain never forms the tilted-base object the
  lemma prices, the fixed-point ratio has no derivation HERE, and a simpler CENTERED second-
  difference bound does the job with better constants. v3: replace the GEOM pricing accordingly.
- Touching account: PASSES at A = 2 across both spines plus root (re-derived); one constant bug
  (the tail constant c ignored) and two false K^xi-clearance claims inherited from the abandoned
  normalization - strike in v3.
- Base case: PASSES (multiplicity 2, large exponent room; c <= 0.12 is dead-tree slack; the
  tilt-sum claim is true but idle in this architecture).
- HONESTY CLAUSE: FALSE AS A UNIVERSAL, in the FAVOURABLE direction - the referee checked the
  fetched Newman-Piza paper and its printed condition is a ONE-SIDED enclosing ball, not two-sided
  arc curvature. The hypothesis ledger IMPROVES. But the dropped G3 tail-form citation gap must be
  reinstated (the tail strength at the deep quantile still needs its source named).

STATUS: CONSOLIDATION of I8_from_curvature_sketch_iter73.md (refereed REPAIRABLE), the addendum's
Parts 1-3, and the referee's repairs (report I8_sketch_REFEREE_iter74.md), as ONE document with one
hypothesis ledger and reconciled constants. Refereed MAJOR REVISION as above; v3 owed. Nothing here
is new relative to its sources; what is new is that it is in one place, with the right reasons
attached to the right conclusions.

## 1. Statement

SCOPE, STATED WITH THE THEOREM RATHER THAN BURIED (iter 150; arithmetic in section 7): this is an
asymptotic statement whose OWN hypotheses first hold at l_0 ~ 1e80. The class and (H-wand) both
require o(1) chord tilts, and the tilt binds at the base scale, where it runs to tens at any
reachable size (~44-88 at l = 1e6, ~19-38 at 1e30, still above 1 at 1e65). Legitimate for an
asymptotic theorem; recorded here because a reader of the statement should not have to reach
section 7 to learn that no instantiable scale satisfies the hypotheses.

CONDITIONAL THEOREM (I8 at the strength the corner route needs). Z^2 bond FPP, iid weights in
[a,b], 0 < a < b < infinity. Assume:

(H-curv) POINTWISE UPPER curvature at e_2, in profile form: with u(s) := g((s,1)) (convex and even
  in s by lattice symmetry), u(s) - u(0) <= c_+ s^2 for |s| <= delta. [Equivalent at e_2 to MG2A's
  H2 upper half, constant C = c_+ + g(e_2)/2 + o(1). [V3, iter 92: consumption route updated - the
  proof now consumes this DIRECTLY through first differences at the axis (the GEOM re-wiring in
  section 3); the slope lemma is retired. Still nothing two-sided, still pointwise-upper only.]]

(H-wand) [V2REF: RE-SCOPED per the referee's statement-MAJOR - the hypothesis must cover the pairs
  the proof actually PRICES, which are the bulk and deep-far segments, not the anchored class]
  Wandering with stretched-exponential tails at scale W_r = r^xi for some xi <= 3/4: for FREE
  geodesics between the priced pairs - endpoints at depths in [d(r)-range, d(K r)-range], chord
  tilts o(1) around e_2 - P(wall-ward transversal deviation >= sigma W_r) <= C exp(-c sigma^theta),
  theta > 0.
  [REF1, iter 149 - A NEW DEFECT, found by the independent referee and not by any previous round:
  this printed depth range FAILS TO COVER THE WINDOW'S DEEP END, by a factor C_K K^xi = 10.09.
  Earlier referees found only the shallow-end mismatch and it was repaired; the deep end was never
  checked, and the class admits far-depths up to C_K d(K s') while the hypothesis as printed is
  stated only to d(K r)'s own range. The fix is to widen the stated range to cover
  C_K K^xi d(r) - free in kind, since it is the same hypothesis at a constant multiple of the
  quantile, but it is a REAL hole in the ledger until written, and any consumer quoting (H-wand)
  at the window's deep members is quoting something this line does not currently supply.] The anchored pairs' own wandering is never consumed. [HONESTY CLAUSE, CORRECTED in
  the favourable direction per the referee's check of the fetched Newman-Piza source: its printed
  condition is a ONE-SIDED enclosing ball at the direction, not two-sided arc curvature - so the
  pedigree this hypothesis imports is WEAKER than v2 first stated. CITATION LANDED for the
  exponent (iter 93, from the survey text on disk): xi <= 3/4 under curvature is Newman-Piza
  Theorem 7 (ADH survey Theorem 4.7: d = 2, F(0) < p_c, E exp(alpha tau) < infinity, x a
  direction of curvature). STILL OWED, stated exactly: Theorems 4.6/4.7 are IN-PROBABILITY
  cylinder-containment statements - they name the exponent, NOT the stretched-exponential TAIL
  at the deviation quantile that (H-wand) consumes. The tail FORM remains an explicit debt
  (plausibly in the concentration-plus-curvature quantification; not yet verified in any source
  on disk). SEARCH TRAIL (so the debt is not re-walked): arXiv 2502.12797 (Lam-Nakajima, bounded
  weights Z^d) CHECKED AND RULED OUT iter 101 - moderate deviations for passage TIMES only, no
  geodesic-localization statement, no curvature input; the LPP watermelon-style tail upgrades are
  the wrong model. The debt is a PRINTED Z^2-FPP theorem of the form P(deviation >= sigma W_r)
  <= C exp(-c sigma^theta) under curvature - still unfound; the fallback remains deriving it
  inside the program from (P-conc) plus (H-curv) via chaining, which would move it from citation
  debt to a lemma with its own referee.] [V5-2, iter 115 - the fallback now EXISTS with explicit
  constants, pending its referee: localization_tail_draft_iter106.md, all five gaps priced (G-c
  closed iter 114). If it survives, wire: theta = 2, C = 1 (Form B), and
  c = (c''/2) c_- = c1 c_- / (12 sqrt(2 + b/a_w))   [U[1,2]: c1 c_-/24],
  where c1 is (P-conc)'s rate and c_- the enclosing-ball constant of (H-curv-LOWER) - note the
  supplier consumes the LOWER one-sided curvature side, a hypothesis this document does not
  otherwise carry; the two-sides ledger lives in the draft's section 3. Range compatibility
  checked by hand iter 115 (referee to confirm with the draft): upper range clean at all
  consumption scales r' >= ~l^c/K for any fixed delta; lower range forces only the A >= C3 c''
  choice recorded at [V5-1]. My check, not acceptance - the draft's referee owns the verdict.]
  [REF3 ON THIS SEAM, iter 162 - the draft's referee returned: [V5-1] CONFIRMED (and made vacuous
  by the draft's new wlog c1 <= 3 sqrt(2+b/a_w)/C3, under which A = 2 suffices outright).
  [V5-2] DEFECT, mine: "upper range clean at all consumption scales" is an ASYMPTOTIC claim with an
  unstated threshold l_1, defined by l^{c b/2}/log l >= 2 A sqrt(K)/(delta^2 c'' c_-), which for
  plausible U[1,2] constants lands at l_1 ~ 1e91 to 1e127 - ABOVE this document's own 1e80 scope
  note. So the seam opens even LATER than the construction's own hypotheses do. Consistent with the
  scope section's story (and improved the same way: everything scales with the base exponent c),
  but the honest ledger line is now: the localization supply to (H-wand) is valid for l >= l_1,
  not "at all consumption scales". Also inherited from the draft's referee: the supply carries the
  draft's r >= r_0 condition, and the tilted-span reading of (H-curv-LOWER) is NOT free - v2's
  tilted pairs have THREE options, priced (iter 165, from the referee's own fallbacks): (i) declare
  the stronger offset reading in this ledger as an added hypothesis; (ii) use the restricted union
  (draft section 6, REF3-5/6), which avoids the reading entirely at no constant cost - the default;
  or (iii) keep the full union and DERIVE the offset form from the geometric enclosing ball with
  the referee's explicit loss c_- -> c_-/(2+rho) at far sites, which costs the seam's wiring
  constant a factor 4 (U[1,2]: c = c1 c_-/96 instead of c1 c_-/24). For AXIS-ALIGNED spans none of
  this is needed: the offset reading is a THEOREM (midpoint minimality - convexity plus lattice
  reflection - now also a store row, verified 0/80k fresh trials plus the referee's 0-violation
  sweep).]

(P-Alex) Full-plane Alexander (published, unconditional for bounded weights):
  E T(x,y) <= g(y-x) + C sqrt(|y-x|) log |y-x|, uniform over directions.

(P-conc) Kesten-scale concentration for FREE passage times (published, unconditional). [V2REF:
  this covers free times ONLY - it never covers T_+.]

(H-I3) [V2REF: ADDED - the worst-defect fix. The consequence chain below consumes upper-tail
  sqrt-scale concentration for the CONFINED time T_+ (the corner note's input I3), and v2's
  original ledger omitted it entirely. Its current status: "no obstruction identified" per the
  corner referee, with a candidate closure via the entropy route walked in
  I3_entropy_route_walk_iter86.md (ledger entry 22) - PENDING REFEREE. Until that walk survives
  review, every consequence below is ALSO conditional on I3.]

THEN the one-wall nonrandom fluctuation satisfies
    A_+(l) := E T_+((0,0),(0,l)) - g(l e_2) = O( sqrt(l) (log l)^{max(1, 2/theta)} ).
Consequently P2(l) <= MEANGAP(l) <= A_+(l) is at sqrt-polylog scale, I8 of the salvaged corner
note holds, and (per that note's section 7 and the refereed pinning of CRUX 3b) the corner
threshold is alpha > 1/3: package-relatively, the program assembles exactly for chi in (1/3, 1/2).

## 2. The construction: a two-spine dive

Fix K with 5 <= K <= 10. [REF1, iter 149 - INDEPENDENT REFEREE FINDING, applied in place: this
document printed only "Fix K >= 5" and that is NOT ENOUGH. The per-member window needs
2^xi <= C_K, which caps K at 37 for xi = 3/4 and at 10 uniformly over xi <= 3/4. An unbounded K was
free to violate the very window this section defines. The upper bound is free to satisfy - K is a
fixed parameter of the construction - but it was missing, and nothing downstream had noticed.]
Dive depth at scale r: d(r) := sigma W_{r/K} with sigma := (A log l / c)^{1/theta},
A = 2, c the tail constant of (H-wand), l the GLOBAL top scale. [V4-1 fix, iter 98: this
GOVERNING definition had still omitted /c while section 3's tag claimed it fixed - the combined
referee's patchwork finding 1. One token, constant-level.] [Reconciliation: the referee's tree accounting needed A >= 2 over O(2^J K)
segments; the spine has only O(K log_K l) segments, for which A > 1 suffices; A = 2 is taken
uniformly - it costs only the polylog constant.] [V5-1, iter 115 - seam check against the tail
lemma's now-explicit range ledger (localization draft, G-c): the union's A = 2 is not the only
constraint; the lemma's Form B lower threshold requires A >= C3 c'' (so that sigma^2 = A log l/c
dominates (2 C3/c_-) log r' at r' up to l; c'' = c1/(6 sqrt(2+b/a_w))). Take
A := max(2, C3 c'') - constant-level, cost only in GEOM's polylog constant (GEOM scales with
sigma^2 ~ A). Upper range checked clean: all consumptions sit at r' >= ~l^c/K (the section-5
base case), where sigma^2 = Theta(log l) <= delta^2 sqrt(r') for l large, ANY fixed delta - no
window condition survives.]

CLASS. [V3.1, iter 98 - the combined referee found my iter-92 SOLID window [0, C_K d(K s')]
over-shot: the sketch referee's window was PUNCTURED, and the puncture was load-bearing. A solid
window admits a dead band of shallow members (far-depth in (0, sigma W_{s'/K})) whose far child
is priced by an (H-wand) instance the re-scoped hypothesis does not supply; and D = 0 below the
root contradicts branching-one.] P(s) := anchored pairs (0, y) -> (D, y + s') with s' in
[s/2, s], far-depth D in {0} UNION [sigma W_{s'/K}, C_K d(K s')], tilt DERIVED from the depth
window (<= 2 C_K d(K s)/s; not a free parameter - the V4-4 fix, t(s) was undefined). D = 0
members (the root, and admitted generally) take the TWO-CHILD step - branching stays contractive
per the referee's re-check, and child 0's far-depth d(s) = sigma W_{s/K} lands INSIDE the
punctured window at the child scale.
[REF1, iter 149 - independent referee CONFIRMED branching-one, and supplied the structural reason
this document never states: the puncture stratum is a SOURCE with no incoming edges. The far-depth
map is the CONSTANT map D -> d(s) > 0 (a super-attracting fixed point; the class parameter is reset
every step), so no child of any member ever has far-depth 0. Stratifying f_0 (the D = 0 members)
from f_+ (the band), f_0 never appears on a right-hand side and is evaluated at the TOP SCALE ONLY:
the dependency graph is a PATH, not a tree, which is why there is no 2^j growth to control. Counts
reproduced by brute force: 1 + 2J anchored members, (K-2) + 2(J-1)(K-1) = O(K log_K l) segments.
ONE SENTENCE OWED, flagged rather than quietly relied on: read literally, the single-symbol sup
recursion carries coefficient 2 at EVERY level and survives only by 0.001 in the exponent (base
l^0.4990 against break-even c = 0.12176). The stratified reading is what makes it comfortable;
without that sentence written into the document the base case is lucky, not proved.]

STEP at scale s on a class pair: chain points w_0 = (0,0) [translate], w_j = (d(s), j s'/K) for
j = 1..K-1, w_K = (D, s'). Pathwise T_+ <= sum of segment T_+'s; expectations add by linearity.
  - Child 0 (w_0, w_1): anchored, far-depth d(s) = d(K s'/K), scale s'/K - IN CLASS P(s/K).
    THE ONLY RECURSING CHILD.
  - Children 1..K-2: bulk at depth d(s), vertical chords. [V3, iter 92: the "clearance = K^xi,
    polylogs cancel" claim was inherited from the abandoned normalization and is STRUCK - what the
    touching account actually needs is only P(wall-ward dev >= d(s)) <= l^{-A} for these pairs,
    which is (H-wand) at their own scale by the choice of d(s). No ratio claim is consumed.]
    Full-plane priced via (P-Alex) + touching term.
  - Child K-1 (w_{K-1}, w_K): depths d(s) and up to C_K d(K s'). [V3: the K^xi-clearance phrasing
    struck here too, same reason; the touching account needs only the (H-wand) tail at this pair's
    own scale and depths, supplied by the re-scoped hypothesis.] BULK-TYPED, full-plane priced,
    NOT recursed. Tilt of its chord
    <= K^{1+xi} s^{xi-1} polylog = o(1). [This re-typing is the load-bearing architectural fact;
    found twice independently - addendum Part 3 and referee report section 1. V4-3 fix, iter 98:
    the fixed-point/ratio sentence that stood here (t over eta <= C_K - 1 = 2.02) is MARKED IDLE
    - it was the enabling fact of the RETIRED slope lemma and nothing in the v3 wiring consumes
    it; C_K survives only as the window constant above.]
  - ROOT: (0,0) -> (0,l) has far-depth 0; its chain yields TWO anchored children (one per end).
    Two spines total, branching one thereafter.

## 3. Pricing

TOUCHING (all full-plane-priced segments): each pays crude x P(touch) <= b(s/K + depths) x l^{-A},
with the quantile set so that P actually reaches l^{-A}: sigma = (A log l / c)^{1/theta}, where c
is the tail constant in P(dev >= sigma W) <= C exp(-c sigma^theta). [V3, iter 92: the tail
constant c was silently dropped in v2 - the referee's one constant bug. It enters sigma, hence
d = sigma W, hence GEOM's polylog constant; no exponent moves.] Across O(K log_K l) spine
segments: total O(K log l x l x l^{-2}) = o(1) at A = 2.

BULK MEANS: (K-1) segments per level at scale s/K: (P-Alex) gives g(chord) + C sqrt(s/K) log l each.

GEOM at scale s: chords (d(s), s'/K) once, (0, s'/K) x (K-2), (D - d(s), s'/K) once, total (D, s').
Exact telescoping (the waypoints are ON the chain, no leak - referee attack B).
[V3 RE-WIRING, iter 92, per the v2 referee: the two-spine chain's GEOM terms are FIRST differences
AT THE AXIS - g((offset, s'/K)) - g((0, s'/K)) with offsets d(s) and |D - d(s)| - NOT tilted-base
second differences. The slope lemma priced an object this architecture never forms. Direct
pricing: by the chordal form of (H-curv) (pointwise-upper at e_2; the 3a conversion in the sketch
referee's report), each term is <= C c_+ offset^2 K / s', so
    GEOM(s) <= C c_+ [d(s)^2 + (C_K d(K s'))^2] K / s' <= C' c_+ sigma^2 K^{1+2xi} s^{2xi-1}
             <= C'' sqrt(s) (log l)^{2/theta}   (xi <= 3/4),
    [REF1 ON V5-3, iter 149: CONFIRMED INDEPENDENTLY, with one constant of mine sharpened. The
    referee's tight bracket is K[C_K^2 + 2^{2xi} K^{-2xi}] = C_K^2 K + 2^{2xi} K^{1-2xi}; my V5-3
    below wrote the second term as 2 K^{1-2xi}, i.e. 2 where 2^{2xi} = 2.83 belongs at xi = 3/4 -
    my constant was slightly SMALL. The conclusion is unchanged and was reproduced by brute force:
    K = 5 valid (printed 55.90 >= tight 46.83, 1.194x loose), K = 4 FAILS (printed 32 < tight
    48.04). The referee also diagnoses WHY the document's printed K^{1+2xi} is right at all - it is
    what one gets by reading d(K s') as sigma (K s')^xi rather than sigma (s')^xi, so the print is
    correct for the wrong reason, which is exactly the kind of thing that survives until someone
    re-derives it.]
    [V5-3, iter 117 - the K-power discrepancy SETTLED by hand, referee to confirm: with
    d(K s') = sigma W_{s'} = sigma (s')^xi (the definition, read directly), the tight
    coefficient is C_K^2 K + 2 K^{1-2xi} - the REFEREE'S reading. This document's K^{1+2xi}
    is an upper bound iff K^xi >= C_K, which FAILS at K = 4 (2.83 < 3.41) and holds at K = 5
    (3.344 > 3.019) and beyond (monotone) - so the print is valid exactly on the document's
    own range K >= 5, loose by ~22% there, and NOT robust to lowering K. Both keep
    GEOM <= C sqrt(s) polylog; nothing downstream moves.]
the same scaling with cleaner consumption: H2-pointwise-upper at e_2, nothing else. The slope
lemma of section 4 is RETIRED from this proof - retained only as the record of what the abandoned
tree architecture would have needed.]

## 4. The slope lemma (RETIRED from this proof at v3 - see the GEOM re-wiring in section 3.
## Retained as the record of the tree architecture's need; internally correct per the v2 referee,
## modulo an unstated range condition. NOT consumed by the two-spine proof.)

For u convex, even, with u(s) - u(0) <= c_+ s^2 on |s| <= delta: u'(s) <= [u(2s) - u(s)]/s
<= 4 c_+ s, hence for base tilt t and increment eta with t/eta <= 2.02 + 2:
    u(t + eta) + u(t - eta) - 2 u(t) <= eta [u'(t+eta) - u'(t-eta)] <= 4 c_+ eta (t + 2 eta)
                                     <= 17 c_+ eta^2.
The level-uniform ratio t/eta <= C_K - 1 is the class fixed point - the SAME fact that stabilizes
the class. One lemma, two jobs. [Why pointwise-upper suffices where arc-pointwise does not: the
referee's counterexample (piecewise-linear interpolation of s^2, corners accumulating at e_2)
shows arbitrary tilted second differences can be first-order under pointwise pinning alone; the
ratio bound is exactly what excludes that regime. My earlier "the arc shrinks" reason is dead;
this is the true reason.]

## 5. The sum

    f(s) <= f(s/K) + (K-1) [C sqrt(s/K) log l] + C' sqrt(s) (log l)^{2/theta} + touching,
two spines, unrolled geometrically (ratio 1/sqrt(K) per level on the forcing), base at s0 = l^c
(c <= 0.12) paid crudely at C s0 x (multiplicity 2):
    A_+(l) <= 2 f(l/K) + root terms = O( sqrt(l) (log l)^{max(1, 2/theta)} ).
No branching factor exists; the early stopping serves only the base and the tilt-sum bound
(total accumulated tilt <= C K^{1+xi} sum over levels of r_j^{xi-1} polylog, dominated by the
smallest running scale l^c: o(1)).

## 6. What this document does NOT claim

- Nothing unconditional: (H-wand) is curvature-pedigreed and open on Z^2; no unconditional
  sublinear wandering exponent exists at current knowledge (search receipt: LOG iter 80).
- Nothing about the WALL: CRUX section 2's obstruction is untouched. chi = 1/3 remains open.
- Not a proof: a consolidation of a refereed-repairable sketch. [V4-2 fix, iter 98: the attack
  list that stood here was STALE - it pointed at the retired slope lemma and at the honesty
  clause's ORIGINAL claim, which the [V2REF] correction reversed (one-sided, favourable).
  Current open surfaces for the NEXT referee: the punctured-window step stability as restored
  (V3.1), the two-child contractive branching at D = 0, the GEOM constant's K-power (SETTLED
  by hand at [V5-3], iter 117: referee's tight reading C_K^2 K confirmed; the K^{1+2xi} print
  valid exactly on K >= 5, fails at K = 4 - the [V5-3] bracket carries the arithmetic for
  confirmation), and the (H-wand) tail-form citation debt
  [V5-2 note: the debt's in-program fallback is now a complete draft with explicit constants
  (localization_tail_draft_iter106.md) - the NEXT referee's surface includes that draft's five
  priced gaps and the iter-115 seam check (range compatibility + the A >= C3 c'' line), so the
  debt either becomes a lemma of the program or dies in that review].]

Sources: I8_from_curvature_sketch_iter73.md (with [REF] corrections); addendum Parts 1-3;
I8_sketch_REFEREE_iter74.md; C1_corner_route_REFEREE_iter72.md (for the I8 consumer's status);
CRUX 3b resolved banner (the pinning); ledger entries 16, 17, 21.

## 7. SCOPE: the threshold above which this construction's own arithmetic holds
## (iter 150, from referee 1's l_0 caveat, computed out; my first computation of it was WRONG and
## the error is kept below because it is instructive)

The class definition and (H-wand) both require the chord tilts to be o(1). Referee 1 recorded, as a
standing caveat rather than a defect, that every o(1) tilt claim here holds only for l >= l_0 with
l_0 "astronomical". That is worth a number, because "o(1)" in a document reads like a small quantity
and here it is not one at any scale a person will ever instantiate.

The tilt is LARGEST AT THE BASE SCALE r_0 = l^c (c <= 0.12), not at the top, so that is where it
binds:  tilt(base) = K C_K 2^{1-xi} * sigma * l^{c(xi-1)} = 17.95 * sigma * l^{-0.030} at K = 5,
xi = 3/4, with sigma = (2 log l / c_tail)^{1/2}. Evaluated:

    l = 1e6    tilt ~ 44 to 88        l = 1e30   tilt ~ 19 to 38
    l = 1e65   tilt ~ 2.5 to 4.9      l = 1e100  tilt ~ 0.27 to 0.55
    threshold for tilt < 1:  l_0 ~ 1e80 (c_tail = 2) to 1e90 (c_tail = 0.5).

So the construction's tilts are not merely large at accessible scales - they are of order tens at
1e30 and still above one at 1e65. Nothing about this is a defect in an ASYMPTOTIC theorem, and the
result was never claimed at finite scale. But it should be stated rather than left inside an "o(1)":
no numerical experiment at any reachable size can probe the regime where this construction's own
hypotheses hold, so the machine-checks in this campaign test bookkeeping, never the regime.

MY FIRST COMPUTATION OF THIS WAS WRONG, kept because the error is the instructive part: I evaluated
the tilt at the TOP scale l, getting a threshold of 1e7 to 1e9, and was about to record that the
referee had overstated "astronomical". The tilt carries l^{c(xi-1)} with the BASE exponent c, not
l^{xi-1} - the base scale is the small one, and a tilt that shrinks with scale is worst where the
scale is smallest. Same shape as the night's other errors: the arithmetic was right for a quantity
nobody needed. Referee 1's characterisation stands, and now it has a number.

### 7.1 WHAT DRIVES the 1e80 threshold - it is the base case, not the geometry (iter 152)

The base-scale tilt is 17.95 * sigma * l^{-c(1-xi)}, where c is the BASE-SCALE EXPONENT (r_0 = l^c).
The threshold is therefore set by c, and c is currently capped at 0.12 by the base case. Solving for
l_0 as a function of c (tail constant 1.0, K = 5, xi = 3/4):

    c = 0.12  ->  l_0 ~ 1e85        c = 0.30  ->  l_0 ~ 1e31
    c = 0.20  ->  l_0 ~ 1e49        c = 0.50  ->  l_0 ~ 1e18
                                    c = 0.80  ->  l_0 ~ 1e10

So the astronomical scope is not a property of the dive geometry at all. It is the price of running
the base case at c <= 0.12, and it moves by seventy orders of magnitude across the plausible range
of c.

WHY THIS MATTERS BEYOND TIDINESS, and it connects to referee 1's owed sentence. That cap traces to
the base case read LITERALLY, with the single-symbol sup recursion carrying coefficient 2 at every
level - which is exactly what put the break-even at c = 0.12176 and left the whole thing surviving
by 0.001 in the exponent. Referee 1's own stratification result says the literal reading is not the
right one: the puncture stratum is a SOURCE, f_0 never appears on a right-hand side, the dependency
graph is a PATH, and the recursing branch carries coefficient 1 rather than 2. Under that reading
the base-case constraint should relax substantially, and every order of magnitude it relaxes buys
several orders off l_0.

CLAIMED EXACTLY AND NO FURTHER: I have NOT re-derived the base-case constraint under the stratified
reading - that is the referee's territory and it is precisely the sentence flagged as owed. What is
established here is only the DEPENDENCE: l_0 is a steep function of c, and c is set by the base
case. If the owed sentence lands, it does not merely promote the base case from lucky to proved; it
also drags the theorem's scope down from 1e85 toward something a person can at least write.

### 7.2 MY OWN SEAM CHECK HAD THE SAME BLIND SPOT referee 1 found (iter 153)

Referee 1's two defects are one CLASS: the hypothesis as printed does not cover what the proof uses,
in a parameter dimension nobody thought to check (an unbounded K; the window's deep end). Applying
that lens to my own work rather than waiting for it to be applied to me:

AT ITER 115 I CHECKED THE SEAM between the localization lemma and this document in the QUANTILE
dimension (sigma-range clean at all consumption scales; the A >= max(2, C3 c'') compatibility line)
and in the SCALE dimension (consumption at r' >= ~l^c/K). I did not check the ARC/TILT dimension,
and it is the one that bites.

The supplier's (H-curv-LOWER) is assumed on an o(1) ARC around e_2. This document's priced pairs
have tilts bounded by the class window, and section 7 computes those tilts: tens at any reachable
scale, below one only past l_0 ~ 1e85. SO THE SUPPLY IS ONLY VALID ABOVE THE SAME THRESHOLD. When
the localization lemma supplies (H-wand) here, the arc condition - not the quantile, not the scale -
is what pins the seam to l_0.

WHAT THIS DOES AND DOES NOT CHANGE. It does NOT introduce a new hypothesis or move an exponent: both
documents were already asymptotic, and 7 already stated the threshold for this document's own class.
What it changes is the LEDGER: the seam check at iter 115 was recorded as "upper range clean, one
compatibility line owed", which reads as a seam that is fine apart from a constant. Honestly, the
seam is fine apart from a constant AND above 1e85, and the second half was missing. Recorded here in
place rather than left for the next referee to find, because that is the whole point of learning a
defect class from someone else's finding.

### 7.3 THE OWED SENTENCE, DERIVED - and it drags the scope from 1e85 to ~1e18 (iter 158)

Referee 1 flagged one sentence as owed: read literally, the sup recursion carries coefficient 2 at
every level and survives by 0.001 in the exponent, and the STRATIFIED reading is what makes it
comfortable. It supplied the structure (f_0 never appears on a right-hand side; the dependency graph
is a path; f_0 is evaluated at the top scale only) and left the consequence unwritten. Deriving the
consequence of a referee's OWN structural finding is not answering my own question in my own favour,
so here it is.

CHECK FIRST, that I have the structure right: under the LITERAL reading the base term is multiplied
by 2^J with J = (1-c) log l / log K, i.e. by l^{(log2/logK)(1-c)}, so the base contributes exponent
    c + 0.4307(1-c) = 0.4307 + 0.5693 c,
and requiring that to sit below 1/2 gives c <= 0.12176. That is referee 1's break-even to five
decimals, reproduced from the structure rather than copied; the level-sum factor comes out
1/(1 - K^{-1/2}) = 1.8090, also exactly its figure. So the reading is right.

THE CONSEQUENCE. Under the stratified reading the recursing branch carries coefficient 1, and the
factor 2 is applied ONCE at the top rather than per level. The base term is then simply C s_0 = C l^c
against the C sqrt(l) polylog the levels contribute, so the constraint is
    c < 1/2   (with polylog slack),
not c <= 0.1217. The admissible base exponent moves by a factor of four.

WHAT THAT BUYS, via 7.1's table: l_0 falls from ~1e85 at c = 0.12 to ~1e18 at c = 0.5. The theorem's
scope stops being a number with no physical meaning and becomes merely enormous. Nothing about the
mathematics changes - no exponent, no hypothesis, no constant in the main estimate. What changes is
that the construction is inside its own hypotheses sixty-seven orders of magnitude sooner.

STATUS, exact: this is MY derivation of the consequence of referee 1's finding, checked against two
of its own numbers, and I am not the referee of my own document. It should be confirmed by whoever
reviews v3 - the specific things to check are that the level sum really is geometric with ratio
K^{-1/2} under the stratification, and that nothing else in section 5's accounting reintroduces the
per-level factor 2 that the strata remove.

[REVIEWED 2026-08-12 (session 17556890, the "whoever reviews v3" this paragraph asks for; two
loop fires, LOG lines of 02:0x and 02:1x). BOTH NAMED CHECKS CLOSE AFFIRMATIVELY, and the claim's
arithmetic reproduces independently: break-even 0.121765 from c + 0.430677(1-c) <= 1/2, level
factor 1.80902 - both match the printed figures. (i) The level sum IS geometric with ratio
K^{-1/2}: section 5's forcing term scales as sqrt(s) with s -> s/K per level, and the member
count per level is constant (two chains) under REF1's brute-forced 1 + 2J count, not 2^j. (ii)
Section 5 does NOT reintroduce a per-level 2 - its display already carries coefficient 1 on
f(s/K), the multiplicity 2 once at the base, and the words "no branching factor exists"; what the
owed sentence supplies is the JUSTIFICATION of that display against the D = 0 members of the sup
(REF1's source-stratum structure), not a repair of it. Checked further that no OTHER constraint
caps c below 1/2: the base tilt l^{c(xi-1)} and the tilt sum both IMPROVE as c grows, and the
localization validity floor wants the base scale larger - the 0.12 cap's sole source was the
coefficient-2 reading, as 7.1 asserts. TWO FLAGS, not defects: section 5's parenthetical
"(c <= 0.12)" and 7.1's "c is currently capped at 0.12" become STALE the moment v3 adopts the
stratified base case - update both prints alongside that adoption; and the sharpened localization
of the literal reading's failure (its LEVEL sum already converges at ratio 2/sqrt(5) = 0.894; only
the base term ever broke) is worth one sentence in v3 so the repair's target is named. l_0 ~ 1e18
at c = 0.5 stands as derived, on 7.1's own table.]
