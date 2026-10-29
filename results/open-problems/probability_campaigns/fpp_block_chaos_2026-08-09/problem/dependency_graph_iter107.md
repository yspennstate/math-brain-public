# The corner package's input graph: every edge sourced, the cycle check, and a phantom gap
# dissolved (iter 107, author's hand)

STATUS: DERIVED BOOKKEEPING - a dependency audit, not new mathematics. Every edge below cites the
file and section it was read from; the next referee verifies EDGES, not prose. Purpose: the
localization draft's gap G-d demanded a circularity check (does the H-version of the wandering
tail consume A_+, which v3 is busy proving?). The check is a graph question; here is the graph.

## Nodes and edges (consumer <- inputs, with the scale each input is consumed at)

C1 CORNER TARGET <- corner note (C1_corner_route_attempt_iter60.md):
  - Claims 1-6: deterministic (l1 geometry, surgery, reflection, split, Efron-Stein). No scale.
  - I2 = (P-conc) for FREE times, LOWER direction, wall pairs, all r <= R [note sec 3, lines
    145-148: S(r) is the free time's lower-deviation scale]. PUBLISHED.
  - I3 = confined-time UPPER concentration <- THE WALK [note sec 8 (I3); walk file]. See below.
  - I8 = A_+ at sqrt-polylog <- V3 DOCUMENT. See below.
  - F3 = g_+ = g <- the corner referee's self-contained proof [C1_corner_route_REFEREE_iter72.md].

THE WALK (I3_entropy_route_walk_iter86.md, repaired):
  - Tensorization + BLM 6.15: general probability, clean-source-verified [DHS 1401.0917 App A].
  - Claim 4 occupation bound: DETERMINISTIC [corner note sec 4].
  - Localization (T_+ <= br): deterministic.
  - CONSUMES NO WANDERING, NO CURVATURE, NO A_+. (The repaired S8 is arithmetic.)

V3 DOCUMENT (I8_from_curvature_v2_iter82.md, as repaired):
  - (H-curv) = c_+ one-sided UPPER pinning at e_2: consumed by GEOM at every scale s = l/K^j
    [v3 sec 3, the re-wired first-difference pricing].
  - (H-wand) = FREE-geodesic wall-ward deviation tail at the priced pairs' own scales
    [v3 sec 2 bullets as repaired: "P(wall-ward dev >= d(s)) <= l^{-A} ... is (H-wand) at their
    own scale"]. THE GEODESICS IN THESE EVENTS ARE FREE ONES - the touching complement is where
    T_+ = T; no confined geodesic's wandering is ever consumed.
  - (P-Alex): full-plane means at every scale [v3 sec 3 bulk pricing]. PUBLISHED.
  - Base case, tilt sum: deterministic/arithmetic.
  - (P-conc) ON THE LEDGER IS A PASS-THROUGH: v3's recursion consumes it nowhere (the combined
    referee's W6 finding, and this audit confirms it); it sits on the ledger because the
    CONSEQUENCE CHAIN cites the corner note, which consumes it as I2. The ledger line should say
    "consumed by the consequence chain's corner-note citation, not by this document's recursion"
    - a one-line clarification for the next pass.
  - (H-I3): same pass-through structure (the combined referee's correction of my own W6 premise).

LOCALIZATION DRAFT (localization_tail_draft_iter106.md - supplies (H-wand)'s tail form if it
survives):
  - (P-conc) for FREE times, both directions, legs at o(1) tilts: PUBLISHED.
  - (P-Alex): PUBLISHED.
  - c_- one-sided ENCLOSING-BALL curvature in an o(1) arc.
  - CONSUMES NO A_+, NO T_+ QUANTITY, NO CONFINED OBJECT. Free plane only.

## The cycle check

Path of concern (G-d's fear): v3 -> (H-wand) -> localization -> A_+ -> v3. THE THIRD EDGE DOES
NOT EXIST: the localization draft's free version consumes (P-Alex) - the PUBLISHED full-plane
mean cap - never E T_+ and never A_+. The graph is a DAG. No induction-order architecture is
needed.

## The phantom dissolved

G-d assumed the v3 consumer needs the tail for HALF-PLANE geodesics. Tracing the actual
consumption sites: v3's touching events are free-geodesic deviations (the whole point of the
deep pricing is that on the non-touching event T_+ = T); the corner note's two concentration
inputs are free-lower (I2) and confined-upper (I3, via the walk, no wandering); Claim 4 is
deterministic. NOBODY IN THE CURRENT PACKAGE CONSUMES H-GEODESIC WANDERING TAILS. The
localization draft's hardest-named gap is a phantom of its author's framing - the free version
is the only version any consumer needs. G-d is hereby re-scoped in the draft's terms: the
H-version remains an interesting object and remains unproved, and nothing here needs it.
[Referee instruction: verify the three consumption-site readings above against the cited
sections; if any site secretly needs a confined-geodesic tail, this dissolution is wrong and
G-d's circularity architecture question revives.]

## The package's unpublished-input list after this audit

If the walk, v3-as-repaired, and the localization draft all survive their referees, the corner
side of the program rests on exactly TWO unpublished inputs, both one-sided curvature conditions
at the axis, each consumed once:
  c_+ (upper pinning) -> GEOM;  c_- (enclosing ball) -> the wandering tail.
Everything else on the corner side is published, deterministic, or refereed inside the campaign.
THE WALL (CRUX section 2) remains untouched by all of it, and chi = 1/3 remains open.
