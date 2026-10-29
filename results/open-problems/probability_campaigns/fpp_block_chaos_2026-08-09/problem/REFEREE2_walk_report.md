# Referee report 2: the I3 entropy walk's named attack surfaces, S8 as applied, and the
# iter-116 brackets (S9-a overlap; C1 section 3 instantiation)

Referee: independent, second pass. Everything below was re-derived from the definitions before
being compared with what the walk prints. Where I quote a file I mark it READ; where I derived a
thing myself I mark it DERIVED. Machine checks in `referee2_check.py`, transcript in
`referee2_check_output.txt` (same directory).

Notation as in the walk: weights iid in [a_w, b], 0 < a_w <= b; T_+ = passage time minimised over
paths confined to the closed half plane H = {x >= 0}; r = wall-pair distance; q(x) = x(e^x - 1).

## VERDICTS

| item | subject | verdict |
|---|---|---|
| 1 | S3 tensorization over the subgraph-indexed product | CONFIRMED |
| 2 | S5 intersection of all geodesics under non-uniqueness, in H | CONFIRMED |
| 3 | S8 constant chase as applied | CONFIRMED (constants exact; a strictly better one is available - see 3E) |
| 4 | S9-a iter-116 overlap bracket + C1 section 3 instantiation | CONFIRMED |
| 5 | text-level defects found | 3 minor, listed in section 6; none moves a constant or an exponent |

No arithmetic defect found. The repair the previous referee prescribed has been carried out
correctly and the four constants the walk prints -- 1/(2b), 4 lambda^2 b^3 (r/a_w),
a_w/(16 b^3), 4 b^2 sqrt(r)/a_w -- are each exactly what the definitions give.

--------------------------------------------------------------------------------------------------
## 1. (S3) TENSORIZATION OVER THE SUBGRAPH-INDEXED PRODUCT -- CONFIRMED

The convention that has to be checked is which variable is integrated and which are frozen.

CONVENTION (the only one that makes S4 usable): for a product measure mu = (x)_i mu_i on a finite
index set I and f >= 0 with E f log f < infinity,

    Ent_mu(f) <= Sum_{i in I} E[ Ent^{(i)}(f) ],
    Ent^{(i)}(f) := E^{(i)}[f log f] - E^{(i)}[f] log E^{(i)}[f],

where E^{(i)} integrates the i-th coordinate ONLY, all others held fixed. (DERIVED via the
duality Ent(f) = sup{E[fg] : E e^g <= 1} plus the Han/chain decomposition; the proof never
inspects what the index set means.) This is the convention under which, conditionally on the
other coordinates, T_+ is a function of the single variable tau_i and BLM 6.15 applies verbatim
with an independent copy tau'_i. The walk's "Ent_i" is this object. Convention correct.

Three H-specific checks, all pass:

(a) PRODUCT STRUCTURE IS NOT TOUCHED BY H. T_+ is defined as a minimum over the (fixed,
configuration-independent) set of H-paths. It is a deterministic function of the weights, not a
law conditioned on any event -- this is the only way the half-plane could have broken the product,
and it does not. The edge set of B* n H is a sub-collection of the edges of Z^2; the restriction
of a product measure to a sub-collection is a product measure. Entropy depends only on the law, so
Ent over the full product of a function of the sub-collection equals Ent over the sub-product, and
Ent^{(i)} = 0 for every i outside B* n H. The sum legitimately runs over the box's H-edges only.

