# I3 walked via the entropy route: the QV bridge is not consumed at all (iter 86)

STATUS: DERIVED WALK against the ADH survey's section 3.4.2 presentation (Theorem 3.11, the
argument of [54, Corollary A.5], Talagrand-strength upper tail), extracted text on disk
(scratchpad adh_survey_text.txt, pages 47-49). NOT YET REFEREED. This walk targets exactly the
corner note's input I3: sqrt-scale stretched/Gaussian UPPER-tail concentration for the H-CONFINED
passage time T_+ between wall pairs, direction e_2, bounded weights.

## Why this route, not Kesten's

The corner referee narrowed I3's gap to one named place: the predictable-quadratic-variation
bridge in Kesten's 1993 Theorem 3 (expected-QV to pathwise-QV via truncation/stopping - the
multi-page core). THE MODERN ROUTE DOES NOT CONTAIN THAT BRIDGE. The survey's 3.4.2 proof runs:
Herbst argument on the log-MGF; tensorization of entropy over edges; the Boucheron-Lugosi-Massart
symmetrized modified log-Sobolev inequality; optimizer combinatorics; one exponential moment on
the geodesic-intersection count; calculus. No martingale, no filtration, no QV. If every step is
subgraph-safe, I3 follows WITHOUT walking Kesten's machinery - the named gap is bypassed, not
crossed.

## The walk, step by step, each with its inputs and its H-status

