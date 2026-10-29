# (C1) corner lemma, iteration 60: a confinement route that does NOT pay the wandering scale

STATUS BANNER (added iter 69 by the author). This file was written by an agent that died on
the session limit at 22:34; the file is complete (ends with section 9.4 as designed) and is
SALVAGED - NOW REFEREED (iter 80/81: sections 0-8 ACCEPT, section 9 MAJOR, corrections applied
in place throughout; full report C1_corner_route_REFEREE_iter72.md). Original banner text follows.
What I have verified by hand (iter 69): Claims 1, 2, 3, 5, 6 are correct as
written (all elementary - l1 geometry, subpath optimality, reflection exchangeability, the exact
split, Efron-Stein with Claim 4's edge count); the 7.3 cross-check is EXACT symbolically, not just
to six digits ((1+alpha)^2/(2(2+alpha)) = alpha reduces to alpha^2 + 2alpha - 1 = 0); the 7.4 table
arithmetic checks. NOT verified: I3 (confined-time concentration, flagged by the author itself as
the second-most-likely error) and I8 (the open input P2 <= C sqrt(l) log l, on which every
conclusion is conditional). Sections 9.1-9.4 not yet adversarially checked. Needs a hostile referee
when agent capacity returns at 1am.

RECONCILIATION WITH ITER 68 (the two crossed in flight - this note cites 3b's "exclude each other by
0.08", which was superseded hours after this agent launched). The iter-68 refereed correction says:
within the hypothesis set the envelope exponent is PINNED to the true fluctuation exponent,
alpha = chi (chaos needs alpha <= chi, concentration at scale Q forces alpha >= chi). Combining with
THIS note's conditional threshold (corner closes iff alpha > 1/3):

  THE PACKAGE ASSEMBLES IFF chi > 1/3   (conditional on I8, I3, and the standing hypothesis set).
  [QUALIFIED iter 80/81 per referee: the IFF is PACKAGE-RELATIVE only - relative to this hypothesis
  set and these routes; a different route could in principle assemble below 1/3. And the interval
  is OPEN at the top: chi in (1/3, 1/2), since assembly AT chi = 1/2 self-refutes (linear variance
  contradicts the sublinear conclusion). Quote as: "package-relatively, assembles exactly for
  chi in (1/3, 1/2)".]

Three regimes. If chi = 1/3 (KPZ, the conjectured truth): alpha = 1/3 and the corner fails AT the
point by an arbitrarily small polynomial - the routes meet and still do not overlap. If chi in
(1/3, 0.4142]: this route's window is NON-EMPTY where the old shift route's was empty - the
conditional structural picture CHANGES from "disjoint under chi <= 0.414" to "assembles precisely
when chi > 1/3". If chi in (0.4142, 1/2]: both routes close. Stated plainly: conditional on the
one-wall Alexander bound, this program proves sublinear variance exactly in the worlds where the
conjectured value chi = 1/3 is FALSE in the upward direction - it can never confirm KPZ, only
exploit its failure. Nothing unconditional excludes chi in (1/3, 1/2], so that world is live.

VERDICT (stated first, details below). CONDITIONAL BEAT, with the condition named exactly.
The route removes W_s from the RANDOM half of the cost unconditionally, and reduces ALL that
remains to a single DETERMINISTIC number: the expected gain a path gets from being allowed to
cross the wall,
    P2(l) := E[ min(T_+, T_-) ] - E[ T ]  >= 0   for the two wall endpoints at distance l.
If P2(l) <= C sqrt(l) log l -- the one-wall analogue of Alexander's PUBLISHED free-FPP rate -- the
corner cost is l^{1/2 + o(1)} and the threshold is alpha > 1/3, replacing alpha > sqrt(2)-1.
I HAVE NOT PROVED THAT BOUND. It is the single hardest open piece of this note and section 6.4
says plainly what is and is not known about it. Everything else here is proved or is a routine
adaptation of a published argument, and is labelled as such in the ledger (section 8).
Unconditionally the note proves: (i) the random half of the cost is sqrt(l) n^{o(1)}, no wandering
input, no angular window; (ii) MEANGAP = Part1 + P2 with Part1 <= C sqrt(l) unconditionally; and
(iii) three negative results (section 9) [DOWNGRADED per corner referee, iter 80/81: 9.1's
class-wide pin is NOT delivered as displayed (s unbound, chaining floor missing, wandering-lower
input unstated), so "every pathwise route is pinned" is FALSE AS WRITTEN and weakens to: THE ROUTES
EXAMINED - the shift, its mean version, reflection folding, excursion repair - are pinned at W_l or
worse. The mean/fluctuation split remains the only escape KNOWN TO US, not the only one possible.]

RESULTING THRESHOLD. With cost exponent gamma (defined below) the criterion is
    alpha > gamma / (2 - gamma)   (at beta = eps = delta = 0),
    exactly:  alpha > (1 + 2 beta + 4 delta + 12 eps) / 3 when gamma = 1/2.
On PUBLISHED, Kesten-scale inputs gamma = 1/2 and the threshold is alpha > 1/3, replacing the
refereed alpha > sqrt(2) - 1 = 0.4142 of the shift route. The two obstacles of CRUX section 3b
therefore MEET at alpha = 1/3 instead of excluding each other by 0.08; they still do not overlap,
because 1/3 is excluded by a strict inequality (an arbitrarily small polynomial in n).
[ANNOTATED IN PLACE, iter 69: this paragraph was written against the PRE-iter-68 form of 3b. The
refereed current form pins alpha = chi (nature's exponent), so the correct statement is: the package
assembles iff chi > 1/3, fails marginally at KPZ's chi = 1/3, and the old 0.08 exclusion applied
only to the superseded shift route. See the RECONCILIATION block in the banner above.]
At envelope-scale inputs gamma = alpha the criterion is alpha < 1, i.e. it closes everywhere.

CROSS-CHECK OF THE ARITHMETIC MACHINERY. The same budget computation applied to the shift route's
cost exponent (1+alpha)/(2+alpha) reproduces the referee's alpha^2 + 2 alpha - 1 > 0 exactly (see
section 7.3). The two routes differ only in the cost exponent: 1/2 versus (1+alpha)/(2+alpha), and
1/2 is strictly smaller for every alpha > 0.

--------------------------------------------------------------------------------------------------
## 0. Conventions

Z^2 bond FPP, iid weights omega(e) in [a,b], 0 < a <= b < infinity, non-degenerate (a < b; the case
a = b is trivial since then T_Lambda = T for all pairs in the box). d = l1 distance. g = time
constant (a norm on R^2, defined by lattice paths, no rotation used anywhere). Lambda = {0 <= x <= n},
T_Lambda the passage time over paths confined to Lambda. H := {x >= 0}, T_+ := T_H the passage time
over paths confined to H; H^- := {x <= 0}, T_- := T_{H^-}. Envelope Q_r = r^alpha, W_r = sqrt(r Q_r)
= r^{(1+alpha)/2}. Corner box B = [0,h] x [-2h,2h], h = n^beta W_n = n^{beta + (1+alpha)/2}. Target:
    max_{u,v in B} [ T_Lambda(u,v) - T(u,v) ] <= n^{-3 eps} Q_n = n^{alpha - 3 eps}
off an event of probability exp(-4 n^{theta_1}).
Throughout, kappa := beta + (1+alpha)/2, so h = n^kappa and l := d(u,v) <= 5h.
Geodesics: fix any measurable selection (ties broken by a fixed rule); nothing below uses uniqueness.

READ = taken from C1_corner_lemma_draft.md or CRUX_iteration_arithmetic.md. DERIVED = mine.
Established and not re-derived, per instruction: (D1) any pointwise bound B on the one-block
increment is Theta(n); (D3) max_j |gamma cap Lambda_ij| >= c' W for every geodesic in every
configuration. Neither is used or contradicted below: this note never resamples a block and never
bounds a block occupation.

--------------------------------------------------------------------------------------------------
## 1. Step 1 (DERIVED, deterministic): the corner problem is a HALF-PLANE problem

CLAIM 1. For u,v in B with h <= n/(20 b/a), every path used below stays in {x <= n}, and
    T_Lambda(u,v) - T(u,v) <= T_+(u,v) - T(u,v).
Proof. T(u,v) <= b*d(u,v) <= 5bh (monotone staircase inside the bounding box of u,v, which lies in
B and hence in Lambda), so any geodesic gamma from u to v has |gamma| <= (b/a) 5h edges and stays
within l1-distance 5(b/a)h of u; likewise the H-confined geodesic, since T_+(u,v) <= b d(u,v) too
(the staircase can be taken inside H: both endpoints have x >= 0, and a monotone staircase between
them has all x-coordinates between those of u and v). Hence all paths considered have
x <= h + 5(b/a)h < n, so confinement to Lambda is implied by confinement to H. QED.
h < n requires kappa < 1, i.e. beta < (1-alpha)/2 -- satisfied in the program's range
(alpha <= 1/2, beta < 1/4). CONSUMES: l1 geometry, boundedness. No probability, no window.

Consequence: the right wall of the column is irrelevant to (C1) on Z^2, and the single wall x = 0
is a reflection axis of the lattice. That is what makes section 4 available.

--------------------------------------------------------------------------------------------------
## 2. Step 2 (DERIVED, deterministic): first-exit / last-return surgery kills the arbitrary
##         direction and lands on AXIS-DIRECTED wall pairs

CLAIM 2. For every u,v in B and every configuration, either the free geodesic gamma from u to v
lies in H (and then T_+(u,v) = T(u,v)), or there exist vertices p = (0,y_1), q = (0,y_2) on the
wall with d(p,q) <= |gamma| <= 5(b/a) h such that
    T_+(u,v) - T(u,v)  <=  T_+(p,q) - T(p,q).
Proof. Let t1 be the first time gamma leaves H and t2 the last; the vertex of gamma immediately
before t1 has x = 0 (to reach x <= -1 from x >= 0 one traverses the edge {(0,y),(-1,y)}), call it p;
the vertex immediately after t2 likewise has x = 0, call it q. By construction gamma[u->p] and
gamma[q->v] lie in H. Concatenating gamma[u->p], an H-geodesic from p to q, and gamma[q->v] gives an
H-path from u to v, so
    T_+(u,v) <= T(gamma[u->p]) + T_+(p,q) + T(gamma[q->v]) = T(u,v) - T(gamma[p->q]) + T_+(p,q),
and T(gamma[p->q]) = T(p,q) by subpath optimality. QED.
CONSUMES: subpath optimality, concatenation. No probability, no window.

WHY THIS MATTERS. q - p is a multiple of e_2. The arbitrary relative direction of (u,v) -- the
feature that forced the draft's L3 to consume H1a, H1b, H1c with their angular windows REMOVED
(referee correction 2) -- is discharged deterministically here. Every probabilistic input from now
on is consumed at the single lattice direction e_2. This repairs referee correction 2 for the route
below: no all-direction hypothesis, no window, no curvature at any direction.

--------------------------------------------------------------------------------------------------
## 3. Step 3 (DERIVED): mean / fluctuation split -- where the wandering scale disappears

For a wall pair p,q at distance r write
    T_+(p,q) - T(p,q) = [T_+ - E T_+] + [E T - T] + MEANGAP(p,q),   MEANGAP := E T_+ - E T >= 0.
The first two terms are deviations of two passage times around their own means; the third is a
DETERMINISTIC number. This is the whole trick. The shift construction pays W_s because it must
place a path at distance D from the wall and D must dominate the transversal deviation; here no
path is ever exhibited -- T_+ is confined by definition -- and the only geometric quantity left is
a difference of expectations, which no wandering lower bound can obstruct (section 8.1).

COST FORMULA. Let S(r) and S_+(r) be scales such that, with z = n^delta,
    P( T(p,q) < E T(p,q) - z S(r) ) and P( T_+(p,q) > E T_+(p,q) + z S_+(r) )
are each <= C exp(-c z^theta), uniformly over wall pairs at distance r. [CANDIDATE
INSTANTIATION for the T_+ half - the walk's referee has now RETURNED (iter 154) and CONFIRMED this
bracket, including the deterministic branch; the constant IMPROVES to c = a_w/(8 b^3), a factor two
better, because Claim 4's deterministic bound on #G_+ makes the walk's variational step redundant.
Both values are recorded: as instantiated at iter 116, c = a_w/(16 b^3); as improved by the
referee, c = a_w/(8 b^3). Consumers may quote the improved one:
S_+(r) = sqrt(r), theta = 2, C = 1, c = a_w/(8 b^3) - the repaired S8 of I3_entropy_route_walk_iter86.md, whose
S9-a split covers ALL pair distances r at this z unconditionally (overlap algebra a_w < 4b,
made explicit there iter 116). The T half is published (I2). Abstract form kept here;
constants live with their supplier.] Then, taking a union bound
over the at most C h^2 wall pairs in range and the at most C h^4 pairs (u,v) (all polynomial in n,
killed by exp(-c n^{delta theta})),
    max_{u,v in B} [T_Lambda(u,v) - T(u,v)] <= z [ S(R) + S_+(R) ] + max_{r <= R} MEANGAP(r),
    R := 5(b/a) h,
off an event of probability exp(-c n^{delta theta}); set theta_1 := delta theta.
S, S_+ and MEANGAP are non-decreasing in r, so evaluating at R is legitimate.

--------------------------------------------------------------------------------------------------
## 4. Step 4 (DERIVED): reflection as an EXACT conditional identity, and an unconditional
##         sqrt(l) bound on half of the mean gap

The wall line x = 0 carries vertical edges that belong to both H and H^-; let F be the sigma-field
they generate. The map R(x,y) = (-x,y) is a lattice automorphism fixing every wall vertex and every
wall vertical edge, and mapping the non-wall edges of H bijectively onto the non-wall edges of H^-.
Since the weights are iid:

CLAIM 3 (conditional exchangeability). For p,q on the wall, conditionally on F the pair
(T_+(p,q), T_-(p,q)) is exchangeable, and in fact T_+ and T_- are conditionally iid. Hence
T_+ - T_- is conditionally symmetric and E T_+ = E T_-.
CONSUMES: the lattice reflection in the axis x = 0 and independence. No rotation, no window.

CLAIM 4 (deterministic bounds at the wall). For p,q on the wall at distance r: the wall segment
joining them lies in H and in H^-, so T_+ <= b r, T_- <= b r, and every geodesic (free, +, or -)
between them has at most (b/a) r edges; also T_+ - T_- <= (b-a) r. (Same diameter argument as the
refereed occupation lemma of CRUX section 5, in its simplest case -- consistent with it, READ.)

CLAIM 5 (exact split of the mean gap). Using T_+ = min(T_+,T_-) + (T_+ - T_-)^+ and Claim 3,
    MEANGAP(r) = E T_+ - E T = (1/2) E|T_+ - T_-|  +  P2(r),
    P2(r) := E[min(T_+,T_-)] - E[T]  >= 0    (the EXPECTED MIXING GAIN: what a path gains by being
    allowed to cross the wall, over the better of the two one-sided options).

CLAIM 6 (Part 1 is unconditionally sqrt-scale). Var(T_+(p,q)) <= (b-a)^2 (b/a) r, hence
    (1/2) E|T_+ - T_-| <= (1/2) sqrt(E (T_+-T_-)^2) = (1/2) sqrt(2 E[Var(T_+ | F)])
                       <= (1/2) sqrt(2 Var(T_+)) <= C_1 sqrt(r),  C_1 = (b-a) sqrt(b/(2a)).
Proof of the variance bound: Efron-Stein, Var(T_+) <= (1/2) sum_e E[(T_+ - T_+^{(e)})^2]; resampling
one edge moves T_+ by at most (b-a) and only if e lies on the +geodesic of one of the two
configurations, so the sum is at most 2 (b-a)^2 E|gamma_+| <= 2 (b-a)^2 (b/a) r by Claim 4.
CONSUMES: Efron-Stein, boundedness, Claim 4. Unconditional. No window. This is the exact point at
which the reflection earns something: without Claim 3 the difference of the two one-sided times
would have no reason to be centred, and its size would not be a variance.

[STRUCK per corner referee, iter 80/81 - FALSE without a kurtosis input; referee counterexample
in C1_corner_route_REFEREE_iter72.md. The step E|T_+ - T_-| >= c sqrt(E(T_+ - T_-)^2) runs the
moment inequality BACKWARDS: a first moment does not dominate the root-second-moment without
anti-concentration control. The floor claim is withdrawn; nothing downstream consumed it.]
Original text: Note also the FLOOR: MEANGAP(r) >= (1/2)E|T_+ - T_-| >= c sqrt(E Var(T_+|F)), which
under the program's own H3-lower (variance at envelope scale) is >= c Q_r. So the route cannot ever
cost less than Q_r -- and Q_r is inside the budget (section 7), so the target is not vacuous.

--------------------------------------------------------------------------------------------------
## 5. Step 5 (DERIVED): what is left is ONE deterministic number, in three equivalent forms

After Claims 1-6 the entire corner obligation is
    cost <= z [S(R) + S_+(R)] + C_1 sqrt(R) + P2(R),    R = 5(b/a) h,
with the first three terms at sqrt scale unconditionally (section 8). The residue P2 admits three
equivalent formulations; each is a statement about EXPECTATIONS only, with both endpoints on the
wall and the direction always e_2.

(F1) MIXING GAIN. P2(l) = E[min(T_+,T_-)] - E[T] <= ? sqrt(l) polylog.
(F2) ONE-WALL NONRANDOM FLUCTUATION. A_+(l) := E T_+((0,0),(0,l)) - g(l e_2). Then
     A_+ = MEANGAP + A, where A(l) := E T - g(l e_2) >= 0 is the FREE nonrandom fluctuation, which
     Alexander's published theorem bounds by C sqrt(l) log l. With Claim 6, (F1) at sqrt scale is
     EQUIVALENT to A_+(l) <= C sqrt(l) log l.
(F3) RATE OF g_+ = g. The one-wall time constant g_+ := lim a_l / l (a_l := E T_+((0,0),(0,l)),
     subadditive by concatenation at wall points) equals g(e_2): g_+ >= g is immediate, and
     g_+ <= g_w -> g by the standard cylinder-constant argument. So the qualitative statement is
     available; (F2) is exactly its RATE.

That the residue is deterministic is the structural payoff. Sections 9.1-9.2 show that every
pathwise route -- including the mean version of the shift -- is pinned at W_l by a mechanism that
simply does not apply to a difference of two expectations.

--------------------------------------------------------------------------------------------------
## 6. The single hardest open piece, stated without cosmetics

6.1 WHAT I HAVE NOT PROVED: P2(l) <= C sqrt(l) log l, equivalently A_+(l) <= C sqrt(l) log l.
Nothing in this note establishes it, and no unconditional bound on P2 better than the trivial
P2 <= (b-a)(b/a) l is in hand. Every number in the verdict is conditional on it.

6.2 WHY IT IS PLAUSIBLE. It is the one-wall analogue of a published theorem (Alexander 1997) whose
proof needs subadditivity, concentration and a two-parameter family of split points. All three
survive at the wall: T_+(p,r) <= T_+(p,w) + T_+(w,r) for EVERY w in H (not merely wall w), so the
split points form a full two-dimensional family inside H; concentration at sqrt scale for T_+ is a
routine adaptation (I3); the limit shape enters only through g, which is unchanged by (F3).

6.3 WHY IT MIGHT FAIL, stated as strongly as I can. (i) Alexander's method uses translation
invariance of h(x) = E T(0,x) in the full lattice; the one-wall mean h_+(p,q) is invariant only
under e_2-translations and depends on both depths, so the method needs a version for a proper
subgroup -- I did not check that his argument survives it. (ii) Half-space FPP/LPP is genuinely a
different object at the boundary (different limit laws; at the critical boundary parameter even
different exponents in the solvable models), so "the boundary cannot be worse than the bulk" is an
intuition, not an argument. (iii) The route is not automatically better than the shift route: with
A_+ ~ l^gamma the criterion is alpha > gamma/(2-gamma), and the shift route corresponds to
gamma = (1+alpha)/(2+alpha); at alpha ~ 0.414 that is 0.586, so any gamma above about 0.59 makes
this route WORSE than the one it replaces. gamma = 3/5 already gives alpha > 3/7 = 0.4286.

6.4 THE ONE CONCRETE CHECK THAT WOULD SETTLE THE DIRECTION CHEAPLY. Measure it. E T_+ - E T for
p = (0,0), q = (0,l) is a two-Dijkstra-per-sample quantity on an l x C l lattice patch with [a,b]
weights (one run confined to x >= 0, one free), and its growth exponent over l = 2^6..2^12 with a
few thousand samples separates gamma = 1/2 from gamma = 2/3 (= the shift scale W_l at alpha = 1/3)
decisively -- the two differ by a factor l^{1/6}, about 3x across that range. That is the same
machinery as MG3 and it should be run before anyone builds on section 7. Until it is run, or the
one-wall Alexander bound is proved, the threshold below is a conditional statement.

--------------------------------------------------------------------------------------------------
## 7. The arithmetic

7.1 MASTER CRITERION. Let gamma be the exponent such that the total cost is n^delta R^gamma with
R = 5(b/a) h = Theta(n^kappa), kappa = beta + (1+alpha)/2 (gamma = max of the concentration-scale
exponent and the exponent of the residue P2). The requirement cost <= n^{alpha - 3 eps} is
    gamma * kappa + delta < alpha - 3 eps,
and at beta = eps = delta = 0 this is gamma (1+alpha)/2 < alpha, i.e.
    ALPHA > gamma / (2 - gamma).

7.2 THE THREE VALUES OF gamma THAT MATTER.
    gamma = 1/2  (Kesten-scale concentration + one-wall Alexander at sqrt scale) -> alpha > 1/3.
      Exactly: alpha > (1 + 2 beta + 4 delta + 12 eps)/3.
    gamma = alpha (envelope-scale versions of both)                              -> alpha < 1, i.e.
      closes for every alpha the program can want. BUT the envelope-scale CONFINED concentration is
      Proposition 2.9's own content, so using it here is circular (see 10.7). The envelope-scale
      one-wall Alexander bound alone is NOT circular and would suffice if the concentration half
      were supplied unconditionally.
    gamma = (1+alpha)/(2+alpha) (the shift route, published inputs)               -> alpha > 0.4142.

7.3 CROSS-CHECK AGAINST THE REFEREED NUMBER (independent re-derivation of a known result).
Feeding the shift route's optimised cost l^{(1+alpha)/(2+alpha)} into 7.1: at alpha = sqrt(2)-1 =
0.414214, (1+alpha)/(2+alpha) = 1.414214/2.414214 = 0.585786 and kappa = (1+alpha)/2 = 0.707107;
product = 0.414214 = alpha exactly. So my criterion machinery reproduces the referee's
alpha^2 + 2 alpha - 1 > 0 to six digits without being told it. That is the check that the budget
arithmetic below is not my own invention.

7.4 NUMERICAL TABLE for gamma = 1/2, beta = eps = delta = 0 (cost exponent = kappa/2 vs budget alpha):
    alpha = 0.50 : kappa 0.750, cost 0.3750, budget 0.500 -> closes, slack 0.1250
    alpha = 0.45 : kappa 0.725, cost 0.3625, budget 0.450 -> closes, slack 0.0875
    alpha = 0.4142: kappa 0.707, cost 0.3536, budget 0.414 -> closes, slack 0.0607 (old route: exactly critical)
    alpha = 0.35 : kappa 0.675, cost 0.3375, budget 0.350 -> closes, slack 0.0125
    alpha = 1/3  : kappa 0.667, cost 0.3333, budget 0.333 -> EXACTLY CRITICAL, does not close
    alpha = 0.30 : kappa 0.650, cost 0.3250, budget 0.300 -> fails
So the route closes on (1/3, 1/2] and fails at 1/3 itself. Against CRUX section 3b: the wall needs
alpha = 1/3 and the corner needs alpha > 1/3. They MEET rather than exclude each other by 0.08, but
they still do not overlap; and with beta, eps, delta > 0 fixed the failure at alpha = 1/3 is by the
genuine polynomial n^{(2 beta + 4 delta + 12 eps)/3}, not by a log.

--------------------------------------------------------------------------------------------------
## 8. Input ledger -- every probabilistic input, its window, and its status

(I1) l1 geometry, boundedness, subpath optimality, concatenation. DERIVED (Claims 1,2,4).
     Deterministic. No window.
(I2) Concentration of the FREE passage time at scale sqrt(r) with stretched-exponential tails,
     needed only in the LOWER direction and only for pairs on the wall, i.e. only at direction e_2.
     PUBLISHED (Kesten 1993; Talagrand 1995), bounded weights. NO ANGULAR WINDOW NEEDED -- and note
     that even the direction is a single lattice axis, not a range.
(I3) The same for the H-CONFINED passage time, upper direction, direction e_2. NOT A CITATION:
     routine adaptation. The Talagrand/Kesten argument needs only [a,b]-boundedness and a
     deterministic bound on the number of edges of the optimiser; Claim 4 supplies |gamma_+| <=
     (b/a) r. Flagged as the second-most-likely place for this note to be wrong.
     [RE-GRADED by the corner referee, iter 80/81: "NO OBSTRUCTION IDENTIFIED" - not "verified in
     mechanism". The iter-70 upgrade summarized the predictable-quadratic-variation control (the
     hard core of Kesten's theorem) instead of walking it; no fourth structural input referencing
     the complement of H was found, but the verification standard was not met. The specific list
     in 6.6.1 remains the attack surface.]
(I4) Efron-Stein plus Claim 4 giving Var(T_+) <= (b-a)^2 (b/a) r. DERIVED, elementary,
     unconditional, no window.
(I5) Reflection exchangeability across x = 0 (Claim 3). DERIVED, exact. Uses the lattice symmetry
     and iid weights only. No window.
(I6) E T(0,x) >= g(x). Standard subadditivity. No window.
(I7) Alexander's nonrandom-fluctuation bound A(l) <= C sqrt(l) log l. PUBLISHED, uniform over
     directions, exponential moments (bounded weights qualify). Used ONLY to show (F1) and (F2)
     are equivalent; the main chain does not consume it.
(I8) THE OPEN INPUT: P2(l) <= C sqrt(l) log l, equivalently A_+(l) <= C sqrt(l) log l. UNPROVED.
     Direction e_2 only, endpoints on the wall only, expectation only.
     [STATUS SHARPENED iter 70, section 6.6.2: the naive wall-splitting route to this bound is now
     PROVED inadequate - the deficit inherits the half-plane midline wandering (Splitting Lemma
     (6.6)), and sqrt scale would need wandering exponent 1/2, false under KPZ. What survives
     [REWORDED iter 81 per the corner referee's worst-defect finding - the word "unconditionally"
     was WRONG: no sublinear wandering exponent is known unconditionally (that is itself open;
     IF the half-plane wandering has any exponent gamma' < 1, THEN A_+(l) <= C l^{gamma'}. A
     sqrt-scale proof must use an approximating-functional method on the depth-inhomogeneous mean
     field, or something new. The pilot (6.5) leans toward the wandering-dominated regime at
     reachable scales without settling the asymptotic. Solvable-world support carries caveats
     C-a/C-b/C-c in 6.6.4(b) (merged iter 90); the PINNING wall is the named kill scenario. And
     per B2(a), the pilot lean is a MAGNITUDE consistency, not a prediction of (6.6).]

NOT CONSUMED, and this is the point of the route: no wandering hypothesis (W) at any scale, no
alignment at the envelope scale, no curvature of g at any direction, no arc, no angular window, no
FKG, no H1a/H1b/H1c, no conforming-geodesic input, and no restricted-distance concentration at the
envelope scale (which would be circular). Referee correction 2 to the draft -- that L3 needs H1a
and H1b with their windows removed because the corner box realises every direction -- does not
apply here: Claim 2 discharges the direction deterministically.

--------------------------------------------------------------------------------------------------
## 9. Negative results (DERIVED): why the mean/fluctuation split is not one option among many

9.1 NO PATHWISE MARGIN CONSTRUCTION CAN BEAT THE WANDERING SCALE.
CLASS P: constructions that (a) exhibit an H-path from u to v built from connectors of deterministic
l1-length and sub-geodesics between translated endpoints, and (b) certify H-containment by the event
that each sub-geodesic deviates from its own segment by at most D_i.
CLAIM: any member of class P has cost >= a * D_1 >= a * (the smallest margin at which the certifying
event holds with the required probability), and since u may be ON the wall (u = (0,y) lies in B),
that margin is at least the corresponding quantile of the transversal deviation, hence >= c W_s.
PROOF: u is on the wall and the first sub-geodesic starts at u' with dist(u', wall) >= D_1, else the
certificate does not imply containment; the connector from u to u' has l1-length >= D_1 and every
edge costs >= a. QED.
So the shift cost is not an artifact of the draft's particular chain; it is a property of the entire
class, and no re-organisation of the chain (one-shot, dyadic, wall-proximity skip) escapes it. This
explains, in one line, why three of the referee's four attacks on L3 failed.

9.2 THE MEAN VERSION OF THE SHIFT IS ALSO PINNED AT W_l -- for a reason worth recording.
Let MEANGAP(D) be the mean gap for endpoints at depth D inside H. Then MEANGAP(0) <= 2bD +
MEANGAP(D) (walk in along the wall normal; the connector is inside H), and MEANGAP(D) <=
(b-a)(b/a) l * P(the free geodesic between the depth-D endpoints touches x = -1), since the gap
vanishes unless the free geodesic exits. For D below the wandering scale that probability is order
one, so the second term is order l; for D above it, the first term is >= 2bD >= W_l. Hence
min over D of this bound is Theta(W_l) FOR EVERY TAIL SHAPE. The defect is not the tail estimate; it
is that the argument charges the FULL deterministic gap on the failure event. Any route that keeps
that structure -- pathwise or in the mean -- stops at W_l.

9.3 REFLECTION FOLDING IS CAPPED AT sqrt(l) AND IN FACT COSTS Theta(l).
The fold phi(x,y) = (|x|,y) maps every lattice edge to a lattice edge and every u-v path (u,v in H)
to an H-path, so
    T_+(u,v) - T(u,v) <= sum over edges e of gamma lying strictly left of ( omega(Re) - omega(e) ).
NUMBER OF TERMS: for wall pairs, Claim 3 makes the geodesic's left-length and right-length
exchangeable, so the expected number of terms is exactly half the expected geodesic length outside
the wall column, i.e. Theta(l). CONSEQUENCE 1 (rigorous): even PERFECT square-root cancellation
would give only sqrt(Theta(l)) = Theta(sqrt l) -- the same scale this note reaches by a route that
does not need cancellation at all. So folding can never be the better device. CONSEQUENCE 2 (sign,
non-rigorous but one-directional): the terms are positively biased, because gamma selects light
edges (its per-edge average is at most T/|gamma| <= g(e_2), and g(e_2) < E omega strictly for
non-degenerate weights) while the mirror edges Re are unselected; so the sum has a drift of order
(E omega - g(e_2)) per term and the fold costs Theta(l), the same order as the deterministic L1
bound of the draft. Reflection is therefore worthless PATHWISE and valuable only DISTRIBUTIONALLY,
which is exactly the use made of it in Claim 3.

9.4 EXCURSION-BY-EXCURSION REPAIR IS ALSO Theta(l). Repairing each excursion separately gives
T_+ - T <= sum over the geodesic's minus-segments of [T_+(w_{i-1},w_i) - T_-(w_{i-1},w_i)], each term
being a conditionally symmetric variable evaluated where it is positive. The bound is honest but
lossy: it forces the repaired path to return to the wall at every crossing point. With N(r)
crossings at scale r the dyadic sum is dominated by the smallest scales (deterministic per-excursion
cost (b-a) r, count up to l/r), giving Theta(l) again. Any repair that is anchored at the crossings
pays for the anchoring; the mean/fluctuation split never anchors.

--------------------------------------------------------------------------------------------------
## 6.5 PILOT MEASUREMENT OF P2 RUN (iter 69, author's hand; the check 6.4 asked for, at
## laptop scale). VERDICT: EXPONENT UNRESOLVED; MAGNITUDE COMFORTABLY INSIDE THE CONJECTURED BOUND.

Setup: Uniform[1,2] weights (a=1, b=2), wall pair p=(0,0), q=(0,l), three Dijkstras per sample
(free / x>=0 / x<=0) on a patch of halfwidth 4 l^{2/3}, seeds fixed, BelowNormal, single process.
l = 24, 48, 96, 192, 384, 768 with n = 400, 300, 200, 120, 60, 80. Results (mean +- SE):

  l     P2              Part1           crossing_frac   E[gap | cross]
  24    0.000           0.139+-0.014    0.000           -
  48    0.011+-0.005    0.409+-0.029    0.037           0.31
  96    0.070+-0.015    0.800+-0.048    0.165           0.43
  192   0.396+-0.055    1.309+-0.096    0.433           0.91
  384   0.599+-0.119    1.884+-0.151    0.633           0.95
  768   1.272+-0.174    2.406+-?        0.68            1.88
  1536  2.305+-0.338    2.991+-?        0.77            2.99   (added iter 71, n=48)

[UPDATED iter 71 after the 1536 octave: three consecutive local P2 slopes are 0.60, 1.09, 0.86,
each +-~0.3, with the crossing fraction STILL rising (0.68 -> 0.77) - the regime has not stabilized
by l = 1536 and the exponent verdict is unchanged: UNRESOLVED, no conclusion quotable either way.
Magnitude margins at 1536: P2 = 2.31 against sqrt(l) = 39.2 (17x inside the conjectured budget) and
against W_l = l^{2/3} = 133 (58x). Laptop scale is exhausted; anything further is a larger-machine
job. Small rig note for reproducers: the 1536 runner's PRINT line mislabels the level as 768 (a
string-replace slip in the extension script); the JSON keys are correct and the data is stored
under "1536".]

RIG VALIDATION. The pathwise invariant T <= min(T_+,T_-) was never violated across ~1,160 samples
(min gap exactly 0.0000 at every level). Positive control: Part1 = (1/2)E|T_+-T_-|, which Claim 6
PROVES is <= C_1 sqrt(l) with C_1 = 1 here, measures 2.41 at l=768 against a ceiling of 27.7, with
local exponent falling 1.56 -> 0.97 -> 0.71 -> 0.53 -> 0.35 across octaves. [CORRECTED iter 81
per the referee's audit: the slopes CROSSED BELOW 1/2 by the top octave - "converging to the cap
from above" was wrong prose; consistent with the proved cap either way. Also: the top-octave
crossing-fraction rise (0.68 -> 0.77) is a 1.1 sigma move, NOT established as rising. And the
truncation caveat the pilot code promises (patch halfwidth 4 l^{2/3}; truncation, if it binds,
raises T_free and biases P2 DOWNWARD, toward the null) belongs here and was omitted.] The rig
measures what it claims to measure - all seven rows independently audited to the digit.

WHAT THE PILOT ESTABLISHES. (1) The probed range is DEEPLY PRE-ASYMPTOTIC: the free geodesic does
not even touch both half-planes until l ~ 100 (crossing fraction 0 at l=24, still only 0.68 at
l=768 and still rising). Everything below l ~ 400 measures the onset of crossing, not gamma.
(2) MAGNITUDE: P2 sits far inside the conjectured budget at every probed scale - at l=768,
P2 = 1.27 against sqrt(l) = 27.7 (a 20x margin) and against W_l = l^{2/3} = 83.7 (a 60x margin).
The open input I8 is numerically comfortable everywhere the pilot can see.
(3) EXPONENT: unresolved. Local slopes over the last two octaves are 0.60 and 1.09, each +-0.35 at
one SE propagated, with the conditional gap E[gap|cross] rising from 0.95 to 1.88 over the top
octave. Consistent with gamma = 1/2, with 2/3, and with the onset still dominating. NO exponent
conclusion may be quoted from this pilot in either direction.

WHAT WOULD SETTLE IT: l up to ~4096 with hundreds of samples per level - an MG3-class larger-machine
itself. Data: scratchpad p2_pilot_results.json, seed 20260809, scripts p2_pilot.py / p2_extend768.py.

--------------------------------------------------------------------------------------------------
## 6.6 HAND-WORK, ITER 70 (author; agents down). Two results: I3 verified in mechanism, and a
## PROVED splitting lemma that both bounds the deficit and KILLS the naive route to I8.

6.6.1 I3 VERIFIED IN MECHANISM (upgrade from "flagged"). Kesten's sqrt-scale concentration proof
consumes exactly three structural inputs: (a) iid bounded weights on a countable edge set; (b)
deterministic localization of every optimizer to a finite box (his Lemma 1.1 argument runs verbatim
for T_+ since T_+((0,y1),(0,y2)) <= b r via the wall segment); (c) a deterministic bound on the
optimizer's edge count in the SUBGRAPH - supplied by Claim 4, |gamma_+| <= (b/a) r. The Doob
martingale over edge revelations, the one-edge influence bound (b-a) 1(e on an optimizer), the
conditional-variance sum <= (b-a)^2 E|gamma_+| <= (b-a)^2 (b/a) r, and Freedman-Bernstein are all
subgraph-agnostic: NOTHING in the argument references edges outside H. Constants depend on (a,b)
only, hence uniform over wall pairs; the union bound in section 3 needs nothing more. Remaining gap
is citation-level writing, not mathematics. (A referee should still attack this - but the attack
surface is now a specific short list, not "routine adaptation".)

6.6.2 A PROVED LEMMA: the one-wall deficit is dominated by dyadic midline wandering.
SPLITTING LEMMA (DERIVED, unconditional). Let a_l := E T_+((0,0),(0,l)), g := g(e_2) per unit,
D_l := a_l - g l >= 0, and let x*_l >= 0 be the depth (x-coordinate) of the first crossing of the
line y = l by the H-geodesic from (0,0) to (0,2l). Then
    D_{2l} >= 2 D_l - 2b E[x*_l],
and consequently, since D_m / m -> 0 (Fekete),
    D_l <= 2b Sum_{j>=0} 2^{-(j+1)} E[x*_{2^j l}].                                  (6.6)
Proof. The H-geodesic gamma from (0,0) to (0,2l) crosses y = l at w = (x*, l); splitting there,
a_{2l} = E[T(gamma[0->w])] + E[T(gamma[w->end])] >= E[T_+((0,0),w)] + E[T_+(w,(0,2l))]. Triangle
inequality in the H-metric pathwise (w is measurable in the same configuration):
T_+((0,0),(0,l)) <= T_+((0,0),w) + b x* (horizontal return path, inside H), and by e_2-translation
invariance of T_+, a_l = E T_+((0,l),(0,2l)) <= E[T_+(w,(0,2l))] + b E[x*]. Summing the two and
comparing with the split of a_{2l} gives 2 a_l <= a_{2l} + 2b E[x*_l]; subtract 2 g l. The dyadic
sum follows by iterating D_l <= (1/2) D_{2l} + b E[x*_l] upward and killing the boundary term with
Fekete. QED.

CONSEQUENCE, BOTH DIRECTIONS STATED HONESTLY.
(+) If the half-plane midline wandering satisfies E[x*_m] <= C m^{gamma'} for some gamma' < 1, then
    A_+(l) = D_l <= C' l^{gamma'} and hence P2(l) <= A_+(l) <= C' l^{gamma'}: the deficit and the
    mixing gain inherit ANY sublinear wandering exponent. This is the first unconditional-in-
    structure upper bound on I8 beyond the trivial linear one.
(-) BUT the route through this lemma cannot reach sqrt(l). The believed (KPZ) depth of the
    H-geodesic between wall points is m^{2/3}, and even the published conditional machinery gives
    only m^{3/4} (curvature-conditional Newman-Piza/Alexander wandering). gamma' = 2/3 gives
    threshold alpha > (2/3)/(2 - 2/3) = 1/2 (the Kesten boundary, useless); gamma' = 3/4 gives
    alpha > 3/5, WORSE than the shift route. For the target alpha > 1/3 one needs gamma' = 1/2,
    i.e. the H-geodesic staying within sqrt(l) of the wall - FALSE under KPZ. So: THE WALL-SPLITTING
    ROUTE TO I8 IS PROVABLY INADEQUATE for the sqrt bound; it pays the full wandering at every
    dyadic scale. Alexander's full-plane sqrt(l) log l theorem beats the wandering (l^{2/3}) by NOT
    splitting at returns - his approximating-functional machinery uses translation invariance in
    all of Z^2. Sharpened statement of what I8 needs: a one-wall version of the approximating-
    functional method that handles the DEPTH-inhomogeneous mean field E T_+(p,q) (invariant only
    under the e_2 subgroup), or an entirely different mechanism. The doubt recorded in 6.3(i) is
    now a proved obstruction with the exact failure point named - FOR THE SPLITTING ROUTE. Caveat
    per the absence discipline: "no such machinery" is a claim about my reading, not the field.
    The half-space growth literature (half-space LPP has an exactly-solvable boundary theory) has
    NOT been searched for a boundary Alexander-type rate; that search is owed before this
    obstruction is treated as load-bearing, and it is the first errand for the next web-capable
    fire.

6.6.3 PILOT CROSS-READ. The pilot's top-octave conditional gap E[gap | cross] doubled (0.95 ->
1.88, local exponent ~ 1 over one octave, +-large): at the probed scales the measured behaviour is
consistent in MAGNITUDE with the dyadic-sum bound of (6.6) evaluated at wandering scale, not
yet with a settled sqrt regime. [ONE-CLAUSE REPAIR per corner referee B2(a), iter 90: (6.6) is an
UPPER bound with no lower-bound content - it cannot PREDICT that P2 tracks wandering, and the
earlier phrase "wandering-dominated regime of (6.6)" wrongly implied it could. The pilot data is
consistent with that regime; the inequality neither predicts nor forbids it.] That
leans the same way as 6.6.2(-): if P2 tracks depth-wandering ~ l^{2/3} asymptotically, the corner
threshold from THIS route is alpha > 1/2 and the route buys nothing over Kesten inputs. The pilot
cannot settle it (SEs +-0.35 on local exponents); the statement that CAN be made is that nothing
measured contradicts (6.6), and nothing measured yet supports the sqrt conjecture over the
wandering alternative at reachable scales.