(b) LOCALIZATION IS REAL, AND SURVIVES RESAMPLING (DERIVED). T_+ <= b r via the wall segment
(r edges, each <= b). Any H-path from (0,0) to (0,r) that visits a vertex at l1-distance R from
(0,0) has at least 2R - r edges, hence time at least a_w(2R - r); at R = 2(b/a_w) r this is
4br - a_w r > br. So minimisers lie in B* := the l1-ball of radius 2(b/a_w) r and T_+ equals its
localized version pointwise. The same holds after resampling any single edge, since tau'_i <= b
keeps the wall-segment bound T_+^{i,'} <= b r intact. This matters: without it, the finite sum is
not the whole entropy.

(c) THE COUNT AND THE SUM USE THE SAME INDEX SET. The tensorization sum runs over edges of
B* n H; G_+ (intersection of all H-geodesics) is contained in B* n H. No leakage either way.

One point worth recording because it is where a subgraph argument usually fails and here does not:
the box B* is DETERMINISTIC (it depends on r only, not on the configuration), so there is no
"random index set" and no conditioning on the geometry anywhere in the tensorization step.

Verdict: CONFIRMED. Nothing in the H-geometry breaks the product structure, and the conditioning
convention is the one S4 needs.

--------------------------------------------------------------------------------------------------
## 2. (S5) INTERSECTION OF ALL GEODESICS UNDER NON-UNIQUENESS, IN H -- CONFIRMED

Statement: (T_+^{i,'} - T_+)^+ > 0 implies e_i in G_+ := intersection of ALL H-geodesics of the
original configuration.

DERIVED. Suppose e_i is not in G_+; then some H-geodesic gamma avoids e_i. Resampling e_i leaves
every weight on gamma unchanged, and gamma is still an H-path, so
T_+^{i,'} <= T'(gamma) = T(gamma) = T_+, i.e. the positive part is 0. Contrapositive gives the
claim. Uniqueness is never used; the quantifier order is exactly what intersection-membership
negates.

NON-UNIQUENESS CUTS THE FAVOURABLE WAY. More geodesics means a SMALLER intersection, hence a
smaller #G_+, hence a smaller entropy bound. Non-uniqueness cannot hurt this argument -- it can
only help. (Contrast with any argument that needs "the" geodesic, which is where selection is
normally required.)

NO MEASURABLE SELECTION IS NEEDED, IN H OR ANYWHERE. G_+ is defined by an intersection, and
membership has a closed measurable form in the localized problem:
    e in G_+  <=>  T_+^{avoid e} > T_+,
where T_+^{avoid e} is the minimum over the finitely many H-paths in B* that omit e (a min of
finitely many continuous functions of the weights, hence continuous; the strict inequality set is
Borel). So #G_+ is measurable with no convention at all. The corner note's fixed-selection
convention (C1 section 0) is compatible and simply idle here -- this referee agrees with the prior
report on that point, and adds that the walk does not even need it to be stated.

WHAT CHANGES IN H: nothing, and the direction of the difference is worth naming. In the full
plane the survey needs existence of a minimiser and (for general weights) a genuinely random
exponential-moment bound on the geodesic count. In H with localization, the minimiser exists
because the H-path set inside B* is finite and non-empty (the wall segment is an H-path, both
endpoints having x = 0, and H is closed). Every object quantified over -- gamma, T_+^{i,'}, G_+ --
lives in B* n H; no edge outside H is ever referenced. H is strictly easier, not merely equal.

S6, re-derived while here: if T_+^{i,'} > T_+ then e_i lies on every original H-geodesic gamma,
and gamma is self-avoiding (weights >= a_w > 0), so
T'(gamma) = T_+ - tau_i + tau'_i <= T_+ + tau'_i, giving (T_+^{i,'} - T_+)^+ <= tau'_i <= b. The
walk's choice of the bound tau'_i rather than the tighter (tau'_i - tau_i)^+ is not sloppiness: it
is what preserves independence from sigma(tau), which the decoupling step consumes. Correct as
written.

Verdict: CONFIRMED.

--------------------------------------------------------------------------------------------------
## 3. (S8) THE CONSTANT CHASE AS APPLIED -- CONFIRMED, ALL FOUR CONSTANTS

I re-derived the whole chain rather than checking the repair for plausibility. Write
U := e^{lambda T_+}, M := (b/a_w) r.

### 3A. The per-edge sum and the decoupling (DERIVED)

Tensorize, apply BLM 6.15 conditionally, use S5 + S6 + monotonicity of q on [0,infinity) with
q(0) = 0:

    Ent(U) <= Sum_i E[ U q(lambda (T_+^{i,'} - T_+)^+) ] <= Sum_i E[ U q(lambda tau'_i) 1{e_i in G_+} ].

tau'_i is independent of the whole original configuration, while U and 1{e_i in G_+} are
sigma(tau)-measurable, so the product factorises exactly and, summing,

    Ent(U) <= E q(lambda tau') . E[ U . #G_+ ].                                        (*)

q monotone on the positive half line: q'(x) = e^x - 1 + x e^x >= 0. Verified symbolically and on a
grid.

### 3B. The q estimate: E q(lambda tau') <= 2 lambda^2 b^2 -- CORRECT

For x in [0,1], e^x - 1 <= (e-1)x, so q(x) <= (e-1) x^2 < 2 x^2. With x = lambda tau' <= lambda b
and lambda <= 1/b this gives q(lambda tau') <= 2 lambda^2 tau'^2 <= 2 lambda^2 b^2.
Machine check: sup_{(0,1]} q(x)/x^2 = e - 1 = 1.71828... <= 2. On the window actually used,
lambda tau' <= 1/2, the true sup is 1.29744, so the printed 2 is safe with room.
The walk's window lambda <= 1/(2b) implies lambda <= 1/b, so the linearisation's own precondition
is met. (The walk does not state that precondition; see minor 6.3.)

### 3C. The survey display, re-derived so the walk need not lean on the extraction

The step the walk imports from the survey, Ent <= [aEq/(1-aEq)] log E exp(#G_+/a) E U, is not a
quotation-dependent fact. DERIVED from (*) by entropy duality: for any V with E e^V < infinity,
E[UV] <= Ent(U) + E[U] log E e^V. Take V = #G_+/a:

    E[U . #G_+] <= a( Ent(U) + E[U] log E exp(#G_+/a) ),
    Ent(U) <= aEq . Ent(U) + aEq . E[U] log E exp(#G_+/a),
    Ent(U) <= [aEq/(1 - aEq)] . log E exp(#G_+/a) . E[U]     provided aEq < 1.

So the display is correct for every a > 0 with a E q < 1. The fidelity of the survey extraction at
p.49 is therefore not load-bearing.

### 3D. Assembly with a0 = 1 -- the walk's three printed constants are EXACT

- a0 E q <= 2 lambda^2 b^2, and at lambda = 1/(2b) this equals exactly 1/2. So a0 E q <= 1/2 on
  the window, hence A/(1-A) <= 2A <= 4 lambda^2 b^2. CORRECT as printed.
- log E exp(#G_+/a0) <= M/a0 = (b/a_w) r, deterministically from Claim 4 (#G_+ <= |any single
  H-geodesic| <= T_+/a_w <= b r/a_w). CORRECT as printed.
- Ent(U) <= 4 lambda^2 b^2 . (b/a_w) r . E U = 4 lambda^2 b^3 (r/a_w) E U on lambda in (0, 1/(2b)).
  CORRECT as printed; verified symbolically (coefficient equals 4 b^3 r/a_w identically).

Herbst (DERIVED, not quoted): with F(lambda) = E e^{lambda T_+}, psi = log F,
K(lambda) := psi(lambda)/lambda has K'(lambda) = Ent(U)/(lambda^2 F) <= C := 4 b^3 r/a_w, and
K(0+) = E T_+, so psi(lambda) <= lambda E T_+ + C lambda^2 on (0, 1/(2b)). F is finite and smooth
because T_+ is bounded, so the differentiation is legitimate.

Chernoff (DERIVED): P(T_+ - E T_+ >= u) <= exp(C lambda^2 - lambda u), optimiser
lambda* = u/(2C) = a_w u/(8 b^3 r), value exp(-u^2/(4C)) = exp(-a_w u^2/(16 b^3 r)), admissible iff
lambda* < 1/(2b), i.e. iff u < C/b = 4 b^2 r/a_w. Substituting u = t sqrt(r):

    P(T_+ - E T_+ >= t sqrt(r)) <= exp(- a_w t^2 / (16 b^3)),   t in (0, 4 b^2 sqrt(r)/a_w).

Both constants reproduce symbolically. So C1 = a_w/(16 b^3) and C2 = 4 b^2/a_w are CONFIRMED, and
the range is genuinely the sqrt-scale one (it grows like sqrt(r)) -- the defect the first referee
found is really gone, not merely relabelled.

Sanity (the direction a wrong constant would betray): on a degenerate toy where the "geodesic" is
a fixed path of m edges, the chain returns psi_c(lambda) <= 2 b^2 m lambda^2, which must be WEAKER
than the exact log-mgf of a sum of m bounded iid weights. It is: for weights on {1,2}, m = 40, the
exact psi_c never exceeds the bound (max difference -3.1e-6 at the smallest lambda tested, the
bound being loose by ~64x). A constant that was too small would have shown up here as a positive
gap.

### 3E. CORRECTED (improved) CONSTANT: c = a_w/(8 b^3) on the SAME range

The walk's constants are valid but not what the argument actually gives. Because Claim 4 bounds
#G_+ DETERMINISTICALLY, step 3C is unnecessary: from (*) directly,

    Ent(U) <= E q(lambda tau') . M . E[U] <= 2 lambda^2 b^2 . (b/a_w) r . E[U] = 2 lambda^2 b^3 (r/a_w) E[U],

valid on the wider window lambda in (0, 1/b] (only the q-linearisation constrains lambda now; the
constraint a E q < 1 disappears with the parameter a). Herbst + Chernoff then give

    P(T_+ - E T_+ >= t sqrt(r)) <= exp(- a_w t^2 / (8 b^3)),   t in (0, 4 b^2 sqrt(r)/a_w),

- the same t-range, with the exponent constant improved by a factor 2. Verified symbolically
alongside the walk's version.

This is not merely a better number. The parameter a is the exact object whose mis-setting (a = r)
was the original defect; the repaired walk keeps it, so the mechanism of that bug is still present
in the architecture even though the value is now safe. Deleting the variational step removes the
parameter entirely and makes the step un-mis-settable. Recommended for v4, with the walk's own
sentence "WE NEED NOTHING RANDOM AT ALL" (S7) as the justification -- that sentence is precisely
the reason the variational step is redundant here, and the walk does not notice it.

If the walk prefers to stay parallel to the survey's architecture, its printed constants stand as
correct; nothing downstream needs changing, since C1 quotes c symbolically.

Verdict: CONFIRMED as printed; improved constant available.

--------------------------------------------------------------------------------------------------
## 4. (S9-a) THE ITER-116 OVERLAP BRACKET, AND THE C1 SECTION 3 INSTANTIATION -- CONFIRMED

### 4A. The two branches, each re-derived

DETERMINISTIC BRANCH. T_+ <= b r (wall segment) and E T_+ >= a_w r (every H-path between the pair
has at least r edges), so T_+ - E T_+ <= (b - a_w) r <= b r pointwise. The event
{T_+ - E T_+ >= z sqrt(r)} is therefore EMPTY as soon as b r < z sqrt(r), i.e.

    r < (z/b)^2.                                                          [walk's figure: correct]

S8 BRANCH. The Gaussian statement admits t = z iff z < 4 b^2 sqrt(r)/a_w, i.e.

    r > (a_w z/(4 b^2))^2.                                                [walk's figure: correct]

### 4B. The overlap -- CORRECT, and unconditional

    (a_w z/(4 b^2))^2 < (z/b)^2   <=>   a_w/(4 b^2) < 1/b   <=>   a_w < 4b,

which holds for every admissible weight pair since a_w <= b < 4b. The ratio of the two thresholds
is a_w^2/(16 b^2) <= 1/16, so the overlap is not marginal: the two branches share at least a
factor-16 window in r, for every (a_w, b) and every z > 0. Both z and r have dropped out of the
condition -- this is why the coverage is unconditional. Verified symbolically and by a sweep over
(a_w, b, z) spanning six orders of magnitude in each: no failures.

INTEGER CHECK, which the walk does not make and should (one line, and it passes). The union runs
over integer distances r >= 1, while the overlap argument is stated for real intervals. If
(z/b)^2 <= 1 the deterministic branch covers no integer at all; but then z <= b, so the S8 floor
is (a_w z/(4b^2))^2 <= (a_w/(4b))^2 <= 1/16 < 1 and S8 alone covers every integer r >= 1. So every
integer r >= 1 is covered at every z > 0. Confirmed numerically in the same sweep.

SPLIT POINT. r* = z^2/(2b^2) lies in ((a_w z/(4b^2))^2, (z/b)^2): the upper side is immediate
(ratio 2), the lower side needs a_w^2 < 8 b^2, i.e. a_w < 2 sqrt(2) b, weaker than a_w <= b. The
walk's example is valid.

### 4C. No smallness condition on delta -- CONFIRMED, with one distinction the bracket should keep

The coverage condition a_w < 4b involves neither z nor r. Since z = n^delta enters only through
those thresholds, NO upper bound on delta is required for the union in C1 section 3 to be covered
at every pair distance. That is exactly what the bracket claims, and it is right.

Distinction worth stating in one clause, because "no condition on delta" can be misread: C1's
union bound still needs exp(-c z^theta) to beat the C h^2 + C h^4 = poly(n) pair count, which
requires delta > 0 STRICTLY (with theta = 2, n^{2delta} >> log n). That is a positivity
requirement from C1's own counting, not a smallness requirement from the walk, and it is already
implicit in C1 section 7's "with beta, eps, delta > 0 fixed" (line 293). The two must not be
conflated. The walk's S9 separately observes delta << kappa/2 for the top scale; with the
program's kappa in [0.65, 0.75] (C1 section 7.4) and delta near 0 that holds with room, and in any
case it is no longer needed for coverage -- if delta ever exceeded kappa/2, the deterministic
branch would cover the top scale instead.

### 4D. The instantiation bracket in C1 section 3 -- EXACT MATCH

C1 line 145-152 requires, uniformly over wall pairs at distance r,
    P( T_+(p,q) > E T_+(p,q) + z S_+(r) ) <= C exp(-c z^theta),
and instantiates S_+(r) = sqrt(r), theta = 2, C = 1, c = a_w/(16 b^3).

Against the walk's delivered statement, term by term:
- S_+(r) = sqrt(r): matches the walk's deviation scale t sqrt(r) at t = z.                     OK
- theta = 2: the walk's exponent is quadratic in t.                                            OK
- c = a_w/(16 b^3): identical to the re-derived C1 of section 3D above.                        OK
- C = 1: the walk's bound carries no prefactor, and the deterministic branch contributes
  probability 0 <= 1 . exp(-c z^2). So C = 1 is correct on BOTH branches.                      OK
- ">" vs ">=": C1 asks for the open event, the walk bounds the closed one; the closed event
  contains the open one, so the walk's bound is the stronger of the two.                       OK
- uniformity over wall pairs: constants involve only (a_w, b); H is invariant under translation
  along the wall, so the law of T_+(p,q) depends on r alone, and by C1 Claim 2 every consumed
  pair is axis-directed with both endpoints on the wall.                                       OK

If the improved constant of 3E is adopted, C1's bracket becomes c = a_w/(8 b^3); C1 quotes c
symbolically and nothing else downstream changes.

ROBUSTNESS TO HOW C1 READS ITS OWN UNION. C1 line 146 applies the tail at each pair's own r and
then uses monotonicity to evaluate the assembled bound at R; a reader could instead apply the tail
at the common deviation z S_+(R) for every pair. I checked the second reading too, because it is
the one that could push t OUT of the range for small r: there t = z sqrt(R/r), the S8 branch needs
r > a_w z sqrt(R)/(4 b^2), the deterministic branch empties for r < z sqrt(R)/b, and the overlap
condition is again a_w < 4b, with exponent exp(-a_w t^2/(16 b^3)) <= exp(-a_w z^2/(16 b^3)) since
t >= z. Both readings are covered by the same algebra, so the bracket does not depend on which one
C1 intends.

Verdict: CONFIRMED.

--------------------------------------------------------------------------------------------------
## 5. LOWER TAIL OF T_+ -- independently re-swept, CONFIRMED NOT CONSUMED

Not in this brief's five items, but the walk asks its referee to confirm it, and it is one of the
walk's own "not covered" entries, so I swept C1 myself rather than inheriting the prior report's
sweep. Every probability statement in C1_corner_route_attempt_iter60.md was enumerated
(lines 84, 146, 157, 352, 364-365). The only two tails consumed are the pair at line 146:
P(T < E T - z S(r)) (free time, LOWER, published input I2) and P(T_+ > E T_+ + z S_+(r))
(confined time, UPPER, input I3). No occurrence of a lower deviation of T_+ anywhere in the file;
line 364's probability is a geodesic-touching event, not a passage-time tail, and line 84's is the
already-assembled event. The walk's non-consumption claim is true, and its non-coverage of the
lower tail costs the consumer nothing.

--------------------------------------------------------------------------------------------------
## 6. MINOR DEFECTS (text-level; none moves a constant or an exponent)

6.1 S9-a's ORIGINAL (iter-98) SENTENCE IS MISSTATED AND SHOULD BE STRUCK. It reads: "for r <= r*
the deterministic bound T_+ - E T_+ <= b r <= b r* empties the deviation event once
z sqrt(r) > b r*". The implication is true pointwise but the CONDITION is evaluated at the wrong
place: for r <= r* the quantity z sqrt(r) is smallest at small r, so "z sqrt(r) > b r*" fails
precisely on the small-r part of the branch it is meant to cover. The correct per-r condition is
z sqrt(r) > b r, i.e. r < (z/b)^2 -- which is what the iter-116 bracket states two sentences
later. As printed the step contains a covering argument that does not cover, immediately followed
by one that does. Strike the first clause or replace "b r*" by "b r".

6.2 S9's "INSIDE the restricted range with room to spare" is true only at the top scale. At
r = O(1) the deviation z = n^delta is far OUTSIDE (0, C2 sqrt(r)) and it is S9-a, not S9, that
carries the pair. S9 reads as though the range check were already discharged. Add the four words
"at the top scale", or move S9-a after S9 so the reader meets the general statement first.

6.3 The q-linearisation's precondition (lambda tau' <= 1, i.e. lambda <= 1/b) is used but not
stated in S8. It is implied by the printed window lambda <= 1/(2b), so nothing is wrong; but it is
the hypothesis that pins the window's SHAPE, and a reader re-optimising the window (as 3E does)
needs it visible. One clause.

6.4 Slack worth naming, not a defect: the deterministic ceiling is (b - a_w) r, not b r, since
E T_+ >= a_w r. Using it widens the deterministic branch from r < (z/b)^2 to r < (z/(b-a_w))^2 and
makes the overlap larger still. The walk's cruder figure is what the bracket's algebra uses, so
the printed overlap claim stands as verified; the remark only says the margin is bigger than
claimed.

--------------------------------------------------------------------------------------------------
## 7. SUMMARY FOR THE LEDGER

The iter-98 repair is correct as executed. Re-derived independently from the definitions, the
walk's S8 delivers exactly

    P(T_+ - E T_+ >= t sqrt(r)) <= exp(- a_w t^2/(16 b^3)),   t in (0, 4 b^2 sqrt(r)/a_w),

and the iter-116 overlap bracket closes all pair distances unconditionally in both z and delta.
The C1 section 3 instantiation (S_+ = sqrt(r), theta = 2, C = 1, c = a_w/(16 b^3)) matches the
without change, and S5 is strictly easier in H than in the full plane (finiteness gives existence;
the intersection formulation needs no measurable selection at all).

Two things I would put in v4: the strictly better constant a_w/(8 b^3) on the same range, obtained
by deleting the variational step that the deterministic Claim 4 makes redundant -- which also
removes the parameter a whose mis-setting was the original defect -- and the three text fixes in
section 6, of which 6.1 is the one that currently prints a covering argument that does not cover.

Machine transcript: referee2_check_output.txt. Script: referee2_check.py.

