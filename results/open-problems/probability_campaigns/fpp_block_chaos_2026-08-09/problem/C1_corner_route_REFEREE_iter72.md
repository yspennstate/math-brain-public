# HOSTILE REFEREE REPORT, iter 72 - C1_corner_route_attempt_iter60.md (base note + author additions 6.5-6.6.4)

Referee mandate: break the document; default to rejection; both authors treated as adversaries.
Method: every attacked inequality re-derived from scratch (marked DERIVED below); pilot arithmetic
recomputed independently in a second lane (python, this session); READ = taken from the file or CRUX.
Context held to: CRUX_iteration_arithmetic.md 3b (resolved banner), 5, 6d.

VERDICT TABLE (details in the numbered sections):
- Base note secs 0-8 (Claims 1-6, cost formula, 7.1-7.4, ledger): ACCEPT as conditional-route note.
  Every displayed inequality I attacked survives; one UNJUSTIFIED side display (the section-4 FLOOR
  note) must be struck or conditioned (defect E0).
- Base note sec 9 (negative results): MAJOR. 9.1's class-wide conclusion is not delivered by its
  own display (defect E1); the verdict/section-5 glosses ("every pathwise route pinned at W_l")
  overstate all four subsections; 9.2/9.3 survive as route-pins with an unstated wandering input;
  9.4's "IS Theta(l)" conflates a worst-case cap with a route yield.
- Splitting Lemma 6.6.2: the LEMMA and its proof are CORRECT (fully re-derived, sec A below).
  MAJOR on the surrounding status language: "unconditionally" is false twice (defect A4 - the
  report's single worst defect), and "the wall-splitting route is PROVABLY inadequate" proves only
  that THIS chain is (defect B1).
- I3 upgrade 6.6.1: MODERATE. No fourth structural input found that references H^c (I looked:
  localization, influence, length, centering, uniqueness - all interior or unneeded). But the
  three-input list COMPRESSES Kesten's predictable-quadratic-variation control - the actual hard
  part of his Theorem 3 - into a clause that is not a proof step (defect C1). "Verified in
  mechanism" overstates; correct status: "no obstruction identified, adaptation still owed".
  half-quadrant point-to-(N,N) IS the wall-pair analogue); three named caveats owed (D1-D3).
- Consistency with CRUX 3b/banner: MINOR. "IFF" defensible only under the package-relative reading;
  the closed right endpoint "chi in (0.4142, 1/2]" is internally inconsistent at chi = 1/2 (F2).
- Pilot 6.5/6.6.3: MINOR. All numbers reproduce to the digit; two misdescriptions (G1, G2) and one
  missing rig caveat (G3). Main result verdicts (exponent unresolved, magnitude inside) are supported.

--------------------------------------------------------------------------------------------------
## A. THE SPLITTING LEMMA (6.6.2) - attacked step by step. THE LEMMA HOLDS.

Statement under attack: a_l := E T_+((0,0),(0,l)), D_l := a_l - g l with g := g(e_2) per unit,
x*_l := depth of the first crossing of y = l by the H-geodesic gamma from (0,0) to (0,2l). Claim:
D_{2l} >= 2 D_l - 2b E[x*_l], and D_l <= b Sum_{j>=0} 2^{-j} E[x*_{2^j l}] (the file's
2b Sum 2^{-(j+1)} is the same number).

A1. WELL-DEFINEDNESS AND THE SPLIT (attacked, survives). DERIVED: a lattice path from y=0 to y=2l
changes y by unit steps, so it has a vertex with y = l exactly; w := the first such vertex of gamma
is measurable given the file's fixed tie-breaking selection, w = (x*, l) with x* >= 0 (gamma is in
H) and x* <= (b/a) 2l (via T_+ <= 2bl and weights >= a, so |gamma| <= (2b/a) l). T_+((0,0),w) is a
composition over finitely many candidate w, each summand bounded by 2bl: integrable, well-defined.
Splitting the edge sum of gamma at w: a_{2l} = E[T(gamma[0->w])] + E[T(gamma[w->end])]. Each
half-path is an H-path with the right endpoints, so PATHWISE T(gamma[0->w]) >= T_+((0,0),w) and
T(gamma[w->end]) >= T_+(w,(0,2l)); randomness of w is harmless because the inequalities hold in
every configuration. Hence a_{2l} >= E[T_+((0,0),w)] + E[T_+(w,(0,2l))]. No gap.