STATUS AFTER 6.6: the note's conditional verdict WEAKENS. The one-wall Alexander bound (I8 at sqrt
scale) is not merely unproved - the natural route to it is now proved inadequate, and the pilot
leans toward the unfavourable regime at small scales. The honest current reading of the corner
route: CONDITIONAL on a half-plane wandering exponent gamma' < 1 existing (open; the word
"unconditionally" that stood here was the corner referee's worst-defect finding, iter 80/81),
cost <= concentration terms + C l^{gamma'}; the route WITH (6.6) AS ITS I8 INPUT beats the shift
route iff gamma' < (1+alpha)/(2+alpha) at the relevant alpha, and reaches the 1/3 threshold only
under the (KPZ-false) gamma' = 1/2. [ONE-CLAUSE REPAIR per corner referee B2(b), iter 90: the
"iff" is about the route with THIS lemma as its input - if I8 at sqrt scale were proved by ANY
means, the route beats the shift regardless of gamma'.] The
mean/fluctuation split remains the only known escape from the W_l pin (section 9 stands), but its
payoff now rests on a mechanism nobody has, rather than on a plausible adaptation.

--------------------------------------------------------------------------------------------------
## 6.6.4 THE OWED LITERATURE SEARCH, RUN (iter 71, author, web). Verdict in two halves.

(a) THE OBSTRUCTION STANDS, now as a checked absence rather than my ignorance. The closest lattice
work is Ahlberg, "Convergence towards an asymptotic shape in FPP on cone-like subgraphs of Z^d"
(arXiv 1107.2280): shape theorem, Lp and a.s. convergence, and - useful to us - the cone shapes are
RESTRICTIONS of the full lattice shape, which makes the note's F3 (g_+ = g) citable rather than
folklore. But it is qualitative: no Alexander-type rate for cones or half-planes appears there, and
no one-wall rate surfaced anywhere else in the search. The searched surface: half-space FPP rate
queries, cone-subgraph queries, and the solvable half-space corpus below. Bounded, as always, by
what the search saw.

(b) BUT THE CONJECTURE GAINS REAL SUPPORT FROM THE SOLVABLE WORLD. In half-space LPP (Baik-Rains
symmetrized LPP; Betea-Ferrari-Occelli stationary half-space; Barraquand et al.), the passage time
to the diagonal in the subcritical boundary regime keeps the SAME law-of-large-numbers constant as
full space, and the boundary's entire effect appears in the fluctuation LAW (GSE/GOE/Gaussian by
boundary parameter) at scale N^{1/3}. If the half-space mean deficit sat at the wandering scale
N^{2/3}, it would dominate those N^{1/3} fluctuations and could not be missed by the exact
formulas; instead the corrections enter AT fluctuation scale. Translated: the solvable analogue of A_+(l) - the one-wall nonrandom fluctuation - sits at Q_l,
the FLUCTUATION scale, not W_l and not even sqrt(l). [GEOMETRY CORRECTED per the corner referee's
D0, iter 90: the feared point-to-diagonal/wall-pair mismatch FAILS - half-quadrant (1,1)->(N,N)
IS wall-pair geometry, both endpoints on the diagonal, confined to one side. The analogy is
structurally right.] Under gamma = alpha the note's own 7.2 closes for every alpha < 1 - as a
TARGET only, per the caveats below.

