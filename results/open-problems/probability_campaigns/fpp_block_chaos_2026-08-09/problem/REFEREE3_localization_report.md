# Referee 3 report: the localization tail draft (iter 106 + G-a/G-b/G-c/G-e/G-f patches)
# Independent re-derivation from the definitions. Working file, written as the checks land.

Object: problem/localization_tail_draft_iter106.md
Seam:   problem/I8_from_curvature_v2_iter82.md [V5-1]/[V5-2]
DAG:    problem/dependency_graph_iter107.md
Machine check: scratchpad/bandcap_check.py + bandcap_results.json

Convention used throughout this report: coordinates are (transversal, longitudinal) = (h, y);
the span pair is 0 -> x = r e_2; a := a_w = essential inf of the weight, b := esssup; rho := b/a_w.

-------------------------------------------------------------------------------
## SECTION A. Re-derivations that CONFIRM the draft

A1. (G-b i) the deterministic band cap. Re-derived independently:
    a path 0 -> r e_2 reaching transversal level D uses >= r vertical and >= 2D horizontal
    steps, so T >= a(r + 2D); the axis path gives T(0, r e_2) <= b r; hence a(r+2D) <= br,
    i.e. D <= r(b - a)/(2a). Exactly the draft's cap. U[1,2] -> r/2, matching bandcap_check.py.
    CONFIRMED. Two riders below (A1a, A1b).

    A1a. a_w > 0 is load-bearing here and in two further places (band cap, G-a's site count, G-f's endpoint confinement).
    (P-conc)/(P-Alex) as published need only bounded weights with F(0) < p_c. The lemma as
    written is therefore a UNIFORMLY ELLIPTIC statement, not a bounded-weights statement:
    every constant in it blows up as a_w -> 0. Say so on the ledger line.

    A1b. The cap generalises to an arbitrary pair (u,v), which G-f needs and does not state:
    any path u -> v that leaves the coordinate bounding box of {u,v} by h in either coordinate
    has >= |u-v|_1 + 2h edges, and the staircase path gives T(u,v) <= b|u-v|_1, so
    h <= (b-a)|u-v|_1/(2a). Deterministic, no arc, no direction. (Used in B6 below.)

A2. (G-a) the through-vertex argument. The transversal coordinate of a lattice path changes by
    0 or +-1 per edge and starts at 0, so if its maximum is >= D then (the max being an integer)
    it is >= ceil(D), and by discrete IVT the path contains a vertex at level EXACTLY
    Dbar := ceil(D). Subpath optimality then gives T(0,x) = T(gamma[0->v*]) + T(gamma[v*->x])
    >= T(0,v*) + T(v*,x), an identity-plus-inequality with NO seam and NO O(b).
    The exactness claim is CONFIRMED. The union does not need "first" - any vertex at level
    +-Dbar works - so the count is over sites, not over first-hitting configurations.

A3. (G-c) the split. Re-derived: with S := T(0,x) - ET(0,x), L1 := T(0,v*) - ET(0,v*),
    L2 := T(v*,x) - ET(v*,x),
        S - L1 - L2 = [T(0,x) - T(0,v*) - T(v*,x)] + [ET(0,v*) + ET(v*,x) - ET(0,x)]
                   >= 0 + [g(v*) + g(x - v*)] - [g(x) + C3 sqrt(r) log r],
    using Fekete (E T >= g) on the legs and (P-Alex) on the span ONLY. So max(S, -L1, -L2)
    >= Delta/3 with Delta = c_- Dbar^2/r - C3 sqrt(r) log r. CONFIRMED, including the
    one-sidedness bookkeeping (span up, legs down) and the iter-116 correction to the
    H-version parenthesis.