A2. THE TWO TRIANGLE INEQUALITIES (attacked for direction, survive). DERIVED, pathwise in each
configuration: the horizontal segment from w = (x*,l) to (0,l) has x* edges, all x-coordinates in
[0,x*] so inside H, each weight <= b. Therefore
  (i)  T_+((0,0),(0,l))  <= T_+((0,0),w) + b x*        [go to w, walk back to the wall]
  (ii) T_+((0,l),(0,2l)) <= b x* + T_+(w,(0,2l))       [walk out to w, continue]
Direction check the prompt asked for: (i) bounds the FIXED quantity a_l from above by
E[T_+((0,0),w)] + b E[x*] - the comparison runs the right way; nothing bounds E[T_+((0,0),w)] by
a_l (which would be false). e_2-translation invariance: H = {x >= 0} is invariant under integer
multiples of e_2 and the weights are iid, so E T_+((0,l),(0,2l)) = a_l EXACTLY; nothing else is
assumed. Summing (i)+(ii) in expectation: 2 a_l <= a_{2l} + 2b E[x*_l] by A1. Subtract 2gl:
2 D_l <= D_{2l} + 2b E[x*_l]. QED as claimed. The lemma is CORRECT.

A3. THE FEKETE STEP (attacked; survives, but the wiring must be stated). Iterating
D_l <= (1/2) D_{2l} + b E[x*_l] upward k times (legitimate: the inequality holds at every scale,
and each application is at a different scale so the chain composes):
  D_l <= 2^{-k} D_{2^k l} + b Sum_{j=0}^{k-1} 2^{-j} E[x*_{2^j l}].