corner referee's D1; stated once, precisely):
(C-a) MEAN vs LAW: the solvable results are distributional (N^{1/3} Tracy-Widom-type laws,
GSE generic / GOE^2 critical); a limit law bounds the MEAN deficit only with uniform
integrability. The literature has the moment convergence - cite THAT, and read "could not be
missed by the exact formulas" with this qualifier.
(C-b) PHASE IDENTIFICATION, and the named kill scenario: FPP's wall carries NO boundary
parameter, so placing it in the SUBCRITICAL phase rests on the removal-not-reward argument (the
wall only deletes paths; nothing rewards hugging it). A PINNING-type wall would sit at the
supercritical N^{1/2} - exactly the scale that kills I8. Only the structural argument excludes
pinning; nothing in the solvable world does.
(C-c) SIGN: LPP's wall DECREASES a max (deficit negative); FPP's INCREASES a min (A_+ >= 0). The
honest plausibility argument and nothing more - it does NOT license gamma = alpha in 7.2 as
anything but a target.

SYNTHESIS OF 6.6.2 + 6.6.4, the honest current picture of I8: the TRUTH is plausibly at fluctuation
scale (solvable-world evidence); the naive wall-splitting proof provably cannot see below the
wandering scale (Splitting Lemma); Alexander's full-plane machinery avoids paying wandering but
consumes full translation invariance; no one-wall rate theorem exists in the searched literature.
So I8 is a genuine open lemma whose truth is well-supported and whose proof needs a mechanism that
does not yet exist on the lattice - most plausibly a depth-inhomogeneous version of the
The pilot's small-scale lean toward wandering-dominated behaviour (6.6.3) is onset, not asymptotic,
on this reading; the pilot cannot distinguish the two and says so.