A4. (G-c) the cancellation and c''. Re-derived:
        Dbar >= D = sigma r^{3/4}  =>  c_- Dbar^2/r >= c_- sigma^2 sqrt(r),
        Delta >= sqrt(r)(c_- sigma^2 - C3 log r) >= (1/2) c_- sigma^2 sqrt(r)
            iff sigma^2 >= (2 C3/c_-) log r,
        t >= Delta/(3 sqrt(C_L' r)) with C_L' = 2 + rho,
        exponent = c1 t >= c1 c_- sigma^2 / (6 sqrt(2 + rho)).
    So c'' = c1/(6 sqrt(2 + rho)) is CORRECT, and U[1,2] (rho = 2) gives c'' = c1/12,
    Form B c''/2 = c1/24. CONFIRMED. The r-cancellation is exactly chi'=1/2 against xi'=3/4.

A5. (G-c) normalisation window. |v*| <= Dbar + |j|, |x - v*| <= Dbar + |r - j|, both
    <= (2 + rho) r for delta <= 1 (up to the ceiling slack, see B4), and both >= Dbar because
    the transversal coordinate alone is Dbar. Span = r. CONFIRMED, C_L' = 2 + rho.

A6. (G-c) Form B. K exp(-c'' c_- sigma^2) <= exp(-(c''/2) c_- sigma^2) iff
    sigma^2 >= 2 log K/(c'' c_-). With K = 18 C1 rho r this is the draft's line. CONFIRMED
    (arithmetic; the value of K is improved in B5).

A7. (G-c) the range ledger's two (P-conc) checks. The range condition for a pair of length L
    at t = (Delta/3)/sqrt(L) is t <= C2 sqrt(L), i.e. Delta <= 3 C2 L. Binding at the SHORTEST
    pair, L >= Dbar. Draft's two checks re-derived:
      span:      Delta <= c_- Dbar^2/r <= c_- delta^2 r <= 3 C2 r   iff delta^2 <= 3C2/c_-;
                 and delta <= min(1, 3C2/c_-) gives delta^2 <= delta <= 3C2/c_-.  OK
      short leg: Delta <= c_- Dbar^2/r <= 3 C2 Dbar  iff Dbar <= (3 C2/c_-) r.      OK
    So the single wlog delta <= min(1, 3C2/c_-) DOES imply both, as claimed - modulo the
    ceiling slack (B4). The iter-114 first print (C''' = min(delta^2, 3C2/c_-)) was indeed
    mixing a squared with a linear constraint; the correction is right. CONFIRMED.

A8. (G-c) mid-band clause. {dev >= D} with D > delta r is contained in {dev >= delta r} by the
    same discrete IVT, and delta r = sigma' r^{3/4} means sigma'^2 = delta^2 sqrt(r), the top
    of the range. Form A there is exp(-c'' c_- delta^2 sqrt r) - stretched-exponential in
    sqrt(r). CONFIRMED (subject to B4's ceiling repair, which is exactly where it bites).

A9. (G-e) one-sidedness. The discrete-IVT argument runs unchanged for {min transversal <= -D};
    the union drops to one level; (H-curv-LOWER) is consumed only for wall-ward displacements.
    I checked every other step for a hidden use of the two-sided form: the band cap (A1) is a
    bound on |transversal| and is used only to COUNT sites, so it is indifferent; the
    normalisations (A5) use |Dbar|; the split (A3) is sign-agnostic. Nothing else uses the
    two-sided form. CONFIRMED, prefactor halves.

A10. (G-d) dissolution. The DAG's third edge (localization -> A_+) genuinely does not exist:
    the free version consumes (P-Alex) for E T, never E T_+. I read the three consumption-site
    claims in dependency_graph_iter107 against the cited sections and found no site needing a
    confined-geodesic wandering tail. The revival clause is not triggered by anything in this
    round. CONFIRMED as bookkeeping.

A11. (Seam, [V5-1]) A >= C3 c''. Re-derived: consumer sets theta = 2, c_tail = (c''/2) c_-,
    sigma^2 = A log l / c_tail = 2A log l/(c'' c_-). Lemma's lower thresholds at r' <= l:
      (2C3/c_-) log r'          <= sigma^2  iff  A >= C3 c'';
      (2/(c'' c_-)) log(K r')   <= sigma^2  iff  A log l >= log r' + log K, ok for A >= 2, l large.
    So A := max(2, C3 c'') is exactly right. CONFIRMED. (And B3 below makes the C3 c'' branch
    vacuous, so A = 2 suffices - a simplification for the v2 side.)

-------------------------------------------------------------------------------
## SECTION B. WHAT IS WRONG. Numbered, with the corrected constant in each case.
## (Checks: REFEREE3_check.py, REFEREE3_check2.py, REFEREE3_check3.py in this directory.)

### B1 [DEFECT - the union contains sites the hypothesis cannot price]. G-a / G-c / G-b(ii).
THE HOLE. The union runs over longitudinal j across the whole length cap,
j in [-(rho-1)r/2, r + (rho-1)r/2] (the draft prints the cruder |j| <= rho r). For U[1,2] that
is j in [-r/2, 3r/2]. A site at j = -r/2 sits at Euclidean distance ~r/2 from the SEGMENT
[0,x]. (H-curv-LOWER) is assumed only for "transversal distance d <= delta r from the
segment", and delta <= min(1, 3C2/c_-) is typically small. So on the literal reading of the
hypothesis, HALF THE UNION IS UNPRICED: Delta has no lower bound at those sites and the
three-way split yields nothing there.
I checked the two obvious escapes and both fail:
  - deterministic exclusion: a path through (+-Dbar, j) needs r + 2|j| + 2 Dbar edges, so the
    length cap permits every j with |j| <= (b-a_w) r/(2 a_w) - Dbar. Those sites are NOT
    excluded;
  - the curvature-free floor: g(v)+g(x-v)-g(x) >= a_w(2 Dbar + r + 2|j|) - b r is NEGATIVE for
    exactly the moderate |j| ~ delta r that matters.
G-b(ii) answers this by reading the hypothesis as an OFFSET condition ("the displaced point v
is arbitrary at its distance in the condition as stated"). As a reading of the printed sentence
that is defensible; as mathematics it is load-bearing and undefended, and for TILTED spans -
which v2 does consume, its class pairs have o(1) but non-zero tilt - it is a genuine
strengthening of Newman-Piza's enclosing ball, not a restatement of it.

THE REPAIR, and it is free - no offset reading, no wider arc, no constant loss. Let n support
B_g at u* = u/g(u) and put phi(y) := <y,n>/<u*,n>; convexity alone gives phi <= g everywhere
with equality on the ray through x, so
   g(v) + g(x-v) - g(x) = [g(v)-phi(v)] + [g(x-v)-phi(x-v)] >= max(0,-phi(v)) + max(0,-phi(x-v)).
For an axis-aligned span phi(y) = g(e_2) y_2, so a site at longitudinal j = -m or j = r+m has
    excess >= g(e_2) * m       -- LINEAR in the overshoot, and needing NO curvature at all.
Feed that through the same three-way split: those sites carry exponent
c1 [g(e_2) m - C3 sqrt(r) log r]/(3 sqrt(C_L' r)), which at m = delta r/2 is
~ c1 g(e_2) delta sqrt(r)/(6 sqrt(2+rho)) - stretched-exponential in sqrt(r). So the union may
be RESTRICTED to j in [-delta r/2, r + delta r/2], where dist(v*, segment) <= delta r/sqrt(2)
< delta r and (H-curv-LOWER) applies exactly as literally written.
NUMERICS (REFEREE3_check3.py): over 6 norms x 4 offsets x 4 overshoots x both sides the ratio
excess/(g(e_2) m) never fell below 2.000 for axis-aligned spans and never below 1.73 for spans
tilted by 0.05-0.20 rad, so the printed bound is conservative. The far-j exponent already beats
the main exponent at every polylog quantile once r >~ 1e6 at delta = 0.1.
CORRECTED STATEMENT (Form A with the clause):
    P(dev >= sigma W_r) <= 12 C1 rho r [ exp(-c'' c_- sigma^2)
                                       + exp(-c1 g(e_2) delta sqrt(r)/(6 sqrt(2+rho))) ],
the second term negligible at every consumed quantile. c'' and c_- are UNCHANGED. This is the
correction I would print.

FALLBACK, if the draft prefers to keep the offset reading instead of adding the clause:
 (a) for AXIS-ALIGNED spans the offset form is a THEOREM, not an assumption. F(h,j) :=
     g(h,j) + g(h,r-j) is convex in j and symmetric about j = r/2 (reflection about the
     transversal axis IS a lattice symmetry, so g(-h,s) = g(h,s)), hence F(h,j) >= F(h,r/2) for
     EVERY j, including j < 0 and j > r. So assuming the hypothesis only at the midpoint - the
     enclosing-ball statement Newman-Piza print - already delivers every site in the union at no
     cost. Verified: 0 violations in 5 norms x 3 scales x 5 offsets x 1401 j-values, minimum
     ratio 0.9999999999999999.
 (b) for TILTED spans the symmetry argument FAILS - measured deficits up to 4.5% (l1 at tilt
     0.05) - so the offset form must be assumed, or derived from the geometric enclosing ball,
     which supplies it with an explicit loss:
        excess >= c d^2 (1/|v| + 1/|x-v|) >= 4 c d^2/(|v|+|x-v|) >= (1/C_L') x (midpoint excess),
     i.e. c_- -> c_-/C_L' = c_-/(2+rho) at the far sites, hence
        c'' c_- -> c1 c_-/(6 (2+rho)^{3/2}),  U[1,2]: c1 c_-/48 (Form A), c1 c_-/96 (Form B),
     and the seam's wiring constant c = (c''/2) c_- becomes c1 c_-/96, not c1 c_-/24 - a factor
     4 the consumer would have to absorb. Measured worst all-j/midpoint ratio over admissible
     norms and tilts: 0.711, against the guaranteed 0.25. (Norms flat at the tested direction -
     l1 at any tilt, l4 at the axis, the hex norm - have c_- = 0 and were excluded; they are
     section 3's "a shape can be flat (kills c_-)", and it is worth noting that l4 at the axis
     is exactly such a shape: its excess is order d^4/r^3, not d^2/r.)

### B2 [DEFECT - the stated range can be EMPTY, and r_0 is never stated]. G-c range ledger.
The ledger prints a polylog lower threshold and the upper limit delta^2 sqrt(r) and calls the
gap "inside the consumer's quantiles". The gap is EMPTY unless r exceeds an unstated r_0.
Measured (REFEREE3_check2.py A1; delta = min(1, 3C2/c_-), c'' = c1/(6 sqrt(2+rho))):
    (C1,c1,C2,C3,c_-,rho) = (1, 1,   1,   1, 1,    2)  ->  r_0 ~ 1e5.5
                            (1, 0.2, 1,   2, 0.2,  2)  ->  r_0 ~ 1e8.5
                            (1, 0.1, 0.5, 2, 0.1,  2)  ->  r_0 ~ 1e10
                            (1, 0.01,0.1, 5, 0.01, 2)  ->  r_0 ~ 1e14
1488 of 2187 gridded parameter points had an EMPTY range at r = 1e3 / 1e6 / 1e10.
CORRECTION: the statement must carry
    r >= r_0,  where  delta^2 sqrt(r) >= max( (2 C3/c_-) log r , (2/(c'' c_-)) log(12 C1 rho r) ).
Same phenomenon as B7(c) and B8; it is the most under-stated thing in the document, because
every consumer line reads "polylog, well inside the range" as though it were free.

### B3 [DEFECT - a band of sigma where Form A is claimed but not proved]. G-c.
The derivation needs sigma^2 >= (2 C3/c_-) log r; the statement is only vacuous (RHS >= 1) for
sigma^2 <= log(18 C1 rho r)/(c'' c_-). Those two intervals fail to cover when
    2 C3 c'' > 1 + log(18 C1 rho)/log r,   i.e. essentially c'' > 1/(2 C3).
45 of 324 gridded parameter points leave such a band (e.g. C1 = 0.5, c1 = 1, C3 = 10, rho = 2:
2 C3 c'' = 1.667). On that band Form A is asserted with a non-trivial right-hand side and there
is no proof of it.
CORRECTION (free): (P-conc) with rate c1 holds with any smaller rate, so add the normalisation
    WLOG  c1 <= 3 sqrt(2 + b/a_w)/C3,   equivalently   c'' <= 1/(2 C3).
Then Form A is proved on the whole stated range. Bonus: it forces C3 c'' <= 1/2, so the
consumer's [V5-1] side condition A >= max(2, C3 c'') collapses to A = 2 - one constraint deleted
from the v2 ledger rather than added to it.

### B4 [DEFECT, minor - the ceiling escapes the curvature window]. G-c, C''' and MID-BAND.
The site is at level Dbar = ceil(D) while the window is stated for D <= delta r; at the top of
the range D = delta r exactly and Dbar = delta r + 1 sits OUTSIDE it. 33 gridded points show it.
The MID-BAND clause is evaluated exactly there, and so is the short-leg range check.
CORRECTION: C''' = delta^2/4 (then Dbar <= (delta/2) r + 1 <= delta r for r >= 2/delta), or read
the window as ceil(D) <= delta r. The draft's C''' = delta^2 is right only up to this.

### B5 [FAVOURABLE - the union count is loose by 1.5x]. G-a / G-c.
The same facts give a sharper count: a vertex at longitudinal j needs r + 2 max(0,-j,j-r)
vertical and 2 Dbar horizontal steps, and the edge count is at most rho r, so
    j in [-(rho r - r - 2 Dbar)/2,  r + (rho r - r - 2 Dbar)/2],  <= rho r + 1 sites per level,
    N <= 2(rho r + 1) <= 4 rho r        (draft: 6 rho r).
CORRECTED CONSTANTS: Form A prefactor 12 C1 (b/a_w) r, not 18 C1 (b/a_w) r; one-sided (G-e)
6 C1 (b/a_w) r; Form B threshold sigma^2 >= (2/(c'' c_-)) log(12 C1 (b/a_w) r).

### B6 [DEFECT (justification, and one omission) - not, in the end, an error in the total].
### G-f (i). I first scored this harder than it deserves; here is the audited version.
(a) THE REASON IS WRONG. "The candidate endpoints are confined by (G-b)'s band cap - a
deterministic fact - so each boundary carries at most C n sites AT SLAB SCALE n". The band cap
at slab scale constrains a piece's excursion relative to ITS OWN endpoints; it says nothing
about where those endpoints are. The crossing points lie on the SCALE-R geodesic, R = M n, and
the only deterministic confinement available is the cap THERE: |h| <= (b-a_w) M n/(2 a_w), i.e.
C M n sites per boundary, and M (C M n)^2 (C M n) pairs-times-prefactor = C M^4 n^3.
(b) WHY THE TOTAL SURVIVES ANYWAY. M is a fixed constant of the engine (5 <= M <= 10 in v2's
own range), so C M n is "C' n" and C M^4 n^3 is "C' M n^3" with C' absorbing M^3. The printed
total and the printed quantile cost (log M + 3 log n + O(1))/(c'' c_-) are therefore CORRECT as
stated - but only because a constant silently swallows M^3, which should be said rather than
left to the reader, and the sentence "at slab scale n" should be struck.
(c) THE CLEAN ROUTE, available only after (ii), which was written one iteration later:
intersect with the complement of {global deviation >= theta n/2}. Then every crossing point has
|h| < theta n/2, each boundary carries at most theta n + 1 sites, and the total is
~ C M theta^2 n^3 with no hidden M-powers at all. This is what I would print, since it also
disposes of the arc problem for the surviving pairs in the same stroke.
(d) THE OMISSION, which is not a constant. "Each boundary carries C n sites, hence at most
C^2 n^2 pairs" counts one site from each of the two boundaries. But a geodesic may enter and
leave a slab through the SAME boundary, and that piece is a geodesic between a same-boundary
pair, whose chord is HORIZONTAL - outside any arc around e_2 at any tilt, so the lemma cannot
price it at any threshold, and the containment as written does not cover it. FREE REPAIR: such
a piece needs no probabilistic input at all - the generalised band cap (A1b) confines its
excursion beyond the bounding box of {u,v} to (b-a_w)|u-v|_1/(2 a_w), deterministically.
SECOND OMISSION in the same union: a geodesic may enter and leave a slab through the SAME
boundary, so (u,v) can be a same-boundary pair with a HORIZONTAL chord - outside any arc around
e_2 at any tilt, so the lemma cannot price it at all, at any threshold. Free repair: such a
piece is controlled deterministically by the generalised band cap (A1b) - its excursion beyond
the bounding box of {u,v} is at most (b-a_w)|u-v|_1/(2 a_w) - so no probabilistic input is
needed for it. Neither point is in the text.

### B7 [DEFECT (arithmetic) - two over-claims around the regime-(ii) closure]. G-f (ii).
The inclusion, the range identity and the quantile are all CORRECT, re-derived and checked to
12 digits: |h2-h1| <= |h1|+|h2| gives max >= theta n/2; sigma^2 <= delta^2 sqrt(R) is EXACTLY
D <= delta R for D = sigma R^{3/4}; sigma^2 = (theta^2/4) sqrt(n) M^{-3/2}; and the top-scale
endpoints are on the axis, so the arc hypothesis is satisfied by construction and no union over
slabs is needed. The two things around them that are not correct:
 (a) "true for every theta below the band cap at any M >= 5". The condition is theta <= 2 delta M,
     and it FAILS when delta < theta/(2M) - e.g. delta = 0.01, theta = 0.2, M = 5 needs
     theta/2 = 0.1 <= 0.05, false. The gridded check is delta-blind: it is delta = 1 implicitly.
     In the regime that matters - theta = the o(1) arc half-width - the condition does hold, so
     the claim should read "for theta <= 2 delta M", which the narrow-arc case satisfies by
     definition. As printed it is an over-claim that would break at small delta.
 (b) "that exponent is only LARGE once n >~ M^3/theta^4". Two factors are missing: the union's
     own logarithm, and 1/(c'' c_-)^2. Honest threshold:
        n_0 = (16/(c'' c_-)^2) (M^3/theta^4) log^2(C M n).
     Measured (REFEREE3_check2.py A3): M = 8, theta = 0.05, c'' c_- = 1 gives n_0 ~ 1e12.5
     against the draft's M^3/theta^4 = 8.2e7 - five orders of magnitude; at c'' c_- = 0.01,
     n_0 ~ 1e16.5. The draft's own worked point (M=5, theta=0.05, n=1e4, exponent 0.0056) is
     honest and I reproduce it exactly; the general threshold quoted next to it is not.
 (c) unstated, same family: G-f(i)'s "far inside the range sigma^2 <= delta^2 sqrt(n)" carries
     its own threshold, (log M + 3 log n)/(c'' c_-) <= delta^2 sqrt(n). At c'' c_- = 0.01 and
     delta = 0.1 that is n >= 1e12.

### B8 [DEFECT - the seam's upper-range line is asymptotic, and its threshold can exceed the v2
###  document's own operative scale]. Section 5 consumer contract; v2 [V5-2].
"all consumptions sit at r' >= ~l^cb/K, where sigma^2 = Theta(log l) <= delta^2 sqrt(r') for l
large, ANY fixed delta - no window condition survives" is true asymptotically and misleading as
a ledger entry. Written out: sigma^2 = 2A log l/(c'' c_-) and r' >= l^cb/K, so the condition is
    l^{cb/2} / log l   >=   2 A sqrt(K) / (delta^2 c'' c_-),      cb = base-scale exponent <= 0.12.
Solved (A = 2, K = 10, cb = 0.12):
    c'' c_- = 1.0,  delta = 1.0   ->  l >= 1e54
    c'' c_- = 1.0,  delta = 0.1   ->  l >= 1e91     > the document's own l_0 ~ 1e80
    c'' c_- = 0.1,  delta = 0.1   ->  l >= 1e109
    c'' c_- = 0.01, delta = 0.1   ->  l >= 1e127
    c'' c_- = 0.01, delta = 0.01  ->  l >= 1e162
For U[1,2], c'' c_- = c1 c_-/12, so c'' c_- ~ 0.01 is c1 c_- ~ 0.1 - entirely plausible. The
operative threshold of the package is max(l_0, l_1), and on these numbers l_1 is the binding
one. CORRECTION: [V5-2] should print the inequality above, and v2 section 7.1's threshold
discussion should carry max(1e80, l_1) rather than 1e80. This is the same defect as B2 seen from
the consumer's side, and it is the one I would put first in the reply to the author.

### B9 [notation, v2 section 2]. The symbol c denotes two different constants in adjacent lines:
the tail constant of (H-wand) in sigma := (A log l/c)^{1/theta}, and the base-scale exponent in
r' >= ~l^c/K. I nearly mis-derived B8 on it. Rename one (cb above).

### B10 [ledger] Three riders that belong in the statement and are not in it:
 (i)  a_w > 0 is load-bearing three times (band cap, site count, endpoint confinement). This is
      a UNIFORMLY ELLIPTIC lemma; (P-conc)/(P-Alex) are not. Every constant blows up as
      a_w -> 0, and the U[1,2] instantiation hides it because a_w = 1.
 (ii) the lemma bounds the TRANSVERSAL COORDINATE's excursion, not the distance to the segment.
      Longitudinal overshoot past the endpoints is a different quantity, controlled for free by
      B1's identity: P(overshoot >= m) <= C poly(r) exp(-c1 g(e_2) m/(3 sqrt(C_L' r))) - a
      sqrt(r)-scale Gaussian tail with NO curvature input. Any consumer needing cylinder
      containment (CRUX's "blocks met per slab") needs this second statement, and it is worth
      printing precisely because it is cheaper than the theorem it accompanies.
 (iii) uniqueness of geodesics is used silently in G-f(i) ("the crossing piece IS a geodesic
      between its own endpoints" -> "THE geodesic between u and v deviates"). Under a continuous
      weight law it is a.s. unique and the step is fine; with atoms the union must read "some
      geodesic between u and v deviates". One clause.

-------------------------------------------------------------------------------
## SECTION C. VERDICTS

G-a  (through-vertex, exactness, count)      CONFIRMED. Exactness is right and the count is
     linear; it is loose by 1.5x (B5), and the union's far-j sites need B1's clause.
G-b(i)  (deterministic band cap)             CONFIRMED, exactly as printed. Add A1a/A1b.
G-b(ii) (direction uniformity)               CONDITIONAL. The (P-conc) half is right: Kesten
     concentration is direction-uniform with x-free constants, so steep legs really are free.
     The second half - "the displaced point v is arbitrary at its distance in the condition as
     stated" - is a reading, not an argument, and it is exactly what the far-j sites need. It is
     FREE for axis-aligned spans (B1 fallback (a): it is implied by the midpoint case) and NOT
     free for tilted spans, which v2 consumes. Repair: B1's overshoot clause, or pay c_-/C_L'.
G-c  (the constant chase)                    CONFIRMED with three corrections. c'' =
     c1/(6 sqrt(2 + b/a_w)) is RIGHT, U[1,2] c1/12 is RIGHT, the cancellation is right, the
     three-way split is right, both range checks follow from the single wlog as claimed.
     Corrections: prefactor 18 -> 12 C1 (b/a_w) r (B5); C''' = delta^2 -> delta^2/4 (B4);
     add WLOG c1 <= 3 sqrt(2+b/a_w)/C3 to close the middle band (B3); state r >= r_0 (B2).
G-d  (H-version / circularity)                CONFIRMED dissolved. No consumption site found in
     this round that needs a confined-geodesic wandering tail; the revival clause is not
     triggered. The iter-116 correction to the H-version parenthesis is right.
G-e  (one-sidedness)                          CONFIRMED. Nothing else uses the two-sided form.
     Prefactor 6 C1 (b/a_w) r one-sided under B5.
G-f(i)  (union over boundary pairs)           CONFIRMED in total, DEFECT in justification.
     The containment needs no conditioning and is right, and the printed C' M n^3 and its
     log-quantile cost are correct - but for a reason the text does not give (M is a constant
     that a constant swallows; the band cap is a TOP-scale fact, not a slab-scale one). One real
     omission: same-boundary excursion pieces, whose chords are horizontal and which the lemma
     cannot price - closed for free by the deterministic cap (B6d).
G-f(ii) (steep-crossing closure)              CONFIRMED in shape, DEFECT(arithmetic) in two
     side-claims. Inclusion, range identity and quantile are exact. "every theta below the band
     cap at any M >= 5" should be "theta <= 2 delta M" (B7a); the threshold is
     n_0 = (16/(c'' c_-)^2)(M^3/theta^4) log^2(C M n), not M^3/theta^4 (B7b). The small-n regime
     IS honestly excluded - the draft's own 0.0056 worked point is correct and I reproduce it -
     but the threshold quoted beside it understates n_0 by 4-9 orders of magnitude.
SEAM  ([V5-1] A >= max(2, C3 c''))            CONFIRMED, and made vacuous by B3's wlog.
SEAM  ([V5-2] upper range)                    DEFECT. True asymptotically, with an unstated
     threshold l_1 that exceeds the document's own 1e80 for plausible constants (B8).

### B11 [INTERACTION between two of the repairs, found in the audit pass and worth printing].
B3's normalisation (c1 <= 3 sqrt(2+b/a_w)/C3, needed to close the middle band) forces
c'' <= 1/(2 C3), hence c'' c_- <= c_-/(2 C3). B8's seam threshold scales as 1/(delta^2 c'' c_-).
So closing the middle band RAISES l_1. Worked: C3 = 2, c_- = 0.2 gives c'' c_- <= 0.05 and, at
delta = 1, l_1 ~ 1e78 - just under the 1e80 already on the books; at delta = 0.1, l_1 > 1e109.
The two repairs are both correct and they pull against each other, so they must be priced
together rather than one at a time.

OVERALL. The mathematics of the lemma holds up: every load-bearing step I re-derived
independently came out the way the draft prints it, including the whole of G-c, which is the
part with the most arithmetic and the one I expected to break. What does not hold up is the
range bookkeeping - the draft treats "polylog, well inside the range" as free in four separate
places (B2, B7b, B7c, B8) and in each of them the threshold is a real, computable, and large
number. If the referee's job is to find the thing that would embarrass the paper, it is not a
constant in Form A; it is that the lemma and its consumer are both vacuous below scales that
nobody has written down, and one of those scales sits above the 1e80 the v2 document already
apologises for.