The boundary term is l * (D_m/m) at m = 2^k l, so killing it needs D_m/m -> 0, i.e. g_+ = g -
NOT bare Fekete. Fekete gives a_m/m -> g_+ := inf a_m/m only. g_+ = g is the note's own F3, and I
verified F3's cylinder argument independently: DERIVED - for any k let m = (b/a)k + 1; the free
geodesic between (m, ik) and (m,(i+1)k) has <= (b/a)k edges (T <= bk via the straight segment,
weights >= a), hence stays in {x >= 1} subset H; concatenating N of them and two horizontal runs
of length m gives a_{Nk} <= 2bm + N E T(0, k e_2), so g_+ <= E T(0,k e_2)/k for every k, and
inf_k E T(0, k e_2)/k = g(e_2) BY DEFINITION of g (Fekete for the free time). With g_+ >= g
(T_+ >= T): g_+ = g, elementary and self-contained. CONSEQUENCE: the Ahlberg citation in 6.6.4(a)
is NOT load-bearing for F3 - good, because its applicability is UNVERIFIED: e_2 is a BOUNDARY
direction of the half-plane cone, and cone shape theorems typically cover interior directions.
Do not cite Ahlberg for F3 without checking the boundary-direction clause; cite the two-line
argument above instead. Dyadic sum convergence (attacked, survives): under E[x*_m] <= C m^{gamma'},
Sum_j 2^{-j} (2^j l)^{gamma'} = l^{gamma'} Sum_j 2^{j(gamma'-1)} < infinity iff gamma' < 1, giving
D_l <= bC l^{gamma'} / (1 - 2^{gamma'-1}). All checks pass.

A4. THE STATUS LANGUAGE AROUND THE LEMMA IS FALSE - THE WORST DEFECT IN THE FILE. Two places:
  - I8 ledger annotation: "What survives unconditionally: A_+(l) <= C l^{gamma'} for ANY half-plane
    wandering exponent gamma' < 1."
  - STATUS AFTER 6.6: "unconditionally, cost <= concentration terms + C l^{gamma'} with gamma' the
    half-plane wandering exponent."
Both assert an unconditional bound. There is NO unconditional gamma' < 1: E[x*_m] = o(m) - sublinear
depth of the H-geodesic between wall points - is itself OPEN. I checked the natural route to it and
it fails: to force depth o(m) one wants g(w) + g((0,2l)-w) - g((0,2l)) >= c(depth), which needs
STRICT convexity of g at e_2 - unavailable, and with a large atom at a the limit shape genuinely
has flat pieces (Durrett-Liggett), so no soft argument can supply it. Unconditionally the lemma
therefore yields only the trivial D_l <= C l (gamma' = 1 diverges the dyadic sum; direct bound
already gives linear). "The first unconditional-in-structure upper bound on I8 beyond the trivial
file; the unconditional wrapper is wrong. REQUIRED REPAIR: replace "unconditionally" with
"conditionally on a half-plane wandering bound E[x*_m] <= C m^{gamma'}, gamma' < 1" in both places,
and strike "unconditional-in-structure". Note the irony against the note's own selling point
(section 8: "no wandering hypothesis (W) at any scale"): the only surviving route to a nontrivial
I8 bound now CONSUMES a wandering hypothesis - for the H-geodesic, a harder object than the free
one. That reversal deserves one honest sentence in the note.

A5. Also unverified as cited: "even the published conditional machinery gives only m^{3/4}
(curvature-conditional Newman-Piza/Alexander wandering)". Newman-Piza is a FULL-plane statement;
its adaptation to H-geodesics between wall points is asserted, not shown or cited. Flag as
"plausible adaptation, unchecked" - same discipline the note applies to I3.

--------------------------------------------------------------------------------------------------
## B. THE CLAIMED CONSEQUENCE (-): "route provably inadequate / sqrt would need gamma' = 1/2"

B1. WHAT IS ACTUALLY PROVED vs WHAT IS ANNOUNCED. Proved: the specific dyadic chain (6.6) outputs
b Sum 2^{-j} E[x*_{2^j l}] >= b E[x*_l] (the j=0 term), so THIS chain certifies nothing below the
wandering scale - tautologically, an upper-bound machine cannot certify below its own output.
Announced: "THE WALL-SPLITTING ROUTE TO I8 IS PROVABLY INADEQUATE". No class of "wall-splitting
routes" is defined (contrast 9.1, which at least defines class P). A different split-based
comparison - e.g. one that compares E T_+((0,0),w) to a_{y(w)} via concentration rather than via a
deterministic connector to the wall - is not covered by anything proved here. REQUIRED REPAIR:
either define the route class whose members provably pay E[x*] per dyadic scale (the honest
mini-class: arguments comparing a_l to the split halves via CONNECTOR PATHS from w to the wall pay
>= a E[x*_l] because every edge costs >= a), or downgrade to "the natural dyadic argument is
inadequate". The threshold arithmetic itself is verified: gamma' = 1/2 -> alpha > 1/3;
gamma' = 2/3 -> alpha > 1/2 (empty window); gamma' = 3/4 -> alpha > 3/5; break-even with the shift
route at gamma' = 0.8284/1.4142 = 0.5858 ("about 0.59" as stated). DERIVED, all correct.

B2. ROUTE vs QUANTITY - the file mostly does NOT commit the conflation the mandate suspected.
6.6.4(b) argues the TRUTH is plausibly at fluctuation scale while the splitting route cannot see
below wandering scale; the synthesis states both sides. Two residual slips: (a) 6.6.3's phrase
"the wandering-dominated regime of (6.6)" implies (6.6) PREDICTS P2 ~ wandering - it cannot; (6.6)
is an upper bound with no lower-bound content linking P2 to E[x*]. (b) STATUS AFTER 6.6: "the route
beats the shift route iff gamma' < (1+alpha)/(2+alpha)" - false as an "iff" about the route: if I8
at sqrt scale were proved by ANY means, the route beats the shift regardless of gamma'. It is an
"iff" about the route WITH (6.6) AS ITS I8 INPUT. One-clause repair each.

--------------------------------------------------------------------------------------------------
## C. I3 UPGRADE (6.6.1) - the hunt for a fourth structural input

Mandate: name any fourth input Kesten's concentration proof uses that the list (a) iid bounded
weights, (b) deterministic localization, (c) deterministic edge-count bound omits. Candidates
attacked, with outcomes:

C-i. GEODESIC UNIQUENESS: not needed. Kesten runs on a fixed measurable selection; the influence
bound |T_+ - T_+^{(e)}| <= (b-a)[1(e on gamma_+) + 1(e on gamma_+^{(e)})] uses optimizers of BOTH
configurations, both available in H. Survives.
C-ii. TWO-SIDED P(e on geodesic | F): not consumed by the martingale bound; only presence
indicators enter. Survives.
C-iii. LOCALIZATION FOR T_+: deterministic here - T_+ <= br via the wall segment (both endpoints
ON the wall; the segment lies in H), so every near-optimizer has <= (b/a)r edges and lives in the
radius-(b/a)r box intersected with H. Nothing beyond T_+ <= br is needed. Survives.
C-iv. CENTERING: Kesten centers at the mean via the Doob martingale itself; no median-to-mean
conversion is consumed (and at sqrt target it would be harmless anyway). Survives.
C-v. THE REAL GAP - PREDICTABLE QUADRATIC VARIATION (defect C1). The note's clause "the
conditional-variance sum <= (b-a)^2 E|gamma_+| <= (b-a)^2 (b/a) r, and Freedman-Bernstein" is not
a proof step. Freedman needs a PREDICTABLE (pathwise) bound on Sum_k E[Delta_k^2 | F_{k-1}], and
that sum is a sum of conditional expectations under DIFFERENT conditionings: there is no pathwise
identity bounding it by E|gamma_+|-anything, and the naive pathwise bound is the edge count of the
box, order r^2 - useless. Bridging expected-QV to predictable-QV is the multi-page technical core
of Kesten's Theorem 3 (truncation/stopping machinery). I could not exhibit any step of that
machinery that references edges outside the subgraph - it is optimizer combinatorics plus
three-item list can carry when the hardest mechanism was summarized rather than walked. VERDICT:
upgrade I3's status to "no obstruction identified; the QV-control pages of Kesten Thm 3 remain to
be walked for H"; do not call it verified. The attack surface the note requested is hereby
narrowed to exactly one named place.

--------------------------------------------------------------------------------------------------

D0. THE MANDATE'S SUSPECTED CONFLATION FAILS. The wall-pair analogue in half-space LPP is passage
from (1,1) to (N,N) in the half-quadrant {i >= j}: BOTH endpoints on the diagonal (= the wall),
path confined to one side, travel ALONG the wall. That is precisely the geometry of the cited
Baik-Rains / stationary half-space line of work (symmetrized LPP = LPP in the half-quadrant with
the point-to-point observable on the diagonal). So "point-to-diagonal geometry vs wall-pair
geometry" is not a defect here: the solvable object IS wall-pair-shaped. READ + DERIVED check.

D1. WHAT THE SOLVABLE RESULTS ESTABLISH (stated precisely, as the mandate requires): for exponential
half-space LPP with boundary (diagonal) parameter in the SUBCRITICAL phase - which includes
diagonal weights with the same law as the bulk - the LLN constant of H(N,N) equals the full-space
constant (4 per unit for Exp(1)), and (H(N,N) - 4N)/N^{1/3} converges to a boundary-dependent
Tracy-Widom-type law (GSE at generic subcritical, GOE^2-type at critical; supercritical breaks
this: LLN constant changes and fluctuations become N^{1/2} Gaussian). CONSEQUENCE the note wants:
the solvable analogue of A_+ - the mean deficit of the wall-pair time against the full-space LLN -
is O(N^{1/3}) = fluctuation scale in the subcritical phase. Three caveats the note owes:
  (D1a) MEAN vs LAW: distributional convergence at scale N^{1/3} bounds the mean deficit only with
  uniform integrability; the solvable literature has the tail bounds, but the note's "could not be
  missed by the exact formulas" should cite moment convergence, not just the limit law.
  (D1b) PHASE IDENTIFICATION: FPP's wall carries NO boundary parameter. Identifying it with the
  SUBCRITICAL phase is an argument ("the wall only removes paths; nothing rewards hugging it"),
  and a good one, but it is an analogy step, not a computation - say so. A pinning-type wall would
  (D1c) SIGN FLIP: in LPP the wall DECREASES the max (deficit negative); in FPP it INCREASES the
D2. With those three sentences added, 6.6.4(b) is an honest plausibility argument and nothing
more - which is what it claims to be ("heuristically"). It does NOT license gamma = alpha in 7.2
as anything but a target. Survives as labeled. MINOR.

--------------------------------------------------------------------------------------------------
## E. BASE NOTE, SECTIONS 9.1-9.4 (never refereed until now) - and one defect in section 4

E0. SECTION 4's "FLOOR" NOTE IS UNJUSTIFIED AS WRITTEN (found while re-deriving Claim 6; it is
outside the banner's verified list, and the banner was right to exclude it). The display
"MEANGAP(r) >= (1/2)E|T_+ - T_-| >= c sqrt(E Var(T_+|F))" uses E|X| >= c sqrt(E X^2) for
X = T_+ - T_-, which is FALSE without anti-concentration input. COUNTEREXAMPLE (concrete witness):
conditionally symmetric X with X = 0 w.p. 1-p and X = +-(b-a)r w.p. p/2 each gives
E|X| = p(b-a)r but sqrt(E X^2) = sqrt(p)(b-a)r; the ratio sqrt(p) -> 0. E|X| >= c sqrt(EX^2)
requires bounded kurtosis of X (Paley-Zygmund), which is not supplied - amusingly the SAME
L^1-vs-L^2 gap that CRUX 6c/6d spent a night on (there as L^2-vs-L^4). What IS available from
boundedness: E|X| >= E X^2 / ((b-a)r) = 2 E[Var(T_+|F)]/((b-a)r), a much weaker floor. The
non-vacuity conclusion ("the route cannot cost less than Q_r, and Q_r is inside the budget") is
therefore UNPROVED as stated; it becomes true under H3-lower PLUS a kurtosis bound on T_+ - T_-.
REPAIR: strike the floor note or condition it explicitly. Not load-bearing for the main chain -
nothing downstream consumes it - but it is a flat error in a note whose other displays are clean.

E1. 9.1 (CLASS P): THE DISPLAY IS SOUND, THE CLASS-WIDE CONCLUSION IS NOT DELIVERED. Two findings.
  (E1a) The proved content is exactly: any class-P member pays cost >= a D_1, where D_1 is the
  FIRST sub-geodesic's containment margin, and D_1 must exceed the deviation quantile of that
  piece AT ITS OWN SCALE s_1 (which 9.1 writes "W_s" with s never bound - the symbol s is
  literally undefined in the section). For members with a SHORT first piece, W_{s_1} is small and
  the display pins nothing. The draft's L3 has s_1 = s = l^{2/(3-alpha)}, so the display does pin
  THE DRAFT's construction and its listed reorganizations (one-shot/dyadic/skip all keep
  piece-scale ~ s). But the announced conclusion - "it is a property of the entire class, and no
  re-organisation of the chain escapes it" - would need the complementary CHAINING floor (many
  small pieces => accumulated mean overhead >= K * something), i.e. a LOWER bound on the
  superadditivity defect / Alexander error at scale s_1, which nothing in hand provides (A(s) >= 0
  is all that is known; A(s) = 0 is not excluded). A many-tiny-pieces member evades the proved
  floor and is excluded only by an unproven chaining cost. REPAIR: restate the conclusion as "the
  W_s shift cost is forced for every class-P member whose piece scale is tied to l by the chaining
  budget; a class-wide pin additionally needs a chaining-cost lower bound (open)".
  (E1b) UNSTATED PROBABILISTIC INPUT: "that margin is at least the corresponding quantile of the
  transversal deviation, hence >= c W_s" consumes median transversal deviation >= c W_s - a
  wandering LOWER bound. Unconditionally unknown; within the program's hypothesis set it is
  Chatterjee-flavoured (exponent existence), but it appears on no ledger. The note's section 8
  boasts "no wandering hypothesis" for the ROUTE; fine - but 9.1's negative result consumes one,
  and must say so.

