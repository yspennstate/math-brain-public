# Referee report 1 of 3: punctured-window step stability, two-child branching, dead band
# Object: problem/I8_from_curvature_v2_iter82.md, section 2 (CLASS + STEP), tags [V3.1], [V5-1].
# Method: everything below is re-derived from the definitions. I read the iter-74 and iter-94
# reports only after finishing my own derivation of items 1-3, and I flag every place where I
# reach a different or a new conclusion.

## 0. Definitions as I read them, and the one convention that generates the confusion

    W_r := r^xi,  xi <= 3/4          (wandering scale)
    sigma := (A log l / c)^{1/theta} (GLOBAL - no dependence on the running scale)
    d(r) := sigma W_{r/K} = sigma (r/K)^xi
    C_K := 1/(1 - K^{xi-1}),  K >= 5

CONVENTION WARNING (this is the single most confusion-generating definition in the document, and
it is the source of the [V5-3] K-power dispute): d is PRE-COMPOSED with one level of descent, so

    d(K s') = sigma W_{K s'/K} = sigma W_{s'} = sigma (s')^xi      NOT sigma (K s')^xi.

Every check below uses that reading. Numerically at K = 5, xi = 3/4:

    K^{xi-1} = 5^{-1/4} = 0.668740      C_K = 3.018782
    K^xi     = 3.343702                 2^xi = 1.681793      2^{1-xi} = 1.189207
    C_K K^xi = 10.09390                 (multiplicative WIDTH of the window band)

CLASS (per-member reading - the window edges as printed are written in the member's own height s'):

    P(s) := { (0,y) -> (D, y+s') : s' in [s/2, s],
              D in {0} u [ sigma W_{s'/K} , C_K d(K s') ] = {0} u [ d(s') , C_K sigma (s')^xi ] }

So the band is a fixed multiplicative window of width C_K K^xi = 10.09, plus the isolated point 0.

STEP at class scale s on a member of height s', far-depth D:
    w_0 = (0,0),  w_j = (d(s), j s'/K) for j = 1..K-1,  w_K = (D, s').
Note the waypoint depth is d(s) - the dive depth at the PARENT CLASS scale, NOT at the chord
scale. This is the "constant-depth" chain (iter-74's attack-B variant), not the on-chord chain.
Consequence, and it matters for everything below: the map D -> (child 0's far-depth) is a CONSTANT
map. It does not depend on D at all. Step stability is therefore not a fixed-point question in
this architecture; it is the question of whether one point lands in one interval.

--------------------------------------------------------------------------------------------------
##    bound on K is required, and (H-wand)'s printed depth range does not cover the deep end)

### 1.1 Height coordinate: exact, no drift
Child 0 and every bulk child has height s'/K. The class scale maps s -> s/K. Membership needs
s'/K in [(s/K)/2, s/K], i.e. s' in [s/2, s] - which is the parent's own hypothesis. The height
ratio s'/s in [1/2, 1] is reproduced EXACTLY, level after level. No accumulation. CONFIRMED.

### 1.2 The three edges of the window, checked exactly

Child 0 is (0,0) -> (d(s), s'/K): anchored, height s'' = s'/K, far-depth D'' = d(s) = sigma(s/K)^xi.
Its own window is  {0} u [ sigma (s''/K)^xi , C_K sigma (s'')^xi ]
                 = {0} u [ sigma (s'/K^2)^xi , C_K sigma (s'/K)^xi ].

  BOTTOM:  D''/bottom = ( (s/K) / (s'/K^2) )^xi = (K s/s')^xi in [K^xi, (2K)^xi] = [3.3437, 5.6234].
           Clears by a factor 3.34 at worst. Uses only s' <= s.
  TOP:     top/D'' = C_K (s'/s)^xi >= C_K 2^{-xi} = 3.018782/1.681793 = 1.79495.
           Clears by a factor 1.795 at worst (worst case s' = s/2).

Both hold for EVERY s' in [s/2, s]. So child 0 lands strictly inside the BAND - never at 0, never
in the hole. CONFIRMED.

  EDGE D = d(s') (bottom of the parent band). Child 0 unaffected (constant map). The far child
  (d(s), (K-1)s'/K) -> (D, s') has minimum chord clearance min(d(s), D) = D (since s >= s'
  gives d(s) >= d(s')), and D = d(s') = sigma W_{s'/K} = EXACTLY the deviation quantile at the far
  child's own scale s'/K. Tight, zero slack. This is what forces the bottom edge - see section 3.

  EDGE D = C_K d(K s') (top of the parent band). Child 0 unaffected. Far child: offset
  |D - d(s)| <= max(D, d(s)) = D (since D/d(s') <= C_K K^xi = 10.09 while d(s)/d(s') <= 2^xi = 1.68),
  so the minimum clearance is now d(s) = sigma (s/K)^xi >= sigma (s'/K)^xi = the quantile at the
  far child's own scale. Also clears, by (s/s')^xi in [1, 1.68].
  The top edge constrains ONLY child 0, through (s/s')^xi <= C_K - see 1.4.

  EDGE D = 0 (the puncture member). Child 0 as above. The far child is
  (d(s), (K-1)s'/K) -> (0, s'): its far end is ON the wall. Under the reflection (x,y) -> (x, s'-y)
  - a lattice symmetry preserving H = {x >= 0} and the iid law - it becomes (0,0) -> (d(s), s'/K),
  i.e. exactly child 0's type: anchored, far-depth d(s), height s'/K, hence in P(s/K). CONFIRMED.
  (This needs the class to be closed under e_2-translation AND under y-reflection. The document
  states neither; iter-74 listed both. One owed sentence, no cost.)

### 1.3 Slack tracking through one full step, and why it does not accumulate
At level j the recursing member has far-depth d(s_{j-1}) = sigma (s_j)^xi where s_j = s/K^j is its
own class scale, and height s'_j = s'_0/K^j in [s_j/2, s_j]. Its child's far-depth is
d(s_j) = sigma (s_{j+1})^xi. So at EVERY level the recursing far-depth sits at the same relative
position in its own window: 3.344x above the bottom edge, and between 1.795x and 3.019x below the
top edge. The slacks are level-independent because d, the window edges and the scale map are all
pure powers of the scale with the same global sigma - the far-depth map is a CONSTANT map, i.e. a
super-attracting fixed point, so one step erases all memory of D. There is no drift to track.
CONFIRMED, and this is a stronger statement than "stable": the class parameter is reset every step.

Lattice rounding (the waypoints j s'/K are not integers) perturbs each depth by O(1). Since
d(s) >= d(r_0) = sigma (l^{0.12}/5)^{3/4} = sigma l^{0.09}/3.34 >> 1, an O(1) perturbation is
negligible against the 1.795x / 3.344x slacks. The document never mentions rounding; iter-74 did
(O(b) per waypoint, O(K log_K l) total, absorbed in polylog). Owed sentence, no cost.

### 1.4 NEW FINDING - an unstated upper bound on K (the document prints only "Fix K >= 5")
The binding inequality in 1.2 (TOP) is, at the worst height s' = s/2,

    2^xi <= C_K = 1/(1 - K^{xi-1})   <=>   K^{1-xi} <= 1/(1 - 2^{-xi}).

At xi = 3/4 this reads K^{1/4} <= 1/(1 - 2^{-3/4}) = 1/0.405396 = 2.466727, i.e. K <= 37.024.
  K = 37: C_K = 1.681917 >= 2^{3/4} = 1.681793   PASSES (by 0.007%)
  K = 38: C_K = 1.674327 <  1.681793             FAILS
Uniformly over the hypothesis's whole range xi in (0, 3/4], the threshold K*(xi) =
[1/(1-2^{-xi})]^{1/(1-xi)} is minimised near xi = 0.37 at K* = 10.61:
  xi = 0.2 -> 12.88;  0.3 -> 10.91;  0.35 -> 10.61;  0.4 -> 10.63;  0.5 -> 11.66;  0.75 -> 37.02.
So the class as printed is step-stable for 5 <= K <= 10 for every xi <= 3/4, and up to K <= 37 if
xi = 3/4 exactly. For K >= 38 the recursing child's far-depth d(s) EXITS its own window at s' = s/2.
This is not hypothetical housekeeping: K is a free design parameter and one is tempted to raise it
(it improves the forcing ratio 1/sqrt(K) and, under the naive sup recursion of section 2 below,
the branching ratio 2/sqrt(K)).
REPAIR, free: either (a) print "5 <= K <= 10", or (b) widen the top edge to
max(C_K, 2^xi) d(K s'), or (c) read the window class-uniformly (edges in s, not s') - see 1.5.
Under (b) or (c) GEOM's C_K^2 is replaced by max(C_K, 2^xi)^2, which is never larger. No cost.
NOTE: this condition does not bite on the VISITED tree, where s' = s at every level up to lattice
rounding, so (s/s')^xi = 1 + O(1/s). It bites on the SUP the recursion is stated over. That is the
same structural pattern as finding 2.2 below, and it is exactly where a recursion must be airtight.

### 1.5 The reading ambiguity, and the good news that it is not load-bearing (except via 1.4)
The printed window edges use the member's own height s'. A class-uniform reading (edges in the
class scale s: {0} u [d(s), C_K sigma s^xi]) is also step-stable, and more cleanly: child 0's
far-depth d(s) then needs sigma(s/K)^xi >= sigma(s/K^2)^xi (clears by K^xi) and
sigma(s/K)^xi <= C_K sigma (s/K)^xi (clears by C_K >= 1, for ALL K). So under the class-uniform
reading finding 1.4 disappears. The document must say which reading it means; one sentence.

### 1.6 NEW FINDING - (H-wand)'s printed depth range does not cover the window's deep end
(H-wand) as re-scoped covers pairs with "endpoints at depths in [d(r)-range, d(K r)-range]". For a
child at scale r = s'/K that range is [sigma(s'/K^2)^xi, sigma(s'/K)^xi]. But the far child's
endpoints sit at depths d(s) (up to 1.68 x sigma(s'/K)^xi) and D (up to C_K K^xi = 10.09 x
sigma(s'/K)^xi). Both are ABOVE the printed upper end of the range - the window's own top edge is
10.09x the printed range's top. So the step again consumes (H-wand) outside its printed scope. This
is the SAME class of error as the [V2REF] statement-MAJOR, at the opposite end from the iter-92
dead band, and it has not been flagged before.
It is harmless in substance, because depth enters monotonically in the favourable direction: the
quantity actually needed is P(free geodesic exits H) <= P(wall-ward dev >= min clearance), and
min clearance >= sigma W_r at every priced pair (verified at all three edges in 1.2), so the
hypothesis is only ever used at inflation sigma. REPAIR, free: state (H-wand)'s scope as
"endpoints at depths >= sigma W_r, chord tilts o(1)" and delete the two-sided range.

### 1.7 Side quantities re-derived while checking the edges
- Class tilt, printed as "<= 2 C_K d(K s)/s": actual max tilt = D/s' <= C_K sigma (s')^{xi-1}
  <= C_K 2^{1-xi} sigma s^{xi-1} = 1.189 C_K sigma s^{xi-1}. Printed constant 2 C_K. VALID, slack
  1.68x. And it is o(1): at the smallest scale s = r_0 = l^{0.12} it is polylog x l^{-0.03} -> 0.
  (Slowly: at l = 10^6 with theta = 2 and c ~ 0.1 the number is still >> 1. Legitimate for an
  asymptotic theorem, but l_0 is astronomical. Same remark as iter-94 V2; not a defect.)
- Far child's chord tilt, printed as "<= K^{1+xi} s^{xi-1} polylog": actual
  <= K C_K sigma (s')^{xi-1} <= K C_K 2^{1-xi} sigma s^{xi-1} = 17.950 sigma s^{xi-1}, versus the
  printed K^{1+xi} = 5^{1.75} = 16.719. The printed CONSTANT is 7.36% short. Absorbed by any honest
  reading of "polylog" (sigma >> 1.074), so an arithmetic nit, not a defect - but it is a nit in
  the same direction as [V5-3]'s, i.e. reading K-powers off the wrong convention for d.
- Free cross-check of [V5-3] (not my item, but it shares the window's top edge): tight GEOM bracket
  = K[C_K^2 + 2^{2xi} K^{-2xi}] = 5[9.11305 + 0.253] = 46.830; printed K^{1+2xi} = 5^{2.5} = 55.902.
  Valid, 19.4% loose. At K = 4: tight = 4[11.65685 + 0.3536] = 48.04 versus printed 4^{2.5} = 32.
  FAILS at K = 4. [V5-3]'s reading and its K >= 5 caveat are CONFIRMED independently.
- GEOM at a D = 0 member: the chain telescopes to
  g((d(s),s'/K)) + g((-d(s),s'/K)) + (K-2)g((0,s'/K)) - g((0,s')) = 2[g((d(s),s'/K)) - g((0,s'/K))]
  exactly (evenness in the depth coordinate + homogeneity K g((0,s'/K)) = g((0,s'))). So the
  puncture member's GEOM is an EXACT identity, needs no dropped term, and is bounded by
  2 C c_+ d(s)^2 K/s'. Against a band member's [d(s)^2 + (C_K d(K s'))^2] K/s' at s' = s, the
  ratio is (K^{-2xi} + C_K^2)/(2 K^{-2xi}) = (0.0894 + 9.113)/0.1789 = 51.4. The two-child step at
  the puncture is ~50x CHEAPER in GEOM than an ordinary band step - it is the cheapest step in the
  tree, not the dangerous one.

--------------------------------------------------------------------------------------------------
## 2. TWO-CHILD STEP AT D = 0 AND CONTRACTIVE BRANCHING - verdict CONFIRMED
##    (the claim is true; the document does not contain its proof - one missing sentence)

### 2.1 The derived fact that makes the claim true: the puncture is a SOURCE, never a TARGET
Split the class into its two strata, P_0(s) := {D = 0} and P_+(s) := {D in the band}. From 1.2:

  - a P_+ member's step produces ONE anchored child, far-depth d(s), which lies in the BAND at
    scale s/K (never 0, never in the hole);
  - a P_0 member's step produces TWO anchored children, both of far-depth d(s), both in the BAND;
  - in neither case is a child's far-depth 0, because the far-depth map is the constant map
    D -> d(s) and d(s) = sigma (s/K)^xi > 0 always.

So with f_0(s) := sup over P_0(s) and f_+(s) := sup over P_+(s) of [E T_+ - g]:

    f_+(s) <= 1 . f_+(s/K) + F_+(s)          (K-2 bulk + 1 far-bulk + GEOM + touching)
    f_0(s) <= 2 . f_+(s/K) + F_0(s)          (K-2 bulk + GEOM + touching)

f_0 NEVER appears on a right-hand side. The dependency graph is a path, not a tree: f_0 is
evaluated at the top scale l only, and f_+ is evaluated once per level. Hence

    f_+(l/K) <= sum over j>=1 of F_+(l/K^j) + f_+(r_0), ratio 1/sqrt(K) = 0.4472, sum factor 1.8090
    A_+(l) = f_0(l) <= 2 f_+(l/K) + F_0(l) = O(sqrt(l) polylog),  base multiplicity exactly 2.

This is section 5's arithmetic, and it is CORRECT - but only under this stratification. CONFIRMED.

### 2.2 What the document actually says, and why it is not yet a proof
Section 2 admits D = 0 "generally" at every scale and writes ONE symbol f over the whole class.
Read literally, f(s) := sup over P(s) obeys f(s) <= 2 f(s/K) + F(s) at EVERY level, because P(s)
contains a D = 0 member at every s. That is branching 2, and section 5's "ratio 1/sqrt(K) per
level" and "multiplicity 2" at the base are then both wrong. The missing sentence is exactly 2.1:
no member's child has far-depth 0, so the branching-2 stratum is entered at most once, at the root.
Owed, free, and load-bearing for section 5's arithmetic.

### 2.3 Does the literal (unstratified) reading survive anyway? Yes - but by 0.001 in the exponent
Unrolling f(s) <= 2 f(s/K) + C sqrt(s) L to the base r_0 = l^c:
  forcing:  sum over j of (2/sqrt K)^j C sqrt(l) L = 9.4721 C sqrt(l) L at K = 5 (versus 1.8090
            with branching 1) - a 5.2x constant, harmless;
  base:     2^J f(r_0) with J = (1-c) log_K l, so 2^J = l^{(1-c) log_5 2} = l^{0.4306766(1-c)}
            and f(r_0) <= C b r_0 = O(l^c). Total exponent 0.4306766 + 0.5693234 c.
            At c = 0.12: 0.3789954 + 0.12 = 0.4989954 < 0.5. Clears sqrt(l) by 0.001.
            Break-even: c = 0.0693234/0.5693234 = 0.1217647. c = 0.125 would NOT clear it.
So the document's stated c <= 0.12 (a vestige of the abandoned 2^J architecture) happens to cover
the literal reading with a margin of one part in five hundred of the exponent. That is not a place
to stand when 2.1 is available and exact. Report it as: claim CONFIRMED, proof owed, and do not
let anyone raise c without re-deriving this line.

### 2.4 Descendant count over j levels - explicit, and no 2^j anywhere in the visited tree
  anchored (recursing) members: level 0: 1 (the root, D = 0); level j >= 1: exactly 2.
                                total 1 + 2J.
  full-plane-priced segments:   root contributes K-2 (its other 2 children are anchored);
                                each stepping band member contributes (K-2) bulk + 1 far = K-1;
                                total (K-2) + 2(J-1)(K-1) with J = (1-c) log_K l
                                = O(K log_K l).   CONFIRMED, exactly as printed.

### 2.5 Free improvement to the touching account (and it kills the branching worry outright)
Section 3 bounds every segment's crude cost by the TOP-scale crude, then multiplies by the segment
count. Keeping the level dependence: crude at level j is <= b(s_j/K + depths) = O(b l/K^{j+1}),
and the number of segments at level j is at most 2^j (K-1). So
    total touching <= b l^{1-A} (K-1)/K . sum over j of (2/K)^j = O(b l^{1-A})   since 2/K = 0.4 < 1.
No J-dependence, no log, and A > 1 suffices EVEN under branching 2. Section 2's reconciliation
bracket ("the referee's tree accounting needed A >= 2 over O(2^J K) segments; the spine has only
O(K log_K l) segments, for which A > 1 suffices") is therefore over-conservative in both
directions: A > 1 suffices either way. A = 2 is taken, so nothing moves; noted for the record.

--------------------------------------------------------------------------------------------------
## 3. THE DEAD-BAND QUESTION - verdict CONFIRMED: the puncture is STILL NECESSARY
##    (and the necessity is architectural, not merely an estimate - stronger than iter-94's case)

I tested the hypothesis the brief asked me to entertain - that the v3 re-wiring (constant-depth
chain, retired slope lemma, first-difference GEOM) has made the puncture unnecessary. It has not,
and the reason is one level deeper than "the touching bound fails".

### 3.1 The architectural argument: no chain of any shape can price the dead band
Take ANY chain w_0 = (0,0), ..., w_m = (D, s') inside H. Its LAST segment ends at the pair's far
endpoint, at depth exactly D. That segment is priced in one of two ways:
  (a) as an ANCHORED member of the class, recursed - possible only if one of its endpoints is ON
      the wall. Its far endpoint is at depth D, so this requires D = 0 (and then the reflection
      (x,y) -> (x, s'-y) puts it in the class, per 1.2);
  (b) as BULK, full-plane priced - which costs crude x P(free geodesic exits H), and exit requires
      wall-ward deviation beyond the minimum chord clearance, which is at most D.
There is no third typing available: recursing an off-wall pair would need near-depth as a THIRD
class parameter and a chain construction from an off-wall near end, which this architecture does
not have (iter-74 said the same about the on-chord chain; it is a property of the class, not of
the chain). So the admissible far-depths are exactly

    D = 0            (last segment anchored by reflection), or
    D >= the deviation quantile of the last segment's own scale (last segment bulk-priceable).

That IS the punctured window. The hole is not an artefact of a particular chain or of a particular
estimate; it is the set of far-depths for which neither typing is available. CONFIRMED NECESSARY.

### 3.2 The bottom edge is not a choice either - it is forced, and it is tight
With the uniform K-chain the last segment has scale s'/K, whose deviation quantile at inflation
sigma is sigma W_{s'/K} = d(s') - EXACTLY the printed bottom edge. At D = d(s') the far child's
minimum clearance equals that quantile with ZERO slack (1.2, edge D = d(s')), so the touching bound
is (H-wand) at the child's own scale with no loss and no room. The window's bottom edge is
therefore derived, not chosen.

### 3.3 What breaks if (0, sigma W_{s'/K}) is admitted - with the arithmetic
Write a dead-band far-depth as D = rho sigma W_{s'/K}, rho in (0,1). Even GRANTING (H-wand) at that
pair (which the re-scoped hypothesis does not supply - it covers depths at the quantile and above),
the best available exit bound is
    P(dev >= rho sigma W_{s'/K}) <= C exp(-c (rho sigma)^theta) = C exp(-rho^theta A log l)
                                  = C l^{-A rho^theta}      instead of l^{-A}.
Feeding that into 2.5's touching sum (total = O(b l^{1 - A rho^theta})):
    the o(1) touching claim of section 3 dies unless  rho > A^{-1/theta}   = 0.7071 at A=2,theta=2;
    the sqrt(l) MAIN RESULT itself dies unless           rho > (2A)^{-1/theta} = 0.5   at A=2,theta=2.
(theta = 1 would give 0.5 and 0.25; theta = 2 is the value the localization draft supplies at
[V5-2].) So more than HALF the dead band is fatal to the theorem's own scale, not merely to a
convenience estimate. And at the bottom of the band the collapse is total: for D = O(1),
rho = O(1)/(sigma W_{s'/K}) -> 0, so l^{-A rho^theta} -> 1, the touching term is Theta(b s') -
LINEAR in the scale - and the recursion f(s) <= f(s/K) + Theta(s) returns A_+(l) = Theta(l).
The theorem asserts O(sqrt(l) polylog). Complete collapse, as iter-94 said, and now with the
threshold made explicit rather than argued at D = O(1) only.

Supporting (not needed for the verdict): at D = O(1) the exit probability is genuinely order one,
not merely unbounded above - condition on the weights outside a fixed box containing the far
endpoint and make the x = -1 detour strictly cheapest inside it; for any non-degenerate weight law
that event has probability p_0 > 0 depending only on the law. I flag that this needs the law to be
non-degenerate, which the theorem's standing hypothesis (iid in [a,b], 0 < a < b) permits but does
not force; the verdict above does not rest on it, since the failure is the ABSENCE of the required
upper bound.

### 3.4 Could a cleverer chain shrink the hole? Only to a floor, and not usefully
A non-uniform chain that refines geometrically near the far endpoint could make the last segment's
scale eps much smaller than s'/K, lowering its quantile to sigma eps^xi and admitting smaller D.
But eps >= 1 on the lattice, so the quantile can never be pushed below sigma = (A log l/c)^{1/theta}
-> infinity. A dead band of at least (0, sigma) is INTRINSIC to this architecture, at every scale,
for every chain. The puncture cannot be removed; at best it could be narrowed, at the cost of
per-member chain designs and more touching terms. Not worth doing, and I am not recommending it.

### 3.5 What is NOT necessary (recorded so the next pass does not confuse the two)
The following pieces of the current window ARE free choices, and I say so explicitly to keep the
necessary part sharp:
  - the top edge constant C_K. In the constant-depth chain the far-depth map is constant, so the
    only requirement on the top edge is that it exceed d(s)/d(s') <= 2^xi = 1.682. ANY constant
    >= 2^xi works. C_K = 3.019 (the on-chord chain's exact fixed point, iter-74) is vestigial here
    - confirming iter-94's remark by an independent route. Narrowing the top edge to 2^xi d(K s')
    would cut GEOM's bracket from C_K^2 K = 45.57 to 2^{2xi} K = 14.14, a 3.2x constant gain.
    PER THE NIGHT'S LESSON I record this as a HYPOTHESIS, not a recommendation: C_K also appears
    in the class tilt bound and in [V5-3]'s settled arithmetic, and nothing should be narrowed
    until someone checks those consumers. It is also the one change that would make finding 1.4
    (the K <= 37 / K <= 10 condition) disappear.
  - the height band [s/2, s]. The visited tree has s' = s at every level up to lattice rounding;
    the band exists only to absorb rounding. It is also the sole source of finding 1.4.

--------------------------------------------------------------------------------------------------
## 4. Verdicts

   (bottom D = d(s'), top D = C_K d(K s'), puncture D = 0), the height coordinate is exact, and
   the far-depth slacks (3.344x above the bottom, 1.795x below the top) are level-independent
   because the far-depth map is constant. Conditional on two unstated items, both repairable free:
   (i) an upper bound on K - the printed per-member window needs 2^xi <= C_K, i.e. K <= 37 at
   xi = 3/4 and K <= 10 uniformly over xi <= 3/4, while the document prints only "Fix K >= 5";
   (ii) (H-wand)'s printed depth range [d(r)-range, d(K r)-range] does not cover the window's deep
   end (the top edge is C_K K^xi = 10.09x that range's top) - restate the scope as "depths
   >= sigma W_r", which is monotone-favourable and costs nothing.
   Also owed: closure of the class under e_2-translation and y-reflection (used by the D = 0 far
   child), and the lattice-rounding sentence.

2. TWO-CHILD STEP AT D = 0 - CONFIRMED. Two spines total, branching one thereafter, is TRUE, and
   the reason is that the far-depth map is constant so no child ever has far-depth 0: the puncture
   stratum is a source with no incoming edges. Counts: 1 + 2J anchored members, (K-2) + 2(J-1)(K-1)
   = O(K log_K l) full-plane segments, no 2^j growth. The document does not state this reason;
   read literally its single-symbol sup recursion has coefficient 2 at every level, which survives
   only because c <= 0.12 sits 0.001 in the exponent below the break-even c = 0.12176. One owed
   sentence promotes the claim from lucky to proved.

3. DEAD BAND / PUNCTURE - CONFIRMED NECESSARY, and by a stronger argument than before. The last
   segment of any chain ends at depth D and can be typed only as anchored (needs D = 0) or as bulk
   (needs D at or above its own scale's deviation quantile); the punctured window is precisely the
   union of those two possibilities, so the hole is architectural rather than an artefact of the
   estimate. Admitting D = rho sigma W_{s'/K} costs l^{-A rho^theta} in place of l^{-A}: the o(1)
   touching claim fails for rho <= A^{-1/theta} = 0.707 and the sqrt(l) main claim itself fails for
   rho <= (2A)^{-1/theta} = 0.5 (A = 2, theta = 2), with total collapse to A_+(l) = Theta(l) at
   D = O(1). No chain refinement can push the hole below sigma. The v3 re-wiring changed nothing
   relevant: the far child's far endpoint is the parent's far endpoint by construction, at depth D,
   in every variant of the chain.

No exponent moves anywhere in this report. All three findings are statement-level and free to fix.

--------------------------------------------------------------------------------------------------
## 5. Self-audit: second derivation, standing caveat, and the strongest case that I am wrong

### 5.1 Second, independent derivation of every load-bearing number
referee1_check.py (this scratchpad) recomputes each quantity from the definitions, without reusing
any algebra above. Where I derived a condition by hand it BRUTE-FORCES the class instead: 501
heights h in [s/2, s] x 11 values of xi x 9 values of K, testing membership of child 0's far-depth
in the child's window directly. Agreement, item by item:
  C_K = 3.018780, K^xi = 3.343702, 2^xi = 1.681793, C_K K^xi = 10.093898
  child-0 slacks at K=5, xi=3/4: 5.6234 above bottom (at s'=s/2), 1.7950 below top   [hand: same]
  K threshold: bisection and closed form agree to 4 dp; Kmax(0.75) = 37.0237, K=37 passes
    (C_K = 1.681977 >= 1.681793), K=38 fails (1.674389); min over xi in (0,3/4] is 10.5818 at
    xi = 0.37, so K <= 10 is safe for every xi <= 3/4. Brute force independently flags K=12 as
    failing at xi in [0.30, 0.50] and K=37 as failing at every xi < 0.75.  [hand: same]
  far child's min clearance / own-scale quantile = 1.000000 exactly (zero slack at the bottom
    edge) - the numeric confirmation that the bottom edge is tight, not chosen.
  unstratified base exponent at c = 0.12: 0.4989954; break-even c = 0.1217646; the direct
    unrolling at l = 10^40 reproduces 2^J = 1.4448e15 = l^0.3789954.   [hand: same]
  GEOM bracket: K=4 tight 48.0416 vs printed 32 (FAILS); K=5 tight 46.8301 vs printed 55.9017
    (valid, 1.194x loose). [V5-3] confirmed from scratch.
  far-child tilt constant 17.9498 vs printed 16.7185 (7.36% short); class tilt 3.5900 vs printed
    6.0376 (valid, 1.682x slack); D=0 GEOM is 51.44x cheaper than a band step.
  dead-band thresholds: theta=2 gives 0.7071 (o(1)) and 0.5000 (sqrt main claim); theta=1 gives
    0.5000 and 0.2500.

### 5.2 Standing caveat that binds items 1 and 3 (not a defect; an l_0)
Both items use "the far child's own scale is s'/K". That is true once the far child's chord is
more vertical than horizontal, i.e. once its tilt K C_K sigma (s')^{xi-1} < 1. At the base scale
s' = r_0 = l^{0.12} this is 17.95 sigma l^{-0.03}, which for l = 10^6 and theta = 2, c ~ 0.1 is
still of order 100. So every o(1) tilt claim, the (H-curv) delta-range condition, and my own
"own scale" reading hold only for l >= l_0 with l_0 astronomically large. Legitimate for an
asymptotic theorem, and already noted at iter-94 V2; recorded here because it is a precondition of
my item-1 and item-3 arithmetic and not just of the document's.

### 5.3 The strongest case that each of my three verdicts is wrong
ITEM 1 (the K bound). Strongest case against me: the K <= 37 / K <= 10 condition exists only under
the LITERAL per-member reading of the printed window together with the full height band [s/2, s].
Under the class-uniform reading it is vacuous (1 <= C_K), and if the band exists only to absorb
lattice rounding - which is what the visited tree needs, since s' = s + O(1) there - then
(s/s')^xi = 1 + O(1/s) and it is vacuous again. So this is a statement-level condition on what is
printed, NOT a mathematical obstruction, and I say so rather than dressing it up. The one check
that settles it: the author states which reading the window has, and why the band is [s/2, s]
rather than [s(1-o(1)), s]. Under either intended reading the fix is one clause.
ITEM 2 (branching). Strongest case against me: if f was never meant as a class-sup but only as the
value along the visited tree, there is nothing to fix. But then the "class" and its window do no
work at all - the whole point of a class is that the induction closes over it - and the document
does write P(s) as a set of pairs. The check: whether section 5's recursion is quantified over
P(s) or over the constructed tree. Either way 2.1 is one sentence and makes both readings correct.
ITEM 3 (the puncture). Strongest case against me: my typing dichotomy assumes the last segment must
be either recursed-in-class or full-plane priced. A third route would be a separate NEAR-WALL lemma
bounding E T_+ - g for pairs with both endpoints at depth O(1) at scale r. That would defeat my
architectural argument - but such a lemma is essentially A_+ itself at the child scale, i.e. the
theorem being proved. So the dead band is precisely the region where the sub-problem is as hard as
the problem; excluding it is not a convenience but the content of the construction. The check that
would overturn me: exhibit a near-wall mean bound for shallow off-wall pairs that does not itself
consume I8. I do not believe one is available in this document's hypothesis ledger.

### 5.4 Where I differ from the two prior reports on this surface
- iter-74 (sketch referee): agrees on the punctured window; its fixed-point identity
  C_K K^{xi-1} + 1 = C_K is exact for the ON-CHORD chain. I confirm iter-94's observation, by an
  independent route, that v3's constant-depth chain makes that identity vestigial - and I add why:
  the far-depth map is a CONSTANT map, so it is a super-attracting fixed point and no identity is
  needed, only 2^xi <= C_K. That inequality is the origin of my new finding 1.4.
- iter-94 (combined referee): agrees the puncture is load-bearing. I strengthen its case from an
  estimate at D = O(1) to an architectural dichotomy valid for every chain (3.1), add the explicit
  rho thresholds (3.3), and add the intrinsic floor sigma (3.4). I also find two things it did not:
  the missing upper bound on K (1.4) and the (H-wand) scope mismatch at the DEEP end (1.6) - it
  found the shallow-end mismatch only. And I note its "branching 2, ratio 2/sqrt(K) < 1 still
  contracts" repair is true for the forcing sum but leaves the base at 2^J f(r_0), which clears
  sqrt(l) by 0.001 in the exponent rather than comfortably (2.3); the stratification of 2.1 removes
  that dependence entirely and is the repair I would print instead.
