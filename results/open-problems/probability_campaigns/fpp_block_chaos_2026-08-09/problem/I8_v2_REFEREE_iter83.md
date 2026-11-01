# Referee report on I8_from_curvature_v2_iter82.md (hostile pass, iter 83)

VERDICT: MAJOR REVISION - the mathematics survives, the document does not. Every displayed
bound re-derived below either holds as printed or holds with a smaller constant by a simpler
argument; no exponent moves; the conclusion A_+(l) = O(sqrt(l) (log l)^{max(1,2/theta)}) stands
on the stated inputs ONCE THE HYPOTHESES ARE RESTATED. But the consolidation commits exactly the
class of error a consolidation referee exists to catch, four times:

  (D1, worst) The consequence chain of section 1 states "the corner threshold is alpha > 1/3:
      package-relatively, the program assembles exactly for chi in (1/3, 1/2)" while the
      document's own hypothesis ledger omits I3 (confined-time upper concentration at the wall,
      status in the refereed corner note: "NO OBSTRUCTION IDENTIFIED", not proved, not published).
      The corner note's banner conditions the threshold on "I8, I3, and the standing hypothesis
      set"; v2 carries I8 (it proves it) and gestures at the standing set ("package-relatively")
      but I3 is dropped BETWEEN the two. (P-conc) as listed covers FREE passage times only - it is
      precisely not I3. A one-ledger document whose main consequence silently consumes an
      unlisted open input is a strengthened claim, i.e. a consolidation error, i.e. the thing the
      banner promises did not happen ("nothing here is new relative to its sources").
  (D2) Sections 3-4 price GEOM by the referee's slope lemma at tilted-base second differences
      with the fixed-point ratio t/eta <= C_K - 1 = 2.02 - but that lemma-and-ratio pair belongs
      to the iter-74 referee's ON-CHORD TREE construction, which v2 does not build. v2's own
      section-2 chain (vertical waypoints at depth d(s), Part 3's architecture) produces NO
      centered second difference at a tilted base; its GEOM is a K-point Jensen gap whose honest
      bound consumes (H-curv) only at BASE TILT ZERO plus monotonicity - no slope lemma, no ratio,
      no fixed point (section T1/B below, with the two-line proof). The "hinge" of the document is
      wired to the wrong construction; the claim "t obeys the fixed-point recursion below" is
      never discharged (no recursion for t is stated anywhere in v2, and in the path architecture
      none exists - nothing compounds).
  (D3) (H-wand) is scoped to "pairs in the recursion's class". The recursion's class (section 2)
      is the ANCHORED pairs - whose free-geodesic wandering the argument never once consumes. The
      pairs whose wandering IS consumed (bulk and far segments, both endpoints off the wall) are
      not in the class. As printed the theorem's hypothesis does not support its proof. The
      sources scoped it correctly ("uniformly over the arc and the class", addendum A.1; bulk
      pairs in sketch (2.1)). One-line repair, but as printed the STATEMENT is defective.
  (D4) The honesty clause attached to (H-wand) is wrong in both directions at once (section T4:
      Newman-Piza's printed curvature condition is ONE-sided - an enclosing ball, re-derived from
      the paper itself below - so "two-sided" overstates the pedigree; and no published route to
      the stretched-exponential TAIL FORM exists at all per the prior referee's attack G and the
      iter-80 search, a caveat v2 dropped).

Conventions: as in the sources. H = {x >= 0}, points (x, y) = (depth, height), g the norm,
u(s) := g((s,1)), W_r = r^xi, sigma = (A log l)^{1/theta}, l the global top scale. DERIVED means
re-derived by me from scratch for this report; READ means taken from the named file. Numbers used
throughout: K = 5, xi = 3/4: K^{xi-1} = 5^{-1/4} = 0.66874, C_K := 1/(1-K^{xi-1}) = 3.0188,
C_K - 1 = 2.0188, K^{1-xi} = 1.49535, K^xi = 3.34370, 2^xi = 1.68179.

--------------------------------------------------------------------------------------------------
## T1. The slope lemma (v2 section 4): the lemma is SOUND, the wiring is NOT

(a) Internal re-derivation (DERIVED, all steps). For u convex and even with u(s) - u(0) <= c_+ s^2
on |s| <= delta:
  - u'_+(s) <= [u(2s) - u(s)]/s for s > 0 (convexity: right derivative <= forward chord slope);
    [u(2s) - u(s)]/s <= [u(0) + 4 c_+ s^2 - u(s)]/s <= 4 c_+ s, using u(s) >= u(0) (evenness +
    convexity put the minimum at 0). VALID ONLY FOR 2s <= delta - the lemma needs the RANGE
    CONDITION 2(t + eta) <= delta, which v2 never states. Harmless here (all tilts are o(1)), but
    a statement of the lemma without its range is not a statement of the lemma.
  - Corners: convexity gives one-sided derivatives everywhere and countably many corners; write
    u(t+eta) + u(t-eta) - 2u(t) = int_0^eta [u'_+(t+x) - u'_-(t-x)] dx (absolutely continuous
    representation of a convex function; integrand defined a.e. and nondecreasing in x). The
    integrand is bounded by its value near x = eta, so the second difference is
    <= eta [u'_+(t+eta) - u'_-(t-eta)]. No differentiability is consumed. THE LEMMA SURVIVES
    CORNERS - v2's target question (its section 6 asks this) has answer yes, PROVIDED the display
    is read with one-sided derivatives; as printed ("u'(s)") it presumes a derivative that
    convexity does not supply. Cosmetic repair.
  - The two-regime bound: if t >= eta, -u'_-(t-eta) <= 0 (u nondecreasing on [0, delta]), bracket
    <= 4 c_+ (t + eta). If t < eta, u'_-(t-eta) = -u'_+(eta-t) >= -4 c_+ (eta - t) (evenness),
    bracket <= 4 c_+ (t + eta) + 4 c_+ (eta - t) = 8 c_+ eta. Both cases <= 4 c_+ (t + 2 eta).
    Hence second difference <= 4 c_+ eta (t + 2 eta). CHECKS, and note it holds for ALL t, eta
    in range - the ratio condition is only needed to make the RHS quadratic in eta.
  - Constant chase: with t/eta <= C_K - 1 = 2.0188: 4 (2.0188 + 2) = 16.075 <= 17. The printed
    "17 c_+ eta^2" and the "2.02 + 2" slack CHECK as arithmetic. (v2's phrasing "with t/eta <=
    2.02 + 2" garbles the roles - the HYPOTHESIS is t/eta <= 2.02, the 2 is the increment's own
    contribution; as printed it reads as a hypothesis t/eta <= 4.02, which would give 4 x 6.02 =
    24.1 > 17 and make the display FALSE. The intended reading is recoverable from the referee
    report; the printed one is wrong. Fix the sentence.)

(b) THE WIRING DEFECT (DERIVED - this is the report's main mathematical finding). Where does v2's
own construction produce a second difference at base tilt t with t/eta <= 2.02? Answer: NOWHERE.
Take v2's section-2 step at scale s on a class pair (0,0) -> (D, s'), D = d(K s'): waypoints
w_0 = (0,0), w_j = (d(s), j s'/K), w_K = (D, s'). The K chords are (d(s), s'/K), (0, s'/K) x
(K-2), (D - d(s), s'/K), summing vectorially to (D, s') (telescoping CHECKS). By homogeneity
(K g(C/K) = g(C)) with m := s'/K:

    GEOM = m [ u(a) + (K-2) u(0) + u(K tau - a) - K u(tau) ],   a := d(s)/m,  tau := D/s'.

This is a K-POINT JENSEN GAP, not the centered second difference u(t+eta)+u(t-eta)-2u(t) of the
referee's attack B. The referee's exact-second-difference identity was derived FOR THE ON-CHORD
CHAIN w_j = (D j/K + d', j r/K) (report iter74 section 2, first display), i.e. for the TREE
architecture the same report then repaired and Part 3 SUPERSEDED. v2 copied the pricing of one
architecture onto the construction of the other. Two consequences:
  (i) Section 3's display "GEOM = [second-difference expressions in the profile u at base tilts
      <= t(s)]" is FALSE for the printed chords. The citation "referee attack B" does not cover
      the object it is attached to (attack B's no-leak theorem is for the on-chord chain).
  (ii) The good news the document misses: for ITS chain the slope lemma is UNNECESSARY. DERIVED
      bound, two lines, consuming (H-curv) at BASE ZERO only plus convexity/evenness:
          GEOM = [g((d(s), m)) - g((0, m))] + [g((D - d(s), m)) - g((0, m))]
                 + [g((0, s')) - g((D, s'))]
      (algebraic identity, using K g((0,m)) = g((0,s'))). Third bracket <= 0 (x -> g((x,y))
      even and convex, hence nondecreasing in |x|). Each of the first two is m [u(z) - u(0)]
      <= c_+ z^2 m with z = d(s)/m resp. (D - d(s))/m - first differences CENTERED AT e_2, the
      only place (H-curv) pins anything. Total:
          GEOM <= c_+ K [ d(s)^2 + (D - d(s))^2 ] / s' <= 2 c_+ K sigma^2 s^{2 xi - 1},
      which is STRONGER than v2's printed C c_+ sigma^2 K^{1+2xi} s^{2xi-1} (factor K^{2xi}
      better) and immune to the 3b counterexample by construction: no tilted-base second
      difference is ever formed, so corners accumulating at e_2 have nothing to bite. This is
      Part 3's own GEOM route (READ: Part 3 "GEOM for the class" paragraph), which v2 abandoned
      for the referee's lemma - the consolidation attached the right conclusion to the wrong
      source. The slope lemma should be kept as a REMARK (it is what one needs if one ever
      recurses the on-chord chain), not as the hinge.
  (iii) The fixed-point romance "one lemma, two jobs" is empty in this architecture: v2's class
      has EXACT far-depth (a deterministic function of separation), so nothing compounds, no
      fixed point stabilizes anything, and the only legitimate appearance of C_K = 3.019 in the
      whole v2 argument is as the geometric-series constant sum_j K^{(xi-1) j} = C_K in the
      tilt-sum bound (T3 below). Even on the most charitable literal reading - run the on-chord
      chain on v2's class to make section 4's object exist - the base-tilt-over-increment is
      t/eta = tau / (K d'(s')/s') = K^{xi-1} = 0.669, NOT 2.02: the 2.02 is the worst case over
      the iter-74 referee's WINDOW class, which v2 does not use (C2 below). Printed as "= 2.02
      at EVERY level", it is false in both readings; as an upper bound it is safe (0.669 <= 2.02,
      and 4(0.669 + 2) = 10.7 <= 17).

T1 verdict: lemma internally correct (add the range condition, fix "u'" to one-sided, fix the
"2.02 + 2" sentence); its ROLE in the document is a consolidation error; repair = replace the
GEOM pricing by the two-line centered bound above (cost: none; constants improve).

--------------------------------------------------------------------------------------------------
## T2. The A = 2 touching account across both spines (DERIVED)

(a) The count. Full-plane-priced segments: root chain contributes K-2 (its two end children are
anchored); each of the 2 spines contributes K-1 per level (K-2 bulk + 1 far child) over
J = (1-c) log_K l levels down to s0 = l^c. Total N = 2(K-1)(1-c) log_K l + (K-2) = O(K log_K l).
v2's "O(K log_K l) spine segments" CHECKS (the constant 2 for the spines is inside the O, but
after iter 74's 2^J fiasco the factor 2 should be PRINTED, not absorbed - that is what "check the
account across BOTH spines" was for).

(b) The form. Per segment: E[T_+ 1(touch)] <= crude x P(touch), crude = b x (l1 staircase length)
= b(chord height + |depth offset|). v2 prints "b(s/K + depths)" - the SOUND form; the iter-74
referee's flagged overcount b(b/a)(l/K + 2d) is NOT inherited. CHECKS. (The decomposition
E T_+ <= E[T 1(no touch)] + crude P(touch) <= E T + crude P(touch) is sound; READ iter74 sec 4,
re-checked.) Waypoint lattice-rounding (O(b) per waypoint, O(K log l) total) was in the iter-74
minors and is DROPPED from v2 - reinstate one clause.

(c) The probability, and a real constant bug. v2's (H-wand) states the tail as
P(dev >= sigma W_r) <= C exp(-c sigma^theta) WITH a constant c. Then sigma = (A log l)^{1/theta}
gives P(touch) <= C l^{-cA}, and the total is O(K log l) x b O(l) x C l^{-cA} = O(l^{1-cA} log l):
o(1) iff cA > 1. v2's reconciliation banner ("A > 1 suffices for the spine; A = 2 taken
uniformly") SILENTLY SETS c = 1. Against its own hypothesis as printed, A = 2 delivers nothing
when c <= 1/2. The iter-74 report normalized c into sigma (its section 4 writes exp(-sigma^theta)
barefaced); v2 reinstated the c in the hypothesis but kept the c-free arithmetic - a
reconciliation error in a document whose banner claims "reconciled constants". REPAIR (free):
define sigma := ((A/c) log l)^{1/theta}, or state A >= 2/c. Cost: the polylog constant only.
Also: at A = 2 the total is O(K log l / l) = o(1) with room; the banner's history line "the
referee's tree accounting needed A >= 2 over O(2^J K) segments" is slack as READ from iter 74
(l^2 x l^{-A} = o(1) needs A > 2 strictly; irrelevant, the tree is dead).

(d) The depth actually clears the quantile - but NOT by K^xi. v2 defines d(r) := sigma W_{r/K}.
Bulk and far segments at level scale s have chord separation m = s'/K, own-scale quantile
sigma W_{s'/K}; their depth is d(s) = sigma W_{s/K}. Clearance ratio = (s/s')^xi in [1, 2^xi] =
[1, 1.68], and = 1 EXACTLY on the instantiated recursion (s' = s always, see C2). v2's printed
"Depth-over-own-wandering = K^xi" (bulk line) and "clears its scale's wandering by K^xi" (far
child line) are FALSE under v2's own d(r). They are TRUE in Part 3's normalization d(m) =
c_theta m^xi (log l)^{1/theta}, where the dive is K^xi deeper. v2 changed the normalization to
the iter-74 referee's (d = quantile at CHORD scale) and kept Part 3's clearance prose - a
consolidation error. CONSEQUENCE: none for validity (the pricing needs clearance >= 1, i.e.
depth >= the sigma-quantile at own scale, which holds with equality; P(touch) <= C l^{-cA}
regardless), but the advertised K^xi SAFETY MARGIN DOES NOT EXIST in v2's construction. Fix the
two sentences or revert to Part 3's d.

T2 verdict: count and form CHECK; total o(1) CHECKS at A = 2 modulo the c-bug (free repair);
two false clearance claims (safe direction); one dropped minor (rounding).

--------------------------------------------------------------------------------------------------
## T3. Base-case multiplicity and the tilt sum (DERIVED)

(a) Stopped term WITH the factor 2. f(s0) <= sup E T_+ - g(chord) <= b(s0 + D(s0)) - 0 <=
b s0 (1 + o(1)) <= 2 b s0 (staircase inside H; D(s0) = sigma W_{s0} = o(s0) since sigma s0^{xi-1}
= o(1) at s0 = l^c, c > 0). Two spines: stopped contribution 2 f(s0) <= 4 b l^c. Against the
budget sqrt(l): o(sqrt(l)) iff c < 1/2. At c = 0.12 the room is l^{0.38} - enormous. CHECKS with
multiplicity 2. NOTE: c <= 0.12 is a TREE-ERA RELIC (it was forced by 2^J = (l/r0)^{0.431}
compounding, iter73 6.1); in the path architecture ANY c < 1/2 works (READ iter74 1(c), which
says exactly this). v2 printing "c <= 0.12" is safe but unexplained slack - one clause should say
the constraint is now only c in (0, 1/2).

(b) Tilt-sum bound with the fixed-point constants. Class tilts at scale r_j = l/K^j are
tau_j = D/s' = sigma r_j^{xi-1} (v2's d; deterministic, nothing compounds). The chord-level
increments a_j = K^{1-xi} sigma r_j^{xi-1} are larger by 1.495. Sum over levels of r_j^{xi-1}
from l down to l^c: geometric with ratio K^{1-xi} = 1.495 INCREASING downward, dominated by the
smallest scale: sum = sigma l^{c(xi-1)} x sum_{i>=0} K^{(xi-1) i} = C_K sigma l^{-c(1-xi)} =
3.019 x (A log l)^{1/theta} x l^{-0.03} at c = 0.12, xi = 3/4 -> 0. v2's claim (dominated by
smallest running scale, o(1)) CHECKS, and this geometric-sum constant is the ONLY honest job
C_K has in the whole document (T1(b)(iii)). Two footnotes: (i) the o(1) is SLOW - at theta = 0.5
and l = 10^6, (2 ln l)^2 x l^{-0.03} = 505, so nothing here is effective at finite scales;
asymptotic-only, as everywhere in this program; (ii) in the path architecture the SUM is not
load-bearing at all - only the MAX tilt (at the base) must clear (H-curv)'s delta-window and
(H-wand)'s o(1) arc, and the max is sigma K^{1-xi} l^{-c(1-xi)} = o(1) directly. The sum bound is
another tree relic, true but idle. v2's prefactor "C K^{1+xi}" is an overcount of the actual
K^{1-xi} increments under its own d (safe direction, inherited from Part 3's normalization -
same mismatch as T2(d)).

T3 verdict: arithmetic CHECKS including the factor 2; exponent room 0.38 at the printed c; both
"fixed-point constants" appearances resolve to the geometric-series constant; printed prefactors
inherited from the other normalization (safe).

--------------------------------------------------------------------------------------------------
## T4. The (H-wand) honesty clause, checked against Newman-Piza's OWN printed hypothesis

The clause (v2 section 1): "every published route to such bounds conditions on two-sided ARC
curvature around the direction". Checked against the source paper itself - Newman-Piza, Ann.
Probab. 23 (1995), fetched and read this session (sites.math.duke.edu/~rtd/FPP/Newman_Piza.pdf,
pp. 986-987). Their definition, verbatim in substance: x is a DIRECTION OF CURVATURE for B_0 iff
there is a closed Euclidean ball D of finite positive radius with (Condition 1') the sphere
boundary S_D contains z = x/mu(x), and (Condition 2') D contains B_0. That is an ENCLOSING ball:
B_0 inside D, touching at z. In norm terms it is EXACTLY the arc-LOWER gap h(phi) - h(0) >=
c_- phi^2 near the tangent direction (shape inside an osculating-or-larger ball = boundary falls
away from the tangent plane at least quadratically = time constant exceeds the tangent-plane
linearization at least quadratically). ONE-SIDED. No inscribed ball, no upper pinning of the gap,
appears anywhere in the definition or in Theorems 6-7. What their xi_x <= 3/4 consumes
(their (2.27)): the direction-of-curvature condition, plus E exp(beta tau(e)) < infinity (bounded
weights qualify), plus the UNCONDITIONAL chi' <= 1/2 of Kesten/Alexander. No geodesic uniqueness,
no unbounded support, no second side of the gap. (READ from the fetched paper; the norm-gap
translation is DERIVED but immediate.)

Consequences for the clause, both directions:
  (a) TOO PESSIMISTIC on sidedness: the flagship published route conditions on the arc-LOWER gap
      only. The hypothesis ledger therefore IMPROVES: (H-curv) is upper-at-a-point (consumed by
      GEOM), the wandering pedigree is lower-on-an-arc (consumed inside (H-wand)); the two are
      complementary one-sided conditions, and NOTHING in the v2 package needs the two-sided pin
      at any single direction. "Two-sided" was READ from iter74 section 3c, which itself hedged
      ("including the LOWER side ... two-sided in the published proofs") without a citation
      check; v2 hardened the hedge into a universal. The universal is false at its flagship
      instance.
  (b) TOO OPTIMISTIC on pedigree existence: Newman-Piza (and LNP) prove EXPONENT statements
      (xi_x <= 3/4 via xi <= (1+chi')/2, an a.s. shape-sandwich argument), NOT the
      stretched-exponential tail P(dev >= sigma W_r) <= C exp(-c sigma^theta) at every scale and
      every o(1) tilt that (H-wand) asserts and the touching account consumes at sigma =
      polylog quantiles. The iter-74 referee said this exactly (attack G: the tail form "must be
      quoted from a specific source or proved in an appendix - it remains open"; his closing
      line: could not verify the published form of the wandering tail, "left as the sketch's G3,
      now flagged as load-bearing at every level"). v2 DROPPED G3's citation gap entirely -
      "every published route to such bounds" presupposes published routes to SUCH BOUNDS exist,
      which no source document claims and the iter-74 report denies. Assuming the tail as a
      named hypothesis is legitimate; describing its pedigree as published-modulo-arc-curvature
      is not.
REPAIR (one paragraph): "(H-wand)'s pedigree: the published exponent bounds (NP/LNP) consume a
ONE-SIDED enclosing-ball arc condition (norm-gap lower bound on an arc) plus unconditional
inputs; the tail FORM used here has no located published statement (G3, open as a citation) and
its standard derivation consumes that same arc-lower condition plus (P-Alex) and (P-conc)." Note
this repair also gives (P-conc) its only job in the document - as printed, (P-conc) is consumed
NOWHERE in sections 2-5 (the touching bound is crude x tail, GEOM is deterministic, means are
(P-Alex)); it enters only through (H-wand)'s pedigree, and the theorem statement should say so
or drop it.

T4 verdict: the clause is false as a universal, in the pessimistic direction on curvature
(ledger improves: arc-LOWER, not two-sided) and in the optimistic direction on the tail form
(G3's citation gap must be reinstated). The clause's structural point - arc curvature enters
through (H-wand), not as a separate assumption - SURVIVES.

--------------------------------------------------------------------------------------------------
## C1. Line-up of v2 claims against strongest sources (consolidation sweep)

Format: v2 claim | strongest source | verdict.
 1. "A_+(l) = O(sqrt(l)(log l)^{max(1,2/theta)})" | iter74 R2 / addendum A.3 | MATCHES.
 2. Statement's "P2 <= MEANGAP <= A_+" | C1 note Claims 5/6, F2 | MATCHES (P2 = MEANGAP - Part1,
    Part1 >= 0; A_+ = MEANGAP + A, A >= 0). DERIVED, checks.
 3. "corner threshold alpha > 1/3 ... assembles exactly for chi in (1/3,1/2)" | C1 note banner:
    conditional on "I8, I3, and the standing hypothesis set"; ledger 15/16 phrasing | STRONGER
    THAN SOURCE: I3 dropped (D1, and C3 below). The "package-relatively ...exactly... (1/3,1/2)"
    phrasing itself MATCHES the refereed ledger-15 form (open at the top, package-relative).
 4. "(H-curv) ... Equivalent at e_2 to MG2A's H2 upper half, constant C = c_+ + g(e_2)/2 + o(1)"
    | iter74 3a | GARBLED SYMBOLS: in iter74, c_+ is the ANGULAR (H2) constant and C the profile
    constant; v2 renames the PROFILE constant c_+ and then reprints the iter74 formula, making it
    read C = c_+ + g(e_2)/2 with both symbols apparently the same object. The correct statements:
    profile-from-angular C_prof = c_+^{H2} + g(e_2)/2 + o(1); angular-from-profile c_+^{H2} =
    c_+^{prof} - g(e_2)/2 + o(1) (h(phi) = u(s)/sqrt(1+s^2), s = tan phi; DERIVED). As printed it
    is circular. Cosmetic but real; fix the sentence.
 5. "consumes it at tilted bases only through the slope lemma ... NOTHING two-sided" | iter74 3b |
    "nothing two-sided" MATCHES; "at tilted bases through the slope lemma" is the WRONG-
    ARCHITECTURE wiring (T1(b)): its own chain consumes (H-curv) at base ZERO only.
 6. "Exact telescoping (waypoints ON the chain, no leak - referee attack B)" | iter74 sec 2 |
    MISATTRIBUTED: attack B's no-leak identity is for the on-chord chain. The vector telescoping
    of v2's chords CHECKS (derived in T1(b)), and no leak exists - but by the T1(b) argument, not
    by attack B. Same conclusion, wrong authority.
 7. "Depth-over-own-wandering = K^xi" (twice) | Part 3 | FALSE under v2's own d(r) (T2(d));
    true only in Part 3's normalization, which v2 abandoned.
 8. "the class tilt fixed point evaluates to C_K ... t/eta <= C_K - 1 = 2.02 at EVERY level"
    | iter74 secs 1(b), 3b | belongs to the iter74 WINDOW class + on-chord chain; v2's exact
    class has no fixed point and (charitably) ratio 0.669 (T1(b)(iii)). FALSE as printed, safe
    as a bound.
 9. "found twice independently - addendum Part 3 and referee report section 1" | both | The
    ARCHITECTURAL move (far child re-typed bulk, branching 1) was indeed found twice - MATCHES.
    But v2 extends the convergence to the fixed-point CONSTANT, which exists only on the referee
    side. Half-true; state the convergence as the re-typing only.
10. Touching crude "b(s/K + depths)" | iter74 sec 4 minor | MATCHES the sound form (overcount
    not inherited). GOOD.
11. "A = 2 ... costs only the polylog constant" | iter74 sec 4 (c normalized away) vs v2's own
    (H-wand) with c | INCONSISTENT with its own hypothesis (T2(c)); free repair.
12. "(P-Alex) ... published, unconditional" | iter74 attack G(iii) | iter74 carried "citation-
    level check owed at write-up (bounded weights vs moment condition)"; v2 DROPPED the caveat.
    Reinstate one clause.
13. "no unconditional sublinear wandering exponent exists (search receipt: LOG iter 80)" |
    ledger 17 | MATCHES.
14. Section 6's four named targets for the next referee | - | MATCH the real weak points except
    that none of them names D1 (the I3 drop) - the document aimed its referee at its constants
    and away from its consequence chain. Noted.
15. Banner "Nothing here is new relative to its sources" | - | FALSE in at least four places:
    the d(r) normalization switch (T2(d)), the A=2-with-c arithmetic (T2(c)), the class
    restatement without the {0} far-depth branch and without the window (C2), and the I3-free
    consequence sentence (C3). Each is a silent edit with content.

--------------------------------------------------------------------------------------------------
## C2. Three documents, three classes (DERIVED comparison)

  iter74 referee: F(r) = anchored pairs at separation r, far-depth D in {0} U [sigma W_{r/K},
      C_K sigma W_r], tilt <= C_K sigma W_r / r. A WINDOW class, built for the on-chord chain
      whose anchor child inherits D/K + d' - the window is what the fixed point stabilizes.
  Part 3: far-depth EXACTLY D = d(K s'), d(m) = c_theta m^xi (log l)^{1/theta}, so D =
      K^xi sigma W_{s'} = 3.344 sigma W_{s'}. NOTE: this sits ABOVE the iter74 window top
      C_K sigma W_{s'} = 3.019 sigma W_{s'}. Part 3's class is NOT contained in the referee's.
  v2: far-depth EXACTLY D = d(K s') with d(r) := sigma W_{r/K}, so D = sigma W_{s'} - INSIDE the
      iter74 window, a factor K^xi SHALLOWER than Part 3's.
Three pairwise-distinct classes. v2's sentence attributing its class's stability to "the class
tilt fixed point ... 3.019" is therefore doubly unmoored: its class is not the referee's (no
window, nothing to stabilize) and not Part 3's (depths differ by K^xi).

DOES V2'S STEP CLOSE? As printed, NO - a real defect, then a real repair:
  - The class admits s' in [s/2, s]. The step dives to d(s) (CLASS-scale indexed). Child 0 =
    (0, y) -> (d(s), y + s'/K) has separation s'/K and far-depth d(s); membership in P(s/K)
    requires far-depth EXACTLY d(K s'/K) = d(s'). d(s) = d(s') iff s' = s. v2's printed equation
    "far-depth d(s) = d(K s'/K)" is FALSE for every s' < s. An exact-far-depth class with a
    separation WINDOW cannot be step-stable under a class-scale-indexed dive.
  - What saves the instantiated argument: the recursion NEVER VISITS s' < s. Root separation l;
    every chain divides separation by exactly K; so every instantiated member has s' = s = l/K^j
    exactly, where the closure is EXACT (including the root's children: far-depth d(l) =
    d(K x l/K), on the nose). The [s/2, s] window is inert decoration inherited from the
    sources' generality.
  - REPAIRS (either, one line): (i) fix separation = scale (drop the window; the honest class is
    a SEQUENCE of pairs, one per level); or (ii) keep the window and dive to d(s') (pair-indexed),
    restoring exact closure at every s'. Cost: none; T2/T3 arithmetic unchanged up to the
    [1, 2^xi] factors already tracked.
  - Also: both the iter74 class ({0} branch) and Part 3 ("TOP LEVEL ONLY" clause) make explicit
    room for the root's far-depth 0; v2's class as printed EXCLUDES the root pair, which v2 then
    handles inline as a special step outside its own class. Legitimate (C4), but the {0} branch
    or Part 3's TOP-LEVEL clause should be restored so the class contains its own root.

## C3. The consequence chain of section 1 (the worst defect, in full)

The chain has four links. (1) A_+ bound => sqrt-polylog MEANGAP: CHECKS (C1 item 2), uniformity
over wall pairs by e_2-translation invariance, evaluation at R = 5(b/a)h legitimate since the
bound is uniform in l. (2) "I8 of the salvaged corner note holds": the note's I8 is
P2 <= C sqrt(l) log l; v2 delivers (log l)^{max(1,2/theta)}. The note's consumption (section 7,
gamma = 1/2 with strict exponent inequalities and eps-slack) absorbs any polylog - CHECKS, but
the sentence should say "I8 at polylog strength", not "I8". (3) "the corner threshold is
alpha > 1/3": the refereed corner note delivers this CONDITIONAL ON I8 + I3 + ITS OWN STANDING
SET. I3 (upper concentration at Kesten scale for the CONFINED time T_+ at wall pairs, feeding
S_+(R) in the note's section 3 cost formula) is: not published; downgraded by the corner referee
from "verified in mechanism" to "NO OBSTRUCTION IDENTIFIED" (ledger 16, note I3 annotation);
and ABSENT from v2 - the word I3 does not occur in the document, and (P-conc) explicitly covers
FREE times only. A reader of v2 alone would conclude that (H-curv) + (H-wand) + two published
inputs buy the alpha > 1/3 threshold. They do not; they buy I8. (4) "package-relatively,
assembles exactly for chi in (1/3, 1/2)": phrasing MATCHES ledger 15's refereed form, and
"package-relatively" legitimately carries the H1-H4/CH standing set - but not I3, which is the
corner note's own extra input, inside no package.

REQUIRED REPAIR (wording, zero mathematics): add to the hypothesis roster a line "(H-conf) = the
corner note's I3: Kesten-scale upper concentration for T_+ at wall pairs - status: no obstruction
identified, unproved", and rewrite the consequence as "hence I8 ...; combined with the corner
note's refereed chain (which additionally consumes I3 and its standing set) the corner threshold
is alpha > 1/3, package-relatively ...". Until that line exists, the theorem-statement of v2 is
STRONGER THAN ITS SOURCES SUPPORT and must not be exported (ledger 21b already gates export on
this report; the gate held).

## C4. The root step (D = 0) is legitimate (DERIVED)

Root chain on (0,0) -> (0,l): w_0 = (0,0), w_j = (d(l), j l/K), w_K = (0, l).
  - Children: j = 0 gives (0,0) -> (d(l), l/K): anchored, separation l/K, far-depth d(l) =
    d(K x l/K) - in class EXACTLY. j = K-1 gives (d(l), (K-1)l/K) -> (0, l): the REVERSED
    anchored pair; class membership needs the class closed under e_2-translation AND y-reflection
    - the iter74 minors required exactly this closure and v2 dropped the clause. Reinstate.
    Two spines thereafter, branching 1: CHECKS.
  - Root bulk children: depth d(l) = sigma W_{l/K}, separation l/K: at their own quantile,
    clearance 1 (not K^xi - T2(d) applies at the root too); P(touch) <= C l^{-cA}; fine.
  - Root GEOM with D = 0 (the question C4 asked): chords (d(l), l/K), (0, l/K) x (K-2),
    (-d(l), l/K); evenness folds the last onto the first:
        GEOM_root = 2 [ g((d(l), l/K)) - g((0, l/K)) ] <= 2 c_+ K d(l)^2 / l
                  = 2 c_+ sigma^2 K^{-1/2} sqrt(l)   at xi = 3/4.
    Two first differences at base e_2 - the sketch's ORIGINAL (2.3), which was always sound at
    the top level. CHECKS; sqrt-polylog; no slope lemma, no tilt, no fixed point.

--------------------------------------------------------------------------------------------------
## Summary of required revisions (all statement-level; no exponent moves anywhere)

R1 (D1, blocking): add (H-conf)/I3 to the hypothesis roster and re-scope the consequence
    sentence (C3). Until then the document's main claim overclaims relative to its sources.
R2 (D3, blocking): re-scope (H-wand) to the pairs actually priced (all pairs at separations in
    [s0/K, l/K] with tilt in the o(1) window, both endpoints at depth >= 0 in H - bulk and far
    segments included, one-sided deviation toward the wall sufficing), not "the recursion's
    class".
R3 (D2): replace the GEOM pricing by the centered two-line bound (T1(b)(ii)); demote the slope
    lemma to a remark with its range condition and one-sided derivatives; delete "t obeys the
    fixed-point recursion below", the "= 2.02 at every level" claim, and the "one lemma, two
    jobs" sentence; keep the 3b counterexample as the reason POINTWISE-UPPER-AT-e_2 suffices
    only because no tilted-base second difference is ever formed.
R4 (D4): rewrite the honesty clause per T4 (arc-LOWER enclosing-ball pedigree, one-sided;
    reinstate G3's missing-citation caveat; give (P-conc) its pedigree role or drop it).
R5 (C2): fix the class (drop the separation window or dive pair-indexed); restore the {0}
    far-depth branch or Part 3's TOP-LEVEL clause; fix the two K^xi clearance sentences and the
    A-vs-c constant (T2(c,d)); reinstate the two dropped iter74 minors (waypoint rounding,
    reflection closure) and the (P-Alex) citation-check caveat; fix the c_+ symbol collision
    (C1 item 4) and the "2.02 + 2" sentence (T1(a)).

WHAT SURVIVES UNCONDITIONALLY OF THIS PASS: the construction (two-spine dive, branching 1), the
telescoping, the touching account's form and total, the base arithmetic with multiplicity 2, the
root step, the conclusion A_+(l) = O(sqrt(l) (log l)^{max(1,2/theta)}) from (H-curv) +
(re-scoped H-wand) + (P-Alex), and - once R1 is applied - the downstream conditional chain in
its sources' own wording. The prize statement after this pass is SMALLER and CLEANER than v2's:
upper curvature at one point for the geometry, lower curvature on an arc inside the wandering
input's pedigree, nothing two-sided anywhere, I3 named.

(Hostile referee, iter 83. Every display in T1-T4/C2-C4 re-derived from scratch; READ/DERIVED
marked inline. Sources read in full: v2 iter82; sketch iter73 with banner; addendum Parts 1-3
with supersession tags; referee report iter74; C1 note iter60 banner + secs 5-8 + 6.5/6.6;
CRUX 3b resolved banner; MG2A section 2; ledger entries 15-21b; Newman-Piza 1995 pp. 977-987.)