E2. 9.2 (MEAN SHIFT PINNED AT W_l): SURVIVES as a route-pin, same unstated input. DERIVED checks:
MEANGAP(0) <= 2bD + MEANGAP(D) is correct (walk-in costs <= bD each way inside H; E T of the
depth-D pair equals E T of the wall pair by translation invariance of the FREE time - the step the
display silently uses, and it is exact). MEANGAP(D) <= (b-a)-scale * l * P(free geodesic of the
depth-D pair touches x = -1) is correct (if the free geodesic stays in H the gap vanishes; else
the deterministic cap applies - and note T_+ <= bl via the straight vertical segment at depth D,
so even the crude cap is honest). The Theta(W_l) minimum then needs P(touch) = Omega(1) for all
D <= c W_l - the SAME wandering lower bound as E1b, again unstated. With it, the "for every tail
shape" claim is right: below the wandering scale the second term is Omega(l) >= Omega(W_l); above
it the first term is >= 2b c W_l. IMPORTANT SCOPE POINT: 9.2 pins THIS argument-shape (charge the
full deterministic gap on the exit event), not the quantity MEANGAP - the section's own wording
("min over D of this bound") is careful; the VERDICT's gloss (see E5) is not.

E3. 9.3 (FOLDING): SURVIVES, and I close a gap in its counting claim. The fold inequality is
verified pathwise, including the two-to-one subtlety (a path using both e and its mirror folds to
a WALK; walk time >= path time, inequality direction unharmed). The count claim "expected number
of folded terms = half the expected off-column length = Theta(l)" needs E|gamma free of the wall
column| >= c l, which the note asserts without proof; here is the missing argument, DERIVED: if
E[off-column edge count] = o(l), then gamma uses >= l - o(l) of the l specific wall-segment edges
(any wall pair path has >= l edges), forcing E T >= l E[omega] - o(l); but E T = a^free_l ~ g l
and g < E omega STRICTLY for nondegenerate weights (classical strict inequality, van den
Berg-Kesten) - contradiction. So the Theta(l) count stands rigorously. Left/right exchangeability
under the reflection needs the geodesic SELECTION rule to commute with the reflection - a
measurability nit the note should fix by choosing an R-equivariant tie-break (or arguing via the
a.s.-unique-geodesic case when weights are continuous). CONSEQUENCE 1 (the sqrt cap on the
method's best case) is a legitimate a fortiori ceiling; calling it "rigorous" is acceptable since
it bounds the method's ideal output, not a theorem about T_+. CONSEQUENCE 2 is labeled
non-rigorous and one-directional; I checked the direction and it is actually REINFORCED by a bias
the note did not charge: conditionally on gamma selecting the left edge e, the mirror weight
omega(Re) is biased UPWARD (the geodesic went left partly because right was expensive), adding
positive drift on top of the selection bias of e. The sign claim is safe.

E4. 9.4 (EXCURSION REPAIR): the inequality chain is verified (each minus-excursion is an
H^- path between wall points, so its time >= T_- of that pair; replacement by the H^+ geodesic
gives the displayed bound with conditionally symmetric terms). The cost accounting: worst case
Sum_i (b-a) r_i <= (b-a)(b/a) l because excursion lengths sum to <= |gamma| <= (b/a)l - so
"Theta(l)" is right as the WORST-CASE value of the bound (the note's "dyadic sum dominated by
smallest scales" derivation is looser than needed; the length-budget argument above is the clean
one). DEFECT: "IS ALSO Theta(l)" asserts the ROUTE YIELDS Theta(l), but the route's yield at the
required confidence is the upper quantile of a sum of conditionally symmetric,
positively-selected terms - typically far below its deterministic cap; no lower bound on the
yield is derived ("any repair anchored at the crossings pays for the anchoring" is a heuristic,
not a floor). REPAIR: downgrade to "admits no better certificate than Theta(l) by the arguments
given; no sub-W_l certificate is exhibited" - which is all section 5 actually needs from it.

E5. THE GLOSSES OVERSTATE 9.x TWICE (defect, propagates to the verdict): the VERDICT's "(iii)
three negative results showing that EVERY PATHWISE ROUTE ... is pinned at W_l or worse" and
section 5's "Sections 9.1-9.2 show that every pathwise route ... is pinned at W_l" are both
FALSE as written: (a) 9.1 pins class P (not "every route") and at the piece scale's W (not W_l) -
the shift route itself, a class member, costs l^{(1+alpha)/(3-alpha)} < W_l, contradicting the
gloss's literal reading; (b) all four subsections pin ROUTES/BOUNDS, not quantities, and two of
them consume an unstated wandering lower bound. The defensible summary is: "every ROUTE SO FAR
PROPOSED - the draft's class of margin certificates, the mean-shift charge, folding, and
excursion repair - is blocked at or above the shift route's value, under a wandering lower bound
at the relevant scale; the mean/fluctuation split is the only known escape." That is still a
strong structural statement, and it is what the evidence supports.

--------------------------------------------------------------------------------------------------
## F. CONSISTENCY: banner "PACKAGE ASSEMBLES IFF chi > 1/3" vs CRUX 3b (resolved form)

F1. THE "IF" DIRECTION CHECKS. CRUX 3b resolved: within the hypothesis set alpha = chi exactly
(chaos needs alpha <= chi; H1a forces alpha >= chi); wall admissible set (0, chi]. This note:
corner criterion alpha > (1 + 2beta + 4delta + 12eps)/3, so for any chi > 1/3 choose beta, delta,
eps small enough (nothing in the file forbids that; verify beta > 0 has no hidden floor in MG2A's
geometry - flagged, not checked here) and the criteria are jointly satisfiable. Conditional on
I8-at-sqrt, I3, and the hypothesis set: assembles. VERIFIED as a sufficient-criteria statement.

F2. THE "ONLY IF" IS PACKAGE-RELATIVE, AND THE RIGHT ENDPOINT IS INCONSISTENT (defect). "Only if"
holds in the sense: at chi <= 1/3, alpha = chi <= 1/3 violates the corner criterion, so THIS
package's criteria fail. It does NOT preclude a different corner argument at alpha = 1/3 - the
file's own 6.3/6.6.2 discussion knows this; the banner should say "this package". Sharper defect:
the regime sentence "If chi in (0.4142, 1/2]: both routes close" is internally inconsistent AT
the endpoint. DERIVED: the package's output is Var(X_N) <= C N^{1-eps} with eps = log2/logM > 0
fixed; if chi = 1/2 (true variance exponent, e.g. Var ~ n/log n has exponent 1/2), the output
contradicts the truth the pin alpha = chi presupposes. So assembly at chi = 1/2 refutes one of
its own hypotheses: the interval must be OPEN at 1/2, and near 1/2 one needs M large (eps < 1 -
2chi). Same correction applies to this note's "closes on (1/3, 1/2]" (7.4) and to CRUX 3b's
"(0.414, 1/2]" phrasing wherever "close/assemble" is meant (as a statement of what is UNPROVEN -
"nothing unconditional excludes chi in (0.414, 1/2]" - the closed endpoint is fine). One-line
repairs. Otherwise the banner's reconciliation, the three regimes, and the annotated supersession
of the pre-iter-68 paragraph are CONSISTENT with CRUX 3b's resolved form, and the "meet at 1/3
instead of excluding by 0.08" statement survives with its conditionality intact.

F3. CRUX 5 / 6d cross-checks: Claim 4's diameter argument is the refereed occupation lemma's
simplest case, correctly READ; nothing in the note consumes the withdrawn CRUX 6/6b/6c material;
so the lesson lands once, in both files.

--------------------------------------------------------------------------------------------------
## G. THE PILOT (6.5, 6.6.3) - independently audited against the RAW DATA this session

G0. PROVENANCE AUDIT (beyond the note's self-report). I located and read the actual artifacts:
scratchpad p2_pilot.py, p2_extend768.py, p2_extend1536.py, p2_pilot_results.json (seed 20260809,
timestamps 22:51-23:06). The rig does what the note says: three Dijkstras per sample (free /
x>=0 / x<=0) on the SAME weight draw, wall pair (0,0)-(0,l), Uniform[1,2], patch x in
[-W,W], W = max(24, 4 l^{2/3}), y-margin 2 l^{2/3}, per-level checkpointing. ALL SEVEN table rows
match the JSON to the printed digits (P2, SEs, Part1, crossing fractions), min_gap = 0.0 at every
level (the pathwise invariant T <= min(T_+,T_-) held in all ~1,208 samples), and the local slopes
0.597/1.086/0.858 match my independent recomputation exactly, with slope SEs 0.35/0.35/0.29 as
claimed. The conditional gaps 0.31/0.43/0.91/0.95/1.88/2.99 all match. EXTRA CHECK the note never
ran, passes: per level, mean((T_+ - T_-)^+) - (1/2)mean|T_+ - T_-| is 1-1.5 sigma from zero at
every level - the Claim-3 exchangeability prediction holds in the data.

G1. DEFECT (misdescription): "Part1 ... local exponent falling 1.56 -> 0.97 -> 0.71 -> 0.53 ->
0.35 across octaves - converging to the proved sqrt cap FROM ABOVE". False as a description: the
sequence CROSSES 1/2 between the 4th and 5th octave and keeps falling (0.53 -> 0.35 -> 0.31 with
the 1536 point). Nothing is converging to 0.5 from above; the level sits far BELOW the cap
(2.99 vs 39.2 at 1536), so a sub-1/2 local slope is unremarkable - but then the positive control
should be described as "cap respected with huge margin", not as slope convergence. Two-word fix.

G2. DEFECT (evidence overstated by one adjective): "the crossing fraction STILL rising
(0.68 -> 0.77)". That step is 0.675 -> 0.771 with binomial SEs 0.052/0.061: a 1.1 sigma rise.
The monotone trend across all seven levels is overwhelming, but the top-octave step alone - the
one the sentence leans on for "the regime has not stabilized by l = 1536" - is not significant.
Say "consistent with still rising (1.1 sigma)".

G3. DEFECT (missing rig caveat, and the author KNEW): p2_pilot.py line 64 comments that patch
truncation, if it binds, biases P2 toward the null, "stated in the report rather than hidden" -
and 6.5 never states it. The direction argument is itself heuristic (all three times are raised
by truncation; the free time plausibly most). Add the one sentence the code promised.

G4. WHAT THE PILOT SECTIONS GET RIGHT (conceded after attack): no exponent conclusion is quoted
in either direction, and the SEs genuinely do not permit one (0.60/1.09/0.86 each +-0.3-0.35
brackets both 1/2 and 2/3); the magnitude margins (17x inside sqrt at 1536, 58x inside W_l) are
correct and honestly labeled pre-asymptotic; the onset diagnosis (crossing fraction 0 at l=24) is
the right reading of why small-l slopes (2.6, 2.5 in the JSON, rightly excluded) are meaningless.
6.6.3's cross-read stays inside "consistent with / cannot settle" except for the phrase flagged
in B2(a). The pilot block is the cleanest part of the author's additions.

--------------------------------------------------------------------------------------------------
## H. DEFECT LEDGER (severity-ordered) AND REQUIRED REPAIRS

H1 [MAJOR, the single worst defect] A4: "unconditionally" attached to A_+(l) <= C l^{gamma'} in
   the I8 ledger annotation and in STATUS AFTER 6.6. No gamma' < 1 is known unconditionally
   (sublinear H-geodesic depth is itself open; strict convexity at e_2 unavailable, flat-edge
   weights show no soft argument exists). Repair: conditionalize both sentences; strike
   "unconditional-in-structure"; add the sentence that the splitting route reintroduces a
   wandering hypothesis into a note whose main claim is "no wandering input".
H2 [MAJOR] E1: 9.1's class-wide conclusion exceeds its display (s unbound; chaining floor
   missing; wandering-quantile input unstated). Repair per E1.
H3 [MAJOR] E5: verdict item (iii) and section 5's gloss "every pathwise route pinned at W_l" -
   false as written (the shift route itself costs l^{(1+alpha)/(3-alpha)} < W_l). Repair per E5.
H4 [MODERATE] C1: I3's "verified in mechanism" overstates; the predictable-QV control of Kesten
   Thm 3 was summarized, not walked. Repair: status "no obstruction identified"; keep the
   three-input list as the skeleton plus the named fourth item (QV-control pages).
H5 [MODERATE] E0: section 4's FLOOR display is false without a kurtosis input (counterexample in
   E0). Repair: strike or conditionalize; non-vacuity of the target is currently UNSUPPORTED.
H6 [MODERATE] B1: "wall-splitting route PROVABLY inadequate" - proved only for the exhibited
   chain (plus the connector mini-class if the note adopts the definition offered in B1).
H7 [MINOR] F2: open the interval at chi = 1/2 in banner, 7.4, and (for "closes") CRUX 3b.
   half-plane flagged as unchecked adaptation; A3: do not cite Ahlberg for F3 (boundary
   direction unverified; the elementary cylinder proof suffices and is two lines).
H9 [MINOR] G1, G2, G3: pilot description fixes; B2(a) "regime of (6.6)" phrase; B2(b) route-
   relative "iff"; Claim-3 selection-rule equivariance nit (E3); section-3 monotonicity remark
   is unproven but unconsumed (the display already takes max over r <= R) - either prove
   monotonicity or delete the remark.

## I. WHAT SURVIVES, STATED POSITIVELY (conceded only because I could not refute it)
- Claims 1, 2, 3, 4, 5, 6 and the section-3 cost formula: re-derived line by line, correct,
  with the stated windows (none). The banner's hand-verification of these is CONFIRMED.
- 7.1-7.4 arithmetic including the exact symbolic cross-check against the shift route: EXACT.
- The Splitting Lemma's statement and proof: correct and, conditional on any proved half-plane
- F3 (g_+ = g at e_2): correct, with a self-contained two-line proof (A3) replacing the
  unnecessary Ahlberg citation.
- The pilot: rig validated against raw artifacts this session; its two main verdicts
  (exponent unresolved; magnitude comfortably inside both candidate budgets) are exactly what
  the data supports, no more.
- The structural point that survives everything above: the mean/fluctuation split remains the
  only exhibited device that avoids paying a wandering-scale cost SOMEWHERE - but after this
  referee pass that statement is a description of the routes tried, not a theorem about all
  routes, and I8 now has NO plausible proof mechanism on the table (6.6.2 killed the naive one;
  6.6.4 shows the truth is nevertheless plausibly favourable). The honest program status is
  therefore exactly what STATUS AFTER 6.6's last sentence says, once H1's false "unconditionally"
  is removed from the sentence before it.

Referee: hostile pass, iter 72. All inequalities re-derived; pilot re-audited from raw JSON;
second-lane numerics in-session. Nothing in this report was accepted on either author's word.