(S1) LOCALIZATION. T_+((0,0),(0,r)) <= b r via the wall segment, so every near-optimal H-path has
<= (b/a) r edges and lives in the finite box B* cap H. The entropy sums below run over the
finitely many edges of that region. INPUT: boundedness + subpath optimality. H-SAFE (the wall
segment IS in H; this is the note's Claim 4 setting). [Same as full plane.]

(S2) HERBST. It suffices to show Ent e^{lambda T_+} <= C r lambda^2 E e^{lambda T_+} on a lambda
range; integrating d/dlambda (psi/lambda) gives psi(lambda) <= C r lambda^2 and Chebyshev closes.
INPUT: calculus on the log-MGF. NO GEOMETRY. H-SAFE trivially.

(S3) TENSORIZATION. Ent e^{lambda T_+} <= Sum_i E Ent_i e^{lambda T_+} over the edges of B* cap H.
INPUT: tensorization of entropy for product measures (general). The product structure is the iid
weights on the SUBGRAPH's edges - a product measure like any other. H-SAFE.

(S4) SYMMETRIZED MODIFIED LSI (BLM Thm 6.15, quoted as survey Lemma 3.12): per edge,
Ent_i e^{lambda T_+} <= E_i[e^{lambda T_+} q(lambda (T_+^{i,'} - T_+)^+)], q(x) = x(e^x - 1),
where T_+^{i,'} resamples edge i only. INPUT: a general inequality for functions of one variable
with an independent copy. NO GEOMETRY. H-SAFE.

(S5) OPTIMIZER COMBINATORICS. (T_+^{i,'} - T_+)^+ > 0 forces e_i to lie in G_+(0,x) := the
intersection of ALL H-geodesics for the original weights. The survey's argument verbatim: if some
H-geodesic gamma avoids e_i, its passage time is unchanged by the resample, so T_+^{i,'} <=
T_+(gamma) = T_+ - contradiction. INPUT: existence of at least one optimizing path in the (finite,
localized) subgraph + subpath logic. H-SAFE VERBATIM - the argument never references edges outside
the optimizers' ambient graph, which is B* cap H throughout.

(S6) INCREMENT BOUND. (T_+^{i,'} - T_+)^+ <= tau'_{e_i} <= b (bounded weights; the resampled
geodesic-candidate uses the old geodesic, paying at most the new weight of e_i). INPUT: candidate-
path comparison. H-SAFE.

(S7) THE ONE GEOMETRIC INPUT: E exp(#G_+(0,x)/a) must be finite with the right growth. Here H is
STRICTLY EASIER than the full plane with general weights: for bounded weights on wall pairs,
#G_+(0,x) <= |any single H-geodesic| <= (b/a_w) r DETERMINISTICALLY (Claim 4 of the corner note,
refereed; a_w denotes the weight floor, kept distinct from the variational parameter).
[REPAIRED iter 98 per the combined referee: choose a = a0 CONSTANT (a0 = 1), NOT a = r. Then
log E exp(#G_+/a0) <= (b/a_w) r / a0 - linear in r at FIXED a0, exactly the role the survey's own
auxiliary lemma plays, still purely deterministic from Claim 4. The old a = r choice was S8's
bug - see below.] The survey needs an exponential-moment estimate for #G in the general-weights
case; WE NEED NOTHING RANDOM AT ALL. H-SAFE, supplied by the refereed lemma.

(S8) ASSEMBLY. [REPAIRED iter 98 - the combined referee found the original a = r choice collapses
the Gaussian t-range to a BOUNDED interval (the Chernoff optimizer exits the shrinking lambda
window at t = O(1)), so the printed range was NOT delivered; repair is the constant-parameter
choice, zero exponent cost, constants below are the referee's.] With a0 = 1: a0 E q(lambda tau')
<= 2 lambda^2 b^2 <= 1/2 for lambda <= 1/(2b) - a CONSTANT window, which is what the survey's own
(3.13) has and what a = r destroyed. Then
    Ent e^{lambda T_+} <= [a0 Eq/(1 - a0 Eq)] (b/a_w)(r/a0) E e^{lambda T_+}
                       <= 4 lambda^2 b^3 (r/a_w) E e^{lambda T_+},   lambda in (0, 1/(2b)).
Herbst + Chernoff deliver P(T_+ - E T_+ >= t sqrt(r)) <= exp(-a_w t^2 / (16 b^3)) for
t in (0, 4 b^2 sqrt(r)/a_w) - the claimed statement, now actually derived. INPUT: arithmetic.
H-SAFE.
[REF2, iter 154 - INDEPENDENT REFEREE: all four constants above CONFIRMED EXACT (reproduced
symbolically and again through a separate variance-proxy parameterization; the Gaussian and boundary
branches agree at the endpoint, both exp(-br/a_w)). It also re-derived the survey display from
entropy duality, so this walk no longer leans on the p.49 extraction at all.
AND IT IMPROVED THE RESULT, which is the deliverable worth having. Claim 4 bounds #G_+
DETERMINISTICALLY, so the variational step here is REDUNDANT: taking
    Ent <= Eq * (b/a_w) r * E = 2 lambda^2 b^3 (r/a_w) E   on the WIDER window lambda in (0, 1/b]
gives
    P(T_+ - E T_+ >= t sqrt(r)) <= exp( - a_w t^2 / (8 b^3) )   on the SAME range t in (0, 4b^2 sqrt(r)/a_w).
A FACTOR TWO BETTER - and, more important than the factor, it DELETES THE PARAMETER a whose
mis-setting (a = r) was the original defect this step was repaired for. The referee's phrasing is
worth keeping verbatim: the bug's mechanism is still in the architecture, merely set to a safe
value. Removing the parameter removes the mechanism.
PRECONDITION OMITTED AND NOW STATED: the q-linearization needs lambda <= 1/b.
DOWNSTREAM: every consumer quoting c = a_w/(16 b^3) may now quote a_w/(8 b^3); the corner note's
instantiation bracket is updated to match.]

(S9-a) ALL-DISTANCES BRANCH (added iter 98 per the combined referee's secondary finding: the
consumer's union bound spans ALL pair distances and the walk checked only the top scale). Split
at any fixed r*: [DEFECTIVE AS PRINTED - REF2 iter 154; the condition below is evaluated at b r*
where it must be b r, so this covering argument fails on exactly the small-r part it must cover.
Use the iter-116 bracket instead. Retained, marked, because a sampled excerpt of this line alone
must not read as correct:] for r <= r* the deterministic bound T_+ - E T_+ <= b r <= b r* empties the
deviation event once z sqrt(r) > b r*; for r > r*, (S8) applies. One sentence, closed.
[REF2 DEFECT, iter 154 - STRIKE THE CLAUSE ABOVE. The independent referee found it evaluates its
condition at b r* where it must be b r, so AS PRINTED it is a covering argument that fails precisely
on the small-r part it exists to cover. The correct statement is the iter-116 bracket immediately
below, which the referee confirmed independently; this sentence is superseded by it and is kept only
so the defect is visible rather than silently rewritten. The deterministic branch empties the event
for r < (z/b)^2, full stop.]
[OVERLAP MADE EXPLICIT with the repaired S8 constants, iter 116 - referee to confirm: the
deterministic branch empties the event for r < (z/b)^2; S8's range t < 4 b^2 sqrt(r)/a_w admits
t = z for r > (a_w z/(4 b^2))^2; the two overlap for every weight pair since
a_w/(4 b^2) < 1/b <=> a_w < 4b, always true. Coverage of ALL r at ANY z is therefore
UNCONDITIONAL - no smallness condition on the consumer's delta is needed, and the r* split
point may be taken anywhere in ((a_w z/(4b^2))^2, (z/b)^2), e.g. r* = z^2/(2b^2).]

(S9) RANGE CHECK AGAINST THE CONSUMER. The corner note's cost formula (its section 3) consumes
upper-tail deviations of T_+ at z = n^delta times sqrt-scale, with delta small and r ~ n^kappa:
z = n^delta << C2 sqrt(r) = C2 n^{kappa/2}. INSIDE the restricted range with room to spare. The
consumer never needs the tail beyond C sqrt(r).

(S10) DIRECTION AND UNIFORMITY. Constants depend on (a, b) only - uniform over wall pairs and over
the e_2 direction the note uses. The union bound in the note's section 3 needs nothing more.

## What this walk does NOT cover, said plainly

- The LOWER tail (the survey routes it through [59]). The note's I3 is the UPPER direction for
  T_+ (its cost formula needs T_+ not to exceed its mean by much, and the FREE time's lower
  deviations come from published full-plane concentration, input I2). So the lower tail of T_+ is
  NOT consumed and its absence costs nothing.
- General (unbounded) weights: (S7) leans on boundedness through Claim 4. The campaign is bounded-
  weights throughout, so this costs nothing here; it WOULD matter for any export beyond [a,b].
- Refereeing: every step above is labeled with its input, but no hostile referee has walked THIS
  walk. The natural attack surfaces: (S3)'s tensorization over a subgraph-indexed product (should
  be immediate; check the conditioning convention), (S5)'s "intersection of all geodesics" under
  non-uniqueness with a measurable selection (the survey handles it; check nothing changes in H),
  and the (S8) constant chase.
- SOURCE-FIDELITY CAVEAT: CLOSED (iter 98). The combined referee fetched a clean source - DHS
  arXiv:1401.0917 Appendix A quotes BLM Theorem 6.15 VERBATIM in exactly the form this walk
  consumes (direction of the positive part and the q function both match; the survey's variant
  shown equivalent by exchangeability). Receipts alongside the referee report. [Original caveat
  retained for the record: the survey was read through a lossy pypdf extraction; the logic stood
  on my own re-derivation but the exact lemma form needed a clean-copy check - now done.]

## Consequence if it survives refereeing

I3's status moves from "no obstruction identified" to "PROVED for bounded weights via the entropy
route, with the named QV gap BYPASSED rather than crossed" - and the corner note's input ledger
entry I3 becomes a citation to standard machinery plus Claim 4, with no unchecked adaptation left.
The corner route's condition set then rests on I8 alone among unpublished inputs (with I8 itself
carrying the v2 conditional reduction). The referee that checks this walk should also confirm the
lower-tail non-consumption claim in (S9)/(the note's section 3) - if the note's union bound ever
uses the lower tail of T_+, this walk is incomplete.
